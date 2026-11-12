# Audit-03 protocol/novelty sub-report — padua-3d-20261106

Auditor: Claude Opus 5.5 (claude-opus-5-5), xhigh. Independent protocol/novelty auditor of Codex work.

- Rules read at `54d554a`; AGENTS, WORKFLOW and CLAUDE_ROLES are unchanged since `7afa6a5`.
- Candidate audited: `696bca5`. Head `54d554a` changes only handoff06's status line and adds handoff07 (checked by diff).
- No git state changes and no repository edits.

## Coverage read

- AGENTS, WORKFLOW, templates; **all 1154 lines of state/IDEAS.md** with every obstruction/disposition table.
- INDEX rows found by grep for the listed sources: LIT-004, 014, 301–331, 377–392, 413, 428, 486–512.
- Handoffs 06/07, LOG from line 282, rounds, gates, report-round06, response-02, deviations-02.
- All round06 gates, preregistrations and literature records; all four attempts in full; results file; cold-storage records and manifest.
- Headers of all t7-r06/t8-r06/t9-r06/t10 records; six of them in full. Old T9 packing and lower-set records, C4 split files, parts of independent-checks-round06, PR #33 body (read-only).

## Own executions

Scripts are in `scratchpad/code`; none writes to the repository.

1. `python3 topics/padua-3d-20261106/code/artifact_manifest.py --verify`: PASS, 154 artifacts, 728307 B.
2. Pin checks: all 57 pins in `independent-r06-pins.json` and all 13 `record_sha256` entries in `t9-r06-run-manifest.json` match the current files.
3. Inventory rebuilt from receipts: exactly **51 identities / 54,836,138 B**, made of 26 legacy-T9 and 25 T7/T8 raw identities.
   - The five T10 `raw_sha256`/`raw_bytes` identities (158,276 B) are not among them.
4. `arith_checks.py` passed every check: census parity counts n1..16 (max F/N = 145/102 < 3/2); F(n) > N for n1..109 (F(109) = 338855); f(109) = −9809, f(110) = 2312, threshold 110; R-Leja sum identity n0..16; parity-permitted degrees ≤ 20 are exactly n ≢ 2 (mod 4); det B_crit = −38/27, density 18/19.
5. `mindet_probe.py` is an exhaustive row-HNF search in exact integers. It reproduces the n2 and n3 minimizer counts (12 and 8).

   | n | Determinants with no admissible lattice | First admissible det (admissible HNFs) | CPU |
   |---|---|---|---|
   | 4 | 1..91 | 92 (24) | 2.6 s |
   | 5 | 1..177 | 178 (24) | ≈24 s |
   | 7 | 483..485 | 486 (24) | — |
   | 8 | 721..723 | 724 (24) | ≈60 s |

   - For n7 and n8 only determinants from the packing bound up were tested, so their minima rest on the imported bound det ≥ ⌈38n³/27⌉.
   - For n = 6, 9, 12, 15 the seed determinant equals 38n³/27 (`t10-search.json`; e.g. n6 det 304), so the seed is minimal given the same bound.

## Findings

**BLOCKING: none.** No claimed status is unsupported on protocol or novelty grounds. The mathematical audit is separate.

### MAJOR

**MJ1. The T10 gate omits LIT-391, the closest in-repository literature entry for its projection target.**
- LIT-391 (`INDEX.md:218`, Wang–Wang–Wang 2014, UNVERIFIED secondary) reports O(log^d n) cube hyperinterpolation norms. The topic cites it as why log³ is the target (`BRIEF.md:38`, `handoffs/04-work.md:125`); audit-01 m15 flagged the same omission for T6.
- No round06/T10 file mentions it (grep); `novelty-gate-T10.md:7–9` lists only DMVX and Cools–Poppe. `t10-log3-target.md` (OPEN) and `t10-log3-corollary.md:21` (CONDITIONAL) never relate themselves to this reported bound.
- Not BLOCKING: no novelty is claimed.
- Lesser omissions (MINOR):
  - IDEA-178, IDEA-013 and PD-N035/037 for T10;
  - LIT-382 for T10.3 and LIT-512 for the kernel route;
  - IDEA-187 and PD-N037 are missing from the T7 inherited list (`novelty-gate-T7-round06.md:21`), and both bear on T7.Q.

**MJ2. T10.1's exact minimal-determinant search stopped at n3 without measured feasibility, and T9.P's finite-complement work inherits the gap.**
- Handoff06 asked for "n = 1..16 (further if cheap) … at minimal det L … exact search". The preregistration (`preregistration-T10.md:5`) limited complete search to n1..3 in advance; records then say "Unrestricted minima for n4..16 remain OPEN" (`t10-census.md:7`; `t9-r06-packing-source.md`, Boundary section).
- No feasibility was measured, though n3 took ≤0.8 s and the whole bounded box 1.96 s.
- Execution 5 shows the search is cheap:
  - n4 = 92 and n5 = 178, self-contained;
  - n7 = 486 and n8 = 724, given the topic's own imported 18/19 theorem;
  - every n ≡ 0 (mod 3), since T10's critical family attains 38n³/27.
- Handoff06 requires measured feasibility evidence before a route is narrowed or abandoned.
- Fix: extend the exact search as far as it is cheap, or record measured feasibility. Note that minimal det is not minimal folded |X|; that question can stay OPEN.

**MJ3. The ID kind and dispositions of D2-rejected frozen rules are inconsistent with WORKFLOW L5 and with the topic's own precedent.**
- These rejected rules sit only inside PD-T MEASURED records (`t8-r06-measurements.md`, the `novelty-gate-T8-round06.md` disposition append, `t10-extraction-complete.md`):
  - T8 Phi2 rule F;
  - U4, plus the D2 kills of U2/U3;
  - the initial Phi3 selectors;
  - the T10-02 extraction rules.
- Precedent in this topic gives such failures their own records: PD-N T4-02 (`t4-mesh-observations.md`) and PD-N T8-03 (`t8-even-family.md`). L5 says an evidenced mechanism failure gets its own PD-N.
- T10-02 is described inconsistently:
  - `attempts/T10.md:14,22` say "finite measured failure" and "failed frozen extraction rules";
  - rounds, report and results say "no literal extraction kill";
  - `evidence/independent-r06-t10-replay.json` records `kill: [6,7] … singular structured sets fail`, against the final "numerically ineligible, not singular" wording.
- Fix: decide each rule's disposition and give each scoped failure a PD-N (MEASURED), or record why none is needed. Add a dated note superseding the receipt's wording.

**MJ4. The T7 and T10 candidate records do not follow templates/IDEA.md.**
- T7: four compressed rows (`attempts/T7-round06.md:17–20`) still say "Active". The final route table (:175–183) gives no disposition reason or resume conditions.
- T10: the candidate paragraphs (`attempts/T10.md:12–16`) lack aliases, a literature field and explicit disposition reasons.
- T8 and T9 records conform.
- Handoff06 requires IDEA-template records with resume conditions; audit-01 M2 is the precedent.

### MINOR (developer to fix)

- **m1. Status criteria are inconsistent.**
  - PROVED-with-imported-LITERATURE (T9-r06-01/05) matches WORKFLOW and the PD-N022 precedent ("Padua unisolvence: LITERATURE").
  - T10-07 has the same dependency type, a read statement whose supporting lemmas were not checked, yet is CONDITIONAL. For Betke–Henk even less was read.
  - Document the criterion or harmonize the labels. A relabel is a material change.
  - Add Status-by-part rows marking the imported theorem as LITERATURE.
  - Record the Chkifa version/date mismatch and its publication status (`t9-chkifa2015.md:5`).
- **m2. T9 theory records fall short of the template and split rules.**
  - The t9-r06 files lack ID kind, Split, Status-by-part, Depends-on with full LIT IDs, Open items and History.
  - Five IDs have no own file: PD-N T9-r06-01/03/04 and PD-T T9-r06-03/04.
  - PD-N T8-r06-07 has no overall status.
  - The `MEAS?` namespace (`t9-r06-measured-maxima.md:1`) is non-standard.
- **m3.** No D3 check (whether the obstruction admits 2-D Padua) is recorded for the T9-r06 obstructions or for PD-N T10-03.
- **m4. Pre-run timing rests on attestation.** Disclose this once in deviations-02.
  - The initial protocols were first published only in `7f773eb`, after some local runs:
    - at that commit the T7 preregistration already says the "equal-size U screen has now completed";
    - the T8 Phi3b append is labelled "after initial route outcomes".
  - The "prospective" addenda first appeared together with their results: T7 C in `aa48696`; the T9 P follow-ups and three T10 addenda in `696bca5`.
- **m5. T8 linked-body reading is a gate qualification, not a supplement.** The C0/C3 bodies and T3 proofs were read after the initial runs. This is repeated in three places: `novelty-gate-T8-round06.md:20`, the attempt, and `literature-T8-round06.md:35`. Make it canonical, like T7's qualification, and link to it.
- **m6. The 51-file stream-hash check is under-documented.**
  - It records no command, script or file list.
  - Its "round06/T10 receipts" wording does not match the count in execution 3, which excludes T10.
  - The T9-r06 raw files carry only node hashes.
- **m7. Duplicate provisional source records.** Consolidate under same-source reuse:
  - Betke–Henk appears as both LIT?…-T10-03 and LIT?…-T9-r06-01;
  - T10-09 duplicates the DMVX entries LIT-322/306;
  - T10-05 duplicates the Cools–Poppe entries LIT-323/381.
- **m8.** `t10-census.md:7` and `t10-neighborhood-search.md:7` still say MEASURED "absent/until independent replay", although the replays exist. Upgrade (material) or restate the reason.

### NOTE

- T7 n3 infeasibility evidence (120-s pilot; 36,082 unresolved after 3,373/159,400 groups) suffices; state the extrapolation.
- The manifest is at 15,648 of 16,384 B.
- At PR preparation, mark the old CONDITIONAL PD-N T9-01 superseded by PD-N T9-r06-04.
- n4 is empty and n6 obstructed, so no no-fold rank≥2 H_n spans n3..6. The T8 special-phase screen covers only n2/n3.
- **No novelty or priority claim found**; "first explicit" R-Leja was correctly killed.
- Scope, results ownership, protected audit/handoff bodies, commit trailers and receipt sizes all comply.

## Stop review (handoff06 (a); rounds T7 = 3, T8 = 2, T9 = 2, T10 = 2)

| Route | Outcome | Qualifies |
|---|---|---|
| T10.1 | Exact n1..3; bounded seeds plus a 4941-box for n4..16 | Result, **MJ2 caveat** |
| T10.2 | 21³/41³ LS/raw vs QR/Leja to n16 | Yes |
| T10.3 | Both frozen rules to n16; exact restricted-QR ranks | Yes (MJ3 wording) |
| T10.4 | 73/18 refutation; log⁴ PROVED; log³ CONDITIONAL | Yes (MJ1) |
| T8.Φ1 | Exact parity-permitted set as the handoff defines it; witnesses for every permitted n ≤ 12 | Yes |
| T8.Φ2 | F D2 kill at n7/n8 | Yes (kill) |
| T8.Φ3 | Selector failures; 2N−1 rigidity; Phi3b count obstructions; some ranks OPEN | Yes |
| T8 S/U | Sampled strata; U2–U4 D2 kills plus the n6 union-parity PD-N | Yes |
| T7.C | Complete n2; measured n3 pilot; 256-draw fallback | Yes (fallback) |
| T7.Q / Φ / U | All survivors measured; Φ survivors or empty/obstructed classes; U screens n3..6 | Yes |
| T9.P | Primary statement; positive-weight result; phase counterexample; family-only complement | Yes (complement: MJ2) |
| T9.B / M / U | Method obstructions; benchmarks to n16; 2015 primary verified | Yes |

**Verdict:** (a) holds for T7, T8 and T9. For T10 it holds once MJ2 is fixed or measured feasibility is recorded. No stop invokes "programme exhausted".

## Eligible auditor MINOR fixes

Scope: wording, links, stale process text, or recording an already documented decision.

Files marked [P] are pinned in `independent-r06-pins.json` (and the T9 ones in the T9 run-manifest). WORKFLOW requires a pin update or a dated companion note. Put the [P] fixes F1, F4, F5, F11, F12 and F13 into one companion note, `audit-03-fixes.md`, and do not regenerate check06's pins.

- **F1** [P] `t8-r06-parity-admissibility.md:31` — replace `PD-N?padua-3d-codex-T8-02` with `PD-N?padua-3d-20261106-codex-T8-02 (old alias PD-N?padua-3d-codex-T8-02)`.
- **F2** `t9-packing-conditional.md`, after line 51, add: "2026-11-06 audit-03 pointer: the density premise is now imported at primary-statement level in [t9-r06-packing-source.md](t9-r06-packing-source.md) (PD-T?padua-3d-20261106-codex-T9-r06-01; PD-N?…-T9-r06-04, strictly positive full-support weights). This record's own status and text are unchanged."
- **F3** `t9-lower-set-transfer.md`, after line 78, add: "2026-11-06 audit-03 pointer: a verified every-prefix premise and explicit sequence are supplied in [t9-r06-explicit-rleja.md](t9-r06-explicit-rleja.md) (PD-T?…-T9-r06-05); lines 26 and 34 describe the earlier state."
- **F4** [P] `t7-r06-torsion-obstruction.md:83–84` — replace with "Independent review completed in [independent-checks-round06.md](../independent-checks-round06.md). Broad T7 target remains OPEN."
- **F5** [P] At `t8-r06-parity-admissibility.md:76–77`, `t8-r06-phase-strata.md:44,59`, `t8-r06-union-parity.md:22,50`, `t8-r06-unit-coordinate-folds.md:81` and `t8-r06-near-order-measurements.md:13,20`, append "2026-11-06 audit-03: independent reruns are recorded in evidence/independent-r06-t8-*.json and independent-checks-round06.md; no status change here."
- **F6** `attempts/T8-round06.md:61–62` and `:103–104` — append the same note.
- **F7** `attempts/T10.md:14` — after "every eligible extraction" insert "(audit-03 note: preregistration-T10.md item 3 says 'every nonsingular extracted set'; see LOG 'second T7/T8 boundary')".
- **F8** `report-round06.md`, after line 6, add: "Provenance: T10 and the ranked routes were proposed in Claude's [handoff06](handoffs/06-work.md); the M=N=20 orbit and the Betke–Henk and Chkifa leads come from Claude's [audit-02](audit-02.md) (the latter two from recollection)."
- **F9** `independent-checks-round06.md:3` — after "check06" insert ", assigned gpt-6-astra high (696bca5 trailer; runtime unexposed)".
- **F10** `LOG.md`:
  - line 3: change "main `76ba421`" to "main `f70a260` (setup base `76ba421`)";
  - line 6: change "records in [report.md](report.md)" to "records in [report.md](report.md), [report-continuation-04.md](report-continuation-04.md) and [report-round06.md](report-round06.md)";
  - headings at :332, :355, :392 and :416: append " — Codex (assigned gpt-6-astra high coordinator; Sol workers per commit trailers; runtime unexposed)".
- **F11** [P] Stale replay text:
  - `t10-census.md:25` — replace "Independent replay was requested … arrives." with "Independent replay: evidence/independent-r06-t10-global.json reproduces 2/12/38 (n1..3)."
  - `t10-neighborhood-search.md:15` — replace "Independent replay remains required …" with "4941-box replay: independent-checks-round06.md."
- **F12** [P] `t8-r06-measurements.md:46` — after "audit control" add " (Claude audit-02 lead; audit-02/T8.md, audit-02/code/m20_check.py)".
- **F13** [P] Lead attribution:
  - `t9-r06-explicit-rleja.md:3` — add "Lead: Claude audit-02.md:168 (recollection), handoff06 T9.U."
  - `t9-r06-packing-source.md:3` — add "Betke–Henk lead: Claude audit-02/T9.md:160 (recollection)."

Not eligible for auditor fixing: the results file (orchestrator only), evidence JSON, and any status or ID change.

## Residual uncertainty

- Reading-before-run claims are attestations; Git shows publication order only.
- No external primary source was re-read in this audit. What LIT-391 actually covers remains unverified.
- `mindet_probe.py` is an independent script. Minima at n7/n8 and at n ≡ 0 (mod 3) depend on the imported 18/19 theorem.
- Mathematical correctness of T7 n2, T9-r06-02, T10-03 and T10-04 is left to the math audit. My arithmetic cross-checks of their stated formulas passed.
