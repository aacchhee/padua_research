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
   The previously proved identity-mass witness also makes admissibility
   necessary for **any nonnegative weights with positive identity mass**,
   hence any strictly positive weights on the full unshifted support.
   Independently reconstruct it as follows. For a three-coordinate relation
   with magnitudes `a>=b>=c>0`, put `u=T_a(x1),v=T_b(x2),w=T_c(x3)`.
   The cosine Gram identity on `X` is
   `1-u^2-v^2-w^2+2uvw=0`. Thus
   `F=1-v^2-w^2+2uvw=u^2>=0` on `X`, has degree at most `a+b+c`, Haar
   integral zero, and identity value one. Nonnegative weights and positive
   identity mass contradict exactness. For two coordinates use
   `T_a(xi)T_b(xj)=cos^2(a*theta_i)` on `X`; for one coordinate use
   `T_r(xj)=1` on `X`. This verifies the transfer in
   [the positive-weight record](theory/t9-r06-phase-weight-boundaries.md).
   Haar weights suffice on every admissible support, so the existence
   class enumerated here also decides full strictly positive weights.
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

### Additional completions

The separate exact order19 crosslink check enumerates all324 lines with
nonzero coordinate projections and reproduces the complete rank histogram
`{3:4,5:24,6:72,7:24,8:48,9:120,10:32}`. Of the32 rank10 lines, exactly24
meet the degree3 Haar criterion. A separate36-generator normalized T2
screen returns exactly the four generators above, with only the first
three cubature-admissible. See `r08-lattice-check-t7link.json`.

The alternate congruence algorithm completed every determinant window at
n4..16. First admissible determinants are
`92,178,304,486,724,1026,1412,1878,2432,3098,3868,4750,5772`, with24
minimizers except8 at n6,9,12,15. In particular, n16 improves the old seed
5792: determinants5765..5771 are empty, while5772 has24 minimizers, e.g.
`(1,0,1671,1,427,5772)`. The n16 computation took70.160seconds; total
window cost is recorded per degree. These are global determinant minima
**conditional on the imported packing bound**; exact finite window
coverage itself is unconditional. See `r08-lattice-check-windows.json`.

The separately compiled frozen producer was rerun at n4 through
determinant352 and fold cap44. It processed28911538 HNFs, of which8634185
were admissible, and retained28 cases. The independent monomial/Fraction
rank implementation gives exactly
`(fold,rank,count)=(35,30,1),(39,33,3),(43,32,24)`. Thus none of the
retained cases is unisolvent. Independently, the HNF
`(4,0,5,5,5,10)` has determinant200,45 folded nodes, exact rational rank35,
and actual-node rank35 over `F401`, with a root of exact order200. All120
numerical degree7 monomial moments have error at most2.23e-16. By `q/8`,
this establishes unisolvent minimum45 in the unshifted Haar lattice class;
the exclusion uses a fresh producer execution and a separate exact rank
implementation. See `r08-lattice-check-minrank-n4.json`.

The alternate implementation also completed n3 at every determinant1..184:
4140222 HNFs,1710190 admissible lattices, minimum determinant38 and minimum
fold16. Every case with at most23 nodes was ranked exactly, giving
`(fold,rank,count)=(16,15,1),(20,17,20),(20,18,3),(22,18,68)`; none has
rank20. The already checked24-node/rank20 witness therefore attains the
global unisolvent minimum24 in the class, with no packing-bound dependency.
The full computation took416.827seconds and wrote38502438 raw bytes outside
Git. See `r08-lattice-check-minrank-n3.json`.

The alternate implementation completed the full n4 determinant1..280
complement as well:14580438 HNFs,2943865 admissible lattices, minimum
determinant92, minimum fold35 at determinant128, and exactly one case
with fold at mostN=35, of exact rational monomial rank30. This agrees with
the producer's separate execution and rules out an exact-N unisolvent
support in the class at n4. The independent run took883.720seconds and
wrote70828964 regenerate-only raw bytes. See
`r08-lattice-check-complement-n4.json`.

A separate execution of the frozen producer completed the det<=8N
complements at n2..6. It reproduces the following finite results:

| n | determinant cap | admissible lattices | minimum fold | ranks of every fold<=N case |
|---|---:|---:|---:|---|
|2|80|205858|7|full histogram in receipt;24 rank10 cases|
|3|160|964755|16|16/15 once;20/17 twenty times;20/18 three times|
|4|280|2943865|35|35/30 once|
|5|448|6749170|54|54/48 once|
|6|672|12910075|91|none, since91>84|
|7|960|21354010|128|none, since128>120|

Here `m/r` means folded count/rank, rather than a ratio. This rerun is a
fresh producer execution; it is distinct from the alternate n2/n3/n4
checks, which are identified separately. The exact integer coverage/ranks
are reproduced; wall times vary because several independent processes
shared the machine. See `r08-lattice-check-producer-complement.json`.
The n7 row is a separately executed uncapped run in
`r08-lattice-check-producer-complement-n7.json`:584906253 total HNFs,
complete determinant interval1..960,304.789seconds. It closes the exact-N
question at n7 in this class independently of the developer's initially
capped main/tail runs. It does not assert global minimum fold128: smaller folds
greater than120 could require determinants above960.
The developer subsequently completed its third segment922..960. I then
independently parsed its three raw segments, checked their byte/hash
identities, verified that their q rows are exactly1..960 without overlap,
and compared every `(q,hnf_total,after_axis_pair_prune,admissible,small)`
field to my uncapped replay. All960 rows agree, reproducing scientific
SHA256 `909f9922a468ac00745d180344299e62d35e9b17e2b16ec881bd707eece5ae39`.
The completion driver `r08_lattice_finish.py` was inspected and its frozen
SHA256 `c676f999ebd1ded2802d008cf74bcf0b2a00e5b1695ca671ec97f51fc001d688`
verified; the fresh comparison used direct JSON parsing rather than
importing that driver. The union's own execution/provenance remains in
the producer's `r08-lattice-n7finish.json`, distinct from my uncapped run.
For n2..5 the observed folded minima7,16,35,54 are also global: each is
at mostN, so any smaller fold would already appear in the complete
det<=8N search. At n6/7 only the absence of folds at mostN is globally
exhaustive; the observed91/128 remain bounded-det minima.

The n5 expanded producer replay completed every determinant1..592 and
fold cap74:137029493 HNFs,30171840 admissible lattices, seven retained
cases. Independent exact monomial ranks are
`(54,48,1),(63,53,3),(72,53,3)`. The canonical HNF
`(5,0,6,6,6,12)` attains determinant360,75 nodes and exact rational rank56;
its actual-node certificate over `F1801` also has rank56 with a root of
exact order360. All220 numerical degree9 moments have error at
most4.45e-16. The same `q/8` reduction therefore gives unisolvent minimum75
in the class, without a packing-bound dependency. The fresh enumeration
took244.794seconds. See `r08-lattice-check-minrank-n5.json`.

The separate producer minimum replay also completed n1..16, agreeing with
the alternate windows and the unrestricted small-degree searches. The
minimum determinants are
`2,12,38,92,178,304,486,724,1026,1412,1878,2432,3098,3868,4750,5772`.
This rerun's full25723-byte receipt is regenerate-only in scratch; the
durable `r08-lattice-check-producer-min.json` is compact15633-byte JSON,
including the full-receipt identity and every raw identity. No scientific
field was discarded to meet the16KiB bound.

## Executed commands and coverage

Executed from the shared workspace, with absolute script/output paths in
the receipts. The equivalent topic-relative commands are:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py controls --out evidence/r08-lattice-check-controls.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py examples --out evidence/r08-lattice-check-examples.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py complement --n 2 --out evidence/r08-lattice-check-complement-n2.json --raw /tmp/padua-r08-independent-lattice-9042e1c/n2.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py complement --n 3 --maxdet 184 --rank-maxfold 23 --out evidence/r08-lattice-check-minrank-n3.json --raw /tmp/padua-r08-independent-lattice-9042e1c/n3.jsonl
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/r08_lattice_check.py complement --n 4 --out evidence/r08-lattice-check-complement-n4.json --raw /tmp/padua-r08-independent-lattice-9042e1c/n4.jsonl
```

Producer sources were frozen at SHA256
`0d03590f8587f799ad5213ba2b41def2b23e80472ff7327076b4b4f19cbfbfe0`
for `r08_lattice.py` and
`e07ad9e51d5b883e7c6d813d396ef32ea0ac24eda253a73f6137f8b8f86feaa4`
for `r08_lattice_enum.cpp`. The actual compiler was g++14.2.0, invoked by
the producer with `-O3 -std=c++17 -Wall -Wextra`. Commands actually run:

```sh
python code/r08_lattice.py build /tmp/padua-r08-independent-lattice-9042e1c/producer-enum
python code/r08_lattice.py run complement --degrees 2 3 4 5 6 --binary /tmp/padua-r08-independent-lattice-9042e1c/producer-enum --scratch /tmp/padua-r08-independent-lattice-9042e1c/producer-complement --receipt evidence/r08-lattice-check-producer-complement.json
python code/r08_lattice.py run min --degrees 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 --binary /tmp/padua-r08-independent-lattice-9042e1c/producer-enum --scratch /tmp/padua-r08-independent-lattice-9042e1c/producer-min --receipt evidence/r08-lattice-check-producer-min.json
/tmp/padua-r08-independent-lattice-9042e1c/producer-enum complement 4 1 352 44 /tmp/padua-r08-independent-lattice-9042e1c/producer-minrank-n4.jsonl
/tmp/padua-r08-independent-lattice-9042e1c/producer-enum complement 5 1 592 74 /tmp/padua-r08-independent-lattice-9042e1c/producer-minrank-n5.jsonl
python code/r08_lattice.py run complement --degrees 7 --binary /tmp/padua-r08-independent-lattice-9042e1c/producer-enum --scratch /tmp/padua-r08-independent-lattice-9042e1c/producer-complement-n7 --receipt evidence/r08-lattice-check-producer-complement-n7.json
```

Additional executed Python drivers imported the frozen independent module
with `importlib.util.spec_from_file_location`. These are their scientific
loops, with JSON writing and progress printing omitted; the receipts retain
their source/raw identities. They do not import producer rank routines.

```python
# Independent window driver: exact executed seed mapping and stopping rule.
seeds = {4:92,5:178,6:304,7:486,8:724,9:1026,10:1412,11:1878,
         12:2432,13:3098,14:3868,15:4750,16:5792}
for n, seed in seeds.items():
    for q in range((38*n**3+26)//27, seed+1):
        good = list(m.forbidden_enumerator(n, q))
        if good:
            break

# Independent order19 link: every nonconstant-coordinate subgroup.
for c in range(1, 19):
    for e in range(1, 19):
        h = (1, 0, c, 1, e, 19)
        r = m.rational_rank(h, 2)
        if r == 10:
            admissible = m.admissible_direct(2, h)

# Expanded producer streams were reparsed and independently ranked.
# raw is the corresponding n4/n5 JSONL path from the commands above.
for line in raw.open():
    r = json.loads(line)
    if r['type'] == 'small':
        rank = m.rational_rank(r['hnf'], n)

# Each attaining witness was independently regenerated before certification.
q, F = m.folding(h)
admissible = m.admissible_direct(n, h)
rank_Q = m.rational_rank(h, n)
actual_root_certificate = m.actual_node_rank(q, F, n)
numerical_moments = m.numerical_node_check(q, F, n)
```

All runs listed in this report are complete. Twelve durable receipts
parse as JSON and each is below16KiB; their32 referenced raw identities
were checked against local byte lengths and SHA256. The independent
source remains frozen at the SHA above. No scientific discrepancy was
found within the declared scope. This is supporting verification, not
the required focused Claude re-audit or approval of the full response.

## Limits

No all-degree existence/nonexistence claim follows. The lattice class here
is the full cosine image of an unshifted finite torus subgroup. The
identity-mass witness extends the necessary criterion, and therefore the
existence/nonexistence conclusions, to any nonnegative weights with
positive identity mass, including arbitrary strictly positive weights on
that full support. Arbitrary phases, zero identity mass, negative weights
and nonlattice nodes are outside these reductions. Cardinality always
counts the entire cosine image `X`; deleting zero-weight nodes changes
that class and is not covered by the determinant/cardinality reduction.
The T7 all-phase classification is cited only for the existing n2 crosslink.
There are no claims of globally optimal continuous Lebesgue constants.
