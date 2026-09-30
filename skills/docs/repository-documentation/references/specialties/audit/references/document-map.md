# Canonical documentation map

Use this as a decision aid, not a mandatory template.

| Document | Primary responsibility | Create when |
|---|---|---|
| README.md | Entry point, value, setup, navigation | Almost always |
| docs/ARCHITECTURE.md | Architecture, boundaries, data flow, decisions | Architecture is non-trivial |
| docs/PROGRESS.md | Current implementation status | Project benefits from tracked implementation state |
| docs/TODO.md | Prioritized pending work | No stronger canonical task tracker exists or user requests it |
| docs/AGENTS.md | Agent orchestration inventory | Agents/AI tools exist |
| docs/SKILLS.md | Skills/capabilities inventory | Skills/capabilities exist |
| CONTRIBUTING.md | Contributor setup/workflow | Collaborative project |
| CHANGELOG.md | Released changes | Versioned/released project |
| SECURITY.md | Vulnerability reporting/security policy | Public/collaborative/security-sensitive project |
| docs/adr/* | Individual architecture decisions | ADR practice exists or is introduced intentionally |

## Avoid duplication

README should summarize and link. Detailed material belongs in the specialized canonical document.
