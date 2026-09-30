# Desarrollo por versión

## Elegir extensión

Configuración nativa si resuelve el proceso; Studio si existe y encaja; addon cuando
requiere lógica/versionado y hosting compatible. Detecta campos x_ y personalizaciones
Studio previas antes de crear duplicados. No reemplaces un flujo estándar con un modelo
paralelo sin necesidad ni incluyas apps Enterprise como dependencia en Community.

Estructura orientativa, creando solo lo necesario:

```text
mi_addon/
  __init__.py
  __manifest__.py
  models/{__init__,modelo}.py
  security/                      grupos, ACL/reglas según versión
  views/                         vistas heredadas, acciones, menús
  data/                          secuencias/configuración pertinente
  wizard/                        operaciones asistidas
  controllers/                   rutas necesarias
  report/                        acciones/QWeb
  static/src/{js,xml,scss}/       assets UI
  tests/                         invariantes y permisos
  migrations/                    scripts si aplica a versión
```

Manifest con versión/dependencias/licencia, orden de data y assets compatibles. Imports
reales en __init__. IDs externos únicos y estables; no reutiliza IDs de otro addon.
Datos demo separados de productivos. Nouupdate según intención: no usarlo para ocultar
configuración rota ni quitarlo masivamente para sobrescribir personalizaciones.

## ORM y reglas

Inspecciona modelos existentes y hereda con _inherit; _name solo para entidad nueva.
Recordsets en lote, super compatible, depends completos para computes, store solo
justificado y constraints para invariantes persistidas. Onchange ayuda al formulario,
no sustituye validación de servidor/API/import. Campos monetarios con currency correcta,
precision/UoM y fechas según versión. Relaciones usan IDs reales; Command en Python y
representación RPC compatible para x2many, sin sustituir relaciones completas por error.
No commit manual dentro de flujo ORM estándar. SQL excepcional debe justificar por qué,
respetar caché/flush y permisos; no usarlo para evitar reglas ni transiciones comerciales.

## Vistas y controllers

Hereda vistas con XPath estable, dependencias correctas y alcance mínimo. Verifica
sintaxis de modificadores, nombres list/tree, acciones y campos en versión instalada;
no copia attrs/states de tutoriales antiguos a versiones incompatibles. Campos
ocultos en vista no son seguridad. QWeb con escape, no renderizar entrada no confiable.
Rutas: auth/type/methods/CSRF según versión, validar recursos/compañía/ownership,
errores coherentes y permisos; no auth public con sudo para datos privados.
No expose métodos peligrosos por RPC sin controles propios.

## Automatizaciones y rendimiento

Cron y acciones automáticas según edición/acceso, idempotentes, acotadas y con logs
sin secretos. No activar automatizaciones que envíen mensajes o generen documentos
externos sin alcance autorizado. Evita N+1, búsquedas en bucle y computaciones costosas;
prefetch/agregación/paginación según versión. Perf mide consulta/proceso antes de
añadir índices o caches. Concurrency: invariantes de unicidad/reserva a nivel adecuado.
