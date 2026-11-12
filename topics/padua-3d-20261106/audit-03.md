# Audit 03 — padua-3d-20261106 — response-02 focused review and substantive audit of the restarted T7–T10 round

- Auditor: **Claude, Opus 5.5 (`claude-opus-5-5`), xhigh**, the independent auditor of Codex development, under handoff 07. This is the topic's third audit round.
- Orchestrator work: the core reruns, the receipt comparison, an independent check of every T8 witness, the n=2 Padua-type check, this report, and the third-round MINOR fixes.
- Six independent Opus 5.5 xhigh subagents each reconstructed one scope. Their reports are appendices: [Part A](audit-03/partA.md), [T7](audit-03/T7.md), [T8](audit-03/T8.md), [T9](audit-03/T9.md), [T10](audit-03/T10.md) and [novelty, records and stops](audit-03/novelty-records.md).
- A Sonnet 5.5 medium subagent applied the mechanical MINOR fixes, which the orchestrator then reviewed ([audit-03-fixes.md](audit-03-fixes.md)).
- No subagent changed Git state.
- Rules read at `54d554a13e135dc99a46c38728c9a2d74897a14c`. They are unchanged since `7afa6a5` and `d0e1bbb`.
- Audited candidate: **`696bca5fe8842b8b99ec298381c948206be79548`**. Head `54d554a` adds only handoff 07 and the status of handoff 06.
- Main: `f70a260`, unchanged. The branch changes only this topic and its results file.
- Date: 2026-11-06.

## Verdict

**Mathematics: accepted. No BLOCKING finding.** Every claimed status is supported:
- T7: the **computer-assisted PROVED complete all-phase n=2 coset classification**, confirmed by a census written independently, by a different method from both the producer and Astra.
- T8: the parity admissibility theorem; nine exact M=N witnesses at n = 1, 3, 4, 5, 7, 8, 9, 11, 12, re-certified here with fresh primes; the fold-count and union theorems; the F, U2, U3 and U4 kills.
- T9: the strict-positive-weight witness; the n ≥ 110 packing consequence, **PROVED with an explicit LITERATURE dependency** on Betke–Henk's 18/19 (statement and normalization primary-read again by this audit); the R-Leja transfer Λ ≤ 8·binom(n+9,9), with the 2015 primary source checked; the permutation-mean method obstruction.
- T10: determinant minima 2/12/38 at n ≤ 3; the critical-lattice folding counterexample (ratio 73/18); the parity Gram I+eeᵀ and the O(log⁴ n) projection bound; the CONDITIONAL O(log³ n) corollary (Kolomoitsev–Lomako Theorem 4.1 read; hypotheses fit); restricted-QR unisolvence.

The Part A response disposes of every audit-02 finding.

**Process and records: six MAJOR findings, so stage WORK.**
- Two directions do not yet meet handoff 06's stop rule (a): T10.1 and T9's finite-complement sub-route.
- The T10 extraction kill is mis-stated.
- Status labels for results with a literature dependency are inconsistent.
- Two gates miss predecessors.
- Killed frozen rules and some candidates lack proper records.

Following WORKFLOW's third-round rule, eligible MINOR items are fixed by the auditor in a separate commit (see the MINOR section below).

## Coverage

| Area | Read |
|---|---|
| Rules | AGENTS, WORKFLOW (including the third-round and proportionate-audit rules), CLAUDE_ROLES, templates |
| Registry | The current `state/IDEAS.md` read **in full** (1,154 lines, every obstruction and disposition table) by the novelty subagent. Relevant INDEX rows (LIT-004, 014, 301–331, 377–392, 413, 428, 486–512). |
| Topic | LOG after audit 02; handoffs 06–07; response-02 and deviations-02; report-round06; rounds; gates; all round06 gates, preregistrations and literature records; the four attempt files; manifests; cold storage; results file |
| Theory | Every `t7-r06-*`, `t8-r06-*`, `t9-r06-*` and `t10-*` file in full (by its scope subagent); diffs of every older file from 7afa6a5 to 696bca5 |
| Primary sources read by subagents | Betke–Henk arXiv math/9909172 (pp. 1, 2, 30, 31); Chkifa 2015 arXiv 1503.01731 (pp. 2–4, 13–15, 17–19); Li–Zong arXiv 2310.18643 (p. 2, restating 18/19); Kolomoitsev–Lomako Theorem 4.1 and its proof (pp. 18–19). Not reachable: the Henk erratum, Minkowski 1904, Belinsky. |

## Independent executions

Commands, hashes and outputs are in [audit-03/receipts.txt](audit-03/receipts.txt); audit code is in [audit-03/code/](audit-03/code/). Environment: Python 3.13.18 (receipts were made under 3.12.14), numpy 2.3.5, sympy 1.14.0, one BLAS thread, no `-O`, isolated scratch directories throughout.

1. **Manifest and core commands (orchestrator).**
   - `artifact_manifest.py --verify` gave PASS: 154 artifacts, 728,307 bytes.
   - All six handoff-07 core commands exited 0: the four `independent_r06.py` modes, the producer n=2 census (203 s) and the certificate.
   - Every scientific field matches the committed receipts, and the raw census hashes are identical.
2. **T8 witnesses (orchestrator, fresh code and fresh primes).** All nine M=N witnesses have exactly N distinct nodes and full rank N on the actual cosine nodes, from N = 4 up to N = 455 at n = 12.
   - The check maps through Z[ζ_L, ½] → F_p, with p ≡ 1 (mod L) prime and the root order verified.
   - The T8 subagent separately validated all 92 producer (p, ω) pairs and certified the witnesses at its own primes above 10⁹.
3. **T7 (subagent).**
   - An independent census without the quotient or kill lemmas visits 40,890,634 strata; 101,496 of them have 10 nodes.
   - The Burnside count gives 2,705,380 quotient strata and the decisions 2342 trace / 12 short-relation / 4 full-rank.
   - Full rank occurs only in the 36 listed groups.
   - 500,000 random-phase draws give no unisolvent set outside the list.
   - Exact rank is certified for all 36. The order-19 rank distribution is reproduced, and T7-06 measures Λ = 1998.95 on three meshes.
4. **T8 (subagent).** All 8 routes and the near-order run reproduce. Also confirmed: the parity proof, 671,080 fold counts, 499,776 rigidity cases, the n6 union rank 82, the F kill (335.9 against 49.8 at n7, 727.6 against 79.8 at n8), and the M21 witness with Λ = 31.2318.
5. **T9 (subagent).**
   - The witness algebra is verified symbolically.
   - Betke–Henk's 18/19 was read for translates of |x|+|y|+|z| ≤ 1, with Λ* of det 38/27 enumerated.
   - The threshold is exact: f(109) = −9809, f(110) = 2312.
   - The R-Leja recursion and indexing check out against the source. Actual Lebesgue constants for n = 1..9 lie far below the bound.
   - QR/localdet snapshots through n16 reproduce bit-identically.
6. **T10 (subagent).**
   - An own HNF enumerator gives minima 2/12/38.
   - The critical-lattice count is 146m³ by brute force.
   - The exact rational Gram check passes for n = 1..10.
   - Restricted-QR unisolvence is verified at n = 2, 3, 5 and 8 with different primes.
   - A rigorous norming bound shows continuous Λ_QR beats restricted QR at n6 and n7.
7. **n=2 Padua-type check (orchestrator).** The order-19 cyclic sets z = (1,3,7), (1,4,6), (1,5,8) have dual lattices of minimum ℓ1-norm 4. Their equal-weight Haar rules are therefore exact through degree 3 = 2n−1, on exactly N = 10 Π₂-unisolvent nodes. That is **the 2-D Padua property, realized in 3-D at n = 2.** Their measured Λ is 8.134, against 7 for QR. The fourth, (1,7,8), is exact only through degree 2.

## Findings

### BLOCKING

None.

### MAJOR

- **E1. T10.1's census is materially incomplete, so T10 does not yet meet stop (a)** ([T10 MAJOR 1](audit-03/T10.md), [novelty MJ2](audit-03/novelty-records.md)). The exact searches are cheap, and the catalogue misses minimizers.
  - **n=2.** 24 det-19 lattices give exactly N = 10 Π₂-unisolvent nodes with positive degree-3 Haar cubature (item 7). They coincide with T7's order-19 survivors, and no record links the two.
  - **n=1 and n=3.** The true minimal folded counts are 4 and 24, not the catalogue's 5 and 26 (exact ranks).
  - **n=4 and n=5.** The exact minimum determinants are 92 and 178, found in seconds.
  - **n=4..12.** With the imported packing bound, complete determinant windows close in minutes. At n = 6, 9, 12 and 15 the seeds already meet the bound.
  - Required: reopen T10.1 with exhaustive or measured-feasibility searches, kept separate for three objectives: minimum det, minimum folded count, and unisolvent minimum. Then restate the headline table.
- **E2. The T10 extraction kill is mis-stated** ([T10 MAJOR 2](audit-03/T10.md), [novelty MJ3](audit-03/novelty-records.md)).
  - The frozen receipt `evidence/t10-quality.json` itself records `extraction_kill` at degrees [6,7]. A rigorous norming bound confirms QR beats restricted QR at n6 and n7.
  - The n8 "win" disappears against the like-for-like global-QR ordering (35.816 against 45.458), and reverses on the 21³ mesh.
  - Required: replace "no literal kill" with "preregistered kill met at n6/7; n8..16 is disclosed post-kill verification". Give the killed rules a scoped PD-N, consistent with this topic's PD-N T4-02 and T8-03 precedent and the L5 rule.
- **E3. T9's finite-complement sub-route fails stop (a)** ([T9 M2](audit-03/T9.md)).
  - The unrestricted complement was set aside without measurement; the 617.9 GB figure concerns a family matrix, not a census.
  - Exact probes over all lattices with ℓ1-minimum ≥ 2n and det ≤ 8N finish in 13 s, 125 s and 706 s at n = 2, 3, 4.
  - They show positive unshifted rules with at most N nodes exist at n = 2, 3 and 4 (minimum node counts 7, 16 and 35), which the record does not state. The n = 4 example with exactly 35 nodes has rank 30.
  - Required: measure and record what is feasible, then continue to higher n or record measured infeasibility.
- **E4. Status labels for literature-dependent results are inconsistent** ([T9 M1](audit-03/T9.md), [novelty m1](audit-03/novelty-records.md), T10 note).
  - T9's packing consequence is "PROVED with explicit LITERATURE dependency".
  - The T9 R-Leja transfer is labelled PROVED, although its source proof uses an unread lemma ([7, Lemma 7]).
  - T10's log³ corollary is labelled CONDITIONAL, in an analogous position.
  - The audit's view:
    - PROVED-with-explicit-LITERATURE-dependency fits WORKFLOW (a cited theorem's dependence "remains explicit") and precedent PD-N022, *where the exact statement and normalization were primary-read*.
    - CONDITIONAL fits where a hypothesis or lemma chain was not checked.
  - Required: state one criterion, apply it to all three, and never shorten such a label to bare PROVED. **AC decides the convention.**
- **E5. Gates miss predecessors** ([novelty MJ1](audit-03/novelty-records.md)).
  - The T10 gate omits **LIT-391** (Wang–Wang–Wang 2014, O(log^d n) hyperinterpolation on the cube), which is the closest in-repository source for the log³ projection target and is cited in BRIEF:38 and handoff 04. It also omits IDEA-178, IDEA-013, PD-N035/037, LIT-382 and LIT-512.
  - The T7 gate omits IDEA-187 and PD-N037.
  - Also record Belinsky's classical theorem, which gives the dilated-polyhedron log³ kernel bound directly (T10 note).
- **E6. Records for killed rules and candidates are incomplete** ([novelty MJ3, MJ4](audit-03/novelty-records.md)).
  - The D2-killed frozen rules (T8 F, U2, U3 and U4, the initial Φ3 selectors, and the T10 extraction rules) have no scoped PD-N.
  - The T7 and T10 candidate records do not follow the IDEA template: rows still say "Active", and disposition reasons and resume conditions are missing.
  - The T7 Φ sub-item "degree-uniform H_n" has no recorded outcome. Folded and mixed unions were not attempted ([T7 M3, M4](audit-03/T7.md)); record these as resume items.

### MINOR

**Auditor-fixed in place (third round)**, in a separate commit and listed in [audit-03-fixes.md](audit-03-fixes.md). Theory files hash-pinned by `evidence/independent-r06-pins.json` are corrected by that dated companion note, not edited. The fixes cover:
- stale "pending rerun" and "integration notes" text;
- the `rounds.md` placement of the handoff-06 stop record;
- the T7 label-decoding note;
- slug normalization;
- attribution of the packing sketch, the fold bound, and the audit-02 M=N and lattice leads to Claude;
- T9 wording: the positivity statement, "critical lattice of 2O", and 108 instead of 648;
- T8 wording and stale-text items;
- the T10 condition-number wording.

**Returned to the developer** (not auditor-fixable):
- T8 MINOR-4: adding disposition reasons is a disposition edit.
- The results file, which is written by the topic orchestrator. It needs the four new T8 PROVED records, "computer-assisted" for T7-06, and links to the round06 successors.
- Template gaps in T9 theory files; five T9 IDs without their own file; the non-standard `MEAS?` namespace.
- Recording D3 for the T9-r06 and T10-03 obstructions.
- One-place disclosure of the round06 protocol timing (prereg addenda published together with results) and of T8's post-run reading.
- The 51-file hash check: record its command and correct its wording.
- Duplicate provisional source records (Betke–Henk twice, DMVX, Cools–Poppe).
- The complement receipt pins a prose hash that is in no commit.
- `t10-log3-target.md` gives two statuses.
- Hard-coded half-shift values in `t10_lattices.py:117`.
- n2..7 rank certificates are not tied by hash to the quality-run selections.
- "certifies" versus MEASURED in the report.
- The preregistered Minkowski request was neither made nor recorded as pending.
- The supplementary checker pins prose, against the rule "new checkers do not pin prose".
- Optional hardening of the manifest guard's suffix and subdirectory scope.

**LOG correction:** `LOG.md:337-338` cites deviations-02 for the model-attribution withdrawal. It is in deviations-01, m11. Recorded in this audit's LOG entry, not edited into history.

### NOTE

- **Unclaimed upgrade.** The T8 finite certificates now meet every computer-assisted-PROVED condition: proved reduction, exact arithmetic, committed checker and evidence, and an independent rerun at different primes. An upgrade would be a material status change for the developer. ([T8 N1](audit-03/T8.md))
- **New lead (T8 subagent, MEASURED).** Half-shifted M = 2N orbits (phase z/(2M)), which the special-strata grid could not reach, are exactly unisolvent at n3, M40. For example z = (1,4,11) has Λ₂₁ ≈ 9.79. That beats every T8 n3 set and Leja (13.17) and approaches T7's optimized 9.74. The "M=2N: 0" row is an artefact of the grid.
- **n=2 Padua-type sets** exist (item 7). Together with E1 and E3, the small-n data show the Haar packing bound has slack at n ≤ 4: rules with at most N nodes exist, but at n = 3 and 4 none found is unisolvent.
- **Duplicate set counts.** The four order-16 n2 groups give one node set, and the 32 order-19 groups give 8, or 2 up to permutation. The 7.053–8.134 "range" is two values.
- **Astra checker method.** The supplementary T7 checker reuses the producer's design; this audit's T7 census is the first check by a genuinely different method.
- **Chronology:** consistent in publication order. Execution order rests on developer attestation, as disclosed. Protected audit and handoff bodies are intact.
- **Pending AC decisions:**
  - T2 gate timing, the T5 probe, and the old budgets (deviations-01);
  - T9 timing and edit, and T7 reading coverage (deviations-02);
  - the E4 label convention.

## Residual uncertainty

- Not read: the Henk erratum, Minkowski's original, Belinsky, Cools–Lyness, and Kolomoitsev–Lomako §3.
- T9 and T10 rely on Betke–Henk for 18/19, corroborated by Li–Zong 2025.
- Determinant minima at n ≥ 7 and at n ≡ 0 (mod 3) depend on that bound.
- Execution order is attested only by the developer.
- No historical novelty is established for any T7–T10 result.

## Required response

Handoff 08 sends this to a Codex response. It answers E1–E6 and the returned MINOR items in `response-03.md`, reopens T10.1 and the T9 complement within the running counters, and gets a focused re-audit of the material changes.
