# P100-007 — Single-participant vertical-force anticipation

Five hypotheses completed; the established causal prior-cycle baseline remains selected. It transfers to the faster run with55.87N MAE, strongly outperforming local extrapolation. No new biomechanical law admitted.

|Attempt|Hypothesis family|Development error|Gain>1%|
|---|---|---:|---|
|1|attempt_001_damped|130.9386|False|
|2|attempt_002_phase|100.7851|False|
|3|attempt_003_bilateral|123.4378|False|
|4|attempt_004_stance|128.1003|False|
|5|attempt_005_phase_bilateral|101.2272|False|


|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_persistence|170.5079|238.925|
|baseline_velocity|156.3821|288.3787|
|baseline_periodic|86.91508|55.87341|
|baseline_flexible|250.2433|173.0685|
|attempt_001_damped|130.9386|219.8783|
|attempt_002_phase|100.7851|94.17585|
|attempt_003_bilateral|123.4378|212.95|
|attempt_004_stance|128.1003|208.4907|
|attempt_005_phase_bilateral|101.2272|100.3414|

Read package/FINDINGS.md first. Each attempt preserves its before-fit hypothesis, fold states, data anchors, predictions, figure and failure.
