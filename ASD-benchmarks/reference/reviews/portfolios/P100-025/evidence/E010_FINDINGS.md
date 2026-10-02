# Two-phase versus shifting-edge descriptions of operando LFP spectra

The archive contains operando X-ray absorption spectra, reference compounds, electrochemical records and author analyses. This task retains the 194 original LiFePO4 spectra and two supplied endpoint references. Three consecutive spectra remain linked because the source also distributes three-spectrum averaged representations. Thirteen complete triplets were reserved by a fixed identifier hash.

The endpoint is the original dimensionless absorption ordinate, scored in the 7070–7200 eV edge window. Each spectrum supplies fixed pre-edge and post-edge calibration outside that window. Consequently, this is retrospective spectral compression rather than online state-of-charge prediction.

The selected six-coefficient response model yields reserved MAE 0.06130, against 0.13619 for a nominal-time two-phase mixture. Its predictors are the two reference shapes, nominal protocol progress, discharge/rest indicators and a linear energy term. The five more restrictive mechanistic candidates did not improve development accuracy.

This outcome supports a reproducible compression reference and a useful negative constraint: clock progress alone is not a validated phase-fraction measurement. The fitted mixture coefficient must not be interpreted as an absolute FePO4 fraction. One sequence cannot establish general battery transfer or a new electrochemical mechanism.

## Experimental scope and evaluation

Retrospective spectral-shape reconstruction after pre/post-edge calibration bands and experimental segment durations are known. This is not an online state-of-charge forecast.

Calibration: Each spectrum contributes only7000–7050eV and7250–7300eV bandmeans. SuppliedmeasuredFePO4/LiFePO4references are normalized identically. Targetband7070–7200eV is withheld.

Validation unit: Complete three-acquisitionblock linked to the source3×binnedrepresentation; oneLFPcycleonly. Fivecontiguouschronologicaldevelopmentfolds holdout wholeblocks, withfuturedevelopmentsegments allowed for thisretrospectivecompressiontask.

Reportwholetripletblock errors; dependentblocksfromonecycle do not yieldindependent-cellconfidence.

Target: raw measured FeK-edge μ(E) (dimensionless μ(E)). Errors use dimensionless μ(E). The selected reference is **flexible**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| pre | rawμ(E),dimensionless |
| jump | rawμ(E),dimensionless |
| rL | normalizedmeasuredLiFePO4reference |
| rF | normalizedmeasuredFePO4reference |
| dL | eV⁻¹ |
| d2L | eV⁻² |
| f | dimensionlessnominalprotocolprogress |
| discharge | binarydischarge/rest2branch |
| rest | binaryrestsegment |
| e | eVrelative7112 |


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


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**equal_mixture**

`pre+jump*(rL+rF)/2`

Parameters: none.

**flexible**

`pre+jump*(rL+(b0+b1*f+b2*f**2+b3*discharge+b4*rest)*(rF-rL)+b5*e/100)`

Parameters: b0 = 1.0293196, b1 = 0.22334025, b2 = 0.31434266, b3 = 0.22137406, b4 = 0.048670034, b5 = 0.2160305.

**lfp_reference**

`pre+jump*rL`

Parameters: none.

**protocol_two_phase**

`pre+jump*((1-f)*rL+f*rF)`

Parameters: none.

**continuous_edge_shift**

`pre+jump*(rL-shift*f*dL+0.5*shift**2*f**2*d2L)`

Parameters: shift = 6.6705178.

**partial_transformation**

`pre+jump*(rL+clip(a+b*f,0,1)*(rF-rL))`

Parameters: a = 1, b = 1.9885868.

**intermediate_spectral_component**

`pre+jump*(rL+f*(rF-rL)+a*f*(1-f)*d2L)`

Parameters: a = 31.578538.

**branch_hysteresis**

`pre+jump*(rL+where(discharge>0,1-(1-f)**pd,f**pc)*(rF-rL))`

Parameters: pc = 0.1, pd = 8.


## Applicability and limitations

- Nominalprogress is normalizedreportedsegmenttime, not measuredstateofcharge or an identifiedphasefraction.
- Author3×binned spectra are excluded as duplicateobservations; onlyunbinnedcolumns are targets.
- Onecell/onecycle; cross-blockcalibration successdoesnotestablishnewbatterychemistry orindustrialcycletransfer.

Onlyfarpreedgeinitialrows near6404eV were inspected forschema. Targetband7070–7200eV reservedvalues were unseen beforefreeze.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/14922524. See source/units audit and prior-art records in research history.
