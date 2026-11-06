# Independent round08 lattice checks

Verification supplement, **not** the Claude audit. Rules and input head:
`9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Codex, coordinator-assigned
`gpt-6.1-sol` xhigh; runtime model metadata is unexposed. Ownership is limited
to this report, `code/r08_lattice_check.py`, and
`evidence/r08-lattice-check*.json`; no Git changes. Read the rules, handoff08,
audit03 T10/T9 and their exact-search checkers, T10 producer and the T7/T2
survivor records. This checks the prescribed existing construction; no new
mechanism, priority claim or literature novelty assertion is proposed.

The cloud-environment runtime skill was read and environment status checked;
the environment was running with current observations. No network access,
credentials or containers were needed. Python3.12.14, NumPy2.3.5,
SymPy1.14.0; numerical runs use one OpenBLAS/OMP thread. Scratch is the unique
`/tmp/padua-r08-independent-lattice-9042e1c/`, regenerate-only. Receipts record
the exact source and raw hashes; no prose is pinned.

## Reconstructed finite reduction

These arguments were reconstructed independently; the implementation imports
neither producer nor audit code.

1. A finite subgroup `H` of the three-torus has an annihilator lattice
   `L <= Z^3` of full rank, and `|H| = [Z^3:L] = q`. Every such lattice has
   exactly one row upper HNF with rows `(a,b,c),(0,d,e),(0,0,f)`, positive
   diagonal, `0<=b<d`, `0<=c,e<f`. Thus determinant `q=adf` contributes
   `sum_(adf=q) d*f^2` HNFs, with no cyclicity or symmetry restriction.
2. The uniform average of a character of frequency `k` over `H` equals one
   for `k in L`, and zero otherwise. Expanding a product of Chebyshev
   polynomials shows that the unshifted pushforward Haar cubature is exact
   through total degree `2n-1` when `L` has no nonzero vector of l1 norm
   below `2n`. This condition is also necessary: a nonzero short `k in L`
   gives a nonconstant product `T_|k1| T_|k2| T_|k3|` whose Haar integral is
   zero and whose discrete average is a strictly positive count of
   annihilating sign variants divided by a power of two. All folded weights
   are positive integer multiplicities divided by `q`.
3. For HNF coordinates, every lattice vector is
   `(a*u, b*u+d*v, c*u+e*v+f*w)`. It suffices to test `u=0,v>0` and `u>0`,
   by negation symmetry, together with the pure third-axis vector. For a
   fixed `u,v`, a short vector exists exactly when
   `u*c+v*e == k (mod f)` for some integer
   `|k| <= 2n-1-a*u-|b*u+d*v|`. The independent enumerator solves this
   congruence using `gcd(u,f)` and an inverse modulo `f/gcd(u,f)`, marking
   the forbidden `(e,c)` entries. This is a different enumeration path from
   the producer's per-HNF scalar closest-residue tests.
4. Solve `B*theta=j` in the order `theta3,theta2,theta1`, with
   `0<=j1<a,0<=j2<d,0<=j3<f`. The resulting `q` distinct torus points are
   all of `H`. Coordinatewise cosine equality is exactly equality of
   numerator residues up to sign. Therefore replacing each numerator by
   `min(h,q-h)` and counting distinct triples computes the actual folded
   cardinality, including boundary degeneracies. Every cosine fibre has at
   most eight points, so `|X|>=q/8`.
5. Consequently `q<=8N` exhausts every candidate with `|X|<=N`, and
   `q<=8(t-1)` exhausts every candidate with `|X|<t`. These reductions are
   unconditional and use no packing theorem. Minimum determinant, minimum
   folded cardinality, and minimum folded cardinality with rank `N` are
   different objectives. A unisolvent set must have at least `N` points.
6. To compute exact ranks, expand ordinary monomials
   `x^alpha` by the binomial formula in torus characters; discard only each
   column's nonzero denominator `2^|alpha|`. Reduce frequencies to their
   canonical remainder modulo the row lattice by triangular integer
   division, then eliminate the resulting integer columns over `Q` with
   `Fraction`. Characters of `H` are linearly independent, so this rank is
   the complex evaluation rank on `H`, which equals the rank on its cosine
   image. This gives exact deficiency as well as exact full rank. It does
   not infer singularity from a failed modular test.
7. A determinant-window search starting at `ceil(38*n^3/27)` is globally
   exhaustive only **conditional on the imported packing bound**
   `det L >= 38*n^3/27`. Its normalization follows from packing l1 balls of
   radius `n`, whose volume is `4*n^3/3`, at lattice density at most18/19.
   This supplement does not primary-verify that source theorem and does
   not remove that dependency. Unrestricted searches from determinant1
   have no such dependency.

The HNF normal form, finite-group character orthogonality and exact Python
integer/Fraction arithmetic are the trusted mathematical/computational
dependencies. Modular actual-node certificates additionally trust SymPy's
prime/root routines; the script explicitly verifies the selected root order.
Numerical cosine and Lebesgue checks remain MEASURED.

## Completed alternate-implementation checks

Frozen independent checker SHA256:
`4abbbfbc4db140caf9c3d83915d33994e36984fc3607a2b852067989d5561596`.

- `controls` exhausts every HNF at determinants1..40 for each of n1,2,3:
  131943 scalar membership comparisons, all equal to the forbidden-entry
  enumeration. Scalar membership uses direct canonical quotient reduction
  on the entire short l1 half-ball, independently of congruence marking.
- `examples` constructs the **actual** folded nodes and Haar weights for
  the order19 cyclic generators. For `(1,3,7),(1,4,6),(1,5,8)`, each has
  10 nodes, dual l1 minimum4, exact rational monomial rank10, and actual
  cosine-node rank10 over `F191` with a root of exact order19. The origin
  node has weight1/19 and each other node weight2/19. The finite reduction
  proves positive degree3 Haar cubature. All20 monomial moment checks on
  numerical nodes have error at most1.67e-16. The 41-cubed Lobatto mesh
  gives `Lambda=8.134069037119591` for all three; this is a sampled lower
  bound, not a certified continuous maximum.
- The old fourth T2 generator `(1,7,8)` also has10 nodes and rank10, but
  dual minimum3 and a degree3 moment error0.25. It is an instructive check
  that full rank and the correct count alone do not give the requested
  cubature. The three cubature examples are the first symmetry class in
  [T2's survivors](theory/t2-finite-survivors.md), among the32 order19 full
  rank subgroups in [T7's complete n2 census](theory/t7-r06-n2-census.md).
- The n3 HNF `(1,3,3,6,0,10)` has determinant60,24 folded nodes, no dual
  vector of l1 norm below6, exact rational rank20, and actual cosine-node
  rank20 over `F61` using a root of exact order60. Its56 numerical degree5
  monomial checks have maximum error1.11e-16. This is an attaining witness
  for the independently checked lower-exclusion search below.
- Full n2 determinant1..80 complement:344574 HNFs,205858 admissible
  lattices, minimum determinant12, minimum folded count7. Exactly24 HNFs
  have folded count10 and rank10; all have determinant19. The rank
  histogram in the receipt retains every fold at most10, including
  deficient cases. This confirms objective(iii)=10 while objective(ii)=7.

Receipts: `r08-lattice-check-controls.json`,
`r08-lattice-check-examples.json`, and
`r08-lattice-check-complement-n2.json` under `evidence/`.

## Commands and ongoing coverage

Executed from the shared workspace, with absolute script/output paths in
the receipts. The equivalent topic-relative commands are:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py controls --out evidence/r08-lattice-check-controls.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py examples --out evidence/r08-lattice-check-examples.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py complement --n 2 --out evidence/r08-lattice-check-complement-n2.json --raw /tmp/padua-r08-independent-lattice-9042e1c/n2.jsonl
```

The n3 determinant1..184 search computing every exact rank through fold23,
the n4 determinant1..280 complement, determinant windows n4..16, and frozen
producer reruns are currently executing. Their results are not claimed in
this initial checkpoint; completed scope and commands will be appended.

## Limits

No all-degree existence/nonexistence claim follows. The lattice class here
is unshifted pushforward Haar on a finite torus subgroup; arbitrary phases,
weighted cubature rules and nonlattice nodes are outside these reductions.
The T7 all-phase classification is cited only for the existing n2 crosslink.
There are no claims of globally optimal continuous Lebesgue constants.
