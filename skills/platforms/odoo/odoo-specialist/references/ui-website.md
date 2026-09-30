# UI, Owl, Website y portal

## Elegir superficie

Diferencia web client ERP, portal autenticado, website público, eCommerce y reportes.
Respeta edición/versiones, editor Website y componentes existentes. Si usuario pide
solo diseño, preserva modelos, métodos, permissions y APIs. Reporte impreso requiere
comprobar PDF, no solo HTML. No crea una SPA independiente como sustituto del ERP.

## Diseño y skills

Descubre skills disponibles: aplica el solicitado, o lee el adecuado para dirección
visual, sistema, Figma, accesibilidad o responsive. Admite otros relevantes sin una
lista obligatoria. Traduce su salida a QWeb/Owl/snippets/assets soportados, no pega
React sin integración. Sin skill disponible, continúa con componentes y criterios
propios. Explica el usado y no supone que esto autoriza delegación o mensajes externos.

Tokens, jerarquía, legibilidad, tablas y formularios deben servir al rol/proceso. UI
de datos ofrece loading/empty/error/access denied/offline según estado real y reintentos
pertinentes. Usa translatable strings, formatos monetarios/UoM y fechas del entorno.

## Implementación

Owl según versión: setup/hooks, servicios/registries y plantillas con prefijo addon.
Extiende componentes con mecanismo soportado, evita monkey patches globales y llamadas
directas no compatibles. Assets en bundles apropiados: backend y frontend no son
intercambiables. Portal/Website necesitan montaje compatible y texto público útil
renderizado cuando convenga; no cargar todo ERP en páginas públicas.
El editor Website/snippets requiere estructuras y opciones compatibles para conservar
edición. Hereda templates mínimo; no reemplaza footer/layout de toda instalación para
ajustar página local. Forms/controllers validan servidor, no solo frontend.

## Responsive y modos

Para UI nueva/modificada, verifica mobile/tablet/desktop e intermedios: 320, 390, 768,
1024, 1280/1440 CSS px, orientación, zoom y teclado. Tablas con scroll local o adaptación
sin ocultar acciones clave; controles táctiles, foco, labels, navegación y contraste.
Prueba título largo, vacío/error, menús, dialogs y datos reales.
Modo oscuro cuando requerido: primero capacidades nativas de la edición/superficie;
si personalizado, tokens semánticos, preferencia sistema/claro/oscuro persistente,
fallback sin JS y reduced-motion. No invertir imágenes ni sobrescribir todos los
assets del ERP; revisar forms, tablas, banners, portal y checkout afectados.

## Contenido y SEO

Artículos/productos/páginas en modelos instalados, no texto incrustado sin edición.
IDs, variantes, compañía/website e idioma correctos. Crear draft salvo publicación
solicitada; recuperar status/URL y probar permisos portal. SEO en alcance: canonical,
HTML útil, enlaces, metadata y schema sin duplicados; integrar seo-geo-web si disponible.
Checkout preserva reglas de stock/precio/impuestos y pasarelas; sandbox sin cobros reales.
