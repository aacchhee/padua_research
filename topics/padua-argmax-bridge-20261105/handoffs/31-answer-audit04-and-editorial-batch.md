# Handoff 31: answer audit-04, fix the 320..510 reader, complete the evidence checks, one editorial batch

- Status: done in f81682557c104e18497d2e08278a99bb97572773
- Previous handoff: 30-claude-audit-onset512-and-manuscripts.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator. Development: Sol medium for technical work and code fixes, Sol xhigh for ordinary mathematics and proof clauses. A distinct Astra high/xhigh agent does supplementary checks. Astra ultra only with a recorded written justification.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `674876435cd75eed281dc22c726eb36c6bb58f4f` (audit-04 outputs; MINOR addenda at `9d46507`); this handoff is the following handoff-only commit
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`
- Stage: WORK (MAJOR findings are open)
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; audit work by eleven Claude Opus 5.5 subagents instructed at xhigh (disclosure in audit-04.md). · 2026-11-08

## Authority

Pushes to this working branch stay authorized. Do not push main, merge, force-push, change tags,
`.github` or settings, submit or contact anyone externally, or mark PR 27 ready. Only AC merges.
Nothing in audit-04 waives a finding or grants readiness. AI declaration, ORCID and contributions are
reserved to AC (do not edit them); the funding statement is confirmed. P1–P4 stand as recorded under
AC's accepted disposition. No Syvert calls beyond what AC authorizes, no new native degree campaign.

## Read first

1. AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the current head; record the SHA.
2. This handoff, [audit-04.md](../audit-04.md) and [audit-04-manuscripts.md](../audit-04-manuscripts.md),
   then the review reports in [audit-04/](../audit-04/) for exact locations and reproduction commands;
   [audit-04/WHEN-INPUTS-ARRIVE.md](../audit-04/WHEN-INPUTS-ARRIVE.md) for the blocked checks.
3. The LOG entry of 2026-11-08 "Focused Claude audit-04".

## Task A (first): fix the reader for the 320..510 return (E4-01, MAJOR)

`code/local_onset512_campaign/return_bundle.py` does every check with `assert` (lines 139–222) and then
prints "pairs 191, proofs 382" unconditionally (line 223). Under `python3 -O` or `PYTHONOPTIMIZE` a forged
26,529-byte ZIP with zero certificates exits 0 and prints acceptance. Required:
1. Replace the asserts by raised errors (or `raise SystemExit` with a message); refuse to run when
   `sys.flags.optimize` is non-zero; compute every printed count from the verified data; document `-E`
   (isolated mode) in `local-onset512-summary.md`, the deposit README and the ZIP's README.txt.
2. Apply the same to `code/local_onset512_campaign/runner.py` `pins()` and to the assert-based pins in
   `zenodo-deposit/RECHECK-SMALL-BUNDLE.md` (and any other recipe that relies on `assert`).
3. Add the controls that failed: a zero-certificate forged ZIP under `-O` must reject; keep the 13 existing
   negative controls. Use the auditor's fail-open probe in `audit-04/code/e4-code/` as a model.
4. The code change gives the reader a new identity. Record it; request a focused re-review by a distinct
   agent; then rerun the reader on the actual canonical ZIP. Do not attribute the repair to the historical run.

Also address, as proportionate: **E4-02** pin the reader's trusted runtime manifest externally (`5b89fa66…`,
`da63280a…`) and authenticate pins before running the checker; **E4-03** the E-02 parity checks for the 189
unsampled pairs (summary and fresh-certificate identity, attempt status, runner identity, extra members,
non-truthiness checks); **E4-04** `verify_compact` accepts a rehashed `observed_returncode: false` (lines 23, 51)
and its output does not record which plan was enforced; **E4-05** the I25 launcher takes worker exits from
`Popen` (ECHILD maps to 0, SIGCHLD not normalized) — normalize SIGCHLD and use waitpid-level status, or
reword the record; **E4-06** reconcile the stale deposit text (`MANIFEST.json.in` pending_items[0], README
lines 252–253 vs 289) and state that the deposited `padua30.zip` carries the unrepaired verifier `7c2dad53`
and pin the repaired one `5867ac0c`; **E4-07** state one size-bound convention (the audit-03 "no deletion credit"
convention gives 9,917,613 B; crediting the shrink of `cold-storage.json` gives 9,897,953 B).

## Task B: complete the evidence checks (needs files)

The audit could not examine the canonical `onset512-return-20261108.zip` (81,602,992 B, `da63280a…`), the I25
bundle `i25-evidence-20261108T112304Z.zip` (2,843,611 B, `d1d03156…`), `padua30.zip` (25,111,335 B, `aac08e5f…`),
the small certificates ZIP, the essential inventory or the review ZIP: AC was asked twice and they were not
supplied to the audit session. Do not assume they were checked. Two options, AC's choice:
- AC supplies the files to Claude, who runs the preregistered checks in WHEN-INPUTS-ARRIVE.md (the reader on
  the actual ZIP after Task A; a data-only check of degrees 320, 384, 458 and 510 from the I25 bundle, about
  1–2 CPU-minutes; byte comparison of the bundle's 942 proofs with the original return for 41..319 and 511 and
  with the new return for 320..510); or
- you run them in your environment under the existing preregistrations and caps and Claude audits the records.

Also decide custody (E4-09, E-10 of audit-03): the 632 MiB of unsampled complete native histories for 320..510
exist only in the ephemeral campaign tree; there is no cold-storage entry and no Zenodo record. Put the options
(transfer, regenerate, accept as recorded) in front of AC; do not claim delivery.

## Task C: one coordinated editorial batch (new paired freeze)

Source of truth: [audit-04-manuscripts.md](../audit-04-manuscripts.md) and the companion/paper/notation reports. Any TeX
edit breaks the 24a98db freeze: make one batch, then a new paired source commit, a `FINAL_BASELINE` update in
`companion-paper/check_correspondence.py`, rebuild both PDFs and the artifact check. AC's decision 2: use the
rename-aware check (`audit-03/code/n/notation_scan.py --baseline-rev 24a98db… --rename-map …`) during the
batch, then re-baseline once at the end. Keep the old 48/162- and 51/147-page artifacts and freezes intact.

Order of work:
1. **C4B-01 (MAJOR, regression):** restore the four reasons deleted from Lemma 4.2's proof in the companion
   (paper lines 172–175, 225–231, 258–261): the f‴ sine-ratio step and f(0)/8 < 3/40 from f(0) = 𝔨_0/π with
   𝔨_0 < 9/5; the bound t(½−t)/(1−t²)² <= 3/40; the reason 𝒲(π−w) >= w²/4; the closing H(w) − H_0 inequality
   with closed endpoints; give the "atom counted once" paragraph its context.
2. **N4-01, N4-02 (MAJOR as groups):** define before use ρ, A, B, x, y, P_n in the §4 roadmap and Fig. 2;
   I_s, φ, M, c, θ_0, U_{n−1}, Li_2, D_φ, J_end/J_cen, L_{jk}, W_z, I_R, the quantifiers of Lemma 5.1; state or
   cite the named tools in the paper (tangent partial fraction, triangular-kernel second difference, Li_2, discrete
   layer cake, centered-cell BV quadrature, finite sine product, the Fourier step behind the cot partial fraction,
   the exponential-type Bernstein inequality, the binary64/Horner/pairwise model); add the four missing
   bibliography entries (IEEE 754, NumPy/Python, Higham, a Fourier-uniqueness theorem) and update the frozen-bib
   baseline in the same commit.
3. **Notation collisions in numbered blocks:** P_n → 𝔭_n (the gate polynomial; blocks Cor 4.7, (74), (75), Theorem
   4.10, Fig. 2), G/𝒢, Θ/𝔗_*, U/U_*, j_*/𝔧_*, A_* in Lemma 4.8, V/W, the C of Theorem 1.2; companion-only: R_1
   (prelim:482), the offset-cutoff rename M → L_0, F_j, w, e, b, r, K, M, δ in §4.2 (C4C-M2) and a one-page
   symbol table for §4.2. Insert the four notation tables (start of §4, start of 4.2, start of 4.3, start of §5).
4. **Proof clauses (both texts):** J1-02, P4-06, P4-07 (the five termwise maxima and 42 + 2L + (49L̄+24)/π <=
   64 + 16L + 3L̄), C4B-02 (the row-average display R_r/n = …), C4C-M3 (the four row identities, about 10 lines),
   C4D-01 (the corner-lemma losses δ_A, δ_D and why k_Wy serves both axes; eight displayed lines and two re-entry rows),
   C4D-02 (insert the two paper sentences for C3-09(b) and C3-06), C4A-04, C4A-06 (the ten hidden steps), C4C-m1..m8;
   the elementary-constant lemma and its forward pointer (J2-02), log π > 11/10 in both lists (J2-01), the source of
   the base values (J2-03), the κ, b, c digits labelled as numerical values not used in any proof (J2-09).
5. **Evidence language and trust (both texts):** "two trees per degree" → 471 distinct trees, each recorded twice
   (J3-01, C4D-03); stored native endpoints neither used nor validated (C4D-04); split the trust table into what the
   text proves and what the program computes (C4D-05); describe the exact leaf maximum I25 executes (C4D-06) and
   display the sine-ratio product form of the kernel (C4D-07); correct G01's "proved in J03" (done by dated note).
6. **Companion pedagogy:** merge the remaining duplicates (19 blocks in C4C, about 13 claims in C4B, C4A-01), add the
   ledger table and the n = 512 worked column, one row-versus-poles figure with a small table, a five-step roadmap
   for Theorem 4.5, the cotangent-partial-fraction and elementary-constant toolkit before Lemma 4.2.
7. **Smaller:** Fig. 2 label collisions (B4-01), paper abstract γ, Table 1 and the roles-table typesetting,
   PDF metadata and stale comments (B4-10), the data statement (B4-06: cite the a433c7d snapshot or the Zenodo DOI
   when AC creates it), the trims of P4-13 (judge each; they are optional), P4-11 (move the Peano half of Lemma 5.1).
8. Rerun `onset512_analytic/check.py` after any change touching the comparison constants (the slacks are about
   2.1e-4; J1-06). Optionally adopt J1-01 (monotone in the quadrant) if it shortens the proof.

Then a focused re-check by a distinct agent, fresh builds, the correspondence check and the paired-mutation test.
A new substantive Claude audit is needed only for changed analytic text (the proof clauses of item 4), not for wording.

## Task D: record findings

Answer in `response-04.md`, one disposition per finding. Re-open the response-03 rows the audit found
unsupported (C2B-M1, M3(b), M3(f), M4, m7, m9, m12; C1-02, C1-09; C3-02/09/10/19; X-13; E-05): either fix them in Task C
or record them honestly as DECISION or OPEN. Also J3-02 (allow at least 7200 CPU-s in the full-recheck recipe and record a
timing calibration), J3-04 (add 2–3 controls that must accept), J3-05 (a one-line computed check of round-to-nearest and
gradual underflow), J1-03 (name H and `uc:origin-identity` as the source of j > 23/250), and the NOTE items you judge worth acting on.

## For AC (not yours to decide)

Supply or confirm the unavailable payloads (Task B); create the Zenodo deposit and DOI; the AI declaration (still omits
Claude Sonnet 5.5 and still carries a draft-status sentence); whether to accept the 632 MiB native-history custody gap.

## Frozen

E01–E15 and J01..J03 theory (changes only by dated addenda), the finite theorems and certificates, the hybrid engine
freeze (`0d9ce0a5…`; verified unchanged), the compact return, the old manuscript artifacts, all audit-01..04 reports,
P1–P4 as recorded. No retry or rescue of any failed scientific case, no thresholds changed, no new degree campaign.

## Publication

Checkpoint each completed task. Evidence index 396 entries / 32,414 B (reviewed exception); conservative generated-output
bound 9,873,956 B (audit-03 convention) against the 10,000,000 B cap; new certificates stay off Git. Update LOG, report,
results and the PR 27 sections (a previous automatic review blocked remote PR metadata editing from the audit session; edit
the PR body yourself). Final IDs and registry application stay deferred. At the session boundary commit outputs first, then
in a separate commit close this handoff as `done in <sha>` and add the next numbered handoff. Exactly one handoff stays open.
