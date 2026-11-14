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
