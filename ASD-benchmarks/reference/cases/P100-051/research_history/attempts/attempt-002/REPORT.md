# attempt-002: softplus

## Hypothesis and rationale

A shared power exponent p=2.084 reaches0.01921uA grouped MAE near the flexible shape baseline0.01807. Test a smooth threshold-turn-on equation based on softplus gate overdrive, independently parameterizing threshold and broadening rather than a fixed zero-gate power origin.

## Equation and fit

`s(V)=k*log(1+exp((V-Vt)/k)); Ihat=Iminus+(Iplus-Iminus)*(s(V)-s(-20))/(s(20)-s(-20))`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.0204424263; worst group MAE: 0.0361399057. Relative mean-error change against the preceding best: -13.145%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.0207968841 uA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
