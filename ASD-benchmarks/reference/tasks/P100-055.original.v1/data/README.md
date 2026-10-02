# Frozen scoring cohort

Individual penetration normal force (N). Independent unit: whole mixture across both ages and replicates. Two independent trace columns per mixture/age are retained; source average columns excluded. Time header supplies time, without an explicit unit in the workbook; the native penetration clock unit is unresolved; no physical time constant is claimed. Dimensionless t/t_ref used in equations. Mix-label ratio meanings require author PDF; do not call these stress or yield-stress measurements.

Known mix label, age and elapsed penetration index only; force is never an input.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. Nine mix labels, two batches per mixture/age according to the source PDF, one early research campaign. Force–penetration-time relationships cannot identify intrinsic constitutive stress without probe kinematics/geometry.
