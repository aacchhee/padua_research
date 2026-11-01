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

Further target proposals will be appended only when their actual results are known. No A5 count or published-table correction is proposed yet.

## A5 n3 status

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.
```

New:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.

Status update proposed after the Part2 Claude audit: the n=3 case is PROVED by `PD-T?proof-attempts-2-codex-06` (15 strict maxima:7interior,6edge,2corner), with finite reduction -05, a single exact certificate, a separate certificate checker and actual independent producer/checker executions. All five obligations are discharged for this new n3 procedure; its physical boundary coverage replaces the old(D)/(E) disc decisions, and `PD-T?proof-attempts-codex-03 (audit pending)` is explicitly reused with its accepted-audit/completed-response qualification. The n=4,…,8 exact-count cases remain OPEN until separately certified. The whole A5 mathematical target is PARTIAL by these degree cases; the source execution table remains MEASURED history. The n3 primary Table3 row agrees, so no published correction is proposed from this case.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## A5 n3 split record

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; valid identities (not tolerance tests) at the degenerate points, including the n = 3 edge case where a cardinal function was observed to vanish along the edge x = +1 (UNVERIFIED as an identity); rigorous root enclosures replacing the per-pattern Newton step; complete box-discard arguments; rigorous arithmetic; committed essential evidence; an independent rerun by a second checker.
```

New:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; valid identities (not tolerance tests) at the degenerate points, including the n = 3 edge case where a cardinal function was observed to vanish along the edge x = +1 (UNVERIFIED as an identity); rigorous root enclosures replacing the per-pattern Newton step; complete box-discard arguments; rigorous arithmetic; committed essential evidence; an independent rerun by a second checker.

Dated split update proposed after the Part2 Claude audit: the preceding obligations remain needed for n=4,…,8. For n=3, their complete exact replacement is PROVED separately in `PD-T?proof-attempts-2-codex-06`, supported by -05 and its certificate/checker/independent-execution records. Preserve this record's original measured search history and Table3 comparison; do not relabel the frozen floating search as a certified algorithm. Exact n3 count:15total=7interior+6edge+2corner. The all-degree n=3,…,8 target is PARTIAL by the proved n3 case and OPEN remaining degree cases. No n6/7/8 correction is certified.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## A4 n3 finite case

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).
```

New:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).

Dated finite-case update proposed after the Part2 Claude audit: n=3 is PROVED separately by `PD-T?proof-attempts-2-codex-07`: max λ_3=17/6+(2/3)sqrt2, equality exactly at(−1,±1). The proof includes the exact strict-maxima certificate plus bounds/classification of non-strict global maxima, and actual independent executions. The all-n conjecture remains OPEN, as do its other uncertified finite degrees and asymptotic neighbourhood/global obligations. The original no-continuum-verification statement above is historical at the pinned source head, not a claim about this new split result.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## Additional registry preparation checklist for certified n3

Propose local result rows05–07 and mappings programme06→result06 (n3 count), programme05→result07 (n3 global case). Preserve all original measured-search rows, programme06's uncertified n4…8 cases and programme05's all-n OPEN conjecture. Apply only in the authorized integration pass after the Part2 Claude audit. No shared registry or final ID is edited in this branch.
