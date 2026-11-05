# Audit-02 family report — EVD (L7 platform scope, compact G1, n1 recipe, storage, manifest, G0/G4 notes)

Subagent auditor: Claude Opus 5.5, effort high, working under the Claude audit-02 orchestrator. The orchestrator saved this report from the subagent's returned text. Scripts and receipts are in [code/R-EVD/](code/R-EVD/); `g1_compact_check.py` there is an unmodified scratch copy of the committed checker.

- **HEAD:** `2473ab5`.
- **Rules:** unchanged since `3f1e74c`: AGENTS `c44a76f1…`, WORKFLOW `423e1bc0…`, CLAUDE_ROLES `7d7fd30a…`.
- **Git state:** no changes. Scripts ran on a `git archive HEAD` copy, with two exceptions run in the repository itself: the read-only verify mode of `check_manifest.py`, and the n1 recipe, which writes only to scratch. `git status --porcelain` was empty before and after both.

**Verdict: ACCEPT WITH MINOR FINDINGS.** Four NOTEs; none needs Codex rework.

## Scope (D = `topics/padua-lanczos-frontier-20261105`)

**Records (sha256 prefix):**
- handoffs/08-reaudit.md `4541b9d2`, response-01.md `025330ae`
- the relevant sections of audit-01.md `63b3ed82`, audit-01/PROT.md §2.3/§3 and audit-01/L7G1.md
- evidence-response-01.md `64486137`, COLD_STORAGE.md `e12ff664`, l7-suite-methods.md `763de489`, l6-n1-methods.md `b7270b21`
- theory/l7-natural-suite-measurements.md `a9332d2f`, theory/g1-finite-growth-measurements.md `bbe0398e`
- g1-fit-methods.md `a98281ff`, g1-fit-spec.md (full)
- g0-disposition-02.md `f8b8f9a2`, g4-disposition-04.md `49eb65ad`

**Code:** g1_compact_check.py `902f6a30`, build_response_evidence.py `90e2fc6c`, response_evidence_check.py `7af1dd0e`, numerical_environment.py `38e77399`, storage_response_inventory.py `714ffab8`, and check_manifest.py `5943a4a7` (unchanged).

**Evidence:** g1-compact-triangle.json `2c99758e`, g1-compact-rotated.json `e52d8ac8`, l7-full-loss-list.json `67483375`, l7-cross-group.json `76105dcf`, response-n1-recheck.json `c683aaf8`, response-evidence-check.json `ef78ec0b`, response-numerical-environment.json `853db3d6`, cold-storage-response-01.json `524e9ae4`, evidence-manifest.json `e204a146`.

**Comparison sources:** g1-fit-actual.json, l7-suite-summary.json, and audit-01/code/L7G1/compare-l7run_haswell.txt.

**Not read:** gate-timing (GATE report), the substance of registry-proposals (TXT report; OLD blocks were checked here only mechanically), and the L1–L6 theory changes.

## Items

### Item 2 / A-M2 — RESOLVED

**What the response added:**
- addendum `theory/l7-natural-suite-measurements.md:87–97`;
- recipe rule `l7-suite-methods.md:31–35`, setting `OPENBLAS_CORETYPE=Haswell OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` before NumPy is imported, with a fresh `--output-dir`;
- COLD_STORAGE bullets.

**Text checks:**
- It discloses default AVX-512 18 cells / 9 directions against Haswell 20 / 6, and keeps MEASURED.
- The robust features listed match audit-01 L7G1, including the span-gap ranking.
- Historical CPU/ISA/glibc are stated as uncaptured. The EPYC 7763 observation is labelled current and separate.
- The grouping is labelled post-registration, with 12 directions over 45 pairs.

**Loss list (`l7-full-loss-list.json`):**
- All 20 rows match the audit's independent Haswell rerun in key, order and 4-significant-figure values.
- They also match the summary's three truncated rows and its counts.
- Aggregate and aggregator pins equal the summary's: `a878a041…` and `e6fe8582…`.

**Cross-group file (`l7-cross-group.json`):**
- All six directions match the audit's Haswell cross-group lines, after inverting the full/window orientation.
- Worker pins equal `worker_json_manifest`.
- 6 full × 4 window = 24 cross pairs, × 64 paired cells = 1536 comparisons.
- Limitation: raw workers for the non-triangle comparisons are gone, so only the triangle part is independently confirmed.

### Item 6 / A-m7 compact G1 — RESOLVED

**Format.**
- Each table has 76 rows in exact (degree, rule) order and is under 16 KiB (9585 and 9692 bytes).
- Pins for the source manifest, report and frozen g1_fit.py are asserted.

**Outward conversion.**
- The conversion uses the frozen 144-bit outward `logq`, halved and scaled by 10^15, with floor on the lower end and ceil on the upper end.
- T24 was checked independently with mpmath at 400 bits ([t24x.py](code/R-EVD/t24x.py)). The inputs were the audit-01 regenerated T24 endpoint files, whose hashes equal the compact `source_cases` pins (bj `d4791cee…`, mirror `c419a417…`, alt `38008a9c…`, pivot `99833b7e…`).
- All 152 values are enclosed, and each integer pair is exactly floor/ceil of the true value.
- rotQ24 has no raw rows here. Its decisive and early intervals enclose the committed 128-bit receipt intervals.

**Logical implication — valid.**
- The checker forms A_s ⊇ {exact a_s} and B_s ⊇ {exact b_s}. Interval minima enclose the exact comparator minimum.
- It then encloses the value at the exact original-box point y_s = (1−τ_s)a_s + τ_s b_s, with τ ∈ {0, ½, 1}.
- It requires the lower end of that enclosure to be > 0. This certifies g·y > 0 at an admissible point of the original endpoint-defined box. It never evaluates a corner of the enlarged rounded box, so outward rounding is the correct direction.
- τ equals the receipt's witness: 1,1,1,1,½,0×9,1×5.

**Margins.**
- late − early/2: T24 ≥ 1.0612479320 and rotQ24 ≥ 0.9516634588, consistent with ">1.06124" and ">0.95166".
- Early minima are 0.59409 and 0.17068.
- Receipt midpoint lower bounds are 93.8078335825 and 50.3543980. So ">93.80/>50.35" is valid, and 93.81 would not be a valid strict lower bound. Audit-01's "≥ 93.81" was the imprecise one.

**Wording.**
- NOT_NEEDED is kept as execution history.
- The original verifier's early-clause scope (g1-fit-methods.md:51) is preserved, and the new early check is labelled a developer compact recheck.

### Item 7 / n1 recipe and storage — RESOLVED (NOTE R2-EVD-2)

- The recipe was executed verbatim into a mktemp scratch directory:
  - PASS, 367 operations;
  - `full_residual_64u_budget_pass` true;
  - raw INCONSISTENT;
  - five rejected controls.
- `independent-analysis.json` (`f0a19220…`) and `independent-trace.json` (`b7a68f20…`) are identical to both the committed response receipt and the original `l6-n1-independent.json`.
- It wrote seven files, all in scratch. These plus four packaging-replay files explain the eleven identities.
- Source `269dfb1e…`, the three inputs and the original receipt `51216448…` are unchanged.
- `cold-storage-response-01.json` says `LOCAL_ONLY_NOT_DELIVERED`, and remote retrievability is not overclaimed. `--check` cannot run here because the /tmp inventory is gone, as documented.

### Item 8 / A-m8 — RESOLVED

- `check_manifest.py` verify mode: PASS, 330 files, 0.15 s. The manifest mtime and size are unchanged, so the verify branch writes nothing.
- An independent `git ls-files` count is also 330, including all 82 tracked audit-01 files. C1 had 328; the two additions are response-01 and the supplementary report.
- No audit-01 file changed. Among handoffs, only 07's status line changed, plus the new 08.
- `code/` and `evidence/` received only additions.
- All 132 tracked topic JSON files parse and are under 16 KiB (710,703 B total).
- `git diff --check 45646d7 HEAD` exits 0.
- Of 576 relative links in the changed Markdown, 425 resolve. The other 149 sit in fenced or quoted literal registry blocks and are relative to the target registry, so none is broken in prose.
- Main is now `9322fba` (PR25), not merged. All 22 non-append literal OLD blocks still match the `9322fba` bytes. PR25 assigns T364–370, N132 and IDEA454–461, with no overlap with this topic's ranges. A reservation refresh is still required.

### PROT-1 G0/G4 notes — RESOLVED

- The notes are additive, and the original FAIL and dispositions are preserved.
- They accurately report:
  - all 12 own-method gaps (G0 T24/n12; G4 rotpi4/n24 and triangle/n20);
  - frozen code `8359bf7`, an Intel Xeon AVX-512 host, the SkylakeX kernel, and the orchestrator rerun;
  - 0.85u residuals and amplification 4.03e3;
  - own methods only, upstream_xy not rerun, historical Q unavailable.
- Recomputed Haswell relative differences, 7.9e-8 (dev) and 6.6e-5 (alt), match "~8e-8 / 7e-5".

**`numerical_environment.py`** records:
- CPU vendor, model and flags; platform and libc;
- Python, NumPy and SciPy versions;
- the loaded BLAS for both clients via threadpoolctl (architecture, version, threads);
- SIMD support and the CPU/thread environment variables.

Its receipt shows an AMD EPYC 7763 without AVX-512, glibc 2.41, NumPy 2.3.5 / SciPy 1.17.0, and OpenBLAS 0.3.30 Haswell on 1 thread. The collector hash matches.

## Executions (own)

| # | Run | Exit | Time | Result |
|---|---|---|---|---|
| 1 | `python3 -B head/D/code/g1_compact_check.py` (Python 3.13.18) | 0 | 0.04 s | PASS; both INCONCLUSIVE ([g1cc.json](code/R-EVD/g1cc.json), `f092c108…`) |
| 2 | mpmath T24 enclosure, [t24x.py](code/R-EVD/t24x.py) | 0 | — | 152/152 enclosed and tight |
| 3 | `response_evidence_check.py` in a scratch copy ([local variant](code/R-EVD/response_evidence_check_local.py)) | 0 | — | checks, status, scope and controls identical to committed `response-evidence-check.json` ([rec-out.json](code/R-EVD/rec-out.json)) |
| 4 | n1 recipe verbatim (`timeout 60s python3 -I -B …l6_n1_independent.py`) | 0 | 0.109 s | as in item 7 |
| 5 | `python3 -B D/code/check_manifest.py` | 0 | 0.15 s | PASS 330 |
| 6 | L7 triangle rerun under the new recipe | 0 | 37.3 s | 20 / 6; comparison byte-identical |
| — | Scratch checks: L7 rows and cross-group ([l7check.py](code/R-EVD/l7check.py), [xg.py](code/R-EVD/xg.py)), receipt overlap ([g1x.py](code/R-EVD/g1x.py)), JSON and links ([jl.py](code/R-EVD/jl.py), [jl2.py](code/R-EVD/jl2.py)), OLD blocks vs `330fab8`/`9322fba` ([old.py](code/R-EVD/old.py)) | — | — | as reported above |

Notes on the runs:
- **Run 3.** The scratch copy turns the `/tmp/padua-response-packaging-replay` identity step into a no-op, because that replay is gone. The four-file byte replay was therefore not independently confirmed. The enclosure, SSE and corruption-control checks did run.
- **Run 6.**
  - Command: `OPENBLAS_CORETYPE=Haswell OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=<scratch>/deps312 python3.12 -B head/D/code/l7_natural.py --external <scratch>/polyrat --output-dir <scratch>/l7h/tri --domains triangle`.
  - A first attempt with the wrong `--external` path exited 1.
  - Metadata: producer `ba2beac1…`, NumPy 2.3.5, SciPy 1.17.0, polyrat hashes pinned.
  - audit-01's `l7_compare.py` on the output is byte-identical to `audit-01/code/L7G1/compare-l7run_haswell.txt` ([compare.txt](code/R-EVD/compare.txt)): count 20, 0/480 flag mismatches, 6 same-group plus 6 cross-group directions.
  - All 43 raw arrays per seed equal the audit-01 Haswell run array-for-array.
  - So the new recipe reproduces 20/6 on this AVX-512 host.

## Findings

**R2-EVD-1 (NOTE; a defect of Claude audit-01, not of Codex)**
- *Problem:* `.gitignore:23` (`*.log`) kept all 16 audit-01 `.log` files (25,193 B) out of Git. Five of them are linked from audit-01 reports:
  - L2.md → `code/L2/tri_all.log`, `rot_node1.log`;
  - L7G1.md → `code/L7G1/l7run_haswell.log`, `runA.log`, `runB.log`.
- *Coverage gap:* the manifest and the supplementary "83 audit files" correctly cover only tracked files, and nobody noticed the gap.
- *Remedy:* disclose in audit-02; preserve copies under audit-02 with a non-ignored suffix; avoid `.log` names for audit-02 outputs. *Orchestrator action:* done in `71131b2`. See audit-02.md.

**R2-EVD-2 (NOTE).** `l6-n1-methods.md:52` still says "not executed as another scientific run in this response" and does not link `evidence/response-n1-recheck.json`. The root execution is recorded in COLD_STORAGE.md:253, response-01.md:83 and the LOG. Add a pointer (same as R2-TXT-5).

**R2-EVD-3 (NOTE).** `response-numerical-environment.json` was collected with `OPENBLAS_CORETYPE=Haswell` forced, as its `environment` field shows. Nothing is overclaimed. Future receipts could record both the default and the forced dispatch.

**R2-EVD-4 (NOTE).**
- Only `g1_compact_check.py` is repository-only. `response_evidence_check.py` and `storage_response_inventory.py --check` depend on /tmp artefacts, as disclosed.
- `storage_response_inventory.py` without `--check` rewrites the committed `cold-storage-response-01.json` in place. That is builder behaviour, but worth stating near the recipe.
