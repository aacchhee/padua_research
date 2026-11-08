# PD-T?padua-3d-20261106-codex-R08-reduction — exact unrestricted finite lattice reduction

ID kind: PD-T. Aliases: round08 HNF reduction; three lattice objectives.
Split from/into: none. Overall status: **PROVED** (local algorithm reduction).
No novelty claim; this writes out the existing audit03 search mechanism.

## Statement and definitions

For a full-rank sublattice L of Z³, write q=[Z³:L], H=L^perp in (R/Z)³,
X={cos(2πh):h∈H}, and N=binom(n+3,3). A lattice is admissible when every
nonzero k∈L has l1 norm>=2n. The algorithms below enumerate exactly all
admissible L in a finite determinant interval, compute |X| and its exact
Pi_n evaluation rank, and reduce a claim |X|<t to determinants<=8(t−1).
The determinant, folded-count and unisolvent-fold objectives are distinct.

## Finite reduction and proof

1. Each L has a unique row upper HNF B with rows(a,b,c),(0,d,e),(0,0,f),
   a,d,f>0, 0<=b<d, 0<=c,e<f. For q=adf there are exactly
   sum_(adf=q) d f² such forms. The loop includes every diagonal divisor
   triple and every allowed b,c,e; it does not quotient coordinate symmetry
   or restrict cyclicity. The receipt's `hnf_total` counts this unpruned
   mathematical scope; `after_axis_pair_prune` counts actual scalar tests.
2. Every lattice vector is (au,bu+dv,cu+ev+fw). The pure last-axis vector
   excludes f<2n. For u=0, sign symmetry permits v>0; the least possible
   absolute third coordinate is dist(ev,fZ), so checking dv<2n is complete.
   This test is independent of b,c. For u≠0, symmetry permits u>0. A short
   vector must have au<2n and |bu+dv|<=2n−1−au, giving exactly the finite
   ceil/floor interval in the C++ loop. Its least possible third coordinate
   is dist(cu+ev,fZ). This exhausts all possible strict l1<2n failures.
   All membership, distance and bound arithmetic is integer arithmetic.
3. The dual group has exactly the q distinct numerator triples modulo q

   ```
   h3 = a*d*j3,
   h2 = a*(-e*j3+f*j2),
   h1 = -b*(-e*j3+f*j2)-c*d*j3+d*f*j1,
   0<=j1<a, 0<=j2<d, 0<=j3<f.
   ```

   Substitution gives Bh divisible by q. Distinct j3 give distinct h3;
   at fixed j3, distinct j2 give distinct h2; at fixed j2,j3, distinct j1
   give distinct h1. Thus this is all H. Cosine equality is coordinatewise
   equality up to sign modulo q, so `min(hj,q−hj)` gives exact node keys.
   Multiplicities divided by q are strictly positive Haar weights.
4. Put adj=q B^−1. A character k restricted to H is represented by
   k*adj mod q; two restrictions coincide exactly when k−k'∈L. Expand
   each tensor Chebyshev T_alpha as 2^−s times the sum of the characters
   obtained by independently changing its nonzero coordinate signs, where
   s is its number of nonzero coordinates. Form the integer character
   incidence column, keeping repeated character multiplicities. Distinct
   characters of H are linearly independent over C, hence the rational
   rank of this integer incidence matrix equals the real evaluation rank
   on H and on X. Exact Fraction elimination therefore proves both full
   rank and deficiency. A deficient modular specialization is never used
   to assert real singularity. The checker uses a separate construction.
5. Each cosine fiber contains at most8 points, so q<=8|X|. Consequently
   every |X|<=N candidate occurs at q<=8N; every |X|<t candidate occurs at
   q<=8(t−1). An attained folded size m and absence of smaller sizes
   through8(m−1) prove the global folded minimum. An attained full-rank
   folded size t and deficient exact ranks for every smaller fold through
   8(t−1) prove the global full-rank (rank-N) minimum. No determinant minimizer is
   automatically a folded or full-rank minimizer.
6. Admissibility makes Haar cubature exact on Pi_(2n−1): every nonconstant
   Chebyshev term expands into nonzero frequencies of l1<=2n−1, whose
   Haar averages vanish. Conversely the local nonnegative witness in
   [the positive-weight record](t9-r06-phase-weight-boundaries.md) makes
   admissibility necessary for **any strictly positive weights on the
   full unshifted X**, since the identity node has positive mass. Thus
   exhaustive admissible enumeration decides existence of any such
   positive rule; Haar supplies positive weights for every survivor.

## Checks, dependencies and scope

Code: `code/r08_lattice_enum.cpp`, `r08_lattice.py` and the small witness,
minimum-rank and tail drivers. All are regenerated from repository inputs;
only raw output is scratch. Exact finite claims and independent executions
are recorded separately in the round08 minima/complement records.

Trusted computation: C++17 integer arithmetic/hash-set equality; Python
integer and Fraction arithmetic, JSON parsing and SHA256. The largest
executed q and products are far below signed64-bit bounds; packed group
keys use uint64_t. NumPy is used only for the labeled floating quality
diagnostic. Imported packing density is needed for the short determinant
windows only, not for this finite reduction or the det<=8N complement.

The scope is zero-phase finite torus subgroups with full positive support.
Arbitrary phases, discarded zero-weight nodes, non-lattice sets, and
Lebesgue upper bounds are not decided. In particular a small positive
rule can be singular on Pi_n. The general all-degree Padua-type question
remains OPEN.

## History

2026-11-06; rules/input9042e1c42964150f30fdbe8563c12ba6c6a8692a;
Codex, assigned Sol xhigh. Completion of handoff08 B5/B6 and audit03 E1/E3;
pre-run scope in attempts/T10-round08.md and T9-complement-round08.md.
