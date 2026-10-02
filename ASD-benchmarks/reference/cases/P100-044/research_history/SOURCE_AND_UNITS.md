# Native optimization semantics

All 48 Schicker submissions, including failures, are retained: Flow MIP, Seidel linear and Seidel quadratic, each on the same 16 order/degree instances. Source-native summaries report Total Runtime as elapsed solver runtime; CPU Runtime is explicitly Gurobi WorkMeasure and is never treated as seconds. The task targets observed elapsed consumption capped at the common 7,200-second budget. It does not estimate uncensored solve time for unfinished jobs.

Before-run inputs are n, maximum degree, formulation identity and the dimensionless n/(1+degree^2) occupancy of the classical diameter-two Moore capacity. This last expression is a known graph-counting bound, not a discovered law. Model/variable counts are recorded after presolve and are excluded as possibly unavailable pre-run metadata. Objectives, bounds, source success flags, solution graphs and full trajectory timing are forbidden predictors.

All formulations of an instance remain together. The first15_3 Flow time series and summary were displayed during schema inspection, so that entire instance is forced into development. Remaining group allocation uses only identifiers. Source runtime values for other instances were not displayed before freeze. Runtime diversity is from structural problem variation, not independent machine repetitions.

Graph certificates may be inspected after the predictive campaign freeze as a separate reproduction check. Published best objectives and Moore bounds cannot be counted as new discoveries. The full source trajectory is preserved, including the missing solution graph for the time-limited linear50_4 run.
