# Modern Software Architect

Skill generalista para arquitectura de software moderna y repositorios limpios.

## Capacidades

- Proyecto existente o desde cero.
- Arquitectura proporcional al problema.
- Monolito, monolito modular, feature-based, hexagonal, clean, servicios, event-driven y otros patrones según contexto.
- Reorganización y refactor de repositorios.
- Detección y limpieza segura de archivos basura.
- Prevención de residuos mediante ignore rules.
- Escalabilidad, resiliencia, seguridad y observabilidad.
- Generación/modificación directa de código.
- Quality gates y validación post-refactor.

## Regla crítica

La skill nunca elimina un archivo solo porque parezca innecesario: primero verifica referencias, build/release/CI, historial y comportamiento; luego valida el proyecto tras la limpieza.

## Validación del paquete

```bash
python scripts/validate_skill.py
```

## Auditoría rápida de un repositorio

El script incluido es conservador y no elimina nada:

```bash
python scripts/audit_repo_hygiene.py /ruta/al/proyecto
```
