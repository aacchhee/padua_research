# PD-T?argmax-bridge-codex-D10-cover — Exact point-bound adapter for a full phase cover

ID kind: PD-T. Aliases: rational-turn point-to-box cover; conditional
near-intersection predicates. Split from: implementation specialization
of PD-T364's existing finite-cover theorem. Split into: source/checker
implementation and actual certificate instances remain separate.

Status: **PROVED analytic sufficient implication**, under the exact
premises below; distinct review required. No successful512 certificate,
numerical corner patch, source adoption or cost claim is asserted.
This is an adapter of the existing cover, not a new cover mechanism.

## Statement and independent premises

Fix n=512, m=513, N=nm and kappa=n/m. Use exactly PD-T101/364's
even-checkerboard nodes, corrected finite kernel and common primitive
S. In particular G has coefficient one at the exceptional(n,0) mode,
and all collision values are its finite polynomial values. Let

    T={(a,b):a>=0,b>=0,a+b<=1},
    Lambda_c=lambda_n(-1,-1).

Require independently established premises:

1. A GLOBAL bound S(alpha,beta)<=M for ALL real alpha,beta, with
   rational M>0. It also bounds the physical lambda and the signed
   families required by D08. D09's independently accepted global norm
   supplies M=34 at512; see independent-checks-D09-global-norm.md.
   A point maximum or unknown global argmax is not a substitute.
   A rational upper on the independently proved coarse D08 norm is
   an alternative. This theorem does not use its own eventual conclusion
   to obtain M.
2. Outward rational constants 0<p_lo<=pi<=p_hi and
   0<L<=Lambda_c. Each vertex upper used below independently encloses
   the ACTUAL S value at that exact rational-turn input, under the
   reviewed point-source contract and its failure guards.
3. The accepted C02 dense-band floor: for every admissible NONCORNER
   physical odd center and every signed phase rho=|alpha|+|beta|<=1/2,
   Delta>1/32. The safe consequence used here is lambda<=S-1/32.
4. A successful independently validated pointwise actual-corner patch:
   at both actual nonnode corners, every admissible inward phase with
   0<rho<=1/2 has lambda<Lambda_c, with equality at phase0. D08's
   three-loss criterion is one allowed witness, specified below. Its
   sufficient theorem alone does not provide a successful witness.

Any finite cover of T by rational triangles/rectangles clipped to T,
accepted by the exact predicates below, proves

    max_[-1,1]^2 lambda_512=Lambda_c,
    argmax lambda_512={(-1,-1),(1,-1)}.                 (1)

All hypotheses include their closed boundaries. No claim that such a
cover has been constructed, is guaranteed to succeed or has a bounded
practical size follows from this implication.

## Physical centers, signs and the floor

The finite center set and admissible phases are

    C={(J,K):0<=J<=n,0<=K<=m,J+K odd},
    D_JK={|alpha|+|beta|<=pi}
       intersect[-J*pi,(n-J)*pi]x[-K*pi,(m-K)*pi],
    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m.           (2)

There are131841 centers. Since n is even, the actual corner centers
are(0,m),(n,m), corresponding to physical(1,-1),(-1,-1).
Every other center is noncorner, including physical edge centers.
At J=0 admissibility requires alpha>=0; at J=n it requires alpha<=0;
the analogous K endpoint signs also hold. A phase zero at a noncorner
center remains subject to the strict defect comparison.

Every physical point has a representation(2). Indeed in a containing
mesh rectangle the normalized L1 distances to its two odd vertices
are either x+y and2-x-y, or1-x+y and1+x-y. Their sum is2, so one is
at most1. Adjacent interior rectangles handle physical boundaries;
ties are included. This is PD-T364's exact all-center cover.

C02 gives Q_v>1/32 when0<K<m and Q_h>1/32 when0<J<n for
n>=160 and the full signed rho<=1/2 guard. Every noncorner member
of C has at least one such interior coordinate: if both coordinates
are endpoints, odd parity gives exactly the two listed actual corners.
Since Delta>=max(Q_v,Q_h), premise3 is uniform over ALL noncorner
centers in(2). No center-dependent radius or sampled class minimum
is needed. No floor outside rho<=1/2 is asserted.

## Exact closed-lattice point canonicalization

Write S^t(a,b)=S(pi*a,pi*b). For integers p,q with p+q even,

    S^t(a+p,b+q)=S^t(a,b),
    S^t(-a,b)=S^t(a,b)=S^t(a,-b).                    (3)

These are finite-board reindexings, valid at collisions and boundaries.
There is no interchange of the n and m meshes. To reduce ANY rational
pair, put s=(a+b)/2,t=(a-b)/2; subtract integers j,k so s',t' belong
to[-1/2,1/2]. Then a'=s'+t',b'=s'-t' differ by the lattice vector
(j+k,j-k), and |a'|+|b'|=2max(|s'|,|t'|)<=1. Thus their absolute
values belong to T. All operations and tie choices are exact rational.

For a unique cache key, enumerate from this representative all
(epsilon_1*a'+p,epsilon_2*b'+q) in T, with epsilons in{+1,-1}
and p,q in{-2,-1,0,1,2}, p+q even, and choose their lexicographic
minimum. One may first use the nonnegative representative. This list
contains every T representative in its symmetry orbit: coordinates
before/after translation lie in[-1,1] and[0,1], so these integer ranges
suffice, and reflections preserve the even lattice. It is finite,
nonempty and exact. In particular all closed-edge/tie equivalents agree.

For raw vertices in[0,1]^2 a simpler first fold is(a,b) when a+b<=1,
and(1-a,1-b) otherwise, followed by the boundary canonicalization.
This uses translation by(-1,-1) and separate evenness. Raw points
outside T are NEVER passed to the old point API under this contract.
Only S values are folded: neither the physical center, defect radius
nor corner geometry is transformed by this cache operation. The key
also records degree and the reviewed source/arithmetic identity.

## Four-point rational bounds on arbitrary enclosing rectangles

Let B=[a_l,a_h]x[b_l,b_h] be a rational rectangle in[0,1]^2. Its
four vertex upper enclosures U_ij are obtained at canonicalized inputs
using(3). Let I_B U denote their bilinear interpolant. Define

    q_B(a,b)=I_B U(a,b)
       +(M*p_hi^2/2)[(a-a_l)(a_h-a)
                         +kappa^2(b-b_l)(b_h-b)].      (4)

D08's point-dependent Peano theorem in radians gives

    S^t(a,b)<=q_B(a,b), (a,b) in B.                  (5)

Interpolation weights are unchanged by multiplying each coordinate by
pi. Both curvature products are nonnegative, so replacing pi² by
p_hi² is safe. This is a rational quadratic, including its mixed
bilinear term. The simpler valid bound

    U_B=max_ij U_ij
       +(M*p_hi^2/8)[(a_h-a_l)^2+kappa^2(b_h-b_l)^2] (6)

may replace every maximum of q_B below. No differentiability of S or
factor counting board points is assumed. For a zero-width side use
the corresponding one-dimensional interpolation, with zero curvature
product; singleton boxes use their point upper. Alternatively choose
a positive-width enclosing rectangle, even for a degenerate patch.

## Rational proxies for the irrational near cut

Let P be the intersection of T with a declared rational closed triangle
or rectangle, and B an enclosing rectangle as above. Empty P is ignored
only after exact emptiness verification; tangencies and singletons stay.
Define the ACTUAL near/far intersections

    A_N=P intersect{pi(a+b)<=1/2},
    A_F=P intersect{pi(a+b)>=1/2}.                   (7)

They cover P, including the shared cut. Set the rational numbers

    gamma_minus=1/(2*p_hi), gamma_plus=1/(2*p_lo),
    Q_N=P intersect{a+b<=gamma_plus},
    Q_F=P intersect{a+b>=gamma_minus}.               (8)

Then A_N subset Q_N and A_F subset Q_F. These are rational compact
polygons, possibly empty or lower dimensional. They can overlap.
Compute rational uppers V_N>=max_QN q_B and V_F>=max_QF q_B when
the respective proxies are nonempty. A proxy emptiness proof makes
its corresponding actual branch vacuous. It is safe to require a
predicate on a nonempty proxy even if the actual branch is empty.

Crucially(8) is only an OUTER set for bounding S. Premise3 is applied
ONLY on A_N; Q_N need not satisfy its radius guard. The complement
of the actual near set is handled by the actual far branch and Q_F,
not by subtracting the defect on an entire cut-crossing rectangle.

## Exact leaf predicates

A patch P can be accepted by either of the following:

* **FAR:** a validated upper on q_B over all P is strictly <L. This
  handles all centers for all its phases, without any defect or corner
  premise on that patch.
* **SPLIT:** if Q_N is nonempty, require V_N-1/32<L and the valid
  actual-corner premise4; if Q_F is nonempty, require V_F<L.
  Every required comparison is exact rational and strict. A proxy with
  no points has no bound field and supplies no unchecked numeric default.

One may omit the far branch in SPLIT if the independent rational test
2*p_hi*max_P(a+b)<=1 proves ALL of P actually near. Then use a full-P
upper V with V-1/32<L and premise4. Likewise FAR may use any proved
full-P upper and needs no near/far classification. These optional
stronger guards are exact linear maximizations. No floating cut test,
midpoint classification or caller Boolean supplies a domain proof.

The same predicates may be applied separately to a finite rational
subdivision of a patch. A finite union is accepted only after exact
coverage, not because its vertices or patch centers were tested.

### Finite exact maximization used in these predicates

All vertices of the rational clipped polygons in(8) are obtained by
pairwise intersections of finitely many rational supporting lines and
exact feasibility tests. Retain dimension0 and1 intersections.
For a rational quadratic q on a compact rational polygon, a finite
rational upper equal to its maximum is obtained by inspecting:

1. Every polygon vertex.
2. On every segment edge, endpoints and its interior stationary point
   t=-b/(2a) when the restricted polynomial is at²+bt+c with a!=0.
   Linear/constant restrictions need only endpoints.
3. The solution of grad q=0 when its2x2 Hessian is invertible, if
   the solution belongs to the polygon.

All listed coordinates and values are rational. A full-dimensional
interior maximum has zero gradient. If the Hessian is singular, a
nonzero null direction through a stationary point has constant q;
extend it to the boundary of the compact polygon. Thus a boundary
candidate already has that value. A zero Hessian/constant polynomial
is included. Lower-dimensional polygons use the segment/point rule.
This proves the finite maximum rule, including all degeneracies,
without algebraic root isolation or a numerical optimizer. Using(6)
instead is a valid simpler conservative checker choice.

## Finite exact COVER geometry

The semantic condition is T subset union(P_1,...,P_k), for a FINITE
list of closed rational patches, each accepted as above. Overlaps are
allowed. One exact verification method forms the line arrangement of
all patch supporting lines and T's three supporting lines. Intersect
each of its finitely many closed faces with T. For every relatively
open face of dimensions0,1,2 lying in T, select one rational point in
its relative interior and check exact membership in at least one P_i.
Membership in every closed polygon is constant on each relatively open
arrangement face, since its supporting lines occur in the arrangement.
Hence this finite check is equivalent to coverage, including every
closed edge/vertex and all intersections. Rational points exist for
every nonempty face, and can be produced from its rational vertices;
the checker reconstructs the arrangement and face incidences itself.

A simpler allowed format is a complete binary partition of[0,1]^2
with rational splits, clipped to T. Reconstruct roots, split values
and child rectangles. Both children must be present, share the exact
split, and have positive progress; leaves must be prefix-free and
complete, with no missing siblings, duplicates or pending leaves.
Then their closed intersections with T cover T automatically.
An outside rectangle in this root has empty intersection with T
exactly when a_l+b_l>1. The strict > is essential: equality leaves a
boundary point. Triangular subdivisions are equally valid when their
exact closed union is checked; they are not forced into a rectangular
interpolation geometry, since B merely encloses each triangle.

## D08 three-point premise in rational turns

This is an optional witness for premise4, not an asserted success.
Choose rational a_*,b_*>0 with p_lo*a_*>=1/2 and
p_lo*b_*>=1/2, so the actual phase rectangle contains the full
inward rho<=1/2 diamond. Put u'=a_*²/2,v'=b_*²/2. Independently
enclose the actual three corner values at inward physical turns
(a_*/n,0),(0,b_*/m),(a_*/n,b_*/m), with uppers W_x,W_y,W_xy.
From a certified L<=Lambda_c define exact rational losses

    d_x=L-W_x, d_y=L-W_y, d_xy=L-W_xy,
    q=min(d_x/u',d_y/v',d_xy/(u'+v')).

The finite strict predicate

    q>(M*p_hi^4/6)*max(u',kappa^4*v')                (9)

implies D08's corner theorem with physical U=pi²u',V=pi²v'
and c=q/pi². Its resulting barrier coefficient is at least

    [q-(M*p_hi^4/6)max(u',kappa^4*v')]/p_hi²>0.

The pi⁴ factor in(9), rather than pi², is required by the squared
coordinate conversion. The true origin remains the symbolic Lambda_c.
The illustrative a_*=1/4,b_*=3/16 fits the half-radius geometry from
pi>3; the separate three-point preparation may retain other fixed
choices under its own guards. No successful losses are supplied here.
At the second actual corner use PD-T364's parity-preserving x reflection
for even n; it permutes the cardinal basis and preserves Lambda_c and
the inward patch. No all-degree energy theorem is substituted.

## Proof of the sufficient global conclusion

Take any physical point and choose an admissible odd-center chart(2).
Put a=|alpha|/pi,b=|beta|/pi. Then(a,b) belongs to T and S at
the signed phase equals S^t(a,b) by separate evenness. Exact COVER
provides an accepted P containing it. A FAR predicate gives
lambda<=S<=upper<L<=Lambda_c, uniformly for all physical centers.

Otherwise use SPLIT. If rho<=1/2 and the center is noncorner,
(5),(7),(8) and premise3 give

    lambda<=S-1/32<=V_N-1/32<L<=Lambda_c.           (10)

If the center is actual corner, premise4 gives strictness unless the
phase is zero, which is exactly that physical corner. If rho>=1/2,
the far branch gives lambda<=S<=V_F<L<=Lambda_c for every center.
The shared rho=1/2 boundary is included; either applicable proof
is valid, and SPLIT conservatively requires both proxy predicates
when present. The whole-near optional guard uses the same near proof.

Thus every physical point except the two actual nonnode corners is
strictly below Lambda_c. PD-T364 gives their value S(0,0)=Lambda_c
and equality of the two by the parity-preserving reflection. This
proves(1). Physical node corners are not omitted: they have value1
and are covered by nonzero odd-center phases, not extra origin cases.
Finite polynomial collisions, zero terms, endpoint weights and parity
are already exact in the inherited lambda=S-Delta identity and in
the independently valid point enclosures. No quotient at a pole,
sign-stability premise or unknown-maximum substitution enters. QED.

## Checker reduction and limits

A consequential checker must independently validate n=512 and each
scientific premise at its exact scope, resolve accepted norm/floor/patch
dependencies, validate outward pi and corner lower bounds, reconstruct
all rational geometry including P subset B, canonicalize point inputs, validate/replay
every actual enclosure used, and recompute(4)--(10) with exact rational
final comparisons. Source failure, nonfinite endpoints, pending regions,
unsupported inputs, malformed/duplicate keys and unvalidated arithmetic
forbid acceptance. Producer bound numbers or success flags alone are
not proof. Review prose is not a runtime hash pin; immutable code,
input, certificate and evidence identities belong to the eventual
implementation manifest and independent replay.

This theorem supplies the finite mathematical reduction only. No
source was changed, no point/cover/native/quadrature job ran, and no
leaf-count, bit-cost, runtime, termination or successful instance is
claimed. N3's finite energy range, C03's astronomical onset and earlier
local patches are not enlarged. The practical certifier and any new
degree remain unresolved until their actual predicates pass.

2026-11-06. Rules/input9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf.
Ordinary parent-assigned Sol xhigh bounded analytic developer block;
actual serving metadata unexposed. Gate/provenance and unexecuted
verification obligations are in the idea and attempt records.


### Supplementary mathematical closure — 2026-11-06

Distinct Astra high reconstruction ACCEPTED the preceding sufficient
implication with no unresolved findings;
[independent-checks-D10-cover-contract.md](../independent-checks-D10-cover-contract.md),
report SHA256bbe827a02277d9dcdee9dca89861b9374e199e86674fdb1954a7308b2d49421b.
The accepted D09 degree512 corner patch now supplies premise4;
a complete validated vertex cover is still absent, so the global
degree512 instance remains OPEN. No proof premise is silently waived.
