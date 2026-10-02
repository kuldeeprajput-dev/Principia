# Frozen scoring cohort

Interpolated time-average streamwise wake velocity (m/s). Independent unit: whole control setting across turbines and downstream sections. Source-native lidar-derived uu grids; grid cells are correlated interpolated products. Raw vlos retained upstream. Rotor-equivalent wind and virtual turbine power are excluded as targets and predictors. No cubic-power identity is counted as a rule. ABL Type II only.

Geometry and actuation settings only; no reserved velocity or rotor-equivalent speed is a predictor.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. Only four controls and one wind-tunnel system; three development controls and one reserved. Spatial errors describe field interpolation/transfer, not independent grid replicates.
