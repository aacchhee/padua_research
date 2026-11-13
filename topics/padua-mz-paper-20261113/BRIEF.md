# BRIEF — finalizing the MZ paper

Written by Claude (claude-opus-5-5), 2026-11-13. AC: "make a brief for a thread to finalize MZ paper".

This is a knowledge base and plan for the finalization thread. It carries no status. The goal is **two submission-ready manuscripts for AC's decision**. Submission, venue choice, cover letter, AI declaration, ORCID and contributions are AC's.

## 0. AC's decision (2026-11-13): split into two papers, MZ-CC and MZ-SP

AC: "yes let's split. call the one MZ-CC and another one MZ-SP".

### MZ-CC: the Clenshaw–Curtis paper

- **Source:** stays in `tracks/mz-constants/paper/`, which keeps continuity with the existing records.
- **Scope:** CC as an MZ family on Π_{N−1}, with sharp endpoint constants.
- **From the current draft:**
  - §2: exact CC identities and the upper bound below two;
  - §3: endpoint minimum eigenvalue;
  - §4: fixed-ratio bounds;
  - §5: three-quarter assumption and hyperinterpolation;
  - the CC rows of §7.
- **From PR #31:**
  - PD-T546/523/522: lim (log N)² λ_min = π⁴/8;
  - PD-T526: λ_max ≤ 5/3 for all N;
  - PD-T527: η_N bounds;
  - PD-T530/531 with PD-T528/529/548 and PD-T547: the λ_max → Λ_edge operator limit and finite brackets;
  - the CC parts of the PR #31 LIT entries (LIT-633).
- **Open in MZ-CC:** the decimal value of Λ_edge (the PD-T027 decimal conjunct).
- **Order:** finished and audited first.
- **Venue (AC, 2026-11-13):** **SIAM Journal on Numerical Analysis**; fallback Math. Comp. Prepare it in SIAM's journal class (`siamart`, current SIAM macros), checking SINUM's instructions for authors at the time of preparation.

### MZ-SP: the signed Padua paper

- **Source:** a new directory, `tracks/mz-constants/paper-sp/`, with its own `manuscript.tex`, `refs.bib`, `README.md`.
- **Scope:** signed Padua rules beyond half-exactness.
- **From the current draft, §6:**
  - marginal compression PD-T021. It uses CC weights and cites MZ-CC as a preprint;
  - exact density and logarithmic boundary weights PD-T295/T377;
  - carriers and the sharp ratio threshold PD-N105–107/PD-T378;
  - the uniform coefficient norm PD-T297;
  - finite witnesses PD-T376, finite illustrations PD-T298/299, normalized bounds PD-T379.
- **From PR #31:**
  - the corner operator B and the signed logarithmic limits (PD-T534/535/536/540/544/545);
  - the certified enclosure (PD-T541/542) and the carrier improvements (PD-T533/537).
- **Open in MZ-SP:**
  - the decimal values of spec(B)'s extremes (the PD-T381 decimal conjunct);
  - the first crossing;
  - effective onsets.
- **Recap:** keep a short recap of the CC conventions and weights, about a page, and cite MZ-CC for the rest.
- **Venue (AC, 2026-11-13):** **Journal of Approximation Theory**; fallback Adv. Comput. Math. Prepare it in Elsevier's `elsarticle` class, checking JAT's guide for authors at the time of preparation.

**Measured material** (PD-T026, PD-T380, PD-T525, PD-T532, PD-T543) goes to whichever paper it describes, always labelled MEASURED.

**Literature splits along the same line:**
- CC MZ prior art (Mastroianni–Russo, An–Wu, ASV) goes to MZ-CC;
- Padua cubature and hyperinterpolation literature goes to MZ-SP;
- some sources appear in both.

## 1. The single draft today (to be split)

- **Source:** `tracks/mz-constants/paper/manuscript.tex` (1,653 lines) and `refs.bib`. Build notes are in `tracks/mz-constants/paper/README.md`. The history is in `topics/mz-constants/directions/M7/manuscript-record.md`.
- **Title:** *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness*.
- **Length:** 25 A4 pages at the last build (2026-11-05). That build was clean: zero warnings, undefined references, overfull or underfull boxes.
- **Status:** "complete development draft … not a submission-ready paper".
- **Sections:**
  1. Problem, conventions, relation to the literature;
  2. Exact CC identities and an upper bound below two;
  3. The endpoint minimum eigenvalue;
  4. Explicit bounds at each fixed degree ratio;
  5. The three-quarter assumption and hyperinterpolation;
  6. Signed Padua rules beyond half-exactness (marginal compression; exact density and logarithmic boundary weights; two signed carriers and the exact ratio threshold; a uniform signed hyperinterpolation norm);
  7. Finite observations and unresolved sharpenings.
- **Results already inside** (README scope table):
  - PD-T013–019, PD-T021–026 and PD-N004;
  - PD-T295, PD-T297–299 and PD-N105–107;
  - PD-T376–379;
  - PD-T380 (MEASURED, companion only).

  Section 7 still presents PD-T020, PD-T027 and PD-T381 as OPEN.

## 2. What is new since the draft: PR #31, merged

Integrate these at their exact registered scopes. Starting text: `topics/padua-mz-sharp-constants-20261106/manuscript-insert.md`, including its K2/K4 interpretation addenda. Final IDs are PD-T522–548.

| Result | IDs | Status | What the paper may say |
|---|---|---|---|
| **Sharp CC minimum** | PD-T546 with PD-T523, PD-T522 | PROVED | lim (log N)² λ_min(G_{N,N−1}) = π⁴/8 through all integers N, on Π_{N−1} and Π_N. **PD-T020 is closed.** |
| **Uniform CC upper bound** | PD-T526 | PROVED | For every N ≥ 2 and p ∈ Π_{N−1}∖{0}: 0 < Q_N(p²) ≤ (5/3)∫p², i.e. λ_max ≤ 5/3 and the upper gap is ≥ 1/3 |
| **η_N behaviour** | PD-T527 | PROVED | Explicit two-sided reciprocal-log-squared bounds on 1 − η_N; η_N → 1 |
| **CC upper limit** | PD-T530, PD-T531, PD-T528/529, PD-T548, PD-T547 | PROVED (parts) | λ_max converges through all N and both parities to an explicit endpoint-operator norm Λ_edge ∈ [1, 3/2], with explicit finite brackets L_N ≤ … ≤ U_N, U_N − L_N → 0, and certified Λ_edge ≥ 1.0044369. **The decimal value is OPEN** (PD-T027 PARTIAL). |
| **Signed Padua log limits** | PD-T534, PD-T535, PD-T536, PD-T540, PD-T544, PD-T545 | PROVED | λ±(m, m−1)/log m converge on both parities to the same limits, inf/sup spectrum(B) of an explicit compact corner operator B with ‖B − B_K‖ ≤ 120/K. c₋ = −‖B‖ is simple, and 0 < c₊ < ‖B‖. **Decimal values are OPEN** (PD-T381 PARTIAL). |
| **Certified operator bounds** | PD-T541, PD-T542 | PROVED | Finite rectangle certificate enclosing ‖B‖ in [0.01316…, 0.47781…]. No useful digits. Say so. |
| **Scalar carriers** | PD-T533, PD-T537 | PROVED | Strictly improved normalized carrier coefficient; ceiling < 1/24 for the inherited scalar family (not optimal) |
| Measured | PD-T525, PD-T532, PD-T543 | MEASURED | Optional, in §7 only, labelled as measured. The fitted intercepts must not be presented as limits. |
| Literature | LIT-633 (Toeplitz-plus-Hankel same-symbol norms) and any other PR #31 LIT entries | LITERATURE | Cite only at the read scope |

**Consequence for the paper's shape.** The paper's headline changes from "orders and one-sided constants" to **exact endpoint constants**: π⁴/8, the uniform 5/3, and operator characterizations of the CC upper limit and of the signed Padua growth. The abstract, introduction, §2, §3, §6 and §7 need restructuring, not just insertion.

## 3. Literature status

- **PR #21 (merged)** supplies the P2 comparison, `topics/padua-literature-20261103/p2-comparison.md`, with proposed priority sentences.
  - It includes the Mastroianni–Russo 2000 record. Its Theorem 11 does not cover the p = 2, u ≡ 1 Clenshaw–Curtis endpoint case, and it states no rates.
  - It also has a MathSciNet citation-check note, `notes/mathscinet-citation-check-2026-11-05.md`.
  - Earlier MZ literature work: `topics/mz-constants/literature-search.md` (it lists remaining full-text gaps) and `literature-response-01.md`.
- **The manuscript's literature section predates PR #21.** Resolve every place where it hedged pending that campaign.
- **Rule:** cite only what has a fulltext-read LIT record at the cited scope, or label coverage honestly. Give AC clickable DOI or journal links for anything still unread that the paper needs.
- **Still-missing items noted earlier** (low priority unless the text needs them): Della Vecchia–Mastroianni–Vértesi 1995 (print only), Brutman 1997, Feldheim 1936.

## 4. AC's manuscript criteria

These are drawn from his instructions on the Padua argmax manuscripts, as recorded in that branch's audit-04 brief (`origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/audit-04-manuscripts.md`):

- mathematical coherence and sufficient explanation matter more than page count;
- notation is introduced before use, with one meaning per symbol, ideally via a notation register;
- named tools are either cited or stated in the form used;
- needed derivations and worked examples are kept;
- the AI declaration, ORCID and contributions are reserved to AC and are not edited by agents;
- the data and code availability statement must be accurate. Computer-assisted parts (PD-T298/299 inertia brackets, PD-T376 witnesses, PD-T531/541/542/547 certificates) need committed checkers named precisely. Bulk data may need a deposit **created by AC** (cold-storage deliveries are still pending).

That branch's notation register and correspondence-check tooling is a usable model. Reuse the approach, not its files.

## 5. Decisions reserved for AC

Ask these early, in one message. Meanwhile, proceed on defaults.

1. **Venue for each paper.** *Decided by AC on 2026-11-13:* MZ-CC → SIAM J. Numer. Anal. (fallback Math. Comp.); MZ-SP → J. Approx. Theory (fallback Adv. Comput. Math.).
2. **One paper or a split.** *Decided by AC on 2026-11-13: split into MZ-CC and MZ-SP (§0).*
3. **Companion document.** *Decided by AC on 2026-11-13:* "companion document may be prepared only for my own reading, arxiv and journal should be the same". Long derivations go in each paper's appendices; any companion is a private reading aid for AC only.
4. **Data deposit.** *AC, 2026-11-13: Zenodo will come later.* Until AC creates it, the text says "available in the repository at commit …" for the committed checkers and receipts. Leave a clearly marked placeholder for the deposit DOI, and make no deposit claim.

## 6. Known pitfalls

- **Do not overclaim the open parts.**
  - PD-T027's decimal value is open; the certified enclosure is only one-sided (≥ 1.0044369).
  - PD-T381's decimals are open; the ‖B‖ enclosure has "no useful digits".
  - No first-crossing claim for the signed Padua indefiniteness: m = 1240 is only the smallest even degree certified negative in this campaign.
- **Keep the PD-T380/PD-T525/PD-T532 fits labelled as measured.** The fitted intercepts exceed the proved limsup, which is exactly why they must not be read as limits.
- **"Rejected" conjectures.** PD-T028/110/116 have registry status OPEN with a binding REJECTED disposition. In the paper, say "refuted", by PD-N105–107 and PD-T377/378.
- **Raw versus normalized constants.** Raw constants 1/9 and 1/36 are energy coefficients, not normalized spectral constants (the PD-T379 note). Keep that distinction.
- **The PR #31 K2/K4 addenda** explain why finite-window model tests rejected an equality model while the inequality theorems stand. The text must not contradict them.
