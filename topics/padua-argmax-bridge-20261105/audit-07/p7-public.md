# P7 public-package audit report (handoff 37 items 2 and 3)

Reviewer: independent Claude subagent P7, Opus 5.5 (requested xhigh; I cannot see the effort level the runtime actually applied). Read-only on the repository.
Repository: /home/user/padua_research, branch codex/padua-argmax-bridge-20261105, HEAD `d6dd6730e5413a238f5c55630d0d907fb5e41563`. The working tree was clean before and after the audit.
Artifact: the uploaded ZIP, sha256 `15885d34498b7f20c20f4b97453babfa85a09d46490dbcb14c051b429e2ee036`. I recomputed this hash myself. Size 5,138,944 B.
Scratch root: /tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit7/p7 (called `P7` below).

## Environment (differs from the reference)
- Python 3.13.18 and NumPy 2.5.3. The reference was 3.12.14 and 2.3.5.
- g++ 13.3.0. The reference was 14.2.
- GMP 6.3.0, the same as the reference.
- 4 cores. No network was used and nothing was installed.

## Method
1. I ran a fresh `unzip -q` of the original ZIP into `P7/x0`, then made it read-only (`chmod -R a-w`).
2. The extraction matched the caller's `zip-ro` copy exactly (`diff -r`).
3. Each execution ran in a separate copy (`P7/w1..w6`). After all runs, each copy was still identical to `x0`: no `.pyc` files, no leftovers, and no `/tmp/padua-public-*` directory remained.
4. Every command went through `P7/tools/run.py`, which uses wait4 accounting. The child processes had:
   - `RLIMIT_AS` 4,000,000,000 B
   - `RLIMIT_CPU` equal to the wall cap
   - core size 0
   - a minimal environment (`PATH=/usr/bin:/bin`, `OPENBLAS/OMP_NUM_THREADS=1`)
   - a process-group SIGKILL at the wall cap
5. CPU figures include waited-for children such as g++ and the kernel.
6. Logs and JSON receipts are in `P7/logs/`.

## Commands executed

| # | Command (cwd = package copy) | Caps (wall/CPU s, AS) | wait status | CPU s | wall s | max RSS KiB | Outcome |
|---|---|---|---|---|---|---|---|
| 1 | `python3 -I P7/tools/census.py x0 repo` (my own checker) | 300/300, 4e9 | 0 | 0.462 | 0.503 | 48,516 | RESULT PASS (the first attempt exited 1 because of a bug in my script, a `Fraction('None')` parse; I fixed it and re-ran) |
| 2 | `python3 -E -B verify.py` (README integrity command, verbatim) | 120, 4e9 | 0 | 0.243 | 0.252 | 49,176 | `PASS integrity: 942 phase records / 471 degrees; 39 polynomial certificates` / `PASS requested verification` |
| 3 | `python3 -O -E -B verify.py` | 120, 4e9 | 256 (exit 1) | 0.228 | 0.303 | 22,680 | Refused: `ValueError: Python optimization is not permitted`, before any PASS |
| 4 | `python3 -E -B verify.py --help` | 60, 4e9 | 0 | 0.055 | 0.103 | 17,200 | usage text |
| 5 | **README quick command, verbatim**: `python3 -E -B verify.py --degrees 41,511 --polynomial-degrees 2,17 --analytic` | 900, 4e9 | 0 | 34.058 | 34.549 | 162,320 | PASS 41/511 both records; analytic assertions PASS; both tables 60/60 PASS; fresh kernel build; PASS polynomial n=2, n=17 |
| 6 | `python3 -E -B verify.py --degrees 100,192,256,295,320,384,500` | 900, 4e9 | 0 | 56.698 | 57.404 | 158,096 | 14/14 `PASS phase` lines and PASS requested verification (my grep count of 16 PASS lines adds the integrity and final lines) |
| 7 | `python3 -E -B verify.py --polynomial-degrees 9` | 1200, 4e9 | 0 | 2.584 | 3.126 | 158,172 | fresh build; PASS polynomial n=9 |
| 8 | `python3 -E -B verify.py --polynomial-degrees 33` | 1200, 4e9 | 0 | 485.993 | 490.681 | **1,717,840** | fresh build; PASS polynomial n=33 |
| 9 | `python3 -E -B verify.py --controls` | 900, 4e9 | 0 | 4.001 | 4.067 | 78,096 | `PASS controls: 27 corruptions rejected; 3 substitutions accepted` |
| 10 | `python3 -E -B verify.py --analytic` | 900, 4e9 | 0 | 0.836 | 0.855 | 49,396 | assertions PASS; paper and companion 60 entries each, failures [] |
| 11 | `g++ -O3 -std=c++17 metadata_kernel.cpp -lgmpxx -lgmp -o P7/build/kernel` (my own build) | 300, 4e9 | 0 | 1.692 | 1.759 | 158,740 | binary sha256 71281c96… (the historical binary was f17fed2e…; the compiler differs) |
| 12 | unchanged `topics/.../small_degree_unification/check.py` run directly on n0009 with `--output P7/build/n9.json` | 300, 4e9 | 0 | 0.348 | 0.353 | 17,656 | accepted; counts bound 40, corner 2, splits 41, equal to the stored compact row |
| 13 | the same for n0016 | 300, 4e9 | 0 | 6.667 | 6.730 | 87,128 | accepted; counts 94/2/95, equal to the stored row |
| 14 | `timeout 1800 python3 -I P7/tools/negatives.py x0 P7/neg` | 1800 wall; per child 600 CPU, 4e9 AS, `timeout=900` | 0 | not recorded (sum of child walls about 13 s) | — | — | 25 controls, see below |
| 15 | `timeout 900 python3 -I P7/tools/neg2.py x0 P7/neg2` | the same | 0 | not recorded | about 4 s | — | 6 controls, see below |

Commands 6 to 9 ran concurrently on the 4 cores. Read-only inspection with git, grep, pdfinfo and pdftotext is not listed in the table.

### Python 3.13 compatibility
On Python 3.13 / NumPy 2.5.3 every phase result matched the expected scientific row exactly, all 31 arithmetic controls and 4 runtime probes passed, and the polynomial results matched. I saw no environment effect on results.

## Item 1: independent census (my own checker, `P7/tools/census.py`)
Everything below passed.

**Files and checksums**
- 1,019 regular files, 10,213,669 expanded bytes, no symlinks.
- The ZIP has no directory entries, no extra fields, no comments, and no members outside `padua-reproducibility/`.
- SHA256SUMS has 1,018 sorted lines. Every hash matches, and together they cover exactly every file except SHA256SUMS itself.
- MANIFEST `payload` has 1,017 entries: every file except MANIFEST.json and SHA256SUMS. All byte sizes and hashes match.
- `public_adapter_sha256` equals verify.py (`792a1ec1…`).

**Phase inputs**
- 942 phase inputs, named exactly n0041..n0511 × {produce, verify}.
- Manifest bytes and hashes match. Each parsed `n` is an int equal to its slot. Strict parse found no duplicate keys and no NaN.
- Origins are 560 "authenticated complete retained input" and 382 "regenerated".
- Produce and verify have identical key sets. Across all 471 degrees they differ only in `CPU_stages`, `CPU_through_receipt_start` and `whole_raw_evidence`.

**Polynomial inputs**
- 39 polynomial inputs, n0002..n0040.json.gz.
- Each is byte-identical to `git show HEAD:<mapped source path>`, and each gunzipped `n` is correct.

**Expected results**
- `expected-results.jsonl` has 942 rows, which parse strictly and cover the exact (n, pass) population.
- All rows have `accepted: true`, no CPU field, and pair-equal scientific fields.
- `expected-summary.json`: I recomputed every count from the 942 rows: S 43,116 / 21,558; lambda 1,290 / 645; native containment 42,174 / 43,116 and 942; M_max 30. I also recomputed every exact minimum and its argmin degrees (near 42, far 41, corner 41, floor 1/512 at 41..44, M 13 at 41..51). All equal the stored summary.
- The summary's `minima` also equals the git-tracked `code/regeneration_i25_20261114/RESULTS.json` `exact_minima`, and its `premises` counts match.

**Byte identity with Git**
- 30 mapped source files are byte-identical to `git show HEAD:<path>`. These include both READMEs, verify.py, the 3 phase checker files, the 3 analytic files, 2 table .tex files, 8 receipts n33..40, and the 11-file `topics/` closure.
- README.txt equals README.md, and both equal the Git `code/zenodo_public_20261114/README.txt` (a6417cac…).
- verify.py is the same at HEAD and at the frozen source `77e4f1e`. build.py (20f5a8cb…) and smoke.py (4de56810…) are also unchanged between 77e4f1e and HEAD.
- The phase and analytic checkers equal the scientific base `656c15b`.
- The two PDFs match the `regeneration-delivery.json` sha256 values (paper b0abf068…, companion 3c7a114a…).
- Both compact polynomial summaries equal their Git originals (sources sha b3dfe4ba… and caeaf733…) with only timing columns removed. Degrees 2-16 have actual_returncode 0 throughout.
- Developer and reviewer counts of "32 unchanged mapped sources" = these 30 Git-identical files plus the 2 PDFs.

## Item 2: verify.py soundness, and negative controls on disposable copies
Each control used its own copy, and I re-generated SHA256SUMS and/or MANIFEST where the label says "refreshed". Before running, I wrote down what a cautious reader would assume ("expected"), so the deviations below are the useful findings.

**Rejected as intended**
- changed byte (checksum)
- missing polynomial input
- extra unlisted file (population)
- extra phase input with refreshed sums (phase population)
- n41 bytes copied into the n42 slot, fully refreshed (degree)
- produce/verify swap with only SHA256SUMS refreshed (manifest identity)
- a one-record endpoint change with refreshed hashes (pair-consistency check)
- an S endpoint lowered in both n100 records: integrity PASS, `--degrees 100` rejects with "stored upper below independent lower"
- an actual-lambda endpoint lowered in both records: integrity PASS, replay rejects
- expected `near_min` changed for n100: integrity PASS, replay rejects with "scientific result mismatch 100/produce"
- duplicate key in an input JSON; NaN in an input
- `../outside` line and duplicate line in SHA256SUMS
- symlinked input file; symlinked `phase/inputs` directory (population differs)
- `--degrees 40`, `--degrees 41,41`, `--polynomial-degrees 41`
- `-O`

**Accepted (deviations from a cautious reader's assumption)**
- N04: an arbitrary extra file accepted once SHA256SUMS is refreshed.
- N08: produce/verify swapped for n300, fully refreshed, and `--degrees 300` still PASSes.
- N12: a duplicate key in every expected-results row is accepted.
- N20 and N23: input bytes changed in substituted fields still pass replay. N20 zeroed `origin_lower_hex` in both n100 records; N23 raised an already-contained S upper by +1.0 in both.
- N21: a CRLF SHA256SUMS is accepted. This is harmless because `read_text` normalizes newlines.

**Static review.** The good parts:
- Path traversal and absolute checksum paths are rejected.
- Symlinks are rejected, both on the leaf (`is_symlink`) and on directories (`rglob` population).
- Input and manifest JSON parse strictly.
- `need()` raises explicitly, so the code does not fail open under `-O`, and `-O` is refused anyway.
- The phase cache is a fresh `{}` per degree.
- The whole `check.check` output dict is compared to the expected row minus `pass`/`accepted`. `check.check` returns neither key; acceptance means it returned without raising.
- The polynomial temporary directory is removed (verified after commands 5, 7 and 8).

## Findings

**P7-01 MAJOR (publication coherence; AC decision): the bundled PDFs describe a different package.**
- Where: `papers/paper.pdf` p. ~59, "Data and code availability" (pdftotext lines 3171-3183), and the identical paragraph in `papers/companion.pdf` (lines 8329-8341).
- Evidence: the paragraph says the reproduction package "comprises a versioned source snapshot, the essential certificate inputs, new native and independent-checker outputs, runtime dependencies, and verification commands". It also points readers to repository paths (`companion-paper/main.tex`, `regeneration-20261114.md`).
- Conflict: this public ZIP deliberately excludes the source snapshot, native outputs and runtime dependencies (README lines 9-11, 49; design note). The deposit's own manuscripts therefore misdescribe the deposit they ship in. The described contents fit the 296 MB preservation archive.
- Fix: either AC amends the DAS at the next TeX freeze to describe the public package (and its relation to the preservation archive), or the README says explicitly that the PDFs' DAS refers to the larger preservation archive plus the repository.
- Not scientific; changing the PDFs is AC's freeze decision.

**P7-02 MINOR (privacy; AC decision before any public upload): internal paths and process metadata are in byte-bound files.**
- 560 phase inputs (the "authenticated retained" set) contain absolute paths `/home/ahomel/a/andreyac/num_tests/padua30/...` in `freeze.path`, `whole_raw_evidence.path` and similar fields. These are a personal home directory and username.
- 382 inputs, MANIFEST.json (PDF sources, including `...-015102-Oslo.pdf`), `analytic/receipt.json` and `polynomial/receipts/n0037-n0040.json` contain `/workspace/padua_research/...`. Receipts n0037-n0040 also contain `/opt/codex/runtimes/codex-primary-runtime/...`.
- `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md` (a required provenance input for the frozen strict checker) contains internal process prose:
  - "Claude audit-01 ACCEPTED" and "Claude remains the required auditor"
  - "Codex development subagent `/root/a1_develop`, requested gpt-6.1-sol xhigh"
  - "PR #6 audit"
  - internal IDs `PD-T?programme-ideas-claude-04`
  - the filename itself includes "codex"
- No email addresses and no "Astra" string appear outside the PDFs. The PDFs name the author and ORCID and contain the AI declaration naming Claude Opus 5.5, GPT-6 Astra and GPT-6.1 Sol; those are intended and AC's.
- Why it matters: none of this affects verification, and the inputs cannot be redacted without breaking byte provenance (their hashes are pinned). But the design note's "no internal handoff, audit history" is not literally true for the corner .md, and the username path will be public.
- Fix: AC explicitly acknowledges this or decides on it. Alternatively, add a README sentence saying that retained records keep their original execution paths and provenance text verbatim.

**P7-03 MINOR: the trust anchor is not stated.**
- Where: README "TRUST AND EXPECTED RESULTS" (lines 80-89) and line 54.
- Evidence: SHA256SUMS, MANIFEST and the expected results all live inside the package. N04 shows that refreshing SHA256SUMS makes extra content pass. N11a and N22a-N24a show that consistently refreshed tampered inputs or expected rows pass the integrity command. Only numerical replay of the affected degree catches arithmetic-relevant tampering, and a forger can of course also edit verify.py.
- The README says integrity "does not rerun interval arithmetic", which is honest. It never says that PASS integrity proves only internal consistency, and that authenticity rests on the archive checksum published by the deposit record or the repository (ZIP sha256 15885d34…).
- Fix: one or two sentences saying that, plus that unreplayed degrees are trusted only through checksums.

**P7-04 MINOR: expected-results.jsonl is not parsed strictly.**
- Where: `verify.py` line 64, `json.loads(s)` rather than `load()`.
- Evidence: N12 (a duplicate key in every row, refreshed) was accepted. The review document's "strict-JSON" claim covers inputs and MANIFEST only.
- Fix: parse each line with the same `pairs`/`parse_constant` hooks, for example by factoring out a `loads(bytes)` helper.

**P7-05 MINOR: polynomial replay checks only three booleans.**
- Where: `verify.py` lines 124-125.
- Evidence: the fresh receipt is not compared with the stored accepted records (`polynomial/receipts/*`: certificate_sha256, bound/corner/split counts). The phase replay, by contrast, compares the whole scientific dict.
- My direct runs (commands 12-13) show the counts do agree for n9 and n16.
- Fix: compare `certificate_sha256` with MANIFEST and the counts with the stored rows. Or state in the README that polynomial replay checks acceptance only.

**P7-06 MINOR: the README omits the memory requirement for polynomial replay.**
- Evidence: `--polynomial-degrees 33` reached 1,717,840 KiB max RSS. Historical times rise through n40 (1,367 s), so memory for higher degrees is likely larger. That is my inference; I did not run them.
- The developer smoke used a 2 GiB cap, which only covered n2/n17.
- Fix: state "about 2 GB or more RAM for the largest polynomial degrees", or give the measured peak.

**P7-07 NOTE: the Python version requirement is ambiguous for 3.13 users.**
- README line 41 says "Python 3.12 and NumPy". verify.py neither refuses nor warns on 3.13.18 / NumPy 2.5.3.
- In this audit 3.13 produced exactly the expected results: all 7 new degrees, 41/511, controls, analytic, and polynomial 2/9/17/33. The g++ 13.3 build also passed.
- Fix: say "Python 3.12 or later (tested with 3.12.14; independently 3.13.18 / NumPy 2.5.3)". The scope of what was tested is the owner's to choose.

**P7-08 NOTE: replay does not determine every input byte.**
- Evidence: N20/N23 (substituted fields changed in both records) and N08 (produce/verify swap) pass a full replay of the affected degree once checksums are refreshed.
- This is by design and stated in the README ("does not establish that every stored native endpoint is valid"). It is recorded so nobody reads the replay as authenticating the input bytes.

**P7-09 NOTE: extra listed files are accepted.**
- The population check compares against SHA256SUMS, not MANIFEST `payload`, so a file added together with its checksum line passes (N04).
- Fix (optional): also require the file set to equal the MANIFEST payload plus {MANIFEST.json, SHA256SUMS}.

**P7-10 NOTE: file permissions in the ZIP.**
- All 1,019 ZIP members carry Unix mode 0600 (`-rw-------`). After extraction by one user, other local users or shared mounts cannot read the files. Harmless for a single user.
- Fix (optional): use 0644 at the next build.

**P7-11 EDITORIAL: README wording and rendering.**
- README.md is plain text, so a Markdown renderer (for example Zenodo or GitHub previews) will reflow the FILES table and the indented commands.
- Line 72 is overlong.
- "The repository supplies no standalone license grant" (line 101) refers to a repository the ZIP user does not have.
- The quick command prints large analytic JSON blocks and has no single "PASS analytic" line, although the README wording is accurate.
- `corner_gap` is serialized as the string `"None"` for n ≥ 256 (512 rows). This is consistent with `check.check`'s `str(gap)` and harmless.

## Item 4: README as a new user
- Both documented commands I ran (integrity, and quick verbatim) produced exactly the documented PASS lines. I did not run the full command.
- Timing claims are consistent with my measurements:
  - My 7-degree replay cost 56.7 CPU s, about 8 s per degree including probes. "About 46 CPU minutes" equals 2770.54 s / 60.
  - The historical polynomial seconds total about 9,260 s, or about 2.6 h (2-16 about 17 s, 17-32 about 1,300 s, 33-40 7,940 s). That supports "a few additional hours".
  - n33 here took 486 CPU s against 806 s historically.
- The README correctly says integrity checks bytes, not arithmetic (subject to P7-03).
- Licence, DOI and authorship: the README invents none and says "implies no upload". MANIFEST `license` says "No standalone license grant ...; owner publication metadata pending".
- Nothing in the README claims an upload or DOI. The PDFs say "The package will be deposited in Zenodo (DOI pending); no permanent deposit has yet been assigned" (see P7-01).

## Item 5: PDFs
**Basic facts**
- paper.pdf: 59 pages, sha256 b0abf068…
- companion.pdf: 152 pages, sha256 3c7a114a…
- Both list Author "Andrey Chesnokov" and CreationDate Sat Nov 7 2026 UTC; the PDFs were regenerated on 14 Nov, so this date comes from a fixed build timestamp.

**Placeholder scan** (pdftotext; grep for TODO, XXX, FIXME, TBD, ??, lorem)
- Found no TODO, XXX, FIXME, TBD, unresolved `??` or lorem.

**Report only (AC's decisions)**
- "Development draft, 8 November 2026." (paper) and "Development draft." (companion)
- AI declaration naming Claude Opus 5.5, GPT-6 Astra and GPT-6.1 Sol
- "Final human review and publication preparation remain to be completed."
- ORCID 0009-0004-4687-1810 and the contributions statement

## Limitations
- I did not run the full `--degrees all` or `--polynomial-degrees all`.
- Of the polynomial degrees, only 2, 9, 16 (direct), 17 and 33 were run.
- I did not inspect the regeneration code under item 1 of handoff 37; that is outside this P7 scope.
- I could not verify the original sources of the 382 regenerated inputs or the observations.jsonl: `local-output` is absent here. I confirmed only internal consistency and agreement with the Git-tracked RESULTS.json.
- CPU for the negatives harness was not separately accounted.
