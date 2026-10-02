# Attempt 2

Arousal descriptor improves animal Brier to0.18337; its strong duration coefficient suggests call-type/context confounding. Test an independent spectral-organization explanation using peak frequency,entropy and flatness, retaining matched species intercepts.

attempt_001_arousal=0.1833687

Primary group-balanced error: 0.19824264975563435. Previous incumbent: 0.18336866461742024. Gain>1%: False. Worst-group MAE: 0.82089138330263.

Equation: Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_peak', 'entropy', 'flatness']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
