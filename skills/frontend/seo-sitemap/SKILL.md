---
name: seo-sitemap
description: >
  Audita, genera y corrige sitemap.xml y robots.txt para proyectos SvelteKit.
  Detecta errores de Google Search Console (URL no permitida, formato no compatible),
  genera rutas dinamicas correctas, valida dominios canonicals y actualiza archivos
  estaticos y rutas de servidor. Usalo cuando el usuario mencione sitemap, robots.txt,
  Search Console, SEO, indexacion, URLs no permitidas, o crawling.
personas: [seo-specialist, web-developer, information-architect]
---

# SEO Sitemap & Robots.txt Skill

Este skill gestiona sitemap.xml y robots.txt para el portafolio SvelteKit desplegado en **cyberdev.qzz.io**.

---

## Contexto del Proyecto

| Propiedad | Valor |
|---|---|
| **Dominio canonico** | `https://cyberdev.qzz.io` |
| **Dominio antiguo (Cloudflare Pages)** | `https://portafolio-svelte.pages.dev` - NUNCA usar en sitemap |
| **Sitemap estatico** | `static/sitemap.xml` (fallback) |
| **Sitemap dinamico** | `src/routes/sitemap.xml/+server.ts` (preferido) |
| **Robots estatico** | `static/robots.txt` (fallback) |
| **Robots dinamico** | `src/routes/robots.txt/+server.ts` (preferido) |

---

## Errores Conocidos de Google Search Console

### ERROR: "URL no permitida"
Causa: El sitemap contiene URLs de un dominio diferente al dominio verificado.
Regla: Todas las <loc> deben usar SOLO https://cyberdev.qzz.io/...

### ERROR: "Formato de archivo no compatible" (robots.txt)
Directivas invalidas que Google rechaza:
- Request-rate: -> NO valida segun spec de Google
- Crawl-delay: fuera de un bloque User-agent: -> invalida

---

## Workflow

### Paso 1: Auditoria

Leer estos archivos:
- static/sitemap.xml
- static/robots.txt
- src/routes/sitemap.xml/+server.ts
- src/routes/robots.txt/+server.ts

Verificar:
- Todas las <loc> usan https://cyberdev.qzz.io
- No hay URLs de portafolio-svelte.pages.dev
- robots.txt no contiene Request-rate:
- robots.txt no tiene Crawl-delay: global (fuera de User-agent)
- Sitemap: apunta a https://cyberdev.qzz.io/sitemap.xml

### Paso 2: Rutas publicas del sitemap

Rutas que SI deben estar en el sitemap:
  /               priority: 1.0  changefreq: weekly
  /about          priority: 0.8  changefreq: monthly
  /servicios      priority: 0.8  changefreq: monthly
  /proyectos      priority: 0.9  changefreq: weekly
  /blog           priority: 0.9  changefreq: weekly
  /contacto       priority: 0.7  changefreq: monthly
  /privacy        priority: 0.3  changefreq: yearly
  /terms          priority: 0.3  changefreq: yearly
  /proyectos/:slug  priority: 0.8  changefreq: monthly (dinamico desde Supabase)
  /blog/:slug     priority: 0.7  changefreq: weekly   (dinamico desde Supabase)

Rutas que NO deben estar en el sitemap:
  /buscar, /admin, /dashboard, /editor, /super-admin
  /auth, /login, /logout, /register
  /api/*, /profile, /settings, /configuracion
  /notifications, /favorites

### Paso 3: robots.txt valido para Google

PERMITIDO:
  User-agent, Allow, Disallow, Crawl-delay (dentro de bloque User-agent), Sitemap

PROHIBIDO incluir:
  Request-rate: (no es directiva estandar de Google)
  Crawl-delay: fuera de un bloque User-agent:

### Paso 4: Verificacion post-fix

1. Confirmar que static/sitemap.xml no tiene URLs de portafolio-svelte.pages.dev
2. Confirmar que static/robots.txt no tiene Request-rate: ni Crawl-delay: global
3. Sugerir reenviar sitemap en Google Search Console (Sitemaps > Reenviar)
4. Sugerir usar "Inspeccionar URL" en Search Console para validar paginas clave

---

## Referencias

- https://support.google.com/webmasters/answer/7451001#error_list
- https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt
- https://www.sitemaps.org/protocol.html
- https://github.com/dandye/information-architecture/blob/main/skills/sitemap-generate/SKILL.md
