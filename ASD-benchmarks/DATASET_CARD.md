# Dataset card · Principia-100 v0.2.0

## Purpose and composition

Principia-100 is an open corpus for evaluating quantitative autonomous scientific discovery from heterogeneous research folders. This release connects 100 source scenarios, reference ASD results **implemented by GPT-6 Astra**, and explicit evaluation contracts. It is usable independently of the Principia application.

| Component | Scope |
|---|---|
| Native corpus | 100 cases; 1,685 scientific assets, unchanged from v0.1.1 |
| Data origin | 85 measured/observed, 8 mixed, 6 computational experiments, 1 mathematical reference corpus |
| Reference results | 100 PDF/Markdown portfolios, executable equations and frozen states, measured labels, predictions, controls and preserved failures |
| Numerical evaluation | 134 public task versions across 99 cases; 1,362 recorded model comparisons, including aliases |
| Adequacy evaluation | Case 8 evaluates source sufficiency; no clinical prediction score is fabricated |
| Default task eligibility | 35 comparative core, 58 limited-scope, 7 diagnostic/adequacy |

## Sources and processing

Original institutions, researchers, versions, measurement/release dates, transport provenance, SHA-256 hashes, bytes and source-specific terms are recorded in the [source catalog](SOURCE_CATALOG.md), [acquisition manifest](ACQUISITION_MANIFEST.json), [citation register](CITATIONS.json) and [license register](LICENSE_REGISTER.json). Native archives preserve publisher files and preprocessing. Source-native does not imply untouched instrument telemetry.

The evaluation layer adds deterministic native readers, fixed cohorts, explicit calibration/history and derived target tables. Learned transformations and model parameters are frozen with their stated training scope. [Publication adaptations](PUBLICATION_ADAPTATIONS.json) map local acquisition metadata to the accepted public layout without changing measurements or numerical targets.

## Labels, baselines and information access

Measured observations and exact mathematical quantities are task targets. GPT-6 Astra findings are fallible reference baselines, not uniquely correct ground-truth laws. Registered-task predictions may use any valid alternative expression within the same input and calibration budget. New endpoints require separate reviewed contracts.

Source documents, author analyses and all current evaluation outcomes are exposed. The original 20 cases were used during Principia development. Source-aware scoring is retrospective; neither a nominal historical holdout nor an unknown model training corpus establishes freshness today. Reference results must not be silently used as fitting targets or claimed to have been unseen.

## Intended use and limits

Use the corpus for inspectable equations, baseline comparisons, uncertainty and falsification studies, reader development, and explicit adequacy judgments. It is not a clinical deployment benchmark, evidence of universal physical laws, or a measured industrial return-on-investment study. Predictive accuracy, explanation, novelty and practical value remain separate assessment dimensions.

Grouping follows the experiment; rows are not automatically independent units. Cases with one instrument, patient, event, session or specimen have bounded transfer claims. Missing training inventories, source preprocessing, calibration burdens, ambiguous metadata, constant targets and absent event classes are documented in the [quality matrix](reference/quality/ELIGIBILITY.json). Abstention and negative results are valid outcomes. No aggregate discovery score is supplied.

## Reuse, supplements and maintenance

Third-party assets retain their source-specific licenses; curator documentation is CC BY 4.0 and curator tools are MIT. Case 59's auxiliary weather provenance remains qualified under depositor terms. Four case-58 PLA response tasks use explicit additional archives. The unresolved case-96 supplemental data are excluded; its original-data task remains included.

Report issues with case/task IDs, hashes and evidence. Version changes to endpoints, cohorts or information budgets rather than overwriting comparisons. The [protocol](EVALUATION_PROTOCOL.md), [external-agent guide](reference/docs/EXTERNAL_AGENT_GUIDE.md) and [release audit](RELEASE_AUDIT.md) define current use. Earlier [source-card details](SOURCE_DATASET_CARD.md) and research receipts remain historical context.
