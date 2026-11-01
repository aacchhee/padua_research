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

whose two indices are `(1,1)` and hence have even sum. Positivity is on the full balls in R^2, as in PD-T075. The explicit witness lies in the open square `(-1,1)^2` for every n>=4: since `0<t_n<=a/256<0.27`, both angles `pi/n+t_n` and `pi/(n+1)+t_n` lie in `(0,pi)`, so both cosines lie in `(-1,1)`. Consequently the theorem holds verbatim when `K_delta(n)` is replaced by `K_delta(n)∩[-1,1]^2`. The square-restricted radius `rho_n^sq=sup{delta>=0 : P_n>=0 on K_delta(n)∩[-1,1]^2}` satisfies `rho_n<=rho_n^sq<=|zeta_n-z_n|_2` whenever `P_n(zeta_n)<0`, hence also `limsup n^5 rho_n^sq<=20*sqrt(2)*pi^4/9`; the bound for rho_n follows from it. (Minor routine extension, PROVED by the same argument; response-01, audit-01 E5-F4.)

## Assumptions

Exact real arithmetic. No assumption about weights, Padua unisolvence, floating-point runs, section consistency, or other obstruction certificates is used.

## Status by part

Overall status: PROVED (written analytic proof; independent reconstruction completed; external Claude audit-01 CONFIRMED, `topics/padua-lanczos-drift-20261101/checks/audit-01/E5-records-30-32.md`; editorial items E5-F3/F4/F8 applied in response-01, Codex re-audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit negative limiting coefficient | PROVED | Elementary fixed-order Taylor proof below |
| Eventual negative witnesses and rho_n=O(n^-5) | PROVED | Limit and explicit distance to z_n |
| Minor routine corollary (response-01): general increment a/n^4 and the sharper constant `2*sqrt(2)*pi^4*(10-2*sqrt(2))/9` | PROVED (same argument; excluded from aggregation; pending Codex re-audit) | Remark "General common increment a/n^4" below |

Candidate disposition: IDEA?drift-codex-30 retained as a quantitative variant of PD-T069/PD-T075. No historical novelty claim.

## Depends on

Only the definitions of P_n and rho_n from PD-T069/PD-T075. The positive node-Hessian theorem in PD-T069 is not needed for this upper bound (it separately shows rho_n>0 for each fixed n).

## Checks

The proof below is analytic and does not depend on a finite computer check. A developer SymPy expansion first suggested the scaling; its role was discovery only. `python3 -I -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py`: PASS (Python 3.12.14, SymPy 1.14.0), output `topics/padua-lanczos-drift-20261101/evidence/e5-exact-checks.json`; hashes/provenance in `e5-manifest.json` beside it. Exact coverage of that script: it enters f with free angles alpha, beta in place of m*theta, m*phi, i.e. already after the node reduction `n*theta=(n+1)*phi=pi`. It checks (i) the first-derivative formula, (ii) its sine-addition form, (iii) the second-derivative formula, (iv) only that n^3 times the displayed cubic `-(2n+1)m^3 pi^3/[3n^2(n+1)^2]` tends to `-(2/3)m^3 pi^3`, and (v) the expansion `(9/2)r^2-30r+46`, its value -4 at r=10/3 and `-4B^2=-6400pi^12/729`. It does **not** check the node reduction itself, that `-(k^3-k)(md)^3/12` equals the displayed cubic or is the leading term of D with an O(n^-5) remainder, the third-derivative/Taylor remainder bound, the n^-7 generator limits, or the distance limit. Those steps rest on the written proof. They were independently reconstructed by the independent checker (`topics/padua-lanczos-drift-20261101/checks/independent-math-01.md`) and by audit-01 (E5 cmd 4, `checks/audit-01/scripts/E5/a_series.py`: raw-definition node reduction, exact h=1/n series of g_m and P_n through h^14, distance limit). No computer-assisted proof is claimed.

The parent's distinct `independent_math_check` agent independently reconstructed both derivative identities, the n^-7 generator limit, the negative quadratic coefficient, and the distance/radius implication with no gap reported. It separately executed 100-digit numerical corroboration for n=10..3000, recorded with its own code/input hashes in the parent-owned independent-check record; those finite values are corroboration, not a finite threshold or the universal proof. External Claude audit-01 reconstructed the proof by hand and by exact series and CONFIRMED it (`topics/padua-lanczos-drift-20261101/audit-01.md`).

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

### Remark: general common increment a/n^4 (minor routine corollary; Claude response-01, audit-01 E5-F8)

For a fixed real a put `t_n(a)=a/n^4` and `zeta_n(a)=(cos(pi/n+t_n(a)),cos(pi/(n+1)+t_n(a)))`. In the proof above the value of a enters only after the display of the n^7 generator limits: `D_(n,m)` and `f''_(n,m)(0)` do not involve a, and the remainder bound is `[n^3+(n+1)^3]|a|^3/(6n^12)=O(n^-9)` for each fixed a. Hence, for every fixed real a,

`n^7 g_m(zeta_n(a)) -> -(a^2+B m^3)`, `B=(2/3)a*pi^3`, `0<=m<=3`.

The quadratic expression defining P_n is homogeneous of degree two in the four generators, so, by the same expansion as above,

`lim n^14 P_n(zeta_n(a)) = (9/2)a^4-30a^2 B+46B^2 = a^2(81a^2-360pi^3 a+368pi^6)/18`.

For a<=0 every term of the middle expression is >=0, so these paths give no witness. For a>0 write `a=(2/3)pi^3 r`, so that `a^2=Br`; the limit is `B^2((9/2)r^2-30r+46)`. It is strictly negative iff `r` lies in `(10/3-2sqrt(2)/3, 10/3+2sqrt(2)/3)`, i.e. iff `a` lies in `(a_-,a_+)`, `a_(±)=(4pi^3/9)(5∓sqrt(2))` (approximately 49.414 and 88.392). The vertex r=10/3 is the a=20pi^3/9 of the Statement. For each such a, `zeta_n(a)` is a negative point for all sufficiently large n, and the mean-value argument above gives `n^5|zeta_n(a)-z_n|_2 -> sqrt(2)*pi*a`. Hence `limsup n^5 rho_n <= sqrt(2)*pi*a` for every `a` in `(a_-,a_+)`. Letting a decrease to a_- gives

`limsup_(n->infinity) n^5 rho_n <= sqrt(2)*pi*a_- = 2*sqrt(2)*pi^4*(10-2*sqrt(2))/9 = (4pi^4/9)(5sqrt(2)-2) ≈ 219.54`,

which sharpens the constant 306.13 of the Statement. The same bound holds for the square-restricted radius: `0<t_n(a)<=a_+/256<0.35` for n>=4, so `zeta_n(a)` lies in `(-1,1)^2`. Status: PROVED, as a minor routine corollary of the proof above. It is not used elsewhere, and it is excluded from the file's status aggregation. The infimum is not attained by this argument: at `a=a_-` the n^-14 coefficient vanishes and the sign is decided by higher-order terms, which are not analysed. No optimality is claimed, either within this one-parameter family or among other witnesses. Corroboration, not proof: `tracks/bivariate-lanczos/code/drift/response01_e5_checks.py`, output `topics/padua-lanczos-drift-20261101/evidence/response-01-e5-checks.json` (PASS). Part A checks exactly, with symbolic a, the factorisation of the limit quadratic, an independent h=1/n series of P_n(zeta_n(a)) whose h^0..h^13 coefficients vanish and whose h^14 coefficient equals the formula, the roots, and the constant. Part C (MEASURED, 120 digits) gives n^14 P_n/limit = 1.00699 at a=1.01a_- and 1.00497 at a=0.99a_+, both at n=10^5. Audit-01 E5 cmd 4 obtained the same general-a limit independently.

## Scope

This settles only PD-T075(U1), for its named certificate P_n. It does not bound `delta_obs(n)` from above: `rho_n<=delta_obs(n)` is a lower comparison for the optimal obstruction radius. Other polynomials of degree <=2n+1 could remain nonnegative on larger neighborhoods. In particular no conclusion about `inf_(n>=3) delta_obs(n)` follows from this proof. The per-degree exact-section obstructions PD-N020/PD-N022 remain valid. Reading (G), actual rounding directions, nonexact residuals, and any rate for the best certificate remain unresolved here.

## Open items

- External Claude audit-01: CONFIRMED (E5 auditor reconstruction; editorial items applied in response-01). Codex re-audit of the response-01 edits pending.
- Optional explicit finite threshold N for negativity at every n>=N; existence of N is proved by the strictly negative limit and no numerical threshold is assumed.
- A matching lower rate for rho_n, or sharper upper witnesses. Within the common-increment family a/n^4 the constant improves to `2*sqrt(2)*pi^4*(10-2*sqrt(2))/9≈219.54` (Remark "General common increment a/n^4", PROVED minor corollary). Unequal increments, the endpoint a=a_-, and other corner nodes are unexplored.
- PD-T075(U2), uniformity for all possible obstruction certificates.

## History

2026-11-01, Codex E5 developer, requested gpt-6.1-sol xhigh; rules/base `806cc7b4509fd93bae652f9545d32d95529f8281`. New analytic subresult split from the original U1 target. Generated outputs are not used as proof. No Git or shared-registry mutation by this worker.
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F4. Definitions: the witness lies in (-1,1)^2 for every n>=4, and the theorem holds verbatim for K_delta(n)∩[-1,1]^2. Original wording: «Positivity is on the full balls in R^2, as in PD-T075, although the explicit witness itself lies in the square for all sufficiently large n.».
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F3. Checks: exact coverage of e5_exact_checks.py stated, with what it does not check, and citations of the independent checker and audit-01 for the rest. Audit status metadata updated (audit-01 CONFIRMED). Original wording: «`python3 -I -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py` exactly checks the derivative identities and limiting quadratic: PASS …»; «Overall status: PROVED (written analytic proof; independent reconstruction completed; external Claude audit pending).»; «External Claude audit remains pending.»; Open item «Required external Claude mathematical audit; the supplementary independent reconstruction found no gap.».
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F8 (optional). Added the Remark "General common increment a/n^4" with written proof, and a status row labelled as a minor routine corollary excluded from aggregation. The main Statement and its constant are unchanged. The Open item on sharper witnesses is extended. Original wording: «- A matching lower rate for rho_n, or sharper upper witnesses.».
