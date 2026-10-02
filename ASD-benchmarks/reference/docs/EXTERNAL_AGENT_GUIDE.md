# External-agent evaluation

## Choose the comparison

Start with quality/ELIGIBILITY.json and an explicit task ID. The baseline is **implemented by GPT-6 Astra**. Matching it is not required. Compare one target, cohort, protocol, information budget and evaluator implementation at a time. Do not pool documentation aliases or raw-access overlays as independent evidence.

1. **Prepared-feature track:** replace an example submission's predictions, equation and declarations; keep the registered columns and exact sample inventory. Use explicit abstentions.
2. **Raw-data track:** resolve a contract in contracts/RAW_ACCESS_REGISTRY.json, derive alternative features from its permitted native observations, and submit their lineage. Different feature names are allowed. Parent targets, groups, eligibility, weights and comparator predictions stay fixed.
3. **New endpoint/budget:** propose and obtain a separate contract. A different task cannot be silently compared to the original cohort's score.

## Raw-data submission

Use `raw-example` to see the submission shape. The example deliberately uses a simple transformation and constant prediction; its native locator must be replaced before scientific review.

Submit submission.json, predictions.csv, derived_features.csv, feature_lineage.json, extractor source and a training inventory. Lineage binds the contract hash and every submitted asset. Each feature declares units, expression, native asset hash, member/column/row or window locator, allowed quantity, source role and availability. Learned transformations need training/tuning groups. Original-data calibration is permitted only under the exact parent contract.

A container or archive hash is not permission to use all its contents. Targets, labels, target-encoding filenames, later responses and undeclared held-group calibration remain prohibited. Do not use identifiers as answer lookup. Quantities not in the information budget need a reviewed amendment.

`raw-validate` checks hashes, exact identities, finite features, declarations, allowed source roles/quantities, declared chronology and training-group consistency. `raw-score` reports parent-cohort numerical errors and matching-baseline comparisons. It labels information compliance **declared_not_independently_verified**: a plausible selector cannot prove arbitrary submitted code obeyed it. This distinction remains necessary in an open corpus.

Native extractor interface `native-v1` accepts:

```text
--data-root PATH --contract JSON --cohort CSV --output CSV
```

The cohort contains IDs/groups, not targets. Output contains sample_id and declared feature columns. `raw-replay --contract ID --submission FOLDER --data-root PATH --output NEW_FOLDER --trust-code` verifies native asset hashes, executes the trusted extractor and compares saved features. The extractor has local filesystem access; this is not a sandbox or proof of training independence. Prediction replay similarly operates only with explicit trust.

## Admit a genuinely different task

The proposer supplies proposal.json, bound evidence and a standalone candidate package: task.json, MANIFEST.json, adapter.json, source assets inventory, native adapter, run.py, rules.json, inputs, observations, comparator predictions and metrics. Adapter output must be `data/inputs.csv.gz` and `data/observations.csv.gz` with exact native identities/groups. It accepts `--data-root` and `--output`, performs no fitting, and must reproduce the packaged values from the declared sources. The frozen runtime supplies `read_table(path)` and `predict(model_state, inputs)` in run.py, with model states under rules.json/models (or the existing versioned fold-runtime format). Every registered comparator is replayed as part of validation. Record source-derived target status and publisher preprocessing.

```sh
python evaluation/benchmark.py propose-task --proposal PROPOSAL --output INTAKE
python evaluation/benchmark.py validate-task --package PACKAGE --data-root DATA --trust-code --output VALIDATION
python evaluation/benchmark.py admit-task --proposal PROPOSAL --package PACKAGE --validation VALIDATION/validation.json --reviews COMPUTATIONAL.json SCIENTIFIC.json --decision MAINTAINER.json --output ADMISSION
python evaluation/benchmark.py register-task --admission ADMISSION --maintainer-id MAINTAINER_ID --output REGISTRATION
```

Both contract reviews bind proposal, package-manifest and validation hashes. Each supplies a distinct reviewer ID, recommendation, and evidence-based status/reason for measurement_semantics, information_budget, grouping, controls, source_rights and scientific_nontriviality. Acceptance requires all six supported in both reviews and a separate maintainer decision; rejection preserves its reasons. Local reviewer/maintainer IDs are declarations, not cryptographic authentication. This is an offline maintenance workflow, not an Internet authorization service.

The decision JSON contains bindings, maintainer_id, rationale, decision (accept/reject), and source_rights. Registration is an explicit maintainer action, never a side effect of proposal intake or scoring. It adds a unique task without replacing existing task IDs or default navigation. Refresh the eligibility matrix, catalog, preparation/release manifests and rights register before exporting a release. Newly registered external adapters require `prepare --trust-code`.

## Scientific findings

Use claims.json to bind a claim to its program, coefficients, variables, units, applicability, source/sample anchors, controls, falsifiers and literature. Failure and abstention claims need a tested proposition and adverse evidence, not an invented equation. Numerical receipts and scientific adjudication are separate artifacts. Follow REVIEW_RUBRIC.md. Generic disclaimers belong in limitations, not discovery counts.

For new reviews use `review prepare`, `review combine`, and, where necessary, `review adjudicate --combined REVIEW.json --decision DECISION.json --output NEW_FOLDER`. Adjudication binds the combined-review hash, an adjudicator ID/scope, every finding, its disposition/rationale/evidence IDs and each resolved dimension. No operation automatically certifies novelty or registers a new discovery.
