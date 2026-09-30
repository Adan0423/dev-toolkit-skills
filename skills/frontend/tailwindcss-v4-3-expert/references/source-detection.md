# Source detection

Tailwind v4 detects source files automatically using text scanning and ignores many irrelevant/generated paths by default.

## Explicit source tools

- `@source "..."` — register an otherwise ignored source.
- `source("...")` — set a scan base path on the Tailwind import.
- `source(none)` — disable automatic source detection.
- `@source not "..."` — exclude a path.
- `@source inline("...")` — intentionally generate/safelist utilities.
- `@source not inline("...")` — explicitly exclude utilities.

## Dynamic classes

Bad pattern:

```jsx
<div className={`bg-${color}-500`} />
```

Prefer complete statically discoverable strings:

```jsx
const variants = {
  blue: "bg-blue-500 text-white",
  red: "bg-red-500 text-white",
};
```

Use safelisting only when generation is truly external/dynamic and cannot be represented with complete source strings.
