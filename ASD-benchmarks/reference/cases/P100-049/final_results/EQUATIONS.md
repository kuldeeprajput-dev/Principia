# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**fixed_rc**

`u120+(u120-u60)*(exp(-t/300)-exp(-t120/300))/(exp(-t120/300)-exp(-t60/300))`

Parameters: none.

**flexible**

`u120+b0*(u120-u60)+b1*(u120-u60)*log(t/t120)+b2*(u120-u60)*log(t/t120)**2+b3*(u120-u10)`

Parameters: b0 = -1.5063359, b1 = 1.4451086, b2 = -0.067591093, b3 = 0.42957476.

**persistence**

`u120`

Parameters: none.

**finite_pulse_diffusion**

`u120+(u120-u60)*(sqrt(t+pulse_s)-sqrt(t)-sqrt(t120+pulse_s)+sqrt(t120))/(sqrt(t120+pulse_s)-sqrt(t120)-sqrt(t60+pulse_s)+sqrt(t60))`

Parameters: none.

**learned_rc**

`u120+(u120-u60)*(exp(-t/tau)-exp(-t120/tau))/(exp(-t120/tau)-exp(-t60/tau))`

Parameters: tau = 204.3657.

**fractional_tail**

`u120+(u120-u60)*(t**(-alpha)-t120**(-alpha))/(t120**(-alpha)-t60**(-alpha))`

Parameters: alpha = 0.066641325.

**diffusion_rc_mixture**

`u120+(u120-u60)*(((1-w)*(sqrt(t+pulse_s)-sqrt(t))/sqrt(pulse_s)+w*exp(-t/tau))-((1-w)*(sqrt(t120+pulse_s)-sqrt(t120))/sqrt(pulse_s)+w*exp(-t120/tau)))/(((1-w)*(sqrt(t120+pulse_s)-sqrt(t120))/sqrt(pulse_s)+w*exp(-t120/tau))-((1-w)*(sqrt(t60+pulse_s)-sqrt(t60))/sqrt(pulse_s)+w*exp(-t60/tau)))`

Parameters: w = 6.3752069e-12, tau = 10.

**boundary_storage**

`u120+(u120-u60)*clip(a+b*u120,0,3)*((sqrt(t+pulse_s)-sqrt(t))-(sqrt(t120+pulse_s)-sqrt(t120)))/((sqrt(t120+pulse_s)-sqrt(t120))-(sqrt(t60+pulse_s)-sqrt(t60)))`

Parameters: a = 0.93003938, b = 0.19250262.


