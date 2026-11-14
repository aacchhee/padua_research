# 2026-11-14 paper-supporting regeneration

`campaign.py` calls the unchanged runner and frozen engine. Its small committed `frozen-inputs.json` pins the full off-Git machine preregistration and exact runner/wrapper identities. The orchestrator committed this freeze before controls or native jobs. See the topic's `preregistration-regeneration-20261114.md` for scope, commands and stopping policy.

`full_return.py` is a new standalone reader/exporter for this generation. It does not use the old reader's historical runner or canonical archive pins. Export and data-only readback commands, from the repository root:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_20261114/full_return.py export local-output/argmax-bridge-20261105/full-return-20261114.zip
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_20261114/full_return.py verify local-output/argmax-bridge-20261105/full-return-20261114.zip --archive-sha NEW_EXTERNAL_SHA256
```

Run export only after the complete native campaign has terminated. The ZIP stores one `INVENTORY.json` plus unique `sha256/<digest>` objects. The inventory maps every retained logical path to its exact bytes and SHA256. It includes all campaign and controls files, every raw history, native build artifact, and referenced dependency not supplied by the separately authenticated release. Repeated identical byte objects appear once; logical paths remain distinct. The reader does not extract or execute archive content. A separately trusted source checkout, committed new freeze profile and authenticated restored `padua30` release are required. The caller supplies the new archive SHA256 explicitly.

Both export and readback reconstruct and validate every one of the 382 passes through the unchanged trusted `compact_pack.evidence.validate_pass`. They also verify exact observed engine commands and return codes, primary/fresh certificate linkage and retained fields, all case admissions, attempts, wrapper exits, operational controls, stage coverage and terminal quiescence. All archive objects receive independent size/digest checks, including files outside the scientific parser's required set. The full readback remains evidence verification pending independent I25 and audit; it does not perform a new native campaign.

After full validation, export writes `evidence-inventory.json` inside the campaign and stages byte-identical essential receipts into the sibling `regeneration-20261114-essentials/` directory with `<directory>-inventory.json`, for independent I25 reconstruction. The essentials inventory records name, bytes, SHA256 and original source path. Export is exclusive and is not a resume/retry path.

The first data-only preparatory preregistration, replaced before the freeze to respect the repository's generated-file budget, is preserved off Git at `regeneration-20261114-preparation-01/`. It contains no admitted or native jobs.

**Dated note, 2026-11-14 (Claude audit-07, in-place MINOR fix).** The first sentences above predate the completed generation: independent I25 reconstruction and audit are done. I25 consumed the separate `regeneration-20261114-direct-essentials/` staging, not the export's `-essentials/` directory. Four export invocations occurred (the first three failed and are recorded in [native-execution.md](native-execution.md)), so "not a resume/retry path" describes the tool, not the history. The executed export/readback reader was `cf64fbe8…`; the committed final reader `94ca2a76…` differs by one added no-shadow `need(...)` line and has not performed a full accepting readback. Source: [audit-07 E7-05](../audit-07/e7-evidence.md).
