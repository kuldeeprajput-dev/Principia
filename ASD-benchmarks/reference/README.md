# Principia-100 reference results and evaluation

**implemented by GPT-6 Astra** — the reference ASD baseline for [Principia-100 v0.2.0](../README.md).

This package contains all 100 scenario portfolios: 99 numerical cases and one source-adequacy assessment. Its 134 public numerical task versions preserve 1,362 recorded model comparisons. Raw-access overlays add alternative feature routes under the same targets; they are not additional experiments. All outcomes are exposed.

| Start here | Purpose |
|---|---|
| [Integrated catalog](../CATALOG.md) | Native data, PDF reports, findings and evaluation scope |
| [100-case audit](quality/README.md) | Task-level eligibility and scientific limitations |
| [Finding register](quality/FINDING_REGISTER.json) | Expressions, coefficients, executable states and exact evidence |
| [External-agent guide](docs/EXTERNAL_AGENT_GUIDE.md) | Scoring, native features, replay and task admission |
| [Review rubric](docs/REVIEW_RUBRIC.md) | Numerical and scientific judgments kept separate |
| [Publication audit](../RELEASE_AUDIT.md) | Fresh public-folder validation and known restrictions |

## Use the evaluator

From this directory, install `evaluation/requirements.lock.txt` in a Python 3.12 environment outside the release. The lock records the tested environment; receipts record actual versions. See the [download guide](../DOWNLOAD.md) for Git LFS.

```bash
python evaluation/benchmark.py list --all-cases
python evaluation/benchmark.py example --task P100-037.original.v1 --output /tmp/p100-example
python evaluation/benchmark.py score --task P100-037.original.v1 --submission /tmp/p100-example --output /tmp/p100-score
python evaluation/benchmark.py prepare --task P100-037.original.v1 --data-root ../scenarios --output /tmp/p100-native
python evaluation/benchmark.py verify
```

Prediction-file scoring executes no submitted code. Replay needs explicit `--trust-code`. Source archives may contain publisher programs; inclusion does not make those programs trusted. Complete native reconstruction includes the declared case-58 supplements. The original case-96 task is included; its optional supplemental task remains excluded for unresolved source-data rights.

## Interpret the reference correctly

Observed targets and exact mathematical quantities are evaluation labels. Astra findings are fallible reference results, including reproductions, scoped extensions, failed hypotheses and abstentions. Alternative valid equations are welcome. Mechanism, novelty and deployment benefit require their own evidence. There is no aggregate discovery score.

Current navigation uses the quality layer and task registry. Original scientific reports and review receipts are preserved as history, including their historical local-release statements. The corpus release is v0.2.0; internal task, evaluator and schema revisions retain their recorded identifiers. [Baseline attribution](BASELINE.md) · [Rights](../LICENSES.md) · [Publication adaptations](../PUBLICATION_ADAPTATIONS.json).
