# Attempt 4

Temporal modulation0.18282 is indistinguishable from arousal0.18337, suggesting duration-driven context discrimination. Falsify a recording-artifact explanation with only duration plus normalized PCM RMS and species: if this matches richer models, calibrated emotional acoustics cannot be inferred.

attempt_001_arousal=0.1833687; attempt_002_tonality=0.1982426; attempt_003_modulation=0.1828181

Primary group-balanced error: 0.18218308593564855. Previous incumbent: 0.18281807523629345. Gain>1%: False. Worst-group MAE: 0.8753347406401762.

Equation: Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_rms', 'log_duration']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
