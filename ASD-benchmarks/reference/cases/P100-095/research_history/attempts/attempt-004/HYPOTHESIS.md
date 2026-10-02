# Directional terrain response

Along/cross orientation of unrotated mean flow modifies energy production, reflecting possible terrain dependence.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 0.3173972561524605, "worst_group": 0.5982098856436229}, {"attempt": "attempt-002", "group_MAE": 0.3122647880296719, "worst_group": 0.575888428751605}, {"attempt": "attempt-003", "group_MAE": 0.3330655183078203, "worst_group": 0.5932360025825785}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Buoyancy-gradient interaction worsens the energy-budget error. Test terrain-direction modulation rather than adding more stability coefficients.
