# P100-044: topology optimization and solver evidence

## Scenario and task

QOBLIB supplies 48 computational runs: three mixed-integer formulations on 16 degree-constrained network-topology instances. The source experiment uses Gurobi 11 on one stated machine, with one deterministic run per formulation and instance. The task predicts resource consumption before solving, using node count, degree limit and formulation. All failures and time-limited runs remain included.

The primary target is elapsed runtime capped at 7,200 seconds. It is observed resource consumption, not an estimate of the unobserved time required to prove optimality. The source column named CPU Runtime contains Gurobi Work Measure and must not be interpreted as seconds. Post-presolve variable counts, objectives, gaps and solution graphs are excluded from predictive inputs.

Twelve complete instances support leave-one-instance-out development. Four metadata-hash-selected instances were reserved for confirmation, with all three formulations kept together. Five substantive attempts tested Moore-bound occupancy, combinatorial growth, smooth resource saturation, formulation-specific thresholds and removal of degree. All failed to displace the established size-degree baseline in development. The reference remains that baseline; this case does not claim a newly discovered runtime law.

## Reproducible resource predictor

For node count $n$, degree limit $d$, and formulation indicators $I_f,I_l$, the reference is

$$
\widehat t=\min\{7200,\exp(z)\}\;\mathrm{s},
$$

$$
z=b_0+b_1\log(n/25)+b_2\log(d/4)+b_3I_f+b_4I_l.
$$

The quadratic formulation is the reference category. The exponential models positive growth in consumption, while clipping represents the experimental resource ceiling. The coefficients and all numerical guards are supplied at full precision in `rules.json`; the coefficient table below is for reading. This is a local resource model, not an asymptotic algorithmic-complexity theorem.

| Coefficient | Value |
|---|---:|
| $b_0$ | 6.7204589 |
| $b_1$ | 11.664625 |
| $b_2$ | -3.9376623 |
| $b_3$ | 2.8806121 |
| $b_4$ | -0.11722548 |


| Predictor | Development MAE, seconds | Confirmation MAE, seconds |
|---|---:|---:|
| Formulation-specific median | 2364.617 | 4095.026 |
| Size-degree reference | 629.721 | 980.825 |
| Nested flexible RBF control | 1614.099 | 1182.146 |
| Smooth resource transition | 759.787 | 1069.290 |
| Degree-free alternative, unselected | 1182.693 | 556.276 |

The degree-free alternative wins retrospectively despite worse development error. It is preserved, not promoted. This reversal and the four-instance confirmation scope prevent a universal claim about the benefit of degree-dependent prediction. Per-instance errors and offline formulation-selection regret are included in the compact evidence; regret is a paired replay diagnostic, not measured operational savings.

## A useful certificate audit: objective versus graph diameter

The released graph files provide an independent check of solution quality. Breadth-first search computes the actual graph diameter,

$$
D_{\mathrm{graph}}=\max_{u,v}\operatorname{dist}(u,v).
$$

All 47 available solution graphs satisfy their declared degree limits and are connected. However, two reported MIP objectives overstate the actual graph diameter:

| Instance and formulation | Reported objective | Verified graph diameter |
|---|---:|---:|
| 40 nodes, degree 6; linear Seidel | 12 | 3 |
| 40 nodes, degree 6; quadratic Seidel | 5 | 4 |

The source formulations allow the auxiliary diameter variable to remain above the graph's true diameter in unfinished solves. These differences are consistent with slack objective variables; they are not evidence that the graph files are corrupted. A source comment repeating the MIP objective is therefore not an independent diameter measurement. One failed run has no solution graph and remains explicitly missing.

The classical Moore counting bound also supplies an independent necessary condition for degree-limited diameter:

$$
n\leq1+d\sum_{i=0}^{D-1}(d-1)^i.
$$

27 released graphs attain the resulting integer lower bound. This bound is established mathematics. The contribution here is executable source verification and correct interpretation of the released outputs, not a new graph-theoretic inequality. The graph audit was performed after predictive freezing and did not modify runtime targets or selected models.

## Interpretation, limitations and use

The occupancy-only model substantially worsened development error: feasibility geometry alone did not predict search effort. Exponential search-count and smooth-threshold alternatives also failed to provide robust gains. These negative results help prevent attractive but unsupported complexity narratives.

A single machine, solver version and deterministic run per configuration cannot establish transferable runtime distributions or industrial scheduling benefits. The resource cap obscures latent solve time, and neighboring instances share substantial structure. Report all four confirmation instances; bootstrap resampling of the 12 formulation rows would exaggerate independence.

Run `python run.py` for frozen replay. The common evaluator scores alternative pre-solve equations using the exact instance groups and physical seconds. Graph certificates are a complementary diagnostic with native anchors in `evidence/graph_certificates.csv`; a new solution-quality endpoint requires its own approved task. The existing outcomes are exposed for future submissions.

Source: [pinned ZIB QOBLIB topology collection](https://github.com/ZIB-AOPT/QOBLIB/tree/2b400f43c197bb0eb9bc9802efa2b28b818ab63c/10-topology). [GraphGolf](https://research.nii.ac.jp/graphgolf/problem.html) describes the related degree/diameter problem; [Gurobi documentation](https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/model.html) distinguishes runtime and work. Complete hypotheses, failed models, coefficient sensitivity, units and hashes are retained in the research history.
