# Supplementary independent checks

Required Claude audit: **PENDING**. Independent Codex subagent checks supplement it.

## A2

- Independent mathematical reconstruction: `/root/a2_independent_route`, requested gpt-6.1-sol xhigh. Read/reconstructed every section of comparison theory04 and independently supplied the elementary one-dimensional asymptotic. Hash-pinned scope and limitations: [independent-checks-a2.md](independent-checks-a2.md). No executed mathematical computation is claimed by that agent.
- Actual independent executions: `/root/input_manifest`, requested gpt-6.1-sol medium, independently ran code/a2_exact_check.py and code/a2_sanity.py into outputs/a2_exact_independent.json and outputs/a2_sanity_independent.json. Both exit0 and are byte-identical to developer outputs. Exact regression:83 kernel terms across n1…6, endpoint/positive-sum/square identities. Diagnostic:67 degrees2…64 plus128,256,512,1024; MEASURED only. Exact commands, code/output identities, versions and scope: [independent-execution-a2.md](independent-execution-a2.md).
- Root inspected the complete analytic proof files and both scripts/receipts. No numerical fit supplies the proof. The theoretical claims have written all-n proofs; these finite diagnostics do not certify unrelated targets.

## A5 / A4(a) / B3 / B1

Not yet submitted for independent execution. Every consequential exact/interval computation needs a different subagent's actual replay and own output. A5 also requires a separate checker that verifies the produced certificate without rerunning the search.
