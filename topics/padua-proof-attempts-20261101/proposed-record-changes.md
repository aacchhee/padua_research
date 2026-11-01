# Proposed changes to the programme-ideas records

These are exact literal replacements checked against refreshed upstream
`9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`. **They have not been applied.**
The proof/input base remains `cadb35066160e466cb1704b9791ad6f374446422`;
upstream changed during the parallel audit. A1 added the continuous-U convention
and B5 corrected the disconnected-domain route; both are already covered here.
The B5 old-text block below uses the refreshed route verbatim.
Apply only after the PR #6 audit and this topic's Claude audit; if either base
changes, reconcile the current bytes first. No final IDs or shared registry
changes are allocated here. Existing measured outputs retain their historical
status and provenance. The statements in this topic's new THEORY files carry
its proof claims, accepted by Claude audit-01; response-01.md disposes F1–F6.

## A1 — split the exact corner formula from the OPEN expansion

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md`

Old:

```text
| exact finite-sum form of Λ_c(n) (N closed-form kernel terms) | MEASURED | agreement with the O(Nn) formula to 2.1e-13, n = 3…64, all four corners (`t2_onepage.py/.out`); identity not written as a proof |
```

New:

```text
| exact finite-sum form of Λ_c(n) (N closed-form kernel terms) | PROVED | Split-off PD-T?proof-attempts-codex-01, `../../padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`: written proof for every n≥1 and all four corners, including continuous singular limits; exact SymPy checks n=1,…,6 and a separate rerun. The expansion itself remains OPEN. |
```

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md`

Old:

```text
## Depends on

None (finite evaluations only).
```

New:

```text
## Depends on

PD-T?proof-attempts-codex-01 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`) proves the exact finite corner identity only. The conjectured asymptotic expansion, its remainder and identification of κ remain OPEN; the existing finite evaluations and fitted constants retain MEASURED status.
```

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md`

Old:

```text
Split into: none.
```

New:

```text
Split into: PD-T?proof-attempts-codex-01 — exact finite-sum form of the corner value, for every n≥1 and all four corners. The asymptotic expansion remains in this record with OPEN status.
```

## B5 — add the generic complement without weakening the counterexample

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-N04-pattern-commutant-not-three-dimensional.md`

Old:

```text
Parameter range: the stated pattern convention; the counterexample is Padua n = 2. **Not covered:** generic node sets (where dimension 3 was measured; a genericity theorem is OPEN, `OPEN_TARGETS.md` B5); other orders or patterns.
```

New:

```text
Parameter range: the stated pattern convention; the counterexample is Padua n = 2. The universal claim remains refuted. Generic node sets are covered separately by PD-T?proof-attempts-codex-02 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md`): for every n≥2, distinct x coordinates imply the three-dimensional commutant, and this condition holds outside a proper real-algebraic subset. The structure on repeated-x strata is not classified.
```

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-N04-pattern-commutant-not-three-dimensional.md`

Old:

```text
Genericity of dimension 3 (B5 in `OPEN_TARGETS.md`); description of the commutant for Padua sets.
```

New:

```text
Genericity of dimension 3 is PROVED for every n≥2 by the split-off PD-T?proof-attempts-codex-02. Description of the commutant on repeated-x strata, including Padua sets, remains OPEN. The exact Padua n=2 counterexample in this record is unchanged.
```

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-N04-pattern-commutant-not-three-dimensional.md`

Old:

```text
PD-T?programme-ideas-claude-01 (definitions only).
```

New:

```text
PD-T?programme-ideas-claude-01 (definitions only). Complementary comparison, not a dependency of this negative proof: PD-T?proof-attempts-codex-02 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md`) proves the all-degree generic equality under distinct x coordinates.
```

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md`

Old:

```text
Related open target: genericity of the three-dimensional pattern commutant, `../OPEN_TARGETS.md` B5.
```

New:

```text
Related target B5 is closed separately by PD-T?proof-attempts-codex-02 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md`): for every n≥2 the pattern commutant is span{I,H_x,H_y} whenever the x coordinates are distinct, hence generically. The universal assertion remains false by PD-N?programme-ideas-claude-04. This comparison adds no dependency to the finite Favard proof.
```

## A5-partial — local obligations only

The maxima counts retain their MEASURED status. This supporting theorem proves
local conditions at exact representatives and their enclosures; the stored
floating iterates are not asserted to be exact zeros. The four other counting
obligations remain OPEN. Rigorous (D) corner and (E) edge-node certificates in
`t3_degenerate.py` also remain needed; obligation (2) is discharged for
`degenerate_max` only.

## Authoritative target-list status annotations (statements preserved)

File: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Old:

```text
Known: MEASURED agreement with the O(Nn) Lagrange formula to 2.1e-13 for n = 3…64, all corners (`checks/code/decisive/gen4-2/t2_onepage.py`). Done when: a written proof. Route: start from the Padua Lagrange formula L_B(x) = w_B(K_n(x, B) − T_n(x_1)T_n(B_1)) (Bos–Caliari–De Marchi–Vianello–Xu 2006; LITERATURE, to be checked at the theorem level), write the product-Chebyshev reproducing kernel K_n on the rhombus j + k ≤ n of cosine products, and sum it at a corner, where cos(aθ_c) = (±1)^a turns the four-fold cosine sum into a Dirichlet-type sum in θ_c + θ_j and φ_c + φ_k.
```

New:

```text
Known: MEASURED agreement with the O(Nn) Lagrange formula to 2.1e-13 for n = 3…64, all corners (`checks/code/decisive/gen4-2/t2_onepage.py`). Done when: a written proof. Route: start from the Padua Lagrange formula L_B(x) = w_B(K_n(x, B) − T_n(x_1)T_n(B_1)) (Bos–Caliari–De Marchi–Vianello–Xu 2006; LITERATURE, to be checked at the theorem level), write the product-Chebyshev reproducing kernel K_n on the rhombus j + k ≤ n of cosine products, and sum it at a corner, where cos(aθ_c) = (±1)^a turns the four-fold cosine sum into a Dirichlet-type sum in θ_c + θ_j and φ_c + φ_k.

Status update after audit: A1 is PROVED for every n≥1 and all four corners by PD-T?proof-attempts-codex-01 (`../padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`), with a written normalization/rhombus proof, exact SymPy n=1,…,6 regression and separate rerun. The previous 2.1e-13 observation remains historical MEASURED evidence. The precise statement above is unchanged. A2/A3 asymptotics and A4 corner argmax remain OPEN.
```

File: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Old:

```text
Known: MEASURED dimension 3 on random instances, n = 3..6 (`checks/code/adv/M2/m2_favard_commutant.py`); dimension 6 for exact Padua n = 2 (PD-N?…-04), so the exceptional set is non-empty. Done when: for each n in a stated range, one exact instance with dim 𝒞_y = 3 plus the semicontinuity argument; for all n, a structural proof. Route: (i) span{I, H_x, H_y} ⊂ 𝒞_y always (check that pattern(H_x) ⊂ pattern(H_y) in this order and that H_y commutes with H_x); (ii) [revised, response-02, audit-02 B4.7] real analyticity plus one witness is not enough on a parameter domain that may be disconnected. Instead express "dim 𝒞_y = 3" as the nonvanishing of a polynomial P in the nodes and weights: write H_x = D⁻¹ĤD with Ĥ the unnormalised (monic) recurrence matrix and D the diagonal of basis norms, so that [H_x, E] = 0 with E symmetric becomes the linear system [Ĥ, F] = 0, F = D²FᵀD⁻² for F = DED⁻¹, whose coefficients are rational in (nodes, weights) because D² is; check this reduction, clear denominators, and take P a suitable maximal minor. One exact witness then shows P ≢ 0, so dim 𝒞_y = 3 off a proper algebraic subset, which is nowhere dense on every connected component; (iii) produce one exact rational instance per n (n ≤ 6) with `padua_pattern_commutant.py` adapted to rational nodes.
```

New:

```text
Known: MEASURED dimension 3 on random instances, n = 3..6 (`checks/code/adv/M2/m2_favard_commutant.py`); dimension 6 for exact Padua n = 2 (PD-N?…-04), so the exceptional set is non-empty. Done when: for each n in a stated range, one exact instance with dim 𝒞_y = 3 plus the semicontinuity argument; for all n, a structural proof. Route: (i) span{I, H_x, H_y} ⊂ 𝒞_y always (check that pattern(H_x) ⊂ pattern(H_y) in this order and that H_y commutes with H_x); (ii) [revised, response-02, audit-02 B4.7] real analyticity plus one witness is not enough on a parameter domain that may be disconnected. Instead express "dim 𝒞_y = 3" as the nonvanishing of a polynomial P in the nodes and weights: write H_x = D⁻¹ĤD with Ĥ the unnormalised (monic) recurrence matrix and D the diagonal of basis norms, so that [H_x, E] = 0 with E symmetric becomes the linear system [Ĥ, F] = 0, F = D²FᵀD⁻² for F = DED⁻¹, whose coefficients are rational in (nodes, weights) because D² is; check this reduction, clear denominators, and take P a suitable maximal minor. One exact witness then shows P ≢ 0, so dim 𝒞_y = 3 off a proper algebraic subset, which is nowhere dense on every connected component; (iii) produce one exact rational instance per n (n ≤ 6) with `padua_pattern_commutant.py` adapted to rational nodes.

Status update after audit: B5 is PROVED for every n≥2 by PD-T?proof-attempts-codex-02 (`../padua-proof-attempts-20261101/theory/proof-attempts-codex-02-generic-commutant.md`). Distinct x coordinates suffice: the constant vector is cyclic for H_x and the first column of the H_y pattern has three entries. The collision discriminant defines a proper real-algebraic exceptional set; analytic dependence is proved directly. Exact rational LDL witnesses n=2,…,6 and a separate rerun check unisolvence, positive norms/pivots, pattern and commutation. Commutant dimension three follows from the all-n proof; the reduced-rank calculation is a consistency check, not an independent dimension test. The Padua n=2 dimension-six exception remains valid. The precise original generic statement above is unchanged.
```


File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`

Old:

```text
## Depends on

None.
```

New:

```text
## Depends on

The existing numerical candidate-count claim retains MEASURED status. Supporting local theorem: PD-T?proof-attempts-codex-03 (`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-03-degenerate-maxima.md`) proves exact identities, critical-point enclosures and rigorous local Hessian bounds for the two degree-3 exact representatives reconstructed from the recorded `degenerate_max` decisions. It does not prove search completeness or upgrade any count.
```

File: `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`

Old:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; valid identities (not tolerance tests) at the degenerate points, including the n = 3 edge case where a cardinal function was observed to vanish along the edge x = +1 (UNVERIFIED as an identity); rigorous root enclosures replacing the per-pattern Newton step; complete box-discard arguments; rigorous arithmetic; committed essential evidence; an independent rerun by a second checker.
```

New:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`; rigorous root enclosures/exclusions replacing the per-pattern Newton steps over every discarded region; complete sign-pattern box-discard arguments without the early return; exact treatment near regular crease crossings; rigorous arithmetic throughout and an independent checker. The separate `degenerate_max` local obligations have replacement certificates in PD-T?proof-attempts-codex-03 for the two degree-3 exact representatives, with Z={L_(2,2)}, background critical points at (theta,phi)=(0,acos(±1/sqrt(3))), rational angle enclosures of width 1e-18 and uniform Hessian margin greater than 3.5 on angle l1 discs of radius 0.0021. These discs rigorously contain the recorded radius-0.002 decision neighborhoods. The stored floating iterates themselves are not exact zeros. A fresh trace of every call for n=3,…,8 found two calls at n=3 and none at n=4,…,8; this trace remains MEASURED execution evidence. Obligation (2) is discharged for the `degenerate_max` path only; the (D) corner and (E) edge-node handlers remain explicit certification work. No maxima count is certified.
```

File: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Old:

```text
Known: the one degenerate cardinal function at n = 3 is now identified exactly: L_{(2,2)} (node (−½, 0)) = (x − 1)(2x² + x + 2y² − 2)/3, so it vanishes identically on the edge x = 1 and, in the angle variable θ (x = cos θ), to second order at θ = 0 (`checks/code/response-02/padua_n3_edge_identity.py/.out`, exact). Still needed: the list of all z_s and sets Z for n = 3…8 (from `t3_maxima.json` and the log), the corresponding identities, and an enclosure of the background critical point along the edge (evenness in θ gives ∂_θ = 0 at θ = 0; the φ-location needs an interval Newton or sign-change certificate). Done when: every degenerate decision of the n ≤ 8 runs is backed by an identity or enclosure. This is one of the five obligations of A5 below.
```

New:

```text
Known: the one degenerate cardinal function at n = 3 is now identified exactly: L_{(2,2)} (node (−½, 0)) = (x − 1)(2x² + x + 2y² − 2)/3, so it vanishes identically on the edge x = 1 and, in the angle variable θ (x = cos θ), to second order at θ = 0 (`checks/code/response-02/padua_n3_edge_identity.py/.out`, exact). Still needed: the list of all z_s and sets Z for n = 3…8 (from `t3_maxima.json` and the log), the corresponding identities, and an enclosure of the background critical point along the edge (evenness in θ gives ∂_θ = 0 at θ = 0; the φ-location needs an interval Newton or sign-change certificate). Done when: every degenerate decision of the n ≤ 8 runs is backed by an identity or enclosure. This is one of the five obligations of A5 below.

Status update after audit: PD-T?proof-attempts-codex-03 (`../padua-proof-attempts-20261101/theory/proof-attempts-codex-03-degenerate-maxima.md`) supplies exact local replacement certificates for the two degree-3 points (theta,phi)=(0,acos(±1/sqrt(3))) with Z={L_(2,2)}. The factorization is (x-1)(2x^2+x+2y^2-2)/3; both the cardinal value and angle gradient vanish at the exact representatives. The background gradient is exactly zero there, the angles have rational enclosures of width 1e-18, and exact rational interval bounds give a uniform margin greater than 3.5 on radius-0.0021 angle l1 discs covering both recorded radius-0.002 decision neighborhoods. Two separate n=3,…,8 instrumented executions found two calls at n=3 and none at n=4,…,8. That call coverage is MEASURED execution evidence; the theorem concerns the exact representatives and enclosed neighborhoods, not exact identities at the stored floating iterates. Obligation (2) is discharged for the `degenerate_max` path only. Rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`, as well as the four other A5 obligations, remain needed. Counts remain MEASURED.
```


## PR-preparation registry checklist (F5; deferred, not applied)

Line numbers below were checked at `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`;
use the stable IDs when upstream moves. Preserve the explicit no-shared-edit /
no-final-ID instruction for this stacked topic. Before applying this checklist,
refresh PR #6, PR #10 and the shared allocation ledger; do not reserve IDs here.

| Registry / current rows | Required integration |
|---|---|
| `state/IDEAS.md:493`, PD-N?programme-ideas-claude-04 | Replace the stale “genericity of dimension 3 OPEN” comparison with the all-degree generic result 02. Preserve the exact Padua counterexample and its PROVED status. |
| `state/IDEAS.md:481`, IDEA?programme-ideas-claude-17 | Link results 01 and 03. Keep the expansion and argmax OPEN, counts MEASURED, and corner/edge-node and other counting obligations unresolved. |
| `state/IDEAS.md:472`, IDEA?programme-ideas-claude-08 | Link result 02 as the generic complement; preserve the universal-claim rejection. |
| `PROOF_STATUS.md:94`, PD-T?programme-ideas-claude-04 | Record A1 → result 01, dependencies and completed audit. Keep the expansion OPEN and finite fits MEASURED. |
| `PROOF_STATUS.md:96`, PD-T?programme-ideas-claude-06 | Link result 03 as supporting local work, with the restricted obligation-(2) scope and remaining (D)/(E) certification. Keep counts MEASURED and completeness OPEN. |
| `PROOF_STATUS.md:100`, PD-N?programme-ideas-claude-04 | Add result 02 as a complementary comparison, not a dependency of the negative proof or a reversal of its disposition. |
| New `PROOF_STATUS.md` rows | Add PD-T?proof-attempts-codex-01/-02/-03, all PROVED within their exact statements, links to these theory records, Claude audit-01 and response-01. No count/argmax/asymptotic upgrade. |
| `ID_CROSSWALK.md:311,313,317` | Update the source-record cross references for programme-ideas -04/-06/-N04 and the completed audit; preserve all existing IDs and mappings. |
| New `ID_CROSSWALK.md` rows and split mapping | Add all three provisional result IDs and their durable paths. Explicit original-to-split mapping: PD-T?programme-ideas-claude-04's exact finite corner identity → PD-T?proof-attempts-codex-01; its asymptotic expansion stays OPEN. Record B5/result 02 as the positive generic complement and A5-partial/result 03 as supporting local work. |

Apply the source edits and this registry checklist together in a later authorized
integration pass, after reconciling PR #6. Audit-01 accepts the three proofs;
no new scientific claim, registry write or allocation is made by this checklist.
