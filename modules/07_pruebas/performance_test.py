"""Crea 100 reservas y consulta la API en tandas concurrentes exactas.

Ejecutar directamente con Python. Consulte PRUEBA_RENDIMIENTO.md.
"""

import argparse
import asyncio
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
import logging
import math
from pathlib import Path
import platform
import sys
from time import perf_counter
from uuid import uuid4

import aiohttp


def positivo(valor):
    numero = float(valor)
    if not math.isfinite(numero) or numero <= 0:
        raise argparse.ArgumentTypeError("El valor debe ser positivo y finito")
    return numero


def entero_positivo(valor):
    numero = int(valor)
    if numero <= 0:
        raise argparse.ArgumentTypeError("El valor debe ser un entero positivo")
    return numero


def registrar(evento, **datos):
    logging.info(json.dumps({
        "fecha_utc": datetime.now(timezone.utc).isoformat(),
        "evento": evento, **datos,
    }, ensure_ascii=False))


class Evidencia:
    """Guarda cada cuerpo distinto una vez y lo referencia desde el log."""

    def __init__(self, salida):
        self.salida = salida
        self.pendientes = {}
        self.guardados = set()
        (salida / "respuestas").mkdir()

    def referenciar(self, cuerpo):
        nombre = f"respuestas/{hashlib.sha256(cuerpo).hexdigest()}.txt"
        if nombre not in self.guardados:
            self.pendientes[nombre] = cuerpo
        return nombre

    def guardar(self):
        # Se escribe fuera de la tanda para no frenar el tráfico con E/S de disco.
        for nombre, cuerpo in self.pendientes.items():
            (self.salida / nombre).write_bytes(cuerpo)
            self.guardados.add(nombre)
        self.pendientes.clear()


async def solicitud(cliente, metodo, url, identificador, evidencia, *,
                    datos=None, ids_esperados=None, puerta=None, reloj_tanda=None):
    if puerta is not None:
        await puerta.wait()
    inicio = perf_counter()
    registro = {
        "id": identificador, "metodo": metodo, "ruta": "/reservas",
        "inicio_relativo_ms": (round((inicio - reloj_tanda[0]) * 1000, 3)
                               if reloj_tanda else 0),
        "estado_http": None, "bytes_respuesta": 0,
        "respuesta_archivo": None, "error": None, "correcta": False,
    }
    cuerpo = b""
    try:
        async with cliente.request(metodo, url, json=datos, allow_redirects=False) as respuesta:
            registro["estado_http"] = respuesta.status
            cuerpo = await respuesta.read()
            registro["tiempo_ms"] = round((perf_counter() - inicio) * 1000, 3)
            registro["bytes_respuesta"] = len(cuerpo)
            registro["respuesta_archivo"] = evidencia.referenciar(cuerpo)
            esperado = 201 if metodo == "POST" else 200
            if respuesta.status != esperado:
                registro["error"] = f"Se esperaba HTTP {esperado}"
            else:
                contenido = json.loads(cuerpo)
                if metodo == "POST":
                    registro["correcta"] = (isinstance(contenido, dict)
                                              and isinstance(contenido.get("id"), int)
                                              and contenido.get("recurso") == datos["recurso"])
                elif ids_esperados is None:
                    registro["correcta"] = isinstance(contenido, list)
                else:
                    registro["correcta"] = (
                        isinstance(contenido, list) and len(contenido) == 100
                        and all(isinstance(item, dict) for item in contenido)
                        and {item.get("id") for item in contenido} == ids_esperados
                    )
                if not registro["correcta"]:
                    registro["error"] = "El contenido no coincide con los datos preparados"
    except (aiohttp.ClientError, TimeoutError, ValueError) as exc:
        registro["error"] = f"{type(exc).__name__}: {exc}"
    registro.setdefault("tiempo_ms", round((perf_counter() - inicio) * 1000, 3))
    return registro, cuerpo


def percentil(valores, proporcion):
    ordenados = sorted(valores)
    return ordenados[max(0, math.ceil(len(ordenados) * proporcion) - 1)]


async def ejecutar(opciones, evidencia):
    url = opciones.host.rstrip("/") + "/reservas"
    timeout = aiohttp.ClientTimeout(total=opciones.timeout)
    identificador = uuid4().hex[:10]
    ids = set()
    async with aiohttp.ClientSession(timeout=timeout) as cliente:
        registro, cuerpo = await solicitud(cliente, "GET", url, "verificacion-inicial", evidencia)
        registrar("VERIFICACION_INICIAL", **registro)
        evidencia.guardar()
        if not registro["correcta"] or json.loads(cuerpo) != []:
            raise RuntimeError("La API debe estar disponible y sin reservas. Use una instancia de laboratorio nueva.")
        for numero in range(1, 101):
            datos = {
                "recurso": f"performance-{identificador}-{numero:03d}",
                "inicio": "2026-11-04T08:00:00Z",
                "fin": "2026-11-04T09:00:00Z",
            }
            registro, cuerpo = await solicitud(cliente, "POST", url, f"reserva-{numero:03d}",
                                               evidencia, datos=datos)
            registrar("CREACION_RESERVA", **registro)
            evidencia.guardar()
            if not registro["correcta"]:
                raise RuntimeError(f"Falló la creación de la reserva {numero}; no se inicia la carga.")
            ids.add(json.loads(cuerpo)["id"])
    if len(ids) != 100:
        raise RuntimeError("La API no devolvió 100 identificadores distintos.")
    registrar("DATOS_PREPARADOS", reservas_creadas=len(ids))
    print("100 reservas creadas. Iniciando tandas de consulta...", flush=True)

    resumenes = []
    for indice, cantidad in enumerate(opciones.concurrencias, start=1):
        registrar("INICIO_TANDA", tanda=indice, concurrencia_objetivo=cantidad)
        # El pool admite toda la tanda; no reduce silenciosamente la concurrencia.
        conector = aiohttp.TCPConnector(limit=cantidad, limit_per_host=cantidad)
        async with aiohttp.ClientSession(timeout=timeout, connector=conector) as cliente:
            puerta = asyncio.Event()
            reloj = [0.0]
            tareas = [asyncio.create_task(solicitud(
                cliente, "GET", url, f"tanda-{indice}-solicitud-{numero:05d}", evidencia,
                ids_esperados=ids, puerta=puerta, reloj_tanda=reloj,
            )) for numero in range(1, cantidad + 1)]
            await asyncio.sleep(0)  # Todas las tareas llegan a la misma puerta.
            reloj[0] = perf_counter()
            puerta.set()
            respuestas = await asyncio.gather(*tareas)
            duracion = perf_counter() - reloj[0]
        evidencia.guardar()
        registros = [registro for registro, _ in respuestas]
        for registro in registros:
            registrar("SOLICITUD", tanda=indice, concurrencia_objetivo=cantidad, **registro)
        tiempos = [r["tiempo_ms"] for r in registros]
        correctas = sum(r["correcta"] for r in registros)
        p95 = percentil(tiempos, 0.95)
        resumen = {
            "tanda": indice, "concurrencia_objetivo": cantidad,
            "solicitudes": len(registros), "correctas": correctas,
            "fallidas": len(registros) - correctas,
            "estados_http": dict(Counter(str(r["estado_http"]) for r in registros)),
            "duracion_s": round(duracion, 3),
            "solicitudes_por_segundo": round(len(registros) / duracion, 2),
            "min_ms": min(tiempos), "promedio_ms": round(sum(tiempos) / len(tiempos), 3),
            "p50_ms": percentil(tiempos, 0.5), "p95_ms": p95,
            "p99_ms": percentil(tiempos, 0.99), "max_ms": max(tiempos),
            "ultimo_inicio_ms": max(r["inicio_relativo_ms"] for r in registros),
            "umbral_p95_ms": opciones.p95_ms,
            "resultado": "CUMPLE" if correctas == cantidad and p95 < opciones.p95_ms else "NO_CUMPLE",
        }
        registrar("RESUMEN_TANDA", **resumen)
        resumenes.append(resumen)
        with (evidencia.salida / "resumen.csv").open("w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=list(resumen))
            escritor.writeheader()
            escritor.writerows({**r, "estados_http": json.dumps(r["estados_http"])} for r in resumenes)
        print(f"Tanda {cantidad}: {correctas}/{cantidad} correctas; p95={p95:.1f} ms; {resumen['resultado']}", flush=True)
        if indice < len(opciones.concurrencias):
            await asyncio.sleep(opciones.pausa)
    cumple = all(r["resultado"] == "CUMPLE" for r in resumenes)
    registrar("RESULTADO_PRUEBA", reservas_creadas=100,
              solicitudes_consulta=sum(r["solicitudes"] for r in resumenes),
              resultado="CUMPLE" if cumple else "NO_CUMPLE")
    return 0 if cumple else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="http://127.0.0.1:8000")
    parser.add_argument("--concurrencias", nargs="+", type=entero_positivo, default=[1000, 2000, 5000, 6000])
    parser.add_argument("--timeout", type=positivo, default=60, help="Segundos máximos por solicitud")
    parser.add_argument("--p95-ms", type=positivo, default=500, help="Umbral didáctico")
    parser.add_argument("--pausa", type=positivo, default=2, help="Segundos entre tandas")
    parser.add_argument("--salida", type=Path, help="Carpeta nueva para esta ejecución")
    opciones = parser.parse_args()
    raiz = Path(__file__).resolve().parents[2]
    salida = opciones.salida or raiz / "dist/rendimiento" / (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid4().hex[:8])
    salida.mkdir(parents=True, exist_ok=False)
    logging.basicConfig(filename=salida / "performance_test.log", level=logging.INFO,
                        encoding="utf-8", format="%(message)s")
    evidencia = Evidencia(salida)
    registrar("CONFIGURACION", host=opciones.host, reservas=100,
              concurrencias=opciones.concurrencias, timeout_s=opciones.timeout,
              umbral_p95_ms=opciones.p95_ms, pausa_s=opciones.pausa,
              python=platform.python_version(), sistema=platform.platform(), aiohttp=aiohttp.__version__)
    print(f"Log: {(salida / 'performance_test.log').resolve()}", flush=True)
    try:
        return asyncio.run(ejecutar(opciones, evidencia))
    except (Exception, KeyboardInterrupt) as exc:
        evidencia.guardar()
        registrar("PRUEBA_INTERRUMPIDA", error=f"{type(exc).__name__}: {exc}")
        print(f"Prueba interrumpida: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
