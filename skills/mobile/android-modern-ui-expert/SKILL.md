---
name: android-modern-ui-expert
description: Design, create, modernize, review, and repair Android user interfaces in Android Studio. Use for Kotlin/Jetpack Compose UI work, Material 3 and Material 3 Expressive, adaptive layouts for phones/tablets/foldables/desktop-class windows, dark mode, edge-to-edge, Navigation 3, accessibility, previews, UI tests, and Kotlin Multiplatform projects. Always inspect the existing project before changing architecture or dependencies, preserve working business logic, and prefer stable official Android/Kotlin APIs unless experimental APIs are explicitly justified.
metadata:
  author: custom
  version: "1.0.0"
  last-updated: "2026-08-14"
  keywords:
    - android
    - android-studio
    - kotlin
    - jetpack-compose
    - material3
    - adaptive-ui
    - dark-mode
    - accessibility
    - navigation3
    - kotlin-multiplatform
---

# Android Modern UI Expert

## Mission

Create Android interfaces that are modern, native, coherent, adaptive, accessible, performant, maintainable, and faithful to the product's actual requirements.

This skill is not a visual reskinning shortcut. It must understand the project before editing it, choose the smallest technically correct modernization path, implement the UI, verify behavior on representative form factors, and report what changed.

Use official Android and Kotlin guidance as the primary source of truth. When current API versions, deprecations, Android Studio behavior, or library compatibility matter and internet access is available, verify them against official documentation instead of guessing.

Read `references/source-map.md` when current Android/Kotlin guidance or API selection needs verification. Read `references/ui-quality-gates.md` before final validation.

## Non-negotiable rules

1. **Inspect before editing.** Never assume the project uses Compose, Material 3, Navigation 3, Hilt, KMP, a version catalog, or any particular architecture.
2. **Do not break business logic to improve appearance.** Preserve domain logic, permissions, persistence, networking, authentication, and navigation semantics unless they are explicitly in scope.
3. **Prefer stable APIs.** Use stable AndroidX/Kotlin APIs by default. Alpha, beta, experimental, or opt-in APIs require a concrete benefit and must be clearly disclosed. If a stable alternative satisfies the requirement, use the stable alternative.
4. **Do not invent versions.** Reuse the project's BOM/version catalog/version strategy. If a dependency must be added, verify the current compatible release when possible.
5. **Do not duplicate entire screens for phone/tablet.** Build one adaptive experience whose layout changes with available window space, posture, and input method.
6. **Do not hard-code a design to one screenshot size.** Avoid fixed widths/heights whose only purpose is to make one preview look correct.
7. **Dark mode is a first-class state.** Unless the product explicitly forbids it, verify both light and dark themes and system theme switching.
8. **Accessibility is part of correctness.** A visually attractive screen that cannot be understood or operated accessibly is incomplete.
9. **Edge-to-edge and insets must be intentional.** Never hide content behind system bars, display cutouts, IME, or navigation regions.
10. **Keep composables focused.** UI code must not make direct database or network calls. Separate UI state, events, and side effects from rendering.
11. **Never expose secrets.** Do not print, move into UI code, document, or commit API keys, signing credentials, tokens, service-account secrets, or private configuration.
12. **Finish with verification.** Build the affected module and run the relevant tests when tools permit. Never claim validation that was not actually performed.

## Operating modes

Determine the mode from the codebase before making changes.

### Mode A — Existing Compose project

Modernize the existing design system and screens without unnecessary architecture churn. Reuse current tokens, components, navigation, dependency injection, and state-management conventions when they are sound.

### Mode B — Existing Views/XML project

Do not silently rewrite the whole app in Compose. Decide between:

- improving the requested screen in the existing View system,
- incrementally introducing Compose for a bounded screen/component,
- or proposing a Compose migration when the user explicitly requests modernization at that scope.

If a dedicated XML-to-Compose skill is installed, prefer delegating broad migration mechanics to it.

### Mode C — New Android project or new feature surface

Prefer Kotlin + Jetpack Compose + Material 3. For new Compose navigation architecture, prefer current stable Navigation 3 when compatible with the project and task. Keep module count proportional to product complexity; do not create enterprise-style layers for a trivial app.

### Mode D — Kotlin Multiplatform project

Only activate KMP-specific decisions when KMP is already present or explicitly requested. Decide separately whether to share:

- business logic only,
- data/domain layers,
- or UI with Compose Multiplatform.

Do not force shared UI when platform-native UX differences are important. Keep Android-specific integrations in the appropriate source set.

## Phase 0 — Understand the request

Before touching code, determine:

- target screen(s) or flow,
- whether the goal is creation, redesign, modernization, repair, or review,
- target devices/form factors,
- visual/brand constraints,
- required behavior and states,
- whether screenshots, mockups, Figma references, or an existing design system are authoritative,
- whether architecture/dependency migration is in scope.

If the user provides a visual reference, treat it as a product requirement, not permission to discard native Android behavior or accessibility.

## Phase 1 — Inspect the project

Inspect the smallest set of files needed to establish ground truth. Typical targets include:

- `settings.gradle.kts` / `settings.gradle`
- root and module `build.gradle.kts` / `build.gradle`
- `gradle/libs.versions.toml`
- `gradle.properties`
- `AndroidManifest.xml`
- app/module source structure
- theme/color/type files
- navigation setup
- representative screens and reusable components
- ViewModels/state holders
- existing previews and tests
- KMP source sets when present

Identify and record:

1. Android Gradle Plugin strategy and Gradle wrapper.
2. Kotlin version strategy and Compose compiler configuration.
3. `compileSdk`, `targetSdk`, `minSdk` where relevant.
4. UI toolkit: Compose, Views, or hybrid.
5. Material version/system.
6. Navigation system and back-stack ownership.
7. Theme implementation, dynamic color behavior, dark mode, typography, shapes.
8. Existing design-system module/components.
9. Adaptive-layout support and large-screen behavior.
10. Edge-to-edge/inset handling.
11. Accessibility semantics and localization patterns.
12. Test strategy: unit, Compose UI, screenshot, instrumentation, macrobenchmark.
13. KMP/CMP structure, if any.

Do not modify dependencies until this inspection is complete.

### Required pre-edit summary

Before large changes, internally establish:

- **Current UI stack**
- **Problems detected**
- **Constraints that must be preserved**
- **Modernization path**
- **Files likely to change**
- **Risks**

For a small localized change, keep this reasoning concise; for a full redesign, make it explicit in the response.

## Phase 2 — Define the UI strategy

### 2.1 Preserve product identity

If the project already has brand colors, typography, logos, spacing conventions, or component primitives, extend them instead of replacing them with arbitrary trendy visuals.

Do not use random gradients, glassmorphism, excessive blur, oversized corner radii, or animation merely to make the interface look "modern". Every visual treatment must improve hierarchy, affordance, feedback, readability, or brand expression.

### 2.2 Prefer Material 3 foundations

For Compose work, prefer Material 3 components and `MaterialTheme` as the default foundation.

Model the design system with tokens for at least:

- color scheme,
- typography,
- shapes,
- spacing/layout rhythm when the project benefits from it,
- elevation/container treatment,
- iconography conventions,
- motion conventions.

Use Material 3 Expressive only when the installed stable APIs support the needed component/style and the product benefits from its stronger motion/shape/typographic expression. Do not convert a restrained productivity UI into an expressive UI without a product reason.

### 2.3 Dynamic color

Dynamic color may be supported when compatible with product branding. If branding must remain exact, keep a branded scheme as the default and make dynamic color opt-in or omit it.

### 2.4 Dark mode

Dark mode must be designed, not inverted mechanically.

Verify:

- readable foreground/background contrast,
- icons and illustrations remain visible,
- disabled/secondary content is distinguishable,
- surfaces have intentional hierarchy,
- system bars match the active theme,
- dialogs/sheets/snackbars remain legible,
- destructive/success/warning colors remain understandable,
- screenshots/previews include both light and dark variants.

Do not default every dark theme surface to pure black unless the design specifically calls for it.

## Phase 3 — Build adaptive layouts

Design for the **current window**, not a device-name assumption. Android apps can be resized, split-screen, freeform, folded/unfolded, or run on desktop-class environments.

### 3.1 Compact windows

Typical priorities:

- single primary content pane,
- bottom navigation when appropriate,
- touch-first controls,
- full-screen detail destinations when content benefits from focus,
- concise app bars and actions.

### 3.2 Medium/expanded/large windows

Use extra space to improve productivity rather than merely stretching components.

Consider:

- navigation rail or drawer,
- list-detail or supporting-pane patterns,
- adaptive grids,
- side-by-side filters/details,
- bounded content widths for reading/forms,
- persistent secondary actions where useful.

Avoid full-width text fields, dialogs, cards, or paragraphs that become uncomfortably wide on tablets/desktop windows.

### 3.3 Adaptive navigation

When Material 3 Adaptive is already available or is an appropriate stable addition, use adaptive navigation primitives such as `NavigationSuiteScaffold` so navigation can switch between bar/rail/drawer behavior based on the window.

For projects using Navigation 3, use its current stable patterns for back-stack ownership and, where appropriate, adaptive scene strategies for multi-pane experiences.

Do not migrate a stable existing navigation architecture only to satisfy fashion. Navigation migration must solve a real requirement or be explicitly requested.

### 3.4 Lists and grids

For large collections:

- use lazy layouts,
- provide stable item keys when identity exists,
- use adaptive grid cells when card/list content benefits from additional columns,
- keep readable minimum item widths,
- do not cram content into extra columns solely because space exists.

### 3.5 Foldables and posture

When the app targets foldables or the current libraries expose posture/hinge information, avoid placing critical controls under a hinge/fold and consider dual-pane layouts where they improve the task.

### 3.6 Keyboard, mouse, trackpad, and desktop-class input

For large-screen/ChromeOS/desktop-style use cases, verify:

- Tab and directional focus behavior,
- visible focus indication,
- click and scroll behavior,
- hover states where useful,
- text selection,
- conventional keyboard shortcuts when the workflow benefits,
- right-click/context actions only when they have a discoverable alternative.

Touch remains supported even when precise pointing devices are present.

## Phase 4 — Edge-to-edge and system UI

For modern Android targets, treat edge-to-edge as a baseline layout concern.

- Use the project's current supported edge-to-edge setup.
- Apply system-bar, display-cutout, navigation, and IME insets intentionally.
- Do not stack duplicate padding from both `Scaffold` and manual insets.
- Verify scrollable content under transparent system bars.
- Verify bottom actions and text fields when the keyboard is visible.
- Keep status/navigation bar icon appearance synchronized with theme/background.

If targeting Android 15/API 35 or newer behavior, remember that edge-to-edge can be enforced; verify the current official guidance before implementing compatibility work.

## Phase 5 — Components and screen states

Every screen must define the states relevant to its data and permissions. Do not design only the ideal success state.

Consider:

- loading,
- empty,
- populated,
- partial content,
- recoverable error,
- unrecoverable error,
- offline,
- permission required/denied,
- unauthenticated/expired session,
- disabled action,
- destructive confirmation,
- success feedback.

Use skeletons only when they improve perceived continuity; a progress indicator is often clearer for short or indeterminate waits.

### Forms

Forms must provide:

- persistent labels where ambiguity would occur,
- validation near the relevant field,
- correct keyboard/IME options,
- focus order,
- password visibility controls where applicable,
- enabled/disabled/loading submit behavior,
- no data loss on ordinary configuration changes,
- clear server-side error mapping.

Do not encode validation only with red color.

## Phase 6 — State and Compose architecture

Prefer unidirectional data flow.

A screen should generally receive immutable UI state and event callbacks. Keep business state in an appropriate state holder such as a ViewModel when the project uses that pattern.

Guidelines:

- keep presentational composables as stateless as practical,
- use `remember` for local ephemeral UI state,
- use `rememberSaveable` when local UI state should survive recreation and is suitable for saving,
- collect lifecycle-aware flows using the project's recommended AndroidX lifecycle APIs,
- keep one-off effects explicit,
- never launch uncontrolled repeated work from recomposition,
- never access repositories/database/network directly from a leaf UI composable.

Do not add a ViewModel merely because a component has a boolean expanded state.

## Phase 7 — Accessibility and inclusive UI

Accessibility is a release gate.

### Semantics

- Add meaningful semantics/content descriptions to actionable or informative non-text elements.
- Decorative imagery should not create useless TalkBack noise.
- Use semantic roles/state descriptions for custom controls.
- Merge or clear semantics intentionally for compound components.

### Touch and pointer targets

For touch interfaces, interactive targets should normally provide at least a 48dp x 48dp target area. Built-in Material components often enforce this; custom controls must be checked explicitly.

### Text and scaling

- Use `sp`/theme typography for text.
- Do not clip content at larger system font scales.
- Avoid fixed-height text containers that break when text expands.
- Test long labels and localization expansion.

### Contrast and meaning

- Maintain sufficient text/icon contrast.
- Never communicate status only by color.
- Provide text/icon/state alternatives for error, warning, success, selection, and disabled states.

### Navigation and focus

- Ensure logical focus order.
- Ensure dialogs/sheets manage focus predictably.
- Ensure custom gestures have accessible alternatives.

### Internationalization

- Use string resources instead of hardcoded user-facing strings.
- Respect RTL layouts where supported.
- Avoid concatenated UI strings that translators cannot reorder correctly.

## Phase 8 — Performance-conscious UI

Optimize only after identifying a likely issue, but avoid known anti-patterns from the start.

- Use lazy containers for large scrolling data sets.
- Supply stable keys when available.
- Avoid expensive work in composition.
- Hoist calculations when they do not depend on frequently changing state.
- Avoid recreating heavyweight objects every recomposition.
- Use `derivedStateOf` only when it actually reduces unnecessary updates.
- Keep animation scope bounded and avoid animating expensive layout work without need.
- Load and size images appropriately; do not decode full-resolution media for tiny thumbnails.
- Respect existing baseline-profile/macrobenchmark infrastructure.

If a performance regression is suspected, measure it. Do not claim a recomposition or startup optimization without evidence.

## Phase 9 — Previews and visual verification

Create or update previews for reusable components and important screens when the project uses Compose previews.

Representative preview matrix:

- phone compact,
- landscape/medium window when relevant,
- tablet/foldable expanded,
- desktop-class large window when relevant,
- light theme,
- dark theme,
- increased font scale,
- long/localized content,
- loading/empty/error states.

Use `@Preview` multipreview annotations to reduce duplication where useful.

If screenshot testing is configured, add coverage for visually important states and form factors. Official Compose Preview Screenshot Testing is a strong option for Android-target Compose UI; check current limitations before applying it to non-Android KMP targets.

Do not overwrite approved golden/reference screenshots automatically after a failure. Review the diff first.

## Phase 10 — Functional UI testing

Use semantics-driven Compose UI tests instead of brittle coordinate-based tests when possible.

Test the behavior that matters, such as:

- navigation destination changes,
- selected state,
- form validation,
- enabled/disabled state,
- expanding/collapsing content,
- error and retry,
- accessibility labels/roles where critical.

Do not test implementation details that are invisible to users unless they represent a regression risk.

## Phase 11 — Kotlin Multiplatform / Compose Multiplatform

When KMP is active:

1. Inspect source sets and supported targets.
2. Determine whether UI is Android-only or shared with Compose Multiplatform.
3. Keep platform services behind appropriate abstractions.
4. Reuse shared UI only when behavior and design are genuinely cross-platform.
5. Preserve platform-native expectations for navigation, system integration, permissions, keyboard behavior, and windowing.
6. Verify library support per target before moving dependencies into `commonMain`.

Do not assume every AndroidX library is supported on every KMP target. Verify the current support matrix.

## Phase 12 — Multidevice experiences

Distinguish **adaptive UI across form factors** from **cross-device interaction**.

Do not add Nearby, Cast, cross-device SDKs, account transfer, or other multidevice communication APIs merely because the app supports tablets or wearables. Use cross-device APIs only when the product flow explicitly spans multiple devices.

If the requested experience does span devices, first define ownership of session/state, handoff behavior, privacy, connectivity failure behavior, and which device is authoritative.

## Phase 13 — Implementation discipline

When editing an existing project:

- make small coherent commits/changes when tools support it,
- reuse existing naming/package conventions,
- remove obsolete UI code only after references are gone,
- avoid parallel duplicate design systems,
- avoid adding a third-party dependency for something AndroidX already solves adequately,
- do not change unrelated formatting or architecture,
- keep previews/test fixtures out of production behavior,
- use resources for strings/dimensions/assets when appropriate.

When MCP/IDE/file tools are available, use them to inspect actual project files and build output rather than inferring project state from filenames alone.

## Phase 14 — Build and verify

Choose commands from the actual project structure. Examples are illustrative only.

Potential checks:

- compile/assemble the affected Android module,
- run relevant unit tests,
- run Compose UI/instrumentation tests when an emulator/device is available,
- run screenshot validation when configured,
- inspect lint output for the affected scope,
- manually review previews for the target matrix.

On Windows, use the project wrapper appropriate for Windows; on Unix-like systems use the corresponding wrapper. Never replace the project's wrapper with a system Gradle installation just for convenience.

If a check cannot run because an emulator, SDK, secret, backend, or tool is unavailable, state that limitation precisely.

## Completion report

After implementing the work, provide a concise report with:

1. **What was changed** — screens/components/themes/navigation/adaptive behavior.
2. **Why** — product and Android rationale.
3. **Files changed** — important paths only.
4. **Dependencies/config changes** — exact additions/removals, if any.
5. **Adaptive behavior** — compact vs expanded behavior.
6. **Dark mode/accessibility** — what was verified.
7. **Validation performed** — build/tests/previews actually run.
8. **Remaining issues** — only real unresolved risks or follow-ups.

Do not say "production ready" solely because the project compiles.

## Anti-patterns to reject

Reject or refactor these patterns when encountered in scope:

- one fixed pixel-perfect layout for every screen size,
- tablet UI that is just a stretched phone UI,
- duplicated phone/tablet screen trees with drifting business logic,
- direct API/database calls from composables,
- hardcoded user-facing strings,
- color-only status indication,
- clickable icons with tiny hit targets,
- missing dark-theme validation,
- custom controls without semantics,
- nested scroll containers that fight each other without a clear reason,
- unkeyed large lazy lists with unstable item identity,
- heavy image decoding for thumbnails,
- automatic golden screenshot replacement after failures,
- dependency/version upgrades unrelated to the requested UI task,
- introducing experimental APIs with no disclosed need,
- forcing KMP or Navigation migration without product/technical justification.

## Source priority

When guidance conflicts, prefer sources in this order:

1. Current `developer.android.com` documentation and AndroidX API/release notes.
2. Current official `android/skills` guidance for agent workflows.
3. Current `kotlinlang.org` / JetBrains Kotlin Multiplatform documentation.
4. Official Android sample repositories such as `android/nowinandroid`.
5. Third-party material only when official sources do not answer the question, and clearly mark it as secondary.

Use the source list in `references/source-map.md` for the main documentation families reviewed when this skill was created.
