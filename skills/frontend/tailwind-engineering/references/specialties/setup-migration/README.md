# Tailwind CSS v4.3 Expert Skill

A reusable agent skill for production-grade Tailwind CSS v4.3 work.

## Scope

- Analyze existing projects before changing UI code.
- Install Tailwind using the correct official integration for the build tool.
- Upgrade Tailwind v4.x projects to v4.3 and plan v3 → v4 migrations.
- Build reusable design systems with `@theme`.
- Apply responsive design and container queries correctly.
- Use v4.3 features such as scrollbar utilities, `@container-size`, `zoom-*`, `tab-*`, improved `@variant`, and functional utility defaults.
- Diagnose missing classes/source detection issues.
- Refactor Tailwind-heavy markup into reusable framework components.
- Validate build, accessibility states, themes, and responsive behavior.

## Important principle

Tailwind is not used as a substitute for architecture. The skill prefers reusable components, clear design tokens, framework conventions, and minimal dependencies.

## Validation

```bash
python scripts/validate_skill.py
```

## Project audit

```bash
python scripts/audit_tailwind.py /path/to/project
```

The audit is read-only. It reports likely Tailwind integration/version clues and legacy v3 patterns; it does not edit files.
