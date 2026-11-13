# Audit 02 — padua-3d-20261106 — focused Part A re-audit and substantive T7–T9 audit

- Auditor: **Claude, Opus 5.5 (`claude-opus-5-5`), xhigh**, the independent auditor of Codex development, under handoff 05.
- Depth: Opus 5.5 xhigh throughout. The batch adds novel mechanisms, negative results and computer-assisted PROVED claims.
- Orchestrator work: producer reruns, receipt comparison, two exact checks of its own, and this report.
- Five independent Opus 5.5 xhigh subagents each reconstructed one scope. Their reports are appendices: [Part A](audit-02/partA.md), [T7](audit-02/T7.md), [T8](audit-02/T8.md), [T9](audit-02/T9.md) and [novelty and records](audit-02/novelty-records.md).
- No subagent changed Git state. Each executed code only in its own `git archive` copy.
- Rules read at `e14ac15fd95f557e13d9c739ae097227cdb562c8`. They are unchanged from `d0e1bbb` (`git diff` of AGENTS.md, agents/ and templates/ is empty).
- Audited candidate: **`e80e000f2ba439ea62c966d255ef1b900b608b27`**. Head `e14ac15` adds only handoff 05 and the status of handoff 04.
- Reconciled main: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. The candidate differs from main only inside this topic and its results file.
- Date: 2026-11-06.

## Verdict

**Mathematics: accepted.** Every claimed PROVED, CONDITIONAL, MEASURED and OPEN status in the Part A response and in T7–T9 is supported. That includes:
- the computer-assisted PROVED T7-06 (the 20-node translated rank-two cubic survivor);
- PROVED T7-07, T8-02 (every-phase M=10), T9-01 (Λ > 1.2274), T9-02 (coefficient 1/(24π³)) and T9-03;
- the CONDITIONAL PD-N T9-01 (n ≥ 110, conditional on density ≤ 18/19).

The Part A response disposes of every audit-01 finding: each is fixed, or left unresolved and disclosed. No accepted T1–T6 statement, proof or status changed, apart from the agreed m1 wording "each of R₁, R₂, R₃". No BLOCKING finding.

**Process: four MAJOR findings, so stage WORK.** The main one is that **every new direction stopped early without a valid stop reason under handoff 04**. The others are a T9 gate gap, an undisclosed T9 gate edit, and one ID-kind question.

At AC's instruction (2026-11-06) the continuation is [handoff 06](handoffs/06-work.md). It is a more adventurous Codex round with the 25-round counters restarted.

## Coverage

| Area | Read |
|---|---|
| Rules | AGENTS.md, WORKFLOW, CLAUDE_ROLES, HANDOFF/IDEA/THEORY templates |
| Registry | The current `state/IDEAS.md` read **in full** (1,154 lines, every obstruction and disposition table) by the novelty subagent. Relevant `literature/INDEX.md` rows. |
| Topic | LOG from audit 01 onward; handoffs 03–05; response-01, response-deviations-01 and all `candidates-*-response-01.md`; report-continuation-04 and report corrections; rounds; gates; results file. All T7/T8/T9 gates, preregistrations, literature records and attempts; `mathematical-development-T8.md`; both new supplementary-check records; manifest and cold storage. |
| Theory | Every `theory/t7-*`, `t8-*` and `t9-*` file in full (by its scope subagent). Diffs of every pre-existing T1–T6 file, e5b6445→e80e000. |
| Primary sources | None newly read. Minkowski's 18/19, Betke–Henk and Chkifa are recollections only; see the residual uncertainty section. |

## Independent executions

Commands, code hashes and outputs are in [audit-02/receipts.txt](audit-02/receipts.txt); audit code is in [audit-02/code/](audit-02/code/). Environment: Python 3.13.18 (receipts were made under 3.12.14), numpy 2.3.5, sympy 1.14.0, scipy 1.17.0, mpmath 1.3.0, one BLAS thread, no `-O`.

1. **Manifest and producers.** `artifact_manifest.py --verify` gave PASS: 56 artifacts, 309,009 bytes. All 14 handoff-05 commands exited 0 in a detached worktree of `e80e000`.
   - Every scientific field matches the committed receipts.
   - The only differences are Python version, timings and output paths, plus the T8 `preregistration_sha256` field.
   - That field is expected to differ. The committed f089f36d… is the file at `51c031a`, which I verified by hashing. The rerun hashes the current file (MINOR T8-3).
2. **T7-06 exact certificate (orchestrator).** I wrote fresh code, independent of the producer and of the Astra checker.
   - The coset has 20 distinct nodes.
   - The 20×20 monomial determinant, mapped through Z[ζ₁₀₁₀, ½] → F_p, is nonzero mod **8081** and **20201** (primitive 1010th roots verified). These primes differ from the developer's 607 and 5051, so the set is Π₃-unisolvent.
   - Its floating determinant is −1.85e−6, which suggests poor conditioning.
   - The T7 subagent separately certified it with 6 primes × 3 roots and verified T7-07's quartic exactly in Q(ζ₁₀₁₀).
3. **T8 (subagent).** An independent census, which does not use unit reduction for coverage, enumerated 3,446,517 folded primitive triples at n = 3.
   - It reproduces 15,733/112,314 classes and 95/300 node sets, with exact ranks.
   - The cubic full-rank set is unique: M=38, z=(1,6,17).
   - Also verified: the O slice 1/5 survivors, the P quadratics exactly in Q(ζ₁₂₀), the trace theorem (with 36,252 rigorous F_p phase cases) and the E-rule kill.
4. **T9 (subagent).**
   - Exact symbolic box integral for T9-01.
   - A falsification search: the minimum Λ over 4-point n = 1 sets is 2.0, and a linear program over projections onto Π₁ gives 1.5. Neither is below 1.2274.
   - Interval-certified threshold n = 2420.
   - Exact check that f(109) < 0 < f(110).
   - Padua consistency for n = 1..12.
   - Its own maxima evaluation agrees with the receipts to 6e−15.
5. **Part A (subagent).**
   - The actual-point full-cap invariant census reproduces 636/1392/757/2520/4803 with 0 survivors.
   - The symmetry classes 18/100/301 and the lexicographic choice (1,15,19) reproduce.
   - Four mutations of the manifest guard each fail loudly.
6. **New lead, orchestrator check.** A phase-shifted cyclic orbit with **M = N = 20, z = (1,2,7), phases (30,75,69)/120** has 20 distinct nodes and full rank 20 modulo 241, 601 and 1201. It is therefore exactly Π₃-unisolvent.
   - The T8 subagent found it; it lies outside PD-N T8-02, which needs n = 2 in the family.
   - A seeded floating screen of 300 random (z, φ) per degree finds numerically full-rank M = N orbits at n = 3, 4 and 5 (25%, 34% and 14%), and none at n = 2 or 6. This is consistent with the parity-trace condition. **MEASURED lead only, unrecorded in theory.**

## Claim results

| Record | Status claimed | Audit |
|---|---|---|
| Part A material fixes (M1–M5) | — | Accepted: predecessors, retained candidates and resume conditions, permanent T2 timing qualifier, full-class D3 diagnostic, PD-N→PD-T mapping. |
| T7-01/02 general dictionary, short-relation lemma | PROVED | Accepted, including double counting of zero coordinates (verified exactly: 380/400 entries break without it). |
| T7-03 finite/HNF/stratum reduction | PROVED | Accepted. Rank variation within a stratum is confirmed (det −9/4 example). No census is claimed. |
| T7-04 rank-two shortcut refutation; T7-05 ten-point example | PROVED | Mathematics accepted. ID kind: see MAJOR C4. |
| T7-06 cubic survivor | PROVED (computer-assisted) | **Accepted:** proved reduction, exact arithmetic, committed checker and receipt, and three independent certificates. |
| PD-N T7-07 quartic, no signed degree-4 rule | PROVED | Accepted; the integral cos²δ > 0 checked exactly. |
| T8 order cap and quotients | PROVED | Accepted. |
| T8 U/O/P classifications, E screen | MEASURED | Accepted. Reproduced independently. |
| T8-02 every-phase M=N=10 obstruction; trace theorem | PROVED | Accepted. Scope is n = 2 only; n = 3 counterexamples to any extension exist (item 6). |
| T9-01, T9-02 | PROVED | Accepted. The real/complex norm distinction is handled correctly. |
| T9-03 Haar/dual reduction | PROVED | Accepted. |
| PD-N T9-01, n ≥ 110 | CONDITIONAL on density ≤ 18/19 | Accepted as CONDITIONAL; the threshold is exact. |
| T9-04/05 transfer and correction | PROVED implications | Accepted. The missing premises are named and no construction is claimed. |
| T9-06 refined maxima | MEASURED | Accepted. The preregistration (`51c031a`) predates the receipts (`e80e000`). |
| Fekete Λ ≤ N | duplicate classical baseline | Accepted. |

## Findings

### BLOCKING

None.

### MAJOR

- **C1. None of the three directions meets handoff 04's stop rule.** That rule allows an early stop only on a gate kill, a proved obstruction or a recorded exhaustion. See [novelty A1–A3](audit-02/novelty-records.md) and [T7 NOTE-4](audit-02/T7.md).
  - **T7 (2/25 rounds).** The stated "proved obstruction" covers only the refuted shortcut inferences and one survivor's cubature marker (`attempts/T7.md:263-271`).
    - The decisive n = 2/3 all-coset census from handoff 04 was not run, and its infeasibility was not shown.
    - The survivor rule was not applied: no degree-uniform rule, and no D2 quality screen. T7-06's Lebesgue constant was never measured.
  - **T8 (2/25 rounds).** "Recorded scope exhaustion" (`attempts/T8.md:126-131`) does not hold.
    - Coset unions (handoff variant 4) were never attempted.
    - The special-phase strata became resumable once T7-03 met their resume condition, but were not resumed.
    - M = N phase-shifted orbits at degrees outside PD-N T8-02 are unisolvent (item 6) and are unexplored.
  - **T9 (1/25 rounds).** Its own stop rule is unmet (`attempts/T9.md:35-43`).
    - Route 3 (class-specific lower bounds) has no record.
    - The finite complement n < 110 has no feasibility statement and no deferral.
  - **Disposition.** No status is affected. AC has since ordered a restarted 25-round continuation (handoff 06). The response must correct the stop wording in rounds/attempts/report and resume these routes there.
- **C2. The T9 gate is incomplete** ([novelty A4](audit-02/novelty-records.md)).
  - No search terms are logged.
  - Missed predecessors:
    - for packing: IDEA-029, IDEA-044, IDEA-109, IDEA-120, LIT-010, LIT-307, LIT-389, LIT-413, OBST-11, LIT-192 and LIT-374;
    - for extraction: IDEA-027;
    - for Fekete: IDEA-209;
    - for the explicit polynomial-bound target: IDEA-047 and LIT-378.
  - T9-K's separation is compared only with T6, not with Subbotin's Corollary 1 on arbitrary projections, which `literature-T6.md` already records.
  - Lattice-rule literature on trigonometric degree is not in INDEX at all: Cools–Lyness K-optimal rules, Noskov, Lyness–Sørevik. Handoff 06 makes this the lead route, so it must be gated first.
- **C3. A T9 gate deviation and an in-place edit of a published gate are not disclosed** ([novelty A5](audit-02/novelty-records.md)).
  - `novelty-gate-T9.md` says its analytic ideas "were developed while reading". That contradicts LOG:203-205 and attempts/T9 step 0.
  - The gate published at `51c031a` was edited in place "before final freeze": the IDEA-203–205 citation was corrected, and T9-LOCALIZED was silently changed from deferred to equivalent.
  - Required: disclose this once in `response-deviations-01.md` (or a `-02` record), restore the history with a dated note, and put it to AC.
- **C4. ID kind for refuted T7 inferences** ([novelty A6](audit-02/novelty-records.md)).
  - The refutations of the rank-two shortcut (T7-04) and of one-phase-per-stratum (inside T7-03) are filed as PD-T.
  - The split rule, the L5 decision and the IDEA-161→PD-N021 precedent point to scoped PD-N records.
  - Propose a classification and record the mapping before final IDs. Disputes go to AC.

### MINOR (fixable without re-audit unless a fix becomes material)

- **n1. Part A hygiene** ([Part A N1–N5](audit-02/partA.md)).
  - Boilerplate copied into candidate template fields (deferred and T5 records).
  - The m5 addendum's "require focused re-audit" in 21 theory files goes stale after this audit.
  - Stale "PD-N T3-01" label at `attempts/T3.md:98-99`, and "T3-02" names three different objects (fix with full namespaced IDs).
  - Inconsistent pointers to the canonical disclosure (LOG vs `response-deviations-01.md`).
  - Stale or unsupported prose:
    - `response-01.md:12-15,75,128`, citing "integration notes" that were never committed;
    - garbled `report.md:194`;
    - `LOG.md:186` and `response-deviations-01.md:28-29`, which attribute the Astra-high choice to AC without a quote.
- **n2. T7** ([T7 MINOR-1/2, NOTE-3](audit-02/T7.md)).
  - IDEA and PD-T/PD-N numbering offsets make bare references ambiguous (`attempts/T7.md:64,115,241`).
  - No provenance is recorded for how the pilot parameters were chosen, and the "registered before execution" note sits in the result commit.
  - The results file omits "computer-assisted" for T7-06.
- **n3. T8** ([T8 MINOR-1–3](audit-02/T8.md)).
  - The E rule has no prospective `gates.md` entry, and its chronology is self-attested.
  - `t8-phase-obstructions.md:13-14,29` still says OPEN without pointing to PD-N T8-02.
  - `t8_cyclic.py:124` hashes the current preregistration, so the field cannot be reproduced; pin the historical hash instead.
  - `t8-finite-screens.md:15` says a rerun is still awaited, though it has been done.
- **n4. T9** ([T9 MINOR-1–3](audit-02/T9.md)).
  - The square-wave term only becomes the operative bound from n = 4592, not 2420.
  - Attribute 18/19 to Minkowski 1904 and drop "normalization" from the unverified items, since lattice packing density is invariant under linear maps.
  - Add coset unions to the escape list in `t9-packing-conditional.md:18-21`.
- **n5. Attribution.** The packing argument (n ≥ 110, 19n³/108, 2-D check, escape list) and the fold bound |H| ≤ 8N came from Claude's handoff 04. The records credit only a "T1 sketch". The ten-point example, Chkifa–Cohen–Schwab and Fekete are correctly attributed.
- **n6. Records** ([novelty MINOR list](audit-02/novelty-records.md)).
  - Mixed ID slug forms; T9 candidates without IDEA? IDs.
  - Stale links: t1-open-class → T7/T9; T1-Haar "deferred" against T9-HAAR; T2 variants without pointers to their T8 outcomes; a double-canonical T5-04; stale metadata SHAs.
  - Frozen gates edited without dated in-file notes.
  - T9 receipts lack command, versions and rules SHA, and `/tmp` raw T9 files are not inventoried.
  - The e80e000 trailer omits that Sol high wrote the T8 proofs, and the allocation deviation is recorded only in prose.

### NOTE

- **Chronology:** consistent. T7/T8 gates and preregistrations at `1c75e1f` precede results at `51c031a`; the T9 gate and preregistration at `51c031a` precede `e80e000`. Commit order is not execution order.
- **PD-N T7-07:** "refuted" would be the more exact reason.
- **Conditional PD-N:** CONDITIONAL PD-N T9-01 has no precedent in PROOF_STATUS; confirm at allocation that the L5 rule accepts it.
- **T8 census independence:** this audit gives the first fully independent reimplementation of the census enumeration. The Astra checker re-ran the producer's enumerator.
- **Unclaimed upgrades:** T8's P ranks and U/O classifications could arguably be upgraded but are not.
- **Hard-coded path:** `t8_cyclic.py` hard-codes `/tmp/padua-3d-20261106`, so concurrent reruns can collide.
- **T7-06 conditioning:** the survivor's tiny determinant makes poor quality likely. Measuring it is part of handoff 06.
- **T9 subagent census (MEASURED, q ≤ 40):** exact unshifted Haar cubatures of degree 2n−1 with at most N nodes exist at n = 2 (7 nodes) and n = 3 (20 nodes, rank 17), consistent with no packing conclusion for n ≤ 109.
- **Unverified lead:** Chkifa, JAT 2013, on ℜ-Leja sequences may supply T9-04's missing premise (recollection).
- **Pending AC decisions** (unchanged): the T2 gate-timing deviation, the unexecuted T5 completion probe, and the earlier unused budgets.

## Residual uncertainty

- No primary source was read for the 18/19 density, Subbotin, Chkifa or the lattice-rule literature.
- Historical novelty of T1, T4, T7-06 and T9-01/02 is not established.
- The M = N floating screen is a MEASURED lead only.
- Commit chronology cannot prove execution order.

## Required response

The response is handled in handoff 06, Part A: answer C1–C4 and n1–n6 in `response-02.md`. Then a focused re-audit covers only the material changes, together with the new handoff-06 work.
