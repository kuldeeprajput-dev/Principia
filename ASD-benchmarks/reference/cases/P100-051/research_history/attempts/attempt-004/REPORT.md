# attempt-004: contact

## Hypothesis and rationale

Splitting the gate halves yields a small mean-error gain, but the off-regime exponent reaches its upperbound12, showing weak physical identifiability. Test a competing series-contact saturation in the softplus overdrive response. A saturation coefficient at its bound or no held-device improvement falsifies its added predictive necessity; it cannot identify actual contact resistance.

## Equation and fit

`s(V)=k*log(1+exp((V-Vt)/k)); f(V)=s(V)/(1+c*s(V)); Ihat=Iminus+(Iplus-Iminus)*(f(V)-f(-20))/(f(20)-f(-20))`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.0204462852; worst group MAE: 0.0353320472. Relative mean-error change against the preceding best: -13.167%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. No material mean-error improvement over the incumbent; retain as negative or competing evidence rather than promote it.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.0217088284 uA after freeze. It was not preselected; later numerical ranking does not change its status.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
