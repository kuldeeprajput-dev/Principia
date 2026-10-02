# attempt-003: polymer

## Hypothesis and rationale

Elapsed-time aging did not improve mean error; charge and time alone cannot explain transfer. Test polymer-dependent current gain and age response, motivated by dilution of conducting and emissive material. Device grouping blocks the identical composition/device calibration from leaking across folds; composition and voltage confounding remain possible.

## Equation and fit

`Phat=C0+theta@[1,d,d*f,L,L*f]`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in nA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 17.1521617; worst group MAE: 91.2103074. Relative mean-error change against the preceding best: -127.385%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 16.962189 nA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
