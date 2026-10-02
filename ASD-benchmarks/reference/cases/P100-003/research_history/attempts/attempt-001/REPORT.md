# Relax

Recorded band-RMS relaxes toward a recent robust level rather than persisting its latest fluctuation; test signed residual structure under hardware-injection contamination.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

R_hat=max(0,m+a*(R1-m)); m=median4.

Coefficients: [0.07956285227335949].

## Grouped development evidence

Mean-group MAE 0.011099744 10^-21 strain; worst-group MAE 0.0139665702. Preserved alternative; not the selected reference.

## Falsification and interpretation

None of the five proposed relaxation, cross-band or robust-response extensions beats the stationary training median during forward development. The retained reference also loses modestly to several controls on the final blocks. These adverse outcomes are part of the result. All data come from one short segment. The DATA bit and declared injection bits are required; other quality bits are retained rather than silently asserted clean. No injection/noise decomposition is identified.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-001` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
