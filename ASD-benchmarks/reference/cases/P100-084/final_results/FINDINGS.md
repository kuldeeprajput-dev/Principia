# Contact and adhesion in calibrated AFM retraction curves

The source contains paired approach/retraction AFM curves from flat, low-roughness and high-roughness cellulose acetate surfaces. The task predicts later retraction force after the complete approach and the first five retraction measurements are available. Those measurements constitute explicit calibration, rather than hidden target information. Measured deflection at the predicted point is excluded because force is its calibrated multiple.

A spherical-contact shape plus localized attraction is the development-selected reference. It obtains 1.360 nN reserved curve-balanced MAE, compared with 2.212 nN for the repulsive spherical shape and 1.522 nN for the flexible polynomial. It also improves reserved RMSE and worst-curve error over the polynomial. A later diagnostic exponent model has lower confirmation MAE but does not replace the frozen reference.

The equation below combines a repulsive spherical-contact shape with localized attraction. Force baseline and calibrated amplitude are in nN. The coordinate $x$ is dimensionless normalized piezo position relative to a fixed approach-force crossing; adhesion ratio and decay length are dimensionless. Because $x$ is not true indentation, this effective surrogate cannot certify Young’s modulus, adhesion energy or a new constitutive law.

There are 13 curve locations and three physical sample categories, with one whole curve per category reserved. Neither independent manufacturing transfer nor a biological cell-response claim is established.

## Experimental scope and evaluation

Predict late retraction after the entire approach and first five retraction samples are available. Targets begin at retraction index 16. Measured retraction deflection is excluded because it algebraically determines force.

Calibration: Approach baseline, first 5 nN above baseline crossing, known ramp extent, and initial five retraction force samples. Every candidate receives the same frozen summaries.

Validation unit: Complete approach/retraction curve is held together; one hash-selected curve per surface type confirms. Curves are locations on three samples, not independent manufacturing batches.

Curve-wise errors; three held curve locations do not justify independent material-population confidence.

Target: native AFM retraction force (nN). Errors use nN. The selected reference is **localized_adhesion**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| x | dimensionless normalized piezo position relative to fixed 5 nN approach crossing |
| base | nN; mean first 10 approach points |
| amp | nN; initial retraction level minus base |
| progress | dimensionless fraction of retraction ramp |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| flexible | 1.66724 | 1.52241 | 1.81065 |
| hertz_shape | 2.11141 | 2.21229 | 2.9722 |
| initial_level | 38.1091 | 38.0093 | 38.7841 |
| conical_contact | 2.01419 | 2.12941 | 2.78362 |
| localized_adhesion | 1.56177 | 1.35975 | 1.72774 |
| shifted_contact_pull_off | 1.81803 | 1.39355 | 1.88172 |
| rough_asperity_exponent | 1.64024 | 1.28194 | 1.54597 |
| hysteretic_detachment | 1.72594 | 1.3856 | 2.21132 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Selected equation and coefficients

$$
\widehat F=F_0+A_0\max(x,0)^{3/2}-aA_0e^{-|x|/\ell}
$$

F0 and A0 are the permitted baseline and approach-calibrated amplitude in nN. The calibrated x, adhesion ratio a and length ell are dimensionless. The registered task excludes measured target retraction deflection, which would determine force algebraically.

| Coefficient | Frozen value |
|---|---:|
| A | 0.289977133 |
| ell | 0.536657266 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Piezo position is not true indentation; effective contact models are predictive surrogates, not certified elastic moduli.
- No stem-cell response measurements are present in this retained package; no osteogenesis conclusion follows.
- Ramp sampling frequency is not resolved; progress is dimensionless and no relaxation time in seconds is inferred.

Schema showed initial retraction rows that are inside the declared first-five calibration window, plus a few first approach rows. Late reserved retraction targets were not inspected.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/20281797. See source/units audit and prior-art records in research history.
