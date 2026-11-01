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

Status update proposed after the Part2 Claude audit: A2(i)–(iii) are PROVED in `PD-T?proof-attempts-2-codex-01`, `-02`, `-03`, with separate supporting comparison `-04`. For every n≥2, Λ_c(n)≥(4/π²)log²n−54, the absolute leading-term error is at most95log n, and the absolute remainder after the stated b log n is at most68. These are written analytic proofs; finite exact regressions and independent reruns are supplementary. Dependency: `PD-T?proof-attempts-codex-01 (audit pending)`; its Claude audit-01 at95279b8 accepted A1, with minor dispositions pending upstream. The full A3 expansion and global A4 remain OPEN. This update does not replace the original statement, source coverage or proposed route above.
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
