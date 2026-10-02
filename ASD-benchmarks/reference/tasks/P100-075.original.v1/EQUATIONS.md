# Explicit frozen equations

## reference

y_hat=max(0,c+b1*s)

Coefficients in equation order: `[-0.8590802454101593]`; K = 200.0 kPa.

## baseline_copy

y_hat=c

Coefficients in equation order: `[]`; K = 200.0 kPa.

## baseline_log_additive

y_hat=max(0,c+b1*ln(E/30)+b2*s)

Coefficients in equation order: `[-0.05662530206803568, -0.7570852818573747]`; K = 200.0 kPa.

## baseline_quadratic

y_hat=max(0,c+b1*x+b2*s+b3*x*s+b4*x^2+b5*x^2*s), x=ln(E/30)

Coefficients in equation order: `[0.5812978260495674, -1.240440018423564, -0.08382356981264968, -0.24487275128872252, 0.1607349548852278]`; K = 200.0 kPa.

## attempt_001_saturation

y_hat=max(0,c+b1*q+b2*s), q=E/(K+E)-30/(K+30)

Coefficients in equation order: `[-1.4342459653760593, -0.7191465948627176]`; K = 3000.0 kPa.

## attempt_002_synergy

y_hat=max(0,c+b1*x+b2*s+b3*x*s), x=ln(E/30)

Coefficients in equation order: `[-0.18115186155916724, -1.3356950200122222, 0.4457576287641661]`; K = 200.0 kPa.

## attempt_003_mechanical_only

y_hat=max(0,c+b1*ln(E/30))

Coefficients in equation order: `[-0.18531488265548213]`; K = 200.0 kPa.

## attempt_004_threshold

y_hat=max(0,c+b1*I(E>=200)+b2*s+b3*s*I(E>=200))

Coefficients in equation order: `[-0.3254507254626259, -1.431804721918484, 1.184537444997816]`; K = 200.0 kPa.

## attempt_005_shear_only

y_hat=max(0,c+b1*s)

Coefficients in equation order: `[-0.8590802454101593]`; K = 200.0 kPa.

## attempt_006_calibration_scaling

y_hat=max(0,c+b1*x+b2*s+b3*x*s+b4*(c-5)*s), x=ln(E/30)

Coefficients in equation order: `[-0.18115186155916702, -1.9295159119836087, 0.44575762587104095, -0.46242639365185434]`; K = 200.0 kPa.

## attempt_007_saturating_synergy

y_hat=max(0,c+b1*q+b2*s+b3*q*s), q=E/(K+E)-30/(K+30)

Coefficients in equation order: `[-3.7380263998239034, -1.1454083391499525, 6.672738040758973]`; K = 3000.0 kPa.

