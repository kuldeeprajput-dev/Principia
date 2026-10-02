# P100-043: forecasting language-model learning curves

## Scenario and question

Gemstones releases computational training trajectories for transformers with different widths and depths. This task uses 22 constant-learning-rate, non-cooldown architectures from the pinned public release. The author-merged logs already filter some problematic runs; they are not independent raw training experiments. The practical question is whether two early validation checkpoints can predict subsequent validation loss without completing every training run.

The target is natural-log perplexity, in nats per token, at native checkpoints between 20 and 100 billion training tokens. Each evaluated architecture supplies its latest checkpoints at or before 10 and 20 billion tokens. Width, depth and parameter count are known. Later losses, cooldown results and future optimization history are unavailable to the predictor. Token counts are reconstructed from integer optimizer steps, not the lexical order of JSON keys.

Seventeen complete architectures support leave-one-architecture-out development; five metadata-stratified architectures were reserved for confirmation. Run chunks and stages remain linked. Seven substantive attempts tested aspect dependence, two relaxation rates, parameter-size dependence, early-anchor attenuation, combined geometry, finite-size saturation and a symmetric geometry penalty. Selection and stopping were frozen before confirmation. Every result is now exposed for future users.

## Supported result: a calibrated size-dependent decay

Let $T_1<T_0$ be the early calibration token counts, $L_1,L_0$ their losses, and $N$ the parameter count. The selected forecast is

$$
\widehat L(T)=L_0+(L_0-L_1)R(T;\beta),
$$

$$
R(T;\beta)=\frac{(T/T_0)^{-\beta}-1}{1-(T_1/T_0)^{-\beta}},
$$

$$
\beta=\exp\!\left[-0.47112414-0.05777846\log\!\left(\frac{N}{5\times10^8}\right)\right].
$$

All logarithm arguments are dimensionless. The two fitted global coefficients were estimated using development architectures only; the early losses are explicit same-architecture calibration, not hidden fitted offsets. The equation exactly reproduces the later anchor and predicts diminishing loss reduction. The executable implementation guards loss at zero; that guard is not evidence about an asymptotic irreducible-loss floor. Full-precision coefficients are in `rules.json`.

This is a validated extension within the released training configuration. Standard power-law learning curves and architecture-dependent scaling are established prior art. A negative size coefficient here is an empirical forecast correction; it does not prove that parameter count causally controls optimization dynamics.

## Performance and counterexamples

Errors are averaged within each architecture and then equally across architectures. Native checkpoints are dependent and do not count as independent replications.

| Forecast | Development MAE | Confirmation MAE |
|---|---:|---:|
| Early-loss persistence | 0.122844 | 0.132858 |
| Shared power exponent | 0.008292 | 0.007991 |
| Nested flexible RBF control | 0.010912 | 0.010850 |
| Selected size-dependent exponent | 0.007249 | 0.005277 |
| Bounded-size alternative, unselected | 0.007617 | 0.005088 |

All errors are nats per token. The selected model reduces mean confirmation error by 34.0% relative to the shared exponent, winning on four of five architectures. It beats the flexible model in mean error but only on two of five individual architectures. The smallest held architecture, 384 by 13, favors the shared exponent. The bounded-size alternative is a retrospective winner; it does not replace the development-selected reference.

| Held architecture, width by depth | Selected MAE |
|---|---:|
| 384 by 13 | 0.010217 |
| 512 by 12 | 0.004195 |
| 1024 by 28 | 0.004139 |
| 1280 by 36 | 0.006609 |
| 1536 by 50 | 0.001224 |

## What failed and what remains uncertain

The two-rate model was almost indistinguishable from the shared power model in development, with a boundary-constrained slow exponent and a poorly conditioned fit. These data do not identify two independent relaxation mechanisms. Aspect-only and symmetric geometry alternatives also failed to improve the selected forecast. Adding geometry to size lowered the worst development-group error but worsened average error; this tradeoff remains visible.

Five confirmation architectures, one training corpus, one tokenizer and no independent seed replications cannot establish a universal scaling law. Training-only fold coefficient ranges and anchor perturbations are sensitivity diagnostics, not population confidence intervals. The forecast is limited to 20–100 billion tokens under the disclosed early calibration. It does not determine compute-optimal model size, wall-clock cost or downstream task quality.

## Use, significance and evaluation

A compact calibrated forecast could help prioritize continuation of expensive runs. The current evidence demonstrates forecast accuracy on released trajectories, not saved compute in a deployment. Numerical error, mechanism, novelty and practical impact remain separate judgments.

Run `python run.py` to verify frozen predictions and group metrics. The shared evaluator accepts alternative equations under the same input budget; agreement with this formula is unnecessary. Report group errors, coverage, calibration use and any prediction intervals. New corpora or learning-rate regimes require a separate task and fresh confirmation.

Source and prior art: [Gemstones release](https://github.com/mcleish7/gemstone-scaling-laws), pinned commit `5f420478f6057b0cbb4d13405fb10ca64675bccb`; [Gemstones paper](https://arxiv.org/abs/2502.06857). Detailed source hashes, exclusions, attempts, failures and prior-art records are retained in the research history. This note is a local scientific reference, not certified ground truth or a priority claim.
