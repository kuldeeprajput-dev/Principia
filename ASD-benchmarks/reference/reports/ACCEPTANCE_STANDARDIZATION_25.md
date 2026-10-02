# Local acceptance report

**Status: standardized local release candidate. No publication performed.**

The authoritative layer indexes 100 scenarios: 25 explored portfolios with working task evaluators and 75 pending cases. It standardizes existing evidence rather than conducting another discovery campaign. Native source files and historical result trees remain preserved.

## Verified coverage

| Check | Result | Receipt |
|---|---|---|
| Catalog and task identity | 100 cases; 25 equipped; 75 pending; 54 local tasks | [registry.json](../registry.json); [FINAL_VALIDATION.json](FINAL_VALIDATION.json) |
| Original-data core | 49 tasks reconstruct from the original corpus alone | [RAW_RECONSTRUCTION.json](RAW_RECONSTRUCTION.json) |
| Explicit supplements | 4 PLA tasks and 1 corrected cycling task reconstruct with declared sources | [RAW_ACCEPTANCE.json](RAW_ACCEPTANCE.json) |
| Native numerical/identity parity | 54/54 tasks; 754 columns; 307, 478 task rows; maximum numerical difference 2.28e-13 | [RAW_RECONSTRUCTION.json](RAW_RECONSTRUCTION.json) |
| Historical metric preservation | All 533 model comparisons independently reproduce | [EVALUATOR_COMPUTATIONAL_REVIEW.json](EVALUATOR_COMPUTATIONAL_REVIEW.json) |
| Portable numerical references | All 54 task examples replay from frozen state | [EVALUATOR_COMPUTATIONAL_REVIEW_EVALUATOR_EXAMPLES_REPLAY.json](EVALUATOR_COMPUTATIONAL_REVIEW_EVALUATOR_EXAMPLES_REPLAY.json) |
| Evaluator adversarial fixtures | 97 passed: 39 numerical/submission, 15 review/proposal, 35 legacy imports, 8 endpoint checks | [EVALUATOR_COMPUTATIONAL_REVIEW.json](EVALUATOR_COMPUTATIONAL_REVIEW.json) |
| Native integrity and causal prefixes | 8 native guards plus 20 linked-group/chronological checks passed | [RAW_INVARIANTS.json](RAW_INVARIANTS.json); [LINKED_GROUPS.json](LINKED_GROUPS.json) |
| Human-readable portfolios | 25 PDFs; 74 pages visually inspected | [PDF_QA.json](PDF_QA.json) |
| Scientific assessments | 25 portfolios; 69 findings; separate computational and scientific reviewers | [PORTFOLIO_REVIEW_BINDINGS.json](PORTFOLIO_REVIEW_BINDINGS.json) |
| Review conversion | 54 exact task mappings; 15 historical claims conservatively not mapped one-to-one | [SCIENTIFIC_REVIEW_CONVERSION.json](SCIENTIFIC_REVIEW_CONVERSION.json); [COMPUTATIONAL_REVIEW_CONVERSION.json](COMPUTATIONAL_REVIEW_CONVERSION.json) |
| Existing evidence preservation | All 9, 299 inventoried files unchanged; 609, 286, 104 bytes | [PRESERVATION.json](PRESERVATION.json) |
| Public-ready projection | 53 distributable task versions; 514 model-score comparisons verified in exported tree | [PUBLIC_EXPORT_VALIDATION.json](PUBLIC_EXPORT_VALIDATION.json) |

Counts of task rows are sums across versioned tasks, not distinct participants or independent experiments. Numerical tolerance concerns float64 serialization; original native asset hashes remain exact. The receipt reports the precise maximum difference 2.2737367544323206e-13.

## Corrections and scope distinctions

The shared evaluator fixes complete event-prediction failure to F1 zero when its denominator is positive. Undefined no-event cases carry reasons. Historical receipts remain intact. Case 58's secondary loss measurement is now in observations rather than predictors; storage predictions remain unchanged. Native adapters preserve explicit nonpositive-stiffness eligibility and correct source-cell/timestamp anchors. Learned calibrations and scoring scales retain frozen training scope.

Negative findings remain negative: support for a falsification does not turn it into a successful positive predictor. Findings, numerical models and tasks have separate IDs. First-continuation historical claims without a one-to-one registered contract remain assessable scientific evidence but receive no invented claim-specific numerical validation.

The local layer has 54 tasks. Its allowlist export excludes the corrected cycling task and its supplemental native/detailed numerical assets because sufficient data-specific redistribution evidence is unresolved. Original cycling and all 25 case portfolios remain represented. The public case 96 executable review packet is restricted to original-corpus evidence. PLA supplemental data retain their author's CC BY 4.0 terms. All exclusions and exact stored sizes appear in [RELEASE_MANIFEST.json](../RELEASE_MANIFEST.json).

## Demonstrated workflow

A different existing router model is accepted and scored under the same registered task. A source-bound orthogonal polymer-loss proposal remains pending independent contract review; the same proposal attempting to overwrite a registered task is rejected. Every current task is exposed, including the formerly fresh PLA challenge. Future submissions may propose valid alternatives without reproducing a reference equation.

## Scientific limits

There are 333 older alternative-model fold records without source-recorded training-group lists. Their validation linkage and numerical replay are verified, but absent historical training membership is not claimed verified. All current cycle-001 scopes include recorded training groups.

This migration establishes reproducibility and consistent assessment; it does not establish new physical laws, definitive novelty or deployment impact. Small group counts, calibrated apparatus/site scope, source processing and public-data exposure continue to limit generalization. Agent reviews are advisory and do not constitute human expert adjudication or independent laboratory replication. Prediction-file scoring cannot verify hidden training behavior; explicitly trusted replay is not a security sandbox.

The local-data audit verifies native bytes consumed by the 25 adapters. The historical preservation inventory intentionally excluded disposable caches/logs/figures and files above 150 MB; no destructive operation was applied to those exclusions. Original publisher archives retain their contents. No private research data, machine-specific user paths or operational history is admitted to the public-ready package.
