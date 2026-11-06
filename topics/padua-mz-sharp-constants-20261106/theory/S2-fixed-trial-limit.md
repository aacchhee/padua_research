# PD-T529 — quantified fixed-trial endpoint form limit

2026-11-06 ID history: `PD-T?mz-sharp-codex-S2-04` → `PD-T529`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: microscopic cardinal form convergence; fixed-J signed endpoint
sampling; explicit constrained-trial error.
Split from: supporting local-form statement for S2's endpoint model,
PD-T528. PD-T027 is now PARTIAL: limit existence is PROVED via PD-T530;
its decimal value conjunct remains OPEN.
Split into: none.

## Statement

Fix an integer J>=1, put A=pi*J, and let N>=ceil(2A) be an integer.
Write ell_(N,j) for the degree-N cardinal polynomials at cos(pi*j/N),
and set p_(N,j)=ell_(N,j)−2(−1)^j ell_(N,0) for 1<=j<=J.
Each p_(N,j) has degree at most N−1. Define the J-by-J matrices

    C_N,ij = N² integral_{−1}^1 p_(N,i) p_(N,j) dx,
    D_N,ij = N² Q_N(p_(N,i) p_(N,j)),
    C_ij = integral_0^infinity t f_i(t) f_j(t) dt,
    D_ij = delta_ij*omega_i+4(−1)^(i+j),

where f_j and omega_j are exactly those registered in S2-endpoint-model.md.
Then, in Euclidean operator norm,

    ||C_N−C|| <= e_(N,J) = 1000 J(1+A⁴)/N²,                  (1)
    ||D_N−D|| <= d_(N,J) = 20(1+8A³)/N+4J/(N²−1).           (2)

C is positive definite. If m_J=lambda_min(C), and e_(N,J)<m_J, the
largest generalized eigenvalues lambda_(N,J) of(D_N,C_N) and lambda_J
of(D,C) obey the explicit fixed-J bound

    |lambda_(N,J)−lambda_J|
        <= [d_(N,J)+(5/3)e_(N,J)]/[m_J−e_(N,J)].            (3)

The endpoint sampling map extends boundedly from the completion of
span{f_j:j>=1} in L²((0,infinity),t dt) to the weighted endpoint sample
space. Its squared norm is exactly the registered Lambda_edge, and

    1 <= Lambda_edge <= 5/3,
    liminf_{N even} lambda_max(G_(N,N−1)) >= Lambda_edge,
    liminf_{N odd}  lambda_max(G_(N,N−1)) >= Lambda_edge.     (4)

There is no full-space upper-limsup or finite-to-limit spectral assertion.

## Definitions and assumptions

Lebesgue CC with N+1 Lobatto nodes and unnormalized dx. All matrix and
function definitions above are exact real quantities. Si(x)=integral_0^x
sin(v)/v dv. For a_j=pi*j,

    f_j(t)=2(−1)^j a_j² sin(t)/[t(t²−a_j²)],
    omega_j=2[(−1)^j+a_j Si(a_j)].

Removable singularities are filled continuously. Endpoint sample weight
omega_0=1. The norm on the range is |f(0)|²+sum_(j>=1)omega_j|f(a_j)|²;
for finite linear combinations only finitely many nonzero samples occur.

## Status by part

Overall status: **PROVED** in analytic development.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Fixed-J form and Rayleigh errors(1)–(3), bounded model, lower limits(4) | PROVED | Explicit analytic proof below; independent audit separately required |

Candidate disposition: retained supporting model lemma. Fixed-J
convergence is not equated with norm convergence of the full finite-N
problem. PD-T027's sharp-limit/value conclusion remains OPEN.

## Depends on

PD-T013 exact cardinal/DCT-I formula, degree coefficient and CC weights.
PD-T526 uniform5/3 bound. Elementary cosine integrals,
Riemann-sum estimates and finite-dimensional quadratic-form comparisons.
No external published result, computer proof or model-tail estimate.

## Checks and sources

Source/rules SHA2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
No numerical calculation is used in this proof. The independently checked
uniform bound is a dependency. Model finite measurements are separately
recorded in S2-endpoint-model.md and evidence/S2-model.json; they do not
prove this all-N statement. No novelty/priority claim.

## Proof

### 1. Exact degree constraint and cardinal ratio

The coefficient of T_N in an interpolant with nodal values v_k is
(1/N)sum c_k(−1)^k v_k, with c_0=c_N=1/2 and otherwise c_k=1.
The two nonzero nodal values of p_(N,j) make this coefficient zero.
Thus its degree is at mostN−1, and the family is independent because
p_(N,j)(cos(pi*k/N))=delta_jk for 1<=k<=J.

Set sinc(z)=sin(z)/z with sinc(0)=1. The exact cardinal formula reduces to

    p_(N,j)(cos(t/N)) = f_j(t) R_(N,j)(t),

    R_(N,j)(t) = sinc²(a_j/(2N)) cos(t/(2N)) /
       [sinc((t+a_j)/(2N)) sinc((t−a_j)/(2N)) sinc(t/(2N))].  (5)

All apparent nodal singularities are removable. For 0<=t<=N and
N>=2A, the three denominator arguments have magnitude at most3/4.
Each sinc is at least9/10, and the numerator is between0 and1.
Using |1−sinc z|<=z²/6 and |1−cos z|<=z²/2, subtraction of the
numerator and denominator products in(5) gives

    0<=R_(N,j)<=2,
    |R_(N,j)−1| <= (t²+a_j²)/N².                           (6)

For explicit constants, the sum of the five product-factor deficits is
at most t²/(4N²)+a_j²/(6N²); divide by(9/10)³. This is less than
the displayed bound. For all0<=t<=N*pi the denominator sinc factors
are at least 2sqrt(2)/(3pi),2/pi,2/pi respectively: the first argument
is at most3pi/4, and the other two have magnitude at mostpi/2.
Consequently

    0<=R_(N,j)(t)<=3pi³/(8sqrt(2))<9.                      (7)

The change of variable x=cos(t/N) now gives

    C_N,ij=integral_0^(N*pi) t sinc(t/N)
                   R_(N,i)(t)R_(N,j)(t) f_i(t)f_j(t)dt.   (8)

On t<=N, (6) and |1−sinc(t/N)|<=t²/(6N²) imply

    |sinc(t/N)R_(N,i)R_(N,j)−1|
         <=4(t²+a_i²+a_j²)/N².                            (9)

### 2. Explicit continuous-mass error

The identity

    f_j(t)=2 integral_0^1[cos(a_j s)−(−1)^j]cos(ts)ds

shows |f_j(t)|<=4. For t>=2A, its rational formula gives
|f_j(t)|<=(8/3)a_j²/t³<=3a_j²/t³. Therefore

    integral_0^infinity t |f_i f_j|dt <=32A²+9/64,
    integral_0^infinity t³|f_i f_j|dt <=64A⁴+9A²/8.         (10)

Combining(8)–(10), and estimating the actual and limiting tails beyondN
with(7), yields

    |C_N,ij−C_ij|
       <=[512A⁴+(45/8)A²]/N²+(369/2)A⁴/N⁴
       <=1000(1+A⁴)/N².                                  (11)

Indeed, the two tails cost at most(9²+1)integral_N^infinity
t|f_i f_j|dt<=82*9a_i²a_j²/(4N⁴). Since N>=2A, this is at most
(369/8)A²/N². The last coarse constant in(11) exceeds the sum for
all A>=pi. A J-by-J matrix with all entries at mostb in absolute
value has operator norm at mostJb, proving(1).

### 3. Explicit fixed-node weight error

For j>=1 put b=2pi*j and

    F_j(x)=(1−cos(bx))/(2x²),
    F_j(0)=b²/4.

Then 0<=F_j<=b²/4 and |F_j'|<=b³/12. The latter follows from
F_j(x)=(b²/2)integral_0^1(1−v)cos(bxv)dv.
Let S_N be the bracket in PD-T013, so w_j=(2/N)S_N(pi*j/N).
For oddN=2q+1 its exact telescoped form is

    N S_N =1+sum_(k=1)^q N*2[1−cos(bk/N)]/(4k²−1).

The difference between its kth summand and F_j(k/N)/N is nonnegative
and at most b²/[4N(4k²−1)]. Since sum_(k>=1)1/(4k²−1)=1/2,
the total correction is at most b²/(8N). Right-rectangle error on
[0,q/N] and the omitted interval of length1/(2N) cost at most
(b³/24+b²/8)/N.

For evenN=2q, the same sum stops atq−1, its constant is
N²/(N²−1), and its additional top term is
N[1−cos(pi*j)]/(N²−1). Replacing the last by the half-endpoint
trapezoid term [1−cos(pi*j)]/N makes an error at most
2/[N(N²−1)]. The missing half lower endpoint and Lipschitz trapezoid
error cost at most(b²/8+b³/24)/N. Thus, for either parity,

    |N S_N−g_j| <=[b³/24+b²/4+2]/N,
    g_j=1+integral_0^(1/2)F_j(x)dx
       =cos(pi*j)+pi*j*Si(pi*j).

The last equality is an integration by parts with a removable lower
endpoint. Doubling gives the convenient coarse bound

    |N²w_j−omega_j|<=20(1+(2pi*j)³)/N.                    (12)

At j=0 the exact endpoint formulas give
|N²w_0−1|<=1/(N²−1). The exact nodal values of the trial basis imply

    D_N=diag(N²w_1,...,N²w_J)+4N²w_0 ss^T,
    D=diag(omega_1,...,omega_J)+4ss^T,
    s_j=(−1)^j.

Since ||ss^T||=J, equation(12) proves(2).

### 4. Bounded model and generalized eigenvalue comparison

C is positive definite: its quadratic form is the integral of a continuous
nonnegative function; if zero, the function sum u_j f_j is identically
zero, so its samples at a_k give every u_k=0. Every omega_j is positive: its exact integral expression is
omega_j=2[1+integral_0^(1/2)F_j(x)dx]>=2.

Apply the already proved5/3 uniform CC bound to every fixed linear
combination of the p_(N,j), then pass to the proved form limits(1)–(2).
This gives D<= (5/3)C for everyJ. Hence endpoint evaluation is a bounded
map on the dense finite span, extends to its completion, and has squared
norm Lambda_edge=sup_J lambda_J<=5/3. Its extension coordinates agree
with the continuous weighted-sequence evaluations by definition.

For completeness Lambda_edge>=1: the diagonal-mass addendum below proves
C_jj/(pi*a_j)->1, while the elementary Dirichlet integral gives
(omega_j+4)/(pi*a_j)->1. Their single-trial ratios therefore tend1.
No special-function matrix formula or numerical value is needed.

For any unit Euclidean vectoru, (1)–(2) and C_N>= (m_J−e_(N,J))I give

    |(u^T D_N u)/(u^T C_N u)−(u^T D u)/(u^T C u)|
      <=[d_(N,J)+(5/3)e_(N,J)]/[m_J−e_(N,J)].

Taking the supremum proves(3). The finite trial space is contained in
Pi_(N−1), so the full lambda_max is at least lambda_(N,J). Let N tend
to infinity along either parity, then take sup overJ, to obtain(4).

### Diagonal-mass addendum

The optional lower assertion Lambda_edge>=1 is routine but must not import
an unproved special-function identity. One direct route suffices. Put a=pi*j,
t=a+v on |v|<=a/2. Then

    t*f_j(t)²=4a⁴ sin²(v)/[t(t+a)² v²].

For each fixedv its ratio to a*sin²(v)/v² tends1 as a tends infinity,
and the ratio is bounded by an absolute constant on this interval. Outside
|v|<=a/2, the mass divided bya tends0: on t<=a/2 use
|f_j(t)|<=C min(1,1/t), whose t-weighted mass is O(log a); on t>=3a/2
use |f_j(t)|<=C a²/t³, whose mass is O(1). Dominated convergence on
v with the integrable sinc-square function then gives C_jj/a ->
integral_{−infinity}^infinity(sin v/v)²dv=pi. The elementary integral
can be proved by writing sin v/v=integral_0^1 cos(sv)ds, or by one
integration by parts and the Dirichlet integral. The latter equals pi/2,
proved for example by inserting e^(−epsilon v), integrating the derivative
with respect to frequency, and then Abel limiting by the Dirichlet tail
bound. Also omega_j/a ->pi from the same Dirichlet integral. Thus the
single-trial ratio tends1, establishing the lower assertion without relying
on the closed-form matrix formula or any floating calculation.

## Scope and open items

Equations(1)–(3) control each fixedJ with explicit constants; they do not
remain useful merely by allowingJ to grow arbitrarily withN. They prove
only lower spectral limits for the full CC problem. The full upper limsup
requires controlling vectors whose endpoint index support grows, the other
endpoint and mesoscopic/macroscopic escape, in the correct mass metric.
The norm value of the infinite model has no certified Galerkin-tail bound.
These are precise OPEN obligations, not consequences of pointwise entries.

## History

2026-11-06, S2 Codex mathematical developer, requested gpt-6.1-sol xhigh;
runtime metadata unexposed. Derived after publishing the exact operator
prediction and independently of final S4 upper-fit results. No Git/shared
registry operation. Independent mathematical check requested separately.


## 2026-11-06 current obligation pointers (audit A5)

The preceding open-obligation discussion describes this fixed-J theorem's
scope. The full upper-limsup obligation is subsequently proved in
S2-qualitative-limit.md and the quantitative spectral error in
S2-finite-certificate.md. The certified decimal and A3 registry interpretation
remain unresolved. Audit-01 accepts the fixed-J proof.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
