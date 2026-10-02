# P100-071: Dataset Based on Chinese Hamster Ovary (CHO) Cultivations including Turbidity, Permittivity, O2 and CO2 Measurements

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Bioprocess engineering. The current default task predicts Viable-cell density in million cells/mL. Independent unit: experiment pair (both reactors). Its packaged cohort contains 92 assigned rows in 3 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Retrospective extension:** A causal decline gate improves the original exposed spectral rule, but the negative spectral comparator and pair heterogeneity block a biological interpretation.

Limit: The apparent advantage over flexible wins only one of three exposed pairs; the strongest development spectral control remains better. Source sensor-quality and availability controls remain essential.

**Unsupported or falsified:** The proposed optical/electrical moment closure loses to a stronger linear spectral control.

Limit: Only 2/9 pairs improve. Earlier decline correction improves oldreference by 22.70% on exposedpairs but its gain over flexible control wins only 1/3 pairs.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Viable-cell density (million cells/mL) | original corpus |
| round2 | Viable-cell density (million cells/mL) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Inline estimation of viable CHO cell density
> P100-071 | Scenario and findings | September 2026 reference results

The practical question is whether inline dielectric and optical measurements can estimate viable-cell density without using future or offline responses as predictors. A compact spectral correction improves a simple permittivity calibration modestly, but does not establish a cell-size mechanism or match the best flexible comparator.

## 1. Scenario and available measurements

The OWL University dataset contains 24 CHO-K1 cultivations organized as 12 paired experiments: nine batch and three fed-batch pairs, with two parallel reactors per experiment. Native workbooks and author-aligned tables contain inline turbidity, dielectric spectra, gas and process measurements alongside offline reference measurements. The source reports 48 variables and working volumes of 0.55-0.8 L.

The pilot predicts viable-cell density (VCD) at offline sampling times, expressed in million cells/mL. Offline counts supply the measured target; their recorded standard errors are retained as context. Neither offline VCD nor its uncertainty is an online input. The paired reactors share an experimental group and are not split between training and validation.

## 2. Experimental method

Nine pairs supported development: seven batch and two fed-batch. A fixed metadata-based allocation reserved EXP005 and EXP009 (batch) and EXP012 (fed-batch), giving six reactors and 92 measured reference rows. Five substantive attempts studied optical response, dielectric size correction, sensor fusion, causal memory and conductivity effects. Grouped development validation and a simplicity decision preceded frozen confirmation.

Predictors use valid native sensor readings in the preceding 30 minutes, with a latest-reading fallback limited to two hours. Source quality flags and the Cole-fit R² threshold of 0.9 are respected. Missingness is preserved. Imputation, scaling, missingness indicators and flexible-model settings were learned on development data only. Author-aligned duplicates are not treated as additional experiments.

## 3. Tested equation and mechanistic hypothesis

Let *P* be permittivity and Δε the dielectric increment, both represented in pF/cm, and let *f*<sub>c</sub> denote the characteristic frequency. The hypothesis used a frequency-adjusted spectral feature:

$$
S=\Delta\varepsilon\left(\dfrac{f_c}{1\,\mathrm{MHz}}\right)^4.
$$

This unit-normalized expression has the same numerical values as `deltaeps_fc4` when frequency is entered in MHz. Fixed development imputation and standardization produce dimensionless features *z* for *P*, *S* and their binary missingness indicators *m*. The selected equation is:

$$
\eta=4.26734+3.81514z_P-0.484008z_S-0.854704z_{m_P}+0.489791z_{m_S},
$$

$$
\widehat N=10^6\max(0,\eta)\;\mathrm{cells\,mL}^{-1}.
$$

The campaign hypothesized that frequency dependence could compensate for size-related changes in dielectric response under restrictive polarization assumptions. That is a testable motivation, not a measured decomposition of cell size, viability or membrane properties. All imputation medians, means, scales and full-precision coefficients are in `rules.json`.

<!-- pagebreak -->

## 4. Findings and predictive performance

**The spectral correction improves the simple calibration consistently, but only modestly.** It reduces experiment-mean RMSE from 1.72548 to 1.63107 million cells/mL, a 5.47% gain, and improves all three reserved pairs. This falls short of the frozen 10% practical-improvement threshold.

| Frozen model | Mean experiment RMSE (million cells/mL) |
|---|---|
| Spectral correction, selected before confirmation | 1.63107 |
| Linear permittivity comparator | 1.72548 |
| Spectral-availability control | 1.65850 |
| Flexible radial-basis-function comparator | 1.33835 |

The primary metric takes the square root within each experiment, then weights the three experiments equally:

$$
E_{\mathrm{RMSE}}=\dfrac{1}{3}\sum_{g=1}^{3}\sqrt{\dfrac{1}{n_g}\sum_{i=1}^{n_g}(\widehat N_{gi}-N_{gi})^2}.
$$

This is not pooled RMSE. The selected model's individual experiment RMSEs are 1.28788, 1.76149 and 1.84385 million cells/mL for EXP005, EXP009 and EXP012. These are prediction errors, not a percentage of correctly identified cells.

**Sensor availability and flexible response modeling limit the proposed mechanism.** An availability-only control uses whether the spectral feature is available, rather than its magnitude, and already reaches 1.65850. The spectral model improves this by only 1.65%. The flexible comparator performs better still. The negative fitted spectral coefficient is inconsistent with reading the correction as a straightforward positive viable-cell contribution.

## 5. Practical value and limits

The study provides a reproducible soft-sensor comparison under causal information access, including realistic missingness and source quality flags. It shows that a sensor's availability can carry predictive information that must be controlled before its signal is assigned a biological mechanism. This distinction matters when judging whether an additional sensing modality is worth using.

Potential uses include culture monitoring and less frequent offline sampling; control performance, yield, assay replacement and savings were not measured. Three pairs, including only one reserved fed-batch pair, do not establish transfer to another cell line, plant or sensor. No independent cell-size or membrane-property measurement identifies the hypothesized correction.

Individual pair errors, mode and sensor quality should accompany the aggregate. Three pairs do not justify a precise population confidence interval. Missingness may reflect sensor or process state rather than a cellular mechanism.

## 6. Evidence and use

Reproduction: `python run.py` replays the four predictors with fixed transforms. `data/observations.csv.gz` links each response to the source workbook, sheet and cell and retains causal sensor timestamps. Coefficients and the flexible model's stored parameters are in `rules.json`.

Evaluation: `evaluator/README.md` specifies the VCD target, experiment-pair grouping, matched baseline comparisons, prediction replay and scientific review. New features require separately reviewed causal preparation.

Status: no new physical VCD law was admitted. All confirmation responses are exposed; future revisions require fresh experiment pairs for new confirmation. This introduction changes neither the data nor the models.

Source: Uhlendorff and colleagues, [CHO cultivation dataset](https://zenodo.org/records/20829178), OWL University, 2026, DOI 10.5281/zenodo.20829178. Native and aligned source representations remain distinguished in the analysis.
