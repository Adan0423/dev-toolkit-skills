# MCP, API, CLI y operaciones de base de datos

## Descubrir y conectar

Inspecciona herramientas disponibles por descripción/capacidades, no solo nombre.
Identifica proveedor, proyecto/cuenta, endpoint, motor, versión y entorno, sin mostrar
credenciales. Permisos pueden ser read-only, metadata-only o restringidos por esquema.
MCP no agrega permisos que la identidad conectada no tiene.

Supabase, InsForge, PostgreSQL, MongoDB y otros necesitan conectores/protocolos apropiados;
una tool execute_sql no implica acceso a otro proveedor. No fabrica URLs, IDs, RPC,
schemas o tablas. Si hay skill específica instalada, úsala solo cuando su procedimiento
aporte a la operación concreta; no carga todos los proveedores.

Sin MCP puede usar CLI/API oficiales ya configurados dentro del alcance. Si no hay acceso,
prepara archivos y consultas de inspección, explica qué ejecutar y qué resultado falta.
No instala conectores, habilita acceso público o crea una base/proyecto salvo solicitud.
No exige compartir contraseñas en el chat o guardarlas en repo.

## Leer

Empieza por identidad y metadatos relevantes. Consultas de datos requieren necesidad,
autorización y límites; prefiere conteos/aggregados/muestras sintéticas para revisión.
No presume que SQL iniciado con SELECT es libre de efectos; revisa funciones y operación.
Ejecutar triggers/procedimientos no es lectura de metadatos.

Usa mecanismos read-only y timeouts soportados por motor/proveedor cuando ayuden.
«Read-only» no convierte una consulta pesada en económica. Reporta truncado/paginación;
ausencia, denegación, error y desconocido son estados distintos. Inventario bajo un rol
restringido no demuestra inexistencia de objetos ni grants invisibles.

No muestra payloads con credenciales, tokens, hashes de contraseña o PII. Esquemas de
proveedor/auth/storage/system solo se tocan cuando explícitamente están en alcance.
No se inventa un usuario de prueba real; usa datos sintéticos y entorno permitido.

## Escribir cuando autorizado

Deja SQL/migración y efecto concretos revisables antes de pedir autorización que falte.
La autorización previa para aplicar a un destino confirmado sigue vigente; no la pide
de nuevo por rutina. «Revisar» o «diseñar» no autoriza modificar la cuenta remota.

Comprueba motor/versión, destino, branch/entorno, roles, historial y diff. Ejecuta dry-run,
validate-only o branch aislada cuando existan y sean útiles; una validación no es aplicación.
No simula esos modos si API/MCP no los soporta. Usa transacciones solo si operación/motor
permiten; consulta [migraciones](migrations.md) para locks y recuperación.

Ante error/timeout no repite creación masiva o grant sin reconciliar estado. Revisa
errores parciales y alcance persistido. Si no puede proseguir de forma segura, conserva
archivos, informa qué cambió realmente y qué falta; no sube privilegios como workaround.

## Verificar

Consulta esquema y registro aplicado, valida invariantes y permisos por ruta real de
cliente/backend. Para RLS/grants compara roles de runtime; probar como service/owner
no demuestra aislamiento. Si MCP solo usa rol administrativo, la verificación de
usuarios necesita un canal apropiado o queda pendiente, no se declara aprobada.

Devuelve proyecto/entorno identificable sin secretos, objetos y cambios, pruebas y
pendientes. Conservar logs sanitizados/IDs de migración permite reconciliar reintentos.
No exporta backups, borra usuarios ni cambia billing/red por pedir un esquema profesional.
