# P100-047.original.v1

**Target.** Adjusted dissolved oxygen at observed nitrate/water-mass state

**Target units.** umol/kg

**Metric kind.** mae

**Timing contract.** Contemporaneous adjusted oxygen diagnostic using independently instrumented nitrate and CTD measurements from the same aligned synthetic profile. No prospective acquisition claim. Adjusted T/S flags1,2,8 permit source interpolation; oxygen/nitrate/pressure flags1,2 only.

**Calibration.** No confirmation target fitting. Causal target histories only for 38/41/95 as explicitly declared.

**Independent unit.** Whole float profiles; rolling half-year tests 2023H2,2024H1,H2,2025H1, earlier times train. July2025 onward reserved. Two serially sampled floats, not hundreds of independent oceans.

**Scope limits.** Author-adjusted, aligned/calibrated products. In-situ-temperature surface oxygen-solubility proxy used for comparison; no potential-temperature or pressure-corrected AOU claim. No causal Redfield stoichiometry from correlated water masses.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| pressure | dbar |
| temperature | degC |
| salinity | psu |
| nitrate | umol/kg |
| float_id | identifier |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-047.original.v1 --output NEW_SUBMISSION; then score --task P100-047.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
