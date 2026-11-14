# D10 finite-cover contract — distinct supplementary mathematical review

2026-11-06. Reviewer: distinct Codex agent `/root/d01_corner_review`,
requested Astra high; actual serving metadata are not independently
exposed. Ordinary mathematical review of the Sol xhigh developer's
bounded analytic block. Rules were read at
`9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf`; the rule files are unchanged
at review head `96882eaa270adbde69ce24e731256eebbbd03adb`.
Root owns Git, shared records, source adoption and any subsequent run.

**Verdict: ACCEPTED as a proved sufficient implication, with no unresolved
finding.** A complete finite cover satisfying these independently validated
premises implies the stated degree-512 maximum and exact two-corner equality
set. No completed cover or new degree is established by this review.
In particular the successful actual-corner patch remains an explicit
premise, distinct from its sufficient three-loss theorem or a reported
producer success.

## Frozen inputs and actual scope

The author confirmed the following files frozen at 18:16:28 UTC. I read
the draft completely, reviewed the final changes and independently checked
the final SHA256 identities:

| File | SHA256 |
| --- | --- |
| `theory/D10-cover-contract.md` | `777f5815cc6d737d1e45c43d3069ad9bf801a2f8226aeef76c4097dd3ef043dd` |
| `ideas/D10-cover-contract.md` | `b899dec4c2e2a4f952db3122f52c2c9abe932e83a677d139bd9b4b116785890c` |
| `attempts/D10-cover-contract.md` | `3e12baaaaa28b0b9c6a5ee08b1a441b546586c11e7deac0b2703e614596f1277` |

The same-session full registry reading and subsequent complete current
delta review are retained from D09. The registry remains exactly
`08e6886269a7bb76eaeb60b57f37935f5a390f37ae1df5d0167cdaac2ed7093a`.
Fresh searches and focused rereads covered finite covers, phase charts,
projected floors, interpolation, corner predicates and point API guards.
The full mathematical shortlist includes PD-T364's phase-structure,
the phase-checker reduction, N3 bootstrap-cover and its candidate,
C03 effective assembly, C02 dense-band floor, D08 point-box/corner/norm
and the accepted D09 norm. The C11 point entry and its accepted review
were inspected at the relevant domain/failure boundary.

This is an explicit adapter of the existing PD-T364 cover mechanism.
The author's preliminary-sketch/gate chronology is disclosed canonically
in `attempts/D10-cover-contract.md`; I do not reinterpret that history as
a prospective new-mechanism gate. The consolidation disposition is correct.
The period adapter, Peano argument, phase cover and near/far/corner logic
are not claimed as new. No historical priority or external-literature
claim is made. The inherited cusp and sign obstructions remain in force.

## Physical coverage, parity and strictness

The n=512 convention is consistent throughout: m=513, the exceptional
kernel coefficient is one, the odd board contains `2nm` terms and S uses
the factor `1/(2nm)`. The physical centers have `J+K` odd and the
explicit inward admissibility constraints stated in equation (2).
There are `513*514/2=131841` such centers. Since n is even, exactly
`(0,m)` and `(n,m)` are endpoint/endpoints of odd parity, giving the
two physical nonnode corners `(1,-1)` and `(-1,-1)`.

I reconstructed the PD-T364 cover: the two odd vertices of each physical
mesh rectangle have normalized L1 distances summing to two. One therefore
has distance at most one, including mesh edges, node points and tied
boundaries. Using an adjacent interior rectangle at the outer boundary
preserves the explicit endpoint signs. There is no nearest-center
uniqueness requirement and no mesh interchange.

The full reflection identity is `lambda=S-Delta`, with
`Delta>=max(Q_v,Q_h)>=0`. Projected defects supply inequalities, not
replacement equalities. C02's n>=160 dense-band theorem gives each
applicable projection strictly above 1/32 for all signed phases with
rho<=1/2. Every noncorner center has at least one interior coordinate,
so one applicable projection exists, even at a physical edge. Thus the
safe subtraction 1/32 covers every such center, including zero phase.
At actual corners the projections are not substituted for the separate
corner premise. C02's proof and exact normalization retain both parity
meshes, endpoint orientations and finite polynomial collision values.

At a corner center, inward admissibility makes the absolute phases the
actual inward angular distances times their respective mesh factors.
Zero phase is exactly that physical corner; a nonzero admissible phase
cannot map back to it. For even n, x reflection preserves checkerboard
nodes, endpoint weights and the cardinal basis and exchanges the two
nonnode corners. This gives their equal value without assuming global
optimality. The odd-n y-reflection alternative in the predecessor is not
needed at fixed n=512. Physical node corners have value one and occur as
nonzero phases in the odd-center cover; they are not extra origin cases.

## Exact symmetry and point API boundary

Translations by `pi(p,q)` with p+q even preserve the finite odd board;
coordinate negations preserve both parity and the separately even finite
kernel. Reducing `(a+b)/2` and `(a-b)/2` independently modulo integers
therefore produces a closed-diamond representative for every rational
pair. The identity `|s+t|+|s-t|=2max(|s|,|t|)` proves the stated bound,
including half-integer ties. Coordinate absolute values place it in T.

The proposed finite orbit enumeration yields a unique cache representative:
from a representative in `[-1,1]^2`, any reflected/translated representative
in T needs integer translations only in `[-2,2]`. Reflections preserve the
even translation lattice, so the list is the same full T orbit from every
starting representative. Taking its lexicographic minimum is legitimate
also on the closed diagonal and at its endpoints. For vertices in the
unit square the fold `(a,b)->(1-a,1-b)` above a+b=1 is exactly translation
by `(-1,-1)` followed by reflection.

Only the S evaluation is folded. The physical center, actual radius,
corner geometry and defect domain are not changed by cache equivalence.
The C11 entry requires rational nonnegative a,b with a+b<=1 and integer
2<=n<=2147483647 on its reviewed LP64 domain. Every canonical point meets
the phase guard, but a valid input is not promised successful evaluation.
Root/sign/partial-sum/nonfinite failures must remain rejecting outcomes.
Source/arithmetic identity and degree are part of the cache key. The
contract does not extend C11 to raw out-of-triangle vertices or claim its
whole-box evaluation has been implemented.

## Peano factors and conditional near/far predicates

D08's ordinary signed-family Peano bound is valid globally in radians
with curvature remainder

    (M/2)[(alpha-alpha_l)(alpha_h-alpha)
               +kappa^2(beta-beta_l)(beta_h-beta)].

Under alpha=pi*a and beta=pi*b the interpolation weights are unchanged
and each curvature product gains pi squared. Each product is nonnegative
inside B, so the outward replacement by `p_hi^2` gives exactly D10 (4).
Replacing the bilinear interpolant by the largest vertex upper and the
products by one quarter of each side-length squared gives (6), with
factor `M*p_hi^2/8`. There is no board-term counting factor and no
differentiation of the nonsmooth S. The norm M=34 is independently accepted
globally in D09 for precisely the needed complete signed families.
Zero-width rectangles use the indicated one-dimensional rule; point
rectangles use their point upper. Every patch must be checked to lie in B.

The rational cut directions are correct:

    1/(2*p_hi) <= 1/(2*pi) <= 1/(2*p_lo).

Consequently the actual closed near set is contained in Q_N and the
actual closed far set in Q_F. Their rational proxies may overlap and may
contain points outside the corresponding actual branch. They are used
only as domains on which to upper-bound S. Subtracting 1/32 occurs only
for a noncorner physical point on the actual rho<=1/2 branch. The far
branch uses no floor. Thus the construction does not make the invalid
whole-box inference from mere intersection with the near diamond.

Both comparisons are strict rational comparisons against L<=Lambda_c.
An empty proxy makes its actual branch empty; a nonempty proxy may impose
an unnecessary but safe stronger condition. The optional whole-near test
`2*p_hi*max_P(a+b)<=1` truly puts every point of P inside the actual
closed near domain. Equality rho=1/2 is covered; ordinary SPLIT requires
both nonempty proxy predicates, while the optional whole-near guard can
use the valid near argument alone. No floating midpoint or caller Boolean
can establish these domain facts.

## Closed rational geometry and finite maximization

Clipping by T and the rational proxy lines produces compact rational
polygons, including dimension zero and one. Pairwise supporting-line
intersections and exact feasibility checks determine their vertices;
tangencies are retained rather than discarded as empty. On a segment,
a rational quadratic has its maximum at an endpoint or at its rational
stationary point. For a full-dimensional polygon, an interior maximum
has zero gradient. An invertible rational Hessian yields a rational
stationary point. If the Hessian is singular, any stationary interior
point has a nonzero null direction along which q is constant; extending
to the compact polygon boundary gives the same value among the boundary
candidates. Linear and constant cases are already included. This proves
the finite rational maximum rule without an optimizer or root isolation.
The uniform bound (6) is also safe if the checker chooses to omit this
sharper rule.

The arbitrary-union coverage method is sound: supporting-line arrangement
faces include dimensions two, one and zero. Membership in each closed
convex patch is constant on each relatively open face because all its
boundary lines are included. Checking a rational relative-interior point
therefore checks that entire face. The checker must reconstruct the
arrangement, incidences and nonempty faces, rather than trust a submitted
sample list. Including all dimensions prevents a missed diagonal edge,
isolated vertex or boundary intersection.

The alternate complete binary tree covers `[0,1]^2` by induction when
each internal node has both exact children, a common rational split and
strict progress. Complete prefix-free leaves clipped to T cover T.
For a rectangle inside that root, the minimum of a+b is `a_l+b_l`;
its intersection with T is empty exactly when this minimum exceeds one.
Equality leaves a point and must not pass the outside test. Missing
siblings, duplicated leaves, gaps and pending leaves cannot support a
cover conclusion. Degenerate triangles/patches remain valid when their
closed union and enclosing boxes are checked exactly.

## Corner witness conversion and sufficient implication

The optional three-point witness is itself correctly scaled. With
`u'=a_*^2/2`, `v'=b_*^2/2`, the physical squared-phase coordinates are
U=pi squared times u' and V=pi squared times v'. The minimum rational
loss ratio q ensures the D08 loss premises with `c=q/pi^2`. Its slope
condition is therefore

    q > (M*pi^4/6) max(u',kappa^4 v').

Replacing pi to the fourth power by `p_hi^4` is safe. This is why (9)
requires pi to the fourth power, not merely pi squared. Its positive
barrier coefficient is bounded below by the stated numerator divided by
`p_hi^2`. The lower-pi tests `p_lo*a_*>=1/2` and `p_lo*b_*>=1/2`
ensure the full inward half-radius diamond lies in the phase rectangle.
For the illustrative 1/4 and 3/16 choices, pi>3 suffices. The origin
value stays the symbolic actual Lambda_c; the certified L is used only
to produce safe losses. The source calls are actual corner/cardinal
values, not substituted common-primitive values.

The global implication then follows pointwise. Choose an admissible odd
center for each physical point, take absolute phases to obtain a point
of T, and use a covering accepted patch. FAR gives strict comparison at
every center. SPLIT gives strict comparison at noncorner near points
through the floor, at all far points through S<L, and at nonzero-phase
actual-corner near points through premise 4. The only possible equality
points are the two actual corners, and PD-T364/reflection supply their
common value. This proof needs neither N3's finite energy premise at512
nor a bootstrap assumption about an unknown maximizer.

The implication status is therefore PROVED even though an application
still requires the actual successful corner witness and every accepted
cover predicate. No concurrent three-point success report was promoted
to an accepted premise by this review. The D10 author correctly preserves
that distinction in its final attempt record.

## Execution, limitations and disposition

Actual review consisted of textual reads/searches, read-only diff/hash
checks and independent paper reconstruction. No synthetic scalar test,
native build, point/board call, quadrature, phase cover or new degree run
was performed. Only this assigned report was written. No author file,
shared record, source/evidence or Git state was modified.

No BLOCKING, MAJOR or MINOR finding remains in the frozen scope.
Acceptance supports preparing a checker for this exact contract; it
does not approve such an implementation or supply its arithmetic,
provenance, parser or independent replay checks. No practical size,
termination, cost, successful cover, finite-degree extension or updated
global threshold follows. This supplementary check does not replace
the required Claude audit.
