# Contrato CSV y límites del análisis

Columnas obligatorias: `platform,account,currency,attribution,conversion_event,period,
campaign,spend,impressions,clicks,conversions`. Opcional: `conversion_value`.
Números con punto decimal, sin símbolos o separadores de miles; UTF-8, encabezado y coma.
Un archivo debe usar una misma granularidad y filas no solapadas, sin totales duplicados.
El helper no puede detectar solapamiento semántico de exportaciones: revísalo antes.

`period` identifica intervalo de reporte, por ejemplo `2026-09-01/2026-09-07`.
`attribution` debe describir ventana/modelo, incluido clic/vista; `conversion_event`
debe describir resultado y definición. Distintos valores de estos campos quedan separados.
No introduce comparabilidad solo por igualar las etiquetas. Conserva metadatos originales.

Ejecuta `python scripts/analyze_ads_csv.py reporte.csv` desde la carpeta de esta skill.
Emite JSON por stdout; error de datos emite diagnóstico por stderr y código 2.
`--group-by campaign,ad_id` permite dimensiones adicionales presentes en el CSV.
Para sumar campañas explícitamente usa `--group-by ''`; plataforma, cuenta, moneda,
atribución, evento y período siempre quedan separados.

Los campos obligatorios vacíos, NaN, infinito y valores negativos se rechazan. Impresiones
y clics son enteros; conversiones permiten fracciones. Valor ausente en cualquier fila
del grupo invalida el ROAS del grupo, evitando completar ingresos desconocidos con cero.
Cero explícito es un valor conocido. No calcula CVR, alcance, beneficio ni incrementalidad.
No aplica cambios de campaña y no convierte moneda.

El [CSV de ejemplo](../assets/report-example.csv) contiene datos sintéticos para mostrar
el formato; no representa ninguna cuenta ni benchmark. Adapta moneda/evento a la cuenta.

## Registro de experimento

| Campo | Contenido |
|---|---|
| Hipótesis/ID | Qué mecanismo se espera y por qué |
| Evidencia de partida | Fuente, período, población y limitaciones |
| Variable | Una variable interpretable o diseño multivariable justificado |
| Comparador | Control y asignación; describir sesgos si no aleatorio |
| KPI/guardrails | Negocio, calidad, límite de pérdida y presupuesto |
| Criterio de revisión | Volumen/ventana acordados según retraso y efecto esperado |
| Resultado | Observado, incertidumbre y cambios concurrentes |
| Decisión | Adoptar, descartar, continuar o inconcluso |
