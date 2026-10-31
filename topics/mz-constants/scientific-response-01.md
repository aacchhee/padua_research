# Scientific response to audit-01 — M1, L1–L3, P4 and I3

Date: 2026-10-31. Developer: Codex scientific-response subagent, `gpt-6.1-sol` xhigh, explicitly assigned by the orchestrator; no separate runtime effort telemetry is exposed. Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, pinned by the orchestrator at `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994` and unchanged by the `bc85509` main integration. No Git operation was performed by this worker. The immutable [audit-01](audit-01.md) was not edited.

Owned scope: the 11 theory files and two paper files listed in the hash table, plus this response. The orchestrator owns the shared registries, report, LOG, crosswalk, source records, bibliography integration, final manifests, Git and PR. Audit M2 is a separate source-screen assignment; its threat-list text and citations are not supplied by this response. All existing theory statuses and scoped negative dispositions are preserved. No global ID is allocated. The added endpoint corollary is analytically PROVED in development under existing PD-T022 and requires focused independent re-audit; this document is a development response, not an acceptance record.

## Reading and novelty scope

Read the rules, audit-01 in full, all 21 current MZ theory records, the complete manuscript and README, complete `state/IDEAS.md` including the obstruction and disposition tables, `literature/INDEX.md`, and the full M3 candidate record. Searched `supersed`, `dominat`, `rho`, `degree-sensitive`, `mass floor`, `coefficient.floor`, and `endpoint corollary` across state, literature, MZ directions and theory. Closest entries: IDEA-062/063 (qualitative sign proof and floor alternative) and IDEA-073 (degree-sensitive refinement), with the endpoint upper-gap obstruction retained in PD-T027. The change is the explicit specialization of an existing proved inequality, not a new mechanism or a priority claim. No new candidate or historical exclusion is proposed; all earlier candidates and failures remain retained. The orchestrator will synchronize the IDEA-073/063 comparison outside this worker's file ownership.

## M1 — stronger endpoint statement and simplified B

Disposition: addressed in the owned sources; focused independent re-audit PENDING.

The original PD-T014 quantitative statement is preserved verbatim in its canonical file:

\[
0<Q_N(p^2)\le\left(2-\frac2{\pi N}\right)\int p^2<2\int p^2,
\quad 0\ne p\in\Pi_{N-1},\quad N\ge2.
\]

Its original sign proof and coefficient-floor quantitative argument remain valid. PD-T014 now identifies the strict qualitative statement as its frozen target and explicitly labels the floor-derived constant a quantitatively superseded alternative. PD-T015 retains its exact original mass inequality

\[
N^{-1}E\preceq M\preceq(\pi/2)E
\]

and its independent PROVED status, proof, and substantive supporting role. It is neither downgraded nor deleted when its application yields a weaker spectral constant.

The added **PD-T022 endpoint corollary** is

\[
\lambda_+(N,N-1)\le 1+(1-2/N)^2
=2-\frac4N+\frac4{N^2}<2\qquad(N\ge2).
\]

Derivation: PD-T022 gives \(\lambda_+(N,n)\le1+\rho_{N,n}\), with
\(\rho_{N,n}=\max\{2n/N-1,0\}^2\). At \(n=N-1\), \(1-2/N\ge0\), so
\(\rho_{N,N-1}=(1-2/N)^2\). For \(N=2\), \(2n=N\), \(\rho=0\), and exactness gives \(\lambda_+(2,1)=1\); the upper inequality is equality. For every \(N\ge3\), \(2n>N\), \(\rho>0\), and the existing strict case of PD-T022 gives a strict upper inequality. Thus the zero-rho case is not passed through a proof requiring positive rho.

For every \(N\ge2\),

\[
\frac4N-\frac4{N^2}>\frac2{\pi N},
\qquad 4-4/N\ge2>2/\pi.
\]

Moreover, for every integer \(0\le n<N\), monotonicity in \(n\) gives

\[
1+\rho_{N,n}\le1+\rho_{N,N-1}
=2-4/N+4/N^2<2-2/(\pi N).
\]

Therefore the original PD-T025 choice
\(B=\min\{2-2/(\pi N),1+\rho_{N,n}\}\) is identically
\(B=1+\rho_{N,n}\) for the entire stated range. PD-T025 and manuscript equation `Bcc` now state that simpler value and its justification. The CC application uses PD-T013 and PD-T022; PD-T014 is retained as a weaker alternative rather than an additional input needed for B.

Manuscript replacements: abstract and `main-upper` use \(2-4/N+4/N^2\); the leading upper theorem states the strengthened endpoint bound with the N=2 equality case; its proof keeps the independent qualitative sign argument and names its explicit forward dependency on the degree-sensitive theorem. A separate corollary after `thm:ratio-upper` proves the endpoint substitution, and a remark preserves the weaker floor-based proof and explains quantitative supersession. The degree-sensitive theorem's own proof directly repeats the sign argument and does not depend on the leading theorem, avoiding circular dependence. README scope and build guidance are synchronized. The orchestrator will update the report and registry headline outside this scope.

Affected claims: PD-T014 (original theorem unchanged, stronger corollary cross-reference added), PD-T015 (unchanged independent supporting theorem), PD-T022 (new explicit endpoint corollary under existing ID), PD-T025 (identical simplified B); no OPEN sharpening is promoted.

## L1 — unconditional Padua liminf

Disposition: addressed. In PD-T028, replaced

> liminf eta_Padua≥1 once the CC endpoint convergence is established

with the explicit unconditional consequence already proved in PD-T021: PD-T018 gives \(\lambda_-(N,N-1)\to0\), while compression gives
\(\eta_{\mathrm P}\ge\eta_{\mathrm{CC}}\ge1-\lambda_-(N,N-1)\), hence
\(\liminf\eta_{\mathrm P}\ge1\). Neither full CC defect convergence nor a Padua limsup is needed for that implication. PD-T028's universal positivity, upper-spectrum, endpoint-order and convergence targets remain OPEN.

## L2 — exact non-vacuity range and finite-table limits

Disposition: addressed. PD-T018 and the manuscript explicitly retain the witness-proof threshold \(\log N\ge128\), while stating

\[
\frac{128000}{(\log N)^2}<1
\quad\Longleftrightarrow\quad
\log N>\sqrt{128000}=357.770876399966\ldots.
\]

Thus the explicit comparison constant is vacuous over all computationally feasible full-spectrum calculations considered in this work. The threshold is given exactly rather than rounded to an inaccurate integer criterion. Saying it is vacuous for every mathematically computable integer N would be false, so the text describes feasible spectral computations. The finite tables do not exhibit or determine an asymptotic leading constant. No new fit, asymptotic extrapolation, data, or estimate of PD-T020's \(c_*\) is introduced. README includes the same scope limitation. PD-T018 remains PROVED and PD-T020 remains OPEN.

## L3 — full interpolation-space lower consequence

Disposition: addressed. The unchanged PD-T017 inequality holds on \(\Pi_N\), hence directly implies

\[
\lambda_-(N,N)\ge K_N^{-1},\qquad
\lambda_-(N,N-1)\ge\lambda_-(N,N)\ge K_N^{-1}.
\]

The canonical statement and manuscript now state both consequences. The previous consequent mentioned only degree N−1; History records that correction to presentation without changing the original inequality, proof or PROVED status.

## P4 — reciprocal semantic provenance

Disposition: addressed in the canonical theory headers, with IDs and clickable links:

| Relationship | Clarified meaning |
|---|---|
| PD-T019 ↔ PD-T018 | Separation of the original endpoint discussion into different witnesses; PD-T018 is not a proof dependency or a conjunct/case of PD-T019's exact norm identity |
| PD-T019 ↔ PD-N004 | Separate finite negative claim using PD-T019 as its proof dependency; not a decomposition of the norm identity |
| PD-T027 ↔ PD-T014 | Related target/support separation from the original M1 discussion; the qualitative threshold is not a proved part of the sharp-limit/uniform-gap statement |
| PD-T028 ↔ PD-T021 | Related target/support separation from the original M4 discussion; marginal compression is not a proved conjunct/case of the genuine two-dimensional targets |
| PD-T014 ↔ PD-T015 | Independently retained supporting mass inequality split from the quantitative proof, not a part of the spectral target's own statement |

No standalone original-target ID was invented. The links retain historical split provenance without implying a PARTIAL decomposition where there is only supporting information. Each edited file's History states that the original mathematical statement and status are preserved. The orchestrator owns the crosswalk/registry synchronization.

## I3 — odd/even marginal degrees

Disposition: addressed. The manuscript's separately checked Padua degrees 10, 20 and 31 now carry the parenthesis “covering odd and even degrees.” The distinct spectrum-table degrees remain 10, 20, 30 and 40; no measurement was changed or rerun.

## Executed checks, preserved artifacts and runs needed

Executed in `/workspace/padua_research`, Python 3.12.14:

```sh
python tracks/mz-constants/code/m3_exact_check.py --max-n 25
```

Result: `EXACT: 324 pairs, 2<=N<=25, 0<=n<N: PASS`; filter plateau, cutoff, no-alias reproduction, upper Z signs and ratio bound. Executed checker SHA-256: `246bd4b95226182b0231730d7ad6ae6d7716623d31b28193c0e44d932825d2dd`.

An additional inline Python/Fraction diagnostic checked the endpoint identity and domination using the stronger rational comparison \(2-2/(3N)\) (with \(\pi>3\)), plus monotonicity over every \(0\le n<N\), for \(2\le N\le1000\): 500499 degree pairs, all passed. The same inline run found 68 unique TeX labels, 49 reference occurrences and no undefined labels, checked all 11 newly explicit local Markdown theory links, and confirmed the assigned PROVED/OPEN statuses. Output is retained under ignored `local-output/mz-constants/scientific-response-01/checks.json`. These are finite diagnostics and source-consistency checks by the developer, not an independent audit or an all-N computational proof. The universal corollary and dominance are established by the analytic substitutions above. No numerical spectrum or fitted law was newly calculated.

Before any source edit, the existing original v1 PDF, source, bibliography, README and original build manifest were copied to ignored `local-output/mz-constants/paper-v1-preserved/`. PDF SHA-256: `a594ea305fc0f91bb3a2c49d9c6311288440fcffa6eb9e1e95177748d34d3155`; size: 419412 bytes. The ignored `preservation-manifest.json` records every original/copied identity. This preserves the original PDF and its hash outside Git without overwriting its original build manifest or source-record hashes. External cold-storage delivery remains the orchestrator's pending task.

Runs needed: integrate the separate M2 literature text/citations; compile the integrated response with the README's `pdflatex`, `bibtex`, `pdflatex` twice sequence into distinct ignored `local-output/mz-constants/paper-response-01/`; inspect logs and relevant pages; refresh final response manifests; focused independent re-audit of PD-T022's endpoint specialization, the strengthened manuscript translation, the B simplification, and the listed editorial/provenance changes. No response-01 PDF build or independent re-audit is claimed by this worker.

## Scientific-completion file hashes

These are the exact scientific worker completion snapshot, before any subsequent orchestrator M2 manuscript edit or final build. The ignored `completion-hashes.json` also records the full before/after SHA-256 and sizes, and `scientific-completion-snapshot/` retains these source bytes for inspection. The final integrated audit handoff must pin the later integrated bytes if the orchestrator changes these files. This response's own identity is provided in the worker handoff to avoid a self-referential hash.

Snapshot UTC: `2026-10-31T21:49:24.844357+00:00`.

| File | Completion SHA-256 | Bytes |
|---|---|---:|
| `tracks/mz-constants/theory/m1-upper-bound.md` | `b315927af335c8894afcb588616879fdb7d73ee1da30ad1946baed3c39e3f93a` | 6816 |
| `tracks/mz-constants/theory/m1-coefficient-floor.md` | `5de9b57e78e315a0686aa5cd39a99ee469756b9c093e994f6a7dea544929920f` | 4236 |
| `tracks/mz-constants/theory/m2-cardinal-lower.md` | `1c9a3bf5fe8bb9dfbb2943500fb7aafd092eb8a5892c43a2e292f117fabf7776` | 6899 |
| `tracks/mz-constants/theory/m2-parity-upper.md` | `1897c95812140a7c8fbdd8331923014cb871be5d628977d1f0f942fce43af827` | 7359 |
| `tracks/mz-constants/theory/m2-u-witness.md` | `8d43f94f191dba8b6f600a06e190fd24e274cd273ec536b1e2369ae7160f5678` | 4130 |
| `tracks/mz-constants/theory/m2-eta-counterexample.md` | `eb5f6b7ad392401427c1f0e70453f26a0da890c77b1e697f448a964651c6afec` | 4522 |
| `tracks/mz-constants/theory/m2-padua-marginal.md` | `44de243749883d44d54a7ac33dca69450d8777aec035b740766bd1936d437497` | 6993 |
| `tracks/mz-constants/theory/m3-upper-ratio.md` | `dd8512d6041ecba85ebf9de564e48ffff48f26e0c9c770c53741125c2e0e34ba` | 5504 |
| `tracks/mz-constants/theory/m3-hyperinterpolation.md` | `586a8d2304e7ce48277c1786b36bcd9b5f51fa4f467128ad414b7322882416d2` | 5688 |
| `tracks/mz-constants/theory/open-upper-limit.md` | `3a9b96df7a21995b986ea08271e9fa1bface2a1fd300029665a1462e95125c7c` | 3324 |
| `tracks/mz-constants/theory/open-padua-target.md` | `3ab82f62455fec55436a3f087914c8fbd1bc0b68066494e0424a3be1975f4c66` | 3654 |
| `tracks/mz-constants/paper/manuscript.tex` | `c769b3993af30c89fd6dea86d9ca91acf1d53c48820a5c3b3153cc4c28bb692a` | 41584 |
| `tracks/mz-constants/paper/README.md` | `567ea876bfad141c8d433a6bd8154c5da98b288c99cde13497941aebf904c71c` | 7910 |
