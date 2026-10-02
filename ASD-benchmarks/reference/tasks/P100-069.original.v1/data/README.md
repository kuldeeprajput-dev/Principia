# Frozen scoring cohort

Lubricant temperature (degree C). Independent unit: whole thermal experiment/run. Original identification and validation folder assignment preserved. First native sample of each 5 s bin used for compact, deterministic low-frequency thermal analysis; no interpolation. Startup TL is permitted calibration. Neither later lubricant temperatures nor their finite differences enter prediction. Source already presents a lubricant-temperature observer.

Causal housing/environment/friction history through current sample plus first lubricant temperature. Exclude t=0 from scoring because it is calibration, not a forecast.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. Five identification runs and eight source validation runs in one gearbox. Initial calibration and measured housing/friction signals are required; no unseen gearbox or sensorless temperature claim.
