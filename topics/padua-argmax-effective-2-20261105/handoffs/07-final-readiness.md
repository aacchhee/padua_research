# Handoff 07 — padua-argmax-effective-2-20261105 — final readiness bookkeeping

- Status: done in c094182a223da10c9f97ec7e832b8914594dce2a
- Previous handoff: 06-preparation-audit.md (done in 205fcb644559409501dc94a0a11ba66721977ecb)

- Next agent / model / effort: Codex, gpt-6.1-sol medium. This is mechanical bookkeeping; no mathematics. If a registry or classification decision unexpectedly arises, stop and use gpt-6-astra ultra per AC's standing instruction. Record the actual models.
- Role: orchestrator (readiness bookkeeping)
- Branch: codex/padua-argmax-effective-2-20261105
- Input head SHA: `205fcb644559409501dc94a0a11ba66721977ecb` (preparation-audit-01 output; the commit publishing this file comes later)
- Main / base: `330fab835f43e5ba5b24e320c2d7e9647e6cbd60`
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 (configured; high requested) · 2026-11-05

## Task

[preparation-audit-01](../preparation-audit-01.md) accepted registration, allocation, preservation, rehearsal and the PR body. Finish the readiness bookkeeping for AC's merge decision:

1. **Live refresh.** Fetch `main` and every open PR, drafts included. Record their SHAs. At handoff: main `330fab8`, #21 `67b3e01`, #24 `45646d7`.
   - If main moved, merge `origin/main` without rewriting history and re-run `preparation/check_registration.py` with a fresh baseline.
   - Repeat the reservation union check for T364–375/N132–137/IDEA454–465/LIT594–597 against every live and retired ledger. Record the result.
2. **Rehearsal.** If any foreign head moved since the pins above, re-run the squash rehearsal (`preparation/rehearse_integration.py`, external `--output`) at the live heads. Otherwise cite preparation-audit-01 check 6, which ran these exact heads.
3. **Results.** In both `results/padua-argmax-effective-2-20261105.md` and this topic's section of `RESULTS.md`, replace "required Claude preparation audit remains pending" with a link to preparation-audit-01 recording acceptance. Keep the two copies equal modulo the `../topics/`→`topics/` normalization.
4. **Re-pin.** Re-pin `evidence-manifest.json` to the new source commit, retaining previous-index provenance. Historical audit and response pins stay as reviewed.
5. **PR25 body.**
   - AUDIT: preparation-audit-01 ACCEPTED (Claude Opus 5.5 high), with P1–P3.
   - PR: fresh live pins, replacing the stale PR24 `3a179f6` statement (P1), and the current head.
   - Keep the AC items unchanged: the broader A0 reading; physical cold-storage delivery; fulltext priority for T06/Bos 2006 and T03's generating-curve analogue.
   - State the exact decision requested from AC: whether to merge PR25 (squash) after these checks.
6. **Storage (P2).** Re-hash the 40 local outputs if they are present, or record "not retained; regenerable except timing and hardware-dependent capped frontiers". Never claim delivery.
7. **Hygiene.** Run `git diff --check 330fab8 HEAD`, the link check, the JSON/16 KiB checks and the cold-storage plan.

You may mark PR25 ready for review once steps 1–7 pass, or leave it as a draft if AC prefers; record which. Never merge.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- LOG; preparation-audit-01; preparation/record.md; the current PR25 body.

## Scope limits

- No change to any Statement, proof, constant, status or final ID. Any such change returns the topic to AUDIT.
- No new mathematics or science runs. PD-T099 stays OPEN; global range exactly 2–32. Remaining H1/H2 research belongs to a later topic.
- Never renumber IDs or touch other topics' rows or sections.
- No main push, merge, force-push, tags, settings or `.github`. Only AC merges.

## Acceptance and outputs

- The refreshed receipts, the results update in both copies, the re-pinned index and the updated PR25 body are complete.
- Commit the outputs first. Then, in a following commit, close this handoff:
  - **If nothing material moved:** record in the LOG that the topic awaits AC's merge decision, and open handoff 08. Its body names only AC's decision and the post-merge follow-up: if PR25 is merged, close the topic and record completion in the LOG; if not, AC's instruction defines the next step.
  - **If a foreign or main movement changed shared registries:** instead open a Claude re-check handoff (Opus 5.5 high).
- Push before replying.
