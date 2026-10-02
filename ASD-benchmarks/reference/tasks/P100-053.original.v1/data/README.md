# Inputs and observations

Source: [authoritative dataset record](https://zenodo.org/records/16031381). Identifiers: 10.5281/zenodo.16031381. Source terms: cc-by-4.0. Exact source-asset hashes and URLs are in `../rules.json`.

`inputs.csv.gz` contains only declared prediction-time features and identity columns. `observations.csv.gz` separately contains held-out responses, group identifiers and native source/sample anchors. These are derived analysis tables from the earlier frozen campaign; source data remain unchanged. `../evidence/predictions.csv.gz` holds the original saved prediction values for the packaged models.

Torque features `early`, `finding`, `gradient_proxy`, `roughness`, `prev_y`, `prev_early`, `prev_gradient`, `first_y` and `mean_past_y` are in Nm. `usage` and `history_gap` are cycle counts; `left` and `has_history` are binary. Features use the recorded first-forward-crossing policy. `group` is workpiece ID; observations retain native JSON filename, location and timestamp. The target is Nm.

Prepared input columns: `early`, `finding`, `gradient_proxy`, `roughness`, `usage`, `left`, `has_history`, `prev_y`, `prev_early`, `prev_gradient`, `first_y`, `mean_past_y`, `history_gap`.

All preprocessing and prior analyses were source-aware. The paired/grouped holdout was respected during the original campaign; these responses are now exposed. The final script only replays fixed parameters. Original acquisition/source audits and row-level timing evidence are preserved in research history.

`eligibility.csv` preserves all 2,500 assigned operations and their original statuses; the predictor/target tables contain the 2,473 operations with measured target support. No failed target window is filled or extrapolated.
