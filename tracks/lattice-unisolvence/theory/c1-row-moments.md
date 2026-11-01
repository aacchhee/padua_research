# PD-T?lattice-c1-codex-03 — Row-root moment criterion for total-degree interpolation

Final ID: **PD-T086** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T. Aliases: smaller mixed-axis matrix; Cartesian-row kernel reduction.
Split from: none. Split into: none.

## Statement

Let K be any field and n>=1. Let x0,...,xn be distinct. On row i choose q_i distinct y roots, with0<=q_i<=n+1 and `sum_i q_i=N=binom(n+2,2)`. Let `Q_i(y)=prod_(selected row roots)(y-root)`, with Q_i=1 if q_i=0, and coefficients q_(i,s) interpreted as0outside0<=s<=q_i. Put M=n(n+1)/2. Define the M-by-M matrix B with rows `(b,t)` for1<=b<=n,0<=t<b and columns `(i,r)` for0<=i<=n,0<=r<=n-q_i, by

`B_((b,t),(i,r))=x_i^t*q_(i,b-r)`.

Then the N selected nodes are unisolvent for Pi_n if and only if det B!=0. This is a complete mixed-axis criterion valid over every field. At n2 with q_i=2 it reduces, up to row order/sign, to the three root-sum criterion PD-T?lattice-c1-codex-01. For the mod4 families at cardinality-matching degrees, every q_i<=n+1, so the reduction applies directly. It does not assert that B is nonzero for those families at all degrees or at Chebyshev labels.

## Definitions, assumptions and status

Distinctness is within each row's y roots; different rows may share y labels. All weights used below exist because x are distinct. The column count is `(n+1)^2-N=M`, so B is square. Overall status PROVED (developer complete proof; independent Astra reconstruction pending). No novelty claim: this is an elementary row-interpolation/divided-difference framework, with the bounded literature coverage in C1/candidates.md.

## Depends on

Elementary univariate Lagrange interpolation and the leading-coefficient identity proved below. No charter or unread literature dependency.

## Proof

Write `w_i=1/prod_(j!=i)(x_i-x_j)`. For any p(x) of degree<=n, `sum_i w_i*p(x_i)` is the x^n coefficient, by the Lagrange formula. More generally p has degree<=n-b if and only if `sum_i w_i*x_i^t*p(x_i)=0` for every0<=t<b. Sufficiency follows inductively: t0 removes the leading coefficient; once p has degree<=n-t, the tth identity is the leading-coefficient identity for x^t*p of degree<=n, removing its coefficient of degree n-t. Necessity follows because x^t*p then has degree<n.

Any f in Pi_n that vanishes at all selected nodes has row restrictions `f(x_i,y)=Q_i(y)g_i(y)` with deg g_i<=n-q_i. Conversely choose any such g_i and interpolate the row polynomials in x by the unique degree<=n Lagrange interpolant F(x,y). It has degree<=n in each variable, and it vanishes at all selected nodes. Its y^b coefficient p_b(x) has degree<=n-b exactly when the previous paragraph's b weighted moments vanish. All conditions with b>=1 together enforce total degree<=n; b0needs no condition. Those conditions are

`sum_(i,r) w_i*g_(i,r)*x_i^t*q_(i,b-r)=0`, for1<=b<=n,0<=t<b.

Rescale free unknowns by h_(i,r)=w_i*g_(i,r), a bijection because w_i!=0. This is precisely B*h=0. The row interpolation map from g to F is injective: zero F has zero restrictions, and nonzero Q_i in K[y] cannot annihilate g_i. Hence ker B is isomorphic to the kernel of Pi_n evaluation. The two square evaluation dimensions agree, so evaluation is bijective exactly when B is invertible.

At n2,q_i2, the free columns are one per row and Q_i coefficients at y1,y2 are-s_i,1. The rows of B are `(-s_i)_i`, `(1)_i`, `(x_i)_i`; their determinant differs only by a sign from det of rows(1,x_i,s_i), proving the claimed reduction.

## Checks, sources and scope

The n3 symbolic/exact calculation is recorded separately in C1/symbolic.json after execution; it is not load bearing for this general proof. All-field criterion uses axis-root polynomial coefficients and x powers, not a tautological re-evaluation of the full N-by-N Vandermonde. Its matrix is smaller, with no pairwise-node evaluations. Existing multiline interpolation frameworks are close predecessors; no publication novelty claim. Properties: periodicity only for the mod4 application; complete structural criterion yes; no Lebesgue conclusion.

## Open items and history

For the specific periodic families the next task is det B nonvanishing or an explicit counterexample across n, and a useful inverse bound for stability. These remain OPEN. Independent reconstruction pending.2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f; round7frozen before derivation.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
