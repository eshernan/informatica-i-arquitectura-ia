# Sesión 13 — Configuración segura y despliegue reproducible

**Fecha:** 11 de noviembre de 2026, 6:00–10:00 p. m.
**Resultado:** ejecutar la imagen identificada en sesión 12 con configuración externa, sin secretos incorporados y con un procedimiento reproducible de migración y arranque.

## Alcance

Pruebas y CI se trabajaron el 4 de noviembre. Esta sesión utiliza esa entrega y se concentra en configuración, secretos, permisos y reproducción del despliegue. Aunque la imagen sea la misma, cada ambiente debe aportar su configuración sin incorporar credenciales al artefacto ni al repositorio.

Se conserva FastAPI, Caddy, Compose y PostgreSQL. No se incorpora un gestor de secretos externo, TLS público ni otra plataforma. Logs detallados y respaldo/restauración se reservan a sesión 14.

## Secuencia de cuatro horas

| Hora | Tema y acción |
|---|---|
| 6:00–6:20 | identificar el commit y la imagen aprobados en sesión 12 |
| 6:20–7:10 | separar código, configuración no secreta y secretos |
| 7:10–7:50 | demostrar variables externas, permisos y secuencia de migración/arranque |
| 7:50–8:00 | pausa |
| 8:00–9:25 | preparar configuración documentada y reproducir el despliegue |
| 9:25–9:50 | comprobar ausencia de secretos y ejecutar el caso funcional |
| 9:50–10:00 | entregar instrucciones y pendientes para operación |

## Taller

1. Use la imagen y el commit identificados en la sesión anterior.
2. Documente las variables obligatorias, su significado y el comportamiento si faltan.
3. Obtenga la conexión a PostgreSQL mediante configuración externa.
4. Prepare un `.env.example` con valores ficticios, sin credenciales reales.
5. Compruebe que archivos con secretos no se versionan ni se copian a la imagen.
6. Separe los valores públicos de laboratorio de cualquier configuración real.
7. Ejecute el proceso del contenedor como usuario no privilegiado.
8. Ejecute las migraciones una sola vez antes de las réplicas.
9. Pida a otro integrante reproducir el arranque con las instrucciones y la configuración de ejemplo.
10. Cree y consulte una reserva, y registre los permisos o variables que impidieron el arranque si los hubo.

## Validación

```bash
make check
make test-all
git status --short
```

La misma imagen debe poder arrancar con su configuración documentada. No copie secretos reales en logs, capturas, README o historial de comandos. Las pruebas siguen ejecutándose como comprobación del despliegue, sin repetir el taller de CI.

**Evidencia:** commit e imagen utilizados, variables documentadas, configuración de ejemplo, revisión de secretos, usuario de ejecución y procedimiento de migración/arranque reproducido por otra persona.
