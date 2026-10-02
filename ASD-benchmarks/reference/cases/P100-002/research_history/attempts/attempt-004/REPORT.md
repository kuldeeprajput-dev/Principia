# Volatility

Curvature and trend gains can be driven by noisy jumps. Gate the causal slope by the recent median absolute fluctuation while allowing slow relaxation; test whether robustness improves worst-star behavior.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

F_hat=F1+a*DeltaF/(1+abs(DeltaF)/s)+b*(F1-median24); s=max(MAD6,1e-9).

Coefficients: [-1.1813227617401574, -0.33225807472300983].

## Grouped development evidence

Mean-group MAE 0.00315063358 relative flux (native normalization); worst-group MAE 0.0108220981. Preserved alternative; not the selected reference.

## Falsification and interpretation

The selected two-term local response improves one-hour-ahead error over persistence and the constrained nonlinear comparator. Its negative slope coefficient damps the latest increment. That is consistent with short-timescale measurement fluctuations or mean reversion; it does not identify a physical rotation frequency or prove an oscillation mechanism. Two stars do not establish population-level precision. Later diagnostic candidates score better on confirmation but were not promoted. No period estimated from the full sector is a predictor.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
