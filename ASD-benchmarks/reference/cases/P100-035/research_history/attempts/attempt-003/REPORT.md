# Attempt 3

Spectral organization0.19824 fails despite arousal0.18337. Test temporal envelope dynamics as a competing explanation: duration,envelope variability and modulation frequency, without centroid/high-band energy. This challenges whether static spectral content contributes beyond temporal call structure.

attempt_001_arousal=0.1833687; attempt_002_tonality=0.1982426

Primary group-balanced error: 0.18281807523629345. Previous incumbent: 0.18336866461742024. Gain>1%: False. Worst-group MAE: 0.8842878277155618.

Equation: Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_duration', 'envelope_cv', 'log_modulation']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
