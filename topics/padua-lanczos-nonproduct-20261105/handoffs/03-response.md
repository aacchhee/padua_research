# Handoff 03 — padua-lanczos-nonproduct-20261105 — developer response to audit 01

- Status: open
- Previous handoff: [02-audit.md](02-audit.md)

- Next agent / model / effort: Codex. Use gpt-6-astra high as coordinator, following AC's 2026-11-05 allocation recorded in handoff 01. Mechanical record edits may use gpt-6.1-sol medium. The A3 statement correction is mathematical record work, so use gpt-6.1-sol high.
- Role: developer and topic orchestrator
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `ea13ed4a6cdc97dcd43f71a68d31681dcd9676d6` (the audit-output commit; the commit that publishes this file comes later)
- Main / base: `be9a8318150204711d5446d2ea26284cf1ed0819`. Fetch main first; if it has moved, merge `origin/main` into the branch (never rebase published history).
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 xhigh (configured) · 2026-11-06

## Task

Answer every finding in [audit-01.md](../audit-01.md) in a new `response-01.md`. For each finding, give one of:
- a fix, with commit and location;
- an evidence-based rejection;
- an explicit unresolved item.

Do not edit audit-01.md.

1. **A1 (MAJOR), P3 framing.** Fix the wording only; do not change the P3 theorem statements. State plainly that μ_(n,η) agrees with SH_n on all moments through degree 2n+1. Hence Gram matrices, monic basis, creators, pivots, source scales and the frozen-response map are η-independent, and only the ambient normal projector changes. Put this in:
   - the P3-03 Scope;
   - the report headline (`report.md:11-19`);
   - the N4 row of `gates.md`;
   - the paper-consequence paragraph (`report.md:211-219`);
   - the PR body.

   Record once in LOG the coordinator's decision that an n-dependent weight mode is within P3's scope (`attempts/P3.md:14-16`), labelled as a coordinator decision pending AC (Q2).
2. **A2 (MAJOR), P3 gate timing.** Complete the canonical LOG paragraph with items (a)–(d) of A2:
   - (a) when the proposal was made and what it said;
   - (b) which required reads were still incomplete;
   - (c) whether the gated candidate is identical to the proposal;
   - (d) that the gate-before-admission order rests on self-report, because both first entered Git in `6988024`.

   Add the qualifier proposed in A2 to the P3 IDEA record. Do not repeat the disclosure elsewhere; link it. AC's decision (Q1) is pending, so write the date placeholder as pending.
3. **A3 (MAJOR), P1 chain rule.** Qualify the MEASURED chain g_j = 1/binom(2j,j) as holding under BJ:
   - `theory/p1-continuous-creator-probe.md:31-37` and `:132-134`;
   - `ideas/P1.md:192-194` and `:210`.

   If you add the mirror and alternating values, (1,0,…,0) per the audit recomputation, state who computed them. This is a material change to a recorded claim, so it receives a focused diff re-audit.
4. **MINOR 1–18.** Fix each or answer it in the response.
   - MINOR 2 (N2 screen skipped before the P3/P5 proofs) needs one canonical dated LOG paragraph, linked to Q3.
   - For MINOR 16 (D4 symmetry), choose between weakening the wording and adding the proof. Adding the proof is material and goes to focused re-audit.
   - Keep frozen receipts byte-unchanged. Disclose receipt-provenance issues (MINOR 11) in prose rather than rewriting the receipts.
5. NOTEs need no action. Address them only where convenient.
6. Update the LOG (stage and next step), the topic results file and the PR #30 body. The AUDIT section should summarise audit 01 and link it.

## Read first

- AGENTS.md, agents/WORKFLOW.md (Work cycle; Proportionate audit and records) and agents/codex/CODEX.md at the branch head.
- [audit-01.md](../audit-01.md) in full, and the LOG entry "2026-11-06 — Claude audit 01".
- The records each finding names, at the cited lines.

## Scope limits

- **Do not reopen:**
  - the accepted proofs P3-01/02/03, P4, P5-01/02 and P1/P2 admissions;
  - the reflection method;
  - the P6 finite outcomes;
  - the three INCONCLUSIVE N2 verdicts.
- **Storage:** AC decided on 2026-11-06 that storage is a separate cleanup topic, with no cleaning action while the repository stays under 10 MB (LOG, 2026-11-06). Do not move, delete or compact evidence for storage reasons.
- **Final IDs and registries:** no final IDs or reservations yet, and no shared-registry edits. Those belong to PR preparation after the response and any focused re-audit.
- **AC questions:** Q1–Q3 in audit-01 were referred to AC by the Claude orchestrator on 2026-11-06. Record AC's answers in LOG if they arrive, and do not presume them.
- **Authority:** no rule or `.github/` changes, no force-push, no tags, no merge. Only AC merges.

## Acceptance and outputs

- `response-01.md` answers every finding.
- The fixes are committed, and all records are consistent with them.
- The material changes (A3, and MINOR 16 if you add a proof) are listed explicitly with their commit and diff range, for focused re-audit.
- If no material change was made, state that, so the topic proceeds to PR preparation per WORKFLOW.

Commit the response outputs first. In a following commit, set this handoff's status to `done in <response-output-sha>` and add handoff 04:
- if a material change exists: Claude, Opus 5.5 high, focused re-audit of exactly those diffs, plus the readiness inputs;
- otherwise: PR preparation (reservation, final IDs, registry edits by reviewed diff), with a Claude readiness check.

Push, then reply with the short continuation prompt.
