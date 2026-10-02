# P100-001.original.v1

**Target.** Twenty-first integer sequence term on the inverse-hyperbolic-sine scale

**Target units.** asinh(integer term)

**Metric kind.** mae

**Timing contract.** Only first16 terms and horizon5 supplied; names, OEIS IDs and published formulas are forbidden predictors.

**Calibration.** Sixteen observed prefix terms per sequence, including confirmation sequences; no suffix term used in rules.

**Independent unit.** Canonical affine-normalized sixteen-term prefix family; semantic relationships not exhaustively known

**Scope limits.** Hash-selected finite-range OEIS reference challenge, not mathematical proof or new sequence discovery. Affine prefix aliases linked; other semantic dependence remains. Finite continuations never uniquely determine a law.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| prefix_json | JSON array of 16 exact integer terms |
| horizon | sequence steps (fixed 5) |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-001.original.v1 --output NEW_SUBMISSION; then score --task P100-001.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
