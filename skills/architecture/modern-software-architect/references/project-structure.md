# Estructura de proyecto

## Principios

- El árbol debe ayudar a responder “¿dónde vive esta responsabilidad?”.
- Prefiere agrupación por dominio/feature cuando evita dispersión.
- Mantén infraestructura y delivery separables del core cuando existe beneficio.
- Limita carpetas genéricas.
- Evita nesting profundo sin semántica.
- No dupliques la misma jerarquía artificialmente en todas las capas.

## Monorepo

Define límites claros de packages/apps/libs, ownership, dependencias permitidas, tooling compartido y caché/build reproducible.

## Polyrepo

Úsalo solo si independencia real de ownership/release supera el costo de coordinación y versionado.

## Shared

Algo va a `shared` únicamente si tiene múltiples consumidores reales y no pertenece conceptualmente a un dominio concreto.
