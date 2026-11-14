# PD-T?argmax-bridge-codex-D06-four — Cubic-over-quartic aliases for actual four-copy rows

ID kind: PD-T. Aliases: parity-grid rational alias; cubic-over-quartic
cosine row; actual physical lambda row blocks; four reflections before
absolute value; point-only bounded root count. Split from: the proposed
cheap actual-function row evaluator.
Split into: none. The evaluator/certifier target remains OPEN; this file
proves its exact structural reduction, not its implementation or cost.

## Statement and conventions

Let n>=2, m=n+1, N=nm, and fix a physical point
(cos theta,cos phi), 0<=theta,phi<=pi. Put

    xi=pi-theta, zeta=pi-phi, b_r=r*pi/m,
    t_j=j*pi/n,
    O={(j,r):0<=j<=n, 0<=r<=m, j+r odd}.

The factors e_j,f_r equal 1/2 at the endpoints of their own meshes and
1 in the interior. Use precisely the accepted corrected Padua kernel

    P_n(x)=T_n(x)+T_m(x),
    D_n(u,v)=[P_n(cos u)-P_n(cos v)]/[cos u-cos v],
    G_n(u,v)=D_n(u,v)-cos(nu).                         (1)

D_n is its finite polynomial divided difference on the diagonal. Thus
there it equals P_n'(cos u); no rational singular expression defines a
cardinal. Equivalently D_n is the accepted finite rhombus cosine sum.

For a row r define the complete four-copy value

    V_r(t)=sum_(sigma,tau in {+1,-1})
                   G_n(xi+sigma*t,zeta+tau*b_r).       (2)

Here (2) is a finite polynomial expression for every t. The actual
Lebesgue function is exactly

    lambda_n(cos theta,cos phi)
       =(1/(2N))*sum_(r=0)^m f_r
                   sum_(0<=j<=n, j+r odd) e_j*|V_r(t_j)|. (3)

For each fixed r, all noncollision parity-grid values in (2) agree
with a rational function Q_r(z)/B_r(z), z=tan(t/2), where

    deg Q_r<=8, deg B_r<=8, B_r not identically zero.   (4)

The coefficients depend on the physical point, n and r. More precisely,
the alias has the form U_r(c)/W_r(c), c=cos t, with deg U_r<=3 and W_r
monic of degree four. Thus there are at most four interior denominator
events and, unless U_r is zero, at most three interior numerator roots.
These events partition (0,pi) into at most eight open intervals on each
of which the rational alias has constant strict sign. If U_r is
identically zero, all its noncollision grid values are zero.

Every grid point at a denominator event is evaluated using the actual
finite expression (2), including removable collisions. The node-angle
endpoints t=0,pi are also direct actual terms, with factors 1/2. This
requires at most six direct four-copy terms per nonretained row.

Retain a whole physical row whenever sin(zeta+tau*b_r)=0 for either
tau. Such rows belong to the at-most-two labels

    b_r=zeta or b_r=pi-zeta.                          (5)

On each other row, each signed block sum is exactly a linear combination
of eight ordinary cotangent partial sums on mesh pi/n. Thus the full
point value (3) has O(n) bounded-degree polynomial/root-partition objects,
O(n) direct four-copy evaluations and O(n) cotangent-block objects.

These are guaranteed representation counts. No bound on root isolation,
coefficient generation, exact equality decisions, evaluation bit cost,
arithmetic precision or runtime is asserted. In particular (4) is an
identity for the parity GRID VALUES, not an identity between the true
polynomial V_r(t) and its rational alias for every real t.

Status: **PROVED**, analytic developer structural contract; distinct
independent review pending. A validated fast point evaluator, whole-box
upper, complete tail budget and global argmax bridge remain OPEN.

## Dependencies

PD-T101 supplies the corrected cardinal kernel and positive weights;
PD-T185 supplies (1)'s divided-difference identity; PD-T228 and
C02-corner-halfdiamond.md supply the already proved four-reflection
normalization, reconstructed below. N2/C02/C11 are predecessors for
cotangent partial sums, not proofs of an actual four-copy row formula.
C09/C12/C14/C15 concern common-S coefficient-vertex uppers and do not
supply the equality (3)-(4). N5's actual projected defects and N6's
two-trace obstruction are kept at their own scopes. PD-N085 is an affine
per-cardinal sign-preservation obstruction, not an assumption here.
No external theorem, source claim, numerical execution or fitted result
is a premise of this proof.

## Proof

### 1. Reflect node labels and preserve the actual normalization

Let an original even-board node have indices p,q, p+q even, and weight

    w_pq=2e_p*f_q/N.

The accepted corrected cardinal formula is

    L_pq(cos theta,cos phi)
      =(w_pq/4)*sum_(sigma,tau) G_n(theta+sigma*p*pi/n,
                                               phi+tau*q*pi/m). (6)

Set j=n-p, r=m-q. Then j+r is odd, since n+m=2n+1 is odd. This
reflection preserves the endpoint factors. Separate angular evenness
and 2pi periodicity of G_n turn the four arguments in (6), with their
multiplicities, into (xi+/-t_j,zeta+/-b_r). Therefore

    L_pq(cos theta,cos phi)=(e_j*f_r/(2N))*V_r(t_j).

The weights are positive, so summing absolute values proves (3).
Equivalently C02's F normalization gives sum_four F=(-1)^j*V_r/2,
so its coefficient 1/N also gives precisely the coefficient 1/(2N)
in (3). There is no extra factor of two from changing board parity.
Nothing has separated the absolute values of the four copies. Endpoint
copies that coincide are still counted with their original multiplicity;
the separate half endpoint factors are also retained. This proof uses
the finite polynomial and so covers all physical edges, corners and
initially zero cardinals without a sign assumption.

### 2. Freeze only the parity oscillation, keeping the corrected mode

Fix r and put

    epsilon=(-1)^(r+1), A=cos(n*xi), E=sin(n*xi),
    a=cos xi, b=sin xi,
    eta_tau=zeta+tau*b_r, y_tau=cos eta_tau.

For j+r odd one has (-1)^j=epsilon. Hence, at t=t_j,

    cos(n*(xi+sigma*t))=epsilon*A,
    cos(m*(xi+sigma*t))
       =epsilon*[cos(m*xi)*cos t-sigma*sin(m*xi)*sin t]. (7)

There is no residual dependence on j other than t and its fixed row
parity. Write w=xi+sigma*t. The elementary angle subtraction identity
rewrites the right side of (7) as

    P_n(cos w)=epsilon*[A*(1+cos w)-E*sin w]          (8)

on that parity grid. For cos w!=y_tau, subtract the corrected highest
mode epsilon*A in (1) BEFORE simplifying. Equations (1),(8) yield

    G_n(w,eta_tau)
       =[k_tau-epsilon*E*sin w]/[cos w-y_tau],
    k_tau=epsilon*A*(1+y_tau)-P_n(y_tau).             (9)

The subtraction is essential for k_tau and the normalization. Omitting
it would give a different rational numerator and a different cardinal.
Both P_n(y_tau) values are constants with respect to the node angle;
their degree-dependent construction cost has not disappeared.

Define the rational alias R_r(t) as the sum of the four quotients in
(9), wherever their denominators are nonzero. Equation (9) proves

    R_r(t_j)=V_r(t_j)

at all grid points where none of the four denominators vanish. The
substitutions in (7) are restricted to the parity grid, so this equality
is not asserted between samples.

### 3. Explicit half-angle polynomials and the uniform degree bound

For 0<=t<pi set z=tan(t/2). Then

    cos t=(1-z^2)/(1+z^2), sin t=2z/(1+z^2).

For each of the four labelled pairs (sigma,tau) put

    d_(sigma,tau)(z)
       =a*(1-z^2)-2sigma*b*z-y_tau*(1+z^2),
    h_(sigma,tau)(z)
       =k_tau*(1+z^2)
              -epsilon*E*[b*(1-z^2)+2sigma*a*z].      (10)

Both are real polynomials of degree at most two. Their quotient is
exactly the corresponding term of the rational alias. Define

    B_r=product_(sigma,tau) d_(sigma,tau),
    Q_r=sum_(sigma,tau) h_(sigma,tau)
                       *product_((sigma',tau')!=(sigma,tau))
                                            d_(sigma',tau'). (11)

The labels in the product retain repeated factors when copies coincide.
Equation (11) gives R_r=Q_r/B_r away from all denominator zeros and
proves (4). No expansion is required to establish the degrees.

None of the four d polynomials can be identically zero. Vanishing of
its constant, linear and quadratic coefficients would force
a-y_tau=0, b=0 and -a-y_tau=0, hence a=b=0, contradicting a^2+b^2=1.
Their product is therefore nonzero. The half-angle degree argument alone
would give eight denominator and eight numerator candidates. Pairing
the two sigma copies gives a sharper form without additional assumptions.
Write c=cos t, s=sin t. For each tau,

    sum_(sigma=+/-1)
       [k_tau-epsilon*E*(b*c+sigma*a*s)]/[a*c-sigma*b*s-y_tau]
        =ell_tau(c)/d_tau(c),
    d_tau(c)=c^2-2a*y_tau*c+y_tau^2-b^2,
    ell_tau(c)=2[(a*k_tau+epsilon*E*b*y_tau)*c
                              -(k_tau*y_tau+epsilon*E*b*a)]. (11a)

Indeed the denominator product is (a*c-y_tau)^2-b^2*s^2,
which is d_tau since a^2+b^2=c^2+s^2=1. The numerator product sum is
2k_tau*(a*c-y_tau)-2epsilon*E*b*(a-y_tau*c), exactly ell_tau.
Consequently define

    W_r(c)=d_+(c)*d_-(c),
    U_r(c)=ell_+(c)*d_-(c)+ell_-(c)*d_+(c).           (11b)

W_r is monic quartic and deg U_r<=3, with R_r=U_r/W_r at every
noncollision point of the alias. There is no hidden growing degree.
Moreover

    d_tau(c)=[c-cos(xi+eta_tau)]*[c-cos(xi-eta_tau)]. (11c)

Expanding the two factors proves (11c), using sin^2 eta_tau=1-y_tau^2.
Thus the four denominator event candidates are explicitly known cosines;
no general quartic isolation is needed to describe their set.

The map t->cos t is strictly decreasing on (0,pi). If U_r is nonzero,
its at-most-three real roots together with at most four denominator
events make at most seven distinct interior cuts and eight open
intervals. On each interval U_r and W_r are continuous and nonzero,
so their quotient has constant strict sign. Its parity samples are
consecutive indices with step two; a block may contain none. A numerator
root at a grid point with W_r nonzero contributes zero. If U_r is
identically zero, every noncollision parity sample is zero; no finite
list of all its roots is requested. Actual denominator grid points
remain direct in that case. This zero case also makes Q_r identically
zero, since its rational function vanishes on an open set.

This reasoning does not require simple roots, distinct denominators,
strict coefficient signs, or a lower bound on separation of events.
It proves a count, not a bounded-work algorithm for locating the cuts.

### 4. Finite collisions and the point at infinity

A grid point at which any d factor vanishes is evaluated directly with
(2). For a colliding copy the polynomial continuation is exactly

    G_n(w,eta_tau)=P_n'(y_tau)-T_n(y_tau),
                         cos w=y_tau,              (12)

which is finite also for y_tau=+/-1. All other copies can likewise be
evaluated by their finite polynomial. One must not use the limit of the
alias (9): it was obtained from identities valid only on a discrete
mesh, so its off-grid derivative or removable value need not equal
(12). This remains true even if symbolic common factors cancel.

There are at most four interior denominator-event locations, hence at
most four distinct parity samples requiring this direct treatment.
Evaluate t=0 and t=pi directly as well, whenever their indices have the
row parity. This covers z=0 and the half-angle point z=infinity without
inferring a value from the leading coefficients of Q_r/B_r. Their
weights are e_0=e_n=1/2. All other e_j are one. Thus at most six
direct four-copy sample evaluations per ordinary row suffice.

An explicit check prevents a false continuous-identity interpretation.
Take xi=zeta=0 and r=m. Then epsilon=(-1)^n, eta_tau=+/-pi and,
for all noncollision parity samples, the alias of each copy is zero:
k_tau=E=0. Thus its Q_r is identically zero. Nevertheless t=pi is an
admitted parity sample because n+m is odd, and the actual finite value is

    G_n(pi,pi)=(-1)^n*2n,
    V_m(pi)=8n*(-1)^n.                               (13)

Indeed P_n'(-1)=(-1)^n*(m^2-n^2), followed by the corrected subtraction
of (-1)^n, gives the first equality. The alias zero cannot replace this
endpoint polynomial value. Formula (3) retains its half endpoint factors.

### 5. Eight ordinary cotangent channels, with at most two retained rows

Suppose first that sin eta_tau!=0 for both tau. For any nonpole w,
the elementary difference and sum cotangent identities give

    1/[cos w-cos eta]
       =-[cot((w-eta)/2)-cot((w+eta)/2)]/[2sin eta],
    sin w/[cos w-cos eta]
       =-[cot((w-eta)/2)+cot((w+eta)/2)]/2.

Therefore each of the four terms in (9) equals

    c_tau*cot((xi+sigma*t-eta_tau)/2)
          +d_tau*cot((xi+sigma*t+eta_tau)/2),
    c_tau=epsilon*E/2-k_tau/(2sin eta_tau),
    d_tau=epsilon*E/2+k_tau/(2sin eta_tau).            (14)

There are eight labelled cotangent channels, allowing duplicates. On
one of the open intervals from section 3, no denominator event occurs.
Thus no channel in (14) crosses its pole there; its reduction modulo pi
has a constant wrap. For t_j=(delta+2k)*pi/n, delta=1-r mod 2, each
channel argument is a fixed offset plus sigma*k*pi/n. Reverse the
finite consecutive k block when sigma=-1. After the fixed wrap, this
is exactly a cotangent partial sum with spacing pi/n and all its sample
arguments strictly between zero and pi. The signed sum of R_r over
the block is consequently the sum of these eight weighted partial sums.
Multiply by its constant sign from section 3 to obtain the sum of the
actual |V_r(t_j)| over that block.

The existing C02 partial-sum mathematics can enclose these sums after
its literal guards and complete weighted error charges are supplied.
This identity does not inherit N2's original signed-row total or its
coefficient budget: c_tau,d_tau in (14) are the actual new weights.

If sin eta_tau=0, the rational degree bound remains valid but (14) is
not an allowed formula. For example at cos eta=1 the copy reduces to

    (1-epsilon*A)*csc^2(w/2)+epsilon*E*cot(w/2),      (15)

so an ordinary cotangent backend alone would omit a genuine term.
Retain every such complete row directly instead. Since zeta,b_r belong
to [0,pi], sin(zeta-b_r)=0 or sin(zeta+b_r)=0 implies precisely that
b_r is zeta or pi-zeta, including the endpoint cases. This proves (5)
and the at-most-two row count. Coincident labels are merged. All
retained rows use their finite polynomial values, with the original
endpoint factors and four-copy multiplicities.

There are m+1=n+2 physical row labels. Each nonretained row has at most
eight blocks, eight partial sums per block, and six direct terms;
at most two retained rows have at most n+1 direct terms each. Hence one
may conservatively count at most 64(n+2) cotangent-block objects and
2(n+1)+6(n+2) direct four-copy evaluations, plus O(n) bounded-degree
polynomial/partition objects. A four-copy direct evaluation entails its
four original G copies; no claim about their cost is hidden in this
count. Combining all these terms in (3) proves the stated reduction.

## Evaluation obligations and limits

The polynomial degree in z is bounded, while its coefficient arithmetic
can still depend strongly on n. At algebraic physical coordinates,
coefficients lie in algebraic fields involving the node angles; their
field degrees/heights and exact comparison costs are not bounded here.
For arbitrary real input no total exact zero/sign/equality oracle is
supplied. A numerical implementation must explicitly handle U_r=0,
multiple/nearby roots, roots coincident with a grid point, denominator
events and the t=pi endpoint. Bounded root count does not bound the
precision or iterations needed to certify any of these branches.

The representation gives exact signed blocks only after their root,
sign and integer-endpoint decisions are correct. Outward root intervals,
guards, bounded ambiguous samples and failure handling need a separate
contract. The at-most-two degenerate rows are point dependent; a whole
physical phase box can move across many such labels and move all the
root/event locations. This point theorem supplies no whole-box operation
count, freezing estimate or interval upper.

Even on nonretained rows sin eta_tau may be arbitrarily small. Every
partial-sum approximation and arithmetic radius must be multiplied by
the full weights in (14), then assembled with (3)'s factors. No accepted
common-S coefficient sum, D04 error, C11 point radius or C12/C15 tail
charge transfers to these eight channels without a separate proof.
Actual finite-polynomial evaluations and their outward errors must be
included as well. Useful cancellation-aware tail bounds and validated
root isolation are unresolved implementation obligations.

Thus the proved result is the exact point-only structural reduction and
its count of mathematical objects. A fast evaluator, practical cheap
certifier, global phase cover, effective argmax onset, compact M_infty
rate and newly certified degree do not follow.

## Verification and provenance

Analytic finite algebra only. No numerical helper, symbolic/code job,
native build, full board, quadrature, fit or cover ran. The exact
coefficient, parity, weights, identically-zero case, double denominator
case, endpoint infinity, collisions and degenerate eta branches are
all addressed above. Distinct review must independently reconstruct
the identity and counts at the frozen file hashes; developer status is
not reviewer acceptance.

2026-11-06. Rules/input `7db857380ab99e19998e01e4ce9832496b222a31`.
Parent-assigned ordinary Sol xhigh twenty-minute analytical cap; serving
metadata not independently exposed. The parent supplied the hypothesis
after publishing the D04 cost failure. Fresh gate, comparisons and
alternatives are in the owned new idea/attempt. Root alone owns Git and
shared records. Earlier D04/D05 proofs and all predecessor files remain
unchanged.
