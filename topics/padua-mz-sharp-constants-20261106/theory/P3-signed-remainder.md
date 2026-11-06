# PD-T544 — a uniform signed logarithmic remainder

2026-11-06 ID history: `PD-T?mz-sharp-codex-P3-01` → `PD-T544`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: dyadic sinc estimate; reciprocal-cardinal pole remainder.
Split from: supporting estimate for P3's reverse-bound attempt at PD-T020.
Split into: none. This is not a case or conjunct of PD-T020.

## Statement

Let g=(g_k)_(k>=1) be any finitely supported real or complex sequence.
For nonintegral t>0 set

    B_k(t)=t^2/[k(t^2-k^2)]-1_(k<t)/k,
    (Eg)(t)=sin(pi t) sum_(k>=1) g_k B_k(t).

Then, with continuous extension at positive integral t,

    integral_0^infinity |Eg(t)|^2 dt/t
        <=1600 sum_(k>=1) |g_k|^2/k.                  (1)

The constant is uniform in the support, its length and its location.
No regularity, sign, cancellation or envelope assumption is imposed.

## Definitions and assumptions

All norms and sums are exact. The input measure gives mass 1/k to k;
the output measure is dt/t. Values at isolated points do not affect
the estimate. The sine removes each simple pole, and the jump from
the strict indicator also vanishes after multiplication by the sine.

## Status by part

Overall status: PROVED in analytic development.

| Part | Status | Evidence |
|---|---|---|
| Uniform all-input estimate (1) | PROVED | Elementary sinc orthogonality and weighted Schur proof below |

Historical checkpoint: the original PD-T020 target was OPEN at this
supporting checkpoint. It is now PROVED via PD-T546 together with PD-T523.
Candidate disposition: retained continuation of S1's signed-transfer
obligation; independent review of this new proof remains separate.

## Depends on

Elementary integration, Cauchy–Schwarz and the Schur inequality (proved
in PD-T017, used here for a discrete-to-continuous kernel). No numerical
data, external singular-integral theorem or fitted parameter is used.

## Proof

### 1. Elementary sinc orthogonality

Put sinc(x)=sin(pi x)/(pi x), with sinc(0)=1. For integers k,l,

    integral_R sinc(t-k) sinc(t-l) dt=1_(k=l).          (2)

For the diagonal, integration by parts and
integral_0^infinity sin(bu)/u du=pi/2 for b>0 give
integral_R sin^2(pi t)/(pi^2 t^2)dt=1. The latter Dirichlet integral
can be established without a Fourier theorem: its exponentially
damped value is arctan(b/epsilon), by differentiating in b and
integrating epsilon/(epsilon^2+b^2); Dirichlet tail estimates, uniform
in epsilon>=0, justify passing epsilon down to zero.

For k!=l, cancel the integer signs and use partial fractions on
sin^2(pi t)/[(t-k)(t-l)]. Each of the two resulting integrals
integral_(-R)^R sin^2(pi t)/(t-k)dt tends to zero: after shifting by
the integer k the integrand is odd, and the excess end intervals
have integral O_k(1/R). Apparent poles are removable. The product
is absolutely integrable, so its integral is zero. This proves (2).
Consequently every finite sequence h satisfies

    integral_R |sum_k h_k sinc(t-k)|^2dt=sum_k |h_k|^2. (3)

### 2. Fixed dyadic blocks and the signed pole

For every integer j let d=2^j, I_j=[d,2d) and

    J_j={positive integers k:d/2<k<4d}.

Each positive integer belongs to at most four J_j. On I_j split the
sum into k in J_j and its complement. The exact identity on J_j is

    B_k(t)=1/[2(t-k)]+D_k(t),
    D_k(t)=-1/[2(t+k)]+1_(k>t)/k.                    (4)

The pole contribution is

    sin(pi t) sum_(k in J_j) g_k/[2(t-k)]
       =(pi/2) sum_(k in J_j) (-1)^k g_k sinc(t-k).

Since t>=d and k<4d, (3) gives

    integral_(I_j) |pole|^2 dt/t
       <= pi^2/(4d) sum_(J_j)|g_k|^2
       <= pi^2 sum_(J_j)|g_k|^2/k.

Sum over j. Its operator norm is at most 2pi<7. This is the step
where signs are retained; no absolute harmonic pole sum is estimated.

### 3. The nonsingular comparable-scale part

For k in J_j and t in I_j one has k>t/4. Hence (4) gives

    |D_k(t)|<=9/(2t).

If J_j is nonempty, d>=1/2, so
sum_(k in J_j) k <=8d^2+2d<=12d^2. Cauchy–Schwarz gives

    |sum_(J_j)g_k D_k(t)|^2
      <=[sum_(J_j)|g_k|^2/k] [sum_(J_j) k|D_k(t)|^2]
      <=243 sum_(J_j)|g_k|^2/k.

Multiplication by sin(pi t) cannot increase this bound. Integration
on I_j and the fourfold overlap give squared norm at most
972 log(2) sum |g_k|^2/k. Thus this operator's norm is below 32.
Empty blocks, including all j<=-2, contribute zero here.

### 4. The separated-scale part

Write its sum as a kernel against input mass 1/k. For k outside J_j,
either k<=d/2<=t/2 or k>=4d>2t. The kernel K(t,k)=k B_k(t) satisfies

    |K(t,k)| <= (4/3)(k/t)^2,  k<=t/2,
    |K(t,k)| <= (4/3)(t/k)^2,  k>=2t.                (5)

Its weighted row sum is below 1. For the first part, a nonempty
sum requires t>=2, and

    (4/(3t^2)) sum_(k<=t/2) k <=1/3.

For t>=1/2, put n=ceil(2t). The second row sum is bounded by

    (4/3)t^2 [n^(-3)+1/(2n^2)]
       <=1/(6t)+1/6<=1/2.

For t<1/2 it is at most (4/3)t^2 sum_(k>=1)k^(-3)
<=2t^2<1/2. These bounds also apply when the actual complement of
J_j is smaller than the two separated ranges in (5).

For every k the weighted column integral is at most

    (4/3)[integral_0^(k/2)(t/k)^2 dt/t
           +integral_(2k)^infinity(k/t)^2dt/t]=1/3.

The discrete-to-continuous Schur inequality therefore gives operator
norm at most 1. For completeness it follows by applying
|sum K g/k|^2 <=(sum |K|/k)(sum |K||g|^2/k), then integrating and
using the column bound. The factor sin(pi t) again has modulus <=1.

The three pieces have norms below 7, 32 and 1. The triangle
inequality proves (1), with the conservative constant 40^2.

## Checks, sources and scope

Pure analytic proof; no script was executed. Rules/source
`0205690b9c4e959a28e949083e9a1808735abf4b`; development began after R
publication `17ca9f441cece178354e70504a6c739df501a224`. The gate and
candidate are ../novelty-gate-P3.md and ../ideas/P3-reverse.md.

PD-N005's failed absolute-cardinal L1-column estimate is never used.
This theorem controls the signed homogeneous remainder only. Actual
CC weights, endpoint columns, the global cotangent correction and the
bulk remain assembly obligations before PD-T020 can be upgraded.

## History

2026-11-06, P3 round1, Codex mathematical developer; requested
gpt-6.1-sol xhigh, serving metadata unexposed. New supporting result
in separate files; accepted predecessor statements/proofs unchanged.
