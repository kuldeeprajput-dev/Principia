# Native-voltage dynamics of an acoustically levitated object

The archive contains 31 raw laser-Doppler voltage traces and paired noise-reduced representations from an acoustically levitated object. This task forecasts the raw voltage 5 ms ahead, using only a 15 ms causal delay history and an initial offset calibration. The paired GHKSS outputs never serve as targets or predictors. Most stored traces use a 0.5 ms step; trace 1172 uses 1 ms, and the adapter preserves both grids while maintaining the physical forecast horizon.

The strongest development-selected result is the constrained seven-coefficient delay predictor, with 0.109 V reserved MAE across six traces. This is a reproducible forecast reference, not a discovered mechanical law. A useful complementary result is that a DC-invariant harmonic recurrence reduces reserved error from 0.197 to 0.133 V and largely removes systematic bias.

For a known constant-plus-harmonic signal, a third-order recurrence preserves a constant offset: $\widehat V=V_0+(1+2\cos\omega h)y_0-(1+2\cos\omega h)y_1+y_2$, where $h=0.005$ s and the delayed values are centered on $V_0$. Its delay coefficients sum to one. The measured improvement tests the relevance of that invariance, rather than claiming the identity is new.

The source paper and supplied code disagree on the LDV velocity conversion. Consequently, voltage remains the endpoint, and fitted nonlinear delay coefficients are not labeled as damping, stiffness or mechanical force coefficients. Whole-trace transfer in one installation is the maximum supported scope.

## Experimental scope and evaluation

Predict raw voltage 5 ms ahead using up to 15 ms of causal delay samples and a fixed initial 20 sample offset. Issue every 5 ms after 50 ms; no future filtering.

Calibration: Initial 20 raw samples only; no GHKSS/noise-reduced series or future spectral estimate is used.

Validation unit: Complete acquisition trace, with raw/denoised pair linked; six metadata-hash-selected traces confirm. Alltraces shareone levitator/object setup.

Complete-trace errors; no claim of independent object-population confidence.

Target: raw LDV voltage 5 ms ahead (V). Errors use V. The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| y0 | V; current raw value minus initial offset |
| y1 | V; 5 ms lag minus offset |
| y2 | V; 10 ms lag minus offset |
| y3 | V; 15 ms lag minus offset |
| offset | V; first 20 sample mean |
| t | s; stored timestamp |


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


## Selected equation and coefficients

$$
\widehat V=V_0+b_0+b_1y_0+b_2y_1+b_3y_2+b_4y_3+b_5y_0^2+b_6y_0y_1
$$

V0 is the initial offset and y0 through y3 are declared causal voltage delays relative to it. b0 is in V, the linear coefficients are dimensionless and quadratic coefficients are in V^-1. Unresolved LDV conversion precludes a velocity-unit claim.

| Coefficient | Frozen value |
|---|---:|
| b0 | -0.0941881909 |
| b1 | 1.65369442 |
| b2 | -1.21897618 |
| b3 | 0.117599654 |
| b4 | 0.333451745 |
| b5 | 0.348731593 |
| b6 | -0.292484962 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Primary source conversion lists 125/4 while supplied MATLAB code uses 500/4; native voltage is retained to avoid asserting an unsupported velocity scale.
- Stored 1/2 kHz sample grids differs from article 4 kHz acquisition; the adapter preserves stored timing.
- The filename-to-excitation-amplitude mapping is not supplied. Cross-trace prediction is not proof of independent object or arbitrary excitation transfer.
- Polynomial coefficients in voltage-delay space are not mechanical force coefficients.

First three raw samples of 1142n were seen during schema audit, beforethe 50 ms eligible issuance window. No reserved target values were inspected.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/16033764. See source/units audit and prior-art records in research history.
