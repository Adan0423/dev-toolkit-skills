# Diagnóstico, pruebas y operación

## Diagnóstico

Reproduce con modelo/registro, rol, compañía/contexto y secuencia. Traza UI→RPC/controller
→método/ORM→reglas→dependencias/datos. Logs/traceback mínimos sin secretos. XML parse
errors: external IDs/dependencias/XPath/sintaxis versión. Registro/modelo ausente:
imports/manifest/addons_path/instalación, no crea campos arbitrarios para tapar error.
Frontend: bundle, registry, template, consola/red y caché. Performance: medir proceso,
queries/prefetch y carga antes de índices/caches. No seguir mismo reintento fallido indefinidamente.

## Validación significativa

Lint/sintaxis Python/XML/JS y manifest son controles estáticos. Runtime requiere
Odoo/PostgreSQL/filestore y deps del proyecto. Prueba instalación limpia del addon y
actualización sobre copia existente. Usa TransactionCase y pruebas HTTP/UI/tours o
framework frontend compatible según riesgo. Confirma que tests se descubran/importen;
elige flags/tags CLI según versión, nunca ejecutar comandos de prueba contra producción.
No declarar tests aprobados cuando solo compila código o faltan dependencias Enterprise.

Prueba invariantes, rol autorizado/denegado, compañía A/B, import/API además de formulario,
errores/vacíos y transición completa en datos de prueba. Una prueba espejo del código
no demuestra negocio. UI: rango mobile/tablet/desktop, teclado y modos en alcance;
reportes HTML/PDF y traducción. Repite checks solo ante cambios o fallos nuevos.

## Hosting y despliegue

Online: no asumir addons Python; funciones permitidas del plan/Studio/imports/APIs.
Odoo.sh: ramas/builds/staging y addons Git según proyecto; verifica neutralización de
copias y servicios. On-premise/Docker: configuración/addons_path, PostgreSQL, filestore,
workers/proxy/long polling o websocket según versión. No abrir puertos, quitar TLS ni
cambiar dbfilter como reparación visual. No guardar odoo.conf con secretos en Git.

Antes de cambio de esquema/upgrade autorizado: copia consistente DB+filestore+config
necesaria, prueba restauración o registra limitación, compatibilidad/deps y ventana.
Actualiza solo módulos pertinentes, no -u all por rutina. Reiniciar servicio, activar
cron o deploy son acciones independientes del parche: respeta alcance ya autorizado.

## Migraciones

Inventaría versión origen/destino, módulos, external IDs, Studio, localizaciones y datos.
No confunde actualización de addon con salto de versión mayor. Usa proceso oficial
o herramientas compatibles cuando correspondan, prueba copia antes y compara conteos,
relaciones, permisos, saldos/stock pertinentes y flujos críticos. Scripts de migración
con versión/fases correctas, repetibles cuando proceda; no modifica DB a ciegas.
Downgrade de código no revierte esquema/datos: plan incluye restore coherente; considera
operaciones nuevas posteriores al corte para no prometer reversión sin pérdida.

## Casos para evaluar futuras ejecuciones

1. Online sin addons: guía/Studio compatible, no declarar addon instalado.
2. AccessError multiempresa: revisar rol/contexto/reglas, no sudo general.
3. Odoo antiguo: API/vistas de versión real, no copiar JSON-2/modificadores incompatibles.
4. Import con timeout: deduplicar por clave y recuperar resultados antes de repetir.
5. Website solo diseño: preserve checkout/modelos, responsive y contenido editable.
6. Migración con filestore: backup/restauración y pruebas, no solo dump de tablas.
7. Sin runtime: parche y validación estática, integración pendiente explícita.
8. Flujo factura/stock: métodos estándar y pruebas aisladas sin operación real implícita.

Estos casos no se presentan como ejecutados por el hecho de escribir este documento.
