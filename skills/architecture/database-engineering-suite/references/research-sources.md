# Fuentes, inspiración y mantenimiento

Investigación: 2026-09-30. Síntesis propia para este repositorio; no se importaron textos
o scripts de terceros. Las políticas, sintaxis y límites se deben revalidar para la
versión/edición/proveedor real. Las URLs `current` pueden cambiar de versión.

## Directorios solicitados

| Fuente consultada | Aporte | Límite |
|---|---|---|
| [skills.sh: MongoDB schema design](https://www.skills.sh/mongodb/agent-skills/mongodb-schema-design) | Organización por tarea y acceso a la fuente mantenida por MongoDB | No convierte umbrales ilustrativos ni planes de Atlas en reglas universales |
| [Fuente MongoDB](https://raw.githubusercontent.com/mongodb/agent-skills/main/skills/mongodb-schema-design/SKILL.md) | Guías selectivas para modelado, validación, patrones y diagnóstico | Se estudió su estructura; no se copió ni instaló el paquete |
| [SkillsMP](https://skillsmp.com/es) | Descubrir ejemplos públicos y revisar procedencia | No certifica calidad/seguridad; la búsqueda específica de database no pudo recuperarse |
| [Impeccable](https://impeccable.style/) | Documentar contexto y separar tareas de revisión | Diseño visual no aporta garantías de integridad o permisos; no se exige instalarlo |
| [Awesome Skills: database schema designer](https://awesomeskill.ai/skill/softaworks-agent-toolkit-database-schema-designer) | Separar modelo, constraints, migración y revisión en entregables | La portada no pudo recuperarse en esta consulta; sí se consultó esta ficha. Sus puntuaciones no son evidencia de seguridad de una base |

El toolkit ya conserva `scalable-database-architect`. Esta nueva skill tiene una entrada
corta y guías de ejecución/seguridad; no reemplaza ni modifica esa fuente anterior.
Si se quiere reducir el catálogo, instalar la nueva como entrada principal de trabajo
de bases de datos y conservar la anterior como material fuente opcional.

## Documentación oficial consultada

- [PostgreSQL: constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).
- [PostgreSQL: Row Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html).
- [PostgreSQL: GRANT](https://www.postgresql.org/docs/current/sql-grant.html).
- [PostgreSQL: EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html).
- [PostgreSQL: CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html).
- [MySQL 8.4: GRANT](https://dev.mysql.com/doc/refman/8.4/en/grant.html).
- [MySQL 8.4: commits implícitos](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html).
- [SQLite: foreign keys](https://www.sqlite.org/foreignkeys.html).
- [MongoDB: modelado](https://www.mongodb.com/docs/manual/data-modeling/).
- [MongoDB: schema validation](https://www.mongodb.com/docs/manual/core/schema-validation/).
- [DynamoDB: modelado NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-modeling-nosql.html).
- [Firestore: condiciones de seguridad](https://firebase.google.com/docs/firestore/security/rules-conditions).
- [Redis: ACL](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/).
- [SQL Server: Row-Level Security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17).

Las fuentes apoyan mecanismos concretos por motor; no afirman que el mismo DDL funcione
en todos. Modelado, plantillas, ejemplos y protocolo MCP son redacción propia.
Para un motor/proveedor no investigado aquí, consulta sus fuentes oficiales antes de
generar o aplicar sintaxis específica. No se afirma certificación de proveedor.

## Mantener

Editar solo la guía relevante; mantener enlaces y ejemplos coherentes. Cambios a assets
SQL requieren ejecutar tests del motor correspondiente. La validación SQLite incluida
no demuestra comportamiento PostgreSQL, MongoDB o de permisos remotos. Si cambia una
instrucción de seguridad, verificar roles/rutas reales en un entorno autorizado.

Después reconstruir el ZIP y comprobar su contenido; registrar qué se verificó y qué
necesita un servidor/conexión. Crear la skill no instala motores ni conecta cuentas.
