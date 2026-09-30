# Revisión de estructura, integridad y rendimiento

## Inspección con límites

Empieza por esquema, migraciones/código consumidor y metadatos. Inspecciona tablas,
columnas, PK/UNIQUE/FK/CHECK, índices, views, triggers/funciones relevantes, roles y
políticas. Declara objetos no visibles por permisos, salida truncada y datos no medidos.
No exporta tablas ni funciones completas indiscriminadamente.

Separa revisión estática de comprobación de datos: constraints declarados pueden no
estar validados en todo el histórico; un campo no nulo en un sample no implica NOT NULL.
Orphans/duplicados, valores inválidos, asociaciones entre tenants y divergencias requieren
consultas acotadas y autorizadas. No cambia valores solo porque parezcan erróneos.

El [inventario PostgreSQL](../assets/postgres-metadata-audit.sql) usa solo catálogos y
esquema `public` como ejemplo. Cambia filtro al alcance real; los límites son de salida,
no prueba de exhaustividad. No asume equivalente en MySQL/SQLite/NoSQL.

## Hallazgos útiles

Para cada hallazgo: objeto y evidencia, regla afectada, impacto, prioridad, recomendación,
prueba y limitación. Ejemplos: FK sin tenant en shared schema, dato sensible expuesto
por grant de tabla, money float, índice redundante, arrays no acotados o backfill sin
validar. Similaridad de nombres no es evidencia de redundancia.

Usa [plantilla de revisión](../assets/schema-review.md). No aplica una puntuación ficticia
de «seguridad 100%». Auditar todos los motores no es requisito para revisar una tabla.

## Rendimiento con evidencia

Identifica consulta/operación, parámetros representativos, frecuencia, tamaño/cardinalidad,
selectividad, p50/p95 cuando disponibles, CPU/I/O, bloqueos y volumen devuelto. Distingue
plan estimado y ejecución observada. No recomienda sharding por un SELECT sin LIMIT.

En SQL comienza por EXPLAIN sin ejecutar cuando la pregunta puede resolverse así.
EXPLAIN ANALYZE ejecuta la operación: comprobar side effects, coste y autorización.
Incluso SELECT puede invocar funciones con efectos. Rollback no deshace todo efecto
externo. Usa entorno adecuado y límites; nunca prueba DML en producción solo para medir.

Prioriza filtros/selectividad, JOIN correcto, proyección necesaria, paginación estable,
índice compuesto justificado, evitar N+1 y estadísticas vigentes. Offset/keyset dependen
de UX y acceso; keyset necesita orden único/estable. No «optimiza» ocultando denegación
o devolviendo menos negocio del requerido.

Locks/long transactions, pool saturado, serialización/red y llamadas repetidas pueden
ser la causa. Revisa conexión directa/pool/serverless del proveedor real; no impone un
pool grande sin límite de conexiones. Partición requiere patrón de pruning/retención;
no mejora toda consulta. No hace VACUUM/ANALYZE/reindex o borra índices fuera de alcance.

NoSQL: explain/estadísticas compatibles, documentos leídos/devueltos, hot partitions,
fan-out, índices y coste. Distingue Query vs Scan y TTL vs acceso; evita scans globales
por comodidad. Verifica consistencia de resultados, no solo rapidez.

## Antes/después

Define hipótesis, cambio limitado y criterio medible. Compara misma operación, datos y
contexto razonables; registra caché/estadísticas/variación. Un índice puede acelerar
lectura y empeorar escritura: informa ambos cuando importen. No afirma porcentaje de
mejora sin baseline y medición. Si no hay motor/telemetría, entrega hipótesis y plan de
prueba, y marca recomendaciones como no verificadas en ejecución.
