# P100-069: Replication Data for: "Lubricant Temperature Observer for Gearboxes in Industrial Robots"

> Principia-100 | Standardized portfolio | 1 October 2026

## Scenario and evaluation contract

Domain: Robotics thermodynamics. The current default task predicts Lubricant temperature in degree C. Independent unit: whole thermal experiment/run. Its packaged cohort contains 16,568 assigned rows in 8 groups.

**All supplied outcomes are now exposed.** Historical reserved evaluations remain part of the evidence record; future scores are retrospective. No newly established fundamental law or measured deployment impact is admitted by this packaging.

## Current portfolio findings

**Validated extension:** A causal housing/speed observer is a useful calibrated reference within one gearbox, with long-duration failures.

Limit: Worst original run 2.728 C; no new gearbox/sensorless claim. Source already describes an observer.

**Retrospective extension:** Two memory clocks improve mean and long-duration prediction but substantially worsen cooldown; the slow physical mechanism is unidentifiable.

Limit: Only 5/8 runs improve; cooldown bias+1.616079 C. Slowtau 6400 s hitsgrid limit and varies 1600/6400 acrossfolds. Diagnostic-better temperature-power .732699 was worse in development and isnot promoted.

## Versioned tasks

| Task family | Target and information | Source scope |
|---|---|---|
| original | Lubricant temperature (degree C) | original corpus |
| continuation | Lubricant temperature (degree C) | original corpus |

Different targets, calibration budgets and cohorts have different task IDs. Their raw error values cannot be pooled into a scenario ranking. Exact equations, coefficients, permitted variables, timing, groups and per-model results are bound in the task packages.

Evaluation: the shared CLI provides numerical scoring, explicit coverage and abstention, uncertainty and event diagnostics. Agent review separately assesses scientific support; no aggregate discovery score is produced.

<!-- pagebreak -->

## Detailed reference note: Gearbox temperature: useful slow memory, failed identification

## Scenario and practical question

The source contains five identification trajectories and eight validation trajectories from one instrumented industrial-robot gearbox. Housing, lubricant and environmental temperatures, angular speed and friction torque were recorded. We estimate lubricant temperature in °C from current/past external sensor and motion history, permitting only the first lubricant measurement as initialization. First native samples in each 5 s bin are retained; startup calibration is not scored. The development set has 1796 rows; the diagnostic has 16560 scored rows in 8 whole runs. This is a calibrated observer, not a new-gearbox or sensorless predictor.

## Compact equation and interpretation

For previous-sample input f, define H_tau as housing forcing initialized at the measured lubricant temperature and S_tau as absolute-speed forcing initialized at zero. For delta t>0,

$$
H_\tau(t_i)=e^{-\Delta t/\tau}H_\tau(t_{i-1})+(1-e^{-\Delta t/\tau})T_H(t_{i-1}),
$$

$$
S_\tau(t_i)=e^{-\Delta t/\tau}S_\tau(t_{i-1})+(1-e^{-\Delta t/\tau})|\omega(t_{i-1})|.
$$

$$
\widehat T_L=(1-c)H_{\tau_f}+cH_{\tau_s}+\gamma_fS_{\tau_f}+\gamma_sS_{\tau_s}.
$$

The frozen values are tau_f=200 s, tau_s=6400 s, c=0.416930, gamma_f=8.615867 K/(rad/s), gamma_s=28.276798 K/(rad/s). Each mode is stable and the housing weights sum to one. This is a phenomenological parallel-memory observer: its gains are not identified heat capacities, convection coefficients or causal heating pathways.

## Findings, counterexamples and admission

1. **Retrospective predictive candidate:** slow memory reduces development MAE 0.638738→0.346777 °C against the reidentified one-mode model, and exposed equal-run MAE 1.400021→1.221122 °C. Both long-term run errors improve,2.582778→1.160053 and 2.727926→1.471979 °C. Mean long-term underprediction is substantially reduced.
2. **Falsified robust upgrade:** only 5/8 diagnostic runs improve. Cooldown MAE deteriorates 0.424427→1.708414 °C, with +1.616079 °C bias. The highest-speed heat-up also worsens 1.745870→2.079139 °C. No unconditional replacement or thermal-protection claim follows.
3. **Unidentified slow mechanism:** the 6400 s slow clock reaches the grid boundary; outer fits alternate 1600/6400 s, while slow gain changes roughly 9.3–31.5 K/(rad/s). Five constant-speed trajectories underexcite the competing states. The clock is not admitted as a physical law.
4. **Preserved competing explanation:** temperature-dependent friction-power gain has lower exposed error 0.732699 °C, but development 0.700478 °C did not support selection. It is retained without promotion. Strong multiscale ridge history achieves 0.411038 development but 3.579450 exposed, emphasizing out-of-duration/regime failure.

The source authors already describe a two-state model and observer, reporting 1.3 K validation MAE under their protocol. The released archive provides reading/plotting scripts, not the exact observer coefficients or implementation; publisher access did not yield the full method. Our housing-innovation tests are **two-state-inspired**, not matched author reproduction. No superiority to that observer is claimed.

## Value, limits and next discriminating evidence

The new evidence identifies where motion-memory can aid long-duration monitoring and where it fails during cooling. Initial lubricant calibration and external housing sensing remain required. The model can be benchmarked, but an operational decision needs independently specified temperature limits, threshold-delay/miss rates and new tests. Obtain fresh cooldown/variable-load trajectories, jointly exciting speed and torque, and a matched author observer before promoting any model. New gearboxes are needed for unit transfer. No industrial savings or new thermodynamic law has been demonstrated.

## Source and reproducibility

[Author dataset](https://doi.org/10.18419/DARUS-5015); [author publication description](https://www.isw.uni-stuttgart.de/publikationen/?a=38484793430882); [paper DOI](https://doi.org/10.1109/IECON58223.2025.11221072). Exact states are in rules.json, numerical anchors in data/observations.csv.gz and full development failures in ../cycles/. Run `python run.py`; evaluator use is documented in README.md.

## Experimental and evaluation contract

All native assets and original final packages remain unchanged. Source hashes and prepared inputs were frozen before fitting. Training uses only the original development groups; leave-one-complete-group-out predictions determine the selection. Least-squares coefficients use equal-group weighting, while tuning/selection uses equal-group MAE. Candidate grids are training-only inside each outer fold. The preselected default is the least complex model within 1% of the lowest development MAE, including strong controls. It is **double_speed**.

Only after candidate and stopping freeze were all original confirmation groups replayed. They were already exposed in the previous campaign: every score below is a **retrospective diagnostic, not fresh confirmation**. All candidates remain visible, including those whose diagnostic error is lower than the selected default. They are not promoted afterward. Error units are degree C; thousands of correlated rows do not create thousands of independent experiments. No population confidence, new-law or deployed-impact claim is admitted.

## Whole-group numerical evidence

| Model/test | Development OOF MAE | Exposed diagnostic MAE | Fitted constants/clocks |
|---|---:|---:|---:|
| housing | 8.534959 | 4.026116 | 0 |
| single_speed | 0.638738 | 1.400021 | 2 |
| single_power | 0.963506 | 1.039525 | 2 |
| double_speed | 0.346777 | 1.221122 | 5 |
| innovation_power | 0.963506 | 1.039525 | 3 |
| innovation_speed | 0.638738 | 1.400021 | 3 |
| variable_tau | 0.829203 | 1.100160 | 3 |
| temperature_power | 0.700478 | 0.732699 | 3 |
| ridge_history | 0.411038 | 3.579450 | 32 |

The prior frozen reference has diagnostic MAE **1.400021**. The new controls have identical access to the new permitted inputs. Inspect evidence/by_group.csv for bias, RMSE, p 95 and adverse groups.

## Evaluator and scope

The standalone evaluator supports explicit abstention, matched covered-cohort baselines, intervals, code replay and separate scientific review. Prediction quality does not automatically admit novelty. Future agents must declare inputs/calibration and obtain new experimental groups for fresh confirmation. All point-reference intervals here are absent; error percentiles are descriptive, not calibrated confidence intervals.
