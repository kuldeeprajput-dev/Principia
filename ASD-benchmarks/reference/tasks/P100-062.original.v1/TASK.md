# P100-062.original.v1

**Target.** measured anodic permeation current

**Target units.** μA

**Metric kind.** mae

**Timing contract.** Forward extrapolation within two linked permeation traces. Parameters are learned only from earlier chronological blocks; confirmation is the last20% of each trace. Known imposed current step and initial three-point current calibration are permitted.

**Calibration.** Mean first3 native current observations per trace; all candidate families receive identical values. Fit parameters may use development prefixes only.

**Independent unit.** Two chronological traces with no independent specimen identifiers; nonoverlapping temporal blocks are scoring units, not independent specimens. All trace linkage is explicit.

**Scope limits.** The two traces do not establish independent-specimen transfer. Temperature is293K; nominal sheet thickness1.2mm.; Native time zero is used as reported; true boundary concentration and its step timing are not independently measured.; An effective relaxation scale must not be relabeled a unique lattice diffusivity because trapping, boundary kinetics and baseline uncertainty can be confounded.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| t | s since third baseline observation |
| offset | μA; mean first3 observations |
| drive | mA/cm²; imposed cathodic-current step |
| high | binary known high-current condition |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-062.original.v1 --output NEW_SUBMISSION; then score --task P100-062.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
