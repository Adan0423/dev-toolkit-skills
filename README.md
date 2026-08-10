# 🧰 dev-toolkit-skills

> Repositorio centralizado de **skills** y **prompts** reutilizables para agentes de IA (Claude / Antigravity).  
> Extraídos y depurados desde proyectos reales: portafolio-svelte, TabulaSapiens, tienda-dropshipping, wix.

---

## ¿Qué es esto?

Un repositorio personal de skills de agente organizadas por categoría de stack — **no por proyecto de origen**. Cada skill es un patrón reutilizable que puede activarse en cualquier proyecto futuro que use el mismo stack.

- **Skills** (`skills/`): Carpetas con `SKILL.md` que los agentes cargan automáticamente para tareas específicas.
- **Prompts** (`prompts/`): Prompts de alto valor para tareas recurrentes (auditoría, documentación, meta-gestión de skills).
- **Docs Index** (`docs_structure.json`): Manifest principal de uso rápido; expone el skill de documentación Qoder (`qoder-wiki`) y el mapa real de documentos disponibles en el repo para cargarlo en proyectos ajenos.

---

## 📂 Estructura

```
dev-toolkit-skills/
├── README.md
├── docs_structure.json        ← índice documental generado desde qoder-wiki/docs
├── prompts/
│   ├── meta/          ← Creación, extracción y organización de skills
│   ├── audit/         ← Auditoría de sistemas full-stack
│   └── docs/          ← Mejorar documentación / README
└── skills/
    ├── design/        ← UI/UX, estética, diseño visual (20 skills)
    ├── frontend/      ← React, Tailwind, Vite, SEO (12 skills)
    ├── backend/       ← Supabase, Auth, Monitoring (4 skills)
    ├── automation/    ← Agentes, workflows, browser, release y edición (6 skills)
    ├── platforms/wix/ ← Skills específicas de Wix CLI (8 skills)
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

## 🤖 `skills/automation/` — Agentes, Workflows, Browser

| Skill                     | Cuándo activarla                                                             | Stack           |
| ------------------------- | ---------------------------------------------------------------------------- | --------------- |
| `agent-browser`           | Automatización web: navegación, scraping, formularios, capturas de pantalla  | inference.sh    |
| `agent-ui`                | Componente de chat/agente para React/Next.js con streaming, tools, approvals | React / Next.js |
| `ai-automation-workflows` | Pipelines de IA: batch, scheduled, event-driven, agent loops                 | Python / CLI    |

---

## 🏗️ `skills/platforms/wix/` — Plataforma Wix

| Skill               | Cuándo activarla                                                                  | Stack    |
| ------------------- | --------------------------------------------------------------------------------- | -------- |
| `wix-app`           | Construir extensiones CLI de Wix: dashboard pages, plugins, widgets, backend APIs | Wix CLI  |
| `wix-auth`          | Obtener access tokens para llamar APIs de Wix                                     | Wix      |
| `wix-design-system` | Componentes de @wix/design-system: props, ejemplos, testkits                      | Wix DS   |
| `wix-docs`          | Buscar documentación oficial de Wix API/SDK antes de escribir código              | Wix      |
| `wix-headless`      | Conectar servicios Wix (Stores, Bookings, CMS) a frontend headless                | Wix SDK  |
| `wix-manage`        | Gestionar soluciones de negocio Wix via REST API                                  | Wix REST |
| `wix-vibe-headless` | Conectar frontend ya construido a Wix via REST puro (sin SDK, sin build step)     | REST     |

---

## 💼 `skills/cv-builder-harvard` + `skills/cv-harvard-ats` — Curriculum Vitae

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
git clone https://github.com/<tu-usuario>/dev-toolkit-skills.git

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

### Opción D — Referenciar el SKILL.md directamente

Pega el contenido del SKILL.md como instrucciones en tu sesión de agente.

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

| Categoría | Skills |
|---|---|
| design | 20 |
| frontend | 12 |
| backend | 4 |
| automation | 6 |
| platforms/wix | 8 |
| docs-cv | 2 |
| docs | 1 |
| meta | 4 |
| **Total skills** | **57** |
| **Total prompts** | **4** |

---

## 📌 Notas

- **Skills NO eliminadas de sus proyectos de origen** — este repo es una copia centralizada
- **`tabulasapiens-developer`** excluida: muy project-specific (sleep cycles, neural network)
- **`seo-sitemap`** tiene contexto específico de `cyberdev.qzz.io` — adaptar dominio al usarla en otro proyecto
- Skills de React con posible solapamiento (`react-frontend`, `react-frontend-expert`, `react-2026`) se conservan todas — cada una tiene matices diferentes en profundidad y casos de uso
