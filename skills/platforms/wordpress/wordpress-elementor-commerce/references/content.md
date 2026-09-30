# Artículos, medios y ajustes

## Editorial

Usa WordPress para artículos/páginas/taxonomías; Elementor para plantillas o páginas
que necesitan maquetación. No copies cada artículo completo a una plantilla compartida.
Preserva cuerpo editable y bloques válidos, evitando un widget HTML gigante.
Mapea título, slug, extracto, cuerpo, autor real, idioma, estado/fecha, taxonomías,
featured_media y campos soportados. No inventar autorías, reseñas ni estadísticas.

Confirma identidad/capabilities antes de escribir. Cargar sin instrucción de publicar:
borrador. Publicación explícita ya autoriza esa operación en los recursos solicitados.
Programación usa zona del sitio y estado soportado. Cambiar slug publicado requiere
evaluar redirect. Consulta duplicados por origen/slug, conserva mapa IDs y revisiones.
Recupera recurso tras guardar: ID, status, link, contenido y render real. Restricciones
de acceso no equivalen a datos vacíos. En lote registra cada éxito/fallo/pendiente.

## Medios

Comprueba licencia, tamaño, MIME y uso. Biblioteca/API de medios devuelve attachment ID
y tamaños; completa alt/caption reales, asigna imagen destacada y comprueba srcset.
Upload no implica asignación a post ni widget; sustituye referencias importadas por
medios reales. No duplicar tras timeout; no permitir SVG inseguro. Fallo de imagen
no debe ocultarse publicando un recurso roto.

## Ajustes y datos personalizados

Identidad, portada/blog, navegación, idioma/zona, permalinks, comentarios, SEO y caché
según alcance. Registra anterior→solicitado→persistido. No cambia roles, pagos, tasas,
envíos o privacidad global por implicación de un diseño. Formulario real requiere
destino/integración, error y éxito comprobados sin enviar a terceros no autorizados.

ACF u otro plugin de campos solo si aporta valor y existe/instalación está autorizada.
Registra tipos/capabilities y Dynamic Tags compatibles. Meta plugins no necesariamente
es writable por REST core ni por MCP. No crear datos falsos para satisfacer un widget.
Conserva gestor SEO/canonical/schema y multilingual. No desactiva indexación en sitio
real para esconder cambios; usa draft/staging cuando corresponda.

## Importación

REST core usual wp/v2: descubre posts/pages/media/taxonomías y schemas actuales;
cookie+nonce para admin o Application Passwords HTTPS según soporte. WP-CLI solo con
shell autorizado; en multisite confirma URL. Templates/kit Elementor exportan diseño,
no sustituyen backup WP/Woo. WXR/CSV/JSON requieren herramienta y mapeo adecuados.
No importar sobre contenido sin backup/match por ID, ni search-replace bruto que
corrompa serialización. Sin acceso prepara import y guía sin declarar persistencia.
