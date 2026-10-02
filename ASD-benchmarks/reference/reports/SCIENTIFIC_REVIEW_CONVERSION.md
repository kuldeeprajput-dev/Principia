# Scientific review conversion audit

**PASS — 25 portfolios, 69 findings and 366 evidence-asset bindings checked.**

The common review packets preserve the scientific reviewer’s finding statements, dispositions, six dimension judgments, adverse evidence, falsifiers, equations and source bindings. Claims remain distinct from reviewer judgments. The combined records preserve both roles and their scope disagreements without an aggregate score.

## Corrected classification mapping

The initial fallback confused support for a negative conclusion with support for a predictor. It has been corrected: supported negative findings are `falsified`, with their source classification retained; measurement audits are `metrology_correction`. All 69 claims retain `source_classification`.

| Original class | Common class | Findings |
|---|---|---:|
| measurement_audit | metrology_correction | 3 |
| numerical_control | predictive_reference | 16 |
| reproduction | reproduction | 9 |
| retrospective_extension | predictive_reference | 16 |
| unsupported_or_falsified | falsified | 17 |
| validated_extension | validated_extension | 8 |

## Verification and limits

- Original finding identities and inventories are unchanged
- Statements, scientific dispositions, all six dimension judgments, adverse evidence and falsifiers are unchanged
- Original classifications are retained and explicit canonical mappings do not turn negative findings into positive predictors
- Claims contain no reviewer dimensions or reviewer disposition fields
- Claim, scientific and computational reviews bind to the exact claim/evidence hashes
- Every copied evidence asset has matching bytes and SHA-256; all finding and dimension references resolve
- Combined review preserves both role judgments and their disagreement inventory
- All current outcomes are exposed; no automatic scientific admission, novelty certification or aggregate score
- Existing equations are unchanged; missing inline equations use explicit evidence-bound records without invented equations
- Historically reserved PLA challenge provenance remains available in the byte-identical bound scientific assessment

The 54 directly linked findings have registered numerical task references. The other 15 historical first-continuation claims have no one-to-one task mapping in these packets and retain `not_assessed` computational reliability/reproducibility. This is a conservative documentation boundary, not evidence that those claims are false.

Evidence-bound equation records do not invent positive equations and are not independently executable. Executable task packages and their parity results are assessed separately. The original scientific review, copied byte for byte and hash-bound, preserves the detailed numeric outcomes and historical validation descriptions.

The PLA challenge’s original freeze/reservation history remains distinct from its present exposed status. The four PLA material/response task links and optional BikeZ corrected-interval link were rechecked against target, units, calibration and source scope. The optional BikeZ supplemental evidence remains separate and excluded from public export pending data redistribution evidence. No new literature search, scientific fit, experimental replication or novelty certification was performed for this conversion audit.

Per-packet hashes, scope counts and all check outcomes are recorded in `SCIENTIFIC_REVIEW_CONVERSION.json`.
