# Supplementary evidence review of response 05 — 2026-11-13

**Result:** no unresolved finding in the reviewed code changes. E5-01's producer-file allowlist defect is repaired and independently exercised through real storage, completion, export and reader functions on synthetic records. This is **not canonical-archive compatibility verification**: the onset ZIP remains absent. E5-02's optimization hole and E5-04's FTZ+DAZ blind spot reject the independent adversarial controls below. The new `log(pi)>11/10` assertion executes and the eight historical output intervals are unchanged.

Reviewer: separate Codex supplementary reviewer; dispatch metadata supplied by the coordinator: `gpt-6-astra`, high; runtime-serving model/effort not exposed to this worker. This supplements the cross-family audit handoff and is not a Claude audit. Rules read at full HEAD `520b3645a4b8a584cb17eddc64defb97747cb253`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; also handoff 33 and audit-05/e5-evidence.md. Novelty gate **N/A**: review of existing-code repairs, no new mechanism, claim, threshold, ID or novelty assertion. Only this report is written in the repository; no Git mutation, developer-source fix, engine campaign, retry, witness regeneration or Syvert execution by this reviewer.

## Candidate identity and inspection

Paths below are relative to `topics/padua-argmax-bridge-20261105/`. These are reviewed working-tree bytes, not an invented candidate commit.

| File | SHA-256 |
|---|---|
| `code/local_onset512_campaign/return_bundle.py` | `3f903e62b5c155e85603be43a60724c226b800dd9908685146fd7c5b69c2c234` |
| `code/local_onset512_campaign/check_reader_repairs.py` | `68bc9b7047b5b9c081c4e9f7f59828d79f3568398d3e2bcaad437ba6aa75cd9d` |
| `code/local_onset512_campaign/runner.py` (unchanged) | `a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad` |
| `compact_pack/storage.py` (unchanged) | `274d009dbba97a34729b21d1319e26f684406ad8313782397c5a83ed88c69768` |
| `code/onset512_analytic/check.py` | `5ce8cc0701ed105fa619674993583f749046709cb02d233570e2dedc59ca1d2d` |
| `code/independent_phase_checker/runtime_probe.py` | `9f1c503e5c0b0739c1e4d85a5f2b920cc515f0d55f2c3039b66ce59278fd1751` |
| `code/local_onset512_campaign/README.md` after wording correction | `9bd96336c8823328af1c53ac3679e8d3cd351d8a8c7409e326933e81b36d7059` |

Inspection confirms the reader admits only the new registered paths: a top-level `.preserve.lock` with exactly zero bytes, and a per-pass `storage-dedup.json` with exactly the producer's four keys, actual nonnegative integers (booleans excluded), the producer's fixed scope string, and consistent relink counts. The producer really creates both names. The consistency rule permits zero-length immutable files with positive relinks and zero logical bytes, as it must. Receipts are validated when present; their existence is not promoted to a scientific proof obligation. Existing path, inventory, external SHA, helper, historical runner, typed exit and source-pin checks are retained.

The reader's default archive SHA stays `da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e`; the trusted manifest SHA stays `5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16`; historical campaign runner stays `459d0728a0cb264d241bc76d270209842fc2aa55c0fadd32e23f8e3b0523af9e`. The current runner is not credited with that historical execution.

## Independent execution

Working directory `/workspace/padua_research`; scratch directory `S=/tmp/padua-audit05-supplementary`. Environment: Linux x86_64, kernel 6.18.57, glibc 2.41, Python 3.12.14 (Clang 22.1.3 build), NumPy 2.3.5, GCC Debian 14.2.0-19. No random scientific input. The custom reader fixture retains seed hex `00`, yielding sample `[435,499]`. The developer roundtrip also exercises its real exporter-created random selection; it is a transport sample, not a scientific result.

Exact commands actually run (shell variable `S` is notation for the absolute scratch directory above):

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/check_reader_repairs.py > /tmp/padua-audit05-supplementary/reader-regression.json
python3 -E -B /tmp/padua-audit05-supplementary/independent_reader.py /tmp/padua-audit05-supplementary/reader-data > /tmp/padua-audit05-supplementary/reader-independent.json
python3 -E -B /tmp/padua-audit05-supplementary/independent_analytic.py > /tmp/padua-audit05-supplementary/analytic-independent.json
gcc -shared -fPIC -O2 /tmp/padua-audit05-supplementary/mxcsr_review.c -o /tmp/padua-audit05-supplementary/mxcsr_review.so
python3 -E -B /tmp/padua-audit05-supplementary/independent_runtime.py /tmp/padua-audit05-supplementary/mxcsr_review.so > /tmp/padua-audit05-supplementary/runtime-independent.json
python3 -E -B /tmp/padua-audit05-supplementary/independent_pins.py > /tmp/padua-audit05-supplementary/pins-independent.json
```

All final commands exited **0**; harnesses catch expected rejections, rather than reporting those expected cases as child successes. The analytic harness launches actual subprocesses and records their exits below. A first analytic-harness attempt exited 1 due to the reviewer's comparison of the emitted result against the entire archival receipt, including receipt-only provenance fields. I corrected only that scratch comparison to compare emitted keys; rerun passed. No developer code changed for this harness error.

### Reader and storage

The independently executed developer suite passes **60 controls**, including the existing negatives, real producer roundtrip, source-pin-before-checker failure, external archive/manifest pin failures, optimization refusals, typed exits, historical runner pin, unsampled/fresh-certificate linkage, unsafe names, extra members and transport bounds. Its large-size controls adapt ZIP metadata, not actual multi-GiB archives; do not interpret them as an allocation stress test.

My separate reader harness reuses only `fixture()` to generate synthetic scientific records. Its own storage setup, exporter call, rewritten ZIPs and assertions are separately written. For each degree/pass it calls **actual `storage.deduplicate()`**; even degrees have both `S-build.json` and `lambda-build.json` referencing six empty immutable files, odd degrees have no build manifests. Observed: **382 receipts, 1,152 examined paths, 1,151 actual relinks, zero logical bytes relinked, empty actual lock**. Real `completed()` and `export()` run, all 382 receipt files and the empty lock appear in the ZIP, and the reader accepts **191 pairs / 382 proofs**, invoking four sampled closure adapters.

The actual exported synthetic ZIP is `S/reader-data/producer.zip`, 1,956,540 B, SHA-256 `620b1cf9b6e4f6875c023dea6164c703d5585d7e60f4448abf95dc310288d794`. It is test data, not a replacement canonical artifact.

The custom harness then rewrites and rehashes ZIP inventory for each of **17 expected rejections**:

| Mutation class | Observed rejection |
|---|---|
| missing count, extra key, nonobject receipt | storage dedup receipt schema |
| boolean, string or negative count | nonnegative integer counts |
| relinks exceed examined; nonzero bytes with zero relinks | consistent counts |
| wrong scope | storage dedup scope |
| duplicate count key; NaN | duplicate JSON key; nonfinite JSON |
| one-NUL-byte lock | preserve lock must be empty |
| extra top-level file; nested lock; extra pass receipt; job 999; nested receipt member | corresponding unregistered campaign/pass/job/nested member |

**Adapters and limits:** both positive suites use synthetic certificates and replace trust pins, essential-proof arithmetic and sampled closure validation. My harness copies actual reader/runner bytes into a temporary package and points `ROOT`, `RELEASE` and script locations there; it does not adapt storage, `completed()`, export, member validation or ordinary reader linkage. The result is real producer-to-reader transport coverage with arithmetic adapters, not acceptance by the real scientific checker. This distinction also applies to the developer's positive suite.

Separately, actual unmodified `R.pins()` passed against this workspace: **13 frozen source files and 180 arithmetic files**. Independent negative controls change only the identity-return SHA for (a) FREEZE.json, (b) frozen `build.py`, and (c) `flint/NTL-interface.h`; each actual `R.pins()` invocation rejects the mismatch. These are identity-return adapters, not modified source files. The regression's ordering control confirms an exception from the pin function prevents checker construction. This review does not re-label the adapter-positive reader run as a real-checker positive.

### Analytic guard and new lower bound

The checker now refuses optimized Python before its assertion-bearing computation. Its new assertion uses the exact rational interval's **lower** endpoint, `log(PI).lo > F(11,10)`. Normal execution passes and matches every emitted non-version key of historical `receipt.json`, including all eight enclosures.

Scratch `false_gate.py` changes only `peak.hi < 41/1000` to `<1/1000`. Scratch `false_logpi.py` changes only the new lower bound from `>11/10` to `>2`. Neither is production code.

| Case | Actual child exit / result |
|---|---|
| original `-E -B` | 0, eight intervals unchanged |
| false peak `-E -B`; false log-pi `-E -B` | 1 each, `AssertionError`, empty stdout |
| false peak `-O -B`; `-OO -B` | 1 each, optimization refusal, empty stdout |
| false peak `-B`, `PYTHONOPTIMIZE=1` | 1, optimization refusal, empty stdout |
| false peak `-E -B`, `PYTHONOPTIMIZE=1` | 1, `AssertionError`, empty stdout |
| false peak `-E -O -B`, `PYTHONOPTIMIZE=1` | 1, optimization refusal, empty stdout |
| original `-E -B`, `PYTHONOPTIMIZE=1` | 0, eight intervals unchanged |

The guard closes the reported false-PASS path even when `-O` is explicit; `-E` correctly ignores environment optimization but cannot override explicit `-O`. This is a code/control check, not a new proof review of all analytic series bounds.

### Runtime probe under adversarial MXCSR

The independent C helper consists only of `_mm_getcsr()` and `_mm_setcsr()` wrappers. The Python harness imports NumPy and the real probe before setting modes; computes `np.array([2.0**-1022])/np.array([2.0])`; reads its `uint64` view **without a floating-point comparison**; invokes real `runtime_probe.main()` in the same thread; and restores original MXCSR in `finally` after every case. Initial MXCSR was `0x1fa2`.

| Mode / MXCSR | Computed division bits | Actual probe outcome |
|---|---|---|
| nearest / `0x1fa2` | `0x0008000000000000` | accepts; 31 arithmetic controls, four probes true |
| FTZ / `0x9fa2` | `0x0` | rejects: gradual_underflow false |
| DAZ / `0x1fe2` | `0x0008000000000000` | accepts; 31 controls, four probes true |
| **FTZ+DAZ / `0x9fe2`** | **`0x0`** | **rejects: gradual_underflow false** |
| round down / `0x3fa2` | `0x0008000000000000` | rejects: ties_even_up false |
| round up / `0x5fa2` | `0x0008000000000000` | rejects: ties_even_down false |
| round toward zero / `0x7fa2` | `0x0008000000000000` | rejects: ties_even_up false |

This directly checks the reported adversarial FTZ+DAZ failure. It establishes finite behavior in the present process only. DAZ by itself is not rejected: these inputs do not test consumption of a subnormal operand. No universal IEEE, SIMD-loop, library or historical-worker conformance claim follows.

## Finding and disposition

**SE5-01 MINOR, resolved.** The reader README inherited present-tense “All evidence remains under the named local-output/ tree,” contrary to the stated missing canonical ZIP and unverified custody. Reported to developer/coordinator; the coordinator changed it to the historical write location and explicitly limited current availability. I reread the corrected bytes (README hash above). No source fix was made by this reviewer. No further code rerun was needed for this prose-only correction.

E5-05..07/E5-09 remain accurately scoped notes: the compact verifier's unchanged optimization behavior was not rerun; ZIP mode metadata remains data rather than executable content; export-side `completed()` retains its bool-equals-zero weakness while the reader rejects noninteger exits; the reader remains specific to the historical campaign. Those notes are not new failures of these repairs.

## Local execution identities and remaining limits

Scratch scripts/reports are local working output, not archived evidence. Their availability beyond this workspace is not guaranteed; no cold-storage transfer is claimed. The durable developer regression reproduces the repair's essential positive/negative controls from committed source. Additional independent controls have these exact identities for custody and reproduction from retained scratch files:

| Scratch file under `S` | SHA-256 |
|---|---|
| `independent_reader.py` | `d05a101d238beef390c3dab697d7b3e6c048c0e3832cc69e616b12d0f9844662` |
| `independent_analytic.py` | `070eda7858ed0e5129d77fcc4e8e7893c6d2f048e1ac0770edbc299042ce0ab9` |
| `independent_runtime.py` | `fae745887af4069475efcb4286db240a824dc010f865fc72bbead6ae09d9ced8` |
| `independent_pins.py` | `32e19fa73d0428acab7460cd9d9a065ecd8765ddead9f87cbd37cafcb9f92ca3` |
| `mxcsr_review.c` | `9ca8bfdb2a526763b5bbc268a9196e09aa28c6ea8d0836584e3d55cf37fd7add` |
| `mxcsr_review.so` | `2fedf9a68bf5e3b13d9bae51f4dcba3a2430d0e47240f7a60971b1bca85dfac9` |
| `false_gate.py` | `ac028546c6f3c0695d2a16cf7b641e4daf17c2b6ba96e35cd0322ac664212657` |
| `false_logpi.py` | `d726ad0f17360ce4cb126f3832157236aae77c046c76305fa66fa8c34faf8aae` |
| `reader-regression.json` | `d4fcdad4ec08211be01055a13188a2205e647bbd895760a5c55d4161189b0ff9` |
| `reader-independent.json` | `c0795e30ea1d911187adfa5216b2372e0e64216eb27a89221c875821c23aa663` |
| `analytic-independent.json` | `fe1a4bea301da25da8c75bb55aefa5d90c082a1541db5491738f593701be50ed` |
| `runtime-independent.json` | `9d36b9ad6faf496621d7a196c5e140e33d0485c6b50d8bb617b8633e13fe302f` |
| `pins-independent.json` | `169bbb6d9281931900e1178530ccea03ec5af17bc991355acdb16e0681a85d46` |

No repeat of the unchanged compact-return verification is claimed. The absent canonical onset ZIP, I25 bundle, derivative/inventory/review ZIPs and native histories are not supplied by these synthetic controls. Canonical compatibility, data-only I25 checks and historical custody remain governed by the existing open-evidence record. This supplementary check does not grant PR readiness or discharge the next cross-family audit.
