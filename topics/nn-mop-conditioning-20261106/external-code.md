# External source availability and normalization review — 2026-11-06

Current status after AC supplied the exact archive: **M4 PASS; M2 PASS; finite non-Advanpix comparison completed**. The initial access block below is preserved as history and superseded by the dated execution addendum.

Worker: Codex; assigned technical development gpt-6.1-sol medium; serving metadata not independently exposed. Rules/source head `b4a04981d42c7cd872957facf5e3995e4096ca67`. No Git operations or third-party commits by this worker.

## Source identity and current blocker

Required AC archive: `IEP-MOP-main.zip`, 1,020,330 bytes, SHA256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`. The accepted predecessor [G5 receipt](../nn-mop-stability-20261105/g5-run/README.md), [audit](../nn-mop-stability-20261105/audit-g5-01.md), and [complete per-member inventory](../nn-mop-stability-20261105/audit-g5-01/source-inventory.json) pin those bytes; they do not supply the bytes in this workspace. Repository revision of the archive is unknown.

The coordinator's workspace search and this worker's `rg --files /workspace` filename search found no archive/extracted source. The latter does not cover hidden files. `command -v octave-cli` found no executable. Octave installation was not attempted because source execution is blocked independently; installability has not been disproved.

On this turn the supported web connector returned inaccessible/Internal Error for the [public GitLab project](https://gitlab.kuleuven.be/numa/public/IEP-MOP), its main archive, raw `src/utils/kravchuk_exact.m`, and the [SIAM supplement](https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip). Bounded searches for `"IEP-MOP" github`, `"IEP_initial_data.m"`, and `"IEP-MOP-main.zip"` returned no useful source. GitHub fetch rejected the generic repository-search endpoint as unsupported (HTTP400); this is a connector endpoint limitation, not evidence that no mirror exists. No network-policy bypass, proxy removal, contact, or download was performed. Prior shell proxy failure is coordinator evidence, not a new worker shell request.

**Current M4: BLOCKED, not FAIL.** Historical G5 PASS is retained; it is not a new reproduction. **M2: BLOCKED, not numerical mismatch.** No LIT-347 metric table, condition number, or external comparison was run or claimed.

## Fulltext coverage (LIT-347 access addendum, no new LIT identity)

The supported web connector accessed [arXiv v2 fulltext](https://arxiv.org/html/2506.19796v2), 2265 parsed lines, on 2026-11-06. Read relevant fulltext portions: §3.1 equations12–16; §4.2 normalization discussion/equations28–30; all Algorithm2 in §4.3; §6.1–6.2. This is not a claim to read the complete article or authenticate the published PDF/source bundle. The existing [assessment](../padua-literature-20261103/notes/faghih-sinum-2026-assessment.md) was also inspected; its published-paper observations remain attributed there.

LITERATURE, bounded to the portions read: equation14 uses an upper Hessenberg matrix with unit subdiagonal; equation29 converts a nonunit matrix by diagonal similarity. Equation30 permits local products rather than a full accumulated diagonal. Algorithm2 includes monic conversion, while §6.1 retains scaled bases for CORE/REORTH. Equation34 uses relative spectral matrix norm. Section6.2's conditioning error is obtained from a perturbation experiment, not an induced worst-case Jacobian norm. The archive is needed to identify exactly which returned matrices/bases each driver uses.

The HTML Example1 expression and size notation must not override the inspected-source convention in the accepted G5 receipt: that code uses integer nodes0..paperN, hence paperN+1 topic nodes. Likewise reconstruct binomial factors and input preparation from the pinned data functions, not a possibly malformed HTML formula. The local source-family generator includes the binomial factor and normalized nodes. Source fidelity remains M2's job.

## Required restart sequence

1. Supply the exact pinned archive in this executor; verify SHA and all inventory members. Safely extract outside Git and read every executed source file before running.
2. Establish Octave platform and run unchanged predecessor G5 driver/selected paperN10 Kravchuk CORE case against its fixed decade rule. Only actual execution can re-pass M4.
3. Compare local monic reconstruction against pinned `kravchuk_exact`/`hahn_exact` and returned matrices for one configuration to relative1e-12; state node units, path, orientation, scaling and norm. Mismatch kills the LIT metric claim.
4. Only after both pass run requested N4–32 identical-input comparisons. A single step-line matrix omits off-path NN information; obtaining the whole NN triangle requires the additional shifted paths/boundary data. Never fill unobserved NN fields with a reconstruction from insufficient data.

## Superseding execution addendum — AC archive restored, 2026-11-06

The earlier block was resolved by AC supplying `/workspace/attachments/d3b8457a-2c90-4d56-a9a3-f05ea55b5826/IEP-MOP-main.zip`. It matches the required SHA and all27 inventory entries. `code/c4_prepare.py` safely verifies/extracts to `/tmp` and emits exact source-family inputs. All executed third-party files were inspected before running, including all nested functions in the three algorithms. No source edit or third-party commit. Source [receipt](c4-source-receipt.json).

Current status is **M4 PASS; M2 PASS**. Historical blocked records remain above. Unchanged G5 driver completed on isolated Octave9.4, same selected gate result2.691214553706643e-10 as the predecessor9.4 audit. The quoted paper value remains attributed to that receipt, not newly authenticated paper-data bytes. M2 reconstructed exact monic H agrees with pinned exact generators for N6 in both families; [final bit-exact fidelity receipt](c4-m2-bits-receipt.json). Numerical KRYL error beyond1e-12 in this case is distinct from exact-generator normalization fidelity; the same historical c4-m2-receipt.json records both the valid pre-grid
normalization gate and a failed exploratory all-solvers-1e-12 diagnostic.
Only that stronger solver diagnostic was overbroad; the receipt's M2 PASS
remains the authoritative pre-grid gate.

Source inspection resolves the earlier normalization uncertainty: `IEP_CORE` and `IEP_KRYLREORTH` both finish by copying the diagonal, multiplying the first superdiagonal by the raw subdiagonal, multiplying the second superdiagonal by its two neighboring raw subdiagonals, and setting subdiagonal to1. `IEP_KRYL` already has unit subdiagonal. All returned H matrices therefore use the same monic upper-Hessenberg convention as our first-e1 path after integer-coordinate conversion. The returned V/W from CORE/REORTH retain different basis scaling; they must not be substituted into a monic-H eigenvector identity without adjusting the basis.

Source parameters: `kravchuk_data(paperN,.4,.5)` includes binomial factors and nodes0..paperN; `hahn_data(paperN,1,1.5,1)` has (alpha_s+1)_k/k! ×(beta+1)_(paperN−k)/(paperN−k)!, alpha=(1,1.5),beta=1. This exactly matches the frozen rational family before rounding, though archive integer and topic normalized inputs have different rounding histories. The identical-input screen uses normalized arrays imported/exported as IEEE754 hex to avoid decimal JSON-parser rounding. Every compared normalized node and weight bit is checked against the C3 source construction. Ordinary numeric JSON transport failed this check atN12 and was discarded as exploratory; [rejected receipt](c4-exploratory-receipt.json).

### Authorized runtime setup and actual commands

Read the cloud runtime/networking skill and current environment status/policy. Package-manager egress was enforced and Debian allowed. `curl -I` with additional-network permission reached `https://deb.debian.org/debian/dists/trixie/Release` through the inherited proxy. An isolated apt list/cache downloaded octave9.4.0 and17 dependencies from signed Debian trixie metadata. Packages were extracted with `dpkg-deb -x`, never installed into the system. Proxy and CA settings were retained. The first update also consulted inherited snapshot sources, which returned CONNECT403; setting `Dir::Etc::sourceparts=-` selected only the allowed configured source. Package hashes, BLAS/LAPACK and source-output identities are in [runtime receipt](c4-runtime-receipt.json).

Runtime environment for the commands below:

```sh
export LD_LIBRARY_PATH=/tmp/c4-apt/root/usr/lib:/tmp/c4-apt/root/usr/lib/x86_64-linux-gnu:/tmp/c4-apt/root/usr/lib/x86_64-linux-gnu/octave/9.4.0
export OCTAVE_HOME=/tmp/c4-apt/root/usr
```

Source pin/input producer (from repository root; source extraction stays outside Git):

```sh
python3 topics/nn-mop-conditioning-20261106/code/c4_prepare.py --archive /workspace/attachments/d3b8457a-2c90-4d56-a9a3-f05ea55b5826/IEP-MOP-main.zip --extract /tmp/c4-iep-source --inputs /tmp/c4-shared-input.json --receipt /tmp/c4-source-replay.json
mkdir -p /tmp/c4-g5-replay
/tmp/c4-apt/root/usr/bin/octave-cli --no-init-file --no-site-file --quiet --eval "addpath('/workspace/padua_research/topics/nn-mop-stability-20261105/g5-run'); driver('/tmp/c4-iep-source/IEP-MOP-main/src','/tmp/c4-g5-replay');"
/tmp/c4-apt/root/usr/bin/octave-cli --no-init-file --no-site-file --quiet --eval "addpath('/workspace/padua_research/topics/nn-mop-conditioning-20261106/code'); c4_external('/tmp/c4-iep-source/IEP-MOP-main/src','/tmp/c4-shared-input.json','/tmp/c4-fidelity-replay.json','m2');"
python3 topics/nn-mop-conditioning-20261106/code/c4_fidelity.py --external /tmp/c4-fidelity-replay.json --receipt /tmp/c4-m2-replay.json
```

Historical ordering matters: the **pre-grid M2 gate** is
[`c4-m2-receipt.json`](c4-m2-receipt.json), whose selected Krawtchouk
exact-generator error was 8.657548935371719e-17. It passed before the
full grid. The `m2` wrapper mode above selects only Krawtchouk N6; its replay
receipt is a fresh single-configuration check, not a reproduction of the
committed two-family `c4-m2-bits-receipt.json`. The latter was produced
**after** the full bit-transport grid, by applying the fidelity checker to
that full output. Its two selected N6 cases confirm the final transport and
normalization; it was not the gate used to authorize that same grid.
The pre-grid values (reference 8.657548935371719e-17, CORE
7.483383125034624e-15) differ slightly from the post-grid bit-transport
values (7.184849749441866e-17 and 7.47242929475129e-15). Decimal versus
bit transport is a likely explanation, but this cause has not been
proved by a controlled comparison. The difference remains unexplained
beyond that hypothesis; neither receipt is replaced.

Only after the pre-grid M2 and M4 gates pass:

```sh
/tmp/c4-apt/root/usr/bin/octave-cli --no-init-file --no-site-file --quiet --eval "addpath('/workspace/padua_research/topics/nn-mop-conditioning-20261106/code'); c4_external('/tmp/c4-iep-source/IEP-MOP-main/src','/tmp/c4-shared-input.json','/tmp/c4-external-grid-bits.json','full');"
python3 topics/nn-mop-conditioning-20261106/code/c4_fidelity.py --external /tmp/c4-external-grid-bits.json --receipt /tmp/c4-m2-bits-replay.json
OPENBLAS_NUM_THREADS=1 python3 topics/nn-mop-conditioning-20261106/code/c4_compare.py --external /tmp/c4-external-grid-bits.json --native /tmp/nn-mop-c3-grid-raw.json --raw /tmp/c4-comparison-bits-raw.json --evidence topics/nn-mop-conditioning-20261106/c4-tables
```

The external wrapper executes348 calls across both families and every topicN4–32, each in original archive integer mode and shared normalized mode. Original paperN5–30 is included. The external source's remaining Advanpix-only conditioning/backward/random-weight experiments were not executed; a licensed toolbox is unavailable. No statement that every configuration in every archive script has been reproduced is made.

All NN comparisons for the external methods add a high-precision H+d0 functional lift, with d0 calculated from the actual binary64 input. This is labeled as composite postprocessing throughout. It can return a formal moment array lacking positive-real spectral data; no compatible positive common-input inverse is claimed. No eigenvalue-based positivity check, MATLAB experiment, licensed Advanpix reproduction or uniform stability result is inferred from these finite outputs.

### Response replay and table interpretation

The final two-family M2 receipt pins `/tmp/c4-external-grid-bits.json`
(SHA256 `efc7fd299093f433d8936ff628b6df2dd4561ca0572ad9dcdc56ff4ccb697e6b`).
The post-grid fidelity command immediately above reproduces its scientific
payload; the replay output filename is deliberately separate. The comparison
uses `/tmp/nn-mop-c3-grid-raw.json`, the preserved native producer output.
To produce a fresh platform-specific native run, execute:

```sh
OPENBLAS_NUM_THREADS=1 python3 topics/nn-mop-conditioning-20261106/code/c3_grid.py --output /tmp/c3-replay-summary.json --raw /tmp/c3-replay-raw.json
```

Pass that fresh raw path to `c4_compare.py --native` to compare that run;
completion and errors may differ with the numerical stack. A native
`breakdown`, missing method or missing coefficients now produces a recorded
failure status and blank metrics in its CSV row, while other methods remain
available. The original authenticated tables retain their schema and bytes.

CSV columns `a1`, `a2`, `b1`, `b2` and `E_NN` in CORE/KRYL/REORTH tables
measure **returned H plus the input-anchor functional lift**. `H_integer`
measures the returned matrix alone. In C4/A-LU/A-QR/B-nodeqr tables the NN
columns measure native full NN coefficients. The CSV headers are shared
across those methods; interpret them with these method-specific definitions.
The rejected exploratory receipt retains its historical M2/M4 gate labels;
those labels do not validate its discarded decimal-transport comparison.

The response regression command, using preserved authenticated raw inputs,
is:

```sh
OPENBLAS_NUM_THREADS=1 python3 topics/nn-mop-conditioning-20261106/code/response_code_checks.py
```

It writes replay tables and raw output under `/tmp/nn-mop-response-code-checks`,
compares the full healthy scientific payload and every CSV byte, exercises
native failure rows, runs the byte-exact extracted C2 checker, and refreshes
`c1-error-comparison.json` against the final comparison receipt. See
[response-code-checks.md](response-code-checks.md) and its JSON record.

### Audit-02 documented implementation limits (code unchanged)

`c4_compare.py` handles the native producer's fixed schema, including
breakdown rows. Its malformed-input handling is not a general schema or
nonfinite-value validator: a list-valued coefficient, string-valued
measurement entry or integer-valued method source can still raise an
exception; NaN coefficients can be reported `ok`. These shapes cannot be
produced by `c3_grid.py`'s fixed schema and `allow_nan=False` output.
MINOR-6 is addressed by documenting this boundary, without changing code
or the authenticated healthy payload/tables.

`response_code_checks.py` is a historical regression script without CLI
arguments. It requires the exact `/tmp` paths EXTERNAL, NATIVE, BASELINE
and MATRIX declared at its top; the last is
`/tmp/nn-mop-conditioning-20261106/c1-matrix-all.json`. Its work directory
is fixed at `/tmp/nn-mop-response-code-checks`. The source/grid/native and
comparison regeneration commands above describe those producers, but a
fresh platform run need not reproduce authenticated historical raw bytes;
the baseline digest assertion requires the preserved authenticated raw.
The matrix raw pin and diagnostic provenance are recorded in
[response-code-checks.md](response-code-checks.md). No standalone
regeneration recipe for that authenticated matrix raw is supplied here.

A successful regression run overwrites the tracked `c1-error-comparison.json`
and `response-code-checks.json`, including platform strings. Its
`source_commit` is hard-coded to `3d5b29d7aa8c1274793139d7040695035e1bda22`,
not a dynamically observed checkout identity. Running it is therefore not
a read-only verification command. MINOR-7 takes the optional documented-
limitation disposition; an output-argument refactor is not performed in
this documentation-only preparation step. The audit-02 failed invocation
and receipt-only coverage remain recorded in the audit.
