# Response 01 — MZ audit findings and batch reconciliation

Audit answered: [audit-01.md](audit-01.md), delivered at `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`; originally audited candidate `fdf0648cbaa9fb722c611d709e638de7dfe86368`. The auditor's report and evidence are unchanged. Developer: Codex orchestrator; AC requested gpt-6.1-sol xhigh and root runtime model/effort metadata is not separately exposed. Scientific edits were assigned explicitly to gpt-6.1-sol xhigh, targeted literature to gpt-6.1-sol high, and supplementary focused review to gpt-6-astra high.

Rules read at the audit-delivery head above, unchanged by main integration. AC's priority is binding: charter first, MZ second. AC merged PR #2 into main at `08fafe62d9798385dfafaacc9a41344272737e68`; this branch merged that main in `bc85509adc303126c6d8276a4457393e81d7f394`. All 105 charter track/topic files and every accepted charter ID were preserved. This response imports no programme rule amendment and changes no rule, template or repository setting.

**Disposition:** all M1, M2, L1–L3 and P1–P6 requests are addressed below; P7 is acknowledged with formatting and readiness wording corrected. The original mathematical statements remain PROVED, MEASURED or OPEN exactly as audited. M1 adds an explicit corollary and needs focused Claude re-audit; the supplementary Astra review does not replace that requirement. The PR remains draft and returns to AUDIT when this response package is pinned. No merge is performed or requested before that focused acceptance.

## M1 — use the stronger endpoint corollary

**Addressed; material corollary exposed, focused re-audit required.** PD-T022 already gives lambda_plus(N,n)≤1+max(2n/N−1,0)². At n=N−1 this is

\[
\lambda_+(N,N-1)\le 2-\frac4N+\frac4{N^2}<2,\qquad N\ge2.
\]

At N=2 exactness gives equality with one; for N≥3 the first inequality is strict. Its gap exceeds the old 2/(πN) gap because 4−4/N≥2>2/π. Monotonicity in n proves that the min in PD-T025 selects 1+rho for every n<N, so B is simplified accordingly.

The abstract, leading inequality/theorem, report ranking, manuscript application and README now use the stronger endpoint constant and identify its dependency on PD-T022. The degree-sensitive proof uses PD-T013 directly, so the leading manuscript theorem's forward reference is not circular. PD-T014 keeps its independent short qualitative proof and its original weaker quantitative statement/proof as a valid, explicitly superseded alternative. PD-T015 remains a substantive independent PROVED mass inequality and supporting alternative; being quantitatively dominated is neither a theorem refutation nor a reason to downgrade it. The IDEA-063/073 comparison is explicit in both direction records and the current idea table. No new PD or IDEA ID is allocated.

Exact source-level changes and development checks are recorded in [scientific-response-01.md](scientific-response-01.md). The new bound does not establish a uniform endpoint gap independent of N or a sharp limit; PD-T027 stays OPEN.

## M2 — screen the missing mean-convergence/converse-MZ family

**Addressed by an actual targeted screen and an explicit named unresolved disposition.** Twenty additional literal queries and source/access outcomes are in [M0](literature-search.md); [source record](../../literature/records/mz-mean-convergence-screen.md) and [literature response](literature-response-01.md) record Erdős–Feldheim 1936, Askey 1972 and its 1969 report, Nevai III 1984 with the 1990 addendum, Lubinsky paper147, Smith's explicit Lobatto theorem, and Mastroianni–Russo/Xu follow-ups.

Selected original text was reached for Erdős–Feldheim, Askey's earlier report, Lubinsky and Smith. Lubinsky's converse inequalities have the relevant general form, but the CC nodal-coefficient and critical-logarithmic specialization was not established. Smith's inspected Lobatto theorem has a different continuous weight and input norm. Nevai's exact theorem/addendum and the corrected Askey journal body remain pending-reference. Follow-ups are bibliography-level pointers, not inherited theorems. The manuscript names this family and the precise node, endpoint-weight, norm and borderline-rate translations still required. Neither overlap nor its exclusion has been proved; the permitted wording remains “self-contained proof”, with novelty unresolved.

The allocation owner openly reserves LIT-061–065 for these five groups after the merged charter's first block and MZ's original block. The original 65 mappings are unchanged. There are now 24 MZ source entries, 65 combined literature IDs and 70 MZ provisional-to-final mappings. The next unreserved literature ID is LIT-066; no competing member reservation is overwritten.

## L1 — unconditional Padua liminf

**Addressed.** PD-T028 now states the already established liminf eta_Padua≥1 consequence unconditionally through PD-T021 and PD-T018. The remaining full signed-Padua targets stay OPEN. No limsup, positivity or two-dimensional upper bound is inferred from compression.

## L2 — explicit non-vacuity and finite-data interpretation

**Addressed with an exact threshold.** PD-T018 and the manuscript state that 128000/(log N)² improves the trivial bound one only when log N>sqrt(128000)≈357.7709, although its witness proof starts at log N≥128. The explicit comparison constant is therefore vacuous throughout all feasible reproduced spectra; “all computable N” would be too strong as a literal mathematical statement. The finite table does not reveal the asymptotic leading coefficient. No shifted-log fit is promoted to a limit estimate, and no new fit result is added to PD-T020.

## L3 — full interpolation-space lower consequence

**Addressed.** PD-T017 and the manuscript now state lambda_min(CC,N)≥1/K_N explicitly; restriction also gives the degree-N−1 consequence. The original all-polynomial inequality already quantified over Π_N, so this states the full consequence without altering its proof or degree hypotheses. The full-space formulation is also used in the new mean-convergence source comparison.

## P1 — one owner, one ledger, actual propagation

**Addressed.** The merged charter's already reconciled ledger has first priority. The [successor shared ledger](../padua-batch-20261031/ALLOCATIONS.md) has one fixed owner, the root Codex MZ orchestrator, and records all four topics, charter first / MZ second, the remaining order for AC, every preserved reservation, and the five explicit MZ literature additions. The older rotating-owner proposal is superseded.

Published ledger-only propagation, by normal non-force commits:

| Active member | Published ledger commit | Scope |
|---|---|---|
| MZ | b56c7d65520b4c9a1311342de19fb47c9ba1d8f1 | Reconciled owner/order and reservations |
| programme-ideas | c989031bacb3d35c711f4ace40a10e8909802106 | Only topics/padua-batch-20261031/ALLOCATIONS.md |
| bivariate-Lanczos | 48f7a02697d7753279e27d3ad462a4817c67ade0 | Only the same ledger path |

All three ledger files have blob `43c581fb242fd28ebe4d89ee4a42e3bbd660a159`, SHA-256 `39dfc9a9abcffcc7e8d28caf0c537a9dcf4536b42186cc00991ee67b33516f56`. [Reconciliation receipt](ledger-reconciliation-01.json) pins before/after heads and proves the two Claude-member commits changed no other path. Their science, source records and rules were not imported or edited. The already merged/deleted charter branch is not retroactively rewritten: its accepted block is preserved, and the successor ledger reaches main only if AC merges MZ next. No main push, force-push or PR merge occurred.

Next free IDs are PD-T029, PD-N007, LIT-066 and IDEA-077. The originally requested next-free LIT-061 was consumed transparently by this audit's five new source records; all other prior next-free values are unchanged. Future reservations on either Claude member require this owner's reconciliation.

## P2 — explicit dependencies and mathematical parts

**Addressed.** Every MZ PROOF_STATUS row lists its actual IDs or elementary/no-result dependencies and its actual proved, measured or open mathematical parts. This includes PD-T014's qualitative/alternative/corollary roles, PD-T024→PD-T022/023, PD-T021's distinct PD-T018 and PD-N004 consequences, and the limited weight-only uses of PD-T017. Supporting background in OPEN rows is not presented as a proof of their targets. The 13 accepted charter rows are preserved verbatim.

## P3 — current dispositions in both registries

**Addressed.** PROOF_STATUS names IDEA-060 REJECTED: refuted (PD-N002), IDEA-061 REJECTED: failed (PD-N003), IDEA-068 REJECTED: refuted (PD-N004), IDEA-069 REJECTED: failed (PD-N005), and IDEA-070 REJECTED: failed (PD-N006), each with a canonical link and precise scope. The negative theorem itself remains PROVED; the rejected object is the specified mechanism or assertion.

state/IDEAS.md has an explicit current table for all IDEA-052–076, superseding the retained historical seed table. Successful M1/M2/M3 seeds are developed, the manuscript gate is met, and M4/M5/M6 deferred targets remain explicit. For IDEA-064/067/072, “equivalent” is expressly an IDEA disposition relative to the supplied mechanism; the separately proved fact is retained. No PD-N is created for equivalence and no candidate is removed.

## P4 — reciprocal links with correct semantics

**Addressed.** PD-T019, PD-T018 and PD-N004 now reciprocate the prototype-extension/finite-consequence links. PD-T015 names PD-T014 as its development parent while remaining logically independent of that theorem. PD-T027↔PD-T014 and PD-T028↔PD-T021 use IDs and canonical links. The crosswalk distinguishes developmental separation and supporting information from a decomposition of a theorem's own statement; no false PARTIAL classification or circular logical dependency is introduced.

## P5 — preserve registry policy and one authority

**Addressed.** The four original PROOF_STATUS policy paragraphs are restored verbatim, including the exact `REJECTED: refuted (see PD-Nnnn)` convention, the dependency/disposition warning, measured-record requirement and substantive-splitting rules. PROOF_STATUS, ID_CROSSWALK and the idea registry identify the shared batch ledger as authoritative. The charter member ledger is retained only as its first-block historical provenance, not a second allocator. No workflow, agent, template or scientific status rule changes.

## P6 — refreshed main/charter pins and actual integration

**Addressed.** Current charter provenance is head `317a26597dedc9adc9cfc6a26fa00078df7d29e4`, merged main `08fafe62d9798385dfafaacc9a41344272737e68`; the full main-into-MZ merge SHA is recorded above. final-id-map.json preserves the original eb7bdcd pin under an explicit historical key and refreshes the current source. LOG no longer claims that no IDs are reserved. Historical rehearsal objects remain provenance, and the canonical rehearsal is refreshed against the actual merged charter main and current response. Its source SHA/conflicts/semantic checks and repair-patch identity are recorded in batch-rehearsal.json and integration-impact.md.

## P7 and informational notes

**Formatting addressed:** glued hashes, numbers and words in the touched integration/idea summaries are separated for safe copying. **Readiness wording:** after focused acceptance, the concrete decision requested from AC is to review and squash-merge PR #3 next, preserving the already merged charter; no all-batch or automatic merge is requested. At this response handoff the PR remains draft for the focused re-audit. The cold-storage SHA-256/base-SHA convention remains explicitly documented, as audit P7 permits; no Windows delivery is invented.

I1/I2 are acknowledged: Claude independently reproduced the numerical evidence and checked An–Wu's primary conditional wording. I3 is addressed by identifying the odd/even marginal construction degrees. I4 needs no rewrite of historical pending-review wording beyond the dated review/response context. No original audit report was edited to resolve a finding.

## Verification and focused handoff

- Scientific developer executed the unchanged M3 checker: all 324 (N,n) pairs pass. Its exact scalar specialization/dominance diagnostic covered 500,499 degree pairs; the all-N conclusion uses the written algebraic proof, not that finite test.
- The supplementary Astra high reviewer independently executed bounded exact checks, checked the all-N reasoning and independently read the two live ledger APIs/commits. Its final report and exact file hashes are linked in independent-response-01.md; it does not replace Claude's focused re-audit.
- Integrated manuscript build executed pdflatex, BibTeX and two further pdflatex passes into the separate paper-response-01 destination. Result: 15 A4 pages; no final LaTeX/BibTeX warning, undefined reference, overfull or underfull box. Original v1 PDF/source identities are preserved separately; current build hashes are in paper/README.md.
- Current registry, historical-manifest identity, accepted-charter preservation, ledger propagation, source/producer immutability and fresh rehearsal checks are recorded in response-01-checks.json. Current response hashes are pinned in response-01-targets.json; audit-targets.json remains the historical fdf0648 scope, not a falsely refreshed old audit.

Focused Claude scope: the added endpoint specialization and its manuscript translation/classification, the L1–L3 clarifications, named M2 source coverage, actual P1 propagation/priority and P2–P6 registry metadata/merge preservation. The already accepted unchanged proofs and unchanged numerical producer code need not be redeveloped. Independent audit-01 remains immutable. Sharp constants, novelty/fulltext gaps and the full 2D target remain unresolved; only AC merges.

Next: `Claude (Opus 5.5 xhigh): Continue codex/mz-constants-20261031; focused re-audit response-01.md.`
