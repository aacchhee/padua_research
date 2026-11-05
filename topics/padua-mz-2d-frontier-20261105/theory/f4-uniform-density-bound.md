# PD-T297 — uniform signed Padua coefficient norm

Development alias: `PD-T?mz2d-frontier-codex-f4-01`. Final ID assigned during audited preparation; [mapping](../preparation/final-id-map.json).

ID kind: PD-T. Aliases: weighted-L1 density-tail bound; signed Padua
hyperinterpolation stability. Split from: PD-T114, whose unchanged target
is the endpoint all-m uniform norm. Split into: none. Global IDs and
crosswalk changes are orchestrator-owned.

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`; base
`440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Codex mathematical worker,
requested gpt-6.1-sol xhigh; resolved runtime metadata not independently
exposed. 2026-11-05. No numerical or computer-proof dependency.

## Statement

For every integer m>=2 and 0<=n<=m-1, use exactly the even-checkerboard
Padua nodes, signed interpolatory Lebesgue weights, and direct quadrature
coefficient operator H_(m,n) defined in PD-T113, with the frozen node/measure conventions and the norm identity of PD-T112. Then

\[
 2\le \|H_{m,n}\|_{C([-1,1]^2)\to L^2(dx\,dy)}\le C_*<30,
\qquad
 C_*={4\sqrt2\,\pi\over\pi-4/3}
       +{68\over3}\left({1\over2}+{1\over\pi}\right).
 \tag{1}
\]

In particular (1) proves the uniform boundedness requested by PD-T114
for n=m-1. The constant is deliberately coarse; no sharpness is claimed.

## Definitions and assumptions

Let theta_j=j*pi/m and phi_k=k*pi/(m+1). The nodes are
z_jk=(cos(theta_j),cos(phi_k)), j+k even. Put epsilon_j=1/2 at
j=0,m and 1 otherwise; eta_k has the analogous convention at 0,m+1.
The positive Chebyshev checkerboard weights are

\[
 \rho_{jk}={2\epsilon_j\eta_k\over m(m+1)}.
\]

They have total mass one and differ from the signed dxdy weights w_jk.
Write `nu(dx)=dx/(pi sqrt(1-x^2))`, a probability measure. All L2 norms
without another measure mean unnormalized dxdy (or dx in one dimension).
All polynomials and operators are real. No assumption about the signs
of the noncorner weights, signed Gram positivity, or signed spectral
upper bounds is made.

## Status by part

Overall status: **PROVED in development**, complete analytic argument
below; independent mathematical check and Claude audit-01 accepted.
The density, tail and comparison calculations below are routine proof
steps of (1); they are not separate asymptotic targets.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Uniform norm bound (1), every m>=2 and 0<=n<m | PROVED in development | Analytic proof below; Claude audit-01 accepted |

Candidate disposition: retained, IDEA-395.
No negative candidate or global novelty claim is asserted.

## Depends on

- PD-T101, its locally proved cardinal normalization, to identify w/rho.
- PD-T111, its exact finite triangular moment sum; repeated here with
  all substitutions needed for the tail estimate.
- PD-T112, the exact weighted-L1 formula for this operator norm.
- PD-T113, the direct signed coefficient-operator definition.
- PD-T013, positivity of the CC weights (also PD-T017 equation (2)).
- PD-T017 section 1, the elementary CC sine weight floor; the slightly
  sharper constant used here follows from its displayed error estimate.
- PD-T022, the one-dimensional CC upper bound <2 on degree<N.

These are local analytic results. No theorem from an unread external
source, no F1/F2 conclusion, and no finite computation is used.

## Proof

### 1. Identify the signed density exactly

Let c_0=1, c_a=2 for a>0, and h_a=integral T_a dx. Integrating the
PD-T101 cardinal formula gives, at every retained node z=(x,y),

\[
 w_z=\rho_z d_m(z),\quad
 d_m(x,y)=\sum_{a+b\le m}c_ah_ac_bh_b T_a(x)T_b(y)
                   -2h_mT_m(x).                         \tag{2}
\]

In particular the exceptional highest-x mode and its factor 2 are retained.
The absolutely convergent cosine series from PD-T017 gives

\[
 g(x)=\pi\sqrt{1-x^2}=\sum_{r\ge0}t_rT_{2r}(x),
 \quad t_0=2,\quad t_r=-{4\over4r^2-1}\ (r\ge1),
 \quad \sum_{r\ge0}|t_r|=4.                              \tag{3}
\]

Indeed multiplying its `(pi/2)sin(theta)` series by two gives (3),
including both endpoints by continuity of both sides and uniform convergence of the absolutely summable series (the Weierstrass M-test). Since c_(2r)h_(2r)=t_r
and the odd moments vanish, the sum in (2) is precisely the triangular
partial sum with r+s<=R=floor(m/2) of g(x)g(y).

Put `M=2R+1` and `\sigma_R=sum_(i=1)^R 1/(2i-1)`. PD-T111's finite identity is

\[
 A_R:=\sum_{r+s\le R}t_rt_s
 ={8\over M(M+1)}-{16\sigma_R\over M^2-1}.                    \tag{4}
\]

For R>=1, `\sigma_R<=1+(R-1)/3=(R+2)/3<=R(R+2)/(2R+1)`.
Inserting this last bound into (4) gives

\[
 A_R\ge-{4\over M}.                                    \tag{5}
\]

For clarity, `16/(M^2-1)=4/[R(R+1)]`, so (5) is exactly equivalent
to `\sigma_R<=R(R+2)/M`. The telescoping absolute tail of (3) is
`sum_(r>R)|t_r|=2/M`. In the finite triangle, changing signs from t_rt_s
to |t_rt_s| changes only its two nonzero coordinate axes; their total
change is `8 sum_(r=1)^R |t_r|=16-16/M`. Therefore

\[
 \sum_{r+s>R}|t_rt_s|={16\over M}-A_R
       \le {20\over M}\le {20\over m}.                  \tag{6}
\]

The last inequality uses M=m or m+1. The exceptional correction is zero
for odd m; for even m>=2,

\[
 2|h_m|={4\over m^2-1}\le {8\over3m},
\]

because `(2m+1)(m-2)>=0`. Equations (2),(3),(6) and |T_a|<=1 yield

\[
 \|d_m-g\otimes g\|_\infty\le {68\over3m}.             \tag{7}
\]

### 2. A coarse raw-Chebyshev sampling estimate

For every one-dimensional q of degree<=m-1,

\[
 \int q^2\,d\nu\le \kappa m\int q^2\,dx,
 \qquad \kappa={1\over2}+{1\over\pi}.                   \tag{8}
\]

Here is an elementary endpoint proof. The orthonormal Legendre expansion
and Cauchy-Schwarz give `||q||infinity^2<=m^2||q||2^2/2`, since
`|P_l(x)|<=1` and `sum_(l=0)^(m-1)(2l+1)/2=m^2/2`.
One direct verification of `|P_l|<=1` is the classical finite-integral
identity

\[
 P_l(x)={1\over\pi}\int_0^\pi
       (x+i\sqrt{1-x^2}\cos u)^l\,du,
\]

whose integrand has modulus<=1; expanding its generating series gives
`(1-2xt+t^2)^(-1/2)`, identifying the polynomial with P_l.
Now write the left side of (8) as `pi^(-1) integral_0^pi q(cos t)^2 dt`.
On `[1/m,pi-1/m]`, `sin t>=2/(pi*m)`, so that portion is at most
`(m/2)||q||2^2`. The two omitted intervals have total length 2/m;
their contribution is at most `m||q||2^2/pi`. This proves (8).

Apply (8) in each coordinate, using Fubini, to p in Pi_(m-1):

\[
 \int p^2\,d(\nu\otimes\nu)\le \kappa^2m^2\|p\|_2^2.
\]

PD-T101's discrete cosine orthogonality, restricted below its exceptional
mode (m,0), gives exactly
`sum_z rho_z p(z)^2=integral p^2 d(nu tensor nu)` for this space.
Equivalently, the full tensor cosine sums are exact in each coordinate
below 2m and 2(m+1), while a nonzero checkerboard-alternating product
would require x-frequency congruent to m modulo 2m and y-frequency
congruent to m+1 modulo 2m+2, hence total degree at least 2m+1,
impossible for p^2 of total degree<=2m-2. Since sum rho=1, Cauchy-Schwarz now gives

\[
 \sum_z\rho_z|p(z)|\le \kappa m\|p\|_2.                  \tag{9}
\]

### 3. The positive main density has a uniform forward L1 bound

Put v_z=rho_z g(x_z)g(y_z)>=0 and `\alpha_0=pi-4/3>0`. For an interior
N-axis CC node, write `\chi_{N,j}=j*pi/N`. PD-T017's weight formula `W_N,j=(2/N)B_N(\chi_{N,j})`
and error bound `|B_N-(pi/2)sin(\chi_{N,j})|<=(2/3)sin(\chi_{N,j})` give

\[
 W_{N,j}\ge \alpha_0\,{sin(\chi_{N,j})\over N}.                  \tag{10}
\]

This applies to every N>=2; at endpoints the right side is zero.
At retained interior nodes, (10) in the two axes gives

\[
 v_{jk}\le {2\pi^2\over \alpha_0^2}W_{m,j}W_{m+1,k};
\]

the same inequality holds at boundary nodes because v=0 there.
Both CC rules are positive. Enlarge the sum to the full rectangle and
apply PD-T022 in each coordinate (each coordinate degree is at most m-1):

\[
 \sum_zv_z p(z)^2\le {8\pi^2\over \alpha_0^2}\|p\|_2^2.      \tag{11}
\]

The total v mass is <=4. To check the normalization exactly, expand
`2*1_(j+k even)=1+(-1)^(j+k)` in its sine-product sum. For the odd one
of m,m+1, reflection j->N-j cancels the alternating sine sum. The
unalternated sine sum is `sum_(j=1)^(N-1) sin(j*pi/N)=cot(pi/(2N))`.
Consequently

\[
 \sum_zv_z={\pi^2\over m(m+1)}
       \cot{\pi\over2m}\cot{\pi\over2(m+1)}\le4,         \tag{12}
\]

using cot(t)<=1/t for 0<t<pi/2 (from tan(t)>=t). Thus (11),(12)
and Cauchy-Schwarz imply

\[
 \sum_zv_z|p(z)|\le {4\sqrt2\,\pi\over \alpha_0}\|p\|_2.     \tag{13}
\]

### 4. Assemble in the exact weighted L1 formula

Since rho>=0 and g tensor g>=0, (2),(7) imply
`|w_z|<=v_z+[68/(3m)]rho_z`. Combine (9),(13):

\[
 \sum_z|w_z|\,|p(z)|\le
 \left[{4\sqrt2\,\pi\over \alpha_0}+{68\kappa\over3}\right]\|p\|_2.
\]

PD-T112's exact norm identity proves the upper bound in (1), also for
every subspace Pi_n with n<m. For a fully rational coarse check of the
constant, pi>3 implies `pi/(pi-4/3)<9/5` and `kappa<5/6`; also
sqrt(2)<3/2. Hence `C_*<54/5+170/9=1336/45<30`.
Finally H_(m,n) reproduces the constant one by degree-m exactness, so
its norm is at least `||1||_(L2(dxdy))=2`. This proves (1). ∎

[Claude audit-01](../audit-01.md) accepted the mathematics at its stated scope; [response-01](../response-01.md) addresses the editorial findings. Supplementary reconstruction is recorded in [independent-checks-math.md](../independent-checks-math.md).

## Checks and sources

Proof is analytic; no numerical run supplies a premise. G5 preregistration
predates runs and is retained in `../attempts/F4.md`. The novelty gate and
all retained alternatives are in `../ideas-f4.md`. Local prior-art sources
and their primary-reading limits are those of the cited dependency files;
no new external source was contacted or promoted to a proof dependency.
Supplementary independent checking and Claude audit-01 are complete; see the linked audit and supplementary check above.

## Scope and open items

This establishes uniform boundedness of the unchanged direct signed
coefficient operator, with a coarse explicit value. It does not bound
the absolute-Gram spectrum uniformly: PD-N052 remains intact. It gives
neither signed Gram positivity nor lambda_+<2, and uses neither. Endpoint
reproduction still stops at Pi_1 for m>=3 by PD-N051. Sharp operator norms,
limits and fixed-function convergence remain separate questions.

Independent reconstruction of (2), the tail sign bookkeeping,
checkerboard discrete exactness, the CC floor factor, and total mass
(12) is complete and Claude audit-01 accepted. Next: audited preparation
and orchestrator registry disposition, following response-01.

## History

2026-11-05: derived after complete recorded local novelty gate. The first
raw-density idea sought an O(log m) Chebyshev L1 bound; it was deferred
because the elementary O(m) estimate already cancels the uniform O(1/m)
density tail. G0 PASS was confirmed by the orchestrator before any F4
computation; this proof requires no computation. The original target
PD-T114 is preserved, with this proposed substantive resolution pending
independent audit and final-ID integration.

2026-11-05, documentation response to audit-01: the pending wording in the earlier dated history above records the development state at that time. Claude audit-01 subsequently accepted the mathematics; response-01 records the permitted editorial changes. No earlier execution or statement is relabeled.

2026-11-05: mechanical final-ID registration after accepted Claude audit-01 and response-01. The earlier audited source/receipt identities are historical; proof content changes only by ID substitution.
