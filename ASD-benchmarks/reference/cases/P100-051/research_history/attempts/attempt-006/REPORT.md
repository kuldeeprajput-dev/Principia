# attempt-006: anchored_bend

## Hypothesis and rationale

The calibration-ratio exponent reduces development MAE to0.01665uA,8%below the shared shape template, but its off-regime exponent is at the bound. Challenge the power-law explanation with an anchored cubic bending correction in positive gate and independent off-branch power. Similar performance would weaken a unique mechanistic interpretation; poorer performance favors the compact calibration-coupled form only predictively.

## Equation and fit

`s_positive=u+a*u*(1-u)+b*u*(1-u)*(2*u-1); s_negative=u^q; Ihat=Il+(Ih-Il)*s`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.0177498532; worst group MAE: 0.0437825167. Relative mean-error change against the preceding best: -6.626%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.0185020991 uA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
