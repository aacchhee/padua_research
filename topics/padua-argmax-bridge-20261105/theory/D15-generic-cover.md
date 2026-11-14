# PD-T?argmax-bridge-codex-D15-cover — Generic exact point-to-cover sufficiency

ID kind: PD-T.
Aliases: degree-parameterized Peano phase cover; both-parity generic
finite certificate; dynamic global norm and actual three-point corner.
Split from: the requested generic D15 mathematical contract. This is a
NEW statement, not a change to D10's literal n512 theorem.
Split into: concrete certificates, executable source adoption and
independent instance checks remain separate records.

## Statement

For EVERY integer n>=160 put m=n+1,N=nm and kappa=n/m. Use exactly
PD-T101/PD-T364's corrected even-checkerboard Padua cardinal polynomials,
original endpoint weights and finite-polynomial collision values.
Let lambda_n be their Lebesgue function, Lambda_c=lambda_n(-1,-1),
and S_n the common odd-board primitive defined below.

Suppose the following SAME-DEGREE premises are established independently:

1. A rational M>0 satisfying S_n(alpha,beta)<=M for ALL real phases.
   This is a true GLOBAL norm premise, not a sampled maximum or an
   assumption about the desired physical argmax. It also bounds the
   signed families as proved below.
2. Rational 0<p_lo<=pi<=p_hi and0<L<=Lambda_c. Every S vertex
   upper used in the certificate is a validated outward rational upper
   for the ACTUAL corrected S_n at its exact rational-turn argument.
3. At both actual nonnode corners a validated pointwise patch covers
   the CLOSED inward phase half diamond A,B>=0,A+B<=1/2, gives
   lambda_n<=Lambda_c there, and gives strict inequality unless A=B=0.
   The explicit three-ACTUAL-point criterion below is one sufficient
   witness for this premise; it must actually pass at this n and M.
4. A FINITE complete exact closed cover of

       T={(a,b):a>=0,b>=0,a+b<=1}

   is supplied with validated point uppers and the exact FAR, NEAR
   or SPLIT leaf predicates below. A complete binary midpoint tree
   rooted at[0,1]² and clipped to T is one allowed format.

Then

    max_[-1,1]² lambda_n=Lambda_c,
    argmax_[-1,1]² lambda_n={(-1,-1),(1,-1)} if n even,
                         ={(-1,-1),(-1,1)} if n odd. (1)

All domain boundaries, chart ties, nodes, initially zero cardinal terms
and removable kernel collisions are included. A validated three-point
patch keeps the TRUE symbolic Lambda_c at its origin and needs no
positive constant margin there. No assertion that these premises pass,
that a certificate exists, or that a producer terminates follows.

## Status, dependencies and quantifier boundary

Overall status: **PROVED analytic sufficient implication** by the proof
below. Distinct Astra mathematical review of this NEW generic contract
is pending. No numerical/native job or successful D15 instance is
asserted; final Claude audit remains separate.

The substantive ingredients already have their own results:

| Dependency | Exact domain used here |
|---|---|
| PD-T364 | Every n>=2: corrected common primitive, full defect, closed physical odd-center cover, corner equality and node-preserving reflections. |
| D08-point-box.md / D08-point-box-corner.md, accepted supplementary report486f58f8... | Every n>=2: global signed-family Bernstein, common ordinary Peano and even ACTUAL-cardinal squared-phase three-loss theorem. |
| C02-defect-dense-band.md | Every n>=160: each applicable projected defect>1/32 at every physical signed phase with rho<=1/2; both coordinate orientations and degree parities. |
| Independent same-degree norm and actual finite enclosures | Hypotheses, not supplied by this generic theorem. |

D10-cover-contract.md is the accepted n512 predecessor. Its predicates
are reconstructed with arbitrary n here, and its quantifiers remain
unchanged. C13-onset-budget.md supplies a separately proved both-parity
assembly precedent, not a lower-domain estimate imported below its
n500000 floor. No C13 asymptotic comparison is used. The D14 finite-grid
norm is an OPTIONAL witness for premise1 after its separate acceptance;
this core implication does not depend on D14 or a completed model.

This is a standard assembly/parameterization variant of PD-T364/D10,
not a new finite-cover or interpolation principle or priority claim.
Prospective comparisons and retained alternatives are in the new D15
generic idea/attempt records. Older proofs/source/evidence are unchanged.

## Definitions: finite polynomial, physical centers and full defect

Set h_0=1,h_r=2 for r>0 and

    G_n(u,v)=sum_(r+s<=n) h_r*h_s*cos(ru)*cos(sv)-cos(nu),
    Gamma^-={(j,k):0<=j<2n,0<=k<2m,j+k odd},
    S_n(alpha,beta)=(1/(2N))*sum_Gamma^-
        |G_n((j*pi+alpha)/n,(k*pi+beta)/m)|.

The exceptional(n,0) coefficient is ONE. These finite polynomials
define every collision; no quotient at a pole or zero-times-infinity
rule changes a value. N=nm is the mesh product, not the node count.
The physical nodes have0<=j<=n,0<=k<=m,j+k even. Their endpoint
weights are e_j,f_k=1/2 at endpoints and1 inside, w_jk=2e_j*f_k/N.
The cardinal formula sums the four finite kernels before taking the
absolute value. Its full triangle defect Delta is nonnegative.

The physical ODD centers and admissible signed phases are

    C_n={(J,K):0<=J<=n,0<=K<=m,J+K odd},
    D_JK={|alpha|+|beta|<=pi}
       intersect[-J*pi,(n-J)*pi]x[-K*pi,(m-K)*pi],
    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m.         (2)

For every such physical chart PD-T364's EXACT full-defect identity is

    lambda_n(cos theta,cos phi)
       =S_n(alpha,beta)-Delta_JK(alpha,beta),
    Delta_JK>=max(Q_v(K),Q_h(J))>=0.                (3)

Projected defects provide lower bounds for Delta; they do not replace
the exact equality by equality with a projection, and are never added.
Endpoint reflection multiplicities are already exact in(3): an
interior residue has one reflected preimage of weight1; endpoint
residues have two coincident preimages of weight1/2. Thus no endpoint
correction or omitted collision term appears in(3).

## Closed physical coverage and both parity corner sets

For an arbitrary(theta,phi) in[0,pi]² choose a containing physical
mesh rectangle, using the adjacent interior rectangle on a square
boundary. In its normalized local coordinates x,y in[0,1], the
L1 distances to the two odd vertices are either x+y,2-x-y or
1-x+y,1+x-y. Each pair sums to2, so one distance is<=1.
Its center belongs to C_n, is physical, and gives(2) with
rho=|alpha|+|beta|<=pi. Ties and all rectangle/square edges are
retained. This proves coverage at every n>=2 without enumerating
representative centers or assuming where a maximizer lies.

The center(n,m) is odd for every n since n+m=2n+1, and its image
is(-1,-1). Among the other endpoint pairs, (0,0) is even;
(0,m) is odd exactly when n is even; (n,0) is odd exactly when
n is odd. Thus the ACTUAL nonnode corner centers are precisely

    (n,m),(0,m) if n even;
    (n,m),(n,0) if n odd.                           (4)

At(n,m), physical admissibility forces alpha<=0,beta<=0. Writing
A=-alpha,B=-beta gives the canonical actual corner chart

    Lambda_n(A,B)=lambda_n(-cos(A/n),-cos(B/m)).     (5)

For even n, x reflection sends each node index j to n-j, preserves
j+k even because n is even, and preserves endpoint weights. It
therefore permutes the corrected cardinal basis and maps(-1,-1)
to(1,-1). At(0,m), alpha>=0,beta<=0, so A=alpha,B=-beta
gives lambda_n(cos(A/n),-cos(B/m)), exactly this reflected chart.
For odd n, m is even; y reflection sends k to m-k and likewise
preserves node parity and weights. At(n,0), alpha<=0,beta>=0,
so A=-alpha,B=beta gives lambda_n(-cos(A/n),cos(B/m)).
This is the y-reflected chart. The two corner values are equal in
either parity. There is no interchange of the unequal n,m meshes.

At physical corners the four reflected finite kernels coincide, so
Delta=0. At either ODD corner (3) therefore gives

    S_n(0,0)=Lambda_c.                             (6)

Node corners are different: their interpolation value is1 and they
are covered by nonzero boundary phases in odd-center charts. They
are not additional zero-phase actual corners.

Every center in C_n other than the two in(4) has an interior index
0<J<n or0<K<m. Indeed otherwise both indices are endpoints and
the preceding parity enumeration is exhaustive. On the ACTUAL
signed near domain rho<=1/2, C02 applies because n>=160 and gives
Q_h>1/32 in the first case or Q_v>1/32 in the second. Hence

    Delta_JK>1/32                                  (7)

uniformly for ALL noncorner centers, including physical edge centers,
at ALL physically admissible signed near phases. A phase0 at a
noncorner center is included in(7), not exempted. The theorem makes
no claim that(7) holds outside rho<=1/2 or at an actual corner.

## Global norm and exact phase canonicalization

From premise1 and(3), the global physical lambda is<=M. Every fixed
coefficient family |epsilon_i|<=1 satisfies

    |sum_i epsilon_i L_i(x,y)|<=lambda_n(x,y)<=M

on the square. Every board coefficient family of magnitude<=1 is
similarly dominated by S_n<=M on ALL real phases. The actual corner
substitution(5) stays inside the square for ALL real A,B. Thus both
complete signed polynomial families have the global M needed by D08.
No assumed value or location of an unknown maximizer enters.

Write S^t(a,b)=S_n(pi*a,pi*b). For integers p,q with p+q even,
finite board reindexing and separate cosine evenness give

    S^t(a+p,b+q)=S^t(a,b),
    S^t(-a,b)=S^t(a,b)=S^t(a,-b).                  (8)

These identities hold for EVERY n>=2 and at all finite collisions.
For any rational pair put s=(a+b)/2,t=(a-b)/2, and choose integers
j,k with s'=s-j,t'=t-k in[-1/2,1/2]. The equivalent phases
a'=s'+t',b'=s'-t' satisfy |a'|+|b'|=2max(|s'|,|t'|)<=1.
Their absolute values are in T. The translation is(j+k,j-k), an
even-lattice vector. Rational ties may be resolved by any fixed exact
convention without losing a phase value.

For raw rectangle vertices in[0,1]², use the simpler first fold
(a,b) if a+b<=1 and(1-a,1-b) otherwise. The latter is translation
by(-1,-1) followed by sign reflection. From a T representative,
enumerate all(eps_1*a+p,eps_2*b+q) in T, eps_i in{-1,1},
p,q in{-2,-1,0,1,2},p+q even, and select the lexicographic minimum
as canonical key. This enumeration is finite and nonempty; it
contains every T representative in the orbit because both the
initial reflected coordinates and target T coordinates lie in[-1,1]
or[0,1], so translations cannot lie outside that integer range.
Sign reflections preserve the even lattice. The canonical keys agree
on every closed edge/tie equivalence, including the phase hypotenuse.

ONLY S evaluation arguments are folded. Rectangle widths, clipped
patches, actual physical centers, inward signs, defect guards and the
corner point arguments are NEVER folded by this cache operation.
The degree and validated arithmetic/source identity belong in each
actual enclosure key. No raw vertex outside T is passed to a source
whose literal point domain is T.

## Ordinary-phase rectangle upper and its units

For a rational rectangle B=[a_l,a_h]x[b_l,b_h] in[0,1]², obtain
validated actual S uppers U_ij at its four raw vertices, through(8).
Let I_B U be the positive bilinear interpolant, and put

    q_B(a,b)=I_B U(a,b)
       +(M*p_hi²/2)[(a-a_l)(a_h-a)
                         +kappa²(b-b_l)(b_h-b)],
    U_B=max_(i,j) U_ij
       +(M*p_hi²/8)[(a_h-a_l)²+kappa²(b_h-b_l)²].  (9)

Then S^t<=q_B<=U_B on ALL of B, including its part outside T.
For a zero-width side the interpolation is identity in that coordinate
and its curvature term is0; a singleton uses its actual point upper.

For completeness, the smooth primitive component vector has coordinate
frequencies r/n and s/m with |r|,|s|<=n, including the corrected
exceptional mode. D08 signed-family Bernstein therefore gives
l1 second-derivative bounds M and kappa²M. Its nonnegative common
Peano kernel, applied before the l1 norm, gives remainder M/2 times
the two coordinate endpoint products in RADIANS. Replacing alpha,beta
by pi*a,pi*b contributes pi², safely replaced by p_hi² because
the products are nonnegative. Their maxima are width²/4, proving(9).
This is the already proved D08 all-n calculation. S itself need not
be differentiable; its cusp is not treated as smooth or squared-even.

## Actual radius and rational outer proxies

Let P=B intersect T, or any declared rational closed triangle/rectangle
patch intersected with T and enclosed in B. All exact lower-dimensional
intersections are retained. Define the ACTUAL sets

    A_N=P intersect{pi(a+b)<=1/2},
    A_F=P intersect{pi(a+b)>=1/2}.                  (10)

They cover P with their shared closed seam. Their exact rational
OUTER proxies are

    gamma_minus=1/(2*p_hi), gamma_plus=1/(2*p_lo),
    Q_N=P intersect{a+b<=gamma_plus},
    Q_F=P intersect{a+b>=gamma_minus}.             (11)

Because p_lo<=pi<=p_hi, A_N is a subset of Q_N and A_F is a subset
of Q_F. All proxies are rational compact polygons, possibly empty,
segments or points, and may overlap. Their only use is to bound S.
The projected defect floor(7) is applied ONLY on A_N at a physical
noncorner center. Membership in Q_N does NOT prove its radius guard.

For each nonempty proxy require validated rational upper values

    V_N>=max_(Q_N) q_B, V_F>=max_(Q_F) q_B.         (12)

Taking either upper to be U_B is always allowed. A sharper exact
quadratic maximum is optional: enumerate the rational polygon vertices;
on each segment edge test its endpoints and any interior stationary
parameter of its rational quadratic restriction; and in dimension2
test the rational stationary point when the Hessian is invertible.
If the Hessian is singular and an interior maximum is stationary,
q_B is constant along a nonzero Hessian null direction through that
point; extend to the boundary, which already has that value. Thus
no maximum is lost. Constant/linear restrictions and dimension0/1
polygons use the point/edge rule. All coefficients, intersections,
stationary parameters and values are rational, so this is a finite
exact maximization, not a numerical optimizer or a new root job.
An empty proxy is discarded only after exact emptiness verification
and supplies no unchecked default value.

## Leaf predicates and exact closed coverage

A nonempty P is accepted by ONE of these alternatives:

- **FAR:** a validated upper V>=max_P q_B satisfies V<L.
  One may take V=U_B. This handles every center and every radius.
- **NEAR:** an exact rational guard proves max_P(a+b)<=1/(2*p_hi),
  and a validated V>=max_P q_B satisfies V-1/32<L. Premise3 is
  also required. This makes ALL of P actually near, including equality.
- **SPLIT:** for each nonempty proxy in(11), require its comparison

      V_N-1/32<L for Q_N nonempty,
      V_F<L       for Q_F nonempty,                 (13)

  and require premise3 for the actual-corner near case. Empty proxies
  make only their associated actual branch vacuous. The near comparison
  is used only after actual membership in A_N, not throughout Q_N.

All comparisons are strict EXACT rational inequalities. A nonempty
proxy is conservatively checked even if its actual branch is empty.
At the actual seam rho=1/2 both branches are covered; SPLIT requires
both relevant proxy comparisons. A whole-NEAR leaf may omit the far
comparison because its independent guard puts every point under(7)
or premise3. For P=B intersect T its convenient exact guard is

    2*p_hi*min(a_h+b_h,1)<=1.                      (14)

For a nonempty clipped rectangle, min(a_h+b_h,1) is its maximum
coordinate sum. If a_h+b_h<=1 the upper-right vertex attains it.
Otherwise the line a+b=1 intersects B whenever a_l+b_l<=1,
by continuity on a segment from its lower-left to upper-right corner.
This proves(14), including every tangency.

The simplest accepted COVER witness is a FINITE complete binary tree
rooted at[0,1]². Each internal node declares an axis and splits its
rectangle at the EXACT rational midpoint, with BOTH child subtrees
present. Starting with the root, reconstruct all child rectangles.
Require valid finite syntax, positive split progress, all children,
no missing/pending subtree or trailing token, and a leaf predicate
for every nonempty clipped leaf. Distinct leaves are prefix-free.
The two CLOSED children have exactly their closed parent as union.
Induction therefore proves their clipped leaves cover every point
of T, including all shared faces, chart ties and the hypotenuse.

For a leaf B in this root, its intersection with T is empty IF AND
ONLY IF

    a_l+b_l>1.                                    (15)

Indeed every coordinate sum in B is>=a_l+b_l; if this is<=1 the
lower-left vertex belongs to T. Thus the OUTSIDE predicate may omit
the leaf only under strict(15). Equality leaves a real tangent point
and MUST be bounded. No float midpoint classification, sampled
membership or caller Boolean proves COVER or emptiness.

A finite family of rational triangles/rectangles is also allowed
if exact closed coverage T subset union(P_i) is independently proved.
For example, their finite rational supporting-line arrangement can
be checked on every relatively open face of dimensions0,1,2 in T.
Membership in each closed patch is constant on a relatively open
face since its boundary lines are in the arrangement. Exact rational
interior representatives and all incidences therefore verify the
entire closed union, including degenerate intersections. A triangle
may use any enclosing rectangle B for(9); its interpolation region
need not be the triangle itself. None of these finite verifiers
asserts that a successful certificate can be generated.

## A same-degree three-ACTUAL-point corner witness

The following explicit witness supplies premise3. Use positive
rational a_*,b_* whose radian rectangle contains the inward half
diamond. It is sufficient to check p_lo*a_*>=1/2 and p_lo*b_*>=1/2,
or prove this containment separately. For the requested primary

    a_*=1/4, b_*=3/16,

containment already follows from pi>3: both pi/4 and3pi/16 exceed
1/2. No numerical geometry experiment is needed. For different
endpoints the containment is a separate actual-domain proof.

Obtain ACTUAL corrected lambda point uppers W_x,W_y,W_xy for the
canonical corner chart(5) at

    (A,B)=(pi*a_*,0),(0,pi*b_*),(pi*a_*,pi*b_*).

The D07-type inward PHYSICAL angle-turn inputs for those values are

    (a_*/n,0),(0,b_*/m),(a_*/n,b_*/m),              (16)

not(a_*,b_*). Put u'=a_*²/2,v'=b_*²/2 and define exact safe losses

    d_x=L-W_x, d_y=L-W_y, d_xy=L-W_xy,
    q=min(d_x/u',d_y/v',d_xy/(u'+v')),
    t=(M*p_hi^4/6)*max(u',kappa^4*v').             (17)

The witness passes only if

    q>t.                                          (18)

In particular all three losses are positive. The right side is
DYNAMIC in the independently proved same-degree M and kappa, not
an inherited norm34 or a fixed512 threshold. Let

    e=(q-t)/p_hi²>0.                               (19)

Then throughout the CLOSED actual corner rectangle,

    Lambda_n(A,B)<=Lambda_c-(e/2)(A²+B²).          (20)

To prove this directly from the all-n D08 theorem, set

    u=A²/2, v=B²/2, U=pi²*u', V=pi²*v', c=q/pi².

The safe losses satisfy d_x>=cU,d_y>=cV,d_xy>=c(U+V).
For the SMOOTH signed cardinal functions the global M bounds second
derivatives in u,v by M/3 and kappa^4*M/3. This is D08's even
signed-family fourth-derivative argument, valid for every n>=2,
including the two axes and the double origin. Its common Peano
remainder in the actual norm is

    (M/6)[u(U-u)+kappa^4*v(V-v)].

Positive bilinear weights cancel the mixed terms in the three losses
and give total loss>=c(u+v). The remainder is at most
(M/6)*max(U,kappa^4*V)*(u+v). Thus the net coefficient is

    epsilon=[q-(M*pi^4/6)*max(u',kappa^4*v')]/pi²
            >=(q-t)/p_hi²=e>0,

proving(20). Both substitutions contribute their required pi powers;
the criterion is pi_hi^4, not pi_hi². The true origin entry in the
bilinear interpolation is EXACTLY Lambda_c. Replacing it by a
rounded upper would introduce a positive constant error and would
not prove punctured-origin strictness. Only L minus point uppers is
used for the three nonorigin losses. This argument neither makes S
smooth in squared coordinates nor assumes fixed cardinal signs.

The node-preserving x/y reflections established in(4)--(5) transfer
the SAME losses, M, kappa and bound to the other actual corner in
its inward chart. Therefore(20) supplies premise3 on both full
closed inward half diamonds. Another independently proved strict
actual-corner patch may replace(16)--(20), but its actual domain
and equality set must explicitly cover that same half diamond.
An old energy theorem restricted to degrees<=128 cannot supply
this premise at n>=160 without a separate valid extension.

## Global proof and exact equality set

Take an arbitrary physical point and its odd-center chart(2).
Put a=|alpha|/pi,b=|beta|/pi. The signed radius gives(a,b) in T,
and separate evenness(8) gives S_n(alpha,beta)=S^t(a,b).
Exact COVER supplies an accepted closed patch P containing(a,b).
It cannot be an OUTSIDE leaf because(15) is strict.

If P uses FAR, then(3),(9) and its strict comparison give

    lambda_n<=S^t<=V<L<=Lambda_c.                  (21)

Otherwise suppose first that the ACTUAL rho=pi(a+b)<=1/2.
For SPLIT the point belongs to Q_N and its near upper is available.
For NEAR its guard supplies the same bound over all P. If the
center is noncorner, (7) gives

    lambda_n<=S^t-1/32<=V_N-1/32<L<=Lambda_c,      (22)

with the whole-P V in place of V_N for NEAR. No projection is added
to another, and no floor was applied outside its guard. If instead
the center is one of(4), its admissible phase signs are exactly the
inward chart signs previously proved. Premise3, or(20), gives strict
lambda_n<Lambda_c unless alpha=beta=0. At that zero phase the
point is exactly the actual corner, where(6) gives equality.

If the actual rho>1/2, a whole-NEAR patch is impossible by its guard.
For SPLIT the point is in Q_F and its far bound gives(21). The
rho=1/2 seam is included in the near proof and, when present, in
the far proof too. Thus every physical point except the two listed
corners is strictly lower. The two actual corner values are equal
by their node-preserving reflection and are Lambda_c by(6).
This proves(1). Finite-polynomial continuity also ensures the global
maximum exists; no localization of an unknown maximizer was used.
No uniform positive margin is claimed in a neighborhood approaching
either corner, where the intended loss vanishes quadratically.

## Norm witnesses, source guards and execution boundary

The core theorem permits ANY independently proved rational global M.
After separate acceptance, the D14 quarter-grid implication is one
model-free way to obtain it: validate the15 points(i/4,j/4),i+j<=4,
canonicalize them by(8), let V bound their finite maximum, and take
any rational M>=784V/663. Its finite-grid norm proof, not the
sampled maximum itself, supplies global validity. Those point
enclosures may be shared with the complete cover only if their
degree/input/source/arithmetic identities agree. The D14 review
obligation is not waived by this optional composition. A completed
model, D09 norm34 or existing512 receipt is not a required premise.

The mathematical statement applies to EVERY integer n>=160.
It is NOT a claim that a particular executable supports that range.
Read-only inspection at this input found D07's actual-point guard
`2<=n<=2048` and inward turn guard[0,1]; C11's point/partial integer
guards include2048 and its point domain is the closed T. Their
literal precision, tails, failure/fallback behavior and guards are
unchanged. This makes2048 an allowed source-domain candidate by
inspection, not a completed source audit or successful computation.
The old D11/D10 adapter's hardcoded512 is not thereby generalized.
No generic executable for n>2048, guard widening or numerical
source evaluation is licensed by this theorem. Such an instance
would need its own validated evaluator and accepted implementation.

Before an actual certificate can establish(1), an independent checker
must authenticate n and every same-degree premise, validate/replay
the outward point enclosures, prove the chosen global norm, reconstruct
canonical S keys and exact closed geometry, verify all strict rational
comparisons and the actual corner witness, and preserve the complete
source/tail/runtime trusted base. Missing data, nonfinite endpoints,
unsupported domains, an incomplete tree, malformed keys, unvalidated
arithmetic or a failed strict comparison forbids acceptance. FLOAT
producer success, a sampled maximum or source inspection alone supplies
none of these premises. Code/input/evidence pins are separate from
prose records. Distinct mathematical/source review and root release
must precede any D15 native run under its own explicit protocol.

No numerical/native, kernel, phase, board, root, quadrature, producer
or checker job ran for this proof. It proves no successful2048
instance, another degree, certificate existence, termination, useful
leaf count, bit complexity, performance scaling or historical speedup.
All older finite/global theorems retain their exact quantifiers and
dependencies; this is a separate sufficient implication.

## Provenance and remaining review

2026-11-06, parent-assigned Codex gpt-6.1-sol xhigh20min, input/rules
`8040e0b2c9869a7871ad1825e9b9c746186db084`; serving metadata unexposed.
The complete relevant gate preceded this new generic candidate, as
recorded in `../ideas/D15-generic-cover.md`. Only its new idea,
attempt and this theory file were written. No old D10/D14/source/
evidence, shared registry or mutable Git state was changed.

Developer mathematical status is PROVED under the explicit witness
hypotheses. Distinct Astra high review of the frozen generic proof
is required BEFORE any D15 source/run release. Successful witness
generation and independent actual instance replay remain OPEN until
performed in their separately authorized scope. Final Claude audit
and root's adoption/publication remain separate obligations.


### Supplementary review closure — 2026-11-06

Distinct mathematical reconstruction ACCEPTED this unchanged developer
scope; [independent-checks-D15-generic-cover.md](../independent-checks-D15-generic-cover.md),
report SHA2564ea70bd2f18260e5321db44d6296b3cf3886901c86a298fd324bbdb06593fd90.
The preceding pending supplementary-review wording is historical. Exact
review scope, process notes and computational provenance remain in that
report. Final Claude audit is separate; executable instance/source release
is not implied by acceptance of a sufficient mathematical contract.
