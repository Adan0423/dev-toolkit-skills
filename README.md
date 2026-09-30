# 🧰 dev-toolkit-skills

> Toolkit personal de **skills**, **paquetes** y **prompts** reutilizables para agentes de IA.
> Extraídos y depurados desde proyectos reales: portafolio-svelte, TabulaSapiens, tienda-dropshipping, wix, apps Android/desktop.

[![skills](https://img.shields.io/badge/skills-94-blue?style=flat-square)](docs/skills/skill-packages.md)
[![packages](https://img.shields.io/badge/SKILL%2F-46%20paquetes-purple?style=flat-square)](SKILL/)
[![source](https://img.shields.io/badge/skills%2F-56%20fuente-green?style=flat-square)](skills/)
[![prompts](https://img.shields.io/badge/prompts-4-orange?style=flat-square)](prompts/)

---

## 🎯 ¿Qué es esto?

Un repositorio de skills de agente organizadas **por categoría de stack**, no por proyecto de origen. Cada skill es un patrón reutilizable que se activa en cualquier proyecto futuro con el mismo stack.

### 📦 Las dos capas del repo

| Capa | Carpeta | Estado | Para qué |
| :--- | :--- | :--- | :--- |
| 🎁 **Paquetes** | [`SKILL/`](SKILL/) | ✅ **Listos para usar** | Instalar directo en tu agente. Formato `.skill` o `.zip`. **Sin compilación.** |
| 🛠️ **Fuente** | [`skills/`](skills/) | 🔧 **Desarrollo / pruebas** | Modificar, mejorar, debuggear. Código fuente con `SKILL.md` + referencias. |
| 💬 **Prompts** | [`prompts/`](prompts/) | ✅ **Listos para usar** | Plantillas reutilizables (meta, auditoría, docs). |

> 💡 **En una línea:** usa `SKILL/` en el día a día; usa `skills/` cuando quieras mejorar una skill o ver cómo está hecha.

---

## 🚀 Instalación Rápida

```bash
# 1. Clonar
git clone https://github.com/Adan0423/dev-toolkit-skills.git

# 2. Instalar un paquete .skill (formato nativo)
cp -r dev-toolkit-skills/SKILL/skill-creator.skill /tu-proyecto/.agents/skills/skill-creator.skill

# 2'. O descomprimir un .zip
unzip dev-toolkit-skills/SKILL/pdf.zip -d /tu-proyecto/.agents/skills/pdf
```

📖 **[Guía completa de instalación →](docs/install/quickstart.md)**

<details>
<summary><b>⚡ Opción rápida: usar el repo como fuente global de skills</b></summary>

```json
{
  "skillsPath": [
    "C:/Users/TRINIDAD/Downloads/proyectos/dev-toolkit-skills/SKILL",
    "C:/Users/TRINIDAD/Downloads/proyectos/dev-toolkit-skills/skills"
  ]
}
```

</details>

---

## 🧠 Activar una Skill

Todas las skills se activan **por nombre o por descripción** (triggers). Ejemplos:

```text
"Usa skill-creator para crear una skill de auditoría de APIs"
"Aplica adaptive-web-ui-stack-architect antes de elegir librería de UI"
"Humaniza este texto para que no suene a IA"
```

La mayoría se dispara automáticamente por los **triggers** definidos en su `description`.

---

## 📚 Documentación

| Documento | Contenido |
|---|---|
| 📖 **[Guía de Instalación](docs/install/quickstart.md)** | Instalación, formatos, uso, verificación |
| 📋 **[Índice de Documentación](docs/INDEX.md)** | Mapa completo de la documentación |
| 🎁 **[Paquetes `SKILL/`](docs/skills/skill-packages.md)** | 45 paquetes · qué hace, funciones, casos de uso, entornos |
| 🛠️ **[Skills fuente `skills/`](docs/skills/source-skills.md)** | 56 skills · desarrollo, pruebas, referencias |
| 💬 **[Prompts](docs/prompts/README.md)** | 4 prompts reutilizables |
| 🗂️ **[docs_structure.json](docs_structure.json)** | Índice documental para cargar en otros proyectos |

---

## 🎁 Paquetes Listos para Usar (`SKILL/`)

**45 paquetes** = **38 skills únicas** (`.skill` + `.zip`, sin compilación).

| Categoría | Paquetes | Descripción | Documentación |
|---|:---:|---|---|
| 📄 Documentos y Archivos | 4 | PDF, Word, PowerPoint, Excel | [Ver →](docs/skills/skill-packages.md) |
| 📝 Documentación y Escritura | 5 | Coautoría, curador de repo, humanizar texto, README | [Ver →](docs/skills/skill-packages.md) |
| 🎓 Currículum Vitae | 2 | CV Harvard + optimización ATS | [Ver →](docs/skills/skill-packages.md) |
| 🎨 Design, Frontend y UI | 11 | Arquitecto UI, Tailwind v4.3, temas, artefactos web | [Ver →](docs/skills/skill-packages.md) |
| 🪟 Escritorio (Windows) | 2 | UI/UX para WinUI/WPF/Electron/Tauri/Qt | [Ver →](docs/skills/skill-packages.md) |
| 🏗️ Arquitectura y Datos | 7 | Claude API, MCP, arquitectura, BDs escalables | [Ver →](docs/skills/skill-packages.md) |
| 🔐 Seguridad y Corrección | 4 | OWASP, auditoría Android, pack de corrección | [Ver →](docs/skills/skill-packages.md) |
| 🤖 Android y Móvil | 5 | Cámara, UI moderna, scrcpy, ingeniería móvil | [Ver →](docs/skills/skill-packages.md) |
| 🧪 Agentes, Testing y Media | 5 | skill-creator, testing web, GIFs, arte generativo | [Ver →](docs/skills/skill-packages.md) |

> ℹ️ `humanizer.zip` (corrupto) fue eliminado del repo. La versión vigente es **`humanizer-2.9.1.zip`**.

### Skills destacadas

| Skill | Descripción corta | Entornos |
|---|---|---|
| [`skill-creator`](SKILL/skill-creator.skill) | Crear, editar y **optimizar** skills con evals | Cualquiera |
| [`adaptive-web-ui-stack-architect`](SKILL/adaptive-web-ui-stack-architect.zip) | Analiza el proyecto **antes** de elegir stack UI | Web |
| [`secure-software-auditor`](SKILL/secure-software-auditor.zip) | Auditoría de seguridad defensiva (OWASP) | Web, API, móvil, desktop |
| [`modern-software-architect`](SKILL/modern-software-architect.zip) | Arquitectura limpia, escala proporcional, limpieza | Multi-lenguaje |
| [`scalable-database-architect`](SKILL/scalable-database-architect.zip) | BDs escalables: modela, indexa, asegura | PostgreSQL, MySQL, NoSQL |
| [`system-correction-skill-pack`](SKILL/system-correction-skill-pack.zip) | Diagnostica y corrige bugs end-to-end (4 skills) | Web, API, móvil, desktop |
| [`android-modern-ui-expert`](SKILL/android-modern-ui-expert.zip) | UI Android moderna: Compose, Material 3 | Android (Kotlin) |
| [`humanizer`](SKILL/humanizer-2.9.1.zip) | Elimina "olor a IA" del texto | Cualquiera |
| [`web-ui-ux-frontend-architect`](SKILL/web-ui-ux-frontend-architect.zip) | Arquitecto UI/UX web completo con QA | Multi-framework |
| [`mcp-builder`](SKILL/mcp-builder.zip) | Construye servidores MCP (Python/TS) | Python, Node/TS |

📖 **[Ver las 46 con detalle (qué hace, funciones, casos de uso) →](docs/skills/skill-packages.md)**

---

## 🛠️ Skills Fuente (`skills/`) — Desarrollo y Pruebas

**56 skills** de primer nivel (+1 sub-skill) con `SKILL.md`, `references/` y `scripts/`.

| Categoría | Skills | Descripción |
|---|:---:|---|
| 🎨 `design/` | 20 | UI/UX, estética, motion, tipografía, auditorías |
| ⚛️ `frontend/` | 12 | React, Tailwind, Vite, SEO, routing |
| 🗄️ `backend/` | 4 | Supabase, Postgres, Clerk, Sentry |
| 🤖 `automation/` | 6 | Agentes, browser, video, release, workflows |
| 🏗️ `platforms/wix/` | 7 | Extensiones, auth, headless, design system |
| 💼 `docs-cv/` | 2 | CV Harvard + ATS |
| 📚 `docs/` | 1 | Sincronización de documentación |
| 🧠 `meta/` | 4 | Crear y gestionar skills |

📖 **[Ver las 56 con detalle →](docs/skills/source-skills.md)**

---

## 💬 Prompts (`prompts/`)

4 prompts reutilizables listos para copiar/pegar en cualquier agente:

| Prompt | Para qué | Cuándo |
|---|---|---|
| `meta/prompt-skill-creator.md` | Crear una skill paso a paso | Al identificar una skill candidata |
| `meta/prompt-organizar-skills-repo.md` | Extraer skills de proyectos | Limpieza o nuevo proyecto |
| `audit/prompt-auditoria.md` | Auditoría full-stack (arquitectura, UX, seguridad, performance) | Revisar un sistema completo |
| `docs/prompt-mejorar-readme.md` | Sincronizar README con el código | Documentar un proyecto |

📖 **[Ver los 4 prompts en detalle →](docs/prompts/README.md)**

---

## 📊 Estadísticas

<details open>
<summary><b>Resumen</b></summary>

| Métrica | Total |
|---|:---:|
| 📦 Paquetes en `SKILL/` | 45 (13 `.skill` + 32 `.zip`) |
| 🎁 Skills únicas en `SKILL/` | 38 |
| 🛠️ Skills de primer nivel en `skills/` | 56 (+1 sub-skill) |
| 💬 Prompts | 4 |
| **Total skills únicas del repo** | **94** |
| 🆕 Skills añadidas en la última actualización | 14 |

</details>

### Skills descomprimidas por categoría

| Categoría | Skills |
|---|:---:|
| design | 20 |
| frontend | 12 |
| backend | 4 |
| automation | 6 |
| platforms/wix | 7 |
| docs-cv | 2 |
| docs | 1 |
| meta | 4 |
| **Total** | **56** |

---

## 📋 Convenciones

Al añadir una skill:

1. Carpeta en la categoría correcta: `skills/<categoria>/<nombre-kebab-case>/`
2. `SKILL.md` con frontmatter:
   ```yaml
   ---
   name: nombre-en-kebab-case
   description: "Qué hace + cuándo se activa (triggers concretos)"
   ---
   ```
3. `name` en kebab-case, inglés, **sin mencionar el proyecto de origen**
4. `description` "insistente": triggers concretos, no vagas
5. Código reutilizable → `scripts/`, no en el body
6. Documentación >500 líneas → `references/` con índice
7. Añadir a la tabla correspondiente del README
8. Empaquetar en `SKILL/` (`.skill` y/o `.zip`) cuando esté lista para producción

---

## 📌 Notas

- **Skills NO eliminadas de sus proyectos de origen** — este repo es una copia centralizada
- **`tabulasapiens-developer`** excluida: muy project-specific (sleep cycles, neural network)
- **`seo-sitemap`** tiene contexto específico de `cyberdev.qzz.io` — adaptar dominio
- **9 skills duplicadas** en `.skill` + `.zip` — preferir `.skill` para instalar
- **`humanizer.zip` eliminado** por estar corrupto — usar `humanizer-2.9.1.zip`
- **Solapamiento de arquitectura** entre `software-project-architect`, `modern-software-architect` y `frontend-ui-engineering` (distinta profundidad/alcance)
- **Bloque Android/móvil** nuevo (5 skills): cámara, UI moderna, auditoría, scrcpy
- **Idioma mixto**: varias skills nuevas en español; el naming de carpetas sigue en inglés

---

<div align="center">

**[⬆ Volver arriba](#-dev-toolkit-skills)**

Hecho con 🧰 para construir agentes más capaces

</div>
