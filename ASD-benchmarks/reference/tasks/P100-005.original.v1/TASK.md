# P100-005.original.v1

**Target.** Exact maximum stable-set cardinality

**Target units.** vertices

**Metric kind.** mae

**Timing contract.** Full graph adjacency is permitted; certificate facet coefficients and published ranks are forbidden predictors.

**Calibration.** None for deterministic bounds; source-independent exhaustive bitset search supplies labels. Labels are computable mathematical invariants, not physical measurements.

**Independent unit.** Source certificate implication family; author-certified graphs and linked edge subgraphs remain together

**Scope limits.** Finite selected source graphs, not theorem proving for arbitrary graphs or rediscovery of source LS+ ranks. Exact search comparator defines attainable error, so approximate bounds cannot claim superior accuracy.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| graph6 | graph6 encoding of an undirected labeled graph |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-005.original.v1 --output NEW_SUBMISSION; then score --task P100-005.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
