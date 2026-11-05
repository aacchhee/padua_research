# Local artifact inventory — padua-lanczos-nonproduct-20261105

Status: **local working artifacts only; external archival pending**. No file
has been delivered to AC's cold storage, and no historical receipt alone is
treated as proof of staging. These indexes describe local observations;
they are not a `padua-cold-storage-v1` retrievable archive for
`tools/cold_storage.py verify/restore/export`. A later actual archive needs
that tool's manifest/export procedure and verification. The machine-readable inventory observes actual
local files at generation time and separately records missing paths and
identity mismatches. It does not promote an incomplete execution to success.

## Inventory and committed checker output

| Inventory | Contents | Content identity and provenance |
|---|---|---|
| [evidence-manifest.json](evidence-manifest.json) | Committed code and compact evidence receipt indexes | Each indexed chunk has bytes/SHA-256; each code/receipt has bytes/SHA-256 and Git blob ID at the recorded source head |
| [cold-storage.json](cold-storage.json) | Index of actual external working-file observations | Each raw-file entry has path, observed bytes/SHA-256 and availability, with references to the committed receipt and its exact identity/command JSON pointers |
| `inventory/*.json`, as indexed above | Bounded machine-readable chunks | Each file is below16KiB; only chunks named by the current indexes are authoritative |

Receipt basenames in external-file references resolve under this topic's
`evidence/` directory through the hashed receipt inventory. A reference's
JSON pointer identifies its exact path field; sibling `bytes`/`sha256`
fields, when supplied, preserve the expected identity. `command_pointers`
locate the frozen generating command in that same immutable receipt. This
avoids duplicating long commands for every log while retaining the full
source-command-data chain. Empty command pointers mean the receipt supplied
no enclosing command; consult its recorded execution context and the linked
attempt/method record rather than inventing one.

Completed checker results are in the committed
[mathematical review](independent-checks-math.md),
[scan review](independent-checks-scans.md) and their indexed execution
receipts. Their scope limits remain authoritative. Raw producer/checker
rows, logs, exact inputs, basis exports and unsuccessful run artifacts stay
outside Git. No third-party fulltext PDF or extract is included.

## Regeneration and handoff

The generator reads code and evidence bytes from the **committed source
head**, ignoring working-tree edits and uncommitted receipts:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/inventory_evidence.py
```

Only explicit receipt paths under the campaign's `/tmp` directory are read
by default; it does not recursively search arbitrary files or execute any
recorded command. To inspect a preview without changing the topic, add
`--output-dir /tmp/padua-lanczos-nonproduct-20261105/inventory-preview`.
An explicitly supplied additional artifact root must be a specific
authorized directory, never a broad environment/credential directory.

For scientific regeneration, use a fresh working directory and the exact
commands and source/input identities in the relevant receipt. Typical
dependencies are Python3.12, NumPy/SymPy for supplementary algebraic probes,
and g++/GMP for rational native scans. Any FLINT successor records its own
version and dependency path. Do not overwrite the original run's data or
claim byte-identical timing metadata from a new run.

Native endpoint JSONL files optionally have a separate `native-jsonl-v1`
scientific digest: omit only top-level `elapsed_seconds` and
`exact_gram_pairs_checked`, serialize each row with sorted keys, compact
separators, UTF-8 and a trailing newline, then SHA-256 the concatenation in
original row order. This permits exact scientific-field comparison when
run times or whole-run guard counts differ. It does not certify omitted
guards, completeness, correctness or external delivery; those require the
execution/check records.

## Retention and retrieval

Current raw paths are under
`/tmp/padua-lanczos-nonproduct-20261105/`. They are session working storage,
with no retention guarantee after environment reset/deletion. No cleanup of
these raw artifacts was performed. A missing path remains marked unavailable
and must not be described as an archived file.

The repository workflow designates AC's Padua-specific eventual destination
as `Downloads\padua\cold_storage\padua-lanczos-nonproduct-20261105\`.
This session has no demonstrated transfer path to that computer. Delivery is
pending; no unrelated destination was substituted. AC or a later authorized
session can copy the actual retained files, verify their byte sizes and
SHA-256 values, and add a delivery receipt. Until then retrieval means
reading an existing local path and checking its observed identity, or
regenerating from the repository and comparing scientific fields. The
inventory's source head and committed code/data identities survive even
when ephemeral raw files do not.

## Final observation

The inventory source head is `62668c194ea510907f7a2a9d47c33d7c67f7a4dc`.
It indexes40 code files,70 receipts,317 external paths and497 references.
All990 available declared byte/hash comparisons match. Two inherited
frontier G1 paths were outside the explicitly read campaign root and remain
unavailable to this inventory; no new campaign path is unavailable. The
18 JSON index/chunk files total238,041 bytes and each is below16KiB. The
[canonical repository-wide budget observation](LOG.md#canonical-storage-budget-observation)
remains an audit issue. No inventory observation changes a run's status.
