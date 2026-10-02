# P100-097 exploration summary

The archive combines measured figure tables, simulation figure tables and illustrative videos from a pedestrian-foot-tracking study. The DAT files are MATLAB binaries. This task uses only the measured specific-volume/speed tables: the authors' F2D experiment and four external condition panels F3B–F3E. Simulation F3A and algebraically derived flow outcomes are excluded.

The article identifies external unidirectional, counterflow and multidirectional sources. The two panels attributed to the multidirectional study are reserved together; development uses the other three cohorts. Every tenth source row is retained by a fixed pre-fit index rule. Missing original person/run identifiers prevent individual-level or independent-population claims.

Five hypotheses compare finite-jam exclusion, exponential encounter slowdown, free-area saturation, geometric distance headway and a two-regime law. The development-selected free-area exponential reaches0.28514m/s reserved MAE, compared with0.24194m/s for the published source law and0.27568m/s for the flexible control. Its signed bias is+0.27346m/s and its worst-condition MAE is0.40587m/s.

The positive improvement claim is therefore rejected. The useful result is a traceable transfer limitation: a stronger development fit does not establish a better law across different crowd-flow conditions. Direction, geometry, source processing and participant dependence remain confounded. No evacuation-safety benefit or new universal crowd law is admitted.

| Model | Development MAE | Reserved MAE | Reserved worst-group MAE |
|---|---:|---:|---:|
| constant | 0.542255 | 0.350905 | 0.398428 |
| flexible | 0.148966 | 0.275681 | 0.385648 |
| published_source | 0.19236 | 0.241943 | 0.338439 |
| greenshields | 0.134612 | 0.300779 | 0.432625 |
| underwood | 0.139742 | 0.311701 | 0.470036 |
| free_area_exponential | 0.127172 | 0.28514 | 0.405867 |
| distance_headway | 0.13885 | 0.282015 | 0.402514 |
| two_regime_exclusion | 0.135308 | 0.288053 | 0.405161 |


## Attempt history

**attempt-001 — greenshields**: Attempt1: a finite-jam-density linear speed-density law represents crowd exclusion and predicts zero speed at an effective limiting density. Parameters are response descriptors, not safety thresholds. Development MAE=0.134612; worst group=0.191536; fitted parameters=2.

**attempt-002 — underwood**: Development evidence available before this fit: greenshields: MAE 0.134612, worst group 0.191536.

The finite-jam linear model improves the flexible control. Test a competing crowd-interaction mechanism: cumulative encounters reduce speed exponentially with density, without a finite hard jam point. Development MAE=0.139742; worst group=0.201068; fitted parameters=2.

**attempt-003 — free_area_exponential**: Development evidence available before this fit: greenshields: MAE 0.134612, worst group 0.191536; underwood: MAE 0.139742, worst group 0.201068.

Test available-area saturation in the source-paper model family, refitting only development cohorts. The excluded personal area and saturation rate have mechanistic interpretations but are not independently measured body dimensions. Development MAE=0.127172; worst group=0.186148; fitted parameters=3.

**attempt-004 — distance_headway**: Development evidence available before this fit: underwood: MAE 0.139742, worst group 0.201068; free_area_exponential: MAE 0.127172, worst group 0.186148.

Reconcile two-dimensional area with one-dimensional stepping clearance. Converting available area to a distance before applying a time-headway law is an independent geometric explanation. Development MAE=0.13885; worst group=0.195771; fitted parameters=3.

**attempt-005 — two_regime_exclusion**: Development evidence available before this fit: free_area_exponential: MAE 0.127172, worst group 0.186148; distance_headway: MAE 0.13885, worst group 0.195771.

Test explicit free-flow saturation followed by finite-jam crowd exclusion. A fitted onset density challenges the single linear slope and source exponential regimes; thresholds are descriptive rather than safety limits. Development MAE=0.135308; worst group=0.194621; fitted parameters=3.

All substantive attempts and failures are retained. See FREEZE.json and CONFIRMATION_RECEIPT.json for chronology and exact evidence binding.
