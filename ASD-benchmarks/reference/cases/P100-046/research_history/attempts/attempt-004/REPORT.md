# Relaxation

Double-adiabatic closures omit anisotropy relaxation. Add only the60-second-old parallel/perpendicular ratio as a relaxation driver, with currenttemperature still forbidden.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

T_hat=T0*exp(clip(a*ln(n/n0)+b*ln(B/B0)+c*(T_parallel0/T0-1),-5,5)).

Coefficients: [-0.2851959360901397, 0.45465161137594673, -0.005804660951170249].

## Grouped development evidence

Mean-group MAE 1.86607888 eV; worst-group MAE 2.32953512. Preserved alternative; not the selected reference.

## Falsification and interpretation

A two-exponent local closure using density and field ratios improves confirmation error over persistence, fixed CGL scaling and the nonlinear control. The fitted density exponent is negative. That is a local empirical association along a spacecraft trajectory, not an independently identified thermodynamic polytropic index. Current density and magnetic field are allowed, so this is a contemporaneous closure rather than future-state forecasting. Eulerian spacecraft samples are not tracked fluid parcels. Two held blocks and one orbit segment do not establish a universal plasma law.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
