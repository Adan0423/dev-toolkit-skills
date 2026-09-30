# Database Performance Review

## Baseline

| Query ID | Calls | Avg | p95 | Rows | Plan | Notes |
|---|---:|---:|---:|---:|---|---|

## Query budgets

| Endpoint/Job | Max rows | Max page | Max query time | Max queries/request | Batch |
|---|---:|---:|---:|---:|---:|

## Connection budget

- Pool:
- Max connections:
- App instances:
- Workers:
- Reserved admin connections:
- Saturation threshold:

## Optimizations

| Query | Change | Before | After | Improvement | Regression risk |
|---|---|---:|---:|---:|---|

## Index changes

### Added

### Removed

### Candidates only

## Timeouts

- statement:
- lock:
- idle transaction:
- transaction:

## Verification

- EXPLAIN:
- statistics:
- load test:
- correctness:
- rollback:
