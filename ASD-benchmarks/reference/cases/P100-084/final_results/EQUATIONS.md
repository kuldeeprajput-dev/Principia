# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`base+amp*(b0+b1*x+b2*x**2+b3*x**3+b4*x**4)`

Parameters: b0 = -0.14312993, b1 = -0.13844709, b2 = -0.03699308, b3 = -0.0014587107, b4 = 0.00030246077.

**hertz_shape**

`base+amp*maximum(x,0)**1.5`

Parameters: none.

**initial_level**

`base+amp`

Parameters: none.

**conical_contact**

`base+amp*maximum(x,0)**2`

Parameters: none.

**localized_adhesion**

`base+amp*maximum(x,0)**1.5-A*amp*exp(-abs(x)/ell)`

Parameters: A = 0.28997713, ell = 0.53665727.

**shifted_contact_pull_off**

`base+amp*(maximum(x+shift,0)/(1+shift))**1.5-A*amp*exp(-((x-center)/width)**2)`

Parameters: shift = -0.3, A = 0.23257463, center = 0.5, width = 0.96865225.

**rough_asperity_exponent**

`base+amp*maximum(x,0)**p-A*amp*exp(-abs(x)/ell)`

Parameters: p = 4, A = 0.26500518, ell = 0.40913028.

**hysteretic_detachment**

`base+amp*maximum(x,0)**1.5-A*amp*0.5*(1+tanh((x-xoff)/width))*(1-minimum(maximum(x,0),1))`

Parameters: A = 1.7107473, xoff = 0.5, width = 0.5.


