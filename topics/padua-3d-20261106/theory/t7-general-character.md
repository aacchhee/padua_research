# PD-T?padua-3d-20261106-codex-T7-01 — general finite-coset character dictionary

ID kind: PD-T. Aliases: general-H folded Fourier factorization.
Split from: none. Split into: none. Supports the T7 target, which remains OPEN.

## Statement and assumptions

Use turns: T^d=(R/Z)^d and c(t)=(cos(2πt_j))_j. Let H≤T^d
be any finite subgroup, a any real phase, L={u∈Z^d:u·h∈Z for all
h∈H}, and G=Z^d/L. For I_n={α∈N_0^d:|α|_1≤n}, define

    B[r,α] = Σ_{ε∈{−1,1}^d: [εα]=r} exp(2πi(εα)·a), r∈G.

Signs at zero coordinates are repeated in this sum. Evaluation of the
product-Chebyshev basis on X=c(a+H) has the same rank as B, over C.
Its real evaluation rank has that same integer value. Thus evaluation is
injective iff B has |I_n| independent columns. No cyclicity, rationality
of a, or coordinate reflection symmetry is assumed.

## Status by part

Overall status: PROVED (written proof below; no novelty claim).

| Part | Status | Evidence |
|---|---|---|
| Character factorization and rank equivalence | PROVED | Finite character orthogonality below |
| Rational integer zero-phase implementation | PROVED as an identity | Last paragraph of proof; finite replay separately MEASURED |

## Depends on / sources

Elementary finite abelian character orthogonality, proved below. This is
the general-H version of [T3 cyclic rank](t3-cyclic-rank.md), not a new
interpolation mechanism. Literature comparison and coverage limits are
in [literature-T7](../literature-T7.md). No published theorem is imported.

## Proof

Every character of H is the restriction of an integer torus character.
For completeness, write the full-rank annihilator lattice in Smith form
by integer row and column operations. These operations identify
Z^d/L with a product of cyclic groups; its dual has precisely the
solutions of Lh⊂Z. The original H is contained in that dual. Equivalently,
start with a common denominator for the finite group and use finite
cyclic character orthogonality: annihilating twice recovers H. Therefore
G indexes all |H| distinct characters of H.

Let F[h,r]=exp(2πir·h), h∈H. For r≠s the character r−s is
nontrivial on H: select h_0 with its value different from 1. Translating
the sum over H by h_0 proves Σ_h exp(2πi(r−s)·h)=0. On the diagonal
the sum is |H|. Consequently F*F=|H|I and F is invertible.

With T_α(x)=∏_j T_{α_j}(x_j), expand each cosine into two exponentials:

    V_H[h,α] = T_α(c(a+h)) = 2^(−d) Σ_r F[h,r] B[r,α].

Hence V_H=2^(−d)FB. Replacing its repeated identical rows by one row
per distinct node gives V_X and preserves the kernel and rank. A real
matrix has equal real and complex ranks, for example by its nonzero
minors. Product-Chebyshev polynomials form a basis of Π_n by their
triangular nonzero leading terms, so this also proves the assertion for
polynomial evaluation, independently of basis choice.

At a=0 the entries of B are integers. Rows r and −r are identical:
ε↦−ε is a multiplicity-preserving bijection. Pairing these rows and
summing their entries multiplies a paired row by 2 and leaves any
self-inverse row unchanged, preserving rank. The code evaluates each
character on a supplied generating list of H, which identifies its
class exactly; it uses precisely this paired integer dictionary.

## Checks and scope

[t7_cosets.py](../code/t7_cosets.py) first reproduces inherited T2/H39,
Padua n≤10 and the full invariant T1 n=2,3 control. Commands and actual
hashes are in [T7 attempts](../attempts/T7.md) and the small receipt.
Those computations validate an implementation; this proof does not
depend on a finite census. Arbitrary-phase B is generally complex and
must not be replaced by the zero-phase integer dictionary.

## Open items / history

The all-coset minimal-node census and a degree-uniform 3-D family remain
OPEN. 2026-11-06, Codex, assigned gpt-6.1-sol xhigh, rules e5b6445;
runtime model metadata is not exposed. Provisional ID.
