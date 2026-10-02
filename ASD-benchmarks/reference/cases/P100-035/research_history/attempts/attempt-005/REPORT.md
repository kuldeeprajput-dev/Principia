# Attempt 5

Duration plus uncalibrated recording RMS0.18218 matches acoustic arousal/modulation. Test a synthesis excluding amplitude: duration,centroid,entropy,envelope variability and modulation. A gain would support reproducible acoustic structure, while no gain strengthens the recording/context confounding caution.

attempt_001_arousal=0.1833687; attempt_002_tonality=0.1982426; attempt_003_modulation=0.1828181; attempt_004_recording=0.1821831

Primary group-balanced error: 0.18300232930838467. Previous incumbent: 0.18218308593564855. Gain>1%: False. Worst-group MAE: 0.8865785808069295.

Equation: Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_duration', 'log_centroid', 'entropy', 'envelope_cv', 'log_modulation']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
