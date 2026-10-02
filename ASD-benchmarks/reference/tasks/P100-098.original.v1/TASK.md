# P100-098.original.v1

**Target.** Number of facets of the five-point KRW polytope

**Target units.** facets

**Metric kind.** mae

**Timing contract.** Ten exact pairwise distances permitted; source facets/incidence/f-vector forbidden predictors.

**Calibration.** None for exact geometric algorithms; training-only coefficients for coarse degeneracy heuristics.

**Independent unit.** Source facet-incidence combinatorial type modulo coordinate permutation; all metric representatives of that type stay together

**Scope limits.** Five-point finite source catalog; published theory already characterizes generic types and arrangement. Exact computational reproduction is not a new theorem or independent experimental truth. Exact metric duplicate representations are deduplicated; generic/strict representatives with same coordinate-relabeled facet incidence remain in one group. Incidence-derived family labels are not predictors. Native POINTS and supplied metric vectors can differ by uniform scale; verify exact proportional distance multiset, which preserves facets.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| metric_json | JSON array of 10 positive rational distances; arbitrary common scale |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-098.original.v1 --output NEW_SUBMISSION; then score --task P100-098.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
