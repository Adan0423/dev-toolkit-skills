# README quality rules

A strong README answers, quickly:

1. What is this?
2. Why would I use it?
3. Who is it for?
4. What does it need?
5. How do I run it?
6. How is it structured?
7. Where is deeper documentation?
8. What is its current status?

## Badges

Prefer a small, truthful set. A badge row with 15 technologies is usually worse than a readable stack section.

## Stack presentation

Use categories only when they exist. Example:

| Layer | Technologies |
|---|---|
| Frontend | ... |
| Backend | ... |
| Data | ... |
| Infra | ... |
| Tooling | ... |

## Structure tree

Show key paths only. Do not dump thousands of files.

Comment paths with responsibility, e.g.:

```text
src/
├── api/          # HTTP/API boundary
├── domain/       # Core business rules
└── workers/      # Background jobs
```

## Images

A real screenshot often communicates more than decorative artwork. Prefer relevant visuals with alt text.
