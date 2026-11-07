# PD-T?argmax-bridge-codex-D32 — Generic guarded point-to-cover sufficiency from degree41

ID kind: PD-T. Aliases: radius-aware low-domain phase certificate;
actual-near subset guard; final-witness norm and corner assembly.
Split from: new D32 lower-domain generic contract, not an edit of D15.
Split into: concrete degree certificates, executable validity and cost
claims remain separate. D29's new floors have their own three files.

## Exact statement and status

For EVERY integer n>=41 put m=n+1,N=nm,kappa=n/m. Use precisely
PD-T101/PD-T364's corrected even-checkerboard Padua cardinals, original
endpoint weights and finite-polynomial values at collisions. Let

    Lambda_c=lambda_n(-1,-1), S^t(a,b)=S_n(pi*a,pi*b),
    T={(a,b):a>=0,b>=0,a+b<=1}.

Suppose these independently valid SAME-DEGREE witnesses are supplied:

1. Rational0<p_lo<=pi<=p_hi and a rational0<L<=Lambda_c.
2. A proved rational GLOBAL bound M>0 for S_n on ALL real phases.
   The optional grid or own-tree witnesses below suffice; a sampled
   maximum without their norming proof does not.
3. A finite exact CLOSED cover of T by patches P_B=B intersect T,
   with rational rectangles B in[0,1]², validated actual S uppers at
   every needed raw vertex, and the strict leaf alternatives below.
4. For every retained B whose near comparison is used, a rational
   delta_B>0 with a PROVED floor witness: for every physical noncorner
   odd center and every admissible signed phase satisfying

       |alpha|+|beta|<=r_B,
       r_B=min(1/2,p_hi*(a_h+b_h)),                  (1)

   its exact full defect obeys Delta_JK>=delta_B. A valid weaker
   lower floor may be used. The theorem/domain establishing it is a
   premise; positivity or numerical sampling does not establish it.
5. At BOTH actual nonnode corners an independently proved patch covers
   the CLOSED inward half diamond A,B>=0,A+B<=1/2 and gives

       lambda_n<=Lambda_c,
       lambda_n<Lambda_c unless A=B=0.              (2)

   The explicit same-degree three-ACTUAL-point test below is one
   sufficient witness, valid mathematically for every n>=2.

Then

    max_[-1,1]² lambda_n=Lambda_c,
    argmax lambda_n={(-1,-1),(1,-1)} for even n,
                   ={(-1,-1),(-1,1)} for odd n.     (3)

The theorem includes every closed boundary, chart tie, node, initially
zero term and removable kernel collision. It is a sufficient implication,
not a statement that any witness exists, can be produced, passes, or has
a bounded point count/runtime. It proves no new finite argmax degree.

Overall status: **PROVED analytic developer sufficient implication**
under the explicit valid-witness hypotheses above; distinct mathematical
review pending. The optional D29/D27 substitutions below remain
**CONDITIONAL on their own distinct review/acceptance**, pending at this
write. The core implication does not assume those pending results.

## Exact objects and accepted dependencies

Set h_0=1,h_j=2 for j>0 and

    G_n(u,v)=sum_(r+s<=n)h_r*h_s*cos(ru)*cos(sv)-cos(nu),
    S_n(alpha,beta)=(1/(2N))*sum_(0<=j<2n,0<=k<2m,j+k odd)
       |G_n((j*pi+alpha)/n,(k*pi+beta)/m)|.           (4)

The exceptional(n,0) coefficient is ONE. Finite polynomials define
all values, including collisions. Physical nodes have0<=j<=n,
0<=k<=m,j+k even. Their weights are2e_j*f_k/N, with endpoint e,f=1/2
and interior e,f=1. The cardinal expression sums its four reflected
finite kernels BEFORE taking its absolute value. N is the mesh product,
not the number of nodes.

Physical odd centers have0<=J<=n,0<=K<=m,J+K odd and admissible phases

    |alpha|+|beta|<=pi,
    -J*pi<=alpha<=(n-J)*pi,
    -K*pi<=beta<=(m-K)*pi,
    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m.          (5)

PD-T364 gives the exact full identity and separate projection bounds

    lambda_n(cos theta,cos phi)=S_n(alpha,beta)-Delta_JK,
    Delta_JK>=max(Q_h(J),Q_v(K))>=0.                (6)

Endpoint residues have two coincident reflected preimages, each with
half weight; interior residues have one with full weight. Consequently
(6) has no endpoint correction. Projections are lower bounds for the
full defect and are never added or substituted into its exact identity.

| Dependency | Scope used here |
|---|---|
| PD-T364/PD-T101 | All n>=2 exact objects, full physical cover, defect, corner equality and parity reflections |
| Accepted D08 ordinary Peano/Bernstein and actual three-loss theorem | All n>=2; ordinary S phases and squared ACTUAL cardinal phases are distinct |
| Accepted D14/D19 | All n>=2 optional global norm witnesses from valid same-degree vertices |
| C02 dense-band defect | Only its original n64/n160/n4096 guarded domains, when chosen |
| Explicit valid floor, point and corner witnesses | Hypotheses; pending D29/D27 are optional substitutions only |

D15's accepted literal n>=160 statement and D21's n>=4096 statement
remain unchanged. This proof reconstructs their assembly at the stated
lower domain using an explicit floor premise. No old finite receipt,
completed-model norm or asymptotic primitive comparison is required.
An analytic corner substitution can introduce its own model/PD-T271
dependencies and must retain them explicitly.

## Closed geometry, canonical keys and Peano upper

A finite complete binary midpoint tree rooted at[0,1]² is a sufficient
cover representation. Decode both CLOSED children at every exact rational
midpoint, require positive split progress and finite valid syntax, and
reject missing/pending subtrees or trailing tokens. At a leaf B retain
P_B unless a_l+b_l>1. This is the exact emptiness criterion: otherwise
the lower-left vertex itself belongs to T. Equality is a real tangent
point. The closed-child union identity proves full closed coverage by
induction, including shared edges and the hypotenuse. Another finite
rectangle family with an independently proved exact closed cover is
equally sufficient.

For integers p,q with p+q even, exact finite reindexing gives

    S^t(a+p,b+q)=S^t(a,b),
    S^t(-a,b)=S^t(a,b)=S^t(a,-b).                  (7)

For raw vertices in[0,1]² first fold(a,b) to(1-a,1-b) when a+b>1.
Only ON the hypotenuse may the canonical T key be chosen as the
lexicographic minimum of(a,b),(b,a). Equivalently enumerate the exact
even-lattice/separate-sign orbit. There is no interior coordinate
interchange or n,m swap. Folding changes evaluation arguments only,
never the rectangle, its widths, center indices, signs or radius guards.
Keys include n and the validated arithmetic/source identity.

For validated vertex uppers W_v let I_B W be their positive bilinear
interpolant and define

    theta_B=(p_hi²/8)[(a_h-a_l)²+kappa²(b_h-b_l)²],
    V_B=max_(raw vertices v)W_v,
    q_B=I_B W+(M*p_hi²/2)[(a-a_l)(a_h-a)
                          +kappa²(b-b_l)(b_h-b)],
    U_B=V_B+theta_B*M.                              (8)

Then S^t<=q_B<=U_B on the ENTIRE B, including portions outside T.
Zero-width factors are0 and interpolation is the identity in a collapsed
coordinate. D08 proves this by applying a common nonnegative ordinary
Peano kernel to the SMOOTH signed component vector before its l1 norm.
The global derivative bounds are M,kappa²M in radians; turn coordinates
contribute pi², safely replaced by p_hi². S itself need not be smooth.

## Actual near radius and strict leaf alternatives

For nonempty P_B let low=a_l+b_l, high=min(a_h+b_h,1). These are its
exact sum extrema. If a_h+b_h>1, the segment from lower-left to
upper-right meets a+b=1, proving the upper endpoint also in tangent
cases. Define ACTUAL closed sets and rational OUTER proxies

    A_N=P_B intersect{pi(a+b)<=1/2},
    A_F=P_B intersect{pi(a+b)>=1/2},
    Q_N=P_B intersect{a+b<=1/(2*p_lo)},
    Q_F=P_B intersect{a+b>=1/(2*p_hi)}.             (9)

They satisfy A_N subset Q_N,A_F subset Q_F and A_N union A_F=P_B.
The proxies may overlap. They bound S, not defect-domain membership.
Q_N is nonempty iff low<=1/(2*p_lo); Q_F is nonempty iff
high>=1/(2*p_hi). Equality retains a tangent proxy.

At an ACTUAL near point of P_B,

    rho=|alpha|+|beta|=pi(a+b)<=1/2,
    rho<=p_hi*(a_h+b_h), hence rho<=r_B.            (10)

This proves the full signed-radius guard for the floor in premise4,
even when B crosses the near/far seam. It does not establish that every
point of Q_N or B satisfies rho<=1/2. It needs no monotonicity assertion
about a chosen floor function of r. Apply the floor pointwise ONLY after
the actual near branch and a noncorner physical center are established.

Every retained leaf must pass at least one strict EXACT rational rule:

- **FAR:** a valid V>=max_(P_B)q_B obeys V<L.
- **NEAR:** 2*p_hi*high<=1 and a valid V>=max_(P_B)q_B obeys
  V-delta_B<L. The independent actual-corner premise5 is used as needed.
- **SPLIT:** for each nonempty proxy require V_N>=max_(Q_N)q_B,
  V_F>=max_(Q_F)q_B and

      V_N-delta_B<L when Q_N is nonempty,
      V_F<L         when Q_F is nonempty.           (11)

  The independent actual-corner premise5 is used on its actual near
  branch. An empty proxy makes only that actual branch vacuous.

Taking every V,V_N,V_F=U_B is always a valid conservative option.
D15's exact polygon maximization is also allowed: test vertices and
stationary points of edge restrictions, and the interior stationary point
when the Hessian is invertible. For a singular Hessian, an interior
stationary maximum extends along a null direction to the boundary with
the same value. This includes constant, linear and degenerate0/1D
proxies. All coefficients and tests are rational. No numerical optimizer
or unverified empty-set flag establishes these upper bounds.

All required comparisons are strict. At the actual seam both branches
are closed; SPLIT checks both nonempty proxies. A whole-NEAR leaf may
omit far comparison only because its separate rational guard proves
actual nearness throughout. FAR works at every center/radius without a
floor. The floor is never applied to an actual corner.

## Optional floor substitutions and their exact scopes

For0<=r<=1/2 put

    a=1-r²/4,
    U=347a/1000-157r/500, V=17a/20-r/2,
    W=779a/750-5r/6,
    B_n(r)=11711U/48400-120V/(157n)
                -250W/(157n)-100V/(3n²).           (12)

The U,V,W in(12) are scalar defect auxiliaries, unrelated to vertex or
polygon upper symbols in(8)-(11). The following are valid substitutions
IF their named theorem is valid/accepted on its stated domain:

| Integer degree | Permitted delta_B, with r=r_B | Dependency status at this write |
|---|---|---|
| 41..63 | max(1/512,min(1/32,B_n(r))) | D29-radius41, distinct review pending |
| 64..159 | max(1/64,min(1/20,B_n(r))) | Accepted C02 original domain |
| 160..511 | max(1/32,min(1/20,B_n(r))) | Accepted C02 original stronger tier |
| 512..4095 | 1/20 | D29-floor512, distinct review pending |
| 4096 and above | 1/16 | Accepted C02 original strongest tier |

Every noncorner physical odd center has at least one interior index;
the corresponding applicable projection supplies the floor, and(6)
transfers it to Delta. The other projection is not added. Any weaker
proved positive floor remains allowed, so pending D29 never invalidates
an otherwise independently supplied witness. D29's n41 uniform1/512
is another optional simpler witness, also pending distinct review.
There is no extension of C02's n64 formula by citation below64.

## Same-degree actual-corner witness, without a source-domain extension

Let W_x,W_y,W_xy be validated ACTUAL corrected lambda uppers in the
canonical inward chart

    Lambda_n(A,B)=lambda_n(-cos(A/n),-cos(B/m))

at(A,B)=(pi/4,0),(0,3pi/16),(pi/4,3pi/16). Let

    d_x=L-W_x, d_y=L-W_y, d_xy=L-W_xy,
    u'=1/32, v'=9/512,
    q=min(d_x/u',d_y/v',d_xy/(u'+v')),
    t=(M*p_hi^4/6)*max(u',kappa^4*v')
      =M*p_hi^4/192.                               (13)

Require q>t and put e=(q-t)/p_hi²>0. Accepted unrestricted D08 gives
on the ENTIRE closed rectangle0<=A<=pi/4,0<=B<=3pi/16,

    Lambda_n(A,B)<=Lambda_c-(e/2)(A²+B²).           (14)

Indeed its squared variables are u=A²/2,v=B²/2, endpoints pi²u',pi²v',
and loss coefficient c=q/pi². Its remainder coefficient is
(M/6)max(pi²u',kappa^4*pi²v'). Thus the exact net coefficient is
[q-(M*pi^4/6)max(u',kappa^4v')]/pi²>=e. The pi^4 factor is essential.
The origin interpolation entry remains the TRUE symbolic Lambda_c;
only nonorigin losses use L. No rounded origin upper is substituted.
Both pi/4 and3pi/16 exceed1/2 since pi>3, so(14) supplies(2).

The same global M bounds physical lambda by(6), hence all complete
signed cardinal families. Actual corner substitution remains in the
physical square for all real A,B, giving D08 its required GLOBAL norm.
Separate evenness of signed cardinals justifies the squared coordinates;
the argument does not assume S is smooth in them or fix cardinal signs.

The corresponding inward PHYSICAL angle-turn inputs are

    (1/(4n),0), (0,3/(16m)), (1/(4n),3/(16m)).      (15)

They are not the turn phases1/4,3/16. The D08 theorem is valid for every
n>=2, while the unchanged D07 actual-point source has literal degree
guard2<=n<=2048. Hence fresh use for41..1023 is within its inspected
degree domain, subject to a separate source contract/review and actual
successful enclosures. This is not a claim of implementation support
or successful lambda calls for every n>=41.

For n>=1024, D27's new analytic pi/4 square with radial loss1/8 may
replace(13)-(15) ONLY after its independent result review/root adoption.
It retains its own analytic norm/model and PD-T271 dependencies; the
phase Peano norm need not equal that inherited analytic norm. Accepted
D17 already supplies a pi/6 square with loss1/8 from4096. Either square
contains the inward half diamond. Any other independently validated
patch satisfying(2) is allowed. For2049..4095, D07's unchanged guard
alone supplies no corner point witness; pending D27 is not acceptance.

## Final global norm and retained premises

The finite continuous S has a finite true global maximum M*, attained
on T: reduce(alpha+beta)/(2pi),(alpha-beta)/(2pi) into[-1/2,1/2]
by integer translations and use(7). This proves global finiteness BEFORE
any sample or derivative estimate. D08 with M* gives

    S^t<=V_B+theta_B*M* on B.                       (16)

For the final complete tree, if EVERY retained theta_B<1, apply(16)
at a maximizing point and a retained leaf containing it. It follows

    M*<=R=max_(retained B)V_B/(1-theta_B).           (17)

Thus any rational M>=R is a valid final norm, including ceil(R).
This accepted D19 argument uses exactly the FINAL retained leaf-corner
union and retains tangent leaves. It is not an equality of continuous
and sampled maxima.

Alternatively the accepted D14 quarter-grid uses the15 points
E={(i/4,j/4):i,j>=0,i+j<=4}. Their exact canonical union has13 keys,
by the two nontrivial hypotenuse pairs. With their validated upper
maximum V_E, any rational M>=784V_E/663 is global. Its ten closed
quarter-square covers and Peano absorption, not the sample maximum,
prove that factor. A separately proved global M is also allowed.

A producer may use the coarse grid first, then build/refine/prune a
tree. This has no effect on the logical FINAL requirements. If it uses
the grid norm in the final proof, retain/authenticate every grid upper
needed by that proof. If it drops those points, derive the replacement
M from the final tree or another retained valid witness. On EVERY norm
change, recompute the entire final collection of Peano bounds, phase
predicates and norm-dependent actual-corner criterion. For an analytic
corner branch reauthenticate its theorem/domain/dependencies; it does
not acquire an artificial dependence on the chosen phase M. No old
grid, discarded child, old degree or previous passing margin may be a
hidden premise. A final norm derived from a smaller set need not equal
or improve the discovery norm; success is checked, not presumed.

## Complete physical proof and equality set

Every physical mesh cell has two odd vertices. In normalized local
coordinates their L1 distances are x+y,2-x-y or1-x+y,1+x-y; each
pair sums to2. One distance is<=1. Taking an adjacent physical cell
on a square boundary proves(5) covers EVERY physical point, with all
ties and edges retained. Apply separate phase evenness and put
a=|alpha|/pi,b=|beta|/pi. Then(a,b) belongs to T and its closed cover
contains it in a retained P_B.

The odd endpoint-pair centers are exactly(n,m),(0,m) if n is even,
or(n,m),(n,0) if n is odd. Every other odd center has an interior
index. At(n,m), admissibility forces alpha,beta<=0, the canonical
inward phases. If n is even, x reflection j->n-j preserves node parity
and weights and transfers the chart to(0,m). If n is odd, m is even
and y reflection k->m-k transfers it to(n,0). Neither swaps n,m.
The two corner values agree. At these corners all four reflected
kernels coincide, Delta=0, and(6) gives S_n(0,0)=Lambda_c. Thus an
actual lower S(0,0) endpoint is a permitted L in premise1.

For FAR,(6),(8) and its comparison give lambda<=S^t<=V<L<=Lambda_c.
Otherwise take an ACTUAL near point. For a noncorner center,(10)
establishes the exact floor premise and lambda=S^t-Delta<=V-delta_B<L;
for SPLIT use V_N since the point is in Q_N. At an actual corner the
admissible signs are precisely the inward ones just enumerated, so(2)
gives strict descent except at its origin. Actual far points with
rho>1/2 cannot occur in a whole-NEAR leaf; their Q_F comparison gives
the FAR exclusion. The actual seamrho1/2 is retained and safe by both
closed branches. Every noncorner zero-phase point uses its noncorner
floor; it is not an exempt equality point.

Only the two actual corner origins remain, both attaining Lambda_c.
Even endpoint-pair node corners have value1 and occur at nonzero
odd-chart phases, so no additional origin/equality point arises. All
cardinal zero terms and collisions retain their finite-polynomial
values throughout. This proves(3), with no assumed location of an
unknown maximizer. No uniform positive loss near either equality
corner is claimed; the actual-corner loss vanishes quadratically. QED.

## Compact certificate essentials and arithmetic boundary

A self-contained final receipt, together with its authenticated interval
data/trusted base, must retain enough to recompute at least:

1. n, corrected object identity, rational pi bracket, same-degree origin
   lower L and the chosen floor/corner theorem identities and domains.
2. Complete exact closed tree/cover geometry, including tangent leaves;
   the complete union of needed canonical S keys; actual physical corner
   point keys when that branch is used. Every used enclosure must have
   validated endpoints, correct argument/degree and source/arithmetic pins.
3. The final norm proof and ALL its retained point premises: final own
   corners for(17), explicit grid keys for D14, or an independent proved
   norm witness. Its rational M must be recomputed/checked.
4. Every r_B,delta_B, actual-near guard, proxy emptiness condition,
   q_B/U_B upper and strict chosen predicate, recomputed from those final
   premises. Stored leaf tags/margins alone are not verification.
5. The actual three-point losses and(13), or the valid analytic corner
   branch, with symbolic origin equality and both parity-correct charts.

These need not all be duplicated in a small summary if exact authenticated
inputs and a checker reconstruct them. Missing norm-support points or an
unvalidated interval cannot be replaced by a count, hash list or producer
success Boolean. No float classification, sampled maximum or source
inspection alone supplies any of the witness premises.

D23's cheap lower-order full-row inclusion is proved for every n>=2
under its exact row/guard/tail hypotheses; its specially small uniform
error corollary is only for160<=n<=2147483647. At41..159 charge the
ACTUAL returned widths, all analytic tails and numerical radii. Do not
import that small corollary below160. The actual four-copy lambda API
is distinct from the common-S row evaluator. Current finite integer
source guards likewise do not establish executable support for every
mathematical degree in this theorem.

No numerical/native/scalar job, implementation, guard edit or finite
instance was performed for this proof. Future implementation/source/SPEC,
distinct review, root release, actual completed result and independent
replay are separate. Certificate existence/termination, optimal pruning,
small point count, uniform cost and all-degree argmax remain unclaimed.

## Provenance and next obligation

2026-11-06, Codex requested gpt-6.1-sol xhigh20min mathematical developer;
serving metadata unexposed. Input `4f8c169171e55b7d5f00f57a8b3ce8340a498960`;
unchanged rules read at `02beaef2b22f8232286713dab0a1b7c95582ce13`.
Gate and unsuccessful/deferred alternatives are preserved in the new
idea/attempt records. Only the three assigned new D32 prose files were
written. Distinct mathematical review must check this implication before
use; D29/D27 pending dependencies and any implementation stay separate.


## Root review closure — 2026-11-06

Distinct [D32 review](../independent-checks-D32-cover.md), SHA256 `82a4a38e3cabd181c3afd15fc268dee8d841fd8ffdf235315701082bf6b575f4`, accepts the generic n>=41 sufficient implication and explicit source/domain limitations. Root adopts that implication; D29 floor and D27 analytic-corner substitutions are now independently accepted at their stated ranges. This dated note supersedes only historical pending wording and preserves the reviewed proof prefix. No degree41 instance, producer termination or executable source release follows. Final Claude audit remains separate.
