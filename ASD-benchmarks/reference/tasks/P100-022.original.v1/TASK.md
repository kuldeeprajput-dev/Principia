# P100-022.original.v1

**Target.** Initial positive forming-sweep current

**Target units.** microampere

**Metric kind.** mae

**Timing contract.** A fixed SHA-256 allocation reserved ten complete devices per composition. Development used five hash-assigned device folds. Exact duplicate native traces were linked and deduplicated. The task predicts the initial positive forming branch from voltage and composition alone; no current calibration or later sweep is a predictor.

**Calibration.** None. First100 voltage rows of each device, V>=0.05V; no measured current allowed as predictor.

**Independent unit.** Complete device, both compositions; all duplicate device traces linked. No future current or state permitted.

**Scope limits.** Complete device, both compositions; all duplicate device traces linked. No future current or state permitted.; A compact composition-conditioned forming-current equation improves the logistic control and is essentially tied with a larger spline on reserved devices. Its negative I-rich precursor coefficient prevents admission as a new physical conduction law.; No independent population confidence interval from dependent rows.

## Permitted inputs

| Variable | Unit and availability |
|---|---|
| voltage_V | V |
| bromine_rich | indicator |

## Comparable evaluation

All current outcomes are exposed. Future scores are retrospective. Original selection and confirmation history remain separately recorded. Model IDs, finding IDs and task IDs are distinct. Reference selection is never rewritten from confirmation winners.

Primary aggregation: mean of complete-group errors, without dependent-row population bootstrap. The shared evaluator reports physical-unit errors, per-group/worst-group performance, matched coverage, abstention and optional prediction-interval or event diagnostics. Event thresholds are exploratory unless independently justified.

From the benchmark root: python evaluation/benchmark.py example --task P100-022.original.v1 --output NEW_SUBMISSION; then score --task P100-022.original.v1 --submission NEW_SUBMISSION --output NEW_REPORT. Prediction-file scoring executes no submitted code. Optional replay --trust-code is explicit local trusted execution. Different endpoints require propose-task and independent review.
