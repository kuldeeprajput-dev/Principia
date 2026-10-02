# attempt-007: shape_blend

## Hypothesis and rationale

Anchored cubic bending remains worse than the calibration-ratio exponent and reaches its curvature bound, reinforcing a near-quadratic accumulation shape but not a unique mechanism. Test shrinkage of the normalized training template toward linear interpolation as an independent regularized representation; this challenges whether template flexibility, rather than calibration-ratio information, is the remaining source of gain. Stop if it fails to surpass the incumbent on grouped mean and worst-device error.

## Equation and fit

`s=a*interp(V,training_grid,training_shape)+(1-a)*u; Ihat=Il+(Ih-Il)*s`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.0180674158; worst group MAE: 0.0386320946. Relative mean-error change against the preceding best: -8.534%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.0176570535 uA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
