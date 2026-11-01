# E6P findings: E6, novelty/IDEA coverage, protocol/evidence/provenance

Auditor: Claude Opus 5.5, high effort. Independent auditor, not the developer. I made no change inside the git repository and ran no state-changing git command (only `git fetch origin`, `git ls-remote`, `git show/diff/log`).
Audited branch head: `36c93794ce02f92c76c89e5a9ec8095eb238d91d` (= origin/codex/padua-lanczos-drift-20261101 = refs/pull/15/head). Scientific source: `b09e1db`. Base/main: `806cc7b` (= origin/main at audit time). Rules read at head: AGENTS.md c44a76f1…, agents/WORKFLOW.md 3ac67448…, agents/claude/CLAUDE_ROLES.md 7d7fd30a… (sha256).

## (a) Files read

- **Full `state/IDEAS.md`. I read every line, 1–736, in sequential chunks** (all tables, seeds, MZ/lattice/programme/bivariate sections, OBST-01..15, all obstruction/disposition tables, IDEA-001–209 and the bivariate seeds/IDEA-077–176). sha256 `de45820ecb33f8694b0ed4a13177fc2d91094729dc2f164e3d26034fada4d4a0`, 159295 bytes. Its content is identical at HEAD and at main 806cc7b.
- Campaign files, read in full: handoffs/01-work.md, handoffs/02-audit.md (daa0a5a6…), ideas-e1.md (297e0595…), ideas-e3-e4.md (d0803b35…), ideas-e5.md (cbffb519…), ideas-e6.md (883b485b…), directions/E6.md (d94e442d…), external-code.md (5670ca67…), LOG.md (3b6ca13c…), COLD_STORAGE.md (7019bb47…), theory drift-codex-e6-50 (0c82b965…), e6_benchmark.py (e328b7d5…), e6_smooth.py (de624205…), code/drift/README.md, e6-provenance.json, independent-e6-root.json, archive-receipt.json. I read the following in part: final-validation.json, protocol-check.json, allocation-scan.json, final-recheck-allocation.json, report.md (E6 section), proposed-record-changes.md (E6 blocks), directions/E1.md (gate section), E5.md (grep), theory e1-05 and e5-31 (grep), and the predecessors PD-T042 and PD-T043 (statement sections). I also read the `rule_sel`, `benchmark` and `_rng11_sets` functions of L2/l2_core.py and L1 `rotate`.
- Literature: the relevant rows of literature/INDEX.md (LIT-240–259, 280–285, 360–361). **I did not read the whole INDEX.** I read the old L2 prior-art review (topics/bivariate-lanczos-20261031/reviews/L2-prior-art-01.md) in part, using a grep for the Hokanson/ZN/BNT/selection passages, lines 13–216. Its digest/fulltext limits (WebFetch digest, UNVERIFIED) are preserved below.
- Upstream source, read: polyrat `index.py` and `arnoldi.py` (`_update_rule`, `vandermonde_arnoldi_CGS`, `vandermonde_arnoldi_eval`), plus the imports of `basis.py` and `__init__.py`.

## (b) Commands executed and results

1. `git -C /workspace/padua-drift-external/polyrat rev-parse HEAD` returned `6903d7af…`. `git status --porcelain` was empty. `git ls-remote https://github.com/jeffrey-hokanson/polyrat.git` shows upstream `HEAD` and `refs/heads/master` = `6903d7af9995c9d88e661fb229626696e00fdfba`. `version.py` reads `0.2.2`.
2. `sha256sum polyrat/{arnoldi,index,basis,version}.py` gives e51f3561…, 84df400c…, 9ce50feb…, 1d13b63c…. **All four match external-code.md:10–13.**
3. Python hash check of every e6-provenance.json entry (9 files): all bytes and sha256 match HEAD.
4. Manifest sweep, in-repo entries: e1-manifest 13/13 OK, e1-scalar-manifest 28/28 OK, e5-manifest 5/5 OK, e6-provenance 9/9 OK, final-validation 81/81 OK (bytes and sha256 at HEAD). The off-repo `/workspace/padua-drift-runs/{e1,independent}/…` entries (10 and 36) are **absent in this workspace**.
5. Sizes: evidence/ total 2,009,189 B, max 616,693 B. All 86 branch-added/modified files total 2,725,125 B (this includes ID_CROSSWALK.md at 252 KB, which is not generated). No file exceeds 1 MB. **PASS** (1 MB per file, 5 MB total).
6. `git diff --name-status 806cc7b...HEAD`: 86 files. Outside `topics/padua-lanczos-drift-20261101/` and `tracks/` it touches only `ID_CROSSWALK.md` (+7 lines, a reservation link) and `topics/padua-batch-20261031/ALLOCATIONS.md` (+42 lines: the drift reservation plus the imported MZ section). There are no `.github/`, `state/`, `PROOF_STATUS.md` or `literature/` changes. Under `tracks/bivariate-lanczos/theory`, only the 13 `drift-codex-*` files are added (A). The 77 old theory files at 806cc7b are unchanged. Code adds are own `code/drift/*` only. A grep of the diff for vendored code or PDF markers found nothing.
7. `git fetch origin` (no new objects) and `git ls-remote origin 'refs/pull/*/head'`: PR8 head 6eeec5b is an ancestor of main (merged). Open heads: PR12 b2804ac, PR14 14de1df, PR15 = audited head. PR14's ledger imports the drift block (PD-T136–155, PD-N062–071, IDEA-246–285, LIT-445–459) unchanged, with its own MZ ranges T106–135, N044–061, IDEA210–245, LIT427–444. PR12's diff vs main does not touch PROOF_STATUS/IDEAS/INDEX/CROSSWALK/ledger. **No collision found.** `gh api` was 403 (no repo API access), so open/closed state was inferred from refs and ancestry only.
8. `git log 806cc7b..HEAD`: all 7 commits carry `Agent: Codex` and `Model:` trailers, with "orchestrator exact variant/effort unexposed" disclosed. Author is Andrey Chesnokov. Prefixes are valid. Commit 36c9379 changes only the handoff-01 status line and adds 02, which is correct per WORKFLOW.
9. Orchestrator reruns (not mine; outputs read from `scratchpad/runs/`, Python 3.13.18, numpy 2.3.5): audit-e6-full.json, audit-e6-grids12.json, audit-e6.json and audit-e6-smooth.json. **Every case object is JSON-identical** to the committed e6-benchmarks.json (12/12), e6-frozen-grids12.json (2/2) and e6-smooth.json (12/12). audit-e6-smooth.json is byte-identical (sha 0cc4627e…). The n16 grids were not rerun.
10. **My own independent check**, `scratchpad/audit/E6P/indep_e6_check.py` (sha 5c216563…), output indep_e6_check.json (96c1999a…). Command: `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -W ignore::DeprecationWarning indep_e6_check.py indep_e6_check.json`. It imports no campaign code. It does five things:
    - It regenerates the seed-11 nodes from their written definition. The input sha256 matches the recorded values a356501… (rotpi4) and 806ae0a… (triangle).
    - It calls polyrat `vandermonde_arnoldi_CGS` directly.
    - It compares against my own re-implementations of dev and of reversed-order mirror full CGS2. Max|polyrat[y,x] − own dev| = **0** and max|polyrat[x,y] − own mirror-reversed| = **0** on both sets. This confirms by execution the source reading: polyrat orders each degree (0,t),(1,t−1),…,(t,0), and `_update_rule` takes the smallest array index with a one-step difference. So `[y,x]` gives dev including order, and `[x,y]` gives mirror with the within-degree order reversed.
    - It builds an independent long-double (u≈1.1e-19) CGS3 reference for Π_n: product Legendre in the inverse-rotated frame (κ≈7.8e2) for rotpi4, and my own Koornwinder/Dubiner basis (κ≈1.0e2) for the triangle.
    - Results. Principal-angle gap for polyrat `[y,x]`: **rotpi4 n24 0.004105469352251652** (campaign 0.004105469352253462). **triangle n20 0.010163571396223762** (campaign …751). `[x,y]`: 0.0136183 and 0.0028935, both matching. **The ~4e-3 and ~1e-2 drift reproduces.** Gram: max|QᵀQ−I| = 6.883e-15 is entirely the (0,0) entry; the off-diagonal max is 2.0e-16 (rotpi4) and 2.8e-16 (triangle). Adversarial off-sample relative error at the campaign midpoints is 1.01386e-3 and 1.56943e-3 (reproduced). At 400 uniform random interior points it is **1.08e-3 (rotpi4) and 7.45e-3 (triangle)**. Smooth targets, polyrat `[y,x]`, random interior points:
      - rotpi4 exp(x+y): test 3.6e-14 (reference-span fit 6.5e-16).
      - rotpi4 cos(3x+y)e^{y/2}: train 1.9e-15, test 1.66e-13 (reference 4.6e-15).
      - triangle: all smooth targets ≤2.3e-15 test.
      - 1/(2+x²+0.7xy−y): polyrat and reference errors are equal (approximation-limited).
    - A first attempt with a product-Legendre triangle reference (κ 3.8e14) gave 0.0101638. I discarded it as ill-conditioned; it is retained in the log only.
11. The same polyrat call under the system numpy 2.5.3 (no PYTHONPATH) fails with `TypeError: only 0-dimensional arrays can be converted to Python scalars` in upstream `_update_rule` (`int(np.argwhere(...))`). Upstream polyrat at this pin is incompatible with numpy ≥2.5 (2.3.5 only warns).
12. Workspace inventory: `/workspace/exports/` (the scientific ZIP), `/workspace/padua-drift-runs/{e1,independent,root-independent-e6.json}` and `/workspace/padua-drift-external/chebfun-examples` **do not exist in this audit workspace**. Only polyrat, deps and python-deps are present.

## (c) IDEA coverage table

| Campaign candidate | Overlapping IDEAS entries / records | Disclosed? | Verdict |
|---|---|---|---|
| IDEA?drift-codex-01 normal-quotient span map | IDEA-140/PD-T041, IDEA-148/PD-N013, IDEA-151/PD-T051/N015, PD-T047/050/053–055. Also IDEA-087/088 (Fischer-type first-order conditioning, settled background per AC: different map, nodes/weights→coefficients) | Yes for the main ones. IDEA-087/088 not named | Variant, no novelty claim; adequate (P-F7, low) |
| -02 raw propagator growth | IDEA-140/PD-T041, IDEA-131, PD-N009 | Yes | Correctly marked duplicate/consolidated |
| -03 explicit-family matching theorem | IDEA-140, IDEA-148, PD-T055 | Yes | OPEN/deferred; fine |
| -04 scalar-operation bridge | PD-T041/046/047 named. **Not named:** IDEA-141/PD-T042 (first-order derivative of the coefficient map, coefficient-channel gains), IDEA-142–144/PD-T043 (term-wise and closed-loop dot-product rounding through the coefficient map), IDEA-139 | **Partially; the closest coefficient-error mechanism is undisclosed** | P-F6 (medium) |
| -05 coherent/multinode capacities | IDEA-151, -04, PD-T041 | Yes | Disclosed; record text is stale (P-F8) |
| -10 polynomial-surrogate certificate | IDEA-127/130/134/140/147/148/150/151, LIT-241–243 (BPS) | Yes | Variant, no novelty; fine |
| -11 unqualified inverse norm | IDEA-134/140/147/151, PD-T032/041/046/054 | Yes | Consolidated; fine |
| -14 every-error lower bound | IDEA-148, PD-T047, PD-T055 | Yes | Quantifier refutation scoped; fine |
| -15 projection-only closure obstruction | IDEA-148/151, PD-T047/050/053/055, PD-N013/015, OBST-03, IDEA-084 (via gate) | Yes | Fine |
| -16 multi-degree extension | PD-T041/047/050/055, IDEA-140/148/151 | Yes | Deferred/OPEN; fine |
| -30 corner witness | IDEA-168/PD-T069, PD-T075, IDEA-157 (gate IDEA-156–168) | Yes | Quantitative variant; fine |
| -31 √ε square family | IDEA-157/PD-T061 (three-node square √ε law), IDEA-161/PD-N021 (square-case δ=O(ε) refuted), IDEA-162 | PD-T059/T061 are disclosed in the theory record. ideas-e5:33 omits PD-T061 and PD-N021 | P-F7 (low) |
| -32/-33/-34 failed paths | IDEA-168/PD-T069/T075, -30 | Yes | Scoped REJECTED: failed; fine |
| E6-50 upstream Hokanson benchmark | IDEA-086 (truncated multivariate V+A is established window recurrence, priority background), IDEA-148/PD-N013, IDEA-151/PD-T051, LIT-281/360 | PD-N013/T051 yes. IDEA-086 not named | Equivalent, no novelty; low (P-F7) |
| E6-51 coordinate orientation | IDEA-151/PD-T051 | Yes | Fine |
| E6-52 "drift ⇒ all fits fail" | IDEA-148/PD-N013 (explicitly excludes the inference) | Yes | Refuted by one counterexample; reason word missing (E6-F5) |
| E6-53 BNT comparator | LIT-285, L2 review | Yes | Fine apart from the label (E6-F5) |
| E6-54 ZN code | LIT-283/284/361, IDEA-116 (measured V+A baselines) | LIT yes | Deferred with a resume condition; fine |

No candidate renames an existing IDEA entry as new. Every novelty statement is "no historical novelty claim" or "variant", consistent with the WebFetch-digest/UNVERIFIED literature limits of LIT-281/283–285/360/361 and the L2 review. No novelty claim is stronger than the evidence.

## (d) E6 record disposition

PD-T?drift-codex-50 is claimed **MEASURED**. My verdict is **CONFIRMED-WITH-CORRECTIONS**: all numbers, the source/order mapping and the scope are confirmed, and the corrections are wording and scope only, with no status change. The evidence:
- Upstream pin and file hashes match.
- The source reading, and my execution, confirm that `[y,x]` = dev including order and `[x,y]` = mirror with reversed order.
- The orchestrator's full-suite, n12-grid and smooth reruns are case-identical.
- My independent long-double reference reproduces the gaps to ≤2e-15.
- Reference conditioning (3778, 101) and the rank exclusions (L-shape 493/496, annulus 495/496, cb_cubic 89/465; disk and cb_equi fail κ<1e8) are as stated, and their noncertifying treatment is conservative and correct.
- The record does not substitute polyrat for BNT or ZN (lines 72–74, 84, 89–90) and does not claim general smooth-data failure (lines 16, 43, 84).

## (e) Findings

**E6-F1 (medium). Off-sample test set is centre-concentrated; reported test errors are test-set-specific and understate boundary error.** Location: theory e6-50:14, :32; directions/E6.md:25, :55; report.md (E6 table, "errors about 2e−15").
- Evidence: the test points `(P[:128]+P[-128:])/2` are midpoints of two iid uniform samples, so their density is triangular and peaks at the centre. With uniform interior points (my run 10):
  - the triangle adversarial test error is 7.45e-3 vs the reported 1.57e-3 (4.7× larger);
  - rotpi4 exp(x+y) test error is 3.6e-14 vs "at most 2.2e-15" (16×);
  - a generic smooth target on rotpi4 gives 1.66e-13, against 4.6e-15 for a reference-span fit.
- The qualitative conclusion stands: smooth fits stay accurate, and E6-52 is refuted.
- Required response: state the test-point distribution and that the values are specific to it. Preferably add a uniform/boundary-inclusive test set, or rephrase "≈2e−15" as midpoint-specific.

**E6-F2 (low). Adversarial training residual equals the gap by construction, not as a finding.** Location: theory e6-50:14 ("equal, to the displayed numerical precision"); report.md table column; proposed-record-changes.md:100/118 ("fit residuals match those gaps").
- Evidence: f = U·v with v the leading right singular vector of (I−WWᵀ)U, so ‖(I−WWᵀ)f‖ = gap identically.
- Required response: say "by construction"; the informative quantity is the off-sample error.

**E6-F3 (low). The Gram-error metric is saturated by the first column's normalization.** Location: theory e6-50:13; E6.md:37; report.md.
- Evidence: max|QᵀQ−I| = 6.8833827526759706e-15 is identical for every method on every M=1681 set. It is the (0,0) entry; the off-diagonal max is ≤2.8e-16.
- Required response: report the off-diagonal maximum, or note that the metric is non-discriminating. This does not affect any claim's truth.

**E6-F4 (low). The smooth target exp(x+y) is special on rotpi4.** Location: theory e6-50:14; E6.md:55.
- Evidence: x+y = √2·ξ, where ξ is a local axis of the π/4-rotated square, so the target is univariate in the reference frame. Its being "independently fixed" before results is not documented in LOG or provenance. My generic non-ridge targets confirm accuracy (≤1.7e-13), so the conclusion survives.
- Required response: note the alignment and the target-selection chronology, or add one generic target.

**E6-F5 (low). ideas-e6 records are not in provisional-ID/template form.** Location: ideas-e6.md:7–11.
- Labels are `E6-50…54`, not `IDEA?drift-codex-50…54`. Template fields are collapsed (no aliases, kill criterion "written before testing", or test discriminability).
- E6-52 says "REJECTED broad inference" without a reason word; it should be `REJECTED: refuted` (within the scope of one counterexample).
- E6-53 is labelled "Equivalent" although its content is "inapplicable: univariate".
- The E6-50 number collides visually with PD-T?drift-codex-50.
- Required response: reformat and supply the dispositions.

**E6-F6 (low). Upstream/environment constraint not recorded.** Location: external-code.md:15–17; README.md:63–80; handoff 02:112.
- Evidence: polyrat at this pin raises a TypeError under numpy ≥2.5 (run 11).
- Handoff 02's representative E6 command omits `PYTHONPATH`, so it fails with this workspace's default Python. README pins numpy 2.3.5 but gives no warning.
- Required response: note "numpy<2.5 required for upstream `_update_rule`".

**E6-F7 (low). Independent coverage statements are stale or narrow.** Location: theory e6-50:68, :87–88; E6.md:66.
- Now covered: the n12 grids and the full suite have been rerun case-identically by the audit orchestrator, and my independent code reproduces rotpi4/triangle.
- Still not independently rerun: the n16 grids.
- external-code.md:21 cites a `chebfun-examples` checkout path that is absent here. The provenance relies on the URL/commit/sha, which is acceptable, but the local-retention claim is unverifiable.
- Required response: update the coverage text at the response step.

**P-F1 (medium). Cold-storage and off-repo artifacts are not retrievable from the audit workspace.** Location: COLD_STORAGE.md:9–10; archive-receipt.json; handoff 02:129–132; independent-e6-root.json (`output_path`); e1-scalar-manifest and independent-scalar-01 off-repo entries.
- Evidence: the ZIP `/workspace/exports/…b09e1db.zip` (sha 27476b62…), the 3.6 MB raw capacity file, root-independent-e6.json, and 46 manifested `/workspace/padua-drift-runs/{e1,independent}` artifacts are absent, so their hashes could not be verified. Windows delivery is disclosed as pending.
- Required response: keep cold-storage verification as an explicit unresolved item. Before readiness, either deliver and record a readback receipt, or state that verification relies on committed compact evidence plus regeneration. The archive identity in handoff 02 remains unverified by this audit.

**P-F2 (low). final-validation omits a registry change.** Location: final-validation.json:12 (`"protected_and_scientific_registry_changes": []`); handoff 02:121 ("scientific registries remain unchanged").
- Evidence: `ID_CROSSWALK.md` (one of the four final-ID registries) gains a 7-line reservation-link section, and the shared ledger is modified. Both are permitted by WORKFLOW (the reservation/link clause), but the receipt's empty list is inaccurate.
- Required response: list the two reservation-only edits explicitly.

**P-F3 (low). The "AC relaxed novelty gate" authority is unrecorded.** Location: ideas-e1.md:3; ideas-e5.md:8.
- No LOG entry or AC message records a relaxation. The executed gate (full summary/obstruction scan, mechanism searches, full shortlisted entries) does meet WORKFLOW's minimum.
- Required response: cite the AC instruction or drop the word "relaxed".

**P-F4 (low). LOG does not link handoff 02 with a line.** Location: LOG.md:6, :82–83 (handoff 02 is described but not linked; WORKFLOW requires a one-line link per handoff).
- Handoff formats otherwise follow templates/HANDOFF.md. Handoff 02 adds a "Load-bearing questions" section and renames "Scope limits" to "Scope limits and provenance", which is harmless. Handoff 01's body is unchanged in history.
- Required response: add the link line.

**P-F5 (low). The allocation union scan relied on orchestrator-supplied PR inventory.** Location: allocation-scan.json:`remote_inventory.provenance`; final-recheck-allocation.json `checked_heads` (PR12 3473cc0, PR14 328a3ec, both since superseded by b2804ac and 14de1df).
- My ref-level recheck (run 7) found no collision, and PR8 is merged.
- Required response: refresh at preparation, as the handoff already requires.

**P-F6 (medium). The IDEA?drift-codex-04 / record e1-03 predecessor list omits the closest coefficient-error mechanisms.** Location: ideas-e1.md:67, :85; directions/E1.md:7; theory drift-codex-e1-03 Depends/Sources.
- Evidence: PD-T042 (IDEA-141) already derives the exact first-order derivative of the window coefficient map with respect to coefficient errors, with on/off-pattern gains. PD-T043 (IDEA-142–144) studies term-wise and closed-loop dot-product rounding through that map. The new bridge's key conclusion, that first-order coefficient and norm errors lie in the span-normal kernel, is the span-output counterpart of those Gram-output results. No campaign file names PD-T042/043 or IDEA-139/141–144 (grep).
- Required response: add them as closest entries, with a separation statement (span-normal quotient vs Gram defect; formal l∞ operation graph vs Gaussian/dot64 models).

**P-F7 (low). Minor undisclosed overlaps.**
- IDEA-087/088 for -01 (a different conditioning map).
- PD-T061 and PD-N021/IDEA-161 for -31 in ideas-e5:33 (PD-T061 is cited in the theory record).
- IDEA-086/IDEA-116 for E6-50/54.
- Required response: add them to the closest-entry lists.

**P-F8 (low). Stale independence status.** Location: ideas-e1.md:95–96 (IDEA-05 "MEASURED pending independent full finite reproduction"); theory e1-05:85 (Open items still lists "Independent executed full finite reproduction").
- These contradict e1-05:43/47/91 and LOG:66–71 (independent-scalar-01 done).
- Required response: synchronize (cross-reference for the E1 auditor).

**Counts:** E6: 0 high, 1 medium (F1), 6 low (F2–F7). Protocol/novelty: 0 high, 2 medium (P-F1, P-F6), 6 low (P-F2–P-F5, P-F7, P-F8). **Total: 0 high, 3 medium, 12 low.**

## (f) Remaining uncertainty

- I could not verify the ZIP, the raw artifacts or the root E6 output hashes (absent in this workspace).
- PR open/closed status was inferred from refs, because the GitHub API was unavailable (403).
- The n16 grids were not rerun by anyone independent.
- Bitwise equality has been shown only with numpy 2.3.5 and OpenBLAS single-threaded, on Python 3.12/3.13.
- My references are long-double CGS3 numerical constructions, not exact rational certificates. Their agreement with the campaign to ≤2e-15 supports, but does not prove, the reported gap values.
- I did not reread fulltexts (Hokanson/ZN/BNT). Literature statements remain at their recorded WebFetch-digest/UNVERIFIED level.
- I read literature/INDEX.md and the L2 prior-art review only in the relevant parts.
- BNT and ZN execution remain unperformed (correctly disclosed).
