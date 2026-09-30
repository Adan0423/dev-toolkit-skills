# Documentation & Repository Curator

A reusable skill for evidence-based project documentation, README redesign, documentation consolidation, and safe repository cleanup.

## What makes it different

It does **not** start by writing a README. It first audits the real repository, verifies the stack from manifests/config/source, inventories existing documentation, proposes a canonical documentation map, and waits for approval.

It is designed to work globally across languages and project types, including monorepos.

## Key capabilities

- README redesign grounded in the actual project
- Mermaid architecture/data-flow diagrams
- verified Shields.io badges
- optional Skill Icons and repository-local images
- ARCHITECTURE / PROGRESS / AGENTS / SKILLS / TODO / CONTRIBUTING documentation
- environment variable inventory without exposing secrets
- duplicate/stale documentation detection
- safe merge/move/archive/delete proposals
- broken relative-link checks
- conservative repository hygiene
- Spanish/English/document-language adaptation

## Safety model

Destructive cleanup is never automatic from filenames alone. The skill requires evidence and an explicit approval gate before writing, moving, merging, archiving, or deleting documentation.

## Validation

Run:

```bash
python scripts/validate_skill.py
python scripts/audit_docs.py /path/to/project
```

`audit_docs.py` is read-only. It reports documentation inventory and suspicious duplicates/backup-like files; it does not delete anything.
