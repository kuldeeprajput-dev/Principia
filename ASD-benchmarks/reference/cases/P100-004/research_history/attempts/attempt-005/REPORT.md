# Subsystems

Lepton and jet activities have different resolutions. Split the Rician variance into lepton and jet components and examine whether the separate coefficients are stable across periods.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

Same Rician mean, with sigma^2=a_l^2*L+a_j^2*J+c^2.

Coefficients: [0.29677012051576024, 2.564886697203304, 0.980540878460635, 9.460519969609544].

## Grouped development evidence

Mean-group MAE 19.9312419 GeV; worst-group MAE 20.5625106. Preserved alternative; not the selected reference.

## Falsification and interpretation

A quadrature combination of coherent recoil, activity-dependent resolution and a positive floor improves held-period prediction over scalar activity alone and the constrained nonlinear control. A Rician-mean revision and separate subsystem variances do not justify their extra structure in development. The source is a selected four-lepton sample without the Monte Carlo/control samples needed to identify background, missing particles or detector-resolution components causally.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-005` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
