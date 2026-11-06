# PD-T526 — uniform CC upper bound by a reflected core

2026-11-06 ID history: `PD-T?mz-sharp-codex-S2-01` → `PD-T526`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: five-thirds endpoint upper bound; IDEA386 normalized remainder;
positive reflected moment completion.
Split from: PD-T027, uniform-gap conjunct; its sharp-limit
statement remains unchanged and OPEN.
Split into: none.

## Statement

For every integer N>=2 and every real polynomial p of degree at mostN−1,
with the Lebesgue Clenshaw–Curtis rule Q_N at cos(j*pi/N),

    0 < Q_N(p²) <= (5/3) integral_{-1}^1 p(x)² dx

when p is nonzero. Thus lambda_max(G_(N,N−1))<=5/3 uniformly, and
2−lambda_max>=1/3. This bound is not asserted sharp.

## Definitions

Use PD-T013's exact Chebyshev mass matrices M,R on indices0,...,N−1:
a^T M a=integral p² and a^T R a=Q_N(p²) for p=sum a_i T_i.
Write s=i+j and r=2N−s. Set

    H_ij = 1_{s even}/(r²−1),
    K_ij = H_ij                         if s<=N,
           1_{s even}/(s²−1)            if s>N.

All denominators in H are positive because r>=2. In the second line
of K, s>N>=2, so that denominator is positive as well.

## Assumptions

Exact real arithmetic, the Lebesgue measure dx, N+1 Lobatto nodes,
and degree at mostN−1. No external asymptotic theorem is assumed.

## Status by part

Overall status: **PROVED** in analytic development.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Uniform five-thirds upper bound for allN>=2 | PROVED | Analytic proof below; independent audit not supplied by this worker |

Candidate / claim disposition: retained successful quantitative continuation
of IDEA386. PD-T027's sharp limit remains OPEN. The uniform upper-gap
conjunct of that target is established by this split result; its limit/value
conjunct is not.

## Depends on

PD-T013: exact moment/alias formulas and positive CC weights.
PD-T015: M>=E/N, E=diag(2,1,...,1). Its explicit all-N proof is read.
Elementary positive-integral and finite-dimensional quadratic-form bounds.
No dependence on PD-T014's sign replacement or on numerical spectra.

## Checks

The proof is analytic. No mathematical numerical run is needed or claimed.
Frozen source/rules SHA:2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.
Novelty-gate provenance: ../novelty-gate-S2.md.
Independent reconstruction remains a coordinator-owned audit obligation.

## Sources

The full reflected-core completion is the retained local IDEA386, read in
full. The new calculation supplies its missing continuous-mass normalized
bound. No external literature fact or historical priority claim is used.

## Proof

PD-T013 gives the exact identity

    R = M−H+K.                                             (1)

Indeed, for s<=N, R_ij=M_ij and H_ij=K_ij. For even s>N,
(M−R)_ij=1/(r²−1)−1/(s²−1)=H_ij−K_ij. For odd s every
entry of H,K and M−R vanishes.

The matrix H is positive semidefinite. For any real a,

    a^T H a = (1/2) integral_0^1 (1−x²)
       [ (sum_{i even} a_i x^(N−1−i))²
        +(sum_{i odd} a_i x^(N−1−i))² ] dx >=0.           (2)

To verify each coefficient, (1/2) integral_0^1
x^(2N−2−i−j)(1−x²)dx=1/((2N−i−j)²−1).
All exponents N−1−i are nonnegative, including the endpoint i=N−1.
No assertion of positive semidefiniteness is made for K or for M−R.

Let L_N=N if N is even, and L_N=N+1 if N is odd. In every nonzero
K entry, its denominator is u²−1 for an even integer u>=L_N:
if s<=N, u=2N−s>=N; if s>N, u=s>N. Since s and2N are even,
u is even. Therefore

    0<=K_ij<=1/(L_N²−1).

Each row has at most ceil(N/2) nonzero entries, because K only
couples indices of the same parity. Put

    kappa_N = ceil(N/2)/(L_N²−1).

Using 2|a_i a_j|<=a_i²+a_j² and symmetry, the row-sum bound gives

    a^T K a <= sum_ij K_ij |a_i a_j|
              <= kappa_N sum_i a_i².                    (3)

This is only an estimate for the transition term in (1); the gap form
is never replaced by its value at |a|. By PD-T015,

    sum_i a_i² <= a^T E a <= N a^T M a.

Consequently K<=beta_N M, where

    beta_N = N*ceil(N/2)/(L_N²−1)
           = N²/[2(N²−1)]             for evenN,
             (N+1)/[2(N+2)]           for oddN.

For evenN>=2 the first expression is at most2/3; for oddN>=3
the second expression is less than1/2. Equations(1)–(3) yield

    a^T R a <= a^T M a+a^T K a
              <= (1+beta_N) a^T M a <= (5/3)a^T M a.

Positive CC weights and polynomial unisolvence give the strict positive
lower inequality for nonzero p, completing the proof.

## Scope

This proves the uniform endpoint upper gap analytically for everyN>=2,
with no finite-range numerical certification or crossover. It retains the
original coefficient signs, so PD-N104's failed intermediary is bypassed.
The constants do not locate the much smaller sharp upper spectral limit.
It yields limsup lambda_max<=3/2, because beta_N tends1/2, but it
neither proves existence of the limit nor identifies its value.

## Open items

Audit-01 accepts this proof. The endpoint model and norm convergence are
proved in S2-qualitative-limit.md; S2-finite-certificate.md proves a
quantified finite-to-model error. A certified decimal remains unresolved.
Pointwise entry or fixed-vector convergence alone would not suffice.
The original PD-T027 is to retain its exact sharp-limit question with a
link to this uniform-gap conjunct, according to coordinator/auditor disposition.

## History

2026-11-06, S2 Codex mathematical developer; requested gpt-6.1-sol xhigh,
runtime metadata unexposed. Rules/input SHA above. After full closest-1D
gating and K0 clearance, completed IDEA386's previously unestimated
transition remainder using PD-T015. No Git or shared-file operation.
