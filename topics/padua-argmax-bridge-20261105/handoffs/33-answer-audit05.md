# Handoff 33: answer audit-05, fix the onset reader allowlist, one paired wording batch

- Status: open
- Previous handoff: 32-claude-audit-response04.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator. Development: Sol medium for code, Sol xhigh for the proof-clause edits, a distinct Astra high/xhigh agent for the focused re-check. Astra ultra only with a recorded written justification.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `8ab8285b8ea08a1122282e853db81e78eac48080` (audit-05 outputs, MINOR addenda at `acd0b1d`); this handoff is the following handoff-only commit
- Main / base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3` (merged at `941aa33`)
- Stage: WORK (MAJOR findings are open)
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; audit work by four Claude Opus 5.5 subagents instructed at xhigh (disclosure in audit-05.md). · 2026-11-13

## Authority

Pushes to this working branch stay authorized. No main push, merge, force-push, tag, settings or `.github` change, no external contact or submission,
no PR readiness. Only AC merges. AI declaration, ORCID, contributions and the draft marker are AC's. P1–P4 and the funding confirmation stand.
No new native campaign, retry or rescue, no changed thresholds, no final-ID assignment. Do not remove another topic's evidence.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at the current head (record the SHA); this handoff; [audit-05.md](../audit-05.md) and
[audit-05-manuscripts.md](../audit-05-manuscripts.md); the reports in [audit-05/](../audit-05/) for exact locations and the controls to reuse;
[audit-04/WHEN-INPUTS-ARRIVE.md](../audit-04/WHEN-INPUTS-ARRIVE.md).

## Task A (first): E5-01 reader allowlist (MAJOR) and the small evidence items

1. `code/local_onset512_campaign/return_bundle.py` lines 171–216: add `storage-dedup.json` (per pass) and the top-level `.preserve.lock` to the allowlist
   with schema or empty-file checks; the recorded 11,713 members fit 60 per case only with `storage-dedup.json` present. Add a **round-trip control**: run
   the real `compact_pack/storage.py deduplicate()` and `export()` on a synthetic campaign tree and feed the archive to the reader (positive case), keep all
   existing negative controls (the reviewer's 14 own reader controls in `audit-05/code/e5-code/` are a model), and keep optimization refusal. New reader
   identity; record it; focused re-review by a distinct agent; only then the canonical-ZIP run.
2. **E5-02** `onset512_analytic/check.py`: document `python3 -E -B` in every rerun command (it relies on 28 asserts and prints PASS under `-O` for a falsified
   copy); an optimization guard is optional. **E5-04** state the exact scope of the runtime probe (it cannot detect flush-to-zero when denormals-are-zero is also
   on; J03 lines 264–267 and the J3-05 disposition overstate it) or compare bit patterns. **E5-03** state this topic's own counted share (1,995,804 B = HEAD minus
   main), that main alone is 9,733,758 B, and the 2,087 B `FREEZE.md` exception convention, in the LOG, results and pr-update text; nothing else is needed.
   **E5-08** the README wording items beyond the dated notes already added by the auditor (the campaign README should say which runner ran what).
3. NOTE items to act on if cheap: E5-05..E5-07, E5-09 (record, no change needed).

## Task B: still-blocked evidence checks

The canonical `onset512-return-20261108.zip`, the I25 bundle, the derivative/inventory/review ZIPs, historical PDFs and the 632 MiB native histories were not
available to the audit. AC does not know where the I25 ZIP is; do not ask again for its location without new evidence. If AC supplies the canonical ZIP, Claude runs
the preregistered checks in WHEN-INPUTS-ARRIVE.md after Task A is complete; if the I25 bundle cannot be found, say plainly in the records that the data-only
checks of 320/384/458/510 remain OPEN, or propose a bounded regeneration of exactly those four witnesses from the engine's primary receipts, preregistered
and reviewed (not a claim that a regenerated bundle has the lost ZIP's identity). Custody of the native histories remains for AC (transfer, regenerate or accept as
recorded).

## Task C: one paired wording batch (new freeze)

Any TeX edit breaks the ad908acb freeze: make one batch, then a new paired TeX/Bib commit, the `FINAL_BASELINE` update in a separate commit, rebuild,
`check_correspondence.py`, `--archival`, `check_baseline_controls.py`, the mutation test and the rename-aware scanner with an updated map (add the missing rename
`F_0(hk` → `F_0(h_m k`), and a focused re-check by a distinct agent. Items (details and locations in audit-05-manuscripts.md):

1. **M5A-01 (MAJOR, both texts):** replace "It forces |x−y| >= π−v" by the correct "rho >= π−v" (companion 2178–2180, paper 936–938; the collision occurs
   exactly when x + y = π − v); remove the comma splice. This is material for review.
2. **M5B-01 (MAJOR, companion):** certification-unified.tex lines 1623–1629: remove "are retained" and "remain at their recorded computation sites"; say what is
   absent or unverified, as the paper does. Check the other places where the companion repeats the custody wording.
3. **M5B-02..M5B-07** paper additions missing from the companion (explicit proof of Theorem 1.1 and citations of Theorem 4.10 and Proposition 5.3; physical-corner
   naming; the abstract notes); IEEE rounding model out of "Proved in the text"; restore the lost section 3.3 reasons (trapezoid bound 1/(8z²), recurrence
   psi(y/2) = psi(1+y/2) − 2/y, the psi'(r+1/2) statement, the (cu:kappa) citation, kappa named before the pairing step); label and cite the base-value table, move it
   after Cor 4.7 or define its symbols, state its provenance and assert log pi > 11/10 in the checker if the text says check.py evaluates it; define eps_fp, w_B, R_l, and
   the internal name "I25" before use.
4. **M5A-02..M5A-07:** the three lost one-line reasons (prefactor identity 2aτ(v/2)/(π²ν) and wrap cost 8P/(3πm(j−1)), define τ(w) = w cot w before use; the primitive
   ∫T_t dt = 4a log sin(t/2); the reason A cos x + B sin x <= sqrt(A²+B²)); the C4B-06 residuals (chord bound sin t >= 2t/π and the alternating remainder rule in the
   companion, the |N_s| <= 8 reason near first use, the envelope's pole decomposition, lines 999, 1310, 620); split the sentence defining both h_m = π/m and h_j(t) (touches
   `uc:signed-outer`); the remaining notation collisions listed in M5A-05 (e, r(w), tau in the paper; w and the section 4.2 symbol table in the companion; eta_± and zeta);
   the ledger table's forward pointers (D_phi, G_phi, C_{6,phi}, M_phi, B_out); Figure 3 and the worked-number table closer to the row decomposition, labelled, and
   without "the independent audit's" wording.
5. **B5-01** paper Figure 2: copy the companion's fixed labels. **B5-02** equation numbers still on their own line at (11), (20), (25), (39), (50), (54): split the G_g
   row or record a DECISION. **B5-03** the explicit pi bracket in the companion. **B5-04** both data statements: cite the post-repair snapshot or the DOI once AC has one
   (placeholder until then; do not cite a433c7d as the current version). **B5-05/B4-09** roles table columns; **B5-09/10** companion Figure 3 and the table reference;
   the editorial items in audit-05-manuscripts.md.
6. Correct or honestly re-label the response-04 rows listed in audit-05.md in `response-05.md`; add a dated correction to the supplementary review's "retained" rows
   (B5, C1, C10) and to `pr-update-20261113.md` (audit-05 result, the open items, the budget share).

## For AC

(1) Budget: the global generated-class bound 11,751,309 B exceeds the 10,000,000 B cap; main alone is 9,733,758 B, this topic's counted share is 1,995,804 B.
Decide how to treat it (cap exception, cold-storage destination, or reducing the share); nothing was removed. (2) The canonical 320..510 ZIP and the I25 bundle (or
confirmation they are lost), custody of the 632 MiB histories, and the post-repair snapshot and DOI for the data statements. (3) The AI declaration (still omits
Claude Sonnet 5.5, which orchestrated audits 02–05) and the draft marker remain yours.

## Frozen

E01–E15, J01..J03, the finite theorems and certificates, the hybrid engine freeze `0d9ce0a5…`, the compact return, the old artifacts and freezes (24a98db,
ad908acb stay in Git), all audit reports, P1–P4 as recorded. Do not edit earlier audits.

## Publication

Checkpoint each task. At the session boundary commit outputs first; then in a separate commit close this handoff as `done in <sha>` and open the next numbered
handoff; exactly one handoff stays open while work remains. PR 27 stays a draft; edit its record yourself (update `pr-update-20261113.md`).
