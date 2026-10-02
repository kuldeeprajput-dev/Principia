# P100-011 source and units audit

Can a compact utilization law transfer Offline capacity to latency-constrained Server throughput?

**target:** Closed-division Server throughput for matched token-generating workloads

**target units:** tokens/s

**timing contract:** Predict reported Server throughput using same-system Offline benchmark result, workload label and accelerator count. This is calibrated scenario transfer, not performance prediction before benchmarking.

**calibration:** Matched Offline throughput on every evaluation system; held-system Server/Interactive results forbidden.

**independent unit:** Submitter+platform system; all model/scenario aliases linked

**scope limits:** Self-selected published MLPerf submissions; quality99.9 aliases removed and inferred results excluded. Different task families, software and latency constraints confound mechanism. No hardware causal efficiency ranking.

**exposure:** Source-aware public data. Limited schema/header and first-row previews recorded before task freeze; any inspected examples remain explicitly exposed. Confirmation performance withheld until selection and stopping freeze.

Source data stay byte-identical. Exact consumed rows/members and transformations are in native.py. All outputs record native source anchors.
