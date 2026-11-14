# MZ-SP: Marcinkiewicz–Zygmund constants of signed Padua rules beyond half-exactness

**Status (2026-11-14).** Complete internal draft in Elsevier's `elsarticle` class (preprint, 12 pt, A4), 50 pages. It has passed two internal referee rounds (mathematics, Opus 5.5 xhigh: no CRITICAL or MAJOR finding, the ‖B‖ enclosure certificate rerun bit-identical, brackets match the receipts; exposition, Opus 5.5 high), answered in [response-internal-sp.md](../../../topics/padua-mz-paper-20261113/response-internal-sp.md). The **Codex audit is pending**. Not submitted. Authorship, venue, cover letter, AI declaration, ORCID, CRediT, funding and submission are AC's; the manuscript carries placeholders. Venue chosen by AC (2026-11-13): Journal of Approximation Theory, fallback Adv. Comput. Math.; the class and options follow JAT's usual `elsarticle` template, to be re-checked against JAT's guide for authors at submission.

The paper depends on [MZ-CC](../paper/README.md), which is to go out first (AC, 2026-11-13: "mz-cc first, mz-sp cites"). Three CC spectral inputs (λ₊ ≤ 2−4/N+4/N², λ₋(N,N−1) → 0, λ₋(512,511) < 1/4) are **cited** from MZ-CC (Cor 3.2, Thm 4.3, Prop 8.1), not reproved. The bibliography entry `MZ-CC` is a placeholder until the arXiv identifier exists.

## Files

| File | Role |
|---|---|
| [manuscript.tex](manuscript.tex) | LaTeX source (`elsarticle`, `elsarticle-num`, `\biboptions{sort&compress}`) |
| [refs.bib](refs.bib) | Bibliography; the `coverage` field records what was read of each source |

`elsarticle.cls` and `elsarticle-num.bst` are **not** in Git: they come from TeX Live (Debian package `texlive-publishers`; TeX Live 2023 here). Not in Git: any PDF or build output, and the private companion reading aid.

## Build

From the repository root, with a scratch output directory (it copies `*.tex` and `*.bib`, runs `pdflatex; bibtex; pdflatex; pdflatex`, prints pages, log issues and hashes):

```sh
bash topics/padua-mz-paper-20261113/tools/build.sh tracks/mz-constants/paper-sp /tmp/mz-sp
```

Explicit sequence in a scratch directory holding `manuscript.tex` and `refs.bib`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

Last build (2026-11-14, head `a0206a8`, pdfTeX 1.40.25 / TeX Live 2023 Debian): **50 A4 pages**, zero LaTeX and BibTeX warnings, no over- or underfull boxes, no undefined references. Hashes are in the [manuscript record](../../../topics/mz-constants/directions/M7/manuscript-record.md). A preamble workaround (`\hfuzz=3pt` inside the output routine) tolerates a 2.6 pt overfull box in `elsarticle`'s preprint footer.

## Mathematical scope

Numbers are the **frozen numbering** (checked against the compiled `.aux` on 2026-11-14; wording may change, numbers must not, see [correspondence-sp.md](../../../topics/padua-mz-paper-20261113/correspondence-sp.md)). Statuses are those of the registry records at `b5388c2`, unless marked provisional. Q^P_m is the interpolatory signed Padua rule for Lebesgue measure (total mass four), Gram matrices on total-degree spaces 𝒫_n.

| No. (label) | PD ID(s) | Status | Exact scope |
|---|---|---|---|
| Lem 2.1 (`lem:weight-comparison`) | routine part of PD-T017 | PROVED here | CC weights, bracket error, interior bound π−4/3, floor (1+d_j)/N² |
| Prop 2.2 (`prop:cc-inputs`) | PD-T014/022, PD-T017/018, PD-T019 / PD-N004 | cited from MZ-CC (LITERATURE-style dependency) | λ₊(N,n) ≤ 2−4/N+4/N² for n<N; λ₋(N,N−1) → 0; λ₋(512,511) < 1/4. Not reproved; needs MZ-CC public |
| Thm 3.1 (`thm:padua`) | PD-T021 | PROVED | For **any** rule on the Padua points exact on 𝒫_m (signed weights allowed): first-coordinate marginal Σ_{k} w̃_{jk} = 2w_j, with w_j the CC weights with m intervals; λ_min ≤ λ₋(N,n), λ_max ≥ λ₊(N,n), η ≥ η^CC; for Q^P_m liminf ‖I−G_{m,m−1}‖ ≥ 1 and defect at m=512 exceeds 3/4 |
| Lem 4.1 (`lem:density`) | PD-T101, PD-T111 | PROVED | Integrated cardinal density of the signed weights |
| Thm 4.2 (`thm:padua-weights`) | PD-T295 | PROVED | Even m: lim m⁴w_{jk}/log m = −16e_je_k(−1)^j at fixed indices (j+k even); whole-grid majorant with 4096 |
| Prop 4.3 (`prop:padua-odd-weights`) | PD-T377 | PROVED | Same limit over odd m; majorant with 8192 |
| Thm 5.1 (`thm:padua-carriers`) | PD-N105, PD-N106 | PROVED | Even m: carriers with Q^P_m(p²)/log m → −16ab/9 (a+b<1/2) and 8ab/9 (2a+b<1/2), degree ≤ m−1; λ₋ → −∞, λ₊ → +∞ at n = m−1 |
| Prop 5.2 (`prop:padua-odd-carriers`) | PD-T378 | PROVED | Odd-m carriers (even y mesh m+1); divergences over all integers m |
| Cor 5.3 (`cor:padua-ratio`) | PD-N107, PD-T378 | PROVED | G^P_{m,n} = I for n ≤ m/2; for every fixed τ ∈ (1/2, 1), λ₋(m,⌊τm⌋) → −∞ and λ₊ → +∞ over all integers m; no uniform strong MZ constant η_τ < 1 |
| Rem 5.4 (`rem:refuted`) | PD-T028, PD-T110, PD-T116 | REJECTED: refuted (registry OPEN retained by AC) | Consequences of 5.1–5.3 for the signed rule only; not for positive Chebyshev Padua cubature or tensor CC |
| Lem 5.5 (`lem:fejer-cosine`) | inside PD-T379 proof | PROVED (auxiliary) | Closed form for J₋(a) |
| Prop 5.6 (`prop:padua-growth`) | PD-T379 | PROVED | One-sided normalized bounds for λ^P_±(m,m−1)/log m over all integers m. Raw constants 1/9, 1/36 are energy coefficients, not normalized spectral constants. No sharp law |
| Prop 5.7 (`prop:carrier-improvement`) | PD-T533 | PROVED | limsup λ₋/log m ≤ −κ_new, κ_new > κ^car₋ (≈ 0.02964 against 0.02962); one-sided |
| Prop 5.8 (`prop:carrier-ceiling`) | PD-T537 | PROVED | Scalar carrier family: κ₋(a,b) < U₋ < 1/24. Not optimal, not a bound on the spectrum |
| Thm 6.1 (`thm:log-reduction`) | PD-T534 | PROVED | \|Q^P_m(p²) − log R · L_m[p]\| ≤ 4096‖p‖², ‖L_m‖ ≤ 120, spectral error 4300/log m, m ≥ 4, both parities |
| Lem 6.2 (`lem:corner-kernel`) | PD-T535 | PROVED | Two-variable quantitative Mehler–Heine-type corner kernel limit, error O(1/m) |
| Thm 6.3 (`thm:corner-operator`) | PD-T536 | PROVED | B compact selfadjoint, ‖B−B_K‖ ≤ 120/K; λ^P_±(m,m−1)/log m → c_± = inf/sup σ(B), c₋ < 0 < c₊, over all integers m. No decimal of c_± |
| Rem 6.4 (`rem:finite-comparison`) | PD-T536 (4) | PROVED | Explicit but coarse finite comparison; certifies no finite range |
| Rem 6.5 (`rem:two-corners`) | review F8 | remark | Two active corners double multiplicities, not values (limited to what the proof shows) |
| Prop 6.6 (`prop:elliptic-kernel`) | PD-T539 (**weakened**) | PROVED | Elliptic-integral kernel of B, β ≤ 0 a.e.; the log-singularity sentence of the record is dropped |
| Prop 6.7 (`prop:positivity`) | PD-T540 | PROVED | c₋ = −‖B‖ simple, eigenfunction > 0 a.e.; 0 < c₊ < ‖B‖ |
| Prop 6.8 (`prop:rectangles`) | PD-T541 | PROVED | Rectangle upper and lower certificates for ‖B‖ |
| Prop 6.9 (`prop:enclosure`) | PD-T542 | PROVED, **computer-assisted** | 0.013164946500379018110831 ≤ ‖B‖ ≤ 0.477809279990884889210594; fixes no decimal digit |
| Cor 6.10 (`cor:norm-lower`) | PD-T?mz-paper-claude-02 | PROVED, provisional | ‖B‖ = −c₋ ≥ κ_new (≈ 0.0296418) and c₊ ≥ κ^car₊ (≈ 0.0127789); lower bounds only |
| Thm 7.1 (`thm:padua-operator`) | PD-T297 | PROVED | Direct signed coefficient operator H_{m,n}: 2 ≤ ‖H_{m,n}‖_{C→L²} ≤ 28.3763348311… < 30 for every m ≥ 2, 0 ≤ n < m, with no sign condition on the Gram form |
| Rem 7.2 (`rem:reproduction`) | PD-T113 | PROVED | H_{m,n}q = q for q ∈ 𝒫_k, k ≤ min(n,m−n); ‖f−H f‖ ≤ (2+C_P)E_k(f). **The explicit bound is implied by PD-T297 and PD-T113 but stated in no record; for the audit** |
| Prop 7.3 (`prop:no-quadratics`) | PD-N051 | PROVED | H_{m,m−1} reproduces 𝒫₁ but not 𝒫₂, m ≥ 3; no fixed-function error bound with k ≥ 2 |
| Prop 8.1 (`prop:padua-brackets`) | PD-T107, PD-T298, PD-T299 | PROVED, **computer-assisted** | Strict rational brackets for λ^P_±(m,m−1), m = 10, 20, 30, 40, 60, 80, by exact inertia counts and diagonal-dominance reduction; "η < 0.83" is arithmetic on the brackets (for the audit) |
| Prop 8.2 (`prop:padua-finite-negative`) | PD-T376 | PROVED, **computer-assisted** | Exact trial-Rayleigh intervals at m = 1101, 1240, 1600 are strictly negative, so the form is indefinite there. **Trial quotients, not eigenvalue brackets. No first crossing**: 1240 is only the smallest even degree certified negative in this campaign |
| §8.3 (1)–(4) | PD-T026, PD-T538, PD-T543 | MEASURED | Negative-weight counts at m = 10…40 and marginal check; 16 minimum rows, window slopes ≈ −0.092 (finite-window slopes are **not** the limits c_±); mode-2 weights; B_K proxies at K = 128 (not enclosures) |
| App. A (Lem A.1–A.4) | PD-T534, PD-T535, PD-T536 proofs | PROVED | Reduction, kernel limit, finite-rank transfer (Lem A.4) |
| App. B (Lem B.1, B.2; B.2–B.5) | PD-T539–PD-T542 proofs | PROVED | Arcsine convolution, Abel sums, positivity, rectangle certificates, finite check behind Prop 6.9 (integers n_L, n_U listed in B.5) |

### Open (Section 9)

1. Decimal values of c_± (the decimal conjunct of PD-T381, whose other conjuncts are PROVED by PD-T534/535/536). Enclosure of ‖B‖ is coarse; no upper certificate for c₊.
2. The first sign change of the form on 𝒫_{m−1}, parity dependence, and whether it stays indefinite.
3. Effective onsets and usable rates for the divergences and for λ^P_±/log m → c_±.
4. The sharp norm of H_{m,n} and its limit at n = m−1.
5. Fixed-function convergence H_{m,m−1}f → f in L².

Declined, recorded as a candidate and **not** in the paper: |λ^P_±(m,⌊τm⌋)| ≍ log m for every fixed τ ∈ (1/2, 1) (see [report.md](../../../topics/padua-mz-paper-20261113/report.md)). Optional shortenings kept available but declined by the orchestrator: Appendix A.2 Step 1 (about 0.8 page) and Prop 5.8 (about 0.4 page).

## Placeholders reserved for AC

Author names and affiliations, CRediT, declarations, `\date`, funding, commit hash and Zenodo DOI in the data and code availability section and after Prop 8.2 ("DOI to be added"; no deposit exists, no deposit claim is made), the MZ-CC arXiv identifier in `refs.bib`, MSC (47B38, 65G20 added; AC to confirm). The witness arrays of Prop 8.2 are in no repository: they belong to AC's Zenodo deposit. Before an arXiv upload, remove the `% IDs:` TeX comments (one carries the provisional ID `PD-T?mz-paper-claude-02`; all comments are public in the source). The DOIs of BCDMVX06 and Xu96 are to be resolver-checked by AC.

## Records

[Topic log](../../../topics/padua-mz-paper-20261113/LOG.md) · [BRIEF](../../../topics/padua-mz-paper-20261113/BRIEF.md) · [split map](../../../topics/padua-mz-paper-20261113/split-map.md) · [plan](../../../topics/padua-mz-paper-20261113/plan-sp.md) and [plan review](../../../topics/padua-mz-paper-20261113/review-plan-sp.md) · [correspondence table, changes log and frozen numbering](../../../topics/padua-mz-paper-20261113/correspondence-sp.md) · [notation register](../../../topics/padua-mz-paper-20261113/notation-sp.md) · referee reports [mathematics](../../../topics/padua-mz-paper-20261113/referee-sp-math.md) and [exposition](../../../topics/padua-mz-paper-20261113/referee-sp-exposition.md) · [provisional claim 02](../../../topics/padua-mz-paper-20261113/theory/sp-corner-norm-lower.md) with [check](../../../topics/padua-mz-paper-20261113/check-new-corollaries-02.md) · [topic report for AC](../../../topics/padua-mz-paper-20261113/report.md) (open questions, Zenodo file list) · [manuscript record](../../../topics/mz-constants/directions/M7/manuscript-record.md). The per-citation literature scope table for MZ-SP in [literature-mz-paper.md](../../../topics/padua-mz-paper-20261113/literature-mz-paper.md) is still a placeholder; the exposition referee restricted new citations to read sources.
