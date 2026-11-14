# MZ-CC: Marcinkiewicz–Zygmund constants of Clenshaw–Curtis quadrature beyond half-exactness

**Status (2026-11-14).** Complete internal draft in SIAM's `siamart` class, 32 pages. It has passed two internal referee rounds (mathematics, Opus 5.5 xhigh: no CRITICAL or MAJOR finding, the Λ_edge certificate rerun byte-identical; exposition, Opus 5.5 high), answered in [response-internal-cc.md](../../../topics/padua-mz-paper-20261113/response-internal-cc.md). The **Codex audit is pending**. Not submitted. Authorship, venue, cover letter, AI declaration, ORCID, contributions, funding and submission are AC's; the manuscript carries placeholders for them. Venue chosen by AC (2026-11-13): SIAM J. Numer. Anal., fallback Math. Comp.

This is the first of two papers split from the single 2026-11-05 draft (AC, 2026-11-13). The signed Padua material is in [MZ-SP](../paper-sp/README.md), which cites this paper for three CC spectral inputs. Reading order for AC: MZ-CC first (arXiv first, then MZ-SP).

## Files

| File | Role |
|---|---|
| [manuscript.tex](manuscript.tex) | LaTeX source (`siamart251216`, bibliography style `siamplain`) |
| [refs.bib](refs.bib) | Bibliography; the `coverage` field records what was read of each source |
| [siamart251216.cls](siamart251216.cls), [siamplain.bst](siamplain.bst) | SIAM macros v1.4.8 (2025-12-16). SIAM's class is not on CTAN; these are byte-identical public GitHub copies, committed at AC's request. **Replace them by SIAM's official macro download before submission** and rebuild |

Not in Git: any PDF, build output, or the private companion reading aid (BRIEF §5 item 3).

## Build

From the repository root, with a scratch output directory (it copies the sources, runs `pdflatex; bibtex; pdflatex; pdflatex`, and prints pages, log issues and hashes):

```sh
bash topics/padua-mz-paper-20261113/tools/build.sh tracks/mz-constants/paper /tmp/mz-cc
```

Explicit sequence (the same, in a scratch directory that holds a copy of the four source files):

```sh
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

Last build (2026-11-14, head `a0206a8`, pdfTeX 1.40.25 / TeX Live 2023 Debian): **32 pages** (486 × 720 pt), zero LaTeX and BibTeX warnings, no over- or underfull boxes, no undefined references. Hashes of source and PDF are in the [manuscript record](../../../topics/mz-constants/directions/M7/manuscript-record.md) (PDF bytes change on every rebuild; the source hashes identify the draft). Avoid `\S` in the text: in `siamart` it loads a bitmap TS1 font and breaks microtype font expansion.

## Mathematical scope

Numbers are the **frozen numbering** (checked against the compiled `.aux` on 2026-11-14; later passes may change wording but must not renumber, see [correspondence-cc.md](../../../topics/padua-mz-paper-20261113/correspondence-cc.md)). Statuses are those of the registry records at `b5388c2` unless marked provisional. "PROVED" means a complete proof is in the paper or its appendix at the scope stated. Nothing here is an audit statement.

| No. (label) | PD ID(s) | Status | Exact scope |
|---|---|---|---|
| Thm 1.1–1.3, Cor 1.4 | restatements of 3.1, 3.3, 4.1–4.7, 5.2, 5.3, 6.1, 7.2, (8.3) | PROVED | Introduction summaries, each with a pointer to the proved statement; no extra claim |
| Lem 2.1 (`lem:identities`) | PD-T013 | PROVED | CC weights, positivity, aliasing, defect and mass matrices |
| Lem 2.2 (`lem:floor`) | PD-T015 | PROVED | (1/N)E ⪯ M ⪯ (π/2)E on Π_{N−1} |
| Lem 2.3 (`lem:weight-comparison`) | part of PD-T017 proof | PROVED (routine) | sin θ_j/N ≤ w_j ≤ 5 sin θ_j/N; w_j ≥ (1+d_j)/N² |
| Lem 2.4 (`lem:schur`) | none registered | PROVED (routine) | Weighted Schur test; **include in the audit** |
| Thm 3.1 (`thm:ratio-upper`) | PD-T022 | PROVED | Q_N(p²) ≤ (1+ρ)∫p² on Π_n, n<N, ρ = max{2n/N−1,0}²; strict if 2n>N |
| Cor 3.2 (`cor:ratio-endpoint`, also `thm:upper`) | PD-T014, PD-T022 | PROVED | λ₊(N,N−1) ≤ 2−4/N+4/N² < 2; equality at N=2, strict for N ≥ 3 |
| Thm 3.3 (`thm:five-thirds`) | PD-T526 | PROVED | λ₊(N,n) ≤ min{1+ρ_{N,n}, 5/3} for all N ≥ 2, n<N. 5/3 is **not** claimed optimal |
| Rem 3.4 | PD-N002, PD-T016 | PROVED | D is not PSD for N ≥ 5; Q_N(T_N²)/∫T_N² = 2(4N²−1)/(4N²−2) > 2 |
| Thm 4.1 (`thm:cardinal`) | PD-T017 | PROVED | ∫p² ≤ K_N Q_N(p²) on Π_N, K_N = O((log N)²) explicit |
| Lem 4.2 (`lem:U-exact`) | PD-T019; PD-T?mz-paper-claude-01 (a), onset part | PROVED | Exact U_{N−1} quotient; q_N < 1/3 for every N ≥ 57 (the 57 is the new part) |
| Thm 4.3 (`thm:harmonic`) | PD-T018 | PROVED | λ₋(N,N−1) ≤ 128000/(log N)² for all N ≥ 2. The constant is far from π⁴/8 (factor ≈ 7·10⁸ in K_N) |
| Lem 4.4 (`lem:volterra`) | PD-T522 | PROVED | ‖V‖ = 2/π on L²(0,1); quotient π⁴/8 attained at cos(πy/2) |
| Prop 4.5 (`prop:sharp-trial`) | PD-T523 | PROVED | limsup (log N)²λ₋(N,N−1) ≤ π⁴/8 through all N. **Proof route differs from the record** (through Lem A.1(c)); statement unchanged; flagged for the audit |
| Thm 4.6 (`thm:sharp-min`) | PD-T546 (with PD-T523) | PROVED | lim (log N)²λ₋(N,N−1) = lim (log N)²λ₋(N,N) = π⁴/8 through all integers N, with the finite bound (σ_N+τ_N), L=log N ≥ 16. **Closes PD-T020** |
| Cor 4.7 (`cor:interp-norm`) | PD-T?mz-paper-claude-01 (d) | PROVED, provisional | ‖𝓘_N‖_{ℓ²_w→L²} = λ₋(N,N)^{−1/2}; ‖𝓘_N‖/log N → 2√2/π² |
| Lem 4.8, 4.9 | PD-T544, PD-T545 | PROVED | Signed-remainder bound; discrete-primitive bound (lemmas of the π⁴/8 proof; proofs in Appendix A) |
| Prop 5.1 (`prop:fixed-trial`) | PD-T529 (**weakened**) | PROVED | Qualitative fixed-J limits, positive definiteness of the model form, 1 ≤ Λ_edge ≤ 5/3, liminf λ₊(N,N−1) ≥ Λ_edge. Explicit constants of PD-T529 are dropped (they serve only the omitted PD-T531) |
| Thm 5.2 (`thm:edge-limit`) | PD-T530 (definition PD-T528) | PROVED | lim λ₊(N,N−1) = Λ_edge ∈ [1, 3/2] through all N, qualitative (no rate) |
| Prop 5.3 (`prop:edge-certified`) | PD-T547; Lem C.1 = PD-T548 | PROVED, **computer-assisted** | Λ_edge ≥ 1.0044369, **one-sided**. Trust base listed in Appendix C |
| Cor 6.1 (`cor:endpoint`) | PD-T527; PD-T?mz-paper-claude-01 (a)(b) | PROVED (a)(b provisional) | K_N⁻¹ ≤ 1−η_N ≤ min{1, 128000/log²N}; 1−η_N = λ₋(N,N−1) for N ≥ 57; (log N)²(1−η_N) → π⁴/8; κ₂(G_N)/(log N)² → 8Λ_edge/π⁴ ∈ [0.08249, 0.12320] (the lower end is computer-assisted via Prop 5.3) |
| Rem 6.2 (`rem:rate`) | none | remark | No rate usable at computable N; decimal of Λ_edge open |
| Thm 7.1 (`thm:ratio-lower`) | PD-T023 | PROVED | ∫p² ≤ C_*(1−n/N)⁻²Q_N(p²) on Π_n, C_* = 12(1+π)⁴(1+2/π); degenerates like N⁻² at n = N−1 |
| Cor 7.2 (`cor:strong`) | PD-T024 | PROVED | Spectrum of G_{N,n} in [(1−ϑ)²/C_*, 1+max{2ϑ−1,0}²] for n ≤ ϑN, ϑ<1; C_* not claimed optimal |
| Prop 8.1 (`prop:counterexample`) | PD-T019, PD-N004 | PROVED | λ₋(512,511) < 1/4, so ‖I−G_{512,511}‖ > 3/4 (An–Wu's m=513, n=511); their conditional theorem stays valid |
| Prop 8.2, eq. (8.3) (`prop:hyper`) | PD-T025; CC application with PD-T?mz-paper-claude-01 (c) | PROVED (c provisional) | Upper-Gram hyperinterpolation estimate for any positive rule; CC factor √2(1+√B), B = min{1+ρ_{N,n}, 5/3}, so (1+√(5/3))√2 < 2.2910·√2 |
| App. A (Lem A.1 `lem:endpoint-rep`; proofs of 4.5, 4.8, 4.9, (4.6) finite bound) | PD-T546 proof §1–2, PD-T523, PD-T544, PD-T545 | PROVED | Endpoint representation of the interpolant and the long proofs of §4.2 |
| App. B (Lem B.1, B.2; B.1–B.3) | PD-T529, PD-T530 proofs | PROVED | Core density, continuum identity, proof of Thm 5.2 |
| App. C (Lem C.1; certificate) | PD-T548, PD-T547 | PROVED, computer-assisted | Closed forms of the model mass; finite reduction; enclosures 1.004436918864667280457774 ≤ q(u) ≤ …779 for the J = 512 trial vector; exact comparison with 10044369/10⁷ passes; the upper endpoint bounds q(u) only, not Λ_edge |

**Omitted on purpose:** PD-T531 (finite brackets L_N ≤ λ₊ ≤ U_N; long proof, no digits at practical N; existence of the limit is Thm 5.2) and PD-T524 (historical conditional prediction, superseded by PD-T546). **Not claimed:** optimality of 5/3, of C_*, or of 128000.

### Measured items (Section 9, labelled as such; no proof uses them)

- Table 1: extreme eigenvalues of G_{N,N−1}, N = 40…1280, double precision, with a (log N)²λ₋ column (PD-T026, MEASURED). Consistency check at N = 3, 4, 5, 9, 10, 21, 40, 81 to within 1.35·10⁻¹³.
- J-Galerkin proxy of the model quotient: 1.00443691886… (J = 512), 1.0044369671… (J = 2048, so J = 512 is not converged) (PD-T532, MEASURED). **Not a certified decimal.**
- PD-T525 fits are not used.

### Open (stated as open problems in Section 9)

1. A two-sided certified enclosure, hence the decimal value, of Λ_edge (the decimal conjunct of PD-T027, whose other conjuncts are PROVED by PD-T526 and PD-T530).
2. Rates in Thms 4.6 and 5.2 usable at computable N.
3. Identification of the endpoint sampling operator with a classical operator (Toeplitz-plus-Hankel or Wiener–Hopf type) whose norm can be computed.

Declined strengthening, recorded as a candidate and **not** in the paper: sup_N λ₊(N,N−1) ≤ 23/15 (referee F2; see [report.md](../../../topics/padua-mz-paper-20261113/report.md)).

## Placeholders reserved for AC

Authors and `\thanks`, keywords and MSC codes (suggested additions 41A05, 42C05), funding footnote, commit hash and Zenodo DOI in the data and code availability statement (no deposit exists; after audit F1 the text says only that an archived copy is planned, and names the committed repository files), AI declaration, ORCID, contributions. Before an arXiv upload, remove the `% IDs:` / `% Source:` TeX comments, three of which carry the provisional ID `PD-T?mz-paper-claude-01` (the comments are public in the TeX source). Confirm "252 (2027)" for LIT-045 and the editor and series data of LIT-052.

## Records

[Topic log](../../../topics/padua-mz-paper-20261113/LOG.md) · [BRIEF](../../../topics/padua-mz-paper-20261113/BRIEF.md) · [split map](../../../topics/padua-mz-paper-20261113/split-map.md) · [plan](../../../topics/padua-mz-paper-20261113/plan-cc.md) and [plan review](../../../topics/padua-mz-paper-20261113/review-plan-cc.md) · [correspondence table and frozen numbering](../../../topics/padua-mz-paper-20261113/correspondence-cc.md) · [notation register](../../../topics/padua-mz-paper-20261113/notation-cc.md) · [literature scope check](../../../topics/padua-mz-paper-20261113/literature-mz-paper.md) · referee reports [mathematics](../../../topics/padua-mz-paper-20261113/referee-cc-math.md) and [exposition](../../../topics/padua-mz-paper-20261113/referee-cc-exposition.md) · [provisional claim 01](../../../topics/padua-mz-paper-20261113/theory/cc-defect-condition-corollary.md) with checks [1](../../../topics/padua-mz-paper-20261113/check-cc-defect-corollary.md) and [2](../../../topics/padua-mz-paper-20261113/check-new-corollaries-02.md) · [topic report for AC](../../../topics/padua-mz-paper-20261113/report.md) (open questions, Zenodo file list) · [manuscript record](../../../topics/mz-constants/directions/M7/manuscript-record.md) (history of the single draft since 2026-10-31, and the current builds and hashes).
