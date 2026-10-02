# Precision

Weight precision may alter latency-constrained efficiency even after Offline calibration. Test a declared4-bit indicator within workload; software/hardware confounding prevents causal precision claims.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

S_hat=Q*sigmoid(b_workload+a*I_4bit).

Coefficients: [0.6330641060988361, 7.999999999999999, 2.733981055891699, 1.6468619616458542, 1.6639779292755712, 3.6358475620384, 0.5951855628792831].

## Grouped development evidence

Mean-group MAE 7569.8588 tokens/s; worst-group MAE 146735.982. Preserved alternative; not the selected reference.

## Falsification and interpretation

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection. Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-005` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
