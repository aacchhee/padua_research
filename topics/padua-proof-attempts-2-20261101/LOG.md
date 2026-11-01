# Second proof attempts on programme-ideas open targets

- Branch: `codex/padua-proof-attempts-2-20261101` · Base: `a09d910ae7d5526b1e216066421a0bee7fc20da4` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh), PENDING.
- Stage: WORK · Next: `Codex (gpt-6.1-sol xhigh): Continue codex/padua-proof-attempts-2-20261101.`
- Claims: no new result yet; A2 active, A5/A4(a)/B3/B1 not started.
- PR: draft against `codex/padua-proof-attempts-20261101`; additions under this topic only. Local IDs only; proposed upstream edits remain literal proposals.
- Open for AC: no development approval needed; Claude audit is a later handoff.

## 2026-11-01 — Codex orchestration

- Rules read in full at branch head `a09d910ae7d5526b1e216066421a0bee7fc20da4`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`. Initially read at clean checkout `07c5f5465d6de306aa81dbe8ca1f615295163864`, then re-read after creating requested branch from part 1.
- Pinned heads: part 1 `a09d910ae7d5526b1e216066421a0bee7fc20da4`; current main `9739a0c56b7a3976422ce60a8441bfbbfd6554df`; programme PR #6 `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; Lanczos `a2dd845b8a231e1b00733e1361e2a9ad3bad222f` (read required local ID 304(a) at this revision).
- Commands: fetched all four branch heads with explicit supported network permission, then `git switch -c codex/padua-proof-attempts-2-20261101 a09d910ae7d5526b1e216066421a0bee7fc20da4`. Default sandbox fetch failed to connect to session proxy; explicit network permission succeeded. Runtime and networking skill read; enforced policy inspected, no proxy override or credential disclosure.
- User allocation: mathematics `gpt-6.1-sol xhigh`; mechanical/code work `gpt-6.1-sol medium`. Root runtime-resolved model/effort is not separately exposed; root does orchestration/integration and discloses this rather than inventing metadata. Spawned development allocations are explicit. No ultra allocation.
- `/root/a2_develop`: `gpt-6.1-sol xhigh`, mathematical A2 development. Owns only new attempt A2, theory IDs 01–04, code/output prefixes a2_. Full-paper reading and target-specific registry gate precede borrowed methods and proof attempts.
- `/root/input_manifest`: `gpt-6.1-sol medium`, mechanical input review/gate receipts and manifest generator. Owns only inputs-review.md, code/evidence_manifest.py and evidence-manifest.json. Root alone controls Git and LOG/plan/shared records.
- Part 1 results are PROVED with audit PENDING. Dependencies must use `PD-T?proof-attempts-codex-0N (audit pending)`. Refresh upstream at boundaries and during sustained development; if Claude findings land, stop dependent work, record impact, adapt, and merge only when a depended-on rule/input changed. Never rebase or rewrite published history.
- Pre-run ordering/kill criteria: [plan.md](plan.md). A2 starts first. Subsequent targets start only after its stop. Independent subagent reruns supplement, and do not replace, Claude audit.
- Input drift assessment and complete blob-pinned file list: inputs-review.md and evidence-manifest.json (being prepared). No upstream/main merge performed.
- Latest pushed checkpoint: none yet.

## Runs needed

- Required independent Claude audit at final development head: `Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-2-20261101.`
- No bridge to AC's computer is exposed. Intended local working-track file: `C:\Users\andreyac\Downloads\padua\results\padua-proof-attempts-2-20261101.md`. Intended entry will contain pinned rules/heads, each final target status, proof/evidence paths, draft PR link, commands and audit prompt. This is an intended entry, not a performed write. Never write RESULTS.md or another topic's file.
- Required large evidence, if any, stays in local working storage until AC's Padua cold-storage destination is available; manifest SHA-256, size, command and checker output. Committed outputs ≤1 MB each and ≤5 MB total.

### Input-change trigger and integration impact (before merge)

- Inspection of `git diff a09d910..9bd14a6 -- topics/programme-ideas-20261031/OPEN_TARGETS.md topics/programme-ideas-20261031/checks/decisive-gen4-2.md` confirms depended-on inputs changed since part 1's programme pin. A2 now explicitly inherits only the global upper bound; B1 fixes injectivity, nonvanishing poles and general position; A4 distinguishes neighbourhood/global obligations; B3 fixes the reference class, positive boundary gap and fixed-n,p negative family. The decisive record corrects legacy certification wording. This meets AC's explicit merge exception, so merge the pinned programme head, not main. Rules are unchanged between branch base and this head.
- Impact: develop against the corrected target statements already supplied by AC. No part1 code/output/proof is changed by this integration; part1's audit remains pending. New scientific writes remain topic-local. Imported upstream changes are inherited by merge, not edits to upstream files by this topic. No rebase or published-history rewrite.

### Part1 audit arrival — dependent work paused and impact assessed

- During draft PR creation GitHub reported part1 base advanced to `95279b833bca5967fcf47c1b71a56ff622185b4e`. Fetched the head immediately and stopped A1-dependent A2 development before continuing. Read its full `audit-01.md`.
- Claude (configured claude-opus-5-5 xhigh) accepts all three PROVED statements and B1 OPEN, with F1–F5 minor record/wording findings and F6 protocol notes. Part1 response dispositions are not yet present. No proof/checker/status change is requested.
- Impact: A1 formula used by A2 is accepted without a gap. No mathematical adaptation to it is needed. A5's future completeness checklist explicitly includes rigorous (D) corner and (E) edge-node handlers from `t3_degenerate.py` (F2); part1 theorem03 covers only the `degenerate_max` path, not those handlers. F3 separates MEASURED trace coverage from the local theorem statement. B5 evidence phrasing (F1) is not a part2 dependency. Upstream proposal/registry findings F4/F5/F6 are not fixed by editing part1 here; our proposals must retain routes/history and explicit pending registry items.
- Dependencies retain AC's requested literal `PD-T?proof-attempts-codex-0N (audit pending)` for consistency, with this dated qualification: audit-01 at `95279b8` has ACCEPTED the proofs, minor dispositions remain pending upstream. This label does not deny that the audit was performed.
- The arrived audit is a changed authoritative part1 input; merge pinned `95279b8` under the same explicit integration exception. New topic files remain the only authored changes; no part1 file is edited here.
- Draft PR [#12](https://github.com/aacchhee/padua_research/pull/12) opened against part1 and attached to this chat. Initial pushed head `b3c333b6519740c21953ed41501a66d37768c1f2`; pending audit integration resolves its temporary base divergence.

### A2 source-reading checkpoint

- The A2 developer completed its target-specific relaxed gate, full Kolomoitsev–Lomako paper reading and bounded Bos2006 primary theorem reading; exact locators and failed shell-download limitation are recorded in attempts/T-A2.md. A2 remains OPEN while deriving a positive node-angle sum and uniform comparison bounds.
- Mechanical input support saved 157 immutable Git-object input identities: original part1 scientific files/rules, newly arrived audit/support, programme inputs and comparison versions, and the Lanczos prerequisite. See inputs-review.md and evidence-manifest.json. No scientific execution is implied by hashing sources.
- `/root/a2_independent_route`: gpt-6.1-sol xhigh, supplementary read-only derivation/check of the node-angle sum and possible one-dimensional comparison; no Git authority, no other target work. May write only own code/output prefixes a2ind_ if a consequential run is needed, which then requires a separate actual rerun.
- Latest pushed checkpoint: `818ca4ad0942eb4743860f913a299ff30d959dae`; draft PR12 remains WORK with AUDIT PENDING. New source-reading checkpoint follows. No counts, asymptotic coefficient or global argmax is claimed.
