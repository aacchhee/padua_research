# Supplementary mathematical audit: explicit S2 finite brackets

Date: 2026-11-06. Codex supplementary independent checker, requested
`gpt-6-astra high`; actual runtime model/effort metadata is unexposed.
Rules/source corpus: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.
Scope: mathematical validity and literal computability of the specified
finite certificate. This is not a full novelty, historical-priority or
registry-classification audit. No new mechanism is proposed; full
Claude audit remains separate.

## Verdict, final record and dispositions

**PASS for the explicit certificate theorem.** All finite-profile error
constants, residual-kernel bounds, bracket inequalities and convergence
claims check. No unresolved BLOCKING, MAJOR or MINOR finding remains.
No finite certificate matrix or spectral enclosure was numerically
evaluated by this checker.

Final [S2-finite-certificate.md](theory/S2-finite-certificate.md) SHA-256:
`f8e895eb3a5061de9fd1e96a603f56047919ba3600634266304b0e2e2358a90f`.
The original reviewed version was
`1578d787b297756181e0070497affcb23f336334651fe43bf491440bfc3285d7`.
Read its complete argument and checked the final additions and unchanged
proof. Dependencies were already reconstructed in
[S2-limit](independent-checks-S2-limit.md),
[S2-model](independent-checks-S2-model.md) and
[S2](independent-checks-S2.md).

Two review points were resolved by the developer:

- **Computability clarification, resolved:** the strict admissibility
  test e<m initially looked as if it required deciding equality of
  arbitrary computable reals. The final equivalent clipped formula(C)
  avoids that issue without changing L_N or any certificate constant.
  Its validity is checked below. Finite-integral evaluation of the
  model matrix is also made explicit.
- **MINOR, fixed:** the newly added display initially duplicated the
  existing equation(4). Its label and reference are now(C). No bound,
  schedule or proof step changed. Moving future refinements out of
  the theorem's status table also changes no mathematical content.

## 1. Finite residual operator certificate

On the unit square, the separate-variable Lipschitz constants of the
three kernel terms are at most

    1,       (1/2) integral_0^Y y²dy=Y³/6,
    alpha integral_0^T t²dt=alpha T³/3.

The first term is still Lipschitz across s+r=1 despite the corner
in the maximum. Each point lies within1/(2Q) of its cell midpoint
in each coordinate, so the full kernel error is at most A/Q.
Row and column integrals of the absolute error are also at most A/Q;
the Schur bound therefore controls the operator norm by that value.

Using normalized cell indicators, the step operator's matrix is
b(s_l,s_m)/Q, exactly B_Q. It is zero on the orthogonal complement
of the cell-constant functions. Hence its largest spectral value
on all of L² is max(0,lambda_max(B_Q)), not the finite matrix maximum
alone. This verifies the definition of u and B<=uI.

Both alpha and u are nonnegative. Since H>=H_Y, M_T<=M and
||g||²<=M(g), the residual inequality implies

    (K−H)(g)/2 <=alpha M_T(g)+u||g||²
                <=(alpha+u)M(g).

The continuum form identity then proves the model certificate.
There is no multiplication by a potentially negative coefficient
when discarding a positive term.

## 2. Finite-profile constants, including odd N

Normalize a^T M_N a=1. The coefficient floor gives sum a_i²<=N,
sum|a_i|<=N, and |a_i|<=sqrt(N). On a full even cell the integrated
test displacement is2/N²; on a full odd cell it is at most1/N².
The coarser common2/N² bound gives the term2||v'||/N in(4).
At odd N the final even cell is half length, costing at most
|a_(N−1)| ||v||/N<=||v||/sqrt(N). The absent odd coefficient adds
nothing. This proves the displayed quadrature bound uniformly in
N>=2 and confirms the joint profile norm bound

    ||g^+||²+||g^-||²<=1.

### Continuous endpoint mass

For v(s)=cos(st), each endpoint-profile error is at most
eta(t)=2t/N+1/sqrt(N). The physical normalized coefficient sum is
bounded by1 using Cauchy–Schwarz, and the profile transform is bounded
by its L² norm, also at most1. Thus each squared-value error is at
most2eta(t), and the sum of the two is at most4eta(t).

For N>=T the endpoint intervals are disjoint because their angular
length is at most1<pi/2. Put x=T²/N²<=1. Their exact weighted masses
are at most1, and sinc(t/N)>=1−x/6. Hence their unweighted masses
are at most

    1/(1−x/6)<=1+x.

This last inequality follows from (1+x)(1−x/6)>=1 on[0,1].
Integrating the two-profile squared error gives

    integral_0^T 4t eta(t)dt
       =8T³/(3N)+2T²/sqrt(N).

Together these give exactly E_M, with no missing T power or endpoint
factor. The claim holds for the stated full range N>=max(2,T).

### Compact transition form

The rescaled finite kernel differs from k by at most4/(3N²), since
max(s+r,2−s−r)>=1 and N>=2. The same-parity quadratic form has
factor1/4 in the q_e,q_o measures. Their combined total variation
is at most2, so this contribution is at most4/(3N²), below the
recorded2/N² allowance.

For the kernel k, sup|k|<=1 and its separate Lipschitz constant is2.
The one-variable quadrature error is at most4/N+1/sqrt(N). Applying
it in both variables, with each measure/profile variation bounded
by2, costs at most four times that error per parity. Summing both
parities and multiplying by1/4 gives at most
8/N+2/sqrt(N). This verifies E_K, including the final-cell cases.

### Positive reflected form

The exact factor (N/4)sinh(y/N) was already checked in the qualitative
proof and is at least y/4. At fixed y, the test v_y has supremum1
and derivative bounded by y. Equation(4) gives an amplitude error
at most2y/N+1/sqrt(N). Each q-value and profile integral is at most2
in absolute value, so the sum of the two squared errors is at most
8(2y/N+1/sqrt(N)).

First discard the nonnegative integral beyond Y and lower the positive
weight to y/4; then subtract the squared-error bound. This order
avoids multiplying an error by the growing sinh factor. The resulting
error is

    integral_0^Y 2y(2y/N+1/sqrt(N))dy
       =4Y³/(3N)+Y²/sqrt(N),

exactly E_H. The profile term is one half of the sum of the two
H_Y forms, with the correct parity normalization.

Combining these estimates with the residual inequality gives
alpha(1+E_M)+u+E_K+E_H for the finite excess over1. This is exactly
the stated second certificate in(2); there is no extra factor2 on
u because the sum, rather than each profile norm separately, is at
most1.

## 3. Upper-bracket convergence and boundary values of delta

Write delta=Lambda_edge−1 in[0,1/2]. Fix alpha>0 with alpha>=delta.
If a sequence of unit vectors had residual at least c>0 as T,Y→infinity,
then

    H_Y(g)/2+alpha M_T(g) <=K(g)/2−c<=1/2.

This gives a uniform M_T bound because alpha is strictly positive.
After weak extraction, compactness of K gives convergence of its
quadratic forms. Weak convergence also gives pointwise convergence
of cosine and Laplace transforms. Fatou on the expanding nonnegative
integrals puts the limiting g in the actual form domain and gives
the appropriate lower bounds for M and H. The limiting positive
residual is therefore at most

    (K−H)(g)/2−alpha M(g)<=(delta−alpha)M(g)<=0,

a contradiction. This proves u_cont→0 without assuming a spectral
gap or a quantitative compactness rate.

The midpoint error gives u<=u_cont+2A/Q. Under the stated schedules,
A/Q=O(N^−1/4) for bounded alpha, and every term in E vanishes;
the largest displayed scale in E is O(N^−1/3). These estimates do
not assign a rate to u_cont. Rounding alpha to the finite grid costs
at most1/N, while ||M_T||<=T²/2 bounds the residual change by
T_N²/(2N)→0. The grid includes the needed values near1/2 for odd
as well as even N.

For delta=0, choose any fixed positive alpha<=1/2, take N→infinity,
and only then let alpha decrease to0. No invalid alpha=0 coercivity
argument is needed. For0<delta<1/2 use alpha>delta and then decrease
it. For delta=1/2, choose alpha=1/2 itself; the contradiction above
still holds because its right side is zero. Rounding may move the
grid point slightly below or above delta, but its vanishing operator
error compares it with the fixed admissible alpha, so this causes
no gap. Hence limsup U_N<=Lambda_edge in every case.

Each candidate in the finite upper minimum bounds both quantities.
The5/3 cap also bounds both, so taking minima is valid and U_N is
always at least Lambda_edge. Thus U_N→Lambda_edge.

## 4. Lower bracket and literal computability

For each admissible J the checked fixed-trial perturbation inequality
gives lambda_(N,J)>=lambda_J−r_J(N). The full finite maximum is at
least its trial maximum, and lambda_J<=Lambda_edge. The constant1
also bounds both quantities from below. Therefore the entire finite
maximum defining L_N is valid, including the empty admissible set.

For every fixed J, eventually J<=T_N, N>=ceil(2pi J), e_J(N)<m_J,
and r_J(N)→0. Taking a liminf first for this J and then the supremum
over J gives liminf L_N>=Lambda_edge. Together with L_N<=Lambda_edge,
this proves convergence of the lower bracket.

The final computability clarification is correct. Let
v=d+(5/3)e>0 and x=m_J−e. Since lambda_J<=3/2, if0<x<=2v then
lambda_J−v/x<=1. If x<=0 the original candidate is inadmissible
and contributes only the baseline1. Thus both cases agree with

    max(1,lambda_J−v/max(x,2v)),

which also agrees when x>2v. Its denominator is bounded away from
zero by the known positive2v. This continuous expression avoids
deciding equality of m_J and e. The remaining integer comparison
with2pi J terminates because that number is irrational.

The model matrices can be evaluated using only finite-interval
integrals: d(a)=2 integral_0^a sin²(v)/v dv and Si(a), with their
removable origins filled continuously. Their closed-form Gram
identities were independently reconstructed in the model check.
Finite symmetric eigenvalues are computable continuously from such
entries; positivity of C_J permits the generalized eigenproblem.
Finite minima, maxima and the displayed safeguarded division retain
computability. The statement therefore does provide a computable
sequence epsilon_N, not merely a definition requiring unknown
infinite-dimensional spectral data.

## 5. Final scope

Both the actual maximum and the exact model norm lie in[L_N,U_N]
for every N>=2. The bracket width consequently bounds their absolute
difference and tends to zero. This establishes the stated explicit
finite-to-limit error specification.

Its evaluation may be expensive, and the convergence proof provides
no elementary power/log rate for the width. No actual finite eigenvalue
enclosure, numerical error certificate or certified decimal model
value has been produced here. Those are distinct future computations
or refinements; they are not missing premises of the proved analytic
bracket theorem. The required Claude audit remains separate. No
further S2 certificate development is requested by this review.
