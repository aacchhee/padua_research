# PD-T?drift-codex-30 — An explicit corner witness gives rho_n = O(n^-5)

ID kind: PD-T.
Aliases: E5; common-angle corner perturbation; explicit negative witness for the Padua Turan certificate; U1 of PD-T075.
Split from: PD-T075, exact subquestion (U1) whether the positivity radius rho_n of P_n tends to zero.
Split into: none. PD-T075's separate uniform-obstruction question (U2) is not resolved here.

## Statement

Let n>=4 and let

`g_m(x,y) = T_(n-m)(x) T_m(y) - T_m(x) T_(n+1-m)(y)`, `0<=m<=3`,

`P_n = 9(g_1^2 - g_0 g_2/2) + g_2^2 - g_1 g_3`,

precisely as in PD-T069. Write `K_delta(n)` for the union of closed Euclidean delta-balls around the Padua nodes `(cos(j*pi/n),cos(k*pi/(n+1)))`, `j+k` even, and

`rho_n = sup{delta>=0 : P_n>=0 on K_delta(n)}`.

Put `a=20*pi^3/9`, `t_n=a/n^4`, and define the explicit point

`zeta_n = (cos(pi/n+t_n), cos(pi/(n+1)+t_n))`.

Then

`lim_(n->infinity) n^14 P_n(zeta_n) = -6400*pi^12/729 < 0`.

Consequently `P_n(zeta_n)<0` for all sufficiently large integers n, and

`limsup_(n->infinity) n^5 rho_n <= 20*sqrt(2)*pi^4/9`.

In particular `rho_n=O(n^-5)` and `rho_n->0`. This is an upper rate only: no matching lower rate or optimality of the exponent 5 is asserted.

## Definitions

`T_j(cos theta)=cos(j theta)` defines the Chebyshev polynomials. All limits are along positive integers n. The nearby Padua node used below is

`z_n=(cos(pi/n),cos(pi/(n+1)))`,

whose two indices are `(1,1)` and hence have even sum. Positivity is on the full balls in R^2, as in PD-T075, although the explicit witness itself lies in the square for all sufficiently large n.

## Assumptions

Exact real arithmetic. No assumption about weights, Padua unisolvence, floating-point runs, section consistency, or other obstruction certificates is used.

## Status by part

Overall status: PROVED (written analytic proof; independent reconstruction pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit negative limiting coefficient | PROVED | Elementary fixed-order Taylor proof below |
| Eventual negative witnesses and rho_n=O(n^-5) | PROVED | Limit and explicit distance to z_n |

Candidate disposition: IDEA?drift-codex-30 retained as a quantitative variant of PD-T069/PD-T075. No historical novelty claim.

## Depends on

Only the definitions of P_n and rho_n from PD-T069/PD-T075. The positive node-Hessian theorem in PD-T069 is not needed for this upper bound (it separately shows rho_n>0 for each fixed n).

## Checks

The proof below is analytic and does not depend on a finite computer check. A developer SymPy expansion first suggested the scaling; its role was discovery only. A small symbolic/measurement corroboration script and separate independent reconstruction are requested in the E5 direction record. No computer-assisted proof is claimed.

## Sources

Internal predecessors PD-T069 and PD-T075. No external source is used as a mathematical dependency. Literature/INDEX.md and the L3 source comparisons were consulted; historical novelty remains unclaimed.

## Proof

Fix `m` in `{0,1,2,3}`. Set `theta=pi/n`, `phi=pi/(n+1)`, and regard

`f_(n,m)(t)=g_m(cos(theta+t),cos(phi+t))`

as a function of the common angle increment t. Since `n*theta=(n+1)*phi=pi`, direct differentiation gives `f_(n,m)(0)=0` and

`D_(n,m):=f'_(n,m)(0)=(n+1)cos(m theta)sin(m phi)-n sin(m theta)cos(m phi)`.

Put `d=theta-phi=pi/(n(n+1))` and `k=2n+1`. The identity `theta+phi=k*d` and the sine addition formulas yield the exact identity

`D_(n,m) = [sin(k*m*d)-k*sin(m*d)]/2`.

Using `sin v=v-v^3/6+O(v^5)` in the first term, and the same expansion in the second term, gives

`D_(n,m) = -(k^3-k)(m*d)^3/12 + O(n^-5)`

`= -(2n+1)*m^3*pi^3/[3*n^2*(n+1)^2] + O(n^-5)`.

Here m is fixed; the remainder is valid because `k*m*d=O(n^-1)` and `k*(m*d)^5=O(n^-9)`. In particular

`n^3 D_(n,m) -> -(2/3)*m^3*pi^3`.

A second direct differentiation gives the exact formula

`f''_(n,m)(0) = -(2n+1-2m)cos(m theta)cos(m phi) - 2m sin(m theta)sin(m phi)`.

Thus `f''_(n,m)(0)/n -> -2`. This includes m=0, for which the formula is simply `-(2n+1)`.

For completeness, the Taylor remainder is uniform enough in n for the chosen scale. Each product of two cosines in the definition of f is the average of two cosines with frequencies whose absolute values are at most n for the first product and n+1 for the second. Hence, for all real t,

`|f'''_(n,m)(t)| <= n^3+(n+1)^3`

when n>=4 and `0<=m<=3`. Taylor's theorem therefore gives

`f_(n,m)(t_n)=t_n D_(n,m)+(t_n^2/2)f''_(n,m)(0)+R_(n,m)`,

`|R_(n,m)| <= [n^3+(n+1)^3]*t_n^3/6 = O(n^-9)`.

Multiplying by n^7, with `t_n=a/n^4`, proves

`n^7 g_m(zeta_n) -> -a^2 -(2/3)*a*pi^3*m^3`.

Write `B=(2/3)*a*pi^3=(40/27)*pi^6`. Since `a^2/B=10/3`, the four limits are `-B*(r+m^3)` with `r=10/3`. The quadratic expression defining P_n is continuous, and an elementary expansion gives

`9[(r+1)^2-r(r+8)/2]+(r+8)^2-(r+1)(r+27)`

`= (9/2)r^2-30r+46 = -4` at `r=10/3`.

It follows that

`n^14 P_n(zeta_n) -> -4*B^2=-6400*pi^12/729`.

The limit is strictly negative, so zeta_n is a negative point for every sufficiently large n. Its distance from the Padua node z_n satisfies

`n^5 [cos(theta+t_n)-cos(theta)] -> -a*pi`,

and the same limit holds with theta replaced by phi: this follows either from the mean value theorem or from `sin(theta)/theta ->1`. Therefore

`n^5 |zeta_n-z_n|_2 -> sqrt(2)*a*pi=20*sqrt(2)*pi^4/9`.

Whenever `P_n(zeta_n)<0`, P_n fails to be nonnegative on `K_delta(n)` as soon as `delta>=|zeta_n-z_n|_2`. Thus `rho_n<=|zeta_n-z_n|_2` eventually. This proves the stated limsup and O(n^-5) bound.

## Scope

This settles only PD-T075(U1), for its named certificate P_n. It does not bound `delta_obs(n)` from above: `rho_n<=delta_obs(n)` is a lower comparison for the optimal obstruction radius. Other polynomials of degree <=2n+1 could remain nonnegative on larger neighborhoods. In particular no conclusion about `inf_(n>=3) delta_obs(n)` follows from this proof. The per-degree exact-section obstructions PD-N020/PD-N022 remain valid. Reading (G), actual rounding directions, nonexact residuals, and any rate for the best certificate remain unresolved here.

## Open items

- Independent reconstruction of the two derivative identities, limiting coefficient, and distance bound.
- Optional explicit finite threshold N for negativity at every n>=N; existence of N is proved by the strictly negative limit and no numerical threshold is assumed.
- A matching lower rate for rho_n, or sharper upper witnesses.
- PD-T075(U2), uniformity for all possible obstruction certificates.

## History

2026-11-01, Codex E5 developer, requested gpt-6.1-sol xhigh; rules/base `806cc7b4509fd93bae652f9545d32d95529f8281`. New analytic subresult split from the original U1 target. Generated outputs are not used as proof. No Git or shared-registry mutation by this worker.
