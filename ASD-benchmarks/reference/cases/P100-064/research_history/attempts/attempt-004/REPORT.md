# attempt-004: saturation

## Hypothesis and rationale

Polymer interactions inflate worst-device MAE to91.2nA, exposing unstable extrapolation across sparse formulation groups. Replace linear current gain with bounded-growth asinh current response while retaining polymer and logarithmic age terms. Test whether current-response saturation improves transfer without creating a universal strain law.

## Equation and fit

`Phat=C0+theta@[1,S,L,S*f]`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in nA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 11.5823935; worst group MAE: 30.9145461. Relative mean-error change against the preceding best: -53.547%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 16.2679495 nA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
