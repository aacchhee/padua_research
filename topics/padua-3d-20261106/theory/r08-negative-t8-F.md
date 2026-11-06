# PD-N?padua-3d-20261106-codex-r08-T8-F — the frozen determinant optimizer F fails its finite D2 screen

ID kind: PD-N.
Aliases: Phi2; F; determinant-only M=N optimizer.
Split from: measured failure components of PD-T?padua-3d-20261106-codex-T8-r06-05 or T10-02, as identified below; the original measurements remain historical.
Split into: none. No final ID is allocated.

## Statement

For the frozen F outputs at n=7 and n=8, Lambda_21 is respectively 335.945252452707 and 727.556759689502, exceeding the same-degree Leja controls 49.812587823086 and 79.821346686799. These are consecutive tested parity-permitted n>=6, so the preregistered D2 kill fires. At n=4 the QR loss had already removed promising status. The negative statement concerns this seeded, bounded optimizer, not existence of a better phase or generator.

## Definitions

N=binom(n+3,3), Pi_n is the three-variable total-degree polynomial space on [-1,1]^3, and Lambda_q is the sampled interpolation Lebesgue function on the q^3 tensor Chebyshev–Lobatto mesh. Lambda_q is a floating lower sample, not an enclosure of the continuous norm. D2 is the frozen finite comparison rule in the linked preregistration.

## Assumptions

n=3,4,5,7,8; M=N; first-unit primitive cyclic generator; 64 seeded draws, top three determinants and at most 250 Nelder–Mead evaluations per finalist; rational phase denominator 65521

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Failure of the named frozen mechanism in the recorded finite screen | MEASURED | Preserved producer receipts, supplementary replays and independent audit; no status upgrade is made here |
| Universal singularity, asymptotic growth or whole-class impossibility | OPEN, outside statement | Neither mesh comparisons nor deficient modular ranks establish these conclusions |

Candidate / claim disposition: **REJECTED: failed** within the recorded operational gate.
Rejection reason: failed — the named finite algorithm did not meet its frozen cardinality, numerical-eligibility or quality requirement. This is a mechanism disposition, not rejection of an unresolved theorem.

## Negative-result scope

Attempted mechanism: Phi2 F in preregistration-T8-round06.md, candidate alias IDEA?padua-3d-20261106-codex-T8-r06-F.
Parameter range: n=3,4,5,7,8; M=N; first-unit primitive cyclic generator; 64 seeded draws, top three determinants and at most 250 Nelder–Mead evaluations per finalist; rational phase denominator 65521

## Depends on

[Preregistration](../preregistration-T8-round06.md), Phi2 and common D2; [measurement record](t8-r06-measurements.md), PD-T?padua-3d-20261106-codex-T8-r06-05; exact certificate reduction PD-T?padua-3d-20261106-codex-T8-r06-04 in [certification](t8-r06-certification.md).

## Checks

This response worker read the receipts and relevant checker/audit reports at rules/input head `9042e1c42964150f30fdbe8563c12ba6c6a8692a`; it did not rerun the optimizers or claim a new independent execution. Producer commands, environments, source/input hashes and raw identities are retained in the linked receipts. Round06 producer metadata: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. Independent audit03 used Python 3.13.18 and its own code; those are historical executed checks, not this worker's runs.

## Sources

No external theorem is load-bearing. Predecessor and reading coverage: [round08 gate supplement](../novelty-gate-supplement-round08.md).

## Proof or evidence

[t8-r06-phi2.json](../evidence/t8-r06-phi2.json) contains all five selected outputs and the explicit kill field. Lambda_21 at n=3,4,5 is 19.793888,54.028747,71.879058. All five selected sets have exactly N nodes and two full-rank modular certificates; the loss is quality, not rank. F at n=9,11,12 was not run after the kill. [Independent T8 replay](../evidence/independent-r06-t8-phi2.json) and [audit03/T8](../audit-03/T8.md) reproduce the finite outcomes.

## Scope

No six-row growth conclusion is available: only four n>=4 rows were measured. The broad continuous M=N cosine-orbit target remains OPEN. The earlier necessary parity theorem and finite positive witnesses are separate results.

D3: this is a frozen three-dimensional algorithm and comparison screen. It does not assert that every lattice/coset family fails, and does not exclude the two-dimensional Padua construction. Its n, N, prescribed search and comparator hypotheses are essential.

## Open items

Do not rerun F as a rescued rule. Resume only with a separately gated and prospectively frozen mechanism that differs mathematically or algorithmically, not a best-of-degrees splice; its counterexample screen must precede further quality degrees.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh, runtime model/effort not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Added under handoff08 E2/E6 in response to audit03 E2/E6 and novelty MJ3. This is a retrospective durable home for an already observed failure, not a prospective gate or a new run. Original pinned prose and receipts are unchanged.
