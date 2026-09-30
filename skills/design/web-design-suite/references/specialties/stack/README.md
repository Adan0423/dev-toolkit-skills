# Adaptive Web UI Stack Architect

A reusable Agent Skill that selects web UI technologies based on the project instead of personal preference or popularity.

## What it does
- audits an existing frontend or requirements for a new one
- detects current UI/styling dependencies
- chooses a minimal coherent UI stack
- researches official docs when compatibility is time-sensitive
- avoids duplicate/competing component systems
- plans safe integration or migration
- validates accessibility, performance, responsive behavior, and maintainability

## Typical prompts
- "Choose the best UI stack for this Next.js dashboard and implement it."
- "Audit my frontend dependencies and remove overlapping UI libraries safely."
- "Should this project use Tailwind, Panda, Bootstrap, MUI, AntD, shadcn, or headless primitives?"
- "Pick icons, animation, tables and component primitives for this app based on its requirements."

## Validation
```bash
python scripts/validate_skill.py
python scripts/inspect_frontend_stack.py /path/to/project
```
