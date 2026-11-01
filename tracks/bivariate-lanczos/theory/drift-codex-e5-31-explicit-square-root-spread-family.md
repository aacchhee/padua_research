# PD-T?drift-codex-31 — An explicit square-case family with square-root support spread and residual constants

ID kind: PD-T.
Aliases: E5 square sqrt(epsilon) case; four-atom split of a three-node measure; residual-aware construction.
Split from: none; concrete refinement/example of the PD-T059/PD-T061 square-root mechanism, not a solution of PD-T056 reading (G).
Split into: none.

## Statement

Let `Z={(0,0),(1,0),(0,1)}`, `mu=(delta_(0,0)+delta_(1,0)+delta_(0,1))/3`, and `V=Pi_3`. Give `V*` the maximum absolute monomial-moment norm (monomials `x^a y^b`, `a+b<=3`), dual to the coefficient l1 norm on V. For `0<epsilon<=1/300`, put `t=sqrt(3*epsilon)` and define the unit-mass positive measure

`mu_epsilon = delta_(t,t)/6 + delta_(-t,-t)/6 + delta_(1,0)/3 + delta_(0,1)/3`.

Then:

1. `||L_(mu_epsilon)-L_mu||_infinity=epsilon` exactly. Its exact degree-1 sections are defined, consistent, and noncommuting. The measure is supported within `sqrt(6*epsilon)` of Z.
2. For every unit-mass positive measure nu supported within `delta<=1` of Z, if

   `||L_nu-L_(mu_epsilon)||_infinity<=gamma*epsilon`, `0<=gamma<1/3`,

   then `delta>=sqrt((1-3*gamma)*epsilon/3)`.

Thus this explicit family has minimal exact support spread comparable to sqrt(epsilon), and the lower order persists under the stated smaller residual allowance. For allowance epsilon, the original mu itself has delta=0 and residual exactly epsilon.

## Definitions and assumptions

Exact arithmetic; degree n=1, so the original measure has the square count `M=N_1=3`. Support proximity means inclusion in the union `K_delta(Z)` of closed Euclidean balls, not a fixed number of new atoms. All residuals use the fixed-mass functional convention (R2) of PD-T058, with mass one. A statement about all small consistent perturbations is not made.

## Status by part

Overall status: PROVED (explicit analytic construction and inequalities; independent reconstruction completed; external Claude audit-01 CONFIRMED, `topics/padua-lanczos-drift-20261101/checks/audit-01/E5-records-30-32.md`; editorial items E5-F3/F7 handled in response-01, Codex re-audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact epsilon perturbation and positive four-atom representation | PROVED | Direct moments below |
| Noncommuting consistent sections | PROVED | Explicit Gram/multiplication matrices below |
| Lower spread under residual gamma*epsilon, gamma<1/3 | PROVED | Double-zero cubic and uniform local bound |

IDEA?drift-codex-31: retained explicit reading-(E) instance of the known square-root mechanism. Closest predecessor PD-T061 (IDEA-157); PD-N021 (IDEA-161) is the related δ=O(ε) refutation. The deferred (G) realization is the separate candidate IDEA?drift-codex-35 (deferred, `topics/padua-lanczos-drift-20261101/ideas-e5.md`). The general finite-precision (G) target remains OPEN; no novelty claim.

## Depends on

Definitions of exact sections and residual conventions from PD-T057/PD-T058. The construction and support bound below are direct and do not rely on the abstract existence theorem PD-T061.

## Proof

For a monomial of degree <=3, replacing the mass 1/3 at the origin by the two masses 1/6 at `(t,t)` and `(-t,-t)` changes exactly the three degree-two moments `x^2`, `xy`, `y^2`, each by `t^2/3=epsilon`. Constants, degree-one moments, and degree-three moments are unchanged. This proves the exact moment norm assertion. The split atoms have distance `sqrt(2)*t=sqrt(6*epsilon)` from the origin; the other atoms are in Z.

In the ordered polynomial basis `(1,x,y)`, write `e=epsilon`. The Gram matrix M and coordinate-weighted Gram matrices X,Y are

```
M = [[1,   1/3,     1/3],
     [1/3, 1/3+e,   e  ],
     [1/3, e,       1/3+e]],

X = [[1/3,   1/3+e, e],
     [1/3+e, 1/3,   0],
     [e,     0,     0]],

Y = [[1/3, e, 1/3+e],
     [e,   0, 0    ],
     [1/3+e,0,1/3  ]].
```

M is positive definite: its leading minors are `1`, `2/9+e`, and `(1+18e)/27`, all positive. The matrices `A=M^(-1)X` and `B=M^(-1)Y` represent the two projected multiplication operators in this basis. The exact symmetric orthonormal sections are simultaneously similar to A,B via the Cholesky factor of M, so they commute exactly when A,B commute. Direct multiplication gives

`[A,B]_(0,1) = 3e(12e-1)/(1+18e)^2`,

which is nonzero for `0<e<=1/300`. Since these sections come from the displayed positive measure, they satisfy all exact consistency conditions.

For the lower bound use

`p(x,y)=xy(1-x-y)=xy-x^2 y-xy^2`.

The polynomial p and its gradient vanish at every point of Z. The direct moment calculation gives `L_(mu_epsilon)(p)=epsilon`. Moreover

`|p(x,y)|<=3*delta^2` on `K_delta(Z)`, `0<=delta<=1`.

Indeed, near the origin `|xy|<=delta^2/2` and `|1-x-y|<=1+sqrt(2)*delta<=3`. Near `(1,0)` write `x=1+u`, `y=v`, `u^2+v^2<=delta^2`; then `p=-(1+u)v(u+v)`, whose absolute value is at most `(1+delta)*delta*sqrt(2)*delta<=2sqrt(2)*delta^2<=3delta^2`. The argument near `(0,1)` is the same with x and y exchanged.

The coefficient l1 norm of p is 3, hence the assumed functional residual gives

`L_nu(p)>=epsilon-3*gamma*epsilon=(1-3gamma)*epsilon`.

Positivity and unit mass imply `|L_nu(p)|<=3delta^2`. Combining the two inequalities proves the lower bound. Finally mu has moment residual epsilon by the first calculation and has support radius zero.

## Checks

Developer exact symbolic multiplication of the displayed rational matrices confirms `det M=(1+18e)/27` and the displayed commutator entry. This is an elementary identity displayed for direct checking, not a finite computer-assisted proof. `python3 -I -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py`: PASS (Python 3.12.14, SymPy 1.14.0). Exact coverage for this record: M, X, Y are typed into the script as the displayed rational matrices, not built from the atoms. The script checks `det M=(1+18e)/27` and `[A,B]_(0,1)=3e(12e-1)/(1+18e)^2` for those typed-in matrices. Its "moment" check covers only the origin split: at a formal displacement t, the moment differences between the two split atoms and the original origin atom are `t^2/3` in degree two and 0 otherwise. It does **not** check that the displayed M, X, Y are the moment matrices of mu_epsilon, the cubic jets of p on Z, `L_(mu_epsilon)(p)=epsilon`, or the local bound. Those rest on the written proof. They were checked by the independent checker (it built M, X, Y from the four atoms; receipt `moment_matrices_built_from_four_atoms: True`, paragraph below) and by audit-01 (E5 cmd 6, `topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E5/c_square.py`, which found float grid sup|p|/δ²≈1.8≤3). Evidence and hashes are in `topics/padua-lanczos-drift-20261101/evidence/e5-exact-checks.json` and `e5-manifest.json`.

The parent's distinct independent mathematical checker constructed all moments afresh from the atoms, formed M,X,Y from their monomial exponents, and separately verified the determinant, commutator entry, double-zero cubic jets, and `L_(mu_epsilon)(p)=epsilon`: PASS. It reconstructed the local bound and residual argument with no gap. Its code/output/input hashes belong to the parent-owned independent-check record. External Claude audit-01 reconstructed the construction and bounds and CONFIRMED them.

## Sources

Internal predecessors PD-T059/PD-T061 (square-root rate; PD-T061 is the closest, with abstract constants and Open item "Explicit constants") and PD-T058 (residual conventions). PD-N021 (IDEA-161) refutes δ=O(ε) in reading (E) for every square unisolvent set. This record is one explicit instance consistent with it, not a new refutation. No external theorem is imported. Literature comparisons make no historical novelty claim.

## Scope: what this says about (E) and (G)

This is a specified consistent data family in reading (E), with an explicit positive measure, atoms, spread, norm, and residual constants. It does not assert that this family is produced by a floating-point Padua/Lanczos run. Its local recurrence residual relative to the original multiplication operators has not been bounded by a smaller roundoff parameter u. Taking `u=epsilon` and allowing an unspecified constant in O(u) makes mu itself an admissible approximation with radius zero. Taking `u=o(epsilon)` would make the lower support bound informative, but realizing the family with local computed-recurrence errors of that smaller size is a separate unproved obligation. The residual lower constant here is 1/3, not an unspecified O(1) prohibition. This explicit test therefore does not promote the known (E) square-root mechanism into a (G) theorem.

## Open items

External Claude audit-01 completed (CONFIRMED). This instance supplies explicit constants for one family only. It does not give the universal constants c, C of PD-T061. A genuine (G) construction or obstruction must specify actual computed/formed data, their consistency or correction residual, the local roundoff parameter u, and a nontrivial residual constant. PD-T056 reading (G), including Padua n=3/4, remains OPEN.

## History

2026-11-01, Codex E5 developer, requested gpt-6.1-sol xhigh; rules/base `806cc7b4509fd93bae652f9545d32d95529f8281`. New explicit family and residual-aware proof, within assigned square sqrt(epsilon) alternative. No Git/shared-registry change.
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F3. Checks state the developer checker's exact coverage, with what it does not check, and cite the independent checker and audit-01 for the rest. Audit status metadata updated. Original wording: «`python3 -I -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py` verifies the moments, Gram determinant, commutator entry, and the corner derivative identities of PD-T?drift-codex-30: PASS …»; «… external Claude audit pending).»; «External Claude audit remains pending.»; «Required external Claude mathematical audit.».
- 2026-11-01 (Claude response-01, Opus 5.5 high): audit-01 E5-F7/P-F7. Named PD-T061/IDEA-157 as closest predecessor and PD-N021/IDEA-161 as related. The deferred (G) candidate is split off as IDEA?drift-codex-35. Mathematics unchanged. Original wording: «IDEA?drift-codex-31: retained concrete variant of the known square-root mechanism. The general finite-precision (G) target remains OPEN; no novelty claim.»; «Internal predecessors PD-T059/PD-T061 (square-root rate) and PD-T058 (residual conventions).».
