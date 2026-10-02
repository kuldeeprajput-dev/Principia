# Frozen scoring cohort

Storage modulus G prime (Pa). Independent unit: whole temperature sweep. Native DFS text exports only; paired TAD exports are linked duplicates, not independent samples. Target storage modulus and secondary loss modulus are separate native instrument outputs, though both share systematic calibration. No compliance correction was applied by the authors. A single purchased polymer batch.

Temperature and imposed frequency only. Loss modulus is withheld as an orthogonal mechanistic check; never a primary predictor.

inputs.csv.gz contains IDs and permitted predictors only; observations.csv.gz contains the corresponding measured/author-derived target. Native anchors are in native_anchors.csv.gz; source hashes are in SOURCE_ASSETS.json. Missing native targets remain missing and cannot be manufactured into zeros. Startup calibration for the gearbox is explicitly unscored. All targets are now exposed for future agents. Temperature transfer within one material; no batch-to-batch or general polymer law claim. Positive modulus spans orders of magnitude.

Three native G-prime readings are negative (source/instrument response). They remain unchanged in observations.csv.gz. Log error is defined for 32 positive responses; physical MAE/RMSE/bias retain all 35. This eligibility/reporting correction was made after confirmation was opened; it changes no selected model, coefficient or saved prediction.
