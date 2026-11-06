# PD-T?padua-3d-codex-T5-02 — Chebyshev section commutator ranks

ID kind: PD-T.
Aliases: exact truncated multiplication census; standard commuting-extension bound.
Split from: none. Split into: none.

## Statement

For normalized product arcsine measure on `[-1,1]^d`, let `A_i` be coordinate
multiplication compressed orthogonally to total-degree polynomials `Pi_q`,
`q>=0`. Every pair `i!=j` has

`rank[A_i,A_j] = 2 floor((q+1)/2)` for `d=2`, and

`rank[A_i,A_j] = 2 floor((q+1)^2/4)` for `d=3`.

If real symmetric matrices of size `N` extend all these sections and commute,
then, writing `r=dim Pi_q`,

`N >= r + rank[A_i,A_j]/2`.

Consequently every positive cubature exact through degree `2q+1` satisfies
that same lower bound. In the cube this gives `N>=5,12,24,41` for degrees
`3,5,7,9`, respectively.

## Definitions

The measure is `pi^(-d) product_i (1-x_i^2)^(-1/2) dx_i`. Orthonormal
one-dimensional polynomials are `p_0=1`, `p_k=sqrt(2) T_k` for `k>0`.
Their recurrence coefficients are `c_0=1/sqrt(2)` and `c_k=1/2` for `k>=1`:
`x p_k = c_k p_(k+1) + c_(k-1) p_(k-1)` with the negative-index term absent.
The tensor basis is restricted by total degree. The commutator is `AB-BA`.

## Assumptions

Exact real arithmetic; orthogonal compression for this precise measure.
The completion bound assumes real symmetric extensions. The cubature
corollary assumes strictly positive weights after removing zero weights,
arbitrary real nodes, and exactness on every polynomial of degree `<=2q+1`.
No symmetry of the nodes is assumed.

## Status by part

Overall status: PROVED, by the hand argument below.
Candidate disposition: retained specialized evaluation of a known mechanism.
No novelty or sharpened Möller/Degani bound is claimed. The repository's
IDEA-207 already records the corresponding floating 3D ranks.

## Depends on

Elementary orthogonality and finite-dimensional linear algebra. The boundary
identity is also PD-T097. No source digest is used as a proof dependency.

## Checks

`python topics/padua-3d-20261106/code/t5_exact.py --output
topics/padua-3d-20261106/evidence/t5-exact.json` was executed with Python
3.12.14 / SymPy 1.14.0. Exact rational matrices for d=2,3 and q=0..4 agree.
These checks are corroboration, not a finite computational premise of the
proof. Independent actual replay of the code is PENDING.

## Sources

Predecessor pointers: IDEA-207; literature records
`literature/records/degani-schiff-tannor-2005.md` and
`literature/records/dunkl-xu-2014.md`. The extension bound is the familiar
DST/Möller mechanism, reconstructed here. This worker did not complete a
primary fulltext read of either source and does not import their theorems.

## Proof or evidence

First take d=2. The full multiplication operators commute. If P is the
orthogonal projection to `Pi_q`, the commutator of their compressions is
minus the skew product of the two maps from `Pi_q` to its next-degree
orthogonal layer. Both maps vanish on `Pi_(q-1)`. Thus the commutator is
supported only on the degree-q block. Label that block by
`e_a=p_a(x)p_(q-a)(y)`, `a=0,...,q`.

The x-boundary map takes `e_a` to
`c_a p_(a+1)(x)p_(q-a)(y)`; the y-boundary map takes it to
`c_(q-a) p_a(x)p_(q-a+1)(y)`. Their cross products match exactly when
the labels differ by one. The commutator block is therefore a skew
tridiagonal path of size `q+1`, with consecutive nonzero edge magnitudes
`c_a c_(q-a-1)`, `a=0,...,q-1`. No zero edge occurs.

A skew tridiagonal path of even size L has determinant equal to the product
of the squares of its odd-numbered edges, by expanding successively at an
end. It is invertible. For odd L its determinant is zero by skew symmetry,
and its leading principal submatrix of size L-1 is invertible. Hence its
rank is `2 floor(L/2)`. This includes L=1 and proves the 2D formula.

For d=3 and the pair x,y, split by the spectator z-degree `k=0,...,q`.
Both compressed operators preserve each such subspace, and on it they
are the two-dimensional sections at degree `q-k`. The commutator is a
direct sum. Its rank is

`sum_(m=0)^q 2 floor((m+1)/2) = 2 floor((q+1)^2/4)`.

Permutation of coordinates gives every pair.

For the extension bound write a symmetric extension in blocks
`Atilde_i=[[A_i,B_i],[B_i^T,D_i]]`, where B has `s=N-r` columns.
Its top-left commutativity equation reads
`[A_i,A_j]=B_j B_i^T-B_i B_j^T`. The right side has rank at most `2s`.
This proves the bound; no bottom-block or compatibility equation has
been solved.

For a positive cubature let V have entries `sqrt(w_l) p_alpha(x_l)`,
with `|alpha|<=q`. Degree-2q exactness gives `V^T V=I_r`.
Degree-(2q+1) exactness gives `A_i=V^T diag(x_(l,i)) V`.
Complete V to an orthogonal matrix in R^N. Conjugating the commuting
real diagonal node matrices by it gives commuting symmetric extensions
with the required top-left blocks. Applying the preceding bound proves
the cubature corollary.

## Scope

This is a necessary node bound. It neither proves attainability nor excludes
positive near-Gaussian cubature at larger node counts. It is below
`dim Pi_(q+1)` at all four listed degrees. Noncommutation of the original
sections excludes only zero-surplus (Gaussian) completions; it does not
exclude near-Gaussian rules. No universal Li–Sun–Xu conclusion follows.

## Open items

The compatibility equations and the least possible completion size remain
unresolved. A minimization of completed-section commutator norms is a
separate nonlinear problem and was not run. No global or local minimizer
is claimed. General minimal cube cubature remains OPEN.

## History

2026-11-06: Codex, gpt-6.1-sol xhigh, rules at
`ccd9e905d19c0c625c196c4a3f3e707058ed042a`; exact reproduction and hand
specialization. The known mechanism is explicitly preserved as predecessor.
