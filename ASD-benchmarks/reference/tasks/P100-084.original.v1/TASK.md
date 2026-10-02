# P100-084.original.v1

**Target.** native AFM retraction force

**Target units.** nN

**Metric kind.** mae

**Timing contract.** Predict late retraction after the entire approach and firstfive retraction samples are available. Targets begin at retractionindex16. Measured retraction deflection is excluded because it algebraically determines force.

**Calibration.** Approach baseline, first5nNabovebaselinecrossing, known ramp extent, and initialfive retractionforce samples. Everycandidate receives the same frozen summaries.

**Independent unit.** Complete approach/retraction curve is held together; one hashselectedcurveper surface type confirms. Curves are locations on three samples, not independentmanufacturingbatches.

**Scope limits.** Piezo position is not true indentation; effective contact models are predictive surrogates, not certified elasticmoduli.; No stem-cell response measurements are present in this retained package; no osteogenesis conclusion follows.; Ramp sampling frequency is not resolved; progress is dimensionless and no relaxation time in seconds is inferred.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| x | dimensionless normalized piezo position relative to fixed5nNapproach crossing |
| base | nN; mean first10approachpoints |
| amp | nN; initialretractionlevel minusbase |
| progress | dimensionless fraction ofretractionramp |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-084.original.v1 --output NEW_SUBMISSION; then score --task P100-084.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
