# P100-100.round2.v2

Documentation correction of P100-100.round2.v1. Native values, coefficients, grouping and numerical evidence are unchanged. No new fitting or confirmation.

**Target.** Next successful ICMP round-trip time

**Target units.** ms

**Metric kind.** mae

**Timing contract.** Predict next probe RTT using only five previous completed RTTs and radio asof previous completion, <=0.5s old. No current response-completion timestamp, ICMPseq, cumulative average/loss, future gap, throughput or same-probe radio in inputs. Successful response conditional target; missing lost responses retained when inputs eligible. Expanded information budget: payload_B, last_rtt, mean5_rtt, mean3_rtt, trend_rtt, RSRP, RSRQ, last2_rtt, last3_rtt, median5_rtt, std5_rtt, route

**Calibration.** The previous five completed RTTs and causal radio observations constitute permitted online history; no response from the currently predicted probe is a calibration input. The preregistered parity-filter reference has no fitted coefficients and uses rhat=max(0,(3*last2+10*mean5-3*last-3*last3)/7). Other model coefficients, route offsets and transformations are fitted in their applicable outer training runs. The original55ms-breakpoint coefficients describe a separate historical comparator, not the current reference or a universal task calibration.

**Independent unit.** Whole PING run;6 original-development runs from3calibrated routes contribute5965 assigned and5938 measured-RTT observations. Sequential probes are dependent and all runs share one platform.

**Scope limits.** Repeatedly exposed development OOF cohort of6complete PING runs, distinct from the original3reserved runs. Task predicts conditional successful-response RTT using declared causal history;27assigned responses have no observed RTT and remain missing. No new-network, packet-loss reliability, scheduler identification or queue-mechanism claim is established.

## Permitted inputs

| Input | Units |
|---|---|
| payload_B | B |
| last_rtt | ms,previous completion |
| mean5_rtt | ms,previous5 completions |
| mean3_rtt | ms,previous3 completions |
| trend_rtt | ms,previous RTT difference |
| RSRP | dBm,asof previouscompletion |
| RSRQ | dB,asof previouscompletion |
| last2_rtt | ms; second previous completed RTT |
| last3_rtt | ms; third previous completed RTT |
| median5_rtt | ms; median of preceding 5 completed RTTs |
| std5_rtt | ms; SD of preceding 5 completed RTTs |
| route | calibrated route label |

Current outcomes are exposed. Alternatives may use the same information budget; different endpoints require a distinct reviewed contract.
