# Independent native future-mutation checks

All six test variants passed. This is a causal-input audit of native preparation, not a new discovery evaluation or a new held-out confirmation. No frozen scientific package, model, original source or published outcome was changed.

| Case | Coverage | Inputs after native mutation | Target response |
|---|---|---|---|
| 007 | One midpoint origin in each of 3 force recordings | Exactly unchanged | +123 N |
| 009 | One midpoint origin in each of 6 eligible NWB sessions | Exactly unchanged | +5 pixels |
| 080 | One midpoint origin in each of 31 aerobic recording segments | Exactly unchanged | +1 μS |
| 099 | One midpoint origin in each of 130 eligible MAT sessions | Exactly unchanged | +0.001 author trace units |
| 088 | First-trial and midpoint origins in each of 3,984 unannounced-feedback blocks | Exactly unchanged in both variants | Current binary choice flipped |

## Method

The unchanged native adapter is copied to a disposable directory. Source records strictly after the forecast issuance are modified, the fixture manifest is recomputed, and the adapter reconstructs observations from that fixture. Case 88 modifies current and future unavailable outcomes, choices and feedback-type metadata while preserving legitimately available instructions and earlier revealed history. All declared numeric predictors at the chosen origins must remain unchanged; the targets must change. This tests native preparation, rather than merely changing a target column in an already prepared prediction file. Original source hashes are checked again after the tests.

The exact tested adapter, task and source-manifest hashes, selected sample identities, partition labels, mutation details and per-origin differences are in `ASD7_NATIVE_PREFIX.json`. `asd7_native_prefix.py` is the implementation; its SHA-256 is bound in the receipt.

## Coverage limits

- These are finite adversarial probes, not a proof for every input or every issuance time. All currently exposed partitions are eligible for this software-integrity audit.
- The tests begin with released products. They do not establish that publisher filtering, denoising, normalization or extraction was causal. These upstream limitations remain in the scientific portfolios.
- Existing timing, shapes, missingness and quality flags are preserved. Eligibility changes induced by newly introduced missing values are outside this probe.
- Case 009 retains seven NWB files, but `sub-16_ses-16-3-1-Ach-M1_behavior+ophys.nwb` provides no eligible task origin. Case 099 covers all 130 task-eligible sessions; the 27 source files lacking the required trace are outside the task.
- Case 088 tests unannounced-feedback blocks. Announced current instructions are permitted information and are not treated as a forbidden future input.
- Prefix invariance does not establish a physiological mechanism, a causal effect or practical deployment validity.

## Portable replay

Run from the benchmark root with the recorded scientific dependencies:

```sh
python evaluation/tests/replay_native_prefix.py --data-root /path/to/local-datas --output NEW_AUDIT_FOLDER
```

Add `--cases 7` to run one supported case. The launcher verifies bound evidence and code, stages the exact adapters in a disposable campaign layout, and preserves original source bytes. The archived script remains unchanged. Its original campaign receipt is historical evidence; a later execution is a software-integrity replay, not new scientific confirmation.
