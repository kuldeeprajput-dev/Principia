# Compiler runtime: calibrated startup and work scaling

A compact positive startup-plus-work model transfers across reserved circuit families more accurately than proportional-runtime and flexible controls. The result is an empirical software-runtime relationship under a paid-in-compute Qiskit pilot calibration, not a new quantum-device law.

## Data and evaluation

The IBM Benchpress native benchmark archives provide repeated mean compilation times for circuits evaluated by several SDKs on the same reported CPU brand. Exact circuit filenames pair candidate SDK outcomes with Qiskit pilot timing and structural metadata. Twenty-four circuit families (98 candidate-SDK observations) are used for development and five complete families (37 observations) for confirmation. All circuit sizes and SDK outcomes remain linked by family. Only positive finite successful matched runs are scored; author failures remain in AUTHOR_FAILURE_AUDIT and the native archives, without assigning synthetic timeout values.

Target: **Author-benchmarked mean compilation wall time after matched Qiskit pilot**, measured as seconds. Primary error: absolute natural-log time ratio. Must execute the complete Qiskit pilot first; its runtime and resulting circuit statistics are known only afterward. Candidate SDK timing is withheld. Pilot cost is not free. This is runtime diagnostics, not pre-compilation prediction or quantum-device performance.

Circuit family after stripping numeric size suffixes; compiler observations on each family stay linked. One local CPU family; no independent hardware transfer. Whole circuit families held across allSDKs; exact same inputfilename matched. No held family candidate-runtime measurements enter fitting. Qiskit pilot is declared per-instance calibration.

## Findings and equations

**P100-031-F01 — validated_extension (partially_supported).** A positive Staq startup floor plus shared pilot-time scaling improves reserved-family runtime prediction over matched frozen controls.

rules.json models.reference: t_hat,k=A_k+B_k*x^p, SDK order Staq,Tket,BQSKIT; fixed negligible floors for Tket/BQSKIT.

Effective overhead plus growing computational work explains the observed short/long-runtime curvature within these paired software experiments.

Falsifying evidence and limits: The pilot is a measured per-circuit calibration with real computational cost. Only successful matched cases and five held families are tested; no asymptotic-complexity, cross-hardware, quantum-physics or deployed-benefit claim is established.

**P100-031-F02 — informative_falsification (supported).** Three independently estimated SDK startup floors are not identifiable from the available data.

Attempt010 estimates three floors plus three scales and one power; attempt011 fixes Tket/BQSKIT floors to exp(-60) and retains five parameters.

Full-model Jacobian rank6/7 and near-zero floors motivate an identifiability correction; reduced model rank5/5 preserves the gain.

Falsifying evidence and limits: A positive Staq floor is an empirical identifiable fit parameter, not a uniquely identified source-code operation. Alternative pipeline decompositions require new measurements.

Selected executable model: `attempt_011`. Let x be mean Qiskit pilot compilation time in seconds for the same circuit. For SDK k in [Staq,Tket,BQSKIT], t_hat,k=A_k+B_k*x^p seconds. A=[0.005339508539937091, 8.75651076269652e-27, 8.75651076269652e-27] seconds, B=[0.079343488274299, 9.604758776957347, 64.93054436976479] seconds^(1-p), and p=1.1558996610350212. Tket/BQSKIT floors are fixed at exp(-60) seconds as numerical zero. The five fitted parameters are [log(A_Staq), log(B_Staq), log(B_Tket), log(B_BQSKIT), p]=[-5.232621663965042, -2.533968898712965, 2.262258681585249, 4.173318150433576, 1.1558996610350212]. Powers apply to x measured in seconds; changing units requires the stated scale transformation.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 0.2265189 | 0.2341363 | 0.4761506 |
| constant | 1.366381 | 1.659961 | 2.871836 |
| domain | 0.4988712 | 0.4244018 | 0.6489612 |
| flexible | 0.7397175 | 1.033337 | 1.573155 |

Confirmation contains 37 scored observations in 5 groups. Individual-group scores and every attempted model remain available. Reserved-family mean absolute log ratio is 0.234136, versus 0.424402 for SDK-specific proportional pilot scaling, 1.033337 for the constrained flexible control and 1.659961 for SDK constants. The selected model has worst-family log error 0.476151 versus 0.648961 for proportional scaling. These are geometric error factors of about exp(0.234136)=1.264 on the primary aggregate, not a percentage accuracy. Five families cannot establish universal compiler complexity.

## Interpretation, limitations and use

Only device-transpilation successful matched tasks forTket/BQSKIT/Staq; no service remote latency. Missing/failed/timeouts excluded from conditional-success runtime target and retained in source audit; cannot infer success probability or realized routing speedup. Author timing environment differs in frequency/run state despite same CPU model. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

The interpretable Staq floor captures an effective fixed overhead in this release, with work increasing with pilot runtime. The full seven-parameter model initially had negligible Tket/BQSKIT floors and a rank-deficient Jacobian; removing those floors preserved development performance and restored rank five (condition number about10.28). The shared exponent and scales are calibrated empirical relationships, not asymptotic algorithmic complexity or proof of a physical startup mechanism. CPU frequencies, repetition summaries, success selection and limited SDK versions bound deployment relevance. Pilot measurement cost must be included in any scheduling utility claim.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Benchpress paper compares quantum software performance and reports compilation/task successes/failures; no new quantum physical law inferred from runtime.](https://www.nature.com/articles/s43588-025-00792-y) (checked 2026-10-02).
- [Primary benchmark implementation; exact archived results are frozen locally, not rerun against current software.](https://github.com/Qiskit/benchpress) (checked 2026-10-02).
