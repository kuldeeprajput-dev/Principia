# Frozen equations and complete coefficients

## reference

max(0,p); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_persistence

max(0,p); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_velocity

max(0,p+v); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## baseline_flexible

max(0,p+b0+sum_j b_j exp(-mean((z-center_j)^2)/2)); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[0.29901295179129894, 0.9453339048160002, -0.12380141953305546, 0.5114869058980785, -0.06896876139046289, 0.865514320013273, 0.06779666057290942, 0.09426186942618572, -1.7057414892298786, -0.12936311655656102, -0.021997464949562458, -0.08461705124296504, 0.5663807912231585, 0.09360445383858332, -0.1111476388852655, 0.4602964776835843, -1.57345367844368, -0.41008183821796684, -0.12316394860178903, 0.30359105072847165, -0.2425359693859176]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_001_relaxation

max(0,p+b0*r); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[0.14025724451764782]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_002_inertia

max(0,p+b0*r+b1*v); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[0.1941185640382664, 0.08274017646100337]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_003_arousal

max(0,p+b0*r+b1*v+b2*u+b3*du); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[0.19604297660635986, 0.08236840341781625, 0.32103097739432845, 0.4513379980953617]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_004_asymmetry

max(0,p+b0*r+b1*max(v,0)+b2*min(v,0)); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[0.19155969942182574, 0.03431794030366944, 0.14690699520673295]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

## attempt_005_curvature

max(0,p+b0*r+b1*v+b2*a); p=current quarter-second radius(px), r=preceding5s mean-p, v=2*(p-p_t-0.5s), a=p-2*p_t-0.5s+p_t-1s, u=ln(1+speed/(1cm/s)),du=u-u_t-1s. Coefficients of pixel features dimensionless; u/du coefficients px.

Coefficients: `[0.1013210875698881, -0.05506367934765827, 0.23510211552144378]`.

Training-only transformations and calibration parameters, when present, are complete in rules.json. Their arrays are part of the state and must not be refit on the scoring cohort.

