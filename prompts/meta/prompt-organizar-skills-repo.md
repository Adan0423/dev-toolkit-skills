# Prompt: Extraer y organizar skills desde mis proyectos

Úsalo cuando quieras que Claude analice uno o varios proyectos tuyos y extraiga
skills reutilizables para tu repositorio `claude-skills` (o el nombre que hayas
elegido).

---

## PROMPT

```
Actúa como un arquitecto de conocimiento técnico. Vas a analizar el/los
proyecto(s) que te comparto (código, documentación, prompts sueltos,
decisiones de diseño) y extraer de ahí SKILLS reutilizables para mi
repositorio personal de skills de Claude.

CONTEXTO SOBRE MÍ:
- Full Stack Developer freelance
- Stack principal: PHP, WordPress, JavaScript/Node, React, Next.js,
  TypeScript, Supabase, Python, VBA/Excel, Git
- Tipos de trabajo recurrentes: desarrollo frontend, integración de APIs
  externas (ej. Aliclik, Insforge), automatización en Excel/VBA, diseño de
  portafolios/CV, documentación técnica, pitches para clientes freelance

REGLA PRINCIPAL — GLOBAL PERO DEPENDIENTE DEL STACK:
Ninguna skill debe quedar atada a un proyecto específico (ej. "aliclik-store"
o "portfolio-supabase" NO son nombres válidos de skill). En cambio, cada
skill debe capturar el PATRÓN reutilizable detrás del stack/tecnología, de
forma que sirva en cualquier proyecto futuro que use ese mismo stack.

Ejemplo de la diferencia:
- ❌ Mal: "skill para el catálogo de Aliclik"
- ✅ Bien: "skill para integrar y consumir APIs REST externas con manejo de
  mock/producción" (nace del proyecto Aliclik, pero sirve para cualquier
  integración de API futura)

- ❌ Mal: "skill para mi portafolio en Supabase"
- ✅ Bien: "skill para modelar y limpiar datos reales en Supabase
  (reemplazar datos demo, RLS, migraciones)"

TU TAREA, PASO A PASO:

1. ANALIZAR
   Revisa el proyecto que te comparto e identifica:
   - Qué decisiones técnicas repetibles tomé (patrones de arquitectura,
     convenciones de nombres, estructura de carpetas, manejo de errores)
   - Qué instrucciones o prompts usé de forma recurrente
   - Qué problemas resolví que probablemente se repitan en otro proyecto
     con el mismo stack

2. PROPONER SKILLS CANDIDATAS
   Antes de crear nada, dame una lista de skills candidatas con:
   - Nombre propuesto (kebab-case, en inglés, ej. `nextjs-api-integration`)
   - Stack/tecnología de la que depende
   - Descripción de una línea (qué hace y cuándo se activa)
   - De qué proyecto(s) la extrajiste
   Espera mi confirmación antes de continuar con la siguiente skill.

3. CREAR ESTRUCTURA
   Para cada skill aprobada, crea:
   ```
   nombre-skill/
   ├── SKILL.md          (frontmatter: name, description "pushy" y específica)
   ├── references/        (si hay documentación de apoyo extensa)
   ├── scripts/            (si hay código reutilizable, no solo explicado)
   └── assets/             (plantillas, snippets base)
   ```
   Organiza las carpetas del repo por categoría de stack, no por proyecto:
   ```
   claude-skills/
   ├── README.md
   ├── frontend/        (react, next.js, tailwind)
   ├── backend/         (apis, supabase, insforge, node)
   ├── automation/      (vba, excel, python scripts)
   ├── docs-cv/         (documentación, cv, pitches)
   └── design/          (ui/ux, portafolio)
   ```

4. README DE USO
   Genera/actualiza el README.md raíz del repo con:
   - Qué es este repositorio y cómo se usa con Claude (Claude Code / Claude
     Desktop / proyectos)
   - Tabla de skills disponibles: nombre | categoría | stack | cuándo se
     activa
   - Instrucciones de instalación/activación de una skill en un proyecto
     nuevo
   - Convención de nombres y checklist para agregar una skill nueva

5. VALIDACIÓN FINAL
   Antes de cerrar, revisa que:
   - Ninguna skill mencione el nombre de un proyecto específico en su
     `description`
   - Cada skill sea aplicable a "cualquier proyecto que use X stack", no
     solo al proyecto de origen
   - No haya dos skills con solapamiento >70% de propósito (si lo hay,
     propón fusionarlas)

Empieza por el paso 1: pídeme qué proyecto(s) vas a analizar primero si no
te los he compartido ya.
```
