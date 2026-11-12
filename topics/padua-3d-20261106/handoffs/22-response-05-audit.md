# Handoff 22 — padua-3d-20261106 — focused audit of response05 material changes

- Status: done in 65afacf5c961ff1de224791548e87f88eaf97c33
- Previous handoff: [21-response-05.md](21-response-05.md).
- Next agent/model/effort: **Claude, Opus5.5 (`claude-opus-5-5`), high**; auditor may choose xhigh for the mathematical statement/attribution check. Use the workflow allocation for any bounded delegates; orchestrator alone controls Git/PR/handoffs.
- Role: independent auditor of Codex response05.
- Branch: `codex/padua-3d-20261106`. PR33: https://github.com/aacchhee/padua_research/pull/33 .
- Input head SHA: **`57f4669be083ec286d84b0f1e2f14b3b50ed14ca`**, completed response05 outputs. The following commit changes only handoff21’s status and publishes this handoff.
- Baseline for the focused diff: `ae4ab4741265f55ac10847659af89dad05441274` (audit05/fixes/handoff21 head).
- Main/base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`; fetch current heads first.
- Stage: **AUDIT**.
- Written by/date: Codex, gpt-6-astra high, 2026-11-12. Wording developer gpt-6.1-sol high; record/provenance developers gpt-6.1-sol medium. Runtime-internal model metadata beyond assignments is unexposed.

## Task: review the material response only

[Audit05](../audit-05.md) accepted the mathematics and all statuses. Do **not** reopen the accepted D1 proof, D2–D4 results or earlier campaigns absent a concrete new inconsistency. This is the focused re-audit required by handoff21 for the explicit H1 hypothesis, H2–H6 attribution/dispositions and manifest/ID changes. No new research, optimizer execution, proof campaign, quota spending or source-acquisition campaign is authorized. All directions remain frozen.

Read [response05](../response-05.md), its [mathematical notes](../response05-math-notes.md), [provenance note](../response-05-provenance.md), and the baseline-to-input diff. Resolve every H1–H6 and developer-returned item from audit05/fixes by checking the stated fix or documented coverage limitation. The prior auditor report/fix notes and protected frontier records are unchanged.

### 1. H1: explicit node domain, with no proof strengthening

Check D1-04, D1-05, the Chebyshev lift in D1-01, paper TheoremA/abstract, the final report and topic results: every node is in the **closed** cube, boundary points allowed; positivity, exactness through2n−1 and sufficiently-large-n quantifiers remain explicit. Generic projection identities keep their original R^d scope. No exterior-node conclusion, degree2n−2 strengthening or higher-dimensional theorem is introduced.

Root compared the proof sections with baseline: spectral-obstruction and finite-frame proof bodies are byte-identical; the weight-transfer proof only repeats cube membership in its setup. Check that statement clarification matches the accepted arccosine lift and p>0 weight transfer. This is material statement wording, not a new proof request.

### 2. H2–H5: attribution and actual source coverage

- H2: neighbouring effective LP fixed-excess results are credited: Yudin1997 indirectly through Lyubich p2; Lyubich Thm4.1/§5/Prop5.1 primary-read by the **prior auditor**, not newly read by this response; Xu2003 positive-interior disk result search/abstract-only. The old missing-reflection-step reason for a sphere failure is withdrawn. No sphere/disk theorem, effective cube constant or new proof premise is imported.
- Paper §2 gives the positive-weight-only, non-effective answer to Li–Sun–Xu’s n³/6+O(n²) question (0808.0180v2 pp3,16; signed weights allowed p1). The signed question/n³/4 conjecture stay OPEN; AMO14/Kolountzakis1/GL1.1 and Kuperberg receive mechanism credit, without a priority claim.
- H3: Lyness2003 optimality reports at excerpt coverage and the unread Belgian chapter are named. Minima n1/2/3/6/9/12/15 are credited as reportedly already optimal; local certificates do not claim their discovery. Other cases retain priority limits.
- H4: WWW2014/LIT391 receives secondary/abstract credit for reported cube log³ hyperinterpolation; exact operator/hypotheses remain unverified. The checked KL transfer is an alternative derivation, not a new bound.
- H5: the dated D5 addendum now compares D3 with LIT413, unread classical degree-five cube-rule compendia, T8 twenty-node unisolvent sets and n1/2 lattice packages; D4 with IDEA466/609/611 and the established mesh theorem. The completeness sentence means every manuscript claim has a comparison **or named unresolved comparison gap**, not an exhaustive literature search. No first-existence/certification claim.

Use the original audit05 source coverage and the newly corrected records; do not require full acquisition of already disclosed non-load-bearing gaps. Do not fabricate primary reading or treat a source report as a locally reconstructed proof. Existing E4 labels/dependencies remain unchanged.

### 3. H6 and returned record items

[frontier-dispositions-20261112.md](../frontier-dispositions-20261112.md) is a dated companion to the unchanged protected frontier assessment: C5 deferred, expressly **not subsumed** by non-effective D1; C6 deferred; both have precise resume conditions. C8 is completed bounded record work with explicit source gaps and no scientific restart. No final IDs or rejected/proved frontier theorem is invented.

Check the manuscript/process split and28-entry bibliography. Repository status/artifacts/counters/review records now live in [paper-repository-context.md](../paper-repository-context.md). The manuscript contains no internal .md/IDEA/handoff/Claude/supplemental-review process references. Incomplete title/journal/original-source metadata is explicitly incomplete, not fabricated. Check D3’s added disposition-reason field without any change to the finite theorem/status.

Verify existing full provisional split IDs reciprocally for T7-03/T7-09 and R08-minima/D4-minima. These are header repairs, not final allocation or changed science.

### 4. Provenance and actual verification

- Historical `evidence/fd4-manifest.json` and `fdr-d2-quality-replay.json` are byte-unchanged. All nine D4 prose acceptance pins are explicitly retired in the canonical provenance note **before** the D4 header edit; code/data integrity remains in the master. No historical JSON is silently rewritten.
- Master inherited inputs now include unchanged `audit-04/code/A1/aud_enum.cpp` alongside the two inherited lattice scripts. The enumerator source itself is unchanged. Current g++14.2.0 is recorded only as a current observation; the old compiler is unrecoverable. Each implementation’s original/replay binary is identical; the two implementations’ binaries differ.
- New `code/r05_quality_replay.py` actually runs the fixed monomial/SciPySVD assessment and pencil guards: n3=5478.148340739174,n4=546899.5809121559,69,433 queries each. The fresh receipt includes command/code/input identities, versions and observations. The old missing metadata remains disclosed and is not backfilled. These are MEASURED fixed-input checks, not optimization, exact rank or certified suprema.
- New `code/r05_manifest_replay.py` generates/verifies in a disposable tree, runs44 existing codec controls, explicitly mutates the newly inherited source and checks rejection/restoration, and checks the live master was unchanged. The nested checker's hardcoded historical head is identified as historical.

Low-cost actual commands from repo root, using new output paths:

```sh
python topics/padua-3d-20261106/code/artifact_manifest.py --verify
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B topics/padua-3d-20261106/code/r05_quality_replay.py --output /tmp/padua-audit06-quality.json
python -B topics/padua-3d-20261106/code/r05_manifest_replay.py --output /tmp/padua-audit06-manifest.json
```

All old scientific code, inputs and certificates are unchanged apart from the administrative master generator. Integrated master PASS:366 artifacts, three inherited inputs,19,358bytes. Conservative repository generated-output class8,685,984bytes. The approved provisional32KiB/file/master and10MBrepo allowance still applies and stays discussed in PR. No cold-storage delivery claimed. Current counters/freeze are unchanged.

## Read first

AGENTS.md, WORKFLOW and Claude role at fetched head; handoff21 and audit05/fixes (plus targeted A/D1a/D1b/D5 appendices); response05/math/provenance notes; exact baseline-to-input diff; changed D1/D5 records; manuscript and repository companion; frontier disposition companion; master/replay source/receipts; LOG latest response05 entries and topic results. This response generates no new mechanism or priority claim; use the original full novelty gate plus the full listed predecessors for its corrected attribution scope.

## Limits and acceptance

- No new research/optimization/proof campaign; no unused quota spending; no final IDs/reservations/shared-registry application. Do not change main/tags/settings/.github or merge. Only AC merges.
- No edits to earlier audit/fix/frontier records or old handoff instruction bodies. Audit/fix eligible MINOR records in place under the third-round-onward rules, list them and commit separately; return material/uncertain findings to development.
- Write `audit-06.md` with precise diff/input coverage, actual commands/results, findings/dispositions and residual uncertainty. A new broad audit is not requested. Update LOG/topic results/PR within that scope.
- If accepted, stagePR and open handoff23 to **Codex gpt-6-astra high** for refreshed reservation/final-ID/registry preparation plus one readiness reviewed-diff/reservation check, then freeze. If material findings remain, stageWORK and open23 for a focused response06. No implicit broad restart.
- Commit outputs first; in the following commit change only handoff22’s status to `done in <output-sha>` and add handoff23. Keep exactly one open handoff, push before replying and end with the appropriate short continuation prompt. Only AC merges.
