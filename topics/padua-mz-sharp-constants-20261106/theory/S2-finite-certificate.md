# PD-T531 — explicit finite spectral brackets

2026-11-06 ID history: `PD-T?mz-sharp-codex-S2-06` → `PD-T531`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: finite-window residual certificate; computable finite-to-limit error.
Split from: the quantitative obligation of the registered S2 endpoint model.
Split into: an elementary asymptotic rate and a certified decimal norm value
remain OPEN. The certificate below uses exact finite matrix eigenvalues.

## Statement

There are explicit, wholly finite quantities L_N,U_N defined below such that
for every integerN>=2,

    L_N <= min(lambda_max(G_(N,N−1)),Lambda_edge),
    max(lambda_max(G_(N,N−1)),Lambda_edge) <= U_N,
    epsilon_N := U_N−L_N >= |lambda_max(G_(N,N−1))−Lambda_edge|,
    epsilon_N ->0.                                             (1)

The definitions involve only finite real symmetric matrices, the fixed-J
model matrices and ordinary integrals over finite intervals. Thus(1) is
an explicit computable finite-to-limit error. It is not an elementary
power/log formula, a practically evaluated error, or a certified decimal
evaluation ofLambda_edge. No floating-point matrix solve is a certificate
without its own enclosure of the finite eigenvalue.

## Definitions

Use M,H,K,V and Lambda_edge from S2-qualitative-limit.md. For T,Y>0 put

    M_T(g)=integral_0^T t [integral_0^1 g(s)cos(st)ds]²dt,
    H_Y(g)=integral_0^Y y [integral_0^1 g(s)e^{−(1−s)y}ds]²dy.

For alpha>=0, the bounded self-adjoint residual on L²[0,1] is

    B_(T,Y,alpha)=K/2−H_Y/2−alpha M_T.

Its continuous kernel is

    b(s,r)=1/[2 max(s+r,2−s−r)²]
           −(1/2)integral_0^Y y e^{−(2−s−r)y}dy
           −alpha integral_0^T t cos(st)cos(rt)dt.

For an integerQ>=1 let s_l=(l−1/2)/Q,1<=l<=Q, and let B_Q be the
real symmetric Q byQ matrix with entries b(s_l,s_m)/Q. Define

    A=1+Y³/6+alpha T³/3,
    u(T,Y,alpha,Q)=max(0,lambda_max(B_Q))+A/Q,
    E_M(N,T)=T²/N²+8T³/(3N)+2T²/sqrt(N),
    E_K(N)=8/N+2/sqrt(N)+2/N²,
    E_H(N,Y)=4Y³/(3N)+Y²/sqrt(N),
    E(N,T,Y,alpha)=alpha E_M(N,T)+E_K(N)+E_H(N,Y).

For every N>=max(2,T), the following two individual certificates hold:

    Lambda_edge <=1+alpha+u(T,Y,alpha,Q),
    lambda_max(G_(N,N−1))
       <=1+alpha+u(T,Y,alpha,Q)+E(N,T,Y,alpha).             (2)

To make(1) a single explicit sequence, set

    T_N=Y_N=max(1,floor(N^(1/12))), Q_N=max(1,floor(sqrt(N))),
    U_N=min(5/3, min_{k=0,...,ceil(N/2)}
        {1+k/N+u(T_N,Y_N,k/N,Q_N)+E(N,T_N,Y_N,k/N)}).

For the lower bound use C_J,D_J,lambda_J=lambda_max(D_J,C_J),m_J=lambda_min(C_J)
and the fixed-trial bounds

    e_J(N)=1000 J[1+(pi J)^4]/N²,
    d_J(N)=20[1+8(pi J)^3]/N+4J/(N²−1),
    r_J(N)=[d_J(N)+(5/3)e_J(N)]/[m_J−e_J(N)].

The admissible set A_N consists of all integers 1<=J<=T_N satisfying
N>=ceil(2pi J) and e_J(N)<m_J. Finally define

    L_N=max({1} union {lambda_J−r_J(N):J in A_N}).

These definitions are finite also when A_N is empty.

There is no equality oracle hidden in the admissibility test. For eachJ
with N>=ceil(2pi J), put v=d_J(N)+(5/3)e_J(N)>0 and x=m_J−e_J(N).
After clipping below by1, its contribution toL_N can equivalently be
computed as

    max(1,lambda_J−v/max(x,2v)).                           (C)

Indeed lambda_J<=Lambda_edge<=3/2. Ifx<=2v, both the original clipped
contribution (including the inadmissible case x<=0) and(C) equal1;
ifx>2v, the formulas coincide directly. Thus only continuous computable
operations with denominator at least2v are needed. The remaining test
N>=ceil(2pi J) is decidable because2pi J is irrational. Matrix entries
require no tail-integral oracle either: in the closed-form C_J formula
one may evaluate

    d(a)=gamma+log(2a)−Ci(2a)=2 integral_0^a sin²(v)/v dv,

and all Si terms are likewise ordinary integrals on finite intervals.

## Assumptions and status

Exact real Lebesgue CC, N+1 Lobatto nodes, degree at mostN−1.
Overall status: **PROVED** in analytic development; independent challenge
requested. No finite certificate matrix has been numerically evaluated.

| Mathematical part | Status | Scope |
|---|---|---|
| Explicit brackets(1) and certificates(2) | PROVED | Finite matrix formulas and explicit constants below |

The theorem concerns the exact operator norm and an explicit computable
error. Future refinements are listed under Practical limits and checks,
outside its proved statement; see also S2-endpoint-model.md.

## Depends on

PD-T015 finite mass floor. S2-uniform-upper.md exact signed decomposition
and5/3 bound. S2-fixed-trial-limit.md exact C_J,D_J and fixed-J errors.
S2-qualitative-limit.md continuum identity, domain density, compactK,
mass floor and Lambda_edge>=1. The prospective/formalization record is
ideas/S2-certificate.md and novelty-gate-S2.md. No external source or
historical novelty/priority assertion is used.

## Proof

### 1. Finite matrix upper bound for the residual

The kernel b is separately Lipschitz with constant at mostA. Indeed the
three terms have derivative bounds1,Y³/6,alpha T³/3. Its midpoint
step-kernel differs uniformly from b by at mostA/Q. By the elementary
Schur bound its operator norm differs by at mostA/Q. The step operator
has the finite matrix B_Q on the space of cell constants and is zero
on its orthogonal complement. Consequently

    B_(T,Y,alpha) <= u(T,Y,alpha,Q) I.                    (3)

The outer max(0,...) is essential because of that infinite-dimensional
zero subspace. From H>=H_Y,M_T<=M,||g||²<=M(g) and alpha,u>=0,

    (K(g)−H(g))/2 <= alpha M_T(g)+u||g||²
                         <=(alpha+u)M(g).

The continuum identity D=M+(K−H)/2 proves the first part of(2).

### 2. Explicit finite-profile quadrature errors

Take a finite coefficient vector with a^T M_N a=1. Then sum a_i²<=N.
Use the even/odd step profiles e,o and g^+=(e+o)/2,g^-=(e−o)/2
from the qualitative theorem, on cells[2k/N,min((2k+2)/N,1)]. For every
C¹ testv, writing q_e(v)=(2/N)sum_(i even)a_i v(i/N), and similarlyq_o,

    |q_e(v)−integral e v|,
    |q_o(v)−integral o v|
           <= 2||v'||_infinity/N+||v||_infinity/sqrt(N).  (4)

For full cells this follows from their width2/N and sum|a_i|<=N.
For oddN, the final even half-cell has missing mass|a_(N−1)|/N
at most1/sqrt(N); the absent final odd value is0. This proves(4)
without a hidden endpoint coefficient bound. Also

    ||g^+||²+||g^-||²=(||e||²+||o||²)/2<=1.              (5)

For v=cos(st), equation(4) implies that each physical endpoint profile
F_(g^±)(t) differs from (1/N)sum(±1)^i a_i cos(it/N) by at most
2t/N+1/sqrt(N). Each of these two quantities has absolute value<=1.
Their squared difference is thus at most twice that error. The two
physical endpoint intervals[0,T/N] and[pi−T/N,pi] are disjoint when
N>=T. Their total continuous mass is at most1, and sinc(t/N)>=
1−T²/(6N²). Hence their unweighted t dt masses total at most
1+T²/N². Integrating the squared-difference estimate gives

    M_T(g^+)+M_T(g^-) <=1+E_M(N,T).                     (6)

For K_N the exact rescaled same-parity kernel at grid points is
1/[max(s+r,2−s−r)²−N^-2]. Its difference from k(s+r) is at most
4/(3N²). The total variation of q_e andq_o together is at most2,
so this costs at most2/N² in the quadratic form. For k itself use(4)
in each variable: its supremum is1 and its Lipschitz constant is2;
each of q_e,q_o and the profile integrals has total variation at most2.
The two-variable replacement costs at most8/N+2/sqrt(N). Therefore

    a^T K_N a <=[K(g^+)+K(g^-)]/2+E_K(N).               (7)

For H_N retain its exact positive integral representation

    a^T H_N a =integral_0^infinity (N/4)sinh(y/N)
                     [q_e(v_y)²+q_o(v_y)²]dy,
    v_y(s)=e^{−(1−s)y}.

Both the q-values and the corresponding integrals have absolute value
at most2. Equation(4) bounds their differences by2y/N+1/sqrt(N),
so the sum of their squared differences is at most8 times this.
Truncate to[0,Y], and use (N/4)sinh(y/N)>=y/4, to get

    a^T H_N a >=[H_Y(g^+)+H_Y(g^-)]/2−E_H(N,Y).          (8)

Combine(3),(5)–(8) with the exact signed decomposition R_N=M_N−H_N+K_N.
Its excess quadratic form is at most

    alpha[M_T(g^+)+M_T(g^-)]+u[||g^+||²+||g^-||²]
       +E_K+E_H <=alpha+u+E.

Maximizing proves the finite part of(2).

### 3. Convergence of the finite certificates

Write delta=Lambda_edge−1 in[0,1/2]. For any fixed alpha>0 with
alpha>=delta, define the positive upper spectral value

    u_cont(T,Y,alpha)=max(0,sup_{||g||=1} B_(T,Y,alpha)(g)).

Then u_cont(T,Y,alpha)->0 as T,Y->infinity. To prove this, suppose a
sequence of unit vectors had residual bounded below by a positive constant.
Pass weakly inL² to g. Compactness ofK gives convergence of its forms.
The nonnegative truncated physical/Laplace integrals and pointwise transform
convergence give Fatou lower bounds M(g),H(g). The residual upper bound
and alpha>0 force M(g)<infinity. The limiting positive residual would
therefore be at most

    [K(g)−H(g)]/2−alpha M(g)
       <=(delta−alpha)M(g)<=0,

a contradiction. This is a spectral compactness argument, not entrywise
convergence. No uniform numerical rate is asserted for u_cont.

The midpoint comparison also gives

    u(T,Y,alpha,Q)<=u_cont(T,Y,alpha)+2A/Q.

With the specified T_N,Y_N,Q_N, both A/Q_N and E tend0 for boundedalpha.
Rounding a fixed alpha in[0,1/2] to k/N costs at most1/N inalpha and
at most T_N²/(2N) in residual operator norm; both vanish. Ifdelta<1/2,
choose any alpha in(delta,1/2] and then letalpha decrease todelta.
Ifdelta=1/2 choosealpha=1/2. This proves limsup U_N<=1+delta.
Every U_N boundsLambda_edge andlambda_max by(2) and the uniform5/3
theorem, so U_N->Lambda_edge.

For each fixedJ, eventually J<=T_N,N>=ceil(2pi J),e_J(N)<m_J and
r_J(N)->0. The fixed-J lemma gives lambda_J<=Lambda_edge and a finite
trial eigenvalue withinr_J(N) oflambda_J. Since both full eigenvalues
andLambda_edge are at least1, L_N bounds both from below. Finally
sup_J lambda_J=Lambda_edge, so L_N->Lambda_edge. Equations(1) follow.

## Practical limits and checks

This gives an exact finite specification ofepsilon_N and proves its
vanishing. The crude Lipschitz constants may make it computationally
expensive and weak at accessibleN; no practical performance claim is made.
An elementary power/log bound for this certificate and a certified decimal
value ofLambda_edge remain OPEN as future refinements. They are not parts
of the theorem above. The exact norm is identified by the registered
operator(P), and the brackets permit certified evaluation in principle.
Replacing a finite eigenvalue by a floating approximation requires a
certified enclosure (for example interval LDL or a residual plus a valid
spectral upper certificate). No such solve has been run for this theorem.
Independent mathematical review and required Claude audit remain separate.

## History

2026-11-06, S2 round5, Codex mathematical developer; requested
gpt-6.1-sol xhigh, runtime metadata unexposed. Exact finite certificate
derived after the qualitative proof and before any certificate numerics.


## 2026-11-06 practical limitation (audit A8)

MEASURED float estimates of these proved formulas, from
 audit-01-support/S2/LN_est.out and UN_est.out: L_N stays 1 until about
4.4·10⁶, is about 1.00356 at 10⁸ and 1.00442 at 10¹⁸. U_N is about
1.08 at 10⁶ and 1.062 at 2.7·10⁸. Thus the certificate remains wider than
0.05 throughout the audited feasible evaluations. These are estimates of
the formula, not rigorous decimal enclosures; the convergence theorem and
its quantifiers are unchanged.


## 2026-11-06 audit completion pointer

The earlier requests for independent/Claude review describe the development
boundary. Claude audit-01.md now accepts this analytic proof at its stated
scope. That completed audit supersedes earlier pending-review metadata; it
does not certify floating decimal values or approve this response.
