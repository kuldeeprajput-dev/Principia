# Frozen equations and complete coefficients

## reference

clip(w*F+(1-w)*mu; w=sigmoid(b0+b1*(Q-.3)); mu=b2,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[-2.1392927775759514, 2.104288249996586, 84.6100504251943]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_constant

clip(weighted development median HR,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[78.0]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_fourier

clip(F,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_autocorrelation

clip(A,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

clip(b0+sum_j b_j exp(-mean((z-center_j)^2)/2); training-only z scaling,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[85.39806300029448, 9.45740019901618, -10.549239389501961, -2.3582050111418154, 0.28759058647307434, -0.6537507016049932, 0.6387972086326098, 14.164807544469895, 0.07041902772104636, -0.6010388091370154, 1.0193207599780822, 2.9119957501553433, 4.6177002947730355, -8.711677416517691, 7.828307154519031, 1.9348995958080442, 1.4593696424712481, 1.7388613721473347, -11.246454378506163, -5.82619675006199, -9.209333667486947]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_alias

clip(F-sigmoid(b0+b1*(S-.5))*(F-H),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[-0.852668273411295, 1.0705003970935674]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_fusion

clip(w*F+(1-w)*A; w=sigmoid(b0+b1*(Q-.3)+b2*D),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[-1.7082088949169945, -1.0049408672163036, 0.8324049425398257]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_shrinkage

clip(w*F+(1-w)*mu; w=sigmoid(b0+b1*(Q-.3)); mu=b2,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[-2.1392927775759514, 2.104288249996586, 84.6100504251943]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_motion_fusion

clip(w*F+(1-w)*A+b4*ear; w=sigmoid(b0+b1*(Q-.3)+b2*D+b3*motion),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[-1.03657330886646, -2.0101589420283257, 0.5181291927258077, 0.38332716070981937, 21.638318867005346]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_agreement_gate

clip(C=H if S>=threshold else F; select C only when abs(C-A)<abs(F-A),30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[0.25]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_006_consensus_shrink

clip(w*(F+A)/2+(1-w)*mu; w=sigmoid(b0+b1*(Q-.3)-b2*D), mu=b3,30,240) bpm; F=FFT rate,A=ACF rate,H=half-rate candidate,Q=spectral concentration,S=half-frequency relative power,D=abs(F-A)/60

Coefficients: `[-2.0484727609204536, 1.8866977800637492, 0.06881749666361361, 84.56649114516628]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

