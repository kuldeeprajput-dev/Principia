# P100-056.original.v1

**Target.** applied force

**Target units.** kN

**Metric kind.** mae

**Timing contract.** Given current imposed displacement, concrete class, and beam-specific initial force-displacement calibration prefix through≤10mm; no later force or failure capacity allowed.

**Calibration.** Given current imposed displacement, concrete class, and beam-specific initial force-displacement calibration prefix through≤10mm; no later force or failure capacity allowed.

**Independent unit.** Whole beam; six beams in two concrete classes

**Scope limits.** Four development beams and two confirmation beams. Header audit exposed confirmation first11points (all below10mm); these are permitted calibration only. All late damage rows retained.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| deflection_mm | mm |
| calibration_deflection_mm | mm |
| calibration_force_kN | kN |
| initial_stiffness_kN_mm | kN/mm |
| recent_stiffness_kN_mm | kN/mm |
| lightweight | 1 |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-056.original.v1 --output NEW_SUBMISSION; then score --task P100-056.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
