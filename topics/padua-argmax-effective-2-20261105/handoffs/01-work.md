# Handoff 01 — padua-argmax-effective-2-20261105 — effective all-degree Padua argmax, phase 2

- Status: done in 352daad8c164617331c34ae81a7ce7331f501bb9
- Previous handoff: none (new topic; phase 1 is `topics/padua-argmax-effective-20261103/`, merged as PR #19)

- Next agent / model / effort: Codex. Use **gpt-6-astra at ultra** for the orchestrator and all mathematics. This continues AC's instruction for this problem (2026-11-03: "This looks like a topic that warrants astra with ultra reasoning"), which overrides the WORKFLOW allocation table for this campaign; record that justification in LOG. Use gpt-6.1-sol medium for code, ports, timing and replays, and a separate gpt-6-astra high instance for supplementary independent checks.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-effective-2-20261105
- Input head SHA: `5db1e01` (main, PR #19 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `5db1e01`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05

## Where phase 1 left the problem

**Target PD-T099 (OPEN).** For every n ≥ 2, max_{[−1,1]²} λ_n = Λ_c(n), attained exactly at the two parity-correct non-node corners. Conventions are those of PD-T101 and phase 1's BRIEF.md §1–2.

**Proved on main:**
- **Finite range 2 ≤ n ≤ 32** (PD-T209, T162/166/169/174/177, T181, T214, and PD-T246 for 17–32), all via the certificate theorem PD-T210.
  - The native C/GMP producer and C++/GMP checker are in `topics/padua-argmax-effective-20261103/code/native_*`. They use 192-bit fixed scale, are inherited n ≤ 100 capped, and canonicalize every rational after the late fix.
  - Degree 40 has 352 producer leaves, but its checker hit the 600 CPU-second cap without acceptance. Degrees 33–39 were never run.
  - Measured cumulative cost exponent ≈ 5.6. The projections are n ≈ 61 in 24 h and n ≈ 82 in 7 days of single-core CPU. These are MEASURED extrapolations.
- **Eventual theorem PD-T229**, with N_* non-effective. Its chain:
  1. PD-T216 (global phase bound): S_n ≤ aΛ_c + C log(n+1) on the phase diamond, with C absolute but not explicit.
  2. PD-T217 (local gain): S_n ≤ aΛ_c + Cρ² log(n+1) + Cρ for ρ ≤ ρ₀.
  3. PD-T224 (noncorner coset defect): Δ ≥ 1/4096 for n ≥ 48 and ρ ≤ 1/64. This one is explicit.
  4. PD-T225 (localization).
  5. PD-T228 (local corner comparison): explicit, but it needs log n ≥ 10⁷.
- **All-degree corner slopes PD-T250/251**: A_n, B_n ≤ −n²Λ_c/8, and strict descent for 0 < h_x + h_y ≤ 1/(2[n(n+1)]³), a physical radius of order n⁻⁶.
- **Negatives PD-N084–086:**
  - PD-N084: complete coefficient positivity fails.
  - PD-N085: fixed κ/n² affine sign boxes eventually fail.
  - PD-N086: individual fixed-sign cardinal factorization fails at n = 4.
- **Measured (PD-T247/248/252):**
  - local K ≈ 0.29 → 0.22 for n = 17 → 1000;
  - global C ≈ 1.59 → 1.45 for n = 17 → 200;
  - far-coset margins 0.15–0.34;
  - no edge-cell reversal in 1536 comparisons;
  - and, from PD-T206, the majorant excess max S − Λ_c ≈ 9e-5 at n = 40, at scaled phase ρ ≈ 0.06 from a coset.

**Why making the existing chain effective cannot close the bridge.** This is a diagnosis by Claude, to be verified as gate A0 below.
- PD-T225 localizes by (1−a)Λ_c ≤ C log(n+1) with 1 − a ≥ ρ²/(2π²).
- To force ρ ≤ 1/64 one needs ρ²Λ_c/(2π²) > C log(n+1). With Λ_c ≈ (4/π²)log²n + 1.2255 log n + 1.846 and even the *measured* C ≈ 1.45–1.6, this requires **log n ≳ 3×10⁵**.
- So no constant-sharpening of PD-T216/217/224/225 yields an n₀ within reach of any finite certification. Phase 1's G5 was "not evaluable" for this reason.
- Phase 2 must therefore change the **architecture**, not the constants.

## Main idea for phase 2: a hybrid of a cheap per-degree certifier and sharp asymptotics

These are proposals. Each passes the novelty gate before work; the nearest entries are IDEA-305, 316, 320, 326–330 and 336–348.

### H1 — phase-diamond certifier

The phase-1 records reduce the global problem to a fixed phase diamond: the odd-coset cover and same-primitive argument in gated-codex-04/09 (PD-T218/223) and the phase form in PD-T216. Every physical point has a representation (J, K, α, β) with |α| + |β| ≤ π, and λ_n = S_n(α, β) − Δ_n^{(J,K)}(α, β). Here S_n is the shifted-lattice primitive, which does not depend on the coset, and Δ ≥ 0 is the defect, which does.

Verify this structure exactly, including the endpoint-weighted reflections at the physical boundary. Then certify PD-T099 at each degree by covering the **fixed** phase diamond with boxes, in three regions:

- **far region:** S_n < Λ_c on the box, with no defect needed;
- **near-coset region, noncorner cosets:** S_n − Λ_c < (lower bound on Δ over the coset class). Use PD-T224's 1/4096, or a sharper class-wise bound proved for larger ρ, because the S-excess peak sits near ρ ≈ 0.06, outside ρ ≤ 1/64;
- **corner cosets:** strict descent from the corner. Use PD-T251's slopes with an exactly computed per-degree second-order bound on a box of fixed *scaled* size, so the descent radius is of order n⁻² physical. Then use ordinary box bounds outside that box.

The point is cost. S_n at a phase point is a sum over 2N = 2n(n+1) terms of a kernel G_n = D_n − cos(nu) with a closed trigonometric form. Each box needs O(n²) operations for value and derivative enclosures. The box count over a fixed diamond should be nearly independent of n, because S_n/Λ_c approaches a limit profile. So the per-degree cost is about n² × boxes, against today's ≈ n^5.6. If that holds, degrees in the hundreds or thousands become certifiable in the sandbox.

Requirements:
- a written proved reduction from PD-T099 at degree n to the box predicates;
- exact or outward-rounded arithmetic, using FLINT/Arb ball arithmetic in C, or GMP/MPFR with outward rounding;
- a separate independent checker on its own arithmetic path, never sharing the producer's kernel;
- cross-validation against PD-T246 and PD-T214 on n = 9–32, including corruption controls.

### H2 — sharp, explicit asymptotics for n ≥ N₁

Prove, for all n ≥ N₁ with **explicit** N₁ and remainders:
- a uniform expansion of S_n(α, β) on the diamond against an explicit limit profile, with remainder sup|S_n − profile_n| ≤ r(n);
- class-wise defect lower bounds that are uniform in n;
- a corner comparison on a fixed scaled box.

The far-region inequality needs r(n) well below the measured margins (0.15–0.34). PD-T159's |error| ≤ 54 is about 300 times too crude, so this means explicit Euler–Maclaurin or Poisson-summation remainders with honest constants, not O(1) existence.

If N₁ ≤ the degree H1 can reach, then PD-T099 is PROVED for all n.

### H3 — the corner zone at scale n⁻²

H3 can serve H1, H2 or both. Close the gap between PD-T251's n⁻⁶ radius and the n⁻² scale. Two routes:
- an aggregate sign-change or remainder estimate, such as the weighted-energy premise of PD-T227/IDEA-330;
- per-degree exact Hessian or Bernstein bounds on a fixed scaled corner box, which is H1's corner predicate.

PD-N085 rules out fixed κ/n² *affine* sign boxes; aggregate control is not excluded.

### Retained alternatives

- **R3** (all-degree E-C comparison, PD-T248/249) remains a way to cover degrees without enumerating them.
- **R4/R5** remain deferred unless a concrete new structure appears.

## Tasks, in order

0. **Setup and replay.**
   - Read the rules at the branch head and record the SHA. Fetch main and record any movement.
   - In a fresh subagent, replay the native producer and checker at n = 17 and n = 24 from `topics/padua-argmax-effective-20261103/code/native_*`, and compare with the committed receipts.
1. **Gates A0–A5** (below). Record each verdict in `gates.md` before moving on.
2. **H1 build and validation**, if A1 passes.
   - Write the reduction theory file first.
   - Then write the producer, the independent checker and the controls, and validate on n = 9–32.
   - Then extend the certified range degree by degree, reporting box counts, times and memory.
3. **H2 analysis in parallel**, with separate subagents and disjoint files: the explicit profile, the remainder, the class-wise defects and the corner box. Each lemma gets its own theory file, with explicit constants.
4. **H3**, as needed by H1's corner predicate or H2's corner comparison.
5. **Optionally, finish degree 40** with the existing native checker, outside any cap, as a cross-check on H1. This is not required.
6. **Assembly.**
   - If the certified range reaches N₁, write the all-degree theorem, its dependency list and the finite certificate inventory.
   - Otherwise report the certified range, the best proved N₁ and the exact remaining gap.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **A0, diagnosis check.** Recompute independently the localization threshold implied by PD-T216 + PD-T225 with C ∈ [1.4, 1.7] and ρ = 1/64, and also for ρ = 1/16. Confirm or refute "log n ≳ 3×10⁵". If it is refuted, record the correct value; if that value is ≤ 10⁴, R1 (effective constants in the existing chain) is reopened as a main line.
- **A1, H1 structure and cost probe** (float, MEASURED).
  - Check the coset-independence of S_n and the reflection rules at the physical boundary, exactly at n = 3–6 against direct evaluation.
  - Then measure the box count a float version of the three-region cover needs at n = 17, 32, 64, 128, 256, at the same safety margins the exact version would use.
  - **Pass:** the box count grows at most like log² n, and the projected exact per-degree time at n = 256 is ≤ 10 min in the sandbox.
  - **Kill (H1 as designed):** the box count grows at least like n, or the corner region needs boxes shrinking faster than n⁻² physical. Then record the profile, and redesign the corner predicate once (via H3) before abandoning H1.
- **A2, defect classes.** Float-measure min Δ over each noncorner coset class (edge distance k = 1, 2, 3, …, interior) for ρ ≤ 0.1, 0.2, 0.3 at n = 48, 96, 192. Pre-register the ρ₁ at which a provable class-wise lower bound must hold for H1 and H2 to fit the measured S-excess.
  - **Kill (near-coset plan):** for some class, min Δ is below the max S-excess on the same ρ-ring at two consecutive measured n. Then that class needs a different predicate (corner-like descent), recorded with the class.
- **A3, profile and remainder scaling** (MEASURED). Fit sup over the diamond of |S_n − profile_n| for n up to 2000 against r(n) ∝ log n/n, 1/n and log² n/n. The profile is the candidate H2 limit, defined before the fit.
  - **Pass:** the best-fit law gives r(n) < 0.05 at some n ≤ 2000.
  - **Kill (H2 with that profile):** no law reaches 0.05 before n = 10⁵. Then redefine the profile once, including the next correction term, and stop H2 if that also fails.
- **A4, bridge arithmetic.** From A1/A3, project N₁ (H2) against the H1-certifiable degree within 24 h and within 7 days of sandbox CPU.
  - If N₁ is within 2× of the 7-day H1 range, the main line is H1 + H2.
  - If it is beyond 10×, record the gap and pivot effort to H2 sharpening or R3.
  - This replaces phase 1's unevaluable G5 by a computable test.
- **A5, counterexample screen.** H1's float cover at every n up to the A1 range doubles as a counterexample search. Any box where the far-region or defect predicate fails by more than its error bound is re-examined exactly. A confirmed non-corner point with λ_n ≥ Λ_c is a scoped PD-N disproving PD-T099 at that n.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- Phase 1 (`topics/padua-argmax-effective-20261103/`):
  - BRIEF.md (knowledge base: §1–2 conventions, routes and pilot numbers);
  - report.md, audit-01.md, response-01.md, LOG.md;
  - attempts/*.md, ideas/*.md, theory/*.md;
  - code/native_producer, code/native_checker, code/gates, code/r6;
  - checker-provenance-01.md, independent-checks-canonical.md, literature-g8.md.
- `topics/padua-argmax-alln-20261101/`:
  - theory gated-codex-01–17 (PD-T215–231), above all 01, 02, 03, 04, 09, 10, 11, 13 and 14;
  - argmax-alln-codex-03/08 (PD-T210/214);
  - PD-T206/207;
  - report.md.
- `topics/padua-proof-attempts-2-20261101/` theory 01–04 (PD-T156–159) and 70–77 (PD-T185–192).
- PROOF_STATUS rows PD-T099, T101, T156–T159, T185–T192, T206–T231, T246–T252 and PD-N079–N086. IDEAS entries IDEA-206, 290–305, 316–355 and the argmax rows of the Obstruction table.
- literature/INDEX.md before any attribution. Phase 1's G8 access gaps are in literature-g8.md. The Lebesgue-function literature pass on PR #21's branch (unmerged) can be read with `git show origin/claude/padua-literature-20261103:<path>`.

## Scope limits

- Write only inside `topics/padua-argmax-effective-2-20261105/` and `results/padua-argmax-effective-2-20261105.md`.
  - Do not edit merged topic, theory, code or registry files. Import or copy frozen code instead.
  - Put proposed shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to any other open branch: PRs #20–#24 at writing, and any later ones.
- Novelty gate (relaxed scan, WORKFLOW) before H1, H2, H3 and any new mechanism. Record the closest entries, the applicable obstructions (PD-N079–086 above all) and which hypotheses each idea breaks, the verdict and the cheapest test.
- Provisional IDs: `PD-T?argmax-effective-2-codex-NN`, and likewise for PD-N, IDEA and LIT. When the draft PR opens, reserve final ranges by the fresh-range procedure, with headroom: main, every open PR (#20–#24 at writing), retired reservations (including phase 1's unused PD-T253–265, PD-N087–091, IDEA349–355, LIT471–473) and the batch ledger.
- Statuses follow AGENTS.md:
  - Float covers, fits and projections are MEASURED.
  - A finite PROVED degree needs the written reduction, exact or outward arithmetic, committed producer and checker code, a small essential receipt (or a cold-storage manifest with the checker result), and acceptance by the independent checker run by a different subagent.
  - An all-degree claim needs the explicit N₁ and certified coverage of every n < N₁.
  - Never infer a constant from a fit.
- Storage (WORKFLOW, PR #18): commit code and small evidence (normally under 16 KiB per file). Certificates, box trees and sweeps go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`, under `Downloads\padua\cold_storage\padua-argmax-effective-2-20261105\`. Hand them to AC.
- **Compute.**
  - Large-n certification uses compiled code (C with FLINT/Arb, or GMP/MPFR). Python is acceptable for prototypes and for n ≤ about 32.
  - In the sandbox, a single run may use up to 6 h wall and a campaign up to about 48 h of cumulative CPU. AC may change these numbers.
  - Do not use AC's NTNU servers (syvert0/1/2) or any other machine without asking AC in the chat first. If more compute is needed, stop at a recorded checkpoint and ask, giving the exact commands, the projected times and the expected certified range.
- **Literature.**
  - You may open any public page holding relevant literature. Cite a source only after reading its fulltext, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `LOG.md` with an entry per gate and step boundary.
- `plan.md`, written before the first run, with time boxes.
- `gates.md` with A0–A5 verdicts.
- `attempts/H1.md`, `attempts/H2.md`, `attempts/H3.md` and `attempts/R3.md` if R3 is used.
- `theory/` records in THEORY-template form, one per result: the reduction, each lemma, each finite range, and each PD-N.
- `independent-checks*.md`, `evidence-manifest.json`, `results/padua-argmax-effective-2-20261105.md` (kept current) and `report.md` at the end.
- Push at every gate and step boundary, and at least every ~10 minutes while something has changed.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- The report contains:
  - A0–A5 verdicts;
  - the H1 certified range, with per-degree cost, box counts and the independent acceptance record;
  - H2's proved N₁ and remainders, with their dependencies;
  - H3's status;
  - whether PD-T099 is now PROVED, PARTIAL (with the exact remaining interval of degrees) or refuted at some n;
  - a short "for the paper" paragraph on the statements the Padua Lebesgue-function paper can now make.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-argmax-effective-2-20261105.`
