# Saturation

An intensity-dependent spectral response can look like saturation. Test a nonnegative saturating excess model against the power law, and inspect boundary parameters rather than asserting detector saturation from fit alone.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

H_hat=B_H+a*max(L-B_L,0)/(1+max(L-B_L,0)/c).

Coefficients: [0.5146116245557677, 9999999.999865348].

## Grouped development evidence

Mean-group MAE 14.3503496 counts/s; worst-group MAE 25.1144697. Preserved alternative; not the selected reference.

## Falsification and interpretation

A power response of high-channel excess to low-channel excess improves transfer over fixed hardness, background-ratio and flexible controls. The exponent describes detector count-space hardening across this event, not a deconvolved photon spectrum. Detectors share one incident burst and differ in response and orientation. No independent-event replication, dead-time correction claim or universal hardness–intensity law follows.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-003` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
