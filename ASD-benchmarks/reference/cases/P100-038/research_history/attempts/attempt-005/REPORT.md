# attempt-005

# Volatility-conditioned reversion

If measurement scatter drives reversals, short-mean displacement should couple to past spread; remove long-mean and directional terms.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 1.2577260893238156, "worst_group": 1.7260980576240144}, {"attempt": "attempt-002", "group_MAE": 1.2286967795825008, "worst_group": 1.6533308691555735}, {"attempt": "attempt-003", "group_MAE": 1.2157744053119888, "worst_group": 1.6225962561123695}, {"attempt": "attempt-004", "group_MAE": 1.2106757105974493, "worst_group": 1.6268131523052112}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Asymmetric trend nearly matches flexible control, but gains remain small. Test a one-parameter volatility-driven reversal model.

Development whole-group MAE: 1.2158767. Worst-group MAE: 1.6340852. 3 scored groups and 2754 rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.
