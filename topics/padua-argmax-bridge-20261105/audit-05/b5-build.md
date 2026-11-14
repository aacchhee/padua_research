# B5 — builds, paired correspondence, freeze/baseline, adversarial controls, rendering, bibliography, dispositions

Audit-05 (handoff 32) subagent report. Auditor: Claude Opus 5.5 (`claude-opus-5-5`), xhigh,
independent auditor (subagent; no Git state changes, no repository writes). Date 2026-11-13.
I read the rules at head `33b9eca8167980cad0b0a491da7de64280c9a158`: AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md and handoff 32, plus response-04.md, pr-update-20261113.md,
the 2026-11-13 LOG entries (l.2898–3054), audit-04/b4-build.md and audit-04/n4-notation.md.
The rules are byte-identical from 8a94ce6 to HEAD. Branch `codex/padua-argmax-bridge-20261105`.
The final TeX/Bib freeze is `ad908acb21d3589d85635618ff68f63dd01cfbca`.
Labels: [D] direct observation; [E] executed here; [I] inference or record reading.
This scope has no novelty content (build, records and presentation), so the full read of `state/IDEAS.md` was omitted.
Outputs are under `$A`: A=/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit5.

## Verdict (this scope)

**ACCEPT for build reproduction, paired correspondence, freeze/baseline separation, adversarial
baseline behaviour and bibliography. No BLOCKING or MAJOR finding in this scope.**
Five MINOR findings show that several response-04 dispositions are inaccurate or have been overtaken:
- B4-01 / P4-14: the paper figure is not fixed.
- B4-04 / X-13: the equation numbers are still displaced.
- B4-05: the companion π bracket is unchanged.
- B4-06 / P4-15: the cited snapshot is now stale.
- B4-09: the roles-table spacing is unchanged.

One further MINOR is record wording (report.md). The remaining findings are EDITORIAL or NOTE.
Fixes to frozen TeX need a new paired freeze and a helper rebaseline, so they return to development.
The PR update text claims neither readiness nor custody.

## 1. Fresh builds [E]

Environment: pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), Latexmk 4.83, Python 3.13.18,
git 2.43.0, poppler 24.02.0. Commands, run from the repository root:

```sh
export PADUA_PAPER_OUTPUT_DIR=$A/build/paper PADUA_COMPANION_OUTPUT_DIR=$A/build/companion
bash topics/padua-argmax-bridge-20261105/paper/build.sh            # exit 0; pdflatex x3, bibtex x2
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh  # exit 0; pdflatex x3, bibtex x2
```

Both pinned template files were fetched and hash-verified by build.sh. `git status --short --ignored`
on paper/ and companion-paper/ was empty before and after, so latexmk wrote nothing into the tree.

| Artifact | Pages | Bytes | SHA-256 (fresh) | BUILD.md (TeX Live 2025/dev) |
|---|---:|---:|---|---|
| paper main.pdf | **57** | 787050 | `c1547cda…6617f6` | 57 p, 786999 B, 5616921e… |
| companion main.pdf | **150** | 1216569 | `1cd9ac98…a7a678` | 150 p, 1216528 B, b6898b2e… |

Byte identity was not expected (different TeX Live). The page counts, all labels and the .bbl reproduce,
and `main.bbl` is byte-identical between the two texts. CreationDate is 2026-11-07 00:00 UTC
(SOURCE_DATE_EPOCH), A4, PDF 1.5. All fonts are embedded and subset, with no Type 3 fonts (40/42 fonts).
Text copies: `$A/build/text/{paper,companion}.txt`. Page index: `$A/build/page-index.md`
(generator `$A/b5-code/page_index.py`, adapted from audit-04). Printed page numbers equal physical pages.

### Page index summary [E]

| Item | Paper p. | Companion p. |
|---|---:|---:|
| §1 / Thm 1.1 / Thm 1.2 / Fig. 1 | 1 / 3 / 3 / 2 | 2 / 5 / 6 / 4 |
| §2 / Lemma 2.1 / Remark 2.2 (unlabeled, located in text) | 4 / 5 / 6 | 9 / 12 / 19 |
| §3, 3.1, 3.2, 3.3 / Lemma 3.1 / Prop 3.2 | 6, 7, 10, 12 / 12 / 13 | 19, 20, 27, 34 / 34 / 37 |
| §4 / roles array / Fig. 2 / §4.1 | 16 / 17 / 18 / 18 | 45 / 50 / 51 / 50 |
| Lemmas 4.1–4.4 / Thm 4.5 | 18, 21, 24, 26 / 28 | 52, 58, 66, 70 / 74 |
| §4.2–4.5 / Cor 4.6, 4.7 / Lemma 4.8, 4.9 / Thm 4.10 | 27, 39, 42, 44 / 40, 40 / 42, 44 / 46 | 72, 104, 107, 114 / 104, 105 / 107, 114 / 117 |
| Table 1 (60 outward enclosures) | 41 | 106 |
| §5, 5.1–5.3 / Lemma 5.1 / Cor 5.2 / Prop 5.3 | 46, 48, 49, 52 / 47 / 51 / 52 | 117, 122, 129, 141 / 119 / 140 / 141 |
| Fig. 3 (row/pole schematic, companion only, unlabeled) | — | 91 |
| Table 2 (trust) / Table 3 (coverage) | 54 / 54 | 143 / 144 |
| Declarations / References | 55 / 55–57 | 147–148 / 148–150 |

## 2. Logs [E]

| Check | Paper `main.log` | Companion `main.log` |
|---|---|---|
| TeX errors (`^!`, file:line errors) | 0 | 0 |
| LaTeX/Package/Class warnings | 0 | 0 |
| undefined references/citations; multiply-defined labels | 0; 0 | 0; 0 |
| overfull boxes | 0 | 0 |
| font warnings (only xcolor `Info` model substitutions) | 0 | 0 |
| underfull \hbox | 4 (none at badness 10000) | 8 (none at 10000) |
| underfull \vbox (one per page) | 57 | 150 |
| bibtex `main.blg` warnings | 0 | 0 |

Underfull \hbox counts fell from 17/17 at audit-04, because the trust table is now ragged.
Page limit: companion 150 ≤ 5 × 57 = 285 [E].

## 3. Correspondence helper and independent counts

### 3.1 Helper scripts as listed in handoff 32 [E]

I read both scripts before running them; neither writes into the tree.
- `check_correspondence.py` (SHA-256 `bb231904…7edd8`) only reads files and runs read-only
  `git ls-tree`/`git show`.
- `check_baseline_controls.py` (`ef474bb5…e309`) mutates only in-memory copies.

With `-B` no `__pycache__` is written. I ran both from the repository. `git status --porcelain --ignored`
was byte-identical before and after (4 pre-existing ignored paths outside the manuscripts).

| Command (`python3 -B topics/…/companion-paper/…`) | Exit | Output |
|---|---:|---|
| `check_correspondence.py` | 0 | `PASS: paired TeX/Bib source baseline ad908acb…; same headings, 19 statements, 85 numbered display environments, 116 labels and bibliography.` |
| `check_correspondence.py --archival` | 0 | `PASS … c6e195fa… / ac945041…; 13 statements, 90 numbered display environments, 113 labels` |
| `check_baseline_controls.py` | 0 | `PASS: 7 baseline controls; paired theorem quantifier; paired numbered formula; paired unnumbered formula; paired bibliography; paired extra TeX file; paired main preamble text; companion-only statement mismatch` |
| `check_correspondence.py --artifacts --paper-output … --companion-output …` | 2 | argparse: `current --artifacts requires --original-paper-pdf and --original-companion-pdf` |

**The documented artifact mode cannot run**, because the original 48/162-page PDFs are absent.
Historical PDF byte preservation was **not** verified by me.

As a diagnostic, `$A/b5-code/artifact_diag.py` imports the helper from a git-archive copy and stubs
only `preserved_pdf`. On the fresh builds it gives all 116 built numbers matching and 150 ≤ 5×57.
A one-label renumber, a missing label and identical output directories each fail. Note that the
helper's PASS string still says "historical 48/162-page PDFs preserved" under the stub. It is a
hard-coded message, not evidence (see B5-07).

### 3.2 Own parser on the FRESH .aux files [E]

The parser is `$A/b5-code/aux_counts.py` (brace-balanced; it does not import the helper). Output is in `aux_counts.out`.
- **Labels:** 116 in each aux file, with identical key sets. **All 116 compiled numbers and all anchors are equal.**
  The anchors are 86 equation, 18 theorem-class, 5 section, 3 subsection, 2 figure and 2 table.
  The source labels (116 distinct) equal the aux keys in both texts.
- **Numbered displays:** 85 unstarred environments in each text carry 86 equation numbers. All of (1)–(86) are
  rendered at the right margin in both PDFs, and none beyond. The starred display counts differ (5 vs 9),
  as allowed.
- **Statements:** 19 in each text: 4 theorems, 9 lemmas, 2 propositions, 3 corollaries and 1 remark. 18 are labeled.
  The unlabeled Remark 2.2 is at p.6/p.19. The source-order kind/number/title/label lists are equal.
- **Headings:** the 16 numbered toc entries are equal in order and title. The paper has 7 paragraph and 5 subparagraph
  entries; the companion has 40 and 5.
- **Floats:** the companion has an extra **unlabeled Figure 3** (p.91). It is the last figure, so the shared
  figure and table numbers are unaffected. Tables 1–3 have the same numbers in both texts.
- Relative to the audit-04 build (24a98db), 18 equation numbers moved (32–49) and the tables were renumbered
  (trust 1→2, coverage 2→3). The cause is the moved `ul:log-series` toolkit and the new Table 1.
  All internal references use `\ref`. I found no hard-coded number in the sources or the current records.

## 4. Freeze, baseline separation, adversarial controls, rename scanner

**Freeze/baseline [E]:**
- `ad908acb` changes only five .tex files.
- The one-line `FINAL_BASELINE` update (`24a98db…` → `ad908acb…`) is in the **separate** later commit
  `98261ae`. That commit also changes build.sh default output directories and adds `check_baseline_controls.py`.
- `FINAL_BASELINE` equals the freeze.
- `git diff --name-only ad908acb HEAD -- '*.tex' '*.bib'` is empty: no TeX/Bib change after the freeze.
- build.sh/dependencies stay outside the freeze by design (B4-08c).

**Adversarial harness [E]:** `$A/b5-code/mutation_harness.py` is the audit-04 harness with HEAD=33b9eca,
BASELINE=ad908acb and the display target updated to the renamed `w_{\log}`. Copy trees come from
`git archive 33b9eca -- …/paper …/companion-paper` under `$A/build/mutation/`. The committed helper ran from each copy
with read-only `GIT_DIR`. "Pairwise" is the helper's own `compare_pair()`. Raw results are in `mutation_harness.out`.

| ID | Mutation (identical in both texts unless stated) | Helper vs ad908acb | Pairwise |
|---|---|---|---|
| S0 | none | PASS 19/85/116 | PASS |
| S1 | constant `j_*=23/250→24/250` in Corollary 4.6 | **FAIL** (comparison-unified.tex) | PASS |
| S1b | quantifier Thm 1.1 `n\geq2→n\geq3` | **FAIL** (introduction.tex) | PASS |
| S2 | inside numbered display ul:log-series (`w_{\log}^2→^3`) | **FAIL** | PASS |
| S3 | unnumbered γ bracket `\log257→\log258` | **FAIL** | PASS |
| S4 | companion-only constant in Cor 4.6 | FAIL | FAIL (statements) |
| S5 | rename `\mathfrak T→\mathfrak S`, **no map** | **FAIL** | PASS |
| S6 | S1 declared as a "rename" | **FAIL** | PASS |
| S7 | README.md append (outside freeze by design) | PASS | PASS |
| S8 | extra `sections/extra.tex` | **FAIL** (file set) | PASS |
| S9 | bib year 1954→1955 | **FAIL** (references.bib) | PASS |
| S10 | `\newtheorem{theorem}{Theorem}[section]` → no `[section]` | **FAIL** (main.tex) | PASS |
| S11 / S11b | companion-only prose (heading occurrence / before first proof) | FAIL | FAIL (headings) / PASS |

**Every paired identical silent mutation fails against the freeze while pairwise comparison passes.**
The audit-03 scanner, run with baseline ad908acb, fails S5 without a map and passes with the declared one-entry map.
It also passes S6 under a permissive map, a known scanner limitation (B4-08e); the byte-strict helper is unaffected.
The repository status is identical before and after every check, and the manuscript files are unchanged [E].

**Rename-aware scanner against old 24a98db [E]**, run as
`python3 -I -B …/audit-03/code/n/notation_scan.py --repo . --out $A/build/notation/{nomap,map} --baseline-rev 24a98db… [--rename-map …/paper/notation-renames-audit04.json]`.
The map has 31 entries, all literal notation substitutions; none maps a constant.
Both runs exit 1: the pair check PASSes and the baseline check FAILs.
- Without a map: 22 numbered and 6 statement blocks differ per text.
- **With the declared map:** 19 numbered blocks plus 3 statements differ, identically in both texts. This matches the LOG.

My content-aligned comparison (`$A/b5-code/block_align.py`, `residual_diff.py`; outputs `*.out`) shows exactly what remains beyond the literal map:
1. **One moved display:** `ul:log-series` moved from position 21 to position 4 in comparison-unified.tex.
   Its content is byte-equal after the map. The index-aligned scanner therefore reports it plus **17 cascade shifts**
   (uc:scalar-definitions … uc:kappa-series), whose contents are unchanged.
2. **One undeclared literal rename** in `uc:signed-outer`: `F_0(hk` → `F_0(h_m k`. The map only covers `F_0(h(`.
3. **Three statement changes:**
   - **Lemma 5.1 `cert:positive`.** The hypotheses are now explicit: M, ω_a, ω_b ≥ 0, a finite family of C² functions, a
     choice of W_z ≥ F(z) at each vertex, and I_RW defined as their bilinear interpolant. This replaces "the maximum is finite… If W_z≥F(z)… Here I_R
     is bilinear interpolation".
   - **Prop 5.3:** "both retained phase trees" → "both retained certificate records".
   - **Thm 4.5:** the complete signed board sum `(2𝖭)^{-1}Σ_{Γ^-} ε_rs H_rs, ε_rs∈{−1,1}` is inserted into the statement.

None of these changes a constant or threshold. They match the handoff's "moved definitions, explicit assumptions,
witness wording". They are **not rename-only**, and I did not suppress them with a map.

## 5. Rendered pages [E; PNGs under `$A/build/png/`]

Viewed:
- Paper: p1, p17 (roles array crop), p18 (with 220/500-dpi zooms), p27, p35, p41, p54, p55–57, and crops of
  (11), (20), (25), (34), (39), (49), (50), (54), (63), (67), (69).
- Companion: p51 (300 dpi), p63/p73 crops, p91 (300 dpi), p100 and p143, plus text of p1 and p147–150.

The title and abstract pages are legible. The paper defines γ in the abstract, and the companion pdftitle now equals its printed title.
Tables 1–3 are legible, and the trust table is ragged. The dense proof pages (paper p35, p41; companion p91, p100) are legible.
I spot-checked the arithmetic on companion p100: 1/3+13/168+5/96<1/2 and (L+9)/n·n²/(6(n−1)²)<13/168 hold.
The references are well formed. Defects: B5-01, B5-02, B5-05, B5-09, B5-10.

## 6. Bibliography [E, search-level; Crossref not reachable]

- Both references.bib files are byte-identical, with 26 entries. The .bbl files are identical.
- The order is correctly alphabetical: … FLINT, Fousse, GMP, **Harris (NumPy)**, **Higham**, **IEEE**, Johansson,
  **Katznelson**, Kolomoitsev, Kuznetsova, Laguardia, …
- All 27/26 PDF link targets (paper/companion) are exact.

New entries, checked by web search:
- **NumPy:** Harris et al., Nature 585, 357–362 (2020), DOI 10.1038/s41586-020-2649-2 — confirmed.
- **Higham:** 2nd edn, SIAM 2002, DOI 10.1137/1.9780898718027 — confirmed.
- **IEEE Std 754-2019:** DOI 10.1109/IEEESTD.2019.8766229 — confirmed.
- **Katznelson:** 3rd edn, CUP 2004, DOI 10.1017/CBO9781139165372 — confirmed via the chapter DOI.

The new entries are cited in context in the paper: IEEE at certification l.394, Higham "Chapters 3–5" at l.399, NumPy at l.400,
and Katznelson "Chapter I" for Fourier uniqueness at corner l.394. The companion cites IEEE, Higham and NumPy but not
Katznelson (B5-11). No separate Python reference exists; the Python `fractions` documentation URL is cited instead.

Existing entries:
- **Laguardia–Russo** has `number={5}` → renders "15(5), 39–50 (2022)". The journal record confirms vol. 15, issue 5,
  pp. 39–50 and DOI 10.14658/PUPJ-DRNA-2022-5-4. One arXiv citation gives 65–77; I treat the journal as authoritative.
- **Kuznetsova:** UMJ 47(2) 259–266 (1995), DOI 10.1007/BF01056716, confirmed. The Ukrainian original is pp. 220–226; the bib
  correctly cites the English translation.
- **Pimenova:** Dokl. AN SSSR 249(1) 52–54 (1979). Article metadata is confirmed via the Mathdoc record DAN_1979_249_1_a11.
  The Math-Net ID `dan43113` was **not** independently confirmed: mathnet.ru and geodesic.mathdoc.fr do not resolve
  from this session, and Crossref is blocked.

## 7. Disposition accuracy (non-proof rows) [D/E/I]

| Row | Claim | Check | Result |
|---|---|---|---|
| B4-01, P4-14 (figure part) | labels/arrow revised, render inspected | paper p18 zoom | **Not fixed in paper** (B5-01). Companion p51 is fixed. |
| B4-02 | ρ defined before use | paper p16 (25) "Put x=…, ρ=x+y" precedes roles p17 and Fig. 2 p18; companion p50 precedes p51 | Fixed |
| B4-03 | 𝔭_n vs Chebyshev P_n | roles array keeps P_n=T_{n+1}+T_n; figure and gates use 𝔭_n | Fixed |
| B4-04, X-13 | "VERIFIED current layout"; "no overfull boxes" | see B5-02 | **Inaccurate** |
| B4-05 | companion explanations restored | companion l.302–303 unchanged | **Not fixed** (B5-03) |
| B4-06, P4-15 | a433c7d snapshot cited | a433c7d = 24a98db manuscripts + pre-repair reader | **Overtaken** (B5-04) |
| B4-07, B4-10 (AC part) | AI/ORCID/contributions unchanged | byte-equal to 24a98db | Correct (report only, B5-12) |
| B4-08 | scanner a syntactic aid | §4 | Correct |
| B4-09 | ragged columns and column separation | trust table ragged; roles array unchanged | **Partial** (B5-05) |
| B4-10 | γ, metadata, comment | abstract, pdftitle, l.1 comment | Fixed |
| B4-11 | issue 5 mirrored | bib/.bbl | Fixed |
| B4-12 | TeX Live history retained | TL2023 reproduces 57/150, 116 labels, .bbl | Correct |
| N4-11 | four citations, mirrored | 26 identical entries | Fixed; Katznelson is cited in the companion only via `\nocite` |
| N4-12, C4B-10 | 19/85/116, archival, 7 controls | §3–4 rerun | Confirmed |
| N4-02, P4-04 | named tools cited in the forms used | IEEE/Higham/NumPy/Python Fraction in paper certification l.393–402; companion trust table | Present (content is in proof reviewers' scope) |
| J3-01, P4-08 | 471 trees vs 942 records | Prop 5.3, Table 3, §5.3 text in both | Fixed in manuscripts. **report.md l.22 still says "all942 phase trees"** (B5-08) |
| E-05 | campaign-summary attribution withdrawn | preregistration l.39 scopes PA1; response-03 unchanged | Correct |
| E4-01 (record part) | no removable asserts, optimize refusal | 0 `assert` in return_bundle.py, runner.py, verify_compact.py, check_reader_repairs.py; `sys.flags.optimize` refusal in both campaign readers | Consistent. The reader reruns are outside this subagent's scope |
| Superseded response-03 rows | reopened, no inherited FIXED | response-03.md unchanged since a433c7d; response-04 tables list every reopened row | Correct, except the X-13 wording (B5-02) |
| Model/runtime | disclosed | all 8 commits since 941aa33 carry Agent/Model trailers with "serving metadata unexposed" | Consistent |

**pr-update-20261113.md** [D/I] agrees with the records on these points:
- 57/150 pages; 19/85/116; ad908acb; 560/280 (41..319+511).
- 40/31/3/60/7 controls.
- Budget figures: 11,751,309 / 11,729,562 / 1,827,288 (LOG l.2974, l.3028; MANIFEST `final_batch_bound`).
- Ranges PD-T392–431, PD-N146–161, IDEA490–529, LIT598–613 (ALLOCATIONS.md l.9–12).
- Rules unchanged and main merged.

It states "Draft", claims no readiness, custody, DOI or publication, and says the focused Claude audit is required.
Before AC or Codex use it, it needs:
- the audit-05 AUDIT result;
- the B5 MINOR items as open;
- optionally, a note that the 7 committed controls append comments to bib and main.tex
  (stronger paired controls were run in audit-05, §4).

## 8. Declarations (consistency only; AI/ORCID/contributions/draft marker are AC's)

The Funding, Competing interests, Author contributions and AI declaration blocks are byte-equal to 24a98db.
- **Funding** matches AC's recorded confirmation (response-03 l.108).
- **ORCID** 0009-0004-4687-1810: the ISO 7064 mod 11-2 check digit (0) is valid [E].
- **AI declaration:** still omits the Claude Sonnet 5.5 use recorded in the LOG (B4-07, unchanged).
- **Draft marker:** the paper reads "Development draft, **8 November** 2026" although its sources were frozen on 13 November.
  The companion reads "Expanded companion, 13 November 2026 … Development draft."
- **GitHub (`gh api`):** the repository is public; `main` still lacks the topic directory; commit a433c7d resolves.

## Findings

**B5-01 — MINOR (figure legibility; disposition inaccurate).**
- *Location:* paper Figure 2, p.18. Source is `paper/sections/localization-unified.tex` l.134–136:
  `\node at (1.65,1.20) {absolute gate}` and `\node[anchor=west] at (1.45,.68) {$\mathfrak p_n$ on $\rho\leq1$}`.
- *Reason:* the hypotenuse x+y=π still runs through the "g" of "gate" and through "ρ≤" [D, 500-dpi crop
  `png/paper-p18-fig2-zoom500.png`]. The companion (l.336–339) moved both labels outside the triangle with
  `fill=white`, and it renders cleanly (p.51). The two figure sources now differ.
  Response-04 B4-01 / P4-14 and BUILD.md ("root checked rendered paper page 18") imply the fix was verified.
- *Impact:* the journal article's key figure still has collisions; the meaning is recoverable.
- *Fix:* copy the companion's four node/arrow lines into the paper, then make a new paired freeze and rebaseline the helper.
  This returns to development.

**B5-02 — MINOR (record accuracy: B4-04 / X-13).**
- *Location:* response-04 rows B4-04 ("VERIFIED current layout … no overfull boxes") and X-13 ("CORRECTED
  current evidence … no overfull boxes and selected renders were inspected").
- *Reason:* audit-04's finding was that amsmath sets the equation number on its own line, **with no overfull box**.
  That is still true [D, crops `png/paper-eq-stitch.png`, `companion-eq-stitch.png`; E, pdftotext scan] for:
  - (11) cu:D — p.9 / p.24;
  - (20) cu:row-expand — p.14 / p.39;
  - (25) ul:charts — p.16 / p.47;
  - (39) uc:completed-model, formerly (38) — p.23 / p.63;
  - (50) uc:scalar-constants — p.26 / p.70;
  - (54) uc:uniform-allowance, the G_g / C̄_E display — p.27 / p.73.

  The source of (54) is unchanged. The other own-line numbers, (34), (49), (63), (67) and (69), are normal
  vertically centred multi-line numbers.
- *Impact:* the disposition replaces one unsupported FIXED with an irrelevant criterion.
- *Fix:* either split the G_g row (and optionally the others) with a new freeze, or record a **DECISION**
  ("amsmath fallback accepted") listing these six locations. That decision belongs to AC or the developer and is not yet documented,
  so it is not an auditor in-place fix.

**B5-03 — MINOR (B4-05 not implemented).**
- *Location:* `companion-paper/sections/comparison-unified.tex` l.302–303. The text there moved with the toolkit and is byte-unchanged:
  "Consecutive partial sums … through 40 terms … bracket π".
- *Reason:* the companion still omits the bracket `16𝒜_40(5)−4𝒜_39(239)<π<16𝒜_39(5)−4𝒜_40(239)` that the
  paper displays at l.93–101. The companion does state the parity rule in §5 (certification l.536–551) and
  "reversing the bounds in the subtracted term" for its separate 𝒜_80 construction (l.1660). Both passages already
  existed at 24a98db and are not linked from the toolkit.
- *Impact:* response-04's B4-05 row ("Missing companion explanations restored") is inaccurate for this item.
  The mathematics is unaffected.
- *Fix:* copy the paper's unnumbered definition of 𝒜_N, the bracket display and the Machin sentence into the companion.
  No numbered environment changes, but a new freeze is required.

**B5-04 — MINOR (data availability; B4-06 / P4-15 overtaken by response-04's own changes).**
- *Location:* `paper/main.tex` l.82–84 ("the reproducibility snapshot is …/tree/a433c7d") and
  `companion-paper/main.tex` l.88–89 ("Manuscript and checker sources are available in the pinned repository
  snapshot …/a433c7d").
- *Reason:* a433c7d contains the 24a98db manuscripts (51/147 pp.) [E: `git diff --quiet 24a98db a433c7d` on the TeX/Bib files].
  It also contains the pre-repair readers: return_bundle.py, runner.py and verify_compact.py differ from HEAD (+208/−95).
  zenodo-deposit/README.md l.30–33 itself says a433c7d "predates audit-04 repairs and is not a final reviewed source snapshot".
- *Impact:* the companion's sentence is false for the present version. The paper's "the reproducibility snapshot"
  points to superseded sources.
- *Fix:* cite the post-audit reviewed snapshot commit or the DOI at packaging, or describe a433c7d as the historical 8-November
  snapshot. The DOI is AC's action; this must be resolved before readiness or submission.

**B5-05 — MINOR / EDITORIAL (B4-09 partially done).**
- *Location:* roles array, `localization-unified.tex` paper l.108–115 (p.17) and companion l.310–317 (p.50).
- *Reason:* the source is unchanged since 24a98db. The columns still abut: "noncorner λ_n", "π/4 corner", "/30 n≥256"
  [D, `png/paper-p17-roles.png`]. Only the trust table was made ragged.
  Response-04 says "Ragged columns and column separation corrected".
- *Fix:* `\begin{array}{l@{\quad}l@{\quad}l@{\quad}l}` in both texts, then a new freeze.

**B5-06 — NOTE (scanner reporting precision).** The "19 changed numbered blocks" in LOG l.3009–3010 come from
index alignment. In content they are **one moved display, 17 unchanged shifted displays and one undeclared literal rename**
(`F_0(hk→h_m k`), plus three substantive statement edits (§4). The categories reported are accurate and
conservative. Optionally add `F_0(hk` to the map and describe the move as a move.

**B5-07 — NOTE (control scope).** The seven committed controls cover the bibliography and main.tex only by appending
comments, and they include no statement-constant, numbering-setup or rename case. The byte-strict freeze makes this
sufficient, and the stronger audit-04-style set passes (§4). The artifact-mode PASS string hard-codes
"historical 48/162-page PDFs preserved" (B4-08a repeat). Consider a separately named current-artifact mode
that prints that the preservation check was skipped.

**B5-08 — MINOR (record wording; eligible for the auditor's in-place fix).**
- *Location:* `report.md` l.22, under the heading "Current result — local verification complete, 2026-11-08", last changed at a433c7d.
- *Reason:* "recertified all942 phase trees, two per degree41..511" contradicts the J3-01 / P4-08 correction
  (471 distinct trees, 942 records) that response-04 says was applied to "operational notes".
- *Fix:* "all 942 phase witness records (471 distinct trees, two records per degree 41..511)", with a dated addendum.

**B5-09 — EDITORIAL.** Companion Fig. 3 (p.91; comparison-unified.tex near l.2837).
- The η₋ arrow collapses to overlapping arrowheads, and its label sits detached to the right.
- The "u_{rk}" label is placed between two dots.
- *Fix:* place v_r mid-cell or widen the η₋ offset, and anchor the u_{rk} label below one dot.

**B5-10 — EDITORIAL.** Companion certification-unified.tex l.1604, "The last two rows give 471 phase degrees …",
renders on p.143 directly below Table 2 (trust), while Table 3 floats to p.144. The sentence is ambiguous on the page.
*Fix:* "The last two rows of Table~\ref{cert:coverage} …", as the paper does at l.487.

**B5-11 — NOTE.**
- Katznelson2004 enters the companion only through the shared `\nocite`. The companion proves ψ′(1/2)=π²/2
  by the finite sine product and never uses Fourier uniqueness, so audit-04's "all entries cited in both running texts" no
  longer holds for the companion. This is harmless.
- The Pimenova Math-Net ID is unconfirmed here (§6).
- The paper and companion trust tables (Table 2) differ in rows: paper 6 rows; companion 5, with elementary constants merged into
  "Analytic branches". Their wording also differs, but the content is consistent. Floats are not paired by the helper.

**B5-12 — NOTE (AC-reserved; report only).**
- The AI declaration omits the Sonnet 5.5 use recorded in the LOG.
- The paper's draft marker is dated 8 November against the 13 November sources.
- The class artifact "Corresponding author(s). E-mail(s): …;" remains.
- Funding and ORCID are consistent.

## Commands run (read-only on the repository; outputs under $A)

1. `git rev-parse/log/show --stat/diff --name-only|--stat|--quiet/ls-tree/archive/merge-base/grep` (read only);
   `git status --porcelain --ignored` before and after each stage (unchanged); `gh api` (repo, commit a433c7d, main contents).
2. Both `build.sh` runs (§1); `pdfinfo`, `pdffonts`, `sha256sum`, `stat`, `pdftotext -layout|-bbox`, `pdftoppm`; log/blg greps.
3. The three helper commands of handoff 32 (§3.1) plus `--artifacts` without originals (exit 2).
4. `python3 -I $A/b5-code/page_index.py …`, `aux_counts.py`, `mutation_harness.py /home/user/padua_research $A/build/mutation`
   (9.3 s), `artifact_diag.py`, `notation_scan.py` ×2 (with and without map, baseline 24a98db), `residual_diff.py` ×2,
   `block_align.py`, `eqcrop.py`; ad hoc greps of the bib, citation and numeric literals.
5. WebSearch ×7 (DOIs and metadata). Crossref, mathnet.ru and geodesic.mathdoc.fr are unreachable (DNS / not allowed).

Total CPU was well under 2 minutes, within the 30 CPU-minute cap. I did not run the reader, runtime-probe or analytic
commands of handoff 32; they belong to other subagents.

## Outputs

- `$A/b5-build.md` (this report).
- `$A/b5-code/`: page_index.py, aux_counts.py(+.out), mutation_harness.py(+.out), artifact_diag.py(+.out),
  residual_diff.py(+_paper/_companion.out), block_align.py(+.out), eqcrop.py.
- `$A/build/{paper,companion}/` (PDF, aux, log, bbl), `$A/build/text/`, `$A/build/page-index.md`, `$A/build/png/`,
  `$A/build/mutation/`, `$A/build/notation/`.
