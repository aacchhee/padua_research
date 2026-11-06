# N3 round6 fixed calibration attempt

## Preregistration — before first numerical execution

UTC: 2026-11-06T06:47:50.143186+00:00. Rules/input published head `fc8c2885f47b08cecc7f65328db0e740cbc205ea`, branch `codex/padua-argmax-bridge-20261105`. Delegated producer requested Codex Sol medium; actual serving metadata not independently exposed.

Read gate/registry delta and exact scope: `../ideas/N3-round6-calibration.md`. Degree order **24,32 only**, known-degree overlap. Existing accepted n17 search cost222.371068930CPU-s is historical comparison context; it used the smaller inherited patch and is not a matched-patch rerun. No cost law from these points.

Uniform search cap1500CPU-s,100000boxes; per-degree total process-group CPU cap1600s. Separate worker RLIMIT_CPU soft1595/hard1596 plus parent process-group watchdog1595CPU-s sampled0.25s reserve below1600. Fresh per-degree build; setup/constants CPU and compiler/build-helper child CPU are measured separately from search. Stop/freeze at first failure, cap or incomplete frontier, or after32. No adaptive runs/parameters, no n64/n128, no n41+ native extension.

Use unchanged C source and outward interval header, confirmed identical to accepted n17 build source pins. MPFR128-bit directed endpoint arithmetic and binary64 outward operations remain unchanged. New Python driver validates fixed published receipt SHA e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0, PASS, exact127-degree coverage/counters, kappa1/16000, phase1/128 and existing checker C++/wrapper plus evidence/data identities. Historical prose entries in the old receipt are never new guard pins. Local guard is exact Fraction arithmetic: maxabsphase<=1/128 and a²/2+n²b²/[2(n+1)²]<=1/16000, restricted to integer2..128. Inherited geometry radius is also retained. localmask only requests defect computation when Cu lacks strictness; **actual** nextafter(Su−actual defect,+infinity)<Lc remains required. Outside predicate, splits, constants and complete partition semantics remain unchanged.

Every worker snapshots C/header/MPFRheader/newdriver, compiles in its own fresh directory, records exact command, source/header/compiler/runtime/loaded-mapping closure and verifies it after search. Original diagnostics stay local. Only the existing `n3_compact_candidate.py` projection may remove diagnostic S_upper/corner_upper/defect_lower fields ignored by checker. All roots/path/kinds/pending/nonleaf metadata retained; separate exact-byte replay required. Deterministic gzip may be essential evidence if<16KiB; no data splitting or deleted historical artifacts. Parent owns all shared records/theory/Git and copying evidence; bulk remains local, archival destination pending.

Actual fixed launch from `/workspace/padua_research`:

```sh
python topics/padua-argmax-bridge-20261105/code/n3_outward_r6.py
```

This sequentially launches the same file with `--worker 24`, then `--worker 32`, preserving actual argv/exit/CPU/stdout/stderr identities in `../evidence/n3-r6-producer.json`. No numerical calls have run at this preregistration.

| Preregistered code/data | Bytes | SHA256 |
|---|---:|---|
| `topics/padua-argmax-bridge-20261105/code/n3_outward_r6.py` | 12216 | `789f119b4ed5778ff4d031563d9f3b0b831ae71dc27f7bf7b3589296a0c9cd54` |
| `topics/padua-argmax-bridge-20261105/code/n3_outward.c` | 4830 | `cfeae9fe2b61e9c7ec2c4d943762ac988e64fa02652ccfe4342430c4ee5f22dd` |
| `topics/padua-argmax-bridge-20261105/code/n3_outward_interval.h` | 4215 | `6dca513ddbd94264d454872c9f5e753e355d15b49152dc4b19d51cff7635131b` |
| `topics/padua-argmax-bridge-20261105/code/n3_outward_full.py` | 8417 | `9c6460f4407498d08bd26f36fe8f7b56290a5fb33eb06e49fa6d5735a84b7b29` |
| `topics/padua-argmax-bridge-20261105/code/n3_compact_candidate.py` | 2605 | `2e90bbb1d130ba1560a00b1712bad187b6303288cdb3c28fdcfae6bec200e3ad` |
| `topics/padua-argmax-bridge-20261105/code/n3_native_receipt.py` | 2979 | `44990cb6b9e65ee8fe788663be91e7bde71ee6ce77dec7b228d56825f7209577` |
| `topics/padua-argmax-bridge-20261105/code/check_corner_exact.cpp` | 5725 | `3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3` |
| `topics/padua-argmax-bridge-20261105/code/check_corner_range.py` | 7416 | `66fc2d9583260572125bd6c70a943577f94f1dd1ce2755a2c47ad96fffa9a982` |
| `topics/padua-argmax-bridge-20261105/evidence/independent-corner-range.json` | 6262 | `e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0` |
| `topics/padua-argmax-bridge-20261105/evidence/n3-corner-batch.json` | 3601 | `97e20cc877ad5afd0c9dfe96c1e399a42d820b38c18626e2b69bfa54f6acfc88` |
| `topics/padua-argmax-bridge-20261105/evidence/independent-corner-replay.json` | 7892 | `573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b` |
| `topics/padua-argmax-bridge-20261105/evidence/phase-checker-full-n17-round5.json` | 6264 | `49060e7633068f6ffb531e63614855a5d88c466c10e6d4d1b07a8c21043e6423` |
| `topics/padua-argmax-bridge-20261105/evidence/n3-phase-n17.json.gz` | 5266 | `80dcb2db069332e018653931bdb94e3995ceca5c9d96741fd1b87110474267a6` |
| `local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include/mpfr.h` | 57588 | `588c2bd606cba060afb49cd024f9119e996089a341a99d1dc7e0367622335a13` |
| `local-output/argmax-bridge-20261105/check-corner-range/own-n2-128.jsonl` | 363463 | `47f3d233b5fd7bc46dca8c45a0de2ecc09be4d36988ab83b16f87c44a843bd20` |

## Executed outcomes

Not started at preregistration; append outcomes below without rewriting the plan.

### Exact guard controls after preregistration

Executed import of the new driver and range_premise(): all fixed published code/data identities matched. local_range accepted the full closed phase square at degrees2/24/32/128, rejected invalid degrees1/129 and bool, and rejected an upper endpoint nextafter(1/128,+infinity). These are cheap exact rational guard controls, not a cover replay or mathematical approval. No C/MPFR numerical test preceded preregistration.

### n24 complete — observed 2026-11-06T06:54:43.805589+00:00

Actual exit0; no watchdog stop; complete=true,pending0,accepted=false. Search 363.070380277CPU-s; total subprocess 363.812374CPU-s; compiler child 0.434822CPU-s; own build 0.103234610CPU-s; constants setup 0.052799040CPU-s. 2036visits and 1016splits; counts {"corner-orbit-plus-defect": 456, "far": 512, "local-corner-plus-defect": 20, "outside": 32, "split": 1016}.

Frozen compact plain `local-output/argmax-bridge-20261105/N3/outward-r6/n24/n24-phase-compact.json` (62755bytes), SHA256 `8c984dc87c9170ae07f106a530a7915596bca30f273371bb2de2f89c8443ec92`; deterministic gzip 5070bytes, SHA256 `77bbdcf13363835fbca25d96b69eb277e2e5778e0e001c621f7eab0fc05ad51d`. Original diagnostics and full build/runtime closure remain local. All source/binary/header/runtime and fixed-premise identities revalidated after search. Notified parent and separate phase checker immediately; independent acceptance is separate. Exact argv/UTC/exit/source/build/projection/raw/CPU identities are in `../evidence/n3-r6-producer.json`. n32 started once under the preregistered order.

### n32 complete — observed 2026-11-06T07:05:20.349082+00:00

Actual exit0; no watchdog stop; complete=true,pending0,accepted=false. Search 619.326637711CPU-s; total subprocess 620.093411CPU-s; compiler child 0.439454CPU-s; own build 0.055791133CPU-s; constants setup 0.099998765CPU-s.1980visits,988splits,992leaves;32outside,512far,428corner-orbit-plus-defect,20local-corner-plus-defect.

Frozen compact plain `local-output/argmax-bridge-20261105/N3/outward-r6/n32/n32-phase-compact.json` (60925bytes), SHA256 `1cedd123ca9bfb69c200036161c521b5cbe1fca8e7197c4dd5ec557b640fa234`; deterministic gzip 4989bytes, SHA256 `2107db169168455ba770fcce7f5fd60d0fb4454575a83077aaffc9a4e4d024e3`. Source/binary/header/runtime and fixed-premise identities revalidated after search. Notified parent and separate phase checker immediately. Independent replay/acceptance belongs to that distinct agent.

### Fixed block outcome and final validation

Launcher exited0 after24→32, both first runs complete and producer accepted=false. Block frozen: no retries, parameter adaptation, n64/n128 or other degree work. Measured total subprocess CPU 983.905785s; producer inventory 9457bytes, essential compact gzip sum 10059bytes, local run directory 704652bytes including all raw diagnostics/build closures. Bulk remains local; archival destination pending.

Final nonnumerical validation rehashed 167 code/data/source/header/compiler/runtime/input/output identities, verified exact gzip decompression, compact projection omits only the three ignored leaf diagnostics with all other nonleaf metadata unchanged (plus declared projection provenance), checked full prefix-free four-root partitions, exact degree order, completion, false producer acceptance, actual exit0 and caps. This is provenance/structure validation, not arithmetic replay or producer approval.

| Instance | Patch | Search CPU-s | Leaves |
|---|---|---:|---:|
|17 historical accepted overlap|Inherited T251/T369 only|222.371068930|1288|
|24 round6|Published common phase1/128 patch|363.070380277|1020|
|32 round6|Published common phase1/128 patch|619.326637711|992|

These are finite measurements. n17 used a different patch and is not a matched-method scaling point. n24/32 are two known-degree calibrations: no asymptotic cost/box-count law, global degree extension, B3/B4/onset or all-degree claim follows. The independent checker and formal Claude audit obligations remain separate.
