# Handoff 06 — padua-3d-20261106 — adventurous round: restarted budgets on the most promising 3-D routes

- Status: open
- Previous handoff: [05-audit.md](05-audit.md)
- Next agent / model / effort: **Codex**.
  - Coordinator: gpt-6-astra high.
  - Mathematical workers: gpt-6.1-sol xhigh.
  - Code and screens: gpt-6.1-sol high.
  - **Astra ultra is allowed when necessary** (AC's original instruction): for a stalled proof of a degree-uniform family or of the packing obstruction, with a written justification in the LOG each time.
- Role: developer and orchestrator.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `9e71858a1c702236b5c6d64a6680324704632af3` (audit-02 output). The following commit publishes this file.
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`. Fetch first and reconcile if main has moved.
- Stage: **WORK**.
- Written by / date: Claude, claude-opus-5-5 xhigh · 2026-11-06, at AC's request.

## AC's instruction (2026-11-06, verbatim)

> "make then a more adventurous handoff for one more codex round, indicate what are the most promising rounds"

> "one more means restarting the 25 counter"

**Budget.** Every direction below starts a **new counter at 0, with a ceiling of 25 rounds**: T7, T8, T9 and the new T10.
- T10 is Claude's proposal, made for this adventurous round; AC may drop it.
- The rounds used under handoffs 01 and 04 are history and do not count.
- A round counts when its result and LOG entry are pushed (rounds.md rule).

**Stop rule (stricter than handoff 04, because audit-02 C1 found every direction stopped too early).** A direction may stop before 25 only when one of the following holds, recorded in `rounds.md` and the attempt file:
- (a) every route listed for it below has a recorded outcome: a result, a gate kill under its preregistration, or a proved obstruction covering that route's whole stated class;
- (b) a theorem closes the whole direction; or
- (c) AC says so.

"Programme exhausted", "scoped to the mechanisms tested" or "requires new premises" is **not** a stop reason while a listed route is untried. If a route is blocked (a source cannot be retrieved, or a computation is infeasible), record the measured feasibility evidence, try the listed fallback, and move to the next route.

## Part A — respond to audit 02 first (short)

Write `response-02.md` answering every finding of [audit-02](../audit-02.md). Do this before the first Part B round counts.
- **C1.** Correct the stop wording in `rounds.md`, `attempts/T7–T9.md` and `report-continuation-04.md`. These routes resume below.
- **C2.** Complete the T9 gate: search terms; IDEA-027/029/044/047/109/120/209; LIT-010/192/307/374/378/389/413; OBST-11; Subbotin's Corollary 1. Write the **T10 gate** (below) before any T10 run.
- **C3.** Disclose once the T9 gate timing and the in-place edit (`response-deviations-02.md`), with a dated history note, for AC.
- **C4.** Propose the ID kind for the refuted T7 inferences, with the mapping.
- **n1–n6.** Fix the MINOR items. Correct the attribution of the packing sketch and the fold bound to Claude's handoff 04 (n5).

## Part B — the most promising rounds, ranked

This is Claude's judgement, from audits 01–02 and the handoff-04 work. Spend the early rounds on items 1–3. Each item names its first round's deliverable and its kill rule. Every finite claim needs exact certification; every quality value is MEASURED; every degree-uniform rule is preregistered before the degrees it is tested on.

### 1. T10 — near-Padua Chebyshev-lattice cubature, then extraction to N nodes (highest expected value)

**Why.** This is the 3-D form of the mechanism that actually makes 2-D Padua work.
- **T9-03 (PROVED):** an unshifted coset's Haar rule is exact through degree D exactly when the dual lattice H^⊥ has no nonzero vector of ℓ1-norm ≤ D.
- **2-D Padua** is the cosine image of a lattice whose dual packs diamonds with no gaps. That is why it carries degree-(2n−1) cubature on exactly N nodes and has (log n)² Lebesgue growth.
- **In 3-D the octahedron does not tile space.** The cost of that is only a factor of about **19/18 in the leading node count** (PD-N T9-01, CONDITIONAL), plus lower-order terms. Compare De Marchi–Vianello–Xu's parity grids at about 1.5·N, and Cools–Poppe's blending lattices at 1.5–2.4·N (LIT-381).
- Cools–Poppe call systematic Chebyshev-lattice searches "ongoing research" (§6, LIT-381, verified fulltext).
- The T9 audit's small census (MEASURED) already found an exact unshifted degree-5 Haar rule on **exactly 20 nodes** at n = 3, of rank 17, so not unisolvent.
- **So optimal-lattice cosine cubature at about N nodes exists at small n.** The open question is how close to N it gets, and whether interpolation can be extracted from it with log-type quality.

**Gate first (C2).** Lattice rules of trigonometric degree measured in ℓ1 are an established subject: Cools–Lyness "K-optimal" 3-D lattice rules; Noskov; Lyness–Sørevik; Cools–Nuyens; Cools–Poppe 2011 Chebyshev lattices; also Betke–Henk 2000 on densest lattice packings of 3-polytopes, which recomputes the octahedron value. Register these as LIT, with coverage labels, before any run. Novelty may be claimed only for what the comparison leaves.

**Routes, in order**
- **T10.1, census of optimal dual lattices** (first round). For n = 1..16 (further if cheap), find integer lattices L ⊂ Z³ whose shortest nonzero ℓ1-norm is at least 2n, at minimal det L.
  - Use exact search, seeded from the literature's K-optimal rules and from scaled Minkowski-optimal lattices.
  - For each, record |H|, the folded node count |X| (a = 0, and the half-period shifts), the ratio |X|/N, the exactness degree and the exact Π_n rank.
  - Control: the 2-D analogue must recover Padua's counts for n ≤ 12.
  - Deliverable: a table of minimal |X|/N against n, MEASURED (exact per n).
- **T10.2, quality of the cubature-based projection.** On the best lattices, measure the hyperinterpolation / discrete least-squares operator norm on the 21³ and 41³ meshes. Expect polylogarithmic behaviour; compare with log³ n and with QR/Leja interpolation.
- **T10.3, extraction to exactly N nodes.** Remove |X| − N nodes:
  - by pivoted QR or LU on the cubature nodes, which is approximate Fekete restricted to a near-minimal cubature set;
  - by a **structured** rule (remove a sub-coset or a boundary layer, as Padua's single extra condition does), preregistered.

  Measure Λ against QR and Leja. Use T9-05 (PROVED implication) to state exactly what norm control would turn this into a proved bound.
- **T10.4, theory.** If |X|/N → 19/18 numerically, attempt a proof that optimal Chebyshev lattices give |X| ≤ (19/18 + o(1))·N. Also attempt a Λ = O(log³ n) bound for the cubature projection: the Dirichlet-kernel argument of the 2-D Padua theory, PD-T101-style.

**Kill.** For the extraction route only: QR beats every extracted set at two consecutive n ≥ 6, or minimal |X|/N stays above 1.5 for every n ≤ 16. A kill of extraction leaves T10.1/T10.2 as results.

### 2. T8 — phase-shifted cyclic orbits with M = N on the admissible degrees

**Why.**
- PD-N T8-02 kills M = N only at n = 2. The audit verified exactly that z = (1,2,7) with phases (30,75,69)/120 gives a **Π₃-unisolvent 20-node orbit** (`audit-02/code/m20_check.py`).
- A seeded floating screen finds numerically full-rank M = N orbits at n = 3, 4 and 5 (25%, 34%, 14% of random draws), and none at n = 2 or 6. This fits the half-period parity-trace condition (`theory/t8-even-parity.md`).
- When N is odd (n ≡ 0 mod 4) there is no half-period involution at all.
- With generic phases nothing folds, unisolvence is Zariski-open in the phases, and **the phases become free continuous parameters for quality**.

**Routes**
- **T8.Φ1.** Prove the exact admissible-degree set: the n for which the parity-trace balance allows full rank, for some sign pattern (−1)^z. Then certify one unisolvent orbit per admissible n ≤ 12 exactly.
- **T8.Φ2.** Optimize quality within the family under a preregistered objective: maximize log |det| in an orthonormal basis (Fekete-within-family), then measure Λ. Track whether the optimized (z, φ) follows a pattern in n, and preregister any degree-uniform rule before testing it at larger n.
- **T8.Φ3.** M = N + small and M = 2N − 1 with phases, under the same pattern.
- Then resume the **special-phase strata** (now resumable through T7-03) and **coset unions** (T8 variant 4, never attempted).

**Kill** (per preregistered rule): the D2 rule against Leja/QR. Optimized-phase sets that still lose to Leja at two consecutive admissible n ≥ 6 kill the family.

### 3. T7 — cosets: finish the census, measure the survivor, optimize phases

**Routes**
- **T7.C, the n = 2/3 all-coset census** through T7-03's symbolic minors. This is finite by |H| ≤ 8N. If it is infeasible, record measured cost and then complete n = 2 exactly and run an exact random-phase sample at n = 3.
- **T7.Q, quality.** Measure Λ for T7-06, which was never measured, and for every census survivor.
- **T7.Φ, phase optimization.** For rank-2/rank-3 H with |H| = N (no folding at generic phase), optimize the phase a ∈ T³ for det/Λ, at n = 3..6. Look for a degree-uniform pattern H_n.
- **T7.U, unions** of 2–4 cosets sized exactly N: the 3-D analogue of 2-D Padua as a union of two tensor grids. Read IDEA-182/PD-N034 first; it is the warning.

### 4. T9 — make the packing obstruction unconditional, and class-specific lower bounds

- **T9.P.** Verify the 18/19 lattice packing density of the octahedron from a retrievable source (Minkowski 1904; Betke–Henk 2000). If it cannot be fetched, request the PDF via AC's papers folder and record that as pending.
  - Then upgrade PD-N T9-01, extend it to phases (cancellation) and to non-Haar positive weights if possible.
  - Use T10.1's minimal-det data for the finite complement n < 110.
- **T9.B.** Class-specific lower bounds:
  - every Padua-stack ordering, through the T4 permutation-mean comparison (alternating ≈ 0.089 per degree, MEASURED);
  - cosine-coset families through their shortest dual vector. That would explain why the T2/T8 survivors are poor.
- **T9.M.** Certified or refined maxima to n ≈ 16 for QR, locally optimized Fekete, and the best T8/T10 sets, with preregistered fits. This is the benchmark the constructive routes must beat.
- **T9.U.** Verify the Chkifa (JAT 2013, ℜ-Leja) lead as the missing T9-04 premise. That could give the **first proved polynomial Λ for an explicit minimal 3-D set** (the Leja lower set), if the source supports it.

### 5. Lower priority (only if items 1–4 are blocked)

- The T5 commuting-completion probe (n ≤ 4), still unexecuted.
- Mod-6 fibres and lattice-plus-correction, only with a stated structural reason.

## Rules carried

- D0/D1 have passed; new tools must reproduce their controls first.
  - T10: the 2-D Padua lattice.
  - T8: PD-N T8-02 at n = 2, and the audit's M=N=20 orbit.
  - T7: the T7-06 certificate.
- **D2:** preregistration in `gates.md` plus the direction file before each family run; kill rules as written.
- **D3:** every obstruction must admit 2-D Padua and be enumerated over the full finite class where it is finite.
- **Records.**
  - Every candidate gets a provisional IDEA-template record, failed and deferred ones included, with resume conditions.
  - Use full namespaced provisional IDs.
- **Status rules.**
  - Numerical agreement earns MEASURED only.
  - A computer-assisted PROVED needs all of: a proved reduction, exact arithmetic, committed checker and evidence, and an independent rerun.
  - A literature fact is LITERATURE with coverage labels.
- **No novelty or priority claim** without the gate plus a source comparison.
- Receipts stay under 16 KiB with committed code. Raw catalogues are regenerate-only with recorded identities. Do not hard-code shared `/tmp` paths (audit-02 NOTE).
- Checkpoint and push at each round boundary with a LOG entry. Give AC a progress update about every five minutes of sustained work.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the head.
- [audit-02.md](../audit-02.md) and its appendices, especially [T8](../audit-02/T8.md) (M = N lead) and [T9](../audit-02/T9.md) (Haar census note).
- The LOG; handoffs 04 and 05; `report-continuation-04.md`.
- T7/T8/T9 theory and attempts; literature-T1/T7/T9; LIT-381 and the Cools–Poppe record; the full `state/IDEAS.md` for the T10 gate.

## Scope limits

- Do not reopen accepted theorems, killed families (the T4 stacks at n7, the T8 E rule) or the H39 cover.
- Do not edit audit reports or earlier handoff bodies.
- No final IDs, reservations or shared-registry edits.
- Do not touch other topics, main, tags, `.github/` or settings. Only AC merges.

## Acceptance and outputs

- `response-02.md` and its fixes.
- Per direction:
  - `attempts/T7.md`–`T10.md` updated or created;
  - gates, preregistrations, literature records and theory files with explicit statuses;
  - code and receipts.
- `rounds.md` with the new counters and a valid stop reason (or the ceiling) for each direction.
- An updated report, LOG, results file and PR body.

When done:
- Commit the outputs.
- In a following commit, close this handoff `done in <sha>` and open handoff 07 for a Claude audit: a focused re-audit of the Part A material changes plus a substantive audit of the new work, Opus 5.5 xhigh.
- Push before replying, and end with the short continuation prompt.
