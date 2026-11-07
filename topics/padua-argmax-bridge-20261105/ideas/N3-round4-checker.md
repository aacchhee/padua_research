# IDEA?padua-argmax-bridge-phase-checker-r4 — Independent Arb enclosure repair gate

Aliases: hybrid sine-quotient enclosure; finite-harmonic collision fallback;
range intersection; same-tree independent phase replay.

Rules/input: `0039456f3cf45c3cf4564d57bea30f80156b5483`.
Assigned developer: Codex Sol medium; serving metadata not independently
exposed. Date: 2026-11-06. **Current status: MEASURED, bounded repair gate FAILED; see execution below.**
At preregistration, only this new gate record was written. Implementation
and controls began only after the coordinator published bda45a4; the full
replay remains unrun because the bounded gate failed.

## Scope and inherited gate

This is an implementation repair of IDEA-454/IDEA-320, closest verification
machinery IDEA-344. It is not a new mathematical certificate predicate or a
novel primitive. The inherited complete campaign gate is
`../novelty-gate-baseline.md`; the specific N3 gate is
`../novelty-gate-N3.md`. Those gates, the full IDEA-320/343/344/454/458
records, PD-T364's primitive/collision section, round-2 measurements and the
independent phase-math review were inspected. The new-main IDEAS summary
diff from c000899 to 0039456 was checked: its changes concern the Lanczos
frontier aliases/dispositions and do not change these N3 predecessors.
This targeted implementation continuation does not claim a fresh exhaustive
novelty search or external literature comparison. No external theorem is
transferred. The proportional workflow changes were also read.

The original independent finite-cosine kernel is frozen at SHA-256
`236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6`.
Its actual full n17 replay checked1288/1288leaves, with924passing and364
failed sufficient enclosure predicates, using60.60368947CPU seconds.
Failures were184far and180corner-orbit-plus-defect; all28local and32outside
leaves passed. This is the precise failure being repaired, not a pointwise
counterexample or failure of PD-T364.

The target is the **same immutable original full n17 compact candidate**:
plain81585bytes, SHA-256
`64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b`;
gzip5266bytes, SHA-256
`80dcb2db069332e018653931bdb94e3995ceca5c9d96741fd1b87110474267a6`.
The gzip decodes to those exact plain bytes. No new producer tree,
changed leaf kind or relaxed threshold is substituted for this target.

## Proposed independent enclosure and assumptions

Keep Arb real-ball arithmetic and the whole-sum nonsmooth mean-value
lemma, complete projected-center minimum, four-reflection summation before
absolute values, endpoint multiplicities, strict predicates and complete
tree geometry already specified by PD-T364. Do not read, copy, import or
link the MPFR producer's interval implementation. The shared mathematical
identity and certificate schema are explicit common dependencies.

For each integer k>=1 and real argument interval Z, evaluate

    R_k(z)=sin(kz)/sin(z),
    R'_k(z)=[k cos(kz) sin(z)-sin(kz) cos(z)]/sin(z)^2

**only if the outward Arb enclosure of sin(Z) excludes zero**. These are
identities on that whole interval, not pointwise substitution in an interval
crossing a collision. Near a denominator zero or whenever this test fails,
retain the original everywhere-valid finite harmonic formula and derivative.
A tiny nonzero denominator may still yield a broad quotient; it creates no
permission to discard the finite bound or widen an accepted predicate.

Independently intersect every available valid range with the global bounds

    R_k(Z) subset [-k,k],
    R'_k(Z) subset [-floor(k^2/2),floor(k^2/2)].

The second constant follows directly from the finite harmonic expansion:
R_k is [k odd]+2 sum cos(jz) over1<=j<k with j congruent to k-1 modulo2.
Hence |R'_k|<=2sum j: this sum is k^2/2 for even k, and (k^2-1)/2 for odd
k. Thus the requested k^2/2 bound is safe, with an exact integer refinement
for odd k; k=1 gives derivative0. The value bound follows from the k unit
complex exponentials, or by the finite cosine triangle inequality. These
are routine verification arguments submitted for source/math inspection,
not a new separately registered theorem.

Each intersection must itself outward-enclose the exact intersection.
An empty intersection among purportedly valid bounds is an implementation
contradiction: reject the arithmetic call and record it. Never replace it
with zero, select a more convenient bound or average endpoints. Avoid any
assumption that outward conversion of an intersection ball makes its
printed endpoints literally nested inside every input ball.

For predictable comparison with the frozen kernel, retain its valid final
S/corner upper bounds as alternative bounds and take the minimum with the
new valid bounds; retain its valid projected lower bound and take the
maximum with the new one. This guarantees the final scalar bounds are no
weaker than the baseline without relying on interval-operation monotonicity
under Arb radius rounding. Preserve exact rational strict comparisons.
This extra baseline work is included in the runtime gate below.

The exact local patch through every integer n2..128 is separately proved
under independent receipt
e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0,
with common kappa1/16000 and phase square1/128. It is not proved by this
repair. Original n17's28local leaves already passed with the old inherited
radius, so patch expansion is unnecessary to repair this frozen tree.
Any later guard integration uses that published finite theorem; no caller
success flag or future all-degree constant is accepted. New code follows
the current rule against pinning prose: pin code/data/evidence and identify
mathematical prose by reviewed publication, without a new prose-hash guard.

## Separation criterion and applicable obstructions

The falsifiable computational distinction is **independent acceptance of
the same complete1288-leaf tree** within a bounded cost, where the frozen
finite-cosine-only implementation failed364leaves. A merely compiled kernel,
tighter point values or fewer failed sample boxes does not satisfy it.
Producer-bound agreement is diagnostic only, never the acceptance premise.

PD-N079 still prohibits primitive-only corner dominance. PD-N085's affine
sign obstruction is not bypassed by asserting fixed cardinal signs;
PD-N086's coarse-sign obstruction remains respected by derivative hulls
across zeros. A zero denominator invokes a valid finite formula. Complete
odd-center coverage, endpoint multiplicities and strict corner exclusion
remain mandatory. No Bernstein predicate changes are proposed.

Novelty verdict: **implementation/enclosure variant, no novelty claim**.
Scope of a failure: this specified hybrid repair on the frozen n17 tree;
not all Arb enclosures, phase certification, or PD-T099.

## Ordered tests and predeclared kill criteria

After the coordinator publishes the boundary, perform these in order:

1. Bounded controls on the changed arithmetic only: exact/symmetric
   collision neighborhoods about0 and integer*pi, denominator crossings,
   k=1/2/3/17/18, finite-polynomial value/derivative cross-checks, valid
   intersection/global clipping, exact midpoint/radius behavior, and the
   existing input/build-corruption controls relevant to modified code.
   Any contradictory/empty valid intersection or unsound enclosure stops
   the run immediately. A denominator crossing must execute fallback.
2. Cheapest decisive leaf gate: the prior far failure root0/path01010
   must pass strict far comparison (oldS upper12.86916394136224 versus
   Lc lower8.6179478249936). Four fixed prior corner-orbit-plus-defect
   failures must also pass their **original** predicates:
   root0/path1100111, root0/path11011111, root3/path0011000,
   root0/path1111111111101111. The short and long paths exercise broad
   and narrow boxes with the same periodic collision handling. This is
   bounded diagnosis, not a complete-cover certificate. If any remains
   unresolved, stop this initial hybrid variant before the whole replay,
   recording its exact inequality and timing; no silent higher-order or
   internal-subdivision rescue is included in this gate.
3. Freeze the changed source and request a distinct agent's focused
   arithmetic/source/math inspection, including quotient derivatives,
   denominator tests, intersection validity, nonsmooth whole-sum use,
   geometry, complete profiles and build/input provenance. Material
   changes need the focused re-review required by the current workflow.
4. Only after that inspection passes, execute **ONE** whole original
   candidate replay, no max-leaf cap and no changed tree. Stop at120CPU
   seconds if unfinished and record partial status. Pass requires all1288
   original leaves checked, zero failed predicates, zero pending regions,
   accepted=true, and at most120CPU seconds. Any remaining failure or cap
   makes this fixed repair unsuccessful and is recorded precisely.

The120CPU-second cap is approximately twice the measured60.60-second
baseline and includes arithmetic plus checker work; compiler subprocess
CPU must be reported separately so the budget is not hidden by Python's
process_time accounting. It is a repair cost gate, not the inherited B2
box-growth law. No n128 whole-cover run, new degree claim, automatic
new tree, duplicate full replay or higher-order escalation is authorized
by a passing sample gate alone. Root retains the campaign round budget.

## Actual results and disposition

At preregistration, no changed kernel, bounded control or new full replay
had run. The following dated execution is the resulting disposition.
No PD-N or final IDEA allocation requested. Durable predecessor evidence:
`../evidence/phase-checker-full-n17.json`; independent source review:
`../independent-checks-phase-math.md`. Original records remain unchanged.


## Execution at published boundary bda45a4 — bounded failure, no full replay

Parent authorization followed published commit
`bda45a4c1392bea87de0841b6b23e5c35b2a694b`. A separate
`../code/phase_checker/hybrid_kernel.cpp` was implemented without reading or
copying producer arithmetic. The original kernel remains byte-identical at
23611645... . The existing provenance builder now selects the new fixed
source name; all fresh-build/dependency/input machinery is preserved.

Executed:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/hybrid_controls.py

All40ratio controls pass (k1/2/3/17/18, exact/crossing/narrow integer*pi and
away intervals). All4independent triangular-polynomial value/gradient
diagnostics pass. Contradictory intersection is rejected with code3; JSON
negative controls pass. A small uneven-endpoint box returns finite bounds.
Each gate case's retained baseline7-tuple matches the frozen original
receipt **bit for bit**. Final hybrid-combined upper/lower bounds are no
weaker on those cases. Numerical reference diagnostics supplement source
review; they do not constitute a generic proof of the implementation.

With independent Lc lower8.6179478249936:

| Original root/path | Kind | New S upper | New corner upper | New defect lower | Original predicate |
|---|---|---:|---:|---:|---|
| 0/01010 | far | 7.63022063807659 | 6.670775632801408 | 0 | PASS |
| 0/1100111 | corner-orbit-plus-defect | 9.03124292608716 | 8.742498890697016 | 0 | FAIL |
| 0/11011111 | corner-orbit-plus-defect | 8.843523044070748 | 8.592540147308648 | 0 | FAIL |
| 3/0011000 | corner-orbit-plus-defect | 9.031242885518816 | 8.742498890669053 | 0 | FAIL |
| 0/1111111111101111 | corner-orbit-plus-defect | 8.616364533784965 | 8.615885355124734 | .421587417135256 | PASS |

Thus **gate2 fails**. The implementation repairs the nominated far box
and the narrow corner/defect box, but three nominated corner/defect
predicates remain unresolved. Their natural projected-defect lower bounds
are0, and two also retain corner upper values above Lc. These exact
inequalities are the observed obstruction; no universal causal diagnosis
of all collision or gradient dependence is claimed.

Checker CPU for all bounded controls was1.264207362seconds; compiler child
CPU was separately1.054607seconds. Two kernel calls per nominated leaf
(final combined and diagnostic baseline/hybrid pair) took.159–.224CPU
seconds. No total-full-cover timing is inferred. The120CPU full-replay gate
was not reached or tested.

Frozen implementation/controls/evidence:

- hybrid kernel SHA-256
  9a976e77d861c291468d6bfa4d2104c6c42ace953781ce1c5ff1a43073505d7d;
- provenance builder SHA-256
  406368f07354f7d0d861eb92aa0bd2fc720ca9fccc86f8ed650d7da0872e8c18;
- bounded control source SHA-256
  e388f935f70dadfc342f4b9f9523e577fb018a65fef485cdf815ca3d05e71164;
- short evidence `../evidence/phase-checker-round4-bounded.json`, SHA-256
  8bb4097c650d2429488a037cddd0c01df2df15bdd67538026b64e124769a441e.

The evidence pins the full local receipt with source/dependency/binary
closure and the exact unchanged candidate identity. A distinct reviewer
was given the frozen source and bounded results. No full original-tree
replay, altered tree, fallback refinement, new degree or second kernel
iteration was launched. Original receipts and old theory records remain
unchanged. Disposition: **specified hybrid repair FAILED at its bounded
leaf gate; stop this variant and retain it**. This is neither rejection
of all phase certification nor a mathematical counterexample or new PD-N.
Any next implementation is a separately authorized and gated step.

### Independent source-review counterexample, same frozen candidate

The distinct reviewer `/root/review_phase_round4` actually exercised the
frozen hybrid and reported an additional diagnostic robustness failure:

    phase_ratio(k=1, turn=-2, lo=.125, hi=.375)
    return code 0
    output [1,1,0,0,1,1,NaN,NaN]

Here exact R_1=1 and R'_1=0. This execution is attributed to that reviewer,
not a new run by the developer. It exposes a gap outside the40developer
ratio test cases. The reviewer is isolating the squared-denominator ball
and indeterminate-intersection path; its final report owns the independent
finding and reproduction. No false full-certificate acceptance has been
established: the phase-bounds API separately rejects nonfinite final bounds.

The frozen source/evidence hashes above are retained. No source fix,
additional arithmetic campaign or whole-tree replay follows this finding.
The specified round4 variant remains stopped. Parent requires publication
of this failed checkpoint before a separately scoped round5 bug repair;
that future step does not erase these three original leaf-gate failures or
this NaN-success counterexample. The next gate still requires every
original bounded leaf predicate and a focused review before any full replay.
