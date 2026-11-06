# Readiness 01 — PR #28 (nn-mop-stability-20261105)

- **Reviewer:** Claude, Opus 5.5, effort high, as handoff07 requires. Role: independent readiness reviewer and topic orchestrator. I did not apply the registries or assign the IDs; Codex did.
- **Date:** 2026-11-06 (UTC).
- **Rules:** read at branch head `578bb1e`. AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md are unchanged since main `f654e32`.
- **Prepared input:** `dd092fb74b3030fe28dd8dd221ef59e0e80b2b72`, published with handoff07 at `578bb1e`.
- **Reviewed diff:** `80086a1af5d232c110f9c7c754d43b47332cbe71..dd092fb`, which is the same over the seven registries as `414e781..dd092fb`.
- **Verdict: READY for AC's merge decision.**
  - No BLOCKING or MAJOR finding.
  - Ten MINOR items were fixed in place under the round-3 auditor rule, in the separate commit `7c97833369a09b8f9db0781628a3265fbd3aca41`. That commit changes no claim, status, threshold, input or result.
  - One proposed item was declined (R-M5 below).

## Method

Two independent Claude Opus subagents (high effort) checked disjoint scopes:
- **S1:** the seven shared-registry diffs against id-map.json and the durable records;
- **S2:** audit-02's R-1 to R-8, numeric invariance, the evidence manifest, checker runs and the G5 wording.

I did the reservation refresh and the paper-data verification for G5 myself, and made the in-place fixes. The subagents changed no Git state.

## Registry application (S1)

| Check | Result |
| --- | --- |
| Preservation | 7 files, 185 insertions and 4 deletions. PROOF_STATUS.md, RESULTS.md, literature/INDEX.md, state/CURRENT.md and ID_CROSSWALK.md are pure appends at end of file. state/IDEAS.md edits only the original IDEA-090/117/378 rows in place; PAPER_MAP.md only the original NN row. No foreign ID is renumbered or deleted. None of the new IDs occurs in the base registries or in PR #27's head registries. |
| Rows against id-map and records | Checked exhaustively: all 18 PD-T (T432–449), 7 PD-N (N162–168) and 26 IDEA (530–555) rows, LIT-614, the LIT-567/568 reuse and all 54 crosswalk rows. Every one of the 57 id-map keys appears as a crosswalk alias, and no provisional `?nn-mop-stability` ID in the repository is unmapped. |
| Status counts | PD-T: 9 PROVED, 5 MEASURED, 4 OPEN. PD-N: 6 PROVED, 1 MEASURED. No PARTIAL. All 25 theory files carry their final ID and status, and their split relations run both ways. The OPEN parents PD-T448 (sharp growth) and PD-T449 (stable solver) name their supporting results without becoming PARTIAL; PD-T446 and PD-T447 are OPEN. |
| Candidates | Every deferred, equivalent, refuted and failed candidate is represented, including the five prescribed alternatives IDEA-551–555. IDEA-090 and IDEA-378 remain deferred with resume conditions, and IDEA-117 carries the continuation pointer. |
| Process stage and links | The new registry content has no process stage. All 202 added links and anchors resolve. This topic's RESULTS.md section is identical to its results file from line 3 on (path prefix aside). |

## Record hygiene and invariance (S2)

**R-1 to R-8 are confirmed by diff:**
- **R-1:** the dated Codex chronology addendum sits below the canonical AC-decision entry (LOG.md:111–115), the response-01 parentheticals are marked as Codex text, and the D6 heading is qualified.
- **R-2:** the finite Hahn record has `Split from: none`, with the certificate listed as a dependency.
- **R-3:** parent/child split relations are two-way.
- **R-4:** the growth target quotes handoff01 verbatim, byte-identical to lines 54–64, and adds an explicit reformulation and reason.
- **R-5:** the dependency wording is localized.
- **R-6:** the wording is "(n,0)".
- **R-7:** convergence and 100-dps claims are scoped as historical only.
- **R-8:** old pins are labelled historical at `4e87fc0`. Every historical hash was recomputed from that commit.
- The audit-02 leftovers in the G record are fixed.

**Invariance.** A numeric-token diff over every changed record accounts for every changed number:
- dates and final IDs;
- pin labels;
- the quoted handoff numbers;
- the lower-bound record SHA in plot-receipt.md, verified;
- the G5 rewording, whose values remain in the G5 receipt and audit.

`git diff --stat 414e781 dd092fb` is empty for all of the following:
- audit-01 and audit-02 and their script directories;
- all `code/*.py`;
- `evidence/projection-reference.json` (SHA-256 `37c3c060…`);
- response-01;
- input-snapshot;
- the unedited attempts.

**Evidence manifest.** All 69 file rows plus both input-inventory fields were recomputed at `dd092fb`: SHA-256, Git blob and bytes, with 0 mismatches. After the in-place fixes I updated the 7 affected rows, and recomputation again gives 0 mismatches. There are no new prose checker pins.

**Checks actually executed:**
- `python topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py`: PASS, 61 sizes, 43,676 checks, code pins verified. This was rerun after the in-place fixes. All 61 receipt-table rows are byte-identical to `414e781`.
- `python topics/nn-mop-stability-20261105/audit-g5-01/check.py`: PASS. With `--archive` pointed at AC's upload: PASS, archive verified, 33 entries and 27 files. The checker only hashes and inspects members; it executes nothing.

**Required wording.** The G5 wording "G5 reproduction gate PASS (one configuration, Octave 8.4, to the decade); large-N variation measured; topic-metric comparison not yet run" appears in gates.md, report.md, attempts/D7.md, external-code.md and the results file. G4 is never PASS, and nothing claims a general stable algorithm or sharp growth.

## G5 paper-data verification (orchestrator)

Codex's audit-g5-01 left this as an explicit unresolved item, because arXiv is blocked for its executor.
- I re-downloaded `https://arxiv.org/src/2506.19796v2` at readiness: 88,273 bytes, SHA-256 `f736e8f03b536382141c2c98620c3cd408e0ff2c772ce58f47030e944864d461`, identical to the earlier record.
- `data_experiment1_kravchuk.dat` (SHA-256 `0ae382c8…`) gives paper N=10, err_H_core = 6.85119133277418e-10, the value quoted in the gate.
- `python3 -I g5-run/cmp.py <bundle>/Experiments/experiment1 g5-run` regenerates `g5-run/compare.txt` byte-identically.
- The same comparator applied to Codex's Octave 9.4 outputs (`audit-g5-01/ours_*.dat`) gives a gate value of 2.691215e-10, log10 ratio −0.406, a PASS.
  - Its exceedances of one decade, by column:

    | Column | Krawtchouk N | Hahn N |
    | --- | --- | --- |
    | e_N CORE | 22, 27 | 12, 18, 19 |
    | e_N KRYL | 14, 20, 21, 23, 29 | 10, 11, 13, 14, 18, 20 |
    | e_N REORTH | 23, 24, 28, 29, 30 | 22, 27 |
    | biorthogonality CORE | 25, 26 | 19, 28 |
    | biorthogonality KRYL | 23, 29, 30 | 10, 11, 13, 14, 18, 20, 26 |
    | biorthogonality REORTH | none | none |

  - These are large-N or KRYL-sensitive entries, consistent with the measured variability; none is the gate configuration.

The paper reference is therefore authenticated against the published bundle. This was done by Claude, not by a third executor. The bundle itself is not committed.

## In-place MINOR fixes (commit `7c97833`, separate from this report)

1. state/IDEAS.md, IDEA-090: restored the original resume condition ("outside this campaign; resume only on AC request and coordinate with the Leuven line") beside the new pointer (S1 M1).
2. PAPER_MAP.md, NN row: "full error-source decomposition" restored as OPEN. The finite stage-isolation result PD-T438 does not separate boundary amplification from layer rounding (S1 M2).
3. PROOF_STATUS.md, PD-N162–168: each disposition cell now names the killed candidate (IDEA-532/536, 540, 541/544 safeguard shortcut, 543, 542, 547's literal P11, 548), following the PD-N118/132 convention (S1 M3).
4. state/IDEAS.md, IDEA-541/544: record the already documented PD-N164 disposition of the positivity-only normality-safeguard shortcut (candidates-D4.md:83–85; S1 M4).
5. PROOF_STATUS.md, PD-T446: PD-T447 is its parent, not a dependency (S1 N1).
6. literature-D4.md:3/7/15/23: restored the alias headings (LIT?…-D4-0x, LIT-D4-0x) and the stale "needs a new provisional record" line (S1 M6, S2 MINOR-1).
7. Stale provisional or pending text: integrable-*.md:3 ("provisional allocation"), dictionary-graph.md:5 ("Proposed"), novelty-gate-D6-D7.md:110–111 (G5 source supplied) (S1 M6).
8. Bare local labels D4-01 to D4-05 in the integrable records, candidates-D4.md and literature-D4.md replaced by their final IDs from id-map.json (PD-T443, PD-N164, PD-N165, PD-T444, PD-N166, LIT-D4-03) (S1 M7).
9. theory/conditioning-growth-target.md:50: the quote is cited as handoff01 lines 54–64 (S2 MINOR-2).
10. evidence-manifest.json: rows updated for the seven edited pinned theory files, in the same commit.

**Declined:**
- **R-M5 (S1):** move the D2 gate options (the Gragg–Harrod comparator and path-as-backward-error) into state/IDEAS.md with resume conditions. audit-01 MINOR 8 explicitly accepted "state that the gate does not apply" for D2, which claims no mechanism, and response-01 did that. Writing new resume conditions would also exceed an auditor's in-place fix. They stay recorded in novelty-gate-D2.md and ID_CROSSWALK.md:1650.
- **Stale history text in conditioning-lower-krawtchouk.md:268/309:** left unchanged, because plot-receipt.md pins that file's hash and the text is cosmetic. NOTE only.

## Reservation refresh (orchestrator, 2026-11-06)

**Heads checked:**
- main `f654e32daff27b6846849311092f6daebbbf235b`;
- open PR #27 `4b728b04216a5490910780bc609a82b853058426` (draft, unchanged since preparation);
- this PR #28 at prepared `dd092fb`.

Every other PR (#1–6, 8–26, 29, 30) is closed and merged; #7 does not exist as a PR. Thirteen ledgers were read on each head, together with every final ID used in PROOF_STATUS.md, state/IDEAS.md, literature/INDEX.md and ID_CROSSWALK.md.

**Findings:**
- No foreign registry uses any ID inside this topic's ranges.
- Mentions of T432–471/N162–177/IDEA530–569/LIT614–629 in other ledgers acknowledge PR #28's reservation: padua-batch:396, lanczos-frontier:62 and lanczos-nonproduct:53.
- PR #27 owns T392–431, N146–161, IDEA490–529 and LIT598–613, directly below this topic's ranges.
- PR #30 (merged) owns T472–501, N178–180, IDEA570–589 and LIT630–632, directly above.
- Maximum used: T494, N178, IDEA584, LIT630. Maximum reserved: T501, N180, IDEA589, LIT632.
- This topic's assignments are PD-T432–449, PD-N162–168, IDEA-530–555 and LIT-614, all inside its own permanent reservation (first published `d879256`). The unused remainders T450–471, N169–177, IDEA556–569 and LIT615–629 stay as permanent gaps.
- **No collision.** Per WORKFLOW, the check is repeated before merge if main or any open PR's ledger changes in the meantime.

## Residual limits (scientific and reference data)

- Sharp matching conditioning growth (PD-T448) and a general stable NN solver (PD-T449) remain OPEN. G4 is forward-threshold success with adverse strict-backward evidence, not a stable-solver PASS.
- G5 reproduces one configuration to the decade on two Octave platforms. There is no MATLAB, bitwise or all-size reproduction. The comparison against this topic's fieldwise NN metric has not been run, and the paper's Advanpix conditioning-error column is not reproduced. Neither the third-party code nor the paper data is committed; their hashes are recorded.
- The projection reference is a new fixed-configuration run; the Nov-5 bytes remain lost.
- Floating tables are precision or platform measurements, not outward enclosures.
- Storage: about 1.2 MB committed for this topic, below AC's 10 MB threshold. No cleanup.

## Decision requested from AC

Merge PR #28 (squash) if you accept:
1. the audited scope above;
2. the G5 scope (one-configuration reproduction, topic-metric comparison still to do);
3. the permanent ID gaps.

If any ledger on main or an open PR changes before the merge, the reservation check must be rerun first. Only AC merges.
