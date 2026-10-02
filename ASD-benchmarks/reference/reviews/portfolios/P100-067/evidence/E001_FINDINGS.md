# Microplastic transit through a fluid interface
> P100-067 | Scenario and findings | September 2026 reference results

The practical question is whether upstream particle motion predicts passage time through a visible rheological interface. In the reserved experiments, the elementary constant-speed transit approximation outperforms the proposed orientation correction. This is a useful scoped reproduction and a negative mechanistic finding.

## 1. Scenario and available measurements

The Mrokowska, Dzień and Krztoń-Maziopa dataset provides particle trajectories and orientation, particle descriptors, fluid rheology, density and refractive-index profiles across nine fluid configurations. The configurations belong to three numbered families. Multiple particle categories, including disks, rods and a sphere, allow geometry-dependent hypotheses to be tested alongside simpler transport descriptions.

The pilot's response is complete transit time across the visible interface, in seconds, rather than a full predicted trajectory. Interface width *h* is supplied by the recorded interface bounds. Upstream speed and orientation are obtained from observations strictly before entry. Source members, density-profile members and observation cutoffs remain attached to each response.

## 2. Experimental method

A fixed metadata-based allocation reserved one complete configuration per family: 1.1, 2.1 and 3.1. The remaining six configurations supported development. Five substantive attempts tested buoyancy, speed-gradient persistence, orientation-dependent drag, spatial adaptation and orientation fluctuations. Selection used complete development configurations, with all candidates and controls frozen before confirmation.

The reserved cohort contains 76 trajectories: 28, 23 and 25 in the three configurations. Linked representations are not independent replicates. Earlier analyses that interpolated predictor information across interface entry were invalidated; the retained evidence uses strict native upstream observations. Ambiguous thickness and fluid-filename metadata are not used to support thickness-dependent or normal-stress claims.

## 3. Equations and the proposed mechanism

The elementary transport comparator assumes that upstream speed persists over the interface width:

$$
T_0=\dfrac{h}{v_{\mathrm{up}}}.
$$

Here *h* is in metres and upstream speed is in m/s, giving *T* in seconds. The upstream speed is measured in a separate observation window, not calculated from the target transit, so this comparison is not an accounting identity.

For the tested orientation extension, define *a* from upstream orientation angle θ and disk/rod indicators *I*:

$$
a=\dfrac{1+\langle\cos(2\theta)\rangle}{2},\qquad \widehat T=T_0\exp(\eta).
$$

$$
\eta=b_0+b_v\ln\!\left(\dfrac{v_{\mathrm{up}}}{0.01\,\mathrm{m\,s}^{-1}}\right)+b_D I_D a+b_R I_R a.
$$

The dimensionless coefficients are (-0.371975, 0.211069, 0.350457, 1.051199), in the displayed order. The correction tests whether projected orientation acts as a transferable drag-state indicator. The stored orientation variable is mean cos(2θ), not mean cos²θ; the transformation above gives mean cos²θ for the same observations.

<!-- pagebreak -->

## 4. Findings and predictive performance

**The elementary transit predictor wins all three reserved configurations.** It has mean absolute log error 0.117418 and balanced physical MAE 0.047682 s. The selected orientation extension reaches 0.366041 and 0.230554 s, respectively. Thus, additional mechanistic-looking terms do not improve this transfer test.

| Frozen model | Absolute log error | Balanced MAE (s) |
|---|---|---|
| Orientation extension, selected before confirmation | 0.366041 | 0.230554 |
| Constant upstream-speed comparator | 0.117418 | 0.047682 |
| Particle/family categorical comparator | 0.359262 | 0.115559 |
| Development mean-orientation control | 0.266464 | 0.104537 |

For configuration *g*, particle category *p* and trajectory *i*, define absolute log error ℓ. Let *K*<sub>g</sub> be the number of observed particle categories and *n*<sub>gp</sub> their trajectory counts. The primary metric is:

$$
\ell_{gpi}=|\ln(\widehat T_{gpi}/T_{gpi})|,\qquad E_{\log}=\dfrac{1}{3}\sum_{g=1}^{3}\dfrac{1}{K_g}\sum_{p=1}^{K_g}\dfrac{1}{n_{gp}}\sum_{i=1}^{n_{gp}}\ell_{gpi}.
$$

Particle categories receive equal weight within each configuration; configurations then receive equal weight. Physical MAE uses the same nesting. Log error is dimensionless, not a percentage accuracy. For the simple comparator, configuration-specific physical MAEs are 0.0260, 0.0241 and 0.0929 s, making the weaker transfer to configuration 3.1 visible.

**Individual upstream orientation is not established as the transferable mechanism.** The fitted orientation model also loses to its categorical comparator and to a control that substitutes development-family mean orientation. Together with the preserved development controls, this undermines the interpretation that individual orientation supplies robust predictive drag information in this experiment.

## 5. Practical value and limits

For a process with known interface bounds and observable upstream motion, the simple transit scale provides a transparent benchmark for retention-time or separation studies. The data indicate when a richer drag correction must justify itself against a parameter-free reference. Neither separator performance nor environmental residence time outside this apparatus was tested.

Constant-speed prediction succeeding here does not prove that drag is unchanged across the interface. Compensating accelerations, the observed window and limited configurations can all affect total transit time. The orientation proxy is two-dimensional; normal stresses are unmeasured. Three reserved configurations do not establish universal behavior across fluids, particle sizes or interfaces, and do not support a precise population confidence interval.

## 6. Evidence and use

Reproduction: `python run.py` replays the four models. `rules.json` gives exact coefficients and the development-only mean-orientation lookup. Native sample anchors and cutoffs are retained in `data/observations.csv.gz`; group results are in `evidence/`.

Evaluation: `evaluator/README.md` specifies positive transit predictions, exact sample alignment, nested grouping, abstention and separate scientific review. A valid alternative mechanism need not match the reference formula.

Status: the supported result is a scoped reproduction of the elementary transit approximation, not a new transport law. All confirmation targets are exposed; a revised mechanism needs fresh configurations for independent confirmation.

Source: Mrokowska, Dzień and Krztoń-Maziopa, [microplastic sinking experiments](https://data.mendeley.com/datasets/ccm9k8pjft/1), Mendeley Data v1, DOI 10.17632/ccm9k8pjft.1. Exact source assets and hashes are in `rules.json`.
