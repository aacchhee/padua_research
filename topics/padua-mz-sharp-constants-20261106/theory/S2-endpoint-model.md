# PD-T?mz-sharp-codex-S2-03 — microscopic signed cardinal sampling model

ID kind: PD-T.
Aliases: endpoint cardinal norm; sine-rational edge model; Nyquist cosine
sampling in radial Lebesgue mass; microscopic CC model.
Split from: PD-T027 sharp-limit/value conjunct; the uniform gap is separately
proved in S2-uniform-upper.md.
Split into: S2-fixed-trial-limit.md, S2-qualitative-limit.md and
S2-finite-certificate.md supply the subsequent proof and computable error.

## Statement / preregistered prediction

For Lebesgue CC on Pi_(N−1), the predicted common even- and odd-N limit is

    Lambda_edge = sup_{J>=1, u in R^J nonzero}
        [4(sum_{j=1}^J (−1)^j u_j)² + sum_{j=1}^J omega_j u_j²]
        / integral_0^infinity t (sum_{j=1}^J u_j f_j(t))² dt,      (P)

where, writing a_j=pi*j,

    omega_j = 2[(−1)^j+a_j*Si(a_j)],
    f_j(t) = 2(−1)^j*a_j²*sin(t)/[t(t²−a_j²)].

All removable singularities are filled by continuity. Si(x)=integral_0^x
sin(v)/v dv. The prediction is that lambda_max(G_(N,N−1)) tends(P),
with the same constant along both N parities. Formula(P), rather than a
post-fit decimal, is the frozen exact candidate prediction. No final S4
extrapolation has been read by this worker. A model Galerkin norm
computation will follow coordinator publication of this prediction.

## Definitions

For t>=0 define the microscopic Lobatto cardinal functions

    L_0(t)=sin(t)/t,
    L_j(t)=2(−1)^j*t*sin(t)/(t²−a_j²)       (j>=1).

Then f_j=L_j−2(−1)^j L_0, and equivalently

    f_j(t)=2 integral_0^1 [cos(a_j*s)−(−1)^j]cos(t*s) ds.

Thus f_j(0)=−2(−1)^j, f_j(a_k)=delta_(jk) for every k>=1,
and f_j(t)=O_j(t^-3) at infinity. For finite u, the endpoint sample at0
is u_0=−2sum(−1)^j u_j. The exact quadratic numerator in(P) is
u_0²+sum omega_j u_j². The denominator uses t dt, from
N² dx=N sin(t/N)dt under theta=t/N.

The candidate Hilbert space is the completion of finite linear combinations
of f_j under the positive norm integral t f²dt. Formula(P) is the squared
norm of evaluation into the weighted sequence space. Boundedness was a
registration obligation and is proved in S2-fixed-trial-limit.md, then
sharpened in S2-qualitative-limit.md. The formulation defines the norm without assuming
a classical bounded Wiener–Hopf symbol.

## Assumptions

Exact Lebesgue CC, N+1 Lobatto nodes, degree N−1. The proposed local trial
family has fixedJ as N tends infinity, and uses no other endpoint data.
Both parity sequences agree by S2-qualitative-limit.md. The quantitative
finite-to-limit error is proved in S2-finite-certificate.md.

## Status by part

This file preserves the registered definition/prediction (P); it makes no
separate current PROVED claim duplicating its follow-on theorems.
The convergence theorem is PD-T?mz-sharp-codex-S2-05 in
S2-qualitative-limit.md, and the finite certificate is
PD-T?mz-sharp-codex-S2-06 in S2-finite-certificate.md. Their statements and
proofs are authoritative. The original prediction above is historical.

## Depends on

PD-T013 cardinal/DCT normalization and exact positive weights.
IDEA386/PD-N104 supply predecessor/obstruction memory, not the model formula.
The gate and candidate record are novelty-gate-S2.md and ideas/S2-endpoint.md.
No external literature result is used. An eventual Toeplitz-plus-Hankel or
Wiener–Hopf spectral identification must specify the correct domain and symbol;
those labels alone supply neither the norm nor a convergence theorem.

## Checks

No model numerical computation at this registration boundary. Source/rules
SHA2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861. Runs needed after publication:
construct continuous Gram by its closed form, validate selected entries by
independent quadrature, then solve small-to-moderate Galerkin pencils.

## Sources

Only local exact formulas, independently derived here. No primary source
is cited without a fulltext reading, and no novelty/priority claim is made.

## Derivation and precise limitations

Let ell_(N,j) be the degreeN Lobatto cardinal polynomial. For fixedj>=1,
use the exact degree-constrained polynomial

    p_(N,j)=ell_(N,j)−2(−1)^j ell_(N,0).

The DCT-I coefficient ofT_N is (1/N)sum c_k(−1)^k p(x_k),
where c_0=c_N=1/2 and all other c_k=1. The two nonzero nodal values
of p_(N,j) cancel this coefficient exactly; p_(N,j) belongs Pi_(N−1).
This is not the inadmissible full-space trial ofPD-N006.

The cardinal formula gives, at theta=t/N,

    ell_(N,j)(cos(t/N)) -> L_j(t),
    p_(N,j)(cos(t/N)) -> f_j(t).

The cancellation removes the common sin(t)/t tail, leaving t^-3 decay.
From PD-T013's exact weights, a fixed-node Riemann-sum limit gives

    N²w_0 ->1,
    N²w_j ->2[cos(pi*j)+pi*j*Si(pi*j)]=omega_j.

Indeed, the limiting bracket is
1+(1/2)integral_0^(1/2)(1−cos(2*pi*j*x))/x²dx
=cos(pi*j)+pi*j*Si(pi*j). Both N parities have this same limit.
A proof with explicit fixed-J error is the next development obligation.

For fixedu, these identities predict precisely the numerator and denominator
of(P). Even proved fixed-J form convergence would give only
liminf lambda_max>=Lambda_edge. It would not supply the reverse inequality:
maximizing vectors may spread over unbounded endpoint indices or mesoscopic
scales. This was the open upper-limit obligation at registration. It is
resolved subsequently by the domain-density, compact remainder and positive
form argument in S2-qualitative-limit.md; a classical symbol is not needed.

## Closed-form model matrix to check after registration

For i,j>=1 let C_ij=integral_0^infinity t f_i(t)f_j(t)dt and
D_ij=delta_ij*omega_i+4(−1)^(i+j). Write

    d_j=gamma+log(2*a_j)−Ci(2*a_j),
    Ci(x)=−integral_x^infinity cos(v)/v dv.

The derived evaluation formulas to be checked numerically after publication are

    C_ij=2(−1)^(i+j)(a_i²*d_j−a_j²*d_i)/(a_i²−a_j²),  i!=j,
    C_jj=2[a_j*Si(2*a_j)+d_j].

They follow by partial fractions and translated sin² integrals; the exact
integral definition in(P) is canonical. A generalized eigenvalue of(D_J,C_J)
is a finite model lower bound/measurement, not a proof of the infinite norm
or of convergence of the actual CC spectrum.

## Development crosslinks and future refinements

The exact prediction was published before computation. The finite model
matrix and actual model solve passed independent replay. Fixed-J errors,
the full operator-norm limit and an explicit computable vanishing spectral
error are proved in the linked follow-on files. Certified decimal evaluation,
an elementary/practical rate, and an optional classical symbol identification
remain OPEN as future refinements. S2 stopped after five productive rounds
at coordinator instruction, without any certificate numerical solve.

## History

2026-11-06, S2 Codex mathematical developer; requested gpt-6.1-sol xhigh,
runtime metadata unexposed. Exact operator prediction sent to coordinator
before any new model numerical solve or final S4 fit was read.


2026-11-06 supplementary-check correction: the T_N coefficient display
was corrected from2/N to1/N (the top DCT-I coefficient has the additional
half factor). The exact cancellation, trial family, model expression,
matrices and every numerical calculation are unchanged.

## Development after the frozen prediction

The coordinator published the exact prediction at513f3bd802abf23f9c1470930a68f4e09e2a8c77
before the authorized solve. The finiteJ512 measured model eigenvalue is
1.0044369188646673, with raw receipt evidence/S2-model.json and producer
code/S2_model.py. The distinct checker reproduced the actual run and
quadratures and analytically verified the closed-form Gram. This decimal
is not asserted to be the infinite norm.

S2-fixed-trial-limit.md proves fixed-J form/eigenvalue convergence with
explicit errors and has supplementary distinct-review PASS. The later
S2-qualitative-limit.md proves the full common-parity limit, by
core density and compact-positive-form variational arguments; its proof
passed separate distinct review. S2-finite-certificate.md then gives
explicit finite L_N,U_N bracketing both the actual finite eigenvalue and
the model norm, with U_N−L_N->0. That stronger proof passed its own distinct
review and is not attributed to the earlier checker approval.

The registered formula is unchanged. The supporting theorem files carry
their current part-by-part statuses and independent review records. The
certified numerical norm value, a practical elementary convergence rate,
and any classical Toeplitz-plus-Hankel/Wiener–Hopf symbol identification
remain OPEN. No final S4 fit has been read by this worker.
