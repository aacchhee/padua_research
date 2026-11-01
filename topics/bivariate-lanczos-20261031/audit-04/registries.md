# Audit 04 — independent registry integration review

Verdict: **FINDINGS**. The allocation and preservation checks pass, but the new canonical IDEA dispositions and dependency summaries do not faithfully represent the accepted records. A4-M1 and A4-M2 require preparation corrections; A4-L1 is a lower-severity generator repeat-run defect. This review does not reopen the accepted mathematical audit.

## Provenance and scope

- Auditor: Codex subagent `/root/audit_l2`, explicitly launched with `model=gpt-6-astra`, `reasoning_effort=xhigh` as requested by AC; no independent runtime confirmation is exposed. These are launch settings, not runtime attestation.
- Rules and reviewed head: `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`; read `AGENTS.md`, `agents/WORKFLOW.md` (including the new local working-track paragraph), and `agents/codex/CODEX.md`.
- Accepted scientific baseline: `cf01449fc96233c9074ce25efcb056535414aa1d`; current-main comparison: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`; preparation code checkpoint supplied by the orchestrator: `2e1530be33a3ecc5a9d677e25b86ccacb13b90b2`. Draft PR #10 publication/Git state is checked by the orchestrator, not independently attested here.
- Read the complete current `state/IDEAS.md`, its obstruction and disposition tables, new PROOF_STATUS and NEGATIVE_RESULTS rows, allocation ledger, SPLITS and corresponding final crosswalk rows; inspected relevant full candidate entries, current disposition amendments and theory sections. Read both preparation scripts in full. INDEX coverage here is identifier inventory/preservation and relevant rows, not a renewed full literature or source audit; that work belongs to the other assigned reviewer. No new novelty, priority, proof, or negative-result claim is made.
- Only this report and `audit-04/registries/` were written. No developer file, Git state, PR comment, or external local working-track record was changed.

The complete per-file SHA-256 input manifest is `registries/independent-results.json:source_sha256` (rules, registries, allocator/checker, generated row inputs, all candidate files, SPLITS and all 77 theory files). Evidence identities and generating commands are in `registries/evidence-manifest.json`.

## Findings

### A4-M1 — MEDIUM: new IDEA rows import historical or placeholder dispositions

Locations: `state/IDEAS.md:642`, `:652`, `:662`–`:672`, `:690`–`:693`; cause `topics/bivariate-lanczos-20261031/pr-prep/allocate.py:107`–`:113`.

The generator takes the first top-level `- Disposition` line inside a candidate's initial section. Later corrections, result tables and inline dispositions are ignored. This is consequential, not just an abbreviated index:

| New registry row | Current accepted record | Required summary |
|---|---|---|
| IDEA-135, line 652: the claim “single-relation row selection, not truncation” **survives** | `directions/L1/candidates.md:194`–`:199` explicitly rejects the titled claim; PD-N011 refutes it, while a narrower two-relation observation survives | **REJECTED: refuted**, finite measured scope, PD-N011; distinguish the retained control from the rejected causal claim |
| IDEA-125, line 642: rejection includes “tensor over-prediction” | `directions/L1/candidates.md:45` withdraws that reason and restricts failure to non-product sets | Retain the narrowed non-product failure; do not reintroduce the withdrawn tensor reason |
| IDEA-145–150, lines 662–667: all **pending** | `directions/L2/candidates.md:104`–`:110`: E1 survives as an estimate; E2 is equivalent in effect in scope; the formed-section candidate survives with corrected hypotheses but its unconditional one-pass F and J variants fail; H_drift and E3 fail; the two-pass window survives its stated tests | Register these current, part-specific dispositions. For IDEA-148 retain the disclosed post-hoc drift criterion; IDEA-149 is **REJECTED: failed**, PD-N017 |
| IDEA-151–155, lines 668–672: only “see record” | L2 candidates lines 154–156, 178, 194: tested rules/strategies fail in named finite scopes; pivot-adaptive selection has a deferred continuation; IDEA-211 is deferred and untested | Expose failed versus deferred status and the resume condition; do not present deferred work as tested or rejected |
| IDEA-173–176, lines 690–693: “R01.md.” / “see record” / “R02.” / “R03.” | `directions/L5/candidates.md:86`, `:90`, `:94`, `:106` give the current scoped dispositions, including the as-written kill of IDEA-501, refuted prefix claim, explanation failure with a retained positive theorem, and failed/equivalent/retained rule variants | Summarize those dispositions rather than the original run placeholders; preserve the post-hoc qualifications and the positive theorem |

All 100 candidate IDs are retained. The failure is their canonical disposition fidelity, not deletion. Correct all affected summaries using explicit current disposition data or a reviewed mapping; changing the regex to pick the last matching line is insufficient for tables and mixed parts. Keep the historical preregistration text intact. The stale MEASURED title of PD-N025 and IDEA-166's MEASURED reference also illustrate why the final summary must be reconciled with the actual current theorem status (PROVED refutation, measured survey outside its statement), rather than copied without review.

### A4-M2 — MEDIUM: dependency extraction reverses edges and drops shorthand references

Locations: `PROOF_STATUS.md:140`, `:104`, `:106`; `state/IDEAS.md:673`, `:674`, `:685`; cause `pr-prep/allocate.py:57`–`:65`, `:71`–`:72`, `:93`.

- PD-T053's registry dependency list is `PD-N013, PD-N015, PD-N016, PD-T050, PD-T051, PD-T052`. Its actual source, `tracks/bivariate-lanczos/theory/reference-free-span-drift-lower-bound.md:42`, says **“None (elementary linear algebra). Results that depend on this file: …”**. The extractor reverses downstream-use edges and creates artificial cycles with PD-N013/015/016 and PD-T050/051. PD-T053 must have no mathematical dependencies here; downstream uses can be recorded separately.
- PD-N020 lists only PD-T057. `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N301-padua-n3-exact-backward-obstruction.md:36` names provisional T301, **302, 303**, so the final list must include PD-T057, **PD-T058, PD-T059**. The same shorthand pattern affects other rows, including PD-N022.
- IDEA-156 becomes `PD-T058, 303`; IDEA-157 becomes `PD-T059(d)–(f), 305, 306`; IDEA-168 becomes `PD-T068, 313, PD-N022`. The bare numbers remain old local identifiers next to final identifiers. Their intended final references are respectively PD-T059; PD-T061/PD-T062; and PD-T069. Preserve the namespace/context or convert the entire reference group.

Use an explicit reviewed dependency/reference mapping, or parse only genuine forward dependencies while resolving contextual shorthand. Check the resulting dependency graph against source meaning, not merely that every final token names an existing row. Retain the existing final IDs.

### A4-L1 — LOW: the advertised allocator corrupts its own outputs on a prepared tree

Locations: `pr-prep/allocate.py:10`–`:11`, `:39`–`:51`, `:128`–`:141`.

The documented no-argument invocation on the current prepared inputs finds zero literature entries because INDEX now starts with final IDs. It exits 0 after rewriting the map from **404 to 177 entries**, dropping **all 227 LIT mappings**, and emitting only 177 crosswalk rows. Repeating with `--apply` also adds a second Final ID line to **all 77 theory files**: its duplicate-header check looks only before the first blank paragraph, while the existing allocation line is after it.

These are actual independent executions in a temporary copy under the owned audit directory, removed automatically afterward; the live preparation outputs were never passed to the allocator. Full exit codes/stdout/counts are in `independent-results.json:isolated_generator_rerun`.

Acceptance: support repeat invocation while retaining the complete 404-entry map and exactly one correct header per theory file, **or** enforce and document a one-shot input precondition and fail before any write on a prepared tree. A4-M1/M2 repairs must not regenerate from the current unguarded allocator and thereby lose allocations.

## Executed checks and bounded passes

Commands were run from `/workspace/padua_research`, Python **3.12.14**:

```text
python topics/bivariate-lanczos-20261031/pr-prep/check_integration.py > topics/bivariate-lanczos-20261031/audit-04/registries/check_integration.json
python topics/bivariate-lanczos-20261031/audit-04/registries/check_registries.py > topics/bivariate-lanczos-20261031/audit-04/registries/independent-results.json
```

The developer checker exited **0**, reporting 111 final theory/negative rows, 100 new IDEA rows, 292 final LIT rows, 77 matching headers, no duplicate IDs/status mismatch/broken checked links, and no size-limit failure (3,387,111 bytes in its filesystem-based inventory at that instant). That pass does **not** test disposition freshness, dependency direction, complete shorthand conversion, or generator reruns; it is therefore a false indication of semantic completeness if used to approve A4-M1/M2. Its size inventory includes matching untracked filesystem paths, so this subagent does not present it as an independent committed-output inventory.

The final independent checker exited **0** for its structural checks, and separately reports the repeat-run defects. Verified:

| Namespace | Final range | Count |
|---|---|---:|
| PD-T | PD-T029–PD-T080 | 52 |
| PD-N | PD-N007–PD-N031 | 25 |
| IDEA | IDEA-077–IDEA-176 | 100 |
| LIT | LIT-066–LIT-292 | 227 |

- A bijection of **404** provisional/final entries; contiguous expected ranges with no duplicate values; crosswalk exact membership; all 77 theory files represented; 25 negative rows; all **48 seed + 52 developed candidates** represented. No accepted main-range collision.
- Every preexisting main registry row remains byte-identical, including provisional rows: 55 PROOF_STATUS, 111 IDEA, 101 INDEX and 247 crosswalk rows (these are row counts, not unique-ID counts).
- Exactly one matching Final ID header in each of 77 live theory files; registry overall status agrees with each theory file. Removing only the new allocation line recovers each accepted scientific-baseline theory file exactly.
- All **11** final split/provenance rows agree with SPLITS after full-ID substitution and insertion of the source column. The 11 include a new supporting-result row and an in-place correction/negative record, not eleven independent theorem splits. PROVED parts, separate CONDITIONAL/MEASURED/OPEN results and the two registered refuted-variant dispositions in PD-T037/PD-T058 remain distinguished. Historical “pending audit” text in split provenance is not treated as a new status change.
- The ledger's explicit AC exception gives Claude ownership of this block while preserving the other member allocations. The orchestrator separately reports current active PR #11 reserves LIT-293–298 after this block and #6 retains provisional IDs; those remote checks are not claimed as this subagent's execution.

Checker development note: the first independent invocation exited 1 because it incorrectly assumed the accepted-science INDEX already contained all preparation literature entries (178 versus 227). Its output is retained as `initial-checker-results.json`. The final checker inventories the current 227 retained provisional aliases and separately reports 49 preparation additions, zero removals; substantive coverage of those additions is assigned to the literature reviewer. This initial checker assumption is not a repository finding.

No mathematical proof checker or numerical benchmark was rerun in this preparation-only review. Source hashes and the exact executed final checker permit reproduction of the bounded passes; they do not approve the new summaries despite those structural passes. **Return the preparation corrections to WORK; retain the accepted science and allocations.**
