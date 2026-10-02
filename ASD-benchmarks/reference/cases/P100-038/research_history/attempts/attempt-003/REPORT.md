# attempt-003

# Noise-gated extrapolation

Signal scatter should attenuate trend response; divide the slope by1+past spread in dB, a declared empirical scale.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 1.2577260893238156, "worst_group": 1.7260980576240144}, {"attempt": "attempt-002", "group_MAE": 1.2286967795825008, "worst_group": 1.6533308691555735}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Two-scale reversion improves persistence while slope-only fails. Test whether scatter suppresses noise-driven trend.

Development whole-group MAE: 1.2157744. Worst-group MAE: 1.6225963. 3 scored groups and 2754 rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.
