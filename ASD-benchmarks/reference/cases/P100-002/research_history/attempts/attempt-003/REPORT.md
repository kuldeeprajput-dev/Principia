# Oscillator

A rotating brightness pattern has both velocity and curvature. Test a second-order local oscillator approximation against simple slope and mean reversion; transferred coefficients must survive held-star validation.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

F_hat=F1+a*(F1-F2)+b*(F1-2*F2+F3).

Coefficients: [-0.9526276662634185, 0.3080708901591124].

## Grouped development evidence

Mean-group MAE 0.00296966632 relative flux (native normalization); worst-group MAE 0.00959555624. Selected before confirmation.

## Falsification and interpretation

The selected two-term local response improves one-hour-ahead error over persistence and the constrained nonlinear comparator. Its negative slope coefficient damps the latest increment. That is consistent with short-timescale measurement fluctuations or mean reversion; it does not identify a physical rotation frequency or prove an oscillation mechanism. Two stars do not establish population-level precision. Later diagnostic candidates score better on confirmation but were not promoted. No period estimated from the full sector is a predictor.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-003` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
