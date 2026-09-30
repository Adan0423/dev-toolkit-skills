# Adaptación por lenguaje y framework

Identifica versión, router y renderizado antes de elegir API. Consulta documentación
oficial de esa versión. Estos son puntos de integración, no código universal.

| Stack | Intervención habitual | Atención |
|---|---|---|
| HTML/CSS/JS, PHP | Head de plantillas y servidor | No duplicar head ni devolver 200 a inexistentes |
| Next.js/React | Metadata API en App Router; head/SSR en Pages Router | Diferenciar routers y revisar salida/streaming según versión |
| React Router/Remix | Meta de rutas, loaders y respuestas | Estado de error real y datos antes del head |
| Vite React/Vue SPA | Router, head manager y despliegue | index.html compartido no produce HTML inicial por registro |
| Nuxt/Vue | useSeoMeta/useHead, Nitro según versión | SSR/SSG/híbrido y contenido dinámico |
| SvelteKit | svelte:head, load servidor, endpoints | Metadata por datos, status y sitemap |
| Astro | Layouts/head, colecciones y endpoints | Rutas estáticas/dinámicas y regeneración |
| Angular | Title/Meta, SSR/prerender oficial | Versión de SSR e hidratación pública |
| Laravel/Symfony | Blade/Twig, controladores/middleware | Escape, dominio y paginación |
| Django/Flask/FastAPI | Templates/contexto, vistas/respuestas | Una API sola no sustituye HTML público |
| Rails | Layouts/helpers/controllers | Estado, canonical y caché |
| ASP.NET Core/C# | Razor/MVC y middleware | En Blazor comprobar renderizado real |
| Spring Boot/Java | Thymeleaf/vistas y controladores | Separar API, páginas y errores proxy |
| Go/Rust/Elixir | Templates, handlers, router/Plug | Escape, estado y dominio público |
| Hugo/Jekyll/Eleventy/SSG | Plantillas, colecciones y build | Preview, borradores y lastmod |
| CMS headless | Frontend público y webhooks | Slug/locale/publicación e invalidación coherente |

Para cualquier lenguaje no listado, identifica HTTP, plantillas, routing y despliegue
y aplica engineering.md. No atribuyas incompatibilidad SEO al lenguaje. APIs, apps
nativas y paneles privados no necesitan páginas SEO por cada pantalla: trabaja sobre
su sitio público.

Google puede renderizar JS; otros consumidores difieren. Compara HTML inicial y DOM,
enlaces, recursos bloqueados, fetch e hidratación. Para contenido público importante
evalúa SSR/SSG/prerender si falta contenido rastreable: coste, hosting y frescura.
No declares todos los SPA invisibles ni migres automáticamente. Evita cloaking.

```text
resolver ruta → cargar registro publicado → ausente: 404
→ derivar metadata/schema → entregar HTML
→ sitemap usando la misma regla de publicación
```

Comprueba dos detalles distintos y slug ausente: metadata variable y error real.
Cuando aporte valor, añade controles CI de host preview, XML/JSON, indexabilidad y
enlaces críticos. Evalúa invariantes reales, no snapshots del texto editorial.

Fuente: [Google JS SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics).
