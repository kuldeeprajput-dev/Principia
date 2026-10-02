# P100-093 — Paired-well lectin-fluorescence response distributions

Five substantive attempts completed; paired multiplicative fluorescence scaling selected. Held technical-block MAE3272.21native units is below registered controls, with one-plate and unresolved channel-caption limits.

|Attempt|Hypothesis family|Development error|Gain>1%|
|---|---|---:|---|
|1|attempt_001_multiplicative|3510.698|True|
|2|attempt_002_recruitment|3821.699|False|
|3|attempt_003_location_scale|3510.193|False|
|4|attempt_004_saturation|3534.02|False|
|5|attempt_005_tail_selective|7920.459|False|


|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_copy|12047.52|14030.59|
|baseline_shift|8722.627|9471.531|
|baseline_flexible|11800.14|8023.274|
|attempt_001_multiplicative|3510.698|3272.206|
|attempt_002_recruitment|3821.699|4505.16|
|attempt_003_location_scale|3510.193|3756.221|
|attempt_004_saturation|3534.02|3019.117|
|attempt_005_tail_selective|7920.459|8670.019|

Read package/FINDINGS.md first. Each attempt preserves its before-fit hypothesis, fold states, data anchors, predictions, figure and failure.
