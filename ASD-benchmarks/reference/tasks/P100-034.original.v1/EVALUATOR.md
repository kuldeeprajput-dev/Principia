# Evaluation contract

Primary metric: mae with equal independent-group weights; units nA. Each prediction must be finite and align exactly to every declared sample identity; missing predictions require explicit coverage/abstention treatment in the shared scorer. Alternative equations receive the same tests and need not match our model.

Inputs and calibration: First-pulse mean across ten sweeps at0.4 and0.75mM per animal. Later1.5/3/6mM targets are excluded from calibration.

Timing: After two lower-dose blocks, forecast mean first-pulse current at the three later calcium doses; all animal data linked.

Registered primary task, group definitions and exposure are in `task_spec.json`. Check source hashes before preparation. Local trusted reference replay uses `python run.py`; arbitrary prediction-file scoring does not execute submitted code. Intervals, event thresholds and proposed new endpoints must declare meanings and uncertainty assumptions; never derive acceptance tolerances from a comparator error.

No aggregate scientific-discovery score is implied by lower prediction error. Scientific review separately assesses mechanism, novelty, applicability and negative evidence.
