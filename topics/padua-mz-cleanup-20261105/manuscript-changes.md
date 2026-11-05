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

Result: 22 A4 pages, 491835-byte PDF. pdfTeX 1.40.26 and BibTeX 0.99d, TeX Live 2025/dev/Debian. Both final logs contain zero `Warning`, `Overfull`, `Underfull`, `undefined`, or leading-`!` markers. Rendered page 16 was visually inspected: carrier theorem, displayed equations and proof fit the margins. A scripted source check found zero provisional-ID markers. `git diff --check` passed. Numerical tables were compared with the exact displayed source brackets during transcription, but no spectrum/eigenvalue run was executed here.

An initial BibTeX invocation from the repository root with the absolute `/tmp/manuscript` argument failed under TeX's `openout_any=p` restriction. Running BibTeX from its output directory corrected this build-path issue; the final complete sequence above passed. No earlier PDF, v1 preservation manifest, or response-01 build product was changed.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `tracks/mz-constants/paper/manuscript.tex` | 63933 | `cec0409659bcb6b642d6603a5724b9ebfcfff4f7f7125875857bce96a4d76dbc` |
| `tracks/mz-constants/paper/refs.bib` (unchanged) | 8810 | `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63` |
| `/tmp/padua-mz-cleanup-paper/manuscript.pdf` | 491835 | `ee2d0c1f674ce9a07e14c512416c4401ec031511360e16ee14a960bd7717510d` |

PDF bytes may change with TeX timestamps/output identifiers. These hashes pin this accepted-result pass, before possible orchestrator additions. Build products are scratch, not archived retrieval or cold-storage delivery; no PDF is committed.

## 2026-11-05 — cleanup-result extension (historical scratch-only 24-page build)

The intermediate 24-page TeX source with SHA-256 `6d28fe6cecaa9fee32267b068670d4a41243baf6de27746d7375937acc5fd063` was scratch-only and was never committed. Its source and PDF receipt below is retained as historical provenance.

At the orchestrator's request, after the accepted-result pass was committed as `58a3d15` and main `aff30e8` was merged, the manuscript worker read the complete new local theory files and the actual m = 1600 producer and independent-checker receipts. Input head inspected: `ef9723bef6dd061109db1237f3338626093e1052`; rules still read at `ad503cb0603fc017444b0aa732240981eefa4d24`. Same inherited user-requested gpt-6.1-sol xhigh; runtime model/effort not independently exposed. No Git operations or shared-registry edits by this worker.

The original accepted-result source/PDF hashes above identify that historical pass and are not overwritten. The current extension adds:

| Location | Statement and scope | Source |
|---|---|---|
| Status, abstract, §1 | All-integer divergence now stated; old accepted results distinguished from cleanup results awaiting Claude audit | Odd-carrier development plus accepted even carriers |
| §6.2 odd-degree proposition | Same fixed-index limit for odd m, global majorant 8192, floor-half proof with both phase limits | `theory/odd-weight-asymptotic.md` |
| §6.3 odd-carrier proposition | Correct even y mesh M=m+1; polynomial degrees with +1/2 overhead, parity sums and all-integer divergence | `theory/odd-carriers.md` |
| §6.3 ratio corollary | Both extrema diverge on all integers at every fixed theta>1/2; exactness through half-degree remains unchanged | Existing PD-N107 and odd-carrier extension |
| §6.3 normalized-bound proposition | Exact integral definitions of A,J_minus,J_plus, rescaled dominated-convergence proof, A=4log2, one-sided normalized coefficients; raw 1/9 and 1/36 are not spectral constants | `theory/growth-carrier-bounds.md` |
| §7 finite-witness proposition | m = 1600,n1599 exact dyadic polynomial has Rayleigh quotient in (-23415/10^6,-23414/10^6); indefinite by positive constant direction; this is not an eigenvalue bracket | `theory/finite-indefiniteness.md` (orchestrator-owned); actual `/tmp/mz-cleanup/cert-m1600.json` and `/tmp/mz-cleanup/independent-m1600.json` inspected |
| §7 certificate reduction/trust | Exact Legendre norm, outward Arb node tables, integer fixed-point tensors/error enclosure; separate forward-error path under documented IEEE/BLAS assumptions; no eigensolver accuracy premise | Actual producer/checker source and receipts |
| §7 open questions, README | Parity classification complete; first crossing, sharp growth limits and sharp operator norms remain distinct | Above exact scopes |

Only final IDs occur in the manuscript. New results use source-path comments without provisional or invented final IDs, pending orchestrator preparation. No new external source, idea, novelty claim, or priority sentence is introduced by translation. Bibliography unchanged. The long cosine-transform closed form in the growth record is not duplicated: the manuscript defines its exact constants by convergent positive integrals and proves the norm limit and one-sided bounds directly.

Actual build: incremental pdfLaTeX twice with output directory `/tmp/padua-mz-cleanup-paper`, after the previously successful BibTeX pass (bibliography unchanged). `pdfinfo` reports 24 A4 pages. Both final logs have zero warning/error/undefined-reference/overfull/underfull markers. `git diff --check` passed. Page 22 was rendered with `pdftoppm -f 22 -l 22 -scale-to 1300 -png -singlefile ...` and visually checked: proposition, quotient interval and certificate discussion fit the page. No eigenvalue/certificate computation was rerun by the manuscript worker. The source receipts were inspected, not independently executed here.

| Current artifact | Bytes | SHA-256 |
|---|---:|---|
| `tracks/mz-constants/paper/manuscript.tex` | 72502 | `6d28fe6cecaa9fee32267b068670d4a41243baf6de27746d7375937acc5fd063` |
| `tracks/mz-constants/paper/refs.bib` (unchanged) | 8810 | `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63` |
| `/tmp/padua-mz-cleanup-paper/manuscript.pdf` | 507863 | `fb7c737d0f50d0aa404e4a76c3d83d7963f8bf9e5a8ba15faf176b98fee63917` |

This pin predates any final-ID substitution or later m = 1240 addition. No m = 1240 certificate or first-crossing claim is in the current source. The PDF remains scratch; no cold-storage delivery is claimed.

## 2026-11-05 — three finite witnesses (final current pass)

The orchestrator confirmed completed producer and independent acceptance at m = 1101,1240,1600; all six short receipts and the finite theory were committed in `39479ff`. This worker inspected `theory/finite-indefiniteness.md` and the additional actual producer/checker JSONs at 1101 and 1240. Section 7's finite proposition now has all three exact rational trial-Rayleigh intervals:

- m = 1101: `(-35067/10^6,-35066/10^6)`;
- m = 1240: `(-273/10^7,-270/10^7)`;
- m = 1600: `(-23415/10^6,-23414/10^6)`.

The text states only that 1240 is the smallest even construction degree certified negative **in this campaign**. No lower-degree positivity theorem, earliest mathematical crossing, or unfinished fine-scan result is claimed. Earlier m = 1600-only receipt text is historical. Current proof/trust and all other C2/C3 integrations are unchanged from the preceding extension.

Actual final incremental pdfLaTeX build: 25 A4 pages, zero final LaTeX/BibTeX warning/error/undefined-reference/overfull/underfull markers. `git diff --check` passed. Final page 22, containing the three-witness table and certificate reduction, was rendered and visually checked; formulas/table fit the margins. Numerical and certificate runs belong to their separate producer/checker agents. The manuscript worker performed only source/receipt review and document compilation.

| Current artifact | Bytes | SHA-256 |
|---|---:|---|
| `tracks/mz-constants/paper/manuscript.tex` | 73027 | `d0da06adcad1f6d9aa6bcf6add2631c5a065d104fc3327ebee234632a6c8e04f` |
| `tracks/mz-constants/paper/refs.bib` (unchanged) | 8810 | `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63` |
| `/tmp/padua-mz-cleanup-paper/manuscript.pdf` | 510003 | `4f58e5b9a1d2fa0e0295502eb70e414fbffec3962cc4149190b158ade7d419fa` |

These hashes identify the final manuscript-worker pass before orchestrator final-ID substitution. All generated products remain scratch; preserved v1/response-01 artifacts were untouched. No PDF is committed or claimed delivered. Claude audit is pending.

## 2026-11-05 — response to cleanup audit-01 (current build)

Rules/input: `a64ef35` (full response input recorded by the orchestrator). Codex manuscript-response worker, inherited user-requested gpt-6.1-sol xhigh; runtime serving metadata is not independently exposed. Read the rules, workflow, Codex role, handoff 03, audit-01 findings F12–F16, current source/scope/build receipts and M7 history. This is an editorial translation response, with no new mechanism, mathematical claim, proof change, scientific status upgrade, external citation or novelty claim; the idea-generation gate does not apply.

- **F12 fixed:** README and the finite-witness certificate discussion now distinguish committed small receipts from separately staged witness arrays and exact norm files. External cold-storage delivery remains pending.
- **F13 fixed:** both Padua spectrum tables now use `\lamin(G^\Pa_{m,n})` / `\lamax(G^\Pa_{m,n})`; the Clenshaw–Curtis table's original symbols are unchanged.
- **F14 fixed:** the finite certificate trust statement explicitly names FLINT exact integer/rational arithmetic as well as Arb outward ball tables and the alternate checker's existing IEEE/BLAS assumptions.
- **F15 fixed:** the earlier 24-page `6d28fe…` source is explicitly labelled scratch-only and never committed. Its historical hash/PDF receipt remains intact.
- **F16 fixed within scope:** missing spaces in touched README, attempt and change-record prose were repaired. The M7 history is append-only by the orchestrator's explicit instruction; its earlier dated entries remain unchanged, and the new spaced entry records the current response/build. Historical pending-review wording in earlier build entries is preserved as history.

Current status metadata in the manuscript and README now cites cleanup Claude audit-01's completed acceptance at its stated mathematical/translation scopes, with editorial dispositions in response-01. This confers no PR readiness, merge permission, submission readiness or historical novelty clearance. No certificate, checker or spectrum program was executed or changed by this worker; all accepted numerical data, code and certificate identities are preserved.

### Actual build and checks

From repository root, with BibTeX run in its output directory:

```sh
mkdir -p /tmp/padua-mz-response-paper
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-response-paper tracks/mz-constants/paper/manuscript.tex
(cd /tmp/padua-mz-response-paper && BIBINPUTS=/workspace/padua_research/tracks/mz-constants/paper: bibtex manuscript)
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-response-paper tracks/mz-constants/paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-response-paper tracks/mz-constants/paper/manuscript.tex
```

Two additional final pdfLaTeX passes applied the current audit-status metadata after that sequence. The final build has **25 A4 pages**. Final LaTeX/BibTeX logs contain zero warning, overfull/underfull, undefined-reference or leading-error markers. A source scan finds no provisional PD-T/PD-N/IDEA/LIT marker. Page 22 was rendered with `pdftoppm -f 22 -l 22 -scale-to 1200 -png -singlefile` and visually inspected; the table, quotient intervals, trust paragraph and delivery note fit their margins. Bibliography bytes are unchanged. Build output remains scratch, with no PDF commit or archival-delivery claim.

| Current artifact | Bytes | SHA-256 |
|---|---:|---|
| `tracks/mz-constants/paper/manuscript.tex` | 73392 | `9e10c6353fd625807bfca98fc1f868f1db37cc1eaea89c66751cfbd27c4ba28d` |
| `tracks/mz-constants/paper/refs.bib` (unchanged) | 8810 | `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63` |
| `/tmp/padua-mz-response-paper/manuscript.pdf` | 510218 | `87bb1e486f52f080f74b229624620954240f98f2926538c2b178be076e11980c` |

Earlier 22/24/25-page receipts above identify their dated source versions; they are not current hashes. PDF timestamps and TeX version may change regenerated PDF bytes. The current source hash identifies this editorial response before later final-ID preparation.
