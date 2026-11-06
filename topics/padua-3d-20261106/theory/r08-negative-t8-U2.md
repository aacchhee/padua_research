# PD-N?padua-3d-20261106-codex-r08-T8-U2 — the frozen U2 optimizer fails its finite D2 screen

ID kind: PD-N.
Aliases: cyclic 2-coset union; independently translated common-H optimizer.
Split from: PD-T?padua-3d-20261106-codex-T8-r06-05, the finite failure of the named frozen rule documented below; the original measurements remain historical.
Split into: none. No final ID is allocated.

## Statement

The frozen U2 algorithm loses to Leja on the same 21^3 mesh at n=7 and 9, consecutive eligible tested degrees n>=6. It therefore meets its preregistered D2 kill. Eligibility is along the r-divisibility sequence and excludes rows with no certified interpolant; it does not mean consecutive integers in every case.

## Definitions

N=binom(n+3,3), Pi_n is the three-variable total-degree polynomial space on [-1,1]^3, and Lambda_q is the sampled interpolation Lebesgue function on the q^3 tensor Chebyshev–Lobatto mesh. Lambda_q is a floating lower sample, not an enclosure of the continuous norm. D2 is the frozen finite comparison rule in the linked preregistration.

## Assumptions

tested n=2,3,5,6,7,9; r=2; r divides N, common cyclic H of order M=N/r, independently translated rational cosets; 48 seeded starts, top two determinants and at most 200 Nelder–Mead evaluations; no quality-based selection

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Failure of the named frozen mechanism in the recorded finite screen | MEASURED | Preserved producer receipts, supplementary replays and independent audit; no status upgrade is made here |
| Universal singularity, asymptotic growth or whole-class impossibility | OPEN, outside statement | Neither mesh comparisons nor deficient modular ranks establish these conclusions |

Candidate / claim disposition: **REJECTED: failed** within the recorded operational gate.
Rejection reason: failed — the named finite algorithm did not meet its frozen cardinality, numerical-eligibility or quality requirement. This is a mechanism disposition, not rejection of an unresolved theorem.

## Negative-result scope

Attempted mechanism: U2 in preregistration-T8-round06.md.
Parameter range: tested n=2,3,5,6,7,9; r=2; r divides N, common cyclic H of order M=N/r, independently translated rational cosets; 48 seeded starts, top two determinants and at most 200 Nelder–Mead evaluations; no quality-based selection

## Depends on

[Preregistration](../preregistration-T8-round06.md), U2/U3/U4 and common D2; PD-T?padua-3d-20261106-codex-T8-r06-05 [measurements](t8-r06-measurements.md); PD-N?padua-3d-20261106-codex-T8-r06-03 [union parity](t8-r06-union-parity.md), used only for its exact no-fold common-even-order class.

## Checks

This response worker read the receipts and relevant checker/audit reports at rules/input head `9042e1c42964150f30fdbe8563c12ba6c6a8692a`; it did not rerun the optimizers or claim a new independent execution. Producer commands, environments, source/input hashes and raw identities are retained in the linked receipts. Round06 producer metadata: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. Independent audit03 used Python 3.13.18 and its own code; those are historical executed checks, not this worker's runs.

## Sources

IDEA-181/182 and PD-N034 are comparison predecessors, not unqualified impossibility premises. [Gate supplement](../novelty-gate-supplement-round08.md).

## Proof or evidence

| n | U2 Lambda_21 | Leja Lambda_21 |
|---:|---:|---:|
| 7 | 290.101684932329 | 49.812587823086 |
| 9 | 768.826300711809 | 84.458023998580 |

At n=6, the selected 84-node set has modular rank 82 at two primes. The separately PROVED common-half-period result gives the upper bound 82 for the stated no-fold class; no Lebesgue value was assigned there.

The canonical producer receipt is [t8-r06-union2.json](../evidence/t8-r06-union2.json). The supplementary replay is [independent-r06-t8-union2.json](../evidence/independent-r06-t8-union2.json); [audit03/T8](../audit-03/T8.md) separately reproduces the outcomes. Every defined quality output has exact N-node count and nonzero modular determinants at two verified splitting primes.

## Scope

This is a bounded-optimizer failure, not a universal assertion about cyclic unions or phases. Independently translated cosets leave PD-N034's fixed unshifted adjacent-mod4 hypothesis, but escaping that obstruction alone gives no quality estimate. Finite D2 losses do not disprove a polylogarithmic theorem for a different family.

D3: this is a frozen three-dimensional algorithm and comparison screen. It does not assert that every lattice/coset family fails, and does not exclude the two-dimensional Padua construction. Its n, N, prescribed search and comparator hypotheses are essential.

## Open items

U2 is not resumed by extending the same killed optimizer. A different folded phase class, unequal subgroup orders or mixed cyclic/noncyclic union needs an exact count/rank mechanism and a new prospective gate before an unseen quality run.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh, runtime model/effort not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Added under handoff08 E2/E6 in response to audit03 E2/E6 and novelty MJ3. This is a retrospective durable home for an already observed failure, not a prospective gate or a new run. Original pinned prose and receipts are unchanged.
