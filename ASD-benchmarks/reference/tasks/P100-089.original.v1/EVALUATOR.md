# Evaluation contract

Primary metric: brier with equal independent-group weights; units probability squared. Each prediction must be finite and align exactly to every declared sample identity; missing predictions require explicit coverage/abstention treatment in the shared scorer. Alternative equations receive the same tests and need not match our model.

Inputs and calibration: Causal previous choice and running mean within protocol, reset at protocol start; no future outcomes. Reward/probability are experimenter settings, not necessarily participant knowledge.

Timing: Before each choice using trial settings and only prior choices in that protocol; numeric Hidden and EV excluded.

Registered primary task, group definitions and exposure are in `task_spec.json`. Check source hashes before preparation. Local trusted reference replay uses `python run.py`; arbitrary prediction-file scoring does not execute submitted code. Intervals, event thresholds and proposed new endpoints must declare meanings and uncertainty assumptions; never derive acceptance tolerances from a comparator error.

No aggregate scientific-discovery score is implied by lower prediction error. Scientific review separately assesses mechanism, novelty, applicability and negative evidence.
