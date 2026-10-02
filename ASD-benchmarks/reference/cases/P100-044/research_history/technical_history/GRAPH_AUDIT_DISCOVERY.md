# Preserved diagnostic failure

An independent post-freeze graph audit initially asserted BFS diameter equals reported MIP objective. It failed on two source graphs: linear topology40_6 has BFS3 versus reported12; quadratic has BFS4 versus reported5. Source ZIMPL constraints bound an auxiliary diameter from below; an unfinished feasible solution need not tighten it. The audit now separately tests degree feasibility and D_graph<=D_MIP, preserving both values. No runtime targets, models, splits or confirmation receipts changed. This is an exposed-source diagnostic finding.
