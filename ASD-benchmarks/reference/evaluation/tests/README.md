# Reusable evaluator tests

Run these scripts from any checkout using the benchmark's Python dependencies. They locate the benchmark relative to their own files; they do not read historical research directories, refit models or access the network. An omitted `--output` uses a temporary directory. Supplied output directories contain disposable fixtures and JSON receipts.

```
python evaluation/tests/test_shared_engine.py --output /tmp/p100-numerical-tests
python evaluation/tests/test_review_workflow.py --output /tmp/p100-review-tests
python evaluation/tests/test_legacy_import.py --output /tmp/p100-legacy-tests
python evaluation/tests/test_scientific_endpoints.py --output /tmp/p100-endpoint-tests
python evaluation/tests/independent_metric_parity.py --output /tmp/p100-parity-tests
```

These suites exercise numerical/submission checks, task proposals and independent reviews, legacy imports, and endpoint diagnostics. The receipt for each invocation records its current check count. The separate parity script recomputes every registered historical model score with direct group reductions rather than calling the shared metric engine. Each script exits nonzero on failure.

The legacy importer is prediction-only: unknown input access and training exposure remain unknown, and no equation or scientific finding is invented. Reference replay is tested separately because it explicitly executes locally trusted model code.

Additional collection checks:

```sh
python evaluation/tests/test_linked_groups.py --report /tmp/p100-linked-groups.json
python evaluation/tests/test_collection_integrity.py --output /tmp/p100-collection-integrity.json
```

The linked-group suite covers 20 frozen grouping/chronology contracts. The integrity suite checks registry counts, task schemas, 100 reader packages, claim bindings, sealed evaluator assets and the release allowlist. Use a new output destination. Native source reconstruction and causal-prefix mutation tests are documented in `../preparation/README.md`.

ASD5 adds13 source-specific adverse diagnostics in test_asd5_diagnostics.py, including incomplete-pair event coverage, zero-event F1, signed optical responses and timing/domain counterexamples. The original97 fixtures remain in place.
