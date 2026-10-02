# Parallel

Workload utilization may hide multi-accelerator queueing/coordination overhead. Test a bounded utilization response to accelerator count within workload and held systems.

This hypothesis/configuration was recorded before execution. Selection uses development data only. Every failure remains part of scientific history.

## Executable candidate

S_hat=Q*sigmoid(b_workload+a*ln(1+N)).

Coefficients: [0.5549975531411513, 7.999999999999999, 2.618949011976792, 1.5293232290015515, 1.836037546635328, 4.014159041202058, 0.16476518259418454].

## Grouped development evidence

Mean-group MAE 7088.35846 tokens/s; worst-group MAE 109908.836. Selected before confirmation.

## Falsification and interpretation

A workload-specific bounded utilization response with an accelerator-count term improves the reserved mean error over direct Offline transfer, a single utilization factor and the constrained flexible control. However, simpler workload-only alternatives perform better retrospectively and are retained without reselection. Reserved mean error is much larger than development error, reflecting difficult system-scale transfer. Several workload logits contact bounds; coefficients are not universal efficiencies. Offline calibration is mandatory, so this is not prediction from specifications alone.

Parameter sensitivity is in parameter_sensitivity.json. Fold extrema are descriptive, not population confidence intervals. All validation/training group memberships are retained in metrics.json and SCIENTIFIC_CHECKS.json.

## Replay

Run `python develop.py PATH_TO_LOCAL_DATAS attempts/attempt-002` only in a new exploratory workspace; the script refuses to overwrite completed evidence. The current confirmation outcomes are exposed. Frozen prediction replay is `python run.py` inside final_results.
