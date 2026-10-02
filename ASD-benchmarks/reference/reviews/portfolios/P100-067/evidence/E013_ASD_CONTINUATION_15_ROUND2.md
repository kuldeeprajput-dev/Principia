# Fifteen-scenario ASD continuation: round 2

30 September 2026. Local research edition; no publication or paid model runs.

This round completed **33 scientific tests across all fifteen scenarios**, including explicit falsifying controls, and fitted fifteen matched flexible baselines. Four scenarios produced useful retrospective candidates. Their improvements below are measured on the **same grouped development cohorts** as their predecessors. They are not new confirmation scores, percentage accuracy, or measured industrial savings.

| Scenario | Previous comparator error | Selected new error | Reduction | Group wins |
|---|---:|---:|---:|---:|
| 61: membrane permeation | 0.004109 | 0.003340 mol m⁻² s⁻¹ | 18.71% | 5/6 gas-temperature blocks |
| 72: yeast residual sugar | 14.657 | 13.464 g/L | 8.14% | 5/6 strains |
| 60: ultrasonic peak response | 0.155761 | 0.100101, normalized | 35.73% | 20/30 files |
| 82: soil respiration | 0.240895 | 0.237048 g CO₂ m⁻² h⁻¹ | 1.60% | 28/48 forward blocks |

The comparator is the strongest exact-cohort predecessor found in the retained continuation, including flexible controls. New matched HGB models also remain in the comparison. The acoustic metric divides each file's MAE by its condition's mean training voltage; its ordinary voltage MAE also improves, from **0.536629 to 0.258478 V**. The soil and biological cell-density tasks use group RMSE; the other displayed physical errors are group MAE.

**The strongest mechanistic lead is case 61.** It combines known transport relations more economically and rejects useful countermodels. Case 72 provides a simple early-assay forecast. Case 60 makes a substantial predictive improvement, but the waveform check rejects identifying its fitted frequency directly with measured resonance. Case 82 is a modest observational extension consistent with established rewetting effects.

**No new physical law or demonstrated industrial intervention impact is admitted.** All previous confirmation groups were exposed before this round. They were excluded from new fitting and selection, and their scores were not reopened. No fresh external cohort was acquired. The original final reference packages remain unchanged; these additions are research candidates and preserved negative evidence.

Numerical verification covers **48 fitted model sets and 316,635 saved out-of-fold predictions**, with a separate metric implementation and checks that prediction ignores target values and identifiers. The report is supported by [the catalog](_support/continuation_20260930b/CATALOG.csv), [selection record](_support/continuation_20260930b/SELECTION_AND_STOPPING.json), [computational review](_support/continuation_20260930b/COMPUTATIONAL_REVIEW.json) and [evaluator guide](_support/continuation_20260930b/EVALUATOR.md).

<!-- pagebreak -->

## 61. A smaller membrane transport closure

The experiment measures hydrogen flux through four calibrated membranes in H₂/N₂, H₂/Ar and H₂/He mixtures. The task predicts mixture flux from gas composition, normal feed flow, temperature, pressure, geometry and declared pure-H₂ calibration. Development comprises 120 mixture measurements in six whole gas-temperature blocks; 64 pure-gas measurements provide the same twelve calibration coefficients to the physical models. These are calibrated devices, not unseen membranes.

The selected model keeps axial hydrogen depletion and a nonlinear Stefan film. With total feed molar flow F, inlet mole fraction x₀ and cumulative permeation q,

$$
x_b(q)=\frac{F x_0-q}{F-q},\qquad \frac{dq}{dA}=J.
$$

Dimensionless pressures π are pressure divided by 1 bar. At each axial cell, surface composition and flux satisfy

$$
x_s=1-(1-x_b)\exp\!\left(\frac{J}{\kappa\pi_r}\right),\qquad J=P_m(T)\left[(\pi_r x_s)^{n_m}-\pi_p^{n_m}\right]_+.
$$

The code enforces nonnegative flux and feed/equilibrium capacity bounds. It uses the original 22.414 L/mol normal-flow convention. Permeance and pressure exponents come from the unchanged pure-gas calibration.

The improvement comes from a constrained film description: nominal diameter/length scaling, a developing axial profile, and an approximate gas factor rather than freely fitted gas labels. For gas g,

$$
G_g=\left[\frac{M_{H_2}^{-1}+M_g^{-1}}{M_{H_2}^{-1}+M_{N_2}^{-1}}\right]^{0.2}.
$$

The local film coefficient is

$$
\kappa_j=K_c\frac{d_*}{d}\left(\frac{L_*}{L}\right)^{0.6}\left(\frac{F_n}{F_*}\right)^{0.6}\left(\frac{T}{T_*}\right)^{0.3}G_g w_j.
$$

The entrance weights follow the inverse cube root of normalized axial position and have unit arithmetic mean over the 64 cell centers. Reference values are 0.01 m diameter, 0.14 m length, 5 L/min normal flow and 673.15 K. Molar masses use the same units throughout the gas ratio. The two fitted log K values are **−1.549537** for the narrower family and **−1.671062** for the wider family, under the documented 64-cell convention. Full precision, all twelve pure-gas coefficients and every fold calibration are in the model state.

This replaces **six mixture coefficients with two**, while reducing development MAE by 18.71%. All three gas-level mean improvements are positive, though one of six blocks loses. Pooling both geometry families raises error to **0.004277**; reversing the reduced-mass gas ordering raises it to **0.006200**. These controls support the usefulness of the retained structure within this experiment.

The mass factor omits collision-integral and viscosity differences; it is not full kinetic theory. The source paper already contains axial/film transport. Sparse geometry families cannot identify a universal geometry law. The 64-cell score is 0.00333994; refinement to 1,024 cells preserving the same local film field gives 0.00333728 without refitting. This numerical check supports the reported gain.

Source: [workbook-matching study](https://doi.org/10.1016/j.ijhydene.2024.05.225); [NIST diffusion reference](https://srd.nist.gov/JPCRD/jpcrd1.pdf). Evidence: [case findings](61_chemistry_membrane_permeation/research_history/continuation-20260930b/FINDINGS.md), [selected state](61_chemistry_membrane_permeation/research_history/continuation-20260930b/cycle-006/states.json), [mesh check](61_chemistry_membrane_permeation/research_history/continuation-20260930b/mesh_consistency/RESULT.json).

<!-- pagebreak -->

## 72. Early-assay clocks for residual sugar

The HPLC task forecasts glucose plus fructose from each fermentation's own 22 h and 72 h assays. Whole strains are held out, keeping monocultures, cocultures and linked replicates together. This round uses six development strains and 153 later assays. The previously exposed two-strain cohort is not rescored. This is a chemistry task, distinct from the original competition-percentage task.

For either glucose or fructose, define

$$
k_q=\max\{\log(q_{22}/q_{72}),0\},\qquad u=\frac{t-22\,\mathrm{h}}{50\,\mathrm{h}}.
$$

The selected two-parameter rule is

$$
\widehat q(t)=q_{72}\exp\!\left[-k_q\left(u^{\beta_q}-1\right)\right],\qquad \widehat S(t)=\widehat G(t)+\widehat F(t).
$$

The fitted glucose exponent is **2.039890** and the fructose exponent is **1.245706**. Concentrations are g/L and times are hours; k and β are dimensionless. All development prefixes decline, so the positive-rate clipping is inactive there. Prefix agreement is imposed and is not counted as validation.

The equation implies a changing fractional depletion rate:

$$
-\frac{d\log\widehat q}{dt}=\frac{k_q\beta_q}{50\,\mathrm{h}}u^{\beta_q-1}.
$$

It replaces the earlier abrupt constant acceleration after 72 h with a smoother effective clock. It is an interpretable compressed-exponential forecast, not a measurement of biomass growth, transporter expression or nitrogen limitation.

Mean strain MAE falls from **14.656974 to 13.464268 g/L**. Five strains improve and one worsens slightly. Removing any one strain leaves the mean improvement positive. A new matched HGB scores **14.562860 g/L**. A three-parameter context model scores 13.370341, less than 1% better, so the simpler two-clock rule is retained. A single common sugar clock scores 14.081046 and does not replace it.

The practical opportunity is a compact early-assay estimate of later residual sugar. The data do not demonstrate improved fermentation control, reduced processing time or avoided spoilage. Transfer to new media, temperatures or independently prepared strains still requires fresh experiments. Distinct glucose/fructose behavior and exponential consumption models are established prior art; no biochemical novelty is certified.

Source: [original dataset](https://zenodo.org/records/18757697), [earlier sugar-consumption modeling](https://pmc.ncbi.nlm.nih.gov/articles/PMC8160661/), [transporter study](https://pmc.ncbi.nlm.nih.gov/articles/PMC1855598/). Evidence: [case findings](72_biotechnology_yeast_competition/research_history/continuation-20260930b/FINDINGS.md), [selected state](72_biotechnology_yeast_competition/research_history/continuation-20260930b/cycle-002/states.json), [all strain effects](72_biotechnology_yeast_competition/research_history/continuation-20260930b/ROBUSTNESS.json).

<!-- pagebreak -->

## 60. Better pulse prediction, a rejected resonance interpretation

The dataset contains native voltage waveforms at two nominal transmitter frequencies, three contact/distance conditions and multiple rectangular pulse widths. This continuation holds out complete widths across all six conditions: five development widths, thirty files and ten pulses per file. Repeated pulses are not independent sensors. The task predicts post-trigger absolute peak voltage with condition calibration learned only from the other widths.

The candidate calculates the maximum of two oppositely signed, shifted edge responses:

$$
h_f(t)=e^{-t/\tau_f}\sin(2\pi r f t)\,\mathbf{1}_{t\geq0},\qquad \widehat A=g_c\max_{t\geq0}|h_f(t)-h_f(t-w)|.
$$

Here f is nominal frequency in cycles/µs, w and τ are µs, the condition gain is in volts, and r is dimensionless. The peak calculation uses analytic stationary points. It is exact within this two-edge ansatz, not an exact description of every transducer component.

The selected constant-Q constraint is

$$
\tau_f=\tau_{110}\frac{110\,\mathrm{kHz}}{f},\qquad \tau_{110}=15.939439\,\mathrm{\mu s},\qquad r=1.109909.
$$

Six condition gains remain necessary. Together these are eight fitted coefficients, as in the preceding frequency-specific model.

Normalized group MAE decreases from **0.155761 to 0.100101**; physical MAE decreases from **0.536629 to 0.258478 V**. Twenty files improve and ten worsen. All five width-level mean effects are favorable, and removing any one width preserves a mean gain. A common damping time scores 0.159458; fixing r=1 under constant Q scores 0.173374. Both controls fail to replace the selected predictor.

The mechanistic check is less favorable. A separately specified spectral analysis used all 300 development waveforms and did not refit the peak model. Only **7/15** files in the 110 kHz family and **0/15** in the 500 kHz family have a median spectral peak within 5% of the selected effective frequency. The measured spectral ranges are approximately **57–122 kHz** and **251–313 kHz**, respectively. Windowing, transfer paths and noise also influence these spectra; the evidence identifies no unique replacement mechanism.

Consequently r remains an **effective prediction parameter**. Do not label it a newly discovered resonance shift or a measured time-base error. The result may help calibrate pulse-width response within this apparatus; it does not establish unseen-sensor transfer, localization accuracy or hardware optimization impact.

Source: [TU Graz measurements](https://zenodo.org/records/17266427), [prior excitation/mounting study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11722765/). Evidence: [case findings](60_acoustics_ultrasonic_transmission/research_history/continuation-20260930b/FINDINGS.md), [selected state](60_acoustics_ultrasonic_transmission/research_history/continuation-20260930b/cycle-004/states.json), [spectral comparison](60_acoustics_ultrasonic_transmission/research_history/continuation-20260930b/waveform_falsification/selected_model_comparison.csv).

<!-- pagebreak -->

## 82. A modest directional moisture-history effect

The soil task predicts respiration at already calibrated source contexts using measured temperature and moisture. Evaluation uses three forward periods for each of sixteen source site labels, yielding 48 blocks and 20,128 scored development observations. Site labels include potentially related locations/treatments; they are not asserted to be sixteen independent experimental replications.

Let x=(T−10 °C)/(10 °C), z=(M−25)/20 with moisture M in percent, and ΔM be the change from the most recent strictly earlier site-date measurement within 30 days. Missing history gives zero change. The candidate is

$$
\widehat R=A_c\exp\!\left(bx+cz+dz^2+exz+mI_{\rm miss}+\eta\max(\Delta M/20,0)\right).
$$

Respiration R and each context amplitude have units g CO₂ m⁻² h⁻¹. The full fitted coefficients are b=0.572429, c=−0.039548, d=−0.033841, e=0.307950, m=0.086732 and **η=0.434388**. All context amplitudes are fitted within training periods; none is an unseen-site calibration. The missingness indicator refers to current moisture. The model also retains the exact temperature/moisture data conventions in its frozen code.

Mean block RMSE improves from **0.240895 to 0.237048**, a **1.60%** reduction. Twenty-eight blocks improve and twenty worsen; twelve of sixteen source-label mean effects are positive. A drying-only counterpart scores 0.240625 and its extra coefficient collapses to zero. An absolute-change control scores 0.240194. The new matched HGB scores 0.242973. The optimized drying/no-pulse control also improves slightly over the older baseline, so not all of the difference from that older baseline can be attributed to wetting history.

This is compatible with known rewetting responses, but seasonal state, substrate availability and sampling intervals remain confounded. Rainfall, microbial activation and controlled wetting were not measured as interventions. The effect is small enough to retain as an exploratory covariate rather than a universal respiration law or a carbon-management benefit.

Source: [established Birch-effect study](https://pubmed.ncbi.nlm.nih.gov/17403645/), [prior history-aware respiration modeling](https://www.pnnl.gov/publications/encoding-diel-hysteresis-and-birch-effect-dryland-soil-respiration-models-through). Evidence: [case findings](82_ecology_soil_respiration/research_history/continuation-20260930b/FINDINGS.md), [selected state](82_ecology_soil_respiration/research_history/continuation-20260930b/cycle-001/states.json), [site-label sensitivity](82_ecology_soil_respiration/research_history/continuation-20260930b/ROBUSTNESS.json).

<!-- pagebreak -->

## Complete portfolio and next use

All fifteen scenarios received a distinct new scientific test. The table counts substantive model hypotheses and explicit falsifying controls; technical repairs, baseline refits and the waveform consistency analysis are separate.

| Case | Tests | Outcome of this round |
|---|---:|---|
| 24: fatigue | 1 | Free strain exponent does not improve the established family. |
| 27: boiling | 2 | Physical slip/profile revisions fail; a stronger HGB control is useful. |
| 37: routers | 1 | Bottleneck power explanation loses to the flexible comparator. |
| 53: screw driving | 1 | Multiplicative wear transfer fails; fresh S01 acquisition remains pending. |
| 57: foam | 1 | Shear-rate correction adds negligible value; metrology limits remain. |
| 60: acoustics | 6 | Better prediction; direct resonance interpretation rejected. |
| 61: membranes | 8 | Better constrained transport closure; two calibration families still needed. |
| 67: settling | 1 | Entry-velocity blend loses to the development RBF. |
| 71: CHO | 1 | Moment-ratio sensor fusion loses to the strongest spectral control. |
| 72: yeast | 4 | A compact two-clock sugar forecast improves grouped error. |
| 73: rumen | 1 | Fractional gas-growth curve fails; total gas is not methane. |
| 82: soil | 3 | Small directional moisture-history gain, observational only. |
| 83: hives | 1 | Weather-increment model remains weaker than flexible forecasting. |
| 92: BLE | 1 | Local channel redistribution does not replace the previous model. |
| 100: latency | 1 | Parity noise-filter hypothesis loses to simple lag-two persistence. |

The root [latest-research index](LATEST_RESEARCH.md) and each case's versioned `FINDINGS.md` are the reader entry points. Equations, coefficients, fold states, predictions, unfavorable tests and per-group errors remain in research history. Original final packages are preserved; a future release must decide explicitly which retrospective candidate, if any, becomes a revised reference.

**Replay and evaluation.** The shared [evaluator guide](_support/continuation_20260930b/EVALUATOR.md) provides examples, strict submission checks, matched coverage and review records. It reports numerical performance without certifying novelty. The source-and-result preservation checks, missing/truncated/hash-mismatch tests, target-perturbation tests, independent metric computation and input timing reviews are documented in the [acceptance report](_support/continuation_20260930b/ACCEPTANCE_REPORT.md).

**Lessons to carry forward.** A good next hypothesis must distinguish explanations, not just add a coefficient. Test simple history controls; preserve all group failures; use an independent measured observable to challenge a physical interpretation; and keep a numerical discretization's physical field constant during convergence checks. Prefer simpler equations inside the declared error tolerance. For the next substantive leap, prioritize fresh membrane campaigns and independently prepared yeast experiments, with calibration and selection frozen before outcomes arrive.

The detailed [handoff](ASD_RESEARCH_HANDOFF_ROUND2.md) records these lessons and the remaining evidence requirements. This is reproducible research progress, not a claim that every scenario must yield a new law.
