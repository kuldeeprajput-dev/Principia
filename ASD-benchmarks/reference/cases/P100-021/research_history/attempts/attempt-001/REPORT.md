# attempt-001: edge

## Hypothesis and rationale

The inverse-area control improves over a constant but misses die-level extremes. Test a common fabrication width loss delta: R=A/(w-delta)^2. This distinguishes edge loss from arbitrary polynomial curvature. Keep all extreme junctions; a fitted delta is an effective parameter, not direct microscopy.

## Equation and fit

`Rhat=exp(a)/(w-delta)^2`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in ohm. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 2142.8847; worst group MAE: 27866.1366. Relative mean-error change against the preceding best: -0.233%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 766.270626 ohm after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
