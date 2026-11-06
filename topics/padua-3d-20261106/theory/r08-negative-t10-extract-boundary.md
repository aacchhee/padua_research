# PD-N?padua-3d-20261106-codex-r08-T10-extract-boundary — the frozen boundary-priority extraction fails numerical eligibility

ID kind: PD-N.
Aliases: T10-02; extract-boundary; delete innermost layer first.
Split from: measured failure components of PD-T?padua-3d-20261106-codex-T8-r06-05 or T10-02, as identified below; the original measurements remain historical.
Split into: none. No final ID is allocated.

## Statement

At n2 the frozen structured rule is eligible but loses to global QR (Lambda_41 8.749156358 versus7). At every tested n3..16 it is numerically ineligible, with no valid interpolation Lebesgue value assigned. It therefore fails the prescribed extraction mechanism; jointly with restricted QR's n6/n7 losses the operational extraction kill was met.

## Definitions

N=binom(n+3,3), Pi_n is the three-variable total-degree polynomial space on [-1,1]^3, and Lambda_q is the sampled interpolation Lebesgue function on the q^3 tensor Chebyshev–Lobatto mesh. Lambda_q is a floating lower sample, not an enclosure of the continuous norm. D2 is the frozen finite comparison rule in the linked preregistration.

## Assumptions

n2..16; original n2..7 run and unchanged post-kill n8..16 run; condition>=1e12 or reproduction residual>1e-7 suppresses interpolation quality

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Failure of the named frozen mechanism in the recorded finite screen | MEASURED | Preserved producer receipts, supplementary replays and independent audit; no status upgrade is made here |
| Universal singularity, asymptotic growth or whole-class impossibility | OPEN, outside statement | Neither mesh comparisons nor deficient modular ranks establish these conclusions |

Candidate / claim disposition: **REJECTED: failed** within the recorded operational gate.
Rejection reason: failed — the named finite algorithm did not meet its frozen cardinality, numerical-eligibility or quality requirement. This is a mechanism disposition, not rejection of an unresolved theorem.

## Negative-result scope

Attempted mechanism: the structured extraction retaining N nodes by boundary-coordinate count descending, then folded integer lexicographic order, with no rank repair.
Parameter range: n2..16; original n2..7 run and unchanged post-kill n8..16 run; condition>=1e12 or reproduction residual>1e-7 suppresses interpolation quality

## Depends on

[Preregistration-T10](../preregistration-T10.md), item3 (original rule); [t10-quality.json](../evidence/t10-quality.json); [t10-extraction.json](../evidence/t10-extraction.json); PD-T?padua-3d-20261106-codex-T10-02 [quality](t10-quality.md); PD-T?padua-3d-20261106-codex-T10-09 [finite extraction](t10-extraction-complete.md).

## Checks

This response worker read the receipts and relevant checker/audit reports at rules/input head `9042e1c42964150f30fdbe8563c12ba6c6a8692a`; it did not rerun the optimizers or claim a new independent execution. Producer commands, environments, source/input hashes and raw identities are retained in the linked receipts. Round06 producer metadata: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. Independent audit03 used Python 3.13.18 and its own code; those are historical executed checks, not this worker's runs.

## Sources

No external theorem is needed. The finite-screen PD-N precedents are PD-N?padua-3d-20261106-codex-T4-02 and PD-N?padua-3d-20261106-codex-T8-03; [gate supplement](../novelty-gate-supplement-round08.md).

## Proof or evidence

The original receipt explicitly records `extraction_kill.degrees=[6,7]`. At n6/n7, inherited QR Lambda_41 is22.42092675/27.56215199, versus restricted-QR30.49906208/38.84271526. The boundary rule is numerically ineligible there (condition about4.773e16/9.964e18), not proved singular. The subsequent unchanged n8..16 pass is **disclosed post-kill verification**, not revival. Against inherited QR on mesh41, n8 has45.45825696 versus45.53579545; on mesh21 it loses44.36601607 versus43.88676861. [Audit03/T10](../audit-03/T10.md) additionally compares the same lexicographic-basis global QR ordering:35.816 versus45.458 for restricted QR on mesh41. Floating pivot ties depend on basis/node order; the different inherited ordering cannot establish a robust n8 advantage. n9..16 restricted QR loses again on mesh41. Historical receipts' “no universal/continuous-norm kill” remains a limit on mathematical quantifiers; their wording does not undo the operational n6/7 kill.

The audit independently tested structured modular ranks at n3..8:17/20,34/35,51/56,79/84,111/120,155/165. Deficient reductions do not certify characteristic-zero deficiency; these checks are evidence only.

## Scope

No exact singularity theorem is asserted at n3..16, and no continuous-norm comparison is assigned to an invalid numerical solve. The historical phrase “singular structured sets fail” is read here as operational numerical failure; exact singularity remains OPEN. Post-kill diagnostics do not revive the rule.

D3: this is a frozen three-dimensional algorithm and comparison screen. It does not assert that every lattice/coset family fails, and does not exclude the two-dimensional Padua construction. Its n, N, prescribed search and comparator hypotheses are essential.

## Open items

An exact null-polynomial certificate would settle singularity of a specified selected set, but is not needed to preserve this measured numerical failure. A repaired or different extraction is a new prospective candidate; no rank-repair fallback belongs to this frozen rule.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh, runtime model/effort not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Added under handoff08 E2/E6 in response to audit03 E2/E6 and novelty MJ3. This is a retrospective durable home for an already observed failure, not a prospective gate or a new run. Original pinned prose and receipts are unchanged.
