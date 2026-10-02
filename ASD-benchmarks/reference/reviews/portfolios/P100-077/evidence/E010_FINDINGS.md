# Joint ONE-STEP tagging: an assay-dependence reference

## Experiment and information budget

Nine Fig6H FCS wells span three dose multipliers (1, 3, 6) and three named experimental replicate blocks. The source paper establishes dual tagging in a hiPSC line; that biological result is prior art. We analyze green mNeonGreen and red mCherry area channels with a reproducible gate: finite signals, positive FSC-A/SSC-A, and channel-specific thresholds at the BOB negative control’s 99.5th percentiles. The source’s manually drawn FlowJo gates are unavailable. These endpoint frequencies therefore **are not a reproduction of the published percentages**.

Let $p$ and $q$ be green- and red-positive fractions from the same well, and $j$ the jointly positive fraction. Inputs $p,q$ are contemporaneous measurements. Their product is an independence hypothesis, not an identity: the marginals alone do not determine $j$. The primary response is $100j$ in percentage points. The task is a distributional diagnostic, not prediction of editing yield before an experiment or proof of correct genomic integration.

## Selected relation and evidence

A compact constant association equation was selected from development blocks A and C:

$$j(1-p-q+j)=\theta(p-j)(q-j),\qquad \theta=58.3803082.$$

The unique solution is restricted to the Fréchet interval $\max(0,p+q-1)\leq j\leq\min(p,q)$. The saved log-odds coefficient is 4.06697864463; `run.py` solves the bounded scalar equation deterministically. A large effective association is compatible with shared delivery competence, cell-state variation or optical/gating effects; it does not distinguish these mechanisms.

| Model | Development block MAE | Reserved block B MAE |
|---|---:|---:|
| Independence, $j=pq$ | 0.23714 | 0.29297 |
| Constant joint rate, physically bounded | 0.27173 | 0.27256 |
| Flexible bounded marginal/dose model | 0.08983 | 0.03222 |
| Selected constant odds ratio | 0.07938 | 0.09624 |

The selected equation improves the independence comparator on the reserved block but **does not beat the flexible control**. All three held wells belong to one replicate block; this is not three independent biological confirmations. Reported errors are percentage points, and no clinical or industrial performance threshold is asserted.

## Attempts, interpretation and limits

Five hypotheses tested a mixture of independent and maximally shared competence, constant odds association, a common transfectable fraction, dose-dependent competence and negative resource competition. The competition fit returns essentially independence and fails to explain the development joint frequency. This is supported negative evidence for that bounded family. The source experiment does not uniquely identify a molecular dependence mechanism.

The practical value is a transparent assay-consistency relation and a strong requirement that new claims compare against both independent marginals and a flexible model with the same readouts. A one-parameter explanation can remain interpretable while failing to be the best predictor. Stronger scientific claims would require more independent replicate experiments, single-color compensation controls, documented gates and orthogonal integration assays. Gate sensitivity remains a limitation of this exact task; the endpoint must not be silently redefined to match source percentages.

## Reproduction and evaluation

`python run.py` verifies integrity and replays all model predictions. `rules.json` contains every coefficient and bound; `EQUATIONS.md` gives each candidate equation. The native adapter reconstructs fractions from the checksum-verified FCS archive. Predictions never read the withheld joint target. `task_spec.json` freezes the contemporaneous input budget and exact gating definition. Alternative equations can be scored on these observations, but better numerical error alone does not prove editing mechanism or novelty. Selection and stopping were frozen before block B was opened; all results are now exposed for future users.

[Original study](https://doi.org/10.1093/nar/gkaf809), [primary open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12359036/), and [native source](https://zenodo.org/records/15772077). Native data: CC BY 4.0. Literature reviewed 2 October 2026.
