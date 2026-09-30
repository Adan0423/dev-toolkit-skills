# Seguridad de datos, filas, columnas y campos

## Qué proteger y ante quién

Define amenaza y superficie: cliente/API/backend/administrador, tenant/usuario, acciones,
datos sensibles y caminos alternativos (views, RPC, funciones, jobs, exportación).
Usa menor privilegio y roles separados de runtime, migración y administración. Un cliente
no obtiene owner/service credentials. Cifrado, masking y validación no sustituyen permiso.

Matriz mínima: rol → objeto → operación → filas → columnas permitidas → contexto validado.
Incluye lectura, insert, update, delete, export y operaciones masivas relevantes. No
revoca grants globalmente sin revisar consumidores y alcance autorizado.

## Relacionales

PostgreSQL: distingue privilegio de tabla/columna de RLS. `USING` selecciona filas
accesibles; `WITH CHECK` valida valores nuevos. Policies permissive pueden combinarse
por OR: una permisiva demasiado amplia puede abrir acceso. Owner y BYPASSRLS pueden
eludir políticas; FORCE afecta owner, no superuser/BYPASSRLS. RLS no cubre TRUNCATE.

Revisa grants efectivos por herencia, PUBLIC, esquemas, secuencias, default privileges,
views y funciones. Revocar un grant de columna no anula otro de tabla que da el mismo
acceso. Prueba SELECT directo además de API; serializers/SELECT con projection no son
protección suficiente para un rol con acceso libre a la tabla.

Datos sensibles: grants por columna o vistas/objetos separados y roles adecuados según
motor; verifica comportamiento de vistas/RLS en versión real. Para UPDATE limita también
columnas como tenant_id, owner_id, rol, saldo y estado de aprobación; RLS por fila no
implica que todas las columnas de esa fila deban ser editables.

Función privilegiada: justifica SECURITY DEFINER, identidad, validaciones, search_path
seguro, nombres cualificados y EXECUTE. No eleva permisos para arreglar un error de
acceso. La identidad/tenant para una política debe venir de contexto autenticado verificado;
un parámetro/GUC que cualquier cliente puede falsificar no es barrera de autorización.
Pools deben limpiar contexto entre solicitudes. No confía en tenant enviado por frontend.

MySQL/MariaDB: comprueba grants, roles y permisos de columnas en versión real; no genera
CREATE POLICY de PostgreSQL. Filtros en views/backend deben examinarse como mecanismos
propios, con acceso directo restringido. SQL Server: distingue RLS, permisos de columna,
masking y privilegios que permiten leer fuente. SQLite no ofrece GRANT/RLS de servidor;
protección de archivo/proceso, API y controles de aplicación son necesarios.

## NoSQL

MongoDB: usuarios/roles por recurso y operación, aislamiento de tenants en rutas de
acceso reales, auth de backend y validación de campos. Projection y validator no son
ACL de campo. Si hacen falta campos secretos para otro rol evalúa separación de datos
o mecanismos disponibles y sus límites. Cifrado de campo requiere gestión de claves,
compatibilidad/consulta e identidad autorizada, no solo elegir algoritmo.

Firestore: Rules para SDK cliente; servidor usa IAM y lógica de autorización. Revisa
lecturas y escrituras separadas, campos inmutables y rutas de colecciones. DynamoDB:
IAM, recursos/acciones/condiciones y acceso backend; verifica GSI y claves permitidas.
Redis: ACL comando/keys y red; no supone aislamiento por campo. Ningún filtro opcional
que el cliente controla debe ser la única defensa multiempresa.

## Aplicación y operación

Parametriza valores SQL; allowlist para identificadores/sort dinámicos. En consultas
NoSQL valida estructura y operadores permitidos: un objeto del usuario no se incorpora
como filtro confiable. Controla mass assignment; el cliente no fija roles/propietarios
o flags de aprobación fuera de una operación autorizada.

No guarda contraseñas en texto claro ni emplea hashing genérico como solución de login:
usa proveedor/mecanismo de contraseñas apropiado al stack. TLS verificado, gestión de
secretos, backups cifrados, acceso a logs y retención deben revisarse según alcance.
Clasifica PII y evita muestras reales en entregables. Auditoría de cambios no debe
registrar tokens/payloads privados. Borrado/retención afecta copias y datos derivados.

## Probar acceso efectivo

Con datos sintéticos prueba usuario A/B, tenants distintos, anónimo y roles autorizados.
Comprueba lectura de fila ajena y columna restringida, inserción con tenant falso,
cambio de owner/role, UPDATE/DELETE ajenos, vistas/RPC y exportación si están expuestos.
Incluye permiso válido para evitar «todo denegado» como falso éxito. Repite por la
ruta cliente real; pruebas owner/service solo acreditan administración.

Documenta resultado esperado y observado. Revocar admin del usuario, cambiar billing
o exportar tablas no está incluido por pedir una revisión de seguridad. Si no puedes
probar, entrega consultas/test plan y limita la conclusión a hallazgos de configuración.
