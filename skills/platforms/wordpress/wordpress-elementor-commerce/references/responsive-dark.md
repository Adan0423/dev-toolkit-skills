# Responsive, accesibilidad y modo oscuro

## Responsive

Inspecciona breakpoints del sitio y herencia del editor, no presupone valores default.
Diseña mobile first en prioridades de contenido, aplicando controles de la versión
sin desconocer su cascada. Layout continuo con flex/grid, límites de lectura y
tipografía fluida cuando soporte. Prueba anchos entre presets; tablet merece diseño
propio cuando el contenido lo requiere. No encubras overflow con overflow:hidden global.

Imágenes fluidas, dimensiones y srcset WordPress; embeds con relación de aspecto.
Tablas/código: scroll local etiquetado si necesario. Títulos largos, breadcrumbs,
etiquetas/productos y precios no deben salir del contenedor. No recortes controles.
Menú móvil: botón real, aria-expanded, teclado, Escape y foco correcto; focus trap
solo si es modal. Popups, avisos cookies, banners y sticky CTA no deben tapar checkout.
Prueba admin bar, teclado virtual, orientación y safe areas. Viewport y zoom habilitados.

## Sistema/Claro/Oscuro

Elige entre plugin mantenido compatible o tokens/CSS/JS pequeños en lugar soportado,
según instalación/licencia, complejidad y preferencias. Inspecciona plugin existente
antes de añadir otro. Selecciona por funcionamiento real, no por el nombre Dark Mode.
Verifica que soporte páginas Elementor/editor objetivo, WooCommerce y exclusiones;
una variante de kit no es por sí sola selector de tema para visitantes.

Define tokens de superficie, texto, bordes, links, foco y estados; aplica raíz
data-theme/clase. Sistema sigue prefers-color-scheme; preferencia explícita manda
y persiste entre páginas/recargas. Storage con fallback/try-catch, sin JS legible.
Bootstrap temprano minimiza destello: respeta CSP y caché compartida, no abrir seguridad.
Mantén color-scheme para formularios nativos y no uses inversión global de imágenes.

Estilos inline/globales de Elementor y CSS de addons pueden imponer colores: inspecciona
computed styles, corrige controles/tokens/selectores acotados. Evita !important indiscriminado
y selectores por IDs frágiles. Prueba logo, iconos, imágenes transparentes, forms,
dropdowns, tablas, overlays, modal, notices Woo, mini-cart, cuenta y checkout.
No intentes recolorear iframes de pago de terceros con CSS del sitio: usa apariencia
soportada por la pasarela; si no existe, presenta superficie legible y declara límite.

## Accesibilidad

Objetivo WCAG 2.2 AA: contraste texto normal 4,5:1, grande 3:1, foco/controles pertinentes;
skip link, headings lógicos, landmarks, labels, errores asociados y teclado completo.
Targets cómodos preferiblemente 44×44 CSS px; no depende de hover. Respeta reduced-motion,
forced-colors y zoom. Un plugin overlay no demuestra accesibilidad del sitio ni sustituye
corregir HTML/controles. Prueba contenido y estados, no solo el widget de accesibilidad.
