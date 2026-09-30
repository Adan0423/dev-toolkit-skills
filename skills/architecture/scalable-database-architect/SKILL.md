---
name: scalable-database-architect
description: >
  Skill profesional para diseñar, auditar, refactorizar, optimizar y asegurar bases
  de datos escalables. Decide entre modelos relacionales y NoSQL según el proyecto,
  elimina tablas/columnas innecesarias, diseña relaciones, constraints, índices,
  particiones, funciones, RLS/RBAC, límites, paginación, pooling y observabilidad.
  Nunca optimiza a ciegas: primero comprende workload y patrones de acceso, después
  mide, modifica y verifica.
version: 1.0.0
language: es
tags:
  - database-architecture
  - postgresql
  - sql
  - nosql
  - mongodb
  - dynamodb
  - scalability
  - performance
  - security
  - rbac
  - rls
  - query-optimization
---

# Scalable Database Architect

## Misión

Actúa como **Database Architect + Database Performance Engineer + Database Security Engineer**.

Debes ser capaz de:

1. comprender el producto y sus patrones reales de acceso;
2. elegir el modelo de datos correcto;
3. diseñar esquemas escalables;
4. eliminar tablas, columnas, índices y relaciones innecesarias;
5. preservar integridad y claridad;
6. optimizar lecturas/escrituras con evidencia;
7. encapsular operaciones complejas en funciones cuando sea apropiado;
8. imponer límites para evitar consultas y conexiones abusivas;
9. mejorar autorización y seguridad de acceso a datos;
10. preparar migraciones reproducibles;
11. medir nuevamente después de cada optimización.

No debes transformar una base de datos sencilla en una arquitectura compleja sin necesidad.

---

# 1. Principios no negociables

## 1.1 Workload first

Nunca diseñes una base de datos sin conocer primero:

- entidades;
- volumen actual;
- crecimiento esperado;
- número de usuarios;
- concurrencia;
- lecturas/escrituras;
- patrones de consulta;
- latencia objetivo;
- consistencia requerida;
- tamaño de objetos;
- retención;
- búsquedas;
- reporting/analytics;
- multi-tenancy;
- disponibilidad;
- recuperación;
- restricciones regulatorias si existen.

El esquema debe optimizar el **workload real**, no un ejemplo académico.

## 1.2 Simplicidad primero

Prefiere:

- menos entidades;
- relaciones claras;
- columnas con propósito;
- constraints explícitos;
- índices justificados;
- una fuente de verdad;
- migraciones entendibles.

Evita:

- tablas “por si acaso”;
- columnas duplicadas sin necesidad;
- columnas calculables almacenadas sin motivo;
- tablas genéricas tipo EAV para todo;
- JSON usado para evitar modelar relaciones importantes;
- índices sobre todas las columnas;
- triggers innecesarios;
- funciones para operaciones triviales;
- particiones prematuras;
- sharding prematuro.

## 1.3 Medir antes y después

Toda optimización debe responder:

- ¿qué consulta es lenta?;
- ¿qué frecuencia tiene?;
- ¿qué recursos consume?;
- ¿qué plan de ejecución usa?;
- ¿qué cambia con la optimización?;
- ¿cuánto mejora?;
- ¿qué coste añade a escrituras/almacenamiento/complejidad?

Nunca declares una optimización exitosa sin evidencia.

---

# 2. Fase DISCOVER — Comprender el sistema

Antes de diseñar o modificar, inspecciona:

## Proyecto

- lenguajes;
- frameworks;
- ORM/query builder;
- drivers;
- servicios;
- API;
- workers;
- jobs;
- cache;
- colas;
- analytics;
- búsqueda;
- archivos.

## Base de datos actual

- motor y versión;
- schemas;
- tablas/colecciones;
- columnas/campos;
- tipos;
- PK;
- FK;
- constraints;
- índices;
- vistas;
- funciones;
- triggers;
- policies;
- roles;
- grants;
- particiones;
- extensiones;
- migraciones;
- seeds;
- volumen por tabla;
- cardinalidad;
- crecimiento;
- datos huérfanos;
- duplicados.

## Workload

Construye un catálogo:

| Query/operación | Frecuencia | Filtra por | Ordena por | Join | Filas devueltas | Escritura | Latencia objetivo |
|---|---:|---|---|---|---:|---|---|

Clasifica:

- hot path;
- normal path;
- background;
- reporting;
- admin;
- maintenance.

---

# 3. Elegir tipo de base de datos

No elijas tecnología por tendencia.

## 3.1 Relacional / SQL

Preferir cuando existen:

- relaciones claras;
- transacciones;
- integridad referencial;
- joins;
- reporting;
- datos estructurados;
- reglas de negocio fuertes;
- consistencia fuerte.

Ejemplos típicos:

- usuarios;
- pagos;
- órdenes;
- inventario;
- permisos;
- facturación;
- ERP;
- CRM;
- sistemas administrativos.

PostgreSQL es una opción generalista cuando el proyecto requiere estas propiedades.

## 3.2 Documental

Considerar cuando:

- entidades agregadas se leen juntas;
- estructura cambia entre documentos;
- atributos son variables;
- no se requieren joins relacionales frecuentes;
- la denormalización mejora claramente el acceso.

Ejemplo:

- catálogo heterogéneo;
- contenido flexible;
- documentos con subestructuras.

En MongoDB, prioriza el principio:

`data accessed together → stored together`

Decide conscientemente entre:

- embedding;
- references.

## 3.3 Key-value / wide-column

Considerar cuando:

- el acceso está determinado por claves;
- existen patrones de acceso muy predecibles;
- se necesita gran escala horizontal;
- no se necesitan consultas relacionales arbitrarias.

Para DynamoDB:

- diseñar primero access patterns;
- elegir partition key con buena distribución;
- usar sort key para agrupación/rangos;
- diseñar índices secundarios solo para accesos reales;
- evitar Scan como patrón principal.

## 3.4 Graph

Considerar cuando el valor principal está en recorrer relaciones:

- redes;
- dependencias;
- rutas;
- fraude;
- conocimiento;
- recomendaciones basadas en conexiones.

No usar graph si consultas relacionales simples resuelven el problema mejor.

## 3.5 Time-series

Considerar si predominan:

- eventos temporales;
- métricas;
- telemetría;
- series de tiempo;
- retención/rollups.

## 3.6 Vector

Usar almacenamiento/vector search cuando exista búsqueda semántica real.

No reemplazar el modelo transaccional completo por un vector store.

## 3.7 Arquitectura políglota

Usar más de un motor solo si existe una necesidad demostrable.

Ejemplo:

- PostgreSQL → sistema transaccional;
- Redis → cache;
- motor de búsqueda → full-text especializado;
- object storage → archivos;
- vector store/extensión → embeddings.

Cada motor extra aumenta:

- operaciones;
- observabilidad;
- fallos posibles;
- sincronización;
- costes.

---

# 4. Diseño relacional

## 4.1 Entidades

Cada tabla debe representar un concepto estable.

Pregunta para cada tabla:

- ¿qué entidad representa?;
- ¿qué lifecycle tiene?;
- ¿quién la posee?;
- ¿por qué no puede formar parte de otra tabla?;
- ¿qué operaciones se realizan sobre ella?

Si no existe una respuesta clara, cuestiona la tabla.

## 4.2 Columnas

Cada columna debe tener:

- significado claro;
- tipo correcto;
- nulabilidad deliberada;
- unidad/formato definido;
- ownership conceptual.

Evita:

- `field1`, `field2`;
- columnas duplicadas;
- múltiples representaciones del mismo dato;
- flags que representan estados incompatibles;
- guardar texto cuando existe un tipo adecuado;
- timestamps sin semántica;
- JSON para atributos relacionales críticos.

## 4.3 Normalización

Usa normalización como punto de partida para:

- reducir inconsistencias;
- eliminar duplicación accidental;
- representar relaciones.

No persigas normalización extrema si empeora un workload medido.

La denormalización debe ser:

- deliberada;
- documentada;
- sincronizable;
- validada por rendimiento.

## 4.4 Relaciones

### One-to-one

Usar solo cuando exista una razón clara:

- ciclo de vida distinto;
- datos opcionales muy grandes;
- separación de seguridad;
- separación de dominio.

No crear tablas 1:1 sin beneficio.

### One-to-many

Usar FK desde el lado many.

Ejemplo conceptual:

`users 1 → N orders`

### Many-to-many

Usar tabla puente cuando la relación tenga cardinalidad N:M.

Ejemplo:

`users ← user_roles → roles`

La tabla puente puede contener atributos propios si pertenecen a la relación.

## 4.5 Constraints

Usa la base de datos para proteger invariantes.

Considera:

- PRIMARY KEY;
- FOREIGN KEY;
- UNIQUE;
- NOT NULL;
- CHECK;
- EXCLUDE cuando corresponda.

No delegar toda integridad únicamente a la UI o API.

---

# 5. Diseño documental / MongoDB

## 5.1 Embedding

Favorecer cuando:

- child se lee casi siempre con parent;
- el child pertenece a un único parent;
- tamaño está acotado;
- atomicidad dentro del documento es útil.

Beneficio:

- menos operaciones;
- menos joins/lookups;
- recuperación conjunta.

## 5.2 References

Favorecer cuando:

- la entidad se comparte;
- crece sin límites razonables;
- tiene lifecycle independiente;
- se consulta individualmente;
- existe many-to-many complejo.

## 5.3 Evitar documentos gigantes

Analiza:

- arrays sin límite;
- crecimiento indefinido;
- hot documents;
- frecuencia de actualización;
- tamaño máximo permitido por motor.

## 5.4 Validación

La flexibilidad de esquema no significa ausencia de contrato.

Usa schema validation para campos críticos.

---

# 6. Diseño key-value / DynamoDB

Diseña desde access patterns.

## Partition key

Debe:

- distribuir carga;
- evitar hot partitions;
- permitir localizar datos.

## Sort key

Úsala para:

- jerarquías;
- rangos;
- orden temporal;
- agrupación.

## Query sobre Scan

Favorece `Query`.

Un `Scan` lee datos antes de filtrar y puede consumir capacidad innecesariamente.

Si se necesita recorrer datasets grandes:

- paginar;
- limitar;
- mover a procesos batch;
- considerar export/analytics.

## Secondary indexes

Crear solo cuando existe un access pattern adicional frecuente.

Cada índice tiene coste de:

- almacenamiento;
- escritura;
- capacidad;
- mantenimiento.

---

# 7. Estrategia de índices

Un índice debe existir por una razón medible.

Analiza columnas utilizadas en:

- WHERE;
- JOIN;
- ORDER BY;
- GROUP BY;
- claves de búsqueda;
- policies RLS.

## 7.1 B-tree

Default para:

- igualdad;
- rangos;
- orden.

## 7.2 Composite indexes

Ordenar columnas según el patrón real de filtros/orden.

No asumir que:

`INDEX(a,b,c)`

equivale a cualquier combinación arbitraria.

## 7.3 Partial indexes

Usar cuando un subconjunto pequeño y frecuente merece indexación.

Ejemplo conceptual:

- registros activos;
- pedidos pendientes;
- filas no procesadas.

## 7.4 Covering/index-only

Considerar cuando una consulta hot puede resolverse desde el índice.

No inflar índices con columnas grandes sin medir.

## 7.5 Índices redundantes

Buscar:

- duplicados;
- prefijos redundantes;
- índices nunca usados;
- índices de baja selectividad;
- índices que penalizan writes sin beneficio.

No borrar automáticamente un índice por bajo uso sin revisar:

- jobs mensuales;
- cierres;
- informes;
- operaciones de emergencia.

---

# 8. Optimización de consultas

## Regla principal

No optimizar mirando únicamente SQL.

Examinar:

- plan;
- cardinalidad;
- filtros;
- joins;
- I/O;
- buffers;
- sort;
- locks;
- filas estimadas vs reales.

## PostgreSQL

Usar cuando corresponda:

- `EXPLAIN`;
- `EXPLAIN ANALYZE` en entorno seguro;
- `BUFFERS`;
- estadísticas;
- `pg_stat_statements`;
- estadísticas de tablas/índices.

Cuidado:
`EXPLAIN ANALYZE` ejecuta la consulta.

Para DML, usar entorno seguro o transacción reversible cuando corresponda.

## Query hygiene

Evita por defecto:

- `SELECT *` en endpoints;
- N+1;
- loops haciendo una query por fila;
- joins innecesarios;
- funciones no indexables en filtros hot;
- offsets enormes;
- subqueries repetidas;
- cargas completas para mostrar una página.

Selecciona solo columnas necesarias.

---

# 9. Paginación y límites

Toda colección potencialmente grande debe tener límites.

## Offset pagination

Aceptable para:

- datasets pequeños/medianos;
- navegación simple;
- páginas bajas.

Problemas:

- offsets altos;
- cambios concurrentes;
- coste creciente.

## Keyset/cursor pagination

Preferir para:

- feeds;
- tablas grandes;
- APIs de alto tráfico;
- scroll infinito;
- orden estable.

Debe usar un orden determinista.

Ejemplo:

`created_at DESC, id DESC`

## Límites

Configura según contexto:

- `LIMIT` máximo por endpoint;
- tamaño máximo de page;
- batch size;
- tamaño máximo de payload;
- máximo de IDs en operaciones masivas;
- tiempo máximo de consulta.

Nunca permitir que el cliente elija un límite sin techo.

---

# 10. Query budgets

Cada ruta crítica debe tener un presupuesto.

Ejemplo de conceptos:

- máximo filas;
- máximo tiempo;
- máximo número de queries;
- máximo conexiones;
- máximo batch;
- máximo payload.

No fijar números universales.
Derivar límites del workload y SLO.

---

# 11. Timeouts

En PostgreSQL evaluar:

- `statement_timeout`;
- `lock_timeout`;
- `idle_in_transaction_session_timeout`;
- `transaction_timeout` si aplica.

No establecer timeouts globales arbitrarios que rompan tareas legítimas.

Diferenciar:

- requests interactivos;
- jobs;
- migraciones;
- reporting.

---

# 12. Connection pooling

No abrir una conexión nueva por cada operación sin gestión.

Analiza:

- max connections;
- pool size;
- concurrency;
- workers;
- serverless;
- conexión directa vs pool.

Un pool demasiado grande también puede empeorar el sistema.

Mide:

- conexiones activas;
- waiting;
- saturation;
- transaction duration.

En entornos serverless, preferir drivers/poolers adecuados.

---

# 13. Funciones SQL / stored procedures

Crear función cuando aporta:

- atomicidad;
- reducción de round trips;
- lógica de datos consistente;
- operación multi-step;
- encapsulación de reglas cercanas a los datos.

No crear funciones para:

- simples SELECT triviales;
- esconder queries malas;
- evitar modelar correctamente.

## SECURITY INVOKER

Preferir por defecto.

La función opera con permisos del llamador.

## SECURITY DEFINER

Usar solo si existe necesidad de elevar privilegios controladamente.

Si se usa en PostgreSQL:

- `search_path` seguro;
- objetos schema-qualified;
- propietario mínimo;
- `EXECUTE` restringido;
- inputs validados;
- dynamic SQL parametrizado;
- pruebas de abuso;
- revisar interacción con RLS.

No usar `SECURITY DEFINER` como bypass rápido de permisos.

---

# 14. Transacciones

Usa transacciones cuando varias operaciones forman una unidad lógica.

Verifica:

- atomicidad;
- aislamiento;
- locks;
- duración;
- retry de conflictos;
- idempotencia.

Evita transacciones largas mientras esperas:

- red;
- usuario;
- API externa;
- trabajo pesado.

---

# 15. Concurrencia

Detecta:

- lost updates;
- race conditions;
- double processing;
- duplicate inserts;
- stock negativo;
- asignaciones dobles.

Usa según el caso:

- constraints;
- atomic UPDATE;
- optimistic concurrency;
- `SELECT ... FOR UPDATE`;
- advisory locks;
- idempotency keys;
- unique keys.

No uses locks globales por defecto.

---

# 16. Partitioning

No particionar por moda.

Considerar cuando:

- tabla es realmente grande;
- mantenimiento se beneficia;
- queries filtran consistentemente por partition key;
- retención requiere eliminar rangos;
- datos hot/cold están claramente separados.

Validar con planes reales.

Un particionado incorrecto puede aumentar complejidad y planificación.

---

# 17. Sharding

Sharding es una decisión tardía.

Antes evaluar:

- mejores índices;
- queries;
- hardware/compute;
- pooling;
- caching;
- particionado;
- réplicas;
- archiving.

Solo diseñar sharding cuando:

- una instancia/cluster razonable ya no satisface;
- existe shard key estable;
- cross-shard operations son controlables.

---

# 18. Caching

Cachear solo cuando exista:

- lectura frecuente;
- tolerancia a datos temporalmente stale;
- coste significativo de regeneración.

Definir:

- key;
- TTL;
- invalidación;
- owner;
- consistency model.

Nunca usar cache como fuente de verdad transaccional sin diseño explícito.

---

# 19. Retención y ciclo de vida

Para datos crecientes define:

- cuánto conservar;
- qué archivar;
- qué agregar/rollup;
- qué borrar;
- qué conservar por auditoría.

Evita guardar indefinidamente:

- logs detallados;
- eventos;
- sesiones expiradas;
- temporales;
- tokens;
- jobs completados;
- cachés persistentes.

Aplicar TTL cuando el motor lo soporte y sea apropiado.

---

# 20. Seguridad de consultas

## 20.1 Parametrización obligatoria

Nunca construir SQL concatenando input del usuario.

Usar:

- prepared statements;
- bind parameters;
- ORM/query builder parametrizado.

La parametrización separa datos de estructura SQL.

## 20.2 Dynamic SQL

Si es inevitable:

- parámetros para valores;
- allowlist para nombres de columnas/tablas;
- nunca interpolar identificadores arbitrarios del cliente.

## 20.3 Least privilege

La aplicación no debe conectarse como:

- superuser;
- owner global;
- administrador sin necesidad.

Separar roles cuando sea útil:

- migration/admin;
- runtime API;
- read-only reporting;
- background worker.

## 20.4 RLS

Considerar Row Level Security para:

- multi-tenant;
- acceso por propietario;
- acceso directo desde cliente;
- defensa en profundidad.

Cuando RLS esté habilitado en PostgreSQL, una tabla sin policy aplicable usa comportamiento default-deny.

No usar RLS como sustituto de buenos filtros de rendimiento.

## 20.5 Column-level exposure

No retornar columnas sensibles por comodidad.

Crear:

- SELECT explícito;
- vistas seguras;
- DTO;
- funciones controladas.

## 20.6 Funciones expuestas

Revisar:

- EXECUTE;
- SECURITY DEFINER;
- search_path;
- input;
- output;
- RLS;
- owner.

## 20.7 NoSQL injection

NoSQL no elimina el riesgo de injection.

Nunca permitir que input arbitrario controle operadores/objetos de consulta sin validación.

---

# 21. Multi-tenancy

Elegir conscientemente:

## Shared tables + tenant_id

Ventajas:
- simple operación;
- eficiente.

Requiere:
- filtros correctos;
- índices por tenant;
- RLS/authorization.

## Schema per tenant

Útil en ciertos aislamientos, pero aumenta complejidad operativa.

## Database per tenant

Máximo aislamiento, mayor coste y administración.

No elegir database-per-tenant sin necesidad real.

---

# 22. Migraciones

Toda modificación debe ser reproducible.

Proceso:

1. inspeccionar estado;
2. crear migration;
3. pre-check;
4. aplicar en staging;
5. verificar;
6. medir locks/duración;
7. rollback o forward-fix;
8. producción;
9. post-check.

Para tablas grandes evaluar:

- backfill por lotes;
- índices concurrentes cuando el motor lo permita;
- cambios compatibles;
- expansión/contracción.

No ejecutar ALTER destructivos improvisados en producción.

---

# 23. Observabilidad

Medir:

- p50/p95/p99 de queries críticas;
- queries por request;
- throughput;
- CPU;
- I/O;
- buffer/cache hit;
- locks;
- deadlocks;
- temp files;
- pool saturation;
- replication lag;
- storage growth;
- index usage;
- table scans;
- error rate.

Para PostgreSQL considerar `pg_stat_statements`.

No almacenar datos sensibles completos en logs de queries.

---

# 24. Auditoría de objetos innecesarios

Para cada objeto, clasificar:

## KEEP

Necesario y usado.

## OPTIMIZE

Necesario pero ineficiente.

## MERGE

Duplicado o fragmentación innecesaria.

## DEPRECATE

Ya no debe usarse pero requiere transición.

## DROP CANDIDATE

Potencialmente eliminable.

Antes de DROP:

- buscar referencias;
- ORM/models;
- código;
- funciones;
- vistas;
- triggers;
- jobs;
- reportes;
- BI;
- backups;
- integraciones.

Nunca eliminar automáticamente por intuición.

---

# 25. Detección de columnas innecesarias

Buscar:

- siempre NULL;
- siempre mismo valor;
- duplicación;
- campo derivable;
- legacy;
- no referenciado;
- JSON duplicando columnas;
- flags contradictorios.

Antes de eliminar:

- validar uso histórico;
- contratos API;
- reportes;
- exportaciones;
- migraciones.

---

# 26. Detección de tablas innecesarias

Buscar:

- tabla 1:1 sin propósito;
- catálogo estático que podría ser constraint/enum cuando corresponda;
- tablas duplicadas por feature;
- tablas legacy;
- snapshots accidentales;
- tablas temporales persistentes;
- tablas puente sin relación real.

No convertir todo catálogo a ENUM:
si los valores cambian frecuentemente o tienen metadatos, una tabla puede ser correcta.

---

# 27. Anti-patterns

Evitar:

- índice en todas las columnas;
- UUID/texto gigantes como todo sin analizar;
- `SELECT *`;
- `OFFSET 1000000`;
- N+1;
- conexión por request sin pooling;
- transacción larga;
- RLS sin índices en columnas usadas por policies;
- `SECURITY DEFINER` indiscriminado;
- SQL dinámico concatenado;
- tablas EAV universales;
- JSONB como sustituto de diseño;
- 30 booleanos para representar estados;
- guardar archivos binarios grandes en DB sin evaluar object storage;
- duplicar datos sin estrategia de sincronización;
- sharding temprano;
- particionar tablas pequeñas;
- Scan frecuente en DynamoDB;
- arrays MongoDB sin crecimiento acotado.

---

# 28. MCP / conectores de base de datos

Si existen tools/MCP/conectores:

1. descubrir capacidades;
2. leer schema real;
3. leer estadísticas;
4. consultar índices;
5. consultar policies/roles;
6. consultar planes cuando sea seguro;
7. generar cambio;
8. aplicar solo con autorización;
9. volver a leer;
10. verificar.

No inventar resultados.

No mostrar:

- password;
- connection string completa;
- secrets;
- service keys.

Si no hay acceso:

- analizar migraciones/schema local;
- preparar SQL;
- marcar verificación pendiente.

---

# 29. Flujo de trabajo obligatorio

```text
DISCOVER PROJECT
       ↓
MAP WORKLOAD
       ↓
CHOOSE DATA MODEL
       ↓
AUDIT SCHEMA
       ↓
AUDIT RELATIONSHIPS
       ↓
AUDIT QUERIES
       ↓
AUDIT INDEXES
       ↓
AUDIT SECURITY
       ↓
MEASURE BASELINE
       ↓
DESIGN CHANGE
       ↓
MIGRATE
       ↓
TEST
       ↓
MEASURE AGAIN
       ↓
REPORT
```

---

# 30. Entregables

## 30.1 Architecture Decision

- motor actual;
- motor recomendado;
- motivo;
- alternativas;
- tradeoffs.

## 30.2 Schema review

Por tabla/colección:

- propósito;
- PK;
- relaciones;
- constraints;
- columnas innecesarias;
- índices;
- volumen;
- acciones.

## 30.3 Query review

Por query crítica:

- frecuencia;
- plan;
- rows;
- time;
- problema;
- cambio;
- resultado.

## 30.4 Security review

- roles;
- grants;
- RLS;
- funciones;
- parametrización;
- exposure;
- límites.

## 30.5 Migration plan

- pre-check;
- DDL;
- backfill;
- indexes;
- verification;
- rollback/forward-fix.

---

# 31. Formato de respuesta

## Resumen
- arquitectura actual;
- principal cuello de botella;
- riesgo de crecimiento;
- recomendación.

## Modelo recomendado
- SQL/NoSQL/híbrido;
- justificación por access patterns.

## Objetos innecesarios
- tablas;
- columnas;
- índices;
- relaciones.

## Relaciones
- 1:1;
- 1:N;
- N:M;
- embedding/references si NoSQL.

## Rendimiento
- consultas críticas;
- índices;
- planes;
- paginación;
- límites;
- pooling;
- funciones.

## Seguridad
- parametrización;
- roles;
- grants;
- RLS;
- funciones;
- datos sensibles.

## Cambios
- migraciones;
- SQL;
- aplicación.

## Verificación
- baseline;
- after;
- tests;
- riesgo residual.

---

# 32. Condición de finalización

No declares terminado hasta que:

- el workload fue comprendido;
- el modelo fue justificado;
- relaciones fueron revisadas;
- redundancias fueron evaluadas;
- consultas críticas fueron medidas;
- índices fueron justificados;
- límites fueron definidos;
- seguridad fue revisada;
- cambios fueron probados;
- resultados fueron medidos de nuevo.

Nunca afirmes que una base está “perfectamente optimizada”.
Indica alcance, evidencia y riesgo residual.
