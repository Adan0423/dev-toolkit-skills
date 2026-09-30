# WordPress, Wix y plataformas administradas

Identifica versión, modalidad, plan, editor, extensiones y permisos. Inspecciona quién
genera title/canonical/robots/schema/sitemap. La salida publicada decide si funciona.

## WordPress

Revisa Ajustes → Lectura, visibilidad, Enlaces permanentes y portada. Comprueba sitemap
core `/wp-sitemap.xml` o el real del plugin activo. WordPress.com y autohospedado tienen
capacidades distintas. Si existe Yoast, Rank Math u otro gestor, reutilízalo: no
instales otro que duplique metadatos. Evalúa mantenimiento, capacidades y coste.
Configura títulos/resúmenes por tipo; archivos de autor/fecha, taxonomías y adjuntos
según valor real, sin noindex global. Cambiar permalinks requiere mapa de redirects.
Para código, usa hooks del gestor o plugin propio/tema hijo, nunca core/tema padre.
Usa wp_json_encode, escape y controles de capacidades. Evita title/canonical manual
si ya los genera otro mecanismo. WooCommerce: revisa precio, stock, variantes, ofertas,
schema y breadcrumbs existentes. Purga caché autorizada y verifica como visitante.

Fuentes: [SEO](https://wordpress.org/documentation/article/search-engine-optimization/),
[core sitemap](https://developer.wordpress.org/reference/classes/wp_sitemaps/),
[WordPress.com](https://developer.wordpress.com/docs/platform-features/sitemaps/).

## Wix

Usa ajustes por página/tipo para título, descripción, indexabilidad y canonical;
consulta editor actual para localizar controles. Prueba variables CMS en dos registros
dinámicos. Inspecciona marcado predeterminado antes de añadir schema. Gestiona slugs,
redirects, robots/sitemap y conexiones con motores mediante funciones disponibles.
No trates Wix como servidor Apache ni afirmes acceso a archivos internos.
Editor, Studio, Velo y headless no comparten necesariamente APIs: consulta documentación
vigente. El CMS no garantiza el SEO de un frontend externo. Guardar y publicar son
estados distintos. Sin acceso entrega página/tipo → campo → valor → comprobación;
incluye contenido/schema revisable sin inventar funciones de un plan.

Fuentes: [ajustes Wix](https://support.wix.com/en/article/customizing-your-seo-settings-1420929),
[funciones](https://www.wix.com/seo/features).

## Otros CMS y builders

| Plataforma | Lugar a investigar | Riesgo/límite |
|---|---|---|
| Shopify | Recursos, Liquid, redirects y sitemap administrado | Tema/apps duplicando schema, filtros y variantes |
| Webflow | SEO página/proyecto, CMS, redirects, custom code | Plan, publicación y salida de colecciones |
| Squarespace | Títulos, SEO, slugs, redirects | Código personalizado depende del plan |
| Drupal | Entidades/rutas y módulos activos | Versión y caché, módulos redundantes |
| Joomla | Menús, artículos, plantilla y extensiones | URLs SEF/rewrite y canonical |
| Otro CMS | Campos, plantillas, sitemap y redirects | Separar editable, administrado y no disponible |

Esta tabla orienta investigación, no certifica capacidades actuales. Consulta ayuda
oficial antes de recomendar APIs/opciones. Si la plataforma limita HTTP/HTML, explica
efecto y alternativa soportada. Migración solo con limitación material y coste/beneficio.
