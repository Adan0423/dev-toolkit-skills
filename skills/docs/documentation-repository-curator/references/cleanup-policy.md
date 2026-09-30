# Documentation cleanup and unification policy

## Goals

- one clear source of truth per topic
- fewer contradictions
- fewer stale setup instructions
- preserved history where history matters
- no destructive cleanup without evidence

## Merge decision

Merge two documents only if they substantially share:
- audience
- purpose
- lifecycle
- ownership

Otherwise cross-link them.

## Deletion confidence

### High confidence candidate
- exact/superseded copy
- no inbound references
- no unique useful content
- no tool/build/legal expectation

### Medium confidence candidate
- mostly duplicate but contains unique fragments
- old screenshots or obsolete setup guide
- uncertain external links

Merge useful content first, then seek approval.

### Never treat as casual deletion
- LICENSE / NOTICE / attribution
- SECURITY.md
- CODEOWNERS
- changelog/release history
- migration history
- legal/compliance docs
- generated files required by publishing/build systems
