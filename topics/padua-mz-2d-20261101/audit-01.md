# Claude audit-01 — padua-mz-2d-20261101 (PR #14)

- **Decision: mathematics ACCEPTED for the stated scope.** I found no mathematical error in any of the 22 new records. I accept all 17 PROVED, 2 MEASURED and 3 OPEN statuses and every candidate disposition as written. Nothing is upgraded: PD-T028, PD-T110, PD-T114 and PD-T116 stay OPEN, and PD-T108 and PD-N049 stay MEASURED.
- **Stage → WORK** for a documentation-only response. There are six record/registry findings (F1–F6), all P3, and none changes a claim, proof, status, code or evidence. Per `agents/WORKFLOW.md`, findings set WORK. The developer answers them in `response-01.md`. If the response only makes the listed text edits, the topic may proceed to PR without re-audit. A Claude focused recheck is needed only if the response changes a statement, proof, status, dependency set, code or evidence beyond those edits (F1's transcription included, see below).
- Audited candidate: `e847601c6c1f1261d4862d63360fdfdb0df8a15b`. Branch head at audit start was `14de1dfd69c415c052a9d5593c7e2aa67ffa71ec`. `git diff e847601 14de1df` changes only `LOG.md`, `handoffs/01-work.md` (status line) and adds `handoffs/02-audit.md`, so no scientific byte differs.
- Main/base: `806cc7b4509fd93bae652f9545d32d95529f8281`, refreshed 2026-11-01 and unchanged.
- Rules read at branch head `14de1dfd69c415c052a9d5593c7e2aa67ffa71ec`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`. `git diff origin/main 14de1df -- AGENTS.md agents templates` is empty, so these are byte-identical to `806cc7b` (and per the developer log to `cf89b140`).
- Auditor: Claude, configured model `claude-opus-5-5`, effort xhigh, as requested in handoff02. Reason: a mathematical audit of new all-degree proofs, a computer-assisted finite certificate and several novel scoped negatives (Opus 5.5 xhigh row of the allocation table). The runtime exposes no separate receipt of the serving model. I am a different agent from every Codex developer, worker and the supplementary Astra reviewer. I did not edit any developer proof, code, evidence, frozen review or archive file.
- Role: independent auditor, and topic orchestrator for this step only (Git operations below).

## Read coverage

**Rules and topic.** `LOG.md`, `plan.md`, `report.md`, `definitions.md`, `directions/D0.md`–`D7.md`, `directions/d4-positive-floor-verification.md` (including the archived 4450-byte body), handoffs 01/02, `independent-checks.md`, the D1-relevant part of `independent-math-d1.md`, `supplementary-audit.md` (findings S1/S2, its reconstruction and executions sections, focused rechecks), `response-d4.md`, `response-d5.md` (spot read), and `literature.md` (foundation verdict and conventions).

**Ideas and novelty scope.** I read the complete `state/IDEAS.md` at `e847601`, all 761 lines. For lines 680–737 (bivariate-Lanczos final registration IDEA-120–176, unrelated to MZ) I read each row's first 600 characters, which covers the full candidate and disposition cells for every row except a few long rows. This includes every obstruction and disposition table: the charter obstruction table, the bivariate-Lanczos OBST rows, the MZ obstruction memory, the current MZ disposition table, and the lattice and programme-ideas tables. It also includes the new PR14 section, IDEA-210–227. I read in full the candidate records `ideas-d1.md`, `ideas-d2.md`, `ideas-d4.md`, `ideas-d5.md` (IDEA-219–223), `directions/ideas-d3.md` and `directions/ideas-d7.md` (via D7). The campaign makes no historical-novelty or priority claim: every candidate is "variant", "equivalent" or "no novelty claim". I checked that no failed route is converted into a refuted all-m target (see Dispositions below).

**Theory.** All 22 new files under `tracks/mz-constants/theory/mz2d-*.md`, read in full. Predecessors read in the relevant part: PD-T017 (statement and K_N), PD-T018 (statement and witness), PD-T022 (statement and endpoint corollary), PD-T023 (statement and proof §§1–3), PD-T028 `open-padua-target.md` (full), and the PROOF_STATUS rows for PD-T013–028 and PD-T101. I did not re-read the M1/M2/M3 proofs or the merged manuscript in full. These were accepted earlier (Claude MZ audit-01/02), and the new records use only their statements.

**Code and evidence.** `mz2d_exact.py`, `mz2d_independent_check.py`, the D2 inline diagnostics, `protocol/final-validate.py` and `evidence/exact-parity-scan.json` (results), all read in full. I did not read `mz2d_spectra.py` line by line. It is the D0 floating producer, and I replaced it with my own independent float implementation (below).

**Registration.** `protocol/final-id-map.json`, `final-input-manifest.json` (PR12 advance comparison), `final-validation.json`, the PR14 additions to `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `literature/INDEX.md` (LIT-427/428 rows), the two new LIT records, and the reservation sections of the batch ledger on PR14, PR15 and PR12.

**Literature limit.** I did not re-read any primary source. One attempted fetch of the SVZ 2008 author preprint was not permitted in this session, because the permission prompt went unanswered. I therefore checked LIT-427/428 only for internal consistency and for consistency with the computed weights (Σ|w| − 4 = 4|w_c| for m ≤ 40, since only the two corners are negative; this is compatible with SVZ's reported Σ|w| → 4). No source theorem is a proof dependency of any new claim.

Content identities at `e847601` (SHA-256):

| File | SHA-256 |
|---|---|
| `tracks/mz-constants/theory/mz2d-aliasing.md` | `c6db7a52513e865ccd38b163eeaeace2300ccb775d69c0203d5d7f3d21e7a153` |
| `tracks/mz-constants/theory/mz2d-certified-spectra.md` | `aa11dcd25558648774877d64afa4c194ee515533b7974d8dcac5a22e26b5f01d` |
| `tracks/mz-constants/theory/mz2d-defect-structure.md` | `2c1ae9affe145c000e4a704d4f4b70e54c446419a9bd7bbe88a4d1d980c4407d` |
| `tracks/mz-constants/theory/mz2d-endpoint-rhombus-packet.md` | `bc410b9e5debbd69cf3c108179b7fd3c8b723f5e03ef391705e978abceafec00` |
| `tracks/mz-constants/theory/mz2d-endpoint-tensor-obstruction.md` | `a0d3b5756a1ef3a7e153355bbb556e16f1b4b969f374fec2588a782ddaa16e77` |
| `tracks/mz-constants/theory/mz2d-eta-counterexample.md` | `8123353aa5d0fced7812d58b74da95cae90dfc9902655d3fd32ace2fbe14b583` |
| `tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md` | `f1619b1919400bb3c168debbcca9dd5ba6e3bfbd145c355729ac0237789524ab` |
| `tracks/mz-constants/theory/mz2d-fixed-ratio-rectangular-obstruction.md` | `0b6adc8afda570602603dddd9ee446e5e4a6b42ccdbb643bc80d31ced5488e12` |
| `tracks/mz-constants/theory/mz2d-fixed-ratio.md` | `9116dcb6203d585d2b3eeeee539812a0ffb568f7c9313096db42da7ba7d85c04` |
| `tracks/mz-constants/theory/mz2d-hyperinterpolation-absolute-obstruction.md` | `183d6292bf9c477333bdb69ebe5579924b3bd6b5781ba1b7c6d8ffe67ce4c1ec` |
| `tracks/mz-constants/theory/mz2d-hyperinterpolation-absolute.md` | `ed742f9928c3406cb954bd00378ccafa1d6db208f67a65bcce02cacc8b1f5da0` |
| `tracks/mz-constants/theory/mz2d-hyperinterpolation-reproduction-obstruction.md` | `80e5e604cf451f923133a3644dd67176e42b5e9655c6cc23b47b7a3d0374c8f2` |
| `tracks/mz-constants/theory/mz2d-hyperinterpolation-reproduction.md` | `8059eaa191ae36b2f27f12c81b2f0c240cc2924fe4bab0a6e601e9724633ec4e` |
| `tracks/mz-constants/theory/mz2d-hyperinterpolation-signed-obstruction.md` | `2b68198e74eb686570023ca1fde12a7ac0c1c8e697598c6bb16560b5fa416508` |
| `tracks/mz-constants/theory/mz2d-hyperinterpolation-uniform-open.md` | `0dbd3effb2f10364fe5e7b13670328f113c47caeb67e39c11f8b3f7751655860` |
| `tracks/mz-constants/theory/mz2d-lower-corner-subtraction-obstruction.md` | `2d9201222f632bcec6e3697c650e0aa8ee8e5e5f6989a2e682df8f8ea7ca42fb` |
| `tracks/mz-constants/theory/mz2d-lower-corner-weights.md` | `38e730b7f8a11eea7265dc02d3163d128d7092a1a9cd9a38e8b6742daf87b56a` |
| `tracks/mz-constants/theory/mz2d-measured-spectra.md` | `c15fd5570bb2fbac3234d3bdd0a989dc19608daeaef586b1495680248d53f32a` |
| `tracks/mz-constants/theory/mz2d-tensor-control.md` | `400853f5686dfbeb9b0456a428bd327be8e03d915bc6a6d80b52962534caa460` |
| `tracks/mz-constants/theory/mz2d-upper-open.md` | `67287c2de59618be9f2a672d5aa389fa139c612a0cc7a5bcbb2e20987a879519` |
| `tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md` | `5278ed8ba7e7381aa20d4358473df0cd5961839e74ed9d26d22d4fd548e7027b` |
| `tracks/mz-constants/theory/mz2d-upper-tensor-obstruction.md` | `dbf14f6f85d5816125e132073ee9301cec9544cb24260815f2eb08fa82bc757f` |
| `tracks/mz-constants/code/mz2d_exact.py` | `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70` |
| `tracks/mz-constants/code/mz2d_independent_check.py` | `5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc` |
| `tracks/mz-constants/code/mz2d_spectra.py` | `623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76` |
| `topics/padua-mz-2d-20261101/evidence/d0-manifest.json` | `91b2d9a4645ba4ca0d5451ef9f503a4d22dcf8972624f183d0559460317cd90f` |
| `topics/padua-mz-2d-20261101/evidence/d0-spectra.json` | `3c5c702ed964b240a9e96bb0be55a2a3e86c2c71eb5e49706b7c58680879e4f5` |
| `topics/padua-mz-2d-20261101/evidence/exact-parity-scan.json` | `d4f57cbe7c4185a662e0c7d6828ec8c323a8b3da39b17bab48ef025f09d17094` |
| `topics/padua-mz-2d-20261101/evidence/exact-parity-scan.py` | `d517eaa0c2bf08305d6a647e1b57e363ba0c0f5a665c28390dea508c30991077` |
| `topics/padua-mz-2d-20261101/evidence/exact-spectra.json` | `5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de` |
| `topics/padua-mz-2d-20261101/evidence/independent-additional-checks.json` | `2da16fa5c8f2f480ab7c12270b8c9b95ec49028f9df6b1cf4062af4f11897717` |
| `topics/padua-mz-2d-20261101/evidence/independent-exact-spectra.json` | `18c8623442664aa119d3581b701d200315d454071d6b8f6c89cbaf540fe34d9c` |
| `topics/padua-mz-2d-20261101/definitions.md` | `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db` |
| `state/IDEAS.md` | `6a0a773c28d594561c828e92668571628fd42fa30ad8ae3e4216d7aa67a87f28` |

## Independent executions actually performed

Environment: cloud container, Linux 6.18.44 x86_64, Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, python-flint 0.9.0 (`pip install --target /tmp/padua-flint python-flint==0.9.0`), SymPy 1.14.0, mpmath 1.3.0. BLAS single-threaded. No `-O`. This runtime differs from the developer's (Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0). Disposable worktree at `e847601`. Every output was written outside the candidate tree and copied afterwards to `topics/padua-mz-2d-20261101/audit/claude-audit-01/` (manifest there). Developer receipts were not overwritten: the one script that rewrites a receipt (`final-validate.py`) ran in the disposable worktree and its file was then restored.

**R1 — exact producer rerun (developer code).**
```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output <audit>/claude-mz2d-spectra.json
```
Exit 0 in 31.7 s. Code hash `5d1f005e…`; definitions hash `4ac0e391…`. All four `results` objects equal the stored `exact-spectra.json` after removing only nested `seconds`. That covers intervals, all 16 inertia triples, denominators, diagonal signs, minimum dominance margins, integer-transform SHA-256s and the m30 witness coefficients and forms. The floating proposals are bit-identical on this different NumPy/SciPy stack.

**R2 — developer's independent checker functions, new auditor receipt.** `run_dev_independent_functions.py` imports `mz2d_independent_check.py` from the worktree and calls `stored_witness`, `region_checks`, `nodal_check(1..5)` and `rejection_controls`. It does not call `main`. PASS: 245 cyclotomic nodal moments, 371 nodal-Gram/symbolic-integral pairs, 1,221 region moments, 6/6 malformed-input controls rejected, stored witness matched.

**R3 — auditor-written exact certificate, different method** (`claude_mz2d_audit_check.py`, written without importing developer code).
- The moment formula of PD-T106 (1) is checked against signed weights solved at 60 digits directly from the node Vandermonde, so the alias proof is not used. This covers m = 1..10 and every mode of total degree ≤ 2m+3: 1,365 modes, maximum error 4.6e-60.
- The stored m30 witness is recomputed exactly by first expanding p² in the product-Chebyshev basis (898 terms) and then applying the moment functional, which is a different organisation from the bilinear zᵀQz. a, b, b−4a and a/b equal the stored fractions. A float64 nodal evaluation with Vandermonde-solved weights agrees with the exact Q(p²) to relative error 4.7e-14.
- Spectral brackets are certified by a different exact route from the developer's signed-dominance congruence. λ_min > lo holds because d(Q − lo·H) is positive definite on both parity blocks, by Sylvester's criterion: every leading principal minor is positive, read from an unpivoted FLINT `fflu`, whose row permutation is checked to be the identity and whose last minor is checked to equal `det`. λ_max < hi holds because d(hi·H − Q) is positive definite in the same way. λ_min < hi and λ_max > lo follow from exact rational Rayleigh quotients of rounded vectors. All acceptance tests are explicit `if … raise`, so they are valid even under `-O`.
- Result: m = 10, 20, 30: all six brackets reproduced exactly as in PD-T107, with both PD sides passing on both parity blocks (block dimensions 30/25, 110/100, 240/225) and both Rayleigh sides passing. **m = 40: still running when this record was committed** (two 410-dimensional FFLUs per endpoint). Its outcome will be appended below as a dated addendum, which is the auditor's own record. Until then, the m40 brackets rest on the developer's checker, actually rerun twice by different agents (the developer worker and R1 here), and are accepted on that basis.
- Also: corner weights from 50-digit solved weights for m = 2..14.

**R4 — auditor float/exact regressions** (`claude_mz2d_audit_extra.py`, `check_t110.py`; MEASURED corroboration except where marked exact):
- Every m = 2..40 (float64, Vandermonde weights, Legendre Gram): extrema agree with `exact-parity-scan.json` to ≤ 6.2e-14 and reproduce the PD-T108 table at m = 10, 20, 30, 40. The minimum is 0.2148170295 (m40), the maximum 1.7780886239 (m40), and the first η > 3/4 occurs at m = 26. For every m = 3..40 there are exactly two negative weights, at the two node corners. At m = 2 the corner weight is zero to roundoff (exact value 0 by PD-T111).
- PD-T117: directly formed tensor-CC Gram on Π_n versus the two coordinate CC spectra, for m ∈ {2, 3, 5, 10, 20, 30, 40} and n ∈ {0, ⌊m/2⌋, m−1}. Maximum discrepancy 1.6e-15. The m = 10..40 endpoint values reproduce the PD-T108 tensor columns.
- PD-N049: the rhombus packet, rebuilt from the written operation list, gives quotients 0.8817, 0.8884, 0.9049, 0.9239 at m = 8, 16, 32, 64, matching the record to ≤ 2e-13.
- PD-T115/PD-N053: the diamond filter reproduces random diamond-supported trigonometric polynomials (n < m) at five random points for (m, n) = (3,2), (4,2), (5,3), (6,5), with error ≤ 2.1e-14. The rectangular operator's (1−m, −m) coefficient on cos t cos s equals 1/[4(m−n)(m+1−n)] in all four cases.
- Exact: PD-N045 §1 cycle entries (−4/3, 8/9 at m=3 or 4/9 at m ≥ 4, −4/3) for m = 3..8; the §2 m4 entries −4/9 and 2/15; PD-N051 defects equal h_(m−1) − h_(m+1) (odd m) and h_m (even m), nonzero, for m = 3..15; K_(m−1)(c,c) = m(m+1)(m²+m+1)/24 for m = 1..29.
- PD-T111: the closed form equals the 50-digit solved corner weights for m = 2..14 to 20 digits, including w = 0 at m = 2 and w = −1/18 at m = 3. −w·m⁴ − 4 log m stays bounded (−0.92 at m = 10⁵), consistent with (2).
- Exact: the PD-T110 eqs (2)–(3) mixed-block formula and H₀₁ = 0 hold for all 4,548 opposite-secondary-parity pairs, m = 3..12.

**R5 — registration validator.** `python3 topics/padua-mz-2d-20261101/protocol/final-validate.py`, run in the disposable worktree at `e847601`, gives PASS. The regenerated receipt differs from the committed one only in `entire_topic_new_theory_links_checked`: 98 here versus 97 committed, because one link was added by the later root summary edits the receipt itself warns about. The worktree file was then restored. I also checked these myself:
- all 13 pinned A2 objects are byte-identical (same blobs) at PR12's current head `b2804ac2cbb86568b475964f25dbf0ccf48949ff`, which has advanced past the `7ec02d0` recorded in the receipt;
- the archive body at offset 2255 (4450 bytes) hashes to `bcecd476…`;
- the current open PRs are #12 (`b2804ac`), #14 and #15 (`36c93794ce02f92c76c89e5a9ec8095eb238d91d`, advanced past `2d20672`), and there are no closed-unmerged PRs. Neither #12 nor #15 uses or reserves any ID in PD-T106–135, PD-N044–061, IDEA-210–245 or LIT-427–444. PR15's ledger imports PR14's ranges unchanged and reserves T136–155, N062–071, IDEA246–285 and LIT445–459. The reservations remain intact and disjoint.

Not run: the D0 producer `mz2d_spectra.py` (replaced by my own implementation R4 to m40, not to m100); `final-assign.py` (forbidden); m60–100 Padua spectra; the cyclotomic regressions beyond R2's m ≤ 5.

## Mathematical verification (claim by claim)

**PD-T106 (PROVED, accepted).**
- Folding gives T_a(x_j) = T_A(x_j) and T_b(y_k) = T_B(y_k). The complement (m−A, m+1−B) carries the signs (−1)^j(−1)^k, which equal 1 on the even checkerboard. The two total degrees sum to 2m+1, so exactly one is ≤ m. This proves (1) for all a, b ≥ 0 and m ≥ 1, including fold endpoints.
- (2): (0, m+1) ↦ (m, 0), and h_m ≠ h_(m+1) for every m ≥ 1.
- (3)–(4): multiset product-to-sum. The pencil congruence is by the invertible Legendre-to-Chebyshev C.
- Independently confirmed numerically (R3).

**PD-T109 (PROVED, accepted).**
- I re-derived all six region rows and boundaries: for a > m, b < m−2 is forced, and symmetrically for b > m+1.
- Pullback per sector gives a = εi + δk, b = ε′j + δ′l and labels r + s ≤ c.
- The Fourier integral identity (9) and the bound (1/2π)∫min(L, π/|t|) = 1 + log L are correct, with L ≤ 8n+1.
- The actual sector count is 10 × (1+2+2+4) = 90 ≤ 160, so "at most 160" is right.
- I accept "PASS" as the verdict on the frozen structural kill criterion only. The records correctly say the generic Chebyshev-coefficient bound gives nothing sharp after the Legendre change of basis.

**PD-T107 (PROVED, accepted).**
- The reduction is sound: positive denominator; strict dominance gives nonsingularity along the homotopy, hence the diagonal inertia and invertibility of R; Sylvester's law; and generalized inertia counts the eigenvalues below t.
- The parity-block justification is correct for even m, and the off-block zeros are explicitly asserted.
- The requirements for a PROVED computer-assisted claim are met: proved reduction, exact arithmetic, committed checker and evidence, different-agent rerun. I add an independent rerun (R1) and an independent second certification method (R3).

**PD-N044 (PROVED, accepted; REJECTED: refuted for uniform η(m,m−1) ≤ 3/4, scope m = 30 only).** The Rayleigh implication is correct with signed weights. The stored-coefficient equalities are verified independently (R2, R3).

**PD-T108 (MEASURED, accepted).** Corroborated to m40 by an independent float implementation. m60–100 were not replayed.

**PD-T111 (PROVED, accepted).**
- Integrating PD-T101's cardinal identity at a corner gives (3). The telescoping, (4), the partial fractions (5) and the substitution all check by hand.
- Odd m: S_r ≥ 1 > (N−1)/(2N). Even m: zero at m = 2, and negative for m > 2 via 16(m²−1) > 12m².
- Asymptotic (2) is correct, and the closed form is confirmed numerically (R3/R4).
- The corner sets {(1,1),(−1,1)} for even m and {(1,1),(1,−1)} for odd m are correct for this orientation.

**PD-N048 (PROVED, accepted; failed for the fixed-constant continuous subtraction only).**
- The generating-function sum is correct.
- The rank-one norm is (−w_c)·K = (log m)/6 + O(1).
- The fixed-θ corollary is correct: K_n(c,c) = (n+1)(n+2)(n²+3n+3)/24 ~ θ⁴m⁴/24, giving θ⁴(log m)/6.
- Inside 2n ≤ m one has G = I, so positive part = I + negative part while both diverge. The cancellation remark is exactly right.

**PD-N045 (PROVED, accepted).**
- §1: the cycle 1, T₂(x), T₂(y) has a positive product, invariant under switching, including the m = 3 alias T₂T₂ ↦ T₁T₂ giving R_vz = 0.
- §2: the m = 4 entries are correct.
- §3: the m = 3 cardinal polynomial and w = −1/18 agree with PD-T111 and with R4.
- Scope issue: F1.

**PD-N046 (PROVED, accepted; refuted pointwise majorant).** I checked the m = 2 nodes, L = (2y² − y − x²)/3 at all six nodes, ∫L = 4/9, and the CC weights 4/3 and 1/9.

**PD-N047 (PROVED, accepted).**
- The top U coefficient of p_N is strictly negative, so the degree is exactly N−1.
- (1) follows from PD-T023 applied coordinatewise with 1 − n/N ≥ ε, and the tensor factorisation.

**PD-N049 (MEASURED, accepted).** The admissibility formula (3) is correct (pairing cancels the sine terms; total degree max(r,s)). The quotients are reproduced (R4). This is a scoped, packet-only failure.

**PD-T110, PD-T116, PD-T114 (OPEN, accepted).**
- PD-T110: the parity-block reduction (2)–(4) and the Schur-complement equivalence are correct, and (3) is verified exactly (R4).
- PD-T116: half-exactness is correctly kept as routine and not used to label the target PARTIAL.
- PD-T114: the target wording is preserved.

**PD-T115 (PROVED, accepted).**
- Ĥ(a,b) = κ(a+b)κ(a−b), and max(|a+b|, |a−b|) = |a|+|b|.
- The checkerboard character set (4) is correct; its shortest nonzero ℓ¹ length is 2m, which exceeds n + m − 1.
- Reflection preserves the checkerboard parity.

**PD-N053 (PROVED, accepted; failed for that exact operator).** The congruence analysis at v = (1−m, −m) and the endpoint κ values 1/(m−n) and 1/(m+1−n) are correct for m ≥ 3 and 2 ≤ n < m.

**PD-T112 (PROVED, accepted).**
- Duality plus disjoint continuous tents gives the exact norm Σ|w||p(z)|.
- Cauchy–Schwarz is applied with |w|. A = G + 2G₋ and tr G₋ = χ. τ = V + 2δ, and β ≥ 1.

**PD-T113 (PROVED, accepted).** The product degree r + n ≤ m with r ≤ n gives reproduction. The mass-4 factor 2 is right, and (3) holds without a Gram inverse.

**PD-N050 (PROVED, accepted; refuted general transfer).** Σ|w| = 4t − 2 is attained by 2|x| − 1, and G = 1.

**PD-N051 (PROVED, accepted; refuted E₂-only/higher reproduction).** ⟨Hq, p⟩ = Q(qp) for p ∈ Π_(m−1). The odd-m case uses T_(m+1)(x_j) = T_(m−1)(x_j); the even-m case uses T_(m+1)(y_k) = T_m(x_j) on the checkerboard. The defects are verified exactly (R4). "Maximal complete reproduced space Π₁" is correct.

**PD-N052 (PROVED, accepted; failed uniform majorants only).**
- A ⪰ |w_c|u_cu_cᵀ, χ ≥ s_m, τ ≥ 4 and λ₊ ≥ 1.
- The separation remark |w_c|√K = O(log m/m²) → 0 is correct, so this is not a divergence of the actual norm. PD-T114 stays OPEN.

**PD-T117 (PROVED, accepted).**
- X_ac·Y_bd ≠ 0 would force a+b+c+d ≥ 2m+3 > 2n, so the mixed term vanishes.
- The wedges a−b > m−n and b−a > m+1−n are disjoint for n ≤ m−1.
- The fixed-b slices are the principal matrices A_m^(n−b), giving the upper/lower inclusion via Cauchy interlacing plus the eigenvalue 1 from the constant.
- The b = 0 and a = 0 slices are invariant with blocks A_m^(n) and A_(m+1)^(n), giving the reverse inclusion.
- (4)–(6) follow correctly from PD-T017 (full Π_N, K_N nondecreasing), PD-T018, PD-T022 and PD-T023. This is a positive-control theorem only, as stated.

**Dispositions.**
- "REJECTED: refuted" is used only where a claim's negation is established: IDEA-211, 213, 219, 223.
- "failed" is used only for mechanisms: IDEA-212, 216, 217 (crude subroute), 218 (MEASURED), 222 (majorants), 224.
- The equivalent/deferred candidates (215, 221, 225, 214, 226, 222-target) create no PD-N, and the IDEA-225 consolidation into PD-N045 follows the L5 rule.
- No PD-N is converted into a refutation of a universal spectral target, and the split-from/split-into wording keeps PD-T028 OPEN.

## Findings

All are **P3 (record/registry)**. None affects a claim's truth, status or evidence.

- **F1 — PD-N045's formal Statement and scope omit its §3 negative claim** (`mz2d-upper-sign-obstruction.md`). Since S2, PD-N045 is the canonical record for D4's pointwise positive-floor obstruction: IDEA-225, PD-T116 "Depends on", D4.md and the crosswalk all cite "N045 §3". But its Statement, "Negative-result scope" (attempted mechanism IDEA-212 only) and Split-from header list only the Z-matrix and defect-sign failures. §3 is introduced as "for clarity". *Response requested:* add §3's existing negative statement (w_(1,1) = −1/18 at m = 3, hence no strictly positive pointwise nodal floor or positive-weight Cauchy–Schwarz on arbitrary nodal data; no conclusion about the restricted form on Π_(m−1)), with its scope (m = 3), to the Statement and Negative-result scope. Add IDEA-225 as a second attempted mechanism. This must be a verbatim transcription of §3 with no new mathematics. Any wider change needs a focused recheck.
- **F2 — residual local shorthand after ID normalization.**
  - `ideas-d4.md:110` now reads "Historical provisional `PD-N045` is an alias mapped to N10". This is a garbled substitution: it should say the historical provisional `PD-N?mz2d-codex-41` maps to PD-N045.
  - Unnormalized local labels "N10", "N41" and "candidate 40/41/42" remain in `mz2d-fixed-ratio.md` (lines 59, 67, 107–108), `mz2d-fixed-ratio-diamond-reconstruction.md:129` ("candidate 42"), `directions/D4.md:22, 42–43`, `ideas-d4.md:124, 126, 161, 185`, `ideas-d5.md` ("candidate 31") and the crosswalk's last mapping row ("existing N10").
  - *Response:* replace these with final IDs (PD-N045, IDEA-224/225/226/220) or with full provisional IDs. Frozen review files and the archive (`supplementary-audit.md`, `d4-positive-floor-verification.md`, `response-d4.md`) must not be edited.
- **F3 — PD-T028's own record lacks the reciprocal split link.** PD-T110 declares "Split from: the upper-threshold part of PD-T028". The crosswalk records PD-T110 and PD-T116 as OPEN alongside PD-T028, but `open-padua-target.md` (byte-protected as a prior MZ object) has no "Split into"/supporting note. *Response:* either add a dated administrative header line to `open-padua-target.md` naming PD-T110 (split-off upper part, OPEN), PD-T116 and the supporting records, updating the protected-object manifest accordingly; or state in the crosswalk and response why PD-T028's file stays frozen. Status is unaffected either way: both parent and part are OPEN, so there is no PARTIAL question.
- **F4 — PROOF_STATUS rows use boilerplate in Evidence and Disposition.** All 22 rows say "Written proof or finite evidence as explicitly distinguished in record", including the three OPEN targets, which have no proof. The Depends-on cells are also loose: PD-T110 lists PD-T014, which its record calls background; PD-T116 lists PD-N053, which its record calls context; PD-T114 says "elementary inputs" although it rests on PD-T112/113. *Response:* give each row a short specific evidence/status-by-part cell (for example "analytic proof", "exact checker + different-agent rerun + Claude rerun", "no proof; OPEN target", "float64 m10–100"), and align Depends-on with each record's own "Depends on" section.
- **F5 — the new obstructions are not in an `state/IDEAS.md` obstruction table.** Other campaigns add a scoped obstruction/disposition table (lattice, programme-ideas). PR14 adds only the IDEA table, and the "MZ obstruction memory" table (PD-N002–006, PD-T021/027) has no rows for PD-N044–053. Future novelty gates are required to read obstruction tables. *Response:* add a "Padua MZ 2D obstruction and disposition table" to the PR14 section, one row per PD-N044–053 with exact scope/status. Optionally add a pointer in IDEA-056's row. This is additive only, after the existing rows.
- **F6 — receipts and PR text are stale against current heads.** `final-validation.json` reports 97 topic links (98 at `e847601`). The PR body and receipts cite PR12 `7ec02d0` and PR15 `2d20672`; the current heads are `b2804ac` and `36c9379` (reservations still disjoint and A2 pins unchanged, R5). *Response:* refresh these at readiness with the required reservation recheck. Do not edit the frozen receipts; add new dated receipts instead.

## Remaining uncertainty and limits

- The exact certificates rely on Python integer/Fraction arithmetic, FLINT `fmpz_mat` and the interpreter. R3 uses a different exact method (Sylvester minors from FLINT `fflu`), but the same FLINT library.
- Floating results (PD-T108 to m100, PD-N049, the parity sweep) remain MEASURED. I replayed m ≤ 40 and the rhombus packet up to m64 only.
- No primary literature was re-read (see the Literature limit above). Historical novelty is screened, not cleared.
- The universal signed-Padua targets (λ₊ < 2, positivity, endpoint order, η convergence, η(θ) < 1, uniform operator norm) are untouched and OPEN.
- PR15 still conflicts textually in the crosswalk and ledger (developer rehearsal). This must be reconciled after AC chooses the merge order.

## Auditor evidence

Committed under `topics/padua-mz-2d-20261101/audit/claude-audit-01/`: the auditor scripts, receipts and logs, with a manifest (`MANIFEST.md`) of SHA-256 and byte sizes. Total size is well under the evidence limits.
