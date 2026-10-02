# P100-056 final results

Start with FINDINGS.md/PDF, then findings.json. Reference selection and failures are explicit.

- Run `python run.py` for frozen replay.
- `data/` contains the exposed confirmation cohort, not training data.
- `evidence/` contains all candidate predictions and equally weighted group metrics.
- `preparation/native.py` reconstructs source data with SOURCE_MANIFEST.json integrity checks.
- `task_spec.json` specifies allowed inputs and timing; the authoritative common evaluator is installed by benchmark integration.

Dependencies: numpy, pandas, scipy; openpyxl is required only for native preparation. No networking or fitting occurs during replay.
