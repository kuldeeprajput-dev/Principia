# attempt-010

# Recent-memory necessity ablation

Retain only the week-old residual under the same robust objective. This challenges whether recent operating-history error is required beyond weekly periodicity.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 254.81894367890158, "worst_group": 2212.4607474040095}, {"attempt": "attempt-002", "group_MAE": 227.96687711425687, "worst_group": 1909.187059146815}, {"attempt": "attempt-003", "group_MAE": 331.7668362964181, "worst_group": 2852.452515970945}, {"attempt": "attempt-004", "group_MAE": 232.2719219712091, "worst_group": 1898.9352968627861}, {"attempt": "attempt-005", "group_MAE": 240.2554986078135, "worst_group": 1909.187059146815}, {"attempt": "attempt-006", "group_MAE": 215.83610714779084, "worst_group": 1832.1050322995807}, {"attempt": "attempt-007", "group_MAE": 227.5012656784877, "worst_group": 1911.689799917092}, {"attempt": "attempt-008", "group_MAE": 215.71641518156122, "worst_group": 1830.3733006802463}, {"attempt": "attempt-009", "group_MAE": 235.55057544828702, "worst_group": 2104.7241395252536}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Removing weekly memory worsens the compact robust reference. Test the opposite ablation, preserving only the week-old residual, before stopping.

Development whole-group MAE: 244.21174. Worst-group MAE: 2217.0374. 159 scored groups and 115849 rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.
