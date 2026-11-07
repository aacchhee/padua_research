# U3 supplementary independent checks

2026-11-07. Codex supplementary checker, assigned gpt-6.1-sol xhigh;
runtime model metadata is not independently exposed. Rules and input head:
`38227202bc6908d5a5a874950145761a8ca4312f`. Read AGENTS.md,
agents/WORKFLOW.md, agents/codex/CODEX.md, topic LOG and report-round08.
Only the orchestrator controls Git. This check supplements development;
the required substantive Claude audit remains separate.

## Scope and chronology

Assigned scope: independently reconstruct U3's proposed shifted, folded
and mixed-coset constructions after the orchestrator publishes their gate
and prospective protocol. No new mechanism or research run was generated
before that publication. This verification scope makes no novelty claim;
the producer's prospective gate supplies the mechanism predecessor check.
The full IDEAS registry was not independently reread for this bounded
supplementary check.

Root published the shared [gate](usable-gate.md) at
`26a4b5e3b7d74f58c862e95f51a540a9935d1240`, then released U3 for
registration. The generic independent rational-coset verifier was written
without candidate parameters and remained unexecuted pending publication
of the prospective stream protocol.

Read existing T7 general-character and symbolic-stratum reductions, the
complete n2 census and its quotient/pruning/torsion proofs, rank-two
counterexample and translated cubic survivor/cubature obstruction; T8
rational-phase certificates, unit-coordinate fold counts, mixed phases,
common-even-union obstruction, DCT cubic-eight classification and exact
half-shift trace obstruction; T9's positive identity-mass lemma,
phase-uniform annihilator and unshifted density exclusion.

The phase and count limits to preserve are explicit: node count is
constant on a collision stratum while evaluation rank can vary; a deficient
modular specialization cannot establish real singularity or exclude its
continuous stratum; and the positive full-support unshifted short-dual
criterion does not transfer to arbitrary phases or removal of zero masses.

## Published protocols and final executed scope

Root published the S/F/M/R protocol at
`3b5cb29f5d68306fa61d3079627247110911b552`, then authorized the independent
runs. The initial producer code was frozen at SHA256
`8c230e3a6bd857c8b3f8c63cd49a2c818d1449b60d9cb131c8662158ff8bc79b`.
The prospective F integer-rank completion was published at
`995062b42aa73648bd591a21c9ea240feffc3c6f` before its new exact runs.
Its separate producer helper is SHA256
`73619ff1c4f46c95f4e9fc2cf93f3c91d8a1a9bce42f949a4ca533f51572c823`;
the initial producer source and four receipts stayed unchanged.

All following commands were actually executed from the repository root.
Prefix the actual-node and F-exact commands with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`; the structural and comparison
commands use integer/Fraction arithmetic only.

```text
python topics/padua-3d-20261106/code/uc3_structure.py --route S --degrees 3 5 7 --receipt topics/padua-3d-20261106/evidence/uc3-s-census.json
python topics/padua-3d-20261106/code/uc3_structure.py --route F --degrees 3 4 5 6 7 8 --receipt topics/padua-3d-20261106/evidence/uc3-f-census.json
python topics/padua-3d-20261106/code/uc3_s_matching.py
python topics/padua-3d-20261106/code/uc3_independent.py --inputs topics/padua-3d-20261106/evidence/uc3-selected-inputs.json --quality --controls --receipt topics/padua-3d-20261106/evidence/uc3-selected-check.json
python topics/padua-3d-20261106/code/uc3_f_exact.py --count-receipt topics/padua-3d-20261106/evidence/uc3-f-census.json --receipt topics/padua-3d-20261106/evidence/uc3-f-exact.json
python topics/padua-3d-20261106/code/uc3_compare.py
```

All six final commands exited0. The final S/F structural commands took
32.4102/2.8756seconds; separate support-matching split29.4505seconds;
15selected-node/quality/control check10.8013seconds; all460Fexact ranks
and actual-node cross-checks19.9185seconds. Python3.12.14, NumPy2.3.5,
SciPy1.17.0. No scientific producer or project mathematics is imported.
Fexact imports the checker's own two independently written modules and
pins all three actual code hashes.

Canonical checker implementation limitation: the first F enumeration
finished but its summary exceeded16KiB because every compatible tuple
was embedded; the receipt-size assertion exited1. Its382472-byte raw
catalogue remains at `/tmp/padua-uc3-structure-gmouyec7/complete-census.json`.
The summary was corrected to counts/hashes and a few examples, and BOTH
S/F commands were rerun at the final current structural-code hash.
The final F raw scientific catalogue has the identical382472bytes and
SHA256`c0416ef66264bf45ecb9ed18a8ab0a74ea6abb90e26d7619f5030e352d6de963`.
No initial success or missing receipt is invented.

## Exact cubic structure and S classification

Independent hand product-to-sum reconstruction gave the triangular pivot
order before producer results: the ten pure-mode pivots are
`0,1,4,11,2,8,18,3,12,7`; the remaining ten are
`5,10,15,6,9,13,19,17,14,16`. Their absolute diagonal coefficients are
ten1s, nine1/2s and one1/4. Thus abs det(A)=2^-11 and abs det(8A)=2^49.
The [cubic proof](theory/u3-cubic-triangular.md) displays the same identities.
An independently hard-coded hand-expansion table was inverted using
Fraction Gauss–Jordan and multiplied back exactly. All20inverse row sums
match the producer: induced infinity norm4, entrywise absolute sum52,
constant-frequency inverse-column sum1. DCT orthogonality gives the stated
cardinal formula and coarse rigorous continuum bound2*52−1=103. This bound
and the measured9.79sample have different meanings.

[uc3_structure.py](code/uc3_structure.py) regenerates each signed frequency,
combines cancellations, then strips forced row/column-degree1support edges.
Success gives a unique perfect matching. Conversely a unique perfect matching
has no alternating cycle; collapsing matching pairs produces a DAG, which
has a source/sink corresponding to a degree1column/row. Repeated stripping
therefore detects every unique matching. The matched DAG permits exact
Fraction inverse substitution, with no producer/SymPy inverse imported.

The separate [augmenting-path checker](code/uc3_s_matching.py) independently
decides perfect-matching existence, distinguishing the other two bins that
leaf stripping alone does not separate. All35287parameter outcomes match
the producer casewise:

| n | Pairs | No perfect matching | Nonunique matching | Unique matching |
|---:|---:|---:|---:|---:|
|3|741|733|0|8|
|5|6105|6085|12|8|
|7|28441|28289|152|0|

All exact inverse objectives and determinants match. Cubic Svalues are52
for the four(1,4,11)reflection variants and78for the other four. Every
quintic unique-support member has S434; lexicographic selection is(1,17,30).
The n7absence is only a unique-support obstruction. A nonunique support
does not establish singularity. The [S classification](theory/u3-sparse-classification.md)
and [scoped boundary](theory/u3-sparse-boundary.md) preserve that distinction.

## Complete F counts and characteristic-zero ranks

Independent explicit rectangular group parameters establish all6976listed
instances, their subgroup orders and actual folded cosine nodes. The
embedding recovers v from coordinate2 and u from coordinate1−coordinate2,
so the claimed invariant factors(a,b)are valid. Every2-torsion sign action
is checked against actual fixed folded nodes, never assumed free.

The independent predicate ordering prioritizes short axes; the producer
lets a trace mismatch replace a short-axis flag. Therefore individual kill
bucket counts differ. Exact node counts, their union of exclusions and
the460remaining parameter instances match casewise; this is an accounted
predicate-order distinction, not a mathematical discrepancy.

The [coherent-phase reduction](theory/u3-coherent-integer-reduction.md) is
correct: if2phase∈H, a character-class row can be multiplied by a nonzero
phase to make all its coefficients integers. Independently choose canonical
residues j=f1moda,k=f2modb rather than the producer's first contributing
raw frequency. For phase(e1h1+e2h2)/2 the remaining coefficient sign is
`(-1)^[e1*(f1−j)/a+e2*(f2−k)/b]`, with exact integer divisions even for
negative frequencies. Fourier invertibility and deletion of repeated
cosine rows preserve rank, proving equality with rational dictionary rank.

[uc3_f_exact.py](code/uc3_f_exact.py) uses integer gcd elimination and
canonical row normalization, independently of the producer's SymPy QQ
elimination. Every exact rank agrees casewise, not merely by histogram.
For EACH of the460cases it also evaluates actual-node monomials at two
fresh splitting primes near1.4e9; every modular rank equals the already
established exact rank. Modular deficiency supplies no upper bound.

| n | All parameters | Exact remaining cases | Exact full-rank cases |
|---:|---:|---:|---:|
|3|592|28|0|
|4|0|0|0|
|5|2192|150|2|
|6|1328|0|0|
|7|2864|282|0|
|8|0|0|0|

The two positive tuples are precisely(a,b,r,s,phase-index)=
`(6,18,1,14,0)`and`(6,18,5,4,0)`, each56nodes/rank56at n5.
BOTH have the independent two-prime actual-node certificates in the raw
exact record. They define ONE distinct physical cosine node set: replacing
the third-angle numerators3u+14vby15u+4vnegates them modulo18, and cosine
is even. The independent actual-node hashes agree exactly for the two
parameters; the comparison checker asserts this identity. No actual-node
specialization disagrees with rational rank.
The n4/n8empty invariant types follow also from squarefreeness of70/66
and330/326. [F classification](theory/u3-folded-classification.md) can
use this executed independent completion; the computer-assisted status
still requires publication of the essential code/evidence. Other orders,
embeddings, phases and the wider folded-family target remain outside it.

## Mixed count proofs, positive witnesses and numerical quality

For M's9-point C3×C3component, nonzero phase numerators modulo257make
the three first-axis and three second-axis cosine values individually
distinct, proving9nodes. Its first-coordinate rational angle retains a
factor257in the reduced denominator, whereas the coherent cyclic
component's denominator divides4q. Since257does not divide any of the
six prescribed q, even equality up to sign is impossible across components.
This proves disjointness and total count q+9=N.

For R, global inversion of its order18base has no fixed parameter because
2v=−1mod6has no solution; additional cosine collisions must still be
checked. Exact base counts are retained for all12choices. Its cyclic
component has qdistinct nodes because its first phase is nonspecial;
the same257denominator argument excludes intersection with the base's
denominator12. These arguments do not classify general unions. A component
annihilator alone cannot kill the union, and a common free half-period
action has not been assumed.

[Selected inputs](evidence/uc3-selected-inputs.json) retain all15actual
selected rational constructions, with hashes of the four source receipts.
[uc3_independent.py](code/uc3_independent.py) reconstructs every subgroup
by generator-power closure, folds the union exactly and evaluates actual
cosine monomials at TWO distinct fresh splitting primes near1.3e9. All
15sets have exactlyNnodes and full rank at both primes, including every
M/Rdegree3..8and the twoS/oneFselected sets.

The checker validates primality by deterministic Miller–Rabin below2^64
and validates exact root order using every prime divisor of the angle
denominator. The cyclotomic homomorphism therefore lifts nonzero minors
to characteristic zero. NumPy products are guarded by p<1.9e9, so p²and
subtract-products fit signed64-bit. Python integers handle accumulators.

Quality is independently recomputed using direct cos(alpha·theta) products,
linear solves and21/41angular mesh slices. QR/Leja recipes are rebuilt in
their frozen order, with an independently implemented Chebyshev recurrence
for QR selection; quality evaluation does not import producer code. Maximum
selected-sample difference is3.911e−11, maximum control difference4.264e−14.
Maximum selected condition2is482.56and inverse residual5.70e−13. All guards
pass. These are MEASURED lower samples, not certified suprema or growth laws.

The cubic Ssamples reproduce9.788798269/9.807107748; quintic Sreproduces
55.915123453on both meshes, and Freproduces51.763015722on both. Every
new n>=4selected instance loses to same-degree QR on both meshes. Thus the
specified promising-performance claim fails while all finite positive rank
statements survive. M/R's n6andn7Leja losses meet the written selector kill;
n8is disclosed post-kill validation. This says nothing universal about
folded/mixed constructions or continuum norms.

The [comparison receipt](evidence/uc3-comparison.json) checks current code
pins, raw identities, every support/count/exact-rank result and qualities.
It also INSPECTS the retained M/Rraw rows:512distinct starts per degree,
at most3refinements with<=240evaluations each, all asserted counts, and the
registered maximum-score/tolerance/lexicographic selection. This inspection
is not an independent replay of all512modular screens or optimizer paths.

## Evidence and remaining scope

| Own receipt | Bytes |
|---|---:|
|[S inverse census](evidence/uc3-s-census.json)|3250|
|[S matching split](evidence/uc3-s-matching.json)|1549|
|[F count/trace census](evidence/uc3-f-census.json)|3952|
|[F exact completion](evidence/uc3-f-exact.json)|4014|
|[All selected nodes/qualities/controls](evidence/uc3-selected-check.json)|14864|
|[Cross-comparison/current pins](evidence/uc3-comparison.json)|5427|

Each receipt records the actual current code SHA256, command and raw
path/size/hash. Source snapshots are retained in unique/tmpdirectories;
the code asserts no source mutation during its run. The Fexact receipt
pins both imported own modules. Large raw outputs are regenerate-only,
not archived or required as unexplained premises: committed finite
definitions/checkers regenerate their full mathematical scope. No prose
is pinned by a checker.

No unresolved mathematical discrepancy was found within this scope.
The exact cubic explanation, complete Sfinite predicate classification,
complete registered Fclassification and all15selected positive witnesses
have their separate executed checks. No all-degree stable construction,
positive cubature property, global optimum or general folded/mixed exclusion
is established. Required Claude substantive review remains pending.
