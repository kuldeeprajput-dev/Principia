# Frozen equations and complete coefficients

## reference

C; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_persistence

F; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_velocity

F+v; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_periodic

C; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

F+b0+sum_j b_j exp(-mean((z-center_j)^2)/2); F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[-7.302173125751102, -10.119782030704117, -111.39297129390897, 373.40325679210406, -29.255386889627488, -260.6492691549664, 8.059785507480079, 404.4232690035839, 24.614665743850267, -93.8694539095602, -233.78312826059863, 601.7417706424988, 182.48389822398556, -189.28513762270615, -172.70258945393525, -86.0879923669576, -832.1308407382999, 126.37017647778838, 242.70424733560932, -25.715850692238302, 0.9203391219275429]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_damped

F+b0*v+b1*a; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[0.5245017867048858, 0.4855469001050484]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_phase

F+b0*(C-F)+b1*v; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[0.6170403239090547, 0.25248851499498487]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_bilateral

F+b0*v+b1*a+b2*vO; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[0.20331248849310563, 0.8921226980900576, -0.41360984791263955]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_stance

F+b0*v+b1*a+b2*v*tanh(F/100N)+b3*a*tanh(F/100N); F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[-0.3382437073743341, -0.19854864798499913, 0.9151437161020427, 0.6556618120791294]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_phase_bilateral

F+b0*(C-F)+b1*v+b2*vO; F=current plate1 force(N), v=2*(F-F_t-50ms), a=F-2*F_t-50ms+F_t-100ms, C=past-cycle target phase force, vO=2*(opposite-opposite_t-50ms). Coefficients dimensionless except stated flexible response coefficients N.

Coefficients: `[0.5978908238053491, 0.1933619569544959, -0.10711549461648925]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

