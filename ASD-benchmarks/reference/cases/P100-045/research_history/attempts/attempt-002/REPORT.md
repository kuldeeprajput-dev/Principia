# Power hardness

A fixed hardness ratio assumes an invariant spectrum. Test a power-law count response allowing hardness to change with excess intensity; the exponent is empirical count-space behavior, not a photon spectral index.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

H_hat=max(0,B_H+1000*a*sign(z)*abs(z)^b); z=(L-B_L)/1000.

Coefficients: [0.8565904675797599, 1.3759982824136165].

## Grouped development evidence

Mean-group MAE 14.264918 counts/s; worst-group MAE 24.3822059. Selected before confirmation.

## Falsification and interpretation

A power response of high-channel excess to low-channel excess improves transfer over fixed hardness, background-ratio and flexible controls. The exponent describes detector count-space hardening across this event, not a deconvolved photon spectrum. Detectors share one incident burst and differ in response and orientation. No independent-event replication, dead-time correction claim or universal hardness–intensity law follows.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-002` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
