# PD-T?argmax-bridge-codex-D21 — A supplied static tree certifies its fresh norm and cover

ID kind: PD-T. Aliases: static fresh-point phase certificate;
integer-geometry point verifier; analytic-corner self-norming cover.
Split from: D19's proposed static geometry plus Arb verification.
Split into: any concrete degree result, executable correctness and
measured resource claim require their own evidence/review records.

## Statement and status

For EVERY integer n>=4096 put m=n+1 and kappa=n/m. Use precisely
PD-T101/PD-T364's corrected finite Padua cardinal polynomials,
original endpoint weights and finite-polynomial collision values.
Write lambda_n for their Lebesgue function and

    Lambda_c=lambda_n(-1,-1),
    S^t(a,b)=S_n(pi*a,pi*b),
    T={(a,b):a>=0,b>=0,a+b<=1}.

Supply a FINITE complete binary midpoint tree with root[0,1]²,
tokens a,b for a coordinate split and . for a leaf. Decode both
CLOSED children using exact rational midpoints. Retain every leaf
B=[al,ah]x[bl,bh] with al+bl<=1, including equality/tangency, and
discard a leaf only under the strict exact condition al+bl>1.

For exactly the union K of all retained leaves' canonical four
S vertex arguments, suppose validated SAME-DEGREE rational enclosures

    lower_k<=S^t(k)<=upper_k, k in K               (1)

are supplied. Canonical means a value-preserving orbit representative
as specified below, not an interchange of the unequal meshes. Following
the child containing the root origin reaches a retained leaf with that
vertex, so the origin belongs to K. Set L=lower_(0,0) and require L>0. Fix proved
rational0<p_lo<=pi<=p_hi. For EVERY retained leaf define

    V_B=max_(four raw vertices v of B) upper_canonical(v),
    theta_B=(p_hi²/8)[(ah-al)²+kappa²(bh-bl)²].     (2)

Require theta_B<1 for EVERY retained leaf and put

    R=max_B V_B/(1-theta_B), M=ceil(R),
    U_B=V_B+theta_B*M, f=1/16.                    (3)

Require M>0. Let low=al+bl, high=min(ah+bh,1). Each retained leaf
must pass at least ONE exact strict alternative:

1. **FAR:** U_B<L.
2. **NEAR:** 2*p_hi*high<=1 AND U_B-f<L.
3. **SPLIT:** require U_B-f<L if low<=1/(2*p_lo),
   AND require U_B<L if high>=1/(2*p_hi).          (4)

An absent conditional comparison in SPLIT is vacuous ONLY because
its exact outer proxy is empty. A conservative check of a larger
set is allowed. All nonvacuous comparisons are strict rational ones.
Any fixed deterministic priority among passing alternatives is allowed.

Then the exact global maximizer set is

    argmax_[-1,1]² lambda_n={(-1,-1),(1,-1)}, n even,
                          {(-1,-1),(-1,1)}, n odd, (5)
    max lambda_n=Lambda_c.

This covers ALL closed physical boundaries, axes, chart ties, nodes,
initially zero terms and kernel collisions. It requires NO actual
lambda point evaluation: accepted D17 supplies the corner premise
on n>=4096. The phase norm in(3) comes ONLY from the SAME tree's
own SAME-DEGREE vertices, with no old degree data, fixed-grid norm,
completed-model phase norm or desired argmax premise.

Overall status: **PROVED analytic sufficient implication**, by the
assembly below under explicit validated endpoint hypotheses(1).
Distinct independent D21 mathematics/source review is pending.
No successful supplied-tree witness, new finite degree, executable
termination/cost bound or measured speedup is asserted. In particular,
the proposed n6912 application is **OPEN** before its audited run.

## Fixed definitions and accepted dependencies

With N=nm, h_0=1,h_r=2 for r>0, the finite corrected polynomial is

    G_n(u,v)=sum_(r+s<=n) h_r*h_s*cos(ru)*cos(sv)-cos(nu),
    S_n(alpha,beta)=(1/(2N))*sum_(0<=j<2n,0<=k<2m,j+k odd)
        |G_n((j*pi+alpha)/n,(k*pi+beta)/m)|.        (6)

Thus the exceptional(n,0) coefficient is ONE. Every removable
collision means the finite polynomial value, not a quotient at a
pole. The physical even-board nodes are(cos(j*pi/n),cos(k*pi/m)),
0<=j<=n,0<=k<=m,j+k even, with endpoint half weights as in
PD-T101/364. Their corrected cardinal formula sums four reflected
finite kernels BEFORE absolute values.

| Accepted dependency | Exact scope used |
|---|---|
| PD-T364 and D15-generic-cover | All n>=2 closed physical odd-center cover, full defect, endpoint multiplicities, period/evenness, actual-corner equality and parity reflections; D15 supplies generic phase-cover assembly for n>=160 |
| D08 ordinary signed-family Peano/Bernstein | All n>=2 actual continuous global norm; TURN widths acquire pi²; no smoothness assumption on the absolute sum |
| D19-adaptive-norm, accepted independent report | All n>=2 self-norming closed rectangle cover from its own vertices; all theta<1 before absorption |
| C02-defect-dense-band, accepted independent defect review | All n>=4096 each applicable interior-coordinate projection>1/16 on every ACTUAL physical signed rho<=1/2, both parities/orientations |
| D17-analytic-corner, accepted independent report | All n>=4096 both actual inward corner charts on CLOSED[0,pi/6]²: lambda<=Lambda_c-(A²+B²)/8 |
| Validated SAME-DEGREE actual S enclosures | Hypothesis(1), supplied by a separately reviewed finite-point arithmetic implementation |

Relevant accepted review identities include D15 generic
4ea70bd2f18260e5321db44d6296b3cf3886901c86a298fd324bbdb06593fd90,
D17 corner28dbf04a53286706475e5264dec2676ea7a9d09c298e691a5157bc10f5c94c2b,
and D19 report5b7d66f9066b5db34a65617f117275bde152e44689c8e8d102347f8dba0155f1.
C02's accepted defect report
a435cc44786a4f16903fdcb0563ea435081c36224e357170fabd867e65d73013
states both applicable1/16 floors from4096;
the older D15 literal1/32 is not silently relabeled as stronger.

D17 is an INHERITED ANALYTIC corner theorem: its accepted proof still
depends on its completed-model comparison/norm and PD-T271 trusted
origin constant. This D21 assembly therefore makes NO fully model-free
dependency claim. It does avoid those model norms as numerical inputs
to the fresh phase interpolation. No unproved relative remainder or
D20/global7000 conclusion is used. No change to old theorem quantifiers.

## Closed tree, keys and global norm

At each exact midpoint split, the union of the two closed children is
their closed parent, with their shared face retained in both. Induction
shows all leaves cover[0,1]² and their clips cover T. For a leaf B,
B intersect T is empty iff al+bl>1: all sums are>=al+bl, and otherwise
the lower-left corner itself belongs to T. Equality is a real tangent
point. A finite valid tree with both children, no missing/pending subtree
or trailing tokens is essential; an available point list alone proves
no coverage. An a or b split must make positive progress.

The accepted period identities for integers p,q with p+q even are

    S^t(a+p,b+q)=S^t(a,b),
    S^t(-a,b)=S^t(a,b)=S^t(a,-b).                 (7)

They hold for all real phases and all finite collisions. For a raw
vertex in[0,1]², first map(a,b) to(1-a,1-b) if a+b>1. The result
lies in T. On the hypotenuse ONLY, use the lexicographic minimum of
(a,b) and(b,a). D19 proves this is the canonical T representative
of the even-lattice/separate-sign orbit. Away from the hypotenuse
there is no coordinate interchange. In particular(0,3/4) does not
identify with(3/4,0). The hypotenuse endpoint identification is included.
An equivalent full exact orbit enumeration is allowed.

Canonicalization changes ONLY vertex evaluation arguments. It never
changes B's geometry, widths, physical centers, actual radius or
inward corner signs. A raw vertex outside T is evaluated through its
equivalent canonical key; it is not passed outside a point API's
literal phase domain. A point cache key includes n and the frozen
validated arithmetic/source identity, so no other-degree enclosure
can satisfy(1).

The continuous finite S has a finite global maximum M*, attained on
T. Indeed reduce(alpha+beta)/(2pi),(alpha-beta)/(2pi) modulo integers
to[-1/2,1/2], then use(7) to reach the closed diamond and T. This
establishes a TRUE global norm before any derivative or sample bound.
For every fixed signed board family, D08 signed Bernstein supplies
the l1 component second-derivative bounds M*,kappa²M*. Common positive
ordinary Peano interpolation on B gives

    S^t(a,b)<=V_B+theta_B*M*, (a,b) in B.         (8)

Choose a global maximizing point in T and a retained closed leaf
containing it. Coverage includes shared/tangent/hypotenuse points.
At that point(8) and theta_B<1 imply

    M*<=V_B/(1-theta_B)<=R<=M.                    (9)

Thus(3) is independently sufficient from the NEW leaf-corner uppers.
The argument does not identify M* with a sampled maximum. With this
global M, the SAME ordinary Peano theorem proves S^t<=U_B on all
of each rectangle, including its portions outside T. TURN widths
contribute pi², safely bounded by p_hi²; neither pi nor kappa is
dropped. This proves(2)--(3)'s use in every subsequent predicate.

## Actual near/far guard and the strict alternatives

For P=B intersect T nonempty, min_P(a+b)=low and max_P(a+b)=high.
The minimum is the lower-left vertex. The upper-right vertex gives
the maximum if its sum<=1; otherwise continuity of the line segment
from lower-left to upper-right reaches the hypotenuse, giving maximum1.
This also proves the endpoint/tangent cases.

The ACTUAL closed near and far sets in P are

    A_N=P intersect{pi(a+b)<=1/2},
    A_F=P intersect{pi(a+b)>=1/2}.                (10)

They cover P with their shared actual seam. Rational OUTER proxies are

    Q_N=P intersect{a+b<=1/(2*p_lo)},
    Q_F=P intersect{a+b>=1/(2*p_hi)}.             (11)

The pi bracket gives A_N subset Q_N and A_F subset Q_F. By the exact
sum extrema, Q_N is nonempty iff low<=1/(2*p_lo), and Q_F is
nonempty iff high>=1/(2*p_hi). Equality retains the tangent proxy.
The full-rectangle U_B bounds S on both proxies, so(4)'s SPLIT
comparisons are safe conservative D15 predicates; no polygon optimizer
is needed. Membership in Q_N NEVER supplies the actual floor guard.

FAR gives lambda<=S<=U_B<L at every physical center/radius. NEAR's
independent guard gives actual pi(a+b)<=1/2 throughout P. At any
noncorner physical center, C02 yields full defect Delta>f, hence

    lambda=S-Delta<S-f<=U_B-f<L.                 (12)

For SPLIT choose an ACTUAL branch. On A_F its outer Q_F is nonempty
and U_B<L gives FAR exclusion; on A_N its Q_N is nonempty and(12)
applies at every noncorner center. At the seam either route is safe;
SPLIT checks both nonempty proxies. At an actual corner on any near
branch, use the independent D17 patch as proved next. No floor is
applied at an actual corner or outside ACTUAL rho<=1/2, and no two
projected defects are added.

## Physical charts, corners and full-domain conclusion

PD-T364's physical odd centers are0<=J<=n,0<=K<=m,J+K odd.
Their admissible phases satisfy

    |alpha|+|beta|<=pi,
    -J*pi<=alpha<=(n-J)*pi,
    -K*pi<=beta<=(m-K)*pi,
    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m.

The exact identity, including endpoint reflection multiplicities, is

    lambda_n(cos theta,cos phi)=S_n(alpha,beta)-Delta_JK,
    Delta_JK>=max(Q_h(J),Q_v(K))>=0.              (13)

In every physical mesh cell, the two odd-vertex L1 distances in
normalized local coordinates sum to2. One is<=1, giving one of
these closed charts. This includes all ties and square boundaries
by taking an adjacent physical cell. Apply separate evenness and set
a=|alpha|/pi,b=|beta|/pi in T. The tree covers that point. Physical
rho=|alpha|+|beta|=pi(a+b) is unchanged by this sign reduction.

The ONLY odd endpoint-pair centers are(n,m) and(0,m) for even n,
or(n,m) and(n,0) for odd n. Their physical images are the two
corners in(5). At(n,m), admissibility forces alpha,beta<=0, so
A=-alpha,B=-beta are its inward phases. For even n, x reflection
preserves node parity and weights, taking this chart to(0,m) with
A=alpha,B=-beta. For odd n, y reflection gives(n,0) with
A=-alpha,B=beta. Neither reflection exchanges n and m.

At the actual corners the full defect is0, giving the exact identity

    S_n(0,0)=Lambda_c.                            (14)

Thus the fresh LOWER endpoint in(1) is indeed L<=Lambda_c.
D17's accepted all-n>=4096 inequality at both corners is

    lambda_n<=Lambda_c-(A²+B²)/8,
    0<=A,B<=pi/6.                                (15)

Since pi>3, pi/6>1/2. Every actual inward half diamond A+B<=1/2
lies in that closed rectangle. It gives strict descent unless A=B=0,
where the value is exactly Lambda_c. There is no additional Peano
coefficient or factor conversion to compute in this application;
1/8 already multiplies A²+B², not the squared-phase sum u+v.

Every other odd center has at least one INTERIOR index; otherwise
it is an endpoint pair already enumerated. C02's corresponding
projection supplies Delta>1/16 on all its ACTUAL signed near phases.
Equations(12)--(15), selected by the verified leaf alternatives,
therefore exclude every point except the two actual corner origins.
Both origins attain the common value by the reflection identity.
Even node corners have interpolation value1 and are covered at
nonzero odd-chart phases; no extra equality point arises. All
collisions and zero terms retain their finite-polynomial values.
This proves(5). QED.

## Executable design scope and falsifiable boundary

The intended ONE instance supplies evidence/d19-pruned-tree.json,
113B, SHA2565ff335b5e8c3a813b934f38b0938cf80bf29f546749651cd749e5ffc41c753d1.
Its geometry is independent of degree; its old n2048 field records
provenance. The new literal target is6912. Decode the actual complete
61-token tree and derive its retained canonical corner union before
any evaluation. Request EXACTLY that union at6912, including the
origin, in fixed rational order, with fresh C11 values. The geometry
has41 keys; this count is a cross-check, not a replacement for union
equality. No old endpoint, M35, leaf tag or numerical margin is used.

C11's unchanged point.cpp literal successful-call domain includes
2<=n<=2147483647 on exact rational T. This permits6912 without
changing its guard, precision, tails or kernel. It proves neither
successful calls nor cost there. The D07 actual-lambda guard remains
unchanged and unused. No FLOAT discovery, refinement, pruning, new
keys, degree/precision change, scan, retry or fallback producer is
part of the one-shot design. Preserve the first failure.

The prospective aggregate cap is<=600CPU including cold build,
imports, all supervisor/helper/native processes and finalization.
Source/SPEC/command/resource accounting must be frozen, distinctly
reviewed and root-released BEFORE any native case. Acceptance requires
fresh validated endpoint return codes, exact tree/key/norm/leaf checks,
freeze identities, successful FINAL accounting AND observed exit0.
Provisional artifacts do not prove completed acceptance. An independent
fresh result replay remains separate from source inspection.

No execution occurred during this mathematical design. The supplied
tree might fail at6912 despite earlier success at2048; then THIS witness
is insufficient, and actual global6912 remains OPEN. There is no
claim that this tree works at other degrees, that600CPU suffices,
that native work is uniform in n, or that fewer requested points or
removing discovery has produced a measured runtime improvement.

2026-11-06, parent-assigned Codex gpt-6.1-sol xhigh; full rules/input
ca8d52aa2a48c941473846ab884cccb25f1bdb9f. Fresh comparison gate and
prospective scope are in the D21 idea/attempt. Source ownership,
independent review, release and any finite result stay separate.


## Root contract review closure — 2026-11-06

Report [D21](../independent-checks-D21-static.md), SHA256 `7704a9eb1e866351926278ba1f4e03e41aaa81a78d65604dd4b1358e81717204`, independently accepts this generic sufficient implication and the unchanged first frozen source. Root adopts that implication, not a successful6912 certificate. The fixed primary run is separately released in LOG, with final-accounting/exit0 and fresh replay still required. Reviewed prefix is preserved; final Claude audit remains separate.


## Independent instance closure — 2026-11-06

[D28 result review](../independent-checks-D28-result.md), SHA256 `f68b4a19b05ef1bc5e33341e93f9450fdf9077db74f401e626d8d6de6491d305`, performs the sole independent fresh same6912/41point replay with the separately accepted D23 inclusion backend. Every exact closed-cover predicate, own norm45 and all baseline/new guards pass; accepted final accounting and directly observed exit0 are recorded. Root accepts the complete finite artifact and its cost measurement. This is not a new global-range addition beyond already accepted analytic4096, nor a uniform performance claim. Source/core analytic dependencies are unchanged and explicit.
