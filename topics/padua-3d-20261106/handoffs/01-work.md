# Handoff 01 — padua-3d-20261106 — Padua-type points in three dimensions

- Status: open
- Previous handoff: none (new topic)

- Next agent / model / effort: Codex.
  - **Coordinator:** gpt-6-astra high.
  - **gpt-6-astra ultra:** allowed whenever a step needs it. AC, 2026-11-06: "Allow Astra Ultra when necessary". Record a one-line reason per escalation in LOG.
  - **Code, exact rank and modular certificates, Lebesgue sweeps, replays and bookkeeping:** gpt-6.1-sol medium.
  - **Routine mathematics:** gpt-6.1-sol xhigh.
  - **Supplementary independent checks:** a distinct gpt-6-astra high instance.
- Role: orchestrator and developer
- Branch: codex/padua-3d-20261106
- Input head SHA: `76ba421` (main; this branch adds only BRIEF.md, this handoff, LOG and the results stub)
- Main / base: `76ba421` (PR #29 rules)
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-06. AC: "Make a proper adventurous reasoning topic on 3D, write what you know and what you expect. Allow Astra Ultra when necessary, 25 rounds, otherwise usual rules".

## Read BRIEF.md first

[BRIEF.md](../BRIEF.md) has the knowledge base:
- §1: the target;
- §2: the 2-D mechanism P1–P4 and where each part breaks in 3-D;
- §3: what this repository already proved or measured in 3-D;
- §4: Claude's expectations E1–E6;
- §5: literature to read.

The expectations are steering only. Overturning any of them is a result.

## Goal

Make real progress on the 3-D Padua problem, in either direction:

- **Positive:** an explicit, proved-unisolvent total-degree family in [−1,1]³ for infinitely many n. It should have a proved Lebesgue bound, polylogarithmic ideally (target O(log³ n)), or measured quality that clearly beats the BRIEF §3 baselines (QR approximate Fekete and Leja lower sets) together with a proved bound.
- **Negative:** a theorem that no set in a precisely defined natural class can be Padua-like. Examples of such a class: cosine images of torus-subgroup cosets or of unions of ≤ k cosets, or sets with near-exact positive Chebyshev cubature. Prove the theorem for that class, for all large n.
- **Side results:** small-degree non-existence certificates for near-minimal Chebyshev cubature on the cube, Lebesgue lower bounds for total-degree interpolation in the cube, or anything of comparable weight.

## Directions (all in parallel from the start, after gate D0)

### T1 — obstruction theory

- Formalize the class C_k: node sets that are cosine images of cosets of finite subgroups of the torus 𝕋³, with reflection folding, or unions of at most k such cosets.
- Prove that for |X| = binom(n+3, 3), unisolvence on Π_n combined with any of the following is impossible for all large n:
  - (i) discrete orthogonality of a total-degree basis;
  - (ii) positive cubature of degree ≥ 2n−1;
  - (iii) the full Padua package (P2 + P3 of BRIEF §2).
- **Tools:**
  - aliasing and annihilator lattices (difference sets of the simplex against the dual lattice);
  - Möller-type and Li–Sun–Xu-type counting;
  - the reflection-invariance obstruction for mod-6 fibres (BRIEF §2, P1′ caveat).
- **Sanity requirement:** every obstruction lemma, applied verbatim with d = 2, must fail to exclude 2-D Padua; see gate D3.

### T2 — positive constructions by aliasing design (main positive line)

Search structured design spaces, exactly where possible:

- **(a) Lissajous–Chebyshev / rank-1 Chebyshev-lattice node sets** (Dencker–Erb; Cools–Poppe; Potts–Volkmer). Compute their spectral index sets and test alias-equivalence to the total-degree simplex.
- **(b) Unions of two or three cosets**, such as a DMVX parity subgrid thinned by a second character, sized exactly binom(n+3, 3).
- **(c) Mod-6 fibres and other cardinality-valid index fibres** on Chebyshev–Lobatto axes, revisited only with a new structural reason (PD-N037 is the warning).
- **(d) "Lissajous points + structured correction".** Start from a curve or lattice sample of size near binom(n+3, 3) and fix the deficiency with a small explicit set.

**Method for each family:**
1. Exact unisolvence, either by an exact or modular rank, using the finite-field Padua dictionary idea (rank certificates mod several primes ∤ the relevant products), or by proof.
2. Float Lebesgue constants on a mesh fine enough for n ≤ 20, against the BRIEF §3 baselines, with fits pre-registered.

Families passing gate D2 move to T3.

### T3 — proofs for surviving families

- Prove unisolvence for every n in the family, by an aliasing identity, an ideal or H-basis description, or a Vandermonde factorization in the style of PD-T093.
- Then attack the Lebesgue bound. Use the 2-D Padua Lebesgue machinery of this repository (lattice-sum kernels, PD-T101/T206–231) as the template.

### T4 — baselines with proofs

- **Radon/Berzolari stacking.** Place 2-D Padua sets of degrees n, n−1, …, 0 on n+1 parallel planes at Chebyshev–Lobatto heights, with orderings chosen deliberately. This family is provably unisolvent.
- Measure its Lebesgue growth, and prove a lower or upper bound. Claude's expectation: polynomial growth (BRIEF E2).
- Purpose: an honest proved baseline the positive line must beat, and possibly a short result in itself.

### T5 — cubature and joint-spectrum side line (bounded: at most 8 rounds)

- Exact non-existence certificates for near-minimal product-Chebyshev cubature on the cube at small degrees (5–9). Use algebraic or Gröbner methods, SOS, or exact LP on moment conditions.
- Also a small probe of the commuting-completion and joint-spectrum route (IDEA-120): compute minimal commutator norms of completed truncated multiplication triples at n ≤ 4.
- Kill after 3 rounds without a working exact pipeline.

### T6 — Lebesgue lower bounds in the cube (bounded: at most 8 rounds)

- Survey the literature first; such bounds may be known.
- If none is found, prove Λ(X) ≥ c logᵈ n, or a weaker explicit bound, for every unisolvent total-degree set in [−1,1]³.
- If one exists, record it as LIT and use it to frame T2/T3.

## Gates (kill criteria written here, before any run)

If a criterion proves ill-posed, record why and add a new criterion as a separate dated entry; never edit the original.

- **D0, replay.** Rerun the exact checks of PD-T082 and PD-T093 and two PD-N037 rows from `tracks/lattice-unisolvence/code/`. Also reproduce 2-D Padua sanity values: unisolvence at n ≤ 10, and the corner Lebesgue value Λ_c(n) of PD-T101 at n ≤ 8, from the 3-D tools restricted to d = 2. **Kill:** any mismatch stops new work until it is explained.
- **D1, tool validation.**
  - The 3-D Lebesgue evaluator must reproduce the PD-N037 baselines to their recorded digits.
  - The exact or modular rank tool must reproduce PD-T093's unisolvence and one known PD-N035 deficiency.
- **D2, family screen.** Write the pre-registration in `gates.md` before running.
  - **Promising:** exact unisolvence certified at every admissible n ≤ 12 (or the largest feasible n), **and** measured Λ below the QR approximate Fekete baseline at every n ≥ 4 tested, **and** a pre-registered fit preferring C·log³ n (or C·logᵏ n, k ≤ 4) over C·n^α with α ≥ 1 on n ≤ 20.
  - **Kill (that family):** a certified rank deficiency at an admissible n, recorded as a scoped PD-N, or Λ above the Leja lower-set baseline at two consecutive n ≥ 6.
- **D3, obstruction sanity.** A T1 obstruction counts only if:
  - (a) its d = 2 specialization provably does *not* exclude 2-D Padua;
  - (b) it is checked by exhaustive exact enumeration at small n in 3-D within its class, wherever the class is finite at that n.
- **D4, T5 pipeline.** An exact certificate must reproduce a known existence result (a known small-degree 2-D or 3-D cubature) before any non-existence claim. **Kill (T5):** no working pipeline after 3 rounds.

## Round budget and parallelism

- **25 rounds per direction** (AC: "25 rounds"; Claude reads this as per direction, as for the bridge. AC may correct it). Exceptions: T5 and T6 are capped at 8.
- All directions run **in parallel** from the start after D0, each with its own subagent and disjoint files. Only the coordinator writes LOG, `rounds.md`, `gates.md`, results and the report.
- A round is one development step ending in a pushed LOG entry with its outcome.
- A direction continues only after recorded progress: a new proved lemma, a certified family property, a gate verdict, or a sharper bound.
- Two consecutive rounds without progress end it, with the obstacle recorded. Kills apply regardless of the budget.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- [BRIEF.md](../BRIEF.md).
- `tracks/lattice-unisolvence/`: README.md, theory/ (all c0-*, c1-*, c3-*), code/. Also `topics/lattice-unisolvence-20261031/` (report, audit-01, response-01, independent/).
- `topics/charter-unisolvence-20261031/` (plan and the U1 results relevant to checkerboard unisolvence).
- The 2-D Padua structure:
  - PD-T101, PD-T106, PD-T109;
  - PD-T095–T097 and PD-T102 (commuting pairs);
  - the lattice-sum Lebesgue machinery in `topics/padua-argmax-alln-20261101/theory/` (gated-codex-01–04).
- The programme notes on finite-field Padua and minimal cubature (X7): `topics/programme-ideas-20261031/` and the project reports referenced from IDEAS (IDEA-013, IDEA-029, IDEA-120, IDEA-178, IDEA-185, IDEA-186).
- PROOF_STATUS rows PD-T081–T094 and PD-N032–N038. IDEAS entries above and the lattice obstruction rows.
- `literature/INDEX.md` (LIT-014, LIT-301–322, LIT-377, LIT-380, LIT-392, LIT-393/394) and the linked records. Read BRIEF §5's sources in fulltext before any citation.

## Scope limits

- **Where to write.** Only inside `topics/padua-3d-20261106/` and `results/padua-3d-20261106.md`.
  - Do not edit merged files. Import or copy frozen code instead.
  - At PR preparation, edit the shared registries directly; the readiness check reviews them by diff.
  - Do not write to any other open branch: PR #27 and the sharp-constants and NN-MOP conditioning branches.
- **IDs.** Provisional IDs `PD-T?padua-3d-codex-NN`, and likewise for PD-N, IDEA and LIT. Reserve final ranges when first needed (normally at PR preparation), and recheck at readiness.
- **Novelty gate** before each mechanism, using the relaxed scan. Nearest entries: IDEA-013, 029, 120, 178, 185, 186, and the lattice and charter entries.
- **Statuses follow AGENTS.md.**
  - Float Lebesgue values, fits and searches are MEASURED.
  - Unisolvence for a finite list of n is PROVED only by exact arithmetic, or by modular ranks with a proved reduction (nonzero mod p implies nonzero over ℚ, with exact data), plus committed code and an independent rerun.
  - All-n claims need written proofs.
  - A failed family is a scoped PD-N, never a universal non-existence claim.
- **Storage:** commit code and small evidence, normally under 16 KiB per file. Catalogues, rank tables and meshes go to cold storage via `tools/cold_storage.py`, with `cold-storage.json` and `COLD_STORAGE.md`.
- **Compute.**
  - Sandbox: up to 6 h wall per run and about 48 h of cumulative CPU, as AC approved for the parallel campaigns.
  - Ask AC before using Syvert. If you do, build packs in the "Syvert run pack" structure of the bridge handoff. Until PR #27 merges, read it with `git show origin/codex/padua-argmax-bridge-20261105:topics/padua-argmax-bridge-20261105/handoffs/01-work.md`.
- **Literature.**
  - You may open any public page holding relevant literature. Cite only after a fulltext read, and record LIT entries.
  - List unreachable fulltexts for AC with clickable DOI and journal links.
  - Never commit third-party PDFs or extracts (the repo is public). Do not bypass captchas or bot checks.
- **Commits** are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- **Files.**
  - `LOG.md`, `plan.md` (written before the first run) and `rounds.md`.
  - `gates.md`, with D0–D4 verdicts and pre-registrations.
  - `attempts/T1…T6.md` and `novelty-gate-*.md`.
  - `theory/` records in THEORY-template form: each class definition, obstruction, family, unisolvence proof, Lebesgue bound and PD-N.
  - `independent-checks*.md`, `evidence-manifest.json` and `literature-3d.md` (sources read, LIT entries, access gaps with links).
  - `results/padua-3d-20261106.md`, kept current, and `report.md` at the end.
- **Pushes and PR.** Push at every gate and round boundary, and at least every ~10 minutes while something has changed. Open a draft PR early; no reservation is needed for a draft.
- **The report contains:**
  - D0–D4 verdicts;
  - for each direction, the outcome with record links;
  - which BRIEF §4 expectations were confirmed, refuted or left open;
  - the best family found, with its certified range and Lebesgue table against the baselines;
  - any obstruction theorem with its exact class;
  - what remains OPEN;
  - a "for a paper" paragraph.
- **Closing.** When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the single substantive audit by Claude, Opus 5.5 xhigh, which reads the complete state/IDEAS.md because this branch carries mechanism and novelty content. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-3d-20261106.`
