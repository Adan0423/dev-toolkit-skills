# Prompt: Crear una skill individual con /skill-creator

Úsalo DESPUÉS de tener la lista de skills candidatas (del prompt de
organización). Uno por cada skill, para que Claude use la skill
`skill-creator` y te guíe por el proceso completo (interview → borrador →
casos de prueba → iteración).

---

## PROMPT

```
Usa la skill skill-creator para ayudarme a crear la siguiente skill de mi
repositorio personal `claude-skills`.

DATOS DE LA SKILL:
- Nombre propuesto: [NOMBRE-EN-KEBAB-CASE]
- Categoría/carpeta destino: [frontend / backend / automation / docs-cv / design]
- Stack o tecnología de la que depende: [ej. Next.js + TypeScript + Supabase]
- Proyecto(s) de origen (solo como referencia interna, NO debe aparecer en
  la description final): [ej. tienda Aliclik / portafolio Supabase]

REQUISITO NO NEGOCIABLE:
Esta skill debe quedar GLOBAL respecto al stack, no atada al proyecto de
origen. Extrae el patrón reutilizable, no la solución particular del
proyecto. Si detectas que algo es demasiado específico de un solo proyecto
para generalizarse, dímelo antes de escribir el SKILL.md en vez de
forzarlo.

SIGUE EL PROCESO DE skill-creator:

1. Captura de intención — confírmame:
   - Qué debe habilitar esta skill que Claude haga
   - Cuándo debe activarse (qué frases/contextos míos la disparan)
   - Formato de salida esperado
   - Si necesita casos de prueba (sí, si el resultado es verificable objetivamente;
     no, si es algo más subjetivo como estilo de escritura o diseño)

2. Entrevista — pregúntame sobre:
   - Edge cases que ya me encontré en el proyecto de origen
   - Formatos de entrada/salida reales que usé
   - Dependencias (librerías, MCPs, herramientas externas)
   - Criterios de éxito

3. Escribir el SKILL.md siguiendo esta convención:
   - `name`: kebab-case, en inglés, sin mencionar el proyecto de origen
   - `description`: qué hace + cuándo se activa, en tono "insistente"
     (specific triggers, no vago) — recuerda que Claude tiende a
     sub-activar skills si la descripción es débil
   - Body bajo 500 líneas; si crece, muévelo a references/ con tabla de
     contenidos
   - Si hay código reutilizable de verdad (no solo explicado), va en
     scripts/, no pegado en el body

4. Al terminar, muéstrame:
   - El SKILL.md completo
   - Dónde debe ir dentro de la estructura de carpetas del repo
     (`claude-skills/[categoría]/[nombre-skill]/`)
   - Una entrada lista para pegar en la tabla del README.md raíz

Empieza haciéndome las preguntas de la fase de "Captura de Intención".
```
