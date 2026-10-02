# Linear hardness

A common spectral shape yields an approximately linear high-channel excess response to low-channel excess across detectors. Test held-detector transfer in observed count space.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

H_hat=max(0,B_H+a*(L-B_L)).

Coefficients: [0.4925556348289837].

## Grouped development evidence

Mean-group MAE 16.0249137 counts/s; worst-group MAE 24.6428209. Preserved alternative; not the selected reference.

## Falsification and interpretation

A power response of high-channel excess to low-channel excess improves transfer over fixed hardness, background-ratio and flexible controls. The exponent describes detector count-space hardening across this event, not a deconvolved photon spectrum. Detectors share one incident burst and differ in response and orientation. No independent-event replication, dead-time correction claim or universal hardness–intensity law follows.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-001` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
