# P100-025.original.v1

**Target.** raw measured FeK-edge μ(E)

**Target units.** dimensionless μ(E)

**Metric kind.** mae

**Timing contract.** Retrospective spectral-shape reconstruction after pre/post-edge calibration bands and experimental segment durations are known. This is not an online state-of-charge forecast.

**Calibration.** Each spectrum contributes only7000–7050eV and7250–7300eV bandmeans. SuppliedmeasuredFePO4/LiFePO4references are normalized identically. Targetband7070–7200eV is withheld.

**Independent unit.** Complete three-acquisitionblock linked to the source3×binnedrepresentation; oneLFPcycleonly. Fivecontiguouschronologicaldevelopmentfolds holdout wholeblocks, withfuturedevelopmentsegments allowed for thisretrospectivecompressiontask.

**Scope limits.** Nominalprogress is normalizedreportedsegmenttime, not measuredstateofcharge or an identifiedphasefraction.; Author3×binned spectra are excluded as duplicateobservations; onlyunbinnedcolumns are targets.; Onecell/onecycle; cross-blockcalibration successdoesnotestablishnewbatterychemistry orindustrialcycletransfer.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| pre | rawμ(E),dimensionless |
| jump | rawμ(E),dimensionless |
| rL | normalizedmeasuredLiFePO4reference |
| rF | normalizedmeasuredFePO4reference |
| dL | eV⁻¹ |
| d2L | eV⁻² |
| f | dimensionlessnominalprotocolprogress |
| discharge | binarydischarge/rest2branch |
| rest | binaryrestsegment |
| e | eVrelative7112 |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-025.original.v1 --output NEW_SUBMISSION; then score --task P100-025.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
