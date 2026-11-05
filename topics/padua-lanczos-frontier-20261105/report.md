# Lanczos frontier — checked finite scalar separation and resolved replay gate

Stage WORK. [Draft PR24](https://github.com/aacchhee/padua_research/pull/24), not ready for merge. Rules read at f85c7b5c83822ff60b62c84bed1ec6ae31628422; base/main440d1079e42c3ef21c40d1cf8870f5b206410c6a. No final IDs assigned or canonical registries changed; [literal proposed changes](proposed-record-changes.md) await audited preparation.

## Main result — L4

The rotQ24 degree12 **full formal scalar-CGS2** factor-ten target is now PROVED, computer-assisted, at the exact assumptions of [PD-T?lanczos-frontier-codex-L4a](theory/l4-envelope-bound.md). All90 local source columns and every vector-operation channel of PD-T138 are retained. The exact rational grid has625 points/91 columns, exact starting vector, fixed selections, no data perturbation or underflow/overflow; this is a first-order permissive relative-error model, not a claim about realized IEEE roundings.

The checked alternating capacity upper and BJ capacity lower satisfy

`K_alt² <= 13,462,956,266`,

`K_BJ² >= 2,041,704,913,997 > 100 * 13,462,956,266`.

Hence `K_BJ > 10 K_alt`, which also proves the requested `K_BJ > 10 min(K_alt,K_pivot)`. The new lower uses the **same frozen target90/node/operation signs** as the inherited witness, reading its entire output with the committed [91-integer monic coefficient vector](evidence/l4-readout-certificate.json). No operation-sign search or model change was needed. The old target90 projection is reproduced exactly before the improved readout. Floating SVD proposed a direction; only exact rational arithmetic establishes acceptance.

The envelope upper search alone did not settle the target: all nine preregistered positive-vector tests failed with the old BJ lower. The separate [PD-N?lanczos-frontier-codex-L4-01](theory/l4-N01-fixed-lower-envelope-obstruction.md), PROVED computer-assisted, shows why no upper on that absolute envelope can pass with the **fixed old** lower: its eigenvalue is at least13,462,955,378. This route obstruction does not lower-bound the true alternating capacity, upper-bound BJ capacity, or obstruct the successful stronger BJ lower. Both failed and successful steps remain in [candidate memory](ideas-l3-l4.md) and [attemptL4](attempts/L4.md).

The original PD-T140 experiment remains MEASURED/INCONCLUSIVE as recorded. The newly proved rotQ24 conjunct, combined with inherited PD-T141(c)'s T24 conjunct, settles its mathematical two-grid target separately; canonical target metadata awaits the later audit/preparation. No old sufficient test is relabeled as having passed.

## Verification and evidence

The [supplementary independent check](independent-checks-l4.md) freshly regenerated the full90-source comparator envelope and the full signed BJ output in separate executions, and freshly reran the inherited BJ witness reproducer. The standalone checker recomputes exact Gram products, the complete basis Gram identity, the fixed rational readout's projection energy and denominator, original trace/target controls, strict comparison and the scoped Rayleigh premises. Thirteen malformed controls were actually rejected. Producer and independent checker share FLINT rational arithmetic; independent scalar-loop/projection formulas supplement full source-regeneration review. This is not a wholly independent second derivation of PD-T138.

Small receipts and source pins: [envelope](evidence/l4-envelope.json), [Rayleigh](evidence/l4-rayleigh.json), [full-output witness](evidence/l4-full-witness.json), [fixed certificate](evidence/l4-readout-certificate.json), [independent receipt](evidence/l4-independent.json). Commands and runtime limits are in [producer methods](l4-producer-methods.md) and the independent report. Producer elapsed times were about288s for the envelope and217s for the witness in this sandbox with concurrent work; these are finite execution receipts, not degree-cost curves or hardware benchmarks.

Large exact arrays remain local and regenerable outside Git, with [manifest and retention limits](COLD_STORAGE.md). Physical Windows delivery is pending, and sandbox retention is not guaranteed. No third-party code/PDF/HTML or bulk matrix enters Git. Required Claude scientific/protocol audit remains pending; the supplementary check does not replace it.

## Gates

- **G0 RESOLVED**, additively under its unchanged explanation criterion: [disposition02](g0-disposition-02.md), [methods](g0-attribution-methods.md), [independent review](independent-checks-g0-resolution.md). Existing exact witness/certificate and symbolic replays pass. For numerical replay variation, independent high-precision projection, u-scale local residual propagation and kernel/precision controls explain arithmetic sensitivity. Historical Q/H/dispatch remain missing; old alternating7.301e-12 is scale-consistent, not reconstructed or bounded by a kernel envelope. The original dated FAIL remains unchanged.
- **G1/G2/G3/G4 NOT RUN.** The L4 exact experiments above do not stand in for all-degree growth scans, PD-T055 closure predicates, optimal Padua-radius brackets or high-degree polyrat replay. The L1/L2 and L3/L4 relevant mandatory repository-reading gates are now complete for the saved routes; no primary-fulltext/priority clearance is implied.

## Remaining directions

| Direction | Status and next obligation |
|---|---|
| [L1](attempts/L1.md) | OPEN. Implement preregistered G1 exact growth scan and independently check it; verify saved sheared-product family hypotheses/gauge before any all-degree claim. |
| [L2](attempts/L2.md) | OPEN. Freeze a well-posed predicate/rule class and obtain G2 exact degree12 truth before an all-degree attempt; span capacity alone does not decide closure defects. |
| [L3](attempts/L3.md) | OPEN. Explicit-radius and adaptive-branch drafts remain unchecked; no unconditional selection theorem. |
| [L4](attempts/L4.md) | PROVED finite formal comparison above. Actual IEEE activation, finite-u behavior and all-degree growth remain outside it. |
| [L5](attempts/L5.md) | OPEN. G3 exact small-n optimal-radius certificates unrun; no inference from the named P_n radius to the optimal obstruction radius. |
| [L6](attempts/L6.md) | OPEN. Actual recurrence/moment consistency and complete omitted-operator residual control remain unresolved. |
| [L7](attempts/L7.md) | NOT RUN. Preregistration preserved; code only syntax-checked. G4, source/runtime access, reference/implementation validation and the natural-fit suite remain due. |

## For the paper and protocol

The finite full-scalar factor-ten theorem and its explicit witness can enter a bivariate Lanczos/V+A note after the required audit. It closes a finite comparison, not E2's all-degree result or a universal IEEE instability statement. The fixed-old-lower route obstruction explains the certificate improvement. Primary-source coverage/priority wording remains qualified by the pinned **PR21 (unmerged)** P3 comparison and its stated reading limits; no publication-level novelty is claimed.

Some initial candidate formulas preceded completion of all mandatory shortlisted reading. That prospective novelty-gate timing deviation remains explicitly disclosed; later reading does not cure it. Claude must give a protocol disposition at the later audit. No waiver, merge readiness or final-ID assignment is implied. Next development is the remaining frontier under a new numbered handoff; only AC merges.

## Rechecking without historical scratch files

The compact [combined fixed certificate](evidence/l4-fixed-certificate.json) stores both the625-integer upper vector and91-integer lower vector. [code/l4_recheck_fixed.py](code/l4_recheck_fixed.py) was actually executed on the distinct independent regenerations and [passed](evidence/l4-fixed-recheck.json), including seven malformed fixed-data controls and a control that removes historical lineage fields. This scientific verifier needs only newly generated arrays, the committed rational vectors and pinned source/input bytes; it opens no original developer matrix, candidate, receipt or extraction path and consults no new floating proposal. The original full audit/13 controls remain separate and unchanged. The recipe in COLD_STORAGE.md reconstructs inputs and produces fresh arrays using only the repository and network.
