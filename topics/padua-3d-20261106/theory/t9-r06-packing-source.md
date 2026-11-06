# PD-T?padua-3d-20261106-codex-T9-r06-01 — published octahedron density and its precise consequence

Aliases: T9-R06-P; T9-R06-TH01. Scoped obstruction: PD-N?padua-3d-20261106-codex-T9-r06-04 (strictly positive full-support unshifted minimal cubature n>=110). Supporting lemma: PD-T?padua-3d-20261106-codex-T9-r06-02.

Status: **PROVED with the explicitly imported LITERATURE theorem below**. No conjectural packing premise remains in this new source-dependent record. It does not silently change the status or dependencies of T9-03 or `t9-packing-conditional.md`.

## Imported theorem and source coverage

For the octahedron O={x in R^3: ||x||_1<=1}, the maximal lattice packing density is 18/19. Betke–Henk, *Densest Lattice Packings of 3-Polytopes*, arXiv:math/9909172, PDF page index 30 (printed page 31), explicitly gives this normalization, density, and the densest packing lattice Λ*(O) (a critical lattice of O−O=2O) with basis

```
Bcrit = (1/3) [[ 2,-1,-3],
              [ 3,-2, 1],
              [ 1, 3,-2]].
```

Its determinant is 38/27; its shortest nonzero l1 vector has length 2. The density follows from (4/3)/(38/27)=18/19. The source credits Minkowski [Min04]. The table/normalization and introductory definition of lattice density were read, including the displayed table screenshot; the complete packing classification proof and Minkowski's original 1904 paper were not checked locally. The 2023 Henk erratum's primary indexed abstract says its typo concerns the quadratic coefficient for the **icosahedron**, with its density unchanged. The full erratum PDF was not read. See provisional source records `T9-R06-LIT-BH` and `T9-R06-LIT-ERR`.

## Theorem (unshifted cosine image, arbitrary strictly positive weights)

Let H be a finite subgroup of (R/2pi Z)^3, let L={k in Z^3: exp(i k.theta)=1 for every theta in H}, and let X=cos H. If some cubature on the **full support X**, with strictly positive weights at every node, is exact on Pi_(2n-1) for product Chebyshev probability measure, then

```
|H| >= 38 n^3 / 27,       |X| >= 19 n^3 / 108.
```

Consequently |X|>binom(n+3,3) for every integer n>=110. Thus no such exact unshifted positive rule can have the minimal interpolation cardinality in those degrees. Haar pushforward weights are a special case; the weights need not be Haar.

Proof. The local nonnegative-witness lemma in `t9-r06-phase-weight-boundaries.md` gives ||k||_1>=2n for every nonzero k in L: any shorter dual relation supplies a polynomial of degree ||k||_1 with integral zero, nonnegative on X and positive at the identity node, contradicting strictly positive cubature. (For a one-coordinate relation the direct constant-value contradiction suffices.) Hence translates of nO by L have disjoint interiors. Apply the imported density theorem:

```
(4n^3/3)/det(L) <= 18/19.
```

Since det(L)=|H| and each cosine fiber has at most eight points, the inequalities follow. Notice that the comparison packing lattice is **n Bcrit**, not (n/2)Bcrit. To compare cardinalities, multiply the difference19n^3/108−binom(n+3,3) by108: the required strict inequality is equivalent to

```
f(n)=n^3-108n^2-198n-108 > 0.
```

Here f(109)=-9809, f(110)=2312, and f(n+1)-f(n)=3n^2-213n-305>0 for n>=109. QED.

## Boundary and finite complement

The proof assumes zero phase and strictly positive masses on the full cosine image (positive identity mass already suffices for the witness contradiction). It gives no such sharp theorem if zero masses permit removal of the identity, or for a translated torus subgroup. The separate `t9-r06-phase-weight-boundaries.md` proves why the shortest-dual criterion fails for phases and supplies a weaker phase-uniform annihilator criterion. The degrees1..109 are not excluded by this density estimate. T10's finite computation covers selected lattices through16 and a complete determinant-minimizer census only through3. The additional exact parity-family data through109 and timed sparse-rank probes at17/24/32 are in `t9-r06-finite-complement.md`; they prove that family's oversampling in every degree, not a global complement classification. No global minimal-node claim follows from these larger-degree seeds/families.

## Status by part and dated history — 2026-11-06, response03

ID kind: PD-T. Split from: none. Split into: none.
Betke–Henk's density theorem is LITERATURE, not a locally verified proof;
the witness and implication are local proofs. Overall: **PROVED with
explicit LITERATURE dependency**, under the criterion proposed to AC in
[response03](../response-03.md#e4--proposed-uniform-literature-criterion-ac-decision-requested).
Depends on PD-T?padua-3d-20261106-codex-T9-r06-02 and
LIT?padua-3d-20261106-codex-T9-r06-01. Audit03 companion wording corrections
T9-F2/F3/NV-F13 are applied here; Betke–Henk lead came from Claude
audit02/T9 (recollection). No underlying proof changes. The historical
finite-search boundary above is superseded by the round08 lattice record
when completed; it was not an unrestricted complement classification.
Open: phases, omitted zero-weight supports, self-contained density proof.
