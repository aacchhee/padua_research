# Proposed upstream record changes — literal old → new blocks

These ten approved proposals are now applied in full PR12 preparation under AC's explicit authorization for final IDs and shared updates. The earlier topic-only deferral is superseded. Final IDs: PD-T156–197, PD-N072–073, IDEA-286–311; exact aliases/mapping are in preparation/final-id-map.json. Claude audit-01 accepted the scientific candidate 4265bb94f987ce77d89cd5e15a8c435cbd1411d0; response-01 answers its minor findings. The approved integration is recorded in pr-prep.md; Old/New text below remains the literal pre-application provenance.

Each Old block is preserved verbatim at its stated pin and is also contained in its New block, except that the absent-file proposal has empty Old content. Historical aliases in those preserved paragraphs remain historical; dated additions use existing final IDs. Part2 local PD-T?/PD-N? IDs are distinct from source PD-T098/099/100 and PD-N039/040. The user-required Part1 audit-pending label stays in topic dependency records; shared additions cite accepted PD-T101.

Original Part1 pin: a09d910ae7d5526b1e216066421a0bee7fc20da4. Original programme pin: 9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. Current main/base: 28aaa20861d08074b77efc74eaef75cdcb36234d. Part1 audit/response and merge history are preserved in LOG. All original routes, measured records and unresolved stronger targets remain.

## A2: ordered asymptotic results

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Known: Kolomoitsev–Lomako 2021, Thm 2.1 (LITERATURE, primary excerpt checked by the audit) gives the leading term (4/π²) log² n with an O(log n) remainder for the **global** Padua Lebesgue constant Λ(Pad_n) = max λ_n, not for the corner value; since Λ_c(n) ≤ Λ(Pad_n) it yields only Λ_c(n) ≤ (4/π²) log² n + O(log n). The matching lower bound for Λ_c (the corner leading term) is part of this target, unless A4 is proved first (response-02, audit-02 B4.5); the fitted b agrees with (8/π²)(γ + log(8/π)) only within a post-registration model (pre-registered fit uncertainty is too coarse to separate it, PD-T?…-04). Done when: a proof of the b-term with an explicit O(1) bound. Route: with A1, Λ_c(n) is a Riemann sum of |D_n| over a sheared lattice on the torus; split D_n into the U_{n+1}U_{n+1} and U_nU_n parts, compare with the product of two 1-D Chebyshev Lebesgue sums (each contributing (2/π) log n + c₁), and control the cross terms; Kolomoitsev–Lomako's discretisation lemma is the template (read the full paper first).
```

New:

```text
Known: Kolomoitsev–Lomako 2021, Thm 2.1 (LITERATURE, primary excerpt checked by the audit) gives the leading term (4/π²) log² n with an O(log n) remainder for the **global** Padua Lebesgue constant Λ(Pad_n) = max λ_n, not for the corner value; since Λ_c(n) ≤ Λ(Pad_n) it yields only Λ_c(n) ≤ (4/π²) log² n + O(log n). The matching lower bound for Λ_c (the corner leading term) is part of this target, unless A4 is proved first (response-02, audit-02 B4.5); the fitted b agrees with (8/π²)(γ + log(8/π)) only within a post-registration model (pre-registered fit uncertainty is too coarse to separate it, PD-T?…-04). Done when: a proof of the b-term with an explicit O(1) bound. Route: with A1, Λ_c(n) is a Riemann sum of |D_n| over a sheared lattice on the torus; split D_n into the U_{n+1}U_{n+1} and U_nU_n parts, compare with the product of two 1-D Chebyshev Lebesgue sums (each contributing (2/π) log n + c₁), and control the cross terms; Kolomoitsev–Lomako's discretisation lemma is the template (read the full paper first).

Dated update after accepted Part2 Claude audit-01: A2(i)–(iii) are PROVED in PD-T?proof-attempts-2-codex-01, -02 and -03, with supporting comparison -04. For every n ≥ 2, the corner value is at least (4/π²) log² n − 54, its absolute leading-term error is at most 95 log n, and the absolute remainder after the stated b log n term is at most 68. These are analytic proofs; finite regressions are supplementary and the sign step is analytic. The existing exact-corner dependency is PD-T101. The existing full expansion PD-T098 (A3) and global corner-argmax PD-T099 remain OPEN. The historical route and source coverage above are retained.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## A2: preserve the full A3 target

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
| the conjectured expansion itself | OPEN | needs an analytic proof or rigorous remainder control |
```

New:

```text
| A2 substatement: (4/π²) log² n + b log n + O(1), with b as stated | PROVED | PD-T?proof-attempts-2-codex-03 gives absolute remainder ≤ 68 for every n ≥ 2; supporting -04 and weaker ordered results -01/-02 are separate records. Claude audit-01 accepted this scope. The full PD-T098 A3 expansion remains OPEN. |
| the conjectured expansion itself | OPEN | needs an analytic proof or rigorous remainder control |
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## A5: certification by degree

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.
```

New:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.

Dated certification update after accepted Part2 Claude audit-01: the OPEN_TARGETS A5 certification item is PARTIAL by degree, with PROVED cases n = 3–7 and OPEN case n = 8. The source measured-search record PD-T100 keeps its registry status MEASURED. Separate count records PD-T?proof-attempts-2-codex-06, -10, -16, -41 and -51 certify interior/open-edge/non-node-corner/closed counts 7/6/2/15, 13/12/2/27, 14/9/2/25, 25/14/2/41 and 33/15/2/50 respectively. Their new exact procedures discharge all five obligations through complete certificates, separate verifiers and actual independent producer/checker/control executions. Physical boundary coverage replaces the old (D)/(E) disc decisions; PD-T103 is also explicitly reused at n = 3. The floating search itself is not relabelled as certified.

LITERATURE: arXiv 2605.23299v1, §3.3 Table 3 (LIT-388), agrees for n = 3–5. Its interior/total rows 23/39 and 27/42 for n = 6,7 have scoped candidate corrections 25/41 and 33/50, with exact readings in the topic's literature-comparison receipts. At n = 8, separate PD-T?proof-attempts-2-codex-64 proves at least 44 distinct strict interior maxima, contradicting the reported interior 38 only. Exact interior -65, closed count -61 and global -62 remain OPEN: both complete interior checks reached the deadline without successful atomic receipts, and boundary retries produced no final artifact. The reported total 56 is not replaced with an exact value. No author contact or accepted-erratum claim. The programme's measured values agree wherever certified; no negative record against PD-T100 is needed.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## A5: preserve the measured search record PD-T100

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`

Pinned commit: `806cc7b4509fd93bae652f9545d32d95529f8281`

Old:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`; rigorous root enclosures/exclusions replacing the per-pattern Newton steps over every discarded region; complete sign-pattern box-discard arguments without the early return; exact treatment near regular crease crossings; rigorous arithmetic throughout and an independent checker. The separate `degenerate_max` local obligations have replacement certificates in PD-T103 for the two degree-3 exact representatives, with Z={L_(2,2)}, background critical points at (theta,phi)=(0,acos(±1/sqrt(3))), rational angle enclosures of width 1e-18 and uniform Hessian margin greater than 3.5 on angle l1 discs of radius 0.0021. These discs rigorously contain the recorded radius-0.002 decision neighborhoods. The stored floating iterates themselves are not exact zeros. A fresh trace of every call for n=3,…,8 found two calls at n=3 and none at n=4,…,8; this trace remains MEASURED execution evidence. Obligation (2) is discharged for the `degenerate_max` path only; the (D) corner and (E) edge-node handlers remain explicit certification work. No maxima count is certified.
```

New:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`; rigorous root enclosures/exclusions replacing the per-pattern Newton steps over every discarded region; complete sign-pattern box-discard arguments without the early return; exact treatment near regular crease crossings; rigorous arithmetic throughout and an independent checker. The separate `degenerate_max` local obligations have replacement certificates in PD-T103 for the two degree-3 exact representatives, with Z={L_(2,2)}, background critical points at (theta,phi)=(0,acos(±1/sqrt(3))), rational angle enclosures of width 1e-18 and uniform Hessian margin greater than 3.5 on angle l1 discs of radius 0.0021. These discs rigorously contain the recorded radius-0.002 decision neighborhoods. The stored floating iterates themselves are not exact zeros. A fresh trace of every call for n=3,…,8 found two calls at n=3 and none at n=4,…,8; this trace remains MEASURED execution evidence. Obligation (2) is discharged for the `degenerate_max` path only; the (D) corner and (E) edge-node handlers remain explicit certification work. No maxima count is certified.

Dated split update after accepted Part2 Claude audit-01: the preceding certification obligations are historical for n = 3–7 and remain unresolved for n = 8. PD-T100 and its frozen floating search keep their MEASURED registry status. Complete replacements are separate PROVED count records PD-T?proof-attempts-2-codex-06, -10, -16, -41 and -51, with closed totals 15, 27, 25, 41 and 50 and interior totals 7, 13, 14, 25 and 33. Their supporting reductions, complete certificates, independent verifiers and actual different-agent executions are retained.

Only the OPEN_TARGETS A5 certification item is PARTIAL by these five proved degree cases and the OPEN degree-eight case. The degree-eight lower bound PD-T?proof-attempts-2-codex-64 proves at least 44 strict interior maxima; exact interior -65, closed count -61 and global -62 remain OPEN after deadline failures. The measured 44/62 reference is preserved as measurement, not promoted by the lower bound. LITERATURE: LIT-388 Table 3 has candidate corrections 23/39 → 25/41 at n = 6 and 27/42 → 33/50 at n = 7; at n = 8 only interior 38 is contradicted by ≥ 44. No exact replacement total or accepted erratum is asserted.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## A4: certified finite global cases

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).
```

New:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).

Dated finite-case update after accepted Part2 Claude audit-01: separate PD-T?proof-attempts-2-codex-07, -11, -17, -42 and -52 prove the global maximum and equality only at the two non-node corners for n = 3,4,5,6,7. Their exact values are respectively 17/6 + (2/3)√2; (13 + √2 + 2√5 + √10)/5; (38 + 8√3 + 10√5)/15; (15 + 8β + 20β² + 4√3 + 4√3β)/21 with β = 2 cos(π/7); and the FIELD12 coefficient vector [83/28, -5/7, -4/7, 2/7, -2/7, 0, 2/7, 0, -2/7, 1/7, 2/7, 0] in the basis specified in -52. The equality sets are (−1, ±1) for odd n and (±1, −1) for even n. All five arguments exclude non-strict plateaus as well as comparing certified strict maxima. PD-T099's all-n statement remains OPEN; no unverified degree is included.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## A4(a): exact edges and central envelope

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`

Old:

```text
Known: no counterexample at 75 tested degrees up to n = 200 on finite meshes; the runner-up is an edge maximum near the midpoint of x = ±1 with fitted gap ≈ 0.548 + 0.84/n (MEASURED). Because the gap stays bounded, a proof needs: (a) an expansion of the edge-midpoint value to O(1) precision, R(n) = Λ_c(n) − g + o(1) with g > 0 (a corner-type closed form along the edge, as in A1, is the first step); (b) local upper bounds throughout neighbourhoods of the corners (λ_n ≤ Λ_c(n), with equality only at the non-node corners if "attained only" is to be proved) and of the two edge midpoints (λ_n ≤ Λ_c(n) − δ there); (c) a global bound λ_n ≤ Λ_c(n) − δ on the rest of the square; (d) a rigorous finite verification for n < n₀. Done when: (a)–(c) for n ≥ n₀ together with (d), or any other argument covering the whole square. Point expansions at the corner and the edge midpoint do not control the interiors of their neighbourhoods, and a small-n check does not cover them for large n (response-02, audit-02 B4.4).
```

New:

```text
Known: no counterexample at 75 tested degrees up to n = 200 on finite meshes; the runner-up is an edge maximum near the midpoint of x = ±1 with fitted gap ≈ 0.548 + 0.84/n (MEASURED). Because the gap stays bounded, a proof needs: (a) an expansion of the edge-midpoint value to O(1) precision, R(n) = Λ_c(n) − g + o(1) with g > 0 (a corner-type closed form along the edge, as in A1, is the first step); (b) local upper bounds throughout neighbourhoods of the corners (λ_n ≤ Λ_c(n), with equality only at the non-node corners if "attained only" is to be proved) and of the two edge midpoints (λ_n ≤ Λ_c(n) − δ there); (c) a global bound λ_n ≤ Λ_c(n) − δ on the rest of the square; (d) a rigorous finite verification for n < n₀. Done when: (a)–(c) for n ≥ n₀ together with (d), or any other argument covering the whole square. Point expansions at the corner and the edge midpoint do not control the interiors of their neighbourhoods, and a small-n check does not cover them for large n (response-02, audit-02 B4.4).

Dated split update after accepted Part2 Claude audit-01: PD-T?proof-attempts-2-codex-70 proves an exact formula on all four edges with polynomial removable limits. Separate -71 proves positive complementary-grid gaps including the 2/[n(n+1)] singular correction. Separate -72 proves C_n = Λ_c(n) − g + o(1) for its explicit central complementary-grid sequence over both parities. Separate -73 gives the same positive g as a one-dimensional integral and rational alternating series; two actual exact Fraction/Machin executions yield 0.548504986190 < g < 0.548525055355.

Separate -74 through -77 prove the central-edge envelope expansion R_cen = Λ_c − g + o(1) and 0 ≤ R_cen − C_n = o(1), where R_cen maximizes over both vertical edges with |t − π/2| ≤ π/(n+1). The convention was registered after analytic reductions -70/-71, before -74 through -77 and before the first A4 numerical regression. This is the scope of the proved continuation; the historical searched R(n) is a distinct MEASURED object and its identification with R_cen or a global non-corner competitor remains OPEN. The measured 0.548 fit is not a premise. Uniform phase, gain and defect proofs retain zeros, cusps, endpoints and removable values. Full-square parts (b)/(c), effective global thresholds and all-n PD-T099 remain OPEN. The finite part (d) is separately proved for n = 3–7. Finite identity regressions supplement the analytic proofs.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## B3: computed-section extension

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text
Known: on general symmetric pairs α > ½ is impossible for the symmetrised-product count (PD-N?…-01, PROVED); the two measured cluster examples are not computed sections. Part (i) is itself a quantitative Lin-type question (distance from computed sections to 𝒞_n in terms of δ); `PD-T?bivariate-lanczos-claude-304`(a) (pinned `5f52331`) gives a related square-case bound and should be read first. Nothing here implies S(α) true or false. Done when: either a counterexample inside the computed-section class at distance ≈ c√δ (which would extend PD-N?…-01 to that class), or a theorem with α > ½ under stated hypotheses. Route for a counterexample: two nodes ε apart with M > N chosen so that the recurrence's sections inherit a 45° eigenbasis rotation in the cluster, with the box boundary gap of order √δ.
```

New:

```text
Known: on general symmetric pairs α > ½ is impossible for the symmetrised-product count (PD-N?…-01, PROVED); the two measured cluster examples are not computed sections. Part (i) is itself a quantitative Lin-type question (distance from computed sections to 𝒞_n in terms of δ); `PD-T?bivariate-lanczos-claude-304`(a) (pinned `5f52331`) gives a related square-case bound and should be read first. Nothing here implies S(α) true or false. Done when: either a counterexample inside the computed-section class at distance ≈ c√δ (which would extend PD-N?…-01 to that class), or a theorem with α > ½ under stated hypotheses. Route for a counterexample: two nodes ε apart with M > N chosen so that the recurrence's sections inherit a 45° eigenbasis rotation in the cluster, with the box boundary gap of order √δ.

Dated qualification: the historical sentence “Nothing here implies S(α) true or false” above is superseded for the specified count by PD-N?proof-attempts-2-codex-01. Existing source records are PD-N039 for the earlier symmetric-pair failure and PD-T060(a) for the related square-case bound; their narrower original scopes are preserved.

After accepted Part2 Claude audit-01, PD-N?proof-attempts-2-codex-01 is PROVED and the specified S(α) has disposition REJECTED: refuted in genuine positive-pivot computed sections at fixed n = 1, p = 1/10, M = 4. For all 0 < t ≤ 10^−6, its four-positive-atom family has 0 < δ_t → 0 and computed boundary gap ≥ √δ_t/10, yet n_box = 1/2 while an actual fixed commuting reference within g/2 has joint count 1. Condition (ii) fails for every member and (i) holds; this defeats every α > 1/2 and finite C(1,p). Two developer-side exact executions verify section identities and whole-interval polynomial signs; the written proof supplies the spectral and norm interpretation, independently checked in audit-01.

PD-N?proof-attempts-2-codex-02 separately proves failure of only the literal common shrinking two-dimensional cluster route under its fixed-N,p and full-residual hypotheses, using positive estimate PD-T?proof-attempts-2-codex-80. Shrinking the box around an isolated node escapes that route obstruction. Neither other count objects S_F, an all-n family, nor failure of commuting-reference existence is asserted.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## B3: preserve PD-N039 scope and history

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-N01-symmetrised-product-inertia-count.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text
Whether a δ-tolerant count with α > ½ exists on the class of positive-pivot computed sections (cyclic, size dim Π_n) is not addressed: `OPEN_TARGETS.md` B3. Transfer to the Lanczos topic (LZ-034 / L3) only in this restricted form.
```

New:

```text
Whether a δ-tolerant count with α > ½ exists on the class of positive-pivot computed sections (cyclic, size dim Π_n) is not addressed: `OPEN_TARGETS.md` B3. Transfer to the Lanczos topic (LZ-034 / L3) only in this restricted form.

Dated separate extension after accepted Part2 Claude audit-01: the scope left unresolved by PD-N039's historical statement above is resolved for the specified symmetrised-product S(α) by PROVED PD-N?proof-attempts-2-codex-01. The specified count has disposition REJECTED: refuted at fixed n = 1, p = 1/10, M = 4 for all 0 < t ≤ 10^−6, with computed gap ≥ √δ/10 and n_box = 1/2 versus valid reference count 1. This does not broaden the original PD-N039 theorem retrospectively or relabel its old measurements as section certificates. Other count objects S_F, other degrees and reference-existence questions remain OPEN. The complete proof and exact evidence are in the Part2 topic; the distinct route obstruction is PD-N?proof-attempts-2-codex-02, supported by PD-T?proof-attempts-2-codex-80.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## B1: exterior diagonal poles and source taper

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text
Known: MEASURED with exact blocks for five pole classes, t ≤ 9, M = 120 (`checks/code/decisive/gen1-3/window_exact.py/.out`); the three-block projection without the constraint is false (PD-N?…-02 (i)). Done when: a proof, or a counterexample with general-position poles. Route: the 1-D orthogonal-rational-function three-term recurrence (Bultheel et al.) is the template; express the degree-(t+1) block through a "top-form" functional, as in the adversary's window-parity sketch (`checks/adversarial-gen1-3.md` (ii)(1)), and identify the single linear constraint per direction that W_{t−2} imposes.
```

New:

```text
Known: MEASURED with exact blocks for five pole classes, t ≤ 9, M = 120 (`checks/code/decisive/gen1-3/window_exact.py/.out`); the three-block projection without the constraint is false (PD-N?…-02 (i)). Done when: a proof, or a counterexample with general-position poles. Route: the 1-D orthogonal-rational-function three-term recurrence (Bultheel et al.) is the template; express the degree-(t+1) block through a "top-form" functional, as in the adversary's window-parity sketch (`checks/adversarial-gen1-3.md` (ii)(1)), and identify the single linear constraint per direction that W_{t−2} imposes.

Dated restricted-class split after accepted Part2 Claude audit-01: PD-T?proof-attempts-2-codex-90 through -93 are PROVED for real exterior parallel diagonal poles ell_j = x + y − a_j, a_j > 2, with nodes in [−1,1]², positive weights and injective evaluation on Π_(T+1), M ≥ dim Π_(T+1). For every such fixed sample and every fixed finite T ≥ 3, -90 expresses all lower leakage through one next-pole homogeneous top-form functional and proves that W_(t−2) detects every leakage direction for all outward offsets. Separate -91 constructs a nonzero pole-only sum-of-squared-minors polynomial using a coalescent structural witness for these fixed data; -92 proves the extraction equality simultaneously for 2 ≤ t ≤ T outside its proper real algebraic exception, including distinct ordered offsets. Generic nodes/weights and floating ranks are not substituted for this fixed-data quantifier.

Separate -93 proves finite exceptional parameter sets for both source orders of the literal even-count Ldiag taper. The prose source uses a = 2 + ε, while its line factory uses a = 2 + √2 ε; the normalization clarification covers a = 2 + κ ε for each fixed κ > 0. No individual stored parameter or exception location is certified. These are analytic proofs, not upgrades of the numerical implementation. PD-N040's tested numerical failures and IDEA-192's corresponding rejection remain valid at their original scope, with a dated pointer to these structural splits. Other pole classes and numerical stability remain OPEN.
```

Validation: Old occurs exactly once at its pin and current main; the entire Old block is retained in New.

## Repository-only results summary — proposed new file

Target: `results/padua-proof-attempts-2-20261101.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text

```

New:

```text
# padua-proof-attempts-2-20261101 — second proof campaign

Stage PR (preparation within topic-only scope); Claude Opus 5.5 xhigh audit-01 accepted for the stated scope, with minor findings answered in response-01. [Draft PR12](https://github.com/aacchhee/padua_research/pull/12) remains unready for merge until preparation is complete.

- A2 PROVED: requested corner b coefficient, explicit absolute remainder ≤ 68; local results 01–04.
- A5 certification item PARTIAL by degree: closed counts 15, 27, 25, 41, 50 for n = 3–7 and separate corner-only globals. Degree 8 has at least 44 strict interior maxima; exact counts/global remain OPEN. PD-T100's measured-search status stays MEASURED.
- A4(a) PROVED at its central-envelope scope: R_cen = Λ_c − g + o(1), both parities, 0.548504986190 < g < 0.548525055355; exact all-four-edge formula. Full-square A4 and global runner-up identification remain OPEN.
- PD-N?proof-attempts-2-codex-01 PROVED; specified S(α) REJECTED: refuted on positive n = 1, p = 1/10, M = 4 sections. Count 1/2 differs from valid reference count 1 at the required square-root gap. Other counts/reference existence are not refuted.
- B1 PROVED for generic exterior parallel real diagonal poles, every fixed admissible sample/finite T; literal even-count Ldiag taper except finitely many parameters. Other classes, fixed parameters and stability remain OPEN.

[Full report, proofs and evidence](../topics/padua-proof-attempts-2-20261101/report.md).
Next: Codex (gpt-6.1-sol medium): Continue codex/padua-proof-attempts-2-20261101. Only AC merges.
```

Validation: Target absent at the pin; Old is empty new-file content.

## Complete PR-preparation checklist — proposals only

These integration obligations answered F3 and are now completed under AC's subsequent explicit preparation authorization. The following wording retains the original checklist for provenance. At a later authorized integration, refresh main and active PRs, recheck literal blocks and reserve fresh IDs under WORKFLOW before assigning them. There are currently 42 local PD-T files and two local PD-N files; count the final scope again before reserving. Do not assume an unused range is free. Reserve IDEA IDs for retained candidates when authorized. No range is reserved here.

| Destination / existing record | Required dated addition or mapping |
|---|---|
| state/IDEAS.md, IDEA-206 | Point to A2 01–04, A5 counts/globals and degree-eight lower bound, A4 70–77, accepted audit and exact OPEN boundaries. Replace the stale umbrella A2/A3 wording without closing A3. Preserve the programme measured search and original routes. |
| PROOF_STATUS.md and ID_CROSSWALK.md | Add one row per durable local record with its exact epistemic status and dependencies, then each provisional-to-final mapping. PD-T098 (full A3) and PD-T099 (all-n global) remain OPEN; PD-T100 remains MEASURED. No status aggregation may overwrite a separate proved split. |
| PD-T098 source Split into / Part2 Split from | Include all A2 01, 02, 03 and supporting 04; keep accepted Part1 PD-T101 and full A3 scope/history. |
| PD-T099 source Split into / Part2 Split from | Include finite globals 07, 11, 17, 42, 52 and the exact edge/central-scope records 70, 71, 72, 73, 74, 75, 76, 77. Preserve the all-n full-square target. |
| PD-T100 source Split into / Part2 Split from | Include supporting reductions 05, 08, 09, 15, 18, 19, 40, 50, 53, 60, 63; count cases 06, 10, 16, 41, 51; and degree-eight OPEN closed 61, OPEN global 62, PROVED lower bound 64 and OPEN exact interior 65. Supporting statements do not certify a count. |
| OPEN_TARGETS.md introduction (line 19 at main28aaa20) | Replace the stale combined “A2/A3 asymptotics … remain OPEN” summary by A2 proved / full A3 OPEN; identify the exact central A4 split and finite cases while preserving full-square A4 OPEN. Apply the literal target-block additions above. |
| PD-N039 source Split into / Part2 negative Split from | Add the computed-section extension PD-N?proof-attempts-2-codex-01. Record the route obstruction PD-N?proof-attempts-2-codex-02 as a separate scoped failure, with positive support80; do not broaden the original symmetric-pair statement. |
| PD-N040 source Split into, PROOF_STATUS and IDEA-192 | Add dated pointers to B1 90–93, distinguishing structural validity for exterior Ldiag from the still-valid implementation failure. Preserve tested numerical instability and the original REJECTED: failed disposition. Add crosswalk mappings for all four structural splits and their source relationship. |
| state/IDEAS.md programme obstruction/disposition table | Add local negative01 as PROVED failure of the specified S(α) in computed sections, with exact fixed-n,p scope; add local negative02 as PROVED failure of the literal C1 common shrinking full-residual cluster route. Link support80. Update IDEA-198 only for this specified count, preserving other F and reference-existence questions. |
| Candidate table / crosswalk | Retain B3 C1 as REJECTED: failed with negative02/support80; C2 as consolidated into C3 (not a failed mechanism or negative theorem); C3 as retained successful counterexample with negative01. Retain the n4 candidate aliases IDEA?proof-attempts-2-codex-n4-01/02 with their dated completed dispositions and mappings. Register any other retained attempt candidates under their own final IDEA IDs only when authorized. |
| LIT-379 | Add this topic's full arXiv 2009.07114v1 text reading: Theorem 2.1 global upper context only, Lemmas 3.5(3.20), 3.6(3.29), (4.5)–(4.6); page locators qualified per developer reading. Credit the source product route; the local explicit remainder proof is separate. Preserve the historical secondary row and the prior MZ addendum. |
| LIT-388 and IDEA-048 | Add primary arXiv 2605.23299v1 §3.3 Table 3 readings and exact candidate-correction scope for n6/n7 and interior-only n8. Supersede “pending/UNVERIFIED” only for these newly inspected claims; keep unrelated unverified claims and geometric open problems qualified. No accepted-erratum claim or author contact. |
| LIT-312 | Add this topic's bounded Bos et al. 2006 author-preprint reading: definitions and Theorem 3 sum/integral estimates, not a full-paper read or a premise of the local A2 proof. Preserve prior addenda and journal/preprint coverage gaps. |
| Repository results | Use the proposed results file above and, only when authorized, its own root RESULTS.md section. Preserve every other topic's section. The historical intended Windows entry is superseded by repository-only tracking and must not be written. |

Source aliases in preserved Old paragraphs map to final records as follows: programme -04 → PD-T098; -05 → PD-T099; -06 → PD-T100; programme N01 → PD-N039; programme N02 → PD-N040; Lanczos304 → PD-T060; Part1 A1 → PD-T101. Keep source titles/links and original-to-split mappings in both directions. Exact source paths are in the literal blocks, PROOF_STATUS and ID_CROSSWALK at the recorded main pin.

History: source PD-T100's Runs-needed block was repinned at Part1 squash806cc7b because that accepted update changed the literal paragraph; its older proposal is retained in commitf5f074e. Main e0d9e3d and rule-only28aaa20 changed none of the current Old blocks. Response-01 rechecks all nine nonempty blocks at both their stated pins and main28aaa20, plus the absent new-file target. No earlier history is rewritten.
