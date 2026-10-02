# Native preparation

`prepare(task, data_root, supplemental_root, output)` reconstructs the frozen evaluation cohort directly from source-native measurements. It verifies every retained raw asset for the relevant scenario before parsing. It writes only to a new or empty output directory. It makes no network requests, fits no model and reads no historical prepared table.

The adapter ports preserve the source interpretation of each campaign. `PORTS.json` records the original parser provenance; code and metadata are sealed in `PREPARATION_MANIFEST.json`. The parent evaluator verifies its complete code manifest before importing these adapters.

The output contains inputs, observations, source anchors, explicit calibration inputs, eligibility and groups, plus a receipt. `eligibility.csv.gz` describes membership of reconstructed observations in the frozen task cohort. Native parser exclusions are inherited from the documented parsing contracts; source-only malformed/missing records are not invented as numerical observations. A row absent from this cohort must not be interpreted as an experimental failure or zero response.

Calibration is explicit. Examples include early stiffness, completed previous operations, initial radiomaps and age-zero force curves. No current scored target is silently added as calibration. Case 61 calibration coefficients are frozen fitted states learned from its declared pure-hydrogen experiments, and case 60 condition scales are frozen per-fold training normalizations used only for scoring. Their state and training-scope records are separate from native data. No refitting occurs in preparation.

The cohort registry stores identifier and split metadata only, never cached predictor or target values. A changed source cannot be admitted merely by accepting the old row identifiers. Case 82 preserves source grouping in its anchors while using its explicit forward-fold grouping for evaluation.

Optional case 58 commercial-PLA tasks require the two native archives in an explicit supplemental directory. The corrected case 96 task requires the 21 pinned, earlier-stage annotation text files in an explicit supplemental directory. Original case 96 still reconstructs solely from the core source archive. Missing supplements fail clearly; there is no implicit lookup in research history.

Run full scientific value/anchor parity from the evaluation directory:

```sh
python -m preparation.verify_reconstruction --benchmark ../ \
  --data-root /path/to/local-datas \
  --supplemental-58 /path/to/PLA-native-archives \
  --supplemental-96 /path/to/3_C_vehiclized \
  --report /path/to/new-raw-reconstruction-report.json
```

The verifier uses benchmark tables only as expected outputs for independent QA. Numeric parity uses float64 tolerance 1e-11; identities and metadata are exact. Historical gzip container bytes are not expected to equal freshly serialized containers. Source SHA-256 values remain exact.

Run focused guard and causal-prefix tests with `python -m preparation.check_invariants --data-root /path/to/local-datas`. These checks include source truncation and equal-length mutation, screw trigger timing, settling upstream windows and CHO sensor-quality/future-input handling. They establish computational properties, not a new experiment or an independent laboratory replication.

## Ten-case extension

Cases 13, 21, 51, 54, 56, 64, 74, 85, 87 and 91 add deterministic original-data adapters under new_cases/. Every adapter passed exact cohort identity, group separation and native-value reconstruction checks. Same-device calibration records and exclusions are explicit. No supplemental acquisition is required. The original 25 adapters remain unchanged.
