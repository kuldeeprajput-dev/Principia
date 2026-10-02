# P100-012.original.v1

**Target.** native higher-angle XRR intensity

**Target units.** counts

**Metric kind.** mae

**Timing contract.** Predict higher-angle intensity after measuring a fixed low-angle calibration band of the same spectrum. Position and angle are known acquisition settings.

**Calibration.** Five native intensity samples near2theta1.0deg per spectrum; no other held-out intensity is a predictor. Same calibration for every model.

**Independent unit.** Complete deposition batch is the split unit; wafer is the primary aggregation unit. All positions on a wafer stay together. Three deposition batches develop; fourth confirms.

**Scope limits.** Twelve200mmwafers with65ALDcycles from one process; three confirmation wafers share one deposition run.; Intensity-envelope and fringe parameters are effective metrology surrogates; density/thickness/roughness are not independently identified or verified by the author-fitted SE outputs.; The fixed angle range lies above critical-angle effects; calibrated counts are not absolute reflectivity.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| q | Å⁻¹;4πsin(theta)/lambda |
| q0 | Å⁻¹; calibration mean wavevector |
| I0 | counts; mean at2theta1.0±0.008deg |
| outer | binary noncenter measurement position |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-012.original.v1 --output NEW_SUBMISSION; then score --task P100-012.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
