# P100-034.original.v1

**Target.** first_pulse_ePSC_magnitude

**Target units.** nA

**Metric kind.** mae

**Timing contract.** After two lower-dose blocks, forecast mean first-pulse current at the three later calcium doses; all animal data linked.

**Calibration.** First-pulse mean across ten sweeps at0.4 and0.75mM per animal. Later1.5/3/6mM targets are excluded from calibration.

**Independent unit.** animal

**Scope limits.** One muscle6 cell per animal, control and mutant. Dose sequence is confounded with time; sweeps are technical repetitions. Author peak measurements, not newly extracted raw-ABF amplitudes.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| calcium | mM |
| mutant | binary |
| low04 | nA |
| low075 | nA |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-034.original.v1 --output NEW_SUBMISSION; then score --task P100-034.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
