# Handoff 01 — nn-mop-stability-20261105 — conditioning and stable algorithms for the nearest-neighbour MOP inverse eigenvalue problem

- Status: done in ff783d59587100ab291cb83d690ef27a09f0f154
- Previous handoff: none (new topic; predecessor `topics/nn-mop-iep-20261103/`, merged as PR #22)

- Next agent / model / effort: Codex. This follows the allocation AC set for the argmax bridge on 2026-11-05 ("Run the coordinator on Astra High, easier jobs on Sol and raise to Astra Ultra only when things get serious"):
  - coordinator: gpt-6-astra high;
  - code, replays, sweeps and bookkeeping: gpt-6.1-sol medium;
  - routine mathematics: gpt-6.1-sol xhigh;
  - gpt-6-astra ultra only for a decisive hard step, such as an all-N conditioning theorem or a stability proof, with a one-line justification in LOG;
  - supplementary independent checks: a distinct gpt-6-astra high instance.
- Role: orchestrator and developer
- Branch: codex/nn-mop-stability-20261105
- Input head SHA: `b4d292e` (main, PR #21 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `b4d292e`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-05. AC: "Yes open a topic. You may be a bit more adventurous in plans."

## Problem and what PR #22 settled

**The problem.**
- Data: N distinct real nodes and two positive weight vectors w₁, w₂, giving type II multiple orthogonal polynomials P_ν, ν = (n, m).
- Nearest-neighbour (NN) recurrence, for j = 1, 2: x P_ν = P_{ν+e_j} + b_{ν,j} P_ν + a_{ν,1} P_{ν−e₁} + a_{ν,2} P_{ν−e₂}.
- Unknowns: the four arrays (a₁, a₂, b₁, b₂) on the triangle |ν| ≤ N−1.
- The inverse eigenvalue problem (IEP) asks for these arrays from the nodes and weights.

**Settled (all on main):**
- **PD-T286.** The exact moment formulation, under normality.
- **PD-T288.** The interior divisor d = b₂ − b₁ is nonzero.
- **PD-T289.** Complete reconstruction from the two marginal Jacobi families (algorithm C4, the Filipuk–Haneczok–Van Assche 2015 route). Its divisors have degree ≤ N−2. At the terminal layer b₁ = b₂ necessarily.
- **PD-N100 / IDEA-377.** The literal "commuting pair" dictionary fails. The true structure is lattice compatibility (zero curvature), so this is a one-variable problem and not a model of the bivariate PD-T057.
- **PD-T290 (MEASURED).** The binary64 C4 run (plain Stieltjes marginals followed by the layer recursion) has normwise coefficient error E as follows:

  | N | 4 | 8 | 12 | 16 | 24 | 32 |
  |---|---|---|---|---|---|---|
  | Krawtchouk (p = 2/5, 1/2) | 1e-13 | 2e-9 | 2e-6 | 0.10 | 7e4 | 5e3 |
  | Hahn (β = 1, 3/2; γ = 1) | 1e-12 | 3e-7 | 2e-3 | 70 | 3e2 | 7e5 |

- **Literature on main.**
  - LIT-347: Faghih–Rinelli–Van Barel–Vandebril–Vermeiren, SINUM 64(4) 2026, step-line IEP. On these families the methods are weakly stable. IEP_CORE and IEP_KRYLREORTH(full) are backward stable for most N < 25. Their §7 lists IEP conditioning and NN recurrences as open.
  - LIT-348: Faghih–Van Barel–Vandebril, arXiv 2608.25758, updating and downdating.
  - LIT-562: Van Assche 2011 on NN recurrences.
  - LIT-565–567: Aptekarev–Derevyagin–(Miki–)Van Assche, 2-D discrete Schrödinger / lattice operators for MOPs.
  - LIT-568: Kozhan–Vaktnäs, Christoffel transforms.

**The unresolved point.** PD-T290 measured forward error only. It did not separate C4's error from the problem's conditioning, and no backward error was measured. "C4 loses all accuracy" is therefore not yet "C4 is unstable".

## Directions (run in parallel; be adventurous)

Each direction passes the novelty gate (relaxed scan) before work. The nearest entries are IDEA-117, IDEA-376–379 and IDEA?bivariate-lanczos-claude-041. Also read the obstruction rows for PD-N100.

### D1 — conditioning theory (core)

- Define the first-order condition number κ_N of the map (nodes, weights) → (a₁, a₂, b₁, b₂), in normwise and componentwise forms, matching PD-T290's metric. Do this for the NN map and, for comparison, for the step-line map of LIT-347.
- Compute κ_N exactly, or in high precision with a certified derivative, for both families, N = 4–64.
- Then be adventurous:
  - prove the growth law, for example κ_N ≥ c·ρ^N for multiple Krawtchouk with an explicit ρ(p₁, p₂);
  - identify its mechanism: proximity of the two measures through d = b₂ − b₁, discrete-measure Vandermonde conditioning, or potential-theoretic node-density effects;
  - give a formula that predicts digits lost.
- Tools:
  - the exact first-order span and sensitivity machinery of PD-T136/137;
  - moment-cone conditioning (PD-T058/059);
  - the explicit NN coefficients of the classical multiple Krawtchouk and Hahn families (LIT-562 and sources it cites; read the fulltext before use).
- Done: a PROVED conditioning theorem with explicit constants on at least one family, or a precise PARTIAL. A MEASURED κ_N table is the minimum.

### D2 — where C4 loses accuracy (cheap, first)

- Replace only C4's marginal stage with a stable 1-D Jacobi IEP solver: Gragg–Harrod/RKPW rotations, or Lanczos with full reorthogonalization. Keep the layer recursion unchanged.
- Add a backward-error measurement in the LIT-347 style: from the computed NN data, recover nodes and weights along one fixed step-line path and compare them with the input, in high precision.
- Report forward error / (κ_N·u) and backward error for C4, the stable-marginal C4, and every D3/D4 algorithm.

### D3 — native NN algorithms (adventurous)

Design at least two; implement and test the most promising. Candidates:

- **(a) NN core transformations.** Non-unitary eliminators acting on diag(nodes) that produce the NN lattice directly. Generalize IEP_CORE from one path to the whole triangle.
- **(b) Lattice biorthogonal Lanczos with reorthogonalization over all paths.** Maintain type II vectors on the whole triangle and type I vectors on the dual, with the compatibility relations as explicit invariants.
- **(c) Redundancy as stabilization.**
  - Compute step-line recurrences stably along several lattice paths (IEP_CORE-type), map each to NN data (FHV formulas), and combine them.
  - Combine either by least squares under the zero-curvature constraints, or by projecting onto the compatible manifold.
  - Here the compatibility condition becomes an error-correcting code.
- **(d) A coupled node updater: add one node at a time, Gragg–Harrod-style.** Update both weight vectors and the whole NN triangle, with compatibility as the preserved invariant. This is IDEA-378, which was deferred for lack of a concrete invariant. Specify that invariant first.

### D4 — integrable-systems route (adventurous)

- **Christoffel/Geronimus transforms for MOPs** (LIT-568 and the Branquinho–Foulquié-Moreno–Mañas line; read the fulltexts before citing).
  - Multiplying a weight by (x − c), or dividing by it, has an LR- or QR-type implementation on recurrence matrices: Golub–Kautsky and Gautschi modification algorithms in 1-D.
  - The questions:
    - can NN data for one weight pair be transported to another by stable QR-type steps?
    - can that build a stable algorithm from an easy starting pair, for example two equal-node shifted binomials?
- **Multiple discrete Toda flows** on the lattice, as homotopy or continuation methods in the weight parameters.
- **The 2-D lattice Schrödinger operators of LIT-565–567** as a spectral parametrization. Their spectral data might give a better-conditioned input map than (nodes, weights).

### D5 — backward error and well-posedness

- What is the right backward error for an NN array that is only approximately compatible?
- Define the nearest exactly compatible array and the nearest (nodes, weights) pair, and prove the definition is well-posed near normal data.
- Is "weakly stable" the right target for NN, given κ_N from D1?

### D6 — return to two variables (speculative, bounded to 3 rounds)

- PD-N100 kills the literal commuting-pair reading. Is there a different bivariate object that the NN lattice models exactly? Candidates:
  - discrete OPs on the graph of a map y = φ(x), or on two coincident copies of the nodes;
  - Hermite–Padé pairs viewed as polynomials in two variables;
  - a lattice state space with boundary, as in the zero-curvature description.
- If one exists and is positive, check whether D3's stable algorithms transfer to the Padua/bivariate Lanczos setting (PD-T057, PD-T069).
- Kill after 3 rounds without a concrete exact dictionary.

### D7 — Leuven-ready comparison (at the end)

- Run the public IEP-MOP MATLAB code (`gitlab.kuleuven.be/numa/public/IEP-MOP`, LIT-347) under GNU Octave, if it is installable in the sandbox, on identical inputs. Convert its step-line output to NN data via FHV and compare with D2–D4.
- Record the code's URL, commit and hashes in `external-code.md`; never commit it.
- Draft `note-outline.md`: conditioning theorem, stable NN algorithm, experiments. It is for AC's possible contact with Leuven; make no contact yourself.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **G0, replay.** Rerun `topics/nn-mop-iep-20261103/code/c4_float_baseline.py` for both families, N = 4–32. **Kill:** any mismatch with PD-T290's E values beyond 1 % relative.
- **G1, weak-stability verdict for C4.** With κ_N from D1:
  - **C4 is weakly stable on the family** if E_N ≤ 10·κ_N·u for every N tested.
  - Otherwise C4 has **excess loss** of log₁₀(E_N/(κ_N u)) digits; record it per N.

  Either verdict reshapes D3: under weak stability, D3 must aim at backward stability or better conditioning of the input map, not forward accuracy.
- **G2, stage isolation.** The stable-marginal C4 (D2) passes if its excess loss is below 1 digit at every N where C4's excess loss is above 2 digits. Then the marginal stage was the culprit and the layer recursion is cleared. Otherwise the layer recursion carries excess loss, and D3 targets it.
- **G3, parameter sweep** (MEASURED). Compute κ_N and E_N while the two measures approach proportionality (p₂ → p₁ for Krawtchouk, β₂ → β₁ for Hahn), and for one Angelesco-type pair on disjoint node subsets if the common-support setting allows it. Before running, pre-register the prediction "κ_N ∝ 1/min|d|" and test it.
- **G4, algorithm bake-off.**
  - **Pass:** a new D3/D4 algorithm gains ≥ 2 digits over C4 at some N where κ_N·u ≤ 1e-4 (accuracy achievable there), with measured backward error. Or it is backward stable (backward error ≤ 100·u·‖data‖) on N where C4 is not.
  - **Kill (that design):** it is worse than C4 at N = 16 on both families.
- **G5, external comparison.** Before running new problems, reproduce one LIT-347 configuration (one family, one N) to the paper's reported accuracy level. **Kill:** a mismatch stops G5 until it is explained.

## Round budget

- Up to **10 rounds per direction** (D1–D5 and D7; D6 is capped at 3), all running in parallel with disjoint file ownership.
- A round is one development step ending in a pushed LOG entry with its outcome.
- A direction continues only after recorded progress:
  - a new proved lemma;
  - a sharper bound;
  - a new algorithm passing a gate;
  - or a verdict that narrows the route.
- Two consecutive rounds without progress end it, with the obstacle recorded.
- Keep `rounds.md`. Only the coordinator writes the shared files: LOG, `rounds.md`, `gates.md`, results and the report.
- AC may raise the budget.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `topics/nn-mop-iep-20261103/`:
  - report.md, gate.md, candidates.md;
  - theory/ (all), c4-baseline-01.md, exact-runs.md, literature.md, source-recheck-01.md;
  - audit-01.md, audit-02.md, response-01.md;
  - code/.
- `topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md` (now on main).
- PROOF_STATUS rows PD-T057–T059, PD-T069, PD-T136/137, PD-T286–T290 and PD-N100.
- IDEAS entries IDEA-117, IDEA-376–379 and the PR22 section.
- `literature/INDEX.md` (LIT-119, LIT-347, LIT-348, LIT-562–568) and the linked records.

## Scope limits

- **Where to write.** Only inside `topics/nn-mop-stability-20261105/` and `results/nn-mop-stability-20261105.md`.
  - Do not edit merged files. Import or copy frozen code instead.
  - Put shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to any other open branch: PRs #24, #27 and later ones.
- **Provisional IDs:** `PD-T?nn-mop-stability-codex-NN`, and likewise for PD-N, IDEA and LIT. When the draft PR opens, reserve final ranges by the fresh-range procedure, with headroom: main, every open PR, retired reservations and the batch ledger.
- **Statuses follow AGENTS.md.**
  - Floating experiments, condition-number tables and fits are MEASURED.
  - A theorem about κ_N or about stability needs a written proof. A computer-assisted step needs a proved reduction, exact or outward arithmetic, committed producer and checker code, and an independent rerun by a different subagent.
  - Never infer a rate from a fit.
- **Storage** (WORKFLOW, PR #18): commit code and small evidence, normally under 16 KiB per file. Regenerable outputs go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.**
  - Sandbox only: up to 6 h wall per run and about 48 h of cumulative CPU; AC approved these limits for the bridge campaign the same day.
  - Ask AC before using Syvert or any other machine. If you do, build packs in the structure described in the "Syvert run pack" section of the bridge handoff. Until PR #27 merges, read it with `git show origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/handoffs/01-work.md`.
- **Third-party code** (IEP-MOP) is never committed; record its URL, commit and hashes.
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md` (written before the first run) and `rounds.md`.
  - `gates.md`, with G0–G5 verdicts.
  - `attempts/D1…D7.md` and `novelty-gate-*.md`.
  - `theory/` records in THEORY-template form, one per result.
  - `independent-checks*.md`, `evidence-manifest.json`, `external-code.md` and `note-outline.md`.
  - `results/nn-mop-stability-20261105.md`, kept current, and `report.md` at the end.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- **The report contains:**
  - G0–G5 verdicts;
  - κ_N tables and any conditioning theorem;
  - the weak-stability verdict on C4;
  - the stage-isolation result;
  - each algorithm's forward and backward errors against κ_N·u;
  - the D6 outcome;
  - the external comparison;
  - what remains OPEN;
  - a short "for a Leuven note" paragraph with exact dependencies.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/nn-mop-stability-20261105.`
