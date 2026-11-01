# Proposed upstream record changes — literal old → new blocks

No proposal below is applied to another topic, an existing registry or a final ID.
All original blocks are checked against the full pinned commit specified for the block.
Apply only after the independent Claude audit accepts the relevant Part2 claim and AC authorizes integration.
This is a future application condition, not a request to pause authorized development.
The original routes, source coverage, measurements and unresolved stronger statements are retained.

Initial Part1 head: `a09d910ae7d5526b1e216066421a0bee7fc20da4`.
Programme source pin: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`.
Part1 audit arrived: `95279b833bca5967fcf47c1b71a56ff622185b4e`; impact and merge recorded in LOG.
No Part1 audit finding is fixed by editing Part1 files here.

## A2 proposal 1

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Known: Kolomoitsev–Lomako 2021, Thm 2.1 (LITERATURE, primary excerpt checked by the audit) gives the leading term (4/π²) log² n with an O(log n) remainder for the **global** Padua Lebesgue constant Λ(Pad_n) = max λ_n, not for the corner value; since Λ_c(n) ≤ Λ(Pad_n) it yields only Λ_c(n) ≤ (4/π²) log² n + O(log n). The matching lower bound for Λ_c (the corner leading term) is part of this target, unless A4 is proved first (response-02, audit-02 B4.5); the fitted b agrees with (8/π²)(γ + log(8/π)) only within a post-registration model (pre-registered fit uncertainty is too coarse to separate it, PD-T?…-04). Done when: a proof of the b-term with an explicit O(1) bound. Route: with A1, Λ_c(n) is a Riemann sum of |D_n| over a sheared lattice on the torus; split D_n into the U_{n+1}U_{n+1} and U_nU_n parts, compare with the product of two 1-D Chebyshev Lebesgue sums (each contributing (2/π) log n + c₁), and control the cross terms; Kolomoitsev–Lomako's discretisation lemma is the template (read the full paper first).
```

New:

```text
Known: Kolomoitsev–Lomako 2021, Thm 2.1 (LITERATURE, primary excerpt checked by the audit) gives the leading term (4/π²) log² n with an O(log n) remainder for the **global** Padua Lebesgue constant Λ(Pad_n) = max λ_n, not for the corner value; since Λ_c(n) ≤ Λ(Pad_n) it yields only Λ_c(n) ≤ (4/π²) log² n + O(log n). The matching lower bound for Λ_c (the corner leading term) is part of this target, unless A4 is proved first (response-02, audit-02 B4.5); the fitted b agrees with (8/π²)(γ + log(8/π)) only within a post-registration model (pre-registered fit uncertainty is too coarse to separate it, PD-T?…-04). Done when: a proof of the b-term with an explicit O(1) bound. Route: with A1, Λ_c(n) is a Riemann sum of |D_n| over a sheared lattice on the torus; split D_n into the U_{n+1}U_{n+1} and U_nU_n parts, compare with the product of two 1-D Chebyshev Lebesgue sums (each contributing (2/π) log n + c₁), and control the cross terms; Kolomoitsev–Lomako's discretisation lemma is the template (read the full paper first).

Status update proposed after the Part2 Claude audit: A2(i)–(iii) are PROVED in `PD-T?proof-attempts-2-codex-01`, `-02`, `-03`, with separate supporting comparison `-04`. For every n≥2, Λ_c(n)≥(4/π²)log²n−54, the absolute leading-term error is at most95log n, and the absolute remainder after the stated b log n is at most68. These are written analytic proofs; finite exact regressions and independent reruns are supplementary. Dependency: `PD-T?proof-attempts-codex-01 (audit pending)`; its Claude audit-01 at95279b8 accepted A1; response-01 at7b8884a completed the minor dispositions. The full A3 expansion and global A4 remain OPEN. This update does not replace the original statement, source coverage or proposed route above.
```

Validation: old block occurs exactly once in the pinned source; statement and route/history retained.

## A2 proposal 2

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
| the conjectured expansion itself | OPEN | needs an analytic proof or rigorous remainder control |
```

New:

```text
| weaker A2 substatement: (4/π²)log²n+b log n+O(1), b as stated | PROVED | Separate local result `PD-T?proof-attempts-2-codex-03`: explicit absolute remainder68 for every n≥2; supporting comparison -04; required Part2 Claude audit must be complete before applying this proposal. Full A3 remains OPEN. |
| the conjectured expansion itself | OPEN | needs an analytic proof or rigorous remainder control |
```

Validation: old block occurs exactly once in the pinned source; statement and route/history retained.

## PR-preparation registry checklist (proposals only)

After audit and at the authorized integration step, update the programme IDEA-17 summary, PROOF_STATUS rows for source theory04, and ID_CROSSWALK's original-to-split mapping from programme04 to the Part2 A2 result03/support04. Add rows for local results01–04 without allocating final IDs in this branch. Preserve source04's full A3 OPEN status and source05 global argmax OPEN status. The earlier Part1 proposals and their F1–F6 dispositions are separate upstream work; do not overwrite them.

Finite A5/A4 case proposals below reflect actual certified results. No n6/7/8 published-table correction is proposed until its own certification.

## A5 n3, n4 and n5 status

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.
```

New:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.

Status update proposed after the Part2 Claude audit: n=3,4,5 are PROVED by `PD-T?proof-attempts-2-codex-06`, `-10`, `-16`: respectively15=7interior+6edge+2corner,27=13interior+12edge+2corner,25=14interior+9edge+2corner. Separate exact certificates, independent verifiers and actual different-agent producer/global/checker executions discharge all five obligations for these new procedures. Their direct physical boundary coverage replaces the old(D)/(E) disc decisions; Part1 theorem03 is explicitly reused at n3, with the requested literal audit-pending label qualified by accepted audit/completed dispositions. N=6,…,8 remain OPEN until separately certified; the combined A5 mathematical target is PARTIAL by degree cases. Preserve the original MEASURED search history. Primary Table3 agrees at n3 and n4; no n6/7/8 published correction is certified from these cases.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## A5 n3, n4 and n5 split records

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; valid identities (not tolerance tests) at the degenerate points, including the n = 3 edge case where a cardinal function was observed to vanish along the edge x = +1 (UNVERIFIED as an identity); rigorous root enclosures replacing the per-pattern Newton step; complete box-discard arguments; rigorous arithmetic; committed essential evidence; an independent rerun by a second checker.
```

New:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; valid identities (not tolerance tests) at the degenerate points, including the n = 3 edge case where a cardinal function was observed to vanish along the edge x = +1 (UNVERIFIED as an identity); rigorous root enclosures replacing the per-pattern Newton step; complete box-discard arguments; rigorous arithmetic; committed essential evidence; an independent rerun by a second checker.

Dated split update proposed after the Part2 Claude audit: the preceding certification obligations remain needed for n=6,…,8. Complete exact replacements for n3,n4,n5 are PROVED separately in `PD-T?proof-attempts-2-codex-06` (15total=7interior+6edge+2corner) `-10` (27total=13interior+12edge+2corner), and `-16` (25total=14interior+9edge+2corner), with supporting reductions, committed certificates, separate verifiers and actual independent executions. Preserve this record's original measured search history; do not relabel the frozen floating search as certified. The whole A5 mathematical target is PARTIAL by proved degree cases3,4,5 and OPEN cases6,…,8. No n6/7/8 correction is certified.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## A4 n3, n4 and n5 finite cases

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).
```

New:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).

Dated finite-case update proposed after the Part2 Claude audit: n3 is PROVED in `PD-T?proof-attempts-2-codex-07`, max λ_3=17/6+(2/3)sqrt2 attained exactly at(−1,±1). N4 is PROVED in `-11`, max λ_4=(13+sqrt2+2sqrt5+sqrt10)/5 attained exactly at(±1,−1). N5 is PROVED in `-17`, max λ_5=(38+8sqrt3+10sqrt5)/15 attained exactly at(−1,±1). All three proofs include the strict-count certificate, explicit exclusion/value bounds for non-strict global maxima, and actual independent executions. The all-n conjecture and every uncertified finite/asymptotic case remain OPEN. The original lack-of-continuum-verification statement is historical at the pinned source head.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## Additional registry preparation checklist for certified n3, n4 and n5

Propose local result rows05–11 and15–19 and mappings programme06→results06/10/16 (n3/n4/n5 counts), programme05→results07/11/17 (n3/n4/n5 global cases). Preserve all original measured-search rows, programme06's uncertified n6…8 cases and programme05's all-n OPEN conjecture. Apply only in the authorized integration pass after the Part2 Claude audit. No shared registry or final ID is edited in this branch.
