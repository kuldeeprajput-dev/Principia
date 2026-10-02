# P100-070.original.v1

**Target.** native Bz map ordinate at a withheld pixel

**Target units.** source-native Bz unit (SI conversion unresolved)

**Metric kind.** mae

**Timing contract.** Retrospective reconstruction at one microscopy acquisition; all neighboring measurements are available. No prediction of an earthquake or temperature history.

**Calibration.** Twelve same-map neighbors: cardinal offsets4/8pixels and diagonal4pixels. Centers are20pixel lattice points, none can be a calibration point for another scored center.

**Independent unit.** Two specimens: CSH/119DOA development and CSL/129DOA confirmation. Spatial blocks balance errors but are not independent specimens; development folds are entire200row strips.

**Scope limits.** Native README identifies Bz maps but does not establish numerical SI conversion; scores deliberately remain source-native units.; Temperature profiles, MCMC inversion outputs and maximum-temperature samples are author-derived and excluded as independent targets.; A two-dimensional smooth stencil is not a consequence of the three-dimensional magnetostatic Laplace equation without information about vertical derivatives.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| hx | source-native Bz unit |
| hy | source-native Bz unit |
| ox | source-native Bz unit |
| oy | source-native Bz unit |
| dg | source-native Bz unit |
| gx | dimensionless local contrast |
| gy | dimensionless local contrast |
| lo | source-native Bz unit |
| hi | source-native Bz unit |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-070.original.v1 --output NEW_SUBMISSION; then score --task P100-070.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
