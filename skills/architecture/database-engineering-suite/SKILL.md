---
name: database-engineering-suite
description: >-
  Modela, crea y revisa bases de datos SQL y NoSQL; diseña relaciones, tablas o
  documentos, migraciones, índices y seguridad de filas/columnas. Úsalo para crear
  esquemas, auditar permisos o mejorar consultas, mediante código y MCP compatible.
---

# Database Engineering Suite

Trabaja en español salvo preferencia del usuario. Reutiliza requisitos, esquema y
migraciones existentes antes de proponer cambios. Para una tarea local no exige una
auditoría total ni una entrevista extensa. No reemplaza el motor elegido sin razón.

## Selección de guía

| Tarea | Primera guía |
|---|---|
| Elegir modelo/motor, entidades y reglas de negocio | [Modelado](references/modeling.md) |
| Tablas, relaciones, constraints, DDL/SQL/ORM | [Relacional](references/relational.md) |
| Documentos, claves, colecciones, grafo y consistencia | [NoSQL](references/nosql.md) |
| Roles, tablas, filas, columnas/campos y multiempresa | [Seguridad](references/security.md) |
| Crear/evolucionar esquema y datos existentes | [Migraciones](references/migrations.md) |
| Revisar esquema, integridad, consultas e índices | [Revisión y rendimiento](references/review-performance.md) |
| Inspeccionar o aplicar mediante MCP/API/CLI | [Operaciones y MCP](references/mcp-operations.md) |

Lee primero una guía; añade solo las necesarias. Por ejemplo: un ERD empieza con
modeling, una revisión RLS con security y un cambio de esquema existente con migrations.
No carga todas por defecto. [Fuentes investigadas](references/research-sources.md).

## Contexto y alcance

Determina motor/versión, proveedor, proyecto/entorno, esquema real, lenguaje/ORM,
patrones de acceso, volumen/concurrencia, consistencia y límites relevantes para la tarea.
Pregunta solo lo decisivo que falte. Sin acceso puede producir modelo y código,
etiquetando supuestos; no presenta SQL genérico como validado en todos los motores.

Modela invariantes: cardinalidad, pertenencia, unicidad, estados, retención y operaciones
atómicas. Elige estructura proporcional al negocio. Seguridad es autorización efectiva,
no solo presencia de tablas, grants, una política o cifrado.

## Ejecución y verificación

Descubre capacidades MCP reales por proveedor y operación; no presupone acceso porque
la herramienta se llame «database». Inspeccionar/diseñar no autoriza cambios remotos.
Cuando la aplicación esté autorizada, comprueba identidad, permisos, diff y destino
antes de ejecutar y lee el resultado persistido. No repite una migración tras timeout
sin reconciliar estado. Conserva límites y autorizaciones previas del usuario.

Prepara cambios reversibles en el workspace dentro del alcance solicitado. Para aplicar
en producción o destruir datos necesita autorización concreta si no está ya dada;
primero deja SQL, efecto y recuperación revisables. No crea proyectos, instala conectores
ni exporta datos privados por una petición de diseño. No registra secretos o muestras PII.

Prueba integridad y acceso con datos sintéticos y roles reales de cliente: permisos
positivos y negativos, tenant/usuario ajeno, columnas protegidas y escritura inválida.
Una prueba como owner/service role no acredita aislamiento de usuarios. Read-only
puede limitar visibilidad; ausencia de resultados no prueba ausencia de objetos.

## Entrega

Según alcance entrega ERD/diccionario, decisión de modelo, DDL o comandos nativos,
migración/backfill, matriz de acceso y hallazgos con evidencia. Usa
[plantilla de revisión](assets/schema-review.md) y [plan de migración](assets/migration-plan.md)
cuando aporten. Declara motor, versión, pruebas ejecutadas y pendientes. Nunca afirma
«seguro» u «optimizado» universalmente a partir de revisión estática.
