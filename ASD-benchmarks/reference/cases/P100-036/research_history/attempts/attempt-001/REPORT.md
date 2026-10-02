# Attempt 1

Cultivar/treatment design reaches MAE0.006253 and flexible imaging0.006065, versus constant0.010544. Test a reciprocal quenching coordinate1/(1+max(NPQ,0)) with cultivar offset, motivated by competing excitation-dissipation rates. QY_max and steady NPQ describe different measurement states, so failure would challenge applying a simple Stern-Volmer-like form across them; no rate constant is uniquely identified.

Initial post-baseline hypothesis

Primary group-balanced error: 0.005971382448357383. Previous incumbent: 0.00606506369992722. Gain>1%: True. Worst-group MAE: 0.03308320529549728.

Equation: sigmoid(b0+b1/(1+max(NPQ,0))+b2*tiny); r=Rfd/(1+abs(Rfd)), q=asinh(NPQ), size=ln(1+max(AREA_MM,0))/10

Full coefficients, fit bounds, fold states and native predictions accompany this report. Biological parameters are effective descriptors; shared fit does not establish a unique causal mechanism. Failed candidates remain evidence.
