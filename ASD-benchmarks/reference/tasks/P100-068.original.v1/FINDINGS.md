# Native-voltage dynamics of an acoustically levitated object

The archive contains 31 raw laser-Doppler voltage traces and paired noise-reduced representations from an acoustically levitated object. This task forecasts the raw voltage 5 ms ahead, using only a 15 ms causal delay history and an initial offset calibration. The paired GHKSS outputs never serve as targets or predictors. Most stored traces use a 0.5 ms step; trace1172 uses 1 ms, and the adapter preserves both grids while maintaining the physical forecast horizon.

The strongest development-selected result is the constrained seven-coefficient delay predictor, with 0.109 V reserved MAE across six traces. This is a reproducible forecast reference, not a discovered mechanical law. A useful complementary result is that a DC-invariant harmonic recurrence reduces reserved error from 0.197 to 0.133 V and largely removes systematic bias.

For a known constant-plus-harmonic signal, the recurrence is V̂=offset+(1+2cosωh)y₀−(1+2cosωh)y₁+y₂, with h=0.005 s and yⱼ the centered voltage at j delayed steps. Its coefficients sum to one, preserving a constant level. The measured improvement tests the relevance of that invariance, rather than claiming the identity is new.

The source paper and supplied code disagree on the LDV velocity conversion. Consequently, voltage remains the endpoint, and fitted nonlinear delay coefficients are not labeled as damping, stiffness or mechanical force coefficients. Whole-trace transfer in one installation is the maximum supported scope.

## Experimental scope and evaluation

Predict raw voltage5ms ahead using up to15ms of causal delay samples and a fixed initial20sampleoffset. Issue every5ms after50ms; no future filtering.

Calibration: Initial20 raw samples only; no GHKSS/noise-reducedseries or future spectral estimate is used.

Validation unit: Complete acquisitiontrace, with raw/denoised pair linked; sixmetadata-hashselectedtracesconfirm. Alltraces shareone levitator/object setup.

Complete-trace errors; no claim of independentobjectpopulationconfidence.

Target: raw LDV voltage5ms ahead (V). Errors use V. The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| y0 | V; currentrawminusinitialoffset |
| y1 | V;5mslagminusoffset |
| y2 | V;10mslagminusoffset |
| y3 | V;15mslagminusoffset |
| offset | V; first20samplemean |
| t | s; storedtimestamp |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| driven_harmonic | 0.241871 | 0.213469 | 0.726943 |
| flexible | 0.105944 | 0.109126 | 0.190553 |
| persistence | 0.520368 | 0.438805 | 0.585286 |
| effective_harmonic | 0.222198 | 0.197191 | 0.589883 |
| dc_invariant_harmonic | 0.162204 | 0.133286 | 0.21399 |
| duffing_delay_closure | 0.188062 | 0.185089 | 0.466788 |
| quadratic_drag_closure | 0.18744 | 0.186061 | 0.470078 |
| parametric_drive_closure | 0.165916 | 0.191568 | 0.453074 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


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


## Applicability and limitations

- Primarysource conversion lists125/4 while suppliedMATLABcode uses500/4; nativevoltage is retained to avoid asserting an unsupportedvelocityscale.
- Stored1/2kHz sample grids differs from article4kHz acquisition; the adapter preserves storedtiming.
- The filename-to-excitation-amplitude mapping is not supplied. Cross-traceprediction is not proof of independentobject or arbitraryexcitationtransfer.
- Polynomial coefficients in voltage-delay space are not mechanical force coefficients.

Firstthree rawsamples of1142n were seen during schema audit, beforethe50mseligible issuance window. No reserved target values were inspected.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/16033764. See source/units audit and prior-art records in research history.
