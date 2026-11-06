# PD-N?padua-3d-codex-T4-01 — exponential growth for monotone-height Padua stacks

ID kind: PD-N. Aliases: monotone Radon stack; weighted logarithmic energy.
Split from: BRIEF E2's polynomial-growth expectation, restricted to this
specified height ordering. Split into: none.

## Statement

For every n>=1 put the degree-(n-k) Padua set on z_k=cos(k*pi/n), k=0..n,
using T4-01's exact convention. Let Lambda_M(n) be the continuous cube
Lebesgue constant of this unisolvent total-degree stack. Then

liminf_{n->infinity} log Lambda_M(n)/n >= 3*zeta(3)/(2*pi^2)>0.   (1)

Equivalently, for each epsilon>0 there exists n_0(epsilon) such that every
n>=n_0 satisfies Lambda_M(n)>=exp((3*zeta(3)/(2*pi^2)-epsilon)n).
In particular this ordering has no O(n^a) Lebesgue bound for any fixed real a.
The reflected ascending ordering has the same conclusion.

## Definitions / assumptions / status

Natural logarithms; zeta(3)=sum_{r>=1}r^-3. n is an integer tending through
all positive degrees. Overall status: **PROVED**, written analytic proof,
developer pending independent audit. Candidate disposition: **REJECTED:
refuted** for a polynomial-growth assertion about this ordering only.
No such assertion about the Leja ordering or all plane stacks is refuted.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-codex-T4-02's monotone ordering as a
polynomial-quality baseline, and the restricted BRIEF E2 expectation.
Parameter range: this exact all-n family, with an eventual lower bound;
the onset n_0 is not made effective. No claim of rank failure is involved.

## Depends on

PD-T?padua-3d-codex-T4-01 (all-n unisolvence) and T4-02 (exact determinant
factor and permutation-average comparison). Elementary trigonometry,
integrable Riemann sums and the absolutely convergent integrated Fourier
series justified below. No measurement or unread literature theorem.

## Proof

Write N_j=binom(n-j+2,2) and D_M=product_{i<j}(cos(i*pi/n)-
cos(j*pi/n))^{N_j}. First we prove

lim n^-4 log D_M = -log2/24-zeta(3)/(4*pi^2).                    (2)

Set f(s,t)=log(cos(pi*s)-cos(pi*t)), 0<=s<t<=1. The factorization

f(s,t)=log2+log sin(pi*(s+t)/2)+log sin(pi*(t-s)/2)

shows f is continuous off the diagonal, with integrable logarithmic
singularities. Here is explicit uniform control needed for the discrete
Riemann sum, including the two endpoint corners. For i<j, d=j-i,
min(i+j,2n-i-j)>=d. The inequality sin(pi*u/2)>=min(u,2-u)
for 0<=u<=2 therefore gives

|f(i/n,j/n)| <= log2+2 log(n/d).                                (3)

Consequently the normalized absolute contribution with d<=epsilon*n is
at most

(n+1)/n^2 sum_{1<=d<=epsilon*n}[log2+2log(n/d)]
 <= C*epsilon*(1+|log epsilon|)+O(log n/n),                      (4)

with an absolute C (the elementary integral comparison for log(n/d)
or log(q!) proves this). The same strip has an integral tail tending to
zero, by the identical continuous inequality with t-s in place of d/n.
Outside the strip f is continuous on a compact domain and ordinary
Riemann sums converge. Letting epsilon decrease to zero proves convergence
of the full sums. Also N_j/n^2=(1-j/n)^2/2+O(1/n) uniformly; the normalized
absolute sums are bounded by (3), so this weight replacement has error
O(1/n). Thus

lim n^-4 log D_M = (1/2) int_0^1 (1-t)^2 J(t) dt,
J(t)=int_0^t f(s,t) ds.

Substituting in the two sine terms gives the particularly simple identity

J(t)=t log2+2 int_0^t log sin(pi*v) dv
    =-t log2-(1/pi)sum_{r>=1} sin(2*pi*r*t)/r^2.                 (5)

For a self-contained justification of the series, for 0<rho<1 expand
log|1-rho*exp(2*pi*i*v)|=-sum rho^r cos(2*pi*r*v)/r,
then integrate in v. For rho>=1/2 the absolute logarithm is bounded by
an integrable constant plus |log sin(pi*v)| because
|1-rho*exp(2*pi*i*v)|^2=(1-rho)^2+4rho sin^2(pi*v).
Dominated convergence applies as rho increases to1. The integrated series
has summable r^-2 coefficients, so its limit is uniform in t. This proves
(5), with endpoint values taken by continuity.

Termwise integration in (5) is permitted by this uniform absolute
convergence. Direct integrations give

int_0^1 t(1-t)^2 dt=1/12,
int_0^1 (1-t)^2 sin(2*pi*r*t)dt=1/(2*pi*r).

Equation (2) follows.

From T4-02, log Lambda_M >= [S_n A_n-log D_M]/N, where
S_n=binom(n+3,4), A_n->-log2 and N=binom(n+3,3). Hence

lim n^-4(S_n A_n-log D_M)=zeta(3)/(4*pi^2),
N/n^3->1/6.

Divide the inequality by n and take the lower limit. This proves (1).
The positive lower rate contradicts every fixed polynomial upper bound.
Reflecting z to -z changes neither the cube norm nor node norm, proving
the ascending-order assertion.

## Checks / sources / scope

No numerical fit is used. This is a hand proof, not a finite computer
certificate. Primary historical novelty comparison is pending in
literature-T4.md; no first-result or publication-priority claim.
The exact finite inequality in T4-02 can be evaluated as a diagnostic,
but its floating evaluation is not an independent proof.

## Open items

Independent mathematical audit pending. Effective finite-n remainder/onset
is not proved. Other height orderings remain separate questions; the
O(log^3 n) construction target remains OPEN.

## History

2026-11-06, Codex developer, assigned gpt-6.1-sol/high, runtime metadata
unexposed; rules/input ccd9e905d19c0c625c196c4a3f3e707058ed042a.
The restricted negative conclusion is split from the supplied expectation;
it does not silently replace the original 3-D target.
