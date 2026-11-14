# Handoff 08 — padua-effective-cubature-20261112 — PR preparation after accepted audit 03

- Status: done in `47892f13411132488a82e9dcd512d80dc543cd71` (PR preparation; readiness check in [09-readiness.md](09-readiness.md))
- Previous handoff: [07-narrow-review.md](07-narrow-review.md)
- Next agent / model / effort: **Claude, Sonnet 5.5, high** (technical PR preparation under WORKFLOW's model allocation)
- Role: topic orchestrator / PR preparer
- Branch: `claude/padua-effective-cubature-20261112`
- Input head SHA: `7d796dde11e274dd11919adcf4f7f17949d4a6fc`
- Main / base at audit: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`
- Stage: PR preparation; not ready for merge
- Written by / date: Codex audit orchestrator with gpt-6-astra high record reviewer · 2026-11-14

## Task

Prepare existing draft PR #34 for the auditor's readiness check. Audit 03 accepts response 02 within the narrow scope; all substantive reviews and responses are preserved. There are currently no reserved ranges or final IDs for this topic. Do not start another scientific development/audit campaign.

1. **Refresh and reconcile.** Read current rules and the topic records, fetch main and the topic, record their full SHAs and preserve unrelated work. Merge current main into this already-published branch only if needed; never rebase/force-push published history. Reconcile shared state semantically, preserving every other topic's content.
2. **Inventory and reserve fresh ranges.** Follow WORKFLOW's complete reservation procedure before assigning any final ID:
   - Refresh main and every open PR including drafts. Inspect all relevant ledgers, final IDs and retired reservations; account for closed-unmerged PR reservations not yet preserved as retired.
   - Compute maxima separately in PD-T, PD-N, IDEA and LIT. Reserve strictly above every used/reserved/retired ID, with appropriate headroom; never reuse gaps or shift another reservation.
   - Record namespace/range/count/owner/heads/date and published reservation provenance in the applicable ledger and PR body. Use this topic's ledger unless an existing applicable batch ledger is required by the actual integration scope. Link the ledger as WORKFLOW requires. If provenance/collision cannot be resolved without renumbering accepted IDs, stop only that allocation and refer the concrete conflict to AC.
   - Expected claim inventory is six PD-T records (-01/-02/-03/-04/-05/-07), one PD-N (-06), candidates 01–07 and two source records. **Verify the actual full provisional inventory before sizing ranges**; these counts are guidance, not a reservation or permission to drop aliases/candidates.
3. **Canonicalize accepted records.** Assign final IDs only from the published reservations; preserve every provisional-to-final mapping and alias. Prepare durable theory/negative/idea/literature records in the repository's established format, retaining exact accepted statements, hypotheses, quantifiers, statuses, dependencies and scoped candidate dispositions. In particular:
   - C0's finite/eventual ranges and literature-comparison limits;
   - Delsarte exactness conventions and local versus literature dependencies;
   - the compact-support witness versus general-L1 explicit gamma;
   - the 2–109 torus limitation with M≤8N, not a wider obstruction;
   - measured LP values, unestablished preregistered KILL and discretionary deferral;
   - the retrospective gate history and S4 attribution.
   Do not manufacture a new scientific claim, consolidate away an accepted substantive record or upgrade a status while formatting.
4. **Apply shared registries by reviewed diff.** Update the topic's scientific entries in `state/IDEAS.md`, `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `literature/INDEX.md`, topic/state indexes and the root `RESULTS.md` section as appropriate. Create formal LIT records for the two accepted source transcriptions if required by repository conventions. Preserve all other topics' sections and accepted IDs. Put only scientific content/status/dependencies/dispositions and completed-audit links in shared registries; pending audit/PR/preparation process belongs in LOG, handoffs and PR body.
   - Prepare the topic results' canonical scientific summary and apply only that topic's corresponding section to root RESULTS.md. Do not copy stale process-history paragraphs into the shared scientific view or regenerate another topic's results.
   - Remove completed initialization/preparation tasks from the shared frontier or state their actual post-merge scientific state. Keep detailed process history in the topic log.
5. **Validation and evidence.** Check all final/provisional mappings, links, reserved ranges and changed registry rows against the accepted sources. Run the small relevant manifest/link/format checks; no full unchanged lattice or LP rerun is needed. Do not hash-pin prose into new checkers. No result-bearing code/input/evidence changed in response 02, and audit 03 did not introduce a new computer proof.
6. **Preserve verification limits.** The optional Codex data-dependent gamma/compact/FT replay still could not run because the ancillary download returned HTTP403. Existing independent Opus and developer runs remain their own executions; bounded Codex controls are not a full coefficient replay. Carry this distinction, the explicit arithmetic trust base and inherited cold-storage pending item into the PR. Do not commit third-party coefficients/PDFs/extracts or claim an unperformed execution. If access becomes available and a replay is performed, record exact input/code/output identities and actual result; no denial bypass.
7. **PR #34 and readiness request.** Keep WORK/AUDIT/PR sections up to date around the final canonicalized implementation, audited source/rule SHAs, allocations, validation and limitations. Keep the PR draft until readiness. Normal final-ID/registry application is checked by the auditor's reviewed diff and reservation refresh, not a fresh full mathematics audit; any material scientific change beyond the accepted scope returns for a focused review.
8. **Integration only if relevant.** If this preparation actually requires a multi-PR integration batch, follow WORKFLOW's ledger and disposable sequential-squash rehearsal rules. A standalone topic against current main does not by itself authorize merging other branches. Never merge the real PR; only AC merges.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at the current branch head; record the full rules SHA.
- LOG, audit-01/02/03 and response-01/02; handoff 07 and the separately committed third-round MINOR fix `52e668438142a0a54bb78cf9ac74bf833270011a`.
- All topic theory, candidates/novelty gates, literature-effective.md, report, evidence manifest and its results file.
- Current shared registries, ledgers on main/all relevant PR heads, and the existing PR #34 description before replacing it. The allocation authority is the union of reservations, not this handoff's expected counts.

## Scope limits

- No new proof development, gamma optimization or cube-LP expansion. Do not reopen accepted mathematics merely to repeat audits.
- No main mutation, merge of PRs, force-push, tags, settings or .github changes. Only AC merges.
- No changes to another branch's reservation or accepted identifiers. Preserve disagreements, provenance and all candidate dispositions.

## Acceptance and outputs

- A durable PR-preparation record identifies source/rule/base/head SHAs, complete provisional/final mappings, published reservations and heads checked, shared-file diff scope, actual validation and remaining limitations.
- Canonical theory/idea/negative/literature entries, shared registry rows and the topic's RESULTS.md section agree exactly with the accepted records. No pending process appears in shared scientific registries.
- PR #34 stays draft with a concrete readiness request. An independent **Codex gpt-6-astra high readiness check** reviews the registry/ID diff and refreshes the reservation union against current heads. Repeat that refresh if relevant main/ledger heads change before AC's merge. This is not permission to merge.
- Commit/push preparation outputs first. In a following commit close handoff 08 `done in <output-sha>` and open handoff 09 for that readiness check, or a narrowly identified material-change review if actually necessary. Keep exactly one open handoff while work remains.
