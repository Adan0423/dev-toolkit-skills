# Android UI quality gates

Use this checklist before declaring a UI task complete. Apply only gates relevant to the scope, but do not silently skip critical accessibility or build checks.

## Project fit

- [ ] UI stack was identified from the actual project.
- [ ] Existing design-system primitives were reused where appropriate.
- [ ] No unrelated architecture/dependency migration was introduced.
- [ ] New dependencies are necessary and compatible with the project's version strategy.
- [ ] Experimental APIs are disclosed and justified.

## Visual system

- [ ] Color, typography, shape, spacing, and icon treatment are coherent.
- [ ] Light theme reviewed.
- [ ] Dark theme reviewed.
- [ ] Dynamic color behavior is intentional if enabled.
- [ ] Loading, empty, error, disabled, and success states relevant to the screen are designed.
- [ ] No important meaning is communicated by color alone.

## Adaptive behavior

- [ ] Compact phone/window behavior reviewed.
- [ ] Landscape/medium behavior reviewed when relevant.
- [ ] Tablet/foldable/expanded behavior reviewed when relevant.
- [ ] Large/desktop-class window behavior reviewed when relevant.
- [ ] Content is not merely stretched on large screens.
- [ ] Navigation changes appropriately with available space when needed.
- [ ] Multi-window/resizing does not destroy the layout.
- [ ] Hinge/posture concerns handled if foldables are in scope.

## Input

- [ ] Touch targets are appropriately sized.
- [ ] Keyboard focus order works when keyboard input is in scope.
- [ ] Focus indication is visible.
- [ ] Mouse/trackpad click/scroll behavior works for large-screen targets.
- [ ] Hover/context behavior has an accessible/touch alternative where applicable.

## Insets/system UI

- [ ] Status/navigation bar content is legible.
- [ ] No content is unintentionally hidden by system bars/cutouts.
- [ ] IME does not cover required form actions.
- [ ] Insets are not applied twice.

## Accessibility

- [ ] Informative/actionable non-text UI has meaningful semantics.
- [ ] Decorative images/icons do not create accessibility noise.
- [ ] Custom controls expose role/state/action semantics.
- [ ] Touch targets are normally at least 48dp x 48dp for touch use.
- [ ] Increased font scale does not clip critical content.
- [ ] Long/localized strings do not break layout.
- [ ] RTL is not broken by directional assumptions when supported.

## Compose correctness

- [ ] No direct repository/database/network work is performed during composition.
- [ ] State ownership is appropriate.
- [ ] Side effects are explicit and lifecycle-safe.
- [ ] Large lazy collections use stable keys when identity exists.
- [ ] Expensive work is not repeated unnecessarily during recomposition.

## Testing

- [ ] Affected module builds.
- [ ] Relevant unit/UI tests pass when runnable.
- [ ] Important Compose previews exist or were reviewed.
- [ ] Screenshot/golden diffs were reviewed instead of blindly accepted.
- [ ] Any unrun validation is reported as a limitation.
