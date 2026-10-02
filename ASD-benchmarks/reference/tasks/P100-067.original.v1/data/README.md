# Inputs and observations

Source: [authoritative dataset record](https://data.mendeley.com/datasets/ccm9k8pjft/1). Identifiers: 10.17632/ccm9k8pjft.1. Source terms: CC BY 4.0. Exact source-asset hashes and URLs are in `../rules.json`.

`inputs.csv.gz` contains only declared prediction-time features and identity columns. `observations.csv.gz` separately contains held-out responses, group identifiers and native source/sample anchors. These are derived analysis tables from the earlier frozen campaign; source data remain unchanged. `../evidence/predictions.csv.gz` holds the original saved prediction values for the packaged models.

`width_m`: supplied visible interface width, m; `v_up_m_s`: strict native upstream-window fitted speed, m/s; `orientation_cos2`: upstream mean cos(2θ), dimensionless, with range [-1,1]; `particle`: native particle class; `family`: native configuration family. `group` is complete fluid configuration. Observations contain native trajectory and density file anchors, entry time and last permitted predictor time. Target transit is in s.

Prepared input columns: `width_m`, `v_up_m_s`, `orientation_cos2`, `particle`, `family`.

All preprocessing and prior analyses were source-aware. The paired/grouped holdout was respected during the original campaign; these responses are now exposed. The final script only replays fixed parameters. Original acquisition/source audits and row-level timing evidence are preserved in research history.

The stored field name `orientation_cos2` means mean **cos(2θ)**, not mean cos²θ. The equation converts it using `(1 + orientation_cos2)/2 = mean(cos²θ)`. This notation follows the original extraction and prediction code; no numerical value or fitted coefficient changed.
