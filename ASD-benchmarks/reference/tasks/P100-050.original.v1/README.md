# P100-050 final reference package

Read FINDINGS.md for the scientific conclusions, assumptions, equations, comparisons and limitations. `rules.json` holds executable model states; `run.py` verifies and replays them without fitting.

- `data/inputs.csv.gz`: permitted confirmation predictors.
- `data/observations.csv.gz`: measured targets and native/calibration anchors.
- `evidence/`: predictions, mean and individual-group errors.
- `task_spec.json`: input, grouping and information contract.

Install requirements.txt in an existing environment, then run `python run.py`. All outcomes are now exposed and source-aware. Future model development on them requires new confirmation evidence.
