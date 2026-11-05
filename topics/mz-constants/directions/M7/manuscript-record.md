# M7 manuscript development and readiness

Date: 2026-10-31. Role: Codex manuscript developer; inherited runtime model/effort metadata is not exposed to this worker. Ownership: `tracks/mz-constants/paper/` and this record only, plus ignored local compilation artifacts. No Git mutation or shared-registry edit was performed.

Rules were read at branch-head commit `2dc9264333cdf8372947448f4b9bdd3bb577d0e1` on `codex/mz-constants-20261031`: `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. A read-only diff confirmed these rules are unchanged from the campaign rule/base commit `d36722823441dc40c6e19d69a174459348dd309c`.

## Gate, source scope, and novelty boundary

The orchestrator explicitly activated M7 after independent Astra accepted the analytic M1/M2/M3 results and recorded their scoped prior-art dispositions. The complete independent report's final disposition table supplies that scientific prerequisite. This permits a complete development draft; it does not clear historical novelty or complete the required Claude handoff.

Before synthesis the developer read the complete 160-line seeded `state/IDEAS.md`, including every M0–M7 heading, aliases, full entries, and both obstruction/disposition tables; `literature/INDEX.md`; all ten `literature/records/mz-*.md` files; the complete M0 `literature-search.md`; the scientific theory records used below; and the bounded reproduction and independent audit records. Searches covered cardinal, harmonic, Fejér, sign, Z-matrix, logarithmic squared, eta, and marginal terms across the registry, theory, topics, and literature. This task synthesizes those existing mechanisms and proposes no new candidate or priority claim. Final identifiers come solely from `topics/mz-constants/final-id-map.json`; the orchestrator owns allocation and canonical replacements.

Source scope includes the M1 foundation, coefficient floor, upper threshold and full-degree obstruction; both M2 endpoint proofs, the U identity/counterexample, Padua compression and retained OPEN sharpenings; M3 upper/lower fixed-ratio estimates, eta assembly and hyperinterpolation; and the MEASURED reproduction record. Historical SS1978/80, interpolation-book, LMN/MT/survey, and Widom full texts remain pending-reference. The manuscript's ASV source context uses selected recorded primary coverage and separately attributes the already-known upper-MZ hyperinterpolation mechanism; it does not infer an exclusion from inaccessible literature. No third-party full text or private C4 text was copied, and no private theorem is a proof dependency.

## Completed deliverables

- `tracks/mz-constants/paper/manuscript.tex`: complete 14-page proof draft, not an outline.
- `tracks/mz-constants/paper/refs.bib`: twelve cited sources using only final LIT identifiers; source-reading limits are visible in the notes.
- `tracks/mz-constants/paper/README.md`: build instructions, claim scope, evidence links, limitations, and review handoff.
- Ignored `local-output/mz-constants/paper/manuscript.pdf`: local review artifact, not added to Git. External archival remains pending AC's chosen Padua-specific destination.

The manuscript gives full proofs of the off-diagonal sign/absolute-coefficient comparison, quantitative coefficient floor, cardinal-cell weighted Schur lower bound, degree- and parity-compatible harmonic-U upper bound, filtered Fejér weighted Schur fixed-ratio estimate, exact N=512 counterexample, positive-rule hyperinterpolation application, and signed-weight-safe Padua compression. It retains the exact CC parity ADE and keeps node index, exactness degree and point count distinct.

The conclusions are deliberately scoped: CC eta tends to one and its condition number has logarithmic squared order, but no rate of that order for `1−eta` and no eventual binding side are claimed. The leading endpoint constant and sharp upper limit/uniform endpoint gap remain OPEN. The Padua conclusion is only a liminf lower bound; signed two-dimensional positivity, upper spectrum, lower asymptotics and eta convergence remain OPEN. The An–Wu finite applicability counterexample does not dispute the validity of the source's conditional theorem. The ordinary hyperinterpolant is kept distinct from inverse-Gram least squares.

## Exact compilation and verification

All compilation ran from `/workspace/padua_research` on 2026-10-31. The full sequence executed successfully:

```sh
mkdir -p tracks/mz-constants/paper local-output/mz-constants/paper
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex
BIBINPUTS=tracks/mz-constants/paper: bibtex local-output/mz-constants/paper/manuscript
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass2.txt
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass3.txt
```

An incremental fourth LaTeX pass applied wording/PDF metadata. BibTeX was rerun after narrowing its ASV coverage note to equations (7)–(8), followed by LaTeX passes 5 and 6. Two final reviewer-suggested clarity edits specified positive amplitudes for the alternating-data obstruction and described the *guaranteed* upper-bound gap, then LaTeX passes 7 and 8 executed:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass7.txt
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass8.txt
```

Versions actually queried: pdfTeX 3.141592653-2.6-1.40.26, BibTeX 0.99d, TeX Live 2025/dev/Debian, kpathsea 6.4.0/dev. `pdfinfo` reports 14 A4 pages. Final LaTeX and BibTeX logs have **zero** `Warning`, `Overfull`, `Underfull`, `undefined`, or leading-`!` error markers. Initial first-pass unresolved references were resolved by BibTeX and repeat LaTeX; no warning remains in the final pass.

Pages 1 and 9 were rendered by the commands below and visually inspected before the small final wording/metadata edits. The final pass was checked through its clean log.

```sh
pdftoppm -f 1 -l 1 -scale-to 1500 -png -singlefile local-output/mz-constants/paper/manuscript.pdf local-output/mz-constants/paper/page-01
pdftoppm -f 9 -l 9 -scale-to 1500 -png -singlefile local-output/mz-constants/paper/manuscript.pdf local-output/mz-constants/paper/page-09
pdftotext -layout local-output/mz-constants/paper/manuscript.pdf local-output/mz-constants/paper/manuscript.txt
```

A Python validation found no provisional identifiers and no final PD/LIT identifier outside the allocation map. All six CC and four Padua table rows were parsed from the LaTeX and checked against the existing reproduction JSON: maximum absolute rounding discrepancy `4.673308962033218e-10`, below `5.1e-10`; Padua degree and negative-weight counts matched. This is a transcription check, not a new spectral run. Its ignored output is `local-output/mz-constants/paper/table-transcription-check.json`.

The manuscript developer reviewed the recorded finite outputs but did not rerun the numerical suite. Actual separate replay belongs to the independent Astra report. The source tables remain MEASURED, and none of the analytic proofs depends on a float64 finite check.

## Final development pin

Hashes and byte counts below identify the stable manuscript input and the local PDF produced at 2026-10-31T21:10:03 UTC. The ignored `local-output/mz-constants/paper/build-manifest.json` also records log hashes and validation results. PDF timestamps/output identifiers can change its bytes on recompilation; retained TeX/BibTeX hashes identify the draft itself.

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| `tracks/mz-constants/paper/manuscript.tex` | `072ae4e52c2cea78f2ec13f6e48a3d9529234af6c99d7b747a40c44c31f08c7c` | 39310 |
| `tracks/mz-constants/paper/refs.bib` | `f2f4eb04dec45003a107deac7c91b2f0d4737e2707289d359fd3d0194aeb9bf8` | 4433 |
| `tracks/mz-constants/paper/README.md` | `f433fc6f10b3e0da3bdfec1da80e6e5a177b0967cf6802ec7e1b8217de2512d7` | 6491 |
| `local-output/mz-constants/paper/manuscript.pdf` | `a594ea305fc0f91bb3a2c49d9c6311288440fcffa6eb9e1e95177748d34d3155` | 419412 |

## Readiness and remaining work

M7 development is **COMPLETE**. The earlier independent scientific review accepted M1/M2/M3 analytic validity and recorded actual replays; it does not automatically audit the manuscript's translation. The manuscript's final pinned impact review is requested separately. Required Claude cross-provider audit is **PENDING**, historical novelty is **unresolved**, and the manuscript is **not for submission**. A draft PR may preserve the work with these limits; submission, final authorship, venue, merging, and archival destination are AC's decisions. No submission readiness or audit approval is conferred by this development record.

## 2026-11-05 — signed Padua manuscript integration, accepted-result pass

Codex manuscript subagent, inherited user-requested gpt-6.1-sol xhigh (runtime metadata not independently exposed), on `codex/padua-mz-cleanup-20261105`. Rules/input `ad503cb0603fc017444b0aa732240981eefa4d24`, base/main `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`. No Git operations or shared-registry edits by the worker.

This append-only entry supersedes the historical description of unresolved signed-Padua conjectures for the current draft. Section6 retains the original compression and adds complete analytic proofs of the accepted even-m boundary-weight theorem PD-T295, negative and positive carriers PD-N105/106, sharp ratio threshold PD-N107, and all-m direct signed coefficient norm PD-T297. Section7 adds exact m60/m80 computer-assisted illustrations PD-T298/299 with their inertia reduction and computational trust. The abstract, introduction and open-problem list now agree; AC's OPEN labels on rejected targets remain distinguished from their binding refuted dispositions. No new C1/C2/C3 claim is introduced in this pass. No new external source or historical priority claim is added; bibliography is unchanged; no unmerged PR21 source is cited.

The worker executed pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX in `/tmp/padua-mz-cleanup-paper`, producing22 A4 pages with zero final warning, undefined-reference, overfull/underfull or error markers. Page16 was rendered and visually inspected. Source contains no provisional IDs; `git diff --check` passed. No numerical experiment was rerun. Earlier preserved v1 and response-01 products were not touched. The PDF stays uncommitted scratch, not delivered cold storage. Commands, statement mapping and exact source/PDF identities are recorded in [cleanup manuscript changes](../../../padua-mz-cleanup-20261105/manuscript-changes.md). Independent review of the new manuscript translation remains pending.

### 2026-11-05 — cleanup-result extension of the manuscript

At the orchestrator's request after the accepted-result pass, the same Codex manuscript worker (inherited user-requested gpt-6.1-sol xhigh, runtime metadata not independently exposed) integrated the new odd-degree weight proof and even-y-mesh carriers, completing the all-integer spectral/ratio classification. A separate proposition proves exact carrier norm limits and one-sided normalized logarithmic spectral bounds, with the raw-energy versus spectral normalization caveat. Section7 includes the m1600 dyadic finite witness and its rational trial-Rayleigh interval, producer/checker reduction, explicit computational assumptions, and pending Claude audit. No m1240 claim is included in this pass. Only source-path comments identify new results until final-ID preparation; no provisional IDs or new literature claim was inserted.

The worker read the full new theory files and actual m1600 producer/independent receipts and source; it did not execute the certificate or spectrum calculations. Incremental pdfLaTeX twice produced24 A4 pages, zero final warning/error/undefined-reference/overfull/underfull markers. Page22 was rendered and visually checked. Earlier source/PDF hashes remain historical. The current receipt and source mapping are appended to [cleanup manuscript changes](../../../padua-mz-cleanup-20261105/manuscript-changes.md). Build output stays `/tmp/padua-mz-cleanup-paper`; preserved v1 and response-01 artifacts remain untouched, no PDF committed and no archival delivery claimed. New mathematics and manuscript translation await the required Claude audit.

The final current cleanup pass extends the finite proposition to the independently accepted m1101 and m1240 witnesses, retaining m1600; exact rational intervals bound trial quotients, not eigenvalues. The text states only1240 is the smallest even degree certified negative in this campaign. It makes no lower-degree positivity or first-crossing claim. The worker inspected the committed finite theory and actual additional receipts after root confirmed all acceptances. Final incremental build:25 A4 pages, zero warnings/errors/undefined-reference/overfull/underfull markers; final page22 visually checked. Final hashes are appended to the cleanup manuscript-change record, preserving earlier22/24-page hashes as historical. No Git operation, numerical rerun, PDF commit or archival-delivery claim by this worker.

## 2026-11-05 — cleanup audit response F12–F16

Codex manuscript-response worker, inherited user-requested gpt-6.1-sol xhigh (runtime metadata not independently exposed), at response input `a64ef35`. Cleanup Claude audit-01 accepted the mathematical and manuscript-translation scopes. This response changes wording/status metadata only: small committed receipts are distinguished from separately staged witness arrays and exact norms with delivery pending; Padua tables use the eigenvalues of their own Gram matrix; the trust text names FLINT exact integers/rationals alongside Arb and the alternate IEEE/BLAS model; the intermediate 24-page source is labelled uncommitted scratch; touched prose spacing is repaired. Earlier dated entries are preserved under this record's append-only rule, including their historical pending wording. No proof, claim, scientific status, bibliography, certificate or numerical code/data is changed.

The worker executed pdfLaTeX, BibTeX and repeat pdfLaTeX in `/tmp/padua-mz-response-paper`; the current build has 25 A4 pages and zero final warning/error/undefined-reference/overfull/underfull markers. Page 22 was rendered and visually checked. No provisional IDs occur. Current TeX SHA-256 `9e10c6353fd625807bfca98fc1f868f1db37cc1eaea89c66751cfbd27c4ba28d`; PDF SHA-256 `87bb1e486f52f080f74b229624620954240f98f2926538c2b178be076e11980c` (510218 bytes). Full build receipt is appended to [cleanup manuscript changes](../../../padua-mz-cleanup-20261105/manuscript-changes.md). Build products remain scratch; no numerical rerun, Git mutation, PDF commit or archival delivery was performed by this worker. Final-ID/PR preparation and submission remain separate decisions.

## 2026-11-05 — cleanup final-ID preparation

Codex manuscript-preparation worker, inherited user-requested gpt-6.1-sol xhigh (runtime serving metadata not independently exposed), rules/input `a930f32fbf4568fbc431ddcf0b0fd689f5fa8201`. After the orchestrator's live allocation-union check passed, seven comment-line edits identify PD-T376 finite witnesses, PD-T377 odd weights, PD-T378 odd carriers, PD-T379 normalized one-sided growth bounds, PD-T380 companion MEASURED campaign record, and PD-T381 OPEN sharp-growth target. The companion's extra 23 measured rows are not reproduced in the manuscript. Five comments are replaced and two inserted; no executable TeX, mathematics, hypotheses, numerical values, labels, bibliography or citation set changed. The exact reversible diff is recorded in [cleanup manuscript changes](../../../padua-mz-cleanup-20261105/manuscript-changes.md). Comment-stripped source bytes and layout-preserving PDF text match the audited response exactly. All earlier entries remain historical and unchanged under the append-only rule.

Executed a fresh pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX build in `/tmp/padua-mz-preparation-paper`: 25 A4 pages, zero final warning/error, undefined-reference/citation or overfull/underfull messages; no provisional source IDs. Source SHA-256 `75067c43ce96e825b2a7cc81589ad5a7b1aa4728ab5848939ed21b3433aad0b3` (73673 bytes); PDF SHA-256 `225356bdb1fde444932f14f544998afd65d20f179a113a3b24cdb563e3b33091` (510218 bytes). Bibliography remains SHA-256 `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63` (8810 bytes). No numerical/certificate rerun or fresh visual inspection is claimed. Products stay scratch, earlier preserved artifacts are untouched, and no Git operation, PDF commit or external delivery was performed by this worker. Cleanup Claude audit-01 accepted the scientific and translation scopes; response-01 completed the nonmaterial dispositions. **Preparation checks pending**: PR readiness waits for the orchestrator's checks, with merge/submission and historical-priority decisions remaining separate.

### 2026-11-05 — cleanup readiness metadata

The final-ID manuscript source/build above is unchanged. All nine refreshed-head
integration rehearsals and the distinct Astra medium protocol review passed;
PR26 is prepared for AC review after accepted Claude audit-01 and response-01.
Assigned agent work is complete. Only AC merges; physical Padua cold-storage
delivery remains pending, and no submission or novelty clearance is claimed.
