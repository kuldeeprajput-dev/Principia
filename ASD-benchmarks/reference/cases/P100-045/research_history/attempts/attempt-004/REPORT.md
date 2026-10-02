# Hysteresis

Identical low-energy intensity may have different high-channel responses on rising and falling phases. Add a signed causal low-channel increment to test hysteresis without using high-channel history.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

H_hat=max(0,B_H+a*(L-B_L)+b*(L-L_previous)).

Coefficients: [0.49380825341857093, -0.008144187376717483].

## Grouped development evidence

Mean-group MAE 16.1168335 counts/s; worst-group MAE 25.486255. Preserved alternative; not the selected reference.

## Falsification and interpretation

A power response of high-channel excess to low-channel excess improves transfer over fixed hardness, background-ratio and flexible controls. The exponent describes detector count-space hardening across this event, not a deconvolved photon spectrum. Detectors share one incident burst and differ in response and orientation. No independent-event replication, dead-time correction claim or universal hardness–intensity law follows.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
