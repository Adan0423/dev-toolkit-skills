# Validación, migración y seguimiento

Muestrea por plantilla: inicio, categoría, dos detalles, artículo, conversión,
inexistente y variantes pertinentes. Amplía según riesgo. Usa contenido real sin
exponer datos privados. Herramientas según disponibilidad: cliente HTTP, navegador,
parsers XML/JSON, Rich Results Test, Schema Markup Validator y URL Inspection.

| Control | Evidencia de aceptación |
|---|---|
| HTTP | Estado/destino correcto; inexistente 404 real |
| HTML/DOM | Head por ruta, texto útil, enlaces e hidratación correcta |
| Canonical/robots | Dominio/ruta/idioma y entorno coherentes; sin preview |
| Sitemap | XML parseable, URLs públicas correctas, límites/lastmod |
| Schema | JSON válido, verdad visible y requisitos del tipo |
| Navegación | Breadcrumbs, enlaces, paginación y destinos antiguos |
| Rendimiento | Laboratorio/campo separados, móvil/escritorio |
| Negocio | Contacto, registro, carrito/pago afectados funcionan |

URL Inspection exige propiedad accesible: separa prueba en vivo del estado indexado.
200, búsqueda site: y curl con Googlebot no prueban indexación ni acceso auténtico.
Declara qué no se verificó si faltan acceso/herramientas.

## Migración

Inventaría URLs, destinos, visitas/conversiones y enlaces valiosos. Prepara mapa uno
a uno, redirects permanentes, canonical, hreflang, enlaces, sitemap y analítica.
Elimina bloqueos de staging al publicar. Si incluye dominio, revisa DNS/CDN/certificado.
No borres páginas con tráfico sin estudiar sustituto. Guarda configuración/reversión;
prueba muestras y bucles. Monitorea errores/indexación/conversiones, sin garantizar
ausencia de fluctuaciones.

## Métricas y próximos controles

Baseline: fechas, país/dispositivo, marca/no marca y fuente. SEO: consultas, páginas,
impresiones, clics, CTR, indexación y conversiones. Técnica: errores, schema, CWV.
GEO: muestra de citas/menciones y referencias con límites de content-geo.md.
No inventes números faltantes ni porcentajes de SEO completo que mezclen ranking y código.
Revisión técnica tras publicación y controles 30/60/90 días son calendario orientativo,
no plazo garantizado. Ajusta a volumen/rastreo y estacionalidad; no crees automatizaciones
sin solicitud. Documenta hipótesis, cohortes y cambios simultáneos.

Search Console/Bing: verifica propiedad mediante métodos disponibles, prepara sitemap
y envíalo si autorizado. IndexNow notifica cambios a motores participantes, sin
garantizar indexación. Comprueba integración CMS, clave/host, eventos y respuesta.
No uses Indexing API Google para cualquier URL: verifica tipos admitidos vigentes.

Entrega estados: confirmado, implementado, verificado localmente, publicado, pendiente
de acceso, pendiente del motor o hipótesis. Cada bloqueo debe tener acción, responsable,
datos necesarios y aceptación concreta.
