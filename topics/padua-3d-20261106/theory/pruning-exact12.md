# PD-T?padua-3d-20261106-pruning-exact12 — a 546-node exact cosine determining set

ID kind: PD-T. Aliases: pruned12 canonical-ID witness; exact algebraic
degree-twelve LS support. Split from: none; this exact finite rank claim
is distinct from P3's measured quality claim. Split into: none.
No final ID allocated.

## Statement

Let J be the ordered `ids` list in the essential payload
[pdpr-pruned12-nodes.json](../evidence/pdpr-pruned12-nodes.json), 7554 bytes,
SHA256 `ddf19d3d0ee13125ee9db4a6f6175ed2279ad5b2272aa06a456d1e572df3d0cd`.
Decode J by the canonical integer convention below and interpret coordinates
as **exact real cosines**. The resulting X consists of 546 distinct points
of [-1,1]^3 and is determining for the real total-degree space Pi_12:

`p in Pi_12 and p|X=0 imply p=0`.

Equivalently, its 546-by-455 evaluation matrix has full column rank 455.
Consequently, for every real data vector y in R^546 and every positive
diagonal weight matrix W, weighted least squares on Pi_12 has a unique
coefficient minimizer. This is not arbitrary 546-value interpolation:
546>455, so arbitrary data need not be exactly interpolable.

## Definitions and assumptions

Pi_12={p in R[x1,x2,x3]: total degree(p)<=12} has dimension
N=binom(15,3)=455. Orders are exactly m=(12,13,13). Enumerate triples
lexicographically by i1 first, then i2, then i3, with i3 fastest:

```
0<=i1<=12, 0<=i2<=13, 0<=i3<=13;
retain iff i1%2 == i2%2 == i3%2.
```

An ID is a **zero-based offset in this filtered list**, not in the full
tensor box. The full list has 7*7*7+6*7*7=637 entries. For every j in J,
let i(j) be that entry and define

`x(j)=(cos(pi*i1/12), cos(pi*i2/13), cos(pi*i3/13))`.

J has 546 strictly increasing integer IDs in [0,636]. Its values and
order are completely stored in the essential payload. The theorem does
not require running backward elimination or retrieving temporary arrays
to define X. The exact cosine interpretation is part of the statement;
it is not the exact dyadic interpretation of any rounded coordinate array.

Trusted execution dependencies are the committed payload/checkers and
ordinary Python integer/JSON arithmetic plus NumPy's exact signed-int64
elementwise operations under the bounds below. No floating rank threshold,
conditioning estimate, optimizer result or norm theorem is a premise.

## Status and disposition

Overall status: **PROVED, computer-assisted finite statement**.

| Part | Status | Evidence |
|---|---|---|
| 546 exact cosine nodes are distinct, in the cube and Pi_12-determining; positive-weight LS is unique | PROVED | Written reduction and two independently executed exact full-rank checks |
| Numerical amplification, covariance, errors, conditioning and cost | MEASURED in separate P3 record | No certification or status transfer from rank |

Candidate disposition: retained finite support. The minimum-node and
degree-uniform quality targets remain OPEN. A complete supplementary
independent exact check is recorded; required formal Claude audit is a
separate process, not claimed here.

## Dependencies and essential evidence

The general ring/finite-field implication is the already written, frozen
[pruning certificate reduction](../pruning-certificate.md), specializing
[T8 root-of-unity certification](t8-r06-certification.md). Its exact
hypotheses are verified here; a short proof is repeated below to make the
finite claim checkable. No uninspected imported norm theorem is used.

The essential geometry, modular parameters and producer minor-row IDs are
in the payload above. Actual checker/evidence identities inspected here:

| File | Bytes | SHA256 |
|---|---:|---|
| [Producer/checker](../code/pdpr_certify.py) |15414|`0b4a815fba363b437d3ce19d6d8ceaeac21ecac544e8c53c00561311bb748e13`|
| [Producer receipt](../evidence/pdpr-pruned12-check.json) |3939|`a194732c5517e16f5a4cbbab57f82ef5e43c74c98065eeae778a3b74890fca6f`|
| [Independent checker](../pruning-review/check_certificate.py) |11170|`06f944677ab09c974b0efa8100e4400204f068b158dd81aecbff43c386b33c16`|
|[Independent receipt](../pruning-review/certificate12.json) |9081|`14ab1f794391d7eec81b64cf7c2c18e75d68c715029e11bfd8a59702953cc32d`|

Producer row = historical degree-12 creator revision at e761a12bcc7acfbf47dc6db77592854211931df5; the current shared checker is 16024 bytes, SHA256 `ab3b092cbf29d97ec456f6891cfc109d0f8dbe7652516ea961b301318f230241` ([compatibility](../pruning-artifacts.md#degree16-essential-artifact-and-backward-compatibility)). Audit04 note, 2026-11-08.


The producer's portable `verify` mode also validates the payload's pinned
[P3 receipt](../evidence/pdpr-frontier12.json), 9223 bytes, SHA256
`8eae53503c89eeb059d023f1e9effd679392fbeecd7897683475408de94b607a`.
That provenance check is not a mathematical rank assumption. These small
repository files suffice to replay the exact claim; no /tmp data or Git
object retrieval is needed by `verify` or `load`.

## Proof

The integer decoder verifies all ID bounds/counts/parities. Its different
triples give different real points, since cos(theta) is strictly decreasing
on [0,pi]. Each coordinate lies in [-1,1], proving cardinality and domain.

Compute L=lcm(24,26,26)=312=2^3*3*13. With zeta=exp(2*pi*i/312), the
three coordinates are `(zeta^e+zeta^(-e))/2`, with exponents
`e=(13*i1,12*i2,12*i3)`. Thus they lie in R=Z[zeta,1/2].

The producer uses every unscaled product-Chebyshev column
`T_a(x1)T_b(x2)T_c(x3)`, a+b+c<=12, in degree order
`d=0..12,a=0..d,b=0..d-a,c=d-a-b`. There are 455 columns. They form a
real basis of Pi_12: each T_a has nonzero leading term of degree a, so
the transformation from total-degree monomials is triangular with
nonzero diagonal. Orthonormal sqrt(2) factors from measured OLS are
nonzero real column scalings and are unnecessary in this rank proof.

The producer verifies prime p=313 by complete integer trial division
through isqrt(313), with p odd and p=1 mod312. Its rho=10 satisfies

`rho^312=1; rho^156=312, rho^104=214, rho^24=103 (mod313)`.

The latter three values are not 1, so rho has exact order312, using the
distinct prime divisors 2,3,13 of312. Since p does not divide312, t^312-1
has no repeated roots modulo p. Its cyclotomic factorization and rho's
order imply Phi_312(rho)=0. Substitution zeta->rho therefore defines a
ring homomorphism R->F_313, extending integer reduction and sending
1/2 to inverse(2).

The checker evaluates actual modular coordinates
`(rho^e+rho^(-e))/2` and the Chebyshev recurrence exactly. It rebuilds the
455-row minor specified by `certificate.minor_row_ids` in the essential
payload; these are distinct members of J in their recorded order. Exact
square elimination returns

`det(D_p)=106 mod313`, which is nonzero.

Determinants commute with the ring homomorphism. Consequently det(D)
cannot be zero in R or in its given complex embedding. Its entries are
real, so D is a nonsingular real 455-by-455 minor. The full evaluation
matrix E therefore has rank455.

For every positive diagonal W and nonzero b in R^455,
`b^T E^T W E b=sum_i w_i (Eb)_i²>0`. Thus E^T W E is positive definite,
and the weighted least-squares minimizer for any y is uniquely
`b=(E^T W E)^(-1) E^T W y`. Full column rank proves determination, not
surjectivity onto R^546. This completes the exact finite statement.

## Actual checks and independent execution

The producer build at 2026-11-07 09:48:29–09:48:30 UTC verified the
selected scientific checkpoint's identity **before** its first rank query,
exported the essential payload and checked the stated square minor.
The producer receipt records its exact command, versions, hashes and
1.139154235 CPU seconds; this timing is not part of the proof. It also
records a separate repository-shaped-copy `verify` execution that needed
no raw construction data. One rank query succeeded at p313; no selected
support changed during prime/minor discovery.

The distinct checker actually executed at 09:52:35–09:52:36 UTC. It
independently decodes the filtered list using mixed-radix ordinals, uses
the complete monomial basis in lexical(a,b,c) order, and selects a different
verified field: prime937=3*312+1 and rho15. Its exact order residues are

`rho^312=1; rho^156=936, rho^104=322, rho^24=36 (mod937)`.

It finds rank455, then rebuilds its own recorded 455-row square minor
and verifies determinant702 modulo937. Different residues across the
different bases/fields are expected. This independently executed positive
minor is a second proof of the same real full-column-rank conclusion.
Both checkers prove primality by complete trial division and verify all
required root-order tests; no probable-prime or float rank inference.

Both use reduced signed-int64 residue products, staged pairwise basis
multiplication and elementwise outer-product elimination, never an
unreduced dot-product accumulation. At the larger prime937, a single
residue product is at most936²=876096 and elimination differences have
absolute bound877032, far below 2^63. Python integers handle modular
powers/inverses and determinant products. Producer Chebyshev recurrence
reduces its product before doubling. Its square-minor verification
accounts for any pivot permutation relative to the stored row order.

The independent receipt also records actual producer `verify`/`load` in
a copy containing only checker, payload and P3 receipt, with no raw
directories; it rejects eight malformed mutations: duplicate/boolean/
out-of-range IDs, bad count, wrong schema/root, composite prime and wrong
determinant. Its comprehensive provenance-linkage command also reads
the original raw scientific files; that extra historical linkage check
is distinct from the repository-only exact-rank replay.

A current repository-only replay command, with a fresh output path, is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/pdpr_certify.py verify --payload topics/padua-3d-20261106/evidence/pdpr-pruned12-nodes.json --check /tmp/UNIQUE-pruned12-rank.json
```

This is a reproduction command, not an additional execution claimed by
this writer. Actual producer/independent commands are retained in their
receipts. The proof writer read both complete sources, payload and
receipts and checked their local byte/hash identities; it did not rerun
rank, construction or quality measurements.

## Linkage, sources and limitations

Producer and independent checks agree that the 546 IDs are the P3 primary
A-m546 checkpoint's IDs, in observation order. Under the recorded NumPy
cosine recipe, regenerated little-endian binary64 coordinates match the
checkpoint and assessment arrays, SHA256
`d02960d3658b8901e47479d6ffb058ca9cfd9b96f0fbe3f188b15917959915f4`.
This is measured byte linkage, not equality of rounded numbers with exact
cosines. The theorem proves no exact rank of the separately interpreted
dyadic rounded matrix and no certified perturbation/norm transfer.

Numerical quality belongs to [P3 frontier](pruning-p3-frontier.md),
**MEASURED** under its physical-noise/measure/operator assumptions. Rank
does not certify amplification, conditioning, covariance, approximation
error, optimality, timing or degree-uniform stability. There is no
N-node construction or all-degree theorem here. The older
[455-node U2 exact-dyadic witness](u2-degree12-unisolvence.md) remains a
different unchanged set, exact interpretation and proof.

Sources are elementary cyclotomic specialization, interpolation linear
algebra and the explicitly linked local reduction. Known-method gate
coverage does not supply any unchecked source theorem as a proof premise;
no new source-paper verification, novelty or priority is claimed.

## Open items and history

Formal Claude audit and root's usual ID/publication treatment remain
separate. No further construction or raw retrieval is needed for the
specified exact-rank replay. Certified quality, rounded-node perturbation
control and degree-uniform theory remain open, outside this statement.

2026-11-07, Codex mathematical worker, configured gpt-6.1-sol xhigh;
provider metadata unexposed. Rules/input6d894d50 in this campaign;
root's completed certificate task follows P3 publication
562309744165cd601a489510ddc8026d933b1b27. This durable exact claim is based
on the completed independent receipt, not the earlier unexecuted schema.
Artifact verification consumes0 additional research rounds: P3's
construction was already counted. This writer changed only this new
file, without experiments, source mutation, Git or shared-record edits.

## Dated independent repository-only replay addendum

2026-11-07, Codex coordinator integration: the distinct reviewer additionally
executed its standalone lexical-monomial exact check in a disposable directory
with only the payload and two auditor files, without producer imports, Git,
raw data or the P3receipt. [Actual replay receipt](../pruning-review/certificate12-algebra.json)
records prime937/root15/rank455/minor702 and copied-source identities. This
adds a repository-only independent exact replay path; the earlier comprehensive
measurement-provenance command keeps its stated raw-data dependency. No
mathematical claim, old execution identity or measured quality is changed.
