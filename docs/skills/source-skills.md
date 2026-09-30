# Skills Fuente para Desarrollo y Pruebas (`skills/`)


[Paletas profesionales: nueva skill y guía de uso](color-palettes.md).

> **110 skills únicas**, contando todos los SKILL.md y especialistas anidados.
> Estas son el **código fuente**: úsalas para **desarrollar, probar, debuggear y mejorar** skills. Para instalar en producción, prefiere los paquetes de [`SKILL/`](skill-packages.md).
> [Inventario y revisión individual actuales](organization-review.md). Las tablas detalladas antiguas conservan el catálogo histórico; la recuperación y las nuevas categorías están en el inventario enlazado.

Consulta las [siete familias selectivas](family-skills.md) y su proceso de actualización.

[Marketing profesional: nuevas skills y ejemplos](marketing-skills.md).

[Nueva skill de bases de datos y seguridad](database-engineering.md).

## Cuándo usar esta carpeta

Adición del 30 de septiembre de 2026:
[`odoo-specialist`](../../skills/platforms/odoo/odoo-specialist/SKILL.md), en
`skills/platforms/odoo/`. Desarrollo/configuración Odoo, permisos y multiempresa,
UI, procesos ERP, importaciones, integración y migración según versión/hosting.
Posterior a los totales históricos del catálogo.

Adición del 30 de septiembre de 2026:
[`wordpress-elementor-commerce`](../../skills/platforms/wordpress/wordpress-elementor-commerce/SKILL.md),
en `skills/platforms/wordpress/`. Elementor/WooCommerce/plugins, diseño moderno editable,
responsive, dark mode, contenido/productos y MCP según capacidades. Posterior a los
totales históricos de este catálogo.

Adición del 30 de septiembre de 2026:
[`wordpress-theme-studio`](../../skills/platforms/wordpress/wordpress-theme-studio/SKILL.md),
en `skills/platforms/wordpress/`. Temas con código, skills de diseño, responsive,
claro/oscuro/sistema, contenido/configuración y acceso MCP/REST/CLI. Posterior a los
totales históricos del catálogo.

Adición del 30 de septiembre de 2026: [`seo-geo-web`](../../skills/frontend/seo-geo-web/SKILL.md),
en `skills/frontend/`. Incluye SEO técnico y editorial, estructura para desarrollo,
adaptación por stack/CMS, GEO, migraciones, validación y plan de auditoría. Esta adición
es posterior a los totales históricos que figuran en el catálogo.

| Objetivo | Carpeta |
|---|---|
| Usar una skill en un proyecto (instalar) | `SKILL/` |
| Modificar / mejorar una skill (contribuir) | `skills/` |
| Entender cómo está implementada una skill | `skills/` |
| Probar / debuggear una skill | `skills/` |

---

## 🎨 `skills/design/` — UI/UX y Diseño Visual (20)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `impeccable` | Interfaces premium production-grade; evita estéticas genéricas de IA. Modos: `craft`, `teach`, `extract` | Diseño de alto nivel, teaching, extracción de patrones | Cualquiera |
| `frontend-design` | Diseño visual distintivo al construir UI. Brief → plan → crítica → código | Dirección estética, no templates | Cualquiera |
| `ui-ux-pro-max` | Estilos (50), paletas (21), parejas tipográficas (50), charts (20) | Referencia amplia de sistemas de diseño | Cualquiera |
| `animate` | Animaciones, micro-interacciones, motion design | CSS/JS motion | CSS / JS |
| `bolder` | Cuando el diseño es demasiado seguro/aburrido | Más carácter visual | Cualquiera |
| `colorize` | UI monocromática → más color y expresión | Paletas, contraste | CSS |
| `clarify` | UX copy confuso, labels, mensajes de error | copywriting de UI | Cualquiera |
| `critique` | Evaluar / dar feedback sobre un diseño existente | Review de diseño | Cualquiera |
| `delight` | Polish, personalidad, momentos memorables | Detalles de delight | CSS / JS |
| `distill` | Simplificar, reducir ruido, UI más enfocada | Reducción de complejidad | Cualquiera |
| `layout` | Espaciado, jerarquía visual, layout confuso | Sistema de espaciado | CSS |
| `overdrive` | Shaders, spring physics, animaciones extremas, 60fps | Motion avanzado | CSS / JS |
| `polish` | Revisión final de calidad antes de publicar | QA visual | Cualquiera |
| `quieter` | Diseño demasiado agresivo/overwhelming | Reducir ruido visual | CSS |
| `typeset` | Tipografía, jerarquía de texto, legibilidad | Sistema tipográfico | CSS |
| `shape` | Planear UX/UI antes de codificar (discovery) | Wireframes, flujos | Cualquiera |
| `adapt` | Responsive design, breakpoints, distintos dispositivos | Adaptación | CSS |
| `audit` | Revisión técnica de accesibilidad, performance, anti-patterns | Auditoría técnica | Cualquiera |
| `optimize` | UI lenta, laggy, bundle grande, carga alta | Performance | JS / CSS |
| `algorithmic-art` | Arte generativo con p5.js, flow fields, partículas | Arte algorithmic | p5.js |

## ⚛️ `skills/frontend/` — React, Tailwind, Vite, SEO (12)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `react-router-framework-mode` | Rutas, loaders/actions, SSR/SPA, sessions, error boundaries | Routing moderno | React Router v7+ |
| `react-frontend` | Desarrollo frontend React, buenas prácticas generales | Fundamentos React | React |
| `react-frontend-expert` | Patrones avanzados, arquitectura de componentes | Avanzado | React |
| `react-2026` | Patrones actualizados React 2025/2026 | Modernización | React 19+ |
| `frontend-react-best-practices` | Checklist de mejores prácticas en proyectos React | Revisión | React |
| `frontend-ui-engineering` | Ingeniería de UI: design systems, tokens, componentes | Arquitecto UI | React / CSS |
| `tailwindcss` | Cualquier tarea con Tailwind v3/v4 | Utilidades, config | Tailwind |
| `tailwind-4-docs` | Documentación y características nuevas de Tailwind v4 | Referencia v4 | Tailwind v4 |
| `tailwind-v4-shadcn` | Integración Tailwind v4 + shadcn/ui | Integración | Tailwind v4 + shadcn |
| `tailwind-theme-builder` | Construir/personalizar temas en Tailwind | Temas | Tailwind |
| `vite` | Configuración, plugins, optimización en proyectos Vite | Tooling | Vite |
| `seo-sitemap` | Auditar/generar sitemap.xml y robots.txt | SEO técnico | SvelteKit |

## 🗄️ `skills/backend/` — APIs, Auth, Bases de Datos (4)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `supabase` | Cualquier tarea con Supabase: DB, Auth, RLS, Edge Functions, Storage, CLI, MCP | Plataforma completa | Supabase |
| `supabase-postgres-best-practices` | Optimización de queries, schema design, Postgres | Performance y diseño | Supabase / Postgres |
| `clerk-react-router-patterns` | Autenticación con Clerk en React Router | Auth | Clerk + React Router |
| `sentry-react-router-framework-sdk` | Sentry para error monitoring en React Router | Observabilidad | Sentry + React Router |

## 🤖 `skills/automation/` — Agentes, Workflows, Video (6)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `agent-browser` | Automatización web: navegación, scraping, formularios, capturas | Browser automation | inference.sh |
| `agent-ui` | Componente de chat/agente para React/Next con streaming, tools, approvals | UI de agentes | React / Next.js |
| `agent-graphs` | Workflows multi-agente: grafos de configs con handoff logic | Orquestación multi-agente | LaunchDarkly |
| `ai-automation-workflows` | Pipelines de IA: batch, scheduled, event-driven, agent loops | Automatización | Python / CLI |
| `video-editing` | Edición de video con IA: cortes, vlogs, estructura, render | Pipeline de video | FFmpeg / Remotion |
| `version-release` | Versionar y publicar releases; flujo de release y GitHub Release notes | Release automation | Git / GitHub |

## 🏗️ `skills/platforms/wix/` — Plataforma Wix (7)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `wix-app` | Construir extensiones CLI de Wix: dashboard pages, plugins, widgets, APIs backend | Extensiones | Wix CLI |
| `wix-auth` | Obtener access tokens para llamar APIs de Wix | Autenticación | Wix |
| `wix-design-system` | Componentes de @wix/design-system: props, ejemplos, testkits | Design system | Wix DS |
| `wix-docs` | Buscar documentación oficial de Wix API/SDK antes de escribir código | Documentación | Wix |
| `wix-headless` | Conectar servicios Wix (Stores, Bookings, CMS) a frontend headless | Headless | Wix SDK |
| `wix-headless-entry` *(anidada)* | Punto de entrada en frío: verifica prerequisitos, login del CLI, delega en la skill principal | Bootstrap | Wix CLI |
| `wix-manage` | Gestionar soluciones de negocio Wix via REST API | Administración | Wix REST |
| `wix-vibe-headless` | Conectar frontend ya construido a Wix via REST puro (sin SDK, sin build) | Integración | REST |

> `wix-headless-entry` vive en `skills/platforms/wix/wix-headless/entry/skill.md` (sub-skill anidada).

## 📚 `skills/docs/` — Documentación (1)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `docs-updater` | Sincronizar docs con código: diff de git contra el último tag, actualiza README y CHANGELOG (Keep a Changelog) | Automatización de docs | Git / Markdown |

## 💼 `skills/docs-cv/` — Currículum Vitae (2)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `cv-builder-harvard` | Construir/reestructurar un CV con formato Harvard clásico: cabecera, educación, experiencia, actividades, skills | Formatting CV | CV / HR / Portfolio |
| `cv-harvard-ats` | Reescribir CV con logros cuantificados y optimización ATS: keywords, estructura, score | Optimización ATS | CV / ATS |

## 🧠 `skills/meta/` — Gestión de Skills (4)

| Skill | ¿Qué hace? | Funciones | Entornos |
|---|---|---|---|
| `skill-creator` | Crear una skill desde cero: entrevista → SKILL.md → casos de prueba | Autoría de skills | Cualquiera |
| `writing-great-skills` | Fundamentos para escribir skills con buenas descripciones y triggers | Fundamentos | Cualquiera |
| `qoder-wiki` | Preguntas sobre Qoder: instalación, funciones, MCP, Skills, precios | Documentación Qoder | Qoder |
| `using-superpowers` | Regla operativa de invocación de skills y carga de contexto antes de responder | Meta-operación | Cualquiera |

---

## Referencias Embebidas

Algunas skills incluyen `references/` con documentación detallada (ej. `cv-harvard-ats/references/reglas_ats.md`). Consulta esos archivos para guía profunda.
