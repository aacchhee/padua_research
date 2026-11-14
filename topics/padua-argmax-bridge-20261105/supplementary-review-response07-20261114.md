# Supplementary response-07 review — 2026-11-14

Status: **accepted within this focused supplementary scope; no unresolved
finding**. The required focused Claude review of the material data-statement
and ZIP delta remains the next workflow step.

Reviewer: independent Codex supplementary reviewer, requested GPT-6 Astra high;
the runtime does not expose a separate model/effort confirmation. This review
supplements the required focused Claude handoff and does not replace it.
Rules read at `9d3f5e0f8b270d039d78d4ebc0df53269a7892ab`:
`AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`.
Inputs read: handoff 38, audit-07, and its P7, M7 and E7 reports, together with
the relevant adapter, builder, source-correspondence and negative-control code.

The scope is the one paired publication-coherence response and public ZIP
delta. No novelty or new mathematical claim is proposed, so the full IDEAS
novelty read is not applicable. The accepted mathematics, runtime premises,
finite ranges, numerical engine and scientific checkers are not reopened.
Only this new review file is written in Git by this reviewer. Review scripts
and outputs are under `/tmp/response07-review/`; Git operations belong to root.

## Source review

All six edited TeX files were read as a diff against the input head. Both data
statements now identify the public kit's 942 phase inputs (560 retained and 382
new), 39 polynomial inputs, minimal checker sources, expected results and PDFs,
and distinguish the author's separate preservation archive containing native
histories, runtime payloads and source snapshot. The companion no longer cites
itself as a separate preprint. The certification section says the polynomial
checker is compiled afresh. The M7 editorial changes preserve the prior scope.

Independent Python extraction compared every formal statement and numbered
display to input head: **19 statements and 86 displays per tree, all byte
identical**. A separate baseline inventory compared 106 tracked files across
the phase, independent-phase, onset-512, hybrid-engine, small-degree and compact
directories: all bytes equal to input head before the build.

The adapter diff was read in full. Strict JSON hooks now cover expected rows
and reject duplicate keys, NaN, Infinity and overflowing `1e999` values (direct
calls executed). The 39 stored polynomial receipt records were read through
the new normalization function, including all three format ranges; their
certificate hashes agree with the input manifest. Selected fresh replays
compare certificate hash and bound/corner/split counts, in addition to the
existing acceptance predicates. Manifest payload population and hashes are
checked as well as SHA256SUMS. The new current-aux mode does not require retired
historical PDFs.

The README now renders as Markdown, distinguishes internal consistency from
external archive authenticity, describes unreplayed degrees honestly, records
tested versions and the measured n33 memory cost, and explains the analytic
E12 branch behind the string `"None"`. A transient pre-freeze wording issue
(describing that branch as absence of a corner leaf) was reported and resolved
before source freeze. No outstanding source finding remains.

AC's explicit P7-02 choice, conveyed by root, is **retain with explicit
disclosure**. The README names the home/workspace/runtime path categories and
internal model/audit/PR provenance strings. This is a resolved disclosure
choice, not a pending review blocker. No input sanitization or upload is done.

## Artifact identities already checked

The old public ZIP remains 5,138,944 bytes,
SHA256 `15885d34498b7f20c20f4b97453babfa85a09d46490dbcb14c051b429e2ee036`.
The separate preservation ZIP remains 296,189,961 bytes,
SHA256 `d3452a176a220a649ca889cacd43c9c0d96fb75e12ae84849d0a07ee6b7d354c`.
These were independently hashed, not regenerated or modified.

## Paired freeze and PDF checks

The paired TeX/Bib freeze is
`5f435be21f29f6fbf48e6d8cba15346117d7e151`; the separate pointer/current-aux
commit is `daa77deb6371a12f6a6e36ff7b894ebb71a7f232`. All 16 current TeX/Bib
files independently compare byte-for-byte with that freeze.

Executed from the repository root, all exit 0:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --archival
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_baseline_controls.py
python3 -E -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --built-labels --paper-output local-output/padua-argmax-bridge-20261105/response07-paper-20261114 --companion-output local-output/padua-argmax-bridge-20261105/response07-companion-20261114
```

Results: current 19/86/120, archival 13/90/113, seven baseline controls passing,
and 120/120 current built labels equal without historical PDFs. `pdfinfo`
reports 59/152 pages; 152 is below five times 59. Current `main.log` files have
zero errors, overfull boxes, undefined references or multiply-defined labels.
The reviewer inspected logs/artifacts, not a second TeX build.

The PDFs under the two output directories above have these identities:

| PDF | Bytes | SHA256 |
|---|---:|---|
| paper/main.pdf | 812,804 | `d51627f5b42a647233ae76f95a25754d6b0dff7fbe2ca156d563473ee20c8d39` |
| companion/main.pdf | 1,223,870 | `9de87206d4988dd2997016ba9885f2ec5cd59a110ab36abac5576d50dfa877fc` |

`pdftotext -layout` located the changed paragraphs. Pages were rendered with
`pdftoppm -f N -l N -scale-to 1200 -png -singlefile` (1400 for the main data
statements/trust/timing pages) and inspected: paper 20, 42, 55, 56, 57;
companion 56, 94, 107, 146, 149, 150. All are legible. The public/preservation
distinction is present in both data statements and the companion's final
certification paragraph; the updated trust footnote, retained/new population,
local measure-inequality pointer and rounded timing render correctly.

Root identified that the old builder's immutable preservation receipt would
select the previous PDFs. The developer changed the builder to require a new
`--pdf-identities` record. I reviewed that fix before the adapter checkpoint:
it validates exact paper/companion roles, full source freeze, absolute paths,
integer byte sizes and hashes before output creation, ships the cached
validated bytes and records the manuscript freeze in the manifest. The old
preservation receipt is untouched.

The new aux mode was also called on disposable copies of the actual current
aux files: a missing source label and a changed built number were both rejected
with the appropriate diagnostic.

Root's `/tmp/response07-mutation-harness.py` and output
`/tmp/response07-mutations.jsonl` were reviewed, not independently rerun.
Normalizing only `HEAD` and `BASELINE` assignments makes the harness exactly
equal to committed `audit-06/code/b6-code/mutation_harness6.py`; its SHA256 is
`c571617de1d7afab4fa068b3f4fe80ee44b6e6e4f6b54acc9a097f9cae1f9b2e`.
It uses adapter head `dce3260b88c11a964168a64c34b168ac37f2a11c` and paired
freeze `5f435be21f29f6fbf48e6d8cba15346117d7e151`. All 13 scenario outcomes
were checked: unchanged S0 and README-only S7 pass, all eleven source mutations
fail the strict freeze. The rename scanner's known ability to accept a declared
fake rename is preserved, not mistaken for a mathematical test. Root's
`/tmp/response07-notation.out` reports the empty-map comparison against prior
freeze `e861c752218f...` passing with 19/86 and zero declared renames.

## New public ZIP delta

Adapter/builder checkpoint:
`dce3260b88c11a964168a64c34b168ac37f2a11c`.
New ZIP:
`local-output/argmax-bridge-20261105/zenodo-public-response07-20261114/padua-reproducibility-20261114.zip`.
Independently recomputed SHA256:
`b341e6a1c6875550b58576b2cb167766f5a3cf9a4e4fc620b1134d2c490adbaa`;
**5,149,206 bytes, 1,019 files, 10,229,741 expanded bytes**.

The independent `/tmp/response07-review/zip_delta.py` checked both ZIPs with
`testzip`, unique safe member names, exact manifest/checksum populations and
every embedded byte-size/hash. Every new member is mode 0644. The file set is
unchanged. Exactly nine file contents differ: `MANIFEST.json`, `SHA256SUMS`,
`README.md`, `README.txt`, `verify.py`, the two analytic table TeX files and the
two PDFs. The other **1,010 files are byte-identical**, including all 942 phase
inputs, 39 polynomial inputs, expected result rows/summary, polynomial receipts,
scientific checkers and required provenance closure. The table-file changes are
the already reviewed explanatory paragraphs, not table values or formulas.

The README copies agree. Thirty source-mapped files equal their Git bytes at
the adapter checkpoint. The manifest's builder hash equals that checkpoint's
builder; its paired-source freeze and per-PDF freeze match `5f435be...`.
The shipped PDF bytes equal the inspected PDFs above, so the rendered data
statements are the actual public-kit data statements. The retained disclosure
bytes are unchanged. No source snapshot, native histories or runtime binaries
were added to the public kit.

Actual census command (exit 0), from the repository root:

```sh
python3 -E -B /tmp/response07-review/zip_delta.py local-output/argmax-bridge-20261105/zenodo-public-20261114/padua-reproducibility-20261114.zip local-output/argmax-bridge-20261105/zenodo-public-response07-20261114/padua-reproducibility-20261114.zip /tmp/response07-review/zip-delta.json
```

The archive was independently extracted with Python `zipfile.extractall` to
`/tmp/response07-review/extracted/padua-reproducibility` after the safe-name
census. Numerical commands use that extraction, not the developer's tree.

## Bounded reader commands and controls

The exact README commands were executed once each from the extraction:

```sh
python3 -E -B verify.py
python3 -E -B verify.py --degrees 41,511 --polynomial-degrees 2,17 --analytic
```

They ran through an unmodified off-Git copy of audit-07's `p7-code/run.py`,
which records `wait4` status and child-inclusive CPU accounting, applies CPU/AS
limits, disables core files and kills the process group at the wall cap.
The wrapper commands were:

```sh
python3 -I /tmp/response07-review/tools/run.py integrity /tmp/response07-review/extracted/padua-reproducibility 120 4000000000 -- python3 -E -B verify.py
python3 -I /tmp/response07-review/tools/run.py quick /tmp/response07-review/extracted/padua-reproducibility 300 4000000000 -- python3 -E -B verify.py --degrees 41,511 --polynomial-degrees 2,17 --analytic
```

| Command | CPU/wall caps | Wait status | CPU s | Wall s | Peak RSS KiB |
|---|---|---:|---:|---:|---:|
| Integrity | 120/120 s | 0 | 0.361 | 0.403 | 44,444 |
| README quick | 300/300 s | 0 | 25.855 | 25.914 | 154,468 |

Both have 4,000,000,000-byte AS limits. Integrity reports the stated 942/471/39
population. Quick reports all four selected phase records accepted, polynomial
n2/n17 accepted after a fresh kernel build, and the single analytic PASS line
after exact gates and both 60-entry tables. Both end with PASS requested
verification. The helper's minimal PATH selects **Python 3.13.5, NumPy 2.2.4,
g++ 14.2.0**, distinct from the developer's reference environment. This observed
success does not establish general runtime conformance.

The negative-subset command was:

```sh
python3 -E -B /tmp/response07-review/negative_subset.py /tmp/response07-review/extracted/padua-reproducibility /tmp/response07-review/negative-controls /workspace/padua_research/topics/padua-argmax-bridge-20261105/audit-07/code/p7-code/negatives.py
```

It reuses the P7 disposable-copy/refresh/run helpers with their 600-second CPU,
900-second subprocess-wall and 4,000,000,000-byte AS caps. **Nine of nine
controls reject as expected**: P7 N01 changed byte, N04 extra file with refreshed
sums, N12 duplicate expected-row key with all hashes refreshed, N15 checksum
traversal, N17 symlink; plus NaN and `1e999` in expected rows, a stored polynomial
hash inconsistent with the input manifest, and a tampered n2 bound count.
The count tamper passes integrity but its selected n2 replay rejects with
`polynomial stored result mismatch 2`, demonstrating the new replay comparison.
All other listed controls reject before integrity PASS. The subset's own exit
status is 0; deliberate verifier rejections return 1. The extra n2 replay is
only this negative control, not another successful smoke campaign.

After execution all extracted payload hashes remain unchanged, and all 106
baseline core-tree files still equal the input head. No full 942-record or
39-degree run, new native campaign, new certificate, new theorem premise,
license, DOI, authorship or publication-status claim was introduced.

## Off-Git evidence and limits

All paths in this table are relative to `/tmp/response07-review/`:

| Evidence | Bytes | SHA256 |
|---|---:|---|
| zip-delta.json | 877 | `57821bb08c7a5ea30f24357151fed9a4d636573de100c9a68a46338db0b77771` |
| negative-controls/results.json | 2,917 | `c341b104edc7b26865f2c6e7e86d1bda7179d8dbc59f02520392cbd222d9b871` |
| logs/quick.json | 423 | `0d7e067aa9fffeea00bae7f1f96027900a4d1dff7a05e1ffea1f549176b50d60` |
| logs/integrity.json | 345 | `62ab8d176b8b178f9d4f26bff9684814c8fa5de1a63320ac55d811606fdcafb2` |
| zip_delta.py | 2,117 | `709b92dc4e17a59c67987a10f1940d7723e2605cf6ebfd66479780a8c63d1409` |
| negative_subset.py | 2,070 | `39e15a368bb4de13d66b113df107fa5dc64a5d335888347a4b2e2b975850ca40` |

The original substantive scientific audits and prior broader replays are not
repeated or upgraded here. Preservation archive contents were not re-audited;
only its unchanged complete-file identity was verified. The thirteen-scenario
harness and rename scan were inspected as root executions, while the default,
archival, seven controls, current aux, aux corruptions, ZIP census, reader
commands and negative subset were independently executed by this reviewer.

No unresolved issue remains in this supplementary scope. Handoff 39 should
request only the focused Claude review of the material data statements and ZIP
delta required by handoff 38; it should not reopen accepted science. Other AC
publication metadata and budget decisions remain outside this review. No upload
was performed.
