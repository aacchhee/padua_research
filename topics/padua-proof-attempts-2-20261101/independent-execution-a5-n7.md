# Independent n=7 fresh execution — in progress

Date: 2026-11-01. Executor: Codex subagent `/root/input_manifest`, independent
of the producer developer and checker implementer. Requested mechanical
allocation: gpt-6.1-sol medium; separate serving-model metadata is not exposed.
This supplements the required Claude audit. Rules were initially read at
`a09d910ae7d5526b1e216066421a0bee7fc20da4`, with the changed administrative
rules reread at `842dfaaeff524b4db4141d314afff6ad4a5b7721`. No source, Git,
manifest, shared-checks, handoff or ID changes are made by this executor.

## Sources checked before the fresh run

The five producer modules and schema were compared with every byte size and
SHA-256 in `outputs/a5_n7_frozen-sources.json`. The checker, its separate field
helper and controls were checked against the separately supplied final pins.
All nine matched before producer execution, but the checker files are not
imports or dependencies of that producer. The six producer/schema pins were
unchanged after the completed producer/global construction. The first six rows below are frozen producer/schema dependencies; the
last three record the historical, unused checker versions initially inspected.

| File under `code/` | SHA-256 |
|---|---|
| `a5_n7_field.py` | `678a4fb4cb2e7a8d2a1b045b872d1fca2378ab5b7d929abfa5db04e8376961dd` |
| `a5_n7_nodes.py` | `d3717492025c6f9bc1cf29861eabb2106f8792609bf8824eb3a3dd422be521c1` |
| `a5_n7_boxes.py` | `d668e607df8f0b869887065816ef649468eca468a43b164ec2b913227f334e69` |
| `a5_n7_boundary.py` | `fbf66bd14a76bab02d689a5ef7cdf56e6ca1a095c736f2ee21ad29fd354d66b0` |
| `a5_n7_global.py` | `ca6c636dfd64ef00a5af2f9038524ff280223397415409aee2a4c7ac469a6418` |
| `a5_n7_schema.md` | `10e37040d2e060c26934a67b34f95c00a172075a6876e2299c098f6ef6eb5b59` |
| `a5_checker_n7.py` | `dd106871554bbf437699e3ac615121bd38d5bbd6d5d41bf29a6cf51cac7ed323` |
| `a5_checker_n7_field.py` | `76f9ba3de6d4fa4a3bd403ec2c049997de5acb75dd474ac8e05e9e324d6cd106` |
| `a5_checker_n7_controls.py` | `2a889a8db91e57ebc592c4891ab53a2d662dbe5c13d8fb4fc0f3cfba564064a5` |

During the producer run, before any full n=7 verification by this executor, the
orchestrator approved a bounded checker-only optimization of exact rational
endpoint evaluation using FLINT. The producer's five modules and schema are
unchanged, so no producer restart or invalidation is implied. The historical
three checker identities above must not be reported as unchanged through the
producer stage. The orchestrator reports unchanged verification predicates and
an exact benchmark; this executor claims no independent execution of that
benchmark. Final checker, helper and controls pins are recorded separately below
for their actual full verification and controls execution. No old
full checker result exists to be inherited or relabelled.

The subsequent frozen verification/codec stage uses:

| File under `code/` | Final-stage SHA-256 |
|---|---|
| `a5_checker_n7.py` | `41ab8dd11f6996b2fbbcc31ec9e415b63b350dafad7903768e3df99b99a07cdd` |
| `a5_checker_n7_field.py` | `76f9ba3de6d4fa4a3bd403ec2c049997de5acb75dd474ac8e05e9e324d6cd106` |
| `a5_checker_n7_controls.py` | `724a2f6731e6eaffb17470ab5adbd8b42af107f68b7ea1319158fa924ef16b73` |
| `a5_repack_certificate.py` | `e1cc7fe03b69d5542fabf9d2bc8052e71bf7c33398f68d23543d2610241c7332` |

The first full own verification starts only after those new pins are supplied
and verified. Together with the unchanged six producer/schema dependencies,
all ten current-stage hashes matched before repack and full verification. The
helper hash is carried forward unchanged; the main and controls changed only
before their first use here. Final post-verification confirmation remains pending.

Actual environment was checked: Python 3.12.14, SymPy 1.14.0, ground backend
`flint`, python-flint 0.9.0, FLINT 3.6.0, with the explicitly requested
`PYTHONPATH=/tmp/padua2-deps`. No seed applies. No credential or environment dump
was performed. The schema specifies exact degree-twelve field basis
`a^i*b^j` (i=0,1,2 outer; j=0,1,2,3 inner), principal real embeddings and
precision-128 outward dyadic intervals. Its direct universal-gradient leaves
exclude every compatible sign mask at once through a verified interval bound;
they are distinguished from ordinary explicit mask records and node-cone
leaves. Boundary root discovery may use outward Arb balls, followed by exact
Sturm coverage; a separate checker must verify the supplied partitions rather
than rerun isolation.

## Actual fresh command

Working directory: `/workspace/padua_research`.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n7_boxes.py --boxes 500000 --seconds 5400 --depth 44 --full-depth 44 --root-depth 12 --ambiguity 6 --certificate --boundary --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_certificate.json.gz > topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_producer.jsonl 2>/tmp/a5-independent-n7.log
```

This process is fresh and uses no `--node-file`, prior candidate count, root
list or inherited producer output. Its own log records all 36 recomputed node
gap entries, all with positive rational lower bounds and no zero-gap flag.
Spatial progress remains within the stated bounds, with no unresolved box in
the observed progress records. Memory is monitored; among this executor's own
processes, this producer overlapped only the final sequential n=6 controls, and those controls
subsequently completed and released their cache.

## Completed producer/global/repack and current verification

The producer exited 0 with `complete: true`, zero pending paths and zero
unresolved records. It visited 109795 boxes and supplied 54898 leaves:
50412 direct universal-gradient leaves, 204 node-cone leaves and ordinary leaves
with 96438 explicit compatible-mask records. It found a candidate list of
33 interior, 15 edge and 2 corner points (50 total); this is not promoted to a
certified count before verifier acceptance. The interior phase timer is
2948.8162989616394 seconds and boundary/corner timer is 623.7980008125305 seconds.
Maximum depth is 38 and maximum observed ambiguity 36.

The following global construction, mechanical repack and full own checker all
actually completed with exit status 0:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n7_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_global.raw.json > /tmp/a5-independent-n7-global.log
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_repack_certificate.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_certificate.json.xz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_global.raw.json --global-output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_global.json --receipt topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_repack.json > /tmp/a5-independent-n7-repack.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n7.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_certificate.json.xz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n7_checker.json > /tmp/a5-independent-n7-checker.log
```

The gzip is 856819 bytes, SHA-256
`da4a443bc559dd339ee7239a64480b689e923cc63c9e50dbecc6f13926240fbd`;
decoded JSON is 7,702,327 bytes. The final XZ is 436504 bytes, SHA-256
`a8a78bc7d206507103710d52e5279842b70d5bc1f38dd6c3fe2eca6a5e4fc00a`.
Repacker receipt and a separate direct `gzip.decompress == lzma.decompress`
comparison both verify exactly identical decoded bytes. Only the global
`certificate_sha256` binding changed; equality of all other global fields was
separately checked. No historical artifact was deleted, and raw intermediates
remain local pending storage decisions. No artifact was split. The verifier
uses only the matching XZ/rebound-global pair, never the old raw global binding.

Developer raw gzip SHA-256 is
`e55b0b5592b60d4d4401478605d6ed3f4dd62a84472b414ba15d1eba9155693b`
(856807 bytes). Decoded own/developer count certificates are exactly equal after
removing only `summary.seconds` and `boundary_summary.seconds`. Developer phase
timers are 2852.822651386261 and 670.5874254703522 seconds. The nonbinding global
contents also match exactly. All other mathematical and metadata fields remain
in these comparisons. Actual own full verification is complete; developer-pair
controls and the orchestrator's final evidence promotion remain pending.

## Actual own full verifier acceptance

The own checker exited 0 in 1899.9279202859998 seconds and reports `accepted`,
`count_certified`, `interior_complete`, `boundary_complete`,
`complete_prefix_partition`, `verified_supplied_witnesses` and
`source_hashes_unchanged` all true. Its accepted closed-square count is
50=33 interior+15 open-edge+2 corner maxima. It checked 54898 leaves, 50412
universal-gradient leaves, 204 node leaves, 96438 ordinary mask records,
333 edge patterns, all 36 node records and 2220 directional breakpoints.
The 198 root references represent 33 distinct interior enclosures. Final
ordinary dispositions are 96094 gradient, 146 Hessian and 198 root records;
there are no flat/factor exceptions. Boundary dispositions are 15472 derivative,
836 minimum, 2766 outside, 774 sign and 15 root records.

The verifier independently confirms the principal embedding, degree-twelve
native minimal polynomial and native/tensor inverse. Global flags
`global_argmax_verified`, `global_no_nonstrict_plateau_above_cut`,
`node_leaf_global_exclusion_verified` and
`all_gradient_global_exclusion_verified` are all true. The only attaining
points are `(-1,-1)` and `(-1,1)`, with exact FIELD coefficients
`[83/28,-5/7,-4/7,2/7,-2/7,0,2/7,0,-2/7,1/7,2/7,0]` in the stated tensor
basis. The strict separation cut is `11/2`; all accepted interior/edge upper
bounds are below it and both non-node corner lower bounds exceed it. There
are zero exceptional flat/factor occurrences requiring extra bounds.

All ten current-stage source hashes matched on the post-checker check. These
are recorded machine-verification results supporting the separate written
proofs, not a Claude audit or a unilateral theory-status edit by this executor.

## Remaining verification and limits

Pending: actual developer-pair verification/controls,
final post-run source hashes, final artifact table and acceptance flags.
Mathematical
reduction/field/node/boundary/global proofs and required Claude audit remain
separate dependencies. No n=8 or all-degree conclusion is inferred.
