# Risky choice: history dominates the compact predictive account

## Experiments and task

The source contains seven new behavioral experiments with **540 participants** choosing between fully described lotteries. We use those experiments and exclude the older comparison dataset. Complete participants are split by identifier hash within each experiment: 432 for development and **108 for final confirmation**, containing 26,640 choices. Five folds hold whole development participants out.

The endpoint is the probability of the current risky choice. Predictions are made before that choice. Permitted inputs include current lottery values and probabilities, known feedback instructions, and strictly previous choices/visible outcomes from the same block. Unannounced feedback is masked on the first trial. Current rewards, response time and future choices are excluded. Every comparator receives the same permitted history; this is sequential prediction with observed past behavior, not zero-observation personalization.

## Selected equation

Let $\sigma(z)=(1+e^{-z})^{-1}$, $\Delta$ be risky minus safe expected points divided by the absolute risky magnitude, $p$ the risky probability, $v\in\{-1,1\}$ the gain/loss sign, and $s$ indicate a variable safe lottery. Let $f$ indicate feedback known before choice, $c$ complete feedback, and $H(p)=-p\log p-(1-p)\log(1-p)$. In the current block, $n$ prior choices with $k$ risky choices define $h=(k+1)/(n+2)$. Set $\ell=(y_{t-1}-0.5)$ if history exists, otherwise zero. The frozen rule is

$$\widehat P(\mathrm{risky})=\sigma\!\left(\boldsymbol\beta^\top[1,\Delta,p-0.5,v,s,f,fH(p),fc,\log(h/(1-h)),\ell]\right).$$

In this exact order,

$$\boldsymbol\beta=(-0.338636, 0.732453, 0.0529664, 0.000157704, -0.0398615, 0.129943, 0.0658394, 0.0915562, 1.14435, 0.56123).$$

The historical log-odds coefficient is **1.14435** and immediate persistence coefficient **0.56123**. They are predictive descriptors, not proof that participants implement a Bayesian algorithm or a unique psychological mechanism. Full precision is in `rules.json`.

## Validation and competing explanations

| Model | Development participant Brier | Confirmation participant Brier |
|---|---:|---:|
| Constant probability | 0.23898 | 0.24456 |
| Lottery expected-value/probability model | 0.23774 | 0.24370 |
| Matched flexible history model | 0.15714 | 0.15772 |
| Selected compact history log-odds | 0.15650 | 0.15696 |

Brier is the mean squared probability error within each participant, then averaged equally across participants. Lower is better. The selected model is only slightly better than the flexible comparator: paired difference **-0.000765**, with an exploratory participant-resampling 95% interval **[-0.001598, 0.000055]**. It wins on 62/108 individuals. This supports a compact competitive representation, not a large demonstrated advantage.

At the declared equal-cost threshold0.5, confirmation precision is 0.7707, recall 0.6242 and F1 0.6898. These row-count event diagnostics complement participant-balanced probability scoring; they are not industrial acceptance limits. Calibration bins, log loss and all group errors are retained.

Five attempts contrasted prospective feedback attitudes, visible-outcome learning, choice inertia, additional regret/reward errors and a compact historical log-odds account. Pure attitude and pure experiential models remained near0.236 development Brier, whereas prior choices brought error near0.157. This is **not a new discovery that feedback changes preferences**: the source paper already studies that question. Our bounded contribution is a replayable comparison under an explicitly causal information budget.

After confirmation, we added unfitted diagnostic checks without changing selection: the smoothed empirical propensity alone gives Brier **0.16199**, and copying the previous choice gives **0.22528**. These exposed-data checks are labeled separately and cannot be treated as a new untouched confirmation campaign.

## Scope, significance and reproduction

The experiments repeatedly present the same lottery within a block, making past choices highly informative. Performance does not establish transfer to changing real-world decisions, financial outcomes or clinical behavior. Between-person and between-experiment variation remain; the reported paired resampling interval conditions on these source participants and is not proof of universal psychological generalization. Behavioral history does not resolve attitude, preference stability and learning causally.

`python run.py` verifies hashes and reproduces all saved predictions. The native adapter reconstructs legal histories and sample anchors from the original pinned ZIP. `task_spec.json` fixes the target, cohort, disclosure rules and Brier metric; alternative equations need not resemble this one. `evidence/` includes calibration, event metrics, complete group results and explicitly post-confirmation diagnostic controls. All results are now exposed for future users; no independent experimental replication or new cognitive law is claimed.

[Source study](https://doi.org/10.1038/s41467-025-67729-x), [primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12847909/), and [pinned native source](https://zenodo.org/records/17807047). Native data: CC BY4.0. Literature reviewed 2 October 2026.
