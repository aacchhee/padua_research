# Handoff 01 — nn-mop-conditioning-20261106 — is the exponential NN-MOP conditioning intrinsic? Sharp rates, weak stability, IEP-MOP comparison

- Status: open
- Previous handoff: none (new topic; predecessor `topics/nn-mop-stability-20261105/`, merged as PR #28)

- Next agent / model / effort: Codex, with the allocation AC set on 2026-11-05:
  - coordinator: gpt-6-astra high;
  - code, metric runs, Octave comparison and bookkeeping: gpt-6.1-sol medium;
  - routine mathematics: gpt-6.1-sol xhigh;
  - gpt-6-astra ultra only for a decisive hard step (the sharp Krawtchouk upper rate, a gauge-invariant lower bound, or a weak-stability theorem), with a one-line justification in LOG;
  - supplementary independent checks: a distinct gpt-6-astra high instance.
- Role: orchestrator and developer
- Branch: codex/nn-mop-conditioning-20261106
- Input head SHA: `76ba421` (main, PR #28 merged; this branch adds only this handoff, LOG and the results stub)
- Main / base: `76ba421` (PR #29 rules)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-06. AC: "yes open a codex branch for step 1". Step 1 of Claude's plan of the same day is a focused round that settles the metric question, the sharp rates, weak stability and the IEP-MOP comparison, ahead of a note.

## Where PR #28 left it

- **PD-T432:** the local derivative and the exact induced condition numbers for the NN map and the monic alternating step-line map.
  - Input model: absolute node perturbations at scale one, plus componentwise relative weight perturbations, with masses as null directions.
  - Output metric: the largest relative sup error over the four NN fields (the PD-T290 metric).
- **PD-T437:** an all-N Krawtchouk lower bound with base 5+2√6 ≈ 9.899.
- **PD-T433:** a much coarser explicit upper bound.
- **PD-T434 (MEASURED), N = 4–64:**

  | N | NN Krawtchouk | step-line Krawtchouk | NN Hahn | step-line Hahn |
  |---|---|---|---|---|
  | 16 | 5.1e13 | 2.0e13 | 5.6e15 | 1.5e15 |
  | 32 | 2.6e29 | 7.2e28 | 5.3e32 | 1.1e32 |
  | 64 | 1.2e61 | 3.2e60 | 9.6e66 | 1.7e66 |

  - Per-node growth on N = 48–64 is about 9.8 for Krawtchouk and about 11.8 for Hahn (Claude's arithmetic).
  - The step-line map is only about 4 times better than NN in this metric.
- **PD-N162:** κ·d_min diverges as p₂ → p₁.
- **PD-T438:** C4 has excess loss in its layer recursion at small N.
- **PD-T440:** the orthobasis mixed solve gains about 2.8 digits at N = 8.
- **PD-T441 / PD-N163:** the backward-error geometry, and infinite strict backward error for a raw output.
- **PD-T448 and PD-T449 OPEN:** the sharp matching growth and a general stable solver.
- **The G5 Octave reproduction of IEP-MOP passed.** The field-by-field topic-metric comparison was not run.
- **The record names the gap itself.** "This monic step-line convention need not equal a literature algorithm's diagonally scaled Hessenberg output". "The effect of alternate diagonal scaling of the step-line output" is OPEN (conditioning-local.md).

**The decisive question.** Is "about one digit lost per node" a property of multiple orthogonality, or of the chosen coordinates and metric? Any note to the Leuven group must answer this first.

## Directions (in parallel after M0)

### C1 — the metric question (first priority)

1. **1-D control.** Compute κ for the scalar Jacobi inverse problem of each marginal measure (Krawtchouk with p₁ and p₂; the Hahn marginals) in:
   - (a) the PD-T432 input model with monic output;
   - (b) the symmetric orthonormal Jacobi output (α_k, √β_k).

   Do this for N = 4–64, with the same code path where possible.
2. **Gauge-optimal multiple-orthogonal κ.** Define the diagonal output gauge group: rescalings of the monic polynomials, and their effect on the NN fields and on the step-line Hessenberg entries. Define κ_gauge = inf over gauges of κ, in a theory file, with the optimization domain stated. Compute it, or bound it above and below, for both families, N = 4–64.
3. **The LIT-347 normalization.** Reconstruct the exact Hessenberg normalization used by Faghih et al. from their paper and the pinned IEP-MOP archive. Compute κ in that metric for their test families. Compare it with their reported, and our reproduced, forward errors: does forward error ≈ κ·u explain their "weakly stable" observation?
4. **Input-model variants.** Compute κ under each of these:
   - relative node perturbations in natural spacing;
   - log-weights;
   - fixed-mass constraints.
5. **Theory.** Prove whichever way the screen points:
   - a **gauge-invariant** exponential lower bound (for example, the PD-T437 witness direction survives every diagonal gauge, for a reason that can be proved); or
   - an explicit gauge with polynomial κ, which shows the exponential is a coordinate effect.

### C2 — sharp rates

- **Krawtchouk:** a matching upper bound with base 5+2√6 and an explicit polynomial prefactor, closing PD-T448 for that family in the PD-T432 metric. Then in the C1 gauge-optimal metric if C1 makes it the right one.
- **Hahn:** an all-N lower bound and identification of its base. The measured value is about 11.8 per node, which is MEASURED only.
- **Adventurous:** the base as an explicit function ρ(p₁, p₂) for multiple Krawtchouk, consistent with PD-N162's proximity divergence. That is "how many digits per node, as a function of how distinct the two measures are". It is a practitioner-facing formula for the note.

### C3 — weak stability

- Prove forward error ≤ C·κ·u + O(u²) for one concrete binary64 algorithm, in a stated metric. The PD-T440 orthobasis mixed solve (A-LU) is the natural candidate.
- Alternatively, prove a backward-stability statement in the PD-T441 manifold metric, or a proved obstruction such as an excess-loss lower bound for C4's layer recursion.
- Check it against the frozen grid; see M3.

### C4 — IEP-MOP field-by-field comparison

Run the pinned IEP-MOP code (Octave) and the NN solvers (C4, A-LU, A-QR, B nodeqr) on identical inputs.
- Report errors in two metrics: monic NN fields, and the LIT-347 Hessenberg normalization from C1(3).
- Use both families, N = 4–32, plus every LIT-347 configuration the archive covers.
- Results are MEASURED and platform-dependent; record the platform.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **M0, replay.** Reproduce PD-T434's κ at N = 4, 16 and 32, for both families and both maps, to 1e-10 relative, from committed code. **Kill:** mismatch.
- **M1, metric screen (MEASURED).**
  - Compute the per-node growth ratio, fitted on N = 32–64, for the 1-D monic, 1-D orthonormal, NN monic, step-line monic, LIT-347-normalized and gauge-optimal κ.
  - **Pre-registered verdicts:**
    - **intrinsic:** gauge-optimal ratio ≥ 5 for both families;
    - **coordinate effect:** ≤ 2;
    - **mixed:** otherwise, and C1(5) proof work decides.
  - In addition, record whether the 1-D orthonormal κ grows at most polynomially. That is the expected control.
  - Fits never prove a rate.
- **M2, normalization fidelity.** Before any LIT-347-metric claim, our reconstruction of their normalization must reproduce their code's Hessenberg output on one configuration to 1e-12 relative. **Kill:** mismatch. Then no LIT-347-metric statement is made, and the mismatch is recorded.
- **M3, weak-stability check.** A claimed C3 theorem must hold, with its stated constant C, on every frozen-grid case (both families, N = 4–32) in measured binary64. **Kill (that claim):** any violation. Revisit the proof.
- **M4, comparison sanity.** Re-pass the PR #28 G5 configuration before running new C4 comparisons.

## Round budget and parallelism

- Up to **8 rounds per direction** (C1–C4), all in parallel after M0. Each direction has its own subagent and disjoint files; only the coordinator writes LOG, `rounds.md`, `gates.md`, results and the report.
- A round ends in a pushed LOG entry with its outcome.
- A direction continues only after recorded progress.
- Two consecutive empty rounds end it, with the obstacle recorded. Kills apply regardless of the budget.
- AC may raise the budget.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- `topics/nn-mop-stability-20261105/`:
  - report.md and gates.md;
  - attempts/D1.md, D2.md, D3.md, D5.md and D7.md;
  - theory conditioning-*.md, native-measurements.md, backward-*.md, stable-solver-target.md;
  - code/ (conditioning*.py, native_mixed.py, stage_isolation.py, backward_*.py);
  - g5-run/README.md, audit-01.md, audit-02.md, audit-g5-01.md, LOG.md (AC decisions and the IEP-MOP archive pin).
- `topics/nn-mop-iep-20261103/report.md` and theory/ (PD-T286–290).
- `topics/padua-literature-20261103/notes/faghih-sinum-2026-assessment.md`.
- PROOF_STATUS rows PD-T286–T290, PD-T432–T449 and PD-N100, N162–N168. IDEAS entries IDEA-117, 376–379 and the PR #28 section.
- `literature/INDEX.md`: LIT-347, LIT-348, LIT-562–568 and the PR #28 LIT entries.

## Scope limits

- **Where to write.** Only inside `topics/nn-mop-conditioning-20261106/` and `results/nn-mop-conditioning-20261106.md`.
  - Do not edit merged files. Import or copy frozen code instead.
  - At PR preparation, edit the shared registries directly; the readiness check reviews them by diff.
  - Do not write to any other open branch: PR #27 and `codex/padua-mz-sharp-constants-20261106`.
- **IDs.** Provisional IDs `PD-T?nn-mop-cond-codex-NN`, and likewise for PD-N, IDEA and LIT. Reserve final ranges when first needed (normally at PR preparation), and recheck at readiness.
- **Novelty gate** before each new mechanism. Nearest entries: IDEA-376–379 and the PR #28 IDEA entries.
- **Statuses follow AGENTS.md.**
  - κ tables, fits and comparisons are MEASURED.
  - Rates and stability results need written proofs. Exact or high-precision checks support them but never replace them.
  - State the input and output metric in every statement.
- **Storage:** commit code and small evidence, normally under 16 KiB per file. Larger tables go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.** Sandbox: up to 6 h wall per run and about 48 h of cumulative CPU. Ask AC before using Syvert.
- **Third-party code.** IEP-MOP is never committed. Use AC's pinned archive and record its hashes and URL.
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.
- **No contact with anyone outside the repository.** The note is for AC to use as he decides.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md` (written before the first run) and `rounds.md`.
  - `gates.md`, with M0–M4 verdicts and pre-registrations.
  - `attempts/C1…C4.md` and `novelty-gate-*.md`.
  - `theory/` records in THEORY-template form, one per result.
  - `independent-checks*.md`, `evidence-manifest.json` and `external-code.md`.
  - `note-material.md`: the statements a short note would make, each with its record and metric.
  - `results/nn-mop-conditioning-20261106.md`, kept current, and `report.md` at the end.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR early; no reservation is needed for a draft.
- **The report opens with the M1 verdict:** intrinsic, coordinate effect or mixed, plus the proof status behind it. Then:
  - the sharp-rate status for both families and any ρ(p₁, p₂) formula;
  - the weak-stability result;
  - the IEP-MOP comparison tables;
  - what remains OPEN.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by Claude, Opus 5.5 xhigh. That audit reads the complete state/IDEAS.md if new mechanisms or novelty claims are present; otherwise it records "novelty: not applicable" with the reason. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/nn-mop-conditioning-20261106.`
