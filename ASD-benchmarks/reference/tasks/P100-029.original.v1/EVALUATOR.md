# Evaluation contract

Primary metric: mae with equal independent-group weights; units source fluorescence a.u.. Each prediction must be finite and align exactly to every declared sample identity; missing predictions require explicit coverage/abstention treatment in the shared scorer. Alternative equations receive the same tests and need not match our model.

Inputs and calibration: Spectrum-wide mean fluorescence at native concentrations 0,1,2,5 nominal uM, per replicate; target concentrations 7.5 to30. No maximal-response normalization.

Timing: Predict remaining higher-dose assay values after declared lower-dose measurements; sequential assay not real-time kinetics.

Registered primary task, group definitions and exposure are in `task_spec.json`. Check source hashes before preparation. Local trusted reference replay uses `python run.py`; arbitrary prediction-file scoring does not execute submitted code. Intervals, event thresholds and proposed new endpoints must declare meanings and uncertainty assumptions; never derive acceptance tolerances from a comparator error.

No aggregate scientific-discovery score is implied by lower prediction error. Scientific review separately assesses mechanism, novelty, applicability and negative evidence.
