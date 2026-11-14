# Split map: single MZ draft → MZ-CC and MZ-SP (gate W0)

AC decision 2026-11-13 ("yes let's split. call the one MZ-CC and another one MZ-SP"); see [LOG](LOG.md).

- **Source:** `tracks/mz-constants/paper/manuscript.tex` at `c0e57a9`, 1,653 lines, SHA-256 `75067c43ce96e825b2a7cc81589ad5a7b1aa4728ab5848939ed21b3433aad0b3` (matches the 2026-11-05 recorded hash).
- **Tool:** the split was done by a line-range script with exact-match replacements (each asserted unique), kept outside the repo at `/home/claude/mzwork/split.py`; its effect is fully listed below.
- **Rule:** no statement, proof, number or label was changed. Only the deletions and the glue listed below.

## Numbered statements (old numbering → destination)

Every numbered statement of the old draft is in exactly one paper. None was dropped.

| Old no. | Label | Kind | ID(s) | Destination | New no. (post-split) |
|---|---|---|---|---|---|
| 2.1 | lem:identities | Lemma | PD-T013 | MZ-CC | 2.1 |
| 2.2 | lem:floor | Lemma | PD-T015 | MZ-CC | 2.2 |
| 2.3 | thm:upper | Theorem | PD-T014, PD-T022 | MZ-CC | 2.3 |
| 2.4 | (none) | Remark, retained alternative proof | PD-T015 | MZ-CC | 2.4 |
| 2.5 | (none) | Remark, sign argument and boundary | PD-N002, PD-T016 | MZ-CC | 2.5 |
| 3.1 | lem:weight-comparison | Lemma | (part of PD-T017 proof) | MZ-CC; **statement recapped** in MZ-SP Lemma 1.1, citing MZ-CC | 3.1 |
| 3.2 | thm:cardinal | Theorem | PD-T017 | MZ-CC | 3.2 |
| 3.3 | thm:harmonic | Theorem | PD-T018 | MZ-CC | 3.3 |
| 3.4 | cor:endpoint | Corollary | (PD-T017/018) | MZ-CC | 3.4 |
| 3.5 | rem:rate | Remark | — | MZ-CC | 3.5 |
| 4.1 | thm:ratio-upper | Theorem | PD-T022 | MZ-CC | 4.1 |
| 4.2 | cor:ratio-endpoint | Corollary | PD-T022 | MZ-CC | 4.2 |
| 4.3 | thm:ratio-lower | Theorem | PD-T023 | MZ-CC | 4.3 |
| 4.4 | cor:strong | Corollary | PD-T024 | MZ-CC | 4.4 |
| 5.1 | prop:counterexample | Proposition | PD-T019, PD-N004 | MZ-CC; the consequence λ₋(512,511)<1/4 is **recapped** in MZ-SP Prop. 1.2 | 5.1 |
| 5.2 | prop:hyper | Proposition | PD-T025 | MZ-CC | 5.2 |
| 6.1 | thm:padua | Theorem | PD-T021 | MZ-SP | 2.1 |
| 6.2 | (none) | Lemma, integrated cardinal density | PD-T101, PD-T111 | MZ-SP | 2.2 |
| 6.3 | thm:padua-weights | Theorem | PD-T295 | MZ-SP | 2.3 |
| 6.4 | prop:padua-odd-weights | Proposition | PD-T377 | MZ-SP | 2.4 |
| 6.5 | thm:padua-carriers | Theorem | PD-N105, PD-N106 | MZ-SP | 2.5 |
| 6.6 | prop:padua-odd-carriers | Proposition | PD-T378 | MZ-SP | 2.6 |
| 6.7 | cor:padua-ratio | Corollary | PD-N107, PD-T378 | MZ-SP | 2.7 |
| 6.8 | prop:padua-growth | Proposition | PD-T379 | MZ-SP | 2.8 |
| 6.9 | thm:padua-operator | Theorem | PD-T297 | MZ-SP | 2.9 |
| 7.1 | prop:padua-finite-negative | Proposition | PD-T376 | MZ-SP | 3.1 |

Unnumbered material: Table 1 (CC spectra, PD-T026) → MZ-CC. Table 2 (Padua spectra, PD-T026), the m=60/80 exact brackets (PD-T298/299) and the marginal check → MZ-SP. The PD-T020/PD-T027 open-problem sentences → MZ-CC; the PD-T381 and signed-Padua open-problem sentences → MZ-SP.

## MZ-CC (`tracks/mz-constants/paper/manuscript.tex`): exact changes

Old lines kept: 1–953, 1497–1524, 1620–1653. Removed: old §6 (954–1496) and the Padua parts of old §7 (1525–1619). Edits to kept text:
1. Title and PDF title: "… Clenshaw–Curtis and Padua rules …" → "… Clenshaw–Curtis rules …".
2. Abstract: removed the four signed-Padua sentences (from "For signed Lebesgue Padua rules" to "below thirty.").
3. §1: removed the sentence "For the signed Padua rule the picture is different: … operator."
4. §7: "Tables 1–2 reproduce" → "Table 1 reproduces"; removed the PD-T380 comment line (moved to MZ-SP); removed the signed-Padua open-problem sentences ("Third, …" to "… remain separate.").
5. Closing paragraph: "central CC and Padua statements" → "central CC statements".
6. One TeX comment line before §7 pointing to MZ-SP and this file.

The development-status box is unchanged here; it is rewritten in task 4.

## MZ-SP (`tracks/mz-constants/paper-sp/manuscript.tex`): construction

- Preamble: old lines 1–26, with the PDF title changed. New title *Marcinkiewicz–Zygmund constants of signed Padua rules beyond half-exactness* (provisional), date 13 November 2026, a new short status box.
- Abstract: the four signed-Padua sentences of the old abstract, verbatim, plus "Analytic proofs are included."
- **New §1 (split glue), "Conventions and Clenshaw–Curtis inputs":**
  - old lines 82–95 (η definition) and 108–129 (CC conventions) verbatim;
  - the explicit weight formula with its bracket S_N (as in old Lemma 2.1);
  - **Lemma 1.1** (label `lem:weight-comparison`, kept so §2 references resolve unchanged): the bracket error estimate and two-sided interior weight comparison of old Lemma 3.1 *and its proof's displayed error bound*, which old Theorem 6.9's proof uses. Cited to MZ-CC;
  - **Proposition 1.2** (label `prop:counterexample`, kept for the same reason): λ₊(N,n) ≤ 2−4/N+4/N² < 2 for n<N (old Thm 2.3), λ₋(N,N−1)→0 (old Thms 3.2/3.3), λ₋(512,511)<1/4 (old Prop. 5.1). Cited to MZ-CC.
- §2: old lines 954–1496 verbatim (old §6).
- §3: a two-sentence measured-data paragraph adapted from old lines 1500–1508 (CC-only sentences removed), then old lines 1525–1619 verbatim, then the signed-Padua open-problem sentences of old lines 1628–1638 verbatim, and the reproducibility paragraph adapted (no LIT sentence, since MZ-SP cites nothing but MZ-CC yet).
- `refs.bib`: a single `MZ-CC` placeholder entry. The literature is added in task 5.

## Post-split baseline builds (2026-11-13)

`pdflatex; bibtex; pdflatex; pdflatex` (pdfTeX 1.40.25, TeX Live 2023/Debian), outputs in `/tmp/mzb/`:

| Build | Pages | Log / BibTeX | manuscript.tex SHA-256 |
|---|---:|---|---|
| Pre-split single draft | 25 (A4) | clean, 0 warnings | `75067c43…aad0b3` |
| MZ-CC post-split | 16 (A4) | clean, 0 warnings | `2537ce6f…97ee25` |
| MZ-SP post-split | 11 (A4) | clean, 0 warnings | `0a27b897…0b1aea` |

Gate W0: **PASS** (25 = recorded 25; both split manuscripts build cleanly; every numbered statement is mapped above).

## Class conversion (2026-11-13, separate commit)

By a Sonnet 5.5 high worker, verified by the orchestrator's own rebuild:
- **MZ-CC:** `\documentclass{siamart251216}`, `siamplain`, `\citep`/`\citealp` → `\cite` (29 places), `\newsiamremark`. The theorem counter is shared within sections, as before. SIAM equation numbering is (s.n). Placeholder keywords/MSC (65D32, 41A17, 41A10, 65F35) are for AC. Layout settings are in the preamble only (`\emergencystretch`, `\raggedbottom`, `\hbadness=1500`, and bibliography `\hbadness`). The only body change is that the `eq:mass` display is wrapped in `gathered` with one line break. 16 pages (486×720 pt), clean.
- **MZ-SP:** `\documentclass[preprint,12pt,a4paper]{elsarticle}`, `elsarticle-num`, `\journal{Journal of Approximation Theory}`, `\biboptions{sort&compress}`, frontmatter/tnote. Placeholder keywords/MSC (41A10, 41A63, 65D32, 41A17) are for AC. An `\hfuzz` workaround applies inside the output routine for elsarticle's preprint-footer overfull box. Body changes: four overfull displays are wrapped in `gathered` with a line break, and one `\allowbreak` was added. 15 A4 pages, clean.
- Every theorem-like label keeps its post-split number (14 CC, 9 SP labels compared). The development-status boxes now follow the abstract and keywords. They are removed in task 4.
