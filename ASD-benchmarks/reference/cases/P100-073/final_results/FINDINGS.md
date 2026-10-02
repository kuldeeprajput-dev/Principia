# P100-073: Dataset for publication "Impact of algae species from the Baltic Sea region on ruminal fermentation parameters and Methane Mitigation using an in vitro gas production system"

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Animal nutrition. The current default task predicts Author-converted later fermentation gas volume at native 12/24/36/48 hours in mL. Independent unit: complete DG4 incubation run within each trial; every flask and horizon stay together. Its packaged cohort contains 216 assigned rows in 3 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Unsupported or falsified:** Prefix-exact Gompertz and two-pool gas curves do not improve the strongest forecasting reference.

Limit: Slow rates hit the searched boundary; exact 4/8 hagreement is imposed and cannot validate later gas or biological pools. The nested kernel remains the selected numerical comparator.

**Unsupported or falsified:** A fractional incremental curve fails substantially and should remain a scientific negative, not a benchmark gold equation.

Limit: Every scoring block loses; nine protocol×run blocks are not nine independent experimental runs. Gas volume is not methane or in-vivo digestibility.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Author-converted later fermentation gas volume at native 12/24/36/48 hours (mL) | original corpus |
| round2 | Author-converted later fermentation gas volume at native 12/24/36/48 hours (mL) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Forecasting gas production from an early fermentation prefix
> Principia-100 · P100-073 · Frozen scientific reference, 30 September 2026

## 1. Scenario and available measurements

The Friedrich-Loeffler-Institut campaign measures in vitro rumen fermentation under three distinct algae protocols: biomass added at 4%, extracts added at 2%, and algae used as substrate. Seventeen native CSV files contain gas trajectories, fermentation endpoints, short-chain fatty acids and author legends. The forecasting task uses 196 flasks, each with hourly observations from 0 to 48 h. Gas volume is an author-converted, blank-corrected response in mL; measured pressure and endpoint dry-matter degradation are separate products.

The practical question is whether the first 8 h of an assay can predict its subsequent gas accumulation. This supports early screening and planning of longer assays within these protocols. Total gas alone does not establish methane mitigation, nutritional utility or animal performance.

## 2. Experimental method

Forecasts use only native gas volumes at 4 and 8 h, the known protocol and substrate, and the requested future horizon: 12, 24, 36 or 48 h. No interpolation is needed. Nine complete runs, containing 142 flasks and 568 future observations, support development. Leave-one-run-index-out validation keeps every flask and horizon together. Run 4 in each protocol was reserved by identifier before fitting: 54 flasks, 216 observations and three complete confirmation runs.

Seven cycles test saturation, changing hazard, early curvature, substrate heterogeneity, two pools and decaying early rate. The first-order cycle also serves as domain reproduction; six cycles introduce competing extensions. All coefficients and candidate choices were frozen before a separate confirmation process. Persistence, early linear extrapolation, empirical substrate curves and fixed/nested-tuned kernel models have the same permitted input access. Final targets are now exposed.

## 3. Tested equation and physical interpretation

The selected compact candidate conditions a finite-pool saturation response on early curvature. Let G<sub>4</sub> and G<sub>8</sub> denote observed volumes in mL, t the future time in hours, and j the protocol.

$$
\tau_i=\tau_j\exp\!\left[\gamma_j\left(\dfrac{G_4}{G_8}-0.5\right)\right]
$$

$$
\widehat G_i(t)=G_{8,i}\dfrac{1-\exp[-(t/\tau_i)^{\beta_j}]}{1-\exp[-(8/\tau_i)^{\beta_j}]}
$$

| Protocol | tau (h) | beta | gamma |
|---|---:|---:|---:|
| Biomass supplement | 9.2880 | 0.90890 | -0.98434 |
| Extract supplement | 10.4753 | 0.88701 | -0.33855 |
| Algae substrate | 23.4226 | 0.64229 | -2.30456 |

The equation matches G8 exactly and approaches a finite asymptote. Its dimensionless exponent represents a changing net fermentation hazard; beta below one implies decreasing effective hazard. The forecast is scoped to later observations, not a reconstruction of the unobserved biological mechanism or the entire early curve. Full-precision coefficients are in `rules.json`.

<!-- pagebreak -->

## 4. Findings and predictive performance

The primary metric is the arithmetic mean of RMSE over the three complete reserved runs. It weights runs equally, rather than treating every horizon as an independent experiment.

| Frozen model | Mean run RMSE (mL) |
|---|---:|
| Selected curvature/saturation candidate | 7.50145 |
| First-order saturation | 8.12974 |
| Two-pool saturation | 7.93014 |
| Empirical protocol/substrate curve | 11.18050 |
| G8 persistence | 53.60919 |
| Early linear extrapolation | 237.51363 |
| Fixed kernel comparator | 9.36295 |
| Nested-tuned kernel comparator | 7.24265 |

The compact candidate lowers RMSE by 7.73% relative to first-order saturation, winning two of three runs. It is 3.57% worse than the stronger nested kernel, so it fails the preregistered requirement to improve at least 5% over every baseline. Reserved-run errors are 12.44, 4.63 and 5.44 mL for protocols 1-3. These results support a useful interpretable reference comparison, without admitting a new industrial law.

Two complementary findings are preserved. Unsaturated extrapolation of the 4-8 h rate is unreliable at later horizons. Conversely, a two-pool model nearly matches the best development error while using G8 alone; its slow-pool time constants are poorly identified, including a 500 h boundary. Predictive agreement therefore does not establish a unique microbial or substrate-pool explanation. Algae-specific time constants and simplified tangent-rate variants provided no further development gain.

## 5. Practical value and limits

The compact equation provides an executable forecast with a small protocol-specific parameter table. It can help compare assay forecasting strategies and identify early signals worth measuring. No actual reduction in assay cost or duration was tested. Transfer is limited to repeated runs of these three protocols and familiar substrates, with a valid measured prefix; there is no evidence for new algae species, other inocula or in vivo methane emissions.

Only three final runs are available. Their shared preparation conditions and author blank corrections limit biological independence; row-level confidence intervals would be misleading. Early curvature, substrate accessibility and microbial dynamics remain confounded. Established finite-pool and time-varying-rate models have prior art. Failed hypotheses remain available as scientific evidence.

## 6. Evidence and use

`run.py` reproduces the frozen predictions and grouped metrics. `data/` contains causal inputs and separately anchored responses; `evidence/` records every comparator and run error. The accompanying evaluator assesses other declared discoveries under the same information and validation contract. `research_history/` preserves the source/units audit, split allocation, seven cycles and pre-confirmation freeze. Alternative valid equations are allowed; exact agreement with this equation is not a scientific acceptance criterion.

Source: Brunnbauer and colleagues, [dataset v1.0](https://zenodo.org/records/18335590), DOI 10.5281/zenodo.18335590; linked study DOI 10.3390/ruminants6010018. Model-family prior art: [France et al. (1993)](https://doi.org/10.1006/jtbi.1993.1109). Classification: reproducible reference comparison and preserved negative evidence; no adjudicated novelty.
