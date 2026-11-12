# Audit 05 — padua-3d-20261106 — focused audit of response-04 and the final narrowed programme D1–D5

## Identification

- **Auditor:** Claude, Opus 5.5 (`claude-opus-5-5`), xhigh. Independent auditor of Codex development under handoff 20. This is the fifth formal audit round.
- **Orchestrator work:** core reruns, receipt comparison, this report, and review of the auditor MINOR fixes.
- **Scope subagents:** seven independent Opus 5.5 xhigh subagents. Their reports are appendices:
  - [A: response-04, provenance, budgets, storage](audit-05/A.md)
  - [D1a: line-by-line proof reconstruction](audit-05/D1a.md)
  - [D1b: adversarial scope and primary sources](audit-05/D1b.md)
  - [D2](audit-05/D2.md), [D3](audit-05/D3.md), [D4](audit-05/D4.md)
  - [D5: novelty, E4 applications, paper draft](audit-05/D5.md)
- **MINOR fixes:** applied by a Sonnet 5.5 medium mechanical subagent and reviewed by the orchestrator ([audit-05-fixes.md](audit-05-fixes.md)).
- **Isolation:** no subagent changed Git state. Each executed code only in its own `git archive` copy.
- **Rules:** read at `acf0fbc3782e4911fdc843062f5fe0526c1f0e63`, unchanged since `04ef28b`.
- **Audited candidate:** **`ec5c089f35fa2002a2ed2b293a41034364380170`**. Head `acf0fbc` changes only handoff 19's status and adds handoff 20.
- **Baseline:** `04ef28b`.
- **Main:** `f70a260`, unchanged. The branch changes only this topic and its results file.
- **Date:** 2026-11-12.

## Verdict

**Mathematics: accepted. No BLOCKING finding.** Every claimed status is supported.

**D1, the spectral obstruction.**
- D1-01..03 are PROVED.
- D1-04 (cube theorem) and D1-05 (inverse-polynomial weight corollary) are **PROVED with explicit LITERATURE dependency** on Greenfeld–Lev Thm 1.1, per AC's E4 convention. Two auditors checked this independently:
  - D1a reconstructed every step, including the near-critical squeeze, separation from the positive row identity, compact stationary limits, Bessel saturation and completeness, critical density |O| = 4/3, and the 2-D diamond escape.
  - D1b read the primary Greenfeld–Lev, Lev–Matolcsi, AMO, Kolountzakis, Kuperberg, Lyubich, Li–Sun–Xu and Marzo papers.
- **Literature position.** Within the reading done, D1 is not stated in the literature. It is a **non-effective, positive-weight-only negative answer to Li–Sun–Xu's stated open question** (degree-(2n−1) cube rules with n³/6 + O(n²) nodes). It combines known mechanisms; no priority is claimed.
- D1-06 (general doubling weights) is honestly OPEN at H1/H2.

**D2.**
- The Padua Hilbert–Burch matrices for n = 2..4 were confirmed.
- All 24 algebra cases were confirmed with an independent Buchberger implementation. The auditor also completed the four capped n4 cases, as auditor-side information only.
- The natural-lattice calibration was reconstructed.
- The ORSV real-node counts are genuinely incomplete, and the Jacobi guard failures are genuine.
- The repair chronology is consistent, and Λ = 5478.148 is reproduced.
- The kill rule was applied correctly. Broad C2 stays OPEN.

**D3.** The 20-node positive degree-5 Π₃-unisolvent rule was independently re-certified:
- own exact Krawczyk inclusion in a different basis with its own preconditioner;
- whole-box positivity, interior and separation;
- a different unisolvence method;
- the non-coset argument;
- six mutations rejected.

**D4.**
- The double-Lee bound proof was checked, with brute force for n ≤ 12.
- A fresh C++ enumerator confirms all four complete windows. The minima 92/178/304/486 are now independent of the 18/19 import.
- Whole-cube enclosures were independently recomputed for all 13 QR sets and for the optimized n12 set, giving 25.965428 ≤ Λ ≤ 29.058297, which lies inside the recorded 25.961333 ≤ Λ ≤ 29.062900.
- This rests on the Białas-Cież et al. Prop. 1 dependency, which is primary-read; Lemma 1 itself is quoted from Piazzon–Vianello.

**Response-04.** G1–G7 are verified fixed. The protected records are intact. AC's settled decisions are applied, the budgets are correct, and the manifest guard passes 6 of 6 mutations.

**Records and attribution: six MAJOR findings, so stage WORK.** They are attribution, statement-hypothesis and record items. None changes the mathematics.

## Executions

**Orchestrator** ([audit-05/receipts.txt](audit-05/receipts.txt)), in a detached worktree of `ec5c089`:
- master manifest verify: PASS, 362 artifacts, 2,281,441 bytes;
- `fd1_controls.py`;
- `fd3_certify.py check`;
- `fdc_d3_audit.py`.

All exit 0, and all scientific fields equal the committed receipts.

**Subagents**, all with their own code ([audit-05/code/](audit-05/code/)) and listed in each appendix:
- **D1a:** numerical checks of the defect, Gram and row identities on 3-D product and mixed rules and 2-D Padua n = 2..10.
- **D1b:** the fd1 controls with four mutations; a 50-digit check of the D1-01 identities on the non-lattice D3 rule.
- **D2:** exact Hilbert–Burch, Buchberger replays of all 24 cases, real-root counts, Λ via Legendre/LU and mpmath.
- **D3:** independent exact verifier; producer check; mutations.
- **D4:** brute-force Lee checks, a fresh C++ enumerator, and independent rational enclosures in Fraction/int128.
- **A:** manifest regeneration and mutations, the G1 reflection script, storage totals, links and provenance.

## Findings

### BLOCKING

None.

### MAJOR (returned to development; record and attribution level)

- **H1. The theorem statements need the hypothesis "all nodes in [−1,1]³" made explicit** ([D1a F1](audit-05/D1a.md)).
  - It is implicit at `final-d1/spectral-obstruction.md:9,19`, `weight-corollary.md:9-10,21`, `finite-frame.md:15` and in paper Theorem A. Line 19's "support geometry … otherwise unrestricted" invites the wrong reading.
  - Positive rules with outside nodes exist; for example, degree 1 on ±2e₁.
  - Adding a hypothesis to a statement is a material record change, so it is returned. It is not a defect in the proof.
- **H2. Missing literature for the sphere and disk comparison, and the attribution of D1** ([D1b-1, -2, -4](audit-05/D1b.md)).
  - Fixed-excess lower bounds for positive cubature are known by Yudin-type linear programming: Yudin 1997 for spherical designs; Lyubich (Thm 4.1, §5, Prop. 5.1; primary-read) for projective cubature; Xu 2003 for positive interior Chebyshev-disk rules (search level only).
  - The record's "no spherical L2 cubature excess is imported" implies that no such excess is known. Its reason why the sphere analogue fails is misleading.
  - The paper must say: D1 is not stated in the checked literature; it answers Li–Sun–Xu negatively for positive weights only, non-effectively, with page pins; it credits AMO Thm 14, Kolountzakis Thm 1 and Greenfeld–Lev Thm 1.1 for the mechanism; and it acknowledges the LP fixed-excess results. A suggested sentence is in D1b.
- **H3. Missed lattice predecessors** ([D5 M1](audit-05/D5.md)).
  - Lyness, *Notes on lattice rules* (J. Complexity 2003; excerpt coverage) reportedly defines the octahedral packing index and gives 3-D optimal rules for enhanced degree ≤ 4 and multiples of 6. That may make the minima at n = 1, 2, 3, 6, 9, 12, 15 already known.
  - Cools, *A Belgian view on lattice rules*, is also unread.
  - Both were flagged as leads earlier (`literature-3d.md:18`, `literature-T1.md:57-63`) but are absent from the D5 gate and the paper's gap lists.
  - Cite them at their actual coverage and narrow "locally certified" accordingly.
- **H4. Wang–Wang–Wang is not credited for T10's log³** ([D5 M2](audit-05/D5.md)).
  - LIT-391 and the C8 item require this credit; paper:76 and novelty-gate:44 credit only Kolomoitsev–Lomako.
- **H5. No novelty comparison for D3 and D4, despite a completeness claim** ([D5 M3](audit-05/D5.md)).
  - Missing comparisons: LIT-413 (minimal-cubature certificates), classical degree-5 cube rules, the T8 unisolvent 20-node sets, the n = 1, 2 lattice packages, and IDEA-466/609/611.
- **H6. Frontier dispositions not updated** ([D5 M4](audit-05/D5.md)).
  - C5 was "subsumed if C1 succeeds", but D1 is non-effective, so C5 is not subsumed. It needs a decision and a resume condition.
  - C6 has no resume condition. C8 has no disposition line.

### MINOR

Eligible items are fixed in place by the auditor, as WORKFLOW requires from round 3 onward. They are committed separately and listed in [audit-05-fixes.md](audit-05-fixes.md). Pinned prose is corrected by that companion note.

**Returned to the developer:**
- the paper's manuscript, process-text split and bibliography;
- D3's candidate "Disposition reason" field;
- `evidence/fd4-manifest.json` pinning prose files (A M7);
- the D4 enumerator `audit-04/code/A1/aud_enum.cpp`: it lies outside master-manifest coverage, has no g++ version recorded, and its replay used byte-identical binaries (A M8). Disclose this, or bring the source under the master;
- the D2 quality-replay receipt has no command or code identity (A M9);
- the split-header pairs not covered by audit 04 (A M3, M4).

**Orchestrator items** (applied in the LOG and results entries of this audit):
- results lines still say "pending AC" for the settled decisions (A M5, M15);
- the NumPy2 failure location: it occurred on the first proposal, not during the baseline evaluation (D2 m3).

### NOTE

- **Auditor-side extensions, not producer evidence:**
  - D2 completed the four capped n4 random cases; they are dimension N, unisolvent and radical.
  - D4 is the first fully independent implementation of the enclosures, beyond the supplementary replays that call the producer function.
  - D1b's 50-digit check shows the D1-01 identities hold on the non-lattice D3 rule.
- **Unclaimed scope facts:** exactness through degree 2n−2 suffices, the argument works for every d ≥ 3, and nodes must lie in the closed cube. Stating any of these would be a material change.
- **Storage:** within AC's approved provisional allowance.
  - The repository generated-output class is 8,672,675 bytes. The topic contributes 1,676,496 bytes.
  - The largest generated file is 29,229 bytes, and seven new evidence files are between 16 and 32 KiB.
  - The master manifest is 18,976 bytes.
  - All of this remains for discussion at PR.
- **Chronology:** consistent in publication order. Execution order rests on developer attestation; the new receipts carry no timestamps.
- **Commit trailers:** Agent and Model are separated by a blank line, so Git parses only the Model line as a trailer.

## Residual uncertainty

- **External theorems** that are cited, not re-proved: Greenfeld–Lev Thm 1.1 (D1); Białas-Cież et al. Prop. 1 with Piazzon–Vianello Lemma 1 (D4); Betke–Henk 18/19 (n ≥ 8 minima and the n ≥ 110 count); Chkifa; Kolomoitsev–Lomako.
- **D1 is non-effective.** It says nothing about finite n, signed rules, outside nodes, or interpolation Lebesgue constants.
- **Literature attributions** in H2–H4 rest partly on abstract or excerpt coverage.
- **Historical novelty** is not established for any result.

## Next step

Handoff 21: a focused Codex response-05 to H1–H6 and the returned items. A focused Claude re-audit follows only for the material changes, mainly H1's statement hypothesis. After that comes PR preparation and freezing.
