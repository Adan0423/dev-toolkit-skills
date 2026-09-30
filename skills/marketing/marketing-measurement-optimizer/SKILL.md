---
name: marketing-measurement-optimizer
description: Analiza reportes de marketing y publicidad, audita conversiones y atribución, calcula métricas y rentabilidad, y propone experimentos y optimización basada en evidencia.
---

# Medición y optimización de marketing

## Evidencia antes de decisión

Confirma fuente, cuenta, período/zona horaria, moneda, granularidad, evento, ventana/modelo
de atribución y retraso de conversiones. API, CSV y captura deben distinguir observado,
estimado, modelado y desconocido. Datos faltantes no son cero. No interpreta acceso
denegado/error como cuenta vacía. Evita mezclar totales con filas de anuncios/desgloses.

Para comparar usa cohortes maduras y definiciones iguales; identifica promociones,
estacionalidad y cambios concurrentes. Un ROAS atribuido no prueba incrementalidad.
No suma compras atribuidas a Meta/Google/TikTok como pedidos únicos; contrasta backend/CRM
con IDs y períodos. Reach único no es aditivo. Anonimiza datos antes de compartir.

## Cálculos y calidad

Usa sumas de numeradores y denominadores compatibles, nunca promedio simple de ratios.
CTR = clics / impresiones; CPC = gasto / clics; CPM = gasto × 1000 / impresiones;
CPA = gasto / conversiones; ROAS = valor de conversión / gasto. Denominador cero produce
desconocido/no aplicable, no cero ni infinito. Especifica tipo de clic y conversión.
Conversiones de vista o fraccionadas pueden romper una interpretación de CVR como
probabilidad clic→compra; solo usa esa tasa cuando las definiciones son compatibles.

Para CSV normalizado usa [contrato](references/measurement-contract.md) y
`scripts/analyze_ads_csv.py archivo.csv`. El helper calcula métricas, separa monedas,
cuentas, eventos y atribución, y no decide qué campaña pausar ni opera cuentas.
Para otro formato mapea columnas/documenta unidades antes de usarlo; no sustituye datos.

Rentabilidad: separa ingreso bruto, devoluciones, impuestos y costes variables. Si el
margen de contribución antes de ads es m>0 sobre ingreso compatible, ROAS de equilibrio
aproximado = 1/m; CPA máximo depende de contribución por compra menos beneficio requerido.
Incluye logística/pasarelas/comisiones cuando correspondan; no confunde ROAS con beneficio.
LTV/CAC necesita cohortes y retención observada; no supone ingresos futuros garantizados.

Leads: CPL, tasa de cualificación, citas, cierres, ingreso y tiempo comercial. Usa
capacidad y calidad para decidir; más formularios baratos pueden empeorar adquisición.

## Tracking y código

Audita recorrido completo y evento comercial: disparo, consentimiento, payload, valor,
moneda, transaction/event ID, recepción, deduplicación y resultado backend. Browser y
servidor deben conservar identidad del mismo evento; nunca deduplica compras diferentes.
Revalida normas regionales y mecanismos actuales; server-side no evita consentimiento.

Si se solicita implementación, inspecciona stack/CMS y tags existentes para no duplicar
plugins, GTM y código directo. Respeta CSP, SSR/SPA, navegación, checkout y permisos.
Evita PII/secrets en UTMs/client/logs; identifica IDs de campaña, medium, source y creative
con una convención estable. Prueba eventos en entorno de QA y diagnóstico oficial sin
crear cargos o ventas reales por defecto. No instala tracking por pedir análisis de CSV.

## Experimentos y decisiones

Define hipótesis, variable, KPI comercial principal, guardrails, duración/volumen
justificados, presupuesto, población y criterio de decisión antes de lanzar. Distingue
test aleatorio de comparación observacional y de cambios antes/después. No prescribe
un tamaño de muestra universal ni significancia con datos agregados insuficientes.

Diagnóstico → hipótesis → cambio propuesto → riesgo/límite → prueba → revisión. Trata
fatiga, presupuesto y puja según evidencia comparable; no usa umbrales de CTR/CPA o
porcentajes de escala universales. Presenta «inconcluso» cuando corresponda.

Entrega tabla de hallazgos con evidencia/confianza, cálculo reproducible, acciones
priorizadas y dependencias. Ejecuta cambios de cuenta solo dentro de autorización
previa concreta y verifica persistencia. Monitoreo recurrente requiere solicitud.
