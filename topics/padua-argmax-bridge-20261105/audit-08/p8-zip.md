# P8 focused review of the response-07 public ZIP (handoff 39)

Reviewer: independent Claude subagent P8, Opus 5.5 (xhigh requested; the applied effort is not visible to me). Read-only on the repository.
Repository: /home/user/padua_research, branch codex/padua-argmax-bridge-20261105, HEAD `50070f520b3d5cfe9afbc75f10fdb1bc664b7b71`. `git status --short` was empty before and after.
Artifact: `/root/.claude/uploads/.../fff32280-padua-zenodo-response07-20261114.zip`. I recomputed sha256 `b341e6a1c6875550b58576b2cb167766f5a3cf9a4e4fc620b1134d2c490adbaa` and 5,149,206 B.
Scratch root `P8` = /tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit8/p8. Tools are in `P8/tools`, logs and wait4 receipts in `P8/logs`, and the negatives' JSON in `P8/neg/negatives.json` and `P8/neg3/neg3.json`.

## Environment
- Python 3.13.18, NumPy 2.5.3, g++ 13.3.0 (Ubuntu), 4 cores. No network was used and nothing was installed.
- README requirement wording: "Python 3.12 or newer and NumPy (reference: Python 3.12.14, NumPy 2.3.5) ... (reference: g++ 14.2, GMP 6.3)". My environment meets it as worded. The README's sentence "The audit also passed with Python 3.13.18 and NumPy 2.5.3 for its selected replays and controls" is again true for this audit's runs. (I did not check whether g++ 13.3 is acceptable; the README states no minimum compiler version.)

## Method
1. I ran a fresh `unzip -q` of the uploaded ZIP into `P8/x0`. It was `diff -r`-identical to the caller's `zip-ro`, and I then made it read-only.
2. Each run used its own read-only copy (`P8/w1..w6`). Each negative control used its own writable copy (`P8/neg/*`, `P8/neg3/*`).
3. After the runs, w1, w2, w3, w5 and w6 were still `diff -r`-identical to x0, with no `__pycache__`. w4 (R9) was also identical afterwards.
4. Every command ran through `P8/tools/run.py` (adapted from audit-07), which records wait4 accounting. Limits on each child:
   - `RLIMIT_AS` 4,000,000,000 B
   - `RLIMIT_CPU` equal to the wall cap
   - core size 0
   - minimal environment (`PATH=/usr/bin:/bin`, `OPENBLAS/OMP_NUM_THREADS=1`)
   - process-group SIGKILL at the wall cap
5. All package Python ran as `python3 -E -B verify.py` from inside the copy.

## Commands executed

| # | Command (cwd = copy) | Caps wall=CPU s / AS | wait status | CPU s | wall s | max RSS KiB | Result |
|---|---|---|---|---|---|---|---|
| C1 | `python3 -I P8/tools/census.py x0 audit7-zip-ro repo` (my checker) | 300 / 4e9 | 0 | 0.537 | 0.604 | 51,616 | RESULT PASS |
| R1 | `python3 -E -B verify.py` (README integrity command, verbatim) | 120 / 4e9 | 0 | 0.283 | 0.305 | 48,436 | `PASS integrity: 942 phase records / 471 degrees; 39 polynomial certificates`, then `PASS requested verification` |
| R1b | `python3 -O -E -B verify.py` | 120 / 4e9 | 256 (exit 1) | 0.206 | 0.303 | 22,696 | `ValueError: Python optimization is not permitted` |
| R1c | `python3 -OO -E -B verify.py` | 120 / 4e9 | 256 (exit 1) | 0.209 | 0.256 | 22,336 | same refusal |
| R2 | README quick command, verbatim: `--degrees 41,511 --polynomial-degrees 2,17 --analytic` | 900 / 4e9 | 0 | 33.014 | 33.488 | 163,016 | 4 PASS phase lines; analytic assertions PASS; both tables `failures: []`; `PASS analytic: exact gates and both 60-entry tables`; PASS polynomial n=2 and n=17; PASS requested verification. Ran concurrently with R5-R7. |
| R3 | `--controls` | 900 / 4e9 | 0 | 3.747 | 3.813 | 78,784 | `PASS controls: 27 corruptions rejected; 3 substitutions accepted` |
| R4 | `--analytic` | 900 / 4e9 | 0 | 0.801 | 0.807 | 48,580 | PASS analytic line, then PASS requested verification |
| R5 | `--degrees 77,150,222,333,410,487` (degrees not replayed before) | 1500 / 4e9 | 0 | 47.539 | 48.104 | 153,632 | 12/12 PASS phase lines (both records of each degree) |
| R6 | `--polynomial-degrees 5` | 1200 / 4e9 | 0 | 2.311 | 2.721 | 158,368 | PASS polynomial n=5 (hash and count comparison included) |
| R7 | `--polynomial-degrees 21` | 1200 / 4e9 | 0 | 32.364 | 33.143 | 281,488 | PASS polynomial n=21 |
| R8 | `--polynomial-degrees 28` | 1200 / 4e9 | 0 | 142.149 | 143.585 | 842,136 | PASS polynomial n=28 |
| R9 | `--polynomial-degrees 34` | 1200 / 4e9 | 0 | 546.938 | 551.524 | **1,929,040** | PASS polynomial n=34 |
| N | `timeout 2400 python3 -I P8/tools/negatives.py x0 P8/neg` (69 cases, 3 threads; each child 600 CPU s, 4e9 AS, 900 s timeout) | 2400 wall | 0 | not separately accounted | 60 | — | 64 cases matched my pre-stated expectation and 5 deviated (see below) |
| N3 | `timeout 600 python3 -I P8/tools/neg3.py x0 P8/neg3` (corrected table mutation, 4 cases) | 600 wall | 0 | not accounted | about 1 | — | 4/4 as expected |

Read-only inspection with git, grep, pdfinfo and pdftotext is not listed. Not run: `--degrees all` and `--polynomial-degrees all`, as handoff 39 excludes them, and polynomial degrees 35..40.

## Task 1: census (my own checker, `P8/tools/census.py`): all PASS

**Files and ZIP metadata**
- 1,019 regular files and 10,229,741 expanded bytes, with no symlinks.
- ZIP members: 1,019 entries, all Unix mode 0644, no directory entries, no extra fields, no comment, deflate throughout, one timestamp 2026-11-14 10:00:40, and nothing outside `padua-reproducibility/`.

**SHA256SUMS and MANIFEST**
- SHA256SUMS: 1,018 sorted lines in the `<64 hex>␠␠<path>` format, LF only. Every hash matches, and together they cover exactly every file except SHA256SUMS itself.
- MANIFEST `payload`: 1,017 unique paths, equal to the file set minus {MANIFEST.json, SHA256SUMS}. Every byte size and sha256 matches.
- `public_adapter_sha256` (`92319b64…`) equals verify.py.

**Phase inputs and expected results**
- Phase inputs: 942 manifest rows covering exactly n0041..n0511 × {produce, verify}. The file names match exactly, and strict parsing found no duplicate keys or NaN. Each `n` is an int equal to its slot. The origins are 560 "authenticated complete retained input" and 382 "regenerated complete retained input".
- Expected results: 942 strictly parsed rows over the exact population, all accepted, with pair-equal scientific fields. The summary counts and exact minima (with their argmin degrees) recompute exactly from the rows.

**Polynomial inputs and receipts**
- 39 polynomial inputs n0002..n0040, each byte-identical to `git show HEAD:<mapped path>`, with the correct gunzipped `n`.
- Stored receipts: the 2-16 and 17-32 compact rows plus n33..40 cover 2..40. Each stored `certificate_sha256` equals its MANIFEST polynomial sha256.

**Delta against the audit-07 package**
- Byte-compared with audit7 `zip-ro`: the same 1,019 names, 1,010 members byte-identical, and the changed set is exactly the nine members {MANIFEST.json, SHA256SUMS, README.md, README.txt, verify.py, analytic/tables/paper.tex, analytic/tables/companion.tex, papers/paper.pdf, papers/companion.pdf}.
- MANIFEST `phase_inputs` and `polynomial_inputs` are identical to the old manifest.
- Changed top-level MANIFEST keys:
  - `builder_sha256` is now `fabac559…`, equal to HEAD and dce3260 build.py.
  - `license` wording changed from "in repository" to "in this package".
  - `manuscript_source_freeze` changed from null to 5f435be.
  - `public_adapter_sha256` and `public_adapter_source_commit` changed (77e4f1e to dce3260).
- Changed payload rows: exactly the seven non-list members.

**Git identity**
- 30 mapped sources are byte-identical to `git show HEAD:<path>`. They include README.md, README.txt (both map to `T/code/zenodo_public_20261114/README.txt`; README.md is a byte copy) and verify.py.
- verify.py is also identical at dce3260.
- Both `analytic/tables/*.tex` equal `paper/sections/comparison-unified.tex` and `companion-paper/sections/comparison-unified.tex` at both 5f435be and HEAD. `git diff --stat 5f435be HEAD` on paper/ and companion-paper/ touches only BUILD.md, README.md, build.sh and check_correspondence.py, with no .tex.
- Table delta against the old package:
  - The "Repository paths below are relative to `topics/padua-argmax-bridge-20261105/`" sentence was added.
  - The base_table.py sentence was added (2 places).
  - One cross-reference rewording in companion.tex.
  - No numeric table entry changed, and `--analytic` passes.

**PDFs**
- paper.pdf: sha256 `d51627f5…`, 812,804 B, 59 pages. companion.pdf: sha256 `9de87206…`, 1,223,870 B, 152 pages.
- Both equal the MANIFEST source sha256 and bytes (source_freeze 5f435be) and the delivery receipt `zenodo-public-response07-delivery.json`.
- pdfinfo: Author Andrey Chesnokov, Creation/ModDate Sat Nov 7 00:00:00 2026 UTC (a fixed build epoch).

## Task 3: new verify.py checks and negative controls
I wrote down an expectation for every case before running it. Of 73 cases (69 + 4), 68 matched it, and the 5 deviations are all selection-parsing cases (P8-01, P8-02). My first table mutation, M20, edited a different, unlabelled tabular and was accepted. That was my targeting error, not a verifier fault, and N3 redid it on the labelled table.

**Previously accepted in audit-07, now rejected**
- N04: an extra file with SHA256SUMS refreshed but not MANIFEST → `manifest payload population differs`.
- N12: a duplicate key in every expected row, refreshed → `duplicate JSON key`.

**New checks, rejected as intended**
- Expected-results parsing:
  - M01: a duplicate key in one expected row → `duplicate JSON key`.
  - M02: `NaN` → rejected.
  - M03: `1e999` → `nonfinite JSON number`.
  - M04: `Infinity` → rejected.
  - M21: a trailing blank line → JSONDecodeError.
- Manifest population and payload:
  - M06: a missing payload file with sums refreshed → `manifest payload population differs`.
  - M08: README.txt edited with sums refreshed → `manifest payload identity README.txt`.
  - M09: a wrong payload byte count → `manifest payload identity verify.py`.
  - M10: a duplicate payload path → `duplicate manifest payload path`.
- Polynomial inputs (all rejected at integrity, before any replay):
  - M11: n5/n6 inputs swapped, sums and manifest refreshed → `stored polynomial certificate identity`.
  - M12: n5 re-gzipped, sums and manifest refreshed, receipts not → same message.
- Polynomial receipts:
  - M14: n5 first leaf deleted, with receipt sha, sums and manifest refreshed. Integrity PASS; replay rejects (the frozen check.py exits nonzero → CalledProcessError).
  - M15: stored n5 splits +1, refreshed. Integrity PASS; `--polynomial-degrees 5` → `polynomial stored result mismatch 5`.
  - M16: stored n21 bound −1, refreshed. Replay 21 → `polynomial stored result mismatch 21`.
  - M17: n37 `accepted:false`; M18: n3 returncode 1; M19: n30 row removed. All rejected at integrity.
- Phase-input population: M22, an empty subdirectory in `phase/inputs` → `phase input population`.
- Tables: M20 (N3), the first lower endpoint of the labelled `uc:base-values` table changed 5.257495→5.257494 in paper.tex and in companion.tex, refreshed. Integrity PASS; `--analytic` exits 1 for both.

**Old controls still rejected**
- N01, N02, N03, N05: byte change, missing polynomial input, extra unlisted file, extra phase input.
- N06: n41 bytes in the n42 slot → `phase input degree`.
- N07: produce/verify swap with only sums refreshed.
- N09a: one-record endpoint change → pair check.
- N11b: replay against a tampered expected row.
- N13, N14: duplicate key and NaN in an input.
- N15, N16: traversal line and duplicate line in SHA256SUMS.
- N17, N18: symlinked input file and symlinked directory.
- Lowered endpoints, all integrity PASS and rejected at replay:
  - N22: S endpoint in both n100 records → `stored upper below independent lower`.
  - N24: lambda endpoint in both n100 records → `stored lambda upper below independent lower`.
  - N22x: new degree n410 → same as N22.
- -O.
- Bad selections: `--degrees 40`, `512`, `41,41`, `all,41`, `41,`; `--polynomial-degrees 41`, `1`, `x`.

**Still accepted (by design)**
- N08: produce/verify swap for n300, fully refreshed, replay 300 passes.
- N20: `origin_lower_hex` zeroed in both n100 records, replay passes.
- N23: a contained S upper raised by +1.0 in both records, replay passes.
- N11a, N22, N24 and M05: integrity-only PASS after a consistent refresh. M05 (an extra key in the expected rows) is then rejected by replay 100.
- M07: an extra file added to both SHA256SUMS and the MANIFEST payload.
- M13: n5 re-gzipped with identical JSON and every identity refreshed; integrity and replay both pass.
- M23: an empty directory at the root.
- N21: CRLF SHA256SUMS, harmless because `read_text` normalizes newlines.

**What the README says about the still-accepted cases.** "Trust and expected results" now states the following, which accurately covers every still-accepted consistent-refresh case:
> "SHA256SUMS and MANIFEST.json are inside this package. PASS integrity establishes internal consistency, including the file population against both lists; it does not establish authenticity. Authenticate the ZIP against its externally published checksum in a signed or otherwise trusted deposit record before use. For degrees not replayed, confidence in stored results rests on that external archive identity and the embedded checksums."

N08, N20 and N23 are covered by "The independent checker substitutes independently computed enclosures; it does not establish that every stored native endpoint is valid." P7-03 is resolved. Residual note: no external checksum yet exists, because there is no deposit. That is consistent with "implies no upload".

**Static review of the new code** (verify.py lines 23-35, 53-68, 79, 132-151, 164)
- `loads()` is shared by inputs, MANIFEST, receipts and expected rows. Duplicate keys, NaN/±Infinity constants and overflowing floats are all rejected.
- Population is checked against SHA256SUMS (l.54), the MANIFEST payload (l.59), phase/inputs (l.68) and polynomial/inputs (l.89).
- `polynomial_records` runs inside integrity, so certificate identity covers all 39 degrees even without replay.
- Replay compares `{certificate_sha256, counts}` exactly with the stored record (l.164).
- After a failed replay (M14b) no `/tmp/padua-public-*` directory remained. After R9 finished, `/tmp` had no `padua-public-*` directory.

## Task 4: README as a new user
- Integrity versus authenticity: stated correctly (quoted above).
- Memory: "Polynomial degree 33 used about 1.7 GB RAM in that audit; allow more for higher degrees. The quick smoke covers only polynomial degrees 2 and 17." Measured peaks: n21 281 MB, n28 842 MB, n34 about 1.93 GB (1,929,040 KiB max RSS). The guidance is accurate but gives no upper figure for n35..40 (P8-05).
- Python wording: "Python 3.12 or newer" plus the 3.13.18 sentence, scoped by "these tests do not establish universal conformance". P7-07 is resolved.
- Disclosure (my grep of the extracted package):
  - `/home/ahomel/a/andreyac/num_tests/padua30`: 2,242 occurrences, exactly in the 560 authenticated-retained inputs (the set equals the manifest origin set). README: "The 560 retained phase inputs include /home/ahomel/a/andreyac/num_tests/padua30/..." Accurate.
  - `/workspace/padua_research/`: 1,556 occurrences in exactly the 382 regenerated inputs, MANIFEST.json (2, the PDF source paths), analytic/receipt.json, receipts n0037..n0040, and README itself. README: "other records retain /workspace/padua_research/..." Accurate, though it does not enumerate the files.
  - `/opt/codex/runtimes/codex-primary-runtime/...`: in receipts n0037..n0040 only (plus README). README: "receipts for degrees 37..40 retain /opt/codex/runtimes/... paths". Accurate.
  - `/root/a1_develop`: 1 occurrence, in `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md` line 170. It is not named as a path but falls under the README's "internal provenance and process prose" (P8-04).
  - Process text in the corner .md (6 lines): "Claude audit-01 ACCEPTED", "Claude remains the required auditor", "PR #6 audit", "Codex development subagent ... gpt-6.1-sol xhigh", `PD-T?programme-ideas-claude-04`. README: "including model names and audit and PR references". Accurate.
  - Elsewhere, "codex" appears only in that file name, as referenced by `finite_general.py` and `native_checker/check.py` and in MANIFEST/SHA256SUMS. No absolute path in any gzipped polynomial certificate (0 of 39). No `/tmp/`, `/Users/` or `/mnt/` paths anywhere.
  - Relative `local-output/...` strings appear in 387 files. They are harmless and not absolute.
- Licence, DOI and upload: "This package supplies no standalone license grant ... invents no license, DOI or authorship and implies no upload." MANIFEST license says "in this package". Nothing is invented.
- Stale statements: no occurrence of the old ZIP hash or size, 77e4f1e, d6dd673, or the old PDF hashes in README, MANIFEST or verify.py. No stale wording found.
- Rendering: README now uses Markdown headings and fences, so it renders properly. 9 lines still exceed 80 characters (the longest is line 121, at 93), which is cosmetic.

## Task 5: PDFs (pdftotext; quotes from the paper, p. 56-57)
Certification paragraph:
> "The inputs used for this version combine the 560 authenticated certificate records for degrees 41, . . . , 319 and 511 with 382 newly generated records for degrees 320, . . . , 510. … A new execution of the independent direct-sum checker recertified all 942 records … No stored native numerical endpoint is a premise of this recertification. A separate fresh execution rechecked both records at each of degrees 41, 458 and 511 … The polynomial checker was freshly compiled and rechecked on degrees 2 and 17; the accepted records for all 39 polynomial certificates are retained, and no new full 39-degree replay is claimed. The reproduction record regeneration-20261114.md identifies …"

Data and code availability:
> "Manuscript and checker sources are maintained at https://github.com/aacchhee/padua research. … The public verification kit for this version contains the 942 phase certificate inputs (560 retained and 382 new), the 39 retained polynomial certificates, minimal unchanged checker sources, expected results, exact analytic checkers, verification commands and both manuscript PDFs. A separate preservation archive, held by the author in cold storage, contains the full native histories, runtime payloads and versioned source snapshot. The public kit is intended for deposit in Zenodo; it has not yet been deposited and no DOI has been assigned. Section 5 states the finite verification scope and its implementation assumptions."

- The companion (p. 149-150) carries the same DAS verbatim. It also has: "The public verification kit includes the 39 retained polynomial certificates, the 942 phase certificate inputs (560 retained and 382 new), minimal unchanged checker sources and expected verification results. The kit compiles the polynomial checker afresh; a fresh compilation was checked on degrees 2 and 17. …"
- These match the kit as censused: 942 = 560 + 382, 39 polynomial inputs, the unchanged checker closure, expected results, the analytic checkers, verify.py and both PDFs. They also match the preservation scope. **P7-01 is resolved.**
- Placeholder scan (TODO, XXX, FIXME, TBD, `??`, lorem, placeholder): none. "pending" occurs only in mathematical prose (companion: "no pending region").
- Reporting only (AC-reserved):
  - "Development draft, 8 November 2026." (paper) and "Development draft." (companion)
  - the AI declaration naming Claude Opus 5.5, GPT-6 Astra and GPT-6.1 Sol
  - "Final human review and publication preparation remain to be completed."
  - "not yet been deposited and no DOI has been assigned"
  - ORCID 0009-0004-4687-1810, contributions, funding

## Findings

**P8-01 MINOR: an empty selection silently skips replay and still reports PASS.**
- Where: `verify.py` lines 176 and 181 (`if a.degrees or a.controls:` / `if a.polynomial_degrees:`).
- Evidence: `--degrees ''` and `--polynomial-degrees ''` exit 0 with `PASS requested verification` and no replay (N19; returncode 0, wall about 0.4 s). `degrees()` would reject an empty list (l.101), but it is never called because `''` is falsy. A script that builds `--degrees "$LIST"` with an empty variable gets a false PASS of "requested" verification.
- Fix: test `a.degrees is not None` and `a.polynomial_degrees is not None`, and let `degrees()` reject empty or blank text.

**P8-02 NOTE: abbreviations and whitespace are accepted in selections.**
- argparse prefix matching accepts `--degree 41` (it replayed 41), and `int(' 41')` accepts surrounding whitespace.
- Harmless. Optional fix: `allow_abbrev=False` and a strict `^\d+(,\d+)*$|^all$` pattern.

**P8-03 EDITORIAL: the README lists expected output in a different order from the actual output.**
- Where: README lines 79-81 and 90-92.
- The README lists PASS polynomial before PASS analytic. Actual output order is PASS phase …, about 300 lines of analytic JSON, `PASS analytic: …`, then PASS polynomial …, then PASS requested verification (R2 log lines 14-325).
- A new user may also not expect the large JSON block.
- Fix: reorder the expected lines and mention the JSON output.

**P8-04 NOTE: the disclosure does not name the `/root/a1_develop` path.**
- The disclosure is accurate and complete in substance. The one absolute path not named explicitly is `/root/a1_develop` (1 occurrence, corner .md line 170), which falls under "process prose".
- The README also does not list which non-input files carry `/workspace/...`: MANIFEST.json (PDF sources), analytic/receipt.json and receipts n0037..n0040.
- Per AC's P7-02 decision there should be no sanitisation. Optionally add "/root/... agent path" and the file list to the disclosure sentence.

**P8-05 NOTE: the memory guidance gives no figure for the largest degrees.**
- n34 peaked at 1,929,040 KiB (about 1.93 GB) (this audit) and n33 at about 1.7 GB (audit-07). The README's "allow more for higher degrees" is directionally right, but gives a full-replay user no figure for n35..n40.
- Optional: add the measured n34 figure and say n35..n40 were not measured.

**P8-06 NOTE: `analytic/tables/*.tex` are whole section sources, and only one table in each is checked.**
- Each file is a complete `comparison-unified.tex` section (thousands of lines). `--analytic` checks only the labelled `uc:base-values` 60-entry table. Other numeric tabulars in the same file (for example `$C_\infty$ … 1.801591`, my first M20 variant) are not checked, and editing them passes `--analytic`.
- The README ("two tables", "reads only the two included table sections", "both 60-entry tables") is accurate. Mapping these files to the full section sources is unchanged from audit-07. Recorded so nobody reads `--analytic` as checking every number in those files.

**P8-07 NOTE: the PDFs cite repository records that are not in the kit.**
- The certification paragraphs cite `regeneration-20261114.md`, `code/regeneration_i25_20261114/input-freeze.json` and `code/regeneration_20261114/frozen-inputs.json`. These are repository files, not in the kit or its README.
- The DAS directs readers to the GitHub repository, and the paper states once (pdftotext line 1612, in the comparison section) that "Repository paths below are relative to topics/padua-argmax-bridge-20261105/". That is coherent.
- Optional: a README line saying these provenance records are in the repository and the author-held preservation archive, not in the kit.

**P8-08 EDITORIAL: the receipt field name `cleanup` is easy to misread.**
- Where: `zenodo-public-response07-delivery.json` `checks.developer_smoke.cleanup: false`.
- This looks as if it contradicts README line 99 ("Temporary polynomial builds and receipts are removed on exit"). But in HEAD `smoke.py` (lines 34, 47) `cleanup=True` means "the observer had to SIGKILL the process group", so `false` is the good outcome.
- My runs confirm the README: no `/tmp/padua-public-*` directory remained after any run, including the failing replay M14b and the 551 s n34 run.
- Optional fix: rename the field (for example `forced_kill`) in future receipts.

## Disposition of audit-07 findings in this package
- **P7-01:** resolved. The DAS and certification paragraphs describe the kit and the preservation archive separately and correctly.
- **P7-02:** retained with disclosure, as AC decided. The disclosure is accurate (P8-04 is a NOTE only).
- **P7-03:** resolved.
- **P7-04:** resolved (N12, M01-M04).
- **P7-05:** resolved (M11, M12, M14-M19).
- **P7-06:** resolved (P8-05 is optional).
- **P7-07:** resolved.
- **P7-08:** unchanged by design and stated in the README.
- **P7-09:** resolved (N04, M06; M07 is the residual and is covered by the authenticity sentence).
- **P7-10:** resolved (all members 0644).
- **P7-11:**
  - Markdown rendering and licence wording: resolved.
  - 9 lines over 80 characters: remains, cosmetic.
  - `"None"` corner_gap: now explained in the README.

## Verdict
No BLOCKING or MAJOR finding. Everything else matches the repository and the claims: the nine-member delta, the unchanged 942 phase and 39 polynomial inputs, the new strict checks, the README trust and disclosure text, and the PDFs' data statements. One MINOR finding, P8-01, an empty-selection false PASS, is a small verify.py fix that needs a rebuild if AC wants it in the deposited kit. It does not affect any scientific result.

## Limitations
- No full `--degrees all` or `--polynomial-degrees all`. Polynomial degrees 35..40 were not run.
- The provenance of the 560 and 382 inputs beyond the MANIFEST and Git identities was not re-derived (`local-output` is absent).
- CPU for the negative-control harnesses was not separately accounted. The child walls are in `P8/neg/negatives.json`.
- `run.py` sets RLIMIT_CPU per process equal to the wall cap. Children inherit it individually.
- I did not review the current-aux label mode or the supplementary review's own controls beyond what is reported here.
