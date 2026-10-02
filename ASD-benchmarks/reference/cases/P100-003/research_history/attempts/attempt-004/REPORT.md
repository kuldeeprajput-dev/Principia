# Robust

Narrow-band or broad-band regressors may simply chase fluctuations. Bound the response to a lag deviation using a robust local fluctuation scale, and challenge the apparent benefit against a stationary constant.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

R_hat=max(0,m+a*s*tanh((R1-m)/s)); s=max(MAD4,1e-9).

Coefficients: [0.4178673932788412].

## Grouped development evidence

Mean-group MAE 0.0113942227 10^-21 strain; worst-group MAE 0.0145522633. Preserved alternative; not the selected reference.

## Falsification and interpretation

None of the five proposed relaxation, cross-band or robust-response extensions beats the stationary training median during forward development. The retained reference also loses modestly to several controls on the final blocks. These adverse outcomes are part of the result. All data come from one short segment. The DATA bit and declared injection bits are required; other quality bits are retained rather than silently asserted clean. No injection/noise decomposition is identified.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
