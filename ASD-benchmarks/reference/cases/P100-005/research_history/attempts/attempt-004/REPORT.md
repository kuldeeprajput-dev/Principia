# Triangle lp

The edge relaxation ignores cliques of size3. Add all triangle inequalities to the stable-set LP, then use integer flooring to obtain a valid upper bound. Evaluate whether a cheap local polyhedral strengthening is sufficient on this finite family.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

Edge LP plus sum_(i in triangle) x_i<=1.

Coefficients: [].

## Grouped development evidence

Mean-group MAE 0.435846648 vertices; worst-group MAE 1. Preserved alternative; not the selected reference.

## Falsification and interpretation

Every eligible graph has independence number4. A training-only constant therefore attains zero error, as does independent exact enumeration. That perfect score provides no evidence for a newly discovered general graph rule. This finite, deliberately selected obstruction family is not a representative graph distribution. Classical bounds and exact enumeration are reproductions. A prediction must not be mistaken for a proof or extrapolated to arbitrary graphs.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-004` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
