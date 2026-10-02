# attempt-001: power

## Hypothesis and rationale

The training-normalized shape control lowers MAE by nearly an order of magnitude versus linear/log interpolation, indicating transferable curve curvature. Test one global power exponent shared by both gate halves as a compact transport-shape description; three anchors are explicit calibration.

## Equation and fit

`Ihat=Il+(Ih-Il)*u^p`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.0192095287; worst group MAE: 0.0375484016. Relative mean-error change against the preceding best: -6.321%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.0181389398 uA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
