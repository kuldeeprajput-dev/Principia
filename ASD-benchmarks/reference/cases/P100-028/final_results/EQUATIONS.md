# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`b0*lo+b1*hi+b2*(hi-lo)*r+b3*(hi-lo)*r**2+b4*noise+b5*sep*(hi-lo)*r`

Parameters: b0 = 1.1992482, b1 = -0.22762582, b2 = 0.42375977, b3 = 0.10965828, b4 = 0.097293448, b5 = 0.029495234.

**hold_calibration**

`hi`

Parameters: none.

**linear_increment**

`lo+(hi-lo)*r`

Parameters: none.

**saturating_increment**

`maximum(lo+(hi-lo)*r*(1+k)/(1+k*r),0)`

Parameters: k = 0.009944332.

**coherent_rotation**

`maximum(lo+(hi-lo)*(sin(k*g)-sin(k*glo))/(sin(k*ghi)-sin(k*glo)),0)`

Parameters: k = 3.4152271.

**detuning_saturation**

`maximum(lo+(hi-lo)*r*(1+k0+k1*sep)/(1+(k0+k1*sep)*r),0)`

Parameters: k0 = 1.350705e-16, k1 = 0.0087108042.

**incoherent_power_mixing**

`sqrt(maximum(lo**2+(hi**2-lo**2)*r,0))`

Parameters: none.

**pump_induced_loss**

`maximum(lo+(hi-lo)*(g*exp(-k*g**2)-glo*exp(-k*glo**2))/(ghi*exp(-k*ghi**2)-glo*exp(-k*glo**2)),0)`

Parameters: k = 2.0044305.


