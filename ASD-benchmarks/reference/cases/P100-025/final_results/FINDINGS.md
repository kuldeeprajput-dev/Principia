# Two-phase versus shifting-edge descriptions of operando LFP spectra

The archive contains operando X-ray absorption spectra, reference compounds, electrochemical records and author analyses. This task retains the 194 original LiFePO4 spectra and two supplied endpoint references. Three consecutive spectra remain linked because the source also distributes three-spectrum averaged representations. Thirteen complete triplets were reserved by a fixed identifier hash.

The endpoint is the original dimensionless absorption ordinate, scored in the 7070-7200 eV edge window. Each spectrum supplies fixed pre-edge and post-edge calibration outside that window. Consequently, this is retrospective spectral compression rather than online state-of-charge prediction.

The selected six-coefficient response model yields reserved MAE 0.06130, against 0.13619 for a nominal-time two-phase mixture. Its predictors are the two reference shapes, nominal protocol progress, discharge/rest indicators and a linear energy term. The five more restrictive mechanistic candidates did not improve development accuracy.

This outcome supports a reproducible compression reference and a useful negative constraint: clock progress alone is not a validated phase-fraction measurement. The fitted mixture coefficient must not be interpreted as an absolute FePO4 fraction. One sequence cannot establish general battery transfer or a new electrochemical mechanism.

## Experimental scope and evaluation

Retrospective spectral-shape reconstruction after pre/post-edge calibration bands and experimental segment durations are known. This is not an online state-of-charge forecast.

Calibration: Each spectrum contributes only 7000-7050 eV and 7250-7300 eV band means. Supplied measured FePO4/LiFePO4 references are normalized identically. Target band 7070-7200 eV is withheld.

Validation unit: Complete three-acquisition block linked to the source 3×binned representation; one LFP cycle only. Five contiguous chronological development folds holdout whole blocks, with future development segments allowed for this retrospective compression task.

Report whole triplet-block errors; dependent blocks from one cycle do not yield independent-cell confidence.

Target: raw measured FeK-edge μ(E) (dimensionless μ(E)). Errors use dimensionless μ(E). The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| pre | raw μ(E), dimensionless |
| jump | raw μ(E), dimensionless |
| rL | normalized measured LiFePO4 reference |
| rF | normalized measured FePO4 reference |
| dL | $\mathrm{eV}^{-1}$ |
| d2L | $\mathrm{eV}^{-2}$ |
| f | dimensionless nominal protocol progress |
| discharge | binary discharge/rest 2 branch |
| rest | binary rest segment |
| e | eV relative 7112 |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| equal_mixture | 0.136341 | 0.143238 | 0.161557 |
| flexible | 0.0612244 | 0.0613018 | 0.0777837 |
| lfp_reference | 0.176445 | 0.185151 | 0.203821 |
| protocol_two_phase | 0.141528 | 0.136187 | 0.177433 |
| continuous_edge_shift | 0.146753 | 0.141959 | 0.177433 |
| partial_transformation | 0.10592 | 0.112433 | 0.131155 |
| intermediate_spectral_component | 0.138931 | 0.132147 | 0.177433 |
| branch_hysteresis | 0.120676 | 0.119764 | 0.177433 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Selected equation and coefficients

$$
\widehat\mu=\mu_{\rm pre}+J\left[r_L+(b_0+b_1f+b_2f^2+b_3D+b_4R)(r_F-r_L)+b_5e/100\right]
$$

Here pre is the measured pre-edge level, J is the calibrated edge jump, r_L and r_F are normalized measured LFP/FP reference values, f is nominal segment progress, D and R identify discharge and rest, and e is the declared energy offset in eV. The effective mixing coefficient is unconstrained and is not a phase fraction.

| Coefficient | Frozen value |
|---|---:|
| b0 | 1.0293196 |
| b1 | 0.223340251 |
| b2 | 0.314342655 |
| b3 | 0.221374055 |
| b4 | 0.0486700336 |
| b5 | 0.2160305 |

All comparator expressions, numerical guards and full-precision values remain in EQUATIONS.md, rules.json and run.py.

## Applicability and limitations

- Nominal progress is normalized reported segment time, not measured state of charge or an identified phase fraction.
- Author 3×binned spectra are excluded as duplicate observations; only unbinned columns are targets.
- One cell/one cycle; cross-block calibration success does not establish new battery chemistry or industrial cycle transfer.

Only far pre-edge initial rows near 6404 eV were inspected for schema. Target band 7070-7200 eV reserved values were unseen before freeze.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/14922524. See source/units audit and prior-art records in research history.
