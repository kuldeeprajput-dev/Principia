# attempt-004

# Ramping and weekend asymmetry

Up/down forecast ramps and weekend modulation challenge fixed memory weights.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 254.81894367890158, "worst_group": 2212.4607474040095}, {"attempt": "attempt-002", "group_MAE": 227.96687711425687, "worst_group": 1909.187059146815}, {"attempt": "attempt-003", "group_MAE": 331.7668362964181, "worst_group": 2852.452515970945}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Relative-response fitting fails at331.77 versus227.97MW. Return to absolute residuals and test calendar/ramp modulation, with code evolution logged before fitting.

Development whole-group MAE: 232.27192. Worst-group MAE: 1898.9353. 159 scored groups and 115849 rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.
