# Inputs and observations

Source: [authoritative dataset record](https://zenodo.org/records/17282065). Identifiers: 10.5281/zenodo.17282065. Source terms: Creative Commons Attribution 4.0 International (CC BY 4.0). Exact source-asset hashes and URLs are in `../rules.json`.

`inputs.csv.gz` contains only declared prediction-time features and identity columns. `observations.csv.gz` separately contains held-out responses, group identifiers and native source/sample anchors. These are derived analysis tables from the earlier frozen campaign; source data remain unchanged. `../evidence/predictions.csv.gz` holds the original saved prediction values for the packaged models.

`throughput_Gbps`: Gb/s; `packet_bytes`: bytes; `router`: A or B. `sample_id` combines native filename and CSV row; `group` is the complete run. Power targets are in W. These are original current-traffic measurements copied by exact row anchor; no response is used to construct a predictor.

Prepared input columns: `router`, `throughput_Gbps`, `packet_bytes`.

All preprocessing and prior analyses were source-aware. The paired/grouped holdout was respected during the original campaign; these responses are now exposed. The final script only replays fixed parameters. Original acquisition/source audits and row-level timing evidence are preserved in research history.
