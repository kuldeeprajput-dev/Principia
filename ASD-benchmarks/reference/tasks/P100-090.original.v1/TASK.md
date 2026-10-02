# P100-090.original.v1

**Target.** Mean next-two-second signed angular polarization about instantaneous group centroid

**Target units.** dimensionless signed[-1,1]

**Metric kind.** mae

**Timing contract.** Every predictor uses trajectory rows at/before origin t. Integer positions use previous observed sample only, at most1second stale; current tracked count uses prefix-present IDs, never full-trial future membership. No interpolation from future. Velocities derived by backward1s differences; supplied VX/VY/Pol forbidden because smoothing provenance can include future. Target uses t+1..t+2.

**Calibration.** First2seconds of each trial used as explicit calibration; no future held-group target fit. Whole condition/session A/C/D identifiers keep repetitions linked. Calibration baseline given same prefix access.

**Independent unit.** Whole country/experiment-condition group with all repetitions; participants may recur across conditions and identifiers do not resolve all dependence. One teen condition keptdevelopment, no heldteen generalization.

**Scope limits.** Within-source group-rotation temporal dynamics after observed prefix. Centroid-based XY-derived order differs from authors supplied Pol; no arithmetic identity predicted at same time. Source published conditionmeans already known; confirmation not unseen-world evidence. No novel biological handedness or safety intervention law.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| p_now | dimensionless current signed angular order |
| p_past | previous2integerseconds mean order |
| p_initial | first2seconds mean order, declared pertrialcalibration |
| density | tracked persons/(pi*r90²), proxy persons/m² |
| speed | mean1sbackwardsecant m/s |
| radius90 | 90th-percentile centroiddistance metres |
| polarization_variance | withinframe variance of individual signedorder |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-090.original.v1 --output NEW_SUBMISSION; then score --task P100-090.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
