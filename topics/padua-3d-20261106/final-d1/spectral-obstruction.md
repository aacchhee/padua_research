# PD-T?padua-3d-20261106-codex-D1-04 — eventual fixed excess for positive cube cubature

ID kind: PD-T. Aliases: D1 spectral obstruction; frontier C1; IDEA?padua-3d-20261106-claude-01.
Split from: none; this is the original Chebyshev C1 target, supported by separate D1-01/02/03 lemmas.
Split into: none. General doubling-weight extension remains a separate OPEN target.

## Statement and quantifiers

There exist gamma>0 and an integer n0>=1 such that, for every integer n>=n0 and every positive cubature rule on [-1,1]^3 exact on all real polynomials of total degree at most 2n-1 for normalized product Chebyshev measure,

    N >= (1+gamma) dim Pi_(n-1)^3
       = (1+gamma) binom(n+2,3)
       >= (1+gamma) n^3/6.

Here N is the number of distinct support nodes with nonzero weights. In particular no sequence of Padua-type positive rules with N=binom(n+3,3), degree-(2n-1) exactness and n->infinity exists. This conclusion uses only cubature and positivity, and does not assume Pi_n-unisolvence.

## Definitions and assumptions

The measure is product_j [dx_j/(pi sqrt(1-x_j^2))]. Nodes may lie on any cube face, edge or vertex. Weights are strictly positive after zero weights are removed, and sum to one by constant exactness. Nodes, phases and support geometry are otherwise unrestricted. Pi_m^3 means total degree <=m.

## Status and dependencies

Overall status: **PROVED with explicit LITERATURE dependency**.

| Dependency | Kind / precise use |
|---|---|
| D1-01, finite-frame.md | Local PROVED: polynomial defect identity, exact reflection lift, critical-count squeeze |
| D1-02, stationary-limit.md | Local PROVED: high-leverage removal, orthogonal stationary local law and preserved critical mean intensity |
| D1-03, complete-law.md | Local PROVED: that law has complete exponential spectra almost surely |
| LIT?padua-3d-20261106-codex-D1-GL, sources.md | LITERATURE: Greenfeld–Lev Theorem1.1, exact primary statement and application checked; source proof not locally inherited |

No non-tiling slogan, conjectural packing constant or unverified universality theorem is a proof premise. LM1.1 was independently read as a corroborating source; GL1.1 alone is sufficient. This is a development claim requiring the assigned independent audit, not an audit acceptance or historical-priority claim.

## Proof

First, O={x in R^3:|x|_1<=1} is not spectral. It is a full-dimensional bounded convex polytope, and its facet conv(e1,e2,e3) is a triangle. A centrally symmetric polygon has its vertices paired under the center reflection and therefore has an even number of vertices. This facet is not centrally symmetric. The primary-read Greenfeld–Lev Theorem1.1 therefore excludes a complete orthogonal exponential basis for Lebesgue L2(O). Its spectrum definition exp(2pi i lambda.x) matches D1-02/03 exactly.

Suppose the displayed eventual fixed-excess assertion were false. For every positive integer r choose n_r>=r and a positive rule exact through 2n_r-1 with

    N_r < (1+1/r) D_r,       D_r=binom(n_r+2,3).

D1-01 gives N_r>=D_r, so N_r/D_r->1 and n_r->infinity. Reflect its arccosine representatives by all coordinate signs, with stabilizer-corrected positive weights. D1-01 gives a torus rule exact through l1 frequency degree 2n_r-2, with m_(n_r)<=M_r<=8N_r and m_n/n^3->4/3. Since D_r/n_r^3->1/6, the squeeze gives M_r/m_(n_r)->1.

D1-02 now constructs a translation-invariant probability law of separated orthogonal exponential sets on O whose mean counting measure is |O| times Lebesgue measure. D1-03 implies that almost every realization is a complete spectrum for O. In particular at least one complete spectrum exists, contradicting Greenfeld–Lev's facet condition. The negation is impossible, proving the existence of gamma and n0.

Finally D_r= n_r(n_r+1)(n_r+2)/6>=n_r^3/6. For a Padua-cardinality rule, binom(n+3,3)/binom(n+2,3)=(n+3)/n=1+3/n. This is less than 1+gamma when n>3/gamma, so such rules cannot exist beyond max(n0, floor(3/gamma)+1). That threshold is existential; no value of gamma or n0 has been extracted. QED.

## Exact identities and reproducibility

The proof is analytic. The seven exact finite controls in `../evidence/fd1-controls.json` check the polynomial and torus trace identities on topic parity lattices, a topic cyclic rule and 2-D Padua. Source code SHA256 `e5bf2b9266a8128585c460c42324827b3380b1c3443a9e38ed9cffd457292d1c`; Python3.12.14, SymPy1.14.0; deterministic, seed none. Root reports a separate actual seven-row matching rerun. These are controls, not a computer proof of the eventual bound. Full commands and receipt identities are in the evidence and ledger.

## Scope, limitations and remaining verification

The constants are non-effective. No finite n is ruled out by an explicit threshold here; this does not upgrade the old n<=109 complement classification. No sharp 1/4 leading constant, signed-weight result, minimal interpolation norm lower bound or impossibility of polylogarithmic interpolation follows. The argument does not cover exactness only through 2(1-eta)n for a fixed eta>0. General doubling weights require another local-limit argument and are not included.

The mandatory final reconstruction still checks 2-D Padua, sphere/disk literature, the source/novelty gate and each compactness/quantifier passage. Any material gap found there must return this consequence to CONDITIONAL or OPEN as appropriate, while separately proved supporting lemmas retain their own statuses.

## History

2026-11-12, Codex, assigned gpt-6.1-sol xhigh. R3 preregistration published/pushed at `613735e` before root GO. The C1 target is retained with its original Chebyshev scope and now receives this source-dependent proof. Supporting identities originated in scout S2/S4; the stationary averaging lead was supplied by root. No bare PROVED import, source-proof inheritance or exhaustive novelty claim.
