# A5 independent certificate checker — development and mathematical predicates

Rules read at `3db1eee3fd9507c103c496bdf3da8157331359c5`.
Role: independent checker implementer, Codex `gpt-6.1-sol` xhigh (assigned
allocation; no separate serving-model receipt is exposed). This is supplementary
verification, not the required Claude audit. Only this record and new
`code/a5_checker*` / `outputs/a5_checker*` files are owned by this agent.

## Scope and gate

Read the complete task attachment, AGENTS, WORKFLOW and CODEX at the rules head;
the complete `state/IDEAS.md` headings, identifiers, aliases, summaries and all
obstruction/disposition tables; full shortlisted programme IDEA-17, IDEA-048,
source THEORY -06 and OPEN_TARGETS A5; part-1 THEORY 03 and its audit. Mechanism
searches included `crease`, `arrangement`, `Lebesgue`, `local.max`, `degener`,
`certif`, `Sturm`, `Krawczyk`, `resultant` and `sign.pattern` across registries,
topics, tracks and the literature index. Closest source: IDEA-048 / programme
IDEA-17 and its existing measured maxima list. This is proof completion of that
registered finite target, with no priority or novelty claim. Applicable
obstructions are the source's floating degeneracy decision, early return over
patterns, unjustified Newton-outside discard and approximate crease coincidence.
The decisive test is rejection unless all 1024 masks and every projected-root
Cartesian pair have a verified disposition. Part-1 THEORY 03 only covers the
two `degenerate_max` calls; audit F2 explicitly leaves old corner D / edge-node E
handlers outside it. This checker does not reuse those floating handlers.

The checker reconstructs ten exact degree-three cardinals by its own monomial
Vandermonde inversion, imports no producer or old search module, uses no root
isolation, and performs no subdivision/search. Its certificate format is
`code/a5_schema.md`, communicated by the independent producer developer before
implementation. Its only numerical quantities are timings in the execution
receipt. All proof arithmetic uses SymPy exact algebra over Q(sqrt(2)), rational
Sturm sequences and Python Fraction intervals.

## Why the verifier predicates suffice

These are explanations of the finite verifier's predicates, not an independent
claim that an unexecuted certificate passes. The orchestrator owns the separate
durable finite-reduction theory.

1. **Envelope and cubics.** Pointwise lambda=max over every signed sum P of the
   cardinals, since each absolute value independently chooses its sign. If lambda
   has a strict local maximum z, every active P has a strict local maximum at z:
   P(w)<=lambda(w)<lambda(z)=P(z) locally for w!=z. An interior cubic strict local
   maximum has zero gradient and negative definite Hessian. Indeed, its Hessian
   is negative semidefinite; a null direction has an odd cubic restriction plus
   its constant value, which either changes sign or is constant and hence cannot
   have a strict maximum. Thus singular Hessians exclude strict cubic maxima.

2. **Gradient factor and projection.** The checker verifies A=g*a and B=g*b by
   exact polynomial division. On g=0 the two Hessian rows are a*grad(g) and
   b*grad(g), so the Hessian determinant vanishes there. A nonzero constant
   residual derivative excludes residual critical points. Otherwise it
   independently recomputes both nonzero resultants, their rational conjugate
   norms and squarefree parts. Every real residual zero has each coordinate
   among the corresponding norm roots, even when the norm also adds conjugate
   or leading-coefficient artifacts. Hence all Cartesian coordinate-root pairs
   cover all remaining interior critical points. No generic-fiber or simple-root
   assumption is made.

3. **Supplied root partitions.** Each nonsingleton interval has nonroot rational
   endpoints and Sturm variation difference one. Each singleton is checked by
   exact evaluation. Intervals are ordered/disjoint; touching at a root is
   forbidden. Their number equals the total distinct real-root count from
   variations at minus/plus infinity. These facts prove no root was omitted or
   duplicated. The checker never constructs isolating intervals. It requires
   exactly one disposition for every Cartesian pair in the prescribed order.

4. **Interval exclusions.** The fixed rational sqrt(2) bracket is verified by
   squaring its positive endpoints. Fraction interval addition and multiplication
   enclose their full ranges; powers include zero for even powers of intervals
   crossing zero. Induction through each polynomial's monomial expansion proves
   inclusion. A box entirely outside the open square, a gradient component
   excluding zero, a strictly incompatible signed cardinal, or failure of the
   Hessian's negative definiteness excludes an interior strict maximum. The
   Hessian test uses Hxx>=0, Hyy>=0 or det(H)<=0, each verified throughout its box.

5. **Exact regular creases.** At an alleged regular crease stationary point the
   checker verifies the point in Q(sqrt(2)), both gradient identities, an exactly
   zero cardinal and a nonzero physical cardinal gradient. The two active signed
   polynomials differing at that cardinal cannot both have zero gradient, so
   lambda cannot have an interior maximum there. Injectivity is verified on the
   whole projected pair box; an approximate coincidence or outside Newton iterate
   is never used.

6. **Injection and Krawczyk.** With rational invertible C and interval Hessian H,
   the checker bounds every row sum of |I-C*H| by a number below one throughout
   the stated convex box. Integrating along a segment proves contraction of
   T(z)=z-C*grad(P)(z), and hence injectivity of grad(P). The interval expression
   c-C*grad(P)(c)+(I-C*H(Q))*(Q-c) encloses T(Q). Its strict containment in Q and
   contraction prove existence and uniqueness of a gradient zero there. An
   exactly supplied stationary point may establish existence instead. The
   accepted larger box covers the entire projected pair box, lies strictly in
   the square, has Hxx<0 and det(H)>0, and has every signed cardinal strictly
   positive. Its unique stationary point is therefore a strict lambda maximum.
   Accepted boxes are pairwise disjoint and IDs unique, so counting them cannot
   double-count roots. A root may be established in the larger box without first
   proving that it lies in the original projected pair box: the larger box
   proves its existence; uniqueness covers all candidate roots in the pair box;
   and global disjointness prevents excess counting.

7. **Edges.** Each of the four edges is checked separately and exhaustively.
   Identically zero restricted cardinals are derived exactly. Fixing their sign
   bits to zero gives precisely the canonical patterns, without changing any
   restricted polynomial. Every nonconstant restricted cubic has its derivative
   norm roots covered by a supplied Sturm partition, with every root disposed
   of. A strict maximum of a nonconstant univariate cubic must have second
   derivative strictly negative. A regular zero of a restricted cardinal excludes
   a lambda maximum by the two active tangential derivatives. For an accepted
   edge maximum the checker proves one tangent root by sign change and strict
   concavity, or an exact point and strict concavity. Nonzero restricted
   cardinals have strict fixed signs. An identically zero cardinal is divided
   exactly by normal-side; the quotient's nonzero sign on the edge determines
   the actual one-sided cardinal sign. This is verified for every such cardinal,
   with no assumption about a factor's multiplicity. If the quotient vanishes,
   this sufficient predicate fails and cannot accept a certificate.

   The uniquely derived full sign mask represents lambda on a relative open
   neighbourhood of the edge root. Its strictly negative inward derivative
   persists locally by continuity. Integrating in the inward coordinate, followed
   by the strict tangent maximum on the edge, proves a strict relative square
   maximum. A strictly positive inward derivative instead excludes one. IDs are
   contiguous globally and root intervals on the same edge are disjoint.

8. **Corners.** All four corner records are mandatory. At a cardinal node lambda
   is one, while lambda>=|sum L|=1 globally, so this point is not a strict local
   maximum. At a claimed maximum the checker derives zero/nonzero cardinal sets
   and independently enumerates every active full sign mask. Both inward
   derivatives of each active P must be strictly negative exactly. Finiteness
   and continuity make this decrease uniform in a sufficiently small inward
   quadrant, proving lambda's strict relative maximum. No corner is silently
   inferred from parity or the old numerical handler.

## A4 limitation and independent assessment

The strict-local-maxima list alone does not exclude a non-strict global plateau.
This was reported to the orchestrator before any global assertion. The optional
`global` extension now verifies the following additional evidence, without
changing the count-only assertion when that extension is absent.

For every nonflat polynomial it verifies constant g, so the already checked
nonzero gradient resultants apply to the full gradient. A cubic local maximum
with a singular Hessian is constant along its null line; nearby line points
remain local maxima and hence critical points. The full-gradient resultants
permit only finitely many real critical points and exclude such a maximum.
Every flat/univariate signed polynomial instead gets a supplied exact partition
of [-1,1] into 32 panels. The checker verifies complete coverage and the stated
interval upper bound below 3 on every panel. Thus no active polynomial at a
global value greater than 3 is flat. Every active interior polynomial at a
global maximum is consequently a strict local maximum; finiteness of the active
set and the gap to inactive polynomials make lambda's maximum strict as well.

On an open edge each constant restricted polynomial is explicitly checked to
have value +1 or -1. At a global maximum above 3 every active restriction is
therefore a nonconstant cubic. Its second derivative must be negative: zero
would give either a changing odd cubic or a constant cubic. This puts it in the
complete edge root enumeration. The gradient, sign, Hessian, regular-crease and
positive-inward-derivative dispositions all exclude an active global maximum.
The remaining root disposition proves strict relative maximality, including
strict inward descent. Thus the whole global maximum set is contained in the
strict list after the flat/global extension has passed.

Finally every supplied interior and edge value interval must enclose the range
independently computed over its accepted box and have upper bound below 15/4.
Both nonnode-corner values must equal exactly 17/6+2*sqrt(2)/3, with a verified
lower bound above 15/4; node corners have value one. This proves the two nonnode
corners are precisely the global maximizers. Omitted value rows, flat masks or
panels are rejected. The two part-1 representatives are identified by exact
tangent derivative divisibility by 1-3*y^2 and the sign of their disjoint root
intervals, giving y=+/-1/sqrt(3) without numerical identification. The named
part-1 dependency remains `PD-T?proof-attempts-codex-03 (audit pending)` with the
dated audit acceptance handled by the orchestrator.

## Actual runs so far

All commands use `PYTHONDONTWRITEBYTECODE=1 python -B`; no old module cache is
written. Python 3.12.14, SymPy 1.14.0. The checker does not require python-flint.

* Reconstructed all ten cardinals independently; exact V*V_inverse=I and sum L=1
  passed. Exact Hessian construction and Q(sqrt(2)) sign checks passed.
* Checked the supplied singleton partition {-1,0,1} of t^3-t. Deliberately omitted
  root, multiple-root interval and duplicate singleton variants were rejected.
* Invoked the actual command on the producer's incomplete 128-mask pilot:
  `python -B .../code/a5_checker.py /tmp/a5-n3-pilot.json --interior-only`.
  It returned exit status 1, `all 1024 sign patterns are required`, as required.
* Independently invoked `check_edges` and `check_corners` on the completed first
  boundary artifact `/tmp/a5-n3-boundary.json`. All four edges / 3584 canonical
  masks passed, giving six strict edge maxima; both nonnode corner maxima and
  both node exclusions passed. The edge verification took 71.880 seconds.
* The first full interior integration attempt used generic SymPy resultant
  coercion and was deliberately stopped (exit 143), incomplete and not a pass.
  The final implementation specifies the exact coefficient ring
  Q(sqrt(2))[retained-coordinate], avoiding large unsimplified radical fractions.
  Twelve exact old/new resultant comparisons passed (both projections at masks
  1, 9, 66, 399, 845, 1022). The full integration was restarted after this change.
* The restarted frozen checker completed the preliminary first interior artifact
  `/tmp/a5-n3-interior.json.gz`, hash
  `7b1f83897d018a2166c004c65ab00629a2cb50d1004e9e1b19e53220a773e569`
  (253,723 bytes), in 136.290 seconds, exit 0. It verified all 1024 masks (20
  flat, 1004 residual) and all 35,376 Cartesian pairs: 23,668 gradient exclusions,
  8972 outside, 2147 Hessian, 580 sign, two exact regular-crease exclusions and
  seven accepted roots. Thus the integration reports seven strict interior
  maxima, explicitly scoped `interior only; closed-square count NOT verified`.
  Receipt `outputs/a5_checker_interior-integration.json`: hash
  `b7138bc9f4d34d54f0b0aaa47159207aa821fce00db75de95abdf1d25c9d6781`,
  8465 bytes. This preliminary producer artifact preceded the producer's removal
  of a numerical preconditioner heuristic; every supplied rational preconditioner
  was rigorously checked. The final producer uses exact arithmetic throughout
  and will be independently checked again as the complete closed-square artifact.

Frozen checker SHA-256, communicated to the orchestrator before independent
execution: `d32810f1b478315cd240f7f68c41177fd97836c8337aefd9de8aa90203884cde`.
The optional adversarial runner hash is
`28353ea677c7a99c8a1ea1e8ed6f41afc27972bba19a1b5c0618ef7e09c12362`.
Both are frozen through full integration and the different-agent rerun unless an
essential bug requires a documented correction/restart.

The separate negative-control runner supplies 14 deliberately invalid mutations
when the global extension is present: omitted/duplicated interior masks, a false
gradient division, omitted projected root, omitted Cartesian pair, unknown
disposition, omitted edge, omitted canonical edge pattern, omitted edge root
disposition, omitted corner, false node classification, omitted flat mask,
omitted flat covering panel and false flat upper bound. Its report records the
rejection reason for every mutation and the exact certificate/checker hashes.
It does not replace a positive verification of the original certificate.

Planned final integration commands (not execution claims until receipts below):

```text
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker.py topics/padua-proof-attempts-2-20261101/outputs/a5_n3_certificate.json.gz > topics/padua-proof-attempts-2-20261101/outputs/a5_checker_full-integration.json
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_adversarial.py topics/padua-proof-attempts-2-20261101/outputs/a5_n3_certificate.json.gz > topics/padua-proof-attempts-2-20261101/outputs/a5_checker_adversarial.json
```

These are implementation/integration checks, not yet a complete closed-square
certificate execution. Full producer/checker integration and the required
different-subagent execution remain pending at this checkpoint. An executor
must retain its own output; this implementer's run cannot replace that
independent execution.
