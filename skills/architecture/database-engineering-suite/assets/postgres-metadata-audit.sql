-- PostgreSQL metadata-only example, not a comprehensive audit or migration.
-- Adapt schema 'public' and permissions to the authorized target before running.
-- LIMIT 500 bounds OUTPUT only; a limit hit means this is not a complete inventory.
-- No business-table rows, password hashes or function bodies are selected.
BEGIN TRANSACTION READ ONLY;
SET LOCAL statement_timeout = '10s';
SET LOCAL lock_timeout = '2s';

SELECT current_database() AS database_name, current_user AS effective_role,
       current_setting('server_version') AS server_version;

SELECT n.nspname AS schema_name, c.relname AS object_name, c.relkind,
       pg_get_userbyid(c.relowner) AS owner_role, c.relrowsecurity, c.relforcerowsecurity
FROM pg_catalog.pg_class c
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public' AND c.relkind IN ('r', 'p', 'v', 'm')
ORDER BY c.relname LIMIT 500;

SELECT c.relname AS table_name, a.attname AS column_name,
       pg_catalog.format_type(a.atttypid, a.atttypmod) AS data_type,
       a.attnotnull AS not_null, a.attidentity, a.attgenerated
FROM pg_catalog.pg_attribute a
JOIN pg_catalog.pg_class c ON c.oid = a.attrelid
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public' AND c.relkind IN ('r', 'p')
  AND a.attnum > 0 AND NOT a.attisdropped
ORDER BY c.relname, a.attnum LIMIT 500;

SELECT c.relname AS table_name, k.conname AS constraint_name, k.contype,
       k.convalidated, k.condeferrable, k.condeferred
FROM pg_catalog.pg_constraint k
JOIN pg_catalog.pg_class c ON c.oid = k.conrelid
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
ORDER BY c.relname, k.conname LIMIT 500;

SELECT c.relname AS table_name, i.relname AS index_name,
       x.indisunique, x.indisprimary, x.indisvalid, x.indisready
FROM pg_catalog.pg_index x
JOIN pg_catalog.pg_class c ON c.oid = x.indrelid
JOIN pg_catalog.pg_class i ON i.oid = x.indexrelid
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
ORDER BY c.relname, i.relname LIMIT 500;

SELECT c.relname AS table_name, p.polname AS policy_name, p.polcmd,
       p.polpermissive, p.polroles AS role_oids
FROM pg_catalog.pg_policy p
JOIN pg_catalog.pg_class c ON c.oid = p.polrelid
JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
ORDER BY c.relname, p.polname LIMIT 500;

-- These information_schema views have caller-dependent visibility.
SELECT table_name, grantee, privilege_type, is_grantable
FROM information_schema.table_privileges
WHERE table_schema = 'public'
ORDER BY table_name, grantee, privilege_type LIMIT 500;

SELECT table_name, column_name, grantee, privilege_type
FROM information_schema.column_privileges
WHERE table_schema = 'public'
ORDER BY table_name, column_name, grantee, privilege_type LIMIT 500;

SELECT rolname, rolsuper, rolbypassrls, rolinherit
FROM pg_catalog.pg_roles
WHERE rolname IN (current_user, session_user);
ROLLBACK;
