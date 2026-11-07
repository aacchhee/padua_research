# PD-T?padua-3d-20261106-pruning-exact16 — a 1163-node exact cosine determining set

ID kind: PD-T. Aliases: pruned16 canonical-ID witness; A1163 exact support.
Split from: none; this finite exact-rank claim is distinct from P4's
measured quality statement. Split into: none. No final ID allocated.

## Statement

Let J be the ordered `ids` list in the essential payload
[pdpr-pruned16-nodes.json](../evidence/pdpr-pruned16-nodes.json), 12581 bytes,
SHA256 `ef79d6094cbb1655c82c66666b0fef440990ca5a3059dab1465c03d86f5ebc84`.
Decode those IDs by the integer convention below, interpreting coordinates
as **exact real cosines**. The resulting X has 1163 distinct points in
[-1,1]^3 and is determining for the real total-degree space Pi_16:

`p in Pi_16 and p|X=0 imply p=0`.

Equivalently, its 1163-by-969 evaluation matrix has column rank969.
For every y in R^1163 and every positive diagonal weight matrix W,
weighted least squares on Pi_16 therefore has a unique coefficient
minimizer. This does not interpolate arbitrary1163 data values: the
polynomial space has dimension969<1163.

## Definitions and assumptions

Pi_16={p in R[x1,x2,x3]: total degree(p)<=16}, with
N=binom(19,3)=969. Set m=(16,17,17). Enumerate triples by increasing
i1, then i2, then i3 (i3 fastest), retaining precisely

`0<=i1<=16, 0<=i2<=17, 0<=i3<=17; i1%2 == i2%2 == i3%2`.

Each ID is a zero-based offset in this **filtered** list, not a flattened
index into the full tensor box. Its full count is
9*9*9+8*9*9=1377. The payload has1163 strictly increasing integer IDs
in [0,1376]. If i(j) is the triple at offset j, define

`x(j)=(cos(pi*i1/16), cos(pi*i2/17), cos(pi*i3/17))`.

The committed IDs and orders completely specify X. Neither construction
replay nor temporary arrays are needed to define it. The exact cosine
interpretation is part of the theorem; it is not the exact dyadic
interpretation of rounded coordinates.

Trusted execution dependencies are the specified payload/checkers and
Python integer/JSON arithmetic with NumPy signed-int64 elementwise modular
operations under the bounds below. No floating rank tolerance, optimizer,
conditioning estimate, quality sample or imported norm theorem is a premise.

## Status and disposition

Overall status: **PROVED, computer-assisted finite statement**.

| Mathematical part | Status | Evidence |
|---|---|---|
| The1163 exact cosine points are distinct, in the cube and Pi_16-determining; positive-weight LS is unique | PROVED | Written reduction, essential payload and two actual independent exact full-rank checks |

Candidate disposition: retained finite support. Numerical quality remains
**MEASURED** in [P4 transfer](pruning-p4-transfer.md); it is not promoted
by this proof. Minimum-node and degree-uniform quality targets remain
OPEN. The completed supplementary exact check does not assert completion
of the separate formal Claude audit.

## Dependencies and inspectable evidence

The frozen [certificate reduction](../pruning-certificate.md) specializes
the existing [T8 root-of-unity proof](t8-r06-certification.md). Its
specific hypotheses are verified here; the short argument is given below.
No external source theorem or new global construction claim is imported.

The essential payload above contains every node ID and the producer's
ordered969-row minor. Inspected source/evidence identities:

| File | Bytes | SHA256 |
|---|---:|---|
| [Producer/checker](../code/pdpr_certify.py) |16024|`ab3b092cbf29d97ec456f6891cfc109d0f8dbe7652516ea961b301318f230241`|
| [Producer receipt](../evidence/pdpr-pruned16-check.json) |6981|`4fef2c5480157d564b5788174ec4d5a3b5e6a11b77b9807a43c2dc4dbcfb859f`|
| [Independent checker](../pruning-review/check_certificate.py) |11170|`06f944677ab09c974b0efa8100e4400204f068b158dd81aecbff43c386b33c16`|
| [Independent receipt](../pruning-review/certificate16.json) |13942|`1db03bf1b926ae4e045b2705479666523b466d8d0cea0194cac683f66100582d`|

The portable producer additionally checks the payload's pinned
[P4 receipt](../evidence/pdpr-transfer16.json), 10883 bytes, SHA256
`621d1aaf59f1074881ecf1c8119f0878ce22c94489beb07bd88ea94df33db22c`.
That provenance guard is not a rank-proof assumption. Producer `verify`
and `load` require no raw scratch files or Git objects. The small committed
payload, checker and pinned receipt suffice for repository-only replay.

## Proof

Integer validation checks every ID/count/range/parity. Different retained
triples yield different real points, because cosine is strictly decreasing
on [0,pi]. All coordinates are in [-1,1], establishing domain/cardinality.

Compute L=lcm(32,34,34)=544=2^5*17. Let zeta=exp(2*pi*i/544).
Coordinates are `(zeta^e+zeta^(-e))/2`, with
`e=(17*i1,16*i2,16*i3)`. Thus they belong to R=Z[zeta,1/2].

Use every unscaled product-Chebyshev column `T_a(x1)T_b(x2)T_c(x3)`
with a+b+c<=16, ordered by d=0..16, a=0..d, b=0..d-a, c=d-a-b.
These969 columns form a real basis of Pi_16: each T_a has a nonzero
leading term of degree a, giving a triangular change from total-degree
monomials with nonzero diagonal. The orthonormal factors in measured OLS
are nonzero real column scalings; no sqrt(2) evaluation is needed in F_p.

The producer verifies p=5441=10*544+1 is prime by complete integer trial
division through isqrt(p), and is odd. Its rho=4639 satisfies

`rho^544=1; rho^272=5440, rho^32=2670 (mod5441)`.

The latter two values are not1, establishing exact order544 using its
distinct prime divisors2 and17. As p does not divide544, t^544-1 has
no repeated roots modulo p. Its cyclotomic factorization and rho's exact
order imply Phi_544(rho)=0. Substitution zeta->rho defines a ring
homomorphism R->F_5441, extending integer reduction and sending1/2 to
inverse(2).

The checker evaluates coordinates `(rho^e+rho^(-e))/2` and the unscaled
Chebyshev recurrence exactly. It rebuilds the square969-row minor D
specified by `certificate.minor_row_ids` in the payload, verifies that
these distinct ordered IDs belong to J, and obtains

`det(D_p)=330 mod5441`, nonzero.

Determinants commute with ring homomorphisms; det(D) is therefore nonzero
in R and its given complex embedding. D has real entries, so it is
nonsingular as a real matrix. The full1163-by-969 matrix E has rank969.

For any positive diagonal W and nonzero b in R^969,
`b^T E^T W E b=sum_i w_i (Eb)_i²>0`. Thus E^T W E is positive definite,
and the unique weighted LS minimizer for any y is
`b=(E^T W E)^(-1) E^T W y`. This proves determination and unique LS,
without surjectivity onto R^1163. The exact finite statement follows.

## Actual verification and independent execution

The producer's recorded build ran at 2026-11-07 10:07:37–10:07:46 UTC,
after checking the exported IDs against the fixed P4 primary checkpoint,
and used9.178377628 CPU seconds. Its single prime rank attempt succeeded
at p5441; no candidate support was changed during prime/minor discovery.
The receipt also records an actual repository-shaped-copy `verify` at
10:07:58–10:08:01 UTC, using2.690262208 CPU seconds with no raw data.
The same source separately reverified the unchanged degree12 payload;
that backward-compatibility check does not alter its earlier theorem.
Recorded timings are execution provenance, not proof premises or bounds.

The independent checker actually completed at10:09:02–10:09:10 UTC,
using5.485294878 CPU seconds. It independently decodes the parity list
using mixed-radix ordinals, then evaluates the complete monomial basis
in lexical(a,b,c) order at a different verified compatible prime:

`p'=6529=12*544+1, rho'=58`,

`rho'^544=1; rho'^272=6528, rho'^32=816 (mod6529)`.

It finds rank969, rebuilds its own specified969-row square minor and
verifies determinant1257 modulo6529. This is a second independently
executed nonzero-minor proof. Equal residues across the different fields
and bases are neither expected nor required. Both sources verify exact
primality and root order; neither uses a probabilistic or floating rank test.

Both use signed-int64 residues with staged pairwise products and reduced
elementwise outer-product elimination, avoiding dot-product accumulation.
At the larger prime6529, a residue product is at most6528²=42614784;
elimination differences have absolute bound42621312, far below2^63.
Producer Chebyshev recurrence reduces the product before doubling.
Python integers handle powers/inverses/determinant products, and square
verification accounts for pivot permutation relative to stored row order.

The independent receipt additionally records matching P4 checkpoint/path/
assessment IDs and coordinate bytes, and actual producer `verify`/`load`
in a copy containing only checker, payload and P4 receipt, with no raw
directories. Eight malformed mutations were rejected: duplicate/boolean/
out-of-range IDs, bad count, wrong schema/root, composite prime and wrong
determinant. Its comprehensive historical provenance command also reads
raw scientific files; that extra linkage review is separate from portable
exact-rank replay. No temporary scientific file is needed to define X.

A repository-only replay, with a fresh output path, is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/pdpr_certify.py verify --payload topics/padua-3d-20261106/evidence/pdpr-pruned16-nodes.json --check /tmp/UNIQUE-pruned16-rank.json
```

This command is supplied for reproduction, not claimed as a fresh execution
by this writer. Actual producer/independent commands are in their receipts.
The proof writer read the sources and completed records and checked local
byte/hash identities, without rerunning rank, construction or quality.

## Linkage and limitations

The exported1163 IDs equal the P4 primary A-m1163 checkpoint's IDs in
observation order. Under the stated NumPy cosine recipe, regenerated
little-endian binary64 coordinates match checkpoint and assessment arrays,
SHA256 `2709ac59b448f29ae12901fe5f40484e5c6ac81aca453bd52f30d31e1969dc1e`.
This is measured byte linkage; rounded numbers are not the exact cosines
in the theorem. No exact rank claim about the separately interpreted
dyadic rounded matrix or certified perturbation transfer is established.

All numerical amplification, noise covariance, conditioning, function
error, costs and finite comparisons remain in the **MEASURED**
[P4 record](pruning-p4-transfer.md). A nonzero modular minor gives no
useful real determinant lower bound, stability margin, norm certificate,
optimality or asymptotic rate. Zero modular rank evidence would have been
inconclusive, not a real-rank upper bound. This is not an N-node set or an
all-degree construction theorem.

The [degree12 pruning witness](pruning-exact12.md) and older
[455-node U2 exact-dyadic witness](u2-degree12-unisolvence.md) retain their
own sets, exact interpretations and proofs. No source paper or inherited
unchecked norm theorem is a premise. This is a known finite certification
method, without priority or new-global-theorem claims.

## Open items and history

Formal Claude audit and root's normal ID/publication treatment remain
separate. Certified quality, rounded-node perturbation control and
degree-uniform theory remain open outside this finite statement.

2026-11-07, Codex mathematical worker, configured gpt-6.1-sol xhigh;
provider metadata unexposed. Rules/input6d894d50 in this campaign;
application follows P4 publication e761a12bcc7acfbf47dc6db77592854211931df5
and the actual completed independent receipt. Verification/export consumes0
additional research rounds: P4 construction was already counted. Only
this new theory file was changed by this worker; no experiment, source,
old-theory, shared-record or Git mutation.

## Dated portable independent exact-replay addendum

2026-11-07, coordinator integration: [the independent algebra-only receipt](../pruning-review/certificate16-algebra.json)
records an actual disposable three-file replay using only the payload and
two auditor files. It reads no producer, scientific receipt, Git or raw data
and returns prime6529/root58/monomial rank969/minor1257. The separate full
measurement-linkage command retains its documented raw dependency. This
adds portable independent verification, not a quality theorem or new claim.
