# 🧰 dev-toolkit-skills

> Toolkit personal de **skills**, **paquetes** y **prompts** reutilizables para agentes de IA.
> Extraídos y depurados desde proyectos reales: portafolio-svelte, TabulaSapiens, tienda-dropshipping, wix, apps Android/desktop.

[![skills](https://img.shields.io/badge/skills-109-blue?style=flat-square)](docs/skills/skill-packages.md)
[![packages](https://img.shields.io/badge/SKILL%2F-63%20paquetes-purple?style=flat-square)](SKILL/)
[![source](https://img.shields.io/badge/skills%2F-109%20fuente-green?style=flat-square)](skills/)
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

## Familias con carga selectiva

Siete entradas principales reúnen 34 especialidades: marketing, React, Tailwind,
diseño web, documentación, WordPress y CV. Cada una carga la guía necesaria para la tarea.
[Ver familias, paquetes y mantenimiento](docs/skills/family-skills.md).

## Marketing, contenido y publicidad

[marketing-growth-suite](skills/marketing/marketing-growth-suite/SKILL.md) selecciona
estrategia, contenido, Meta Ads, Google Ads, TikTok Ads o medición. Incluye ideas, copy,
guiones, campañas, optimización y uso de MCP compatible cuando esté disponible.
[Ver las siete skills, paquetes y ejemplos](docs/skills/marketing-skills.md).

## Modelado y seguridad de bases de datos

[database-engineering-suite](skills/architecture/database-engineering-suite/SKILL.md)
modela SQL/NoSQL, genera esquemas y migraciones, revisa integridad/rendimiento y permisos
de tablas, filas y columnas, con MCP compatible cuando esté conectado.
[Guía, fuentes y paquete](docs/skills/database-engineering.md).

## 🧠 Activar una Skill

### Especialista Odoo

[`odoo-specialist`](skills/platforms/odoo/odoo-specialist/SKILL.md) analiza instalaciones,
desarrolla addons, configura procesos ERP, diagnostica errores y trabaja con permisos,
multiempresa, UI/Website, importaciones, APIs y migraciones. Adapta soluciones a versión,
Community/Enterprise y Online/Odoo.sh/on-premise; utiliza MCP si existe y es compatible.

Paquete: [`odoo-specialist.zip`](SKILL/odoo-specialist.zip). Extrae la carpeta del skill
en el directorio admitido por tu agente. Este ZIP contiene instrucciones para el agente;
no es un addon instalable en Odoo.

```text
Usa $odoo-specialist para analizar esta instalación y resolver la tarea según su versión, edición, permisos y procesos.
```

### WordPress con Elementor, WooCommerce y plugins

[`wordpress-elementor-commerce`](skills/platforms/wordpress/wordpress-elementor-commerce/SKILL.md)
crea diseños modernos editables con Elementor, tiendas WooCommerce y plugins pertinentes.
Incluye responsive móvil/tablet/desktop, modo claro/oscuro/sistema, artículos, medios,
productos y configuración. Usa MCP Elementor/WordPress cuando sus capacidades reales
resuelven la tarea, con alternativas editor/REST/CLI y validación de compra sin cobros reales.

Paquete: [`wordpress-elementor-commerce.zip`](SKILL/wordpress-elementor-commerce.zip).
Extrae la carpeta del skill en el directorio admitido por tu agente; no es un plugin
para subir al administrador de WordPress.

```text
Usa $wordpress-elementor-commerce para mejorar este sitio con Elementor y WooCommerce, diseño responsive, modo oscuro y artículos editables.
```

### WordPress: temas con código y contenido

[`wordpress-theme-studio`](skills/platforms/wordpress/wordpress-theme-studio/SKILL.md)
crea temas clásicos o de bloques con código propio, integra skills de diseño y exige
validación responsive, accesibilidad y modo claro/oscuro/sistema. Gestiona artículos,
medios y configuración mediante MCP, REST, WP-CLI o administrador según acceso.

Paquete: [`wordpress-theme-studio.zip`](SKILL/wordpress-theme-studio.zip). Extrae la
carpeta `wordpress-theme-studio` en el directorio de skills admitido por tu agente.

```text
Usa $wordpress-theme-studio y el skill de diseño disponible para crear un tema WordPress responsive con modo oscuro y artículos editables.
```

Este archivo ZIP instala el skill; el tema WordPress se genera al ejecutar una tarea.

### SEO y GEO profesional

Nueva skill: [`seo-geo-web`](skills/frontend/seo-geo-web/SKILL.md).
Audita e implementa SEO técnico, estructura del código, contenido, datos estructurados,
rendimiento y visibilidad en búsquedas con IA. Se adapta a cualquier stack web e incluye
WordPress, Wix y guías para otros CMS. Si falta acceso, prepara cambios e instrucciones
comprobables. Fuentes oficiales y límites de GEO documentados; no promete rankings.

Paquete: [`seo-geo-web.zip`](SKILL/seo-geo-web.zip). Extrae la carpeta `seo-geo-web`
en el directorio de skills admitido por tu agente (por ejemplo, `~/.codex/skills/`).

```text
Usa $seo-geo-web para analizar este proyecto e implementar SEO y GEO desde el código.
```

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
| 🎁 **[Paquetes `SKILL/`](docs/skills/skill-packages.md)** | 63 paquetes · qué hace, funciones, casos de uso, entornos |
| 🛠️ **[Skills fuente `skills/`](docs/skills/source-skills.md)** | 109 skills · desarrollo, pruebas, referencias |
| 💬 **[Prompts](docs/prompts/README.md)** | 4 prompts reutilizables |
| 🗂️ **[docs_structure.json](docs_structure.json)** | Índice documental para cargar en otros proyectos |

---

## 🎁 Paquetes Listos para Usar (`SKILL/`)

**63 paquetes** = **56 nombres de skill** (13 `.skill` y 50 `.zip`).

| Categoría fuente | Paquetes |
|---|:---:|
| `architecture/` | 6 |
| `automation/` | 2 |
| `design/` | 11 |
| `desktop/` | 2 |
| `docs/` | 7 |
| `docs-cv/` | 3 |
| `documents/` | 4 |
| `frontend/` | 5 |
| `integrations/` | 2 |
| `marketing/` | 7 |
| `meta/` | 1 |
| `mobile/` | 5 |
| `platforms/` | 4 |
| `quality/` | 2 |
| `security/` | 2 |

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

📖 **[Ver los 63 paquetes con detalle (qué hace, funciones, casos de uso) →](docs/skills/skill-packages.md)**

---

## 🛠️ Skills Fuente (`skills/`) — Desarrollo y Pruebas

**109 skills únicas**, contando todos los `SKILL.md` y especialistas anidados.

| Categoría | Skills |
|---|:---:|
| `architecture/` | 4 |
| `automation/` | 8 |
| `backend/` | 4 |
| `design/` | 27 |
| `desktop/` | 1 |
| `docs/` | 7 |
| `docs-cv/` | 3 |
| `documents/` | 4 |
| `frontend/` | 16 |
| `integrations/` | 2 |
| `marketing/` | 7 |
| `meta/` | 4 |
| `mobile/` | 4 |
| `platforms/` | 12 |
| `quality/` | 5 |
| `security/` | 1 |

📖 **[Ver las 109 con detalle →](docs/skills/source-skills.md)**

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
| 📦 Paquetes en `SKILL/` | 63 (13 `.skill` + 50 `.zip`) |
| 🎁 Nombres de skill en `SKILL/` | 56 |
| 🛠️ Skills únicas en `skills/` (incluye especialistas anidados) | 109 |
| 💬 Prompts | 4 |
| **Total nombres únicos del repo** | **109** |
| 🆕 Skills recuperadas de paquetes en esta auditoría | 34 |

</details>

### Recuperación y mejora

Se recuperaron las fuentes que faltaban sin sobrescribir las existentes. Las variantes
distintas están en `docs/skills/package-variants/`, fuera de las fuentes activas.

- [Auditoría y propuesta de agrupación](docs/skills/organization-review.md): revisión individual de las 95 skills anteriores.
- [Inventario actualizado](docs/skills/source-reconciliation.json) y [recuperación inicial](docs/skills/source-recovery.json).
- [Herramienta de recuperación](scripts/sync_skill_sources.py): auditoría por defecto, extracción con `--extract-missing`.

La recuperación conserva contenido; no certifica vigencia o funcionamiento de cada skill.

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
4. `description` precisa: propósito y casos de uso, sin activación universal
5. Código reutilizable → `scripts/`, no en el body
6. Detalles por modo → `references/`, cargadas solo cuando sean pertinentes
7. Añadir a la tabla correspondiente del README
8. Empaquetar en `SKILL/` (`.skill` y/o `.zip`) cuando esté lista para producción

---

## 📌 Notas

- **Skills NO eliminadas de sus proyectos de origen** — este repo es una copia centralizada
- **`tabulasapiens-developer`** excluida: muy project-specific (sleep cycles, neural network)
- **`seo-sitemap`** tiene contexto específico de `cyberdev.qzz.io` — adaptar dominio
- **Variantes de paquetes**: no elegir por extensión; comparar contenido con la fuente y el manifiesto
- **`humanizer.zip` eliminado** por estar corrupto — usar `humanizer-2.9.1.zip`
- **Solapamiento de arquitectura** entre `software-project-architect`, `modern-software-architect` y `frontend-ui-engineering` (distinta profundidad/alcance)
- **Bloque Android/móvil** nuevo (5 skills): cámara, UI moderna, auditoría, scrcpy
- **Idioma mixto**: varias skills nuevas en español; el naming de carpetas sigue en inglés

---

<div align="center">

**[⬆ Volver arriba](#-dev-toolkit-skills)**

Hecho con 🧰 para construir agentes más capaces

</div>
