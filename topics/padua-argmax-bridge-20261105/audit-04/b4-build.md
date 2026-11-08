# B4 — builds, paired correspondence, adversarial baseline test, rendering, bibliography, declarations

Audit-04 (handoff 30) subagent report. Auditor: Claude Opus 5.5 (`claude-opus-5-5`), xhigh, independent
auditor (subagent; no Git state changes, no repository writes). Date 2026-11-08.
Rules read at head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9` (AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md, handoff 30, claude-audit-brief-onset512-20261108.md).
Branch `codex/padua-argmax-bridge-20261105`; TeX/Bib freeze `24a98db4c3c4c4d0eede2e3929532956df87911b`.
Labels: [D] direct observation of a file/artifact; [E] executed here; [I] inference/record reading.

`git diff --name-only 24a98db..70a50d7 -- '*.tex' '*.bib'` is empty [E]: the audited TeX/Bib bytes
are exactly the freeze. Only README/BUILD/CORRESPONDENCE-REVISION and check_correspondence.py changed.

## Verdict (this scope)

**ACCEPT for build reproduction, paired correspondence, adversarial baseline behaviour, bibliography
and evidence index; no BLOCKING or MAJOR finding in this scope.** Six MINOR findings (B4-01..B4-06)
concern presentation, one companion-explicitness gap, one inaccurate response-03 row and one
data-availability wording. They need a new paired source freeze plus a helper rebaseline if adopted.
Under WORKFLOW the auditor's in-place MINOR fixes are wording only; a fix that cannot be applied within
those limits (here: frozen TeX, a statement symbol in B4-03, the helper baseline) returns to development.
Verification limits: the original 48/162-page PDFs are absent (`local-output/` does not exist), so
their preservation was **not** verified; Crossref is blocked from this session; no proof audit.

## 1. Fresh builds [E]

Environment: `pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian)`, kpathsea 6.3.5,
`Latexmk 4.83 (31 Jan 2024)`. Commands (from the repository root):

```sh
A=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit4
export PADUA_PAPER_OUTPUT_DIR=$A/build/paper PADUA_COMPANION_OUTPUT_DIR=$A/build/companion
bash topics/padua-argmax-bridge-20261105/paper/build.sh            # exit 0, 3 pdflatex + 2 bibtex
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh  # exit 0, 3 pdflatex + 2 bibtex
```

Both pinned template files (sn-jnl.cls 36d0c327…, sn-mathphys-num.bst b3a7c7fb…) were fetched from
the pinned raw.githubusercontent.com URLs and hash-verified by build.sh. `latexmk -outdir` left no file
next to the sources (`git status --short --ignored` on both directories empty before and after), so no
copy-tree build was needed. Wall: paper 8.3 s, companion 5.3 s.

| Artifact | Pages | Bytes | SHA-256 (fresh) | Reference (BUILD.md) |
|---|---:|---:|---|---|
| paper main.pdf | **51** | 733624 | `ad416ae09df923fe3967e95c2c2f591a3248ab99987e79897ce802067cf8e21d` | 51 p, 733598 B, 1346fc28… |
| companion main.pdf | **147** | 1171239 | `febea0067b656d0f0fc34de07098237b87e3cb2bf3d19b5ffe31af6279dcde79` | 147 p, 1171187 B, 83ca42c8… |

Byte identity was not expected (TeX Live 2023 vs recorded 2025/dev); page counts, all labels and the
.bbl reproduce. `main.bbl` is byte-identical between paper and companion [E]. PDF metadata: CreationDate
2026-11-07 00:00 UTC (SOURCE_DATE_EPOCH honoured), Author "Andrey Chesnokov", A4, PDF 1.5.
Text copies: `$A/build/text/paper.txt`, `$A/build/text/companion.txt` (pdftotext -layout).
Page index: `$A/build/page-index.md` (generator `$A/b4-code/page_index.py`).

### Page index summary (printed page = physical page; verified, no mismatch) [E]

| Item | Paper p. | Companion p. |
|---|---:|---:|
| §1 Introduction / Thm 1.1 / Thm 1.2 / Fig. 1 | 1 / 3 / 3 / 2 | 2 / 5 / 7 / 4 |
| §2 / Lemma 2.1 / Remark 2.2 (unlabeled; located in text) | 4 / 5 / 6 | 9 / 12 / 19 |
| §3, 3.1, 3.2, 3.3 / Lemma 3.1 / Prop 3.2 | 6, 7, 9, 11 / 11 / 12 | 19, 20, 27, 34 / 35 / 38 |
| §4, 4.1 / Fig. 2 (phase triangle) | 15, 17 / 16 | 47, 52 / 52 |
| Lemmas 4.1–4.4 / Thm 4.5 | 17, 18, 22, 24 / 26 | 54, 57, 65, 70 / 73 |
| 4.2, 4.3, 4.4, 4.5 / Cor 4.6, 4.7 / Lemma 4.8, 4.9 / Thm 4.10 | 25, 36, 38, 40 / 36, 37 / 38, 40 / 41 | 72, 103, 105, 112 / 103, 104 / 105, 112 / 114 |
| §5, 5.1, 5.2, 5.3 / Lemma 5.1 / Cor 5.2 / Prop 5.3 | 42, 43, 44, 47 / 42 / 46 / 47 | 115, 119, 126, 139 / 117 / 137 / 139 |
| Tables 1 and 2 (trust table, coverage) | 48 | 140 |
| Declarations / References | 49 / 49–51 | 145 / 145–147 |

The companion's toc carries 38 unnumbered `\paragraph` entries (paper: 6) as explanatory headings,
listed in page-index.md; numbered section/subsection sequences are equal (16 = 16).

## 2. Logs [E]

| Check | Paper `main.log` (41734 B) | Companion `main.log` (49413 B) |
|---|---|---|
| TeX errors (`^!`) | 0 | 0 |
| LaTeX/Package/Class warnings | 0 | 0 |
| undefined references/citations | 0 | 0 |
| multiply-defined labels | 0 | 0 |
| overfull boxes | 0 | 0 |
| font warnings (`Font Warning`, substitutions) | 0 | 0 |
| underfull \hbox | 17 (5 at badness 10000) | 17 (5 at badness 10000) |
| underfull \vbox (while \output active) | 51 = one per page | 147 = one per page |
| bibtex warnings (`main.blg`) | 0 | 0 |

13 of the 17 underfull hboxes are in the justified p-columns of Table 1 (`certification-unified.tex`
l.375–391 paper / l.1533–1549 companion); one in the bbl. Page limit: companion 147 ≤ 5 × 51 = 255 [E].

## 3. Correspondence helper and independent reproduction

### 3.1 Helper as documented [E]

`check_correspondence.py` SHA-256 `25f220209f34582025ebc349d86511b278a51f2399199397fc49abdfffd9df10`.

| Command (`python3 -B topics/…/companion-paper/check_correspondence.py …`) | Exit | Output |
|---|---:|---|
| (no args; source-baseline mode, FINAL_BASELINE 24a98db) | 0 | `PASS: paired TeX/Bib source baseline 24a98db…; same headings, 19 statements, 85 numbered display environments, 116 labels and bibliography.` |
| `--archival` | 0 | `PASS … c6e195f… / ac94504…; 13 statements, 90 numbered display environments, 113 labels` |
| `--artifacts --paper-output $A/build/paper --companion-output $A/build/companion` | 2 | argparse: `current --artifacts requires --original-paper-pdf and --original-companion-pdf` |
| same + nonexistent original paths | 1 | uncaught `FileNotFoundError` traceback (fails closed) |

**What 19/85/116 mean** [D, code]: 19 = formal-statement environments
`theorem|lemma|proposition|corollary|definition|remark` (4 theorems, 9 lemmas, 2 propositions,
3 corollaries, 1 remark) over all section files + main.tex; 85 = unstarred
`equation|align|gather|multline|flalign|alignat|eqnarray` environments; 116 = `\label` commands in the
source. Headings are compared but not counted (16 numbered headings). It is **not** "19 headings".

The documented artifact mode could not be run: the preserved originals are absent here.
**The 48/162-page PDF identities (640116 B 07db8635…, 1153227 B 2ec6b072…) were NOT verified by me.**
Their constants in the helper match the historical BUILD records [D].

### 3.2 Independent reproduction from the fresh .aux files [E]

Own parsers (`$A/b4-code/page_index.py`, `block_diff_a3.py` adapted from audit-03):
- **Labels:** source 116 distinct = paper .aux 116 = companion .aux 116, identical key sets; all 116
  compiled numbers equal; anchors: 86 equation, 18 theorem-class, 5 section, 3 subsection, 2 figure,
  2 table (86+18+5+3+2+2 = 116).
- **Numbered displays:** 85 environments carry 86 equation numbers. Exactly one environment has two
  numbered rows (`align` with `cu:H`, `cu:V` in corner-unified.tex); every other has one row and one label.
  Equations are numbered globally 1–86. All of (1)–(86) render in both PDFs and nothing beyond (86)
  (pdftotext scan).
- **Statements:** 19 in source order with identical kind/title/label/number lists. 18 numbers from labels;
  the unlabeled Remark 2.2 was reconstructed from the shared counter and located on paper p.6 and
  companion p.19 with identical text.
- **Headings:** 16 numbered section/subsection entries in the same order with the same titles in both toc's.
- **Main-file numbering setups:** the paper and companion `main.tex` differ only in comments, pdftitle,
  `\title`, the abstract's first sentences ("where γ is Euler's constant") and the companion notice
  [D, diff]. `\documentclass`, all `\newtheorem`/`\theoremstyle` (theorem counter `[section]`,
  shared), packages, `\nocite` order, `\input` list and backmatter are identical. Diagnostic run of the
  helper's artifact stage with only `preserved_pdf` stubbed (`$A/b4-code/artifact_diag.py`): fresh
  builds give all 116 labels matching and 147 ≤ 5×51. A one-label renumber fails ("Built number differs:
  ul:far192"), as do a missing label and identical output directories.
- **Bibliography:** `references.bib` byte-identical (helper) and `.bbl` identical [E]. 22 entries.
  All 22 are also cited in the running text of both texts, so none depends only on `\nocite` [E, aux].
  Alphabetical numerical order is correct: Beberok; Białas-Cież (De Marchi–Suder 2026) before
  Białas-Cież (Kenne… 2024) by second author; Boas; Bos 2006/2007; Caliari (Sommariva) before Caliari
  2005/2008; De Marchi 2005/2022; FLINT; Fousse; GMP; Johansson; Kolomoitsev; Kuznetsova; Laguardia;
  Landon-Cardinal; Lorentz; Pimenova; Van Barel. All 21 hyperlink targets extracted from the PDF
  streams are exact, including `etna_vol60s428`, `padua_research` and `~marcov`. A "space" in the
  pdftotext output is only the underscore glyph.
- **Unnumbered displays (not covered by the helper, by design):** 11 of 232 paper display blocks have no
  verbatim in-order counterpart among the companion's 611 (`$A/b4-code/unnumbered_match.py`, output
  `unnumbered_match.out`). Ten are reformatted, split, expanded or re-derived with the same content. I checked
  the arithmetic of the expanded ones: 31/25+33/20=289/100, 5/2+17/20=67/20, 27/4+17/16+5/12=395/48,
  51/16+5/6=193/48, sum 39073/1200<33, 31π/80<31/25. The tenth is the paired inner-product notation
  ⟨F,G⟩_n vs ⟨f,g⟩_{𝒫_n}, a deliberate choice recorded in front-onset512-response.md l.82. One is a
  content gap: B4-05.

## 4. Adversarial baseline test [E]

Copy trees under `$A/build/mutation/<scenario>/` from `git archive 70a50d7 -- topics/…/paper
topics/…/companion-paper`. The committed helper ran from each copy tree with
`GIT_DIR=/home/user/padua_research/.git` (read-only `ls-tree`/`show` of 24a98db; `GIT_OPTIONAL_LOCKS=0`).
"Pairwise" calls the helper's own `compare_pair()` on the copy's current sources. Harness:
`$A/b4-code/mutation_harness.py`; raw results `mutation_harness.out`, `artifact_diag.out`.

| ID | Mutation (identical in both texts unless stated) | Helper (24a98db) | Pairwise only | notation_scan (audit-03, baseline 24a98db) |
|---|---|---|---|---|
| S0 | none | PASS 19/85/116 | PASS | PASS, 0 renames |
| S1 | `j_*=23/250 → 24/250` inside Corollary 4.6 | **FAIL** `paper: TeX/Bib source changed: sections/comparison-unified.tex` | PASS | — |
| S1b | Theorem 1.1 `n\geq2 → n\geq3` | **FAIL** (introduction.tex) | PASS | — |
| S2 | inside numbered display (ul:log-series) | **FAIL** | PASS | — |
| S3 | inside unnumbered γ-bracket display | **FAIL** | PASS | — |
| S4 | companion-only change in Corollary 4.6 | FAIL (companion) | FAIL (statements) | — |
| S5 | paired rename `\mathfrak T → \mathfrak S` (5+5 occurrences) | **FAIL** | PASS | no map: **FAIL** (uc:absolute-gate, uc:relative-gate); declared map: **PASS** |
| S6 | S1 change declared as a "rename" in the map | **FAIL** | PASS | no map: FAIL; declared map: **PASS** |
| S7 | README.md prose append | PASS (excluded by design) | PASS | — |
| S8 | new unused `sections/extra.tex` | FAIL (file set) | PASS | — |
| S9 | year 1954→1955 in both .bib | FAIL (references.bib) | PASS | — |
| S10 | `\newtheorem{theorem}{Theorem}[section]` → no `[section]`, both main.tex | FAIL (main.tex) | PASS | — |
| S11b | companion-only prose before the first proof | FAIL (companion) | PASS | — |

The brief's requirement holds: **every paired identical silent mutation fails the independent source
baseline while pairwise comparison passes.** This covers statement constants and quantifiers, numbered
and unnumbered displays, bibliography, numbering setup and file-set changes. The final helper is not
rename-aware: any rename, declared or not, fails until a new reviewed baseline. The rename-aware
audit-03 scanner accepts declared renames but also any constant change declared as a rename (S6), and
it checks only numbered blocks (see B4-08).

## 5. Rendered pages [E, viewed PNGs at 80–220 dpi under `$A/build/png/`]

Viewed: paper p1, 16 (with zooms), 26, 35, 46, 48, 49–51, and nine equation crops; companion p1, 52, 100, 129, 140.
Title/abstract pages, dense §4 pages (paper p35, companion p100), §5 pages (paper p46, companion p129;
I also verified the M. Riesz formula derivation there), the trust/coverage tables and references are
legible. No clipped formula; references are well formed. Defects: B4-01 (figure labels), B4-04
(equation numbers pushed to a new line), B4-09 (table spacing).

## 6. Bibliography accuracy (X-01..X-08 follow-up)

Against repository records [I]: Kuznetsova 1995 (UMJ 47(2) 259–266, DOI 10.1007/BF01056716;
records/kuznetsova-1995.md, LIT-482/483); Pimenova 1979 (Dokl. 249(1) 52–54, Math-Net dan43113;
LIT-484); Kolomoitsev–Lomako (AMC 403, 126192); Van Barel–Chesnokov (Numer. Algorithms 55, 383–402);
CDMSV 2008 poster (LIT-485); Białas-Cież–De Marchi–Suder arXiv 2605.23299 (record, v1);
Beberok et al. CA 63 (2026) 31–65 (version of record, read in literature-refresh-20261107.md /
literature-refresh-recent-20261107.md); ETNA 60 428–445 DOI 10.1553/etna_vol60s428; De Marchi 2005
§1.1 pp.3–5 (root read). Bos 2006/2007, CDV 2005/2008, De Marchi 2022, MPFR, Arb, Lorentz and Boas
agree with the LIT index and standard metadata. Web [E, search-level]: Landon-Cardinal–Govia–Clerk PRL
120, 090501 (2018) confirmed; Laguardia–Russo DRNA 15 (2022) 39–50, DOI confirmed, **issue 5** shown
by the journal URL `drna.padovauniversitypress.it/2022/5/4`. Search did not independently confirm
CA vol. 63 for Beberok et al. (repository read of the publisher footer stands). `api.crossref.org`
is outside this session's allowed network (curl 403; WebFetch DNS failure); no DOI was resolved directly.

Audit-03 X dispositions in the current text [D]: X-01 (arXiv id rendered) fixed; X-02 (poster `\url`,
no "No DOI") fixed; X-03 (DOI added, issue omitted) fixed as scoped, and see B4-11; X-04 fixed; X-05:
**Kuznetsova1995 [17] and Pimenova1979 [21] are added** and cited at Theorem 1 scope (intro l.154–158);
X-06 De Marchi fit + locator present; X-07 poster + De Marchi 2022 §3.3 credit present; X-08
`\cite[Proposition~2.2]{Mesh2024}`, Lorentz (Bernstein enclosure, de Casteljau) and Boas (Bernstein
inequality) present. X-13: see B4-04.

## 7. Evidence index [E]

From a `git archive 70a50d7 -- topics/padua-argmax-bridge-20261105` copy (`$A/build/evidence-tree`):
`python3 -I -B topics/…/code/evidence_index.py --check` → exit 0,
`{"status":"PASS","schema":"bridge-essential-evidence-index-v4","entries":396,"index_bytes":32414,"total_bytes":1710416}`.
evidence_index.py SHA-256 d9d4590d…; evidence-manifest.json SHA-256 855d41a1….

## 8. Data/code availability and Declarations (consistency only; AI/ORCID/contributions reserved to AC)

- Funding (no specific grant): matches AC's recorded confirmation [I, response-03 l.105].
- Data availability: the repository is public (`gh api repos/aacchhee/padua_research`: visibility public)
  [E]. But `main` (f70a260) contains **no** `topics/padua-argmax-bridge-20261105` [E] (B4-06). "DOI
  pending" matches the records (AC's action). The listed package components (frozen engine,
  independent checker, runtime/package pins, commands) match zenodo-deposit/README.md l.26–46 [I].
- §5.3 facts match the records [I]: sampled complete histories 199, 238 (compact-return.md l.54) and
  475, 458 (brief); 942 witnesses / 471 degrees; six-tree distinct replay at 41, 458, 511; Table 2 sums
  280+191 = 471 and 560+382 = 942; 39 polynomial degrees 2..40.
- ORCID 0009-0004-4687-1810: ISO 7064 mod 11-2 check digit is valid [E] and matches handoff 21 [I].
- AI declaration: B4-07 (report only).

## Findings

**B4-01 — MINOR (figure legibility).** *Location:* Figure 2, paper p.16 (`localization-unified.tex`
tikz nodes near l.100–110, e.g. `\node[anchor=west] at (1.35,.45) {$P_n$ on $\rho\leq1$}`), companion
p.52 (l.305–315). *Reason:* the hypotenuse x+y=π runs through the letters "te" of "absolute gate" and
through "≤1" of "P_n on ρ≤1" [D, 220-dpi crop `png/paper-p16-fig-16.png`]. The recorded root/Sol max
inspection called the figure readable. *Impact:* the brief's named figure has visible label/line
collisions; the meaning is recoverable. *Fix:* place "absolute gate" fully inside the light region
(e.g. near (0.9,1.4)). Move the P_n label right of the hypotenuse with a longer arrow, or give the
nodes `fill=white,inner sep=1pt`. Apply identically in both texts, then a new freeze and helper baseline.

**B4-02 — MINOR (notation before use).** *Location:* paper §4 opening, roles table and Figure 2
(`localization-unified.tex` l.82–113, p.16); companion l.287–318, p.52. *Reason:* ρ is used there
but defined only at §4.1 (`comparison-unified.tex` l.8, paper p.17; companion l.32). In the companion
the definition sits below the figure on p.52. The charts paragraph names the "phase radius" |α|+|β|
(paper l.34) without attaching ρ. *Impact:* AC's first-use rule. *Fix:* "write ρ=|α|+|β| for this
phase radius" in the charts paragraph of both texts. This is unnumbered prose and changes no statement.

**B4-03 — MINOR (symbol overload; fix touches a statement, so return to development).**
*Location:* both texts, §4. P_n = T_{n+1}+T_n (`localization-unified.tex` l.20–23; used as P_n(cos u)
in the Theorem 4.5 proof, `comparison-unified.tex` l.675–676, paper p.26). P_n(ρ) := C_4+𝔤+… is the
relative polynomial (Corollary 4.7, l.1586–1640; Theorem 4.10 proof l.418; Figure 2 and caption
l.107–112). 𝒫_n is the node set. *Reason:* two meanings in one section. Figure 2 (p.16) says
"P_n on ρ≤1" / "P_n<0" when only the Chebyshev P_n has been defined. *Impact:* reader confusion; no
mathematical error, since the argument types differ. *Fix:* rename one, e.g. the Chebyshev sum to
T_n^+. That avoids editing the Corollary 4.7 statement; otherwise the statement text changes and needs
a rebaseline.

**B4-04 — MINOR (record accuracy) / EDITORIAL (layout).** *Location:* response-03 row X-13; paper
p.26 eq. (54), companion p.73. *Reason:* X-13 (audit-03) identified eq. (54) and said "break the
bracket in G_g". Response-03 marks it FIXED and states "the earlier Abel identification was mistaken".
The current (54) is the same G_g / C̄_E display, and its number is still set on a separate line
[D, p.26 render]. The same amsmath fallback, with no overfull box, also affects (11) p.8, (20) p.13,
(25) p.15, (38) p.21 and (50) p.24 [D, crops `png/eq-stitch.png`]. *Fix:* split the G_g row (e.g.
`\begin{split}` after 111/2), or change the X-13 row to DECISION (fallback accepted) with this location.

**B4-05 — MINOR (companion explicitness vs paper).** *Location:* paper `comparison-unified.tex`
l.500–515 vs companion l.1270–1276. *Reason:* the paper defines A_N(q), states A_40(q)<arctan(1/q)<A_39(q)
and gives the explicit Machin bracket 16A_40(5)−4A_39(239) < π < 16A_39(5)−4A_40(239). The companion
says only that "consecutive partial sums … through 40 terms … bracket π". It omits which partial sum
enters which bound; the subtraction swaps the roles. *Impact:* the companion reader cannot reconstruct
the consumed π bracket (a J02/certificate premise) without the paper; the mathematics is unaffected. *Fix:* copy the paper's
unnumbered display into the companion with one sentence on the alternating-series parity and the role
swap under subtraction.

**B4-06 — MINOR (data-availability precision).** *Location:* Declarations, "Data and code
availability" (paper p.49, companion p.145; `main.tex` l.80–86 / l.87–93). *Reason:* "Manuscript and
checker sources are maintained at https://github.com/aacchhee/padua_research". The repository is public,
but its default branch `main` (f70a260) contains no `topics/padua-argmax-bridge-20261105`. The sources
exist only on the unmerged branch, and the URL is mutable. *Fix (AC/developer):* cite the immutable
snapshot (commit a433c7d / its ZIP) or the Zenodo DOI once created, or name the branch until merge.

**B4-07 — NOTE (reserved to AC; report only).** The AI declaration lists Claude Opus 5.5, GPT-6 Astra
and GPT-6.1 Sol. The LOG records `claude-sonnet-5-5` as session orchestrator (LOG l.1595, l.2693) and
as the model for the local native replay (l.2703). This was previously raised (l.2697) and left to AC
(l.2702), and it is unchanged. The declaration also contains the draft-status sentence "Final human review and
publication preparation remain to be completed", for AC to remove before submission. ORCID and funding
are consistent; author-contribution roles are AC's choice, and I found no record contradiction.

**B4-08 — NOTE (helper scope; no change required for this freeze).**
(a) Current artifact mode cannot run without both original PDFs (exit 2). An auditor without AC's
local-output therefore cannot run the documented compiled-number/page-ratio check (repeat of X-16).
Consider a separately named flag for new-artifact checks that prints that preservation was skipped.
(b) Nonexistent original paths give an uncaught traceback rather than a `ValueError` message (fails closed).
(c) The freeze covers .tex/.bib only; `paper/template/dependencies.json` and `build.sh` (class/BST
pins) are outside it. Artifact mode compares label numbers only.
(d) Unnumbered displays and prose are not paired, by design; my fuzzy comparison found one content gap (B4-05).
(e) The audit-03 rename-aware scanner treats any declared literal substitution as a rename (S6 passes a
constant change) and checks numbered blocks only; it is safe only with a reviewed map. The final
helper is byte-strict, so this does not affect the 24a98db freeze.

**B4-09 — EDITORIAL.** Table 1 (paper p.48 / companion p.140) uses justified narrow p-columns. This
gives wide gaps ("Direct phase sums", "Python integer/Fraction") and 13 of the 17 underfull hboxes; use
`>{\raggedright\arraybackslash}p{…}`. The roles table on p.16/p.52 has abutting columns ("noncorner
λ_n", "…/30 n≥256"); add column separation. Table 2 uses MATLAB-style ranges ("2:40", "41:319") and
"51:101" in the node column with a different meaning (a range of node counts); use en-dashes.

**B4-10 — EDITORIAL.** The paper abstract uses γ without defining it (intro l.117 defines it; the
companion abstract adds "where γ is Euler's constant"). The companion PDF metadata title differs from its
printed title. Companion `main.tex` l.1 comment "frozen 48-page journal manuscript" is stale (comment
only). Both title pages carry the class artifact "Corresponding author(s). E-mail(s): …;".

**B4-11 — NOTE.** X-03's scoped omission of the Laguardia–Russo issue can now be closed after a primary
check: search-level evidence shows DRNA 15, issue 5 (`number={5}`). literature/INDEX.md row LIT-378
(Beberok et al.) is still "UNVERIFIED, secondary" although topic records read the version of record;
reconcile at PR preparation.

**B4-12 — NOTE (reproducibility).** TeX Live 2023 reproduces 51/147 pages, all 116 label numbers, all
86 equation numbers and the identical .bbl, with +26/+52 bytes. BUILD.md records only TeX Live
2025/dev; optionally add this. There is one underfull \vbox per page, which is cosmetic.

## Commands run (all read-only on the repository; outputs under $A)

1. `git rev-parse HEAD`; `git status --short [--ignored]`; `git diff --stat|--name-only 24a98db HEAD`;
   `git log --oneline`; `git ls-tree`/`git archive` (copy trees); `git rev-parse origin/main`.
2. Both build.sh runs (section 1); `pdfinfo`, `sha256sum`, `stat`, `pdftotext -layout|-bbox|-raw`,
   `pdftoppm` (PNG renders), log/blg greps.
3. `python3 -B …/check_correspondence.py` (source, `--archival`, `--artifacts` without/with bogus originals).
4. `python3 -I $A/b4-code/page_index.py …` → `$A/build/page-index.md`; `block_diff_a3.py`;
   `unnumbered_match.py`; `mutation_harness.py /home/user/padua_research $A/build/mutation` (8.9 s);
   `artifact_diag.py` (helper imported from copy tree; only `preserved_pdf` stubbed).
5. `python3 -I -B …/code/evidence_index.py --check` in the git-archive copy.
6. `gh api repos/aacchhee/padua_research` (visibility); WebSearch ×3; Crossref curl/WebFetch blocked.
Total CPU well under 2 min (builds about 8 s user; harness about 9 s); within the 30 CPU-min cap.

## Outputs

`$A/b4-build.md` (this report); `$A/b4-code/` (page_index.py, block_diff_a3.py, unnumbered_match.py
+ .out, mutation_harness.py + .out, artifact_diag.py + .out); `$A/build/{paper,companion}/` (PDF, aux,
log, bbl), `$A/build/text/`, `$A/build/page-index.md`, `$A/build/png/`, `$A/build/mutation/`,
`$A/build/evidence-tree/`.
