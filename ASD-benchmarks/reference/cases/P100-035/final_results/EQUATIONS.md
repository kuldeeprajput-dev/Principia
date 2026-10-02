# Frozen equations and complete coefficients

## reference

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_rms', 'log_duration']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-3.145577229688622, -0.3683783116211599, 1.2055140005728848, -0.48709290393401616, 1.1538436860247656, 0.2464294188278621, -0.6310322435674381, -0.6937636091245193, -1.4197150371841805]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "log_rms", "log_duration"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_constant

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-0.9176186543755552]`.

Ordered features: `["intercept"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_species

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-1.4231395907083417, 0.18170076389855114, 0.5203550252985866, 1.1486587996278792, 1.1996837040487405, 0.1290851946897309, 0.3597164332820209]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'training_RBF0', 'training_RBF1', 'training_RBF2', 'training_RBF3', 'training_RBF4', 'training_RBF5', 'training_RBF6', 'training_RBF7', 'training_RBF8', 'training_RBF9', 'training_RBF10', 'training_RBF11', 'training_RBF12', 'training_RBF13', 'training_RBF14', 'training_RBF15']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-0.48514257441109, -0.47555994590142214, 0.5876300466321047, 0.09774763165187848, 1.1629915532483197, 0.5209391092238576, -0.29513535679398234, -0.8011781832983222, -0.5448801977870598, -0.15963970155726118, -0.5841286397091398, 0.3340971287808263, -0.42863916095133525, 0.4265155747541613, 1.2135752431814015, -0.225647569538776, -0.27214821346198625, 0.1438156979302327, -0.45995454557403265, 0.2504314296234289, -0.13658595595318093, -0.33524328530440073, -0.4967115989586561]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "training_RBF0", "training_RBF1", "training_RBF2", "training_RBF3", "training_RBF4", "training_RBF5", "training_RBF6", "training_RBF7", "training_RBF8", "training_RBF9", "training_RBF10", "training_RBF11", "training_RBF12", "training_RBF13", "training_RBF14", "training_RBF15"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_arousal

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_duration', 'log_centroid', 'high_share', 'envelope_cv']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-1.1589771535268942, -0.36112352426759775, 1.222700843166941, -0.4769254796814064, 1.1667914317961576, 0.2601711537192966, -0.6212221619816818, -1.4339936518645051, -0.009149093693926807, -0.003614614458664366, -0.24463773825231852]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "log_duration", "log_centroid", "high_share", "envelope_cv"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_tonality

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_peak', 'entropy', 'flatness']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-1.5477035839369329, 0.16357975080928108, 0.7175148543607422, 1.1532858286037686, 1.344029039849254, 0.1982993407939681, 0.3154361727055833, -0.12176287204104645, -0.07497536521655582, -0.22583589048537825]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "log_peak", "entropy", "flatness"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_modulation

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_duration', 'envelope_cv', 'log_modulation']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-1.222726778740143, -0.4813535070199146, 1.1905048176275552, -0.5011364400284215, 1.0949845302602623, 0.2698679507409972, -0.6532534201175833, -1.3384640548691835, -0.15578202902177207, 0.13616608407580408]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "log_duration", "envelope_cv", "log_modulation"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_recording

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_rms', 'log_duration']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-3.145577229688622, -0.3683783116211599, 1.2055140005728848, -0.48709290393401616, 1.1538436860247656, 0.2464294188278621, -0.6310322435674381, -0.6937636091245193, -1.4197150371841805]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "log_rms", "log_duration"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_spectrotemporal

Pr(positive-context)=sigmoid(sum_j b_j*x_j); x in exact order ['intercept', 'species_code=1', 'species_code=2', 'species_code=3', 'species_code=4', 'species_code=5', 'species_code=6', 'log_duration', 'log_centroid', 'entropy', 'envelope_cv', 'log_modulation']; species code lookup in SPECIES.json. Logs use duration/1s, centroid or peak/1000Hz, modulation/1Hz, RMS relative PCM full scale.

Coefficients: `[-1.5422576266657837, -0.4849955989237866, 1.2014902246268113, -0.5047201432217789, 1.1308228841682701, 0.2795733146106299, -0.6729772288450699, -1.3472432425593863, -0.06491317281995389, 0.3965105811859329, -0.10175754409479491, 0.13321545979863222]`.

Ordered features: `["intercept", "species_code=1", "species_code=2", "species_code=3", "species_code=4", "species_code=5", "species_code=6", "log_duration", "log_centroid", "entropy", "envelope_cv", "log_modulation"]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

