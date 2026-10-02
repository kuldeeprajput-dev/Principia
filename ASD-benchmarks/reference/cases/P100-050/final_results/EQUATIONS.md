# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**constant_velocity**

`h+0.2*v`

Parameters: none.

**flexible**

`b0+b1*h0+b2*h+b3*v+b4*a+b5*median`

Parameters: b0 = 0.0057035073, b1 = 0.68530464, b2 = 1.307392, b3 = -0.041932873, b4 = 0.0013639129, b5 = -1.1107696.

**persistence**

`h0`

Parameters: none.

**damped_velocity**

`h+v*tau*(1-exp(-0.2/tau))`

Parameters: tau = 0.002.

**oscillatory_memory**

`h+v*sin(omega*0.2)/omega+a*(1-cos(omega*0.2))/omega**2`

Parameters: omega = 24.355282.

**depth_dependent_memory**

`h+v*0.2/(1+k*sqrt(maximum(h,0)))`

Parameters: k = 10000.

**front_recession_asymmetry**

`h+v*where(v>0,tau_up*(1-exp(-0.2/tau_up)),tau_down*(1-exp(-0.2/tau_down)))`

Parameters: tau_up = 0.002, tau_down = 0.002.

**robust_surface_level**

`median`

Parameters: none.


