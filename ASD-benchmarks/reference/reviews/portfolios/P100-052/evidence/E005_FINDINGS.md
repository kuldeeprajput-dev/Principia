# Wind wake: calibrated shape, unsupported actuation law

## Scenario and practical question

ABL TypeII lidar-derived mean-velocity grids describe two wind-tunnel turbines under greedy control and three active Strouhal settings. Development retains Greedy,St 0.30,St 0.40; exposed diagnostics retainSt 0.25. The 21×21 cells are interpolated and correlated. The target is streamwise velocity in m/s, not power.

This **new calibrated task** additionally permits independently measured no-turbine velocity at the same grid. WT 2 suffixes 2 D/4 D are relative to turbine 2: global planes are 7 D/9 D. Empty 2 D/5 D grids linearly interpolate the first-turbine 4 D background. This correction and calibration are declared, hash-bound and equally available to every new comparator. They are not fresh experimental validation.

## Compact equation

Let x,y,z be rotor-diameter-normalized local geometry, I 2 identify turbine 2 and u_empty be the supplied empty-flow calibration. Define sigma_y=0.35+kx and sigma_z=ell sigma_y.

$$
\widehat u=u_{\mathrm{empty}}-\frac{A+BI_2}{(1+kx)^2}\exp\!\left[-\frac{1}{2}\left(\left(\frac{y}{\sigma_y}\right)^4+\left(\frac{z}{\sigma_z}\right)^4\right)\right].
$$

Frozen values are A=2.968978 m/s, B=0.044251 m/s, k=0.03, ell=1.4. This established flat-core/super-Gaussian family describes a calibrated wake shape, not a newly identified turbulence or momentum closure. No actuation coefficient was selected.

## Findings and falsification

1. **Scoped shape candidate:** the quartic elliptical profile has development MAE 0.268655 versus 0.276592 for the matched background-aware Gaussian, and exposed 0.267234 versus 0.273307 m/s. This is a small 2.2–2.9% descriptive improvement, not the earlier 49% advantage over a weaker omitted-shear control.
2. **Calibration importance:** replacing the independent empty-flow field with 7 m/s, without refitting, worsens development MAE to 0.722592 m/s. Much apparent field-model performance depends on background information rather than actuation physics.
3. **Unsupported frequency law:** matched amplitude, spreading and frequency-gradient models do not improve whole-control development transfer. A later anisotropic actuation candidate has exposed 0.232071 m/s but was worse in development and is not promoted after inspection.
4. **Physically informative source reproduction:** in both development active settings, rotor-disk mean contrasts against Greedy are negative at first-turbine 2 D(−0.111/−0.147 m/s) and positive at 4 D(+0.175/+0.122 m/s) and 5 D(+0.166/+0.108 m/s). Whole-plane mean contrasts remain close to zero(−0.029 to+0.006 m/s). This separates redistribution/recovery within the rotor aperture from a general flow increase. These signs reproduce the source study's wake-recovery explanation; they do not establish a new frequency law or turbine-power gain.

## Value, limitations and next evidence

The calibrated profile is a readable field-reconstruction baseline, while matched contrasts prevent background fit from being mislabeled control discovery. Only one installation, two development actuation frequencies and one greedy campaign are available; cells are not independent repetitions. The separate power summary and derived rotor-energy identities cannot independently prove a new benefit. Reserve new inflow/turbulence/actuation repetitions and rotor-level measured power before claiming control transfer or energy impact. Source interpolation/single-Doppler uncertainty remains relevant.

## Source and executable evidence

[Author data](https://zenodo.org/records/15356141); [original experimental paper](https://wes.copernicus.org/articles/10/2257/2025/). Exact coefficients and input calibration are in rules.json/data; matched contrasts are in ../SECONDARY_AUDIT.json. Run `python run.py`; use the new background-calibrated evaluator protocol, not the historical lower-information task.

## Experimental and evaluation contract

All native assets and original final packages remain unchanged. Source hashes and prepared inputs were frozen before fitting. Training uses only the original development groups; leave-one-complete-group-out predictions determine the selection. Least-squares coefficients use equal-group weighting, while tuning/selection uses equal-group MAE. Candidate grids are training-only inside each outer fold. The preselected default is the least complex model within 1% of the lowest development MAE, including strong controls. It is **supergaussian**.

Only after candidate and stopping freeze were all original confirmation groups replayed. They were already exposed in the previous campaign: every score below is a **retrospective diagnostic, not fresh confirmation**. All candidates remain visible, including those whose diagnostic error is lower than the selected default. They are not promoted afterward. Error units are m/s; thousands of correlated rows do not create thousands of independent experiments. No population confidence, new-law or deployed-impact claim is admitted.

## Whole-group numerical evidence

| Model/test | Development OOF MAE | Exposed diagnostic MAE | Fitted constants/clocks |
|---|---:|---:|---:|
| background_gaussian | 0.276592 | 0.273307 | 3 |
| elliptical | 0.276592 | 0.273307 | 4 |
| act_amplitude | 0.307363 | 0.273157 | 6 |
| act_width | 0.312630 | 0.279610 | 7 |
| act_quadratic | 0.307715 | 0.272116 | 8 |
| anisotropic_act | 0.276551 | 0.232071 | 8 |
| supergaussian | 0.268655 | 0.267234 | 4 |
| ridge_spatial | 0.404321 | 0.404468 | 61 |

The prior frozen reference has diagnostic MAE **0.326260**. For cases 52 and 59 it lacks the newly declared calibration/history, so that comparison is an information-contract change, not a matched claim of algorithmic superiority. The new controls have identical access to the new permitted inputs. Inspect evidence/by_group.csv for bias, RMSE, p 95 and adverse groups.

## Evaluator and scope

The standalone evaluator supports explicit abstention, matched covered-cohort baselines, intervals, code replay and separate scientific review. Prediction quality does not automatically admit novelty. Future agents must declare inputs/calibration and obtain new experimental groups for fresh confirmation. All point-reference intervals here are absent; error percentiles are descriptive, not calibrated confidence intervals.
