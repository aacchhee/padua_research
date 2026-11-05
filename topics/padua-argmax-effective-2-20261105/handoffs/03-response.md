# Handoff 03 — padua-argmax-effective-2-20261105 — Codex response to Claude audit-01

- Status: done in 104eb44fdd77afc422597540c8852d67570dfc4d
- Previous handoff: 02-audit.md (done in 340ec24b3e7a837814a30b088141aa1ef67b8317)

- Next agent / model / effort: Codex. Orchestrator and any mathematical wording or attribution decisions: gpt-6-astra ultra, continuing AC's 2026-11-03 instruction for this problem (handoff 01). Purely mechanical edits may use gpt-6.1-sol medium. Record actual models in trailers and LOG.
- Role: developer (responding to audit)
- Branch: codex/padua-argmax-effective-2-20261105
- Input head SHA: `340ec24b3e7a837814a30b088141aa1ef67b8317` (audit-01 output; the commit publishing this handoff comes later)
- Main / base: `aff30e8` (merged into the topic at `3707a5f`)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 (configured; xhigh requested) · 2026-11-05

## Task

Answer every finding of [audit-01.md](../audit-01.md) in a new `response-01.md`. For each of F1–F12 and E1–E8, give one of:
- the fix, with file and line;
- an evidence-based rejection;
- an explicit unresolved item.

Never edit audit-01.md.

1. **F1 (MAJOR), T06 attribution.** Edit `theory/corner-global-norm-ratio.md`, the H2/H3 gate, the IDEA record and the "For the paper" sentence in report.md:
   - add the predecessors (LIT-312 Theorem 3, LIT-379, PD-T216+PD-T157 and the PD-T227 scope note);
   - restate T06 as an explicit-constant re-derivation of a known O(log² n) theorem;
   - make no "first explicit constant" claim without an inspectable source check. Bos et al. 2006 fulltext is a pending reference.
2. **F2 (MAJOR), T07 attribution and scope.**
   - Cite PD-T227 §Scope (8) and PD-T228 (2^-17/n², eventual, log n ≥ 10^7) as closest predecessors, and state the separation: every n ≥ 2 with an explicit constant.
   - Replace "strengthens … beyond PD-T251" with the true range, n ≥ 473. Present the all-degree usable radius as max(1/(2N³), 10^-11/n²).
   - Apply the same wording in report.md, LOG (as a new dated entry; do not rewrite old entries) and proposed-record-changes.md (CURRENT/PAPER_MAP text).
3. **F3, A0 criterion.** Add a dated criterion-interpretation entry to gates.md about the R1 reopening rule (≤ 10^4) versus the sharpened 7076–8592 value. State your reading. Audit-01's reading: the criterion targets the inherited coarse route, so it is not met. Preserve this as an item for AC's decision.
4. **F4–F5, classification proposals** in proposed-record-changes.md:
   - T01 identities become verification of PD-T215/216/218/223/225/226/228. The orbit formula is a generalization of PD-T228 eq. (3).
   - Register one narrow sufficiency-reduction PD-T, or defer it; audit-01 recommends registering it.
   - T02 is not registered.
   - Fix T01 line 55 and T02 line 73 (cite T04). Add the C-range provenance (PD-T247/252).
5. **F6:** propose a scoped MEASURED record for the phase/projection/box-pilot measurements, or give a reason for none. Cite PD-T232/233/247.
6. **F7:** give explicit dispositions for:
   - box-pilot outcome in ideas/H1.md;
   - signed-polynomial Markov route (equivalent to PD-T227 (6)–(7), or deferred);
   - cell-integral envelope route (deferred, with a resume condition);
   - T04 sub-variant (provisional IDEA label);
   - phase-dependent-log full-diamond profile.
   Also fix the IDEA-320 gate row.
7. **F8:** add the H1 record-ordering (d98613e vs 50bcbb4) and delegated-read disclosures, plus a LOG novelty-gate entry.
8. **F9:** add a second-corner reflection argument or exact citation, with a status row, in T05 and T07.
9. **F10:** cite T03 in N01, or make the sentence a remark.
10. **F11:** correct the reproduction commands (`--output`, no `-I` for scripts importing `phase_probe`). State the scope of structure_probe in gates-structural.md.
11. **F12:** state whether the 40 pending-local outputs still exist in the Codex sandbox, and update COLD_STORAGE.md/cold-storage.json accordingly. If they are not retained, say "not retained; regenerable except timing". Never claim delivery.
12. **E1–E8:** apply them or say why not.

Then:
- Update LOG and results.
- Re-pin evidence-manifest.json and the reviewed hashes for every changed file.
- Run `git diff --check`.
- In response-01.md, state whether any statement, proof step, constant or status changed.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- audit-01.md (complete), LOG.md, and every file named in the findings.
- The cited predecessor records:
  - topics/padua-argmax-alln-20261101/theory/gated-codex-13 (§Scope) and gated-codex-14;
  - literature/lattice-unisolvence/records/padua-2006.md;
  - topics/padua-proof-attempts-2-20261101/attempts/T-A2.md;
  - the literature/INDEX.md rows for LIT-312 and LIT-379.

## Scope limits

- No new mathematics, runs or claims are required. Do not reopen accepted proofs.
- If you do change a statement, proof step, constant or status, say so explicitly. That returns the topic to AUDIT for a mathematical re-audit.
- PD-T099 stays OPEN and the global range stays exactly 2–32. Remaining H1/H2 research (verified phase-box predicates and checker, full-diamond profile/remainder, explicit N1, bridge arithmetic) stays OPEN. It is not part of this step.
- No final ID assignment and no merged-registry edits; literal proposals stay in proposed-record-changes.md.
- Reservation T364–375/N132–137/IDEA454–465/LIT594–597 stays intact.
- Never merge, force-push, change tags, settings or `.github`. Only AC merges. No external machine without AC's permission.

## Acceptance and outputs

- `response-01.md` answers every finding.
- LOG, results, manifest and hashes are updated, and the diff check is clean.
- Commit the outputs first. Then, in a following commit, set this handoff to `done in <sha>` and open handoff 04:
  - if no statement, proof or status changed: a Claude response check (Opus 5.5 high), then PR preparation;
  - otherwise: a Claude mathematical re-audit (Opus 5.5 xhigh).
- Push before replying.
