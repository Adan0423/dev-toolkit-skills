# WooCommerce: diseño y operación

## Preservar la fuente de verdad

Inspecciona versión, tipo checkout (bloques/clásico), tema/widgets, tipos de productos,
moneda, impuestos/envíos/pagos existentes, HPOS e integraciones. Diseño usa datos Woo:
no precios ficticios, formularios checkout propios ni llamadas de pago improvisadas.
No migres bloques a shortcodes o viceversa para facilitar CSS sin evaluar compatibilidad.

Diseña tienda/archivo, detalle simple/variable, galería, filtros, stock, promociones,
productos relacionados, mini-cart, carrito, checkout y cuenta según alcance. Usa
widgets/templates compatibles y disponibles; sin funciones Elementor requeridas,
mantén salida del tema/Woo y aplica estilos seguros o propone opción licenciada.
No garantizar widgets de tienda en cualquier plan. Condiciones Theme Builder no deben
reemplazar accidentalmente páginas de checkout/cuenta con una landing.

## Productos y catálogo

Mapea nombre, slug/SKU, tipo, descripción corta/larga, estado, precio/currency, sale,
stock, categorías/tags/atributos, imágenes y envío solo con datos proporcionados.
SKU y mapa origen→ID para deduplicar; en variables crea/valida atributos y variaciones
con precios/stock correctos. No convierte producto variable en simple para hacer import.
Respeta separadores/formato de API, no sustituir precio con texto formateado de pantalla.
Draft si solo solicita cargar sin publicación explícita; confirma ID/status/URL.

REST Woo (habitualmente wc/v3) es API administrativa autenticada con permisos; Store API
resuelve catálogo/carrito/checkout para compradores y no es sustituto de administración.
Descubre schema/versiones reales. Claves administrativas nunca al JS público.
Store API requiere mecanismos de sesión/nonce/token pertinentes: no inventarlos ni
omitir validaciones para hacer funcionar un botón. Para PHP, usa CRUD Woo en vez de
postmeta/SQL directo; HPOS hace peligroso asumir pedidos como posts en almacenamiento.

## Prueba comercio

Antes/después: selección de variación, añadir/eliminar/actualizar cantidad, stock,
cupón válido/inválido, notices, total/envío/impuestos según configuración, checkout
errores/éxito y cuenta. QA sin cobros reales ni correos a clientes por defecto:
staging/sandbox con datos de prueba autorizados. No crear pedidos/pagos reales para
demostrar estética. No modificar pedidos, reembolsos o pasarelas sin solicitud específica.
Sistemas de pago externos pueden limitar dark mode; documenta lo verificable.

Evita caché compartida de páginas/sesiones carrito, checkout/cuenta según recomendaciones
del stack. Prueba usuario invitado/autenticado sin exponer PII. Rediseño preserva URLs,
eventos analíticos y accesibilidad de precios, variaciones y mensajes.
