# Source and units audit — P100-095

Source: https://zenodo.org/records/18670232. Redistribution: CC-BY-4.0. Native bytes are hash-checked and never modified.

Target: Next half-hour author-derived turbulent kinetic energy (m2/s2). Inputs: energy [m2/s2]; wind [m/s]; vertical [m/s]; temperature [degC]; gradient [K/m]; sin_direction [unitless]; cos_direction [unitless].

Predict next30-min author-derived TKE from completed previous30-min TKE, mean velocity and two-height temperature gradient. No contemporaneous target variance/covariance inputs. Both intervals RawAnyS2/H2 flags0; predictor MetT0.

Whole ISO weeks. Forward folds week4, weeks7–8, weeks9–10 with all earlier weeks training. March15 onward weeks11–13 confirmation. One mountain station during one winter.

MeanTKE2 is author-derived from turbulent measurements; mean wind/thermal gradients are observational predictors, not mechanical interventions. Flag0 subset can select calmer/instrument-quality regimes; no universal turbulence closure.

Exposure: First January1 source row and input-height/flag metadata inspected. No March15+ TKE values/scores printed.

Every output retains exact native row or NetCDF profile/level anchors. Missing/invalid measurements are excluded explicitly; none are imputed. Quality-screening defines the task, not claimed population coverage. No scientific source values are rewritten.
