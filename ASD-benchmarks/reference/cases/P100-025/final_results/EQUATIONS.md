# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**equal_mixture**

`pre+jump*(rL+rF)/2`

Parameters: none.

**flexible**

`pre+jump*(rL+(b0+b1*f+b2*f**2+b3*discharge+b4*rest)*(rF-rL)+b5*e/100)`

Parameters: b0 = 1.0293196, b1 = 0.22334025, b2 = 0.31434266, b3 = 0.22137406, b4 = 0.048670034, b5 = 0.2160305.

**lfp_reference**

`pre+jump*rL`

Parameters: none.

**protocol_two_phase**

`pre+jump*((1-f)*rL+f*rF)`

Parameters: none.

**continuous_edge_shift**

`pre+jump*(rL-shift*f*dL+0.5*shift**2*f**2*d2L)`

Parameters: shift = 6.6705178.

**partial_transformation**

`pre+jump*(rL+clip(a+b*f,0,1)*(rF-rL))`

Parameters: a = 1, b = 1.9885868.

**intermediate_spectral_component**

`pre+jump*(rL+f*(rF-rL)+a*f*(1-f)*d2L)`

Parameters: a = 31.578538.

**branch_hysteresis**

`pre+jump*(rL+where(discharge>0,1-(1-f)**pd,f**pc)*(rF-rL))`

Parameters: pc = 0.1, pd = 8.


