# attempt-005: calyield

## Hypothesis and rationale

Saturating current terms improve over unstable composition interactions but still underperform optical persistence. Test an early-calibrated yield hypothesis: current and age changes multiplied by the initial optical level plus additive current/age corrections. This distinguishes multiplicative optical efficiency from additive drift without using later optical data. If no clear development gain emerges, preserve the negative transfer result.

## Equation and fit

`Phat=C0+theta@[1,C0*d,C0*L,d,L]`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in nA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 46.6359712; worst group MAE: 379.856178. Relative mean-error change against the preceding best: -518.250%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 11.3374035 nA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
