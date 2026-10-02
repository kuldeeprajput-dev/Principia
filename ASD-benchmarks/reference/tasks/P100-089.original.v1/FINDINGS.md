# Context and causal history in binary risk-choice prediction

The native CSV contains27,667 choices from55 participant identities linked across E1.1,E1.2 andE2.2. The advertised fourth experiment,E2.1,is absent. Experimenter reward/probability settings, child/adult status, presentation context and strictly previous choices predict the recorded binary choice. Twelve whole participants are reserved. Primary error is equal-participant Brier score; log loss, calibration and threshold diagnostics accompany it.

## Question and information budget

Before each choice using trial settings and only prior choices in that protocol; numeric Hidden and EV excluded. Causal previous choice and running mean within protocol, reset at protocol start; no future outcomes. Reward/probability are experimenter settings, not necessarily participant knowledge.

## Findings and interpretation

Context and causal choice history support a stronger bounded probability reference than expected value alone. This is useful for assessing new choice predictors with matched online information, not for ranking individual risk tolerance or making demographic decisions.

The selected executable relation is:

`Pr(Choice=1 | available history) = 1 / (1 + exp(-beta dot phi)).`

Let r=reward/2, p=the experimenter-specified probability, a=child, m=multi-option context, v=explicit-description context, h=the previous-choice running mean minus0.5, and l=the immediately previous choice minus0.5. The ordered vector phi is (1,r,p,r*p,r^2,p^2,a,m,v,a*m,a*v,r*a,p*a,r*m,p*m,r*v,p*v,h,l,h*a,h*m,trial_progress). The intercept is -3.302904, and the h and l coefficients are 2.629934 and 1.308668. Child/adult and context interactions alter those effects; an isolated coefficient is not a causal effect. The frozen coefficients already undo training feature-RMS scaling, so the displayed vector is used directly without standardization. Adult age is not included in this selected model.

The full coefficient table and variable ordering are in `EQUATIONS.md`; `rules.json` contains exact precision. All equation inputs and their units are declared in `task_spec.json`.

Compact prospect weighting does not explain the main predictive gain. Context and memory candidates improve the expected-utility comparison but do not beat the frozen flexible control. Correlated history columns in one candidate are regularized rather than mechanistically identifiable.

## Experimental design and performance

The reference `baseline_flexible` was chosen before confirmation. Development error was **0.12736483**; reserved-group error is **0.14335862 probability squared** across **12 groups and 6008 observations**. Scores use equal group weights, with equal row weights within each group. No population confidence interval is inferred from these small samples. Brier score is the mean squared probability error; lower is better. Supplementary threshold statistics are row-count diagnostics, while Brier and log loss are group balanced.

| Frozen model | Confirmation primary error |
|---|---:|
| reference | 0.14335862 |
| baseline_mean | 0.24762301 |
| baseline_utility | 0.18844055 |
| baseline_persistence | 0.23265573 |
| baseline_flexible | 0.14335862 |

5 substantive development attempts were preserved. Selection used whole-group out-of-fold errors and preferred the simplest model within1% of the minimum. Continuation ended only after two consecutive substantive attempts failed to improve prediction and no supported mechanism/robustness gain justified another candidate. Confirmation ran separately after code, source, states, selection and stopping were frozen. No later diagnostic winner was promoted.

## Scope, prior work and value

All trial contexts for each person stay in one partition. The stored probability is an experimenter setting and may be hidden from the participant; this is an analyst forecast. Binary Choice is retained unchanged, with1 treated as the recorded risky-choice code; no separate codebook was supplied. Adult ages are unavailable; age_child uses an explicit adult sentinel. Histories reset at each protocol.

Lacombe et al., Frontiers2025, already report age-dependent context shifts, description/experience differences and exploration/framing hypotheses using binomial models. Expected utility, prospect weighting and logistic choice models are established. Better prediction cannot adjudicate a unique cognitive mechanism.

No new universal law, independent experimental replication, clinical benefit or demonstrated industrial impact is claimed. Alternative valid discoveries can be evaluated using the same task contract; exact agreement with this equation is unnecessary. Negative findings describe failed tested hypotheses, not a lack of scientific phenomena.

## Reproduction and evaluation

Run `python run.py` inside this folder to verify frozen asset hashes and reproduce all saved predictions. It uses no network, fitting, research-history import or hidden model state. Submitter predictions must use the same sample IDs, units, information budget and group cohort. `scientific_checks.py` adds domain diagnostics to the shared benchmark scorer; it does not execute submitted code. New endpoints require a separately reviewed task.

Sources: [authoritative data](https://zenodo.org/records/15412216), [primary study](https://doi.org/10.3389/fnbeh.2025.1644777). Source assets are CC BY4.0; citations and exact native hashes are retained in the scenario research layer. Current confirmation outcomes are exposed for all future users.
