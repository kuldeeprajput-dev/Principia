# P100-004.original.v1

**Target.** Measured missing transverse momentum magnitude

**Target units.** GeV

**Metric kind.** mae

**Timing contract.** Diagnostic event reconstruction from lepton and jet kinematics; met_phi/met_mpx/met_mpy and truth fields forbidden. Inputs are measured same-event objects, not a pre-collision forecast.

**Calibration.** Training events only; no held-period target calibration.

**Independent unit.** Run period, with unique runNumber+eventNumber observations

**Scope limits.** 2015 four-lepton educational skim, no MC or control background supplied. Object recoil and MET share reconstruction components; predictive agreement is not independent discovery of momentum conservation or new physics.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| scalar_activity | GeV |
| recoil | GeV |
| lepton_recoil | GeV |
| jet_activity | GeV |
| jet_n | count |
| max_lep_eta | dimensionless pseudorapidity magnitude |
| muon_fraction | dimensionless fraction |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-004.original.v1 --output NEW_SUBMISSION; then score --task P100-004.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
