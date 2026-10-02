# Same-date ocean anomaly map reconstruction

The input is one NOAA global nighttime sea-surface-temperature anomaly map, dated16August2026, with a1991–2020 climatological baseline. Its NetCDF contains one time plane, a0.01degreeC scale factor and explicit water, land, missing and ice flags. This is a processed satellite product.

The task reconstructs fixed water-pixel targets from twelve neighboring pixels on the same map. Target centers lie on a40pixel lattice; none of those centers can appear among any other target's calibration pixels. Complete20degree geographic tiles are assigned by a fixed hash, with23 eligible tiles reserved.

The selected six-coefficient local stencil achieves0.03284degreeC tile-balanced MAE and0.06714degreeC worst-tile MAE. Unweighted local averaging gives0.05750 and0.2450degreeC. Eight attempts examined spherical distances, Taylor curvature cancellation, directional fronts, diagonal geometry, curvature limiting, latitude correction, range preservation and observation-noise averaging.

These results establish useful numerical reconstruction references. They do not establish ocean dynamics, future heat stress or coral bleaching thresholds. The same-map calibration and exclusion of incomplete coastal/ice neighborhoods are essential parts of the task, and no population confidence is inferred from dependent pixels.

## Experimental scope and evaluation

Retrospective reconstruction of one daily map, using twelve fixed neighboring pixels from the same date. Not a future forecast.

Calibration: Cardinal neighbors at4 and8 pixels plus four diagonal neighbors at4pixels. Target centers lie on a40pixel lattice and can never be calibration pixels for any scored center.

Validation unit: Complete20degree geographic tile for scoring; all tiles belong to one dependent global map, not independent temporal replicates.

Tile-balanced errors and individual tile results only; no population confidence from dependent pixels.

Target: SST anomaly at a withheld pixel (degree C). Errors use degree C. The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| hx | degree C |
| hy | degree C |
| ox | degree C |
| oy | degree C |
| dg | degree C |
| gx | degree C |
| gy | degree C |
| clat | dimensionless cosine latitude |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 0.0356912 | 0.0328365 | 0.0671359 |
| local_mean | 0.0521489 | 0.0574952 | 0.245 |
| zero_anomaly | 0.853588 | 0.798152 | 2.05919 |
| spherical_distance | 0.0501236 | 0.0503713 | 0.134759 |
| fourth_order_smooth | 0.0398408 | 0.0401033 | 0.136667 |
| front_adaptive | 0.0507908 | 0.0496442 | 0.0785472 |
| rotational_ninepoint | 0.0444504 | 0.0454642 | 0.14875 |
| limited_curvature | 0.0392258 | 0.0378708 | 0.101033 |
| latitude_curvature | 0.0371352 | 0.0345851 | 0.0798387 |
| range_preserving | 0.0436794 | 0.0441662 | 0.136667 |
| broad_noise_average | 0.0837839 | 0.0952444 | 0.4075 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


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


## Applicability and limitations

- Fixed complete-water neighborhoods exclude coasts, ice and missing neighborhoods.
- No climate evolution, causal ocean mechanism or coral bleaching hazard is identified. This is not the NOAA coral bleaching heat-stress product.

Only dimensions, flags, coordinates and scale metadata were inspected before this fixed geometry/hash split. All resulting scores become exposed.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://coralreefwatch.noaa.gov/product/5km/index_5km_ssta_clim19912020.php. See source/units audit and prior-art records in research history.
