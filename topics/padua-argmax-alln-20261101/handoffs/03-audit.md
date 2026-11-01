# Handoff 03 — independent audit of Padua argmax part 3

- Status: open
- Previous handoff: 02-part3-work.md
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: independent mathematical auditor of Codex part3 development
- Branch: claude/padua-argmax-alln-20261101
- Input head SHA: `c70e8c0fe80338bb05ad7f7874dbfc20910f5d01` (scientific output commit; the following commit only publishes this handoff and closes02)
- Main/base: `2b52b432fe59c9a50aef9deebe5152c5d6874465`, rechecked unchanged
- Stage: AUDIT
- PR: [draft17](https://github.com/aacchhee/padua_research/pull/17)
- Written by/date: Codex, gpt-6.1-sol xhigh, 2026-11-01

## Goal

Audit the complete part3 development at the exact input SHA. The all-degree PD-T099 target remains OPEN. Do not start another proof campaign, allocate final IDs, alter shared registries, mark the PR ready or merge. AC alone merges.

Read AGENTS.md, agents/WORKFLOW.md and your role file at the branch head, then LOG.md, report.md, plan.md/ideas.md/gate.md, ideas-codex-fallback.md, results/padua-argmax-alln-20261101.md, all new theory records, attempts, input-snapshot.json and evidence-manifest.json. Read the **complete state/IDEAS.md**, relevant full candidates and obstruction/disposition tables: this branch carries mechanism and scoped negative content. Read literature/INDEX before attribution assertions. No 1-D literature theorem was transferred.

## Claimed new results and exact limits

- PD-T?argmax-alln-codex-02: PROVED n2 maximum3 only at(±1,−1), rational explicit proof/checker.
- codex-03: PROVED sufficient Bernstein certificate implication, strict corner leaves, integer outward rules and the general cardinal enclosure constructor.
- codex-07: PROVED n8 global argmax only at its two non-node corners, using the accepted PD-T179 field module and a complete34-leaf cover.
- codex-08: PROVED every9≤n≤16 via PD-T101's local all-n corrected-kernel cardinal theorem, rational Machin/Taylor enclosures and complete covers. Every new degree has distinct-agent replay. With inherited3–7 this gives2–16. No run>=17.
- codex-04: PROVED compact vertical defect limit and envelope max=Λc−min_I g_v+o(1), with positive compact lower bound. Neither center-minimality nor an effective rate is proved.
- codex-05: PROVED horizontal exact decomposition and positive compact defect limit. P2's horizontal envelope remains OPEN; no n↔n+1 swap imports the vertical phase estimates.
- codex-01: MEASURED T1–T5 planning tests. Literal/dated interpretations, unfulfilled general-beta series and inferred-vs-rigorous constants must remain distinguished.
- codex-06: MEASURED geometric pairing screens.
- PD-N?argmax-alln-codex-01: PROVED obstruction only to the precise tie-inclusive finite order O-Lt at n4, inheriting accepted PD-T165/166 roots/value bounds. No refutation of the original ambiguous pairing suggestion, other pairings or PD-T099.

P0 and a positive compact form of P1 close. P2 envelope, P3 corners, P4 interior, P5 strips and P6 effective threshold remain OPEN. Supporting results do not silently upgrade those targets.

## Mandatory mathematical scrutiny

1. Reconstruct the Bernstein implication including boundaries, exact corner-vertex equality and use of a common corner lower bound. Check outward conversion/subdivision, both parities' designated corners, full prefix cover and rejection of malformed/pending certificates.
2. Check PD-T101's explicit corrected kernel, endpoint weights, exceptional x mode, principal n8 embedding, rational π/cosine remainders, periodic cosine indices and exact node-symmetry argument. Independently replay consequential finite certificates; all artifacts are small and in Git.
3. Reconstruct04's compact-uniform tails, moving-pole tubes, parity Riemann density and maximizing-phase assembly. In05 check corrected horizontal normalization and outside-band numerator-difference tail separately.
4. Check N01's root-to-cell cosine inequalities, interval orientation and exact value reversal. Its whole original n4 proof was inherited, not replayed in this step. Distinguish list-cell maxima from whole-diamond suprema and unique/tied nearest-corner formulations.
5. Verify T2/T3 failures are finite planning evidence only; T4≈1.33e14 is an inferred sufficient-localization projection, not a rigorous n0. T1's literal corner issue and missing general-beta series remain explicit.
6. Original Claude observations were separately reviewed by Codex Astra in independent-checks-claude-observations-audit.md. C-01's strip wording is corrected in record02 with old wording preserved. All six prescribed replays match; standalone maj.py whole-square scans are unrerun. Do not count Claude reviewing its own old material as independent approval; retain the independent Codex audit scope.

## Reproducible commands

From repository root:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/check_evidence.py
python -B topics/padua-argmax-alln-20261101/code/part3/finite_n2_exact.py --output /tmp/padua_n2_claude.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_bernstein_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_pilot.json.gz --output /tmp/padua_n8_claude.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n12_pilot.json.gz --output /tmp/padua_n12_claude.json
python -B topics/padua-argmax-alln-20261101/code/part3/pairing_exact_check.py topics/padua-argmax-alln-20261101/outputs/part3/pairing_screens.json --output /tmp/padua_pairing_claude.json
```

Replay remaining n9–11/13–16 with finite_general_check.py and their finite_nN_general.json.gz certificates, writing separate audit outputs. Commands/hashes/timings/controls for every degree are in theory07/08 and independent-checks-part3.md. Code integrity checking alone is not a mathematical replay. Do not refresh/overwrite frozen evidence manifests or developer outputs to conceal a mismatch. Preserve your own small receipts; report actual commands and versions.

Supplementary checks already complete: Astra high finite+edge+T2–T4 and T1n12, separate Astra high pairing checker/reconstruction, Sol medium six original-script replay. These checks supplement this required Claude audit.

## Scope, reservation and outputs

Write audit-01.md and audit-support/ receipts under this topic, update LOG stage and its own results only as needed. Return findings; do not silently fix Codex development and count it independently approved. Scientific claim/code/evidence fixes go through a response and re-audit.

Reservation first published405febab in PR17: PD-T206–225, PD-N078–083, IDEA-316–335, LIT-460–465. No final IDs assigned. Topic-local ALLOCATIONS.md respects02's write scope; proposed shared ledger/crosswalk/scientific rows are in proposed-record-changes.md. Refresh main/all PR reservations before later assignment. Do not reuse permanent gaps.

Generated outputs currently2,127,404bytes; largest269,669bytes. No cold-storage dependency is needed. Preserve≤1MB/file and<5MB total topic evidence; no third-party fulltext.

Connector uses authenticated Andrey Chesnokov noreply commit identity and exposes no email override; this disclosed metadata limitation does not authorize rewriting published history.

Acceptance requires exact scoped verdicts, findings/dispositions, independently performed runs and residual limits. If changes are needed set stage WORK and open the next numbered handoff for Codex response with appropriate model. If accepted set PR and open the next numbered handoff for mechanical PR preparation (refresh union, final IDs, proposed shared edits, validators). The current proposal rows still need actual accepted-audit/final-ID text at preparation; do not apply pending-audit placeholders.

Commit audit outputs first. In a following commit close03 with its real output SHA and open04 with complete next instructions. Only the orchestrator holding this handoff numbers its successor; never overwrite earlier bodies. Push before replying, ending with the short continuation prompt for the next agent.
