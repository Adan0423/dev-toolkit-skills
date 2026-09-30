# Referencias oficiales — Scalable Database Architect

Actualizadas al 14 de agosto de 2026 según documentación consultada.

## PostgreSQL 18

### EXPLAIN / query plans
https://www.postgresql.org/docs/current/using-explain.html

### EXPLAIN
https://www.postgresql.org/docs/current/sql-explain.html

### pg_stat_statements
https://www.postgresql.org/docs/current/pgstatstatements.html

### Table partitioning
https://www.postgresql.org/docs/current/ddl-partitioning.html

### Partial indexes
https://www.postgresql.org/docs/current/indexes-partial.html

### Index-only scans / covering indexes
https://www.postgresql.org/docs/current/indexes-index-only-scans.html

### ANALYZE / planner statistics
https://www.postgresql.org/docs/current/sql-analyze.html

### Client connection defaults / timeouts
https://www.postgresql.org/docs/current/runtime-config-client.html

### Privileges
https://www.postgresql.org/docs/current/ddl-priv.html

### Row Level Security
https://www.postgresql.org/docs/current/ddl-rowsecurity.html

### CREATE FUNCTION / SECURITY DEFINER
https://www.postgresql.org/docs/current/sql-createfunction.html

### Function security
https://www.postgresql.org/docs/current/perm-functions.html

## MongoDB 8.3

### Data Modeling
https://www.mongodb.com/docs/manual/data-modeling/

### Best Practices for Data Modeling
https://www.mongodb.com/docs/manual/data-modeling/best-practices/

### Embedded Data
https://www.mongodb.com/docs/manual/data-modeling/embedding/

### Relationships / embedding vs references
https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/map-relationships/

## Amazon DynamoDB

### Best practices
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html

### Partition key design
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html

### Sort key design
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-sort-keys.html

### Query and Scan
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html

### Core keys and indexes
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

## Supabase / PostgreSQL

### Database overview
https://supabase.com/docs/guides/database/overview

### Connection pooling
https://supabase.com/docs/guides/database/connecting-to-postgres

### Row Level Security
https://supabase.com/docs/guides/database/postgres/row-level-security

### Database functions
https://supabase.com/docs/guides/database/functions

### Database Advisors
https://supabase.com/docs/guides/database/database-advisors

### Securing Data API
https://supabase.com/docs/guides/api/securing-your-api

## OWASP

### SQL Injection Prevention Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

### Query Parameterization Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html

### NoSQL Injection Testing
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.6-Testing_for_NoSQL_Injection

## Principio de mantenimiento

Cuando exista acceso a Internet:

1. comprobar la versión actual del motor;
2. priorizar documentación oficial de esa versión;
3. no aplicar recomendaciones específicas de PostgreSQL a otro motor;
4. no copiar índices/configuración sin medir;
5. documentar diferencias por entorno.
