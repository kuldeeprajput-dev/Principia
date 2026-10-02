# P100-066 - Replication Data for : Boosting hydrogen storage and release in MOF-5 / graphite hybrids via in situ synthesis

Read **FINDINGS.pdf** or its editable **FINDINGS.md** first. The finding index separates empirical prediction, mechanism, metrology correction and falsification.

The default runnable reference is `P100-066.continuation.v1`. Run `python run.py` to reproduce it locally. Other available task versions and comparators are listed in the shared task registry. Matching this reference equation is not required for a valid alternative finding.

From the benchmark root:

```bash
python evaluation/benchmark.py example --task P100-066.continuation.v1 --output /tmp/P100-066-submission
python evaluation/benchmark.py score --task P100-066.continuation.v1 --submission /tmp/P100-066-submission --output /tmp/P100-066-report
```

Optional executable replay requires `replay --trust-code`. It is local trusted execution. The evaluator reports numerical evidence separately from scientific agent review. All current targets are exposed.

The `tasks.json` file lists exact alternative task contracts; compare only identical task/cohort/information budgets. Supplemental tasks are optional and cannot be reproduced from the original scenario alone. Useful reasoning and failures are in the adjacent curated research history.
