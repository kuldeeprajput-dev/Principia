# Evaluation contract

Primary metric: mae with equal independent-group weights; units ug animal^-1 h^-1. Each prediction must be finite and align exactly to every declared sample identity; missing predictions require explicit coverage/abstention treatment in the shared scorer. Alternative equations receive the same tests and need not match our model.

Inputs and calibration: Mean DMS emission at-48/-24h, difference and age at first post-dose row; five post-dose points are forecast. Other VOCs and disease labels excluded.

Timing: Prediction at treatment administration from pre-dose breath samples and scheduled post-dose time.

Registered primary task, group definitions and exposure are in `task_spec.json`. Check source hashes before preparation. Local trusted reference replay uses `python run.py`; arbitrary prediction-file scoring does not execute submitted code. Intervals, event thresholds and proposed new endpoints must declare meanings and uncertainty assumptions; never derive acceptance tolerances from a comparator error.

No aggregate scientific-discovery score is implied by lower prediction error. Scientific review separately assesses mechanism, novelty, applicability and negative evidence.
