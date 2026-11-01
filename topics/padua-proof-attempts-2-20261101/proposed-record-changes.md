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

## A5 n3 through n7 status

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.
```

New:

```text
Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.

Status update proposed after the Part2 Claude audit: n=3,4,5,6,7 are PROVED by `PD-T?proof-attempts-2-codex-06`, `-10`, `-16`, `-41`, `-51`: respectively15=7interior+6edge+2corner,27=13interior+12edge+2corner,25=14interior+9edge+2corner,41=25interior+14edge+2corner,50=33interior+15edge+2corner. Separate exact certificates, independent verifiers and actual different-agent producer/global/checker/control executions discharge all five obligations for these new procedures. Their direct physical boundary coverage replaces the old(D)/(E) disc decisions; Part1 theorem03 is explicitly reused at n3, with the requested literal audit-pending label qualified by accepted audit/completed dispositions. N=8 remains OPEN; the combined A5 target is PARTIAL by degree cases. Preserve the original MEASURED search history. Primary v1 Table3 agrees at n3–5; its exact rows6|23|39 and7|27|42 under the headings “deg. n”, “number of inner local maxima”, “number of local maxima” have scoped candidate corrections25/41 and33/50. Direct post-certification comparisons are outputs/a5_n6_literature-comparison.md and outputs/a5_n7_literature-comparison.md. These agree with the programme measured counts, so no PD-N against that claim is needed. At n8, separate result64 proves at least44distinct strict interior maxima; this contradicts primary v1Table3 interior38 by at least6 and supplies a scoped INTERIOR-ONLY candidate correction (outputs/a5_n8_literature-lower-bound-comparison.md). No exact n8interior count, closed total or global claim is certified: both whole-interior checks hit15:19without atomic successful receipts, and both boundary retries produced no artifact. Whole-interior65/closed61/global62remainOPEN; primary total56 is not replaced with an exact value. No author contact.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## A5 n3 through n7 split records

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`

Pinned commit: `806cc7b4509fd93bae652f9545d32d95529f8281`

Old:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`; rigorous root enclosures/exclusions replacing the per-pattern Newton steps over every discarded region; complete sign-pattern box-discard arguments without the early return; exact treatment near regular crease crossings; rigorous arithmetic throughout and an independent checker. The separate `degenerate_max` local obligations have replacement certificates in PD-T103 for the two degree-3 exact representatives, with Z={L_(2,2)}, background critical points at (theta,phi)=(0,acos(±1/sqrt(3))), rational angle enclosures of width 1e-18 and uniform Hessian margin greater than 3.5 on angle l1 discs of radius 0.0021. These discs rigorously contain the recorded radius-0.002 decision neighborhoods. The stored floating iterates themselves are not exact zeros. A fresh trace of every call for n=3,…,8 found two calls at n=3 and none at n=4,…,8; this trace remains MEASURED execution evidence. Obligation (2) is discharged for the `degenerate_max` path only; the (D) corner and (E) edge-node handlers remain explicit certification work. No maxima count is certified.
```

New:

```text
**Runs needed (certification):** a proved finite reduction of the counting problem; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py`; rigorous root enclosures/exclusions replacing the per-pattern Newton steps over every discarded region; complete sign-pattern box-discard arguments without the early return; exact treatment near regular crease crossings; rigorous arithmetic throughout and an independent checker. The separate `degenerate_max` local obligations have replacement certificates in PD-T103 for the two degree-3 exact representatives, with Z={L_(2,2)}, background critical points at (theta,phi)=(0,acos(±1/sqrt(3))), rational angle enclosures of width 1e-18 and uniform Hessian margin greater than 3.5 on angle l1 discs of radius 0.0021. These discs rigorously contain the recorded radius-0.002 decision neighborhoods. The stored floating iterates themselves are not exact zeros. A fresh trace of every call for n=3,…,8 found two calls at n=3 and none at n=4,…,8; this trace remains MEASURED execution evidence. Obligation (2) is discharged for the `degenerate_max` path only; the (D) corner and (E) edge-node handlers remain explicit certification work. No maxima count is certified.

Dated split update proposed after the Part2 Claude audit: the preceding certification obligations remain needed for n=8. Complete exact replacements for n3,n4,n5,n6,n7 are PROVED separately in `PD-T?proof-attempts-2-codex-06` (15total=7interior+6edge+2corner), `-10` (27total=13interior+12edge+2corner), `-16` (25total=14interior+9edge+2corner), `-41` (41total=25interior+14edge+2corner), and `-51` (50total=33interior+15edge+2corner), with supporting reductions, committed complete certificates, separate verifiers and actual independent executions. Preserve this record's original measured search history; do not relabel the frozen floating search as certified. The whole A5 target is PARTIAL by proved cases3,4,5,6,7 and OPEN case8. Certified25/41 and33/50 supply scoped candidate corrections to primary v1 Table3 rows23/39 and27/42; n8 exact completeness remains uncertified. Separate64proves at least44strict interior maxima, with two actual exact root-witness executions and standalone replay; this gives a candidate correction to primary v1Table3 interior38 only. The complete interior proposal remains unaccepted after the hard deadline; exact interior65/closed61/global62remainOPEN. Programme's measured values agree where certified and its44interior n8is consistent with the lower bound, so no negative record against it is needed.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

History2026-11-01: supersedes the earlier source06 proposal at9bd14a6 (retained in commitf5f074e). AC merged Part1 at806cc7b, replacing its old Runs-needed paragraph with the audited local03 qualification. The current literal block preserves that entire accepted paragraph and appends only Part2 finite-case updates; all original routes and remaining obligations remain.

## A4 n3 through n7 finite cases

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-05-padua-corner-argmax.md`

Pinned commit: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`

Old:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).
```

New:

```text
Proof for all n; rigorous verification for small n (e.g. by a certified sup bound away from the corners).

Dated finite-case update proposed after the Part2 Claude audit: n3 is PROVED in `PD-T?proof-attempts-2-codex-07`, max λ_3=17/6+(2/3)sqrt2 attained exactly at(−1,±1). N4 is PROVED in `-11`, max λ_4=(13+sqrt2+2sqrt5+sqrt10)/5 attained exactly at(±1,−1). N5 is PROVED in `-17`, max λ_5=(38+8sqrt3+10sqrt5)/15 attained exactly at(−1,±1). N6 is PROVED in `-42`: with beta=2cos(pi/7), max λ_6=(15+8beta+20beta²+4sqrt3+4sqrt3*beta)/21, equality exactly at(±1,−1). N7 is PROVED in `-52`: exact FIELD12 value `[83/28,-5/7,-4/7,2/7,-2/7,0,2/7,0,-2/7,1/7,2/7,0]` in the stated basis, equality exactly at(−1,±1); all33interior and15edge values are below11/2<C and direct universal-gradient leaves exclude weak maxima by53. All five proofs include the strict-count certificate, explicit exclusion/value bounds for non-strict global maxima, and actual independent executions. The all-n conjecture and every uncertified finite/asymptotic case remain OPEN. The original lack-of-continuum-verification statement is historical at the pinned source head.
```

Validation: original block occurs exactly once at the pinned programme head; original statement, route and history retained.

## Additional registry preparation checklist for certified n3 through n7

Propose local result rows05–11,15–19,40–42,50–53 and supporting60/63, separate lower64 and OPEN61/62/65, with mappings programme06→results06/10/16/41/51 (n3/n4/n5/n6/n7 counts), programme05→results07/11/17/42/52 (n3/n4/n5/n6/n7 global cases). Preserve all original measured-search rows, programme06's uncertified n8 case and programme05's all-n OPEN conjecture. Supporting field/reflection results60/63 do not certify n8. Result64is a substantive PROVED lower-bound statement with its own file; exact65/61/62stayOPEN after actual timeout/deadline failures. Apply only in the authorized integration pass after the Part2 Claude audit. No shared registry or final ID is edited in this branch.


Current upstream refresh: Part1 is merged at main806cc7b. Existing original pins remain historical. Every current Old block was also checked unique against806cc7b; source06 alone was repinned because its accepted Part1 update changed the literal paragraph. Part2 remains local IDs/no range; inherited final IDs are source provenance.


Refresh2026-11-01 at e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9: its MZ registry/literature additions change none of these five literal Old blocks. Each remains unique at its historical pin AND this current main. All five entire Old blocks remain within their New blocks. The additional n8lower64statement is a future literal append to the existing source history, not an upgrade of the frozen floating search or a complete-count correction. Apply only after the Part2 Claude audit and authorized integration.


## A4(a) exact edge and central complementary-grid point splits

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`

Old:

```text
Known: no counterexample at 75 tested degrees up to n = 200 on finite meshes; the runner-up is an edge maximum near the midpoint of x = ±1 with fitted gap ≈ 0.548 + 0.84/n (MEASURED). Because the gap stays bounded, a proof needs: (a) an expansion of the edge-midpoint value to O(1) precision, R(n) = Λ_c(n) − g + o(1) with g > 0 (a corner-type closed form along the edge, as in A1, is the first step); (b) local upper bounds throughout neighbourhoods of the corners (λ_n ≤ Λ_c(n), with equality only at the non-node corners if "attained only" is to be proved) and of the two edge midpoints (λ_n ≤ Λ_c(n) − δ there); (c) a global bound λ_n ≤ Λ_c(n) − δ on the rest of the square; (d) a rigorous finite verification for n < n₀. Done when: (a)–(c) for n ≥ n₀ together with (d), or any other argument covering the whole square. Point expansions at the corner and the edge midpoint do not control the interiors of their neighbourhoods, and a small-n check does not cover them for large n (response-02, audit-02 B4.4).
```

New:

```text
Known: no counterexample at 75 tested degrees up to n = 200 on finite meshes; the runner-up is an edge maximum near the midpoint of x = ±1 with fitted gap ≈ 0.548 + 0.84/n (MEASURED). Because the gap stays bounded, a proof needs: (a) an expansion of the edge-midpoint value to O(1) precision, R(n) = Λ_c(n) − g + o(1) with g > 0 (a corner-type closed form along the edge, as in A1, is the first step); (b) local upper bounds throughout neighbourhoods of the corners (λ_n ≤ Λ_c(n), with equality only at the non-node corners if "attained only" is to be proved) and of the two edge midpoints (λ_n ≤ Λ_c(n) − δ there); (c) a global bound λ_n ≤ Λ_c(n) − δ on the rest of the square; (d) a rigorous finite verification for n < n₀. Done when: (a)–(c) for n ≥ n₀ together with (d), or any other argument covering the whole square. Point expansions at the corner and the edge midpoint do not control the interiors of their neighbourhoods, and a small-n check does not cover them for large n (response-02, audit-02 B4.4).

Dated Part2 split update proposed after its Claude audit: PD-T?proof-attempts-2-codex-70 proves an exact formula on all four edges with polynomial removable limits. Separate71 proves strict corner dominance at every complementary vertical-edge Lobatto ordinate via a positive triangle-defect sum plus2/[n(n+1)]. Separate72 proves C_n=Lambda_c(n)−g+o(1) for an explicitly specified all-parity central complementary-grid sequence, with one explicit convergent integral g and1/45<g<=2. Odd degrees use the selected nonnode midpoint; even degrees use the nearest complementary ordinate at angular displacement pi/[2(n+1)]. Separate74–77 now PROVE the exact central-envelope expansion R_cen=Lambda_c−g+o(1) and0<=R_cen−C_n=o(1), for the maximum over both x edges and |t−pi/2|<=pi/(n+1). The uniform phase localization, local gain and joint defect proofs retain all removable/zero/cusp cases. The source's historical searched R(n) remains a distinct MEASURED object; no equality to the globally selected noncorner competitor is silently asserted. Separate73 proves a positive one-dimensional integral and rational alternating series for the SAME g, with strict next-term bounds. Two actual independent exact K64 Fraction/Machin executions certify0.54850<g<0.54853; this is an evaluation of the analytic constant, not a fitted premise. The measured0.548fit remains a fit. Parts(b)/(c) and global all-n A4 remainOPEN; finite(d) cases3–7 are separately proved as recorded in the other proposal. Every original route, quantifier and measurement above is retained. The exact edge identity has two actual n1–6 cyclotomic Vandermonde/cardinal-polynomial regressions; finite regression is supplementary to the written proof, not the source of the asymptotic conclusion.
```

Validation: entire Old retained in New; old block unique at pinned current main. Current77resolves the preregistered central-envelope obligation; sourceR_search/global identification remainsOPEN. No shared source is edited.


Rule-only main28aaa20861d08074b77efc74eaef75cdcb36234d changes none of the six literalOld blocks. All remain unique at their historical pins and that current main; original blocks/routes remain retained in full. The new repository-only results rule is handled within the user's TOPIC-only/noRESULTSwrite scope by a topic-local proposed summary at final stop.


Final A4(a) split checklist: add local70–77and mapping source05→70/77at their exact edge/central-envelope scopes; preserve source05whole-square all-n OPEN status, all source routes and historical measurements. No final IDs are assigned here.


## B3 computed-section extension of the symmetrised-product negative

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text
Known: on general symmetric pairs α > ½ is impossible for the symmetrised-product count (PD-N?…-01, PROVED); the two measured cluster examples are not computed sections. Part (i) is itself a quantitative Lin-type question (distance from computed sections to 𝒞_n in terms of δ); `PD-T?bivariate-lanczos-claude-304`(a) (pinned `5f52331`) gives a related square-case bound and should be read first. Nothing here implies S(α) true or false. Done when: either a counterexample inside the computed-section class at distance ≈ c√δ (which would extend PD-N?…-01 to that class), or a theorem with α > ½ under stated hypotheses. Route for a counterexample: two nodes ε apart with M > N chosen so that the recurrence's sections inherit a 45° eigenbasis rotation in the cluster, with the box boundary gap of order √δ.
```

New:

```text
Known: on general symmetric pairs α > ½ is impossible for the symmetrised-product count (PD-N?…-01, PROVED); the two measured cluster examples are not computed sections. Part (i) is itself a quantitative Lin-type question (distance from computed sections to 𝒞_n in terms of δ); `PD-T?bivariate-lanczos-claude-304`(a) (pinned `5f52331`) gives a related square-case bound and should be read first. Nothing here implies S(α) true or false. Done when: either a counterexample inside the computed-section class at distance ≈ c√δ (which would extend PD-N?…-01 to that class), or a theorem with α > ½ under stated hypotheses. Route for a counterexample: two nodes ε apart with M > N chosen so that the recurrence's sections inherit a 45° eigenbasis rotation in the cluster, with the box boundary gap of order √δ.

Dated Part2 extension proposed after its Claude audit: PD-N?proof-attempts-2-codex-01 is PROVED and REFUTES this specified S(alpha) on genuine computed sections at fixedn=1,p=1/10,M=4. For every0<t<=10^-6 its explicit four-positive-atom family has0<delta_t->0 and computedgap>=sqrt(delta_t)/10, yet n_box=1/2 while a fixedpositive-pivot commuting reference within g/2 hasjointcount1. Thus(ii)fails forEVERYmember and(i)holds; everyalpha>1/2 andfiniteC(1,p) isdefeated. Twoactualexactexecutionsverify thepositive-momentsectionidentitiesandwholeintervalpolynomialsigns; fullwrittenproofsupplies allnorm/gap/reference/inertiaquantifiers. The original commonshrinkingjointcluster route is separately REJECTED:failed underfixedN,p and FULLresidualhypotheses in scopednegative02, using positiveestimate80; shrinkingtheBOXaboutanisolatednodeescapes it. Preserve the original route/historyabove. No all-n counterexample, failureofothercountobjectsS_F, or failureofnearbycommutingreferenceexistence isclaimed.
```

Validation: entire Old preserved; unique at pinned current main. No shared source is edited.


## B3 source-negative scope history and separate extension

Target: `topics/programme-ideas-20261031/theory/programme-ideas-claude-N01-symmetrised-product-inertia-count.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text
Whether a δ-tolerant count with α > ½ exists on the class of positive-pivot computed sections (cyclic, size dim Π_n) is not addressed: `OPEN_TARGETS.md` B3. Transfer to the Lanczos topic (LZ-034 / L3) only in this restricted form.
```

New:

```text
Whether a δ-tolerant count with α > ½ exists on the class of positive-pivot computed sections (cyclic, size dim Π_n) is not addressed: `OPEN_TARGETS.md` B3. Transfer to the Lanczos topic (LZ-034 / L3) only in this restricted form.

Dated separate extension proposed after the Part2 Claude audit: PD-N?proof-attempts-2-codex-01 proves the specified symmetrised-product S(alpha) FALSE in the positive-pivot computed-section class atfixedn=1,p=1/10,M=4, withn_box=1/2 versusavalidreferencejointcount1 andCOMPUTEDgap>=sqrt(delta)/10 forALL0<t<=10^-6. This extends the failure to a genuine positive-measure family; it does not retrospectively broaden the original theorem in this record or relabel its old measurements as section certificates. Other countobjectsS_F, otherdegrees andreference-existencequestionsremainOPEN. Fullproof, frozenexactsource, ownoutputsfromtwoactualexecutions and supplementaryanalyticreconstructionare retained in the Part2topic.
```

Validation: entire Old preserved; unique at pinned current main. At authorized post-auditintegration, addlocalnegative01/02andpositive80rows/mappings andupdateIDEA198dispositionforTHEspecifiedS(alpha), preservingoriginalN01scope/historyandotherF/referencequestions. No finalID/range/sharedwrite here.


## B1 exact real exterior parallel class and literal taper splits

Target: `topics/programme-ideas-20261031/OPEN_TARGETS.md`

Pinned commit: `28aaa20861d08074b77efc74eaef75cdcb36234d`

Old:

```text
Known: MEASURED with exact blocks for five pole classes, t ≤ 9, M = 120 (`checks/code/decisive/gen1-3/window_exact.py/.out`); the three-block projection without the constraint is false (PD-N?…-02 (i)). Done when: a proof, or a counterexample with general-position poles. Route: the 1-D orthogonal-rational-function three-term recurrence (Bultheel et al.) is the template; express the degree-(t+1) block through a "top-form" functional, as in the adversary's window-parity sketch (`checks/adversarial-gen1-3.md` (ii)(1)), and identify the single linear constraint per direction that W_{t−2} imposes.
```

New:

```text
Known: MEASURED with exact blocks for five pole classes, t ≤ 9, M = 120 (`checks/code/decisive/gen1-3/window_exact.py/.out`); the three-block projection without the constraint is false (PD-N?…-02 (i)). Done when: a proof, or a counterexample with general-position poles. Route: the 1-D orthogonal-rational-function three-term recurrence (Bultheel et al.) is the template; express the degree-(t+1) block through a "top-form" functional, as in the adversary's window-parity sketch (`checks/adversarial-gen1-3.md` (ii)(1)), and identify the single linear constraint per direction that W_{t−2} imposes.

Dated restricted class split proposed after the Part2Claudeaudit: PD-T?proof-attempts-2-codex-90–93 are PROVED for real exterior parallel diagonal poles ell_j=x+y−a_j,a_j>2. For EVERYfixedpositive Pi_(T+1)-determining sample and EVERYfixedfiniteT>=3,90expresses all lower leakage by a next-pole homogeneous top-formfunctional and provesWt−2detectsEVERYleakage direction forALLoutwardoffsets.91constructs a NONZEROPOLE-ONLYsum-of-squared-minors polynomial using a coalescent projective structural witness for THESEfixeddata;92proves the stated extraction equality for2<=t<=T simultaneously outside itsproperrealalgebraicexception, including distinct ordered offsets. No generic-node/weight substitution or floatingrank premise isused.93proves the literalsourceEVENpolecountLdiagtaper, BOTHsourceorders, has onlyFINITELYmanypotentiallyexceptionalpositiveσ/epsilon_min. No individualstoredparameter iscertified and noexceptionlocationcomputed. The full nonvanishing/injective-evaluation/M/dimension/fixedT hypotheses above are retained. These are analyticproofs with completeindependentfull-file reconstruction, not upgradedversions of the floating 'exact blocks' experiments. The source's numericalimplementationfailure PD-N040 remainsunchanged; otherpoleclasses and numericalstabilityremainOPEN. Preserve the original measurement, route and broaderscope above.
```

Validation: entireOldstatement/measurement/route retained; unique at pinnedcurrentmain. Proposedrows/mappingsforlocal90–93closeONLYthisspecifiedclasspart of B1, preservingtheoriginalbroaderother-classOPENtarget and numericalsolvernegative. No finalID/range/sharedwrite.
