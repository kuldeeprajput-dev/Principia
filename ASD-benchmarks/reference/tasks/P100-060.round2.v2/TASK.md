# P100-060.round2.v2

Documentation correction of P100-060.round2.v1. Native values, coefficients, grouping and numerical evidence are unchanged. No new fitting or confirmation.

**Target.** Post-trigger peak voltage with training-condition-normalized error

**Target units.** V

**Metric kind.** normalized_mae

**Timing contract.** Predict post-trigger peak absolute receiver voltage from imposed pulse width, distance, nominal sensor frequency and condition identity. Each response uses the whole t ≥ 0 trace after subtracting its t < 0 mean. No response-selected waveform window, target-based denoising or validation-response calibration is permitted.

**Calibration.** Condition-specific gains, damping/response parameters and any flexible transformations are learned inside each outer training partition. Scoring divides physical absolute errors by the frozen training-only condition scale stored in evaluation/preparation/metadata/60_normalization.json; that scale is evaluator metadata, not an additional prediction input. The 12 µs damping and six gains in the original task describe one historical comparator rather than every round2 model.

**Independent unit.** Complete pulse-width block held across all six distance/sensor conditions; 30 files and 300 pulse outcomes span five original development widths. Pulses within a file and six conditions at a width are dependent.

**Scope limits.** Repeatedly exposed development out-of-fold cohort at pulse widths 2.5, 7.5, 10, 12.5 and 15 µs, distinct from the original reserved 5 µs cohort. Six calibrated distance/sensor conditions come from one setup. Normalized-error comparison limits contact-amplitude dominance but does not establish unseen-sensor or propagation transfer. Fitted effective frequencies fail direct identification as measured resonance.

## Permitted inputs

| Input | Units |
|---|---|
| distance_mm | mm |
| resonance_kHz | kHz; confounded with sensor type |
| width_us | us |
| condition | calibrated distance/sensor label |

Current outcomes are exposed. Alternatives may use the same information budget; different endpoints require a distinct reviewed contract.
