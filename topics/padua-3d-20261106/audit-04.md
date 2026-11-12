# Audit 04 — padua-3d-20261106 — combined formal audit

This audit covers the handoff-09, handoff-11, handoff-15 and handoff-17 scopes:
- the audit-03 response, exact lattice objectives and the T8 half-shift work;
- the usable campaign U1–U3;
- the interim response and the seven-round continuation;
- the pruning campaign P1–P5 with its exact artifacts.

**Audit record**
- Auditor: **Claude, Opus 5.5 (`claude-opus-5-5`), xhigh**, the independent auditor of Codex development, under handoff 17. It also carries the preserved scopes of handoffs 09, 11 and 15. This is the topic's fourth Claude audit round.
- Orchestrator: producer reruns, an independent check of the 455-node proof, this report, and review of the third-round MINOR fixes.
- Eight independent Opus 5.5 xhigh subagents each reconstructed one scope. Their reports are appendices:
  - [A1 lattice objectives](audit-04/A1.md)
  - [A2 T8 half-shift / finite PROVED proposals](audit-04/A2.md)
  - [A3 response-03, labels, manifests, interim records](audit-04/A3.md)
  - [B1 U1](audit-04/B1.md)
  - [B2 U2 and the 455-node proof](audit-04/B2.md)
  - [B3 U3](audit-04/B3.md)
  - [D pruning and the exact sets](audit-04/D.md)
  - [novelty, gates, budgets, records](audit-04/novelty.md)
- A Sonnet 5.5 medium subagent applied the mechanical MINOR fixes ([audit-04-fixes.md](audit-04-fixes.md)), and the orchestrator reviewed them.
- No subagent changed Git state. Each subagent executed only in its own `git archive` copy.
- Rules were read at `dafb8c8410d9c81671902c382655036d54c8b698`. They are unchanged since `9042e1c`.
- Audited candidate: **`e7c9900ec7dc232d2e117cc72dd47b79c7a0fe26`**. Head `dafb8c8` adds only handoffs 16 and 17.
- Main is `f70a260`, unchanged. The branch changes only this topic and its results file.
- Date: 2026-11-08.

**AC instructions received during this audit (verbatim):**
- "When finished, use opus extra to reassess the 3d frontier: should this direction be frozen or is it worth pursuing some extra rounds? seems that the case is genuinely hard, but you may try to do inspiration round with literature and maybe neigboring fields before deciding."
- "looks like there is a huge gap between log 3d asymptotics and what is actually available of point sets. in 2D Padua group was lucky with lissajous. But I suspect that one has to look for deeper algebraic structures in 2D, not just sin/cos intersections, that may transfer to 3D. I feel that Lissajous/Chebyshev is just a well-known representation of deeper structures"
- "otherwise this branch becomes substantial. I authorize exceeding all limits with 100%, to be potentially discussed at PR"

Claude reads the last instruction as provisional authority to exceed the storage limits by up to 100%, to be discussed at PR. That means the 16 KiB per-file and manifest caps may reach 32 KiB, and the 5 MB repository-wide generated-output limit may reach 10 MB. It is not read as an extension of round budgets. The frontier reassessment is a separate record: [frontier-assessment.md](frontier-assessment.md).

## Verdict

**Mathematics: accepted across all four batches. No BLOCKING finding.** Every claimed PROVED, CONDITIONAL, MEASURED and OPEN status is supported, including the computer-assisted finite claims:
- **Lattice objectives.**
  - Determinant minima for n = 1..16. Independent code covers n1..10 from q = 1 and n4..16 from the packing window.
  - Global folded minima 2/7/16/35/54 and full-rank minima 4/10/24/45/75.
  - The n7 digest `909f9922…`, reproduced by an algorithmically independent enumerator.
- **T8.**
  - The even-n half-shift obstruction.
  - The cubic classification: 741 normalized triples, of which 8 are full-rank, all with |det| = 2^49.
  - The narrow PROVED old-nine M = N existence through n = 12.
- **U1 algebra:** the Gram identity I + eeᵀ, the trace bounds and the Gauss–Markov identity, all checked in exact arithmetic.
- **The PROVED Π₁₂-unisolvence of the 455 stored dyadic points.** It is certified independently three times:
  - by the orchestrator, at two primes;
  - by the U2 subagent, at three primes in two bases;
  - and its NPY bridge is re-established.
- **U3:** the support census, the coherent-phase reduction, the folded universe, the mixed witnesses and the septic labels. The 512-start M/R schedules are now fully replayed.
- **Pruning.**
  - Rank 455 and 969 for the 546- and 1163-site sets, at four new primes and two new bases.
  - Both payload ID sets reproduce from an independent SVD replay of the A-deletion rule.
- **MEASURED claims:** every reproducible one replicates. The search values are lower samples only.

The E4 label convention remains **AC's decision** and is not settled by this audit.

**Process and records: seven MAJOR findings, so stage WORK.** All are record, disclosure or gate items. None changes a theorem.

## Executions

- **Orchestrator** ([audit-04/receipts.txt](audit-04/receipts.txt)):
  - Manifest verify: PASS, 310 artifacts, 1,872,829 bytes.
  - `uc12_payload_check.py` passes (prime 1000037, residue 318086).
  - `pdpr_certify.py verify` passes for both pruned payloads.
  - `t8_r08_check.py --old-witnesses` and `--halfshift --quality` both pass.
  - Its own 455-node checker (`audit-04/code/u12_check.py`): 455 distinct dyadic points (denominators up to 2⁶⁵), full rank modulo 2147483647 and 998244353, coordinate hash matching the payload.
- **Subagents:** independent code and reruns, listed with full commands and hashes in each appendix. In summary:
  - A1: its own C++ enumerator and rank code; producer `min` 1..12 and `complement` 2..5 reruns.
  - A2: an exact census in a different basis, with fresh primes above 2.5e9.
  - A3: 19 manifest mutation controls, historical-manifest verifies and `--list` round trips.
  - B1: all 24 U1 cases plus the continuation, reimplemented independently.
  - B2: the 455-set determinant at three primes; R1–R3 and C3/C4 reruns; a full trace audit of every guarded step.
  - B3: all six U3 claim groups reimplemented, plus the full M/R replay.
  - D: an exact-rank checker; P1–P5 measurements recomputed; the noise normalizations recomputed separately.

## Findings

### BLOCKING

None.

### MAJOR (returned to development; record-level)

- **G1. The T8 tie-repair reasoning is applied at n3 but not at n7** ([A2 MAJOR-1](audit-04/A2.md)).
  - The selected (1,17,212) has an exactly tied partner, (1,17,28): the x₃-reflection, lexicographically smaller. Under the rule used at n3, that partner should be chosen.
  - Λ is identical, so no status changes.
  - Fix: relabel n7, or disclose it with scope, and amend "n5/7 selectors unchanged".
- **G2. The C1 cost-gate failure is hardware-dependent** ([B2 MAJOR-1](audit-04/B2.md)).
  - An unchanged rerun is byte-identical through step 176 and completes 200 steps in 116.05 s, against the cap of 120 s; the recorded run hit the cap at 120.72 s. The full C1 gate then passes, with ratios 0.526 and 0.543.
  - The MEASURED "this hardware" scope holds. The "REJECTED: failed / park" disposition and the C2 motivation, however, read as properties of the recipe.
  - Fix: add a dated addendum, or revise the disposition. The developer proposes which; AC decides any dispute.
- **G3. The documented prose-pins replay fails at the candidate** ([A3 M1](audit-04/A3.md)).
  - `evidence/independent-r06-pins.json` is labelled current but still pins the v5 `artifact_manifest.py`. As a result, `r08_hygiene.py pins` (`response-03-hygiene.md:28`) raises an AssertionError.
  - Scientific impact: none, because the master manifest still pins the file.
  - Fix: refresh the pin, or retire the replay with a dated note.
- **G4. Split headers disagree** ([A3 M2](audit-04/A3.md)).
  - New PD-N homes say "Split from" a parent whose own header says "Split into: none". This affects:
    - the T9 unshifted-minimal-cubature and parity-oversampling records;
    - the two T10 extraction PD-Ns;
    - the five T8 PD-Ns.
  - `response-03-records.md:144-156` asked for these back-links, and they were not added.
- **G5. An undisclosed tolerance deviation in U3 F** ([B3 MINOR-2](audit-04/B3.md)).
  - The F rule registered a relative 1e−9 tie tolerance; the code applies an absolute 1e−9 to the log score.
  - The outcome cannot change. It is a threshold disclosure, so it is returned under WORKFLOW's in-doubt rule.
- **G6. The pruning and U2 gates miss their closest predecessors** ([novelty N-M1](audit-04/novelty.md)).
  - `pruning-gate.md` omits LIT-385 (Cohen–Migliorati and Kadison–Singer/MSS O(N) subsampling; Bartel–Schäfer–Ullrich) and LIT-386 (Piazzon–Sommariva–Vianello Carathéodory–Tchakaloff compression). It also has no comparison row for measure compression or frame sparsification.
  - Classical optimal-design sources behind the "known backward D-optimal design" label have no INDEX record.
  - The Lebesgue-point optimization literature is missing from INDEX: Chen–Babuška, Briani–Sommariva–Vianello, Rapetti–Sommariva–Vianello, Heinrichs. So is **Gunzburger–Teckentrup (arXiv 1407.3291)**, whose optimized 3-D Lebesgue constants for n = 1..5 (2.00, 2.95, 4.05, 5.09, 6.40) are the natural external benchmark for U2. Found by the frontier scout S5; see the [frontier assessment](frontier-assessment.md).
  - Fix: a dated gate addendum stating the differences. No novelty claim is affected.
- **G7. Pruning candidate records and provisional IDs** ([novelty N-M2](audit-04/novelty.md)).
  - `theory/pruning-p5-pair-boundary.md` is not in THEORY-template form.
  - PRUNE-H (deferred) and PRUNE-FORCE-N (abandoned) have no IDEA records, and there is no pruning disposition table.
  - prune-next-02 still reads "retained" and needs a deferral record.
  - 26 new provisional IDs lack the agent component that WORKFLOW requires.

### AC decision items (not developer defects)

- **Storage.** Committed generated output totals about 8.33 MB repository-wide; main alone is about 7.0 MB. This topic contributes 1.34 MB, of which 0.88 MB was added since audit 03. The master manifest is 16,341 of 16,384 bytes.
  - Under AC's 2026-11-08 allowance (up to 100% over), both are currently within the provisional limits: 10 MB total, and 32 KiB per file and manifest.
  - Recorded for discussion at PR ([novelty N-M3](audit-04/novelty.md), [A3 NOTE](audit-04/A3.md)).
- **E4 label convention:** still pending. The audit records its alternative wording again ([A3 m1](audit-04/A3.md)).
- **Lattice stop(a) boundary** ([A1 N3](audit-04/A1.md)). The 120-second gate measures implementation cost, not infeasibility. The auditor's unreplicated runs complete n8 for det ≤ 1320 in 80 s (no rule with at most 165 nodes) and find global minima at n6 and n7:

  | n | global folded minimum | global full-rank minimum | witness |
  |---|---|---|---|
  | 6 | 91 | 112 | (6,0,7,7,7,14) |
  | 7 | 128 | 164 | (7,0,8,8,8,16) |

  AC may decide whether that gate is the "as far as feasible" boundary.
- **Earlier canonical deviations** (deviations-01/02): unchanged and still pending.

### MINOR

Eligible items are fixed in place by the auditor, as WORKFLOW requires from the third round onward. They are committed separately and listed in [audit-04-fixes.md](audit-04-fixes.md). Items outside the auditor-fix limits are returned there. The fixes include:
- A1: the "exact-N positive rule" wording, which should say Padua-type, rank-N; "unisolvent" used for oversampled sets; the "full independent coverage" wording.
- A2: the D2 "cannot be assessed" wording and table labels.
- A3: stale log³ labels and the "published" source wording.
- B1: replication-dependent ordering, "raw unit-noise trace", protocol chronology.
- B2: three omitted regressions, and an assumptions note for the asserts.
- B3: the n8 QR tie-break note.
- D: the 5/15 count, a checker-hash note, the one-observation-per-site traces, the export chronology.
- Novelty: rounds, cold-storage pointers, crediting Claude-originated leads (the n=2 Padua-type observation and the (1,4,11) half-shift lead), and missing-space hygiene.

The orchestrator applies the LOG and results-file items: links to handoffs 15 and 17, and the stale next step.

### NOTE

- The finite exact claims are now each independently confirmed by Claude, beyond the Codex supplements, often by algorithmically different methods.
- The n7 lattice digest no longer rests on one implementation.
- The U3 M/R optimizer schedules are now actually replayed.
- QR/Leja control values depend on floating-point tie-breaking at n8 and n16. Every conclusion survives, since better controls only enlarge the measured losses.
- Chronology: every protocol commit precedes its run.
  - The P2 seed swap came 18 s before its run, and is disclosed.
  - Some driver code was committed together with its results.
  - Execution order rests on developer attestation.
- The interim Codex audit is correctly framed as not being Claude acceptance. Its fixes stayed within auditor-fix limits.

## Residual uncertainty

- Lebesgue and amplification values are lower samples, not certified suprema.
- Timing gates are hardware-dependent (G2).
- The packing-bound dependence (18/19, Betke–Henk) remains a LITERATURE dependency under the pending E4 convention.
- No historical novelty is established. The gate gaps (G6) leave source comparison incomplete for the U2 and pruning mechanisms, which are known techniques.
- Claude did not re-read the full `state/IDEAS.md` this round beyond the novelty subagent's complete read.

## Next step

Handoff 18 combines the developer response to G1–G7 with the frontier decision recorded in [frontier-assessment.md](frontier-assessment.md).
