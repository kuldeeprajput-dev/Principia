# Evaluation contract

Primary metric: mae with equal independent-group weights; units cmH2O. Each prediction must be finite and align exactly to every declared sample identity; missing predictions require explicit coverage/abstention treatment in the shared scorer. Alternative equations receive the same tests and need not match our model.

Inputs and calibration: Source fixed ADC-to-cmH2O conversion; no target-participant fitted coefficients. All history at or before forecast origin.

Timing: At each fixed1s origin predict native gauge pressure0.20s later using only present/past pressure and differential-pressure signals.

Registered primary task, group definitions and exposure are in `task_spec.json`. Check source hashes before preparation. Local trusted reference replay uses `python run.py`; arbitrary prediction-file scoring does not execute submitted code. Intervals, event thresholds and proposed new endpoints must declare meanings and uncertainty assumptions; never derive acceptance tolerances from a comparator error.

No aggregate scientific-discovery score is implied by lower prediction error. Scientific review separately assesses mechanism, novelty, applicability and negative evidence.
