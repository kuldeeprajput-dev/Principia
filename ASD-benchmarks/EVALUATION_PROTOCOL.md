# Principia-100 evaluation protocol · v0.2.0

This release joins the native corpus with GPT-6 Astra reference results and executable evaluation. **All existing outcomes are exposed.** It supports open, retrospective comparisons and separately reviewed scientific claims.

## Evaluation identity

Record release tag/commit, case ID, task ID, protocol version, cohort ID, evaluator manifest hash, runtime fingerprint, submission hash and information budget. Raw-access contracts also bind source selectors and feature lineage. A score from a different endpoint, cohort or calibration budget is not directly comparable.

## Registered tasks and new findings

Follow the [external-agent guide](reference/docs/EXTERNAL_AGENT_GUIDE.md) for prepared-feature scoring, alternative raw feature extraction and new-task admission. The [registry](reference/registry.json) is authoritative for executable tasks. Acquisition-stage [task cards](task_cards/) provide context; their research opportunities do not override a registered contract.

An alternative predictor need not resemble the Astra reference. A different measured endpoint, observation window or input budget requires a distinct contract approved after native reconstruction, comparator replay and independent computational/scientific-critical review. A maintainer explicitly accepts or rejects it before separate registration. Existing tasks cannot be silently overwritten.

## Quantitative evidence

Preserve native values, missingness, linked groups, timing and quality flags. Fit learned transformations on declared development units only. Declare all calibration and target-derived inputs. Use task-specific primary metrics and the same eligible cohort for matched comparisons. Report physical-unit errors, uncertainty, coverage, per-group/worst-group results, and event/interval diagnostics where defined. Whole-unit decisions retain assigned denominators when a method abstains.

Scoring groups may share a specimen, apparatus, session or environment. Do not turn repeated rows into independent replications or random row splits. Current scores cannot be called fresh confirmation. No unit conversion, constant target, leaked source fit or accounting identity becomes a new scientific law through prediction accuracy.

## Scientific review and dispositions

Use the [finding/evidence schema](reference/schemas/claims.schema.json) and [review rubric](reference/docs/REVIEW_RUBRIC.md). Review numerical validity, explanation, prior-art differentiation and practical value separately. Resolve substantive disagreements explicitly while retaining complementary reviewer scopes and original judgments.

Reproduction, validated extension, novelty candidate, falsification and justified abstention remain distinct. Independent computational review is not independent experimental replication. Novelty needs a documented priority assessment; industrial impact needs an operational decision and measured benefit. No aggregate discovery score or equation-match requirement is provided.

## Inputs, labels and execution

The corpus [input allowlist](INPUT_ALLOWLIST.json) describes source-aware discovery inputs. Registered tasks impose narrower permitted quantities, calibration and time windows. An archive hash does not permit arbitrary target fields. Reference predictions and research histories are exposed evaluation resources; disclose their use and never claim they were unseen.

Measured labels live under each task's `data/observations.csv.gz`; reference predictions are comparators, not measured truth. Case 8 supplies a bounded adequacy assessment. Prediction-file scoring executes no submitted code. Trusted replay explicitly executes local code without a security sandbox; declared lineage does not prove information independence.

The earlier [source-corpus protocol](SOURCE_EVALUATION_PROTOCOL.md) remains available as historical context. Its general scientific safeguards still apply; its pre-baseline release status is superseded by this version.
