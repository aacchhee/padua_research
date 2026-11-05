# Handoff 01 — padua-argmax-bridge-20261105 — close the Padua argmax bridge 33 ≤ n < N_*

- Status: open
- Previous handoff: none (new topic; predecessors `topics/padua-argmax-effective-20261103/` (PR #19) and `topics/padua-argmax-effective-2-20261105/` (PR #25), both merged)

- Next agent / model / effort: Codex. Use **gpt-6-astra at ultra** for the orchestrator and all mathematics; AC asked for it on 2026-11-05 ("How about an astra ultra round on that?"), continuing his 2026-11-03 instruction for this problem. Use gpt-6.1-sol medium for code, ports and replays, and a distinct gpt-6-astra high instance for supplementary independent checks.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `9322fba` (main, PR #25 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `9322fba`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05

## The one goal

Prove **PD-T099** for every n ≥ 2: max_{[−1,1]²} λ_n = Λ_c(n), attained exactly at the two parity-correct non-node corners. Equivalently, close the bridge 33 ≤ n < N_*. Two pieces are already in place:
- the certified finite range 2–32 (PD-T209/T214/T246 and the inherited n ≤ 8 records);
- the eventual theorem PD-T229, whose N_* is not effective.

The plan is to meet in the middle:
- a finite certifier pushed upward from 33;
- an all-degree theorem for n ≥ n₁ with an **explicit** n₁ low enough to meet it.

Anything less than full closure is still worth recording precisely:
- a larger certified range;
- an explicit but large n₁;
- or a counterexample.

## What is proved and what blocks it

**Proved and reusable.** Conventions are as in PD-T101 and phase 1's BRIEF.md §1–2.

| Result | Record | Strength |
|---|---|---|
| Corner value Λ_c(n), exact | PD-T101 | Λ_c = (4/π²)log²N + b log N + c + R_n with N = n+½, explicit R_n → 0 (PD-T269–271) |
| Phase structure λ = S − Δ | PD-T364 | Full reflection defect and a sufficient Far/Defect/Corner finite-cover reduction |
| Boundary of the phase diamond | PD-T365 | Exact cotangent formula; profile error ≤ 7/(12[n(n+1)]²); S_n = L_{n(n+1)} at midpoints |
| Noncorner defect | PD-T366 | Δ ≥ 1/8192 for n ≥ 48 and ρ ≤ 1/10 |
| Corner descent | PD-T369, PD-T251 | Strict descent for H ≤ max(1/(2[n(n+1)]³), 10⁻¹¹/n²); slopes ≤ −n²Λ_c/8 |
| Global bound | PD-T368 | Λ_n ≤ 110[1+log(n+1)]² |
| Eventual argmax | PD-T229 | All n ≥ N_*, N_* not effective |
| Rejected: leading-only profile | PD-N132 | No profile a·b_n works, since S_n ~ (4/π)log n at the midpoints |
| Rejected earlier | PD-N079–086 | Includes PD-N085 (fixed κ/n² affine sign boxes) |

**Why the existing chain cannot be made effective.** Gate A0 of PR #25 confirmed it. Localizing via (1−a)Λ_c ≤ C log(n+1) needs log n ≈ 3×10⁵ for ρ ≤ 1/64, and even ρ ≤ 1/10 needs log n in the thousands. The log² deficit competes against an O(log n) term with a fixed constant.

**Consequence: two sharper tools are needed.**
1. The **phase-dependent log n coefficient** must be captured exactly, so that the analytic side compares like with like. That is the profile S_n ≈ (4/π²)a(α,β)log²N + B(α,β)log N + C(α,β), with explicit uniform remainders.
2. The finite side must cover the fixed diamond cheaply.
   - **Evidence that this is feasible:** the PR #25 pilot's unresolved frontier stayed flat in n, at about 800 boxes for n = 17, 32, 64 and 128 after 2000 visits.
   - **Why it did not finish:** the pilot used naive double-precision intervals, which suffer badly from dependency over-estimation, and was capped at 2000 boxes or 60 CPU-s per degree.

**Measured context**, MEASURED and steering only:
- far-coset margins 0.15–0.34;
- local corner K ≈ 0.29 → 0.22;
- global C ≈ 1.59 → 1.45;
- S-excess near cosets about 8×10⁻⁵ at n ≈ 48, roughly 65 % of 1/8192 (PR #25 audit E8);
- the pilot's pending box widths, 0.05–0.2 in phase.

## Routes, including methods from neighbouring fields (AC, 2026-11-05: "Maybe some neighboring field methods?")

Each route passes the novelty gate before work. A relaxed scan by Claude on 2026-11-05 found no `state/IDEAS.md` entry for:
- hypergroup or positive product formulas;
- Abel–Plana or explicit Euler–Maclaurin;
- polygonal Lebesgue constants;
- Taylor models or Bernstein branch-and-bound;
- sum-of-squares certificates;
- ℓ¹-contraction or transference.

Brutman-type ordering exists as IDEA-318, with a recorded kill. The nearest phase entries are IDEA-454–461, 336–348 and 305. Verify these before work. Read literature fulltexts before citing them, and give AC clickable DOI or journal links for anything paywalled.

### N1 — a computer-assisted proof uniform in the degree (main analytic line)

The sources are analytic number theory (explicit estimates), validated numerics, and rigorous asymptotics in dynamics.

- Treat the family n ≥ n₁ as one compact parameter problem rather than infinitely many degrees.
- Using explicit summation formulas with **integral remainders**, write S_n and the corner-coset λ as
  - an explicit model M(α, β, L) in the phase and L = log N, plus
  - a remainder bounded rigorously by r(n) for every n ≥ n₁.
- The summation formulas are Euler–Maclaurin with exactly bounded remainder and the Abel–Plana formula. The boundary result PD-T365 and PD-T270's 1/(4n²) bound show that sums of the shifted-cotangent type admit this.
- Then certify the model inequality by interval branch-and-bound over (α, β) ∈ diamond × t ∈ [0, 1/log n₁], with t = 1/L.
- The end t → 0 is the leading-order problem. It is already understood (PD-T229's structure) and needs only an explicit local version.
- The output is a finite computation that proves PD-T099 for **all** n ≥ n₁ at once.

### N2 — polygonal Lebesgue-constant technique, to supply the profile

- **Sources:** Lebesgue constants of Fourier sums over polygons and polyhedra. Named works:
  - Podkorytov's polyhedral asymptotics;
  - Kuznetsova 1995, LIT on main via PR #21;
  - Liflyand's survey "Lebesgue constants of multiple Fourier series";
  - Dencker–Erb–Kolomoitsev–Lomako 2017 on polyhedral Lebesgue constants and Lissajous–Chebyshev nodes;
  - Kolomoitsev–Lomako 2021, whose Padua sentence gives the leading term.
- **Mechanism:** these decompose the rhombic or polygonal kernel along the polygon's edge directions into 1-D Dirichlet factors. Each edge then contributes a 1-D log term with a phase-dependent coefficient.
- **Goal:** get B(α, β) and C(α, β), the interior profile that IDEA-459 (H2 corrected interior profile) left deferred, in closed form with explicit error.

### N3 — a practical certifier from validated global optimization (finite side)

- Replace naive intervals by **mean-value or first-order Taylor-model enclosures**. These need an interval gradient per box, computable in O(n²) like the value; see Berz–Makino Taylor models and the Hansen/Kearfott interval global-optimization literature.
- Add **Bernstein-basis subdivision** (Garloff-type) where λ is polynomial on a sign-fixed region.
- Near each corner, use **dyadic shells**. The margin there grows linearly in H, so derivative enclosures need only a logarithmic number of shells. Start from a per-degree exact sign radius at the corner: compute exactly the smallest H at which some L_B(c + h) changes sign, which beats the universal 10⁻¹¹/n².
- Reduce by symmetry, but only by symmetries proved in a written lemma.
- Use outward-rounded arithmetic (Arb/FLINT or MPFR) and an independent checker on its own arithmetic path, validated against PD-T246 on n = 17–32 with corruption controls.
- Push the certified range up from 33.

### N4 — positive translation (hypergroup) structure (structural, high risk)

- **Sources:** harmonic analysis on orthogonal polynomials. In one variable, Lebesgue constants of Jacobi or ultraspherical expansions peak at x = 1 because a positive product formula (Askey, Gasper) gives a generalized translation that contracts in ℓ¹. In two variables, see Koornwinder–Schwartz's product formulas on the simplex and the parabolic biangle, and related work on generalized Chebyshev polynomials.
- **Question:** is there, for each x, a nonnegative matrix M(x) on the node indices with column sums ≤ 1 and L(x) = M(x) L(c)? The sign vector at the corner is fixed by L(c). If so, λ(x) = ‖L(x)‖₁ ≤ ‖L(c)‖₁ = Λ_c for every n at once.
- **Warning:** PD-T206 shows that the four-copy average S itself exceeds Λ_c near cosets. So plain averaging is already refuted, and M must be a genuinely different operator.
- **Cheap test:** at n = 3–8 and a grid of x, solve the LP feasibility problem for M(x), both unrestricted and in a structured class (reflection- or translation-generated). Then use exact rational LP to certify feasibility or infeasibility at the critical x.

### N5 / N6 — 1-D classical methods and the Lissajous curve (exploratory)

- **N5 sources:** Ehlich–Zeller 1966, Brutman 1978 and Günttner 1980, already in the PR #21 records, prove 1-D endpoint maxima by explicit cotangent-sum analysis and ordering of local maxima.
- **N6 source:** Padua points are a Lissajous or rank-1 lattice node set (the generating-curve viewpoint of Bos–De Marchi–Vianello–Xu; Dencker–Erb).
- **Question:** does restricting to the generating curve or its parallels yield a 1-D trigonometric representation of λ_n, to which the 1-D tools apply?
- IDEA-318's kill applies to orderings of whole cells; only a new, precise formulation qualifies.

### Retained

R3, the all-degree E-C comparison (PD-T248/249/231), stays available for covering blocks of degrees without enumerating them.

## Tasks, in order

0. **Setup and replay.**
   - Read the rules at the branch head and record the SHA.
   - In a fresh subagent, replay the native producer and checker at n = 24 and the PR #25 pilot at n = 32, against the committed receipts.
1. **Gates B0–B6** (below). Write `plan.md` with time boxes before the first run.
2. **N3 and N1/N2 in parallel**, in separate subagents with disjoint files. Run N4 and N5/N6 as bounded side probes; stop each at its box.
3. **Meet-in-the-middle arithmetic** (B4), as soon as both sides have numbers.
4. **Assembly.**
   - If the certified range reaches n₁, write the all-degree theorem PD-T099 with its full dependency list, and the finite certificate inventory.
   - Otherwise record the certified range, the best proved n₁ and the exact remaining interval of degrees.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **B0, replay.** Any unexplained mismatch stops the campaign until it is explained.
- **B1, margin anatomy** (float, MEASURED).
  - For n ∈ {33, 48, 64, 96, 128, 192, 256}, map the true margins:
    - Λ_c − max λ on the far region;
    - (1/8192 or the sharper class defect) − (S − Λ_c) on near-noncorner rings ρ ≤ 1/10;
    - Λ_c − λ on dyadic corner shells.
  - This fixes the accuracy N1/N2 must reach and the enclosure tightness N3 needs. No pass or kill; it is required input for B3 and B4.
- **B2, N3 throughput** (float first, then outward).
  - **Pass:** a complete float cover at n = 64 within 10 CPU-min, and box counts at n = 33, 64, 128 growing at most like log² n.
  - **Kill (N3 design):** box count growing ≥ n at fixed enclosure order, or corner shells needing boxes smaller than the per-degree exact sign radius. Then raise the enclosure order once (second-order Taylor model), and record before abandoning.
- **B3, N1/N2 model.**
  - Define M(α, β, L) and the remainder bound r(n) in a theory file **before** any fit.
  - Then compare r(n) with half of B1's margins and project n₁.
  - **Kill (that model):** r(n) ≥ half the margin for every n ≤ 10⁶. Then add the next correction term once, and stop N1 with that model if it still fails.
- **B4, meet in the middle.**
  - If the projected n₁ is within the range N3 can certify in about 48 h of sandbox CPU, proceed.
  - If it is within a range that needs more compute, **stop at a checkpoint and ask AC** about NTNU (syvert0/1/2), with exact commands and projected times.
  - If it is beyond any plausible compute, record the gap and put effort into sharpening r(n).
- **B5, N4 LP test.** Exact rational LP at n = 3–8.
  - **Pass:** a structured class of M(x) is feasible at all critical x for every tested n.
  - **Kill:** infeasibility at a certified x for some n, for the unrestricted class. That kills N4 entirely and is recorded as a scoped PD-N.
- **B6, counterexample.** Any box where a predicate fails beyond its error bound is re-examined exactly. A confirmed non-corner point with λ_n ≥ Λ_c is a scoped PD-N disproving PD-T099 at that n.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `topics/padua-argmax-effective-2-20261105/`:
  - report.md, audit-01.md, response-01.md, preparation-audit-01.md;
  - attempts/H1–H3.md, ideas/, theory/ (PD-T364–370, PD-N132);
  - box-pilot.md, phase-probe.md, projection-probe.md, gates*.md;
  - code/.
- `topics/padua-argmax-effective-20261103/`:
  - BRIEF.md, report.md, attempts/, theory/ (PD-T246–252);
  - code/native_*.
- `topics/padua-argmax-alln-20261101/` theory gated-codex-01–17 (PD-T215–231) and argmax-alln-codex-03/08.
- `topics/padua-lebesgue-followups-20261103/` theory (PD-T266–271).
- PROOF_STATUS rows PD-T099, T101, T156–T159, T185–T192, T206–T231, T246–T252, T266–T271, T364–T370 and PD-N079–N086, N132.
- IDEAS entries IDEA-206, 290–305, 316–348, 358 and 454–461, and the argmax rows of the Obstruction table.
- `literature/INDEX.md`, before any attribution. PR #21 (in preparation) holds the Ehlich–Zeller, Brutman, Günttner, Kuznetsova, Kolomoitsev–Lomako and CDMSV records. Read them with `git show origin/claude/padua-literature-20261103:<path>` until it merges.

## Scope limits

- **Where to write.** Only inside `topics/padua-argmax-bridge-20261105/` and `results/padua-argmax-bridge-20261105.md`.
  - Do not edit merged topic, theory, code or registry files. Import or copy frozen code instead.
  - Put shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to any other open branch: PR #21, PR #24 and any later ones.
- **Provisional IDs:** `PD-T?argmax-bridge-codex-NN`, and likewise for PD-N, IDEA and LIT. When the draft PR opens, reserve final ranges by the fresh-range procedure (main, every open PR, retired reservations, the batch ledger), with headroom.
- **Statuses follow AGENTS.md.**
  - Float covers, fits and projections are MEASURED.
  - A computer-assisted PROVED claim, finite or uniform in n, needs:
    - a written proved reduction;
    - outward-rounded or exact arithmetic;
    - committed producer and checker code;
    - small evidence or a cold-storage manifest with the checker result;
    - acceptance by an independent checker on its own arithmetic path, run by a different subagent.
  - For N1, the remainder bound r(n) must be **proved**, not fitted.
  - Never infer a constant from a fit.
- **Storage** (WORKFLOW, PR #18): commit code and small evidence, normally under 16 KiB per file. Certificates, box trees and sweeps go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`, under `Downloads\padua\cold_storage\padua-argmax-bridge-20261105\`.
- **Compute.**
  - Sandbox only: up to 6 h wall per run and about 48 h of cumulative CPU. Claude proposes these limits; AC may change them.
  - Large runs use compiled code (C with Arb/FLINT, or MPFR). Python is for prototypes only.
  - Do not use AC's NTNU servers or any other machine without asking AC in the chat first (gate B4).
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, with an entry per gate and step boundary.
  - `plan.md` and `gates.md`, with B0–B6 verdicts.
  - `attempts/N1…N6.md`, plus `novelty-gate-*.md`.
  - `theory/` records in THEORY-template form, one per result: the model and remainder, each lemma, each finite range, the uniform-in-n certificate, each PD-N.
  - `independent-checks*.md`, `evidence-manifest.json` and `literature-neighbouring.md` (sources read, LIT entries, access gaps with links).
  - `results/padua-argmax-bridge-20261105.md`, kept current, and `report.md` at the end.
- **Pushes and PR.** Push at every gate and step boundary, and at least every ~10 minutes while something has changed. Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- **The report contains:**
  - B0–B6 verdicts;
  - the certified range, with per-degree cost and independent acceptance;
  - the proved n₁ with r(n) and its dependencies;
  - the status of N4–N6;
  - whether PD-T099 is now PROVED for all n, PARTIAL with the exact open interval of degrees, or refuted at some n;
  - a short "for the paper" paragraph.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-argmax-bridge-20261105.`
