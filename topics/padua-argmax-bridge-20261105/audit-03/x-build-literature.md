# Audit X: fresh builds, correspondence, literature, novelty (handoff 28, section 4)

Auditor: Claude Opus 5.5 (claude-opus-5-5), effort xhigh, as an independent auditor subagent of
the Claude audit orchestrator. This agent changed no Git state and wrote no files inside the
repository. Repository: `aacchhee/padua_research`, branch `codex/padua-argmax-bridge-20261105`,
head `f366535e1fa4ede566cb83bdc554220c12b307cf`. I read the rules (AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md) at that head, and the brief `claude-audit-brief-20261108.md` in full.
Date: 2026-11-08.

Labels:
- **[D]**: executed or observed directly in this audit.
- **[E]**: external source checked by me through WebSearch, at metadata, abstract or snippet level
  only. The full text was not opened.
- **[I]**: inherited from repository literature records or other agents. I did not re-verify it.

Network limit [D]: curl through the sandbox proxy returned `CONNECT 403` for every host except
raw.githubusercontent.com (the template fetch worked). WebFetch could not resolve `arxiv.org` or
`www.math.unipd.it`, so I stopped fetching sites as the tool instructs. WebSearch worked. As a
result, **no primary full text was reopened in this audit.** Every source-content judgment below is
[I] or [E].

## Verdicts

- **Builds: PASS.** [D] Both manuscripts build cleanly from the repository sources. The paper has
  48 pages and the companion 162, with 0 undefined references or citations, 0 overfull boxes, all
  fonts embedded Type 1, and no Type 3 fonts. The bytes differ slightly from the recorded PDFs, as
  the brief expected.
- **Correspondence: PASS.** [D] The two manuscripts have the same 5 sections and 12 subsections, the
  same 13 formal statements byte-for-byte, the same 90 numbered display environments (92 equation
  numbers), all 211 paper display blocks present in order in the companion, and 113 labels whose
  compiled numbers agree in the fresh .aux files. The companion's 420 additional displays are all
  unnumbered. The bibliographies (.bib and generated .bbl) are byte-identical, with 13 entries in
  correct alphabetical numerical order. The statements, hypotheses, constants, conventions,
  equality sets and evidence counts agree.
- **Evidence index: PASS.** [D] 396 entries, 32414 bytes, schema v4, run on a `git archive` copy.
- **Constants sanity: consistent, MEASURED only.** [D] A float64 evaluation of the printed
  cardinal formula agrees with the printed expansion (5), including the sign of `-1/N`, for both
  parities and n = 10..401.
- **Literature and attribution: supported with qualifications.** No source found in my searches
  proves the exact all-degree equality set or the fine expansion [E]. The paper's novelty wording is
  modest and supported. Two attribution gaps should be fixed before submission: Kuznetsova/Pimenova
  (X-05) and the earlier numerical lower-order fits (X-06). There are also bibliography rendering
  defects (X-01 to X-03).
- Findings: **0 BLOCKING, 1 MAJOR** (attribution only; no mathematical effect), **7 MINOR**,
  **8 NOTE, 3 EDITORIAL**.

## Task A — fresh builds

### Commands, exit codes and environment [D]

```
cd /home/user/padua_research
export PADUA_PAPER_OUTPUT_DIR=$A/build/paper PADUA_COMPANION_OUTPUT_DIR=$A/build/companion
bash topics/padua-argmax-bridge-20261105/paper/build.sh            # exit 0, user 2.52 s, sys 0.15 s, wall 3 s
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh  # exit 0, user 3.60 s, sys 0.17 s, wall 4 s
```

- A first attempt wrapped the builds in `/usr/bin/time`, which is not installed. That attempt exited
  with 127 without running anything.
- Environment: pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), kpathsea 6.3.5,
  Latexmk 4.83 (31 Jan 2024), pdftotext/pdffonts 24.02.0, Python 3.13, numpy 2.5.3, scipy 1.18.1.
- The recorded builds used TeX Live 2025/dev, pdfTeX 1.40.26 and latexmk 4.86.
- Template: `sn-jnl.cls` (sha256 `36d0c327…`) and `sn-mathphys-num.bst` (`b3a7c7fb…`) were fetched
  from the pinned raw.githubusercontent.com URLs and matched their hashes.
- Writes: `latexmk -outdir` wrote nothing next to the sources. I compared `git status --short
  --ignored` before and after, and ran `find -newer marker` over the whole repository; both show no
  change. The sections are `\input`, not `\include`, so no per-section .aux files are created. A
  copy tree was not needed for the builds. All outputs are under `$A/build/{paper,companion}`.

### Identities and log summary [D]

| Item | Paper (fresh) | Paper (recorded) | Companion (fresh) | Companion (recorded) |
|---|---|---|---|---|
| Pages | 48 | 48 | 162 | 162 |
| Bytes | 640141 (+25) | 640116 | 1153282 (+55) | 1153227 |
| SHA-256 | `08197e7d781fb809fde854c6b520e3fe20ae6dd4b3ee13e19ea8e3bfa1520ce0` | `07db8635…` | `dec7c44c93abfe8fcbd975ef9a0475a967dda2d25c87f64d628675b28769aed3` | `2ec6b072…` |
| main.log bytes | 40296 | n/a | 49851 | 50013 |

- Shared PDF metadata: CreationDate 2026-11-07 00:00 UTC (from `SOURCE_DATE_EPOCH`), PDF 1.5.
- Both logs: 0 LaTeX warnings, 0 undefined references or citations, 0 multiply-defined labels,
  0 overfull boxes, 0 font warnings or substitutions; BibTeX `warning$ -- 0`; xcolor
  "substituted" messages are Info only.
- Underfull: 7 hboxes in the paper (badness 1210–7415) and 8 in the companion (1210–4569).
  Underfull vboxes equal the page count (one per page, a harmless `\raggedbottom`/sn-jnl artifact).
- Fonts: 32 (paper) and 35 (companion), all embedded subset Type 1; no Type 3.
- Byte differences come from TeX engine/package versions. Exact comparison with the recorded PDFs
  is impossible because they are absent from this checkout.

### Page index (printed pages, fresh builds) [D]

The full table of all 113 labels, with number and page in both PDFs, is in
`$A/build/page-index.md`.

| Item | Paper p. | Companion p. |
|---|---|---|
| Title / abstract / "Development draft" | 1 | 1 (draft note p. 2) |
| §1 Introduction | 1 | 2 |
| Fig. 1 (Padua points n=6,7) | 2 | 4 |
| Thm 1.1 Location of the maximum; Thm 1.2 Sharp corner expansion | 3; 3 | 5; 7 |
| §2 Interpolation operator; Lemma 2.1 Cardinal kernel; Remark 2.2 | 4; 5*; 5 | 9; 12; 19 |
| §3 Corner value; §3.1 Exact row formula | 6; 6 | 19; 20 |
| §3.2 Square reference; §3.3 Uniform summation | 8; 9 | 26; 33 |
| Lemma 3.1 Quadrature; Prop 3.2 | 9; 10 | 34; 37 |
| §4 Reflection cancellation; §4.1 Completed model | 13; 14 | 46; 50 |
| Lemma 4.1; 4.2; 4.3; 4.4 | 14; 15; 18; 20 | 52; 55; 63; 69 |
| §4.2 Finite-row telescope; Prop 4.5 | 21; 22 | 70; 72 |
| §4.3 Selected-pair argument; Lemma 4.6 | 34; 34 | 111; 111 |
| §4.4 Odd vertex; §4.5 Outer diamond; §4.6 Actual corners | 36; 38; 40 | 119; 124; 128 |
| §5 Finite completion; Lemma 5.1; §5.1 Small degrees | 42; 42; 42 | 133; 135; 137 |
| §5.2 Phase certificate; unnumbered phase diagram | 43; n/a | 144; 145 |
| §5.3 Evidence and arithmetic | 46 | 158 |
| Declarations; References | 46; 47–48 | 160; 161–162 |

\*Lemma 2.1's `.aux` page is 4, because the label is written before the page break. The statement
prints at the top of p. 5. No `\pageref` is used, so this has no effect.

Layout-preserving text copies for the other auditors (48 and 162 form-feed pages):
`$A/build/text/paper.txt` and `$A/build/text/companion.txt`.

### Correspondence [D]

- `python3 $T/companion-paper/check_correspondence.py`: exit 0, "PASS: original 20 files intact;
  same headings, 13 statements, 90 numbered display environments, 113 labels and bibliography."
  - I read the script first. It runs only `git show` and `git ls-tree`, plus file reads.
  - `git status --ignored` was the same before and after, and `find -newer` showed no new files.
- `--artifacts`: exit 1, `FileNotFoundError` at `local-output/.../paper/main.pdf`. This checkout
  has no `local-output/`, so the preservation check of the recorded PDFs **could not run** (X-16).
  The fresh-build comparison below replaces its label part.
- The repository's `aux_numbers` helper, loaded with `runpy` and `-B`, on the fresh .aux files:
  - 113 source labels, 113 in each .aux, 0 mismatches, 0 extra keys.
  - My own parser (`x-code/page_index.py`) agrees. It finds 5 sections, 3 subsection labels,
    1 figure, 92 equations and 12 theorem-class labels. Remark 2.2 is the unlabeled 13th statement.
- Independent diff (`x-code/block_diff.py`): normalizes only comments and whitespace and compares
  each section file in order.
  - Headings: 17 = 5 sections + 12 subsections, equal.
  - Statements: 13 equal (8 lemma, 2 theorem, 2 proposition, 1 remark).
  - Numbered environments: 90 equal (78 equation, 12 align), giving 92 numbered rows.
  - Display blocks: 211 = 78 + 12 + 7 align* + 3 gather* + 111 `\[`. All are found in order in the
    companion, which has 631 blocks.
  - `\tag` lists are equal and labels are equal. The companion's second tikzpicture (the phase
    diagram) is in `center`, not `figure`, so it is unnumbered.
  - Result: NO PROBLEMS.
- Source freezes: the paper tree has no diff from `c6e195f` to HEAD, and the paper sources have no
  diff from `177be83`. The companion TeX and .bib have no diff from `ac94504`; only
  BUILD/README/review.md were added later. `references.bib` is identical in both trees, and so are
  the generated .bbl files.
- Direct comparison of content (formal statements are identical, so I compared the added companion
  prose):
  - Node convention (2), the coefficient-one kernel, constants (3)–(4), `N=n+1/2`, and the parity
    sets {(-1,-1),(1,-1)} for even n and {(-1,-1),(-1,1)} for odd n.
  - The companion's own parity derivation (intro l.147–150, corner l.123–127) and the n=1 example
    are consistent. I rechecked the n=1 cardinals, Gram matrix and maximum 2 at (-1,±1), and the
    n=2 node list, by hand.
  - Thresholds agree: 2..40 Bernstein, 41..319 phase, analytic n≥320, far 192, corner 256,
    comparison n≥32/160.
  - Evidence counts agree: 280 pairs = 279 consecutive degrees + control 511; 560 = 2 × 280;
    histories for degrees 199 and 238. The companion's breakdown (p.159) is consistent with paper
    p.46.
  - The two abstracts differ only by the companion's two added explanatory sentences.

### Rendered inspection [D] (80–220 dpi PNG, `$A/build/png/`)

- Paper p.1 (title/abstract): clean.
- Paper p.2 (Fig. 1): the crosses sit at the correct nonnode corners for n=6 (even) and n=7 (odd).
- Paper p.22 (Prop 4.5, dense displays): legible. Eq. (54)'s number drops to its own line (X-13).
- Paper p.30 (table (68) and endpoint estimates): legible.
- Paper p.44 ((90)–(92)): clean.
- Companion p.111 (§4.3 / Lemma 4.6): clean.
- Companion pp.144–145 (phase diagram): the labels are clear of the boundary lines, the regions are
  correct (near a+b ≤ 1/(2π), far guard a+b ≥ 1/2), and the closed-region caption text matches.
  The non-floating diagram leaves about 45% of p.144 blank (X-12).

### Evidence index [D]

`git archive HEAD topics/padua-argmax-bridge-20261105 | tar -x -C $A/build/tree`, then
`python3 -B .../code/evidence_index.py --check`. Result:
`{"status":"PASS","schema":"bridge-essential-evidence-index-v4","entries":396,"index_bytes":32414,"total_bytes":1710416}`.
The manifest sha256 is `855d41a1…0c8b`. I did not check the 9774001/10000000-byte generated bound
(outside this scope).

### Printed-constant sanity check [D, MEASURED, float64; not a proof]

`x-code/corner_expansion_check.py` evaluates Λ_c(n) = Σ_B |L_B(-1,-1)| with the printed (6) and
(2), using an O(n³) matrix form, and computes κ from (4) using SciPy `quad` and a digamma closed form
of the odd series, cross-checked against the direct series.

- κ = 0.919710118388, b = 1.225522125742, c = 1.846160310424. These match the repository
  fingerprints 1.2255221257 and 1.8461603104.
- Σ_B L_B = 1.000000000000 for every n tested (partition of unity), which confirms the
  coefficient-one subtraction.
- Remainder R = Λ_c − (5):

| n | R |
|---|---|
| 10 | +3.71e-3 |
| 50 | +5.46e-5 |
| 100 | +1.01e-6 |
| 200 | −3.03e-6 |
| 400 | −1.59e-6 |

- Odd n gives nearly identical values. R·N²/log N stays within [−0.043, +0.174]. R is far smaller
  than 1/N, so the term −1/N and its sign are right.
- R·N² ≈ α log N + β with α ≈ −0.19 on n = 100→200→400. This suggests that the log N/N² order is
  genuinely attained (X-19). Wall time was 2 s.

## Task B — literature, positioning, novelty gate

**Gate scope.** This sub-audit generates no mechanism and assesses only the manuscripts' priority
and attribution claims. I read: all 66 headings of `state/IDEAS.md` (313 KB), its
canonical-disposition and obstruction tables (l.1–122), and the complete Padua argmax sections
(PR17 IDEA-316–335; PR19 IDEA-336–348 with its scoped obstruction table; T2–T4 IDEA-356–358; the
PR25 header); targeted greps of `literature/INDEX.md` (LIT-014, 304, 319, 320, 331, 379, 380, 423,
485, 486, 488, 512 and addenda); the records kolomoitsev-lomako-2021, cdmsv-poster-2008,
kuznetsova-1995, bcdmv-computing-2006, vanbarel-chesnokov-2010, demarchi-2022,
bialas-ciez-demarchi-suder-2026 and the headers of bos-dmv-xu-2007 and caliari-dmv-2008;
`topics/padua-literature-20261103/p1-comparison.md`; and all six topic files named in the task.

**IDEAS limitation:** I did not read the full 313-KB `state/IDEAS.md` body outside these sections.
The registry entries consistently disclaim historical priority ("no new novelty/priority claim").
The manuscript's novelty therefore rests on the literature comparison below, not on IDEAS
dispositions.

### (a) Published leading growth

- O(log² n) for Padua was proved in [4] (BCDVX 2006). A search abstract says "minimal order of
  growth O((log n)²)" [E]. Numerical log² growth was first reported with the discovery in [7] (CDV
  2005) [E].
- The constant: Λ_n = (4/π²) log² n + O(log n) is KL2021, Theorem 2.1 and the Padua sentence on p.4
  of both arXiv v1 and the AMC version [I: LIT-379, record confirmed against AC's journal PDF].
- KL's proof imports the pointwise rhombic asymptotics of Kuznetsova 1995, Theorem 1, with
  Pimenova 1979 as the m=n case [I: LIT-482–484].
- The paper credits KL correctly (intro l.140–142) but omits Kuznetsova and Pimenova (X-05).
- KL's lower construction is at a non-corner point [I], so the paper's corner lower bound is its own.

### (b) Earlier numerical fits and the corner observation

- The 5ECM poster [6] (2008) has a boxed **Conjecture**: the maximum is ≈ (4/π²) log² n and is
  attained at a vertex [I: LIT-485, full one-page read; relation symbol "≲/≈" flagged; not
  reopened].
- De Marchi 2022 [9], §3.3(2), p.23, observes "maxima in the corners where there are no Padua
  points" within an open-problems list [I: LIT-326/377, two independent Codex readings; journal and
  DOI metadata confirmed [E]].
- Empirical squared-log fits:
  - ((2/π) log(n+1) + 1.1)² in De Marchi 2005 (simai2004, §1.1) and as reported for 2022 [I;
    secondary/root-read; not verified by me];
  - Xu points: ((2/π) log(n+1))², BCDMV Computing 2006, Conjecture (17) [I: LIT-486];
  - KL2021 journal numerical section: 4/π²(2 log m log n − log² m) + 1.2 log(m+1) + 1.5 [I:
    publisher-indexed text only; the arXiv v1 lacks it].
- The last fit's 1.2 and 1.5 are close to the proved b ≈ 1.2255 and c ≈ 1.8462. The lower-order
  size was therefore anticipated numerically, though not identified (X-06).

### (c) Generic rigorous Chebyshev-mesh norm bounds

- [3] ETNA 60 (2024): Białas-Cież, Kenne, Sommariva, Vianello [E: authors, venue, DOI, and
  "approximations from above and below with rigorous error bounds" confirmed].
- Proposition 2.2 there gives max_mesh λ ≤ Λ ≤ sec(π/(2m)) max_mesh λ for total-degree projectors on
  the cube, with Padua examples in §3.3 [I: two independent Codex readings].
- The paper's signed-sum identity (§5 opening), global/grid norms (91)–(92) and Lemma 5.1 use the
  same principle. Credit for [3] appears only in the intro (X-08).

### (d) Sharp expansion and exact equality set for every n ≥ 2

- Extended WebSearch ("Padua points Lebesgue function maximum attained corners proof 2025 2026")
  returned only the [9] observation and **this repository's own public PR #17**, with "no published
  all-degree proof" [E].
- The repository's bounded searches report no fine Padua expansion: about 40 root queries plus two
  worker ledgers [I].
- Coverage gaps remain: MathSciNet/zbMATH full text, forward citations of KL2021, and inaccessible
  publisher bodies. I add no exhaustive claim.

### Application citations at actual scope

- [13] Van Barel–Chesnokov 2010 [I: complete Sonnet full-text record, LIT-200/201]: Padua points
  are used as sampling and test sets. Example 1 is an orthogonality test on 5151 points at degree
  100; Example 2 and Table 2 are least-squares problems on 496/861/1326/5151 points. The paper's
  wording "used in computations of discrete bivariate orthogonal polynomials and least-squares
  approximations" is accurate. The interpolation Lebesgue constant does not govern those
  least-squares runs; the paper's "motivate" sentence claims no more than that. It is the author's
  own paper, which is acceptable.
- [11] Laguardia–Russo 2022 [E abstract]: Nyström and collocation methods for 2D Fredholm
  equations based on Padua points, with convergence, stability and conditioning proved. This is
  accurate. The DOI is missing (X-03).
- [12] Landon-Cardinal–Govia–Clerk 2018 [E snippet; I: Eq. (5) record]: Padua Lagrange
  interpolation reconstructs Husimi-Q and Wigner functions, and the Padua Lebesgue constant bounds
  the interpolation error. This is accurate.

### Contribution statement I can support (qualified)

**Known:**
- construction, unisolvence and the kernel formula [4,5,7];
- O(log² n) [4];
- the leading constant 4/π² [10], resting on [Kuz95];
- the corner location conjectured in [6] and observed in [9];
- numerical lower-order fits (KL journal; De Marchi);
- rigorous generic mesh evaluation [3];
- pointwise rhombic asymptotics [Pim79, Kuz95].

**New within the documented bounded search:**
- the exact equality set for every n ≥ 2, which proves [6]'s location conjecture in the sharpened
  two-nonnode-corner form;
- exact identification of b = (8/π²)(γ + log(8/π)), c = c₁² + κ, the half-integer −1/N term, and
  the O(log N/N²) corner remainder, together with its global transfer;
- at method level, cancellation-retaining comparison with strict-exclusion/equality certificates.
  This goes beyond generic enclosure; it is not a claim to have invented mesh certification.

The abstract and introduction already avoid "first" and "to our knowledge". "Our first result
identifies these maximizers exactly" and "The new expansion …" are supported, given X-05 to X-08.

## Findings

**X-01 — MINOR.** *Location:* `references.bib` entry `BialasCiezDeMarchiSuder2026`; ref [2], paper
p.47, companion p.161.
- *Reason:* `eprint`/`archivePrefix` are ignored by `sn-mathphys-num` for `@misc`. Ref [2] therefore
  renders as "Białas-Cież, L., De Marchi, S., Suder, M.: Geometric properties of the Lebesgue
  function (2026)" with no locator [D].
- *Impact:* the reference cannot be located.
- *Fix:* add `note={arXiv:2605.23299 [math.NA]}` (arXiv ID, date and authors confirmed [E]). Rebuild
  and check the .bbl. Both trees share this .bib, so the companion checker's frozen-bib baseline
  must be updated in the same reviewed commit.

**X-02 — MINOR.** *Location:* ref [6] (`CaliariDeMarchiSommarivaVianello2008poster`).
- *Reason:* the `~` in `note` is a TeX tie, so the rendered URL reads "https://www.math.unipd.it/
  marcov/pdf/poster5ecm.pdf" (broken). The text also prints "No DOI." and places the year after
  the URL [D].
- *Fix:* `note={\url{https://www.math.unipd.it/~marcov/pdf/poster5ecm.pdf}}`, dropping "No DOI."
  Coordinate the change as in X-01.

**X-03 — MINOR.** *Location:* ref [11] (`LaguardiaRusso2022`).
- *Reason:* the `url` field is not rendered and the entry has no DOI or issue [D]. The DOI is
  10.14658/PUPJ-DRNA-2022-5-4, issue 5 (Padova University Press page) [E, search-level].
- *Fix:* add `doi`; add `number={5}` after confirming on the journal page.

**X-04 — EDITORIAL.** *Location:* ref [1].
- *Reason:* a stray space appears: "…09710-x . Published online 14 May 2025" [D].
- *Fix:* drop the online-date note; the volume and year suffice for CA.

**X-05 — MAJOR (attribution; mathematics unaffected).** *Location:* paper intro l.140–146 (PDF p.3)
and the identical companion intro l.406–412.
- *Reason:* the paper does not cite Kuznetsova 1995 (Ukr. Math. J. 47, 259–266, DOI
  10.1007/BF01056716) or Pimenova 1979 (Dokl. Akad. Nauk SSSR 249, 52–54).
  - These give pointwise asymptotics of the two-variable discrete rhombic Lebesgue function [I:
    LIT-482–484].
  - KL2021's leading term rests on them.
  - The repository's own P1 comparison (priority wording, items 1–2) recommended citing them for
    the rhombic-kernel mechanism.
  - Their leading factor max(|cos(a−b)|, |cos(a+b)|) reaches 1 on whole lines (P1 comparison).
    That is exactly why the maximizer location is a lower-order question.
- *Impact:* a specialist referee is likely to expect this credit. Including it also gives a
  stronger motivation for Theorem 1.1.
- *Fix:* add one sentence after l.142, for example: "Pointwise asymptotics of the corresponding
  periodic rhombic Lebesgue functions go back to Pimenova [P79] and Kuznetsova [K95]; their leading
  factor is maximal along whole lines through the corners, so the location of the maximum is
  decided by lower-order terms."
  - Add both entries; alphabetical order places Kuznetsova after Kolomoitsev and Pimenova after
    Landon-Cardinal.
  - Make the same change in the companion and update the checker baseline.
  - Before citing, verify the Pimenova transcription on the page image; the repository records
    flag OCR limits.

**X-06 — MINOR (required before submission).** *Location:* intro l.140–146 ("The new expansion
resolves the lower terms…").
- *Reason:* earlier empirical lower-order fits exist and are not mentioned [I]:
  - KL2021 journal numerical section, 1.2 log(m+1) + 1.5;
  - De Marchi's ((2/π) log(n+1) + 1.1)²;
  - the Xu-points Conjecture (17).
- *Impact:* a reader could take the lower-order size as previously unknown. Citing the fits instead
  shows that Theorem 1.2 explains them: b ≈ 1.2255 and c ≈ 1.8462.
- *Fix:*
  1. Verify the KL journal numerical section in AC's local AMC PDF; record kolomoitsev-lomako-2021
     says AC supplied it.
  2. Verify the De Marchi 2005/2022 locators.
  3. Add one sentence with those citations.

**X-07 — MINOR.** *Location:* intro l.83–85 and l.160.
- *Reason:* "observed numerically and posed as a question in earlier work [6,9]" understates [6],
  which states a conjecture of both the location and the size ≈ (4/π²) log² n [I: LIT-485]. Lines
  83–85 and 160 also repeat the same attribution.
- *Fix:*
  - Replace the l.83–85 sentence with "was conjectured in [6] and recorded among open problems in
    [9, §3.3]". Optionally add "the conjectured size (4/π²) log² n was proved in [10]".
  - Delete the duplicate sentence at l.160.
  - Optionally add "confirming a conjecture of [6]" to the abstract.

**X-08 — MINOR.** *Location:* §5 opening (signed-sum identity), (91)–(92) and Lemma 5.1 (paper
pp.42–44); no citation there.
- *Reason:* the global and grid norm bounds are norming-mesh inequalities of the kind in [3],
  Proposition 2.2 [I], and (89) is the standard Bernstein-form range enclosure. The intro credits
  [3] (l.162–164) but the technical section does not.
- *Fix:* add "(cf. [3, Prop. 2.2])" at (92) and a standard Bernstein-enclosure reference at (89).
  Keep the intro's distinction: strict exclusion, equality classification and analytic leaves.

**X-09 — NOTE.** *Location:* intro l.165–166.
- *Reason:* the MP citation ([1], O(n²)) has no stated relevance.
- *Suggestion:* add that [1] also reports numerical corner maxima for MP and leaves their proof
  open (§7.1 [I]). That ties it to Theorem 1.1.

**X-10 — NOTE.** *Location:* intro l.15–21.
- *Suggestion:* credit [4] specifically for the O(log² n) theorem and [7] for the numerical
  discovery [E]. Optionally cite Dencker–Erb–Kolomoitsev–Lomako, J. Complexity 43 (2017) 1–27, for
  two-sided Lissajous–Chebyshev bounds [E metadata].

**X-11 — NOTE.** *Application citations [11–13]* are accurate at their actual scope (see above). No
change is required. Optionally reword [13] as "used Padua points as sampling sets in computations
of …".

**X-12 — EDITORIAL.** *Location:* companion `certification-unified.tex` l.663–692, PDF p.144.
- *Reason:* the non-floating `center` tikzpicture at `x=y=5.5cm` leaves about 45% of p.144 blank
  [D].
- *Fix:* wrap it in `\begin{figure}[htbp]` without `\caption`, which keeps it unnumbered, or reduce
  the scale to about 4.2 cm.

**X-13 — EDITORIAL.** *Location:* paper p.22, eq. (54), and the identical companion block.
- *Reason:* the display is too wide, so the equation number is set on its own line [D].
- *Fix:* break the bracket in G_g.

**X-14 — NOTE.** Lemma 2.1's anchor page is 4 while the statement prints at the top of p.5 [D].
This is cosmetic.

**X-15 — NOTE (reproducibility).** TeX Live 2023 (pdfTeX 1.40.25, latexmk 4.83) reproduces the
page counts and all 113 label numbers, with +25/+55 bytes [D]. Optionally add this to
paper/BUILD.md, which records only TeX Live 2025/dev. The historical counts in paper BUILD/README
("204 displayed math blocks", "Ten numerical bibliography entries") are dated sections; the current
counts are 211 and 13.

**X-16 — NOTE (verification limit).** `check_correspondence.py --artifacts` cannot run in this
checkout because there is no `local-output/`. Byte preservation of the recorded PDFs (640116 and
1153227 B) was **not** re-verified here. The fresh-build label comparison replaces only its
numbering part. To close this, run `--artifacts` on AC's machine or wherever the recorded outputs
live.

**X-17 — MINOR (record hygiene).** *Location:* `paper-positioning.md`, "Recommended combined
narrative", 3rd bullet.
- *Reason:* the bullet says the asymptotic analysis retains "its named computer-assisted constant
  dependency". That contradicts H (analytic, no numerical constant; theory/H l.30–45 and 153) and
  the paper ("proved entirely analytically", intro l.136).
- *Fix:* add a dated addendum noting that H is analytic and that only the global transfer uses
  G01's computer-assisted dependencies.

**X-18 — NOTE.** Novelty wording is identical in both manuscripts and modest; there is no "first"
or "to our knowledge" [D]. Keep the bounded-search qualification for the cover letter and PR. Do
not assert exhaustive priority.

**X-19 — NOTE (MEASURED).** The paper never defines "sharp" (title; Theorem 1.2).
- The float64 evidence suggests the remainder order log N/N² is attained, with α ≈ −0.19. This is
  not proved.
- *Suggestion:* either define "sharp" as "through the O(log N/N²) remainder with explicit
  constants", or keep the title and avoid implying that the remainder order is optimal.

## Commands run (all outside the repository unless they only read it)

```
git rev-parse HEAD; git status --short --ignored (before/after each step); git diff --stat <freeze> HEAD -- <paths>
git log --oneline -1 <sha>; git archive HEAD topics/padua-argmax-bridge-20261105 | tar -x -C $A/build/tree
pdflatex --version; latexmk --version; bash .../paper/build.sh; bash .../companion-paper/build.sh   (env vars above)
pdfinfo; pdffonts; sha256sum; stat; pdftotext -layout (both PDFs); pdftoppm -r 80/200/220 (pages 1,2,22,30,44; 111,144,145)
python3 .../companion-paper/check_correspondence.py            -> PASS (exit 0)
python3 .../companion-paper/check_correspondence.py --artifacts -> FileNotFoundError local-output (exit 1)
python3 -B -I -c "runpy.run_path(check_correspondence.py)['aux_numbers'] on fresh aux"  -> 113/113, 0 mismatches
python3 -I $A/x-code/page_index.py build/paper/main.aux build/companion/main.aux > build/page-index.md
python3 -I $A/x-code/block_diff.py .../paper/sections .../companion-paper/sections -> NO PROBLEMS
python3 -B (copy tree) code/evidence_index.py --check -> PASS 396 / 32414 B
python3 -I $A/x-code/corner_expansion_check.py -> build/corner-expansion-check.txt
curl (8 source PDFs) -> proxy CONNECT 403; WebFetch arxiv.org, www.math.unipd.it -> DNS failure (stopped)
WebSearch x10 (KL2021; CDV2005; MP2026; LR2022 DOI; arXiv 2605.23299; corner-proof 2025/26 extended; DEKL2017; LCGC2018; ETNA2024; BDVX2007; DeMarchi2022)
```

Total CPU was under 1 minute: the builds took about 6.5 s user and the numerics about 2 s.

## Outputs

This report; `$A/x-code/{page_index,block_diff,corner_expansion_check}.py`; under `$A/build/`:
fresh `paper/` and `companion/` outputs, `text/{paper,companion}.txt`, `png/`, `page-index.md`,
`block-diff.txt`, `corner-expansion-check.txt`, build stdout/stderr, git-status snapshots, and
`tree/` (the archive copy used for the evidence check).

## Remaining limits

- No primary full text was reopened, because of network restrictions. All source-content claims are
  [I] or [E] as labelled.
- The recorded-PDF byte preservation was not re-verified (X-16).
- I did not read the full `state/IDEAS.md` body beyond the sections listed above.
- I did not audit the mathematics beyond the float64 constants check.
- No exhaustive novelty or priority conclusion follows from this audit.
