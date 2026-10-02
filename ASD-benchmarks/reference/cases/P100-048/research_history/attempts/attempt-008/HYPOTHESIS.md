# Clearness replaces diffuse-fraction proxy

A fixed0.75 clear-sky transmission scale converts global shortwave clearness into an attenuation proxy. Test whether diffuse instrumentation is necessary for cloud correction; no fitted optical response is reused.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 26.08864484612999, "worst_group": 73.13606005052783}, {"attempt": "attempt-002", "group_MAE": 15.61728917004361, "worst_group": 41.406446157849885}, {"attempt": "attempt-003", "group_MAE": 16.519211218583234, "worst_group": 51.0549779280902}, {"attempt": "attempt-004", "group_MAE": 13.377591210624121, "worst_group": 39.739564319860925}, {"attempt": "attempt-005", "group_MAE": 12.441321651469382, "worst_group": 44.264488520318295}, {"attempt": "attempt-006", "group_MAE": 15.872300499535081, "worst_group": 34.75550705085952}, {"attempt": "attempt-007", "group_MAE": 13.495598917400937, "worst_group": 39.973462149994056}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Robust interaction does not improve mean or worst-day error. Test a different cloud proxy with no diffuse-channel dependency to challenge calibration specificity.
