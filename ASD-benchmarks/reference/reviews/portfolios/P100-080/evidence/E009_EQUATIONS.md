# Frozen equations and complete coefficients

## reference

e; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_persistence

e; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_velocity

e+v; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

e+b0+sum_j b_j exp(-mean((z-center_j)^2)/2); e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[-1.633615228638837, 0.3879970690666743, 0.36019166432636435, 0.2004596689199184, 1.7900649783353384, 1.0257222249175322, 0.5665482407603436, -0.22949142532869482, -0.6934553253927658, -0.10055967855283554, 0.4734411550800949, 0.5202817107344218, 0.35778309999361924, -0.23270502312607147, -0.059380791283726676, 0.025735580873740914, 0.2140893491261083, 0.18131592280410802, 1.3123226938605153, -0.18022542662405172, 0.6051132981044995]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_relaxation

e+b0*r; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[0.06717297141912677]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_damped_drift

e+b0*v+b1*r; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[0.10154510486236827, 0.13895466840535367]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_activity

e+b0*v+b1*r+b2*A; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[0.10260580932662397, 0.14983037103050403, 1.7947281839771927]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_thermal

e+b0*v+b1*r+b2*dT; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[0.10154538437065551, 0.13895540736207584, 9.793287454151724e-05]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_asymmetry

e+b0*max(v,0)+b1*min(v,0)+b2*r; e=current5s EDA mean(uS), v=3*(e-e_t-10s),r=prior120s mean-e,A=prior10s acceleration magnitude SD(g),dT=T-T_t-30s(degreeC). v/r coefficients dimensionless,A coefficientuS/g,dT coefficientuS/degreeC,interaction coefficient1/g.

Coefficients: `[0.1611497685379877, 0.01986845718956287, 0.14818966486693633]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

