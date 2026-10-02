# Attempt 1

Species prevalence Brier0.1973 improves constant0.2055; flexible acoustic model0.1876 indicates waveform information. Test a compact arousal representation: duration,spectral centroid,high-frequency energy and envelope variation with known-species intercepts, holding entire animals out.

Initial post-baseline hypothesis

Primary group-balanced error: 0.18336866461742024. Previous incumbent: 0.18762700534310833. Gain>1%: True. Worst-group MAE: 0.8810454837401377.

Equation: Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_duration', 'log_centroid', 'high_share', 'envelope_cv']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
