# PD-N?argmax-bridge-codex-C01-near-01 — A vanishing finite-n cusp does not replace the fractional residual term

ID kind: PD-N. Aliases: quadratic/entropy-only residual certificate obstruction.
Split from: the pure-quadratic subcase of N1-19's trial modulus, not C1.
Split into: none. Supporting positive coefficient: C01-near-axis-limit.md.

## Exact negative statement

Overall status: **PROVED**, analytic developer consequence; independent review
is separate. There are no finite nonnegative constants K0,K1 and sequence
c_n>=0 with c_n->0 such that, for all integer n>=10^6 and all
0<=alpha<=1/2,

    Q_n(alpha,0)<=K0*alpha²+K1*alpha²log(1/alpha)+c_n*alpha.     (1)

Terms at alpha=0 are defined by continuity. The same obstruction holds if
a nonnegative additive J_n->0 is also allowed in (1).

Candidate disposition: **REJECTED: refuted** only for this proposed
quadratic/entropy-only uniform modulus with vanishing degree errors. This is
a restriction on one sufficient certificate, not a rejection of Q_n-G_n<=
1/40000, the unchanged model, C1 or the physical argmax theorem. A retained
positive fractional term is explicitly outside the rejected scope.

## Proof

Fix alpha>0 and let n tend to infinity in (1). The separately proved
C01-near-axis-limit theorem gives

    q_infinity(alpha)<=K0*alpha²+K1*alpha²log(1/alpha).

Divide by alpha^(3/2) and let alpha decrease to zero. The left side tends
to the strictly positive kappa=4*pi^-2 integral_0^1 sqrt(1-y^4)dy, while the
right side tends to zero. This is a contradiction. An additive J_n->0
disappears in the first limit in the same way.

More generally, any uniform trial upper with an added k*alpha^(3/2), the
same quadratic/entropy terms and vanishing c_n,J_n must have k>=kappa.
This is a necessary asymptotic coefficient, not a sufficient full-domain
bound. The finite-n primitive cusp PD-N079 concerns the opposite ordered
limit and remains a separate obstruction.

## Assumptions, evidence, limits and history

Exactly the fixed N1-18 Q_n and N1-15 model, with no changes to their
cutoffs, exceptional mode or collision convention. Dependency:
C01-near-axis-limit.md; no external theorem, computation or numerical fit.
The full positive target remains OPEN in N1-19 and the C01 attempt. There
is no claim that Q_n is itself maximal at zero or that the favorable
logarithmic loss can be omitted. 2026-11-06, rules/input
4b728b04216a5490910780bc609a82b853058426; Codex, parent-assigned Astra ultra,
serving metadata unexposed.

