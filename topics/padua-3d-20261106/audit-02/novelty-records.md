# Audit-02 scope report: protocol and novelty (T7–T9)

Auditor: Claude, Opus 5.5 xhigh, protocol/novelty subagent. Candidate `e80e000f2ba439ea62c966d255ef1b900b608b27`; head `e14ac15` only adds handoff 05. Rules (AGENTS.md, WORKFLOW.md) read at the head. No Git state or repository file was changed.

## Coverage actually read

- **Registry.** All of `state/IDEAS.md` (1–1154), read in sequential chunks, including every heading, alias and summary and every obstruction/disposition table.
- **Literature INDEX.** Relevant full rows only: LIT-004/010/014/304–307/310/319–323/327/377–383/387/389/391/392/413 and the delta LIT-633. INDEX has no Chkifa–Cohen–Schwab (CCS), Minkowski or Subbotin row.
- **Rules.** WORKFLOW.md, the IDEA and THEORY templates, CLAUDE_ROLES.md.
- **Topic records.**
  - Handoffs 04 and 05, plus the round and stop rules of handoff 01.
  - LOG lines 149–281, rounds.md, gates.md, report-continuation-04.md, the report.md addenda and the topic results file.
  - Every T7–T9 gate, preregistration, literature record and attempt, plus literature-T6.md:40–75.
  - response-deviations-01.md; the candidates-* headings, with the T1-Haar and T5-04 bodies in full.
  - The cold-storage files and evidence-manifest.json.
  - Theory: all t7, t8 and t9 headers. Full text of t7-rank-two, t7-rank-two-survivor, t7-finite-reduction, t9-haar-packing, t9-packing-conditional and t9-averaged-projection.
- **Not read in full.** The other t7, t8 and t9 theory bodies, BRIEF, audit-01 beyond m5, and the bodies of the independent-check files. No mathematical verification was done; it is outside this scope.
- **Executed.**
  - `artifact_manifest.py --verify`: PASS (56 artifacts, 309,009 B, Python 3.13.18).
  - Read-only git inspection of chronology and trailers.
  - Receipt hashes against the cold-storage ledger, and generator blobs against e80e000: all match.
  - IDEAS line counts: 1112 at e5b6445 and 1154 after the merge, matching the gates' claims.

## Findings

### BLOCKING

None. No claimed epistemic status is unsupported within this scope.

### MAJOR

**A1. T7 stopped at 2/25 rounds without a valid stop reason.**
- **Rules.** Handoff 04 (`04-work.md:23`) allows an early stop only on a gate kill, a proved obstruction or a recorded exhaustion. Handoff 01 (`01-work.md:111-113`) says a direction continues after progress, and that two rounds without progress end it.
- **The stated reason.** `attempts/T7.md:263-272` stops on a "proved obstruction, scoped to the mechanisms actually tested". Those obstructions are two refuted shortcut inferences and one fixed survivor's cubature marker (PD-N T7-07). They are not obstructions to the direction. The attempt itself says it is "neither budget exhaustion nor … two no-progress rounds".
- **Census not run.** The handoff's cheapest decisive test, the n=2,3 census (`04-work.md:67`), was not run. The attempt says "Feasibility … was not established" (`attempts/T7.md:152-163`), although the target-order generic stratum is small (217 groups at n=2; `:96-97`).
- **Survivor rule not applied.** The survivor decision rule (`04-work.md:72-74`) calls for a degree-uniform rule and a D2 screen against Leja/QR. Neither was done; even the n=3 quality of the 20-node set was not sampled.
- **Fix.** Resume the rounds, or record the stop for AC's explicit acceptance.

**A2. T8's "recorded scope exhaustion" (`attempts/T8.md:126-132`) does not hold.**
- **A resume condition was met but not used.** T8-02's resume condition, "a proved stratum reduction" (`novelty-gate-T8.md:94-97`), is supplied in this same batch by PROVED T7-03 (`t7-finite-reduction.md:7-18`), which covers cyclic H. The special-phase strata (`04-work.md:96-99`) were nevertheless not resumed.
- **Unions never attempted.** Variant 4, unions of cosets sized N (`04-work.md:101`), was never tried. T8-04 says only "no mask/replacement rule has yet been specified" (`novelty-gate-T8.md:125-138`). That describes absent work, not exhaustion; variant 4 had no structural precondition.
- **Budget.** 23 of 25 rounds remain unused.

**A3. T9's own stop rule (routes 1–3 recorded with outcomes, `04-work.md:163`) is not met.**
- **Route 3 has no record.** The class-specific lower bounds (`04-work.md:159`) have no candidate record, disposition or resume condition anywhere. These are the stack orderings via the T4 permutation mean and the coset classes via their shortest dual vectors.
- **Route 2 is incomplete.** The finite-complement screen for n<110 (`:156`) has neither a feasibility statement nor a deferral.
- **Precedent.** This is the audit-01 M2 pattern: a handoff item left without a disposition.

**A4. The T9 gate (`novelty-gate-T9.md:25-35`) misses closest entries.**
- **No search terms.** Unlike the T7 and T8 gates, it logs no search terms.
- **Cubature-count predecessors omitted (T9-HAAR/PACK).**
  - IDEA-029 (`IDEAS.md:69`: cubature route "conflicts with conjectural Li–Sun–Xu"), IDEA-044/120 and IDEA-109.
  - LIT-010/307 (Li–Sun–Xu, ≥n³/4 nodes) and LIT-389 (no family attains Möller's bound for d>2).
  - LIT-413, and OBST?…-11 with LIT-192/374 (Xu 1994, d=3).
- **Extraction and upper-bound predecessors omitted.**
  - T9-EXTRACT omits IDEA-027 (`:67`), whose dominant-submatrix Lebesgue bound is the closest analogue, and IDEA-049/LIT-387.
  - The Fekete records omit IDEA-209.
  - The LOWERSET target omits IDEA-047/LIT-378, the 2-D Morrow–Patterson O(n²) bound for an explicit minimal set.
- **Subbotin not compared.** T9-K's separation ("keep 2^-s, avoid the 27 loss") is compared only with T6. The topic's own record says Subbotin's Corollary 1 "covers arbitrary projections on the even space", while Theorem 1 carries the 3^-d factor (`literature-T6.md:63-64`). No novelty is claimed, but the separation statement and the "27-fold" framing need this comparison or an explicit coverage limit (cf. audit-01 M1).

**A5. The T9 gate-timing deviation is not canonically disclosed.**
- **The deviation.** `novelty-gate-T9.md:20-21` says "The analytic ideas below were developed while reading". WORKFLOW says to generate candidates only after the gate.
- **Contradicting records.** This conflicts with `LOG.md:203-205` and `attempts/T9.md:57`. It is absent from `response-deviations-01.md`, although handoff 04 (M1/M3) made full-read-before-mechanism a gating item for exactly this reason.
- **Post-publication edit.** The gate published at 51c031a cited the wrong predecessors (IDEA-203–205). It was fixed in place, with the note "Corrected before final freeze" (`:41-44`), even though it had already been published. The same edit silently changed T9-LOCALIZED from "deferred" to "equivalent".
- **Mitigation.** Most T9 routes were supplied by the handoff.
- **Fix.** A canonical dated disclosure, plus an honest correction note.

**A6. ID kind for refuted T7 candidates.**
- Two candidates are "REJECTED, refuted inference": IDEA?…T7-03 (rank-two shortcut) and T7-06 (one phase per stratum) (`attempts/T7.md:104-120,165-180`).
- Their refutations live in PD-T records. PD-T T7-04 is titled a "counterexample to an inference" (`t7-rank-two.md:1-22`), and the stratum counterexample sits inside PD-T T7-03.
- The split rule ("refuted side conjectures into scoped PD-N files"), the L5 decision, and the IDEA-161→PD-N021 precedent (`IDEAS.md:725`) point to scoped PD-Ns.
- This is the converse of audit-01 M5. Propose PD-Ns or justify PD-T for AC; the choice is material at allocation.

### MINOR

**m1. Attribution of Claude's handoff-04 material.**
- **Correct:**
  - The ten-point example is credited to audit T1 NOTE-1 (`t7-ten-point.md:3`).
  - CCS is labelled "handoff04 lead / bibliographic only".
  - Classical Fekete Λ≤N is gate-killed and not claimed.
- **Not credited:**
  - The packing sketch proved as T9-HAAR/PACK came from handoff 04: the ℓ1 criterion, the 2^d fold, the 2-D tightness check, 18/19, n≥110 and 19n³/108, and the escapes. The records credit only a "T1 sketch/lead" (`t9-haar-packing-reduction.md:26,93`; `attempts/T9.md:120-123`), which was a Codex coordinator suggestion (`literature-T1.md:58-63`).
  - The fold bound |H|≤8N in T7-03 and T8-01 is uncredited.
  - The 18/19 value is tied to an unread J. Complexity DOI (`t9-packing-conditional.md:33`; `literature-T9.md:18`). The handoff's actual source, Minkowski 1904 (`04-work.md:143`), is not recorded.

**m2. Provisional ID hygiene.**
- Two slug formats coexist: `…?padua-3d-codex-…` (T1–T6, T8, T9) and `padua-3d-20261106-codex` (T7). WORKFLOW requires the full slug (`WORKFLOW.md:139`).
- T7 uses ellipsized `IDEA?…T7-0x` forms, and its IDEA and PD-T numbers are offset (IDEA T7-02 maps to PD-T T7-03).
- The T9 candidates carry only nicknames. T9-FEKETE and T9-LOCALIZED have no ID at all.

**m3. Stale or unsynchronised records.**
- `t1-open-class.md` (the OPEN target) does not link the T7 or T9-HAAR results.
- IDEA?…T1-Haar still reads "Deferred … no reduction" (`candidates-deferred-response-01.md:5-19`), although T9-HAAR completes the reduction.
- The T2 variant records do not point to their T8 outcomes.
- `t6-universal-lower-bound` does not cross-reference T9.
- "awaiting separate rerun" / "Independent rerun is required" remain in `t8-finite-screens.md:15,29`, `t8-phase-obstructions.md:82` and `novelty-gate-T8.md:212`, despite the executed T8 check. The text should state why the result stays MEASURED (regenerate-only raw data).
- Two different IDEA?…T5-04 records each name the other as canonical (`candidates-deferred-response-01.md:77-91`, `candidates-T5-response-01.md:59-76`).
- The ledger's `source_commit` (7407e13) and the manifest's `rules_input_sha` (ccd9e90) are stale.

**m4. Frozen gates edited in place without in-file dated notes.** This affects the T8 model header (diff 1c75e1f→e80e000; the change is disclosed in the LOG) and the T9 rows (A5).

**m5. T9 evidence records are incomplete.**
- `t9-checks.json` and `t9-maxima.json` lack the command, the Python and mpmath versions, and the rules SHA, so the manifest's `recorded_commands` omits them.
- The raw outputs `/tmp/t9-*.npy` (`t9_maxima.py:80`) are not inventoried, unlike T8's raw outputs, and sit outside the topic tmp root.

**m6. Model provenance understated.**
- The e80e000 trailer gives Sol high only "response/T8 enumeration". In fact the Sol-high worker authored the T8 analytic proofs (PD-N T8-01 and T8-02, PD-T T8-03) (LOG:259-264).
- Handoff 04 assigned Sol xhigh to mathematics (`04-work.md:7`). WORKFLOW allows high, but this is recorded only as a prose correction, not as an allocation deviation.
- Both points should be stated in the PR body.

**m7. Template gaps.**
- T7-02..09 have no Aliases lines.
- T8-01..05 have no per-record literature field.
- T9-LOCALIZED mixes the "equivalent" and "deferred" dispositions.

**m8. Pilot choice not recorded.** Nothing records how H=<(7,7,4)/10,(5,0,5)/10> and a=(1,2,4)/101 were chosen (`preregistration-T7.md:45-56`). Any exploratory runs before registration must be disclosed.

### NOTE

**N1. Chronology is consistent.**
- The T7/T8 gates and preregistrations (1c75e1f, 19:32) precede the T7/T8 code and results (51c031a).
- The T9 gate and preregistration (51c031a) precede the T9 work (e80e000).
- The T8 U/O/P receipts pin preregistration sha256 f089f3…, which is the 1c75e1f text. The E receipt pins 8cad…, whose append is prospective only. This content binding supports prospective order for T8.
- The T7 and T9 receipts pin no preregistration.
- The commits were made via the connector within about 30 minutes, so they show publication order only. The full-read claims are credible but cannot be independently verified.

**N2. Dispositions and statuses.**
- PD-N T7-07 kills T7-08 on one fixed set, so a PD-N is appropriate. "Refuted" would be the more precise reason.
- The T8 PD-Ns are scoped failures.
- CONDITIONAL PD-N T9-01 names its hypothesis exactly ("every lattice packing of the unit 3-D ℓ1 ball has density ≤18/19", UNVERIFIED), keeps the escapes, and does not mark T9-PACK REJECTED. I found no CONDITIONAL-status PD-N precedent in PROOF_STATUS; confirm L5 accepts one at allocation.
- No OPEN target was relabelled PARTIAL.

**N3. No novelty, priority or "first" claims** were found in the T7–T9 records, the continuation report or the results file. "27-fold" is always qualified as relative to "the earlier local certificate".

**N4. Source labels are correct:** CCS (lead), Wang–Wang–Wang (LIT-391, secondary), 18/19 (UNVERIFIED), and the new Poppe–Cools 2012 record (exact pages read).

**N5. Record hygiene checks pass.**
- In this range the results file was written only by the Codex orchestrator.
- All commits carry Agent and Model trailers.
- No generated evidence file exceeds 16 KiB.
- The ledger hashes and byte counts equal the receipts.
