# Complaint workload: a two-timescale reporting reference

A compact blend of recent and slower reporting histories improves reserved-month complaint-count prediction over matched simple and flexible controls. It predicts administrative workload within known vehicle groups, not defect risk or mechanical reliability.

## Data and evaluation

NHTSA2025–2026 public vehicle complaints are deduplicated byODINO andmake/model across componentrecords. The434vehicle cohorts have at leastsix received complaints inJan–Jun2025, fixedbeforealltargetmonths. DevelopmentJul2025–Apr2026 uses4340cohort-monthrows; confirmationMay–Jul2026 uses1302rows inthreecomplete months. Zero counts retained.

Target: **Next-month unique received vehicle complaints per known make/model**, measured as complaints/month. Primary error: complaints/month. Only prior-month LDATE received counts predict next month. Retrospective snapshot may revise product labels and records; historical DATEA/report publication lag means calendar causality is not verified as-issued availability. No incident-date future information used.

Whole target months; same known vehicle cohorts repeat, lag windows overlap. Three held months are not independent fleets or defect experiments. Cohort selected before targetperiod using>=6receivedJan–Jun2025complaints. Development targetsJul2025–Apr2026, rolling forward blocks; May–Jul2026confirmation. No target-month counts enter predictors.

## Findings and equations

**P100-019-F01 — validated_extension (partially_supported).** A compact two-timescale reporting-history blend improves mean reserved-month count error over the frozen matched controls.

count_hat=L3+a(L1-L3)+b(L3-L6),withnonnegativeclipping.

Recent observations and a slow historical level capture persistence with transient reporting variation. The final weights are approximatelyconvex, but their mechanism and crossperiodstability are notidentified.

Falsifying evidence and limits: Onlythreeheldmonths, knowncohorts and retrospectivelyrevised labels. Other unselectedstatescanbetterthisparticularconfirmation; no industrialcostbenefitdemonstrated.

**P100-019-F02 — informative_falsification (supported).** The campaign doesnot identify a unique nonlinear reporting-burst law or a vehicle defect-rate relationship.

Asymmetric003,variance-stabilized004/005 androbust006 remaintraceable.

Square-root stabilization modestlyimproves developmentmean butdoesnot displace simpler002underpredeclared1percentcomplexityrule.

Falsifying evidence and limits: No population vehicleexposure,verifiedfailuretarget or causal recallintervention. A complaint count is not failureprobability.

Selected executable model: `attempt_002`. Let L1 be lastmonth count and L3,L6 trailingthree/sixmonthly means. Selected count_hat=clip[L3+a(L1-L3)+b(L3-L6),0,1e8], a=0.5971048228619386, b=-0.36844397185306554. The final fitted form equals approximately0.5971L1+0.03445L3+0.36844L6. These are fitted descriptive memoryweights, not a universal reporting or failure-rate kernel.

All coefficients, input definitions, training groups and transformations are in `rules.json`; the runnable reference performs no fitting.

## Compact numerical evidence

Errors are computed within declared complete groups (with final survey weights when supplied), then averaged equally across groups.

| Frozen model | Development error | Confirmation error | Worst confirmation group |
|---|---:|---:|---:|
| reference | 3.955552 | 3.511835 | 3.742832 |
| constant | 15.9496 | 15.64825 | 15.75912 |
| flexible | 6.647887 | 3.77217 | 3.943177 |
| persistence | 4.302995 | 3.652842 | 3.868664 |
| trailing3 | 4.159498 | 3.769585 | 4.012289 |
| trailing6 | 4.398105 | 4.075269 | 4.324117 |

Confirmation contains 1302 scored observations in 3 groups. Individual-group scores and every attempted model remain available. Confirmation MAE3.511835complaints pervehicle/month versuspersistence3.652842,trailing3=3.769585,trailing6=4.075269,flexible3.772170 andconstant15.648246. Worstheldmonth3.742832. Several morecomplex unselectedattempts scorebetter retrospectively; they remain unselected. Three adjacent months do not justify narrow population confidence intervals.

## Interpretation, limitations and use

Administrative complaint workload among known productVmake/model labels, not vehicle failures or safety risk. No fleet-at-risk denominator, reporting propensity or causal recall effect; dedupODINO/vehicle across components, snapshot relabeling remains. Whole-group errors/ranges; no row bootstrap or manufactured independent-population confidence. Confirmation becomes exposed after freeze.

Useful for comparing simple interpretable administrative workload forecasts under whole-month validation. The data have no vehicle fleet-at-risk denominator or measured defect incidence. Reporting propensity and revised productlabels prevent causal recall or reliability conclusions; actual staffing/industrial savings were not tested.

## Reproducibility and prior art

Run `python run.py` to verify hashes and replay every frozen equation. Predictions use declared input columns only. The shared benchmark evaluator can score alternative equations under the same task; numerical agreement with these coefficients is not required. Public source-aware confirmation is now exposed. No independent experimental replication or certified novelty is claimed.

- [Complaints identify potential issues together with other sources, not verified incidence. NativeCMPLdocumentation defines received date and duplicateODINOcomponents; autoregressive reporting processes are existing baseline families.](https://www.nhtsa.gov/nhtsa-datasets-and-apis) (checked 2026-10-02).
