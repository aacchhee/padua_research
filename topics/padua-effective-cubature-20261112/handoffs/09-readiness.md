# Handoff 09 — padua-effective-cubature-20261112 — Codex readiness check (registry/ID diff and reservation refresh)

- Status: open
- Previous handoff: [08-pr-preparation.md](08-pr-preparation.md)
- Next agent / model / effort: **Codex, gpt-6-astra, high**
- Role: independent auditor (readiness check)
- Branch: `claude/padua-effective-cubature-20261112`
- Input head SHA: `47892f13411132488a82e9dcd512d80dc543cd71` (the preparation outputs; the commit publishing this file comes later)
- Main / base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`
- Stage: READINESS
- Written by / date: Claude, configured `claude-opus-5-5` (AC's prompt named Sonnet 5.5 high) · 2026-11-14

## Task

Run WORKFLOW's single readiness check, and write `readiness-01.md`.

1. **Reservation refresh.** Repeat WORKFLOW steps 1–3 against current heads:
   - main, and every open PR, including drafts (PR27, PR35 and any new one);
   - any newly closed, unmerged PR.
   
   Confirm that the reservation in `ALLOCATIONS.md` (commit `de39dab`; PD-T674–683, PD-N246–250, IDEA-756–765, LIT-716–720) has priority and collides with nothing. Record the heads checked.
2. **Registry/ID diff review.** Review `git diff b5388c2 47892f1 -- PROOF_STATUS.md state/IDEAS.md state/CURRENT.md literature/INDEX.md ID_CROSSWALK.md RESULTS.md` against the accepted records (theory files, novelty gate, literature-effective.md, audits 01–03, response-01/02). In particular check:
   - every provisional→final mapping in `pr-preparation/final-id-map.json` and the crosswalk, with no alias receiving two IDs;
   - that statements, statuses, dependencies and dispositions match the accepted records exactly, without upgrades. Note the C0 ranges, the Delsarte exactness conventions, PD-T678 (compact) versus PD-T679 (general-L¹), PD-N246 limited to n = 2…109 with M ≤ 8N, the Q2 "KILL not established" disposition, and the retrospective-gate disclosure with S4 attribution;
   - that no pending process appears in the shared scientific registries;
   - that no other topic's content changed.
3. **Validation spot-checks.** Links and table formatting, and `python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify`. No scientific rerun is needed: no result-bearing code or evidence changed.
4. **Limitations to carry into the PR.** These are not to be relabelled: there is no Codex cross-agent γ/compact/FT replay (HTTP 403), and cold-storage archival is pending.

## Scope limits

- Readiness check only. Fix eligible MINOR registry wording in place under the third-round rule, in separate commits. Return material scientific changes for a focused review.
- No merge, force-push, tags, settings or `.github/` changes. Only AC merges.

## Acceptance and outputs

- `readiness-01.md` with model and effort, the heads checked, the reservation verdict, the diff verdict and the remaining limitations.
- **If ready:** mark PR #34 ready for review as WORKFLOW permits, with a merge request to AC. Then close this handoff and record the post-readiness state.
- **Otherwise:** open handoff 10 for the Claude fixes.
- Repeat the reservation check if main or any open PR's ledger changes before AC merges. Keep exactly one open handoff.
