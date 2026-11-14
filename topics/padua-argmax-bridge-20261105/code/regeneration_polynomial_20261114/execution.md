# Current polynomial executable replacement — 2026-11-14

The preregistered minimal sequence completed once after coordinator commit
`ba643bbc7c789e01fecad654991f15c0a8b8d159` and distinct reviewer clearance.
No producer, search, retry or full 39-degree replay occurred.

Executed from the repository root:

```sh
python3 -E -S -B topics/padua-argmax-bridge-20261105/code/regeneration_polynomial_20261114/replay.py --execute
```

Output root:
`local-output/argmax-bridge-20261105/polynomial-regeneration-20261114`.
All 52 pinned files, including all 39 compressed certificate inputs, remained
unchanged. The strict frozen wrapper accepted retained degrees 2 and 17 with
complete partitions, every supplied bound verified and exactly two corner
leaves. This supplements the surviving historical accepted records; it does
not replace them with a claim of a full current replay.

| Stage | Actual exit | Inclusive child CPU seconds | Wall seconds | Maximum RSS KiB |
|---|---:|---:|---:|---:|
| Compile once | 0 | 2.385949 | 2.411827164 | 150664 |
| Linked-library inspection | 0 | 0.006443 | 0.051599842 | 9708 |
| Strict n2 | 0 | 0.106744 | 0.152149973 | 12160 |
| Strict n17 | 0 | 10.333478 | 10.403365231 | 106112 |

Every stage has an owned actual `wait4` status and no cleanup. Raw argv,
stdout/stderr and resource observations are retained alongside the receipts,
`environment.json`, `runtime-closure.json` and `summary.json`.

The newly compiled `kernel` is 67,584 bytes, SHA-256
`e35d6a80952d98edc1927f827346cc436d9f0da31837f9d000918aadada137c7`.
This happens to equal the historical binary pin. The historical file was
absent; these bytes were freshly compiled from the frozen source.

Afterward, a data-only Python copy read the linked-library rows from
`runtime-closure.json` and the tools/GMP-header rows from `environment.json`,
copied each original absolute path beneath `dependency-bytes/`, preserved its
mode and verified size/SHA-256 by readback. Its
`retained-dependency-bytes.json` lists 14 source rows and the retained paths;
unique retained payloads total 41,412,808 bytes. This includes the actual
compiler/tool, Python executable, GMP-header and linked-runtime bytes, rather
than identity records alone. It is an inspected rebuild/runtime closure, not
a claim of a hermetic distribution of all system/compiler headers.

The coordinator's delivery task incorporates this whole output tree into
the current downloadable reproduction. Local retention does not establish
external delivery or durable custody.
