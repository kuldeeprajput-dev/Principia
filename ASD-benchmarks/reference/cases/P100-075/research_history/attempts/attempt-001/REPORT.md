# Attempt 1

The additive log-stiffness baseline (0.956) loses to donor calibration (0.919). Test whether a bounded stiffness occupancy q=E/(K+E)-30/(K+30) avoids over-extrapolating mechanosensing; select K only inside each training fold. Reject a uniquely identified biochemical binding constant if its profile is flat or boundary selected.

Initial post-baseline hypothesis

Primary group-balanced error: 0.9473969388546045. Previous incumbent: 0.9191598813389589. Gain>1%: False. Worst-group MAE: 1.0428588578983355.

Equation: y_hat=max(0,c+b1*q+b2*s), q=E/(K+E)-30/(K+30)

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
