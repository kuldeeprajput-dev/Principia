# attempt-005: anchor_power

## Hypothesis and rationale

Contact saturation collapses almost to zero and does not improve mean error. Reconcile device-to-device shape variation using only permitted zero-gate/on-gate calibration ratio: allow positive-branch exponent to depend on log((I0-Imin)/(I20-Imin)). This tests whether early threshold information explains remaining curvature; negative-branch exponent remains a separate nuisance shape, not an identified transport law.

## Equation and fit

`r=clip((Izero-Iminus)/(Iplus-Iminus),1e-9,1); p=clip(a+b*log(r),0.1,8); Ihat=Il+(Ih-Il)*u^(p if V>=0 else q)`

All coefficients and transforms are in model.json; complete leave-one-group-out states are in fold_models.json. The fit used development only, with equal independent-group weighting. The primary metric is mean group MAE in uA. Full-state training scope and source/table hashes are recorded.

## Development result

Mean group MAE: 0.016646802; worst group MAE: 0.0386113316. Relative mean-error change against the preceding best: 7.863%. Every group, including unfavorable groups, is in metrics.json.

## Falsifying test and interpretation

The competing explanation is tested on complete omitted groups, with simple, domain and flexible controls under the same information budget. The primary-error improvement supports proceeding to a distinct challenge; it does not identify a physical mechanism.

Physical interpretation and confounders are bounded by SOURCE_AND_UNITS.md. No model parameter is interpreted as an independently measured microscopic material property. Report all boundary parameters and sparse-group failures in the final reader.

## Confirmation disposition

Selection and stopping were frozen before confirmation. This candidate scored 0.016303893 uA after freeze. It was preselected.

This REPORT was assembled after confirmation from immutable hypothesis/config, development receipts and frozen states; the original timestamps and hashes are preserved.
