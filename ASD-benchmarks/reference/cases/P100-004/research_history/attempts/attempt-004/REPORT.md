# Rician

The quadrature RMS is not the mean magnitude of a noisy transverse vector. Use the Rician mean with positive resolution variance and compare physical-unit errors under the same information budget.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

MET_hat=sigma*sqrt(pi/2)*[(1+2z)*i0e(z)+2z*i1e(z)]; z=(k*R)^2/(4*sigma^2), sigma^2=a^2*H+c^2.

Coefficients: [0.298635069680928, 1.4136615459761506, 18.233865780493158].

## Grouped development evidence

Mean-group MAE 19.9750886 GeV; worst-group MAE 20.5688132. Preserved alternative; not the selected reference.

## Falsification and interpretation

A quadrature combination of coherent recoil, activity-dependent resolution and a positive floor improves held-period prediction over scalar activity alone and the constrained nonlinear control. A Rician-mean revision and separate subsystem variances do not justify their extra structure in development. The source is a selected four-lepton sample without the Monte Carlo/control samples needed to identify background, missing particles or detector-resolution components causally.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
