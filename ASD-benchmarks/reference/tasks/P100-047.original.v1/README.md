# P100-047 final results

Start with [FINDINGS.md](FINDINGS.md). Exact equations/states: [rules.json](rules.json). Measurement, timing and grouping contract: [task_spec.json](task_spec.json).

`python run.py` verifies and replays the bundled trusted equations. `data/` contains the frozen confirmation inputs/targets; `evidence/` contains every candidate prediction and group errors. Future outcome access is exposed. These files support evaluator-based reference assessment, not certified ground truth or novelty.
