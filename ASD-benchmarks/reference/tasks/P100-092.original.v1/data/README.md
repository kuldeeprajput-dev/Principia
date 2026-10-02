# Inputs and observations

Source: [authoritative dataset record](https://zenodo.org/records/14548531). Identifiers: 10.5281/zenodo.14548531. Source terms: cc-by-4.0. Exact source-asset hashes and URLs are in `../rules.json`.

`inputs.csv.gz` contains only declared prediction-time features and identity columns. `observations.csv.gz` separately contains held-out responses, group identifiers and native source/sample anchors. These are derived analysis tables from the earlier frozen campaign; source data remain unchanged. `../evidence/predictions.csv.gz` holds the original saved prediction values for the packaged models.

`r0`: initial calibration RSSI, dBm. `channel_contrast=r0-mean_channel(r0)` at the same position/port; `spatial_contrast=r0-mean_position(r0)` at the same port/channel, both dB. `day`: actual elapsed days; `port`: P1–P8; `channel`: 37/38/39; `furniture`: binary. Observations retain native member and source-line anchors and position keys. Output RSSI is dBm; error is dB. There is no independent absolute RF calibration. Two low-count calibration cells remain included. Each cell target is the native burst mean.

Prepared input columns: `r0`, `channel_contrast`, `spatial_contrast`, `port`, `channel`, `day`, `furniture`.

All preprocessing and prior analyses were source-aware. The paired/grouped holdout was respected during the original campaign; these responses are now exposed. The final script only replays fixed parameters. Original acquisition/source audits and row-level timing evidence are preserved in research history.
