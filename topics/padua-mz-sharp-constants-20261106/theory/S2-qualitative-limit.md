# PD-T?mz-sharp-codex-S2-05 — qualitative convergence to the endpoint norm

ID kind: PD-T.
Aliases: compact signed transition remainder; two-endpoint weak profiles;
CC upper spectral limit as a microscopic sampling norm.
Split from: the convergence-existence part of the S2 endpoint target.
Split into: the quantitative finite-to-limit error is proved separately in
S2-finite-certificate.md; the numerical value remains MEASURED only.

## Statement

For the Lebesgue CC rule at N+1 Lobatto nodes and degree at mostN−1,

    lim_{N→infinity} lambda_max(G_(N,N−1)) = Lambda_edge,
    1 <= Lambda_edge <=3/2,                               (1)

where Lambda_edge is exactly the variational norm(P) registered in
S2-endpoint-model.md. In particular both N parities have the same limit.
This is a qualitative convergence theorem. It supplies no explicit epsilon(N)
for the full spectral convergence and no certified numerical evaluation of
Lambda_edge. The quantitative error is supplied separately by
S2-finite-certificate.md; a certified decimal remains OPEN.

## Definitions

For g in L²(0,1), write F_g(t)=integral_0^1 g(s)cos(st)ds and

    M(g)=integral_0^infinity t |F_g(t)|²dt,
    H(g)=integral_0^infinity y |integral_0^1 g(s)e^{−(1−s)y}ds|²dy,
    K(g)=integral_0^1 integral_0^1 k(s+r)g(s)g(r) ds dr,
    k(v)=1/[max(v,2−v)]²,  0<=v<=2.

Let V={g in L²(0,1):M(g)<infinity}. The initial core is

    V_0=span{2[cos(pi*j*s)−(−1)^j]:j=1,2,...}.

Its cosine transforms are exactly the f_j of the registered endpoint model.
The discrete matrices M_N,R_N,H_N,K_N in the proof use coefficient indices
0,...,N−1 and the exact decomposition R_N=M_N−H_N+K_N from the uniform
S2 theorem. A letter used for a quadratic form also denotes its matrix
where no ambiguity arises.

## Assumptions

Exact real Lebesgue CC, N>=2. No numerical approximation or external
published spectral theorem is used. Elementary Hilbert-space weak
compactness and integral convergence facts are used explicitly below.

## Status by part

Overall status: **PROVED** in analytic development, independently accepted at its stated scope in audit-01.md.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Qualitative convergence and common-parity limit(1) | PROVED | Variational proof below; no quantitative rate |

This result does not satisfy the campaign's stronger request for an explicit
finite-to-limit spectral error. That part is proved separately in
S2-finite-certificate.md; a certified norm value remains OPEN. No PARTIAL label is inferred merely from supporting lemmas.

## Depends on

PD-T013 exact CC moment/cardinal definitions. PD-T015 mass floor.
PD-T?mz-sharp-codex-S2-01 exact reflected decomposition/uniform bound.
PD-T?mz-sharp-codex-S2-04 fixed-J form convergence and lower-limsup model.
The candidate and prospective refresh are ideas/S2-compactness.md and
novelty-gate-S2.md. No historical novelty/priority claim.

## Checks and sources

Analytic proof only. Frozen source/rules2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
Finite model measurements are not used. Supplementary independent proof
review and the required Claude audit remain separate obligations.

## Proof

### 1. Density of the registered core in the actual form domain

The core V_0 is dense in V simultaneously in L² and in the seminorm M.
Here are details to avoid imposing an unproved boundary trace condition.
Evenly extend g to G(s)=g(|s|) on |s|<1 and zero elsewhere. Its Fourier
transform is 2F_g, so M is one eighth of the squared L²(|t|dt) norm of
that full Fourier transform. For 0<r<1 put G_r(s)=G(s/r). Then its
Fourier transform is r times that ofG at rt. Dilation is an isometry
in L²(|t|dt), and is strongly continuous there: prove it first for
continuous functions supported in compact annuli, then approximate any
weighted L² function. Ordinary L² dilation is also strongly continuous.
Thus inward dilation converges toG in both required norms.

Convolve G_r with an even smooth unit-mass compactly supported mollifier
whose support is small enough to stay inside(−1,1). Its Fourier multiplier
is bounded by1 and tends pointwise to1 as the support shrinks. Dominated
convergence in L²(|t|dt), and the usual direct approximate-identity argument
in L², show convergence in both norms. The resulting even smooth function
vanishes on a neighborhood of±1.

On[0,1] such a function has a cosine series g(s)=b_0+sum_(j>=1)b_j cos(pi*j*s)
whose coefficients decrease faster than every power, by repeated integration
by parts. Since g(1)=0,

    g(s)=sum_(j>=1)b_j[cos(pi*j*s)−(−1)^j].

The partial sums converge in C²[0,1]. Their difference h fromg has
h(1)=0. Twice integrating its cosine transform by parts gives

    |F_h(t)|<=||h||_1,
    |F_h(t)|<=[|h'(1)|+|h'(0)|+||h''||_1]/t².

Splitting the integral defining M(h) att=1 proves M(h)→0. This establishes
the stated density, including any borderline endpoint behavior inV.

### 2. Continuum identity and bounded positive reflected form

For g inV_0, use the exact finite trial polynomial from the fixed-J lemma,
multiplied byN. Its Chebyshev coefficients at1<=i<=N−1 equal g(i/N);
at i=0 they equal g(0)/2. Fixed-J form convergence therefore gives its
continuous mass→M(g) and its discrete mass→D(g), where

    D(g)=|F_g(0)|²+sum_(j>=1)omega_j|F_g(pi*j)|².

For this finite core the sum is finite. The rescaled entries ofK_N converge
uniformly to the continuous kernelk. Same-parity indices constitute half
the double sum, so K_N's quadratic form tends(1/2)K(g).
For H_N the corresponding limit is(1/2)H(g). To justify its singular
corner, g(1)=g'(1)=0 implies |g(s)|<=C(1−s)². Also u=1−i/N and
v=1−j/N are at least1/N, and

    (u+v)²−N^−2 >= (3/4)(u+v)².

Thus the product-weighted rescaled H kernel is bounded and tends continuously
to zero at the only singular corner; ordinary Riemann-sum convergence
applies after an arbitrarily small corner is removed, then uniformly on
that corner by this bound. The boundary coefficient at i=0 changes the
sum byO(1/N), because the kernel is bounded on that row.

The exact R_N=M_N−H_N+K_N now gives the identity

    D(g)=M(g)+(1/2)[K(g)−H(g)]       (g inV_0).             (2)

The mass floor M_N>=I/N gives M(g)>=||g||²_2 on this core. Since0<k<=1,

    |K(g)|<=||g||²_2<=M(g).

Positive sample weights and(2) imply H(g)<=2M(g)+K(g)<=3M(g).
The positive Laplace-square formH is therefore continuous in the M norm
onV_0. By the density just proved it extends continuously toV, with the
same bound. This extension equals its displayed Laplace integral: the
L² convergence of g_n gives pointwise convergence of their Laplace
transforms, and their H convergence is convergence in L²(y dy), so the
limits agree. The floor M>=||g||² also extends toV.

Similarly D extends continuously toV. Its coordinates really are the
stated samples ofF_g: L² convergence gives pointwise convergence ofF_g,
and the bounded sampling map gives convergence in the weighted sequence
space. Thus(2) and

    (1/2)[K(g)−H(g)] <= (Lambda_edge−1)M(g)               (3)

hold for everyg inV. Moreover K<=M and H>=0 give Lambda_edge<=3/2.
The lower bound Lambda_edge>=1 was established in the fixed-J lemma.

### 3. Two endpoint profiles for arbitrary coefficient vectors

Take an arbitrary sequence a^(N) with a^T M_N a=1. The floor gives
(1/N)sum_i a_i²<=1. Build piecewise constant even/odd profiles e_N,o_N
on intervals[2k/N,min((2k+2)/N,1)], with valuesa_(2k),a_(2k+1).
An absent final odd index has value0. The profiles satisfy

    ||e_N||²+||o_N||² <=(2/N)sum_i a_i²<=2.

Put g_N^+=(e_N+o_N)/2 and g_N^-=(e_N−o_N)/2. Pass to a subsequence
on which they converge weakly inL² to g^+,g^-. For each continuously
differentiable testv on[0,1],

    (1/N)sum_i a_i v(i/N) -> integral g^+(s)v(s)ds,
    (1/N)sum_i (−1)^i a_i v(i/N) -> integral g^-(s)v(s)ds. (4)

For evenN this is the elementary cell quadrature estimate; for oddN,
the extra half-cell costs at mostC||v||_infinity/sqrt(N), using
|a_(N−1)|<=sqrt(N). The derivative quadrature error tends0 by the
same l² bound. Thus no uniform endpoint coefficient hypothesis is hidden.

Let p_N=sum_i a_i T_i. At angles t/N its value divided byN tendsF_(g^+)(t),
and at pi−t/N the corresponding limit isF_(g^-)(t), by(4).
For any fixedT, integrate the continuous mass only over these two disjoint
endpoint intervals. Positivity and the exact Jacobian give, on letting
N→infinity thenT→infinity,

    M(g^+)+M(g^-)<=1.                                    (5)

In detail each endpoint integral is integral_0^T t sinc(t/N)
|(1/N)sum_i (±1)^i a_i cos(it/N)|²dt. The sums divided byN
are bounded uniformly by1, so dominated convergence applies on fixedT.
In particular both limiting amplitudes belong toV.

### 4. Compact remainder and positive-core lower semicontinuity

The rescaled K kernel equals

    k_N(s,r)=1/[max(s+r,2−s−r)²−N^−2].

It converges uniformly to the continuous k(s+r). Cell replacement changes
its operator norm by a quantity tending0, sincek is uniformly continuous;
the odd final half-cell contributesO(N^−1/2) by the coefficient bound
above. The integral operator with continuous kernelk on[0,1] is compact:
approximate its kernel uniformly by finite step functions. Weak profile
convergence therefore gives

    a^T K_N a ->(1/2)[K(g^+)+K(g^-)].                    (6)

ForH_N retain its positive integral, rather than subtracting entries.
Define E_N^e(y)=(2/N)sum_(i even)a_i exp(−(1−i/N)y), and similarly
E_N^o. The substitution x=exp(−y/N) in the exact moment integral yields

    a^T H_N a = integral_0^infinity (N/4)sinh(y/N)
                      [E_N^e(y)²+E_N^o(y)²]dy.

For fixedy, (4) implies E_N^e→integral(g^++g^-)e^{−(1−s)y}ds,
and E_N^o→integral(g^+−g^-)e^{−(1−s)y}ds. Fatou's lemma gives

    liminf a^T H_N a >=(1/2)[H(g^+)+H(g^-)].              (7)

This is the step that controls the unbounded reflected core without
assuming norm convergence of its entries.

### 5. Upper spectral limit

Let L be a subsequential upper limit of the largest CC eigenvalue. The
uniform bound keeps it finite. IfL<=1, thenL<=Lambda_edge already.
Otherwise choose maximizing eigenvectors normalized byM_N, and apply
steps3–4 to a further subsequence. The exact signed decomposition yields

    L−1=lim a^T(K_N−H_N)a
       <=(1/2)[K(g^+)−H(g^+)+K(g^-)−H(g^-)]
       <=(Lambda_edge−1)[M(g^+)+M(g^-)]
       <=Lambda_edge−1,

by(3),(5), and Lambda_edge>=1. Hence every upper subsequential limit
is at mostLambda_edge. The fixed-J lemma proves the reverse lower limit
along both parities. This proves(1).

## Scope and open items

The theorem proves convergence to the exact registered operator norm by a
variational compactness argument. It does not upgrade the finite J512
measurement into the value of that norm. The proof has no explicit rate:
weak subsequence extraction, positive-form Fatou and core density are
qualitative. A usable epsilon(N), an infinite-model tail certificate and
a classical symbol/spectral identification remain OPEN. The campaign's
quantitative acceptance criterion is therefore not declared complete.

## History

2026-11-06, S2 Codex mathematical developer; requested gpt-6.1-sol xhigh,
runtime metadata unexposed. Prospective compactness gate refresh recorded
before this proof. Sent for independent challenge after fixed-J lemma.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
