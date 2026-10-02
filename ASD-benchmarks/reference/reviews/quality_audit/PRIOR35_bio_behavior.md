# Scientific quality audit: nine existing portfolios

This is an evidence and contract audit, not a new discovery campaign. Historical files and scores remain unchanged. All listed outcomes are exposed; task versions and cohorts are kept separate. Case74 was developed by this reviewer, so its audit is not independent adjudication.

## P100-066

A real-gas excess-uptake formulation gives a small, scoped retrospective improvement; it does not identify pore volume or establish a new adsorption law.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-066.continuation.v1 | reference: 0.20145998 | sips: 0.20517658 | mae (wt.%), P100-066.continuation.v1.cohort-1 |
| P100-066.original.v1 | reference: 0.54645774 | baseline_domain: 0.63915502 | mae (wt.%), P100-066.original.v1.cohort-1 |

**Scope and calibration.**
- One held-out EG5 composition, 58 points, is one material unit rather than 58 replications.
- Effective affinity temperature parameters and fitted accessible volume are not independently measured enthalpies or pore volume.
- Ideal-excess MAE 0.20810 wt.% is the relevant mechanistic comparison with reference 0.20146; the earlier 0.54646 reference is a weaker historical model.

**Claim quality.**
- Keep source basis, absolute versus excess uptake, and pressure/fugacity conventions explicit.
- 77 K interior optimum does not justify claiming interior optima at 160/273 K, whose maxima reach the sampled boundary.

**Next improvements.**
- Validate on fresh compositions with independently measured pore volumes and matched adsorption/desorption uncertainty.
- Report real-gas versus ideal-excess incremental benefit and signed bias, not only historical-reference gain.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-067

Strictly upstream ballistic transit is a strong control; the selected orientation extension fails, providing useful negative evidence and a causal-input audit.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-067.original.v1 | orientation: 0.36604103 | ballistic: 0.11741798 | log_transit (absolute log ratio), P100-067.original.v1.cohort-1 |
| P100-067.round2.v1 | current/cycle-001: 0.46711668 | previous/results-v2/rbf: 0.3648877 | log_transit (absolute log ratio), P100-067.round2.v1.development-oof |

**Scope and calibration.**
- Configuration→particle category→trajectory weighting is required.
- Only three original confirmation configurations; thickness and fluid filename inconsistencies prevent claims dependent on those quantities.
- Recomputing entry velocity from interpolated points across the entry boundary would introduce future information.

**Claim quality.**
- Original selected orientation absolute-log error 0.36604 is worse than ballistic 0.11742 on the same groups.
- Later development OOF and original confirmation are separate cohorts and cannot be pooled.

**Next improvements.**
- Preserve strict native upstream windows and quantify velocity uncertainty from prefix data alone.
- Obtain fresh rheological configurations with unambiguous particle geometry and orthogonal rheometry before proposing drag mechanisms.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-069

Two thermal memory scales improve average error relative to one speed-driven state, but cooldown and high-speed failures and weak identifiability prevent a robust universal observer claim.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-069.continuation.v1 | reference: 1.2211224 | temperature_power: 0.73269941 | mae (degree C), P100-069.continuation.v1.cohort-1 |
| P100-069.original.v1 | reference: 1.4000206 | baseline_domain: 4.0261159 | mae (degree C), P100-069.original.v1.cohort-1 |

**Scope and calibration.**
- One gearbox, five identification runs, eight validation runs; startup lubricant temperature is permitted calibration.
- Housing/speed inputs are causal previous-sample values; only the first sample in each fixed bin is retained.
- Slow time constant reaches 6400 s grid boundary; constant-speed training cannot separate heat generation and slow storage reliably.

**Claim quality.**
- Reference 1.22112 C improves on single-speed 1.40002, but diagnostic temperature-power model is 0.73270 C and was not development-selected.
- Cooldown error worsens from 0.42443 to 1.70841 C; average improvement alone is not industrial readiness.

**Next improvements.**
- Use fresh variable-load and cooldown protocols, measure torque independently, and validate across gearboxes.
- Specify application-derived maximum bias/temperature-error tolerances before validation; compare source observer under identical calibration.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-071

Causal inline sensing supports a bounded VCD predictor, while availability controls and stronger flexible predictors undermine a specific cell-size mechanism.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-071.original.v1 | spectral: 1.6310723 | flexible: 1.3383499 | rmse (million cells/mL), P100-071.original.v1.cohort-1 |
| P100-071.round2.v1 | current/cycle-001: 2.0225898 | previous/adaptive-003/results/linear_magnitude: 1.7936504 | rmse (million cells/mL), P100-071.round2.v1.development-oof |

**Scope and calibration.**
- Experiment pairs are independent units; both reactors and aligned/original representations remain linked.
- Offline VCD and SEM are responses, never online inputs; imputation, scaling and missingness are training-only.
- Three original confirmation pairs with only one fed-batch pair provide limited transfer evidence.

**Claim quality.**
- Spectral RMSE 1.63107 versus linear-permittivity 1.72548 is only 5.47%; availability 1.65850 and flexible 1.33835 narrow or reverse the claim.
- Original and round2 development OOF tasks have different information budgets/cohorts and require separate summaries.

**Next improvements.**
- Add independent cell-size/viability measurements and matched sensor-availability ablations.
- Confirm on fresh paired fed-batch runs, prespecifying coverage and sensor-quality failure handling.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-072

A bounded early-assay qPCR forecast and a separate HPLC residual-sugar task offer useful predictive references; neither identifies strain fitness reversal or nutrient limitation.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-072.original.v1 | reference: 6.4381285 | baseline_persistence: 7.3735889 | mae (percentage points), P100-072.original.v1.cohort-1 |
| P100-072.round2.v1 | current/cycle-001: 14.558594 | current/baseline-hgb: 14.56286 | mae (g/L), P100-072.round2.v1.development-oof |

**Scope and calibration.**
- Whole strain is the group; biological replicates and times stay linked.
- Original later percentages had partial schema-audit exposure; future scoring is retrospective.
- HPLC sugar g/L and qPCR population percentage are distinct measured endpoints.

**Claim quality.**
- Original reference 6.43813 percentage points beats persistence 7.37359 overall but not for D245.
- Round2 registered current/cycle-001 is 14.55859 g/L; retrospective cycle-003 is 13.37034 and must not silently replace it.
- Round2 timing_contract and calibration incorrectly retain original qPCR/log-odds text despite sugar target and predictors.

**Next improvements.**
- Correct the round2 task contract to define S=G+F in g/L, early 22/72 h HPLC assay calibration, future time and coculture availability, grouping and exact assay anchors; preserve task identity and record documentation correction.
- Validate new strains and independently measure nutrient depletion before mechanistic claims.

**Blocking defects.**
- P100-072.round2.v1 contains scientifically incompatible timing/calibration prose; correct before accepting new submissions under that task.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-073

Curvature-conditioned saturation is a useful compact gas-volume predictor, but it does not beat the strongest nested kernel and does not establish methane mitigation.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-073.original.v1 | curvature_saturation: 7.5014541 | flexible_nested: 7.2426456 | rmse (mL), P100-073.original.v1.cohort-1 |
| P100-073.round2.v1 | current/cycle-001: 29.861607 | previous/baselines/kernel_nested: 7.6153703 | rmse (mL), P100-073.round2.v1.development-oof |

**Scope and calibration.**
- Whole run is independent; flask-level repeated observations are linked.
- Each flask supplies G4 and G8 calibration; targets are author-converted, blank-corrected gas volumes.
- Only three original final runs; in vitro gas is not in vivo methane or animal performance.

**Claim quality.**
- Reference run-RMSE 7.50145 mL improves on first order 8.12974 and dual pool 7.93014 but loses to nested kernel 7.24265.
- Round2 fractional-increment reference 29.86161 mL loses to kernel 7.61537 in development OOF; retain the failure.

**Next improvements.**
- Use fresh independent inoculum/run and diet conditions, with identical prefix calibration for flexible controls.
- Add methane-specific and substrate-depletion measurements for any mitigation or kinetic-pool claim.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-074

The assay supports a reproducible negative result: the development-selected curvature forecast fails against a simple saturation control on held-out dose curves.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-074.original.v1 | reference: 130.23334 | baseline_mm: 82.728979 | mae (source fluorescence units), P100-074.original.v1.cohort-1 |

**Scope and calibration.**
- Nine dose curves are one assay, not biological replicates.
- Only 3/4.5/6 min own-curve calibration is allowed; no future response enters prediction.
- Akt1 copied-time-column defect is excluded with source evidence, not silently repaired.

**Claim quality.**
- Reference MAE 130.23334 fluorescence units is worse than saturation 82.72898 and flexible 111.21386.
- An unsupported positive mechanism and a supported account of its failure must remain distinct finding dispositions.

**Next improvements.**
- Obtain independent biological assays and orthogonal phosphorylation/optical controls before dose-response mechanism claims.
- Retain this case as a falsification/calibration benchmark, without promoting a final-score winner as a fresh discovery.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-078

The cross-laboratory reference is reproducible, but a nearly constant 24-hour endpoint and informative early mortality prevent identification of a growth-capacity mechanism.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-078.continuation.v1 | reference: 0.51560314 | burden_clock: 0.43433076 | mae (log10 CFU / total lung), P100-078.continuation.v1.cohort-1 |
| P100-078.original.v1 | reference: 0.51560314 | baseline_rbf: 0.52773115 | mae (log10 CFU / total lung), P100-078.original.v1.cohort-1 |

**Scope and calibration.**
- Laboratory is the transfer unit; GSK has only 15 eligible exposed 24-hour observations.
- Time-zero calibration is a separate-animal cohort; it is not paired within-animal baseline.
- Early humane endpoints and censored observations are excluded explicitly, producing selection limits.

**Claim quality.**
- Capacity reference 0.51560 log10 CFU loses to burden-clock 0.43433 and clock 0.44677.
- At 24 h the fitted reference is approximately 8.87256+0.01923 L0: almost a constant endpoint, not evidence for identified kinetics.

**Next improvements.**
- Create a separately contracted interval-censored/early-endpoint task if authoritative censoring/time metadata permit it.
- Seek fresh laboratories and early time courses; never impute early-death values as 24-hour measurements.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.

## P100-082

Temperature-response reproduction gives small calibrated-site forecasting gains; optimizer repair and wetting-history benefits remain bounded numerical extensions.

| Task | Reference | Strongest listed control | Metric / cohort |
|---|---:|---:|---|
| P100-082.original.v1 | lloyd_taylor: 0.28747418 | temperature_moisture: 0.2876755 | rmse (g CO2 m^-2 h^-1), P100-082.original.v1.cohort-1 |
| P100-082.round2.v1 | current/cycle-001: 0.23704802 | previous/baselines/old_temperature_moisture: 0.24089518 | rmse (g CO2 m^-2 h^-1), P100-082.round2.v1.development-oof |

**Scope and calibration.**
- Future dates at already calibrated sites, not unseen-site prediction; same-date temperature/moisture are supplied covariates.
- Keep date/context linkage and negative finite flux; no row-level population confidence.
- 96 context amplitudes and related trench/site observations limit independent geographical inference.

**Claim quality.**
- Original Lloyd–Taylor RMSE 0.28747 nearly ties temperature-moisture 0.28768; uncertainty should not overstate a 0.00020 gain.
- Round2 0.23705 versus prior temperature-moisture 0.24090 is development OOF, not repeated fresh confirmation.
- Repairing the thermal optimizer and reproducing known wetting effects is not a new physical law.

**Next improvements.**
- Validate on fresh date blocks and new sites under an explicit calibration budget.
- Use independently observed wetting interventions and measurement uncertainty to separate pulse mechanism from temperature fitting.

**Blocking defects.**
- None identified in this targeted review; this is not a guarantee of universal validity.

Exact inspected paths and hashes are in the accompanying JSON.
