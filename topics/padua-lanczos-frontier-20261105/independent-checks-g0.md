# Independent G0 replay — 2026-11-05

**Verdict: FAIL / campaign blocked under the original G0 kill criterion.** All five separate executions exited 0, including both degree-12 scalar-certificate regenerations. Exact checks pass, but the E6 T24 degree-12 numerical row differs from the frozen row; its precise historical cause remains unresolved. The measured dependence on BLAS kernel is evidence for a plausible explanation class, not proof of the historical cause. No tolerance was introduced to turn this mismatch into PASS.

## Role, scope and provenance

- Supplementary independent checker: Codex, requested allocation `gpt-6-astra`, high. Model identity/effort follows the orchestrator allocation; no separate runtime model metadata is exposed to this worker.
- Rules and code snapshot: `8359bf7a047d9a212bd841224fb97a458cb7435e`, branch `codex/padua-lanczos-frontier-20261105`.
- Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, handoff `01-work.md`, and drift README/source/provenance relevant to this replay. Applied the cloud-environment runtime skill before network restoration.
- This is a replay with no new mechanism, novelty, mathematical claim or status upgrade. The full novelty scan is therefore outside scope. This supplementary check does not replace the Claude audit.
- Only this report is written in the shared checkout. No Git mutation was performed. Frozen code was exported by read-only `git archive 8359bf7a047d9a212bd841224fb97a458cb7435e` into `/tmp/padua-lanczos-frontier-g0/replay`; all executions below use that unmodified snapshot. Bytecode writing was disabled.
- The requested degrees-2–6 alternative is not an option of `e1_reproduce.py`: its inspected CLI accepts the two fixed degree-12 certificates. Both documented full replays were performed instead. This is explicitly degree 12, not a claimed degrees-2–6 sweep.
- Four runtime inputs were absent due to the repository's documented cold-storage move. Their exact Git blobs were read with `git cat-file blob <blob>` into the isolated replay tree, then checked against both recorded byte size and SHA-256. Retrieval succeeded; this is not a scientific mismatch. The shared tree was not repopulated.

## Environment and restored input identities

Python 3.12.14; Linux 6.18.57 x86_64, glibc 2.41; NumPy 2.3.5; SciPy 1.17.0; SymPy 1.14.0; mpmath 1.3.0; python-flint 0.9.0; backports.cached-property 1.0.2. Every numerical execution used `OPENBLAS_NUM_THREADS=1`. Current NumPy runtime reports OpenBLAS 0.3.30, Haswell, one thread; NumPy uses ILP64 and SciPy's build uses LP64. Historical provenance gives the same package versions/platform and threads setting, but does not pin the runtime CPU dispatch or shared-library bytes.

Dependencies were installed outside Git with:

```sh
python -m pip install --target /tmp/padua-lanczos-frontier-g0/deps python-flint==0.9.0 backports.cached-property==1.0.2
```

An initial default-sandbox network attempt failed with socket permission errors. The same network operations succeeded using the supported network-enabled tool permission, preserving proxy and CA settings. No domain-policy bypass occurred.

Polyrat source was retrieved from `https://codeload.github.com/jeffrey-hokanson/polyrat/tar.gz/6903d7af9995c9d88e661fb229626696e00fdfba` into `/tmp/padua-lanczos-frontier-g0/polyrat`. Its four used source hashes exactly match `external-code.md` and `e6-provenance.json`; the unchanged namespace adapter called actual upstream functions. This is not a full polyrat installation test.

| Restored evidence basename | Bytes | Git blob | SHA-256 |
| --- | ---: | --- | --- |
| `audit-02-e1-checks.json` | 108115 | `3e55e1ae08824fa181fdf9f7ddd711a80ca97d80` | `7bb3e3b566d7d25d369ee812c007b690b46bbdcc54b55ceb54f18fec9390d0ee` |
| `e1-multinode-certificates.json` | 55328 | `da3db41d9fa5e1f8deefb131ba44885cdfa16b6c` | `fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0` |
| `e1-scalar-cgs2.json` | 444008 | `128bdee846faa4f7db9447823b81f0fe9b1fc60c` | `e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8` |
| `independent-scalar-01.json` | 186681 | `4bc83fa25380bd7a9fe04c05d076a4cea35cba52` | `2d06b3b4e04956f9c9e2f4127c3937543dc92ee071de2926589d0a40c9bf6a10` |

## Commands actually executed

Working directory: `/tmp/padua-lanczos-frontier-g0/replay`. For these commands, set `PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps`, `OPENBLAS_NUM_THREADS=1`, and `PYTHONDONTWRITEBYTECODE=1`. Help was executed successfully for the three programs exposing argparse; E5 source and README were read because it has no help CLI.

```sh
python -B tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set triangle --output /tmp/padua-lanczos-frontier-g0/reproduce-triangle.json
python -B tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set rotated --output /tmp/padua-lanczos-frontier-g0/reproduce-rotated.json
python -B tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --output /tmp/padua-lanczos-frontier-g0/scalar-finite.json
python -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py > /tmp/padua-lanczos-frontier-g0/e5-exact.json
python -B tracks/bivariate-lanczos/code/drift/e6_benchmark.py --external /tmp/padua-lanczos-frontier-g0/polyrat --sets T24 --grid-degree 12 --output /tmp/padua-lanczos-frontier-g0/e6-T24.json
```

The actual executable resolved to `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python`. The local orchestration harness captured E5 stdout and copied the identical bytes to its JSON output. Each process started separately at about 09:51:11 UTC; the rotated replay finished about 09:53:44 UTC. Timings are wall times with concurrent replays, not performance benchmarks.

| Run | Exit | Seconds | Output bytes | Output SHA-256 |
| --- | ---: | ---: | ---: | --- |
| `reproduce-triangle` | 0 | 2.760 | 927 | `d2622612ba90f903e2b716ae17a6a4ec0e7045ed99d0b0ddcb7ae524c596df7d` |
| `reproduce-rotated` | 0 | 152.841 | 925 | `b9e2caec4a9e36e4f26ec51c3ccff6f79827503aed33c5b200ebc96fd41fbc7b` |
| `scalar-finite` | 0 | 0.065 | 7066 | `71356c807f496deb439199f57834e7f2b107b9c3fa4d1fea4e40ea2563d263ad` |
| `e5-exact` | 0 | 0.781 | 854 | `ba6efdcd1dfd4f10c5b27cd1574689c1500f37abb834bf8a2910b76a448dacd3` |
| `e6-T24` | 0 | 0.674 | 6465 | `47215d4cc60807445fa5b31d4acb00ac89f2065b8353a1a18218f4bd14f260f6` |

## Exact-check outcomes

- **E1 triangle and rotated: PASS.** The wrapper independently regenerates target capacities, signs, expected random-sign lower squares and explicit greedy-sign lower squares, compares them exactly with the pinned compact certificate, and checks the explicit final normal projection. Degree 12, BJ, target columns 86 and 90 respectively. The triangle receipt matches every stable field in committed `e1-reproduction-triangle.json`. The explicit-projection input hash differs because it hashes a temporary artifact containing paths/timings, as the README warns; this is explained metadata variation. Both stable source/certificate/generator hashes match.
- **Finite scalar checker: PASS.** The fresh `sets` and `input_pins_verified` objects equal the committed `response-02-e1-scalar-finite.json` objects exactly. All exact decisions pass. Squared certificate ratios remain 657331.0774535049 (triangle) and 62.08553668985878 (rotated), displayed as floats only after exact decisions. The rotated factor-ten certificate remains inconclusive; a lower certificate ratio below 100 is not a proof that the true ratio is below 100.
- **E5: PASS.** The full fresh JSON equals committed `e5-exact-checks.json`, including symbolic formulas and versions, byte for byte. These are finite symbolic corroborations, not a new all-degree proof.
- The scalar checker was run without `--regenerated`: this run does not freshly recompute the two full-graph comparator uppers. It checks their pinned exact records and reused independent evidence. The separate wrapper runs freshly recompute the two BJ lower witnesses. No claim is made that the complete optional four-output regeneration was performed.

The finite checker embeds an old hard-coded `PYTHONPATH=/workspace/padua-drift-runs/python-deps` prefix in its own `command` string. The actual process environment was the one stated above, captured by the independent harness. This known source formatting behavior is not evidence that the old dependency directory existed here.

## E6 mismatch and bounded diagnosis

Compared against `evidence/e6-frozen-grids12.json`, case T24: n=12, M=325, N=91. Input hash is identical. All five local producer/dependency source pins in `e6-provenance.json`, and all four upstream source pins, were checked and match. The selection assertion covers all parents through degree 47. Both old and new results have full numerical reference rank 91 and `trusted=true`. The reference kappa changes only from 9.133757476150816 to 9.133757476150810, with u*kappa about 1.0141e-15. Upstream yx versus local dev remains exactly equal entrywise (maximum difference 0).

| Method | Frozen span gap | Fresh span gap | Relative change |
| --- | ---: | ---: | ---: |
| upstream_xy | 3.3908605229e-10 | 7.5952754186e-10 | +123.99% |
| upstream_yx | 2.4812027023e-10 | 2.7558694937e-10 | +11.07% |
| dev | 2.4812027023e-10 | 2.7558694937e-10 | +11.07% |
| mirror | 1.3221174302e-14 | 1.4562450798e-14 | +10.14% |
| alt | 7.3010222490e-12 | 1.3027152070e-12 | -82.16% |
| adapt | 8.6560954123e-14 | 7.6816304185e-14 | -11.26% |

All new orthogonality maxima are 2.6645352591003757e-15; frozen values are 3.1086244689504383e-15 (3.3306690738754696e-15 for upstream xy). The qualitative ordering of gaps is preserved, but some deviations are large relative to the measured gaps. In particular, the upstream xy absolute difference is 4.2044e-10 and the alt absolute difference is 5.9983e-12. These exceed the reference's u*kappa scale substantially; dismissing them as reference noise is not justified.

Bounded diagnosis performed:

1. Three additional new processes with the same command/environment produced bytes identical to the first fresh E6 output (`e6-T24-repeat0.json` through `repeat2.json`). This excludes a simple nonrepeatable process effect in the current default runtime.
2. Installed fresh public wheels with `python -m pip install --target /tmp/padua-lanczos-frontier-g0/fresh-numeric numpy==2.3.5 scipy==1.17.0`. Repeated the E6 command with `PYTHONPATH=/tmp/padua-lanczos-frontier-g0/fresh-numeric:/tmp/padua-lanczos-frontier-g0/deps`, output `e6-T24-fresh.json`. It is byte-identical to the current default output. This excludes a difference between the preinstalled and freshly fetched versions as the cause here.
3. Repeated the same fresh-wheel command with only `OPENBLAS_CORETYPE=Sandybridge`, `Nehalem`, or `Prescott` changed; output filenames are `e6-T24-<core>.json`. These supported lower-instruction kernels yielded dev gaps 3.56347e-10, 3.24011e-10, 2.78916e-10, and alt gaps 3.15088e-12, 3.02455e-12, 4.74195e-12. This directly establishes arithmetic-kernel sensitivity for this fixed data and code. None reproduced the frozen row exactly. The probe was diagnostic, not a replacement acceptance run.

The old independent record at `checks/audit-02/E6.md` reports exact numerical agreement for its off-sample/n16-grid checks; it does not establish an independent exact repeat of this n12 T24 row in the current runtime. Its build identification “Haswell” does not record historical dynamic CPU dispatch. The original E6 provenance expressly permits BLAS/library variation, but that permission alone does not identify the cause of this observed difference. Kernel sensitivity is a supported explanation class; the historical dispatch/library identity needed to close the causal attribution is unavailable in the inspected provenance. No algorithm or input discrepancy was found, but neither was an exact explanation demonstrated. Therefore the original G0 kill applies and the campaign remains blocked, with no implication that the mathematical results are refuted.

## Receipt inventory and limits

All local receipt paths below are relative to `/tmp/padua-lanczos-frontier-g0/`. They are temporary working artifacts, not a claim of delivered cold storage. The orchestrator must archive/retrieve them using the topic's prescribed cold-storage process if retention is needed. Individual program output hashes above identify the actual new executions; source hashes and exact commands are in the run receipts. No large output or third-party code was added to Git.

| Receipt | Bytes | SHA-256 |
| --- | ---: | --- |
| `restored-inputs.json` | 2869 | `3bd54364f0641e982fc2bdf229c934df5560c425699046417bdca330d317c944` |
| `environment.json` | 770 | `e45a08ebf99b46773da765e245214e35a4224c94b8f781ec2c7c965ac98cfc64` |
| `run-receipts.json` | 3965 | `614bb7993e40e3e804975e83f52de19b6ebab081bc0de84f08a1ae7661d48797` |
| `comparison.json` | 2692 | `d353fc5a15d735bab9af4ea7e4508f03f78020f9f9c331067cd29fe8b908d5df` |
| `blas-config.txt` | 5006 | `422d0bd02b411c8f589a14ea472bd325616a5f9e67a169b9854ee129e78c0bad` |
| `e6-coretype-probes.json` | 2119 | `b84c979a243c99f082235957f7e2feab04e5200d392f7fa60f46387ed6b4f581` |

Remaining obligation: explain the historical E6 numerical discrepancy with recorded runtime provenance or a justified independent numerical analysis, and record a separate G0 disposition before launching scientific runs. Further parameter/kernel fishing was stopped after the bounded diagnostic. This check does not cover the full aggregate sweep, comparator-upper regeneration, PD-T146's two high-degree rows (G4), or any all-degree claim.

## Durable reproduction harness and validation

The topic-local `code/g0_replay.py` now reproduces snapshot recovery, checks all restored/input/source pins, launches the five separate programs, compares the exact records and the T24 metrics, and optionally repeats the bounded diagnostics. It performs no network or Git mutation. Supply the dependencies and pinned external source above, then run from the repository root:

```sh
python -B topics/padua-lanczos-frontier-20261105/code/g0_replay.py --output-dir /tmp/padua-lanczos-frontier-g0/validation --external /tmp/padua-lanczos-frontier-g0/polyrat --pythonpath /tmp/padua-lanczos-frontier-g0/deps --diagnostics --fresh-pythonpath /tmp/padua-lanczos-frontier-g0/fresh-numeric:/tmp/padua-lanczos-frontier-g0/deps
```

This command was actually executed at 09:59–10:01 UTC. All five main programs and all seven diagnostic subprocesses exited 0; both exact regenerations passed again, and E6 repeated the same baseline and kernel-probe values. The harness exited 1 to flag the numerical difference. Its initial automatic label was `FAIL_UNEXPLAINED_E6`; after review, that label alone was corrected to `EXACT_CHECKS_PASS_E6_DIFF_REQUIRES_DISPOSITION`, with a separate dated checker FAIL disposition in the small receipt. The final source was syntax-checked. Computation and comparison logic are unchanged; the receipt preserves both the executed source hash and the final label-only revision hash. Thus bit equality is diagnostic, not a new automatic acceptance criterion.

No new L1–L7 target runs were performed and no source theorem is invalidated. The committed essential receipts are:

- `g0-summary.json`: 11011 bytes; SHA-256 `263ec293bec7249b3b33494a318c684227228342568ff981cc7b22070c6e6c0a`.
- `g0-kernel-probes.json`: 4311 bytes; SHA-256 `5134b53c87a0aabbedf78f46f9b3f81b6e4f9def57d36848f6f16a2ec6474a84`.
