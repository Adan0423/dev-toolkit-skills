---
name: rbac-database-corrector
description: >
  Diagnostica y corrige conexión, autorización y consistencia entre aplicaciones y
  bases de datos, especialmente PostgreSQL/Supabase. Audita esquema, RLS, GRANT,
  RBAC, funciones SQL, vistas, storage y migraciones, verificando permisos positivos
  y negativos por rol.
version: 1.0.0
language: es
tags:
  - postgres
  - supabase
  - sql
  - rbac
  - rls
  - database
  - authorization
---

# RBAC Database Corrector

## Objetivo

Garantizar que el acceso a datos coincida exactamente con las reglas del sistema.

No basta con que una consulta funcione para el administrador.
Debe funcionar para cada rol autorizado y fallar para cada rol no autorizado.

---

# 1. Descubrir el modelo real

Identifica:

- motor de DB;
- schemas;
- tablas;
- PK/FK;
- vistas;
- funciones/RPC;
- triggers;
- roles;
- grants;
- RLS;
- auth;
- claims;
- storage;
- migraciones.

Si existe MCP/conector de base de datos, úsalo primero para leer el esquema real.

Nunca asumas que el esquema local coincide con producción.

---

# 2. Construir matriz RBAC

Ejemplo conceptual:

| Recurso | Acción | visitante | usuario | editor | admin |
|---|---|---:|---:|---:|---:|
| posts publicados | SELECT | sí | sí | sí | sí |
| draft propio | SELECT | no | sí* | sí | sí |
| crear post | INSERT | no | sí* | sí | sí |
| publicar | UPDATE estado | no | no | sí | sí |
| usuarios | SELECT | no | no | no | sí |

`*` sujeto a ownership/reglas de negocio.

La matriz debe derivarse del producto, no inventarse.

---

# 3. PostgreSQL / Supabase

Distingue dos niveles:

## Object privileges / GRANT

Controlan si un rol puede alcanzar:

- tabla;
- vista;
- función;
- secuencia;
- schema.

## Row Level Security

Controla qué filas puede leer o modificar.

Cuando la API expone directamente PostgreSQL/Supabase, usa ambos controles cuando
corresponda.

---

# 4. Política RLS

Para cada tabla expuesta:

- confirmar si RLS está habilitado;
- listar policies;
- comprobar SELECT;
- comprobar INSERT;
- comprobar UPDATE;
- comprobar DELETE;
- comprobar `USING`;
- comprobar `WITH CHECK`;
- comprobar ownership;
- comprobar claims.

No uses una política `true` global sin justificarla.

---

# 5. Ownership

Patrón conceptual:

```sql
owner_id = current_user_id()
```

En Supabase puede derivarse de `auth.uid()` cuando la arquitectura lo utiliza.

No confíes en un `user_id` enviado por el cliente para autorizar por sí solo.

---

# 6. RBAC

Si el sistema usa roles de aplicación:

- identifica fuente de verdad;
- evita duplicar roles inconsistentes;
- valida claims;
- valida permisos server-side/database-side;
- separa rol de aplicación de rol técnico de PostgreSQL cuando corresponda.

En Supabase, RBAC puede implementarse mediante claims y RLS.

---

# 7. Funciones SQL

Usa funciones para:

- encapsular operaciones atómicas;
- centralizar lógica consistente;
- transacciones;
- validación;
- acciones complejas.

No uses función SQL para ocultar una mala política de autorización.

## SECURITY INVOKER

Preferir cuando la operación debe respetar permisos del llamador.

## SECURITY DEFINER

Usar solo cuando existe necesidad real.

Si se utiliza:

- propietario mínimo necesario;
- `search_path` seguro;
- nombres schema-qualified;
- EXECUTE restringido;
- validar parámetros;
- no aceptar IDs arbitrarios sin autorización;
- probar acceso negativo;
- revisar posibilidad de bypass RLS.

No crearla con privilegios excesivos por comodidad.

---

# 8. Ejemplo de función de permiso

Patrón conceptual, adaptar al esquema real:

```sql
create or replace function private.has_permission(required_permission text)
returns boolean
language sql
stable
security invoker
as $$
  select exists (
    select 1
    from private.user_permissions p
    where p.user_id = auth.uid()
      and p.permission = required_permission
  );
$$;
```

No copiar ciegamente.
Verificar arquitectura, acceso al schema y RLS.

---

# 9. Integridad de datos

Revisa:

- NOT NULL;
- UNIQUE;
- CHECK;
- FK;
- cascadas;
- defaults;
- enums;
- timestamps;
- zonas horarias;
- soft delete;
- auditoría;
- datos huérfanos.

La UI no debe ser la única capa que impide datos inválidos.

---

# 10. Migraciones

Toda corrección estructural debe ser reproducible.

Preferir:

1. migration;
2. transaction;
3. pre-check;
4. change;
5. post-check;
6. rollback documentado.

No editar producción manualmente si existe un flujo de migraciones.

---

# 11. Test por rol

Por cada recurso:

## Positive
El rol autorizado puede ejecutar la operación esperada.

## Negative
El rol no autorizado recibe rechazo.

## Ownership
Un usuario no puede leer/editar/borrar recursos de otro cuando no corresponde.

## Elevation
Un cliente no puede asignarse un rol superior.

---

# 12. Diagnóstico de errores comunes

## 401
Revisar identidad/token/sesión.

## 403 / RLS violation
No desactivar RLS.
Revisar:
- policy;
- claim;
- ownership;
- SELECT/INSERT/UPDATE/DELETE;
- GRANT;
- contexto de autenticación.

## 404
Distinguir inexistencia de recurso vs política que oculta la fila.

## datos incorrectos
Revisar:
- joins;
- filtros;
- tenant;
- ownership;
- caché;
- view;
- función;
- timezone.

---

# 13. Supabase Storage

Para uploads:

- definir bucket público o privado deliberadamente;
- aplicar RLS sobre `storage.objects`;
- restringir paths/owners;
- limitar tipos/tamaño;
- usar API de Storage para operaciones de objetos;
- no hacer escrituras directas a tablas internas de Storage;
- verificar lectura, subida, reemplazo y borrado por rol.

No hacer público un bucket privado para corregir un error de imagen.

---

# 14. Verificación final

Entregar:

- esquema afectado;
- matriz RBAC;
- policies antes/después;
- grants;
- funciones;
- migración;
- tests positivos;
- tests negativos;
- riesgo residual.
