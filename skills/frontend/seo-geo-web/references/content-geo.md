# Estrategia de contenido y GEO

## Contenido y negocio

Define cliente, país/idioma, conversión y páginas actuales. Investiga intención
informativa/comercial/transaccional/navegacional con consultas reales. No inventes
volumen ni dificultad. Mapea intención → página → valor → evidencia → conversión.
Resuelve canibalización conservando URLs valiosas. Clusters y enlaces contextuales
deben servir al lector, sin imponer densidad, cantidad de palabras o frecuencia.
Prioriza procesos reales, límites, comparaciones comprobables, ejemplos propios,
autores responsables y fuentes pertinentes. No alteres fechas para aparentar frescura.
Revisa contenido IA antes de publicar; en temas sensibles requiere revisión competente.

E-commerce: categorías, detalles completos, imágenes y stock real, entrega/devolución.
Decide agotados/retirados según permanencia y sustituto. Local: identidad, dirección,
teléfono, horario y zona reales; no inventes sedes/páginas clonadas por ciudad.
Perfiles y feeds requieren datos/acceso. Para autoridad externa propone recursos o
colaboraciones; no contactes terceros ni compres enlaces sin autorización aplicable.

## GEO: hechos e hipótesis

Google mantiene fundamentos SEO sin archivos ni schema especiales obligatorios para
sus funciones IA. Elegibilidad para enlace de apoyo exige indexación y snippet;
restricciones como noindex/nosnippet pueden afectar visibilidad. No confundas el
control de Googlebot en Search con Google-Extended en otros usos.
Respuestas claras, contexto, fuentes y entidades consistentes son recomendaciones
editoriales; efecto en citas de un motor es hipótesis a medir. No presentes tamaños
de párrafo, número de citas ni FAQ como fórmula garantizada.
Llms.txt: experimento opcional si se solicita o justifica, con coste y comprobación;
no requisito de lanzamiento, no exportar privados, no instrucciones manipulativas.

## Bots y política del propietario

| Proveedor | Finalidades a comprobar en fuente oficial |
|---|---|
| OpenAI | OAI-SearchBot búsqueda; GPTBot posible entrenamiento; ChatGPT-User acciones de usuarios |
| Google | Googlebot Search; Google-Extended usos definidos en documentación |
| Anthropic | Claude-SearchBot, ClaudeBot y Claude-User tienen usos distintos |
| Perplexity | PerplexityBot y Perplexity-User tienen comportamientos distintos |

Verifica user-agents/IP oficiales antes de WAF. Simular user-agent no demuestra visita
auténtica. No desactives seguridad/paywalls ni abras privados. Conserva decisión de
entrenamiento: búsqueda no obliga a permitir GPTBot. Inspecciona precedencia de grupos
robots, no reemplaces todo el archivo con una plantilla permisiva.

## Schema pertinente

Escoge entidad real (Organization/LocalBusiness, Article, Product, BreadcrumbList,
etc.) y requisitos vigentes. FAQ visible puede ayudar, sin prometer rich results a
todos: revisa elegibilidad actual. Schema.org válido no equivale a elegibilidad Google.
No inventes precio, aggregateRating ni datos de autor para rellenar campos.

## Medición GEO

Define consultas, idioma/región, motor/modelo, fecha, búsqueda activada y repeticiones
comparables. Diferencia mención de marca de enlace/cita, registra URL y exactitud.
No extrapoles muestra pequeña a cuota global ni correlación a causalidad. Conserva
evidencia cuando términos del servicio lo permitan. Cruza referentes/conversiones;
hay tráfico sin referente y resultados variables. Verifica informes actuales de
Search Console/Bing antes de prometer segmentación IA; compara periodos y contexto.

Fuentes: [Google IA](https://developers.google.com/search/docs/appearance/ai-features),
[OpenAI bots](https://developers.openai.com/api/docs/bots),
[Anthropic](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler),
[Perplexity](https://docs.perplexity.ai/docs/resources/perplexity-crawlers),
[schema](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
