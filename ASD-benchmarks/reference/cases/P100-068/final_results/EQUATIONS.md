# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**driven_harmonic**

`offset+2*cos(2*3.141592653589793*32*.005)*y0-y1`

Parameters: none.

**flexible**

`offset+b0+b1*y0+b2*y1+b3*y2+b4*y3+b5*y0**2+b6*y0*y1`

Parameters: b0 = -0.094188191, b1 = 1.6536944, b2 = -1.2189762, b3 = 0.11759965, b4 = 0.33345175, b5 = 0.34873159, b6 = -0.29248496.

**persistence**

`offset+y0`

Parameters: none.

**effective_harmonic**

`offset+2*cos(omega*.005)*y0-y1`

Parameters: omega = 179.61948.

**dc_invariant_harmonic**

`offset+(1+2*cos(omega*.005))*y0-(1+2*cos(omega*.005))*y1+y2`

Parameters: omega = 205.54912.

**duffing_delay_closure**

`offset+2*y0-y1+b0+b1*y0+b2*y0**3+b3*(y0-y1)`

Parameters: b0 = -0.12865733, b1 = -0.77087352, b2 = 0.0043998097, b3 = -0.099718.

**quadratic_drag_closure**

`offset+2*y0-y1+b0+b1*y0+b2*(y0-y1)+b3*(y0-y1)*abs(y0-y1)`

Parameters: b0 = -0.12857051, b1 = -0.766421, b2 = -0.11493753, b3 = 0.021047958.

**parametric_drive_closure**

`offset+b0+b1*y0+b2*y1+b3*y0*sin(2*3.141592653589793*32*t)+b4*y0*cos(2*3.141592653589793*32*t)`

Parameters: b0 = -0.22154065, b1 = 1.2112711, b2 = -0.92698825, b3 = -0.10973142, b4 = 0.2356574.


