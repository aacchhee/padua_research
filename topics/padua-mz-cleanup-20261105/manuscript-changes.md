# C4 manuscript integration — accepted-result pass

Rules/input head: `ad503cb0603fc017444b0aa732240981eefa4d24`; base/main `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`. Developer: Codex manuscript subagent, inherited user-requested gpt-6.1-sol xhigh; runtime model/effort metadata not independently exposed. Date: 2026-11-05.

## Scope and source coverage

This is synthesis of accepted local results, with no new mechanism, status upgrade, external source claim, or novelty claim. The novelty gate for generating new candidates is not applicable. Read the rules, workflow, Codex role, cleanup handoff, fixed definitions, literature index, original manuscript/bibliography/README/history, accepted PD-T295/PD-N105/106/107/PD-T297 full proofs, PD-T298/299 exact results/reductions, and the supporting PD-T111 finite identity and existing CC weight lemma. No third-party PDF or full text was accessed or copied. No new citation was added; `refs.bib` is byte-identical to the input. The new literature comparison on unmerged PR #21 was not used, so no sentence requiring `% LIT pending PR21` is introduced.

## Changed sections and claim support

| Location | Added or changed statement | Durable support |
|---|---|---|
| Date/status | Date 5 November; old audits stay scoped, current integration review pending | Topic handoff and PR23 audit; no self-approval |
| Abstract | Even-m opposite-sign Gram divergence above half-exactness, uniform direct-operator norm | PD-T295, PD-N105–107, PD-T297 |
| §1 orientation | Signed Padua contrast and independence from finite spectrum fits | Same accepted analytic records |
| §6.1 | Retains the complete original marginal/compression theorem | PD-T021 unchanged |
| §6.2 first lemma | Cardinal kernel/DCT derivation and integrated signed density, including exceptional `-2 h_m T_m` | PD-T101 and PD-T111 |
| §6.2 boundary theorem | Fixed-index limit `m^4 w/log m=-16 e_j e_k (-1)^j` along even m; bound with 4096 on whole finite grid; proof | PD-T295 |
| §6.3 carrier theorem | Exact polynomial definitions, degree/norm estimates, finite DCT identities, dominated convergence, energy coefficients and spectral divergence | PD-N105 and PD-N106 |
| §6.3 ratio corollary | Identity through half-exactness; both extrema diverge at any fixed ratio >1/2 along even m | PD-N107 |
| §6.3 disposition paragraph | Retained OPEN registry labels do not override REJECTED: refuted dispositions | AC-prescribed PD-T028/110/116 registry treatment |
| §6.4 | Weighted-L1 norm identity, density tail, positive main-density and raw-Chebyshev bounds; `2≤norm≤28.3763348311…<30` for every m≥2, n<m | PD-T112/113 definitions and PD-T297 proof |
| §6.4 last paragraph | Reproduction only through min(n,m−n); no endpoint fixed-function convergence claim | Degree-m exactness and existing PD-N051 |
| §7 finite illustration | Strict exact rational m60/m80 brackets; integer-congruence inertia reduction and stated computational trust | PD-T298/299, PD-T106/107 |
| §7 open questions | CC PD-T020/027 remain open; signed positive conjectures refuted; quantitative onset/odd-m/sharp constants distinguished | Accepted theorem scopes and cleanup handoff |
| README | Current 22-page scope table, explicit rejection dispositions and build receipt | This compilation and above records |
| M7 history | Append-only dated integration entry | This record |

No C1 finite-witness certificate or new C2/C3 theorem has been inserted. They may be integrated only after the orchestrator supplies checked results and final IDs. The optional positive-reference PD-T296 is omitted because the paper's section focuses on the actual signed rule; no claim concerning that reference form is changed.

## Actual compilation and checks

Commands from repository root, except BibTeX in its output directory:

```sh
mkdir -p /tmp/padua-mz-cleanup-paper
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-cleanup-paper tracks/mz-constants/paper/manuscript.tex
(cd /tmp/padua-mz-cleanup-paper && BIBINPUTS=/workspace/padua_research/tracks/mz-constants/paper: bibtex manuscript)
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-cleanup-paper tracks/mz-constants/paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-cleanup-paper tracks/mz-constants/paper/manuscript.tex
pdfinfo /tmp/padua-mz-cleanup-paper/manuscript.pdf
pdftotext -layout /tmp/padua-mz-cleanup-paper/manuscript.pdf /tmp/padua-mz-cleanup-paper/manuscript.txt
pdftoppm -f 16 -l 16 -scale-to 1300 -png -singlefile /tmp/padua-mz-cleanup-paper/manuscript.pdf /tmp/padua-mz-cleanup-paper/page16
```

Result: 22 A4 pages, 491835-byte PDF. pdfTeX 1.40.26 and BibTeX 0.99d, TeX Live 2025/dev/Debian. Both final logs contain zero `Warning`, `Overfull`, `Underfull`, `undefined`, or leading-`!` markers. Rendered page16 was visually inspected: carrier theorem, displayed equations and proof fit the margins. A scripted source check found zero provisional-ID markers. `git diff --check` passed. Numerical tables were compared with the exact displayed source brackets during transcription, but no spectrum/eigenvalue run was executed here.

An initial BibTeX invocation from the repository root with the absolute `/tmp/manuscript` argument failed under TeX's `openout_any=p` restriction. Running BibTeX from its output directory corrected this build-path issue; the final complete sequence above passed. No earlier PDF, v1 preservation manifest, or response-01 build product was changed.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `tracks/mz-constants/paper/manuscript.tex` | 63933 | `cec0409659bcb6b642d6603a5724b9ebfcfff4f7f7125875857bce96a4d76dbc` |
| `tracks/mz-constants/paper/refs.bib` (unchanged) | 8810 | `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63` |
| `/tmp/padua-mz-cleanup-paper/manuscript.pdf` | 491835 | `ee2d0c1f674ce9a07e14c512416c4401ec031511360e16ee14a960bd7717510d` |

PDF bytes may change with TeX timestamps/output identifiers. These hashes pin this accepted-result pass, before possible orchestrator additions. Build products are scratch, not archived retrieval or cold-storage delivery; no PDF is committed.
