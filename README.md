# 🧰 dev-toolkit-skills

> Repositorio centralizado de **skills** y **prompts** reutilizables para agentes de IA (Claude / Antigravity).  
> Extraídos y depurados desde proyectos reales: portafolio-svelte, TabulaSapiens, tienda-dropshipping, wix, apps Android/desktop.

---

## ¿Qué es esto?

Un repositorio personal de skills de agente organizadas por categoría de stack — **no por proyecto de origen**. Cada skill es un patrón reutilizable que puede activarse en cualquier proyecto futuro que use el mismo stack.

- **Skills** (`skills/`): Carpetas con `SKILL.md` que los agentes cargan automáticamente para tareas específicas.
- **Skills Comprimidas** (`SKILL/`): Paquetes comprimidos (`.zip` y `.skill`) listos para compartir, desplegar o importar bajo demanda (46 archivos = **38 skills únicas**).
- **Prompts** (`prompts/`): Prompts de alto valor para tareas recurrentes (auditoría, documentación, meta-gestión de skills).
- **Docs Index** (`docs_structure.json`): Manifest principal de uso rápido; expone el skill de documentación Qoder (`qoder-wiki`) y el mapa real de documentos disponibles en el repo para cargarlo en proyectos ajenos.

---

## 📂 Estructura

```
dev-toolkit-skills/
├── README.md
├── docs_structure.json        ← índice documental generado desde qoder-wiki/docs
├── skills-lock.json           ← lockfile de skills instaladas
├── SKILL/                     ← Paquetes de skills comprimidos (.zip y .skill) (46 archivos / 38 skills)
├── prompts/
│   ├── meta/          ← Creación, extracción y organización de skills
│   ├── audit/         ← Auditoría de sistemas full-stack
│   └── docs/          ← Mejorar documentación / README
└── skills/
    ├── design/        ← UI/UX, estética, diseño visual (20 skills)
    ├── frontend/      ← React, Tailwind, Vite, SEO (12 skills)
    ├── backend/       ← Supabase, Auth, Monitoring (4 skills)
    ├── automation/    ← Agentes, workflows, browser, release, graphs y video (6 skills)
    ├── platforms/wix/ ← Skills específicas de Wix CLI (7 skills)
    ├── docs-cv/       ← CV/Harvard y ATS (2 skills)
    ├── docs/          ← Documentación general y sincronización (1 skill)
    └── meta/          ← Crear/gestionar skills de agente (4 skills)
```

---

## 🎨 `skills/design/` — UI/UX y Diseño Visual

| Skill             | Cuándo activarla                                                                                                | Stack      |
| ----------------- | --------------------------------------------------------------------------------------------------------------- | ---------- |
| `impeccable`      | Crear interfaces premium, production-grade. Evita estéticas genéricas de IA. Modos: `craft`, `teach`, `extract` | Cualquiera |
| `frontend-design` | Diseño visual distintivo al construir UI nueva. Proceso: brief → plan → crítica → código                        | Cualquiera |
| `ui-ux-pro-max`   | Estilos (50), paletas (21), parejas tipográficas (50), charts (20)                                              | Cualquiera |
| `animate`         | Añadir animaciones, micro-interacciones, motion design                                                          | CSS / JS   |
| `bolder`          | Diseño demasiado seguro/aburrido, necesita más carácter visual                                                  | Cualquiera |
| `colorize`        | UI monocromática, necesita más color y expresión                                                                | CSS        |
| `clarify`         | UX copy confuso, labels poco claros, mensajes de error malos                                                    | Cualquiera |
| `critique`        | Revisar, evaluar o dar feedback sobre un diseño existente                                                       | Cualquiera |
| `delight`         | Añadir polish, personalidad, momentos memorables                                                                | CSS / JS   |
| `distill`         | Simplificar, reducir ruido, hacer UI más limpia y enfocada                                                      | Cualquiera |
| `layout`          | Espaciado incorrecto, jerarquía visual débil, layout confuso                                                    | CSS        |
| `overdrive`       | Shaders, spring physics, animaciones extremas, 60fps                                                            | CSS / JS   |
| `polish`          | Revisión final de calidad antes de publicar                                                                     | Cualquiera |
| `quieter`         | Diseño demasiado agresivo u overwhleming                                                                        | CSS        |
| `typeset`         | Tipografía incorrecta, jerarquía de texto, legibilidad                                                          | CSS        |
| `shape`           | Planear UX/UI antes de codificar (fase discovery)                                                               | Cualquiera |
| `adapt`           | Responsive design, breakpoints, layouts en distintos dispositivos                                               | CSS        |
| `audit`           | Revisión técnica de accesibilidad, performance, anti-patterns                                                   | Cualquiera |
| `optimize`        | UI lenta, laggy, bundle grande, tiempo de carga alto                                                            | JS / CSS   |
| `algorithmic-art` | Arte generativo con p5.js, flow fields, sistemas de partículas                                                  | p5.js      |

---

## ⚛️ `skills/frontend/` — React, Tailwind, Vite, SEO

| Skill                           | Cuándo activarla                                                                 | Stack                |
| ------------------------------- | -------------------------------------------------------------------------------- | -------------------- |
| `react-router-framework-mode`   | Rutas, loaders/actions, SSR/SPA, sessions, error boundaries                      | React Router v7+     |
| `react-frontend`                | Desarrollo frontend con React, buenas prácticas generales                        | React                |
| `react-frontend-expert`         | Patrones avanzados de React, arquitectura de componentes                         | React                |
| `react-2026`                    | Patrones actualizados de React para 2025/2026                                    | React 19+            |
| `frontend-react-best-practices` | Checklist de mejores prácticas en proyectos React                                | React                |
| `frontend-ui-engineering`       | Ingeniería de UI: sistemas de diseño, tokens, componentes                        | React / CSS          |
| `tailwindcss`                   | Cualquier tarea con Tailwind CSS v3/v4                                           | Tailwind             |
| `tailwind-4-docs`               | Documentación y características nuevas de Tailwind v4                            | Tailwind v4          |
| `tailwind-v4-shadcn`            | Integración Tailwind v4 + shadcn/ui                                              | Tailwind v4 + shadcn |
| `tailwind-theme-builder`        | Construir y personalizar temas en Tailwind                                       | Tailwind             |
| `vite`                          | Configuración, plugins, optimización en proyectos Vite                           | Vite                 |
| `seo-sitemap`                   | Auditar y generar sitemap.xml y robots.txt (SvelteKit / dominio cyberdev.qzz.io) | SvelteKit            |

---

## 🗄️ `skills/backend/` — APIs, Auth, Bases de Datos

| Skill                               | Cuándo activarla                                                               | Stack                 |
| ----------------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| `supabase`                          | Cualquier tarea con Supabase: DB, Auth, RLS, Edge Functions, Storage, CLI, MCP | Supabase              |
| `supabase-postgres-best-practices`  | Optimización de queries, schema design, configuración Postgres                 | Supabase / Postgres   |
| `clerk-react-router-patterns`       | Autenticación con Clerk en proyectos React Router                              | Clerk + React Router  |
| `sentry-react-router-framework-sdk` | Integración de Sentry para error monitoring en React Router                    | Sentry + React Router |

---

## 🤖 `skills/automation/` — Agentes, Workflows, Browser, Video

| Skill                     | Cuándo activarla                                                             | Stack           |
| ------------------------- | ---------------------------------------------------------------------------- | --------------- |
| `agent-browser`           | Automatización web: navegación, scraping, formularios, capturas de pantalla  | inference.sh    |
| `agent-ui`                | Componente de chat/agente para React/Next.js con streaming, tools, approvals | React / Next.js |
| `agent-graphs`            | Workflows multi-agente: grafos de configs con handoff logic entre agentes     | LaunchDarkly    |
| `ai-automation-workflows` | Pipelines de IA: batch, scheduled, event-driven, agent loops                 | Python / CLI    |
| `video-editing`           | Edición de video con IA: cortes, vlogs, estructura y pipeline de render      | FFmpeg / Remotion |
| `version-release`         | Versionar y publicar releases: flujo de release y GitHub Release notes        | Git / GitHub    |

---

## 🏗️ `skills/platforms/wix/` — Plataforma Wix (7 skills)

| Skill               | Cuándo activarla                                                                  | Stack    |
| ------------------- | --------------------------------------------------------------------------------- | -------- |
| `wix-app`           | Construir extensiones CLI de Wix: dashboard pages, plugins, widgets, backend APIs | Wix CLI  |
| `wix-auth`          | Obtener access tokens para llamar APIs de Wix                                     | Wix      |
| `wix-design-system` | Componentes de @wix/design-system: props, ejemplos, testkits                      | Wix DS   |
| `wix-docs`          | Buscar documentación oficial de Wix API/SDK antes de escribir código              | Wix      |
| `wix-headless`      | Conectar servicios Wix (Stores, Bookings, CMS) a frontend headless                | Wix SDK  |
| `wix-manage`        | Gestionar soluciones de negocio Wix via REST API                                  | Wix REST |
| `wix-vibe-headless` | Conectar frontend ya construido a Wix via REST puro (sin SDK, sin build step)     | REST     |

> `wix-headless` incluye una **sub-skill anidada**: `wix-headless-entry` en `skills/platforms/wix/wix-headless/entry/skill.md` — punto de entrada en frío que verifica prerequisitos del sistema, login del Wix CLI y luego delega en la skill principal. Por eso `skills/` contiene 57 archivos `SKILL.md` para 56 skills de primer nivel.

---

## 📚 `skills/docs/` — Documentación y Sincronización

| Skill           | Cuándo activarla                                                                                | Stack  |
| --------------- | ----------------------------------------------------------------------------------------------- | ------ |
| `docs-updater`  | Sincronizar docs con el código: diff de git contra el último tag, actualiza README y CHANGELOG (Keep a Changelog) | Git / Markdown |

---

## 💼 `skills/docs-cv/` — Curriculum Vitae (2 skills)

| Skill                | Cuándo activarla                                                                                                                                    | Stack                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `cv-builder-harvard` | Construir o reestructurar un CV con formato Harvard clásico: cabecera, educación, experiencia, actividades, skills, una página y estilo profesional | CV / HR / Portfolio      |
| `cv-harvard-ats`     | Reescribir un CV con orientación a logros cuantificados y optimización ATS: keywords, estructura, diagnóstico y score                               | CV / ATS / Reclutamiento |

Estas dos skills ya forman parte del repositorio real y cuentan con sus referencias embebidas:

- [skills/cv-builder-harvard/SKILL.md](skills/cv-builder-harvard/SKILL.md)
- [skills/cv-builder-harvard/references/action-verbs.md](skills/cv-builder-harvard/references/action-verbs.md)
- [skills/cv-harvard-ats/SKILL.md](skills/cv-harvard-ats/SKILL.md)
- [skills/cv-harvard-ats/references/estructura_harvard.md](skills/cv-harvard-ats/references/estructura_harvard.md)
- [skills/cv-harvard-ats/references/reglas_ats.md](skills/cv-harvard-ats/references/reglas_ats.md)
- [skills/cv-harvard-ats/references/formula_logros.md](skills/cv-harvard-ats/references/formula_logros.md)
- [skills/cv-harvard-ats/references/checklist_dimensiones.md](skills/cv-harvard-ats/references/checklist_dimensiones.md)
- [skills/cv-harvard-ats/references/adaptacion_por_industria.md](skills/cv-harvard-ats/references/adaptacion_por_industria.md)

---

## 🧠 `skills/meta/` — Gestión de Skills

| Skill | Cuándo activarla | Stack |
|---|---|---|
| `skill-creator` | Crear una nueva skill desde cero: entrevista → SKILL.md → casos de prueba | Cualquiera |
| `writing-great-skills` | Fundamentos y guía para escribir skills con buenas descripciones y triggers | Cualquiera |
| `qoder-wiki` | Preguntas sobre Qoder: instalación, funciones, MCP, Skills, precios | Qoder |
| `using-superpowers` | Regla operativa de invocación de skills y carga de context antes de responder | Cualquiera |

---

## 📝 `prompts/` — Prompts de Alto Valor

| Prompt | Propósito | Cuándo usarlo |
|---|---|---|
| `meta/prompt-skill-creator.md` | Guiar a Claude para crear una skill concreta con el proceso completo | Después de identificar una skill candidata |
| `meta/prompt-organizar-skills-repo.md` | Analizar proyectos y extraer skills reutilizables | Al empezar un nuevo proyecto o hacer limpieza |
| `audit/prompt-auditoria.md` | Auditoría full-stack integral: arquitectura, UX, seguridad, rendimiento y operativa | Revisar un sistema completo |
| `docs/prompt-mejorar-readme.md` | Sincronizar README y documentación con cambios de código | Documentar un proyecto |

---

## 🚀 Cómo usar una skill en un proyecto nuevo

### Opción A — Instalar la skill principal desde GitHub

El repo ya está publicado en GitHub y el `json` principal del proyecto está en [docs_structure.json](docs_structure.json). Para usar la skill más útil y específica en otros proyectos, instala el skill documental Qoder:

```bash
# Clonar el repositorio fuente
git clone https://github.com/Adan0423/dev-toolkit-skills.git

# Copiar la skill primaria al proyecto destino
cp -r dev-toolkit-skills/skills/meta/qoder-wiki /tu-proyecto/.agents/skills/qoder-wiki
```

La ruta de instalación recomendada es:

```text
/tu-proyecto/.agents/skills/qoder-wiki/
```

### Opción B — Configurar el repositorio como fuente global de skills

En tu archivo de configuración del agente, añade este repo como fuente de skills:

```json
{
  "skillsPath": [
    "C:/Users/TRINIDAD/Downloads/proyectos/dev-toolkit-skills/skills"
  ]
}
```

### Opción C — Consumir el JSON principal

El archivo [docs_structure.json](docs_structure.json) funciona como manifest de uso rápido:

```json
{
  "primarySkill": "qoder-wiki",
  "source": {
    "repo": "dev-toolkit-skills",
    "skillPath": "skills/meta/qoder-wiki",
    "installPath": ".agents/skills/qoder-wiki"
  }
}
```

---

## 📦 `SKILL/` — Paquetes de Skills Comprimidos (.zip / .skill)

El directorio [`SKILL/`](SKILL/) alberga **46 archivos comprimidos** (`.zip` y `.skill`) que contienen **38 skills únicas**. Están optimizados para ser transportados, compartidos o importados de manera atómica en agentes y entornos de desarrollo.

- 🆕 **14 skills nuevas** añadidas desde la última versión de este README
- 💠 Varios skills existen en **ambos formatos** (`.skill` + `.zip`) — elige el que prefieras
- ⚠️ `humanizer.zip` está **roto** (solo contiene `meta.json`); usa `humanizer-2.9.1.zip`

### 📄 Documentos y Archivos (4)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `pdf.zip` | `pdf` | `.zip` (22.2 KB) | Manipulación integral de archivos PDF (extracción, OCR, unión, rotación, formularios, cifrado). |
| `pptx.zip` | `pptx` | `.zip` (167.7 KB) | Creación, edición, extracción y formateo de presentaciones en PowerPoint (.pptx / .potx). |
| `word-document-tools.zip` | `word-document-tools` | `.zip` (250.2 KB) | Creación, lectura, edición y manipulación de documentos de Microsoft Word (.docx / .dotx). |
| `xlsx.zip` | `xlsx` | `.zip` (155.7 KB) | Procesamiento completo de hojas de cálculo (.xlsx, .csv, .tsv), fórmulas, gráficos y limpieza de datos. |

### 📝 Documentación y Escritura (6)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `doc-coauthoring.zip` | `doc-coauthoring` | `.zip` (6.0 KB) | Workflow estructurado para co-autoría y redacción colaborativa de documentación técnica. |
| `documentation-repository-curator.skill` | `documentation-repository-curator` | `.skill` (15.4 KB) | 🆕 Auditar el stack real, rediseñar README, consolidar docs duplicadas e identificar archivos obsoletos. |
| `documentation-repository-curator.zip` | `documentation-repository-curator` | `.zip` (15.4 KB) | 🆕 Misma skill en formato zip. |
| `humanizer-2.9.1.zip` | `humanizer` | `.zip` (23.9 KB) | 🆕 Eliminar marcas de escritura generada por IA (símbolos inflados, lenguaje promocional, em dash, regla de tres, pasiva). |
| `humanizer.zip` | `humanizer` | `.zip` (2.1 KB) | ⚠️ **Roto** — solo contiene `meta.json`. Usa `humanizer-2.9.1.zip`. |
| `project-readme-documentation.skill` | `project-readme-documentation` | `.skill` (5.4 KB) | Análisis de repositorios reales y generación/mejora de README.md basada en evidencias. |

### 🎓 Currículum Vitae (2)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `cv-harvard-ats.skill` | `cv-harvard-ats` | `.skill` (13.1 KB) | Creación, redacción y auditoría de CVs estilo Harvard optimizados para sistemas ATS. |
| `cv-harvard-ats.zip` | `cv-harvard-ats` | `.zip` (13.8 KB) | Misma skill en formato zip, con `references/` completas. |

### 🎨 Design, Frontend y UI (11)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `adaptive-web-ui-stack-architect.skill` | `adaptive-web-ui-stack-architect` | `.skill` (14.9 KB) | 🆕 Analizar el proyecto **antes** de elegir UI libs, motor CSS, primitivas headless, iconos, animación y design system. |
| `adaptive-web-ui-stack-architect.zip` | `adaptive-web-ui-stack-architect` | `.zip` (14.9 KB) | 🆕 Misma skill en formato zip, con `scripts/` y 8 `references/`. |
| `brand-guidelines.zip` | `brand-guidelines` | `.zip` (5.5 KB) | Aplica guías de marca oficiales de Anthropic, tipografías y paletas a cualquier artefacto. |
| `canvas-design.zip` | `canvas-design` | `.zip` (2.59 MB) | Filosofía y creación de diseño visual artístico en PNG y PDF. |
| `frontend-design.zip` | `frontend-design` | `.zip` (7.8 KB) | Dirección estética distintiva e intencional al construir o rediseñar interfaces UI. |
| `tailwindcss-v4-3-expert.skill` | `tailwindcss-v4-3-expert` | `.skill` (14.6 KB) | 🆕 Analizar, instalar, actualizar y validar interfaces con Tailwind v4.3 (plugin `@tailwindcss/vite`, CSS-first, container queries, theming). |
| `tailwindcss-v4-3-expert.zip` | `tailwindcss-v4-3-expert` | `.zip` (19.0 KB) | 🆕 Misma skill en formato zip. |
| `theme-factory.zip` | `theme-factory` | `.zip` (121.8 KB) | Motor de temas (10 presets) para aplicar a slides, reportes, landing pages y artefactos HTML. |
| `web-artifacts-builder.zip` | `web-artifacts-builder` | `.zip` (30.2 KB) | Suite para construir artefactos HTML complejos multi-componente con React, Tailwind CSS y shadcn/ui. |
| `web-ui-ux-frontend-architect.skill` | `web-ui-ux-frontend-architect` | `.skill` (15.3 KB) | 🆕 Analizar, diseñar, modernizar e implementar UI/UX web (Design-first/Code-first/Hybrid) con QA responsive, visual y de accesibilidad. |
| `web-ui-ux-frontend-architect.zip` | `web-ui-ux-frontend-architect` | `.zip` (15.3 KB) | 🆕 Misma skill en formato zip. |

### 🪟 Aplicaciones de Escritorio (2)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `windows-desktop-ui-ux-engineer.skill` | `windows-desktop-ui-ux-engineer` | `.skill` (19.0 KB) | 🆕 UI/UX para desktop en Windows: WinUI 3, WPF, WinForms, .NET MAUI, Electron, Tauri, Qt/QML. |
| `windows-desktop-ui-ux-engineer.zip` | `windows-desktop-ui-ux-engineer` | `.zip` (19.0 KB) | 🆕 Misma skill en formato zip. |

### 🏗️ Arquitectura, Datos y APIs (7)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `llm-api-development.zip` | `llm-api-development` | `.zip` (320.6 KB) | Desarrollo con Anthropic SDK y Claude API (streaming, tool use, MCP, prompt caching, tokens). |
| `mcp-builder.zip` | `mcp-builder` | `.zip` (42.6 KB) | Guía y desarrollo de servidores MCP (Model Context Protocol) en Python (FastMCP) y Node/TypeScript. |
| `modern-software-architect.skill` | `modern-software-architect` | `.skill` (16.4 KB) | 🆕 Analizar, diseñar, reorganizar y modernizar arquitecturas: código limpio, escalabilidad proporcional, limpieza de repositorio. |
| `modern-software-architect.zip` | `modern-software-architect` | `.zip` (16.4 KB) | 🆕 Misma skill en formato zip. |
| `scalable-database-architect.skill` | `scalable-database-architect` | `.skill` (13.1 KB) | 🆕 Diseñar, auditar y optimizar BDs escalables: relacional vs NoSQL, índices, particiones, RLS/RBAC, pooling. |
| `scalable-database-architect.zip` | `scalable-database-architect` | `.zip` (13.1 KB) | 🆕 Misma skill en formato zip. |
| `software-project-architect-skill.zip` | `software-project-architect` | `.zip` (7.8 KB) | Arquitectura global de proyectos de software, estructuras limpias, monolitos, microservicios y monorepos. |

### 🔐 Auditoría, Seguridad y Corrección (4)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `android-codebase-auditor-refactor.zip` | `android-codebase-auditor-refactor` | `.zip` (15.4 KB) | 🆕 Auditar repos Android/Kotlin: deuda técnica, God Classes, almacenamiento inseguro, acoplamiento UI-data. Modo AUDIT read-only primero. |
| `secure-software-auditor.skill` | `secure-software-auditor` | `.skill` (9.8 KB) | 🆕 Auditoría defensiva de seguridad (OWASP) en web, APIs, backend, móvil y desktop, con priorización de riesgos. |
| `secure-software-auditor.zip` | `secure-software-auditor` | `.zip` (9.8 KB) | 🆕 Misma skill en formato zip. |
| `system-correction-skill-pack.zip` | `system-correction-orchestrator` + 3 correctoras | `.zip` (15.4 KB) | 🆕 **Pack de 4 skills**: orquestador de corrección end-to-end, `rbac-database-corrector`, `mcp-integration-corrector`, `role-aware-ui-corrector`. |

### 🤖 Android y Móvil (5)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `android-camera-engineering.skill` | `android-camera-engineering` | `.skill` (9.3 KB) | 🆕 Apps de cámara Android: CameraX, Camera2, HDR, RAW, modo noche, fotografía computacional y UI de cámara. |
| `android-modern-ui-expert.zip` | `android-modern-ui-expert` | `.zip` (14.1 KB) | 🆕 Kotlin/Compose, Material 3 Expressive, layouts adaptativos, dark mode, edge-to-edge, Navigation 3, KMP. |
| `android-modern-ui-expert-install-ready.zip` | `android-modern-ui-expert` | `.zip` (14.7 KB) | 🆕 Misma skill con rutas ya resueltas en `.agents/skills/` para instalar directamente. |
| `mobile-app-engineering.skill` | `mobile-app-engineering` | `.skill` (5.4 KB) | Desarrollo móvil profesional para Expo / React Native, Android nativo (Kotlin/Compose) y KMP. |
| `scrcpy-mobile-dev.zip` | `scrcpy-mobile-dev` | `.zip` (9.2 KB) | 🆕 Usar scrcpy + ADB de forma segura y reproducible en Windows: detectar target, espejo por USB/Wi-Fi, diagnosticar errores. |

### 🧪 Agentes, Testing y Media (5)

| Paquete | Skill Name | Formato / Tamaño | Cuándo activarla / Descripción |
|---|---|---|---|
| `algorithmic-art.zip` | `algorithmic-art` | `.zip` (19.4 KB) | Arte algorítmico y generativo con p5.js, flow fields y sistemas de partículas. |
| `internal-comms.zip` | `internal-comms` | `.zip` (10.6 KB) | Redacción de comunicaciones internas corporativas (status reports, updates, FAQs, incident reports). |
| `skill-creator.skill` | `skill-creator` | `.skill` (72.0 KB) | Creación, edición, evals y optimización de descripciones para skills de agente de IA. |
| `slack-gif-creator.zip` | `slack-gif-creator` | `.zip` (16.3 KB) | Creación de GIFs animados optimizados para Slack con restricciones de tamaño y paleta. |
| `webapp-testing.zip` | `webapp-testing` | `.zip` (10.3 KB) | Pruebas de aplicaciones web locales con Playwright, capturas de pantalla y logs de navegador. |

---

## 📋 Convención para añadir una nueva skill

1. Crea la carpeta en la categoría correcta: `skills/<categoria>/<nombre-en-kebab-case>/`
2. Crea `SKILL.md` con frontmatter obligatorio:
   ```yaml
   ---
   name: nombre-en-kebab-case
   description: "Qué hace + cuándo se activa (triggers específicos, no vagos)"
   ---
   ```
3. El `name` va en kebab-case, en inglés, **sin mencionar el proyecto de origen**
4. La `description` debe ser "insistente": triggers concretos, no "úsalo cuando...necesites"
5. Si hay código reutilizable real, va en `scripts/` — no pegado en el body del SKILL.md
6. Si la documentación supera 500 líneas, muévela a `references/` con tabla de contenidos
7. Añade la skill a la tabla correspondiente en este README

---

## 📊 Estadísticas

### Skills descomprimidas (`skills/`)

| Categoría | Skills |
|---|---|
| design | 20 |
| frontend | 12 |
| backend | 4 |
| automation | 6 |
| platforms/wix | 7 |
| docs-cv | 2 |
| docs | 1 |
| meta | 4 |
| **Total skills descomprimidas** | **56** |
| Sub-skill anidada (`wix-headless-entry`) | 1 |

### Paquetes comprimidos (`SKILL/`)

| Métrica | Total |
|---|---|
| Archivos `.skill` | 13 |
| Archivos `.zip` | 33 |
| **Total archivos** | **46** |
| Skills únicas (desduplicando ambos formatos) | 38 |
| Skills nuevas desde la última actualización | 14 |
| `system-correction-skill-pack` contiene | 4 skills |

### Otros

| Métrica | Total |
|---|---|
| **Total prompts** | **4** |
| **Total skills únicas del repo** (descomprimidas + comprimidas) | **94** |

---

## 📌 Notas

- **Skills NO eliminadas de sus proyectos de origen** — este repo es una copia centralizada
- **`tabulasapiens-developer`** excluida: muy project-specific (sleep cycles, neural network)
- **`seo-sitemap`** tiene contexto específico de `cyberdev.qzz.io` — adaptar dominio al usarla en outro proyecto
- Skills de React con posible solapamiento (`react-frontend`, `react-frontend-expert`, `react-2026`) se conservan todas — cada una tiene matices diferentes en profundidad y casos de uso
- **Duplicados por formato**: 9 skills existen como `.skill` y `.zip` a la vez (`adaptive-web-ui-stack-architect`, `cv-harvard-ats`, `documentation-repository-curator`, `modern-software-architect`, `scalable-database-architect`, `secure-software-auditor`, `tailwindcss-v4-3-expert`, `web-ui-ux-frontend-architect`, `windows-desktop-ui-ux-engineer`). Preferir `.skill` (formato nativo de agente) salvo que necesites distribuir el `.zip`
- **`humanizer.zip` está corrupto** (2.1 KB, solo contiene `meta.json`) — eliminarlo o regenerarlo desde `humanizer-2.9.1.zip`
- **Solapamiento entre skills de arquitectura**: `software-project-architect`, `modern-software-architect` y `frontend-ui-engineering` cubren territorio similar con distinta profundidad y alcance
- **Nuevo bloque Android/móvil** (5 skills en `SKILL/`): `android-camera-engineering`, `android-modern-ui-expert` (2 variantes de formato), `android-codebase-auditor-refactor`, `scrcpy-mobile-dev`
- **Idioma mixto**: varias skills nuevas están redactadas en español (`android-camera-engineering`, `android-codebase-auditor-refactor`, `modern-software-architect`, `scalable-database-architect`, `secure-software-auditor`, `web-ui-ux-frontend-architect`, `windows-desktop-ui-ux-engineer`, `system-correction-*`); el naming de las carpetas sigue en inglés
