# Handoff 01 — padua-lanczos-nonproduct-20261105 — span drift on genuinely non-product families

- Status: done in 38237fecb45f672f20a25d9989a90c31f3ff02a6
- Previous handoff: none (new topic; predecessors `topics/padua-lanczos-drift-20261101/` (PR #15) and `topics/padua-lanczos-frontier-20261105/` (PR #24), both merged)

- Next agent / model / effort: Codex. This follows the allocation AC set on 2026-11-05 ("Run the coordinator on Astra High, easier jobs on Sol and raise to Astra Ultra only when things get serious"):
  - coordinator: gpt-6-astra high;
  - code, exact scans, replays and bookkeeping: gpt-6.1-sol medium;
  - routine mathematics: gpt-6.1-sol xhigh;
  - gpt-6-astra ultra only for a decisive hard step (an all-degree lower or upper bound on a non-product family, or a stability-radius theorem), with a one-line justification in LOG;
  - supplementary independent checks: a distinct gpt-6-astra high instance.
- Role: orchestrator and developer
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `be9a831` (main, PR #29 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `be9a831`. The rules changed in PR #29 ("Proportionate audit and records"); read the new WORKFLOW sections.
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05. AC: "Yes make a handoff for nonproduct".

## Why this topic

PR #24 proved the first all-degree drift separation, PD-T324: on SH_n, the BJ span capacity is at least √(2(4^(n+1)−1)/3), while the mirror capacity is at most 2√6 (n+1)²(N_n−1). The closure-growth theorems PD-T328/329 (≥ 2^(n−4) worst case, ≥ 2^(n−8) mean square) are on the same family.

**The limitation.** SH_n is "physically non-product" but is an **affine image of a product measure**. Its nodes are (s_k, 2s_k + s_l) with Chebyshev-U Gauss nodes s and product weights v_k v_l. The proof runs on the latent product coordinates and the U-recurrence. So the theorem shows that the *ordering rule* can cost exponentially once the coordinates are sheared. It does not yet show that drift is a property of *geometry*.

The two frozen grids of PR #15/24 are in the same position:
- rotQ24 is a rotated product grid, again affine-product;
- T24 is a triangle lattice, which is genuinely non-product. Its exact growth fit came out INCONCLUSIVE (PD-T338).

**Goal.** Prove an all-degree drift separation on at least one family that is **not an affine image of a product measure**, in the PD-T324 aggregate model or a stated variant. Otherwise prove why such separation fails or changes character there.

Definition to fix first, in a theory file: a discrete or continuous measure is **affine-product** if some affine change of coordinates makes it a product measure. **Genuinely non-product** means not affine-product. Prove non-product status for every family used.

## Directions (run all in parallel; be adventurous)

Each direction passes the novelty gate before work, under the rules at the branch head. Nearest entries: IDEA-246–267, IDEA-414–424 (PR #24) and the entries behind PD-N062/063 and PD-N116–118.

### P1 — the triangle, with explicit orthogonal polynomials (main line)

The triangle is the natural genuinely non-product domain with fully explicit bivariate OPs and three-term relations. There are two settings:

- **Continuous:** Jacobi polynomials on the simplex (Proriol–Koornwinder–Dubiner) for the weight x^α y^β (1−x−y)^γ, with explicit matrix three-term coefficients (Dunkl–Xu, *Orthogonal Polynomials of Several Variables*; read the fulltext before citing).
- **Discrete:** bivariate Hahn and Krawtchouk polynomials on the lattice triangle {i + j ≤ N}. Sources: Tratnik; Xu's discrete OPs on the triangle; Griffiths' multivariate Krawtchouk. Uniform weights give the frozen T24-type grid in the limit case α = β = γ = 0. Locate the exact sources and read them.

Steps:
1. Restate the PD-T136/137 aggregate span capacity for a continuous measure, or use exact Gauss-type cubature with enough points (M > N_s at every degree).
2. Express BJ and mirror (and alternating) capacities through the explicit recurrence matrices.
3. Look for a transfer-matrix or recursion structure in degree, as the U-recurrence gave on SH_n.
4. **Aim:** an exponential BJ lower bound and a polynomial good-rule upper bound for all n, on at least one parameter point (α, β, γ) and one discrete grid family.

Watch the symmetry. The simplex has the S₃ symmetry permuting x, y and 1−x−y. Decide whether BJ, mirror and alternating behave differently under it, and say which coordinate choice each statement uses.

### P2 — rotation invariance: the disk (test of "geometry vs coordinates")

- **Families:** disk polynomials, i.e. Zernike-type OPs for the weight (1−x²−y²)^μ, with explicit recurrences (Dunkl–Xu).
- **Exact discrete version:** rational points on circles from Pythagorean triples, giving exact rational disk grids with concentric rational radii.
- **Question:** under full rotation symmetry no coordinate direction is preferred. Does BJ still lose exponentially against mirror, or do all staircase orderings become comparable?
- **Outcomes:** either is informative.
  - A proved separation on the disk shows that the effect needs no preferred axes.
  - A proved polynomial bound for every ordering, or a scoped PD-N, shows that drift is an interplay between coordinates and geometry. Record that as a structural result.

### P3 — breaking SH_n non-affinely (stability route)

- **Family:** perturb SH_n's nodes by a smooth non-affine map, (s_k, 2s_k + s_l + η φ(s_k, s_l)), with a fixed polynomial or trigonometric φ, or perturb the weights non-multiplicatively.
- **First theorem:** a stability radius η₀(n) within which PD-T324's separation persists. Use first-order perturbation of the normal-quotient map plus explicit second-order bounds.
- **The adventurous question:** can η₀ be taken **independent of n**? A positive answer gives, for each fixed η ∈ (0, η₀], a genuinely non-product family with all-degree separation.
- **Kill:** if η₀(n) must decay exponentially for the stated φ. Record the decay and try one other φ before stopping.

### P4 — a structural criterion

Conjecture and test a criterion of the form: "BJ capacity grows exponentially on a measure family iff ⟨some explicit quantity⟩ is bounded below along the BJ chain." Candidates:
- the angle between the BJ multiplication direction and the measure's principal axes;
- the growth of the inverse normal-quotient factors;
- the condition number of the leading coefficient matrices in the matrix three-term recurrence.

Test it exactly on SH_n, T_N, rotQ_N, the disk grids and Padua (P5) at degrees ≤ 12–16, before any proof attempt. One proved sufficient condition that covers P1 or P2 is enough.

### P5 — Padua and cubature measures (bounded, 5 rounds)

- The Padua discrete measure reproduces the product Chebyshev measure up to its exactness degree. Its OPs are therefore product-like below the top degree and deviate only near it (compare PD-T069/T144).
- Decide whether drift there is bounded, polynomial or exponential in n. That links the drift theory to the Padua obstruction results.

### P6 — measured scans (parallel from the start)

- Run exact rational capacity scans (aggregate model, the PD-T338 machinery) on:
  - the lattice triangle with uniform and Hahn weights;
  - the rational disk grids;
  - perturbed SH_n;
  - Padua.
- Cover degrees 2–16 (20 where affordable) and four rules (BJ, mirror, alternating, pivot-adaptive).
- Use the native C++/GMP or FLINT producer, with an independent checker on a distinct path.
- Pre-register fits as in G1 of PR #24. The fits steer the proof work only; they never prove a rate.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **N0, replay.** Reproduce PD-T324's exact small-n checks (n = 2, 3, 4) and three PD-T338 rows (T24 and rotQ24, degree 12, BJ and mirror) from committed code. **Kill:** any mismatch.
- **N1, family admission.** Admit a family to P1–P5 only with:
  - a written proof that it is genuinely non-product;
  - exact rational or algebraic data (or an exact cubature) at every tested degree;
  - M > N_s at every degree.
- **N2, growth screen** (MEASURED). For each admitted family, pre-register before running the slope of log(κ_BJ/κ_best) against degree on degrees 8–16, and the rule "exponential if the slope lower bound is > 0.1 per degree on both halves of the window".
  - **Pass:** proceed to a proof attempt.
  - **Kill (exponential separation on that family):** an upper slope bound below 0.02 per degree. Then try a proof of a polynomial bound instead, which may yield a scoped PD-N or a positive structural result for P2/P4.
- **N3, structure probe** (before any all-degree proof on P1/P2). Exhibit the degree recursion of the BJ capacity (transfer matrix, continued fraction, or explicit product) symbolically at degrees ≤ 8, and check it against N2's exact values. **Kill:** no recursion of bounded order is visible at degree 8. Then switch that family to P4's criterion route.
- **N4, P3 radius.** Compute exact or certified η₀(n) for n = 2–10. Pre-register "η₀(n) ≥ c n^(−k) for some k ≤ 4" as the bounded-decay pass. **Kill (uniform η₀):** certified η₀(n) decaying faster than every polynomial.

## Round budget and parallelism

- Up to **10 rounds per direction** (P5 capped at 5), with **all directions in parallel** from the start after N0. Each direction has its own subagent and disjoint files; only the coordinator writes LOG, `rounds.md`, `gates.md`, results and the report.
- A round is one development step ending in a pushed LOG entry with its outcome.
- A direction continues only after recorded progress: a new proved lemma, a sharper bound, an admitted family, or a gate verdict.
- Two consecutive rounds without progress end it, with the obstacle recorded.
- AC may raise the budget.

## Read first

- AGENTS.md, agents/WORKFLOW.md (including the new "Proportionate audit and records" section) and agents/codex/CODEX.md at the branch head.
- `topics/padua-lanczos-frontier-20261105/`:
  - report.md;
  - theory/ (above all l1-01-sheared-U-aggregate-separation.md, l2-sh-worst-case-closure-growth.md, l2-sh-random-closure-growth.md, g1-finite-growth-measurements.md, l4-envelope-bound.md);
  - attempts/L1.md, attempts/L2.md, ideas-l1-l2.md;
  - g1-methods.md and code/.
- `topics/padua-lanczos-drift-20261101/`: report.md, directions/E2.md.
- `tracks/bivariate-lanczos/theory/`: drift-codex-*.md (PD-T136–146), PD-T053, PD-T069, PD-T144. Also `tracks/bivariate-lanczos/code/drift/`.
- PROOF_STATUS rows PD-T053, PD-T055, PD-T069, PD-T136–T146, PD-T324–T339 and PD-N062/063, N116–118. IDEAS entries IDEA-246–267 and 414–424.
- `literature/INDEX.md` and `topics/padua-literature-20261103/p3-comparison.md` (merged PR #21) for priority wording.

## Scope limits

- **Where to write.** Only inside `topics/padua-lanczos-nonproduct-20261105/` and `results/padua-lanczos-nonproduct-20261105.md`.
  - Do not edit merged files during development. Import or copy frozen code instead.
  - At PR preparation, edit the shared registries directly; they are reviewed by diff under the new WORKFLOW rule.
  - Do not write to any other open branch: PRs #27, #28 and later ones.
- **IDs.** Provisional IDs `PD-T?lanczos-nonproduct-codex-NN`, and likewise for PD-N, IDEA and LIT. Reserve final ranges when first needed (normally at PR preparation) by the WORKFLOW procedure, and recheck at readiness.
- **Statuses follow AGENTS.md.**
  - Scans and fits are MEASURED.
  - An all-degree claim needs a written proof. A computer-assisted step needs a proved reduction, exact or outward arithmetic, committed producer and checker code, and an independent rerun on a distinct path.
  - State the model (aggregate, scalar-operation, finite error) in every statement, and never mix models across a comparison.
- **Storage** (WORKFLOW): commit code and small evidence, normally under 16 KiB per file. Large exact arrays go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.**
  - Sandbox: up to 6 h wall per run and about 48 h cumulative CPU, as AC approved for the parallel campaigns the same day.
  - Ask AC before using Syvert. If you do, build packs in the "Syvert run pack" structure of the bridge handoff. Until PR #27 merges, read it with `git show origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/handoffs/01-work.md`.
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md` (written before the first run) and `rounds.md`.
  - `gates.md`, with N0–N4 verdicts.
  - `attempts/P1…P6.md` and `novelty-gate-*.md`.
  - `theory/` records in THEORY-template form: the non-product definition and admissions, each lemma, each family theorem, each PD-N.
  - `independent-checks*.md`, `evidence-manifest.json`, results kept current, and `report.md` at the end.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR early; no reservation is needed for a draft under the new rules.
- **The report contains:**
  - N0–N4 verdicts;
  - for each family, its non-product proof, the exact scan table and the theorem or obstruction;
  - the answer to the disk question;
  - the P3 radius law;
  - any structural criterion;
  - what remains OPEN;
  - a "for the paper" paragraph stating how the bivariate Lanczos / V+A note's main theorem changes.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-lanczos-nonproduct-20261105.`
