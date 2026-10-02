# P100-054.original.v1

**Target.** second bridge failure load Pb2

**Target units.** mN

**Metric kind.** mae

**Timing contract.** Predict measured second-bridge failure load conditional on reported SEM geometry; geometry may be measured post-test, so this is retrospective geometry-conditioned response, not pre-test control.

**Calibration.** Predict measured second-bridge failure load conditional on reported SEM geometry; geometry may be measured post-test, so this is retrospective geometry-conditioned response, not pre-test control.

**Independent unit.** Cantilever specimen; one source wafer and manufacturing campaign

**Scope limits.** Complete specimen identities linked; three C/D/E manufacturing families for development folds. Header specimens C1,C11,C35,C36 forced development; hash allocation ignores all remaining target values. No toughness/author-fitted correction factors or outcome labels as inputs.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| width_um | um |
| thickness_um | um |
| length_um | um |
| notch_depth_um | um |
| notch_width_um | um |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-054.original.v1 --output NEW_SUBMISSION; then score --task P100-054.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
