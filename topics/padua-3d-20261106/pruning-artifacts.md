# Exact pruning artifact delivery: degrees12 and16

Rules read at `46d1e2b9356e0e5cc385615906c500684cd9ad77`.
Codex gpt-6.1-sol medium technical certificate worker; provider runtime
metadata unexposed. Root owns Git/shared records.
This is verification/export of the already constructed P3 primary candidate,
**0 additional research rounds**, not a new construction or quality search.
No novelty gate is needed for this known certificate/export route; the
existing pruning gate and [proof reduction](pruning-certificate.md) apply.

The essential [payload](evidence/pdpr-pruned12-nodes.json) delivers all **546
canonical parity IDs**, orders `(12,13,13)`, dimension **455**, exact cosine
geometry, a nonzero 455-row minor and source/provenance pins. IDs are offsets
in the parity-filtered lexicographic product, with the third index fastest.
They remain sorted and fixed before any modular query. The payload is7554
bytes, SHA256
`ddf19d3d0ee13125ee9db4a6f6175ed2279ad5b2272aa06a456d1e572df3d0cd`.
It contains no bulk coordinate encoding, factorization or raw optimizer state.

The original degree12 [checker](code/pdpr_certify.py) revision, SHA256
`0b4a815fba363b437d3ce19d6d8ceaeac21ecac544e8c53c00561311bb748e13`,
proves exact full column rank via unscaled product-Chebyshev columns.
It checks prime313 by complete trial division, `L=312`, and exact-order
`rho=10`; residues at L/2,L/3,L/13 are312,214,103. The specified ordered
455-row minor has determinant **106 mod313**, rebuilt separately as a
square matrix. The first eligible prime succeeded; no failed prime or
rank attempts were discarded. Search bounds and the attempt ledger are
inside the payload. Modular failures would be inconclusive about real rank.

Arithmetic uses NumPy int64 elementwise outer products with reduction
before subsequent products, never unreduced dot-product accumulation.
The checker enforces `p<2^30`, verifies all order prime factors, and checks
IDs/counts/exponents/minor membership. The proved reduction supplies the
implication to an exact real **determining set and unique least-squares
fit**, including any positive fixed row weights. Since546>455, this does
not claim interpolation of arbitrary546 data. Numerical conditioning,
continuous sup norms and finite P3 quality inequalities stay MEASURED.
The [independent Astra check](pruning-review/certificate12.json) passes:
its own decoder and lexical monomial basis give rank455 with verified
prime937, root15 and minor determinant702. It independently links all546
IDs and reconstructed binary64 nodes to the P3 checkpoint/path/assessment,
passes verify/load from a copy with no raw files, and rejects eight malformed
payload mutations. This establishes the exact-cosine determining-set
certificate scope, recorded in the [PROVED degree12 application](theory/pruning-exact12.md);
it certifies no measured quality, conditioning or norm.

## Original-source and measured-coordinate linkage

Build uses the published P3 result commit
`562309744165cd601a489510ddc8026d933b1b27` and unchanged scientific-source
commit `46d1e2b9356e0e5cc385615906c500684cd9ad77`.
It checked the P3 receipt's full details/inventory identities, every raw
inventory member, every executed snapshot, and snapshot bytes against a
matching blob at that scientific source commit. Source basename collisions
are resolved by exact blob bytes/hash; no runtime source is substituted.

The primary546 checkpoint IDs equal the original A-path's m546 IDs;
checkpoint nodes equal the assessed map nodes byte for byte. Raw recipe
indices equal an independently implemented canonical parity enumeration.
Reconstruction by `np.cos(np.pi*indices/np.array(orders))` equals the actual
checkpoint nodes bitwise and matches the full-precision assessment's
coordinate hash. The payload records this little-endian binary64 hash and
NumPy version as a separate **MEASURED** linkage. Exact geometry and the
modular proof do not depend on libm reproducing those rounded bytes on
other platforms. Verify reports that platform-sensitive hash comparison
separately from exact rank.

## Commands actually executed

All scientific-source raw paths remain regeneration-only, not archival.
The old scientific receipt/source/artifacts were unchanged. No payload
was built before root authorized the short exclusive CPU window. A first
build stopped before a rank query at an ambiguous `c3_rank.py` basename;
the source matching repair preceded the successful build. Candidate IDs
never changed. The original degree2 engineering selftest proved rank10
and rejected an invalid order root in0.001249CPU; this is engineering only.

With `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1`:

```sh
python topics/padua-3d-20261106/code/pdpr_certify.py build --degree 12 --publication 562309744165cd601a489510ddc8026d933b1b27 --receipt topics/padua-3d-20261106/evidence/pdpr-frontier12.json --payload topics/padua-3d-20261106/evidence/pdpr-pruned12-nodes.json --check topics/padua-3d-20261106/evidence/pdpr-pruned12-check.json
```

Build started09:48:29.784735UTC and ended09:48:30.957656UTC on2026-11-07,
using1.139154CPU/1.172946wall seconds. Python3.12.14, NumPy2.3.5;
no random seeds. The single [check receipt](evidence/pdpr-pruned12-check.json)
contains actual commands, UTC/thread/version/source/payload identities,
build result and the subsequent clone-like verification result.

A fresh directory `/tmp/pdpr-cert-clean12-20261107a` was populated with
only the checker, payload and original P3 receipt under their repository
relative paths. It had no Git checkout or raw NPZ/details/inventory files.
This actual command passed at09:48:41UTC in0.271046CPU/0.271054wall seconds:

```sh
python /tmp/pdpr-cert-clean12-20261107a/topics/padua-3d-20261106/code/pdpr_certify.py verify --payload /tmp/pdpr-cert-clean12-20261107a/topics/padua-3d-20261106/evidence/pdpr-pruned12-nodes.json --check /tmp/pdpr-cert-clean12-20261107a/verify.json
```

That verification reads the payload, local pinned scientific receipt and
checker only. It reconstructs geometry and computes the nonzero exact
minor without the build's raw sources. This is developer re-execution,
not an independent audit. The standard repository-only rerun is:

```sh
python topics/padua-3d-20261106/code/pdpr_certify.py verify --payload topics/padua-3d-20261106/evidence/pdpr-pruned12-nodes.json
```

For numerical use, import `code/pdpr_certify.py` and call
`load(payload_path)` to reconstruct the physical M-by-3 node array.
Evaluate a total-degree12 polynomial model by an ordinary stable LS
solver on those nodes; this artifact supplies no stored dense coefficient
map and makes no hardware-independent timing claim.

Formal Claude handoff remains root's separate obligation; no new primary
status or registry ID is assigned here.


## Degree16 essential artifact and backward compatibility

After P4's quality PASS, root authorized export of its already constructed
primary1163-site candidate from the published P4 input/result commit
`e761a12bcc7acfbf47dc6db77592854211931df5`. This is again **0 additional
research rounds**. The [degree16 payload](evidence/pdpr-pruned16-nodes.json)
is12581bytes, SHA256
`ef79d6094cbb1655c82c66666b0fef440990ca5a3059dab1465c03d86f5ebc84`.
It contains every one of the1163 sorted canonical IDs, orders `(16,17,17)`,
N969, exact-cos geometry and a specified969-row nonzero minor. No ID changed
after any modular query. Source/inventory/checkpoint/path/recipe/map hashes
and bitwise actual-node linkage were checked exactly as for degree12.

The current shared checker is16024bytes, SHA256
`ab3b092cbf29d97ec456f6891cfc109d0f8dbe7652516ea961b301318f230241`.
It maps official source/result commits by degree:12 to5623097 and16 to
e761a12. It also accepts degree12's original46d1e2b scientific-source pin,
preserving the unchanged degree12 payload and historical creator receipt.
Historical creator hashes identify the actual earlier execution; they are
not required to equal a later shared checker revision. The original
payload/check12 bytes remain unchanged. The new revision additionally
requires integer determinant metadata and rejects an unsafe prime size
before primality trial division.

Degree16 uses L544=2^5*17 and verified prime5441. Root4639 has exact order544:
its L/2 and L/17 residues are5440 and2670, and its Lth power is1. The first
eligible prime succeeds with rank969 and rebuilt square-minor determinant
**330 mod5441**; there are no failed prime/root/rank attempts. Composite
numbers preceding that prime are deterministic search rejections, not
failed rank queries. The existing reduction proves the exact-cos geometry
is determining with a unique positive-weight LS fit; the independent
replay obligation is now completed. Since1163>969, arbitrary1163 data
are not thereby interpolable. Numerical quality, dyadic-rounded matrix
rank, conditioning and continuous bounds remain outside this certificate.
The [independent degree16 check](pruning-review/certificate16.json) passes
with its own canonical decoder and lexical monomial basis at different
verified prime6529 and root58: rank969, minor determinant1257. It checks
all P4 raw IDs/coordinates/assessment linkage, repo-only producer verify/load
and eight malformed payload mutations in5.485CPU. The separate
[algebra-only replay](pruning-review/certificate16-algebra.json) passes in
2.674CPU from the payload and two auditor files, with no producer, producer
receipt, Git or raw files. The [PROVED degree16 application](theory/pruning-exact16.md)
records precisely the exact ideal-cosine Pi16-determining and unique-LS
scope. Producer binary64 linkage remains MEASURED; numerical quality,
conditioning and continuous norms remain uncertified.

Root granted an exclusive CPU window after P4's independent numerical
review released its window. With the same three thread variables set to1,
the actual build was:

```sh
python topics/padua-3d-20261106/code/pdpr_certify.py build --degree 16 --publication e761a12bcc7acfbf47dc6db77592854211931df5 --receipt topics/padua-3d-20261106/evidence/pdpr-transfer16.json --payload topics/padua-3d-20261106/evidence/pdpr-pruned16-nodes.json --check topics/padua-3d-20261106/evidence/pdpr-pruned16-check.json
```

It started10:07:37.332152UTC and ended10:07:46.549175UTC on2026-11-07,
using9.178378CPU/9.217048wall seconds, Python3.12.14, NumPy2.3.5, no seeds.
The single [degree16 check receipt](evidence/pdpr-pruned16-check.json),
6981bytes, contains the build, actual portable verify and unchanged-degree12
backward verify commands, identities, UTC/timings and engineering ledger.

The clean directory `/tmp/pdpr-cert-clean16-20261107a` contains only the
new checker and the12/16 payloads plus their scientific receipts under
repository-relative paths. There are no raw files or Git checkout there.
The following actual CLI calls both pass under the same thread settings:

```sh
python /tmp/pdpr-cert-clean16-20261107a/topics/padua-3d-20261106/code/pdpr_certify.py verify --payload /tmp/pdpr-cert-clean16-20261107a/topics/padua-3d-20261106/evidence/pdpr-pruned16-nodes.json --check /tmp/pdpr-cert-clean16-20261107a/verify16.json
python /tmp/pdpr-cert-clean16-20261107a/topics/padua-3d-20261106/code/pdpr_certify.py verify --payload /tmp/pdpr-cert-clean16-20261107a/topics/padua-3d-20261106/evidence/pdpr-pruned12-nodes.json --check /tmp/pdpr-cert-clean16-20261107a/verify12.json
```

Degree16 portable verification used2.690262CPU/2.690316wall seconds at
10:07:58–10:08:01UTC. The new checker then reverified unchanged degree12
rank455/determinant106 and its measured coordinate hash in0.293356CPU/
0.293362wall seconds at10:08:01UTC. These are developer re-executions,
not the independent checker runs.

Before freezing this source, its degree2 synthetic selftest passed in
0.000948CPU and an importlib-driven Python mutation loop rejected nine
malformations in0.000535CPU: boolean degree/ID, duplicate ID, bad count,
unknown schema, invalid root, composite prime, float determinant, and an
overflow-sized prime. The loop constructs the same full degree2 record,
certifies it once, deep-copies each mutation, and requires verify() to
raise ValueError/TypeError/KeyError; all cases are named in the receipt.
The final successful engineering command was:

```sh
python topics/padua-3d-20261106/code/pdpr_certify.py selftest --check /tmp/pdpr-cert16-engineering-20261107b.json
```

Earlier engineering revision a skipped a huge-prime mutation because its
prime guard followed primality; final revision b moved the bound first and
actually rejected that mutation. No actual degree16 rank was queried by
engineering, and there were no failed degree16 builds. All temporary
engineering/clean-copy paths remain regeneration-only. Root owns the
independent disposition, durable application proof and final publication.
