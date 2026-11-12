# Audit 06 — padua-3d-20261106 — focused re-audit of response-05

**Auditor.** Claude, Opus 5.5 (`claude-opus-5-5`), as the independent auditor of Codex development under handoff 22.
- The orchestrator ran the reruns, the H1 proof-identity diff, this report and the auditor fixes, at effort high.
- Two independent subagents audited the two scopes:
  - [H1–H5: statements and attribution](audit-06/H1-H5.md), Opus 5.5 xhigh;
  - [H6, returned records, provenance, manifest](audit-06/H6-records.md), Opus 5.5 high.
- No subagent changed Git state.

**What was audited.**
- Rules read at `c889c1a10f1365f5781afe303481a0073112c696`; unchanged since `ae4ab47`.
- Focused diff from baseline `ae4ab4741265f55ac10847659af89dad05441274` to candidate **`57f4669be083ec286d84b0f1e2f14b3b50ed14ca`**. Head `c889c1a` only closes handoff 21 and adds handoff 22.
- Main `f70a260`, unchanged.
- Date: 2026-11-12.

This is the focused re-audit that handoff 21 required. Accepted mathematics (audit 05) is not reopened.

## Verdict

**Accepted. Stage PR.** No BLOCKING finding. One MAJOR-classified finding was resolved by an auditor fix; the classification rationale is given below.

**H1 — closed-cube hypothesis.** The hypothesis is now explicit in all of these places:
- D1-04 and D1-05;
- the D1-01 Chebyshev lift;
- paper Theorem A and the abstract;
- the final report and the results file.

The orchestrator and the subagent each diffed the D1 files independently. The proof sections of `spectral-obstruction`, `finite-frame`, `stationary-limit` and `complete-law` are byte-identical. The weight-corollary proof gains only the cube membership in its setup. No strengthening was introduced: no exterior nodes, no degree 2n−2, no general d.

**H2–H5 — attribution at its true coverage.**
- Lyubich and Yudin (Yudin via Lyubich), and Xu 2003.
- Li–Sun–Xu, with page pins.
- The mechanism credits.
- Lyness 2003 and the Belgian chapter.
- Wang–Wang–Wang.
- The D3/D4 comparison rows, with the completeness sentence corrected.
- No new priority claim. E4 labels unchanged.

**H6 and returned items.**
- C5 and C6 deferred with resume conditions; C5 is expressly not subsumed by D1. C8 completed.
- The manuscript is separated from repository process text, with a 28-entry bibliography and no fabricated metadata found.
- The D3 disposition field is added.
- The split headers are reciprocal.

**Provenance.**
- The historical JSON is byte-unchanged and the D4 prose pins are retired.
- `aud_enum.cpp` is now an inherited master input.
- Every mutation fails as expected.
- Storage is within the approved allowance: master 19,358 B, repository generated class 8,685,984 B.

## Executions

Orchestrator ([audit-06/receipts.txt](audit-06/receipts.txt)), in a detached worktree of `57f4669`, all exit 0:

| Command | Result |
|---|---|
| `artifact_manifest.py --verify` | PASS, 366 artifacts |
| `r05_quality_replay.py` | n3 = 5478.148340739174, n4 = 546899.5809121559 |
| `r05_manifest_replay.py` | 44 codec controls; the audit-04 source mutation is rejected; the live master is unchanged |

The live worktree was unchanged afterwards. Subagent executions, mutation tests and hash checks are listed in the appendices.

## Findings

### BLOCKING

None.

### MAJOR (resolved by auditor fix; classification recorded for possible developer dispute)

**K1 — Li–Sun–Xu scope** ([H1–H5 M1](audit-06/H1-H5.md)).
- Li–Sun–Xu p1 defines nodes as x_k ∈ R^d. The paper (line 49) and `final-d1/gate.md:42` implied that Theorem A settles the whole positive-weight case. It does not: positive rules with exterior nodes are outside Theorem A.
- The canonical D1 source record (`final-d1/sources.md:46`) already states the correct scope: "only for positive weights with nodes in the closed cube".
- **Auditor action.** The paper and gate wording now conform to that canonical record, with the p1 node definition added (primary-read by the audit-06 subagent).
- No theory statement, status or proof changed. The classification therefore treats this as conformance to an already-documented decision, which is within the auditor-fix limits.
- The developer may dispute the classification at PR preparation; disputes go to AC.

### MINOR (auditor-fixed in place; separate commit, listed in [audit-06-fixes.md](audit-06-fixes.md))

- H-m1, m2, m3, m4: cube-scope conformance in the paper (lines 32 and 71), `final-d1/README.md:5` and `frontier-dispositions-20261112.md:9`.
- H-m5: δ is defined at paper line 73.
- H-m6: Lyubich's initial and title (paper line 118).
- R-m1: process reference in the paper (line 85).
- R-m2: a dated pointer in `final-d4/results.md` to the retired fd4 prose pins.
- R-m3: rounding in `response-05-provenance.md:86`.

**Returned to PR preparation (not auditor-fixed):** H-m7, the Belgian-chapter co-author and DOI metadata. It rests on search-level metadata only.

### NOTE

- The Caliari–De Marchi–Vianello CMA 55 (2008) entry has no repository source record behind it.
- The committed manifest receipt's `verified.bytes` differs from the tree (2,301,684 vs 2,301,750), because the receipt sits inside the tree it describes. Integrity is unaffected.
- "Retirement precedes the D4 header edit" is a statement in the note; both are in one commit.
- `artifact_manifest.py:255` hardcodes an older `rules_input_sha`. This predates the diff.
- Optional pointers from the T10 and minima theory files to the new Wang–Wang–Wang and Lyness credits.
- "OPEN" is used for a literature gap in the D5 gate; "unresolved" would read better.
- Bibliography checks were limited by network access (doi.org, Crossref and OpenAlex are blocked).

## Residual uncertainty

- Lyness 2003, Wang–Wang–Wang and Xu 2003 remain at excerpt or abstract coverage.
- No historical novelty is established.
- D1 is non-effective and positive-weight-only, for nodes in the closed cube.
- The main minimal-node polylog interpolation target remains OPEN.

## Next step

Handoff 23: Codex PR preparation. That covers a refreshed reservation check, final-ID and registry application, H-m7 metadata, and one reviewed-diff readiness check, after which the direction freezes. Only AC merges.
