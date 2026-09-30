# Selección de arquitectura

## Regla base

Selecciona la arquitectura más simple que satisfaga requisitos funcionales y no funcionales actuales y deje margen de evolución.

## Señales

### Monolito simple
Adecuado para dominio pequeño, equipo pequeño, despliegue único y baja necesidad de aislamiento.

### Monolito modular
Preferido por defecto cuando el producto crece pero no necesita independencia operativa por servicio. Usa módulos con fronteras y contratos explícitos.

### Vertical slices / feature-based
Útil cuando las features evolucionan de forma relativamente independiente y agrupar por caso de uso mejora localización del cambio.

### Hexagonal / ports & adapters
Útil cuando el dominio necesita aislarse de infraestructura, hay múltiples adapters o alta necesidad de testabilidad.

### Servicios independientes
Exígelos solo con razones como escalado independiente, ownership claro, aislamiento de fallos, ciclos de despliegue distintos o límites de dominio maduros. Incluye el costo de red, observabilidad, consistencia, despliegue y datos.

### Event-driven
Úsalo cuando desacoplamiento temporal, fan-out, integración asíncrona o alto volumen lo justifiquen. Diseña idempotencia, orden, reintentos y DLQ cuando aplique.

## Anti-regla

Nunca elijas una arquitectura solo porque es popular o “enterprise”.
