# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`b0+b1*hx+b2*hy+b3*ox+b4*oy+b5*dg`

Parameters: b0 = -1.4395409e-07, b1 = 0.52181762, b2 = 0.66219179, b3 = -0.090550196, b4 = -0.26870013, b5 = 0.19873701.

**local_mean**

`(hx+hy)/2`

Parameters: none.

**zero_field**

`0`

Parameters: none.

**fault_axis_anisotropy**

`w*hx+(1-w)*hy`

Parameters: w = 0.49266599.

**dipole_curvature**

`(4*(hx+hy)-(ox+oy))/6`

Parameters: none.

**domain_boundary_adaptive**

`(hx/(gx*gx+eps*eps)+hy/(gy*gy+eps*eps))/(1/(gx*gx+eps*eps)+1/(gy*gy+eps*eps))`

Parameters: eps = 1.4555642.

**finite_footprint_smoothing**

`(hx+hy)/2+k*((ox+oy)-(hx+hy))/2`

Parameters: k = 8.6531364e-21.

**bounded_extrema**

`clip((4*(hx+hy)-(ox+oy))/6,lo,hi)`

Parameters: none.


