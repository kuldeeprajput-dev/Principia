# Quadrature

Combine coherent recoil and stochastic transverse activity in quadrature, with a nonnegative resolution floor. This tests whether two physically distinct contributions explain errors beyond either one alone.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

MET_hat=sqrt((k*R)^2+a^2*H+c^2).

Coefficients: [0.2885606463293234, 1.6952876188332207, 23.00800315418681].

## Grouped development evidence

Mean-group MAE 19.9341237 GeV; worst-group MAE 20.5262649. Selected before confirmation.

## Falsification and interpretation

A quadrature combination of coherent recoil, activity-dependent resolution and a positive floor improves held-period prediction over scalar activity alone and the constrained nonlinear control. A Rician-mean revision and separate subsystem variances do not justify their extra structure in development. The source is a selected four-lepton sample without the Monte Carlo/control samples needed to identify background, missing particles or detector-resolution components causally.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-003` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
