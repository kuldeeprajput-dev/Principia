# attempt-003: two_power

## Hypothesis and rationale

The softplus threshold model improves worst-device error but worsens mean error relative to one power exponent. Separate positive-gate and negative-gate exponents to test whether accumulation and near-off regimes share curvature. Current errors in uA may weakly identify the near-off exponent; retain that limitation and compare high/low gate residuals.

## Equation and fit

`Ihat=Il+(Ih-Il)*u^(p_positive if V>=0 else p_negative)`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.018880978; worst group MAE: 0.037590212. Relative mean-error change against the preceding best: -4.503%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.0176630208 uA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
