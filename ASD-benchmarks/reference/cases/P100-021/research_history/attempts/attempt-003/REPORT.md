# attempt-003: wafer_edge

## Hypothesis and rationale

Neither common width loss nor parallel perimeter conduction beats nominal inverse area. Test wafer-specific area prefactors and width corrections, since the two wafers represent separate fabrication histories. Both wafers remain represented in every development training fold; this is die transfer within known wafers, not unseen-wafer prediction.

## Equation and fit

`Rhat=exp(a+b*wafer_b)/(w-delta0-delta1*wafer_b)^2`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in ohm. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 2181.20387; worst group MAE: 27937.9616. Relative mean-error change against the preceding best: -2.025%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 766.944569 ohm after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
