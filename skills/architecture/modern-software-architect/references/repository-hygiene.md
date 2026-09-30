# Repository Hygiene

## Objetivo

Reducir ruido y riesgo sin borrar fuentes necesarias.

## Auditoría

1. Obtén `git status` y baseline.
2. Detecta `.gitignore` y archivos trackeados que deberían ser generados/locales.
3. Clasifica por tipo: source, config, generated, cache, vendor, artifact, docs, runtime data.
4. Busca referencias estáticas y dinámicas.
5. Revisa build/package manifests, CI, Docker, infra y scripts.
6. Usa herramientas del ecosistema para dependencias/código muerto cuando estén disponibles.
7. Prepara candidatos con nivel de confianza.

## Niveles de confianza

- HIGH: generado reproducible, cache, temporal, log, output de build y no requerido por release.
- MEDIUM: asset/script aparentemente huérfano con búsqueda amplia sin referencias.
- LOW: migraciones, snapshots, configs, infra, release scripts, datos, assets dinámicos.

Solo elimina HIGH automáticamente. MEDIUM requiere pruebas fuertes y validación. LOW se conserva salvo evidencia explícita.

## Después de limpiar

- build/test/lint;
- smoke test si aplica;
- `git status` y diff;
- actualizar ignore rules;
- confirmar que no se borraron archivos fuente o deployment-critical.
