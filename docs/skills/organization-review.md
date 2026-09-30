# Auditoría y propuesta de organización de skills

Fecha: 30 de septiembre de 2026. Se revisaron inventario, frontmatter, descripciones,
extensión de entradas, estructura de paquetes y ejemplos representativos. No se han
probado las 95 skills en proyectos reales ni certificado sus scripts/APIs externos.
No se han fusionado instrucciones ni reemplazado skills existentes.

## Agrupación posterior implementada

Se añadieron [seis familias con carga selectiva](family-skills.md), sin reemplazar
las fuentes anteriores. El inventario actual tiene 101 skills y 55 paquetes.
Las cifras y la matriz de abajo documentan la auditoría previa de 95 skills.

## Recuperación completada

- Antes: 61 SKILL.md en skills/. Después: 95, con 95 nombres únicos.
- Paquetes: 49 (13 .skill y 36 .zip); representan 42 nombres de skill.
- Se recuperaron 31 grupos ausentes, equivalentes a 34 skills: un pack contiene cuatro.
- 571 archivos escritos entre fuentes recuperadas y variantes preservadas.
- Los paquetes originales no se modificaron y las fuentes existentes no se sobrescribieron.
- Se preservaron seis variantes distintas en cinco grupos: algorithmic-art,
  frontend-design, cv-harvard-ats (dos variantes), skill-creator y Tailwind.
- Se normalizaron las envolturas de instalación (.agents/skills/) y paquetes sin carpeta
  raíz al recuperar las fuentes; se conservaron bytes de contenido y recursos.
- Para fuentes ausentes con varias opciones se eligió la que incluía más archivos;
  esto NO acredita mejor calidad ni fecha más reciente. Se preservó la alternativa distinta.

Trazabilidad: [recuperación inicial](source-recovery.json),
[inventario actualizado](source-reconciliation.json),
[variantes para comparar](package-variants/).

## Qué agrupaciones convienen

Agrupar archivos en carpetas organiza el repositorio. Crear una skill principal con
modos/referencias selectivas reduce carga de instrucciones y ambigüedad. Son cosas
distintas: no todos los agentes descubren o invocan automáticamente sub-skills anidadas.
La eficiencia debe comprobarse en el agente objetivo, no suponerse por una jerarquía.

| Familia propuesta | Fuentes que revisar | Organización recomendada |
|---|---|---|
| React engineering | react-frontend, react-frontend-expert, react-2026, frontend-react-best-practices | Entrada común; referencias de componentes/datos, arquitectura, rendimiento y actualización por versión. Mantener React Router como especialidad seleccionable. |
| Tailwind engineering | tailwindcss, tailwind-4-docs, tailwind-theme-builder, tailwind-v4-shadcn, tailwindcss-v4-3-expert | Entrada por versión/problema; modos instalación, migración, tokens/dark mode y shadcn. Comparar variantes antes de fusionar. |
| Web design | impeccable, frontend-design, web-ui-ux-frontend-architect y skills de acabado | Una puerta de entrada para dirección/implementación/acabado. Mantener operaciones pequeñas invocables si aportan precisión; no cargar todas por defecto. |
| Arquitectura | modern-software-architect, software-project-architect | Comparar y consolidar el análisis/estructura compartido. Bases de datos como especialidad independiente. |
| Documentación de repositorio | documentation-repository-curator, project-readme-documentation, docs-updater | Modos auditoría, README y sincronización desde cambios. Coautoría, comunicación y humanización conservan objetivos propios. |
| CV | cv-builder-harvard, cv-harvard-ats y variantes recuperadas | Entrada CV; modos formato, adaptación ATS y revisión. Comparar recursos/versiones y preservar procedencia. |
| SEO y GEO | seo-geo-web, seo-sitemap | SEO/GEO principal con procedimiento sitemap por stack. Eliminar dominio fijo del procedimiento antes de reutilizarlo. |
| WordPress | wordpress-theme-studio, wordpress-elementor-commerce | Entrada opcional que selecciona código propio o builder. Referencias comunes de contenido/acceso/QA; mantener paquetes autocontenidos. |
| Wix | wix-app, wix-auth, wix-docs, wix-design-system, wix-headless, wix-vibe-headless, wix-manage | Selector por app/headless/gestión. Docs/auth/diseño como auxiliares; evitar mezclar APIs de contextos diferentes. |
| Corrección de sistemas | system-correction-orchestrator, rbac-database-corrector, mcp-integration-corrector, role-aware-ui-corrector | Ya es un pack con orquestador y tres especialistas; revisar rutas, contratos y descubrimiento del agente antes de usarlo como patrón. |
| Móvil | mobile-app-engineering, android-modern-ui-expert, android-codebase-auditor-refactor, android-camera-engineering | Selector por stack y tarea; cámara permanece especializada, sin cargarse en toda tarea Android. |
| Documentos | pdf, word-document-tools, pptx, xlsx | Agrupación de carpeta, no megaskill: herramientas, formatos y pruebas son diferentes. |

Mantener Odoo, seguridad, APIs LLM/MCP, escritorio y arte como especialidades claras.
No mezclar WordPress/Odoo/Wix con toda la lógica de SEO o diseño; consumir solo lo
pertinente. Brand-guidelines está orientada a la marca Anthropic: no es un sistema
universal de identidad para cualquier cliente.

## Estructura portable propuesta

```text
skills/frontend/react-engineering/
  SKILL.md                    propósito, selección de modo, invariantes
  references/
    architecture.md
    components-data.md
    performance.md
    framework-versions.md
  scripts/                    solo helpers ejecutables realmente reutilizables
  agents/openai.yaml          metadata del agente objetivo
```

Los procedimientos de references son modos especializados, no skills registradas
automáticamente. Si una especialidad necesita nombre propio e invocación directa,
mantenerla como carpeta con SKILL.md y definir carga/enlaces explícitos. Una skill
padre no debe forzar llamadas recursivas ni cargar todas sus referencias siempre.
Al generar paquetes, incluir recursos necesarios sin depender de rutas hacia fuera.

## Mejora de cada skill: criterios

1. Nombre/description precisos y compatibles con el agente; reducir activación accidental.
2. Inspección del proyecto/versión antes de prescribir herramientas o cambios.
3. Separar instrucciones compartidas de documentación por modo, sin perder invariantes.
4. Verificar referencias, scripts, APIs y fuentes cambiantes cuando se modifique esa skill.
5. Mantener autorizaciones, permisos y alcance del usuario; no convertir cualquier tarea
   en instalación, publicación o migración automática.
6. Probar un caso útil, uno fuera del alcance, un fallo y una limitación de herramientas.
   Validar comportamiento y resultados, no solo YAML o frases del documento.
7. Medir activación correcta, completitud y coste/contexto antes/después en casos comparables;
   no afirmar ahorro porcentual sin evaluación.

32 entradas superan 300 líneas. Es una señal de revisión, no un límite obligatorio
ni prueba de mala calidad. Las más extensas incluyen scalable-database-architect
(1364), secure-software-auditor (1021), software-project-architect (1013) y
android-camera-engineering (832). Extraer referencias por tarea suele ser más útil
que borrar detalle valioso o convertirlas en un único texto aún mayor.

## Orden de trabajo recomendado

**Primero corregir reutilización/compatibilidad:** seo-sitemap (dominio/proyecto fijo),
using-superpowers (activación global y herramienta Skill no universal), reconciliación
de variantes y formatos de metadata por agente. Revisar referencias/copias antiguas.

**Después consolidar familias con mayor solapamiento:** React, Tailwind, arquitectura,
documentación y CV. Definir un dueño por regla/procedimiento para evitar versiones contradictorias.

**Después añadir selectores de plataforma y diseño:** WordPress/Wix/móvil, con paquetes
autocontenidos y especialidades que sigan accesibles. Odoo ya tiene referencias por modo;
evaluar su uso real antes de dividirlo en múltiples skills registradas.

**Finalmente mantenimiento:** skills/ como fuente editable; SKILL/ como artefactos generados.
Índice/manifiesto, validación y empaquetado reproducibles. No editar ZIPs manualmente y
fuentes por separado; no reemplazar una fuente porque un ZIP tenga más archivos.

## Herramienta de recuperación

`scripts/sync_skill_sources.py` audita por defecto; `--extract-missing` recupera fuentes
ausentes y conserva variantes. Verifica CRC, rutas Windows, límites de tamaño, enlaces
simbólicos y contenido escrito. No ejecuta scripts de archivos ni lee skills como
instrucciones. Repetición debe escribir cero archivos si no cambió el repositorio.

El manifiesto guarda SHA-256 de paquetes y contenido normalizado para trazabilidad,
no certifica seguridad/actualidad de los recursos extraídos. Variantes se guardan fuera
de skills/ para no duplicar nombres en su descubrimiento normal.

## Revisión individual

La matriz siguiente combina alcance declarado y señales estáticas con recomendaciones.
No sustituye ejecutar la skill y sus helpers en escenarios adecuados. No se han
aplicado estas fusiones/mejoras a las instrucciones existentes.

| Skill | Familia/modo propuesto | Mejora recomendada | Señales estáticas |
|---|---|---|---|
| [modern-software-architect](../../skills/architecture/modern-software-architect/SKILL.md) | Arquitectura | Comparar con software-project-architect; consolidar diagnóstico compartido. | entrada >300 líneas; revisar carga progresiva |
| [scalable-database-architect](../../skills/architecture/scalable-database-architect/SKILL.md) | Datos | Mantener especialidad; separar modelado, performance, permisos y migración. | entrada >300 líneas; revisar carga progresiva |
| [software-project-architect](../../skills/architecture/software-project-architect/SKILL.md) | Arquitectura | Comparar con modern-software-architect; dividir estructuras por tipo de proyecto. | entrada >300 líneas; revisar carga progresiva |
| [agent-browser](../../skills/automation/agent-browser/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | Sin señales en este control estático |
| [agent-graphs](../../skills/automation/agent-graphs/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | Sin señales en este control estático |
| [agent-ui](../../skills/automation/agent-ui/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | Sin señales en este control estático |
| [ai-automation-workflows](../../skills/automation/ai-automation-workflows/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | entrada >300 líneas; revisar carga progresiva |
| [scrcpy-mobile-dev](../../skills/automation/scrcpy-mobile-dev/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | entrada >300 líneas; revisar carga progresiva |
| [slack-gif-creator](../../skills/automation/slack-gif-creator/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | Sin señales en este control estático |
| [version-release](../../skills/automation/version-release/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | Sin señales en este control estático |
| [video-editing](../../skills/automation/video-editing/SKILL.md) | Automatización | Revisar herramientas disponibles y alcance de acciones externas; pruebas acotadas de pipeline. | entrada >300 líneas; revisar carga progresiva |
| [clerk-react-router-patterns](../../skills/backend/clerk-react-router-patterns/SKILL.md) | Backend específico | Mantener contrato del proveedor/framework; pruebas de sesión/permisos y versiones actuales. | Sin señales en este control estático |
| [sentry-react-router-framework-sdk](../../skills/backend/sentry-react-router-framework-sdk/SKILL.md) | Backend específico | Mantener contrato del proveedor/framework; pruebas de sesión/permisos y versiones actuales. | entrada >300 líneas; revisar carga progresiva |
| [supabase](../../skills/backend/supabase/SKILL.md) | Backend específico | Mantener contrato del proveedor/framework; pruebas de sesión/permisos y versiones actuales. | Sin señales en este control estático |
| [supabase-postgres-best-practices](../../skills/backend/supabase-postgres-best-practices/SKILL.md) | Backend específico | Mantener contrato del proveedor/framework; pruebas de sesión/permisos y versiones actuales. | Sin señales en este control estático |
| [adapt](../../skills/design/adapt/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [adaptive-web-ui-stack-architect](../../skills/design/adaptive-web-ui-stack-architect/SKILL.md) | Stack UI | Mantener selección de stack separada del acabado; revalidar decisiones por proyecto. | Sin señales en este control estático |
| [algorithmic-art](../../skills/design/algorithmic-art/SKILL.md) | Arte generativo | Comparar variante, licencias/assets y entorno; mantener separado de diseño de sistemas. | entrada >300 líneas; revisar carga progresiva |
| [animate](../../skills/design/animate/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [audit](../../skills/design/audit/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [bolder](../../skills/design/bolder/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [brand-guidelines](../../skills/design/brand-guidelines/SKILL.md) | Identidad específica | Mantener alcance Anthropic explícito; no imponer esa marca a proyectos del usuario. | Sin señales en este control estático |
| [canvas-design](../../skills/design/canvas-design/SKILL.md) | Arte estático | Verificar fuentes/licencias y generación; no mezclar con frontend web. | Sin señales en este control estático |
| [clarify](../../skills/design/clarify/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [colorize](../../skills/design/colorize/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [critique](../../skills/design/critique/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [delight](../../skills/design/delight/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | entrada >300 líneas; revisar carga progresiva |
| [distill](../../skills/design/distill/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [frontend-design](../../skills/design/frontend-design/SKILL.md) | Diseño web | Comparar paquete con fuente; definir dirección visual sin competir con cada skill de acabado. | Sin señales en este control estático |
| [impeccable](../../skills/design/impeccable/SKILL.md) | Diseño web | Revisar preguntas obligatorias y comandos exclusivos de runtime; referencias solo por modo. | entrada >300 líneas; revisar carga progresiva |
| [layout](../../skills/design/layout/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [optimize](../../skills/design/optimize/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [overdrive](../../skills/design/overdrive/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [polish](../../skills/design/polish/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [quieter](../../skills/design/quieter/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [shape](../../skills/design/shape/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [theme-factory](../../skills/design/theme-factory/SKILL.md) | Temas de artefactos | Biblioteca selectiva de paletas; separar tema visual de lógica/producto. | Sin señales en este control estático |
| [typeset](../../skills/design/typeset/SKILL.md) | Acabado visual | Mantener operación precisa; integrar con selector de diseño y cargar solo referencias pertinentes. | Sin señales en este control estático |
| [ui-ux-pro-max](../../skills/design/ui-ux-pro-max/SKILL.md) | Biblioteca de diseño | Consultar datos/estilos por necesidad, no cargar catálogo completo en cada petición. | Sin señales en este control estático |
| [web-artifacts-builder](../../skills/design/web-artifacts-builder/SKILL.md) | Artefactos web | Revisar dependencia de claude.ai/harness; distinguir exportable de app integrada. | Sin señales en este control estático |
| [web-ui-ux-frontend-architect](../../skills/design/web-ui-ux-frontend-architect/SKILL.md) | Diseño web | Entrada de análisis/implementación; evitar repetir todas las especialidades visuales. | entrada >300 líneas; revisar carga progresiva |
| [windows-desktop-ui-ux-engineer](../../skills/desktop/windows-desktop-ui-ux-engineer/SKILL.md) | Escritorio | Procedimientos por toolkit; pruebas DPI, teclado, redimensionado y packaging real. | entrada >300 líneas; revisar carga progresiva |
| [doc-coauthoring](../../skills/docs/doc-coauthoring/SKILL.md) | Escritura | Procedimiento de coautoría selectivo; revisar fricción de preguntas y etapas. | entrada >300 líneas; revisar carga progresiva |
| [docs-updater](../../skills/docs/docs-updater/SKILL.md) | Docs repositorio | Mantener modo actualización por cambios; verificar tag/base y no modificar releases sin alcance. | entrada >300 líneas; revisar carga progresiva |
| [documentation-repository-curator](../../skills/docs/documentation-repository-curator/SKILL.md) | Docs repositorio | Entrada auditoría documental; seleccionar README/sincronización sin repetir procesos. | entrada >300 líneas; revisar carga progresiva |
| [humanizer](../../skills/docs/humanizer/SKILL.md) | Escritura | Mantener transformación editorial independiente; revisar efectos sobre hechos/voz. | entrada >300 líneas; revisar carga progresiva |
| [internal-comms](../../skills/docs/internal-comms/SKILL.md) | Comunicación | Adaptar contexto/formato de organización; no inventar políticas de compañía. | Sin señales en este control estático |
| [project-readme-documentation](../../skills/docs/project-readme-documentation/SKILL.md) | Docs repositorio | Convertir en modo README o especialidad; evitar conflicto con curador. | Sin señales en este control estático |
| [cv-builder-harvard](../../skills/docs-cv/cv-builder-harvard/SKILL.md) | CV | Separar formato de adaptación ATS; usar como modo de la familia CV. | Sin señales en este control estático |
| [cv-harvard-ats](../../skills/docs-cv/cv-harvard-ats/SKILL.md) | CV | Comparar dos variantes con fuente; unificar formato/ATS sin perder recursos o procedencia. | Sin señales en este control estático |
| [pdf](../../skills/documents/pdf/SKILL.md) | Documentos | Mantener formato independiente; validar helpers/dependencias y un artefacto real por caso. | entrada >300 líneas; revisar carga progresiva |
| [pptx](../../skills/documents/pptx/SKILL.md) | Documentos | Mantener formato independiente; validar helpers/dependencias y un artefacto real por caso. | Sin señales en este control estático |
| [word-document-tools](../../skills/documents/word-document-tools/SKILL.md) | Documentos | Mantener formato independiente; validar helpers/dependencias y un artefacto real por caso. | Sin señales en este control estático |
| [xlsx](../../skills/documents/xlsx/SKILL.md) | Documentos | Mantener formato independiente; validar helpers/dependencias y un artefacto real por caso. | Sin señales en este control estático |
| [frontend-react-best-practices](../../skills/frontend/frontend-react-best-practices/SKILL.md) | React | Comparar contratos y consolidar reglas compartidas; especializar arquitectura, datos o rendimiento. | entrada >300 líneas; revisar carga progresiva |
| [frontend-ui-engineering](../../skills/frontend/frontend-ui-engineering/SKILL.md) | frontend | Precisar activación, compatibilidad, recursos y escenario de uso con resultado verificable. | entrada >300 líneas; revisar carga progresiva |
| [react-2026](../../skills/frontend/react-2026/SKILL.md) | React | Comparar contratos y consolidar reglas compartidas; especializar arquitectura, datos o rendimiento. | entrada >300 líneas; revisar carga progresiva |
| [react-frontend](../../skills/frontend/react-frontend/SKILL.md) | React | Comparar contratos y consolidar reglas compartidas; especializar arquitectura, datos o rendimiento. | Sin señales en este control estático |
| [react-frontend-expert](../../skills/frontend/react-frontend-expert/SKILL.md) | React | Comparar contratos y consolidar reglas compartidas; especializar arquitectura, datos o rendimiento. | entrada >300 líneas; revisar carga progresiva |
| [react-router-framework-mode](../../skills/frontend/react-router-framework-mode/SKILL.md) | frontend | Precisar activación, compatibilidad, recursos y escenario de uso con resultado verificable. | Sin señales en este control estático |
| [seo-geo-web](../../skills/frontend/seo-geo-web/SKILL.md) | SEO/GEO | Entrada transversal; reconciliar seo-sitemap y revalidar fuentes por motor/plataforma. | Sin señales en este control estático |
| [seo-sitemap](../../skills/frontend/seo-sitemap/SKILL.md) | SEO/GEO | P1: parametrizar dominio/rutas y corregir reglas de robots según motor; integrar como procedimiento SvelteKit. | dominio/proyecto fijo |
| [tailwind-4-docs](../../skills/frontend/tailwind-4-docs/SKILL.md) | Tailwind | Comparar variantes/versiones; separar instalación, migración, tokens/dark mode y shadcn. | Sin señales en este control estático |
| [tailwind-theme-builder](../../skills/frontend/tailwind-theme-builder/SKILL.md) | Tailwind | Comparar variantes/versiones; separar instalación, migración, tokens/dark mode y shadcn. | entrada >300 líneas; revisar carga progresiva |
| [tailwind-v4-shadcn](../../skills/frontend/tailwind-v4-shadcn/SKILL.md) | Tailwind | Comparar variantes/versiones; separar instalación, migración, tokens/dark mode y shadcn. | entrada >300 líneas; revisar carga progresiva |
| [tailwindcss](../../skills/frontend/tailwindcss/SKILL.md) | Tailwind | Comparar variantes/versiones; separar instalación, migración, tokens/dark mode y shadcn. | Sin señales en este control estático |
| [tailwindcss-v4-3-expert](../../skills/frontend/tailwindcss-v4-3-expert/SKILL.md) | Tailwind | Comparar variantes/versiones; separar instalación, migración, tokens/dark mode y shadcn. | Sin señales en este control estático |
| [vite](../../skills/frontend/vite/SKILL.md) | frontend | Precisar activación, compatibilidad, recursos y escenario de uso con resultado verificable. | Sin señales en este control estático |
| [llm-api-development](../../skills/integrations/llm-api-development/SKILL.md) | Integraciones | Revisar SDK/proveedor/autenticación; aislar recetas y comprobar resultado persistido. | entrada >300 líneas; revisar carga progresiva |
| [mcp-builder](../../skills/integrations/mcp-builder/SKILL.md) | Integraciones | Revisar SDK/proveedor/autenticación; aislar recetas y comprobar resultado persistido. | Sin señales en este control estático |
| [qoder-wiki](../../skills/meta/qoder-wiki/SKILL.md) | meta | Precisar activación, compatibilidad, recursos y escenario de uso con resultado verificable. | Sin señales en este control estático |
| [skill-creator](../../skills/meta/skill-creator/SKILL.md) | Meta | Comparar paquete/fuente antes de escoger versión; distinguir creación, evaluación y metadata por agente. | entrada >300 líneas; revisar carga progresiva |
| [using-superpowers](../../skills/meta/using-superpowers/SKILL.md) | Meta | P1: eliminar activación universal y dependencia obligatoria de herramienta Skill; adaptar al agente real. | activación global o umbral artificial |
| [writing-great-skills](../../skills/meta/writing-great-skills/SKILL.md) | meta | Precisar activación, compatibilidad, recursos y escenario de uso con resultado verificable. | Sin señales en este control estático |
| [android-camera-engineering](../../skills/mobile/android-camera-engineering/SKILL.md) | Móvil | Seleccionar por stack/tarea; revalidar APIs y pruebas de dispositivos/roles pertinentes. | entrada >300 líneas; revisar carga progresiva |
| [android-codebase-auditor-refactor](../../skills/mobile/android-codebase-auditor-refactor/SKILL.md) | Móvil | Seleccionar por stack/tarea; revalidar APIs y pruebas de dispositivos/roles pertinentes. | Sin señales en este control estático |
| [android-modern-ui-expert](../../skills/mobile/android-modern-ui-expert/SKILL.md) | Móvil | Seleccionar por stack/tarea; revalidar APIs y pruebas de dispositivos/roles pertinentes. | entrada >300 líneas; revisar carga progresiva |
| [mobile-app-engineering](../../skills/mobile/mobile-app-engineering/SKILL.md) | Móvil | Seleccionar por stack/tarea; revalidar APIs y pruebas de dispositivos/roles pertinentes. | Sin señales en este control estático |
| [odoo-specialist](../../skills/platforms/odoo/odoo-specialist/SKILL.md) | Odoo | Conservar referencias por modo; evaluar Online/permisos/versiones y flujos en ejecución. | Sin señales en este control estático |
| [wix-app](../../skills/platforms/wix/wix-app/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | entrada >300 líneas; revisar carga progresiva |
| [wix-auth](../../skills/platforms/wix/wix-auth/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | Sin señales en este control estático |
| [wix-design-system](../../skills/platforms/wix/wix-design-system/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | Sin señales en este control estático |
| [wix-docs](../../skills/platforms/wix/wix-docs/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | Sin señales en este control estático |
| [wix-headless-entry](../../skills/platforms/wix/wix-headless/entry/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | Sin señales en este control estático |
| [wix-headless](../../skills/platforms/wix/wix-headless/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | Sin señales en este control estático |
| [wix-manage](../../skills/platforms/wix/wix-manage/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | entrada >300 líneas; revisar carga progresiva |
| [wix-vibe-headless](../../skills/platforms/wix/wix-vibe-headless/SKILL.md) | Wix | Revisar contexto API, permisos y enlaces; seleccionar app/headless/gestión sin llamadas inventadas. | Sin señales en este control estático |
| [wordpress-elementor-commerce](../../skills/platforms/wordpress/wordpress-elementor-commerce/SKILL.md) | WordPress | Mantener rama builder/plugins; comprobar planes, editor/MCP y checkout reales. | Sin señales en este control estático |
| [wordpress-theme-studio](../../skills/platforms/wordpress/wordpress-theme-studio/SKILL.md) | WordPress | Mantener rama código propio; contratos comunes de contenido/acceso/QA sin depender de otro ZIP. | Sin señales en este control estático |
| [mcp-integration-corrector](../../skills/quality/system-correction-skill-pack/mcp-integration-corrector/SKILL.md) | Corrección de sistemas | Especialista conectores; descubrir capacidades, autenticación y persistencia. | Sin señales en este control estático |
| [rbac-database-corrector](../../skills/quality/system-correction-skill-pack/rbac-database-corrector/SKILL.md) | Corrección de sistemas | Especialista permisos/datos; probar usuario normal y lecturas/escrituras denegadas. | entrada >300 líneas; revisar carga progresiva |
| [role-aware-ui-corrector](../../skills/quality/system-correction-skill-pack/role-aware-ui-corrector/SKILL.md) | Corrección de sistemas | Especialista UI por rol; diferenciar Empty de Unauthorized/Offline/Error. | Sin señales en este control estático |
| [system-correction-orchestrator](../../skills/quality/system-correction-skill-pack/system-correction-orchestrator/SKILL.md) | Corrección de sistemas | Conservar router; revisar contratos/links de tres especialistas y evitar cargar todo. | entrada >300 líneas; revisar carga progresiva |
| [webapp-testing](../../skills/quality/webapp-testing/SKILL.md) | QA navegador | Verificar runtime/browser disponible; casos de comportamiento y evidencia, no capturas solas. | Sin señales en este control estático |
| [secure-software-auditor](../../skills/security/secure-software-auditor/SKILL.md) | Seguridad | Mantener auditoría especializada; referencias por superficie/stack y pruebas de permisos. | entrada >300 líneas; revisar carga progresiva |
