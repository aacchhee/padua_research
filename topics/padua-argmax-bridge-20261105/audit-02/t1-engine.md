# Audit2 / T1 — final hybrid finite engine and dependent finite degrees

- Auditor: Claude Opus 5.5, xhigh (independent subagent inside the handoff-10 INTERIM Claude audit). Developer audited: Codex. I made no Git state changes and edited no repository files.
- Branch/head: `codex/padua-argmax-bridge-20261105` at `1b6aa31ae759022ce89bb8a3be70a881790e259f`. I read the rules (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md) at this SHA. The working tree was clean before and after (`git status --short` showed 0 lines).
- Labels: [D] derivation, [E] my own execution, [I] inspection only.
- Scope: `code/final_hybrid_engine/`, the theory and audits it relies on (E12, E15, D32, D29/C02, D14, D19), the 41/511 hybrid validation, and the records behind finite degrees 42, 63–64 and 159–160. No novelty content is in scope, so I did not read the full IDEAS file.

## Verdict

**ACCEPT, no BLOCKING or MAJOR finding.**

- The checker implements the proved finite reduction faithfully:
  - D32 cover;
  - C02/D29 floors;
  - D14 grid norm and D19 tree norm;
  - D08 actual corner below 256, E12 above;
  - the E15 whole-cell far192 leaf.
- I independently reproduced all hybrid validation cases and all five D38 low degrees. Every run had a directly observed EXIT 0 and gave results bit-identical to the committed evidence. This holds on a different OS, compiler and Python, and with non-pinned FLINT bytes.
- A finite-layer checker I wrote myself agrees on every certificate.
- 4 MINOR findings and 6 NOTEs are listed below.
- No finite degree depends on the hybrid engine yet. 41 and 511 were already proved, and 42/63/64/159/160 were proved with the D36 engine.

## 0. Identities

- [E] `FREEZE.json` is 4153 B with SHA-256 `0d9ce0a5…eb`, as stated. All 9 `AUDIT.sha256` entries match. All 13 FREEZE `code_data` rows match on bytes and SHA-256, including the D23/D07/C11 native sources, the D09 controller and `phase_checker/setup.py`.
- [E] `independent-checks-final-hybrid-engine.md` is 51294 B with SHA-256 `f812fd44…bafe`, as stated.
- [E] Committed evidence hashes match the review's tables:
  - `evidence/final-hybrid-validation/primary-41.json` = `faca3065…`; `primary-511.json` = `c5369110…`;
  - `fresh-41.json` = `a2af589a…`; `fresh-511.json` = `0c00807f…`;
  - all ten D38 `primary-/fresh-{42,63,64,159,160}.json` match the hashes in theory/D38.
- [E] D36 `FREEZE.json` is 7073 B with SHA-256 `d7481715…01`, and all of its `code_data` rows match.

## 1. Reduction reconstruction and leaf predicates (task 1)

**Objects.** [I] D32(4) and D14 define S_n(α,β) = (1/2N)·Σ over the odd board of |G_n((jπ+α)/n, (kπ+β)/m)|, with S^t(a,b) = S_n(πa,πb) on T = {a,b ≥ 0, a+b ≤ 1}.

- The physical chart (D32(5)) assigns every point an odd center (J,K) and a signed phase with |α|+|β| ≤ π, and λ = S − Δ_JK with Δ ≥ 0.
- Both parity-correct corners are odd centers at phase (0,0), where Δ = 0 and S_n(0,0) = Λ_c. Their phases are inward (α, β ≤ 0).
- [E] The native S kernel matches this normalization. `post_audit_D23_backend/point.cpp:13` computes u = (δ+2k+a)/n and multiplies the turn by π, so the inputs are α/π and β/π. Line 27 rejects anything outside T. Lines 53–54 return FLOOR/CEIL outward binary64 endpoints.

**Leaf predicates.** [I]+[D] `checker.py` matches the theorems:

- **θ (line 65)** = (22/7)²·[(Δa)² + κ²(Δb)²]/8. This is D32(8) and D19, with p_hi = 22/7.
- **FAR (line 106).** Strict U < L, with U = V + θM.
- **NEAR (line 107).** 2·p_hi·min(ah+bh, 1) ≤ 1 and U − δ < L, both strict. The first condition gives ρ = π(a+b) ≤ π·7/44 < 1/2 on the whole box.
  - r_B = min(1/2, p_hi(ah+bh)) is exactly D32(1)/(10).
  - The floor tiers and B_n(r) coefficients (lines 67–77) equal C02(3)/(4) for 64 ≤ n < 160 and 160 ≤ n < 512, D29-radius41(1) for 41 ≤ n < 64, and D29-floor512 (1/20) for n ≥ 512. The tier boundaries 63/64, 159/160 and 511/512 are exact.
- **SPLIT (lines 108–113).** [D] This branch is unreachable (NOTE N3). Reaching it requires U ≥ L (not FAR) and far = False, but far = False forces high < 7/44, so NEAR's first condition holds and NEAR would already have returned. D38 also reports that no SPLIT leaf occurs.
- **Tree decoding (lines 115–137).** Closed midpoint children, both subtrees required, full token consumption, depth ≤ 18, nodes ≤ 2047.
  - OUTSIDE means strictly al+bl > 1. This is D32's exact emptiness test, because the lower-left vertex minimizes a+b.
  - [E] My decoder checks that leaf areas sum exactly to 1 on all 16 certificates.
- **Grid (line 56).** The 15 points (i/4, j/4) with i+j ≤ 4 fold to 13 keys. The hypotenuse identification (a,b) ~ (b,a) is the fold (1−a, 1−b), which is D32(7), not an n,m swap.
- **Norms.** `coarse_norm` = ⌈784·max/663⌉ is D14(1), valid for all n ≥ 2. `tree_norm` = ⌈max V/(1−θ)⌉ over every leaf with al+bl ≤ 1, tangent leaves included, and only if θ < 1 everywhere. This is D19(1).
- **Corner below 256 (lines 93–97).** Strict q > M·p_hi⁴·max(1/32, κ⁴·9/512)/6 from three actual points at physical turns (1/(4n), 0), (0, 3/(16m)) and both. [D] The π/4 × 3π/16 rectangle contains the D32 premise-5 half diamond A+B ≤ 1/2 (π/4 > 1/2 and 3π/16 > 1/2).
- **Corner from 256 (lines 25–28, 90–92).** The E12 identity with no actual data. [I] E12(1): Λ_n(A,B) ≤ Λ_c − (A²+B²)/30 on the closed square [0, π/4]² for every n ≥ 256, at both corners. This contains the half diamond and is strict away from the origin. Root adopted it after a distinct ACCEPT. n = 255 cannot use it; the controls test this boundary.
- **Equality set.** This is D32's conclusion, not something the checker asserts. The corner patches, strict FAR/NEAR leaves and f leaves cover every center class without a gap.
  - [D] NEAR leaves lie in ρ < 1/2, inside the corner patch.
  - The corner phases with 1/2 ≤ ρ < π/2 lie in FAR leaves (S < L ≤ Λ_c) or in f leaves.

**The f leaf (lines 36–47, 126, 178–182).** [I]+[D]

- **Guard.** The leaf is accepted only if all of these hold: n is an integer ≥ 192; the box is a positive closed exact-rational unit box; and 1/2 ≤ al+bl ≤ 1.
- **Normalization.** The box coordinates are a = |α|/π and b = |β|/π, so ρ/π = a+b.
  - al+bl ≥ 1/2 is the minimum of a+b over the whole closed box, so ρ ≥ π/2 everywhere on it.
  - On T, a+b ≤ 1, so ρ ≤ π.
  - al+bl ≤ 1 makes box ∩ T nonempty.
  - This is exactly E15's closed domain π/2 ≤ ρ ≤ π with |α/π|+|β/π| ≥ 1/2.
- **Straddling cells.** [D] A cell straddling ρ = π/2 has al+bl < 1/2 and is rejected; the comparison is exact Fraction arithmetic. Box parts above the hypotenuse carry no physical chart point (D32(5) requires ρ ≤ π) and are covered through the fold by other leaves.
- **Low degrees.** For n < 192, `analytic_far` returns False in the producer, and `decode` / `parse_essential` raise if an f leaf appears.
- **What E15 supplies.** S_n < Λ_c − 3/100 against the true Λ_c, so λ ≤ S < Λ_c at every center class in the leaf, corners included. No L or M is used.
- **Norm.** TREE is rejected whenever an f leaf is present, at three places (lines 146, 157, 166, plus `parse_essential` line 232). GRID is sound because D14 bounds S on all real phases.
- [E] The three f leaves at 511 are [1/4,1/2]², [0,1/2]×[1/2,1] and [1/2,1]×[0,1], each with minimum sum exactly 1/2. This matches the review.
- [D] For every n ≥ 192 the first f leaves appear in the same three positions, because the split-axis rule's choices do not depend on n there. The numeric work at 192–319 is confined to [0,1/4]×[0,1/2] and [1/4,1/2]×[0,1/4].

**Arithmetic exactness.** [I] All proof arithmetic uses Fraction.

- `exact_hex` requires a canonical, finite binary64 hex string and converts it with `F.from_float` (exact).
- `endpoint_record` (D09 controller) rejects nonfinite values and lower > upper.
- In verify mode no float enters any predicate. Timers are operational only.

## 2. Adversarial source review (task 2)

- **Producer/checker separation.** [I] There is no distinct arithmetic. `producer.py:3,16–19` imports `checker` and uses the same `leaf`, `analytic_far` and `vertices`, and "fresh verify" re-executes the same `C.verify`. Independence is at the level of execution and fresh oracle values only; `independent-checks-D36-result.md:91` already says so. My separate re-implementation (section 3c) agrees, which mitigates this for the seven degrees run (NOTE N1).
- **TREE/GRID selection.** [I] `select_norm` recomputes the grid norm, forces GRID when any f is present, and otherwise chooses TREE if Mt ≤ Mcoarse.
  - The producer uses Mcoarse for discovery. Since M_selected ≤ Mcoarse, every leaf stays valid, and verify re-checks with M_selected anyway.
  - Fresh verify preserves the input METHOD and tree and recomputes M from fresh values. It does not re-check that TREE was the minimum; soundness does not need that.
- **Possible silent acceptance.** [I] I found no path.
  - Worker exceptions set FIRST_FAILURE and re-raise (`engine.py:94–98`), giving a nonzero returncode.
  - `stage_run` passes only if rc = 0, no stop, complete reap, CPU ≤ budget and status COMPLETE (`engine.py:132`).
  - `essential_receipt` re-verifies the serialized document and requires equality (`engine.py:155`).
  - Final account `complete` = (no failure) and limit present. Any failure exits with SystemExit(1).
  - `verify` requires the retained key set to equal the needed set exactly, including all 13 grid keys in both methods, and requires 0 < L ≤ upper(0,0).
  - `minimum_used_floor` takes min() over an empty list if there are no numeric leaves; that raises (a false failure), never a false pass.
- **Proof size.** [I] `engine.py:157` rejects a payload of 16384 B or more, so the cap is strict and there is no truncation or splitting. Verify input must be < 16384 B (`engine.py:192`). The receipt embeds absolute paths, which makes its size path-dependent (MINOR M2).
- **Runtime identity.** [I]+[E] `build.py:8–10,49–56` takes libflint, libgmp and libmpfr from fixed paths and records their hashes, but never compares them with a pin. The `setup.py` digest check runs only when the files are missing (`runtime.py:66`). My run with non-pinned FLINT bytes was accepted (MINOR M1).
- **Controls.** [E] The frozen six-group synthetic controls ran inside each of my nine invocations: PASS, 0 native calls, about 0.09 CPU-s. They exercise schema and domain boundaries only.

## 3. Independent reruns (task 3)

**Environment.** [E]

- The pinned Debian packages could not be obtained: `deb.debian.org:443` returns a proxy 403 CONNECT denial.
- I fetched the same version strings from archive.ubuntu.com (`libflint19`/`libflint-dev 3.1.3-2`, `libmpfr-dev 4.2.2-1`) into a fresh directory. All three SHA-256 values differ from the pins because Ubuntu rebuilt them. For example, libflint19 is `9ffa7458…` against the pin `81ac3b20…`.
- I extracted them with `dpkg-deb -x` into the copy tree's runtime path. The resulting `libflint.so.19.0.0` is `8ac5baf1bc72…`.
- The rest is system software: libgmp.so.10.5.0 (6.3.0), libmpfr.so.6.2.1, glibc 2.39, g++ 13.3.0 (Ubuntu 24.04), CPython 3.13.18. The original fresh runs used g++ 14.2.0.
- **This is a recorded substitution, not the pinned runtime.**

**Isolation.** [E]

- I ran everything under `audit2/t1-run/repo/`, a tree built with `git archive HEAD` (read-only) containing only the needed code and evidence paths. This makes the engine's ROOT-relative build and runtime paths resolve inside my scratch area, not the repository.
- The engine's own `check_freeze` re-verified every frozen byte. Each output path is fresh and exclusive.

**Runs.** [E] Commands were run from the copy root. Each was wrapped by `tools/runner.py`, which records the exit code and RUSAGE_CHILDREN CPU.

| # | Command (python3 -E -S -B …) | Exit | CPU-s (wrapper) | CPU through summary | Result |
|---|---|---:|---:|---:|---|
|1|final_hybrid_engine/engine.py --mode produce --n 41 --output out/produce-n41 --run-once|0|5.419|5.408|PRIMARY_ACCEPTED, complete, no failure|
|2|… --mode verify --n 41 --certificate evidence/final-hybrid-validation/primary-41.json --output out/verify-primary-n41|0|5.606|5.599|FRESH_…_ACCEPTED|
|3|… --mode produce --n 511 --output out/produce-n511|0|5.737|5.727|PRIMARY_ACCEPTED|
|4|… --mode verify --n 511 --certificate …/primary-511.json --output out/verify-primary-n511|0|6.087|6.077|FRESH_…_ACCEPTED|
|5–9|post_audit_D36_engine/engine.py --mode verify --n N --certificate evidence/post_audit_D38/primary-N.json --output out/d36-verify-nN, for N = 42, 63, 64, 159, 160 in order|0 each|5.226 / 5.701 / 5.133 / 6.812 / 7.066|5.219 / 5.694 / 5.127 / 6.805 / 7.059|FRESH_…_ACCEPTED each|

- An earlier attempt to use `/usr/bin/time` failed with exit 127 because the binary is absent. The engine was never invoked and no output path was created.
- The nine engine runs total 52.79 CPU-s. With downloads and my checker, the whole audit used under 1.5 CPU-min of the ~40-minute cap. No residual degree and no bulk run was launched.

**(a) Comparison with the review's counts.** [E]

- **41: TREE, M 13** (coarse M 15), 64 S / 3 actual / 101 nodes / 51 leaves, NEAR 5 / FAR 43 / OUTSIDE 3. Matches.
- **511: GRID, M 30**, 45 S / 0 actual / 51 nodes / 26 leaves, NEAR 6 / FAR 17 / ANALYTIC_FAR 3. Only the S kernel was built, with zero lambda builds or calls. Matches.
- My **produce** outputs equal the committed primaries in tree, all S upper hex values, actual hex values, origin-lower hex and the whole verification record.
- My **verify** outputs equal the committed fresh proofs in verification record and S rows.
- Each `original-certificate.json` snapshot hashes to the committed input. Final accounts are complete with no first failure. Controls and checker stages returned 0 with complete accounting.

**(b) D38 degrees.** [E] Every D36 verify verification record equals the committed `fresh-N.json`, and the S rows are identical:

- 42: TREE M 13, 60 S, 95 nodes;
- 63/64: TREE M 14, 49 S, 79 nodes;
- 159/160: TREE M 19, 45 S, 69 nodes;
- each with 3 actual calls and a positive corner gap.

This is a Claude-side independent execution of the five degrees, on a substituted runtime. The original D38 fresh executor was a distinct Codex/Astra reviewer.

**(c) Independent finite layer.** [E] `t1-run/tools/indep_check.py` (SHA-256 `77121911…`) does not import the engine. I wrote it from the D32/D14/D19/C02/D29/E15 statements.

- It decodes the tree and checks the leaf-area partition, then recomputes the fold, θ, GRID/TREE M, FAR/NEAR with the tier floors, the E15 guard, the strict corner test below the cutoff (256 for hybrid, 1024 for D36) and premise closure.
- I ran it on all 16 certificates: committed hybrid primary and fresh 41/511, D38 primary and fresh 42/63/64/159/160, and my produce receipts.
- Every assertion passed. M, leaf classes, every minimum NEAR/FAR margin and the corner gaps equal the recorded values exactly (e.g. corner gap at 41 = 78684125233892449/2474931954647040).
- The native Arb enclosures were trusted inputs to this check, not re-derived.

## 4. CPU accounting and reproducibility (task 4)

- [E] The review's sums match the committed accounts exactly: primaries 6.887400 + 7.353713 = 14.241113, fresh 6.287665 + 7.531237 = 13.818902, total 28.060015. Absolute self hard limits are 112 at 41 and 111 at 511, equal to ⌊120 − waited child CPU⌋ − 1.
- [E] My runs are 14–24% cheaper (5.41 / 5.60 / 5.73 / 6.08 CPU-s) and have hard limit 113. The cost is dominated by fresh compilation: at 41 the S build took 1.63 and the lambda build 2.14 of 5.41 CPU-s, while 67 native calls took 0.84 CPU-s.
  - Per-case CPU therefore tracks the compiler and host, not the mathematics.
  - These figures support neither a scaling law nor a Syvert2 forecast. The review itself says the same.
- [E] Reproducibility was strong: the proofs were bit-identical across compiler, Python, glibc and FLINT build bytes. [I] The weaker points are recorded under M1 and M2:
  - The committed essential receipts do not record library identities; only off-Git raw/build manifests do.
  - Receipt byte size varies with path length: 6645 B vs 6494 B at 41 for the same proof.

## 5. Behaviour at a residual degree, static analysis only (task 5)

- **Termination.** [I]+[D] The producer is a recursive DFS with no while loop. Every node becomes a leaf or splits once.
  - It raises at depth 18 with an unaccepted leaf, at the 2047th node and at the 257th unique S key.
  - Before each call it checks CPU (93 / 110 reserve); a completed call is capped at 10 CPU-s and an unfinished one at 15.
  - The supervisor has 0.25 s polling, wall limits 900/1000 s and group-CPU stops.
  - **It cannot loop.** Every cap is a first failure that consumes the attempt, with no retry. A capped run is a non-result, not a negative result.
- **Degree classes at 43–319.** [D] The tier constants at the residual degrees equal those at the proved neighbours (δ near the origin ≈ 0.03 at 43–62, about 0.049–0.05 at 65–158, 1/20 at 161–191). The D38 neighbours needed only 45–64 S calls and 69–101 nodes. This is plausibility, not a prediction.

  | Degrees | Corner | f leaves | Norm |
  |---|---|---|---|
  | 43–62, 65–158, 161–191 | actual three-point | none | minimum of TREE/GRID |
  | 192–255 | actual three-point | three | GRID forced |
  | 256–319 | E12 analytic, no lambda build | three | GRID forced |

- **Cost of forced GRID.** [D] GRID M is about 15% above TREE M (30 vs 26 at 511). It raises the corner threshold t ≈ 0.508·M, but D38's margins (q ≈ 65–93 against t ≈ 10–15) leave room.
- **Effective cap on certificate size.** [I]+[E] A certificate at the full S and node caps is estimated at about 15.6–15.7 KB, near the 16384 B cap. The cap can therefore bind before 256 S calls, especially with long paths (M2).

## 6. Finite degrees 2–42, 63–64, 159–160 (task 6)

[I] The chain:

- **2–32:** PD-T246 and others, via the PD-T210 certifier.
- **33–40:** `theory/native-finite-range.md` (PD-T210 predicates, committed certificates and independent replays).
- **41:** D34; also re-validated through the hybrid at 41.
- **42, 63, 64, 159, 160:** `theory/D38-calibration-global.md`, using the D36 engine, not the hybrid.

For each D38 degree the full requirement set holds:

- **Reduction:** D32 + C02/D29 + D19 + D08.
- **Arithmetic:** exact (outward Arb → binary64 → Fraction).
- **Checker:** committed D36 code under its FREEZE.
- **Evidence:** committed primary and fresh proofs and accounts, with direct-observation records (`code/post_audit_D38_review/verify-N-observation.json`).
- **Independent rerun:** done by a distinct reviewer, recorded EXIT 0, under the dated PROVED closure in D38; I have now repeated it (section 3b).

These are certified degrees, not calibration runs only. All five use the actual three-point corner and TREE norm, so they are model-free (no E12/E15/PD-T271 premise).

Residual count: 20 + 94 + 159 = **273**, which is consistent. **No residual degree has been run or proved by the hybrid.**

## Findings

| ID | Sev | Location | Finding / evidence | Recommendation |
|---|---|---|---|---|
|M1|MINOR|build.py:8–10,49–56; runtime.py:66|The arithmetic runtime's identity is recorded but not gated. Accepted runs [E1–9] used non-pinned libflint `8ac5baf1…` (pinned deb `81ac3b20…` unobtainable). The committed essential receipts carry no library identity; only off-Git raw/build manifests do. FLINT/Arb is declared a trusted dependency, so this is a provenance gap, not a soundness gap.|Record dependency SHA-256s in the receipt and/or compare them with a frozen expected set (the pack reportedly pins nine aliases; confirm the return verifier checks them). Otherwise state "recorded, not gated" in SPEC.|
|M2|MINOR|engine.py:154,157; checker.py:214,260|The receipt embeds absolute `freeze.path` and `whole_raw_evidence.path`, so size depends on checkout/output path length (+151 B in my run). Estimated ~15.6–15.7 KB at the S/node caps, against a strict 16384 B limit. A near-cap residual case could fail only because of a long Syvert2 path.|Use short pack paths, or repo-relative paths (would need a new freeze and audit). At least preregister the path-length assumption.|
|M3|MINOR|checker.py:31–33,191; engine.py:154|Every receipt, including n < 192 and the model-free 41, carries the E15 descriptor with its dependency list (E08/E07/E06/PD-T271), and 511 records "ANALYTIC_FAR: 3/100" among the "minimum strict margins". A reader can misattribute analytic dependencies to model-free degrees, or read the theorem gap as a numeric margin against L.|In results/report, give each future degree its dependency class (§5 table). Label the 3/100 as the E15 theorem gap versus true Λ_c.|
|M4|MINOR|Review recipe (independent-checks-final-hybrid-engine.md:499–583); runtime.py:66; phase_checker/setup.py:15|The registered fresh recipe needs prerequisites under the repo's `local-output/` and the Debian mirror. Neither is available in a new cloud session (deb.debian.org is policy-denied), and Ubuntu's same-version debs are different bytes. The recipe is therefore not reproducible as written without AC-side cold storage or another source of the pinned debs.|Archive the six pinned debs (or the extracted runtime) in Padua cold storage, or document an allowed mirror/host. Keep "use system versions" disclosed as a substitution.|
|N1|NOTE|producer.py:3,16–19|The producer and checker share arithmetic, and fresh verify reruns the same checker. Mitigated for 41/42/63/64/159/160/511 by my independent finite-layer re-implementation.|Consider adding the ~150-line independent finite-layer check to the pack's return verifier (milliseconds per certificate).|
|N2|NOTE|checker.py:167–171|TREE certificates retain the 13 grid premises, but besides (0,0) none is used by any TREE inequality. This is harmless and matches SPEC's "mandatory" policy.|None.|
|N3|NOTE|checker.py:108–113|The SPLIT branch is unreachable (proof in §1). It is dead code, inherited from D36.|None; optionally document it.|
|N4|NOTE|checker.py:187,191|`minimum_used_floor` includes floors computed for FAR leaves. Metadata only.|None.|
|N5|NOTE|—|Per-case CPU is compile-dominated and depends on the environment (§4). The review's arithmetic is exact.|Do not extrapolate costs.|
|N6|NOTE|—|Degrees 192–319 certified by the hybrid will inherit the E15 and, from 256, E12 chains, including computer-assisted PD-T271. 43–191 would be model-free.|Carry these dependencies in the PROVED statements.|

## Not tested / limitations

- **Runtime:** not run with the pinned Debian runtime bytes, nor with the original g++ 14.2 toolchain.
- **Native enclosures:** the Arb kernel's correctness was not re-derived; it is trusted as in the reviews.
- **Proofs:** I checked statements, domains and interfaces of D32, D29/C02, D14, D19, E12 and E15, not their full proofs. Those have their own accepted audits.
- **Failure paths:** kill, cap and timeout behaviour, the subreaper/ECHILD edge cases and the operational pack launcher were not exercised.
- **Out of scope:** no residual degree, bulk run, Syvert2 or remote job.
- **Supporting reviews:** D34, D35, D36-source, D37, D39 and D40 were read only at verdict level. The final-hybrid review was read in full from line 499, plus its section headers.

## Files (scratch, not in Git)

- Report: `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit2/t1-engine.md`
- Runs: `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit2/t1-run/` contains:
  - `out/{produce-n41,verify-primary-n41,produce-n511,verify-primary-n511,d36-verify-n{42,63,64,159,160}}`;
  - `log-*.json`, holding the exact argv, exit code and CPU per run;
  - `tools/runner.py` (SHA-256 `24d6fca6…`) and `tools/indep_check.py` (SHA-256 `77121911…`);
  - `debs/` (the Ubuntu .deb files).
- Receipt SHA-256 prefixes: produce-n41 `1b84178c` (6645 B), produce-n511 `31d04ffe` (6157 B), verify-primary-n41 `079d46cf`, verify-primary-n511 `20e9ce83`.
