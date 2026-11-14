# New paper-evidence delivery, 2026-11-14

`delivery.py` prepares a **new** downloadable reproducibility bundle from
explicitly supplied completed evidence. It never executes archive code,
native programs, or scientific checkers. It does not recreate the identity
of a missing historical archive or establish numerical correctness. Those
checks and their scope belong in the supplied validation receipts.

The orchestrator supplies the destination and a reviewed configuration;
this directory selects neither permanent storage nor a DOI. Large outputs
stay outside Git. Build only after the campaign, independent checks, and
reviewer outputs have completed and their receipts have been checked.

## Required contents and deduplication

A full configuration must contain each of these asset roles:

| Role | Intended supplied evidence |
| --- | --- |
| `native_return` | Campaign `full-return-20261114.zip`, preserving every full native history, control, accounting/exit record, source, binary, and referenced nonrelease dependency |
| `authenticated_release` | Original user-supplied `padua30.zip`, hash-pinned and retained as inert data |
| `source_snapshot` | Orchestrator's final Git source archive, including manuscript sources, small-degree 2..40 certificate evidence, readers, preregistrations and code |
| `old_proofs` | All 560 authenticated old essential-receipt JSON members, read as data from the pinned old return archive |
| `new_proofs` | All 382 regenerated essential JSON files, plus their staging/inventory record in provenance |
| `independent_results` | Complete 942-case I25 output tree, observations, controls, runtime probes, summaries and outer accounting |
| `independent_review` | Distinct reviewer's actual independently executed replay/control outputs |
| `runtime_dependencies` | Exact supplied trusted runtime artifacts needed to reproduce the native and independent checks, with identity manifests |
| `manuscript_build` | Final paper/companion PDFs, build logs/auxiliary files, and available authenticated publisher class/style/bst dependencies with build-script pins for offline reproduction |
| `provenance` | Input freezes, preregistrations, trust manifest, new campaign and independent validation receipts, delivery instructions and any explicit path mapping |

The role check prevents accidentally omitting a category. It does **not**
infer that declared assets contain all scientifically required evidence:
the orchestrator must verify content against the receipts and use
`expected_files` where meaningful. Do not add synthetic audit scratch or
unrelated old full histories. The old archive can additionally be read using
`tar-members` to expose the essential JSONs directly; its input archive hash
and selected-member count remain in the delivery manifest. Also retain the
authenticated original 36,045,486-byte `return.tar.gz` itself as an inert
`provenance` file: the frozen I25 worker's published command opens that exact
archive and pins its hash. Extracted receipts alone do not close that runtime
input dependency. This supplied archive is distinct from unavailable older
full native histories and needs no historical-archive reconstruction.

The full native archive is included once, intact; do not also add its whole
unpacked tree. The outer ZIP stores every other logical file once per unique
SHA-256 content, so a file referenced by several supplied bounded trees has
one blob and several logical paths. There is no history sampling or pruning.
The original full native inventory remains available in the nested archive.

The outer ZIP contains `MANIFEST.json`, canonical `CONFIGURATION.json`, the
exact accepted `REVIEWED-PLAN.json`, and `blobs/sha256/<digest>`. Its manifest
maps each logical path to byte count, hash, regular-file rwx mode and role. `verify` checks every
outer blob and independently reads every nested native inventory/blob as
data. It checks byte integrity only; use the separate campaign reader for
the scientific `validate_pass` and process-accounting checks. Neither reader
turns a storage receipt into external storage authentication.

## Configuration

Use a JSON file outside Git with `format`, nonempty `description`, and
`assets`. Paths are explicit local inputs. File and tar inputs require a
SHA-256 pin. A tree is frozen in full by the reviewed per-file plan; symlinks
and special files are rejected. Example asset syntax (placeholder hashes
and paths must be replaced):

```json
{
  "format": "padua-regeneration-delivery-v1",
  "description": "New paper-dependent evidence; historical archive identity is not claimed.",
  "assets": [
    {
      "kind": "file",
      "role": "native_return",
      "name": "native/full-return-20261114.zip",
      "path": "/supplied/completed/full-return-20261114.zip",
      "sha256": "SUPPLY_ACTUAL_64_HEX_HASH",
      "profiles": ["full"]
    },
    {
      "kind": "tree",
      "role": "new_proofs",
      "name": "proofs/new382",
      "path": "/supplied/completed/regeneration-20261114-essentials",
      "expected_files": 382,
      "profiles": ["full", "proof"]
    },
    {
      "kind": "tar-members",
      "role": "old_proofs",
      "name": "proofs/old560",
      "path": "/supplied/actual-return-20261107/return.tar.gz",
      "sha256": "b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a",
      "expected_files": 560,
      "members": ["SUPPLY_ALL_560_EXPLICIT_MEMBER_NAMES"],
      "profiles": ["full", "proof"]
    }
  ]
}
```

For the old 560 receipts the explicit member list is
`outputs/all/jobs/{n}/{mode}/essential-receipt.json` for
`n` in `41..319` and `511`, and `mode` in `produce,verify`. The full profile
needs all other role entries as well; this example is deliberately incomplete
and will fail the role check. The authenticated original `padua30.zip` is
25,111,335 bytes with SHA-256
`aac08e5f25bd27b2710de22039efd229b4ee67d8c1e3ffef9456af200e1f74d2`.
Treat its content as data, and supply the matching trust/runtime manifests.

Runtime identity records alone are insufficient for a standalone package:
include the actual pinned independent-checker Python executable, required
Python runtime/standard-library files, NumPy package and its required shared
libraries (including `numpy.libs` where used), with an explicit mapping from
recorded runtime paths to delivered logical paths. Select these bounded
checker-required paths explicitly; do not recursively collect the machine,
all installed packages, compilers, or operating-system directories. Record
any remaining host ABI/loader requirement. The native return already retains
its nonrelease dependencies; the authenticated release supplies its frozen
release dependencies. Avoid duplicating those full trees as separate assets.

Byte restoration and data-only readback do not establish successful
reexecution in a different environment. I25 records include absolute Python
and NumPy paths. A relocated execution needs a new prospective runtime/input
freeze and an explicit path adapter; never edit or pretend to satisfy the
original recorded identity. A compatible native ABI/runtime and compiler
environment remains a prerequisite for a native rebuild. The final source
snapshot must contain the 39 small-degree polynomial certificates and their
checker/source paths, as well as the new readers and run instructions.

An optional `proof` profile selects only assets whose `profiles` include
`proof`. It can provide a small proof/check download, but explicitly lacks
the full native histories and does not replace the full artifact. Include
the required reader/source subset and runtime requirements explicitly. No
implicit profile conversion or evidence dropping occurs.

## Dry proposal, build and readback

Run with Python 3 and `-E -B`. Replace shell variables with the orchestrator's
chosen local paths. First create a dry proposal; this hashes inputs but
creates no package and makes no scientific calls:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_delivery_20261114/delivery.py plan --config "$DELIVERY_CONFIG" > "$DELIVERY_PLAN"
```

Review every logical path, role, count, input identity, archive-member origin
and the `logical_bytes`/`unique_bytes` size estimate. The estimate is the
uncompressed unique payload plus manifest/ZIP overhead; final compressed
size is measured after build. Nested native ZIP bytes remain intact, so its
own internal deduplication is preserved. Verification uses temporary scratch
space up to the size of the nested native ZIP, then removes that scratch.

Only after review, build against that exact proposal. Any changed member,
added file or changed configuration causes rejection:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_delivery_20261114/delivery.py build --config "$DELIVERY_CONFIG" --plan "$DELIVERY_PLAN" --output "$DELIVERY_ZIP"
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_delivery_20261114/delivery.py verify --archive "$DELIVERY_ZIP"
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_delivery_20261114/delivery.py extract --archive "$DELIVERY_ZIP" --destination "$FRESH_DELIVERY_DIRECTORY"
```

Use `--profile proof` for both plan and build of the optional smaller package.
Build refuses an existing output. Extraction validates the full archive
before writing, requires a nonexistent destination under an existing parent,
rejects symbolic-link parents and unsafe or colliding logical paths, writes
regular files exclusively, rehashes each reconstructed file, and restores
only the recorded regular-file rwx bits (including interpreter execute bits;
no setuid/setgid/sticky bits). It adds
`DELIVERY-MANIFEST.json` to the reconstructed root. A failed build/extraction
is left visibly incomplete; there is no automatic retry or overwrite.

Record the build/verify/extract outputs, final ZIP byte count and SHA-256 in
the orchestrator's delivery receipt. Pin or sign that external identity when
transferring the ZIP: internal checks alone do not authenticate an arbitrary
replacement archive. No permanent storage or public availability is implied
by a successful local readback.

Configuration and reviewed-plan controls are retained automatically with
their hashes in the manifest. Do not list the configuration, reviewed plan,
or output ZIP as an input asset; this avoids a self-referential freeze.
Extraction also retains them as `DELIVERY-CONFIGURATION.json` and
`DELIVERY-REVIEWED-PLAN.json`; all three `DELIVERY-*.json` control filenames
and their descendants are reserved against payload collisions.
