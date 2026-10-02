# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**constant**

`b0`

Parameters: b0 = 0.91804327.

**flexible**

`b0+b1/(1+rho)+b2/(1+rho)**2+b3/(1+rho)**3`

Parameters: b0 = -0.61360535, b1 = 4.3674702, b2 = -0.011529246, b3 = -2.7950702.

**published_source**

`1.16*(1-exp(-4.45*maximum(eta-0.23,0)))`

Parameters: none.

**greenshields**

`v0*maximum(1-rho/rjam,0)`

Parameters: v0 = 1.616888, rjam = 3.9724652.

**underwood**

`v0*exp(-rho/rc)`

Parameters: v0 = 1.8191979, rc = 2.1960073.

**free_area_exponential**

`v0*(1-exp(-k*maximum(eta-area,0)))`

Parameters: v0 = 1.4721987, k = 2.180649, area = 0.17724007.

**distance_headway**

`minimum(v0,maximum(sqrt(eta)-ell,0)/tau)`

Parameters: v0 = 1.4114661, ell = 0.38479956, tau = 0.46165786.

**two_regime_exclusion**

`v0*minimum(1,maximum((rjam-rho)/(rjam-rfree),0))`

Parameters: v0 = 1.4701253, rjam = 3.9464206, rfree = 0.38281132.


