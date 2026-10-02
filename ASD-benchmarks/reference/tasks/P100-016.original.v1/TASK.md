# P100-016.original.v1

**Target.** Next-month seasonally adjusted all-items CPI log change

**Target units.** percentage points per month (100 natural log index ratio)

**Metric kind.** mae

**Timing contract.** Only calendar months through t-1 enter predictors for month t. This is a retrospectively revised and seasonally adjusted bulk snapshot, not an as-issued forecast archive. Calendar lags do not establish historical release availability; the nominal origin is after prior-month releases. No month-t prices/employment or CPI accounting decomposition enters inputs.

**Calibration.** All regression coefficients, centering/scales and flexible centers fit only preceding development blocks. No held-quarter target fitting.

**Independent unit.** Whole calendar quarter; forward chronological development folds and2023-onward confirmation. One national economic system, overlapping lag windows and persistent macro shocks; quarters are not independent economies.

**Scope limits.** 1990–2026 US selected national seasonally adjusted series. Revised historical values and seasonal factors can incorporate later information. No causal Phillips-curve, policy intervention, operational financial-return or structural-inflation law claim.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| inflation1 | percentage points per month (100 log ratio) |
| inflation3 | percentage points per month (100 log ratio) |
| inflation12 | percentage points per month (100 log ratio) |
| housing1 | percentage points per month (100 log ratio) |
| medical1 | percentage points per month (100 log ratio) |
| jobs1 | percentage points per month (100 log ratio) |
| mfg1 | percentage points per month (100 log ratio) |
| info1 | percentage points per month (100 log ratio) |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-016.original.v1 --output NEW_SUBMISSION; then score --task P100-016.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
