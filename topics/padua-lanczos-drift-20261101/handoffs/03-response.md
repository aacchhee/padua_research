# Handoff 03 — padua-lanczos-drift-20261101 — developer response to audit-01

- Status: open
- Previous handoff: 02-audit.md

- Next agent / model / effort: Codex, `gpt-6.1-sol` xhigh for the mathematical rescoping (records 11, 14, 15, 32, and any record-05 status proposal); `gpt-6.1-sol` medium for code, checker and editorial items
- Role: developer / topic orchestrator
- Branch: codex/padua-lanczos-drift-20261101
- Input head SHA: `fc4effdb48dc7c0f766267edaf1e2ba855e0bf74` (audit-01 outputs; this file's publication commit comes later)
- Audited candidate: `36c93794ce02f92c76c89e5a9ec8095eb238d91d`; scientific source `b09e1dbe0baafd666cf0d779a671a40f55de2d75`
- Main / base: `806cc7b4509fd93bae652f9545d32d95529f8281`
- Stage: WORK (audit-01 verdict CHANGES REQUIRED)
- Written by / date: Claude, configured `claude-opus-5-5` xhigh (audit orchestrator) · 2026-11-01

## Task

Answer every finding of `topics/padua-lanczos-drift-20261101/audit-01.md` in a new file `topics/padua-lanczos-drift-20261101/response-01.md`. That is 10 medium and 32 low findings: E1-F1–F9, E34-F1–F10, E5-F1–F8, E6-F1–F7 and P-F1–F8. The exact locations, evidence and required responses are in the four reviewer reports under `checks/audit-01/`.

For each finding, give one of:
- a fix, with the commit and file:line;
- an evidence-based rejection;
- an explicit unresolved item for AC.

Never edit audit-01.md or the reviewer reports to resolve a finding. Preserve any disagreement for AC.

Do the medium items first:

1. **E34-F1, E34-F2 (record 15).**
   - Retitle and rescope record 15 as a generic fixed-degree, raw-product-source closure lemma, with T₃/BJ as the explicit instance.
   - State δ_F(1) (exactly δ_Y² = b²θ₂², i.e. (√3/2)δ_J) and the equality in (8).
   - Remove the "unformed J-product", "never formed" and non-product-support interpretation.
   - Credit PD-T055's heuristic span identity (bj-universal-reorthogonalization-obstruction-open.md:49).
   - Propagate to E4.md, IDEA?drift-codex-15 (redo its novelty verdict), report.md, local-results-entry.md and the PD-T055 proposal block in proposed-record-changes.md.
2. **E34-F3 (record 14).** Convert it to an IDEA disposition, recommended as REJECTED: ill-posed formalization of PD-T055's quantifier, together with the PD-T055 note. Or justify keeping a PD-N; in that case retitle it as a quantifier clarification, rewrite the attempted-mechanism line and cite PD-T032 part 2. Either way, remove record 15's dependence on record 14 for U(3).
3. **E34-F4 (record 11).** Add the perturbation-family dependence to the remainder, and state that no uniform remainder is asserted. Mirror this in E3.md.
4. **E5-F1 (record 32).** Rescope case 3 to the eventual-witness mechanism only. Add the remark that fixed-A paths contain finite-n negative points, since η_{n₀}(a/n₀) = ζ_{n₀}.
5. **E1-F1 (pivot tie).**
   - Make `e1_exact.py` detect and record pivot ties.
   - Disclose the rotQ24 (2,1) tie and its 90° symmetry cause in record 04, E1.md and e1-summary.
   - Label the rotQ24 pivot values as X-tie-broken.
   - State that T24 pivot has no tie.
6. **E1-F4 (freeze provenance).**
   - Reconcile E1.md:53/67 and record02:90 with e1-freeze.json.
   - Disclose that 6920ba6 already contains Urow, and add per-field frozen flags or a note.
   - Note that the sharpened-U DEAD rule would fire at low degrees.
7. **E6-F1.** State the midpoint test distribution, or add a uniform or boundary-inclusive test set. Restate the reported test errors accordingly.
8. **P-F6.** Add PD-T042/IDEA-141, PD-T043/IDEA-142–144 and IDEA-139 as closest predecessors of record e1-03 and IDEA?drift-codex-04, with a separation.
9. **P-F1.** Deliver your scientific ZIP and the off-repo artifacts to `C:\Users\andreyac\Downloads\padua\cold_storage\padua-lanczos-drift-20261101\` with a readback receipt. The bridge works when the session is linked to AC's computer; the audit-01 outputs are already in its `audit-01\` subfolder. If you cannot deliver, state explicitly that verification rests on committed compact evidence plus regeneration.

Then address the low items, including:
- E1-F5: state why record 05 stays MEASURED, or propose the finite computer-assisted PROVED (keeping factor10 INCONCLUSIVE and the post-hoc labels);
- E1-F3: commit a checker for record 04's six inequalities, with its output;
- E1-F2: replace the tautological trace check;
- E5-F5: add the missing literal PD-T075 and PD-T069 proposal blocks;
- the stale "pending" lines, the template conformity of ideas-e6, and the LOG link to handoff 02.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at the branch head; this topic's LOG.md (the audit-01 entry); audit-01.md; all four files in checks/audit-01/; the records and files named in each finding.

## Scope limits

- Existing old theory files and shared registries stay unchanged until PR preparation.
- Final IDs remain unassigned. The permanent reservations stay T136–155, N062–071, IDEA246–285 and LIT445–459.
- No main commits or pushes, no PR merges, no force pushes, no tags, no `.github/`, no vendored source or fulltext.
- Do not count your own fixes as independent acceptance.
- Only AC merges.

## Acceptance and outputs

- `response-01.md` with a disposition for every finding ID.
- The changed records, code and evidence, with updated manifests and hashes.
- A LOG entry, and PR #15's AUDIT section updated with the audit-01 text from the end of audit-01.md. This session could not write to GitHub.

Material scientific changes return the topic to AUDIT. These are: the rescope of record 15 or 14, the record-32 scope, any status change of record 05, and any new checker that carries a claim. In that case, commit the outputs, then in a following commit set this handoff to `done in <sha>` and open `04-reaudit.md` for Claude (Opus 5.5 xhigh) with the exact SHA and the changed-claim list. If only editorial or documented resolutions remain, open a PR-preparation handoff instead. Keep exactly one open handoff. Only AC merges.
