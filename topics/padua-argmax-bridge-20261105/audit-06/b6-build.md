# B6: builds, paired correspondence, freeze and baseline, mutation controls, rendered layout, bibliography and dispositions

This is the audit-06 subagent report for handoff 34, the focused audit of response-05.
- **Auditor:** Claude Opus 5.5 (`claude-opus-5-5`), effort xhigh. Independent auditor subagent: no Git state changes and no repository writes.
- **Date:** 2026-11-13.
- **Branch and candidate:** `codex/padua-argmax-bridge-20261105` at head `5b1a4942af498e60e9da4c8860c57cb4f67be4ef`.
  The handoff input head is `26ab08d`; `26ab08d..5b1a494` touches only the two handoff files.
- **Final paired TeX/Bib freeze:** `8937d3b723c09c004f49d3e565d0b02976713a37`. The previous freeze was `ad908acb21d3…`. The code checkpoint is `074c7da`.

Rules read at 5b1a494: AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md. They are byte-identical since be9a831.
Other files read: handoff 34 (in full), response-05.md, the last two LOG entries, audit-05.md, audit-05-manuscripts.md, audit-05/b5-build.md, pr-update-20261113.md, both BUILD.md and README additions, the zenodo-deposit README and MANIFEST budget block, the dated correction in supplementary-manuscript-review-20261113.md, and the build and identity sections of supplementary-manuscript-review-response05-20261113.md.

This scope (build, records, presentation) has no novelty content, so the full `state/IDEAS.md` read is omitted.
Labels: [D] direct observation, [E] executed here, [I] inference or record reading.
A=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit6.

## Verdict (this scope)

**ACCEPT** for the following:
- build reproduction;
- paired correspondence;
- freeze and baseline separation;
- adversarial baseline behaviour;
- rename-scan alignment;
- bibliography;
- the B5-01/02/03/04/05/09/10 layout and record repairs.

**No BLOCKING or MAJOR finding.** All twelve B5-02 tags sit beside their multiline formulas in the rendered PDFs, and a geometry scan of all 87 tags in each PDF found no own-line fallback.

Every non-proof disposition I checked in response-05, LOG, BUILD.md, README, results, pr-update and the deposit README is supported by the files or PDFs. That includes the budget figures, which reproduce byte-exactly.

Remaining items:
- one MINOR record-format item (B6-03);
- two EDITORIAL typesetting items (B6-01, B6-02), which are TeX edits and need a new freeze, so they are not for in-place fixing;
- notes.

## 1. Fresh builds and logs [E]

**Environment:** pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), Latexmk 4.83, Python 3.13.18, poppler pdftotext/pdftoppm/pdffonts.

**Commands** (from the repository root), with `A`, `PADUA_PAPER_OUTPUT_DIR=$A/build/paper` and `PADUA_COMPANION_OUTPUT_DIR=$A/build/companion` set:
- `bash topics/padua-argmax-bridge-20261105/paper/build.sh`: exit 0, 5 latexmk runs, about 10 s;
- `bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh`: exit 0, about 6 s.

Both pinned template files were hash-verified by build.sh. `git status --porcelain --ignored=matching` was identical before and after: the same 4 pre-existing ignored paths, all outside the manuscripts.

| Artifact | Pages | Bytes | SHA-256 (fresh, TL2023) | BUILD.md record (TL2025/dev) |
|---|---:|---:|---|---|
| paper main.pdf | **58** | 798537 | `4da3313c…6a22c` | 58 p, 798493 B, `1dc50b84…c657` |
| companion main.pdf | **152** | 1215656 | `7cd964da…0d32` | 152 p, 1215607 B, `9bd922db…a1c` |

Byte identity is not expected across engine versions; the differences are +44 and +49 B.
- Page counts, labels and the .bbl reproduce. CreationDate is 2026-11-07 (SOURCE_DATE_EPOCH). Both are A4, PDF 1.5.
- Fonts: 40 and 41, all embedded and subset, with no Type 3.
- The companion page limit holds: 152 ≤ 5 × 58 = 290.
- The text copies and page index were published early for the other reviewers. They are `$A/build/text/{paper,companion}.txt` and `$A/build/page-index.md`; checksums are in `$A/build/READY.txt`.

| Log check | paper | companion |
|---|---:|---:|
| TeX errors / LaTeX, Package or Class warnings | 0 / 0 | 0 / 0 |
| undefined refs or cites / multiply-defined labels | 0 / 0 | 0 / 0 |
| overfull boxes / font warnings / blg warnings | 0 / 0 / 0 | 0 / 0 / 0 |
| underfull \hbox (badness 10000) | 5 (1) | 8 (1) |
| underfull \vbox (one per page, class artifact) | 58 | 152 |

At audit-05 the counts were 4 and 8, with **none** at badness 10000. The new badness-10000 line in each text is B6-01.

## 2. Helper commands (handoff 34) and own counts

**Scripts read first [D]:**
- `check_correspondence.py` (`a3cff22b…`) only reads files and runs `git ls-tree` and `git show`.
- `check_baseline_controls.py` (`ef474bb5…`, unchanged since 98261ae) mutates in-memory copies only.

Neither writes into the tree, and `-B` suppresses `__pycache__`.

**Run setup [E]:** I ran them from the root of a `git archive 5b1a494` copy (`$A/build/archive-head`) with read-only `GIT_DIR` pointing at the repository. No `__pycache__` appeared, and the repository status was unchanged.

| Command | Exit | Output |
|---|---:|---|
| `python3 -E -B …/companion-paper/check_correspondence.py` | 0 | `PASS: paired TeX/Bib source baseline 8937d3b…; same headings, 19 statements, 86 numbered display environments, 120 labels and bibliography.` |
| `… --archival` | 0 | `PASS … c6e195fa… / ac945041…; 13 statements, 90 numbered display environments, 113 labels` |
| `python3 -E -B …/check_baseline_controls.py` | 0 | `PASS: 7 baseline controls; paired theorem quantifier; paired numbered formula; paired unnumbered formula; paired bibliography; paired extra TeX file; paired main preamble text; companion-only statement mismatch` |
| `… check_correspondence.py --artifacts --paper-output … --companion-output …` | 2 | argparse: `current --artifacts requires --original-paper-pdf and --original-companion-pdf` |

**Artifact mode cannot run:** the original 48/162-page PDFs are absent. Historical PDF preservation was not verified by me, and no record claims it.

**Own parser on the fresh .aux files [E]** (`$A/b6-code/aux_counts6.py`, brace-balanced, independent of the helper; output in `aux_counts6.out`):
- **Labels:** 120 in each aux file, with identical key sets. **All 120 compiled numbers are equal and all anchor kinds are equal.**
  - Anchor kinds: 87 equation, 18 theorem-class, 5 section, 3 subsection, 3 figure, 4 table.
  - Source labels: 120 distinct per text, equal to the aux keys.
  - Against ad908acb, exactly four labels were added (`eq:kernel-evaluation`, `uc:row-poles`, `uc:worked-values`, `uc:base-values`) and none removed.
- **Numbered displays:** 86 unstarred environments (75 equation, 11 align) carry 87 equation numbers. Every number 1–87 has a label and is rendered at the right margin in both PDFs. Starred display counts differ (5 vs 9), as allowed.
- **Statements:** 19 in each text (4 theorems, 9 lemmas, 2 propositions, 3 corollaries, 1 remark). The source-order kind/number/title/label lists are equal.
- **Headings:** 16 numbered toc entries, equal in kind, number and title. Paragraph entries: paper 7, companion 39; subparagraph entries: 5 each.
- **Floats:** Figures 1–3 and Tables 1–4 are in both texts at the same numbers.
  - Fig. 3: paper p.29, companion p.77.
  - Table 1 (worked values): p.30 / p.77.
  - Table 2 (base values): p.43 / p.108.
  - Tables 3 and 4 (trust, coverage): p.55 / pp.145–146.
- The page-index generator (`$A/b6-code/page_index.py`, the audit-05 tool) independently gives 19/19 statements, 16/16 headings, 120/120 labels with no number mismatch, and printed pages equal to physical pages.

## 3. Freeze, baseline, mutation controls and rename scan

**Separation [E, read-only git]:**
- `8937d3b` changes only 11 `.tex` files (paired main.tex and sections) and no `.bib`.
- `26ab08d` is a separate later commit. It sets `FINAL_BASELINE` to `8937d3b…` (a one-line change in check_correspondence.py) and also changes the build.sh default output directories, adds the rename map and updates the records.
- `FINAL_BASELINE` equals the freeze.
- `git diff --name-only 8937d3b HEAD -- '*.tex' '*.bib'` is empty.
- `git log ad908acb..HEAD -- '*.tex' '*.bib'` lists only 8937d3b.
- Old audits, preregistrations, receipts and response-01..04 are unchanged since 520b364. The only exception is the stated 12-line appended correction in the old supplementary review.

**Mutation harness [E]:**
- Script: `$A/b6-code/mutation_harness6.py`, the audit-05 harness with HEAD=5b1a494 and BASELINE=8937d3b. Raw output: `mutation_harness6.out` (8.3 s).
- Copy trees come from `git archive 5b1a494` under `$A/build/mutation/`.
- The committed helper ran from each copy with read-only GIT_DIR. "Pairwise" is the helper's own `compare_pair()`.

| ID | Mutation (identical in both texts unless stated) | Helper vs 8937d3b | Pairwise |
|---|---|---|---|
| S0 | none | PASS 19/86/120 | PASS |
| S1 | constant `j_*=23/250→24/250` in Corollary 4.6 | **FAIL** | PASS |
| S1b | quantifier in Thm 1.1, `n\geq2→n\geq3` | **FAIL** | PASS |
| S2 | inside numbered display ul:log-series | **FAIL** | PASS |
| S3 | unnumbered γ bracket `\log257→\log258` | **FAIL** | PASS |
| S4 | companion-only constant | FAIL | FAIL (statements) |
| S5 | rename `\mathfrak T→\mathfrak S`, no map | **FAIL** | PASS |
| S6 | S1 declared as a "rename" in a map | **FAIL** | PASS |
| S7 | README.md append (outside the freeze by design) | PASS | PASS |
| S8 | extra `sections/extra.tex` | **FAIL** (file set) | PASS |
| S9 | bib year 1954→1955 | **FAIL** | PASS |
| S10 | `\newtheorem{theorem}{Theorem}[section]` loses `[section]` | **FAIL** | PASS |
| S11 | companion-only prose | FAIL | FAIL (headings) |

**Every paired silent mutation fails against the freeze while the pairwise comparison passes.**
- The audit-03 scanner with baseline 8937d3b fails S5 without a map and passes it with the declared map.
- It also passes S6 under the permissive map. This is the known scanner limitation; the byte-strict helper is unaffected.
- Repository status and the SHA-256 of all 40 manuscript-directory files were identical before and after.

**Rename-aware scanner [E].** The scanner is `audit-03/code/n/notation_scan.py` (`cd8b3cb7…`). It ran in the archive copy with `--out` under `$A/build/notation/`.
- Exit codes: every scan against 24a98db or ad908acb exits 1; the scan against 8937d3b without a map exits 0.
- Every run reports `PASS: current paper vs current companion: 19 statements, 86 numbered display blocks`.
- Against 24a98db:
  - The 33-entry `notation-renames-audit05.json` is the 31-entry audit04 map plus `F_0(hk→F_0(h_m k` and `h_m→\vartheta_m`.
  - With it, residuals are 2+1 statements and 21+2+11 displays per text.
  - With the 31-entry map, the label lists are the same. Content alignment shows the difference: under the 33-entry map the `uc:signed-outer` residual is pure line-break formatting.
- Against ad908acb with the **one-entry incremental map** `[h_m→\vartheta_m]` (reconstructed as the last map entry; root's file is not committed, see B6-04): 1 statement plus 4+2+11 displays per text, identically in both texts.

My **content-aligned** comparison (`$A/b6-code/content_align.py`; outputs `align-*.out`) against ad908acb with that map reproduces the handoff's description exactly, identically in paper and companion:
1. **Certificate wording.** `cert:finite-verification` changes "retained" to "recorded" twice.
2. **Seven display-format changes:**
   - cu:D, cu:row-expand, ul:charts, uc:completed-model and uc:scalar-constants are pure layout. Only line breaks, `aligned`/`gathered` and `\qquad` change; ul:charts also changes its final comma to a full stop.
   - uc:signed-outer adds `\bigl`/`\bigr` and a `\notag\\&\qquad` break. The cell-width rename is covered by the map.
   - uc:uniform-allowance changes `\left`/`\right` to `\Bigl`/`\Bigr`, and the single fraction `(63+…+7\log m+16\log(2m)+(3/2)g_n)/\pi` is split into two fractions over π, which is algebraically identical.
3. **New labelled kernel.** `eq:kernel-evaluation` is the former inline `G_n(u,v)=[P_n(\cos u)-P_n(\cos v)]/(\cos u-\cos v)-\cos(nu)` displayed verbatim (localization-unified.tex l.24 / l.69). It is the only insertion and accounts for the +1 equation numbering.
4. **Nine unchanged index shifts:** ul:primitive … ul:squared-peano. Their content is byte-equal and each moves by +1 index.

No statement other than (1) changed. No constant or threshold changed.

**Permissiveness check [E]:**
- In ad908acb every `h_m` in comparison-unified.tex is the cell width (defined there as `h_m=\pi/m`): 16 paper and 47 companion occurrences.
- After the change, 0 `h_m` remain, with 26 and 63 `\vartheta_m`. `h_m` does not occur in any other section file.
- The series family `h_j(t)` is untouched.
- So the map entry is a single-meaning literal rename and hides no material edit. The `F_0(hk` entry is likewise literal.

## 4. Rendered layout [D, PNGs under `$A/build/png/`]

**B5-02 tags.** The equation numbers 11, 20, 26, 40, 51 and 55 are equation numbers, not page numbers. They were cropped at 200 dpi by `eqcrop6.py` and viewed as stitched images (`paper-b502-stitch.png`, `companion-b502-stitch.png`).

| Label | No. | Paper p. | Companion p. | Rendered tag |
|---|---:|---:|---:|---|
| cu:D | (11) | 9 | 24 | beside two-line aligned formula, vertically centred |
| cu:row-expand | (20) | 14 | 39 | beside two-line formula |
| ul:charts | (26) | 16 | 47 | beside two-line formula (centred between lines) |
| uc:completed-model | (40) | 23 | 64 | beside four-line gathered formula |
| uc:scalar-constants | (51) | 26 | 71 | beside two-line formula (centred) |
| uc:uniform-allowance | (55) | 28 | 74 | beside five-line formula |

**All twelve tags are adjacent to their formulas. None is set on its own line.**
- The geometry scan of **all 87 tags in each PDF** (`tag_scan.py`; outputs `tag_scan-*.out`) found every tag. The six tags with no formula text on the tag's own line have symmetric gaps of at most 3.2 pt above and below: (26), (35), (50), (51), (64) and (68) in both texts. That is the centred multi-line pattern, and no fallback candidate was flagged.
- Also viewed: (25) `eq:kernel-evaluation` and (71) `uc:signed-outer`, whose last-line tag is normal align behaviour, in both texts.

Other pages viewed:
- **Paper Fig. 2 (p.18, 400-dpi zoom) and companion Fig. 2 (p.51, 300 dpi):**
  - The figures are identical. The "absolute gate" label sits outside the triangle with an arrow.
  - The white-filled "𝔭_n on ρ≤1" label sits over the hypotenuse, so no line crosses any text (B5-01 resolved).
  - The label box masks a short segment of the hypotenuse x+y=π (B6-05, cosmetic).
- **Roles arrays (paper p.17, companion p.51):** headed columns (phase region / center / comparison / degree) with visible `\quad` separation (B5-05 resolved). The new symbol table on p.17 / p.50 is legible.
- **Paper Fig. 3 (p.29, 300-dpi zoom) and companion Fig. 3 (p.77):**
  - The η₊ arrow runs from −v_r and the η₋ arrow from v_r, each to the next sample on its right. Both arrows are distinct and labelled, and u_rk sits under one dot (B5-09 resolved).
  - Figure and Table 1 sit beside the row decomposition: p.29–30 for decomposition p.29 in the paper; p.77 for decomposition p.76 in the companion. They are cited in the text.
  - The caption says the values are rounded, illustrative and not proof inputs. No audit-internal wording appears anywhere in the sections (grep for audit/Astra/Codex/Claude/reviewer: 0 hits).
- **Table 2 (base values; paper p.43, companion p.108):**
  - It appears after Corollary 4.7 (p.41 / p.106) and its proof, and is cited in that proof ("Intermediate values are recorded in Table 2").
  - It is followed in the paper by the provenance paragraph: "computed with the exact interval routines of check.py; these 60 intermediate values are not part of its executed receipt.json".
  - Legible, with 15 quantities × 4 degrees = 60 entries.
  - In the paper it floats to the top of p.43, after the §4.4 heading on p.42. The companion places it before §4.4 on p.108.
  - `check.py` has `constants(n)` and `assert log(PI).lo > F(11, 10)` (l.146). Its receipt keys contain none of the 60 values [D].
- **Trust and coverage Tables 3–4 (paper p.55; companion pp.145–146):**
  - Legible and ragged.
  - The companion's "Interval endpoints" row says "Error bound derived below (under the assumed IEEE model)" (M5B-03).
  - The custody paragraph is identical in both texts: inventories "do not establish current custody"; the onset-512 archive and the I25 bundle are unavailable; four data-only checks are open; availability of the 632 MiB histories is unverified (M5B-01).
  - "The last two rows of Table 4" (B5-10) is resolved.
- **Text lint of both PDFs:** no `??` and no doubled words. The only hits are math-extraction artifacts.

## 5. Bibliography and data statements [E/D]

- `references.bib` is byte-identical in the two texts and unchanged since ad908acb. It has 26 entries, and the .bbl files are byte-identical.
- Order is alphabetical by author: Beberok (key MorrowPatterson2026), Białas-Cież ×2, Boas, Bos ×2, Caliari ×3, De Marchi ×2, FLINT, Fousse, GMP, Harris (NumPy), Higham, IEEE, Johansson, Katznelson, Kolomoitsev, Kuznetsova, Laguardia, Landon-Cardinal, Lorentz, Pimenova, Van Barel.
- No new web verification was performed; the audit-05 confirmations stand. B5-11 (Katznelson only via `\nocite` in the companion; Pimenova Math-Net ID unconfirmed) is unchanged.
- **Both data statements** (paper main.tex l.81–92, companion l.88–98) no longer cite a433c7d. They read "A permanent post-repair source snapshot for this version is being prepared" and "deposited in Zenodo (**DOI pending**)", plus "Current retrieval limitations are stated there".
  - This is the pending placeholder that handoff 33 allows. No current snapshot is asserted.
  - The repository URL is unpinned. `main` on GitHub does not contain this topic directory [E, `gh api`], and the remote branch head equals 5b1a494 (B6-06).
- The paper's arithmetic pointer now cites "the expanded companion, Section 5, paragraph 'An elementary derivation of the arithmetic bounds'" (M5B-E6).

## 6. Disposition accuracy (non-proof rows) [D/E/I]

| Row / record | Claim | Check | Result |
|---|---|---|---|
| E5-03, LOG, pr-update, deposit README, MANIFEST | audit input: main 9,733,758; share 1,995,804; union 11,729,562; +2,087 gives 11,731,649. Current: share 2,000,636; 11,734,394; 11,736,481; bound 11,756,141 | own recount, same classifier as audit-02/05 (`budget6.py`) | **Exact.** Growth from input to head is +4,832 B (rename map 3,749, MANIFEST +1,083). No generated-class path outside the topic differs from main |
| E5-08 | campaign README names historical 459d0728 and current a198b651, which has run nothing; deposit README distinguishes repaired E5-01 | README l.21–30; deposit README additions | Supported |
| E5-02 / E5-04 (records) | prospective `python3 -E -B`; J03 dated correction withdraws the FTZ\|DAZ claim | analytic README l.6; J03 addendum; `check.py` l.13 refusal | Supported. Execution is the other reviewers' scope |
| Code identities | return_bundle `3f903e62…`, check.py `5ce8cc07…`, runtime_probe `9f1c503e…`, runner `a198b651…` | sha256sum at HEAD | Match |
| B5-01, M5B-06 | paper figure fixed, rendered | §4 | Supported |
| B5-02, B4-04/X-13 correction | all 12 placements inspected; log inference withdrawn | §4, own crops plus 87-tag scan | Supported |
| B5-03 | companion Machin definition and π bracket | companion comparison l.302–308 | Supported |
| B5-04 | a433c7d not cited as current; placeholder | §5 | Supported |
| B5-05/B4-09, B5-09, B5-10 | rendered and checked | §4 | Supported |
| B5-06 | cumulative map for 24a98db; content alignment | §3 | Supported (exact) |
| B5-07 | 7 byte-strict controls; artifacts mode not reported as run | §2; BUILD.md "not claimed" | Supported. The hard-coded PASS string remains (B6-07) |
| B5-08 | report.md dated correction preserved | tail of report.md | Supported |
| B5-12 | AC fields unchanged | §7 | Supported |
| M5A-07 | figure/table beside the decomposition; illustrative; no internal provenance | §4 | Supported |
| M5B-01/03/05/07, M5B-E1/E2/E5/E6 | custody, IEEE assumption, base table, I25 name, tree-norm splice, weights, pointer | sources and renders (no `I25`, `yields The` or `\delta_r` weights remain) | Supported (wording level only; analytic content is the other reviewers' scope) |
| Builds/pairing paragraph | 58/152; 19/86/120; one kernel number and three exposition labels | §1–2 | Supported |
| Old supplementary B5/C1/C10 | dated correction appended | diff 520b364..HEAD: +12 lines only | Supported |
| Supplementary-response05 source table | 17 SHA-256 rows | recomputed against `git show 8937d3b:` and the code file | 17/17 match |
| LOG | evidence index 396 entries / 32,414 bytes | `evidence_index.py --check` in the archive copy | PASS 396/32414 |
| Handoff discipline | 33 `done in 26ab08d`; one open handoff (34) | status scan | Supported |
| pr-update-20261113.md | Draft; no readiness, custody, DOI or publication; focused Claude review required | read | Supported in content. Formatting: B6-03 |
| Unverifiable here | BUILD.md TL2025 hashes and Oslo copies under `/workspace/.../local-output`; "57/150 artifacts preserved" | not reachable from this session | Access limit, not a finding |

No claim checked in this scope is unsupported by the actual files or PDFs.

## 7. Declarations (AC-reserved; report only)

- The Funding … AI-declaration blocks are byte-identical between the two texts and unchanged across 24a98db, ad908acb and 8937d3b.
- **Funding** matches AC's confirmation (response-03 l.108).
- **ORCID** 0009-0004-4687-1810: the ISO 7064 mod 11-2 check digit 0 is valid [E].
- The **AI declaration** names Claude Opus 5.5, GPT-6 Astra and GPT-6.1 Sol. It still omits the Claude Sonnet 5.5 use recorded in the LOG at audit-05.
- **Draft marker:** the paper still reads "Development draft, 8 November 2026" against sources frozen on 13 November. The companion reads "Expanded companion, 13 November 2026 … Development draft".
- The companion abstract now matches the paper ("not used in any proof"; "quantifies the cancellation that a periodic majorant loses").

## Findings

**B6-01: EDITORIAL (new loose line, both texts).**
- *Location:* the provenance paragraph after the proof of Corollary 4.7. Paper `sections/comparison-unified.tex` l.1873–1875 renders on p.42; companion l.4138–4140 renders on p.107.
- *Reason:* "Table 2 was computed with the exact interval routines of `\texttt{code/onset512\_analytic/check.py}`" cannot break inside the `\texttt` path. The log shows Underfull \hbox badness 10000, the only one in each text, and the line renders with visibly stretched word spacing [D]. Audit-05 had no badness-10000 line.
- *Impact:* cosmetic only.
- *Fix:* any one of:
  - reword so the path starts a line;
  - use `\path`/`\url` or `\allowbreak` after the slashes;
  - move the path into the table note.

  Optionally keep Table 2 out of §4.4 in the paper (`[!t]` before the heading, or a float barrier).
- *Process:* this is a TeX edit, so it needs a new paired freeze. Batch it with any later manuscript change; it is not an auditor in-place fix.

**B6-02: EDITORIAL (pre-existing; same class as B5-05).**
- *Location:* the companion-only "Returning to the comparison outputs" array, `companion-paper/sections/localization-unified.tex` l.357–366, p.107. Unchanged since 2026-11-08.
- *Reason:* default `{lll}` spacing makes "radius-one comparison" abut "relative error", and "…at the actual corner" abut "(58)" [D, `comp-p107-outputs.png`]. Audit-05 flagged only the roles array.
- *Fix:* `\begin{array}{l@{\quad}l@{\quad}l}`, in a later batch with a new freeze.

**B6-03: MINOR (record formatting; eligible for an auditor in-place fix).**
- *Location:* the new response-05 record text, which systematically drops the space between words and numbers or SHAs:
  - pr-update-20261113.md, which is the PR body: "Code checkpoint074c7da", "freeze8937d3b…", "Rules read at520b3645…", "mainb5388c25…", "at58/152pages", "with19statements,86numbered environments and120matching", "All12", "and7mutation controls";
  - the same pattern in response-05.md, results/padua-argmax-bridge-20261105.md ("sourcefreeze"), both BUILD.md and README sections, handoff 34, zenodo-deposit/README.md and the LOG entry.
- *Impact:* readability, and copy/search of SHAs in the PR body (a double-click selects "freeze8937d3b…"). Content is correct.
- *Fix:* restore the spaces. This is formatting only, within the third-round in-place rule for records the orchestrator commits. Never apply it to an old audit or handoff body.

**B6-04: NOTE (reproducibility of the scan record).** Root's one-entry incremental cell-width map against ad908acb is described in LOG and handoff 34 but not committed. It is reconstructable as the last entry of `notation-renames-audit05.json`, and with it I reproduce the stated alignment exactly. Optionally state that in BUILD.md.

**B6-05: NOTE / EDITORIAL (figure).** In Fig. 2 (both texts, paper p.18 and companion p.51) the white box of "𝔭_n on ρ≤1" masks part of the hypotenuse x+y=π. No text is crossed, so B5-01 is resolved and the supplementary review's "does not cross either label" is accurate. Moving the label right, outside the triangle, would keep the boundary continuous.

**B6-06: NOTE (data statement).** "Manuscript and checker sources are maintained at https://github.com/aacchhee/padua_research" is unpinned, and the default branch has no topic directory until AC merges. This is already covered by the OPEN snapshot/DOI item. Before submission, cite the post-repair commit or the DOI.

**B6-07: NOTE (B5-07 repeat).** `check_correspondence.py` `artifacts()` still prints "historical 48/162-page PDFs preserved". The mode was not run, and no record claims it.

**B6-08: NOTE (pre-existing wording).** The companion `comparison-unified.tex` l.336–337 says "the reproducibility package retains …receipt.json", and paper l.130 says "…receipt.json in the reproducibility package". The package is not yet deposited, while the receipt is committed in the repository. Consider "the repository contains" when the data statement is finalised. Unchanged since ad908acb.

**B6-09: NOTE (AC-reserved):** see §7.

## Commands run (read-only on the repository; outputs under $A)

1. `git rev-parse`, `branch`, `status --porcelain --ignored=matching` (before, around the mutation harness and at the end: unchanged). Also read-only `git log`, `show --stat`, `diff --name-only|--stat|-U0`, `ls-tree` and `archive`. `gh api` (repo, `contents/topics?ref=main`, branch head).
2. Both `build.sh` runs (§1). Then `pdfinfo`, `pdffonts`, `sha256sum`, `pdftotext -layout|-bbox`, `pdftoppm`, and log/blg scans.
3. In the `git archive` copy: `check_correspondence.py` (default, `--archival`, `--artifacts` without originals giving exit 2), `check_baseline_controls.py`, and `code/evidence_index.py --check`.
4. Own tools in `$A/b6-code/`:
   - `page_index.py`, `aux_counts6.py`, `mutation_harness6.py` and `content_align.py` (×6: 24a98db with the 33 and 31 maps, ad908acb with the one-entry map, both sides);
   - `notation_scan.py` ×6: 24a98db with no map, the 33 map and the 31 map; ad908acb with no map and the one-entry map; 8937d3b with no map;
   - `eqcrop6.py` ×16, `tag_scan.py` ×2 and `budget6.py`.
5. CPU: about 30 s for the builds plus under 1 min for everything else, well within the 30 CPU-minute cap.
6. Not run: the reader, runtime-probe and analytic commands of handoff 34 (other reviewers' scope); the `--artifacts` mode (originals absent); new web verification of the bibliography.

## Outputs

- `$A/b6-build.md` (this report).
- `$A/b6-code/`, holding the scripts above and their `.out` files.
- `$A/build/`:
  - `paper/` and `companion/` (PDF, aux, log, bbl);
  - `text/`, `page-index.md` and `READY.txt`;
  - `png/`;
  - `archive-head/`, `mutation/` and `notation/`;
  - the status and sha256 snapshots.
