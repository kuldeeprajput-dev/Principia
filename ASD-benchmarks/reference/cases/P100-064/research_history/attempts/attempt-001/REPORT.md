# attempt-001: charge

## Hypothesis and rationale

A pooled current-change conversion has large cross-device error. Test cumulative electrical charge as an additional state variable, motivated by ionic redistribution and electrochemical doping, without claiming that charge causally identifies these mechanisms. Compare to matched current-only and persistence controls.

## Equation and fit

`Phat=C0+theta@[1,d,Q]`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in nA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 7.76535086; worst group MAE: 14.6722248. Relative mean-error change against the preceding best: -2.945%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 16.0553783 nA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
