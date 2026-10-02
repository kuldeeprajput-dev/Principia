# Evaluation protocol, version 3

## Identity and permitted information

The registry is authoritative. Resolve an explicit task ID for comparative experiments; a case-only ID is a navigation shortcut to its current default. Store the task, protocol, cohort, evaluator version and input/target hashes with every score. Never combine scores across different targets, calibration budgets or cohorts.

The task card names the target, physical units, prediction time, permitted predictors, independent experimental unit, chronology, calibration, native sources, selection rules and historical exposure. Source-row labels are alignment metadata. They cannot be used to recover exposed targets. Frozen calibration may legitimately depend on earlier observations if declared; future measurements cannot become present predictors.

`prepare` emits inputs, observations, native anchors, eligibility reasons, calibration records and group metadata. Learned calibrations are separately frozen with training scope. Native quality flags and exclusions remain traceable. The accompanying raw audit compares values and identifiers, not gzip-container encoding.

## Registered-task submission

Generate a working example, replace its predictions and scientific description, and update its asset hashes. See `schemas/submission.schema.json`. A native submission declares its exact task identity, used predictors, information budget, training/exposure history, equations, variables/units, findings, uncertainty convention, prediction file and any executable assets.

Every assigned sample ID must appear exactly once with its correct group. Use `status=predict` and a finite prediction, or `status=abstain` and a reason. Do not silently drop difficult rows. Missing targets are ineligible, not zero-valued outcomes. Numeric identifiers must remain strings. Signed physical targets remain in physical-unit scores; log metrics explicitly report positive-target eligibility.

Optional intervals use `lower`, `upper` and one declared interval level. Point predictions must lie within their intervals. Equal-width intervals remain together in risk–coverage diagnostics. The evaluator does not infer uncertainty from the number of dependent rows.

Version-1 JSON submissions are accepted through an explicit importer. Legacy round-two prediction CSVs can be converted using `evaluation/import_legacy.py`; these imports receive numerical-only results with unknown information-access/training status. Imported predictions do not invent a scientific equation or earn reference admission.

## Metrics and aggregation

The primary metric is frozen per task: group-balanced MAE, group-balanced RMSE, positive-target log error, configuration→particle transit error, or training-scale-normalized error. The shared implementation also reports physical MAE/RMSE/bias, error quantiles, group-level errors, worst-group error and comparisons against every registered comparator on exactly the same scored rows.

Configuration→particle weighting gives each configuration equal weight and each particle type equal weight within its configuration. Other tasks preserve their stated group hierarchy. Flattening rows changes the task and is not permitted.

Coverage includes assigned, eligible, predicted, scored and abstained counts and eligible group-weighted coverage. Partial-coverage performance must be read together with coverage. A method that abstains everywhere receives no numerical skill estimate.

Intervals receive coverage, width and proper interval score at the declared level. These are empirical properties of the exposed cohort. No precise population confidence interval is inferred from a few experimental groups.

Optional `--event-threshold VALUE` reports precision, recall, specificity, F1 and confusion counts for the event `target >= VALUE`, with the threshold in target units. CLI-selected thresholds are **exploratory**. An industrial or clinical threshold must have an external, source-bound meaning and be frozen in a distinct contract before confirmatory event evaluation. Comparator-derived tolerance accuracy is diagnostic only.

Evaluator v3 corrects F1 to `2 TP / (2 TP + FP + FN)`: complete failure has F1 zero when the denominator is positive. A zero denominator is undefined with a stated reason. Historical receipts are preserved unchanged.

Scientific checks include native timing/group invariants, permitted-input audits, relevant endpoint bounds and retained task-specific falsifiers. The machine reports which checks ran; a passing predictive score never silently substitutes for an unperformed mechanism or novelty test.

## Trusted replay and integrity

`validate` and `score` execute no submitted code. They validate schemas, hashes, paths, exact sample identities, units, feature declarations, numeric domains, intervals and abstentions. Training independence cannot be established merely from a submitter's declaration.

`replay --trust-code` stages declared files and predictors, omits inherited secrets, runs with a timeout and compares executable predictions to the submitted file. This is local trusted execution, not OS-level isolation. Do not enable it for untrusted code. Curated reference packages run without network access, historical research imports or implicit external state; OOF models use frozen fold states and cannot claim deployment on unknown IDs. Deployment state is separately identified.

## New findings and new tasks

An alternative model for an existing endpoint uses the existing task. A different measured endpoint, calibration budget or scientific test needs `proposal.json` and bound native evidence:

```sh
python evaluation/benchmark.py propose-task --proposal PROPOSAL_FOLDER --output NEW_REVIEW_FOLDER
```

A valid proposal enters `pending_independent_contract_review`; it does not overwrite a task or become scoreable. Review target semantics, availability, units, grouping, controls, exclusions, source-derived quantities and exposure, then freeze a new version plus adapter and tests. Native anchors and executable assertions are required for admission; source-fitted outputs are not independent measurements.

## Scientific review

Use `claims.json` under `schemas/claims.schema.json` to separate submitter claims from reviewer judgments. Positive claims need an executable expression/program, variables, units, applicability and evidence. Falsifications/abstentions need a tested proposition, negative evidence and limits without an invented positive equation.

```sh
python evaluation/benchmark.py review prepare --claims CLAIMS_FOLDER --output PACKET_FOLDER
python evaluation/benchmark.py review combine --packet PACKET_FOLDER/packet.json --reviews COMPUTATIONAL.json SCIENTIFIC.json --output COMBINED_FOLDER
```

The evidence packet binds the claim and every asset hash. Separate reviewers assess reliability, mechanism, novelty, significance, reproducibility and practical impact. Each dimension uses supported, partially_supported, unsupported or not_assessed, with evidence and rationale. Combining preserves disagreements and does not register a task or admit a discovery automatically.

The first 25 portfolio reviews are schema-preserving adaptations of separately completed agent computational and scientific-critical reviews. Later campaigns extend the same evidence-bound workflow to all 100 portfolios. Conversion records identify original review hashes; these reviews are not independent experiments, human expert adjudication or proof of scientific priority. New submissions require new reviews of their own exact evidence.

## ASD6 diagnostics and corrected contracts

Use CURRENT_TASKS.json and registry superseded_by notices to select current contracts. Seven v2 documentation corrections preserve scientific values and model states, without new confirmation. The evaluator identifies scenario, task, protocol, cohort and version in every report.

Case 89 uses equal-participant Brier score as primary loss. Group-weighted log loss and ten-bin reliability summaries are complementary. An exact zero probability assigned to an observed event has infinite log loss, recorded with an explicit reason; epsilon-clipped log loss is separately labeled diagnostic. The 0.5 classification threshold is a declared prediction convention, not an industrial acceptance threshold. Confusion counts and weighted rates have explicit denominators.

ASD6 diagnostics include physical-domain counts without silently clipping submitted predictions; causal timestamp ordering; learning-curve calibration/monotonicity; synaptic dose ordering; neuronal spike events; laser linear-density secondary error; and formulation-choice regret over complete three-formulation groups. Abstention removes incomplete decision groups and reports decision coverage. These checks supplement physical-unit prediction metrics; they do not certify causation or novelty.

## ASD7 completion and assessment contracts

The completed local collection contains 135 numerical task versions across 99 cases, plus one source-adequacy assessment. Tasks may use probability/Brier loss or signed-asinh error in addition to the physical-unit metrics above. A source sample weight normalizes within each complete group when `aggregation.within_group_weight` is declared; complete groups retain equal mass. This estimand must not silently become a national population estimate. Calibration records use explicit declared columns, including measured pilots and same-sample controls.

Probability extension `asd6-probability/1.1` corrects threshold provenance: an otherwise undeclared 0.5 threshold is a conventional descriptive diagnostic, not a preregistered event. A separately frozen threshold records its source and meaning. Point-error arithmetic is unchanged. Endpoint checks include Fréchet bounds for joint fluorescence percentages and the signed rotation domain; they do not automatically admit a mechanism.

Native future-prefix coverage appears explicitly in each numerical report. Finite source-file counterfactual tests, submitted-prediction replay, grouped preparation, and publisher preprocessing causality are different checks. Absence of a native-prefix receipt is reported rather than inferred as a pass.

Case 8 has one patient, single-echo images and no retained diagnostic labels, repeated echoes, registration truth or absolute signal calibration. Its five investigations therefore support an abstention, not a fabricated clinical endpoint:

```sh
python evaluation/benchmark.py assess --case P100-008 --data-root /path/to/local-datas --output NEW_ASSESSMENT
```

The assessment verifies the native inventory and reconstructs measurement metadata. It returns no prediction metric. A later proposal with a defensible measured endpoint must pass independent contract review before becoming comparable. This distinction is part of completing the scientific exploration, not evidence that every source must yield a positive discovery.


## Quality release, 2 October 2026

Evaluator3.1 preserves historical primary errors while correcting scope-aware review conflicts and case44 decision coverage. Every score verifies the evaluator manifest and records runtime/lock hashes. See EXTERNAL_AGENT_GUIDE.md for raw-access contracts and completed admission/registration, and REVIEW_RUBRIC.md for scientific judgments. The supplied reference baseline is **implemented by GPT-6 Astra**.
