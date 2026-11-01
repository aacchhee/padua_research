# Supplementary independent checks

- Source/rules/base SHA: `cadb35066160e466cb1704b9791ad6f374446422`.
- Checker: Codex supplementary agent `/root/input_review`, assigned `gpt-6.1-sol xhigh`; runtime-resolved model/effort metadata is not separately exposed.
- This is an actual separate rerun and code inspection, not the required Claude (Opus 5.5 xhigh) audit or an approval for merge.

## A1 exact symbolic regression

Inspected `code/a1_exact_check.py` in full before executing it. Executed separately from the developer, from `/workspace/padua_research`:

```text
python topics/padua-proof-attempts-20261101/code/a1_exact_check.py > topics/padua-proof-attempts-20261101/outputs/a1_independent.json
```

The command completed with exit code 0 under Python 3.12.14 and SymPy 1.14.0. Deterministic exact arithmetic; no random seed or numerical tolerance. The independent process produced the output itself; it did not copy or inspect the developer output to establish a rerun.

| n | Nodes | Exact corner cardinal equalities | Rhombus Laurent monomials | Result |
|---|---:|---:|---:|---|
| 1 | 3 | 12 | 5 | PASS |
| 2 | 6 | 24 | 13 | PASS |
| 3 | 10 | 40 | 25 | PASS |
| 4 | 15 | 60 | 41 | PASS |
| 5 | 21 | 84 | 61 | PASS |
| 6 | 28 | 112 | 85 | PASS |

All 332 cardinal-value comparisons passed. Each degree constructs and exactly inverts the unscaled product-Chebyshev evaluation matrix independently of the kernel formula, checks its inverse, and compares every node's cardinal value at every corner with the weighted corrected kernel. It separately checks the rhombus-to-product-U identity by equality of integer Laurent coefficient counters. Thus the computed finite claims concern exact cardinal values and formal Laurent identities, stronger than numerical agreement of summed absolute values.

Inspected reduction details: the cyclotomic order is `2*n*(n+1)`; multiplying its primitive-root exponents by `n+1` and `n` gives the required x- and y-angle cosines. Equality in this abstract cyclotomic field holds in the embedding with primitive root `exp(2*pi*i/order)` used for the real nodes. The correction is `T_n(c_x)*(-1)^j`, and the endpoint weights use exact rationals. The Laurent transform is `(p,q) -> (p+q,q-p)` and correctly partitions the square into common-parity exponent grids of radii n and n-1.

No code finding was identified within this finite scope. The trusted computational dependencies are Python integer/rational arithmetic and SymPy's cyclotomic fields, polynomial arithmetic and exact `DomainMatrix` inversion. This reruns the developer's checker; it is not a separately implemented interpolation checker. It does not prove an all-degree claim by finite sampling, verify a primary-source attribution, or certify numerical evaluation errors.

Content identities at execution:

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| `code/a1_exact_check.py` | `e7ea17bc56e44214fdf4206c654fb1710e7a8d3ca194dcdc15390a066a7920b0` | 3736 |
| `outputs/a1_independent.json` | `f8cd6cfd027989bf4bb59ebaebd9040824b0763ef660db51b5046078f33e8f94` | 1875 |

## Written-proof inspection

Read `theory/proof-attempts-codex-01-padua-corner.md` in full at SHA-256 `07f596870c05388ea0219aac3309bd5b4c651e3c9d5390d9ae7b381b5c35af64`. No mathematical finding was identified in this supplementary inspection.

The local proof does not depend on importing a published proof or extrapolating the finite run. The discrete cosine Gram derivation correctly includes the alternating checkerboard term: its nonzero condition would force x-mode sum n and y-mode sum n+1, impossible at combined degree at most 2n. Its unique exceptional squared norm is the `(n,0)` mode. The square Gram identity therefore gives the cardinal normalization with precisely one unnormalized x-mode subtraction. The corner step correctly removes sine cross terms, and the rhombus transformation partitions all exponent pairs into the two common-parity square grids. The quotient extension `m*(-1)^((m-1)*ell)` at `ell*pi` matches that finite exponential sum, including n=1 and node corners.

This inspection covers the displayed mathematical reduction and its finite check. The developer reports primary inspection of CDMV 2008 §2, eqs. (1),(3), printed p.3 and third-family eqs. (6a–c), printed p.4, and Bos et al. 2006 Theorem 2/eqs. (6)–(9), printed pp.8–9. This checker reviewed the stated parity/orientation translation and its agreement with the proof's formulas, but did not fetch or independently read those primary sources. The source locators are therefore attributed to the developer's inspection rather than presented as this checker's verified reading. The required Claude audit remains pending.

## B5 exact rational witnesses and all-degree proof

Inspected `code/b5_exact_instances.py` and `theory/proof-attempts-codex-02-generic-commutant.md` in full, then independently executed:

```text
python topics/padua-proof-attempts-20261101/code/b5_exact_instances.py > topics/padua-proof-attempts-20261101/outputs/b5_independent.json
```

The command completed separately from the developer with exit code 0 under Python 3.12.14 and SymPy 1.14.0. Exact rational/integer arithmetic; deterministic nodes `(t,t^(n+1))`, `t=1,...,N`, equal weights `1/N`, no seed or tolerances. The run checks exact Vandermonde inversion, the rational monic LDL basis, positive squared norms, weighted self-adjointness, commutation, masks and unit monic multiplication pivots. Positive diagonal similarity yields the symmetric positive-pivot pair without representing radicals.

| n | N | Computed reduced rank | Patterned symmetric variables | Full map rank deduced from proof |
|---|---:|---:|---:|---:|
| 2 | 6 | 3 | 17 | 14 |
| 3 | 10 | 7 | 36 | 33 |
| 4 | 15 | 12 | 65 | 62 |
| 5 | 21 | 18 | 106 | 103 |
| 6 | 28 | 25 | 161 | 158 |

The directly computed rank is the rank `N-3` of the final `N-3` rows of `V^-1`. It is **not** a direct calculation of the full patterned commutator map. The proof identifies its nullspace with affine node-value vectors and hence with the full commutant; rank-nullity then deduces full rank `variables-3` and commutant dimension three. This distinction is correctly disclosed by the script and theory.

The all-degree argument has no finite-computation dependency. Distinct x coordinates and positive weights make the constant vector cyclic for H_x. Its commuting matrices are determined by their first columns; the H_y mask restricts that column to three entries, while I,H_x,H_y supply three independent possibilities by their positive leading pivots. The containment P_x⊆P_y is correct for the stated order. The explicit collision polynomial supplies density throughout the open unisolvent positive domain, avoiding any connectedness assumption. The generalized Vandermonde witnesses follow from the stated Rolle induction; their exponent distinctness is correct. The LDL similarity correctly replaces ordinary symmetry with D-self-adjointness while preserving support and rank. No finding was identified in these arguments or the exact script within the declared scope.

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| `code/b5_exact_instances.py` | `fb56be6166ce10ecae213cd1c4e169594a52b0a922058e52934b88ccd0edf18b` | 4144 |
| `outputs/b5_independent.json` | `251496a1a117054608dd55d32c7dfa5441c5af34cf7cb00d1f99ec0e9e80da02` | 5327 |
| `theory/proof-attempts-codex-02-generic-commutant.md` | `f3137551edfe3230919e271d497ffb56ab49b3035c3165bb2455512e5264b7d3` | proof size in manifest |

Trusted computation: Python exact integers and SymPy rational matrices, LDL factorization and `DomainMatrix` inversion/rank. This is a separate execution of the developer checker, not a separately implemented checker or the required Claude audit. Repeated-x collision strata, other patterns and approximate commuting pairs are outside the theorem. No existing Padua counterexample was changed or invalidated.
