# Modelado conceptual, lógico y físico

## Qué necesita decidirse

Extrae entidades, identidad, pertenencia y ciclo de vida del negocio. Distingue hechos
de supuestos y evita convertir cada pantalla en una tabla. Identifica operaciones y
consultas importantes, con filtros, orden, cardinalidad, frecuencia y crecimiento;
no exige métricas exactas para un primer modelo pequeño.

Anota invariantes: qué no puede duplicarse, qué relación debe existir, quién es dueño,
qué estados/transiciones son válidos y qué debe cambiar atómicamente. Incluye moneda,
zona horaria de negocio, archivos/referencias, retención, privacidad y multiempresa
cuando correspondan. Separar entidad, evento histórico y snapshot evita perder trazabilidad.

## Elección proporcionada

| Necesidad dominante | Modelo a evaluar | Coste/condición a comprobar |
|---|---|---|
| Integridad entre entidades, joins y transacciones | Relacional | Consultas/índices y concurrencia |
| Agregados leídos juntos con estructura variable | Documentos | Tamaño, crecimiento y consistencia de referencias |
| Acceso por clave y patrones conocidos a escala | Clave-valor/DynamoDB | Partición, índices y consultas no previstas |
| Relaciones recorridas de múltiples saltos | Grafo | Recorridos, límites, integridad y coste operativo |
| Eventos/mediciones por tiempo | Series temporales | Retención, cardinalidad, ingestión y agregados |
| Analítica por grandes conjuntos | Almacén analítico/columnar | ETL, frescura y separación del OLTP |

No usa «NoSQL escala / SQL no» ni el lenguaje frontend como argumento. Respeta stack
existente; añadir una segunda base requiere beneficio concreto y plan de consistencia,
operación y recuperación. Redis no es fuente durable por ser rápido: revisa persistencia
y recuperación. La búsqueda/vectorización puede ser un índice derivado, no otro dueño
de la verdad del negocio.

## Tres niveles de salida

1. Conceptual: entidades, relaciones y cardinalidad mínima/máxima; ejemplo 0..N vs 1..N.
2. Lógico: atributos, claves, nullability, dependencias y reglas de validación/acceso.
3. Físico: tipos/DDL o documentos, índices, partición y mecanismos de autorización reales.

Para cada relación especifica dirección de propiedad y qué ocurre al borrar/archivar.
Un N:M con precio, rol o vigencia suele ser entidad asociativa. Una relación opcional
no requiere una tabla independiente si no hay ciclo de vida/reglas propias.

ERD Mermaid o formato editable si aporta; el diagrama no sustituye constraints ni reglas.
Diccionario: columna/campo, tipo, significado, obligatoriedad, default, sensibilidad,
FK/validación, fuente de verdad y responsable de escritura. Marca valores derivados y
duplicación intencional, con mecanismo de actualización.

## Multiempresa y cambios

Decide base/esquema separado o shared tenant según aislamiento, coste y operación.
En shared tenant el vínculo debe preservar pertenencia; no basta un `tenant_id` en
algunas tablas. Una FK compuesta puede impedir referencia a otra empresa, pero no
prohíbe leer sus filas: autorización se verifica aparte.

Para un modelo existente compara requisitos con evidencia del esquema, código, consultas
y migraciones. No elimina tablas/columnas por nombre parecido ni porque un contador
reciente sea cero. Investiga consumidores, retención y uso poco frecuente.

Entrega opciones solo cuando cambien una decisión; recomienda una con motivos y límites.
No diseña sharding, CQRS o EAV de antemano. Si faltan requisitos decisivos, prepara la
parte independiente y pregunta por ellos sin inventar reglas comerciales.
