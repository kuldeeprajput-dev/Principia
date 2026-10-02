# P100-028.original.v1

**Target.** magnitude of native complex USB off-diagonal response

**Target units.** fsu; instrument full-scale units

**Metric kind.** mae

**Timing contract.** Predict conversion response above the two calibration pump strengths; each directedmodepair is calibrated at0,.13,.1402040816pumpunits. Whole strongerpumpmatrices are reserved, not selected edges.

**Calibration.** Native response magnitudes atthreefixedlow/zeropumpconditionsperdirectedmodepair. No highpumpoutcome or targetstandarddeviation is a predictor.

**Independent unit.** Completepumpstrengthmatrix; all156offdiagonaldirectedpairslinked. Oneinstrument/day; strengthlevels are not independent devices.

**Scope limits.** Magnitude in native fsu is not a calibrated dimensionless scattering coefficient; no passivity, quantumfidelity or reciprocity claim is inferred.; Only the purefrequencyconversion13mode experiment is targeted.31modeparametricgain andnumericalinverseproblemproducts remain context,notduplicateindependentobservations.; Finaltenhigherstrengthsettings test within-sweepextrapolation; no hardwaretransfer.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| lo | fsu;lowpumpamplituderesponse |
| hi | fsu;secondcalibrationresponse |
| noise | fsu;zero-pumpresponse |
| r | dimensionless normalizedpumpincrement |
| g | fsu;pumpamplitudecontrol |
| glo | fsu;lowpumpcontrol |
| ghi | fsu;highcalibrationpumpcontrol |
| sep | integer frequency-bin separation;100kHzbins |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-028.original.v1 --output NEW_SUBMISSION; then score --task P100-028.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
