# PD-T535 — quantitative Legendre corner kernels

2026-11-06 ID history: `PD-T?mz-sharp-codex-S3-kernel` → `PD-T535`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: total-degree Bessel corner kernel; reflected-corner decoupling.
Split from: supporting development for PD-T381; no change to its original target.
Split into: none. Same-corner and reflected cases are parts of one uniform
kernel statement.

## Statement

Let P_k be the Legendre polynomial with P_k(1)=1, and let K_(m-1)
be the reproducing kernel of the real total-degree space Pi_(m-1) in
L2([-1,1]^2,dxdy), with unnormalized measure of mass four:

    K_(m-1)((x,y),(x',y'))
      = sum_(k,l>=0,k+l<=m-1) (k+1/2)(l+1/2)
           P_k(x)P_k(x')P_l(y)P_l(y').                   (1)

Write J0(z)=sum_(r>=0) (-1)^r(z/2)^(2r)/(r!)^2 and

    kappa((u,v),(u',v'))
      = integral_(a,b>=0,a+b<=1)
          ab J0(au)J0(au')J0(bv)J0(bv') da db.           (2)

For every integer m>=1, every u,v,u',v'>=0, every four shifts
eta_u,eta_v,eta_u',eta_v' in [0,1], and signs sigma,tau,sigma',tau'
in {-1,1}, put

    z_m  = (sigma cos(u/(m+eta_u)),
            tau cos(v/(m+eta_v))),
    z'_m = (sigma' cos(u'/(m+eta_u')),
            tau' cos(v'/(m+eta_v'))),
    S = u+v+u'+v',
    A = (u^2+v^2+u'^2+v'^2)/4
          + eta_u u+eta_v v+eta_u' u'+eta_v' v',
    C = 3+S+A/4.

Then

    |m^(-4)K_(m-1)(z_m,z'_m)
       - 1_((sigma,tau)=(sigma',tau'))
             kappa((u,v),(u',v'))| <= C/m.               (3)

In particular the convergence is uniform on every coordinate cube
[0,U]^4, with C_U=3+5U+U^2/4 for arbitrary shifts in [0,1]. For the
actual Padua meshes eta_u=eta_u'=0, eta_v=eta_v'=1, one may use
C_U=3+(9/2)U+U^2/4. Equal corners have limit (2); different corners
have limit zero, including corners differing in both coordinates.
The normalization is kappa((0,0),(0,0))=1/24.

## Assumptions and definitions

All statements are in exact real or complex arithmetic. The complex
integrals below represent real polynomials/functions. Angular coordinates
are fixed or belong to a stated bounded set before m tends to infinity.
The signs identify endpoints; no checkerboard or signed Padua-weight
assumption enters this reproducing-kernel result. Both parities of m
are included in the same estimates.

## Status by part

Overall status: **PROVED** (analytic development; audit-01 accepted at stated scope).

| Mathematical part | Status | Evidence |
|---|---|---|
| uniform one-coordinate Legendre/Bessel error, including degree zero | PROVED | elementary integral and power comparison below |
| same-corner triangular kernel limit with explicit error | PROVED | weighted product comparison and cell estimate |
| all reflected-corner limits and m+1 mesh shifts | PROVED | alternating row/column sums and angular Lipschitz bound |

Candidate disposition: bounded supporting proof for the already registered
S3 corner-model route. No separate mechanism or priority claim is made.

## Depends on

Only the elementary Legendre normalization and generating polynomial
identity, derived below, and elementary integrals and finite sums. No
Mehler--Heine theorem, Bessel asymptotic, spectral limit, numerical fit,
or signed-weight limit is used as a premise. The S3 full-form reduction
is the intended application, not a dependency of this kernel theorem.

## Proof

### 1. Elementary integral identities and normalization

Rodrigues' definition is

    P_k(x) = (2^k k!)^(-1) (d/dx)^k (x^2-1)^k.

It gives P_k(-x)=(-1)^k P_k(x). Integration by parts k times proves
orthogonality to degrees below k, since the first k-1 derivatives of
(x^2-1)^k vanish at each endpoint. Its leading coefficient is
c_k=(2k)!/[2^k(k!)^2]. Thus

    integral_-1^1 P_k(x)^2 dx
      = c_k integral_-1^1 x^k P_k(x) dx
      = c_k 2^(-k) integral_-1^1 (1-x^2)^k dx
      = 2/(2k+1).

The last integral equals 2^(2k+1)(k!)^2/(2k+1)!, by integration by
parts or its elementary recurrence. Consequently sqrt(k+1/2)P_k is
orthonormal for dx, proving (1) by tensor products and total degree.

The generating identity

    sum_(k>=0) P_k(x) z^k = (1-2xz+z^2)^(-1/2)          (4)

is algebraic: its coefficient of z^k is

    2^(-k) sum_(r=0)^floor(k/2)
      (-1)^r (2k-2r)! x^(k-2r)/[r!(k-r)!(k-2r)!],

the same coefficient formula obtained from Rodrigues' definition.
The elementary even moments are

    (1/pi) integral_0^pi cos(phi)^(2r) dphi
      = (2r)!/[2^(2r)(r!)^2],                           (5)

and odd moments vanish. These identities follow from the integration
by parts recurrence for powers of sine or cosine.

For x in [-1,1], set q=sqrt(1-x^2). Averaging the geometric series of
(x+iq cos(phi)) gives, initially for |z| sufficiently small,

    sum_(k>=0) z^k (1/pi) integral_0^pi
                             (x+iq cos(phi))^k dphi
      = (1-zx)^(-1)
          sum_(r>=0) binom(2r,r)/4^r
                       [izq/(1-zx)]^(2r)
      = [(1-zx)^2+z^2 q^2]^(-1/2)
      = (1-2xz+z^2)^(-1/2).

Coefficient comparison with (4) proves the integral identity, also
at q=0. Replacing q by sin(t), whose possible sign is immaterial
under phi -> pi-phi, gives for every real t

    P_k(cos t) = (1/pi) integral_0^pi
                      (cos t+i sin t cos(phi))^k dphi.   (6)

Similarly, the exponential series and (5), with absolute uniform
convergence on a bounded real z interval, give

    J0(z) = (1/pi) integral_0^pi exp(iz cos(phi)) dphi.   (7)

It follows directly that |P_k(x)|<=1 on [-1,1], |J0(z)|<=1 on the
real axis, and |J0'(z)|<=1 there. Thus no external asymptotic theorem
has been introduced through these representations.

### 2. Uniform approximation for every k<=m

Fix c in [-1,1] and let X take values 1,-1 with probabilities
(1+c)/2,(1-c)/2. This is just a notation for a two-term weighted
sum, with E X=c and E(X-c)^2=1-c^2. The elementary Taylor bound
|exp(iy)-1-iy|<=y^2/2 for real y implies

    |cos t+i c sin t-exp(itc)|
      = |E exp(itX)-exp(itc)|
      <= (t^2/2)(1-c^2).                                (8)

The first complex number has modulus at most one and the exponential
has modulus one. Factoring the difference of kth powers, then using
(6)-(7) and averaging 1-cos(phi)^2, yields

    |P_k(cos t)-J0(kt)| <= k t^2/4                      (9)

for every integer k>=0 and real t. At k=0 both sides are exactly
zero. In particular, no division by k and no exclusion of k=o(m)
is used.

For u>=0, eta in [0,1] and 0<=k<=m, (9) and |J0'|<=1 give

    |P_k(cos(u/(m+eta)))-J0(ku/m)|
      <= k u^2/[4(m+eta)^2]
           + ku eta/[m(m+eta)]
      <= (u^2/4+eta u)/m.                              (10)

This proves the stated uniform handling of m+1 and all endpoint
degrees, including u=0 and k=0.

### 3. Reduction of the kernel to a triangular sum

For a=k/m,b=l/m, define on [0,1]^2

    F(a,b)=ab J0(au)J0(au')J0(bv)J0(bv').

Let epsilon=0 if sigma=sigma' and 1 otherwise, and delta=0 if
tau=tau' and 1 otherwise. Parity of P_k puts the exact factor
(-1)^(epsilon k+delta l) in (1). Each of the four Legendre and
Bessel factors has absolute value at most one, so (10) and a
four-factor telescoping product bound give error at most A/m in
each product.

On k+l<=m-1 the normalized weight

    w_kl = (k+1/2)(l+1/2)/m^2

satisfies 0<=w_kl<=1/4, since its two factors have sum at most one.
The number of terms is m(m+1)/2<=m^2. Also

    |w_kl-ab|=(a+b)/(2m)+1/(4m^2)<=1/(2m).

Therefore, retaining the alternating factor without changing any
estimate,

    |m^(-4)K_(m-1)(z_m,z'_m)
       - m^(-2) sum_(k+l<=m-1)
                 (-1)^(epsilon k+delta l)F(k/m,l/m)|
      <= (A/4+1/2)/m.                                 (11)

This controls all low-frequency rows too; their weights were not
silently replaced by k or l without a bound.

### 4. Same-corner integral and the triangular boundary

On [0,1]^2, (7) implies

    |F|<=1,
    |partial_a F|<=1+u+u',
    |partial_b F|<=1+v+v'.

Let U_m be the union of cells
[k/m,(k+1)/m] x [l/m,(l+1)/m] with k+l<=m-1. Up to sets of area
zero, U_m contains D={a,b>=0:a+b<=1}, has area (m+1)/(2m)<=1,
and U_m\D has area 1/(2m). The excess consists of the outer half
of each of the m cells with k+l=m-1. The derivative bounds give

    |m^(-2) sum_(k+l<=m-1) F(k/m,l/m)
          - integral_(U_m) F| <= (2+S)/m.

Integrating over U_m\D contributes at most 1/(2m). Hence

    |m^(-2) sum_(k+l<=m-1) F(k/m,l/m) - integral_D F|
      <= (5/2+S)/m.                                   (12)

Combining (11)-(12) proves (3) when epsilon=delta=0.

### 5. Different-corner cancellation

Suppose epsilon=1. For each l, pair successive terms of

    sum_(k=0)^(m-1-l) (-1)^k F(k/m,l/m).

Each complete pair has absolute value at most
(1+u+u')/m by the derivative bound. There are at most m pairs,
and an unpaired terminal term has absolute value at most one.
Thus every row has absolute value at most 2+u+u'. Multiplication
by the additional row sign (-1)^(delta l) does not affect this
bound. Summing the m rows and dividing by m^2 gives

    |m^(-2) sum_(k+l<=m-1)
             (-1)^(k+delta l)F(k/m,l/m)|
      <= (2+u+u')/m.                                  (13)

If epsilon=0 and delta=1, use columns instead and obtain
(2+v+v')/m. The same row bound already covers epsilon=delta=1;
there is no unsupported inference that alternating in both coordinates
must increase the cancellation. Combining either bound with (11)
is at most (3+S+A/4)/m. This proves (3) for every distinct corner.

Finally integral_D ab da db=(1/2)integral_0^1 a(1-a)^2 da=1/24,
which verifies the normalization at the corner origin. Substituting
the coordinate and shift bounds into C gives the stated C_U values.

## Checks and sources

This is an analytic proof; no computation is a mathematical premise.
Read the pinned rules, handoff01, S3 novelty gate and its relevant
local-source shortlist before developing this supporting estimate:
PD-T295, PD-T377, PD-T381, and S3-full-form-log-model.md. The broader
predecessor screening is recorded in ../novelty-gate-S3.md. It is not
recast as a new novelty claim. No external fulltext was used.

Independent mathematical check: [audit-01](../audit-01.md) accepted this
record at its stated scope, separately from supplementary Codex checks.

## Scope and open items

The theorem supplies explicit finite-coordinate Gram-kernel errors and
decoupling of different endpoints. It does not by itself prove compactness
of an infinite corner form, identify its extreme spectrum, or establish
sharp Padua spectral limits. The finite-corner tail and operator passage
belong to the disjoint S3 operator integration. The constants here grow
with U; no uniform claim over all unbounded node indices is made.

## History

2026-11-06; Codex supporting mathematical developer; gpt-6-astra ultra
requested for the decisive limit/error step, with coordinator justification
in LOG. Runtime model/effort metadata are not independently exposed.
Rules/input: 2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861. No Git changes,
shared-record edits, model norm data, or final S4 fits used. The proposed
exact-coefficient route was replaced by its elementary integral
representation to obtain the explicit uniform error (9) without an
external asymptotic theorem; neither route is a new candidate mechanism.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
