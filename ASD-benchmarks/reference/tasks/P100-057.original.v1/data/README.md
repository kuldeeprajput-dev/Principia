# Prepared analysis tables and prediction-time contract

`inputs.csv.gz` contains only IDs, groups and declared predictors; `observations.csv.gz` contains separately bound targets. `evidence/sample_anchors.csv.gz` locates native files/members, rows, waveform columns or timestamps. Anchors are evaluation metadata, never additional predictors. Raw source bytes remain unchanged in the benchmark corpus; these tables are explicitly derived pilot products.

Target: **Native dynamic viscosity**, cP. Processing: Parse native numeric rows only; no smoothing, imputation or log-based target exclusion. All temperatures/rates in each Test ID stay together.

T_K is absolute temperature in kelvin; eta is cP. The factor1000 carries kelvin, so9 is dimensionless and represents an effective activation scale9000K. Formulation amplitudes a_f range52.1603–218.5126cP at333.15K; all ten exact values are in rules.json. A shear-rate input is allowed for competitors, but the selected thermal reference does not use it.

Repeated tests of ten already calibrated formulations in one rheometer dataset; no independent synthesis-lot or unseen-loading transfer. Every calibration coefficient in rules.json was trained on development groups. Baseline kernels use the same input access, training-only category encodings/scales/80 centers and nested whole-group or forward-time tuning. Kernel comparison includes both direct response and residual-to-known-baseline forms. Inner chronological folds with no prior inner training group use the first frozen hyperparameter setting. No response-selected outliers are deleted. Missing targets stay assigned but cannot be scored; coverage is explicit. Logit calculations have fixed numerical bounds but source percentages are unchanged. Predictor eligibility may remove rows lacking causal inputs, with all counts retained in source_and_units_audit.json.

Native units: {"formulation": "source label; calibrated category", "T_C": "degC", "shear_s": "s^-1"}. IDs/group labels identify validation units; they are not numerical predictors. Prediction-time history is permitted exactly as declared, including earlier observed responses inside a held-out chronological or packet run. This is conditional online forecasting, not autonomous multi-step rollout.

Final targets are exposed. Do not tune a new method against them and claim fresh confirmation. See the collection instruction.md for fresh experiments and the per-case historical protocol for the original allocation.
