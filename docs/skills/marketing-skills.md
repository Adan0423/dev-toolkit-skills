# Marketing profesional: estrategia, contenido y ads

La familia `marketing-growth-suite` selecciona una especialidad según la tarea. Incluye
guías y recursos autocontenidos, con fuentes investigadas el 30 de septiembre de 2026.
Se añadieron siete skills fuente y siete ZIPs; no se instalaron globalmente ni se operó
ninguna cuenta publicitaria.

| Skill | Qué permite hacer | Paquete |
|---|---|---|
| [marketing-growth-suite](../../skills/marketing/marketing-growth-suite/SKILL.md) | Elegir especialidad y coordinar una tarea multicanal | [Familia completa](../../SKILL/marketing-growth-suite.zip) |
| [marketing-strategy-lab](../../skills/marketing/marketing-strategy-lab/SKILL.md) | Investigar, idear, trabajar oferta/embudo y planificar canales | [Estrategia](../../SKILL/marketing-strategy-lab.zip) |
| [marketing-content-studio](../../skills/marketing/marketing-content-studio/SKILL.md) | Copy, guiones, UGC, briefs visuales y calendarios | [Contenido](../../SKILL/marketing-content-studio.zip) |
| [meta-ads-specialist](../../skills/marketing/meta-ads-specialist/SKILL.md) | Facebook/Instagram, campañas, creativos, eventos y optimización | [Meta Ads](../../SKILL/meta-ads-specialist.zip) |
| [google-ads-specialist](../../skills/marketing/google-ads-specialist/SKILL.md) | Search, Shopping, Performance Max, YouTube/Display y conversiones | [Google Ads](../../SKILL/google-ads-specialist.zip) |
| [tiktok-ads-specialist](../../skills/marketing/tiktok-ads-specialist/SKILL.md) | Contenido nativo, Spark Ads, Smart+ y señales | [TikTok Ads](../../SKILL/tiktok-ads-specialist.zip) |
| [marketing-measurement-optimizer](../../skills/marketing/marketing-measurement-optimizer/SKILL.md) | Analizar reportes, tracking, rentabilidad y experimentos | [Medición](../../SKILL/marketing-measurement-optimizer.zip) |

## Instalar y pedir trabajo

Descomprime la familia en la carpeta de skills de tu agente. La estructura final debe
ser `<carpeta-de-skills>/marketing-growth-suite/SKILL.md`. El ZIP ya incluye esa carpeta.
Para carga selectiva basta instalar la familia; las seis individuales son alternativas
para quien solo necesite una capacidad. Instalarlas todas aumenta el catálogo activo.

Ejemplos de uso:

- «Usa $marketing-growth-suite para darme 12 ideas de anuncios de TikTok para mi producto».
- «Usa $marketing-growth-suite para preparar textos y guiones para Meta, sin publicar».
- «Usa $google-ads-specialist para revisar este reporte y proponer cambios justificados».
- «Usa $marketing-content-studio para crear un calendario de dos semanas y briefs visuales».
- «Usa $marketing-measurement-optimizer para detectar qué falta en la medición de leads».

Las guías usan producto, audiencia, oferta y evidencia existentes; preguntan solo lo que
afecta la decisión. Sin historial pueden generar hipótesis creativas señaladas como tales.
No prometen resultados ni convierten ROAS de plataforma en beneficio o ventas únicas.

MCP/API se usan cuando exista una conexión compatible y autorizada para esa plataforma.
Preparar ideas no requiere conectar cuentas. Si no puede ejecutar, entrega piezas,
configuración y pasos revisables. Crear estas skills no configura los MCP de publicidad.
Publicar, cambiar presupuesto o contactar creadores requiere alcance autorizado.

## Recursos incluidos

Brief reutilizable de producción, fuentes oficiales por plataforma, contrato CSV,
ejemplo sintético y analizador de métricas. El analizador no modifica cuentas; no suma
contextos incompatibles ni sustituye valores desconocidos por cero. El agente puede
combinar diseño, imagen o video disponibles cuando el resultado necesite esos medios;
no presupone que un prompt sea un archivo de imagen/video ya producido.

La [investigación y sus límites](../../skills/marketing/marketing-growth-suite/references/research-sources.md)
documenta skills.sh, SkillsMP, Impeccable y Awesome Skills, más documentación oficial.
Las referencias comunitarias inspiraron la estructura; los contenidos son una síntesis
propia y no se importaron sus scripts.

## Mantener

Edita la especialidad fuente; cambia selección en el SKILL.md principal y rutas en
`scripts/skill-families.json`. La investigación de la familia es un recurso manual
preservado por el generador; no edites las guías derivadas.

```text
python scripts/build_skill_families.py --family marketing-growth-suite
python scripts/build_skill_families.py --family marketing-growth-suite --check
python -B -m unittest discover -s tests -p test_marketing_metrics.py -v
```

El generador reconstruye la familia y sus seis paquetes individuales. Los paquetes
sin cambios conservan su archivo, evitando modificar familias ajenas al actualizar.
La conciliación general se puede revisar con `python scripts/sync_skill_sources.py`.

## Validación y límites

Se validaron frontmatter, enlaces locales, contenido de ZIPs y siete pruebas de métricas
(ratios ponderados, ceros, valores ausentes, monedas/atribución/cuentas separadas,
números inválidos y conversiones fraccionadas). Se comprobó también la ejecución del
ejemplo en la copia empaquetada. Estas pruebas no certifican ROAS, aceptación de anuncios,
permisos MCP ni comportamiento en cuentas reales.

La revisión de rutas incluye: ideas sin historial → content; Meta con rendimiento bajo
→ meta; RSA → google; autorización Spark → tiktok; CSV multimoneda → measurement;
presupuesto multicanal → strategy. Para cambios de plataforma revalida fuentes vigentes
y realiza una prueba en una cuenta autorizada antes de distribuir esa mejora.
