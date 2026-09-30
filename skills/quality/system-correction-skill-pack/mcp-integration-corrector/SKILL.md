---
name: mcp-integration-corrector
description: >
  Usa MCP y conectores disponibles para diagnosticar y corregir sistemas con estado
  real. Descubre capabilities, tools y resources antes de actuar, separa lectura de
  escritura, respeta permisos, evita inventar resultados y verifica cada cambio
  contra el recurso externo.
version: 1.0.0
language: es
tags:
  - mcp
  - integrations
  - tools
  - resources
  - connectors
  - verification
---

# MCP Integration Corrector

## Objetivo

Usar Model Context Protocol o conectores equivalentes como una capa de observación
y corrección de estado real.

MCP no reemplaza la lógica de autorización de la aplicación.

---

# 1. Descubrimiento obligatorio

Antes de usar una integración:

- descubrir capacidades;
- listar tools;
- listar resources cuando corresponda;
- leer schemas/descripciones;
- identificar operaciones read/write;
- identificar permisos;
- identificar entorno.

Nunca asumir nombres de tools.

---

# 2. Lectura antes de escritura

Secuencia:

```text
DISCOVER
  ↓
READ
  ↓
COMPARE
  ↓
PLAN
  ↓
WRITE
  ↓
READ AGAIN
  ↓
VERIFY
```

Ejemplo:

- leer tabla/schema;
- leer código/migración;
- detectar divergencia;
- aplicar cambio;
- consultar nuevamente;
- ejecutar prueba funcional.

---

# 3. Fuente de verdad

Determina para cada dato:

- código;
- configuración;
- DB;
- storage;
- servicio externo;
- API;
- MCP resource.

Si dos fuentes discrepan, no elijas arbitrariamente.
Identifica cuál debe ser autoritativa.

---

# 4. Operaciones destructivas

No ejecutar directamente sin contexto suficiente:

- delete masivo;
- truncate;
- drop;
- revocación amplia;
- cambio de rol masivo;
- migración destructiva;
- cambio de bucket público/privado;
- overwrite de archivos importantes.

Preparar:
- impacto;
- pre-check;
- backup/rollback;
- operación;
- post-check.

---

# 5. MCP y permisos

El acceso de la herramienta no implica autorización funcional del usuario final.

Ejemplo:
Un MCP puede tener privilegios administrativos sobre una DB.
Eso no significa que debas diseñar la aplicación para que todos los usuarios tengan
esos privilegios.

Usa MCP para inspección/administración según autorización, pero implementa permisos
reales en la aplicación.

---

# 6. Bases de datos vía MCP/conector

Cuando haya acceso:

- inspeccionar schemas;
- consultar tablas;
- revisar funciones;
- revisar policies;
- revisar grants;
- revisar índices;
- ejecutar migraciones autorizadas;
- validar datos.

Nunca imprimir credenciales de conexión.

---

# 7. Storage vía MCP/conector

Verificar:

- bucket;
- access model;
- policies;
- objeto;
- path;
- metadata;
- ownership;
- URL pública o firmada.

No solucionar un problema de acceso elevando todo el bucket a público.

---

# 8. Git / repositorio

Si existe integración con Git:

- leer estructura;
- revisar branch;
- revisar diff;
- modificar archivos;
- ejecutar tests;
- mantener migraciones junto al código.

No incluir secretos en commits.

---

# 9. Errores de integración

Clasificar:

- capability unavailable;
- authentication;
- authorization;
- schema mismatch;
- validation;
- timeout;
- rate limit;
- upstream error;
- stale data;
- partial failure.

No transformar todos los errores en “sin datos”.

---

# 10. Evidencia

Registrar:

- tool utilizada;
- operación;
- recurso;
- resultado resumido;
- cambio aplicado;
- verificación.

Excluir:

- tokens;
- claves;
- cookies;
- secretos;
- datos sensibles innecesarios.

---

# 11. Fallback sin MCP

Si no existe acceso:

- no fingir acceso;
- analizar el proyecto local;
- crear queries/migraciones/parches;
- indicar exactamente qué debe verificarse en el sistema real.
