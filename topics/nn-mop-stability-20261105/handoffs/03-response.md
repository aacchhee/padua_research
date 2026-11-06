# Handoff 03 — nn-mop-stability-20261105 — Codex response to audit-01

A new numbered file each time work passes to another agent or session, opened by the orchestrator holding the previous handoff. Never overwrite an earlier handoff or alter its body; only the status line changes. AC starts the step with `<Agent> (<model, effort>): Continue <branch>.`

- Status: open
- Previous handoff: [02-audit.md](02-audit.md)

- Next agent / model / effort: Codex, `gpt-6.1-sol` high (mathematical development row: the response corrects proof text and measured statements). Use `gpt-6.1-sol` medium for purely mechanical record edits.
- Role: developer and topic orchestrator for the response
- Branch: codex/nn-mop-stability-20261105
- Input head SHA: `a977a44b060e798baed80e70cba61d844b7aab60` (audit-01 outputs; the commit that publishes this file comes later)
- Main / base: `be9a8318150204711d5446d2ea26284cf1ed0819`, merged into the branch at `67248ce`
- Stage: WORK
- Written by / date: Claude, Opus 5.5 xhigh · 2026-11-06

## Task

Answer every finding of [../audit-01.md](../audit-01.md) in `topics/nn-mop-stability-20261105/response-01.md`. For each finding, give one of:
- a fix, with file:line;
- an evidence-based rejection;
- an explicit unresolved item.

Work in this order.

1. **M1.** In theory/dictionary-obstructions.md:55–57, correct the w2 moments to (15,34,90,250) and the equation to 15c0+34c1=−90. Keep the solution (32/23, −75/23) and the conclusion ⟨P,x⟩ = −30/23. Check the whole proof text against code/dictionary_probe.py output.
2. **M2.** Disclose platform dependence of every binary64 number in attempts/D3.md, attempts/D5.md, candidates-D3-D5.md, theory/native-measurements.md and theory/backward-projection-measurements.md:
   - record the producer platform: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0;
   - replace "deterministic" with "deterministic on the recorded platform";
   - replace the "≤30u / below 30u" nodeqr statements (D3.md:132, candidates-D3-D5.md:98, backward-projection-measurements.md:17) with "<100u" or a platform-qualified value. The audit platform gives Krawtchouk N4 nodeqr η_c = 30.78u.

   Keep the 100u conclusions. Do not re-select or re-tune any run.
3. **M3.**
   - Commit the returned rational N4 and N8 projection witnesses, both families and all methods, as small JSON evidence. If you prefer not to commit them, record their SHA-256 together with the producer platform.
   - Make code/independent_check_followup_projection.py compare against the committed identity rather than against regenerated `/tmp` receipts.
   - Per AC (2026-11-06), size is not an issue while the topic stays under 10 MB; take no storage cleanup actions.
4. **M4.** Add provisional IDEA records, retaining all others, for:
   - handoff01 D3 candidates (a) NN core transformations, (b) lattice biorthogonal Lanczos and (c) multi-path step-line redundancy under zero curvature;
   - the D1 alternatives named in handoffs/01-work.md:58: Vandermonde conditioning and potential-theoretic node density.

   Each record needs:
   - closest entries: LIT-347 IEP_CORE, IDEA-378/379, IDEA-031/090, as relevant;
   - a `deferred` or not-attempted disposition, with reason and resume condition;
   - one line on why designs A/B were pursued instead.

   This does not reopen D3.
5. **MINOR 1–16.** Fix all of them as worded in audit-01.
   - Where evidence-manifest.json pins a prose file you edit, update that pin in the same commit (be9a831 rule).
   - Replace proposed-record-changes.md with a short note: under be9a831, registries are edited directly at preparation and reviewed by diff, process stage is never written into registries, and IDEA-378 stays `deferred` with its resume condition.
   - For MINOR 12, replace the bare asserts with explicit raises and compare code hashes against the pins. Rerun `python topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py` and record the result. The finite theorem's statement must not change.

Then:
- update LOG.md (one entry), report.md and results/nn-mop-stability-20261105.md honestly;
- update draft PR #28's WORK section;
- set the stage to AUDIT for a focused Claude re-audit.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head. Main be9a831's "Proportionate audit and records" section now applies to this topic.
- [../audit-01.md](../audit-01.md) in full, and [../audit-01/README.md](../audit-01/README.md) for the auditor's scripts and commands.
- LOG.md, the 2026-11-06 audit entry.
- The theory, attempts and candidate files named in each finding.

## Scope limits

- Do not change any claim, status or result that audit-01 accepted, beyond what a finding requires.
- Every change to a proof, measured value, evidence, candidate disposition or status is material and goes to a focused re-audit.
- Do not edit audit-01.md or the audit-01/ scripts. Disagreements go in response-01.md for AC.
- No final IDs or shared-registry edits yet. Those happen at PR preparation, followed by the readiness check, which includes the reservation refresh against main and every open PR. The ranges T432–471, N162–177, IDEA530–569 and LIT614–629 stay reserved.
- No main commits, merges of PRs, force pushes, tags or `.github/` changes.
- No Leuven contact.
- G5 stays BLOCKED unless AC changes network access.
- Only AC merges.

## Acceptance and outputs

- response-01.md answers every audit-01 finding: M1–M4 and MINOR 1–16, with NOTEs optional.
- The fixes are committed. When an evidence pin is affected, the evidence manifest and its pins are consistent in the same commit; `conditioning_verify_normality.py` passes.
- LOG, report, results and the PR #28 WORK section are updated; the stage is AUDIT.
- Commit the outputs first. Then, in a following commit, set this handoff's status to `done in <output-commit-sha>` and add handoff 04 for Claude: Opus 5.5 high, or xhigh if any proof text changes beyond M1. Handoff 04 covers:
  - a focused re-audit of the material changes only;
  - when that re-audit is accepted, PR preparation and the readiness check.

  Link handoff 04 in the log and end the reply with the short continuation prompt.
