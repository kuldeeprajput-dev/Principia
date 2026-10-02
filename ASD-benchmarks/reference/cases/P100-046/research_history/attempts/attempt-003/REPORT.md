# Polytropic

Reconcile density-only and field-only explanations using a two-exponent local closure. Test whether both exponents are identifiable and improve forward-block error rather than merely absorbing correlated variations.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

T_hat=T0*exp(clip(a*ln(n/n0)+b*ln(B/B0),-5,5)).

Coefficients: [-0.28670183606937777, 0.447489262469799].

## Grouped development evidence

Mean-group MAE 1.86832755 eV; worst-group MAE 2.33787057. Selected before confirmation.

## Falsification and interpretation

A two-exponent local closure using density and field ratios improves confirmation error over persistence, fixed CGL scaling and the nonlinear control. The fitted density exponent is negative. That is a local empirical association along a spacecraft trajectory, not an independently identified thermodynamic polytropic index. Current density and magnetic field are allowed, so this is a contemporaneous closure rather than future-state forecasting. Eulerian spacecraft samples are not tracked fluid parcels. Two held blocks and one orbit segment do not establish a universal plasma law.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-003` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
