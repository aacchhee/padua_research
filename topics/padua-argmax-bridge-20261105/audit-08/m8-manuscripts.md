# M8: focused manuscript diff review (response-07)

- Reviewer: Claude Opus 5.5 (xhigh), independent auditor. Read-only on the repository.
- HEAD: `50070f520b3d5cfe9afbc75f10fdb1bc664b7b71`. Diff base: `9d3f5e0f8b270d039d78d4ebc0df53269a7892ab`.
- Topic directory T = `topics/padua-argmax-bridge-20261105`.
- Work dir: `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit8/m8`. It holds a git archive of HEAD and a `--no-hardlinks` clone checked out at HEAD.
- Public ZIP: the coordinator supplied it extracted read-only at `.../scratchpad/audit8/zip-ro/padua-reproducibility`.

## Verdict

- No BLOCKING or MAJOR findings.
- The audit-07 MAJOR (M7-01/P7-01) is resolved. Both data statements now describe the public kit truthfully and keep it separate from the author-held preservation archive. Neither claims a DOI, a licence or an upload.
- Every TeX hunk is wording or provenance only. No theorem statement, hypothesis, constant, range, threshold, numbered display or proof step changed.
- The rebuilt PDFs match the shipped ZIP PDFs in page count and in extracted text.
- Findings: 3 MINOR, 3 NOTE, 1 EDITORIAL.

## Commit relations

- `5f435be` (parent `9d3f5e0`) is the paired TeX freeze. It touches only the six `.tex` files.
- `daa77de` (parent `5f435be`) is the pointer/tooling commit. It touches only `check_correspondence.py`, where `FINAL_BASELINE` changes from `e861c75` to `5f435be` and `--built-labels` is added, and the two `build.sh` default output dirs.
- `dce3260` and `687e9d4` change no `*.tex`/`*.bib` in the paper or companion trees. `50070f5` changes 2 files outside the manuscripts.
- `git diff 5f435be HEAD -- '*.tex' '*.bib'` is empty. The committed TeX/Bib is byte-identical to the freeze.

## (1) TeX hunk classification (all wording/provenance)

| File:line (HEAD) | Change | Class |
|---|---|---|
| paper/main.tex:81-94 and companion-paper/main.tex:88-101 | New data statement. Companion names the research article, not itself. Paper names the companion. | provenance |
| paper/sections/certification-unified.tex:462-470 | Trust-table footnote replaced by the companion wording (see M8-03) | provenance/trust wording |
| paper cert :521-523 | Adds "freshly compiled and rechecked on degrees 2 and 17 … no new full 39-degree replay is claimed" | provenance |
| paper cert :525-533, companion cert :1634-1642 | Path-convention sentence moved away. "the freeze of the 2026 native campaign for degrees 320,…,510". "The new independent-checker outputs, together with the 942 input records …" | wording |
| companion cert :1840-1842 | 2770.544476 / 768.464785 / 28.165805 s becomes "about 2771 / 768 / 28". I checked the rounding. | wording |
| companion cert :1863-1868 | Public kit contents, 560+382 split, fresh compile, 2/17 | provenance |
| paper comparison :126-127, companion comparison :333-334 | Path convention stated before first path use | wording |
| companion comparison :3045 | Reference to "Section 4" becomes "the earlier measure-inequality paragraph". This is prose only; the display that follows is unchanged. | wording |
| paper comparison :1882-1884, companion :4147-4149 | Names `base_table.py` (the file exists at HEAD and is byte-equal to `analytic/base_table.py` in the ZIP) | provenance |

- The notation scanner with an empty map reports zero renames and equal numbered blocks against both `9d3f5e0` and `e861c75`. This confirms that no numbered block changed.
- Task (5), reconstructing changed mathematics, is not needed because no mathematical or numerical sentence changed. The one numerical edit is the CPU and wall-time rounding, and I checked it.

## (2) Data statements and certification paragraphs, read as a new reader

### (a) Public kit

The statement lists:
- 942 phase inputs (560 retained, 382 new);
- 39 retained polynomial certificates;
- minimal unchanged checker sources;
- expected results;
- exact analytic checkers;
- verification commands;
- both PDFs.

This matches the ZIP README (byte-identical to `T/code/zenodo_public_20261114/README.txt` at HEAD) and its file list.

- Companion cert :1866 says the kit compiles the polynomial checker afresh. That is true per the README ("metadata kernel is freshly compiled").
- Neither text claims that native histories, runtime bytes or a snapshot are in the kit. The paper data statement implies their absence by assigning them to the preservation archive.

### (b) Preservation archive

- It is described as separate and author-held in cold storage, holding native histories, runtime payloads and a source snapshot. No DOI and no upload are claimed.
- Its size and hash (296,189,961 B, `d3452a17…354c`) are not given in either manuscript or in the public README (M8-04). They are consistent across `regeneration-delivery.json`, `zenodo-public-package-20261114.md:55` and `zenodo-public-response07-delivery.json`.
- The word "full" overreaches (M8-02).

### Specific wording checks

- **DOI/licence/upload:** "intended for deposit in Zenodo; it has not yet been deposited and no DOI has been assigned". There is no licence claim. The README says "no standalone license grant".
- **Origin wording:** both statements say "(560 retained and 382 new)". The certification texts say "560 authenticated … with 382 newly generated" and "The new independent-checker outputs, together with the 942 input records". No surviving sentence reads as "all 942 new". The README says "560 authenticated retained inputs and 382 regenerated inputs are the origins of today's complete dataset".
- **"No stored native numerical endpoint is a premise of this recertification":** retained at paper cert :390, :517 and companion cert :1629.
- **Embedded paths and process text:** disclosed in the public README under "Retained paths and provenance" (`/home/ahomel/...`, `/workspace/...`, `/opt/codex/runtimes/...`, model names and audit/PR prose), per AC's "Retain with explicit disclosure". The manuscripts do not mention this, and nothing requires them to. Not a finding.

### Audit-07 editorial items

| Item | Status |
|---|---|
| M7-02 | Fixed |
| M7-05 | Fixed. The convention now precedes the first path. I checked that intro, preliminaries, corner and localization have no `\path`/`code/` use before the comparison `\input` (paper loc:150, companion loc:353). |
| M7-06 | Fixed. All three sentences changed and the campaign is named. |
| M7-07 | Fixed |
| M7-08 | Fixed. The χ pointer, the rounding, and the optional `base_table.py` were all done. |
| M7-09 | Fixed. The paper footnote now equals the companion's and the 2/17 sentence was added. See M8-03 for a side effect. |

## (3) Builds

- Both `build.sh` runs exited 0. latexmk ran 3 pdflatex passes for each.
- The template was pre-seeded from an earlier audit scratch copy; build.sh verified it against `dependencies.json`, with no network.

| | Paper | Companion |
|---|---|---|
| Pages | 59 | 152 |
| `!` errors | 0 | 0 |
| Overfull | 0 | 0 |
| Undefined / multiply defined / LaTeX warnings | 0 | 0 |
| Underfull hbox | 4 (badness 1097, 1629, 2221, 7415) | 7 (1097–3735) |
| Underfull vbox while `\output` is active | 59 (one per page) | 152 (one per page) |

## (4) Scripts (run in the HEAD clone; outputs to scratch)

- **check_correspondence default:** PASS at baseline `5f435be`, with 19 statements, 86 numbered display environments, 120 labels and the bibliography.
- **check_correspondence `--archival`:** PASS 13/90/113.
- **check_correspondence `--built-labels`** on my outputs: source PASS 19/86/120, then "PASS: all 120 built label numbers match".
- **How `--built-labels` works:**
  - It runs the default source-freeze and pair check first.
  - It requires the two output directories to differ (after `resolve()`, so symlinks are caught).
  - It parses `main.aux` in each directory, rejecting duplicate `\newlabel`s.
  - It requires each of the 120 source labels to be present in both files with an equal printed number.
  - It is mutually exclusive with `--artifacts` and refused with `--archival`.
  - It does **not** check page counts, the 5× ratio, PDF existence, aux freshness, or that the two aux files come from different documents. See M8-01.
- **Negative cases I ran:**

| Case | Result |
|---|---|
| Changed number (`thm:main-location` 1.1 → 1.19) | rc 1 "Built number differs" |
| Deleted `sec:introduction` | rc 1 "Missing built label" |
| Duplicated a `\newlabel` | rc 1 "Duplicate built label" |
| Same directory | rc 1 "must be separate" |
| Symlinked alias of the same directory | rc 1 "must be separate" |
| Relative vs absolute spelling of one directory | rc 1 "must be separate" |
| Missing aux | rc 1 (uncaught FileNotFoundError traceback, not a clean message) |
| `--built-labels` without companion output | rc 2 |
| `--archival --built-labels` | rc 2 |
| `--artifacts --built-labels` | rc 2 |
| `--artifacts` without original PDFs | rc 2 |
| **Companion dir holding a copy of the PAPER aux** | **rc 0 PASS (vacuous)** |

- **check_baseline_controls.py:** rc 0, "PASS: 7 baseline controls".
- **notation_scan.py:** rc 0 for all four runs (empty map and `notation-renames-response06.json`, each against `e861c75` and `9d3f5e0`). All give PASS 19/86 and numbered blocks equal after 0 declared renames. No new rename map was added in this diff.
- **base_table.py --format text** (HEAD copy): paper PASS 60, companion PASS 60, rc 0.

## (6) Rendered pages (pdftoppm -r 80, inspected)

- Paper pp. 55, 56, 57 inspected. Rendered but not opened: p. 20, p. 42.
- Companion pp. 149, 150 inspected. Rendered but not opened: pp. 56, 94, 107, 145, 146. Their changed sentences were checked through pdftotext.
- On the inspected pages, layout is clean with no overflow.
- Companion p. 150: the `\emph{…};` renders correctly. The space pdftotext shows before ";" is an italic-correction artefact and is not visible on the page.

## (7) Shipped-PDF identity

| | Mine | Shipped (ZIP) |
|---|---|---|
| Paper | 59 pp, 812,846 B, sha256 `f103703dfd6eb653ff1e141218f592cbf1713d3f60a1fee98a1ef8823e7dc6b7`, pdfTeX 1.40.25 | 59 pp, 812,804 B, `d51627f5b42a647233ae76f95a25754d6b0dff7fbe2ca156d563473ee20c8d39` (= receipt), pdfTeX 1.40.26 |
| Companion | 152 pp, 1,223,938 B, `16f7a5080bfed93c8b9d546fe78506a7ec430b6fa6b1ec8b39791f06f4358640` | 152 pp, 1,223,870 B, `9de87206d4988dd2997016ba9885f2ec5cd59a110ab36abac5576d50dfa877fc` (= receipt) |

- **Text equality:**
  - `pdftotext -layout` output is byte-identical between my build and the shipped PDF, for both documents.
  - Normalised text (whitespace runs squeezed to one space) sha256: paper `7e19a1b22538ae47e4b7e2579c9cd2a60d3cf0742a926764d85e447d9789f3a0`, companion `d90ad6b1c3b4f12ea0170dbd25fd799e56dc847af293825a0401df97dfe8c2e6`. Each is equal for mine and shipped.
- **Why the bytes differ:** pdfTeX version only. CreationDate is equal (SOURCE_DATE_EPOCH).
- **Data statement in the shipped PDFs:** the rendered text matches the TeX.
- **ZIP tables and analytic files:**
  - `analytic/tables/paper.tex` and `companion.tex` are byte-identical (`cmp` rc 0) to HEAD `paper/sections/comparison-unified.tex` and `companion-paper/sections/comparison-unified.tex`. They are whole section files, so the table sections are trivially identical.
  - `analytic/base_table.py` and `check.py` equal the HEAD `code/onset512_analytic` files.
  - ZIP `README.md` = `README.txt` = HEAD `T/code/zenodo_public_20261114/README.txt`.

## Findings

**M8-01: MINOR. The `--built-labels` mode can pass vacuously and checks less than BUILD.md implies.**
- Location: `T/companion-paper/check_correspondence.py:129-135,183-184`; BUILD.md "Response-07" section in both trees ("Current ratio 152 <= 5 * 59").
- Evidence:
  - The mode passes with rc 0 when the companion output directory contains a copy of the paper's `main.aux`.
  - It never checks that each aux belongs to its own document or is fresh relative to the current source.
  - It does not check page counts or the 152 ≤ 5×59 ratio. That check exists only in the retired `--artifacts` path.
  - A missing aux gives an uncaught traceback (still rc 1).
- Fix:
  - In `--built-labels`, also require a `main.pdf` in each directory and print and check page counts with the ratio.
  - Bind each aux to its document, for example by requiring a companion-only marker label or the sectioning/title in `\@writefile`, or by requiring the two aux files to differ.
  - Optionally require the aux mtime to be newer than the sources.
  - Catch FileNotFoundError.

**M8-02: MINOR. "contains the full native histories" overstates the preservation archive.**
- Location: `T/paper/main.tex:90-91`, `T/companion-paper/main.tex:97-98`.
- Evidence:
  - `regeneration-delivery.json` `native_component` covers 191 degrees and 382 passes, with `all_new_histories_retained: true`. The archive holds full native histories only for the 2026 regeneration (320–510).
  - The historical native histories behind the 560 retained records are retired and not recovered (`regeneration-20261114.md`, LOG "historical-only archives … retired").
  - Read with the preceding "560 retained", "the full native histories" can be taken to mean all certificates' histories.
- Fix: "contains the full native histories of the 2026 regeneration for degrees 320–510, the runtime payloads and a versioned source snapshot".

**M8-03: MINOR. The paper footnote no longer names the full trusted platform.**
- Location: `T/paper/sections/certification-unified.tex:463-470`. The same wording is in `T/companion-paper/sections/certification-unified.tex:1576-1581`.
- Old text: "The recorded interpreter, libraries, operating system and hardware are trusted for each executed program row."
- New text: "The Python/NumPy source and runtime identities of each phase-checker worker are checked against … input-freeze.json … Finite runtime probes supplement the implementation assumptions; they do not prove universal IEEE conformance. The polynomial checker uses its separately recorded C++/GMP environment."
- Evidence: neither text now mentions the operating system or hardware anywhere (grep for "hardware" or "operating system" finds nothing). An identity check is not a correctness guarantee. The table's "Implementation trust" column partly covers this, but the explicit statement of the trusted base was removed. This is not a theorem change.
- Fix: keep the new sentences and append "The recorded interpreter, libraries, compiler, operating system and hardware remain trusted for each executed program row." in both texts.

**M8-04: NOTE (AC choice). The archive identities are not in the manuscripts.**
- Location: `T/paper/main.tex:84-94`, `T/companion-paper/main.tex:91-101`.
- Evidence:
  - The data statements identify neither the public kit (5,149,206 B, `b341e6a1…adbaa`) nor the preservation archive (296,189,961 B, `d3452a17…354c`). The public README does not identify the preservation archive either.
  - "held by the author in cold storage" rests on AC's report (`zenodo-public-package-20261114.md:55`). Custody is not independently verified.
- Suggestion: optionally give the preservation archive's SHA-256 in the statement or README, so a later request can be matched to it.

**M8-05: NOTE. The new adapter is not mentioned separately.**
- Location: both data statements.
- Evidence: "minimal unchanged checker sources … verification commands" is accurate for the checkers, but the kit's `verify.py` is a new adapter (README "Trust" section; `zenodo-public-package-20261114.md`).
- Suggestion: optionally write "… and a new verification adapter with commands".

**M8-06: EDITORIAL. "Repository paths below" comes before the repository is named.**
- Location: `T/paper/sections/comparison-unified.tex:126-127`, `T/companion-paper/sections/comparison-unified.tex:333-334`.
- Evidence: "Repository paths below are relative to topics/…" appears before any mention of which repository. The URL appears only in the data statement at the end.
- Suggestion: "Paths below are relative to topics/padua-argmax-bridge-20261105/ in the source repository named under Data and code availability."

**M8-07: NOTE (outside the manuscripts). The package design record lacks a superseding pointer.**
- Location: `T/zenodo-public-package-20261114.md:51-55`.
- Evidence: under "Concrete artifact" it still records the earlier 5,138,944-byte ZIP `15885d34…` with no superseding pointer. `T/zenodo-deposit/README.md:467-473` does supersede it with `b341e6a1…`.
- Suggestion: add a one-line dated pointer to `zenodo-public-response07-delivery.json`.

Reserved to AC, report only: the draft date markers, AI declaration, ORCID, author contributions and funding text are unchanged and visible on paper p. 57 and companion p. 150. I did not assess them.

## Commands (exit status)

1. `git rev-parse HEAD; git diff --stat 9d3f5e0 HEAD -- paper companion-paper; git log; git merge-base --is-ancestor 5f435be HEAD; git diff --stat 5f435be HEAD -- '*.tex' '*.bib'`: 0, 0 (ancestor), empty diff.
2. `git diff 9d3f5e0 HEAD` over TeX, check_correspondence, build.sh, BUILD.md and README: 0.
3. `git archive HEAD | tar -x` into the work dir: 0. `git clone -q --no-hardlinks` plus `git checkout 50070f5` in scratch: 0.
4. `bash T/paper/build.sh` with `PADUA_PAPER_OUTPUT_DIR`: 0. `bash T/companion-paper/build.sh` with `PADUA_COMPANION_OUTPUT_DIR`: 0.
5. `pdfinfo`, `sha256sum`, log greps, `pdftotext -layout` plus `cmp` on mine vs ZIP: 0. Text identical.
6. `check_correspondence.py` (default): 0. `--archival`: 0. `--built-labels`: 0.
7. Negative cases, as in the table above: 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, and **0** for the vacuous case.
8. `check_baseline_controls.py`: 0.
9. `notation_scan.py`, four runs: 0 each.
10. `base_table.py --format text` (HEAD copy): 0.
11. `cmp` of ZIP `analytic/tables/*.tex`, `base_table.py`, `check.py` and `README` against HEAD: all 0.
12. `pdftoppm -r 80` for paper pp. 20, 42, 55–57 and companion pp. 56, 94, 107, 145, 146, 149, 150: 0. Paper pp. 55–57 and companion pp. 149–150 were viewed.
13. `python3 -I -B analytic/base_table.py --help`, run from inside the read-only ZIP directory: 0. Help text only, nothing written.

## Limits

- No network.
- I did not run the ZIP's `verify.py` (integrity or replay), any numerical recertification, or the 13-scenario mutation harness.
- The mathematics was not reopened.
- My pdfTeX is 1.40.25, while the shipped PDFs were made with 1.40.26, so byte identity was not expected.
- The template files were copied from an earlier audit scratch directory, and build.sh verified their hashes.
- I viewed 5 rendered pages. The other changed pages were checked through text extraction only.
- Custody of the preservation archive and the absence of any upload were not independently verified; I relied on the repository records.
