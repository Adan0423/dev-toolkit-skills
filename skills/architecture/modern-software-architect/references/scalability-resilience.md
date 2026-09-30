# Escalabilidad y resiliencia

## Primero mide el problema

Distingue crecimiento de usuarios, throughput, datos, equipo, despliegues y complejidad.

## Patrones posibles

- scale out;
- stateless workers;
- queues;
- batching;
- partitioning;
- caching;
- backpressure;
- retries con jitter/backoff;
- timeout budgets;
- circuit breaker;
- bulkhead;
- idempotency keys;
- graceful degradation;
- redundancy proporcional al SLO.

## Riesgos

Cada patrón añade tradeoffs. Documenta consistencia, costo, latencia, complejidad operativa y modos de fallo.
