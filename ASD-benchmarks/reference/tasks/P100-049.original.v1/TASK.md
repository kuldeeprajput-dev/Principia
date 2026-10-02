# P100-049.original.v1

**Target.** voltage during current-free relaxation

**Target units.** V

**Metric kind.** mae

**Timing contract.** Issue predictions at120s of each current-free block; only actual samples at or before10/60/120s and completed preceding current pulse are predictors. Targets are nearest native samples to300/600/1200/1800s, tolerance15s.

**Calibration.** Three causal voltage samples per block; no fit to later outcomes. Calibration access is identical for every model.

**Independent unit.** Complete rest block linked to preceding current pulse; all blocks belong to one half-cell, so block summaries are not independent-cell confidence.

**Scope limits.** One Li-graphite half-cell and one GITT campaign; no population transfer or diffusion-coefficient identification.; POCV file is preserved but not used because it has a different protocol.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| t | s |
| t60 | s |
| t120 | s |
| u60 | V |
| u120 | V |
| u10 | V |
| pulse_s | s |
| current | A |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-049.original.v1 --output NEW_SUBMISSION; then score --task P100-049.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
