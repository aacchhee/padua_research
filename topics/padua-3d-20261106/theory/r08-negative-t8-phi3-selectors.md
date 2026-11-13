# PD-N?padua-3d-20261106-codex-r08-T8-Phi3-halfgrid — initial nearby-order half-grid selectors fail their frozen continuation

ID kind: PD-N.
Aliases: initial Phi3; N+s binary masks; generic nearby-order count.
Split from: PD-T?padua-3d-20261106-codex-T8-r06-05, the finite failure of the named frozen rule documented below; the original measurements remain historical.
Split into: none. No final ID is allocated.

## Statement

The initial half-grid selector has no exact N-node output for s=1,3,4 at n=2, and for s=2 at n=3. Its generic-phase diagnostics at those same pairs have M>N nodes and fail minimal cardinality. The selected s=2,n=2 output has a nonzero quadratic annihilator, so that particular count-correct output is not Pi_2-unisolvent. No statement excludes arbitrary continuous phases.

## Definitions

N=binom(n+3,3), Pi_n is the three-variable total-degree polynomial space on [-1,1]^3, and Lambda_q is the sampled interpolation Lebesgue function on the q^3 tensor Chebyshev–Lobatto mesh. Lambda_q is a floating lower sample, not an enclosure of the continuous norm. D2 is the frozen finite comparison rule in the linked preregistration.

## Assumptions

s1 at (n,M)=(2,11), s2 at (2,12) and (3,22), s3 at (2,13), s4 at (2,14); complete pair and binary-mask coverage at these degrees

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Failure of the named frozen mechanism in the recorded finite screen | MEASURED | Preserved producer receipts, supplementary replays and independent audit; no status upgrade is made here |
| Universal singularity, asymptotic growth or whole-class impossibility | OPEN, outside statement | Neither mesh comparisons nor deficient modular ranks establish these conclusions |

Candidate / claim disposition: **REJECTED: failed** within the recorded operational gate.
Rejection reason: failed — the named finite algorithm did not meet its frozen cardinality, numerical-eligibility or quality requirement. This is a mechanism disposition, not rejection of an unresolved theorem.

## Negative-result scope

Attempted mechanism: the four initial s=1,2,3,4 selectors, first-unit z=(1,b,c), 1<=b<c<M, phases h/(2M), h in {0,1}^3.
Parameter range: s1 at (n,M)=(2,11), s2 at (2,12) and (3,22), s3 at (2,13), s4 at (2,14); complete pair and binary-mask coverage at these degrees

## Depends on

[Initial Phi3 preregistration](../preregistration-T8-round06.md); [measurement record](t8-r06-measurements.md). The explicit quadratic is elementary; finite enumeration is retained at MEASURED here without a new status upgrade.

## Checks

This response worker read the receipts and relevant checker/audit reports at rules/input head `9042e1c42964150f30fdbe8563c12ba6c6a8692a`; it did not rerun the optimizers or claim a new independent execution. Producer commands, environments, source/input hashes and raw identities are retained in the linked receipts. Round06 producer metadata: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. Independent audit03 used Python 3.13.18 and its own code; those are historical executed checks, not this worker's runs.

## Sources

No external theorem is required. [Gate supplement](../novelty-gate-supplement-round08.md).

## Proof or evidence

| s | n | M | complete binary-mask candidates | exact-count passes |
|---:|---:|---:|---:|---:|
| 1 | 2 | 11 | 360 | 0 |
| 2 | 2 | 12 | 440 | 31 |
| 2 | 3 | 22 | 1680 | 0 |
| 3 | 2 | 13 | 528 | 0 |
| 4 | 2 | 14 | 624 | 0 |

At s2,n2 the selected z=(1,4,9), h=(0,0,1), denominator24 has y in {1,-1/2}; 2y^2-y-1 is an exact degree-2 annihilator. The two modular ranks 9 agree with this upper bound. This does not assert all 31 count-pass candidates are deficient. Evidence: [t8-r06-phi3.json](../evidence/t8-r06-phi3.json), [independent replay](../evidence/independent-r06-t8-phi3.json), [audit03/T8](../audit-03/T8.md).

## Scope

The M=2N-1 zero-mask diagnostics are inherited unshifted baselines, not a new failed phase family and not allocated a PD-N for equivalence. Its sampled high-degree deficient ranks alone do not establish singularity. The distinct Phi3b continuous-stratum continuation has its own theorem, scope and receipt; it is not a rescue of these half-grid selectors. Half-shifted M=2N is a separate handoff08 lead.

D3: this is a frozen three-dimensional algorithm and comparison screen. It does not assert that every lattice/coset family fails, and does not exclude the two-dimensional Padua construction. Its n, N, prescribed search and comparator hypotheses are essential.

## Open items

Retain arbitrary-phase rank questions and the separate Phi3b outcomes. Do not infer no M=2N construction from the coarse special-state grid; handoff08 assigns its half-shifted lead separately.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh, runtime model/effort not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Added under handoff08 E2/E6 in response to audit03 E2/E6 and novelty MJ3. This is a retrospective durable home for an already observed failure, not a prospective gate or a new run. Original pinned prose and receipts are unchanged.
