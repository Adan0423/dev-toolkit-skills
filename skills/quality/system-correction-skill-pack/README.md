# System Correction Skill Pack

Paquete modular para corregir sistemas web, aplicaciones móviles y escritorio.

## Skills incluidas

1. `system-correction-orchestrator`
   - Orquesta el diagnóstico completo UI → backend → DB/storage → UI.

2. `rbac-database-corrector`
   - Corrige PostgreSQL/Supabase, RLS, GRANT, RBAC, funciones SQL y Storage.

3. `role-aware-ui-corrector`
   - Corrige páginas públicas, dashboards, paneles por rol, formularios, imágenes,
     estados y data binding.

4. `mcp-integration-corrector`
   - Descubre y usa MCP/conectores disponibles para inspeccionar y verificar estado real.

## Orden recomendado

Usa `system-correction-orchestrator` como skill principal.
Activa las otras según la capa afectada.

Ejemplo:

`dashboard no muestra imágenes para editor`
→ orchestrator
→ role-aware-ui-corrector
→ rbac-database-corrector
→ mcp-integration-corrector (si hay acceso)
→ verificación end-to-end
