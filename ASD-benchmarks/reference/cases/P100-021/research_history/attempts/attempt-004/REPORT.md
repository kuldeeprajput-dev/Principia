# attempt-004: region

## Hypothesis and rationale

Wafer-specific width offsets worsen transfer and are not identified as stable geometry corrections. Test a common width correction with a separate outer-wafer conductance prefactor, motivated by edge-process nonuniformity rather than assigning coordinate trends absent from metadata. Compare parameter stability and held-out dies; no post-hoc removal of the extreme die.

## Equation and fit

`Rhat=exp(a+b*wafer_b+c*outer)/(w-delta)^2`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in ohm. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 2150.61545; worst group MAE: 28022.7857. Relative mean-error change against the preceding best: -0.595%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 758.152306 ohm after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
