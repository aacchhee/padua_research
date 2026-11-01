# Independent n=6 exact producer and completed verification

Date: 2026-11-01. Executor: Codex subagent `/root/input_manifest`, independent
of the producer developer and checker implementer. Requested mechanical
allocation: gpt-6.1-sol medium; separate serving-model metadata is not exposed.
This is supplementary execution, not the required Claude audit. Rules initially
read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`; changed administrative
rules reread at `842dfaaeff524b4db4141d314afff6ad4a5b7721` during the preceding
n=5 execution. No source, shared-checks, manifest, Git, handoff or ID changes
were made by this executor.

## Frozen inputs

All eight identities below were verified before their relevant stages and again
after the complete producer/global stages and before the own full checker.
There was no source drift. All eight were checked again after the completed
sequential controls and remained unchanged.

| File under `code/` | SHA-256 |
|---|---|
| `a5_n6_field.py` | `1e08c253f78b3e34df1f02947f3e4767949976daa6240aa7753c11a82f9970e5` |
| `a5_n6_nodes.py` | `1901437733a441c5d2279433c63378d17343367c1826400617a7002aa09371b5` |
| `a5_n6_boxes.py` | `fed35e7ef6efe13df5d0df150550abbe9ddaf186a3f8d1f07884e04711a2bdd9` |
| `a5_n6_boundary.py` | `e0d16de330aff00060beff7a9d4be94f80079f326a37e675448f22dc6c3e696a` |
| `a5_n6_global.py` | `ab1e287b4a152975aec91056aa5326fdddb294394eecee5d5725770e1e89dcda` |
| `a5_n6_schema.md` | `e03ea676ad5710d97efafb426066f0cb07857e7e800acede87add5b2606585da` |
| `a5_checker_n6.py` | `34d8c0b7afb261d5f082022f49a84ec6e741f50de31904da5f4221f02f9673c8` |
| `a5_checker_n6_controls.py` | `fd926f0d390ab2336476d054bfcee89aba97c624487f8acd0e64491c664633e0` |

Environment selected explicitly by the commands: Python 3.12.14, SymPy 1.14.0,
python-flint 0.9.0 / FLINT 3.6.0, SymPy ground backend `flint`, using
`PYTHONPATH=/tmp/padua2-deps`. Exact degree-six field basis is
`[1,b,b²,a,ab,ab²]`, with `a²=3`, `b³-b²-2b+1=0` and the principal real
embedding specified in the schema. Outward dyadic intervals use precision 112.
No random seed applies. No secret or environment dump was performed.

## Completed independent producer and global construction

Working directory for all commands is `/workspace/padua_research`.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n6_boxes.py --boxes 200000 --seconds 2400 --depth 40 --ambiguity 8 --full-depth 40 --certificate --boundary --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_certificate.json.gz > topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_producer.jsonl 2>/tmp/a5-independent-n6.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n6_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_global.json > /tmp/a5-independent-n6-global.log
```

Both exited 0. The fresh producer omitted `--node-file` and recomputed all 28
node gap/cone records, all with strictly positive lower gaps. It visited 55607
boxes and completed with zero pending paths and zero unresolved records. Its
27804 leaves include 224 node-cone leaves and 1504228 ordinary compatible-mask
records. Maximum depth is 30 and maximum ambiguity 28. Its candidate list has
25 interior, 14 edge and 2 corner entries, total 41; at that producer stage they
were candidates, subsequently verified by the completed checker below.
Interior phase elapsed time is
1171.3912560939789 seconds and boundary/corner phase is 316.9415180683136 seconds.
The final edge-only progress time of 296.52 seconds excludes subsequent corner
work and is not substituted for the complete phase timer.

Own gzip is 414047 bytes with SHA-256
`c042401f3d8c3e28d045fed9855f3b7817840f68491d8d686cdcd2c587cd48e1`.
Uncompressed JSON is 32,057,489 bytes, decoded in memory only; no file splitting
or committed uncompressed extract was used. Developer gzip is 414031 bytes,
SHA-256 `c7a113b9b623c47309fd186c19ee2dddb2d5a0270c01b118bd11ee1ee069f0f5`.
Decoded certificates are exactly equal after removing only `summary.seconds`
and `boundary_summary.seconds`. Every other mathematical and metadata field
remains in the comparison. Developer phase timers are 887.9484281539917 and
142.7349157333374 seconds respectively. Raw gzip bytes differ as expected.

## Operational memory interruption and adjusted verification sequence

Before the own producer finished, the orchestrator authorized parallel checking
of the already available developer certificate/global pair. These two actual
commands were started:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n6.py topics/padua-proof-attempts-2-20261101/outputs/a5_n6_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n6_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_developer_certificate_check.json > /tmp/a5-independent-n6-developer-check.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n6_controls.py topics/padua-proof-attempts-2-20261101/outputs/a5_n6_certificate.json.gz --spatial-certificate topics/padua-proof-attempts-2-20261101/outputs/a5_n6_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n6_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_controls.json > /tmp/a5-independent-n6-controls.log
```

Their growing caches overlapped the implementer's two full verification
processes and the own producer. At the orchestrator's explicit resource-control
instruction, this executor terminated only its duplicate checker PID 17797
(session 91122) and controls PID 17794 (session 26606) with SIGTERM. Both actually
exited 143. This was an operational interruption, not a mathematical rejection,
and neither execution supplies final acceptance or a completed rerun. Raw
progress logs remain at the stated `/tmp` paths. The own producer continued to
completion without interruption.

Immediately before memory release, `free -m` reported used 14365 MB / available
3642 MB of 18007 MB; after process cleanup it reported used 9787 / available
8220 MB. The completed own producer subsequently released its cache, giving
available 11565 MB. The orchestrator then explicitly cleared one heavy helper
process at a time. The adjusted sequence is:

1. Full own certificate/global CLI verification below.
2. After it exits and releases memory, full controls on the developer pair. That
   runner's `complete_count_and_global_value_certificate` invokes `full.run`
   and `global_values`, so its completed positive control is also an actual full
   developer-pair verification. No third standalone developer CLI replay is
   needed or claimed.

The own full command completed with exit status 0:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n6.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_checker.json > /tmp/a5-independent-n6-checker.log
```

## Completed own verifier and sequential developer controls

The own full checker reports `accepted`, `count_certified`, `interior_complete`,
`boundary_complete`, `complete_prefix_partition` and
`verified_supplied_witnesses` all true. Its verified count is 41 strict local
maxima on the closed square: 25 interior, 14 open-edge and 2 corner maxima.
It checks 27804 leaves, 1504228 compatible ordinary patterns, 224 node leaves,
all 28 node records, 1316 directional breakpoints, 228 edge sign patterns and
16 active corner patterns. Interior dispositions are 1503090 gradient,
224 node-cone leaves, 400 Hessian, 684 references to 25 distinct root boxes,
and 54 flat. Edge dispositions are 3890 derivative, 470 minimum, 864 outside,
428 sign and 14 roots. No optional regular-point or factor predicate is used.

The exact field checks return `field_embedding_verified`,
`principal_embedding_verified` and `native_tensor_inverse_verified` all true,
with `formal_minpoly_degree: 6`. The matching global check returns
`global_argmax_verified`, `global_no_nonstrict_plateau_above_cut` and
`node_leaf_global_exclusion_verified` all true. The only attaining points are
`(-1,-1)` and `(1,-1)`, with FIELD coefficients
`[5/7,8/21,20/21,4/21,4/21,0]` in the stated basis. The strict cut is 5;
all accepted interior/edge value upper bounds and all 54 exceptional flat
occurrences are below it, while the common non-node corner lower bound exceeds
it. The observed exceptional upper bound is
`8526311743724763702119888371493549/5192296858534827628530496329220096`.

The own full verifier records 590.9934989430003 seconds. After its process exited,
`free -m` reported available 17048 MB. All eight source hashes were rechecked and
unchanged. Only then was the developer-pair controls command rerun, with stderr
progress retained and stdout redirected to
`/tmp/a5-independent-n6-controls-sequential.log`. It completed with exit status
0, recording 564.3648265640004 seconds and `all_controls_passed: true`. The
exact completed replay command was:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n6_controls.py topics/padua-proof-attempts-2-20261101/outputs/a5_n6_certificate.json.gz --spatial-certificate topics/padua-proof-attempts-2-20261101/outputs/a5_n6_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n6_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n6_controls.json > /tmp/a5-independent-n6-controls-sequential.log
```

The 38 controls comprise 33 negative cases rejected and 5 positive cases
accepted, including `complete_count_and_global_value_certificate`. That positive
actually executes the full verifier and global-value verification on the
developer pair. Its receipt binds the developer raw gzip hash
`c7a113b9b623c47309fd186c19ee2dddb2d5a0270c01b118bd11ee1ee069f0f5`,
the exact frozen checker and controls sources. The developer global hash is
`af21a0a8f3d1e4301c3a249b6683ce61ce14436e7a2e96e71773b275a8563170`.
No completed standalone developer CLI replay is claimed: the earlier attempt
exited 143 and never produced a final acceptance receipt.

Other controls test exact field/native minimum polynomial, tensor conversion,
principal embedding and FIELD dimension; tensor-tower versus native degree-six
norm equality on two polynomials; all node directional/cone inequalities;
whole-leaf containment; sign-mask, prefix and Sturm coverage; integer-vector
polynomial identities; and omitted or counterfeit global bindings, exceptional
bounds, value rows and corner values. They include denial of exclusion authority
to zero-gap or missing cones. They are finite checker controls, not an exhaustive
proof of correctness. The earlier interrupted logs remain separate and are not
counted among these completed controls.

After the sequential process exited and released its cache, `free -m` reported
available 16562 MB. Thus there was only one heavy helper verifier at a time in
the completed sequence. Every source hash was unchanged on the final check.

## Artifact identities, comparison and limits

Own and developer global mathematical contents are exactly equal after removing
only their matching raw `certificate_sha256` bindings. Each actual verification
uses its matching pair. The completed outputs are:

| Independent output under `outputs/` | Bytes | SHA-256 |
|---|---:|---|
| `a5_independent_n6_certificate.json.gz` | 414047 | `c042401f3d8c3e28d045fed9855f3b7817840f68491d8d686cdcd2c587cd48e1` |
| `a5_independent_n6_producer.jsonl` | 7657 | `8e493e5a40c36a9ec4bd28ec0d0b645c9dac1625c89268e5a6b0adbc77eb3abd` |
| `a5_independent_n6_global.json` | 7077 | `7135a483a834b66ab60608b1e682ede1af9878c325fef06f74ace7d6077f1dcc` |
| `a5_independent_n6_checker.json` | 13396 | `b4b99f4c739dce3e98d336645ca092912b91f5193482518da12f23bc377d2018` |
| `a5_independent_n6_controls.json` | 6334 | `48d0fb053ac064e5d0a4abfeb30d878a3dae665538e52d7d4fe7994c40ca5984` |

Every committed independent output is below 1 MB; the necessary single gzip was
not split. No additional final JSON was fabricated for the interrupted CLI.
The positive developer-pair verification is carried by the controls receipt and
its frozen implementation, with the complete count/global flags in the own
CLI receipt. This executor claims one completed own full CLI check, one completed
developer-pair full verification inside controls, and two interrupted attempts.

No mathematical result or theory status has been edited by this
executor. The separate written finite reduction, exact field embedding proof,
node-cone argument, boundary classification and global plateau proof remain
mathematical dependencies. Required Claude audit remains separate and pending.
No n=7 or n=8 result, or all-degree global theorem, follows from this record.
