# Quality Gates

Usa los comandos nativos del proyecto. No inventes herramientas si no están instaladas.

Orden típico:

1. dependency/install integrity;
2. format/check;
3. lint/static analysis;
4. typecheck/compile;
5. unit tests;
6. integration/e2e relevantes;
7. build/package;
8. smoke/startup;
9. security/dependency checks existentes;
10. git diff/status.

Reporta PASS / FAIL / NOT AVAILABLE por gate importante.
