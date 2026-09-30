# Tailwind CSS v4.3 — Responsive & Adaptive Design Standard

## Objective

Build interfaces that adapt across the viewport continuum instead of targeting a short list of named devices. The implementation must remain usable from narrow mobile layouts through tablets, laptops, desktop monitors, and very wide displays.

Do not claim responsiveness merely because `sm:`, `md:`, and `lg:` classes exist. Validate actual layout behavior.

## Non-negotiable responsive rules

1. **Mobile-first base**
   - Unprefixed utilities define the narrow-screen baseline.
   - Layer larger-screen changes with `sm:`, `md:`, `lg:`, `xl:`, `2xl:` only when the content needs them.
   - Do not use `sm:` as a synonym for “mobile”.

2. **Content-driven breakpoints**
   - Prefer the default breakpoint scale unless the layout demonstrably needs another threshold.
   - Choose breakpoints when content stops fitting or hierarchy becomes inefficient, not because a specific phone/tablet model exists.
   - If custom breakpoints are required, define them centrally with `--breakpoint-*` and use consistent units.

3. **Fluid before fixed**
   - Prefer flexible widths, grids, flex layouts, percentages, `minmax`, intrinsic sizing, and `max-w-*` constraints.
   - Avoid fixed widths that cause overflow on narrow screens.
   - Use `min-w-0` on flex/grid children when long content could force unwanted overflow.
   - Use `max-w-*` or readable content bounds on very wide screens so content does not become excessively stretched.

4. **Component-local responsiveness**
   - Use `@container` when a reusable component must adapt to the space it is placed in.
   - Use `@sm:`, `@md:`, `@max-*`, named containers, and arbitrary container ranges only when they improve portability.
   - Use `@container-size` only when block-size/container query length units such as `cqb` or `cqh` are genuinely required.

5. **Viewport metadata**
   - Ensure the application exposes the correct responsive viewport behavior, directly or through the framework's metadata API.
   - For plain HTML/Vite, verify a viewport meta equivalent to `width=device-width, initial-scale=1.0`.

6. **Media and content**
   - Images, video, canvas, embeds, charts, and code blocks must not force the page wider than the viewport.
   - Preserve aspect ratios intentionally.
   - For wide data tables, choose the product-appropriate behavior: responsive column prioritization, stacked/mobile representation, or scoped horizontal scrolling.
   - Never hide critical information only to make a layout fit.

7. **Navigation**
   - Navigation must remain reachable and understandable at narrow widths.
   - Sidebars may collapse, become drawers, or change hierarchy when space is insufficient.
   - Do not shrink desktop navigation until labels become unreadable.

8. **Forms and controls**
   - Inputs, labels, errors, helper text, actions, and validation feedback must fit without clipping.
   - Multi-column forms should collapse when columns no longer have adequate reading/input space.
   - Touch interaction must remain practical on coarse pointers.

9. **Typography**
   - Avoid text sizes or line lengths that become unusable at either extreme.
   - Use responsive scale changes or fluid values only when they improve hierarchy.
   - Long words, URLs, file names, code, and user-generated content must have a deliberate wrapping/overflow policy.

10. **Viewport height**
    - Be careful with full-height layouts on mobile browsers.
    - Prefer dynamic viewport units (`dvh`, `dvw`) when browser UI changes would otherwise clip important content.
    - Do not lock critical content behind a fixed viewport-height shell without tested overflow behavior.

11. **Orientation and input modality**
    - Use `portrait:` / `landscape:` only when orientation changes the experience materially.
    - Use `pointer-coarse:` / `pointer-fine:` when interaction density or hover affordances should adapt to touch versus precise pointers.
    - Hover must be an enhancement, never the only way to discover or trigger essential behavior.

12. **Accessibility under resize/zoom**
    - Do not use Tailwind's CSS `zoom-*` utilities as a substitute for responsive design.
    - Layouts must remain usable when users enlarge browser text/zoom or use accessibility settings.
    - Respect `motion-reduce`, contrast, forced-colors, and focus visibility where applicable.

## Responsive architecture patterns

### Page-level adaptation

Use viewport variants for global page composition:

```html
<main class="grid grid-cols-1 gap-4 lg:grid-cols-[16rem_minmax(0,1fr)] xl:gap-6">
  <!-- navigation + content -->
</main>
```

### Reusable component adaptation

Use container queries when the same component can appear in different shells:

```html
<article class="@container rounded-xl border p-4">
  <div class="grid grid-cols-1 gap-4 @lg:grid-cols-[10rem_minmax(0,1fr)]">
    <!-- media + content -->
  </div>
</article>
```

### Flexible content shell

```html
<div class="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
  <!-- page content -->
</div>
```

Treat these as patterns, not mandatory snippets. Adapt to the product and existing design system.

## Responsive QA matrix

Do not optimize only for exact device presets. Test representative widths plus continuous resizing between them.

Recommended checkpoints when tooling permits:

- 320px — very narrow mobile
- 360px — narrow/common mobile
- 390px — modern mobile
- 430px — large mobile
- 600px — intermediate/narrow tablet region
- 768px — tablet portrait
- 820px — larger tablet portrait
- 1024px — tablet landscape / compact desktop
- 1280px — laptop/desktop
- 1440px — common desktop
- 1536px — Tailwind `2xl` baseline
- 1920px — full HD desktop
- 2560px — large/ultrawide desktop

Also test:

- portrait and landscape where relevant;
- browser zoom/text enlargement where available;
- pointer coarse and pointer fine behaviors where applicable;
- long localization strings and user-generated content;
- empty, loading, error, and maximum-content states;
- open menus, dialogs, popovers, drawers, tables, charts, and forms;
- shared components inside both narrow and wide parent containers.

## Failure conditions

A responsive task is incomplete if any material screen has:

- unexpected root-level horizontal scrolling;
- clipped controls or text;
- inaccessible navigation or actions;
- overlapping content;
- unreadably narrow columns;
- huge unbounded line lengths on wide screens;
- modal/drawer content that cannot be reached;
- fixed elements covering essential content;
- touch controls that depend on hover;
- breakpoint transitions that produce broken intermediate states;
- layout that works only at the exact widths tested.

## Completion rule

Declare responsive work complete only after:

1. narrow-screen baseline works;
2. intermediate widths are stable during continuous resize;
3. tablet and desktop compositions are intentional;
4. ultrawide layout remains readable and bounded;
5. reusable components adapt to their containers when required;
6. no material horizontal overflow exists;
7. keyboard/touch/focus interactions remain usable;
8. build and project quality gates pass.
