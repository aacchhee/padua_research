# Handoff 04 — padua-lanczos-nonproduct-20261105 — developer response to audit 01 (with AC decisions)

- Status: open
- Previous handoff: [03-response.md](03-response.md). This handoff supersedes it after AC decided Q1–Q3 on 2026-11-06, and carries the complete instruction.

- Next agent / model / effort: Codex.
  - Coordinator: gpt-6-astra high, following AC's 2026-11-05 allocation recorded in handoff 01.
  - Mechanical record edits may use gpt-6.1-sol medium.
  - The A3 statement correction is mathematical record work: use gpt-6.1-sol high.
- Role: developer and topic orchestrator
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `0a8a34f75e3e905c93595d860bbe1b4299e801d6`, the commit recording AC's Q1 decision. The audit output is `ea13ed4a6cdc97dcd43f71a68d31681dcd9676d6`. The commit that publishes this file comes later.
- Main / base: `be9a8318150204711d5446d2ea26284cf1ed0819`. Fetch main first; if it has moved, merge `origin/main` into the branch. Never rebase published history.
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 xhigh (configured) · 2026-11-06, after AC: "Q1 is accepted." and "Yes agree with both suggestions".

## AC decisions (2026-11-06; canonical record in LOG)

- **Q1:** the disclosed P3 gate-timing deviation is accepted with the qualifier proposed in audit-01 A2.
- **Q2:** the P3 result is accepted as the answer to the formal goal, recorded as a weaker variant. An n-independent perturbation remains an OPEN, deferred follow-up target; it is not a precondition for this PR.
- **Q3:** the P3/P5 proofs without the N2 screen are accepted as a dated deviation. No new scans are required for this PR; an optional Padua scan goes under Runs needed.

## Task

Answer every finding in [audit-01.md](../audit-01.md) in a new `response-01.md`. For each finding, give one of:
- a fix, with commit and location;
- an evidence-based rejection;
- an explicit unresolved item.

Do not edit audit-01.md.

1. **A1 (MAJOR), P3 framing.** Fix the wording only; do not change the P3 theorem statements.
   - State plainly that μ_(n,η) agrees with SH_n on all moments through degree 2n+1. Hence Gram matrices, monic basis, creators, pivots, source scales and the frozen-response map are η-independent, and only the ambient normal projector changes. Put this in:
     - the P3-03 Scope;
     - the report headline (`report.md:11-19`);
     - the N4 row of `gates.md`;
     - the paper-consequence paragraph (`report.md:211-219`);
     - the results file and the PR body.
   - Use this as the P3 result's title/scope wording for later registry and paper use: "non-affine-product measures moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight mode".
   - Record once in LOG that the reading allowing an n-dependent weight mode was the Codex coordinator's decision (`attempts/P3.md:14-16`), and link AC's Q2 decision.
   - Add a candidate record for an n-independent perturbation, either one fixed smooth density 1+eta*phi(s,t) or a nonlinear node map.
     - Its IDEA disposition is `deferred`. The resume condition is a follow-up topic.
     - Its first step is a perturbation bound for the normal-quotient map using the degree-≤2n moments, under the original N4 kill test: η₀(n) decaying faster than every polynomial.
     - The record must say it is not a precondition for this PR.
   - Optional: one report paragraph interpreting P3 and P5 together. Both families are non-product and moment-close to product measures, yet they behave oppositely. That suggests the degree-≤2n moments and the normal space, not productness, are what matter. Label it as interpretation, not a theorem.
2. **A2 (MAJOR), P3 gate timing.** Complete the canonical LOG paragraph with items (a)–(d) of A2:
   - (a) when the proposal was made and what it said;
   - (b) which required reads were still incomplete;
   - (c) whether the gated candidate is identical to the proposal;
   - (d) that the gate-before-admission order rests on self-report, because both first entered Git in `6988024`.

   Add the A2 qualifier to the P3 IDEA record, with "AC decision 2026-11-06: accepted". Link the disclosure from elsewhere; do not repeat it.
3. **A3 (MAJOR), P1 chain rule.** Qualify the MEASURED chain g_j = 1/binom(2j,j) as holding under BJ, at:
   - `theory/p1-continuous-creator-probe.md:31-37` and `:132-134`;
   - `ideas/P1.md:192-194` and `:210`.

   If you add the mirror and alternating values, (1,0,…,0) per the audit recomputation, state who computed them. This is a material change to a recorded claim, so it receives a focused diff re-audit.
4. **MINOR 1–18.** Fix each or answer it in the response.
   - **MINOR 2** (N2 screen skipped before the P3/P5 proofs) needs one canonical dated LOG paragraph recording the deviation and linking AC's Q3 acceptance. In it:
     - add to Runs needed an optional exact Padua scan (degrees 2–16, four rules) as evidence for the OPEN sharp-exponent question;
     - state that no P3 scan is required.
   - **MINOR 16** (D4 symmetry): either weaken the wording or add the proof. Adding the proof is material and goes to focused re-audit.
   - **MINOR 11** (receipt provenance): keep frozen receipts byte-unchanged and disclose the provenance issues in prose.
5. NOTEs need no action. Address them only where convenient.
6. Update the LOG (stage and next step), the topic results file and the PR #30 body. The AUDIT section should summarise audit 01 and AC's decisions, and link both.

## Read first

- AGENTS.md, agents/WORKFLOW.md (Work cycle; Proportionate audit and records) and agents/codex/CODEX.md at the branch head.
- [audit-01.md](../audit-01.md) in full.
- The LOG entry "2026-11-06 — Claude audit 01", including AC's Q1–Q3 decisions.
- The records each finding names, at the cited lines.

## Scope limits

- **Do not reopen:**
  - the accepted proofs P3-01/02/03, P4, P5-01/02 and the P1/P2 admissions;
  - the reflection method;
  - the P6 finite outcomes;
  - the three INCONCLUSIVE N2 verdicts.
- **Not part of this response:** no new scans and no development of the deferred fixed-perturbation target.
- **Storage:** AC decided on 2026-11-06 that storage is a separate cleanup topic, with no cleaning action while the repository stays under 10 MB (LOG). Do not move, delete or compact evidence for storage reasons.
- **Final IDs and registries:** no final IDs or reservations yet, and no shared-registry edits. Those belong to PR preparation after the response and any focused re-audit.
- **AC decisions:** Q1–Q3 are decided. Do not re-ask them.
- **Authority:** no rule or `.github/` changes, no force-push, no tags, no merge. Only AC merges.

## Acceptance and outputs

- `response-01.md` answers every finding.
- The fixes are committed, and all records are consistent with them and with AC's decisions.
- The material changes (A3, and MINOR 16 if you add a proof) are listed explicitly with their commit and diff range, for focused re-audit.
- If no material change was made, state that, so the topic proceeds to PR preparation per WORKFLOW. The AC-directed wording and record additions are not material for this purpose.

Commit the response outputs first. In a following commit, set this handoff's status to `done in <response-output-sha>` and add handoff 05:
- if a material change exists: Claude, Opus 5.5 high, focused re-audit of exactly those diffs, plus the readiness inputs;
- otherwise: PR preparation (reservation, final IDs, registry edits by reviewed diff), with a Claude readiness check.

Push, then reply with the short continuation prompt.
