# Independent n=5 exact producer, global evidence and verifier execution

Date: 2026-11-01. Executor: Codex subagent `/root/input_manifest`, independent
of the producer developer and checker implementer. Requested allocation:
gpt-6.1-sol medium for mechanical execution; separate serving-model metadata is
not exposed. This is supplementary execution, not the required Claude audit.
Rules were initially read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`;
the changed administrative rules were reread at
`842dfaaeff524b4db4141d314afff6ad4a5b7721` during this execution. They do not
alter any frozen mathematical computation. No Git mutation, source edit,
manifest edit, shared-checks edit, handoff or ID allocation was performed.

## Frozen source identities and environment

All six files were SHA-256 checked before their relevant stages and again after
the independent producer, global generator, full checker and full controls
completed. Every value matched its supplied frozen pin and remained unchanged.

| File under `code/` | SHA-256 |
|---|---|
| `a5_n5_boxes.py` | `20817eb6ec086dd0c3b81ec8313223a5a53fc3f13feecf7593ef186e13c90b52` |
| `a5_n5_nodes.py` | `d4d61f3b30fbf5c1bf4c7b26aee6ab2dab6675a2ad38d5d079de21ea8bc15733` |
| `a5_n5_boundary.py` | `604483eb40362b43dcfbd211ceafbc9bfc417b201866c2b943d283c17592d1ec` |
| `a5_n5_global.py` | `52400f3df33c47783b951771239a2ff4442b5efdef1946d2e6598dab4735240e` |
| `a5_checker_n5.py` | `6390d465a0e4c83f5cb75673834da4bfbda98c507266c9a81c60c85baceb7bab` |
| `a5_checker_n5_controls.py` | `0508b79bd96f3a3b12c6f907992c5e179910f869d2fdabe3e669e8286164ef91` |

Actual environment: managed Linux workspace, Python 3.12.14, SymPy 1.14.0,
SymPy `GROUND_TYPES='flint'`, python-flint 0.9.0, FLINT 3.6.0. The explicitly
requested `PYTHONPATH=/tmp/padua2-deps` was used on every execution below. No
environment dump or secret inspection was performed. Arithmetic uses exact
`QQ(sqrt(3),sqrt(5))` algebra and outward integer dyadic intervals at precision
96. No random seed applies.

## Commands actually executed

Working directory: `/workspace/padua_research`. Each command below completed
with exit status 0. The fresh producer used no `--node-file`; all 21 node gaps
and cone rectangles were recomputed by that process. The full checker used
neither `--nodes-only` nor `--allow-partial`.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n5_boxes.py --certificate --boundary --boxes 100000 --seconds 3600 --depth 36 --full-depth 30 --ambiguity 6 --root-depth 12 --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz > topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_producer.jsonl 2>/tmp/a5-independent-n5.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n5_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_global.json > /tmp/a5-independent-n5-global.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n5.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_checker.json > /tmp/a5-independent-n5-checker.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n5_controls.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --spatial-certificate topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_controls.json > /tmp/a5-independent-n5-controls.log
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n5.py topics/padua-proof-attempts-2-20261101/outputs/a5_n5_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n5_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_developer_certificate_check.json > /tmp/a5-independent-n5-developer-check.log
```

The producer receipt is JSONL progress plus its final JSON summary, deliberately
named `.jsonl`. All other JSON outputs are single JSON objects. Raw diagnostic
stderr remains at the stated `/tmp` paths; no copied developer node evidence
was supplied to the fresh producer.

## Own artifact completion and observed verifier results

The producer recomputed 21 strictly positive node gaps and accepted cone
rectangles. It completed with no pending path and no unresolved record, visited
20363 spatial boxes, and produced 10182 leaves, of which 150 reference node
cones. Maximum depth was 29; maximum observed ambiguity was 21. The final
ordinary pattern list contains 225656 records. Its interior timer reports
220.7634301185608 seconds, including the fresh node construction (reported
separately at 53.44320607185364 seconds). Boundary construction reports
335.10971689224243 seconds. These are producer phase timers, not an independently
instrumented end-to-end measurement.

The independent full verifier completed in 299.0166610030001 seconds and reports:

- `accepted`, `count_certified`, `interior_complete`, `boundary_complete`,
  `complete_prefix_partition` and `verified_supplied_witnesses` all true.
- 14 verified interior maximum enclosures, 9 verified edge maximum enclosures
  and 2 verified corner maxima, giving `total_maxima: 25` on the closed square.
- 21 node records accepted, 738 checked directional breakpoints and 150 checked
  node leaves; 10182 leaves, 225656 ordinary mask dispositions and 139 edge
  patterns verified.
- Interior dispositions: 225462 gradient, 150 node-cone leaves, 142 root
  references, 48 Hessian and 4 flat. No factor or regular-point fallback occurs
  in this certificate. The 142 root references cover 14 distinct enclosures.
- Edge dispositions: 1070 derivative, 216 minimum, 330 outside, 190 sign and
  9 accepted roots. The four physical edges and four corners are covered.

The additional matching global file also passes. The verifier reports
`global_argmax_verified`, `global_no_nonstrict_plateau_above_cut` and
`node_leaf_global_exclusion_verified` all true. Its only attaining points are
`(-1,-1)` and `(-1,1)`, with exact field value
`38/15 + (8/15)*sqrt(3) + (2/3)*sqrt(5)`. The strict cut is `19/4`; accepted
interior/edge values and the four exceptional flat occurrences are bounded below
the cut, and the two corner lower bounds exceed it. The observed exceptional
upper bound is `15008010243903610701266445927/9903520314283042199192993792`.
These are actual verifier results; their use depends on the separate written
finite reduction, cone argument and global plateau proof.

Full controls completed in 311.3757132770006 seconds, with
`all_controls_passed: true`: 31 controls, consisting of 27 negative and 4 positive
controls. They include a full count/global positive replay; exact cone and
directional-breakpoint coverage; counterfeit gaps, Hessian/radius and positivity
bounds; missing or non-strict whole-leaf cone containment; denial of discard
authority to a zero-gap or missing cone; spatial-mask/Sturm coverage; exact
84-component polynomial agreement for 10 masks; and omitted or counterfeit
global bindings, exceptional bounds, root value rows and corner value. No
separate synthetic zero-gap producer test was executed by this agent at this
stage; the checker rejection control is explicitly distinguished from one.

## Independent output identity

The certificate gzip is 125252 bytes and its uncompressed JSON is 5,201,785
bytes. The latter was decoded in memory only. No artifact was split; the single
gzip and all individual outputs remain below 1 MB.

| Artifact under `outputs/` | Bytes | SHA-256 |
|---|---:|---|
| `a5_independent_n5_certificate.json.gz` | 125252 | `d22c9b1e32728e511ca4ac20506df614b501669a37bc287ed1cde802b6c7f4b3` |
| `a5_independent_n5_producer.jsonl` | 3141 | `a42397d302df3bc736e918707d73658a0e42ff5587c84cd07fe78f5be702c6ed` |
| `a5_independent_n5_global.json` | 3897 | `47d50f724471904d4873c471e48a2dec9992eb537f5597afe13d07fe17152ccb` |
| `a5_independent_n5_checker.json` | 8358 | `80a33c158a9d34afdc4004f77360ce8bd36439107783a7c235d98aba5d524d76` |
| `a5_independent_n5_controls.json` | 5358 | `462377ebbe8a9ad72c00cbcd9b8c1998b3ea24b49a927cfd2b1b3a15bbbf7281` |
| `a5_independent_n5_developer_certificate_check.json` | 8359 | `8dabc97c98a71c9b546caf150e53834fab8c45648d5cbbdc76e081ac236d2e98` |

## Developer-pair comparison — completed after its artifact arrived

At the completion of the first independent runs, the requested developer
artifact was not yet available. It subsequently arrived, and the fifth command
above separately checked its matching certificate/global pair. That execution
exited 0 in 257.67998521499976 seconds and reports the same accepted/count,
boundary, node-leaf and global flags and 25=14+9+2 counts. All six source hashes
were checked again before and after this additional execution and stayed fixed.

Developer `outputs/a5_n5_certificate.json.gz` is 125245 bytes, with SHA-256
`a1238d59781733cc0d380dc513a0a642d0e24b985aeb9b90bb7233756273386e`.
The raw gzips differ. Decoded independent and developer certificates are exactly
equal after removing only `summary.seconds` and `boundary_summary.seconds`;
every other mathematical and metadata field remains in that comparison. The
developer timers are 264.46038269996643 seconds for the interior and
1047.2554004192352 seconds for the boundary. The matching global files are exactly
equal after removing only their respective raw `certificate_sha256` bindings.
No global file was borrowed across the differing raw gzip identities. The two
checker receipts agree after removing only `seconds`, `certificate_bytes`,
`certificate_sha256` and `global_certificate_sha256`.

## Limits

This records actual independent producer/global-generator and separately written
checker execution at n=5. The checker verifies supplied coverage and exact
predicates instead of repeating spatial search or root isolation. The written
finite reduction, node-cone argument, boundary classification and global proof
remain trusted mathematical dependencies, along with exact-arithmetic software
and both implementations' correctness. Thirty-one controls do not constitute an
exhaustive checker proof. No n=6,...,8 count, correction to their published
values, or all-degree global theorem follows. Required Claude audit remains
pending. No theory status was changed by this
executor, and no additional n=3 or n=4 computation was run.
