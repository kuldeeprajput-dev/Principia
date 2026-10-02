# attempt-005

# Bounded operational correction

A15-percent-of-forecast cap tests protection against stale extreme residuals;15% is an exploratory stability bound, not an operator acceptance tolerance.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 254.81894367890158, "worst_group": 2212.4607474040095}, {"attempt": "attempt-002", "group_MAE": 227.96687711425687, "worst_group": 1909.187059146815}, {"attempt": "attempt-003", "group_MAE": 331.7668362964181, "worst_group": 2852.452515970945}, {"attempt": "attempt-004", "group_MAE": 232.2719219712091, "worst_group": 1898.9352968627861}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Calendar/ramp terms do not improve227.97MW memory mean error, although worst authority-month is slightly better. Test a fixed15% safety cap around the simpler absolute correction.

Development whole-group MAE: 240.2555. Worst-group MAE: 1909.1871. 159 scored groups and 115849 rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.
