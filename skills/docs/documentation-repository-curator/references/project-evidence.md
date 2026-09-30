# Project evidence hierarchy

When documentation sources conflict, prefer evidence in this rough order for the specific claim:

1. executable source/configuration used by the current build/runtime
2. package/dependency manifests plus lockfiles
3. CI/CD and deployment configuration
4. tests
5. current canonical docs
6. stale/duplicate docs
7. comments/TODOs
8. assumptions (avoid)

For architectural intent, ADRs and explicit maintainer documentation can outrank code when they describe an in-progress migration. State that distinction clearly.

## Examples

- README says npm, but `packageManager` and lockfile establish pnpm -> document pnpm.
- README says PostgreSQL, but current runtime config and migrations use SQLite -> flag contradiction and document actual state after verification.
- package.json includes a UI library but source never imports it -> do not present it as core stack without further evidence.
