# T-A5 — strict local maxima certification

- Developer: Codex, allocated `gpt-6.1-sol` xhigh (mathematics).
- Rules read at full branch SHA `3db1eee3fd9507c103c496bdf3da8157331359c5`.
- Start / pre-run timebox: **2026-11-01 09:19 UTC**, about six hours; deadline **2026-11-01 15:19 UTC**.
- Ordered scope: certify n=3,4 first, extend through n=8 if practical; all five obligations in programme A5, rigorous global-value corollary separately.
- Kill criteria (written before mathematical runs): stop at a complete checked certification for the reached n, a rigorously established counterexample to the measured count, or the six-hour deadline. A failed computational route is recorded as an obstacle and another viable route may be tried within the box. Never infer completeness from numerical agreement or a partial list.
- Required before promotion: proved finite reduction, exact/outward arithmetic, all consistent signs/regions covered, regular creases and crossings excluded exactly, degenerate corner/edge-node handlers, separate certificate checker, actual independent producer and checker runs, durable proof/evidence records.
- Dependency spelling retained: `PD-T?proof-attempts-codex-03 (audit pending)`; dated acceptance of the part-1 audit and its explicit (D)/(E) handler requirement will be recorded below.
- Authoritative sources: programme `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; part-1 scientific `a09d910ae7d5526b1e216066421a0bee7fc20da4`; part-1 audit `95279b833bca5967fcf47c1b71a56ff622185b4e`.

## Status

A5 PARTIAL by explicit degree cases: n=3 is PROVED under separate result06; n=4,…,8 remain OPEN. The same six-hour A5 box continues with the independently assigned n=4 developer. Result07 proves A4(d) for n=3. Required Claude audit of Part2 remains PENDING.

## Runs needed

Independent producer and independent certificate-checker runs will be assigned by the root orchestrator after the certificate format is fixed. Large evidence stays in /tmp pending AC-selected Padua cold storage; do not split artifacts to evade limits.

## Gate completed before mathematical generation (2026-11-01 09:23 UTC)

Read the complete 496-line `state/IDEAS.md` in successive ranges: all headings, IDs, aliases, summaries and every obstruction/disposition table. Read shortlist charter IDEA-048 in its contextual/baseline record; programme `IDEA?programme-ideas-claude-17` in full (including corrected non-certification wording); source THEORY -06 in full; part-1 theorem03 and exact-code construction; complete frozen `t3_certify.py` and `t3_degenerate.py`, measured count log; authoritative A5 and A4; literature/INDEX first before any literature comparison. The source manifests already pin the authoritative programme and part-1 inputs; source bytes used here agree with those pinned trees.

Mechanism/synonym searches covered ideas, state, theory/tracks, charter/programme/part-1 logs and literature with `piecewise`, `crease`, `crossing`, `degenerate`, `Krawczyk`, `Sturm`, `local.maxim`, `Padua maxima`, and the exact closest IDEA IDs. Closest predecessor is programme IDEA17's crease-aware counting project/source06 and charter IDEA048's geometry question. IDEA058 records the same general requirement for a proved finite reduction and rigorous checker; it is not a Padua count proof. Obstructions applicable here: finite floating samples do not prove completeness; one maximum per Lissajous cell is refuted; source root/early-return/near-coincidence failures remain genuine. Other registry obstructions concern different norms, fields or mechanisms.

Verdict: proof completion / variant of registered target, no priority or new-mechanism claim. Candidate route retained: exhaustive physical-coordinate signed-polynomial stationary systems. Separation criterion is a complete algebraic exclusion certificate for all signs, including crossings and boundary types; a missing sign/coordinate box or unjustified nonisolated-root discard kills the certificate. Cheapest decisive test: degree-three all-sign conic gradients and exact projection resultants before extending degree or implementing expensive interval subdivision. Alternative adaptive interval quadtree remains deferred pending this test; neither route's failure refutes A5.

2026-11-01 dated audit note: part-1 audit at `95279b833bca5967fcf47c1b71a56ff622185b4e` accepts the local theorem03. The required literal dependency remains `PD-T?proof-attempts-codex-03 (audit pending)` as requested. F2 explicitly requires rigorous (D) corner and (E) edge-node handlers. A new physical-coordinate reduction must cover those boundary types directly; the old trace does not discharge them.

## Reduction under development

For λ=max_sP_s, every active P_s is a strict relative local maximum wherever λ is. Interior flips at a zero cardinal force its gradient to vanish exactly; a regular crease or crossing with one regular zero is excluded. For cubics, a strict interior maximum must have negative definite Hessian: on a Hessian null line, the remaining cubic term is either odd or zero. Therefore a common factor of the two gradient components cannot contain a strict maximum, since their Jacobian has rank≤1 there. Coprime residual gradients can be projected by resultants in both coordinate directions, with rational Sturm isolations of their field norms. Every Cartesian pair of isolated coordinate roots must be checked; none may be silently skipped. Edge restrictions and inward derivatives cover all boundary decisions without inheriting the old floating (D)/(E) arithmetic.

## Actual commands and first diagnostics

All new Python commands use `PYTHONDONTWRITEBYTECODE=1 python -B`; no old module output writers are imported. Python3.12.14, SymPy1.14.0; exactfield QQ(sqrt2), Fraction intervals. No randomseed.

1. `python -B code/a5_explore.py > /tmp/a5_explore.txt` (full topic path in shell): completed228.5445s,1024masks.20patterns have an identically zero gradient component;1004remaining gcds have degree0; projection resultantdegrees984×(4,4),16×(2,2),4×(3,3). Diagnostic only; no count / completeness claim relies on this receipt.
2. `python -B code/a5_producer.py --limit128 --output /tmp/a5-n3-pilot.json --unresolved /tmp/a5-n3-pilot-unresolved.json`: completed first128masks,180129bytes; no unresolvedpairs,1acceptedinteriorroot,1exactregularcrossing. This is a prefix pilot, not a certifiedcount. Its output is never a successcertificate.
3. Full1024mask producer begun: `python -B code/a5_producer.py --output /tmp/a5-n3-interior.json.gz --unresolved /tmp/a5-n3-interior-unresolved.json > /tmp/a5-n3-interior.out 2> /tmp/a5-n3-interior.log`.
4. New physicalboundary producer begun: `python -B code/a5_boundary.py > /tmp/a5-n3-boundary.json 2> /tmp/a5-n3-boundary.log`.

Independentchecker implementer `/root/a5_checker` owns a5_checker paths. Its independentverifier reads certificate roots/partitions and checks them with Sturm counts; it does not rerun root search. Root will separately assign anotheragent to execute both producer and checker after the certificate is complete.

Preconditioner correction before the final proof run: root noted that selecting rationalC via a nonrigorous decimal approximation, though only a heuristic followed by exact checks, unnecessarily conflicted with the user's exact/outward-only request. Removed `sp.N` entirely. Every inverseentry is now normalized exactly in Q(sqrt2), enclosed by Fraction arithmetic with the verified radicalbracket, then an exact rational midpoint is selected and optionally simplified by Fraction.limit_denominator. The in-flight first full run used the earlier selector; it remains developmental only and the final producer will be rerun from the corrected code before promotion.

2026-11-01 09:34UTC source-impact update from root: part1 response at `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62` disposes F1–F6 minor findings. The theorem03 mathematical proof, code and scientific outputs are unchanged; its MEASURED trace paragraph moves out of the Statement and D/E obligations become explicit. Root integrates the changed authoritative records. Required literal dependency `PD-T?proof-attempts-codex-03 (audit pending)` is retained, with this dated note that its Claude audit is ACCEPTED and minor finding dispositions completed. No dependentmathematical run needs restart for this record-only change.

New reduction proof saved as result05 (`theory/proof-attempts-2-codex-05-cubic-finite-reduction.md`). The first complete boundary producer found6acceptededge roots and2non-node corners, with0unresolved dispositions acrossall3584canonicaledge masks. This is preliminary untilthe whole certificate and separate independent execution arecomplete. Checkeragent independentlyverified the suppliedboundaryrecords (reported6/2,71.88s); it did not rerun the boundarysearch. Finalall-in-oneproducer will regenerateallcode / evidencefromtheexact-preconditioner revision.

## Final degree-three producer completed (2026-11-01 09:45 UTC)

Frozen corrected modules completed successfully, with no unresolved disposition.
The single essential certificate is `outputs/a5_n3_certificate.json.gz`:
386415 bytes, SHA256 `401a99243ebeb7b3844216a47f8466bbb60086cbba71d2de2088d7626f532b2b`.
It decompresses to2809931 bytes, SHA256
`8340b56cfa17f735645c6585ea059bf489ee001cb76dcc254e24ea165242eae1`.
This is genuine compression of one artifact, not splitting to evade limits.
The committed compressed artifact is below1MB; no cold-storage dependency is needed.

Coverage:1024 interior masks;20 flat and1004 residual patterns;35376 Cartesian
pairs with8972 outside,23668 gradient exclusions,580 sign exclusions,2147 Hessian
exclusions,2 exact regular-crossing exclusions and7 accepted maxima. The four
edges have3584 canonical masks,44 constant restrictions,10508 root dispositions:
2596 outside,2972 derivative exclusions,2470 tangent-Hessian exclusions,2438 sign
exclusions,26 exact regular-edge exclusions and6 accepted edge maxima. Both
non-node corners pass every active-pattern inward-derivative test; both node
corners have value1. Producer receipt reports7 interior /6 edge /2 corner /15 total.
These values remain verification-pending until the separate checker and actual
independent producer/checker run pass.

Additional global predicates: all1004 non-flat gcds are constant; all20 flat
polynomials are bounded by225879/125000<3 using32 supplied exact panels each.
All13 non-corner accepted values are below15/4, while the exact corner value
is17/6+(2/3)sqrt2>15/4. Result07 explicitly rules out non-strict global plateaus
before using this separation. The two x=1 edge roots are identified exactly
with part1theorem03's y=±1/sqrt3 representatives and its local proof is reused.

Actual environment: Python3.12.14, SymPy1.14.0. Every proof inequality and root
partition is exact or outward Fraction arithmetic. Final code has no `sp.N` or
other floating approximation in preconditioner selection. The first complete
corrected producer ran from about09:35 to09:45UTC; only per-phase progress
seconds were logged, not an exact whole-command wall-clock measurement.


## Degree-three done criterion met (2026-11-01)

The complete separate checker exited0 in217.540s, verifying15 total =7 interior +6 open-edge +2 corner maxima, all five A5 obligations and the additional global fields. A different agent actually regenerated the full producer artifact byte-identically and then ran the checker on both its own and the developer artifacts; both exited0 (220.972s/220.474s), with every mathematical result identical. All14 malformed-certificate controls were rejected in both sessions. Code pins were unchanged before/after both complete runs. Actual commands and hashes are recorded in independent-execution-a5.md and independent-checks-a5-checker.md.

Results05,06,07 are now PROVED within their stated degree-three scopes; required Part2Claude audit remains PENDING. Result06 certifies15/7/6/2. Result07 proves exact global maximum17/6+(2/3)sqrt2, attained only at(−1,±1), after explicitly excluding non-strict global plateaus. Primary Table3 comparison agrees at the only certified degree n=3; no correction is made for n=6,7,8.

The n=3 computation is at its done criterion; no further n=3 search is needed. A5's same timebox continues for n=4 in the separately owned T-A5-n4.md and code/a5_n4* paths. Cases n=4,…,8 remain OPEN until their own complete evidence and independent checks exist.
