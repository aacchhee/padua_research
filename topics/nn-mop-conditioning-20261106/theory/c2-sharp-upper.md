# PD-T509 — sharp Krawtchouk NN exponential rate

ID kind: PD-T. Aliases: full-triangle Bernstein–Hermite upper bound;
two-contour sensitivity estimate; common-node logarithmic forcing.
Split from: PD-T448, the sharp growth target, restricted here to its exact
p1=2/5,p2=1/2 Krawtchouk case in the PD-T432 metric.
Split into: none. PD-T448's remaining OPEN conjuncts in its single metric
are itemized in [classification-proposal.md](../classification-proposal.md).

## Statement

For every integer N>=2, set M=N−1, x_k=2k/M−1 for 0<=k<=M, and

    w_(s,k)=binom(M,k)p_s^k(1−p_s)^(M−k),
    p1=2/5, p2=1/2, rho=5+2sqrt(6).

Let F contain every monic NN a1,a2,b1,b2 coefficient at n+m<=M.
For the PD-T432 input norm |dot x_k|<=1 and
|dot w_(s,k)|<=w_(s,k), and its four fieldwise relative sup output norms,

    kappa_N <= 3,000,000 N^13 rho^(N−1).                    (1)

Together with PD-T437's lower bound this proves

    lim_(N→infinity) kappa_N^(1/N)=5+2sqrt(6).               (2)

The prefactor is deliberately loose. The statement includes the complete
triangle, both a fields, both b fields, independent relative weights,
common moving nodes and the support-polynomial terminal successors.

## Definitions, assumptions and status

Use the actual type-II monic moment-polynomial map and PD-T286 NN
conventions. Perturbations may leave the binomial family and need not
preserve mass. The theorem is local first-order sensitivity in exact real
arithmetic. Normality of all required indices through degree N is proved
in PD-T433; it persists in a neighborhood of the base input.

Overall status: PROVED (written analytic development; supplementary checks
and substantive Claude audit-01 accepted this theorem within its scope). Candidate disposition:
retained quantitative continuation of IDEA-533/535 and C2-01 in
../novelty-gate-C2.md; no priority or new-core-mechanism claim.

## Dependencies

- PD-T286: NN recurrence, subleading b differences and normal moment map.
- PD-T432: the induced derivative norm and its mixed input/output metric.
- PD-T433: normality at the exact input.
- PD-T437: verified exact base coefficients and the matching lower bound.

The upper estimate below does not use an asymptotic fit, a numerical
premise, or an external polynomial formula.

## Proof

### 1. Bernstein transform and its exact normalization

Work first in the integer variable k, so that the node velocities satisfy
|xi_k|=|dot k|<=M/2. Fix nu=(n,m), 1<=t=n+m<=M, and let P=P_nu be its
monic degree-t polynomial. Write L=M−t and (M)_r=M!/(M−r)!.
Define the Bernstein transform

    B_M f(u)=sum_k binom(M,k) f(k) u^k(1−u)^(M−k).

For the falling factorial (k)_r, direct binomial differentiation gives
B_M (k)_r=(M)_r u^r. Thus B_M preserves polynomial degree through M and
multiplies the leading coefficient in degree t by (M)_t.

For clarity the equivalent binomial transform is

    H(z)=sum_k binom(M,k)P(k)z^k,
    Q(u)=(1−u)^M H(u/(1−u))=B_M P(u).

Orthogonality says that H has n jets zero at a=2/3 and m jets zero at b=1:
the constraints use (z d/dz)^j, which is an invertible triangular change
of the ordinary jets at either nonzero point. Multiplication by (1−u)^M
and the nonsingular substitution z=u/(1−u) preserve these vanishing
orders, now at p1 and p2. Degree and leading coefficient therefore give

    D(u)=(u−p1)^n(u−p2)^m,
    Q(u)=(M)_t D(u),                                       (3)
    H(z)=(M)_t (1+z)^L(z−a)^n(z−b)^m
                         /[(1+a)^n(1+b)^m].               (4)

This checks the sign and constant: at degree zero H=(1+z)^M; at t=M,
H(−1)=(−1)^M M!. No terminal-only assumption enters (3)–(4).

Put v_k=binom(M,k)P(k). Coefficientwise absolute values in (4) imply,
for every complex u,

    sum_k |v_k||u|^k|1−u|^(M−k)
      <=(M)_t S(u)^L A1(u)^n A2(u)^m,                     (5)
    S=|u|+|1−u|,
    A1=(2/5)|1−u|+(3/5)|u|,  A2=S/2.

In particular sum_k |v_k|<=(M)_t 2^L, by setting z=1 in the
coefficient majorant of (4).

### 2. Exact differentiated jets, including moving nodes

Write eta_(s,k)=dot w_(s,k)/w_(s,k), with |eta_(s,k)|<=1, and let dot P
mean the derivative of the polynomial coefficients at a fixed argument.
Monicity implies deg dot P<=t−1, hence R=B_M dot P has degree <=t−1.
Define

    f_s=B_M(P eta_s),  f=B_M(P xi),  g=B_M(P' xi),
    ell(u)=log(u/(1−u)),  ell_s=log(p_s/(1−p_s)).

The functions inside B_M in this display are arrays at the grid points;
their transforms may have degree M. The differentiated constraints are
exactly the Hermite conditions

    R + f_s + g + f(ell−ell_s)
           has a zero of order nu_s at p_s.                (6)

One direct verification uses z and the analytic factor
exp(epsilon xi_k log(z/a_s)). Its jth Euler derivative at z=a_s produces
(k+epsilon xi_k)^j. Differentiation at epsilon zero yields the two node
terms P'(k)xi_k and P(k)xi_k log(z/a_s). Multiplication by (1−u)^M and
z=u/(1−u) then gives (6). Thus no derivative of a binomial mass with
respect to its location has been introduced: the original weights and
the node coordinates are independent input coordinates.

Split the source in (6) into the two polynomial sources f_s, the two
polynomial sources −ell_s f, and the one common analytic source

    G=g+ell f.                                             (7)

Only the common source will be integrated on a contour enclosing both
jet points. It cannot use the rectangles: Gamma1 encloses the logarithmic
branch point0 and Gamma2 encloses branch point1. The disk Gamma0 instead
avoids both; this common-node cancellation is essential to the estimate.

### 3. An inverse-jet formula for the top three coefficients

Write D(u)=u^t+d1 u^(t−1)+d2 u^(t−2)+..., d0=1. If an analytic source
F_s is prescribed at each jet point, its Hermite interpolant of degree
<t has coefficient of u^(t−j), for 1<=j<=t,

    sum_s (1/(2 pi i)) integral_(Gamma_s)
           F_s(zeta) h_(j−1)(zeta)/D(zeta) d zeta,
    h_(j−1)(zeta)=sum_(i=0)^(j−1) d_i zeta^(j−1−i).        (8)

Here Gamma_s encloses only its designated jet point. For a common source,
replace the sum by one contour enclosing both. To prove (8), use the
polynomial quotient

    K(u,zeta)=(D(u)−D(zeta))/(u−zeta).

The sum of integrals of F_s(zeta)K(u,zeta)/D(zeta) is a polynomial of
degree <t matching every prescribed jet, by the residue formula (or the
local principal parts of F_s/D). Its coefficient is exactly (8).
Equation (6) uses the negative of this interpolant; bounds ignore that
overall sign. In what follows j<=min(3,t).

Because all roots of D lie in [0,1/2],
|d1|<=N/2 and |d2|<=N^2/8. On every contour used below |zeta|<3.
Consequently the uniform bound

    |h_(j−1)(zeta)|<=16N^2                                (9)

holds for these three coefficient functionals, including t=1,2.

### 4. Sharp separating contours for the weight sources

Set c=sqrt(6)−2, and take the positively oriented rectangle boundaries

    Gamma1=boundary([-1,c] + i[-1,1]),
    Gamma2=boundary([c,2] + i[-1,1]).

Their combined length is 14, hence divided by 2 pi is less than 3.
They avoid both roots and enclose p1 and p2 respectively. Throughout
both contours S<5. We claim, throughout both contours,

    A1/|u−p1|<=rho,    A2/|u−p2|<=rho.                    (10)

On their shared vertical side u=c+iy, each ratio
sqrt(alpha^2+y^2)/sqrt(beta^2+y^2) decreases with |y| when alpha>beta.
Apply this separately to |u| and |1−u| in A1,A2: c and 1−c exceed
both c−p1 and p2−c. Thus each ratio in (10) is at most its value at y=0.
The two values are equal, since

    ((2/5)+(1/5)c)/(c−2/5)
        =(1/2)/(1/2−c)=5+2sqrt(6).

On every other side, both distances |u−p_s| are at least one; also
|u|,|1−u|<=sqrt(5), so A1,A2<=sqrt(5)<rho. This proves (10).

If F_s=B_M(P eta_s) and |eta_s|<=1, equations (5) and (10) give

    |F_s/D|<=(M)_t 5^L rho^t<=(M)_t rho^M.                 (11)

Therefore (8)–(9), summed over the two weight sources, bound each of the
top three coefficients by 48N^2(M)_t rho^M. The sources −ell_s f obey
the same bound multiplied by M/2, since |xi_k|<=M/2 and |ell_s|<1.
Their combined bound is 24MN^2(M)_t rho^M.

### 5. The common node source has a smaller exponential bound

At the integer nodes, weighted polynomial differentiation has the exact
matrix identity, for any polynomial P of degree <=M,

    binom(M,k)P'(k)
      =(H_k−H_(M−k))v_k
        +sum_(j!=k) (-1)^(j−k) v_j/(k−j),                 (12)

where H_r=sum_(i=1)^r 1/i and H_0=0. This follows by differentiating
the grid Lagrange basis. Each column's absolute sum is <=3H_M, because
the off-diagonal reciprocal sums are <=2H_M and the diagonal is <=H_M.
In particular

    sum_k |binom(M,k)P'(k)|<=3H_M (M)_t 2^L.               (13)

Use the circle Gamma0: |u−9/20|=2/5. It encloses both p1 and p2 and
its closed interior avoids 0 and 1. The branches log u and log(1−u)
are analytic there. On Gamma0,

    |u|<=17/20, |1−u|<=19/20,
    |u−p_s|>=7/20, |ell(u)|<=log(19)+pi<7.

The last inequality uses the positive real parts of u and 1−u and
1/19<=|u/(1−u)|<=17/3. Equations (5), (13), and |xi|<=M/2 yield

    |G/D| <= (M/2)(3H_M+7)(M)_t
                     (19/10)^L(19/7)^t
            <= (M/2)(3M+7)(M)_t 3^M.                      (14)

The length of Gamma0 divided by 2 pi is 2/5. With (9), its contribution
to each coefficient is bounded, conservatively, by

    8MN^2(3M+7)(M)_t rho^M.

Combining all three source groups gives the explicit uniform estimate

    |[u^(t−j)] R| <= 200N^4 (M)_t rho^M,
          1<=j<=min(3,t).                                 (15)

Indeed the preceding constants sum to
N^2(24M^2+80M+48)<=200N^4. This bounds every mixed direction of input
norm at most one, including simultaneous node and weight perturbations.

### 6. Transfer to the leading three ordinary coefficients

For a degree-t polynomial let c_j denote the coefficient of k^(t−j),
with c_0=1, and set c_j=0 when j>t. The exact inverse Bernstein formula is

    P(k)=sum_(r=0)^t [u^r]Q(u)/(M)_r * (k)_r.              (16)

Only the top j+1 terms enter c_j, and dot q_t=0. For l<=j<=3,

    (M)_t/(M)_(t−l)<=N^l,
    |[k^(t−j)](k)_(t−l)|<=N^(2(j−l)).

The second inequality bounds elementary symmetric functions of the
integers 0,...,t−l−1. Consequently (15) implies

    |dot c_j|<=600N^(2j+3) rho^M<=1000N^9 rho^M=:C,
                1<=j<=3, 0<=t<=M.                       (17)

For later use, (3), (16) and |d_l|<=N^l also give

    |c1|<=2N^2, |c2|<=3N^4, |c3|<=4N^6.                 (18)

Terminal successors have degree N=M+1 and equal the support polynomial
P_N(k)=product_(l=0)^M(k−l), independently of their multi-index. On moving
nodes its derivative is −sum_l xi_l product_(j!=l)(k−j). Its first three
coefficient derivatives are bounded by N^(2j)/2 for j=1,2,3. Its base
coefficients are bounded by N^(2j). These satisfy (17)–(18) too. This
separate check covers every degree-N polynomial used by a terminal field;
the Bernstein transform is not applied beyond its valid degree M.

### 7. Transfer to every NN field, including the a fields

Write tau=c1, sigma=c2, chi=c3. In the integer variable the NN recurrence
at nu, in either direction i, reads

    kP_nu=P_(nu+e_i)+B_(nu,i)P_nu
                      +A1 P_(nu−e1)+A2 P_(nu−e2).

The absent predecessor has coefficient zero. Comparing the next three
powers, with the zero conventions above, gives

    B_(nu,i)=tau_nu−tau_(nu+e_i),
    S:=A1+A2=sigma_nu−sigma_(nu+e_i)−B_(nu,i)tau_nu,
    T:=A1 tau_(nu−e1)+A2 tau_(nu−e2)
           =chi_nu−chi_(nu+e_i)−B_(nu,i)sigma_nu.           (19)

On an axis only one A is present and it equals S. At n,m>=1, put
tau1=tau_(nu−e1), tau2=tau_(nu−e2). Then

    A1=(T−S tau2)/(tau1−tau2),  A2=S−A1.                 (20)

PD-T437 proves the exact base values, with t=n+m,

    A1=(6/25)n(M−t+1), A2=(1/4)m(M−t+1),
    B_(nu,i)=p_i(M−t)+(3/5)n+(1/2)m.

In particular |A_s|<=N^2, |S|<=2N^2 and |B|<=N. The NN difference
identity at eta=nu−e1−e2 gives

    tau1−tau2=−(B_(eta,2)−B_(eta,1))
             =−(M−t+2)/10,  |tau1−tau2|>=1/5.             (21)

This holds even at t=M. It is a base denominator estimate for direct
formulas (20), not the repeated application of a layer-error recurrence.

Differentiate (19) and use (17)–(18):

    |dot B|<=2C,
    |dot S|<=(2+4N^2+N)C<=7N^2 C,
    |dot T|<=(2+6N^4+N)C<=9N^4 C.

Differentiating (20) in the form

    dot A1=(dot T−dot S tau2−S dot tau2
                         −A1(dot tau1−dot tau2))/(tau1−tau2)

therefore gives |dot A1|<=135N^4 C, and |dot A2|<=142N^4 C.
The uniform bound |dot A_s|<=150N^4 C includes the axes; at the origin
both a coefficients and their derivatives vanish identically.

Finally return to x=2k/M−1. Then a_s=4A_s/M^2 and b_i=2B_i/M−1.
The base b field norms are exactly 1/5 by PD-T437. Each a field norm is
at least 1/(5M): its first nonzero marginal coefficient is 24/(25M) or
1/M. Thus every normalized output derivative is at most

    max( (4/M^2)(150N^4 C)(5M), (2/M)(2C)(5) )
      <=3000N^4 C=3,000,000 N^13 rho^M.

Taking the supremum over all mixed input directions proves (1), using
PD-T432's induced norm characterization. PD-T437 gives

    kappa_N >= 5/(2M^2) [rho^(M−1)+rho^(−(M−1))].

The Nth roots of the explicit polynomial factors tend to one. This
lower bound and (1) prove (2).

## Checks, sources and limits

The proof is analytic. Completed supplementary exact small-degree checks
and separate reconstruction are recorded in ../attempts/C2-hard.md and
independent-checks-01.md; Claude audit-01 also reconstructed the proof and
executed independent checks. None is a premise of the all-N conclusion. No literature novelty claim or
unread external formula is used. The mechanism is the already gated
binomial/Hermite continuation, with a norm-matched all-field transfer.

The finite prefactor has not been optimized. This establishes neither a
uniform finite-perturbation radius nor a stable algorithm. It proves no
matching rate for Hahn, for arbitrary parameter pairs, or for a different
output normalization. Those original targets remain separately OPEN.

## History

2026-11-06: Codex bounded decisive hard-step developer, requested
gpt-6-astra ultra under handoff01; justification and allocation owned by
the coordinator. Rules read at local materialized snapshot
76ba4214b100c86a44941f5e9a662ce9ce48efb8; the assigned published topic input
is b4a04981d42c7cd872957facf5e3995e4096ca67. No Git or shared-file edits.
The complete C2 documentary gate was read, as were the relevant full
predecessor records and their proof dependencies. The theorem closes the
stated fixed-pair case, without silently narrowing PD-T448's other cases.

## Final ID aliases (2026-11-06)

- `PD-T?nn-mop-cond-codex-C2-hard-01` → `PD-T509`.
