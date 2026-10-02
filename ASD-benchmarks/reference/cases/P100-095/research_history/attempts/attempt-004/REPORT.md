# attempt-004

# Directional terrain response

Along/cross orientation of unrotated mean flow modifies energy production, reflecting possible terrain dependence.

Development feedback available before this hypothesis: [{"attempt": "attempt-001", "group_MAE": 0.3173972561524605, "worst_group": 0.5982098856436229}, {"attempt": "attempt-002", "group_MAE": 0.3122647880296719, "worst_group": 0.575888428751605}, {"attempt": "attempt-003", "group_MAE": 0.3330655183078203, "worst_group": 0.5932360025825785}]

This attempt tests a distinct explanation/ablation. All reserved groups remain unscored. A failure to beat the incumbent rejects predictive benefit rather than proving absence of the underlying physical process.

Decision rationale: Buoyancy-gradient interaction worsens the energy-budget error. Test terrain-direction modulation rather than adding more stability coefficients.

Development whole-group MAE: 0.31426347. Worst-group MAE: 0.58836506. 5 scored groups and 468 rows. Complete fold predictions and fit states are retained. This is development evidence, not confirmation.
