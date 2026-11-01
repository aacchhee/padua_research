# Actual independent n=4 producer, global evidence and checker execution

Date: 2026-11-01. Executor: Codex subagent `/root/input_manifest`, independent
of the producer developer and checker implementer. Role: supplementary exact
execution, not the required Claude audit. Requested mechanical allocation:
gpt-6.1-sol medium; no separate serving-model receipt is exposed. Rules were
originally read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`.

Read the n=4 spatial/boundary schema and relevant producer/global/checker code.
Ran the requested producer in a fresh process, generated a separate global
certificate bound to that process's own gzip, and ran the independently written
final checker on both independent and developer certificate/global pairs.
Separately executed the checker controls. No source edit, manifest edit,
shared-checks edit or Git mutation was performed.

## Frozen source identities

The following six SHA-256 values match the orchestrator's pins. They were checked
before their relevant stages and all checked again after the completed runs;
none changed.

| File under `code/` | SHA-256 |
|---|---|
| `a5_n4_boxes.py` | `1d389bedef41bc08cf9cd008012870d9dc25eb4960c029020d235324b0afa4c0` |
| `a5_n4_boundary.py` | `4cba7f4c8acb97127cc6ffa12a53bce88a093acfcb36b9ba1aba3b19dd9b70cb` |
| `a5_n4_schema.md` | `eb11ef7928c9c2fc81c6cca597646dfe0c65c88a13a388b28baad3932e8c7ad3` |
| `a5_n4_global.py` | `4dbba47a21a47137ea417a015895aa8c08538215827315da6a5f24caf0c98af3` |
| `a5_checker_n4.py` | `1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143` |
| `a5_checker_n4_controls.py` | `6ff60f6545f98fe09ead2a4749f399091e9de12615ae957cdbb502189ed64b61` |

Environment: Linux, Python 3.12.14, SymPy 1.14.0. The actual independent process
used SymPy `GROUND_TYPES='python'`; `python-flint` was unavailable on its import
path. No `PYTHONPATH` override was used. This differs from the developer's
reported `/tmp/padua2-deps` path selection. Both perform exact algebra; the
backend distinction was explicitly retained and the mathematical certificate
contents were compared rather than assuming bit identity. No environment dump
or credential inspection was performed. No random seed applies.

## Commands actually executed

Working directory: `/workspace/padua_research`. All five mathematical execution
commands exited 0. Both checker calls used the final frozen source and full
boundary/global verification, with no `--allow-partial`.

```sh
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_n4_boxes.py --boxes 200000 --seconds 600 --depth 40 --ambiguity 8 --certificate --boundary --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_certificate.json.gz > topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_producer.json 2>/tmp/a5-independent-n4.log
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_n4_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_global.json > /tmp/a5-independent-n4-global.log
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n4.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_checker.json > /tmp/a5-independent-n4-checker.log
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n4.py topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n4_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_developer_certificate_check.json > /tmp/a5-independent-n4-developer-check.log
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n4_controls.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n4_controls.json > /tmp/a5-independent-n4-controls.log
```

The first command emits JSONL progress records followed by its final summary.
After execution, with the orchestrator's agreement, its initially requested
`.json` receipt was renamed without changing any byte:

```python
from pathlib import Path
p = Path('topics/padua-proof-attempts-2-20261101/outputs')
(p / 'a5_independent_n4_producer.json').rename(p / 'a5_independent_n4_producer.jsonl')
```

This is a filename correction to preserve raw progress; it is not a new producer
run or a rewritten summary. All other `.json` outputs are single valid JSON
objects. The producer was monitored through its actual execution session and
own logs, not through the developer's output.

## Observed completion and certified predicates

The producer visited 5463 boxes, with no unresolved leaf and no pending path.
It produced 2732 leaves and 490672 final compatible-mask dispositions, reaching
maximum depth 28 and maximum ambiguity 15. Its summary reports interior complete
and full boundary complete. Recorded producer phases: 74.40022110939026 seconds
for the interior and 435.69747829437256 seconds for the boundary. These are phase
measurements, not an independently instrumented end-to-end timer.

Both final checker receipts report all of:

- `accepted: true`, `count_certified: true`, `interior_complete: true`,
  `boundary_complete: true`, `complete_prefix_partition: true`, and
  `verified_supplied_witnesses: true`.
- 13 verified interior maximum enclosures, 12 verified open-edge maximum
  enclosures, 2 verified corner maxima, total 27 strict local maxima on the
  closed square.
- 2732 checked leaves, 490672 compatible-pattern records, 86 edge patterns and
  8 active corner patterns.
- Final interior dispositions: 489824 gradient, 714 flat, 82 Hessian and 52 root
  references, with the latter referring to 13 distinct enclosures. No factor or
  regular-point fallback is used by this certificate.
- Boundary dispositions: 480 derivative, 100 minimum, 172 outside, 78 sign and
  12 root records. All supplied boundary root partitions and signs are checked.

Both checks independently pass the additional global certificate:
`global_argmax_verified: true` and
`global_no_nonstrict_plateau_above_cut: true`. The only attaining points reported
are `(-1,-1)` and `(1,-1)`, with exact value
`(13 + sqrt(2) + 2*sqrt(5) + sqrt(10))/5`. The separation cut is 4. All accepted
interior and edge root value upper bounds are below that cut, both corner lower
bounds exceed it, and all 714 flat occurrences are bounded. The observed flat
upper bound is
`195815277203118945162885237407/79228162514264337593543950336`.
These are verifier results supporting the separately written finite reduction
and global proof; this execution record does not substitute for those proofs.

The full checker recorded 469.4071483590001 seconds on the independent pair and
466.3056979419998 seconds on the developer pair. The independent control suite
recorded 8.909429920000093 seconds and `all_controls_passed: true` for 11 controls:
9 deliberate defects rejected and 2 positive checks accepted. Coverage includes
prefix overlap/missing leaves, missing compatible masks, a singular
preconditioner, a false flat witness, zero Hessian as a false exclusion, omitted
or false Sturm roots, exact integer-vector agreement for 14 masks, and rejection
of the strict-only factor fallback as a global plateau argument.

## Artifact identities and comparisons

The independent gzip is 64371 bytes, below the per-output limit. Its uncompressed
JSON is 10,022,239 bytes; that fulltext was decoded in memory and not written as a
committed artifact. The single gzip was not split. The developer gzip is 64360
bytes with SHA-256
`14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61`.
Raw gzip bytes differ, as expected for filename/time headers and reported
timings. Decoded certificates are exactly equal after removing only
`summary.seconds` and `boundary_summary.seconds`; every mathematical and other
metadata field remains in the comparison. Global certificates are exactly equal
after removing only their distinct matching raw `certificate_sha256` bindings.
Each verifier used its own matching binding; no global file was borrowed across
the differing raw gzip identities.

The two checker receipts agree after removing only `seconds`,
`certificate_bytes`, `certificate_sha256` and `global_certificate_sha256`.

| Independent artifact under `outputs/` | Bytes | SHA-256 |
|---|---:|---|
| `a5_independent_n4_certificate.json.gz` | 64371 | `774910755f7213c5e7bb8392c6d0d93e120145e5c896772ec9814516ac6b6032` |
| `a5_independent_n4_producer.jsonl` | 1014 | `c440e48f1f3abe1b7c0c739ebe0cc2ba0a1e0b21fdf758784a388026a2638836` |
| `a5_independent_n4_global.json` | 4148 | `bd5cf543aab16c80ee945c32a17e1827601ebf1cce1efdc160a7065e78b225e0` |
| `a5_independent_n4_checker.json` | 9357 | `55c86e23cedc47b6747da62337f05d990dc0fd7bc1489a3d3e9cc9590550e496` |
| `a5_independent_n4_developer_certificate_check.json` | 9357 | `32202bda458d3385fa054809903b34b2e9939e1c7289dc927115bc405b34aed3` |
| `a5_independent_n4_controls.json` | 1945 | `654dc65be0e02b667769abc43ceedfa3256fa63c7e00cd742b3e083ccaf0dd73` |

## Limits

This is an actual independent producer/global-generator rerun plus execution of
the independently written certificate checker. The checker verifies supplied
tree coverage and exact predicates; it does not repeat spatial search or
root isolation. The trusted mathematical reduction, boundary classification,
global plateau argument, SymPy exact algebra and implementation correctness
remain explicit. Eleven controls do not exhaustively prove the checker correct.
This supplies n=4 evidence only: no n=5,...,8 count, no correction at n=6,...,8,
and no all-degree global theorem follows. Required Claude audit remains pending.
No theory status was changed by this executor and no additional n=3 test ran.
