# Plan de migración

- ID / motor / versión / entorno / esquema / herramienta:
- Problema y comportamiento esperado:
- Diff de esquema/seguridad y SQL/comandos nativos:
- Precondiciones verificadas / historial aplicado / drift:
- Datos afectados / tamaño medido o desconocido:
- Lectores/escritores/ORM/jobs dependientes:
- Alcance y autorización de aplicación, si corresponde:

| Fase | Operación | Invariante | Bloqueo/coste | Verificación | Reintento |
|---|---|---|---|---|---|
| Expandir | | | | | |
| Backfill compatible | | | | | |
| Validar | | | | | |
| Retirar (si autorizado) | | | | | |

- Transacción soportada / commits implícitos / límites y ventana:
- Checkpoint, condición idempotente y tratamiento de concurrencia:
- Rollback de código/esquema vs recuperación de datos / pasos irreversibles:
- Backup/PITR y restore efectivamente probado, si relevante:
- Pruebas de acceso e integridad / antes-después:
- Resultado persistido, error parcial y reconciliación:
- Pendientes y criterio de finalización:
