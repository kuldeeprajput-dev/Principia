# Complete frozen equation register

## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**flexible**

`b0+b1*hx+b2*hy+b3*ox+b4*oy+b5*dg`

Parameters: b0 = 0.0029814451, b1 = 1.0216572, b2 = 0.67311325, b3 = -0.20132167, b4 = -0.098214832, b5 = -0.39762085.

**local_mean**

`(hx+hy)/2`

Parameters: none.

**zero_anomaly**

`0`

Parameters: none.

**spherical_distance**

`(hx+clat**2*hy)/(1+clat**2)`

Parameters: none.

**fourth_order_smooth**

`(4*(hx+hy)-(ox+oy))/6`

Parameters: none.

**front_adaptive**

`(hx/(gx*gx+eps*eps)+hy/(gy*gy+eps*eps))/(1/(gx*gx+eps*eps)+1/(gy*gy+eps*eps))`

Parameters: eps = 0.43935922.

**rotational_ninepoint**

`(4*(hx+hy)-2*dg)/6`

Parameters: none.

**limited_curvature**

`(hx+hy)/2+k*((hx+hy)-(ox+oy))/2/(1+a*(gx*gx+gy*gy))`

Parameters: k = 0.44297639, a = 6.3108872e-30.

**latitude_curvature**

`(hx+clat**2*hy)/(1+clat**2)+k*((hx-ox)+clat**2*(hy-oy))/(1+clat**2)`

Parameters: k = 0.45570864.

**range_preserving**

`clip((4*(hx+hy)-(ox+oy))/6,minimum(hx,hy),maximum(hx,hy))`

Parameters: none.

**broad_noise_average**

`(hx+hy+ox+oy)/4`

Parameters: none.


