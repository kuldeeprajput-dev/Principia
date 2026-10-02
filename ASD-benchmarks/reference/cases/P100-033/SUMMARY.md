# P100-033 — PPG pulse-rate harmonic ambiguity

Six attempts completed. Quality shrinkage is selected by development; held-person error9.3292bpm is better than raw spectral methods and slightly better than a median prior, but worse than flexible fusion. No new cardiovascular law admitted.

|Attempt|Hypothesis family|Development error|Gain>1%|
|---|---|---:|---|
|1|attempt_001_alias|34.25331|False|
|2|attempt_002_fusion|30.50684|False|
|3|attempt_003_shrinkage|11.2705|True|
|4|attempt_004_motion_fusion|28.59009|False|
|5|attempt_005_agreement_gate|32.52944|False|
|6|attempt_006_consensus_shrink|11.42728|False|


|Model|Development group error|Reserved group error|
|---|---:|---:|
|baseline_constant|11.65943|9.800231|
|baseline_fourier|32.2896|30.77508|
|baseline_autocorrelation|31.58865|30.12645|
|baseline_flexible|11.74158|9.031956|
|attempt_001_alias|34.25331|32.07775|
|attempt_002_fusion|30.50684|29.27755|
|attempt_003_shrinkage|11.2705|9.329169|
|attempt_004_motion_fusion|28.59009|29.69514|
|attempt_005_agreement_gate|32.52944|31.30643|
|attempt_006_consensus_shrink|11.42728|9.411953|

Read package/FINDINGS.md first. Each attempt preserves its before-fit hypothesis, fold states, data anchors, predictions, figure and failure.
