# Bases de datos: modelado, creación, revisión y seguridad

La nueva [database-engineering-suite](../../skills/architecture/database-engineering-suite/SKILL.md)
es una skill autocontenida con siete guías que carga según la tarea. Incluye diseño
conceptual/lógico/físico, SQL/DDL y comandos NoSQL, migraciones, revisión, seguridad y
operaciones mediante MCP/API/CLI cuando exista acceso compatible.

## Capacidades

| Área | Qué hace |
|---|---|
| Modelado profesional | Entidades, cardinalidad, reglas del negocio, ERD y diccionario |
| Relacional | Tablas, PK/FK, 1:1/1:N/N:M, tipos, constraints e índices justificados |
| NoSQL | Documentos/referencias, colecciones, claves/partición, índices y validación |
| Seguridad | Acceso efectivo de tablas/filas/columnas o campos, tenant, roles y rutas de API |
| Evolución | Migraciones, coexistencia de versiones, backfill, validación y recuperación |
| Revisión | Integridad, drift, exposición de datos y hallazgos con evidencia |
| Rendimiento | Consultas reales, planes, índices, concurrencia y medición antes/después |
| Acceso | Descubre capacidades reales y prepara cambios cuando no puede ejecutar |

Las guías distinguen PostgreSQL, MySQL/MariaDB, SQL Server y SQLite; documentos MongoDB,
DynamoDB, Firestore y Redis. También orientan evaluación de grafos, series temporales y
almacenes analíticos/vectoriales, verificando motor y documentación antes de generar
sintaxis específica. No se afirma compatibilidad probada con todos esos motores.

La seguridad se analiza por su mecanismo real: RLS no equivale a permisos de columnas,
projection NoSQL no es autorización, ni una FK de tenant prohíbe leer datos de otro tenant.
Se requieren pruebas positivas y negativas por la ruta e identidad reales de la aplicación.

## Instalar y usar

Descomprime [database-engineering-suite.zip](../../SKILL/database-engineering-suite.zip)
en la carpeta de skills del agente. El ZIP ya incluye la carpeta de la skill; el resultado
debe ser `<carpeta-de-skills>/database-engineering-suite/SKILL.md`.
No se instaló globalmente ni se modificó una base real al crear estos archivos.

Ejemplos:

- «Usa $database-engineering-suite para modelar mi sistema de inventario en PostgreSQL».
- «Usa $database-engineering-suite para generar una migración compatible con mi ORM».
- «Revisa estas tablas, columnas sensibles y políticas para aislar empresas».
- «Diseña las colecciones MongoDB según estas consultas y reglas».
- «Inspecciona mediante el MCP disponible y prepara cambios sin aplicarlos».

Crear SQL no implica ejecutar en producción. Si se autoriza aplicar a un destino
confirmado, la skill trabaja dentro de ese alcance y verifica persistencia. Sin acceso
entrega modelo, archivos, consultas y pasos; declara las comprobaciones pendientes.
No instala MCP, crea cuentas/proyectos o exporta datos privados por pedir un modelo.

El repositorio conserva [scalable-database-architect](../../skills/architecture/scalable-database-architect/SKILL.md).
La nueva entrada prioriza carga selectiva y ejecución concreta. Para evitar duplicidad
en el catálogo activo, puedes instalar solo la nueva como entrada de bases de datos y
conservar la anterior en las fuentes del toolkit.

## Recursos y mantenimiento

Incluye plantilla de revisión y de migración, ejemplo relacional SQLite, validator MongoDB
y consultas de metadatos PostgreSQL. Los ejemplos son materiales de desarrollo, no
migraciones listas para aplicar a cualquier negocio. El validator no crea constraints
relacionales ni autorización de usuarios; el inventario no acredita seguridad por sí solo.

La [investigación](../../skills/architecture/database-engineering-suite/references/research-sources.md)
documenta los cuatro sitios solicitados, las fuentes oficiales y los accesos limitados.
Los contenidos son síntesis propia; no se importaron paquetes ni scripts de terceros.

Editar la guía o asset correspondiente y ejecutar:

```text
python -B -m unittest discover -s tests -p test_database_relational_example.py -v
python -B scripts/package_skill.py skills/architecture/database-engineering-suite
python -B scripts/package_skill.py skills/architecture/database-engineering-suite --check
python scripts/sync_skill_sources.py
```

El empaquetador conserva ZIPs cuyo contenido no cambió, valida rutas dentro de la skill
y rechaza archivos `.env` y skills anidadas que necesitan otro empaquetador.
Una comprobación estructural no sustituye revisión de los permisos de producción.

## Verificación realizada

Se validaron metadata, enlaces locales y correspondencia entre fuente y ZIP. Se
ejecutaron nueve pruebas del SQL SQLite: relaciones válidas, vínculos cruzados de
cliente/producto/orden, SKU duplicado, campos inválidos, borrado referenciado y cambio
de pertenencia incompatible. También se ejecutó el SQL directamente desde el ZIP.

Estas pruebas acreditan integridad del ejemplo SQLite, no RLS ni permisos de usuarios.
El SQL PostgreSQL y validator MongoDB quedan sin prueba de ejecución en sus respectivos
servidores. MCP y seguridad remota se verifican al usar la skill en una cuenta autorizada.
