# Protocol/novelty audit: padua-3d-20261106

- Auditor: Claude, Opus 5.5, xhigh (independent subagent; developer Codex). Read-only; no Git state changed, no repository files edited.
- Candidate: `f1a5b0936d8fb2b033c69af59a6366550f170999`. Working tree is at `d0e1bbb`; `git diff --stat f1a5b09 d0e1bbb` touches only the two handoff files.
- Rules read: AGENTS.md, agents/WORKFLOW.md (in full), agents/claude/CLAUDE_ROLES.md, templates/THEORY.md, templates/IDEA.md.
- Scope: novelty gates, candidate records, dispositions, status discipline, literature claims, BRIEF expectations, record hygiene. This audit does not check the mathematical proofs.

## Coverage actually read

- **state/IDEAS.md, complete.** All 1,112 lines, read sequentially, including every obstruction and disposition table (lines 106–117, 256–275, 396–406, 462–474, 505–515, 764–784, 845–850, 911–919 and the 1056+ subroutes).
- **literature/INDEX.md, partial.** Rows LIT-004/010/014, 300–331, 374, 377–394, 488 and 512; searches for Subbotin, Yudin, Sündermann, Kolomoitsev, Calvi, Morrow and Biermann. Also the full DMVX-2009 and Xu-2024 records.
- **Topic files, read in full:** BRIEF, plan, gates, rounds, report, LOG, handoffs 01 and 02, attempts T1–T6, novelty gates T1–T6, literature-3d and literature-T1–T6, preregistration-T5, COLD_STORAGE.md, cold-storage.json, artifact_manifest.py, results/padua-3d-20261106.md, and the PR #33 body (REST API).
- **Theory files:** headers, status and disposition sections of all 21. The t1-*, t4-monotone-lower, t4-quality-target, t5-validation and t3-short-relations files were read in full.
- **Partial:** the first 80/40 lines of independent-checks-computation and independent-checks-math.
- **Not read:** the code, the proof bodies of the other theory files, and preregistration-T2/T4.

**Actually run** (all read-only):
- `artifact_manifest.py --verify` → PASS, 31 artifacts, 177,823 B.
- File-size scan: no topic file is over 16 KiB; the largest is independent-checks-computation.md at 14,268 B.
- `sha256sum` of /tmp/padua-3d-20261106/t2-generators-n{2,3,4}.json matches cold-storage.json, and the generator blob `6e84908` is the same at 7407e13 and f1a5b09.
- `git log --format=%B 76ba421..d0e1bbb`.
- DEKL arXiv 1608.03451v2: fetched and extracted to text.
- Subbotin fulltext: the proxy blocked mathnet.ru (403 / ENOTFOUND), so it was not checked.

## Findings

No BLOCKING finding within protocol/novelty scope. No status is claimed beyond the record, and no novelty or priority is asserted.

### MAJOR

**A1. The T1 gate missed its closest literature comparator.**
- De Marchi–Vianello–Xu 2009 (LIT-322/LIT-306; record `literature/lattice-unisolvence/records/demarchi-vianello-xu-2009.md`) is cited only in BRIEF.md:35 and in no gate or literature-T* file.
- Its 3-D node set, "a union of two complementary tensor parity subgrids" of the Lobatto grid, is the cosine image of a reflection-invariant subgroup: the all-parities-equal code of t1-reflection-classification.md:41-43. That puts it inside the class of PD-N?…T1-01.
- Its p.7 remark that hyperinterpolation there "is not interpolation" because the node count exceeds dim Π_n is the nearest published statement to T1's conclusion.
- Also missing for the cubature conjunct of T1-02: LIT-374, IDEA-109 and OBST?bivariate-lanczos-claude-11 (Xu 1994: no proper Γ for d=3), and LIT-381 (3-D blending lattices at 1.5–2.4× dim Π_k).
- report.md:163-165 puts T1 forward for a structural note, so this comparison must be logged (shortlist plus differences in novelty-gate-T1.md and literature-T1.md) before PR.

**A2. T5's gate and candidate records do not meet the template, and they miss predecessors.**
- novelty-gate-T5.md:130-135 is a table only. It lacks aliases, closest entries read in full, a falsifier, a duplicate/variant/new verdict, discriminability, results and disposition reasons; T5-05 (lines 144-158) is prose.
- Missed predecessors:
  - IDEA-044 (commutator rank and extension size, Degani Thm 2) and IDEA-108 (commuting extensions: Koiran, Curto–Fialkow) for T5-02;
  - IDEA-109, OBST-11 and LIT-374 (Xu 1994, d=3) for the degree-five near-minimal theme;
  - LIT-327 (Xu 2024);
  - Noskov–Schmid and Hirao–Sawa, named in BRIEF §5 and in the X7 note (`topics/programme-ideas-20261031/sources/Round 3 open problems 2023 2026.md`:88). The X7 note is the closest prior record for small-degree certificates, and neither source was searched.
- The D4 16-node "same-parity m=3 Lobatto union" (t5-validation-and-measurements.md:43, 72-82) is DMVX's construction but is unattributed.

**A3. Several considered candidates have no IDEA-template record or no resume condition.**
- (a) Handoff 01:57 and BRIEF.md:37 ask for the T2(a) Lissajous–Chebyshev alias-equivalence test. It is not recorded as run, deferred or subsumed: a search for alias-equivalen, spectral index or Dencker finds nothing in attempts, report or gates. Unshifted Dencker–Erb LC node sets are all-parities-equal reflection-invariant cosets (literature-T1.md:69-70), so PD-N?…T1-01 probably settles them for n≥2. The developer should verify this and record it as the disposition.
- (b) The Haar-lattice / octahedral-packing obstruction lead (literature-T1.md:57-63; t1-open-class.md:58-60; attempts/T1.md:90).
- (c) Completed-section commutator minimization. Handoff 01:82 explicitly assigned it ("compute minimal commutator norms … n ≤ 4"). It was not executed (t5-validation-and-measurements.md:107-118), has no IDEA ID, no resume condition and no LOG deviation entry, yet rounds.md:162-163 says its "resumption condition [is] recorded".
- (d) The Lobatto m4/m5 support probes and the T5-04 symmetric class (attempts/T5.md:55-59): deferred without a resume condition.
- (e) T4-03 is "deferred" (attempts/T4.md:144) without a resume condition. Its content reads as failed or abandoned.
- (f) T2 phase-shifted orbits and even-degree subsequences (attempts/T2.md:25; t2-normalized-screen.md:17-19) have a resume condition only in attempt prose. Handoff T2(b) (DMVX thinned by a second character) and T2(c) (the mod-6 revisit) are not recorded as not launched.
- IDEA T2-01 (novelty-gate-T2.md:24) still reads "active prerecord / Actual tests: none"; it needs its final disposition.

**A4. The T2 gate coverage deviation is undisposed, and the gate file overstates compliance.**
- novelty-gate-T2.md:3 claims a full scan "including obstruction and disposition tables".
- attempts/T2.md:27 admits only "relevant obstruction/disposition searches" and that "full-content pre-run compliance is not claimed".
- WORKFLOW:63 requires reading every obstruction and disposition table in full before mechanisms. "Relaxed bounded scan" is not a defined exemption.
- **Recommended disposition: a disclosed deviation, not cured by later reading.** My full read finds no missed entry that changes T2-01's verdict (variant, no novelty claim, results finite and negative). It does find that IDEA-182 and PD-N034 (adjacent-mod-4 unions, an infinite singular Chebyshev subsequence) were missed for T2-02 (coset union/correction, deferred), and that LIT-381 was listed without comparison.
- **Required:**
  - qualify novelty-gate-T2.md:3;
  - put one canonical disclosure in LOG;
  - carry a permanent timing qualifier into the IDEA registration, as for the IDEA-576 / gate-timing-response-01 precedent;
  - add IDEA-182/PD-N034 to T2-02's closest entries;
  - get AC's acceptance.

**A5. PD-N?…T3-01 (t3-short-relations.md) is not a failed-mechanism record.**
- Its disposition keeps the certificate as "a known prerequisite" and rejects nothing (lines 51-53).
- Its "attempted mechanism" (lines 57-58) is post hoc: nobody proposed it.
- AC's L5 rule (WORKFLOW:101) reserves PD-N for refuted or failed mechanisms. Reclassify it as PD-T, or name a real rejected candidate, before final IDs.

### MINOR

**B1. Stale or pending process text remains in durable records.**
- About 30 sites say "independent audit pending", "Independent rerun pending" or "Required Claude audit remains due", e.g.:
  - t1-minimal-obstruction.md:37,59,184
  - t1-reflection-classification.md:57,73
  - t4-*.md
  - t5-validation-and-measurements.md:6,125 ("MEASURED pending actual independent replay", although the distinct replay ran)
  - t2-finite-survivors.md:11
  - t6-*.md:43/58
- The IDEA template forbids pending process in candidate records, but novelty-gate-T6.md:77,112 and attempts/T4.md:34,65,93 carry it.

**B2. rounds.md is stale and internally inconsistent.**
- The "Current action" column (lines 8-14) still says "independent replay remains due", "independent cover next" and similar.
- It counts T6 as 1 round while attempts/T6.md has Round1 and Round2.
- Line 44 is inaccurate (see A3c).

**B3. The T6-01 verdict was not updated after the Subbotin match.**
- novelty-gate-T6.md:66 still says "variant with explicit … factor 3^d". Subbotin's Theorem 1 already has the same 3^-d.
- Template verdict: duplicate of LITERATURE (Subbotin 1983, Thm 1/Cor 1), retained as a local reproof. The supersession paragraph (lines 118-131) is right; the verdict field contradicts it.

**B4. Two report phrases are slightly overstated.**
- report.md:151 says "verified in primary literature"; :159 says E6 "confirmed as an established literature fact".
- Subbotin's Cor. 3 rests on Yudin's lower bound, which was not read (literature-T6.md:142-143).
- Suggested wording: "located in Subbotin 1983 (Thm 1/Cor 1/Cor 3 read; Yudin input unread) and independently reproved locally".

**B5. Split and ID-kind hygiene.**
- t4-monotone-lower.md:4 is "split from" a BRIEF expectation, but BRIEF.md:5 says nothing there carries a status.
- t4-quality-target.md:5-7 and t6-universal-lower-bound.md:7 list supporting results under "Split into". These are dependencies, not parts of the target.
- t6-universal-lower-bound.md:64 has an OPEN row inside a PROVED file's status table; move it to Open items.
- t1-open-class.md paraphrases handoff 01:42-46 without quoting the original wording in History (WORKFLOW:93).

**B6. PD-N "attempted mechanism" fields point to IDEAs whose aims succeeded.**
- t1-minimal-obstruction.md:45 points to T1-01, which is the obstruction route.
- t5-gaussian-grid-obstruction.md:37-41 points to T5-05.
- t4-monotone-lower.md:30-31 says T4-02, but attempts/T4.md:145 puts the refuted assertion under T4-04.
- The killed construction candidates need their own short records.

**B7. Provisional ID suffixes are reused for unrelated objects.**
- The slug abbreviation `padua-3d` is sanctioned by handoff 01:135.
- But IDEA T4-03 is the slice witness while PD-T T4-03 is the upper majorant.
- IDEA T5-04 is the symmetric class while PD-T T5-04 is the census; attempts/T5.md:50 and :55 use "T5-04" for both.
- PD-N T5-03 comes from IDEA T5-05.

**B8. The coordinator model is attributed to AC.**
- plan.md:3 ("as explicitly requested by AC") and LOG.md:26 attribute the Astra-high coordinator choice to AC.
- AC's quoted words (LOG.md:11) only allow Astra Ultra; the Astra-high assignment came from Claude's handoff 01:7.

**B9. literature-T1.md:21 cites tool-internal tokens** ("turn511134view0", "turn299544view0") as references. These are not durable locators.

**B10. Minor missed predecessors.**
- T4 omits IDEA-047, LIT-302 and LIT-378 (Morrow–Patterson O(n²), the very analogy behind E2), and LIT-382 (the QR/LU approximate Fekete and discrete Leja method behind both baselines).
- T6 omits LIT-391 (Wang–Wang–Wang: O(log^d n) hyperinterpolation) as context for the matching upper bound.

### NOTE

**N1. T6 source coverage is genuinely primary, at the stated locators.**
- literature-T6.md records a close Subbotin read (journal pp. 561–565: Thm 1, Lemmas 1–2, Cor 1 with proof, Cor 3) and DEKL PDF line ranges (Thm 2.3 with its main proof, Thm 3.4 with proof). It is not a secondary report.
- My DEKL v2 extraction confirms Thm 2.3 as stated and eq. (3.15), "Λ ⩾ 3^{-d} L(Γ*)", citing "[25, Theorem 1]" = Subbotin, Math. USSR Sb. 46 (1983) 561–570.
- I could not access Subbotin itself.

**N2. BRIEF E1–E6 statements in report.md:153-159 are accurate and scoped.**
- E1: subclass only. E2: refuted for monotone order only. E3: tested cyclic slice only. E4: untested. E5: unresolved.
- E2's unisolvence half (confirmed by PD-T?…T4-01) and the answer to the T2(a)/P3′ question (A3a) could be added.

**N3. Rounds and budget use.**
- 1–2 rounds per direction against ceilings of 25/8. No stop rule fired for T1, T2 or T3; stopping was the coordinator's choice (rounds.md:167-170).
- plan.md:25-28 anticipated a continuation handoff instead. Put the decision to AC explicitly: continue T1 (noninvariant cosets/unions), T2 and the T5 completion probe, or close.

**N4. Statuses are consistent.**
- t1-open-class and t4-quality-target are OPEN, not PARTIAL (correct).
- The PD-N measured failures (T4-02) are MEASURED with REJECTED: failed.
- The T2/T3 finite PROVED upgrade cites a committed checker plus a distinct-agent replay. The mathematical audit should confirm the reduction.
- Keeping T2-02's exact finite ranks MEASURED is conservative.

**N5. Hygiene checks pass.**
- Manifest verify PASS; no file over 16 KiB; cold-storage ledger hashes match.
- The inventory omits the regenerable /tmp T4 node arrays and the git-restorable D0 fixtures, and its checker_command repeats the generator.
- All nine commits carry Agent/Model trailers with unexposed runtime metadata disclosed. Claude's setup commit and LOG say "effort not exposed".

**N6. At PR preparation, the historical out-of-scope records need dated addenda** linking this topic, not rewrites: IDEA-120 ("Out of scope per AC: 3D Padua"), IDEA-013 and IDEA-029.

## Required before PR

A1–A5. B1–B10 can be fixed in the development response.
