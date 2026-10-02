# attempt-002: perimeter

## Hypothesis and rationale

The common edge-loss model collapsed to nearly zero width correction and did not improve mean error. Test the competing parallel conduction model G=g_A*w^2+g_P*w, which represents an edge channel rather than a reduced conducting width. Positive coefficients constrain passive conductance; a boundary coefficient indicates non-identifiability.

## Equation and fit

`Rhat=1/(exp(a)*w^2+exp(b)*w)`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in ohm. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 2140.35441; worst group MAE: 27886.3023. Relative mean-error change against the preceding best: -0.115%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 771.932654 ohm after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
