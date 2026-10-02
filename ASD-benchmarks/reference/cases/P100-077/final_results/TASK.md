# P100-077.original.v1

**Target.** Joint green-positive and red-positive fraction

**Target units.** percentage points

**Metric kind.** mae

**Timing contract.** Contemporaneous assay diagnostic: green and red marginal positive fractions measured from the same FCS well; joint fraction withheld as target. Marginals do not algebraically determine the joint without an independence/dependence assumption.

**Calibration.** One source BOB negative control defines each channel threshold at its 99.5th percentile, identically for all wells and models. Event gating uses finite scatter/fluorescence and positive FSC-A/SSC-A only; source FlowJo manual gates were not supplied and are not reproduced.

**Independent unit.** Named experimental replicate block A/B/C; three doses within each

**Scope limits.** One hiPSC cell line, one multiplex tagging design, three replicate blocks; same-well marginal readouts are permitted. This tests distributional dependence, not pre-experiment editing yield or a new gene-editing mechanism.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| green | fraction |
| red | fraction |
| dose | source fold dose |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-077.original.v1 --output NEW_SUBMISSION; then score --task P100-077.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
