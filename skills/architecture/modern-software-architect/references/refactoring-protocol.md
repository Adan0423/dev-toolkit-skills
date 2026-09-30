# Protocolo de refactor arquitectónico

1. Captura baseline: build, tests, lint y comportamiento relevante.
2. Define el objetivo estructural y el no-objetivo.
3. Divide el cambio en unidades pequeñas y autocontenidas.
4. Mueve/extrae primero con cambios funcionales mínimos.
5. Ajusta dependencias y contratos.
6. Ejecuta checks.
7. Simplifica duplicación y nombres.
8. Ejecuta checks.
9. Elimina residuos solo con evidencia.
10. Ejecuta checks finales y revisa el diff completo.

Si el repositorio no tiene tests suficientes, crea tests de caracterización para zonas críticas antes de una reestructuración riesgosa.
