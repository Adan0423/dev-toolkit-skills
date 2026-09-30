# Responsive and container-query strategy

Tailwind responsive variants are mobile-first.

## Viewport breakpoints

Use standard responsive variants for page/layout changes driven by viewport size.

## Container queries

Use `@container` on reusable component wrappers and `@sm:`, `@md:`, etc. on descendants when the component should react to its own available width.

Named containers are useful when nested reusable components must target a specific ancestor container.

## Size containers in v4.3

Use `@container-size` when queries/units depend on both inline and block dimensions, including units such as `cqb`.

## Principle

Viewport queries answer: "How big is the screen?"
Container queries answer: "How much space does this component actually have?"

For portable dashboard widgets/cards/panels, prefer the second when it reduces coupling.
