# Frozen equations and complete coefficients

## reference

c*(1+b_line); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[7.581667014750264, 1.8155460826606205, 0.029666186944522752]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_copy

c; c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_shift

c+delta_line; c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[30251.237218920935, 5710.027516280556, 39.16538443159215]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

c+b0+sum_j b_j exp(-mean((z-center_j)^2)/2); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[43857.52587830899, -37349.84450966712, 80758.14635956478, -12890.880581109723, -23933.225973436984, -7896.086196243642, -37731.98306959764, -33697.49004306223, 1680.006094930409, -24043.885882587423]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_multiplicative

c*(1+b_line); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[7.581667014750264, 1.8155460826606205, 0.029666186944522752]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_recruitment

c+delta_line*sigmoid((q-q0)/.1); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[69831.21205116552, 17362.837209146914, 230.39838471308397]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_location_scale

c+delta_line+s_line*control_width*(q-.5); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[30251.237218920945, 5710.0275162805565, 39.16538443159217, 8.13708032183065, 2.4222794164789057, 0.044196958423376655]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_saturation

c+delta_line*c/(K+abs(c)); c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[212629.27810963738, 48192.95550966742, 671.5747610620462]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_tail_selective

c+delta_line+b3*WT*(q-.5)^3; c=paired uninduced AF488 quantile(native units),q=quantile probability,line coefficient order MFSD5/WT SLC30A8/mutant; width=control q.9-q.1. Shift coefficients and K are native fluorescence units; multiplicative/location-scale coefficients dimensionless. Profile threshold/K is additional fitted state.

Coefficients: `[30251.237218920945, 5710.0275162805565, 39.16538443159217, 231424.01465926436]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

