# Frozen scoring cohort

Chemical potency six hours ahead (source potency unit (undocumented)). Independent unit: whole production batch; chronologically latest 81 reserved. Native hx is the source-loader target. Other undocumented abbreviations are excluded. Source units are not asserted to be mg/L or activity U/mL. 406 independent production batches; rows with exact 6 h lag/horizon only. No target smoothing or imputation. This is a six-hour prediction conditional on an available current potency assay, not an inline soft sensor.

Strictly causal potency history and cultivation clock. Matching plus/minus 6 h uses source clock; future values only become targets.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. One industrial facility and one year; historical operational forecasting, no mechanistic law from unmapped sensors. Earlier batches only train later validation blocks.
