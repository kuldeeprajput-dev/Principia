# attempt-002: age

## Hypothesis and rationale

Charge history reduces current-only MAE only slightly and still loses to persistence. Test logarithmic elapsed-time aging as a competing explanation for slow ionic or optical evolution. This asks whether time since activation transfers better than integrated current, with the same device holdout.

## Equation and fit

`Phat=C0+theta@[1,d,L]`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in nA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 8.08651458; worst group MAE: 16.2581485. Relative mean-error change against the preceding best: -7.202%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 16.610172 nA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
