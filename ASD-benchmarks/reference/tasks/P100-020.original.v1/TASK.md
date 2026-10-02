# P100-020.original.v1

**Target.** SST anomaly at a withheld pixel

**Target units.** degree C

**Metric kind.** mae

**Timing contract.** Retrospective reconstruction of one daily map, using twelve fixed neighboring pixels from the same date. Not a future forecast.

**Calibration.** Cardinal neighbors at4 and8 pixels plus four diagonal neighbors at4pixels. Target centers lie on a40pixel lattice and can never be calibration pixels for any scored center.

**Independent unit.** Complete20degree geographic tile for scoring; all tiles belong to one dependent global map, not independent temporal replicates.

**Scope limits.** Fixed complete-water neighborhoods exclude coasts, ice and missing neighborhoods.; No climate evolution, causal ocean mechanism or coral bleaching hazard is identified. This is not the NOAA coral bleaching heat-stress product.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| hx | degree C |
| hy | degree C |
| ox | degree C |
| oy | degree C |
| dg | degree C |
| gx | degree C |
| gy | degree C |
| clat | dimensionless cosine latitude |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-020.original.v1 --output NEW_SUBMISSION; then score --task P100-020.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
