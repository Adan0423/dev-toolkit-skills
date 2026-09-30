---
name: cv-harvard-ats
description: >
  Crea, reescribe o audita un CV/currículum siguiendo el modelo Harvard (orientado a logros cuantificados) combinado con optimización ATS (Applicant Tracking System), para maximizar el score en herramientas de diagnóstico de CV (ATS, Enfoque, Impacto, Claridad, Contacto, Legibilidad) y aumentar la tasa de respuesta de reclutadores. Funciona para CUALQUIER área o industria (tecnología, salud, ventas, administración, educación, legal, operaciones, marketing, ingeniería, seguridad, etc.), no solo tech. Usa este skill siempre que el usuario pida mejorar u optimizar un CV, subir el score ATS, reescribir logros con métricas, adaptar un CV a una vacante específica, o si comparte un diagnóstico o reporte de un analizador de CV (score, palabras clave faltantes, hallazgos) y pide corregirlo. También úsalo si el usuario simplemente pega su experiencia laboral y pide "hazme un CV" o "revisa mi CV", aunque no mencione "Harvard" o "ATS" explícitamente.
---

# Especialidad: ats

Procedencia: `skills/docs-cv/cv-harvard-ats/SKILL.md`. Guía derivada; editar fuente y reconstruir, no esta copia.

Aplica el procedimiento solo al modo seleccionado. Las preferencias del usuario, alcance y contrato común de la familia delimitan sus recomendaciones. No invoca otras skills por defecto.

# CV Harvard + ATS

Convierte cualquier CV (de cualquier industria) en un documento que (1) pasa filtros ATS automáticos y (2) convence a un reclutador humano en menos de 10 segundos de lectura, usando el modelo de currículum de Harvard (Harvard Extension School / Harvard OCS): bullets orientados 100% a logros, no a tareas.

## Principio central

**Una tarea describe lo que hiciste. Un logro describe el resultado que produjiste.** El modelo Harvard reescribe cada línea de experiencia con la fórmula:

```
VERBO DE ACCIÓN (pasado) + QUÉ HICISTE/CÓMO + RESULTADO MEDIBLE (cifra, %, tiempo, dinero, personas, escala)
```

Ejemplo genérico (aplica a cualquier rubro):
- ❌ Tarea: "Encargado de atención al cliente y resolución de quejas."
- ✅ Logro: "Resolví un promedio de 45 quejas/mes, logrando 92% de satisfacción y reduciendo el tiempo de respuesta de 48h a 12h."

Este es el hallazgo #1 que penaliza la mayoría de los CVs (dimensión "Impacto" en los diagnósticos automáticos): describir funciones sin resultado. Corregir esto suele subir el score total 15-25 puntos por sí solo.

## Cuándo usar cada referencia

Antes de escribir o reescribir el CV, lee las referencias relevantes:

- **`references/estructura_harvard.md`** — Formato, secciones y orden del CV modelo Harvard. Leer siempre.
- **`references/reglas_ats.md`** — Reglas de formato/estructura que debe cumplir cualquier CV para no ser rechazado por un ATS. Leer siempre.
- **`references/formula_logros.md`** — Cómo convertir cualquier tarea en un logro cuantificado, con banco de verbos de acción por función (no solo tech) y técnicas para estimar cifras cuando el usuario no las recuerda con exactitud. Leer al reescribir experiencia.
- **`references/checklist_dimensiones.md`** — Las 6 dimensiones que evalúan los diagnosticadores de CV automáticos (ATS, Enfoque, Impacto, Claridad, Contacto, Legibilidad) con el criterio exacto para sacar el máximo en cada una. Leer al auditar un CV existente o un reporte de diagnóstico.
- **`references/adaptacion_por_industria.md`** — Cómo ajustar keywords, verbos y métricas típicas según el rubro (ventas, salud, educación, operaciones/seguridad, legal, marketing, finanzas, tech, atención al cliente, manufactura). Leer cuando el usuario tenga un perfil fuera de tecnología o quiera adaptar el CV a una vacante puntual.

## Flujo de trabajo

### 1. Diagnóstico inicial
Si el usuario comparte un CV existente (con o sin reporte de diagnóstico):
- Identifica cuántos bullets son "tarea" vs "logro" (sin cifra = tarea).
- Identifica si el CV cubre 1-2 áreas claras o está disperso en 3+.
- Verifica los elementos indispensables de ATS (ver `reglas_ats.md`).
- Si hay un reporte/diagnóstico externo (score, keywords faltantes, hallazgos), úsalo como fuente de verdad de lo que falta — no repitas trabajo, complétalo.

Presenta el diagnóstico en 4-6 líneas: qué está bien, qué está fallando, y qué dimensión es más urgente arreglar (normalmente Impacto y Enfoque).

### 2. Recolectar cifras reales (no inventar)
El modelo Harvard exige números, pero **nunca inventes una cifra**. Si el usuario no la tiene:
- Pregunta directamente: "¿Cuántas [personas/reportes/clientes/soles/horas] aproximadamente?"
- Si de verdad no hay forma de saberlo, usa una estimación conservadora explícita marcada para que el usuario la confirme ("~20 reportes/mes — confirma si es correcto"), o reformula el logro en términos de alcance/frecuencia/escala en vez de una cifra exacta ("gestioné el 100% de los reportes administrativos de la oficina" en vez de un número inventado).
- Nunca entregues al usuario un CV con cifras que él no validó.

### 3. Reescribir por secciones
Sigue el orden de `estructura_harvard.md`. Para cada bullet de experiencia aplica la fórmula de `formula_logros.md`. Usa un verbo de acción distinto por bullet (no repetir "participé", "encargado de", "responsable de" — estos son señales negativas en ambos modelos, Harvard y ATS).

### 4. Enfocar el CV
Si el perfil cruza 2+ áreas no relacionadas (ej. seguridad + desarrollo web, o ventas + soporte técnico):
- Pregunta a qué rol(es) apunta el usuario ahora.
- Recomienda 1-2 versiones del CV, cada una liderando con el área relevante y relegando la otra a una línea breve, en vez de un solo CV disperso que intenta cubrir todo. Un CV enfocado sube significativamente la dimensión "Enfoque".

### 5. Optimizar para ATS
Aplica `reglas_ats.md`: una columna, sin tablas/gráficos/columnas paralelas, headers estándar ("Experiencia", "Educación", "Habilidades"), fechas en formato consistente, fuente estándar, PDF con texto extraíble (nunca imagen escaneada), y keywords exactas de la vacante objetivo si el usuario la proporciona.

### 6. Verificación final contra las 6 dimensiones
Antes de entregar, recorre `checklist_dimensiones.md` y confirma explícitamente para el usuario en qué quedó cada dimensión (ej. "Impacto: 5 de 6 bullets ahora llevan cifra ✓", "Enfoque: CV ahora centrado 100% en desarrollo full stack ✓"). Si alguna dimensión sigue débil, dilo con honestidad — no afirmes "esto pasará 100/100" si no es cierto; explica qué le falta al usuario para llegar ahí (normalmente: más cifras reales, o experiencia de liderazgo que aún no tiene).

### 7. Entregar el archivo
Genera el CV final como .docx (usa el skill `docx` para esto) o dile al usuario que puede pedirlo en Word. Nunca generes el CV solo como texto plano en el chat si el usuario lo va a usar para aplicar a trabajos — necesita un archivo descargable con buen formato ATS.

## Advertencia importante sobre "pasar 100/100"

Ningún CV "pasa 100/100" de forma garantizada porque cada herramienta de diagnóstico pondera distinto y hay dimensiones (como "gestión de equipos" o "años de experiencia en el rubro") que no se resuelven reescribiendo texto — se resuelven con experiencia real. Sé honesto con el usuario: este skill lleva el CV al máximo posible *dado su historial real*, no fabrica experiencia que no tuvo. Si el score bajo se debe a algo estructural (ej. falta de experiencia de liderazgo), dilo y sugiere el plan de carrera para conseguirla, en vez de simular en el CV algo que no ocurrió.
