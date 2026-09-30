# Decision Matrix — SQL vs NoSQL

## SQL / PostgreSQL

Elegir cuando:
- integridad y constraints importan;
- relaciones son importantes;
- hay transacciones multi-entidad;
- reporting y joins son habituales;
- se necesita flexibilidad de consulta.

## Document / MongoDB

Elegir cuando:
- agregados se leen juntos;
- estructura documental cambia;
- embedding reduce joins reales;
- relaciones complejas no son el centro.

## Key-value / DynamoDB

Elegir cuando:
- access patterns son conocidos;
- clave define el acceso;
- alta escala horizontal;
- se puede diseñar partition/sort key.

## Graph

Elegir cuando:
- recorridos de relaciones son el problema principal.

## Time-series

Elegir cuando:
- datos se organizan principalmente por tiempo;
- retención/rollups dominan el workload.

## Hybrid

Solo cuando cada motor resuelve un problema claramente distinto.
No usar múltiples bases para demostrar sofisticación.
