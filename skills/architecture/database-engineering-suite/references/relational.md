# Modelado relacional y SQL

Detecta motor/versión antes de producir DDL: PostgreSQL, MySQL/MariaDB, SQL Server,
SQLite u otro no comparten íntegramente tipos, identidad, constraints, índices o DDL.
Usa documentación de la versión real. No transpila sustituyendo nombres mecánicamente.

## Relaciones y tipos

- PK estable: natural/sustituta, bigint/UUID según identidad, volumen y distribución;
  no exige UUID a todo ni email como identidad inmutable.
- 1:N: FK en dependiente; 1:1: FK con unicidad y nullability acorde; N:M: tabla puente
  con unicidad de asociación y atributos propios cuando corresponda.
- Explicita `ON DELETE/UPDATE` según ciclo de vida. Cascade puede borrar historial;
  soft delete puede afectar unicidad y filas relacionadas, no equivale a revocar acceso.
- Multiempresa: el padre debe tener una clave candidata `(tenant_id,id)` cuando la FK
  del hijo referencia ambos. Si ambos campos deben existir, ambos requieren NOT NULL.
- Dinero/cantidades: decimal exacto o unidades menores enteras con moneda y escala
  acordadas; no presupone dos decimales para todas las monedas. Evita float para importes.
- Fechas: diferencia instante, fecha civil y horario recurrente; normaliza instantes y
  conserva zona de negocio donde importe. No impone tipo timestamptz fuera de PostgreSQL.

Normaliza dependencias para evitar anomalías. Desnormaliza solo un dato concreto con
regla de mantenimiento y evidencia de necesidad. JSON es útil para atributos variables,
no para evadir relaciones críticas. Un snapshot de precio en una compra puede ser
correcto aunque el catálogo tenga precio actual: son hechos distintos.

## Integridad

Usa NOT NULL, UNIQUE, FK y CHECK para reglas que el motor puede sostener. CHECK puede
aceptar UNKNOWN por NULL; nullability se define aparte. Las reglas entre filas/tablas
pueden necesitar constraints especiales, transacción o mecanismo adicional; no agrega
subconsultas a CHECK como si fueran universales. Verifica comportamiento de UNIQUE con NULL,
collation/case, timestamps y columnas calculadas por motor.

Estados/transiciones, stock y cuotas requieren evitar read-then-write sin control de
concurrencia. Escoge escritura condicional/locks/optimistic version e idempotencia para
evitar duplicados; restricciones y tests deben demostrar el invariante bajo competencia.
No mantiene «total correcto» solo mediante cálculo en frontend.

Índices se derivan de filtros, joins, orden y consultas reales. Comprueba lo que crean
PK/UNIQUE y lo que no crea la FK en ese motor. Justifica compuesto/covering/parcial;
evita índices duplicados o en toda columna. Considera coste de escritura/espacio.

## Código y aplicación

Genera archivos según convenciones existentes: migraciones SQL o ORM (Prisma, Drizzle,
SQLAlchemy, Django, Eloquent, EF, etc.), sin implementar todos. El ORM no sustituye
constraints, seguridad ni verificación del SQL real. Evita dual drift entre SQL y modelo.
Consulta con parámetros; identifica qué nombres dinámicos deben venir de allowlist.

Incluye consultas representativas, transacciones y seeds sintéticos si se piden. Para
crear en un entorno existente usa [migraciones](migrations.md), no un dump que destruya
datos. `IF NOT EXISTS` no acredita equivalencia con la definición esperada.

## Ejemplo y límites

[Ejemplo SQLite](../assets/sqlite-relational-example.sql) muestra pertenencia e integridad
en un entorno vacío de prueba. Se prueba localmente; no es un esquema comercial completo
ni implementa roles/RLS de servidor. `PRAGMA foreign_keys=ON` debe habilitarse por conexión
y fuera de una transacción cuando corresponda. El SQL no se aplica automáticamente.

Para PostgreSQL hay [inventario de metadatos](../assets/postgres-metadata-audit.sql), que
debe adaptarse al esquema y permisos de la cuenta. No se ha ejecutado contra PostgreSQL.
Para seguridad de tablas/filas/columnas lee [seguridad](security.md); una FK no es un permiso.
