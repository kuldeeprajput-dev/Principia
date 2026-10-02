# Measured crowd speed across source-defined flow conditions

The archive combines measured figure tables, simulation figure tables and illustrative videos from a pedestrian-foot-tracking study. The DAT files are MATLAB binaries. This task uses only the measured specific-volume/speed tables: the authors' F2D experiment and four external condition panels F3B–F3E. Simulation F3A and algebraically derived flow outcomes are excluded.

The article identifies external unidirectional, counterflow and multidirectional sources. The two panels attributed to the multidirectional study are reserved together; development uses the other three cohorts. Every tenth source row is retained by a fixed pre-fit index rule. Missing original person/run identifiers prevent individual-level or independent-population claims.

Five hypotheses compare finite-jam exclusion, exponential encounter slowdown, free-area saturation, geometric distance headway and a two-regime law. The development-selected free-area exponential reaches0.28514m/s reserved MAE, compared with0.24194m/s for the published source law and0.27568m/s for the flexible control. Its signed bias is+0.27346m/s and its worst-condition MAE is0.40587m/s.

The positive improvement claim is therefore rejected. The useful result is a traceable transfer limitation: a stronger development fit does not establish a better law across different crowd-flow conditions. Direction, geometry, source processing and participant dependence remain confounded. No evacuation-safety benefit or new universal crowd law is admitted.

## Experimental scope and evaluation

Source-processed paired density/speed ordinates, used for retrospective condition transfer. Density is the published local spatial descriptor; the task is not an online evacuation forecast.

Calibration: No held-condition speed calibration. The supplied paper fit is an explicitly exposed prior-art baseline, not a newly discovered coefficient set.

Validation unit: Complete source figure cohorts; F3D and F3E are linked as the multidirectional-study family and reserved together. Person/run identifiers are missing, so independence within or between figure cohorts is not established.

Condition-balanced results and both individual reserved figures. F3D/F3E may share participants; no independent-cohort confidence interval.

Target: pedestrian speed (m/s). Errors use m/s. The selected reference is **free_area_exponential**. Selection was frozen before confirmation; diagnostic winners are not substituted afterward.

| Predictor | Unit |
|---|---|
| eta | m²/person specific volume |
| rho | persons/m², exact reciprocal of eta; predictor only |


## Matched comparison

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| constant | 0.542255 | 0.350905 | 0.398428 |
| flexible | 0.148966 | 0.275681 | 0.385648 |
| published_source | 0.19236 | 0.241943 | 0.338439 |
| greenshields | 0.134612 | 0.300779 | 0.432625 |
| underwood | 0.139742 | 0.311701 | 0.470036 |
| free_area_exponential | 0.127172 | 0.28514 | 0.405867 |
| distance_headway | 0.13885 | 0.282015 | 0.402514 |
| two_regime_exclusion | 0.135308 | 0.288053 | 0.405161 |


The primary error is mean group MAE. RMSE and signed bias are complementary; rows within a group do not establish independent replication. No accuracy percentage or industrial tolerance is invented.


## Executable equations and parameters

Each expression below uses the named inputs in the units table. `exp`, `log`, and `sqrt` have their conventional mathematical meanings. Coefficients are fitted on development data only; all calibration is declared above. The portable `rules.json` contains full precision and each model’s complete training scope.

**constant**

`b0`

Parameters: b0 = 0.91804327.

**flexible**

`b0+b1/(1+rho)+b2/(1+rho)**2+b3/(1+rho)**3`

Parameters: b0 = -0.61360535, b1 = 4.3674702, b2 = -0.011529246, b3 = -2.7950702.

**published_source**

`1.16*(1-exp(-4.45*maximum(eta-0.23,0)))`

Parameters: none.

**greenshields**

`v0*maximum(1-rho/rjam,0)`

Parameters: v0 = 1.616888, rjam = 3.9724652.

**underwood**

`v0*exp(-rho/rc)`

Parameters: v0 = 1.8191979, rc = 2.1960073.

**free_area_exponential**

`v0*(1-exp(-k*maximum(eta-area,0)))`

Parameters: v0 = 1.4721987, k = 2.180649, area = 0.17724007.

**distance_headway**

`minimum(v0,maximum(sqrt(eta)-ell,0)/tau)`

Parameters: v0 = 1.4114661, ell = 0.38479956, tau = 0.46165786.

**two_regime_exclusion**

`v0*minimum(1,maximum((rjam-rho)/(rjam-rfree),0))`

Parameters: v0 = 1.4701253, rjam = 3.9464206, rfree = 0.38281132.


## Applicability and limitations

- F3A simulation is excluded; source-processed plotting tables are not raw trajectories.
- Panel-to-study mapping follows the article ordered empirical-condition list and cited original studies: F3B unidirectional/Zhang2011; F3C counterflow/Zhang2012; F3D/F3E cross/four-directional/Cao2017. Exact original run accession IDs are not retained.
- Only within-source condition transfer is assessed. No independent population validation, causal pedestrian mechanism or safe capacity limit is claimed.
- Flow and gait algebraic identities are excluded as predictive targets and confirmations.

Primary article known fitted equation and schema dimensions were inspected before allocation. Reserved numerical ordinates were not viewed before freeze.

## Reproduction

Run `python run.py` in this final package to verify hashes and reproduce every saved prediction. Use `python run.py --inputs new.csv --output predictions.csv --model reference` only with the declared inputs and units. Numerical prediction evaluation does not certify novelty or mechanism. Source anchors and reserved observations are separate from predictor inputs.

Source: https://zenodo.org/records/14737521. See source/units audit and prior-art records in research history.
