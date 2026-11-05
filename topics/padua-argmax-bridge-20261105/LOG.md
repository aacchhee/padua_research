# Padua argmax bridge 33 ≤ n < N_* (PD-T099): log

- Branch: `codex/padua-argmax-bridge-20261105` · Base: main `9322fba` (PR #25 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/padua-argmax-bridge-20261105.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none yet. Reserve when the draft PR opens: main, open PRs #21 and #24, and retired gaps.
- Claims: none yet.
- Open for AC: none at setup. The sandbox allowance is approved. Syvert is pre-approved under gate B4: syvert1 (16 cores, 256 GB) and syvert2 (32 cores, 128 GB), up to all of both for about a week, and AC launches it from Codex's run package.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "I really do not like this 33 to N gap in argmax. How about an astra ultra round on that?", then "Maybe some neighboring field methods?". The handoff is a bridge-only campaign at gpt-6-astra ultra. It meets in the middle: a practical outward certifier pushed upward from 33, and a degree-uniform computer-assisted proof for all n ≥ n₁ with explicit n₁.
- Neighbouring-field routes N1–N6:
  - N1: explicit Euler–Maclaurin/Abel–Plana remainders plus parameter-compact interval certification;
  - N2: polygonal Lebesgue-constant decompositions (Podkorytov, Kuznetsova, Liflyand, Dencker–Erb–Kolomoitsev–Lomako);
  - N3: Taylor-model and Bernstein validated global optimization;
  - N4: positive-translation/hypergroup ℓ¹ contraction (Askey–Gasper, Koornwinder–Schwartz);
  - N5/N6: 1-D Ehlich–Zeller/Brutman analysis and the Lissajous generating curve.
- Claude's relaxed scan of state/IDEAS.md found no entry for N1–N4's mechanisms. IDEA-318 covers Brutman-type ordering. This scan is a pointer only; Codex runs the novelty gate.
- Rules read at `9322fba` (unchanged since `440d107`). Branch created from main `9322fba`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — AC's budget and model allocation

- AC wrote: "I'd allow more rounds if there is progress, let's say 15 rounds per direction. Run the coordinator on Astra High, easier jobs on Sol and raise to Astra Ultra only when things get serious. Sandbox limits are okey, and Syvert has approx same power, no problem to run 20 cores for a week there if that would meet the analytic N."
- Handoff 01 was amended in place before any Codex work (the branch had no commits after setup):
  - model allocation;
  - a round rule of up to 15 rounds per direction, continued only on recorded progress, with two empty rounds ending a direction early;
  - sandbox limits approved;
  - Syvert pre-approved up to about 20 cores × 7 days under the B4 condition, launched by AC.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — Syvert pack structure

- AC: "If you go for building Syvert packs, check latest bttb Syvert campaigns and use same structure, do not overengineer", then "A B C rounds had especially nice structure".
- Claude read the private bttb A/B/C campaign pack (and the later GMRF2D and offline C+D packs) and added a "Syvert run pack" section to handoff 01 in its own words. Nothing from the private repository was copied.
- The structure:
  - one fresh directory and deterministic ZIP per campaign, with a host/workers/limits table;
  - `plans.py` with a frozen job list;
  - `build_pack.py` with a manifest;
  - `run`, `finished_cases` and `collect_data` through `beregning`, with `--workers`, `--resume` and `--retry-interrupted`;
  - typed failures;
  - a sandbox calibration ladder, freezing against the budget, and a guard of twice the longest job;
  - an offline bundled runtime with a preflight against PD-T246;
  - the returned ZIP checked independently before any degree counts.
- Codex had not started; the handoff was amended in place.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — Syvert hosts

- AC: "Syvert1: 16 cores with 256gb memory, syvet2: 32 core with 128gb memory, use all this if necessary".
- The handoff 01 compute limits and the pack table now name both hosts, with up to all of both for about a week under gate B4. syvert0 still needs a separate ask.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — parallelism

- AC: "Run as much as possible in parallel".
- Handoff 01 task 2 now starts all six directions in parallel after task 0 and B1. It also parallelizes independent work inside each direction.
- Only the coordinator writes shared files, and only real dependencies are serialized.

## Runs needed

- B0–B6 and N1–N6 as in handoff 01.

## 2026-11-05 — Codex continuation setup

- Requested coordinator model/effort: gpt-6-astra high; serving identity and effective effort unexposed. Rules read at full input SHA `db922627395faf6ad888dfaecbf5d7c2108b06c3`, reread at reconciled head `cdd5cdd4ff683e65fb6451006c997e1f2c0cb6be`; rule contents unchanged.
- Fetched current topic and main. Merged main `b4d292eea5eed373002506d5e16a3761bd7ae10e` into the published topic lineage without conflicts. Original base remains `9322fba`. PR21 is now merged; literature reads use current main records.
- Shell network requires the execution tool's additional network permission; ordinary Git initially failed to connect to the proxy. The authorized network-enabled fetch succeeded. No credential values read or printed.
- Written pre-run plan: [plan.md](plan.md). B0 fresh replay is first; no new mathematical claim or final-ID range.
