# Candidate Scoring Model

Score each serious candidate 0-5. Adjust weights to project context.

| Criterion | Default weight |
|---|---:|
| Framework/version compatibility | 5 |
| Fit for required UI capability | 5 |
| Accessibility quality | 5 |
| Existing-stack compatibility | 5 |
| Maintainability / API clarity | 4 |
| Design customization | 4 |
| Responsive/touch behavior | 4 |
| Performance/runtime cost | 3 |
| SSR/RSC/build compatibility | 4 |
| Design-token/theming support | 3 |
| Ecosystem maturity | 3 |
| Migration cost | 4 |
| License/commercial constraints | 4 |
| Team familiarity | 2 |

## Product-specific weight shifts
- Enterprise/data-heavy: raise complex widgets, tables, forms, i18n, density.
- Marketing: raise visual freedom, animation, performance, content responsiveness.
- Design system: raise tokens, theming, accessibility, cross-product consistency.
- Embedded widget: raise bundle isolation, Web Components compatibility, CSS scoping.
- Long-lived platform: raise maintenance, migration surface, standards alignment.

Never select purely by total score if a hard compatibility or license constraint fails.
