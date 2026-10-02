# Round2 portability and frozen-reference audit

**Pass:** all 15 cases and all 180 historical reference models reproduce 1,353,974 predictions. Maximum absolute discrepancy is 2.14 × 10⁻¹³. No parameters were refitted.

105 additional checks pass: row-order invariance, target poisoning, unknown/duplicate OOF identity rejection, explicit deployment separation, isolated subprocess execution, and state corruption rejection before numerical-module import.

The runtime contains prediction functions and complete JSON state. Research-history loading is confined to the one-time migration tool, which is not copied into standalone packages. Source states, extraction lineage and local runtime hashes are recorded.

OOF prediction routes sample identity to an independently fitted fold model. The full-development state is separate and must be explicitly selected for deployment. It cannot substitute for the OOF scientific comparison. The initial preregistered round2 candidate remains the default reference; defaults do not imply admission or winner selection.

All historical observations are now exposed for future users. Computational parity does not establish scientific novelty, independent experimental replication or industrial impact.

Three additional declared predecessor-input fields are required: case 27 saturation temperature; case 61 membrane index; case 82 causal past measured temperature. Detailed model-by-model evidence and exact input unions are in `ROUND2_PORTABILITY.json`.
