# Creación y migración de esquema y datos

## Preparar antes de aplicar

Identifica entorno, motor/versión, herramienta de migraciones, historial aplicado y
definición real. Distingue base nueva, drift, cambio de estructura y cambio de datos.
No reescribe migraciones compartidas ya aplicadas para ocultar drift; genera corrección.
Un archivo existente no prueba que fue aplicado, y que el objeto exista no acredita
definición correcta. No reaplica a ciegas si falta registro de una migración antigua.

Registra precondiciones, objetos/código dependientes, volumen, datos afectados,
compatibilidad de lectores/escritores y autorización. Una petición de crear SQL permite
preparar archivos; aplicar a una cuenta remota requiere alcance de aplicación explícito.
Si el usuario ya lo autorizó y el destino coincide, procede sin pedir permiso repetido.

## Cambios con compatibilidad

Usa expandir → migrar → validar → retirar cuando hay clientes desplegados:

1. Añade estructura compatible y permisos mínimos necesarios.
2. Despliega lectores/escritores que toleren coexistencia según plan.
3. Backfill por lotes acotados con condición idempotente/checkpoint y métricas de avance.
4. Valida invariantes, conteos pertinentes, errores y rutas reales de acceso.
5. Retira forma antigua solo cuando consumidores/retención y autorización lo permitan.

No exige cinco fases para una base local vacía. En documentos versiona forma y valida
coexistencia; cambios de índice/validator/TTL necesitan revisar datos antiguos y acceso.
Los updates masivos tienen plan de concurrencia, retry e integridad. No «arregla» filas
inválidas borrándolas sin conocer regla y autorización.

## Bloqueos, transacciones y recuperación

Comprueba si DDL concreto es transaccional, hace commit implícito o exige estar fuera
de transacción en ese motor. No envuelve todo DDL MySQL como si ROLLBACK pudiera deshacerlo.
En PostgreSQL CREATE INDEX CONCURRENTLY tiene requisitos y estados parciales que deben
revalidarse; no lo mezcla con un runner que abre transacción automática.

Considera tiempo de lock/rewrite, CPU/I/O, replica lag y espacio. Configura límites
proporcionales y ventana cuando importa; un plan en vacío no prueba coste con datos reales.
No pausa producción o mata sesiones por una revisión de consultas sin autorización.

Rollback de código, rollback de esquema y recuperación de datos son diferentes.
Un DOWN que hace DROP no reconstruye los datos eliminados. Declara cambios irreversibles,
backup/PITR o roll-forward y qué restore se probó. Un backup sin restore demostrado es
capacidad supuesta. No crea backup/export con información sensible fuera del destino
autorizado. Verifica RPO/RTO cuando sean parte del objetivo.

Reintentos: tras timeout lee objetos/estado/historial antes de ejecutar de nuevo.
Idempotencia se diseña desde identidad y precondición; `IF NOT EXISTS` no detecta drift.
No promete rollback de pagos, emails u otros efectos externos solo por abrir transacción.

## Verificación y entrega

Prueba migración con datos sintéticos y una copia autorizada si importa el volumen;
comprueba constraints, defaults, índices, grants/policies, app/ORM y consultas afectadas.
Valida escritura inválida, borrado, pertenencia y concurrencia relevante. Revisa errores
parciales, secuencias, objetos dependientes y backfill pendiente.

Tras aplicar, consulta estado persistido y confirma entorno, versión de migración,
invariantes y pruebas de acceso. No atribuye éxito a la respuesta del comando solamente.
Entrega diff, precondiciones, SQL/comandos por motor, ejecución/reversión y pendientes.
Usa [plan de migración](../assets/migration-plan.md) cuando el cambio lo necesite.
