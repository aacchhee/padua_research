# PD-T534 — a uniform full signed logarithmic reduction

2026-11-06 ID history: `PD-T?mz-sharp-codex-S3-02` → `PD-T534`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: thin-strip logarithmic form; finite-family signed reduction.
Split from: supporting development for PD-T381, now PARTIAL; its decimal
values conjunct remains OPEN.
Split into: none.

## Statement

For m>=4 put M=m+1 and R=floor(m/2). Let theta_j=j*pi/m,
phi_k=k*pi/M, epsilon_j=1/2 at j=0,m and 1 otherwise, and eta_k=1/2
at k=0,M and 1 otherwise. Retain exactly the pairs j+k even. Define
on real polynomials p in Pi_(m-1) (total degree)

    L_m[p] = -2/(m M R^2) sum_(j+k even) epsilon_j eta_k
             [cos(2R theta_j)+cos(2R phi_k)]
             p(cos theta_j,cos phi_k)^2.

Let Q_m be the signed Lebesgue Padua rule, with unnormalized dxdy mass
4, and ||p||^2=integral_[-1,1]^2 p^2 dxdy. Then

    |Q_m[p^2] - log(R) L_m[p]| <= 4096 ||p||^2,             (1)
    |L_m[p]| <= 120 ||p||^2.                              (2)

Both estimates hold on every m>=4, without a parity restriction. If
nu_minus(m),nu_plus(m) are the extremal Rayleigh quotients of L_m and
lambda_minus(m),lambda_plus(m) those of Q_m, both on Pi_(m-1), then

    |lambda_sign(m) - log(R) nu_sign(m)| <= 4096,
    |lambda_sign(m)/log(m) - nu_sign(m)| <= 4300/log(m).    (3)

Here sign is either minus or plus separately. This is a reduction to an
explicit finite family, not convergence to a fixed limiting operator.

## Definitions and assumptions

Pi_n denotes total-degree-at-most-n bivariate real polynomials. All
sums and norms above are finite, except the continuous Lebesgue norm.
The signed weights are precisely PD-T111's formula, using t_0=2 and
t_a=-4/(4a^2-1) for a>=1:

    S_R(t,s)=sum_(a,b>=0,a+b<=R) t_a t_b cos(2at) cos(2bs),
    w_jk=2 epsilon_j eta_k/(m M)
          [S_R(theta_j,phi_k)-2h_m cos(m theta_j)],
    h_m=2/(1-m^2) for even m, and h_m=0 for odd m.

Endpoint factors are part of every retained-pair sum.

## Status by part

Overall status: **PROVED** (analytic development accepted in [audit-01](../audit-01.md)).

| Mathematical part | Status | Evidence |
|---|---|---|
| uniform triangular-tail expansion | PROVED | elementary strip estimate below |
| complete signed form error (1), all polynomial vectors and both parities | PROVED | nodal error, positive CC floors and tensor upper bound |
| finite-family norm/spectral transfer (2)-(3) | PROVED | variational inequalities below |

Candidate disposition: retained supplied corner-form direction, with a
uniform full-grid error; not merely a fixed-index weight asymptotic.

## Depends on

PD-T111's exact signed weights; PD-T017, proof section 1, positive CC
weight floor; PD-T014's strict upper bound below 2 on Pi_(N-1).
The source files were read in full from blob-verified pinned copies.
No external theorem or measured spectral fit is a proof premise.

## Proof

### 1. A triangular-tail estimate uniform on the square

For t,s in [0,pi], put tau=min(t,pi-t), sigma=min(s,pi-s) and

    V_R(t,s)=sum_(1<=a,b<=R,a+b>R) t_a t_b cos(2at)cos(2bs).

Cosines are unchanged when t,s are replaced by tau,sigma. For R>=2,
we prove

    |R^2 V_R(t,s)-log(R)[cos(2Rt)+cos(2Rs)]|
        <=64+4R(tau+sigma).                               (4)

Partition its indices into the first strip 1<=a<=floor(R/2), the
second strip 1<=b<=floor(R/2), and the middle with a,b>=L+1. These
three parts are disjoint and exhaustive because a+b>R. In the first
strip b runs from R-a+1 to R, giving exactly a terms. There b>R/2,
so b^2-1/4>=3R^2/16, and

    |R^2 t_b+1|=(R^2-b^2+1/4)/(b^2-1/4)<=12a/R.

For clarity, R^2-b^2<=2Ra and the preceding denominator give
32a/(3R)+4/(3R^2)<=12a/R. The cosine Lipschitz bound gives

    |R^2 t_b cos(2b sigma)cos(2a tau)+cos(2R sigma)|
         <=12a/R+2a(sigma+tau).

Using |t_a|<=4/(3a^2) and L=floor(R/2)<=R/2, the difference between
this strip's R^2-weighted sum and

    -cos(2R sigma) sum_(a=1)^L a t_a

has absolute value at most

    sum_(a=1)^L a|t_a|[12a/R+2a(tau+sigma)]
        <=8+(4/3)R(tau+sigma).                            (5)

Furthermore a t_a=-1/a-1/[a(4a^2-1)], and the positive correction
sum is <=(1/3)sum a^(-3)<=1/2 by the integral test. Since
R/4<=L<=R/2 and 0<=H_L-log L<=1, it follows that

    |-sum_(a=1)^L a t_a-log R|<4.

Thus the first strip differs from log R cos(2Rs) by at most
12+(4/3)R(tau+sigma). Interchanging a,b gives the other strip's
bound relative to log R cos(2Rt). In the middle each |t_a| is at
most 16/(3R^2), and there are at most R^2 pairs. The middle's
R^2-weighted absolute sum is therefore at most 256/9<29. The total
is at most 53+(8/3)R(tau+sigma), which proves (4).

### 2. Uniform nodal remainder for the complete signed weights

The absolutely convergent cosine series gives

    f(t)=sum_(a>=0) t_a cos(2at)=pi sin t,
    T_R(t)=sum_(a>R) t_a cos(2at),   |T_R(t)|<=1/R.

The bound telescopes: sum_(a>R)|t_a|=2/(2R+1)<=1/R. Multiplying
the two full series and separating the square and triangular tail
gives the exact identity

    S_R=f(t)f(s)-f(t)T_R(s)-f(s)T_R(t)+T_R(t)T_R(s)-V_R.

Combining this with (4), |f(t)|<=pi tau and |f(s)|<=pi sigma yields

    |R^2 S_R(t,s)+log R[cos(2Rt)+cos(2Rs)]|
       <=pi^2 R^2 tau sigma+(pi+4)R(tau+sigma)+65.          (6)

At the nodes put d_j=min(j,m-j) and e_k=min(k,M-k). Then
R tau<=pi d_j/2 and R sigma<=pi e_k/2, so the right side of (6)
is at most

    (pi^4/4)d_j e_k+[(pi+4)pi/2](d_j+e_k)+65
       <=65(1+d_j)(1+e_k).                                (7)

Both coefficient comparisons follow, for example, from pi<22/7.
The exceptional even-m term satisfies

    R^2 |2h_m|=m^2/(m^2-1)<2,

and is zero for odd m. Thus with D_jk=(1+d_j)(1+e_k), the signed
weight minus log R times the corresponding weight in L_m has
absolute value at most

    134 epsilon_j eta_k D_jk/(m M R^2).                   (8)

This estimate covers every node and retains the exceptional term.
No cancellation or positivity of the signed Padua weights was used.

### 3. Conversion to the continuous norm

Let alpha_j and beta_k be the ordinary positive one-dimensional
Lebesgue CC weights for meshes m and M. PD-T017 gives

    alpha_j>=(1+d_j)/m^2,  beta_k>=(1+e_k)/M^2.           (9)

For all m>=4, mM/R^2<=15/2: for m=2R it is 4+2/R<=5, and for
m=2R+1 it is 4+6/R+2/R^2<=15/2. Consequently (8) is bounded by
1005 alpha_j beta_k, since epsilon_j eta_k<=1.

For each fixed coordinate p has degree at most m-1. Applying
PD-T014 first on mesh m, then on mesh M, and integrating the first
inequality (all intermediate CC weights are positive), gives

    sum_(all j,k) alpha_j beta_k p(cos theta_j,cos phi_k)^2
       <=4 ||p||^2.                                     (10)

Strict inequality holds for nonzero p, but is unnecessary here.
Restriction to the retained nodes and (8)-(10) bound the full signed
form error by 4020||p||^2<=4096||p||^2, proving (1).

The absolute cosine sum in L_m is at most 2. Using (9) also with
1+d_j>=1 and 1+e_k>=1, we obtain

    |L_m[p]| <=4/(m M R^2) sum_(all j,k) p(node)^2
             <=4mM/R^2 sum_(all j,k) alpha_j beta_k p(node)^2
             <=16mM/R^2 ||p||^2<=120||p||^2.

This proves (2) with the same polynomial domain on both parities.

### 4. Extremal transfer

Take the infimum, and separately the supremum, of (1) over the
continuous unit sphere. Since log R>0, this gives the first line
of (3). By (2), |nu_sign(m)|<=120. Since m/R<=5/2,

    |lambda_sign(m)/log m-nu_sign(m)|
       <=[4096+120 log(m/R)]/log m
       <=[4096+120 log(5/2)]/log m<4300/log m.

This proves the second line of (3).

## Checks

This is an analytic result; no finite spectrum or fitted slope enters
the proof. Supplementary independent check:
../independent-checks-S3-model.md, covering original frozen SHA256
3e1a9a0c8fc7c6878ebe2607d2a3ad491a5147ab1e2de51f2ce30e363ccc60d1.
It reported no unresolved mathematical finding and executed707264 exact
coefficient cases R=2,...,256. Required Claude audit remains separate.
This later edit only removes an open-target row from the proved-result
table and records that check; the proof is unchanged. The error constant
is deliberately coarse and does not certify a practical scan window.

## Sources

Pinned source 2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861; predecessor
gate ../novelty-gate-S3.md. PD-T017 is
tracks/mz-constants/theory/m2-cardinal-lower.md; PD-T014 is
tracks/mz-constants/theory/m1-upper-bound.md. No external source used.

## Scope and open items

This proves full signed-form O(log m) order and a uniform o(1)
normalized reduction to the explicit family L_m. It supplies neither
convergence of nu_sign(m), a fixed limiting operator, matching sharp
upper/lower constants, nor parity agreement. Establishing compactness
and the limiting extremal spectrum of L_m remains necessary. PD-T381
stays OPEN. The constant 4300 is an asymptotic transfer bound only.

## History

2026-11-06; Codex S3, allocated gpt-6.1-sol xhigh; runtime metadata
unexposed. Round 2 development after complete prospective gate and K0
clearance. Full source/rules SHA above. No final S4 fits read.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
