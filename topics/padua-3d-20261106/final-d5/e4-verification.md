# D5 R1 — exact E4 primary statement and application checks

2026-11-12; Codex, assigned gpt-6.1-sol xhigh (internal runtime metadata unexposed). Rules/input `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`; R1 published by root at `f9ab1c6` before this registered reading. AC's settled convention is in handoff19. This record verifies the three existing imports, not their external proofs. Source PDFs were actually opened through the web connector; the attempted local curl fetch failed (sandbox proxy; approved retry403). No full PDF bytes/hashes exist locally and none is committed. Coverage is listed per source.

## Betke–Henk — LIT?padua-3d-20261106-codex-D5-01

Primary: [arXiv math/9909172v1](https://arxiv.org/pdf/math/9909172v1), *Densest Lattice Packings of 3-Polytopes*. Read p1 packing/density definitions and §5 p31 octahedron entry; introductory attribution p2. The paper defines density as volume divided by packing-lattice determinant. Its unit octahedron is `O={|x1|+|x2|+|x3|<=1}` and its maximal lattice packing density is `18/19`; the displayed basis is exactly the local `Bcrit=(1/3)[[2,-1,-3],[3,-2,1],[1,3,-2]]`. It credits Minkowski1904. Full classification proof and original1904 source were not read.

Application check: shortest nonzero dual l1 norm at least2n makes `nO+L` an interior-disjoint packing. `vol(nO)=4n³/3` gives `det L>=38n³/27`; eight-to-one cosine folding gives `|X|>=19n³/108`. Local strict-positive full-support unshifted hypotheses and the witness lemma remain essential. The local polynomial threshold n>=110 follows from `n³-108n²-198n-108>0`. This source does not classify folded counts, translated cosets or arbitrary cubature nodes.

**Recommendation:** retain **PROVED with explicit LITERATURE dependency** for the existing packing consequence and finite minima whose lower search cutoff uses it. D4 may independently remove that dependency only for ranges actually rerun from its elementary bound.

## Chkifa — LIT?padua-3d-20261106-codex-D5-02

Primary: [arXiv1503.01731v2](https://arxiv.org/pdf/1503.01731v2), *New bounds on the Lebesgue constants of Leja sequences on the unit disc and on R-Leja sequences*. Read §1.1 definitions, §3 equation(3.5) p14, §4 definitions p17 and Cor4.3/equation(4.8) p19. The actual source uses k-point interpolation and `Delta_k=I_(k+1 points)-I_(k points)`, D0=1. For `2^m<=k<2^(m+1)`, Cor4.3 gives `D_k<=2^sigma1(k)2^m`. Equation(3.5) gives the exact real sequence used locally. Its invoked earlier Lemma7 was not read; no source proof is inherited.

Application check: local `I_k` interpolates degree<=k on k+1 points, hence its difference indexing agrees. The elementary inequalities `2^sigma1(k)<=k+1` and `2^m<=k` give `D_k<=(k+1)^2` (k=0 separately). The locally proved tensor lower-set identity then yields the stated coefficient sum and `8 binom(n+9,9)`. The source introduction already attributes cubic-in-cardinality multivariate R-Leja bounds to earlier work; this is a known bound, not a new optimality claim.

**Recommendation:** retain **PROVED with explicit LITERATURE dependency** in [the existing specialization](../theory/t9-r06-explicit-rleja.md).

## Kolomoitsev–Lomako — LIT?padua-3d-20261106-codex-D5-03

Primary: [arXiv1801.00608v1](https://arxiv.org/pdf/1801.00608v1), *On the growth of Lebesgue constants for convex polyhedra*. Read p1 definition of `L(P)` with normalized `(2pi)^(-d)` torus integral, p2 triangulation-size definition, and Thm4.1 pp18–19. For bounded convex `P` contained in `prod[0,n_j]`, all `n_j>=1`, it states `L(P)<=C(s,d) prod log(n_j+1)`, where s is the number of simplices in a triangulation. Source supporting lemmas/full proof chain remain unverified locally.

Application check: `nO+(n,n,n)` is convex, lies in `[0,2n]^3`, and is triangulated by eight tetrahedra from its origin-center and eight triangular facets, translated and scaled with n. Thus s=8 is fixed. Translation by the integer vector `(n,n,n)` bijects lattice frequencies and multiplies their polynomial by a unit-modulus exponential. Source normalization matches the local Haar normalization. The written local Fejer sampling bound `||Hn||<=13³||D_n||L1` and rank-one correction `||Pn-Hn||<=1` then give the existing log³ corollary, for both stated parity-order choices.

**Recommendation:** retain **PROVED with explicit LITERATURE dependency** in [T10 log³](../theory/t10-log3-corollary.md). This is oversampled projection, not exact-N interpolation. Wang–Wang–Wang is a separate prior-art/application question; failure to fetch it does not reopen this already verified import.
