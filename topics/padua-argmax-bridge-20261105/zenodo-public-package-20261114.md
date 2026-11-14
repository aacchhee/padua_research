# Public reproducibility package design, 2026-11-14

Developer: Codex; instructed gpt-6.1-sol, medium; effective serving metadata unexposed.
Rules/source head: 656c15b758c3cf49782adb3af8b1bced361179e6.
Scope: packaging and standalone input adapter, no new mathematics, native production campaign, or full numerical rerun. The novelty gate is inapplicable. This design is sent to the orchestrator before implementation.

The 296,189,961-byte archive remains unchanged as supplementary custody. It is an unnecessarily large and indirect normal public deposit. Essential input bytes are only 5,553,537 bytes for 942 phase JSON records and 196,496 bytes for 39 compressed polynomial certificates. The replacement contains ordinary named files and a root README.

## Exact proposed public layout

- `README.md`, `MANIFEST.json`, `SHA256SUMS`, `verify.py`
- `phase/inputs/n0041-produce.json` through `phase/inputs/n0511-verify.json`: 942 byte-identical current inputs, two proof records for each of 471 degrees.
- `phase/check.py`, `phase/controls.py`, `phase/runtime_probe.py`: unchanged trusted numerical core and controls.
- `phase/expected-results.jsonl`: every current accepted scientific observation; only CPU timing omitted, source mapping retained in manifest.
- `phase/expected-summary.json`: complete counts and exact margin minima.
- `analytic/check.py`, `analytic/base_table.py`, `analytic/receipt.json`, `analytic/tables/{paper,companion}.tex`: unchanged exact arithmetic and comparison-table source sections.
- `polynomial/inputs/n0002.json.gz` through `n0040.json.gz`; compact accepted receipts.
- A small `topics/` source closure preserving original checker-relative paths: the metadata checker driver, metadata freeze/patch/kernel; baseline strict checker/kernel; four original provenance-only part3 Python files; corner dependency text. These paths permit unchanged strict driver and provenance predicates rather than altering numerical code.
- `papers/paper.pdf`, `papers/companion.pdf`: current paired PDFs.

No archive reader, historical input tar, repository clone, producer, internal handoff, audit history, operating system, runtime binary, or full toolchain is required by the public replay. Source mapping and hashes are metadata, not filenames users must interpret.

## Dependency trace and pruning

The phase core imports only Python standard library and NumPy. Its controls import only that core and NumPy. The public adapter replaces only the historical tar/new-inventory input loader. Both proof records remain separately represented because the published execution claim checked 942 records, even though the theorem has 471 phase degrees. Their scientific fields coincide degree by degree; they are not 942 different theorem cases.

The polynomial metadata driver imports the baseline strict checker dynamically and verifies five frozen source identities. The strict checker reads four part3 source files and the corner dependency text solely for certificate provenance; it imports none of their production functions. Retain those exact bytes and the baseline kernel because frozen metadata requires them. All other producer and native campaign files are excluded. All 39 retained inputs have been traced through the current frozen-inputs.json mapping (2–16, 17–32, 33–40 source roots).

The analytic gate checker has only standard-library dependencies. The comparison-table checker needs its adjacent gate checker plus the two comparison table sections supplied by explicit paths; no complete LaTeX tree is needed to run it. The PDFs provide the mathematical reduction and premises.

## Adapter and bounded verification preregistration

Before numerical work, `verify.py` must hash every listed file, reject missing/extra phase or polynomial input names, enforce all 471 degree/pass pairs and all 39 polynomial degrees, verify each JSON degree and expected row identity, and establish per-degree scientific input/result pair equality. The manifest maps every public input to its exact original source path/member and hash. SHA256SUMS covers all deliverable files except itself; the manifest lists the scientific payload without circular self-hashes.

Phase replay invokes the unchanged `check.check(data, cache)` directly, reusing cache only within one degree and emptying it on degree change. It compares every scientific output field exactly to the expected current observation; CPU is not compared. Same-process runtime probes and arithmetic controls precede numerical replay. `--degrees 41,511` is the preregistered bounded developer smoke (four records); `--degrees all` is available for readers and is not run during package construction. A separately selectable negative-control mode uses the unchanged corruption_controls on n199, whose mutations assume degree 199. Positive substitution controls adapt the existing three n41 data substitutions without changing numerical predicates.

Polynomial replay compiles the unchanged metadata kernel with C++17 and GMP, invokes the unchanged strict driver on retained files, and checks the resulting acceptance and complete-partition fields. Preregistered bounded developer checks: n2 and n17 only. No full 39 replay is claimed.

The root README must distinguish hash/population checks, actual numerical replay, recorded outcomes, mathematical premises, and host binary64/NumPy assumptions. Finite runtime probes do not prove universal IEEE conformance. No license grant, DOI, authorship, or publication destination is invented.

The orchestrator approved this layout. Implementation is in `code/zenodo_public_20261114/`. The root supplies the actual source checkpoint through required `build.py --source-commit <40-hex-SHA>`, distinct from the scientific dependency base recorded above. A root README.txt is byte-identical to README.md. Historical accepted polynomial records cover 2–16, 17–32, and individual degrees 33–40.

Static independent review corrected the public full-polynomial replay timeout (removed because some existing checks exceed 600 seconds), added complete accepted-receipt coverage and original path mappings for unchanged source files, and separated adapter checkpoint identity from the scientific base. The public full command is deliberately uncapped; the prospective bounded developer smoke has an outer owned-child observer.

Prospective developer command: `python3 -E -B code/zenodo_public_20261114/smoke.py --execute` after the orchestrator source checkpoint. It runs only phase41/511, polynomial2/17 with one fresh build, and exact analytic gate/table checks. The observer sets a single CPU affinity, a 300-second per-process CPU cap, 600-second total wall cap, 2 GiB address-space cap and zero core size; timeout cleanup kills/reaps the entire owned process group and records direct wait4 status, inclusive CPU, wall and maximum RSS. Stdout/stderr and receipt stay outside the public package. No repeated full scientific campaign is authorized or required here. Independent review owns data-only structural negatives plus a separate n458 bounded replay.

## Concrete artifact and executed bounded checks

The adapter/build/README/observer source checkpoint is `77e4f1e73f59098ee280d9ed681a33d823e5e7aa`. Static independent review cleared the final builder (`20f5a8cba14851947ebe09d36f6dcee8d111f00ada7655b873a05808948f14a8`), adapter (`792a1ec126ef4b934ba0282bc6cebf4a991362ad95e2d104eedbe6dc84582853`) and observer (`4de568109d35806f1171b0d6c94cda18636bc2645f3e8fc504e19f25c877b94f`) before execution. The normal ZIP was built once from that checkpoint with `build.py --source-commit 77e4f1e73f59098ee280d9ed681a33d823e5e7aa`.

Artifact: `local-output/argmax-bridge-20261105/zenodo-public-20261114/padua-reproducibility-20261114.zip`, **5,138,944 bytes**, SHA256 `15885d34498b7f20c20f4b97453babfa85a09d46490dbcb14c051b429e2ee036`. It contains 1,019 files, 10,213,669 expanded bytes, all 942 phase records and all 39 polynomial certificates. README.txt and README.md are byte-identical. Public accepted polynomial summaries are selected scientific rows with original source path/hash, without internal audit/model prose or CPU timing; individual accepted receipts for 33–40 remain unchanged. MANIFEST supplies the current complete input inventory.

Executed normal public integrity command: PASS all 942/471/39. Executed the preregistered observer exactly once: wait4 status 0, return code 0, inclusive CPU 26.515693 seconds, wall 38.006790054 seconds, maximum RSS 153,208 KiB, no cleanup, empty stderr. All four phase results (41 and 511, both records) exactly match current expected scientific output; one freshly compiled unchanged polynomial metadata kernel accepts degrees 2 and 17; exact analytic assertions and both 60-entry comparison tables PASS. These are bounded adapter checks, not a new full 942-record or 39-degree numerical rerun. The build receipt, observer receipt and stdout/stderr are retained beside the public ZIP outside its immutable payload.

The prior preservation ZIP was independently rehashed locally: unchanged 296,189,961 bytes, SHA256 `d3452a176a220a649ca889cacd43c9c0d96fb75e12ae84849d0a07ee6b7d354c`. AC reports that it is now in cold storage; no external retrieval or transfer is independently asserted. No public upload, DOI or publication metadata was created. Independent fresh extraction, structural negatives and n458 replay are recorded separately by the reviewer.

**Dated note, 2026-11-14 (Claude audit-08, in-place MINOR fix).** The 5,138,944-byte ZIP (`15885d34…`) described above was superseded by the response-07 rebuild: 5,149,206 bytes, SHA256 `b341e6a1c6875550b58576b2cb167766f5a3cf9a4e4fc620b1134d2c490adbaa`, with exactly nine changed members; see [zenodo-public-response07-delivery.json](zenodo-public-response07-delivery.json) and [audit-08](audit-08.md). Source: [audit-08 M8-07](audit-08/m8-manuscripts.md).
