# attempt-005: wafer_area

## Hypothesis and rationale

Both geometry-correction and region-rich models fail to improve mean transfer. Remove width offsets and test only a wafer-specific inverse-area prefactor, a two-parameter fabrication-scale hypothesis. Prefer the one-parameter pooled inverse-area control if the simpler extension remains within1% in mean error; the140853ohm development junction is an explicit counterexample to uniform scaling.

## Equation and fit

`Rhat=exp(a+b*wafer_b)/w^2`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in ohm. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 2143.29645; worst group MAE: 27932.6469. Relative mean-error change against the preceding best: -0.252%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 762.914189 ohm after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
