# Second proof campaign — development report

Stage: **AUDIT**. Required Claude Opus5.5 xhigh audit: **PENDING**. Supplementary Codex reconstruction and executions do not replace it.

Branch: `codex/padua-proof-attempts-2-20261101`; [draft PR12](https://github.com/aacchhee/padua_research/pull/12). The exact scientific output candidate is named in the following numbered `handoffs/02-audit.md` publication.

## Outcomes

| Target | Result at its stop | Durable proof |
|---|---|---|
| A2 | PROVED for all n≥2: requested b coefficient, absolute remainder≤68 | [03](theory/proof-attempts-2-codex-03-corner-log-coefficient.md); support01/02/04 |
| A5 | PARTIAL by degree: complete counts/global theorems n3–7; n8 has at least44interior maxima | [attempt](attempts/T-A5.md); [lower bound64](theory/proof-attempts-2-codex-64-degree-eight-interior-lower-bound.md) |
| A4(a) | PROVED for the precise central-edge envelope: R_cen=Λ_c−g+o(1), both parities,0.548504986190<g<0.548525055355 | [all-edge70](theory/proof-attempts-2-codex-70-all-edge-kernel-formula.md); [envelope77](theory/proof-attempts-2-codex-77-central-edge-envelope-expansion.md) |
| B3 | REFUTED specified S(α): genuine positive sections at fixed n1,p1/10,M4 give n_box1/2 versus valid referencecount1 | [negative01](theory/proof-attempts-2-codex-N01-computed-section-box-count.md); support80/negative02 |
| B1 | PROVED generic exterior Ldiag offsets for every fixed admissible sample/finiteT; literal source taper except finitely many parameters | [detector90](theory/proof-attempts-2-codex-90-pole-topform-detection.md); [class92](theory/proof-attempts-2-codex-92-generic-ldiag-constrained-window.md); [taper93](theory/proof-attempts-2-codex-93-source-ldiag-taper.md) |

The central envelope maximizes on both vertical edges with free angle satisfying `|t−π/2|≤π/(n+1)`. A globally selected competitor or the historical finite search is not identified with it. Full-square A4(b)/(c) remain open.

## Certified strict maxima

| n | Interior | Open edges | Non-node corners | Closed-square total | Count / global proof |
|---|---:|---:|---:|---:|---|
|3|7|6|2|15|[06](theory/proof-attempts-2-codex-06-degree-three-maxima-count.md) / [07](theory/proof-attempts-2-codex-07-degree-three-global-argmax.md)|
|4|13|12|2|27|[10](theory/proof-attempts-2-codex-10-degree-four-maxima-count.md) / [11](theory/proof-attempts-2-codex-11-degree-four-global-argmax.md)|
|5|14|9|2|25|[16](theory/proof-attempts-2-codex-16-degree-five-maxima-count.md) / [17](theory/proof-attempts-2-codex-17-degree-five-global-argmax.md)|
|6|25|14|2|41|[41](theory/proof-attempts-2-codex-41-degree-six-maxima-count.md) / [42](theory/proof-attempts-2-codex-42-degree-six-global-argmax.md)|
|7|33|15|2|50|[51](theory/proof-attempts-2-codex-51-degree-seven-maxima-count.md) / [52](theory/proof-attempts-2-codex-52-degree-seven-global-argmax.md)|

At n=8, **at least44 distinct strict interior maxima** are proved; exact interior65, closed-square61 and global62 remain **OPEN**. Both complete interior checks reached the A5 deadline without a successful full receipt; boundary retries produced no final certificate. Retained progress and the complete interior proposal are not accepted completeness evidence.

Direct arXiv2605.23299v1 Table3 readings give candidate corrections23/39→25/41 at n6 and27/42→33/50 at n7. At n8 only interior38 is contradicted by the lower bound44; its total56 is not replaced with an exact count. Audit is pending; no author contact or accepted-erratum claim.

## Verification and limits

Every consequential mathematical exact/interval run has an actual different-agent execution with its own output. A5 additionally has independent certificate verifiers. A4's three finite supporting computations each have two executions; B3's section identities and whole-interval signs have two. B1 is a structural proof for arbitrary fixed admissible data; no mathematical software run or sampled rank is a premise.

All essential accepted certificates/global pairs and degree-eight lower-bound witnesses are committed. [Manifest](evidence-manifest.json), [independent-check index](independent-checks.md) and case receipts give identities and commands. Generated evidence stays within1,000,000 bytes/file and5,000,000 total. Temporary redundant copies are identified in `outputs/local_untracked_retention.json`, without a cold-storage claim.

Remaining scope: exact n8 completeness/global; all-n full-square A4 and historical/global runner-up identification; B1's other pole classes, individual stored taper parameters and numerical stability. B3 refutes its specified count, not other F or reference existence. Optional B4/B7 were not developed.

Original pins: Part1 `a09d910ae7d5526b1e216066421a0bee7fc20da4`; programme `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; current main `28aaa20861d08074b77efc74eaef75cdcb36234d`; rules adopted at `d8b878b348a94575e7753e5a756d969d41d5bca8`. The required Part1 dependency label “audit pending” is historical: Part1 audit accepted, dispositions completed and PR9 merged; Part2 audit is pending.

All authored changes stay in this topic; no final IDs/shared edits/RESULTS.md write. The repository-results summary is a literal proposal in [proposed-record-changes.md](proposed-record-changes.md), honoring the user's narrower scope. [LOG](LOG.md) contains the concrete intended Windows entry; no local write is claimed.

Next: `Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-2-20261101.`
