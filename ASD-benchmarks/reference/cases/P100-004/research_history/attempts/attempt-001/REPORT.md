# Rayleigh

If uncorrelated transverse reconstruction errors dominate, MET magnitude grows as the square root of scalar activity. Compare this stochastic model with measured recoil and flexible controls.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

MET_hat=a*sqrt(H).

Coefficients: [3.011158525540562].

## Grouped development evidence

Mean-group MAE 21.0775502 GeV; worst-group MAE 21.601025. Preserved alternative; not the selected reference.

## Falsification and interpretation

A quadrature combination of coherent recoil, activity-dependent resolution and a positive floor improves held-period prediction over scalar activity alone and the constrained nonlinear control. A Rician-mean revision and separate subsystem variances do not justify their extra structure in development. The source is a selected four-lepton sample without the Monte Carlo/control samples needed to identify background, missing particles or detector-resolution components causally.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-001` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
