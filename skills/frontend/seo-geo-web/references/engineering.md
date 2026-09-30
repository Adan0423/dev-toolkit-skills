# Arquitectura SEO desde desarrollo

## Contrato y estructura

Centraliza título, descripción, URL canónica, idioma, indexabilidad, imagen social y
entidad. Deriva datos del contenido real y dominio público configurado, no de un Host
sin validar. Separa borradores y privados. Plantillas, sitemap, enlaces y schema deben
compartir política de publicación.

Estructura conceptual; adapta responsabilidades a las convenciones existentes:

```text
config/site                 dominio público, idiomas, identidad
content o modelos CMS       slug, título, resumen, cuerpo, autor, fechas, estado
seo/metadata                normalización y head por ruta
seo/schema                  serialización de entidades verificadas
seo/indexability            publicación y exclusión
routes/templates            HTML, navegación y estado HTTP
public o endpoints          robots.txt, sitemap.xml, imágenes
redirects                   mapa de migración versionado
checks                      comprobaciones relevantes en build/CI
```

No impongas carpetas. Ejemplo conceptual de datos por página:

```json
{"path":"/servicios/auditoria-web/","title":"Auditoría web | Marca",
 "description":"Describe el servicio real y su alcance.","locale":"es-PE",
 "published":true,"indexable":true,"schemaType":"Service"}
```

## HTTP e indexación

Contenido válido: 200. Cambios permanentes: 301/308 a equivalente. Inexistentes: 404/410,
también en SPA. Evita errores con 200, cadenas/bucles y redirigir todo al inicio.
Diagnostica 401/403/429/5xx, WAF, CDN, caché y timeouts antes de cambiar textos.
Excluye HTML con meta robots noindex; otros recursos mediante X-Robots-Tag si procede.
Permite rastreo para detectar noindex. Revisa restricciones combinadas en meta/cabeceras.
Protege staging con autenticación; no heredarlo en producción. Robots no protege datos.

## Canonical y variantes

Coherencia entre HTTPS, host y barras. Una canonical absoluta representativa por página
indexable; es una señal, no orden ni sustituto de redirects. No canonicalizar todo al
inicio ni combinar noindex con canonical a otra página para consolidar señales.
Clasifica tracking, búsqueda, filtros, ordenación y variantes; indexa combinaciones
solo si aportan demanda/contenido propio. Evita espacios infinitos de URLs.
Paginación útil: enlaces reales y canonical propia, no todas a página uno.
Infinite scroll debe permitir URLs rastreables. Usa a href, no solo eventos JS.
Idiomas: versiones reales, hreflang recíproco/autorreferente, códigos válidos,
x-default cuando proceda y canonical del mismo idioma. No ocultes versiones por IP.

## Sitemap y robots

URLs absolutas, públicas, canónicas e indexables, normalmente 200; sin borradores,
sesiones, redirects o búsquedas sin valor. XML escapado y UTF-8. Divide sobre 50.000
URLs o 50 MB sin comprimir, con índice si procede. Lastmod refleja cambios sustanciales,
no cada build. Google ignora priority/changefreq. Sitemap facilita descubrimiento,
no obliga a indexar. Comprueba alcance por host y no reemplaces generadores activos.
Sirve robots.txt como texto en raíz, con sitemap real. Evalúa grupos específicos antes
de editar. No uses noindex en robots ni Crawl-delay esperando soporte de Google.

## HTML y schema

Títulos/resúmenes específicos por ruta, sin límites de caracteres presentados como ley.
Headings lógicos y encabezado principal claro; varios H1 no implican penalización.
Usa semántica y breadcrumbs pertinentes. Alt informativo; decorativas con alt vacío.
OG/tarjetas sociales ayudan a compartir, sin prometer ranking.
Schema: tipos reales, @id estable y requisitos vigentes del resultado objetivo.
Evita entidades duplicadas. Serializa JSON, no concatentes entradas no confiables;
escapa `<` como `\u003c` en scripts JSON-LD para impedir cierre de script inyectado.
Lo marcado debe corresponder al contenido visible y actualizado.

## Rendimiento

Optimiza imágenes/dimensiones, reserva espacio, evita lazy loading de LCP por defecto,
reduce JS/terceros y revisa fuentes/caché. Objetivos CWV de campo al percentil 75:
LCP ≤2,5 s, INP ≤200 ms, CLS ≤0,1; segmenta móvil/escritorio. Lighthouse no prueba
estas métricas de campo ni garantiza posiciones.

Fuentes: [canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls),
[robots](https://developers.google.com/search/docs/crawling-indexing/robots/intro),
[sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap),
[idiomas](https://developers.google.com/search/docs/specialty/international/localized-versions),
[schema](https://developers.google.com/search/docs/appearance/structured-data/sd-policies),
[CWV](https://web.dev/articles/vitals).
