# Quality and accessibility

Tailwind does not replace semantic HTML or interaction design.

## Validate

- visible keyboard focus (`focus-visible`);
- disabled states;
- validation/error states;
- active/selected/current states;
- touch target sizing where relevant;
- text contrast and readability;
- reduced motion where animation exists;
- responsive overflow;
- long content and localization;
- dark/light theme parity;
- high-DPI and zoom behavior when relevant.

## Responsive QA

Test representative widths, but also drag/rescale continuously to catch layout cliffs between breakpoints.

For componentized UIs, validate the same component in multiple parent widths to verify container-query behavior.
