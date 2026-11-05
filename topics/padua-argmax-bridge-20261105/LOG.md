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

## 2026-11-05 — permanent reservation and early draft

- Complete pinned inventory: all 27 ledger/registry copies at current main and sole foreign open PR24, 20 distinct versions. Live all-state listing: 25 PRs, 24 closed-merged, one open, none closed-unmerged. Union reserved upper endpoints T391/N145/IDEA489/LIT597 include permanent headroom.
- Published reservation `f708a83c705a8e8c61ce8fc9ff94e2e531b62951`: T392–431(40), N146–161(16), IDEA490–529(40), LIT598–613(16). No final IDs assigned; [ALLOCATIONS.md](ALLOCATIONS.md).
- Opened [draft PR27](https://github.com/aacchhee/padua_research/pull/27), clearly WORK and AUDIT PENDING. Topic-only scope; shared registry/crosswalk import deferred to audited preparation.
- Independent B0 worker, B1 preparation worker and novelty-input scanner use requested Sol medium. No new mechanism has been developed. B1's ambiguous 'true maximum' wording is operationally refined before execution in [gates.md](gates.md), retaining continuous extrema as unresolved.

## 2026-11-05 — B0 PASS and novelty-input checkpoint

- Fresh Sol-medium worker regenerated n24 and submitted regenerated and committed certificates separately to the frozen C++/GMP checker. Both accepted; every mathematical field agrees: 307 visited,153 splits,152 strict bound leaves and2 corner leaves. Mathematical SHA256 `c352f9a2c9516aae04e1a956b5d4216a7c83273bcc714a20c212d387a2e9039b`.
- Initial pilot preflight STOP: four prose-input hashes no longer matched the historical receipt. Parent fetched the exact historical scientific source `7d394fd9c45495a32ff91961a5d91942aa59e250`; all original hashes then matched. Exact diffs contain accepted audit-response/registration clarifications; executable pins are unchanged. No mismatch was ignored. The initial failed driver's transient timing journal was unavailable; the worker records that limit and preserves checker timings rather than inventing combined timings.
- Resumed n32 pilot matches all deterministic receipt fields:2000 visits,1449 splits,32 outside,374 far,145 corner-orbit-plus-defect,frontier902,depth11,197 profile boxes. New frontier raw identity is retained; historical raw frontier identity is unavailable. Floating pilot remains incomplete and MEASURED.
- [B0 record](independent-checks-b0.md), [receipt](evidence/b0-replay.json), [runner](code/replay_b0.py). No new degree. B1 now released.
- [Novelty baseline](novelty-gate-baseline.md): full1015-line registry scan and all obstruction/disposition tables, mechanism searches across1470 Markdown files, full canonical shortlist with explicit linked-proof/source-reading limits. Each direction must finish its own precise gate before new development. N4 unrestricted LP equivalence and N6 curve coverage are first discriminating obligations.

## 2026-11-05 — N1 model escalation preregistration

- N1's first decisive step (uniform-in-degree interior profile and integral remainder) is allocated to requested gpt-6-astra ultra. Reason: IDEA337/459 and the accepted predecessors leave precisely this stalled hard proof; Sol-level endpoint formulas and the high coordinator's existing coarse bounds do not control absolute-value transitions at the small measured margin scale. A fitted remainder is disallowed. This is the handoff's named hard-example exception, not ultra-throughout: N2/N4/N5/N6 use Sol xhigh and N3 uses Sol medium. If no decisive all-degree lemma emerges, retain its exact obstruction and apply the progress/two-empty-round rule.

## 2026-11-05 — B1 finite map complete; all six directions launched

- Sol-medium B1 worker completed all7 prescribed degrees in118.42 summed per-degree wall seconds, with1672 direct-polynomial formula comparisons (max lambda difference7.99e-15,S difference3.73e-14,projected-bound residual7.33e-15). These are floating residuals, not rigorous error bounds or independent replay.
- Parent independently rehashed every source/raw object, parsed18641 raw rows and verified finite floating values and exact row totals:12474 selected-center far,1127 all-center near-projection,5040 corner-shell; near enumeration covers10989153 center-phase pairs. No extra scientific run was claimed.
- [B1 map](margin-anatomy.md), [receipt](evidence/b1-margins.json). Sampled far S margins grow .00604→.01594; conservative near analytic budget at n48 is4.42e-5 and at256 is1.05e-4. The sharper sampled projected comparison remains .5744→.5516. Expanded sub-.01 phases recover positive S excess at128/256 that older grids missed. Continuous extrema remain OPEN; tiny-shell signs at1e-13 cancellation scale are unresolved.
- B0 PASS and B1 finite map completed before parallel launch. N1 requested Astra ultra (justification above); N2,N4,N5,N6 requested Sol xhigh; N3 requested Sol medium. Each owns separate attempt/gate/idea/theory/code/evidence paths; only root changes shared files/Git. No independent reviewer is a developer self-approval. First-round checkpoint30min, progress-driven continuation with at most15 rounds per direction and two-empty-round stop.
- N3 also attempts native exact n33/34 extension while improving the phase cover. Any new finite proof waits for a different worker's independently executed checker acceptance and committed evidence.

## 2026-11-05 — N6 round1 development boundary and exact finite candidates

- N6 (requested Sol xhigh) completed its precise gate and exact n2 test. The covering family Γ_s(t)=(cos((n+1)t+s),cos(nt+s)) is routine inherited-identity verification, not a new PD-T. The specified fixed-t comparison against s=0/pi is refuted at n2,t=s=pi/4 with exact gap(5sqrt(2)-7)/6>0. [Scoped negative proof](theory/N6-two-trace-obstruction.md), [candidate](ideas/N6-two-trace.md), [attempt](attempts/N6.md), exact developer receipt/code. Independent supplementary review and Claude audit pending. This is no counterexample to PD-T099.
- Round1 progress is a new exact gate narrowing the parallel-family route. Round2's positive-mixture application is not started; the generic variance theorem belongs to N4 to avoid duplicate substantive IDs. Parent publishes this boundary before further N6 development.
- N3 generated exact complete native candidates n33(8141bytes,286leaves) and n34(8253bytes,290leaves). Small essential certificates retained as evidence/n33.json.gz and evidence/n34.json.gz. Producer accepted=false is unchanged. A fresh DISTINCT Astrahigh checker now independently executes the frozen C++/GMP replay and corruption controls; neither degree is counted until actual acceptance is committed.
- N3's first-order whole-sum floating model completes n33(2796visited,16.37CPU-s) and n64(3634visited,92.97CPU-s); n128 remains running. These developer checkpoints are MEASURED, not outward certificates or a complete three-degree B2 growth verdict. Frozen final run receipt follows after the schedule completes.
- [Local storage inventory](COLD_STORAGE.md): first33 B0/B1 working files rehashed; no Windows delivery or durable retention claimed. New finite certificates are committed small essential evidence, not bulk archive claims.
