# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flat_calibration**

`I0`

Parameters: none.

**flexible**

`I0*(q0/q)**4*(b0+b1*q+b2*q**2+b3*q**3)+b4`

Parameters: b0 = -5.4676375, b1 = 103.0535, b2 = -559.28605, b3 = 815.90249, b4 = 20611.473.

**fresnel_tail**

`I0*(q0/q)**4`

Parameters: none.

**roughness_envelope**

`I0*(q0/q)**4*exp(-sigma**2*(q**2-q0**2))`

Parameters: sigma = 15.90302.

**finite_angle_fresnel**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))`

Parameters: qc = 0.069569551, sigma = 2.4887345e-12.

**kiessig_interference**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*cos(q*d+phase))/(1+r*cos(q0*d+phase))`

Parameters: qc = 0.061627145, sigma = 4.566309, d = 86.362353, r = 0.8615946, phase = 1.3224203.

**contrast_decoherence**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*exp(-sc**2*q**2)*cos(q*d+phase))/(1+r*exp(-sc**2*q0**2)*cos(q0*d+phase))`

Parameters: qc = 0.060431698, sigma = 4.4534327, d = 87.303891, r = 0.95, phase = 1.1981691, sc = 3.2411437.

**center_outer_thickness**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*cos(q*(d+dr*outer)+phase))/(1+r*cos(q0*(d+dr*outer)+phase))`

Parameters: qc = 0.061608648, sigma = 4.5473148, d = 87.642909, r = 0.86269467, phase = 1.3016794, dr = -1.4265312.

**instrument_background**

`I0*(((q-sqrt(maximum(q**2-qc**2,0.0000001)))/(q+sqrt(maximum(q**2-qc**2,0.0000001))))**2)/(((q0-sqrt(maximum(q0**2-qc**2,0.0000001)))/(q0+sqrt(maximum(q0**2-qc**2,0.0000001))))**2)*exp(-sigma**2*(q**2-q0**2))*(1+r*cos(q*d+phase))/(1+r*cos(q0*d+phase))+background`

Parameters: qc = 0.057375778, sigma = 6.1574655, d = 86.372444, r = 0.86971607, phase = 1.27576, background = 1677.5033.


