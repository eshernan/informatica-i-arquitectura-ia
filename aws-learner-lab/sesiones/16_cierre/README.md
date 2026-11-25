# Sesión 16 · Ejercicio de integración con todo el grupo

**2 de diciembre de 2026, 18:00–22:00.** Todo el curso opera una sola versión de LibreReserva en un ambiente local. El reto consiste en seguir la reserva de Sala-15 desde su creación hasta la consulta de los datos restaurados. Cada relevo usa la evidencia del anterior y añade su resultado a una bitácora compartida.

## Punto de partida

Traer de la [última clase de contenido](../15_proyecto/SESION_2026-11-25.md) el diagrama, el registro de decisión, las fichas de prueba y el procedimiento de recuperación. Acordar una revisión candidata. El responsable del ambiente prepara las imágenes locales, un volumen de origen para el ejercicio y espacio para otro volumen vacío. Registrar el nombre de ambos antes de empezar. El docente facilita los relevos y plantea las preguntas del incidente.

| Hora | Quién opera | Tarea y relevo |
|---|---|---|
| 18:00–18:20 | Coordinación y verificación | Abrir la bitácora. Acordar una sala libre, el intervalo, las garantías y los criterios de cierre. |
| 18:20–19:00 | Despliegue | Desde un clon limpio, identificar el commit, ejecutar pruebas, construir la imagen, registrar su ID, iniciar PostgreSQL, migrar y levantar las API. Entregar la URL, el esquema preparado y el dibujo de las rutas HTTP y SQL. |
| 19:00–19:40 | Cliente y pruebas | Crear Sala-15, guardar el id, reiniciar las réplicas y consultar de nuevo. Usar otra sala libre para dos peticiones concurrentes incompatibles. Probar el reintento con clave si la versión lo admite. Conservar las filas finales. |
| 19:40–19:50 | Grupo | Pausa. |
| 19:50–20:25 | Operación | Detener PostgreSQL, consultar vida, disponibilidad y reservas. Dibujar el último mensaje que llegó a cada componente. Registrar hora, rutas y respuestas. Recuperar la base y comprobar la reserva original. |
| 20:25–21:20 | Datos y cliente | Pausar escrituras, guardar las filas ordenadas y crear el respaldo. Restaurar en una instancia con volumen vacío separado. Consultar por SQL y desde una API conectada al destino. Comparar identificadores e intervalos. |
| 21:20–21:45 | Verificación y arquitectura | Relacionar cada garantía con una observación. Usar el ADR para explicar dónde se protege el intervalo y qué dependencia falló. |
| 21:45–22:00 | Grupo completo | Cerrar una bitácora común. Asignar responsable a cada brecha. Detener los servicios de práctica después de conservar la evidencia. |

## Reglas de relevo

Quien opera anuncia qué va a cambiar y entrega la hora, el id de la reserva y el resultado. Quien verifica escribe cómo repetir la observación y desde qué destino se obtuvo. Los demás predicen el resultado antes de ejecutar y comparan su predicción con lo observado.

| Garantía | Criterio para el cierre |
|---|---|
| Reproducción | Otro integrante arranca la revisión identificada siguiendo las instrucciones comunes. |
| Persistencia | El id, la sala y el intervalo coinciden después del reinicio de las API. |
| Integridad | Dos peticiones simultáneas para el mismo intervalo libre dejan una sola reserva. |
| Reintento | Se recupera el resultado original con la misma clave y un solo efecto. Si falta la capacidad, registrar la prueba pendiente. |
| Diagnóstico | La bitácora relaciona la falla de una ruta de negocio con una hipótesis comprobada. |
| Restauración | El volumen de destino empezó vacío. Las filas ordenadas y la consulta a la API del destino coinciden con el estado guardado. |

**Formato de la bitácora:** hora · rol · revisión/destino · acción · resultado esperado · resultado observado · evidencia · siguiente responsable. Conservar el origen durante toda la restauración. Si un paso falla, documentar el síntoma y trabajar con la última etapa válida. Cerrar con lo observado y con las pruebas que quedan abiertas.
