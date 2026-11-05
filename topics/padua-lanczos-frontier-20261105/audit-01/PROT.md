# Audit-01 family report — PROT (protocol, novelty gate, G0/G4, IDs, storage)

**Auditor.** Subagent Claude Opus 5.5 (`claude-opus-5-5`), effort xhigh, working under the Claude audit-01 orchestrator. The orchestrator saved this report from the subagent's returned text.

**Files.** The auditor's scripts and receipts are in [code/PROT/](code/PROT/). The orchestrator's own confirming rerun is in [code/ORCH/](code/ORCH/), described in §3(a′).

**Audited content and rules.**
- Topic files at `3a179f6`. The only diff from `9525165` to `3a179f6` is handoff05's status line plus handoff06.
- The orchestrator's later commits `6f10e90` and `763bb9e` contain only `audit-01/**` and are outside the candidate.
- Rules read at `3a179f6`; they are identical to main `330fab8`.
- No Git changes and no repository writes.

**Verdict: FINDINGS REQUIRE WORK** — record and protocol remediation only:
- one MAJOR finding (PROT-3);
- MINOR findings PROT-2 and PROT-4 to PROT-10, all to fix before PR readiness.

## 1. Scope (D = `topics/padua-lanczos-frontier-20261105`)

**Read in full**
- Rules and templates: AGENTS.md, WORKFLOW.md, CLAUDE_ROLES.md; templates IDEA, TOPIC_LOG and HANDOFF; the tools/cold_storage.py header.
- **`state/IDEAS.md`, complete (lines 1–974)**, including every obstruction and disposition table.
  - It is identical at `aff30e8` and at `3a179f6`.
  - The delta to main `330fab8` is PR26's IDEA-466–471, unrelated MZ-cleanup ideas.
- Topic records:
  - D/LOG.md and handoffs 01–06;
  - plan, gates, report, proposed-record-changes, ALLOCATIONS and the results file;
  - all eight ideas-*.md files and attempts/L1–L7.
- G0/G4 records:
  - g0-disposition-02, g0-attribution-methods, independent-checks-g0, independent-checks-g0-resolution, g4-disposition-04 and g4-methods;
  - g0_attribution.py in full;
  - every g0-*/g4-* JSON receipt.
- Other records: l5-03; g1-extended-pilot and g1-remaining-scan.
- Storage files: the three cold-storage*.json indices, evidence-manifest.json and check_manifest.py.
- Reservation ledgers: all eight ALLOCATIONS.md files on main; PR25's ledger at `22e8540` (read-only GitHub API); the cleanup topic's reservation-check.md; PR21's ledger.

**Read in part**
- The headers (title, ID, aliases, split lines, status tables, scope) of all 20 theory files, and the statement/scope sections of l4-N01, l6-N01 and l6-N02.
- The cap/guard passages of g1-batching and g1-optimization.
- COLD_STORAGE.md: the first 60 lines and the layout section.
- literature/INDEX.md: the header and rows LIT-089/090/098, 241–243, 249, 260–263, 280–284 and 360–364.
- The PR21 P3 memo, blob `4741c38943f37ae05ba525552ceafc3f32ac5537`. It is identical at the local pin `890f56c` and at the current head `67b3e01`.
- Inherited sources: the E1 T24 degree-12 endpoints (drift e1-summary.md), the PD-T139 record, and the rule definitions in e1_exact.py, e6_benchmark.py and l2_core.py.

**Not read:** theory proof bodies (other families), the non-G0 independent-check reports, the G1/G2/G3/L4/L6/L7 code, PR21 addenda and CODEX.md.

**Hashes.**
- The SHA-256 of all 83 audited files is in [code/PROT/sha256.txt](code/PROT/sha256.txt).
- Hashes quoted inside the records were spot-checked and match the committed bytes. Examples: the l4-independent, l6-n1 and g0/g1/g4 code and receipts.
- The packed L6 trace decompresses to 69,921 B with the claimed SHA `c3f9950d…`.

## 2. Independent reconstruction

### 2.1 Novelty gate and candidate discipline

Every considered candidate is preserved, with a closest-prior field, a separation criterion and a pre-written kill test.

| Provisional ID | Mechanism | Closest prior (ledger) | Disposition at `3a179f6` |
|---|---|---|---|
| IDEA?…-l1-01 | G1 scan | IDEA-246/248/250; PD-T136/137/139; IDEA-140 | continuation. G1 is INCONCLUSIVE, not yet written back (PROT-6) |
| IDEA?…-l1-02 | SH_n family | IDEA-133/136/137/140/246/248; PD-T033/035/036/038/039/041/044; IDEA-286 (terminology, unrelated) | variant → PROVED as L1a |
| IDEA?…-l1-03 | scalar activation on SH_n | IDEA-249/250; PD-T138/140/141 | deferred, with a resume condition |
| IDEA?…-l2-01/02 | W/R formal readings | IDEA-253–256; PD-T055; PD-N062; PD-T136/137/053; IDEA-141–144/249/250; PD-T042/043 | formalization variants of IDEA-255 → PROVED (L2-01…05) |
| IDEA?…-l2-03 | F, fixed binary64 | IDEA-253/263; PD-T146 | deferred |
| IDEA-253 reading | every-error reading | — | duplicate; not pursued; no PD-N |
| IDEA?…-L3a/L3b | explicit finite-u radius / adaptive finite union | IDEA-251/252; PD-T142/143/046/054; PD-N062; IDEA-151 | quantitative variant / corollary → PROVED as L3-01 |
| IDEA?…-L4a | full-scalar positive-envelope upper | IDEA-246/249/250; PD-T136–141 | old-lower subroute REJECTED: failed (PD-N L4-01); the upper is kept |
| IDEA?…-L4b | full-output same-sign witness | IDEA-250; PD-T138/141 | variant → part of PROVED PD-T L4a |
| IDEA?…-L5-01/02/03 | full-kernel positive span / square covering / inference from ρ_n | IDEA-156/157/168/257; PD-T058/059/065/069/075/144; PD-N020/022/063 | variant (L5a–d PROVED) / deferred / abandoned duplicate inference |
| IDEA?…-L6-01 | complete-square residual barrier | IDEA-106 (credited); IDEA-157/161/258/262; PD-T060/070/145 | PROVED (L6-01) plus scoped PD-N |
| IDEA?…-L6-02 | frozen actual n1 contract | IDEA-262 | duplicate-as-mechanism; it is IDEA-262's contract. The raw branch is REJECTED: refuted (PD-N L6-02); the broader target stays deferred |
| abandoned L6 inferences | u=e; compression; transfer (E)→(G) | IDEA-158/160/162/262; PD-N020/022/023 | abandoned; no PD-N |
| IDEA?frontier-l7-01…04 | empirical questions (the gate is inapplicable, as stated) | IDEA-263–267; PD-T051/146; PD-N015 | 01–02 are now MEASURED (not written back); 03–04 deferred |

**Result of the full IDEAS.md read**
- No existing IDEA duplicates a mechanism pursued as new. Every pursued candidate is a variant or a continuation.
- The topic makes no novelty or priority claim; grep shows only "no … priority claim" disclaimers.
- Omissions from the closest-prior fields are listed in PROT-4. None changes a verdict.
- Dispositions that must be updated at registration (PROT-7):
  - IDEA-248: L1a instantiates it in the aggregate model.
  - IDEA-255: W/R partially resume it, without a realizable error generator.
  - IDEA-262: L6-02 is its contract.

**PD-N records under AC's L5 rule** (a scoped, refuted or failed mechanism with its own negative statement, status and evidence):
- **l4-N01 complies.**
  - Failed mechanism: fixed old BJ lower G_R × any upper on λ_max of the absolute envelope.
  - Statement: λ_max(C) ≥ 13462955378 and G_R ≤ 100·13462955378.
  - Status: PROVED, finite computer-assisted. The true capacity and stronger lower bounds are excluded.
- **l6-N01 complies.**
  - Refuted mechanism: an unbounded-e/u realization with a near-orthogonal square Q and two complete O(u) residuals.
  - Status: PROVED, as a one-line corollary of l6-01(3).
- **l6-N02 complies.**
  - Refuted mechanism: reading the 14 raw slots directly as exact orthonormal sections, with exact witness 2^-55.
  - It carries little science but is not administrative.
- No PD-N was created for an equivalence, abandonment or deferral.

**Priority wording.** report.md:94 cites the "pinned PR21 (unmerged) P3 comparison and its stated reading limits".
- Memo row 14: "no matching result found in the documented search" for PD-T136/137/141.
- Memo row 15: names Barrio–Peña–Sauer Remark 9 as closer prior art for PD-T142/143.
- Coverage is bounded, and nothing in the topic exceeds this evidence.
- The per-result wording that handoff01 required is missing (PROT-9).

### 2.2 Prospective novelty-gate timing deviation (facts)

**When the drafts entered Git**
- The workers read rules at `8359bf7`.
- The reservation commit `40b3eb6` (09:54:24Z) contains no candidates.
- **All pre-gate drafts first enter Git together in `0574c47` (10:05:00Z), the G0-stop commit.** Git cannot order the drafting inside that window.
- The timing therefore rests on the workers' own dated statements, which are consistent and self-incriminating.

**Reading incomplete at drafting time**
- *L1/L2 worker* (ideas-l1-l2.md:13–22):
  - IDEAS heading and table coverage were "not yet certified".
  - Shortlist not read: IDEA-130–144/148/151 and their linked records, IDEA-246–267, PD-N062/063, PD-T138–146, prior audits, PROOF_STATUS rows, PD-T053 and the PR21 addenda.
  - attempts/L1.md:68: "considered the shear family while G0 was still running".
- *L3/L4 worker* (ideas-l3-l4.md:9–23, 163–174):
  - summary-row coverage was incomplete;
  - PD-T136/137/139/140 and PD-N013/015/062 were not read in full;
  - PR21 P3 was unread.
- *L5/L6 worker* (ideas-l5-l6.md:7): the IDEA-246–267 shortlist, the PD-N062-linked records and the obstruction tables were unfinished.
- *L7 worker*: declared the generation gate inapplicable to an empirical study. That is permitted and not part of the deviation.

**Drafted before the gate**
- the SH_n family and its transfer equations (attempts/L1.md:11–39);
- the W/R/F formalizations, the R_smooth class, the constants C_n ≥ 2^(n−4), E_n ≥ 2^(n−8), C_12 ≥ 256 and E_12 ≥ 16, and the F predicate (attempts/L2.md:11–79);
- L3a's complete majorant system and final bound (attempts/L3.md:40–106);
- the L4a envelope and test plan, and the L4b idea;
- the L5-01 positive-spanning draft;
- L6-01's identity, with e/6 and e ≤ 48cu;
- the L6-02 idea.

**Claimed results descended from pre-gate drafts** — essentially all of them:
- SH_n → L1a. The raw-chain idea was replaced by a normal witness, and the mirror coefficient was corrected to −4f.
- W/R → L2-01…05, with the constants unchanged.
- **L3a/L3b → L3-01, "without algebraic repair"** (ideas-l3-continuation.md:91; theory/l3:297–300).
- L4a/L4b → PD-T L4a and PD-N L4-01.
- L5-01 → L5a–d.
- L6-01 → L6-01, sharpened to 24√3cu, and PD-N L6-01.
- L6-02 → L6-03 and PD-N L6-02.

**No further development before each gate completed.** Each continuation records a completed gate before deriving:
- L1/L2: checkpoint 4 at rules `684849d` (11:01Z), plus the handoff03 delta gate;
- L3/L4: completion of the reading before the L4 START;
- L3 and L5: the handoff04 gate at `bb67c1e`;
- L6: the handoff05 gate at `9825d18`.

The handoff02 reading continuations did "no derivation".

**Later gate reads found no duplicate pursued as new.** L4b was reclassified as a quantitative variant of an already-recorded witness mechanism. L6-02 was classed "duplicate as a mechanism" and pursued only as IDEA-262's contract.

### 2.3 G0 and G4 dispositions

**The unchanged criterion.** "Any unexplained mismatch stops the campaign until it is explained." G4 is analogous. This is not a bit-identity requirement.

**Re-derivation from committed numbers (G0, T24 n12).** Computed with [g0_amp.py](code/PROT/g0_amp.py):

| Case | Max local residual/u | Relative source ρ | Gap | Gap/ρ | Historical gap | Needed gap/ρ | Certified K range |
|---|---:|---:|---:|---:|---:|---:|---|
| Haswell dev | 1.070 | 2.930e-15 | 2.7559e-10 | 9.41e4 | 2.4812e-10 | 8.47e4 | BJ [1.43e7, 1.04e8] |
| Nehalem dev | 1.082 | 3.166e-15 | 3.2401e-10 | 1.02e5 | 2.4812e-10 | 7.84e4 | BJ same |
| Haswell alt | 1.023 | 1.825e-15 | 1.3022e-12 | 7.13e2 | 7.3010e-12 | 4.00e3 | alt [1.39e5, 5.83e5] |
| Nehalem alt | 0.846 | 1.952e-15 | 3.0241e-12 | 1.55e3 | 7.3010e-12 | 3.74e3 | alt same |

- **Headroom.** The historical values need only about 0.6% (dev) and 2.8% (alt) of the certified worst-case lower capacity.
- **Span movement covers the differences** (using |Δgap| ≤ ‖P₁−P₂‖):
  - dev: the observed kernel span movement of 4.22e-10 covers the historical difference of 2.75e-11;
  - alt: 2.76e-12 (≥ 3.44e-12 with the committed Prescott probe) is of the order of the 6.0e-12 difference.
- **G4** ([g4_cmp.py](code/PROT/g4_cmp.py)):
  - in all 10 class/case pairs, the historical gap's distance to the nearest current sample is below the inter-kernel span movement (ratio 0.03–0.92);
  - local residuals are ≤ 0.756·u·(operation-size sum);
  - the reconstruction defect is ≤ 1.76e-3 of each error.

**Decisive new execution.** The audit host is an Intel Xeon with AVX-512F. The unchanged frozen `8359bf7` code was run for the own methods: `e6_benchmark.reference/metrics` and `L2.run_sel(…, reorth='fullcgs2')` for dev (= upstream_yx entrywise), mirror, alt and adapt.
- Under the default OpenBLAS dispatch (= SkylakeX), and under an explicit `OPENBLAS_CORETYPE=SkylakeX`, **all 12 historical gaps reproduce bit-for-bit**, with all three input hashes matching:

| Case | dev | mirror | alt | adapt |
|---|---|---|---|---|
| T24 n12 | 2.4812027022747904e-10 | 1.3221174301815153e-14 | 7.301022248971358e-12 | 8.656095412273413e-14 |
| rotpi4 n24 | 0.004105469352253462 | 0.9379680454186219 | 2.122043754569406e-08 | 1.8592487265547192e-06 |
| triangle n20 | 0.010163571396223751 | 1.7289700153511147e-07 | 7.602150159701751e-08 | 9.519397852923627e-10 |

- **Residual propagation on the historical (SkylakeX) basis** ([g0_recheck.py](code/PROT/g0_recheck.py), reusing the committed helpers):
  - dev: max residual 1.162u, ρ = 2.975e-15;
  - alt: max residual 0.851u, ρ = 1.812e-15, normal error 7.3011e-12, amplification 4.03e3. This matches the 3.7–4.0e3 predicted from the committed numbers.
  - The 50-digit reference discrepancy is 2.72e-18. The extended-precision gaps are 2.30e-13 (dev) and 2.59e-15 (alt).
- **Inferred historical platform.** The historical receipts evidently came from an AVX-512 host on the OpenBLAS SkylakeX kernel, which the developer's sandbox could not select.

**Decision.** Both explanations discharge the **unchanged** criteria, without any tolerance waiver and without imposing bit-identity:
- the pins leave only the arithmetic environment as a variable;
- controlled kernel changes move the spans by at least the observed differences;
- u-scale residuals reconstruct the errors;
- precision controls suppress the effect;
- reference noise is excluded.

The new execution confirms the cause directly for every own-method row. upstream_xy was not rerun: the pinned polyrat could not be fetched here. **G0 RESOLVED and G4 RESOLVED are accepted.** The limit sentences at g0-disposition-02.md:49–58 and g4-disposition-04.md:11 are superseded by this evidence and should get a dated additive note (PROT-1).

### 2.4 Status/split hygiene (headers only)

| Record | Provisional ID | Status | Comment |
|---|---|---|---|
| l1-01 | …-codex-**L1a** | PROVED analytic | report.md:7 and the proposals use **L1-01** (PROT-5) |
| l2-01…05 | …-L2-01…05 | PROVED (02: finite computer-assisted) | PD-T055 kept OPEN ✓ |
| l3 | …-**L3-01** | PROVED analytic | no Aliases or Split-into lines; ideas-l3-l4.md:85 says L3a; the broader target is called PARTIAL in attempts/L3.md:3 (PROT-3) |
| l4-envelope | …-L4a | PROVED finite computer-assisted | split from the OPEN rotQ24 conjunct of PD-T140; split into l4-N01 ✓ |
| l4-N01 | PD-N …-L4-01 | PROVED | ✓ |
| l5-01…04 | L5a–d | PROVED | U2 OPEN; PD-T075 PARTIAL through (U1) only ✓ |
| l6-01 | …-L6-01 | PROVED | not a conjunct of PD-T056(G); (G) stays OPEN ✓ |
| l6-02 | contract, no ID | "Status: OPEN … unexecuted" | stale after the run; no pointer to l6-03 (PROT-6) |
| l6-03 | …-L6-03 | MEASURED | split into PD-N L6-02 ✓ |
| l6-N01 / N02 | PD-N …-L6-01 / 02 | PROVED | l6-N01:66 still says the contract is "unexecuted" |
| g1-finite-growth | PD-T?lanczos-frontier-**G1-fit** | MEASURED | the ID has no agent component |
| l7 | PD-T?lanczos-frontier-**L7** | MEASURED | the ID has no agent component; the environment lacks the BLAS dispatch |

**Original targets are not silently upgraded** (apart from the L3 PARTIAL wording outside theory/):
- PD-T055 stays OPEN, and PD-T056(G) stays OPEN.
- PD-T075 stays PARTIAL, with U2 OPEN.
- PD-T140's target becomes PROVED only through its two explicit conjuncts: T24 by PD-T141(c) and rotQ24 by L4a. Its experiment stays MEASURED/INCONCLUSIVE.

**No final IDs are assigned.** `git diff origin/main...HEAD --stat` on the six shared registries is empty; the branch touches only D/ and its results file.

**Reservations — no overlap:**

| Range | Owner | Notes |
|---|---|---|
| T294–323 / N104–115 / IDEA384–413 / LIT574–581 | PR23 | merged |
| **T324–363 / N116–131 / IDEA414–453 / LIT582–593** | **PR24** | first published at `40b3eb6`; acknowledged on main (argmax-effective ledger line 44; cleanup reservation-check) |
| T364–375 / N132–137 / IDEA454–465 / LIT594–597 | PR25 (head `22e8540`) | its ledger states the union maxima before it as T363/N131/IDEA453/LIT593 |
| T376–391 / N138–145 / IDEA466–489 | PR26 | merged; T376–381 and IDEA466–471 assigned |
| LIT482–561 | PR21 | ledger blob unchanged at `67b3e01` |

A grep of main's registries and ledgers finds no ID inside PR24's ranges.

### 2.5 Resource and scheduling decisions

- **≤60 s guards.** The ≤60 s BJ14 → 600 s BJ20 conditions were prospective scheduling gates set by the orchestrator (g1-batching.md:42–49).
  - The three failures (170.857 s, 79.050 s, 72.527 s) are preserved.
  - No BJ20 run happened under those gates.
- **1800 s fused-BJ20 successor.**
  - The committed g1-extended-pilot.md equals the run receipt's `prospective_plan` pin (`d3fe7dfd…`).
  - LOG.md:171 is in `86c6846` (17:03:21Z), before the result commit `b81a1a1` (17:24:17Z).
- **Remaining three rules (900 s native / 1800 s producer).**
  - The authorization is LOG.md:181 at `b81a1a1`, before the result commits `b4d741d` and `9525165`.
  - The prefix of g1-remaining-scan.md hashes exactly to the pinned pre-run `7d283a23…`. The outcome was appended, not rewritten.
- **Limits of the Git evidence.**
  - Plans were often first committed together with their results, so Git cannot prove minute-level order.
  - The "original 1800 s ceiling" is a reading of handoff01's "about 30 min" guidance on when to switch to native code, not an explicit cap. This is harmless.
- **No scientific acceptance changed**, and capped runs are reported as INCONCLUSIVE. **Accepted.**

### 2.6 Storage and evidence

- **Manifest.** `check_manifest.py`, run read-only at the audited state, gives PASS for 226 files.
  - At HEAD `763bb9e` it fails because of the new audit-01/ files (PROT-13).
  - [manifest_at_3a179f6.py](code/PROT/manifest_at_3a179f6.py) reconstructs the manifest from the committed `3a179f6` tree and matches: 226 files, 24,051 B, SHA `bfe91443…`.
- **Topic size.**
  - All 95 topic JSON files are ≤ 15,773 B (largest: g1-fast-overlap.json), 567,328 B in total.
  - The topic totals 2,078,665 B in 233 files.
  - Files over 16 KiB are hand-written Markdown or code, not generated outputs.
  - No third-party code, PDF or HTML is committed.
  - The L6 trace is losslessly compressed (zlib + base64, verified), not split.
- **Repository JSON.** 4,138,124 B in 853 files at `3a179f6`; main has 3,712,841 B. After integration it would be about 4.28 MB, within but close to the 5 MB guidance (PROT-15).
- **Missing raw material.** All raw artifacts and the three external inventories (91,574 B, 42,298 B and 90,836 B) are absent here. The indices pin only the inventory hashes and say `LOCAL_ONLY_NOT_DELIVERED` (PROT-10).

### 2.7 LOG, handoffs and commits

- **Handoffs.** Numbered 01–06, with exactly one open (06).
  - Each publication commit changes only the old status line to "done in <output sha>" and adds the next handoff.
  - No handoff body was altered: the diff excluding status lines is empty.
- **Commits.** All 28 commits in origin/main..HEAD at `3a179f6` have a type prefix and Agent/Model trailers, with the metadata disclosure.
- **LOG.** Its header and Runs needed section are stale (PROT-8).

## 3. Executions

**(a) New executions by this auditor**

*Environment.* Intel Xeon @2.10 GHz (fma, avx2, avx512f); Linux 6.18.44; Python 3.13.18; NumPy 2.5.4 (scipy-openblas 0.3.34, DYNAMIC_ARCH, default SkylakeX); SciPy 1.18.1; mpmath 1.3.0; single-threaded.

1. **Snapshot.** `git archive 8359bf7 | tar -x` into scratch: exit 0.
2. **Fetching the pinned polyrat failed.**
   - A curl to codeload.github.com for polyrat `6903d7a` returned a 378-byte JSON access error. It was discarded, and no add_repo or credentials were used.
   - `pip download --no-deps --no-binary :all: polyrat==0.2.2` exited 0; the sdist SHA is `db8844ed…`. pip ran the sdist's setup.py metadata step in an isolated build environment (disclosed).
   - In that sdist, arnoldi.py and version.py match the E6 pins, but index.py and basis.py do not. **It was not used**, so the upstream_xy rows were not rerun.
3. **Manifest checks.** `python3 -I -B D/code/check_manifest.py`:
   - audited state: PASS 226, exit 0, 0.13 s;
   - HEAD `763bb9e`: AssertionError;
   - `manifest_at_3a179f6.py`: MATCH.
4. **g0_recheck.py**, workers for the default, Haswell, Nehalem and SkylakeX kernels: exit 0, 36.5 s; receipt [g0_recheck-receipt.json](code/PROT/g0_recheck-receipt.json).
   - Kernel-pair span distances: dev Haswell–Nehalem 4.217e-10 and alt 2.764e-12, both equal to the developer's values.
   - The default and SkylakeX Q matrices are byte-identical.
5. **legacy_rows.py** ([script](code/PROT/legacy_rows.py)) under each of the four kernels: exit 0, 2–4 s each. [compare_rows.py](code/PROT/compare_rows.py) shows exact reproduction under default and SkylakeX ([receipts](code/PROT/)).
6. **Arithmetic on the committed receipts:** g0_amp.py and g4_cmp.py.
7. **Read-only queries:** git (log, show, diff, blame, ls-tree), sha256sum and size scans. Read-only GitHub API: the open-PR list (21, 24, 25), PR25's ledger and PR21's tree.

**(a′) Orchestrator confirming rerun.** The audit orchestrator ran the subagent's `legacy_rows.py` separately, on a fresh `git archive 8359bf7` snapshot:
- Default kernel: 4 s, exit 0. Haswell: 2 s, exit 0.
- **The receipts are byte-identical to the subagent's**: default `0c605d73…`, Haswell `c8bc76ff…`. See [code/ORCH/](code/ORCH/).
- The default kernel gives the historical T24 dev 2.4812027022747904e-10 and alt 7.301022248971358e-12 exactly.
- One nuance the orchestrator could not confirm: the Haswell own-method gaps (T24 dev 2.7558697116625464e-10, alt 1.3026291901939954e-12) agree with the developer's recorded current values (2.7558694937119657e-10, 1.3027152069570486e-12) only to about 8e-8 and 7e-5 relative. The subagent's "Haswell reproduces the developer's current values" is therefore exact only for the kernel-pair span distances in item 4, not for these gap rows. The likely cause is the developer's different NumPy/SciPy versions (2.3.5/1.17) or the polyrat path. The historical reproduction does not depend on this.

**(b) Reused, review only:** the developer's and Astra's G0/G4 runs and the G1/L4/L6 receipts, through their committed JSON.

**(c) Source inspection only:** check_manifest.py, g0_attribution.py, e6_benchmark.py, l2_core.py, the e1_exact.py rule definitions, and the storage indices.

## 4. Findings

**PROT-1 (NOTE, positive; additive record recommended).**
- *Location:* g0-disposition-02.md:49–58; g4-disposition-04.md:11; independent-checks-g0-resolution.md item 4.
- *Evidence:* the frozen code reproduces all 12 historical own-method G0/G4 gaps bit-for-bit under SkylakeX on an AVX-512 host, and the historical alt row is reconstructed from 0.85u residuals.
- *Remedy:*
  - Add a dated additive note to both dispositions, keeping the original FAIL, the class-level explanation and the developer's limits.
  - Scope the note to the own methods; upstream_xy was not rerun.
  - Record the BLAS dispatch architecture and CPU ISA in all future numerical receipts.

**PROT-2 (MINOR, protocol; disclosed; remediation required at PR preparation) — prospective gate timing.**
- *Location:* LOG.md:38–40; ideas-l1-l2.md:13–22; ideas-l3-l4.md:9–23; ideas-l5-l6.md:7; attempts/L1.md:68; attempts/L3.md:40–44. The facts are in §2.2.
- *Disposition:*
  - The WORKFLOW deviation is confirmed: candidates were generated before the gate.
  - It is not waived, and later reading does not cure it.
  - It has no effect on mathematical validity: the proofs were written or reconstructed after the full gates and are audited separately.
  - No effect on any novelty verdict was found.
  - Once remediated, it does not block readiness by itself. AC decides acceptance, as with the Lebesgue T2/T3 precedent at IDEAS line 923.
- *Remediation:*
  - **R1.** One dated table listing, for each pre-gate candidate: its first commit (`0574c47`), the reads missing at drafting, the gate-completion checkpoint SHA, the post-gate verdict and the resulting claim.
  - **R2.** A timing qualification in every affected IDEA registration and in the History of each descended PD-T/PD-N record. For L3-01, state that its constants were drafted before the gate and survived unchanged.
  - **R3.** Resolve PROT-4.
  - **R4 (process).** Each worker commits its gate checkpoint before drafting any candidate, or labels pre-gate notes as non-candidate brainstorming.

**PROT-3 (MAJOR) — mislabelled status of the broader L3 target.**
- *Location:* attempts/L3.md:3 ("PARTIAL for the broader L3 target") and ideas-l3-continuation.md:123–124 ("PARTIAL/OPEN").
- *Why it is wrong:*
  - PARTIAL requires an explicit decomposition of the target's own statement, with conjuncts PROVED under split IDs.
  - L3-01 proves an explicit positive radius at each fixed degree, explicitly not a usable or degree-uniform one. It is a supporting result, not a conjunct.
  - Handoff01's listed shapes are alternatives.
  - report.md:86 correctly says OPEN.
- *Remedy:* change both passages to OPEN, naming L3-01 as a proved supporting result, and add a history note. No registry proposal may use PARTIAL. (Same issue as L3-1.)

**PROT-4 (MINOR) — closest-entry completeness.**
- *Location:* ideas-l1-l2.md:176–178.
- *Missing entries:*
  - IDEA-130/134 (OPEN all-degree non-product amplification; PD-T035/037/041) for SH_n;
  - IDEA-148/PD-N013 and IDEA-151/PD-N015 (measured failure of reorthogonalization and selection) for W/R.
- No verdict changes, because the observables and models differ.
- *Remedy:* add these entries with one-line separations.

**PROT-5 (MINOR) — provisional-ID hygiene.**
- Inconsistent labels:
  - L1a vs L1-01 (report.md:7 and proposed-record-changes.md:64 vs theory/l1-01:1);
  - L3a vs L3-01 (ideas-l3-l4.md:85).
- Malformed IDs:
  - `PD-T?lanczos-frontier-G1-fit` and `PD-T?lanczos-frontier-L7` have no agent component;
  - `IDEA?frontier-l7-0N`;
  - some local numbers are letters (L1a, L4a, L5a–d);
  - Aliases lines omit the alternative labels.
- Handoff01's slug overrides WORKFLOW's, but it does not excuse the missing agent component or the non-numeric local numbers.
- *Remedy:* one canonical ID per record, all variants listed as aliases, and a complete provisional-to-final map.

**PROT-6 (MINOR) — stale records** that need additive dated updates:
- ideas-l7.md:18–19 and 33–34 still say "NOT RUN".
- ideas-l1-l2.md:175 has no post-G1 disposition.
- attempts/L5.md:65 lacks the n4/n5 outcomes.
- l6-N01:66 says "unexecuted".
- l6-02:1–3 reads "Status: OPEN" on a contract that is not a claim, with no pointer to l6-03.
- ideas-l3-l4.md:85 has the wrong result label.

**PROT-7 (MINOR) — proposals incomplete for preparation.**
- proposed-record-changes.md has only three literal old→new blocks (PD-T140 target, PD-T141, IDEA-250). The handoff03–05 additions are prose, although handoff01 asks for literal blocks.
- Missing:
  - the PD-T055/056/075/143/146 rows;
  - IDEA-248/251/255/262/263–267 disposition updates;
  - about 22 new IDEA rows with aliases;
  - crosswalk and CURRENT entries.
- L6-02 must be registered as a continuation of IDEA-262 (duplicate as a mechanism) and L4b as a variant of IDEA-250 — never as new mechanisms.
- *Remedy:* complete the literal proposals before readiness.

**PROT-8 (MINOR) — LOG hygiene.**
- The header (LOG.md:4–7) still says "Stage: WORK … G1 incomplete … open handoff 05".
- Runs needed (LOG.md:15–17) still says "G3/G4 remain unrun".
- Unexecuted work has no exact command: F, the n4/n5 uppers, n6–8/G3, BNT/Octave, the ZN code, Franke, the fresh-machine recipe, archival delivery and the upstream_xy replays.
- *Remedy:* refresh the header and Runs needed, additively.

**PROT-9 (MINOR) — per-statement priority wording.**
- *Location:* report.md:92–94. Handoff01 required exact dependencies and P3 priority wording for each statement proposed for the paper.
- *Remedy:* state, per statement:
  - P3 row 14 / group C wording for the SH_n, L2 and L4 extensions of PD-T136–141;
  - row 15 (Barrio–Peña–Sauer Remark 9) for L3-01;
  - "PR21 (unmerged)", memo blob `4741c389`, with its coverage limits.

**PROT-10 (MINOR) — retrievability and provenance.**
- *Location:* cold-storage*.json; COLD_STORAGE.md:13–15; theory/g1-finite-growth-measurements.md; theory/l7…:20.
- *Evidence:*
  - Raw artifacts and inventories are not retrievable from a fresh session.
  - G1's 152 exact endpoint rows (about 358 KB in 8 files) and the 1.03 MB fit report are external. Rechecking INCONCLUSIVE therefore needs hours of regeneration.
  - The L7 record omits the BLAS dispatch.
- *Remedy:*
  - Commit a per-degree outward-rounded [a_s, b_s] table under 16 KiB, or deliver the rows to AC's cold storage.
  - State the retrievability limit in COLD_STORAGE.md.
  - Record the dispatch in the L7 record.

**PROT-11 (NOTE).** The resource successors were documented before their runs and are not scientific changes. Accepted.

**PROT-12 (NOTE).** The PD-N records meet the L5 rule.
- Suggested IDEA wording for L6-01: "barrier PROVED; hypothesized unbounded-e/u realization REJECTED: refuted", in place of ideas-l6-continuation.md:79.
- AC may decide whether the light l6-N01 and N02 each merit a separate final PD-N; the rule permits it.

**PROT-13 (NOTE, for the orchestrator).**
- check_manifest fails at HEAD `763bb9e` because of audit-01/.
- At preparation:
  - refresh the reservation union;
  - merge main `330fab8` and delta-read it;
  - exclude audit outputs from the inventory, or regenerate it with provenance.
- Shared-ledger and crosswalk links remain deferred.

**PROT-14 (NOTE).**
- handoffs/03-work.md lacks the Role and Written-by fields.
- Handoff01 is marked "done" although it ended at its G0 stop rule; this is acceptable as recorded in 02.
- ideas-l6-continuation.md:29 cites PR21 without a pinned SHA; the memo is unchanged.

**PROT-15 (NOTE).** Repository JSON is about 4.14 MB now and about 4.28 MB after integration; this topic contributes 0.567 MB. That is within, but close to, the 5 MB guidance.

## 5. Status check

- Theory-header statuses are consistent with WORKFLOW, except the broader-L3 PARTIAL wording (PROT-3).
- Splits are correct, and no original target is silently upgraded.
- Negative statements are correctly scoped.
- G0/G4 RESOLVED are correct and now causally confirmed.
- G1 is INCONCLUSIVE on both grids, G2 PASS, G3 incomplete (its "otherwise" branch not triggered) and G4 RESOLVED; these are recorded consistently.

## 6. Remaining uncertainty and trusted dependencies

- **Gate timing:** the facts rest on the developers' self-reports; Git places all drafts in the single commit `0574c47`.
- **Reproduction:**
  - Trusts NumPy 2.5.4, SciPy 1.18.1 with scipy-openblas 0.3.34 kernels, CPython floats and mpmath.
  - Covers own-method rows only, not polyrat's upstream_xy.
  - No historical Q bytes exist for comparison, but 12 matching 17-digit values are overwhelming evidence.
- **Capacity argument:** uses rounded decimals of the exact inherited endpoints.
- **Reservations:** checked at audit time; PR heads may move.
- **Proofs:** this family verified none; they are covered by the other family reports.
