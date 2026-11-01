# L2 — independent adversarial reconstruction 01 (rounds R01–R03)

## Header

- **Reconstructor:** Claude Opus 5.5 (`claude-opus-5-5`), effort xhigh, as assigned (adversarial reconstruction of a mathematical direction). I am not the L2 developer. I made no Git state changes.
- **What I wrote:** this file; scripts in `tracks/bivariate-lanczos/code/review_L2/` (9 files, listed under Reruns); logs in `reviews/logs_L2/` (≈ 150 KB). For items 1–3 and the independent ω/PRO reruns I imported nothing from `code/L1` or `code/L2`. I read the developer's code only to check what it computes. Developer commands were rerun separately and are marked "dev command".
- **Date:** 2026-10-31 ≈ 23:50 UTC to 2026-11-01 ≈ 00:35 UTC. The container clock is CET.
- **Branch:** `claude/bivariate-lanczos-20261031`. Head at start: `9378b68b5381dfd76e0571946847c29ffb4a2367`. Head during the reruns: `7c025a121d10d1ca99e9deacaae2b244e1619c3d`.
  - `git diff 9378b68 7c025a1` is empty over every audited L2 path (theory, directions/L2, code/L2) and over the rule files. Only one `plan.md` ledger row (L3 R01) changed.
  - `directions/L3/response-recon-02.md` is untracked; it is not in scope.
- **Read coverage:**
  - Read in full: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `directions/COMMON_RULES.md`, `plan.md` (re-read after the on-disk change), `state/IDEAS.md` (145 lines, two bounded chunks: seed rows 001–048, OBST-01..15, disposition table), `directions/L1/SUMMARY.md`, `directions/L2/R01.md`, `R02.md`, `R03.md`, `candidates.md` (including the post-hoc sections), `STATUS.md`, and the 11 theory files in scope.
  - Code: `code/L2/l2_core.py` in full; `l2_r01_sections.py`, `l2_r01_omega.py`, `l2_r01_verdicts.py`, `l2_r02_selection.py`, `l2_r02_pro.py`, `l2_r02_cost.py` and `l2_r03_dots.py` in full; `l2_r02_verdicts.py` not read. From `code/L1`, only the node constructions, `rotate` and the checkerboard weights.
  - Literature records: simon-1984-mathcomp, simon-1984-laa, larsen-1998, jia-li-2021, zhu-nakatsukasa-2026, and the heads of paige-1976 and paige-1980-lanczos.
  - Online (authorized):
    - arXiv 2001.04402 (Jia–Li), read via tool digest;
    - arXiv 2301.12241v2 (Zhu–Nakatsukasa, "ZN"), read via tool digest, twice;
    - Simon LAA 61 on ScienceDirect: refused (client error);
    - Stewart CS-TR-4246 bitstream (UMD DRUM): blocked (permission prompt not answered). URL: `https://api.drum.lib.umd.edu/server/api/core/bitstreams/a7a5b1b2-5bdf-4fd7-83d9-40b70ec19ca8/content`.
  - No fulltexts were stored in the repository.
- **Novelty scope:** the L2 records make no novelty claims. I checked candidate discipline and PD-N eligibility (§5), not literature novelty.
- **Memory:** none used.

| Audited file | SHA-256 |
|---|---|
| directions/L2/R01.md | `27ad8872b9f0b9d57dd85075bee96a2ebdbd9aa43d751e3f13033c480b91e6a9` |
| directions/L2/R02.md | `79803f8e175131a6db0c7899fbdc39672ad4ea06dbf39523bb2268d41905c877` |
| directions/L2/R03.md | `291ccea2967528811ec5ec6c809c1171ea0e626aeecb174dcc80979630620aa2` |
| directions/L2/candidates.md | `658f0f049ddd0d58d09089cf231e954ed1399577b0d2d87a48f8489f1971a057` |
| directions/L2/STATUS.md | `88655160c1575df405d00e6ebad7792fff9e9df5d2f8f3199b4d676119d51176` |
| theory/semi-orthogonality-implies-accurate-F-section.md (PD-T?…-201) | `6b107b3a6922ed3327ff65dc91fcc650de885fa68c51e2778f0a0db8372b1775` |
| theory/commutator-shadow-recursion-and-span-drift-bound.md (-202) | `acbb064ab03b23040edb74b27496b867cb3da090bdd0f0e73e85cfe1c6ce7699` |
| theory/omega-estimate-tracks-loss-measured.md (-203) | `b12ffb347d49ad500da87521617e1d811c3b3960870dcfe597c9736b05a5cba4` |
| theory/section-accuracy-and-two-pass-window-measured.md (-204) | `65113af686c10b83016f0b0546306a5fca43a186b5f379d57aeaa4c5376cdecd` |
| theory/coupled-section-residuals-general-selection.md (-205) | `6cae588ca01cbd50a37acb0c85b313d107207d402835d2a423e5768e5713c8dd` |
| theory/selection-rules-and-span-drift-measured.md (-206) | `99cf4e44e1118cf10d0588cff8b83236c6840299a7a246aaf6e0ade9c1c4accb` |
| theory/pro2d-strategy-and-cost-measured.md (-207) | `44d975cfae1be7827c0c5756764a701ed9fd1cba30f338b1152351ddf985bb17` |
| theory/reorthogonalization-does-not-restore-graded-spaces.md (PD-N?…-201) | `f84d5b97e87f84cc698d909123af939faabe4ea69b4f065cda673914afa6fba2` |
| theory/pro2d-rounding-only-trigger-fails.md (PD-N?…-202) | `37abe6b9e6cf0dc1a53f00f45d9015763e15ba5f6714fec4bfd8632832441439` |
| theory/one-relation-selections-do-not-keep-spans-near-Sn.md (PD-N?…-203) | `50190e070041cc3dd70641750b88bfac98a6fb45e24339e3ffd9d9b7831766b1` |
| theory/exact-window-dots-do-not-remove-coefficient-channel.md (PD-N?…-204) | `c27f9a3021e0d35aeb67c12c5541fc4ae0de269bbff68c73e499da79da11c4ed` |
| code/L2/l2_core.py | `e8c8fa3378b3531f4fc13faac9902757b97c92c281b2bcd2c02875e0b1c5638d` |
| code/L2/l2_r01_omega.py / l2_r01_sections.py / l2_r01_verdicts.py | `a6b6a981…c875ca` / `25fb34ec…b0b84` / `16f0e4ac…2938d` |
| code/L2/l2_r02_cost.py / l2_r02_pro.py / l2_r02_selection.py / l2_r02_verdicts.py / l2_r03_dots.py | `cc55b06c…fabdf` / `21892f7f…b91eb17` / `3d532822…200cb6ee` / `9ebb6666…2182038` / `a728b100…f933f7` |
| logs r01_omega / r01_sections / r01_sections_w2 / r02_pro / r02_proJ / r02_selection / r03_dots (.raw.gz) | `b1cfd1a3…1e6` / `8f16939c…c61` / `106495bc…e89` / `b5b6a38e…7c3` / `4609986b…14c` / `642d044e…227` / `d89f1680…7d1` |

## Verdict summary

| Claim | Developer status | Verdict (scope) |
|---|---|---|
| PD-T?…-201 Theorem A, Prop. L, Cor. A′ | PROVED | **CONFIRMED.** Theorem A is exact and was stress-tested on 35 instances with no violation (worst LHS/RHS = 0.16). Prop. L(b) and Cor. A′ are first-order. There is one minor gap (A′ applied with reorthogonalization). |
| PD-T?…-202 parts 1–5 | PROVED | **CONFIRMED.** Parts 2–3 check exactly (rational residual 0). Parts 1 and 4 check to 1e-81. Part 5 holds in every case. One wording note on the title. |
| PD-T?…-205 | PROVED "for any one-relation selection" | **CONFIRMED WITH CORRECTIONS.** The recursion defining Ĥ_A is circular unless condition (C) holds; see F1. (C) holds for dev, mirror and alt. It fails for 'adapt' from degree 3 on 4 of 5 tested sets. |
| PD-N?…-201 (span drift) | MEASURED | **CONFIRMED.** The drift is real. With well-conditioned extended-precision references it is 3.6e-3 (rotπ/4, n = 24) and 1.3e-2 (triangle, n = 20), and it scales with the working precision. It is not a reference or conditioning artefact. |
| PD-T?…-203 (ω-estimate) | MEASURED | **CONFIRMED** on rotπ/4, triangle and the cubic checkerboard, reproduced digit-for-digit with independent code. The title overstates the underestimate bound (F5). |
| PD-T?…-204 | MEASURED | **CONFIRMED** for the parts re-measured (triangle, rot0.3, rotπ/4). |
| PD-T?…-206 / PD-N?…-203 | MEASURED | **Partly re-measured:** dev and mirror rules agree. alt, adapt and two-relation not rerun. Verdicts unaffected by F1. |
| PD-T?…-207 | MEASURED | **CONFIRMED WITH CORRECTIONS:** (a) and the cost ratios reproduce exactly; the M-scaling wording and the title range need fixing (F4, F6). |
| PD-N?…-202 | MEASURED | **CONFIRMED** (dev command, rotπ/4 and triangle). |
| PD-N?…-204 | MEASURED | **CONFIRMED** (dev command, cubic checkerboard and rotπ/4). Title "17–19×" should be "14–19×". |

---

## 1. PD-T?…-201 (2D Simon theorem, F-part)

### Reconstructed statement

The setting is the BJ ordering with F = Y and a block window. For every column c of degree ≤ n−1 with F-child k, the relation is

  β_k q̂_k = Fq̂_c − Q̂_W h − Q̂_L g − f_k.

This only *defines* f_k, so (H1) holds for any full-rank Q̂ and any coefficients. Then FQ̂_{n−1} = Q̂(T + G) + E exactly. With Ω = Q̂ᵀQ̂ − I, R = chol(I + Ω), W = Q̂R⁻¹ and S = W_nᵀFW_{n−1}:

  max|S − T| ≤ 2ε_c + 2(μ₁ + η²)τ₁ + ηγ + 2η²(‖T‖₂ + ‖G‖₂)/(1 − η) + 4‖E‖₂.

**Which notion of semi-orthogonality is used:**

- **Theorem A** uses η = ‖Ω‖_F, which is *normwise* over all pairs, including the diagonal. It requires η ≤ 1/4.
- **Local level μ** is *entrywise* over pairs a ≠ b with |deg a − deg b| ≤ 2. For the block window these are exactly the pairs (l, k) with l ∈ W_k.
- **Prop. L(b)** uses ‖Ω_W‖₂ ≤ η.
- **Cor. A′** assumes η ≤ √u (Frobenius).
- **The kill test** uses *entrywise* L(n) = max|Ω| ≤ √u over all pairs. That only gives η ≤ N√u, so Theorem A's η² terms become O(N²u). The developer says so in the Scope section.
- **Consequence:** "PD-T?…-204 is the pattern Theorem A predicts" holds only up to polynomial factors. The measured e_F ≈ 2e-16 is far below the bound.

### Proof check

I re-derived the proof line by line:

- Lemma 1 (exact decomposition).
- Lemma 2: the continuity argument along tΩ is valid; the root gap is ≥ 1 for η ≤ 1/4; x₋(1) ≤ 0.83η.
- Lemma 3 (profile preservation).
- The two block-window facts.
- Every region:
  - (I): r > child(c);
  - (II): c ≤ r ≤ child(c). The degree bookkeeping deg a − deg r ≤ 1 and deg c − deg b ≤ 1 is correct.
  - (IVa): uses symmetry of the square part. (ΩT)_{cr} involves only local pairs, because deg a ≥ deg r − 1 ≥ deg c − 2.
  - (IVb): |T_cr − T_rc| ≤ 2ε_c, because q̂_rᵀFq̂_c = q̂_cᵀFq̂_r exactly.
- The regions cover every (r, c). G enters only through symmetry: S_rc = Ẽ_cr for r ∈ L, which is why the theorem compares S with T and not with T + G.

I found no error. The constants are explicit and modest.

### Counterexample search (`rl2_thmA.py`, all quantities in x87 long double, own Cholesky and triangular solves)

There were 35 evaluated instances; one was skipped because η = 0.83 > 1/4. **No violation was found.** The worst ratio was LHS/RHS = 0.161 (float32, rotπ/4, n = 6); the range was 4e-3 to 0.16. The local term dominates in 29 instances, 4ε in the out-of-span injections.

| Family (data-generating run, all BJ) | Degrees | LHS / RHS |
|---|---|---|
| triangle, one-pass window, double | 6–12 (μ = 1.7e-13 … 4.7e-8) | 0.039–0.049 |
| triangle, two-pass window, double | 8–16 | 0.004–0.095 |
| rot0.3 / rotπ/4, one-pass window, double | 16–24 / 16–22 (η up to 6.4e-4) | 0.004–0.088 |
| rotπ/4, CGS2-all | 16, 24 | 0.096–0.12 |
| float32 runs (rotπ/4, triangle) | 4–12 (μ up to 2.4e-3) | 0.006–0.16 |
| injected coefficient inconsistency σ = 1e-8, 1e-6, 1e-3 (f_k at rounding, μ and ε_c ≈ σ) | 4–12 (η up to 0.20) | 0.006–0.14 |
| injected out-of-span errors σ = 1e-8, 1e-5 | 4–12 | 0.014–0.020 |

The measured e_F values agree with the developer's: triangle one-pass n = 8 gives 2.0e-12, n = 10 gives 1.45e-10 (developer 1.4e-10), both at semi-orthogonal degrees. rot0.3 one-pass n = 20 gives e_F = 7.9e-11 at L = 9.6e-9.

### Prop. L and Cor. A′

- **Prop. L(a)** is an exact identity.
- **Prop. L(b)** holds to first order. The key point is that h⁽²⁾ = −Ω_W h⁽¹⁾ + O(γ_M‖â‖), so the window residual is ‖Ω_W‖²‖h⁽¹⁾‖, with no induction over earlier columns.
- **Measured:** with two passes, μ ≤ 1.9e-16 while η reaches 1.1e-7 on the triangle. So μ ≪ η², consistent with the proposition and far from tight.
- **Cor. A′** follows from these. Its gap is F8.

### Comparison with Simon (as available)

- **Simon Math. Comp. 1984, Thm 2** (record LIT?…-211; digest only): qualitative ("up to roundoff"), with entrywise κ_j ≤ √u. The proof is deferred to PAM-74.
- **Simon LAA 61, Thm 5:** not reachable (ScienceDirect refused).
- **Jia–Li 2021** (arXiv digest), restating Simon's template for joint bidiagonalization:
  - the semi-orthogonality threshold is entrywise, ω₀ = √(ε/(2k+1));
  - local orthogonality β_{i+1}|u_{i+1}ᵀu_i| = O(ε) is part of the error model (their (2.11));
  - vectors have unit length;
  - the conclusion is entrywise O(q̃ε).

So in the template, too, local orthogonality is an explicit hypothesis; in 1D it is automatic (Paige). The developer's version differs in four ways:

- the Frobenius η replaces the entrywise level;
- local orthogonality is an explicit hypothesis that the 2D window cascade can break, and the two-pass window supplies it;
- the bound is exact rather than first-order;
- the bound is fully explicit.

None of these is a defect. The file correctly claims no proof dependence on Simon.

**Verdict:** CONFIRMED (Theorem A, Prop. L(a): exact; Prop. L(b), Cor. A′: first-order standard model, as stated).

---

## 2. PD-T?…-202 and PD-T?…-205

### Exact checks (`rl2_exact.py`)

The test case has M = 24 random nodes, random weights in [0.5, 1.5] and n = 4 (N = 15). The double runs are converted to exact rationals, and f_k is defined by each relation.

| Run | 205 parts 1–2 | 202.3 shadow / K(t,0) / Gram identity | 202.1 (80 digits) | 202.4 | 202.5 |
|---|---|---|---|---|---|
| BJ one-pass window | 0 (exact) | 0 / 0 / 0 | 1.6e-81 | ≤ 9.4e-82 | holds, s = 0..3 |
| BJ CGS2-all (L ≠ ∅) | 0 | 0 / 0 / 0 | 1.6e-81 | ≤ 1.3e-81 | holds |
| BJ window + partial (random L, 2 passes) | 0 | 0 / 0 / 0 | 1.6e-81 | ≤ 8.4e-82 | holds |
| BJ one-pass + out-of-span noise 1e-3 | 0 | 0 / 0 / 0 | 1.2e-81 (‖lhs‖ = 1.1e-3) | ≤ 4.2e-82 | holds: δ_J/(2‖J‖) = 1.6e-4 … 5.5e-4 ≤ max θ = 1.0e-3 … 4.6e-3 |
| alt CGS2-all; alt partial + noise | 0 | n/a | n/a | n/a | n/a |

So parts 1–5 of 202 hold as stated, including the Γ form (not Ω) of the ω-identity that the file insists on. The drift bound is informative within about 5–10× here, and within 6–15× on the benchmarks (§3).

### What θ measures

θ_s = ‖Π̂_s − P_s‖₂ is the sine of the largest principal angle between the computed Ŝ_s and the exact S_s; their dimensions are equal under U(s) and full column rank.

The reported θ_LB(n) = max_{s<n} δ_A(s)/(2‖A‖) is a lower bound for **max_{s≤n} θ_s**, not for θ_n. This matters in principle: for M = N_n sets, θ_n = 0 trivially. PD-T?…-206 and PD-N?…-201 call it a bound on "the principal angle to S_n"; F7 records the wording fix.

The δ_A in the code are computed from the Householder Q-factor of Q̂ (nested spans). This is valid: any unit vector of Ŝ_s gives a lower bound.

### PD-T?…-205 well-definedness — finding F1

The definition of an unformed column is

  Ĥ_A e_m := (Ĥ_{B_m} Ĥ_A e_{p(m)} − Σ h Ĥ_A e_l − …)/β_m.

Suppose m was created by A itself (B_m = A) and A·m is not formed. Then Ĥ_A e_{p(m)} is the formed column whose child is m, so (Ĥ_A e_p)_m = β_m. The right-hand side then contains β_m Ĥ_A e_m, and the defining equation reduces to 0 = (rest): it is self-referential and determines nothing. In operator terms, commuting A past A gains nothing.

The file's claim "the recursion is well defined when processed by degree … unformed ones computed in increasing j" is therefore false in general.

`rl2_cycles.py` (exact combinatorics on supports, block window) tests this:

- **Exhaustive enumeration for n = 2..5** (2, 8, 64, 1024 selections): the recursion is well defined **if and only if** condition (C) holds. (C) says: every unformed A-product belongs to a column whose creator is the other operator. (C) holds for only 2, 4, 8, 16 selections at n = 2..5.
- **Random sampling, n = 6..9** (3000 each): no (C)-selection had a cycle, and no non-(C) selection was well defined.
- **Named rules:** dev (BJ), mirror and alt satisfy (C) and are well defined up to n = 20.
- **'adapt'** (own implementation of the rule in PD-T?…-206, both variants): (C) fails from degree 3 on rotπ/4, rot0.3, the disk and the square. It holds on the triangle up to n = 20.

**Impact:**

- Parts 1–3 of 205 hold, verified exactly, for (C)-selections (BJ, alt).
- Part 4's drift bound does not use Ĥ at all; it holds for any computed nested spans. Hence PD-T?…-206 and PD-N?…-203, which only use θ_LB, are unaffected.
- What breaks is the PROVED scope "for any one-relation-per-column selection".
- The R02 next step "a version of the ω-estimate for selections where both sections are partly implicit (PD-T?…-205)" does not exist for 'adapt' in this form.
- Acyclicity under (C) is supported by the exhaustive check for n ≤ 5, not proved.

**Verdicts:**

- PD-T?…-202: CONFIRMED. Wording note: the title's "reorthogonalization does not reset it" is an interpretation of part 3. Part 3 shows only that g enters as coefficients; that K stays large is MEASURED (PD-N?…-201, and my rerun: |K| = 6.8e-4 under CGS2-all on rotπ/4, n = 24).
- PD-T?…-205: CONFIRMED WITH CORRECTIONS. Restrict the statement to (C)-selections, and prove acyclicity under (C) or label it as checked.

---

## 3. PD-N?…-201 — is the span drift real? (priority)

### Setup (`rl2_drift.py`, `rl2_drift_D.py`, `rl2_sections.py`; own code throughout)

- **Algorithms:**
  - BJ selection with CGS2 against all previous columns;
  - BJ with one-pass and two-pass windows;
  - the mirror selection;
  - BJ + CGS2-all in double **and in x87 long double** (u_LD = 2⁻⁶⁴ ≈ 5.4e-20).
- **Equivalence with ZN's V+A (from the paper text):** ZN 2026's Algorithm 3 orthogonalizes against all previous columns with two CGS passes. Its Remark 3.2 rule is "the smallest k with I[l+1] = I[k] + e_r", and its grevlex example is (0,0), (1,0), (0,1), (2,0), (1,1), (0,2), …. This rule *is* the BJ selection: x^a y^b = y · x^a y^{b−1} for b ≥ 1, and x^a = x · x^{a−1}. So the developer's "fullcgs2 (V+A type)" is ZN's multivariate V+A in grevlex order, up to the 1/M scaling. This is established from the paper text via digest, **not** checked against ZN's code.
- **References for S_n:**
  - **R1:** Legendre product basis in the unrotated frame. The coordinates are computed in long double from the double nodes; S_n is invariant under the linear change of variables. Orthonormalized by my own Householder QR in long double.
  - **R2:** Chebyshev product basis, unrotated frame, long double.
  - **R3:** the R1 basis with LAPACK QR in double.
  - **R4:** the developer's pre-registered reference (box-frame Chebyshev, double).
  - **Triangle:** Koornwinder–Dubiner basis (own homogenised Legendre and Jacobi recurrences), in long double.
  - **L-shape and annulus:** box Legendre basis in long double.

### κ of the column-normalised weighted Vandermonde (rotπ/4, M = 1681)

| Basis | n = 8 | 12 | 16 | 20 | 24 |
|---|---|---|---|---|---|
| R1 Legendre, unrotated | 2.1 | 4.6 | 18 | 1.1e2 | **7.8e2** |
| R2 Chebyshev, unrotated | 8.1 | 25 | 1.0e2 | 5.7e2 | 4.3e3 |
| R4 box Chebyshev (pre-registered) | 1.3e4 | 2.0e6 | 3.0e8 | 5.2e10 | **9.2e12** |
| monomials, unrotated | 5.1e2 | 1.9e4 | 7.1e5 | 2.8e7 | 1.1e9 |

- **Reference agreement:** the largest-angle sine between R1 and R2 is ≤ 2.7e-15 for every n ≤ 24; R1 vs R3 is ≤ 1.1e-13.
- **The pre-registered reference is itself wrong:** R1 vs R4 is 3.2e-8 at n = 16, 5.4e-6 at n = 20 and **9.0e-4 at n = 24**, close to its u·κ. This confirms the developer's disclosure that the pre-registered reference was non-discriminating.
- **S_n is well-conditioned.** With κ ≤ 7.8e2 (1.9 at M = 10⁵), a data perturbation of size u moves S_24 by ≲ n²uκ ≈ 5e-11. The exact-arithmetic answer is *not* sensitive.

### Drift (sine of the largest principal angle to S_s; identical against R1, R2 and R3 to all printed digits)

| rotπ/4, M = 1681 | s = 16 | 20 | 22 | 24 | θ_LB(24) |
|---|---|---|---|---|---|
| BJ + CGS2-all, double (ZN V+A grevlex) — loss 4.4e-16 | 3.3e-9 | 3.5e-6 | 1.1e-4 | **3.6e-3** | 2.5e-4 |
| BJ + CGS2-all, long double — loss 2.0e-17 | 2.5e-12 | 3.7e-9 | 1.6e-7 | **7.7e-6** | 5.3e-7 |
| BJ one-pass window, double — loss 4.2e-3 | 3.1e-9 | 3.4e-6 | 1.2e-4 | 4.5e-3 | 3.1e-4 |
| BJ two-pass window, double — loss 2.5e-4 | 2.8e-9 | 3.4e-6 | 1.3e-4 | 5.5e-3 | 3.8e-4 |
| mirror + CGS2-all, double | 7.3e-8 | 3.4e-4 | 3.3e-2 | **0.96** | 1.6e-1 |
| mirror + CGS2-all, long double | 4.5e-11 | 2.6e-7 | 2.4e-5 | 1.9e-3 | 3.3e-4 |

The developer's values on the same node set are: drift_unrot 4.1e-3, θ_LB 2.8e-4 (fullcgs2); 4.5e-3 (plain, bitwise the same run as mine); mirror 0.94 and 1.6e-1. My CGS2-all run differs by rounding realization only. The developer slices Q[:, :k] as a view; I copy it with fancy indexing; the BLAS paths differ.

**Scaling with precision.** The ratio of long-double to double drift for BJ is 6.5e-4 (s = 12), 7.6e-4 (16), 1.1e-3 (20) and 2.1e-3 (24). For mirror it is 7.6e-4 at s = 20. Compare u_LD/u = 2⁻¹¹ = 4.9e-4. The span angle between the double and long-double runs equals the double drift at every s. The drift is therefore a rounding-error amplification, linear in the working precision within a factor ≤ 4.4. That factor is well inside the realization variance below.

**Triangle** (M = 1681, n = 20; κ(KD) = 1.9 / 4.7 / 18 / 1.0e2 at n = 8 / 12 / 16 / 20; box Legendre κ = 1.7e14). The two Koornwinder–Dubiner references (long double vs double) agree to ≤ 1.5e-14.

| Run | s = 12 | 16 | 18 | 20 | θ_LB(20) |
|---|---|---|---|---|---|
| BJ + CGS2-all, double | 6.9e-10 | 2.5e-6 | 1.9e-4 | **1.3e-2** | 9.8e-4 |
| BJ + CGS2-all, long double | 4.2e-13 | 1.4e-9 | 1.2e-7 | 8.1e-6 | 6.1e-7 |

The developer reports 1.0e-2 and 7.8e-4.

**L-shape and annulus** (M = 3000, BJ + CGS2-all, long-double box-Legendre reference). There the developer could use only θ_LB.

| Set | s = 24 | 28 | 30 |
|---|---|---|---|
| L-shape: drift / θ_LB / κ (u_LD·κ) | 9.8e-6 / 1.2e-6 / 1.8e11 (1e-8) | 3.2e-3 / 3.8e-4 / 2.6e13 (1.4e-6) | 7.1e-2 / 1.1e-2 / 3.5e14 (1.9e-5) |
| annulus | 6.5e-6 / 5.8e-7 / 8.2e8 | 2.9e-3 / 2.2e-4 / 4.0e10 | 0.16 / 1.1e-2 / 2.9e11 |

The developer's θ_LB values are 8.7e-3 and 1.3e-2.

**M-dependence** (fresh uniform squares rotated by π/4, seeds 1–3, R3-type reference with κ printed in the log):

| M | κ(24) | drift s = 16 | s = 20 | s = 24 |
|---|---|---|---|---|
| 1681 | 2.4e2–2.7e3 | 1.8e-9 – 2.7e-9 | 8.5e-7 – 4.3e-6 | **3.9e-4 – 2.0e-2** |
| 10⁴ | 10–14 | 1.7e-9 – 2.6e-9 | 1.2e-6 – 2.3e-6 | 7.5e-4 – 3.4e-3 |
| 10⁵ (2 seeds) | 1.9–2.0 | 1.9e-9 – 2.0e-9 | 8.3e-7 – 9.5e-7 | **6.3e-4 – 7.2e-4** |

The drift does not decay towards √u. At s ≤ 16 it is M-independent. At s = 24 the seed spread at M = 1681 is 50×, and the values settle near 7e-4 by M = 10⁵. That M is about N², i.e. ZN's recommended sampling regime.

**Sections and controls** (`rl2_sections.py`, long-double evaluation, BJ + CGS2-all):

| Case | e_H | e_τ | e_F | max\|K\| | Other |
|---|---|---|---|---|---|
| rotπ/4, n = 16 / 20 / 24 | 1.4e-10 / 2.0e-7 / **4.9e-4** | ≤ 1.8e-16 | 1.7e-16 | 6.8e-4 (n = 24) | F-defect 1.3e-15 |
| triangle, n = 12 / 16 / 20 | 4.4e-11 / 2.3e-7 / **9.5e-4** | ≤ 1.2e-16 | ≤ 1.3e-16 | — | — |
| tensor 41², n = 39 | — | — | — | — | θ_LB 8.3e-15 (developer 8.3e-15); drift against the exact reference (κ = 1.00) 1.1e-14 |

The developer reports e_H = 2.8e-4 (rotπ/4) and 8.4e-4 (triangle).

**Verdict:** the drift is real. It is not a reference artefact: two independent well-conditioned extended-precision references agree to 1e-15. It is not a conditioning artefact: κ ≤ 8e2, and the drift is linear in the working precision. It also follows independently from the proved reference-free bound. **PD-N?…-201 is CONFIRMED.**

- **(a) and (b):** reproduced on rotπ/4 and the triangle.
- **(c):** reproduced (3.6e-3 vs 4.1e-3).
- **(d):** tensor control reproduced.
- **Additions recommended for PD-N?…-201:**
  - the extended-precision reference results, which turn the post-hoc kill into one that any well-conditioned reference gives (the pre-registered verdict stays "inconclusive");
  - the identification of BJ + CGS2-all with ZN's V+A in grevlex order, flagged as unverified against their code. ZN's reported experiments are on a tensor domain and an ellipse; product type and the disk have small drift, so there is no conflict.
  - the realization variance (F4).

---

## 4. MEASURED claims and the frozen kill test

### Reruns

- **ω-estimate, independent code** (`rl2_omega.py`: own BJ run, own causal replay of E1 (5 seeds, median) and E1D). It reproduces the developer's numbers digit-for-digit; my one-pass run is bitwise identical to the developer's. The developer's cubic E1 U = 0.006 differs from my 0.0022 only through the double-Gram floor of L at small n; the verdict is unaffected.

| Set | E1 U / O | E1D U / O |
|---|---|---|
| rotπ/4 | 0.495 / 4.61 | 0.299 / 6.49 |
| triangle | 1.06 / 5.58 | 3.85 / 5.68 |
| cubic checkerboard | 0.0022 / 2.43e5 | 0.0015 / 2.74e5 |

- **PRO-2D-J, independent implementation:**

| Set | max L | reorth columns | total / CGS2-all | (reorth + measure) / CGS2-all | e_F at SO degrees |
|---|---|---|---|---|---|
| rotπ/4 | 7.6e-9 | 81 | 0.57 | 0.33 | ≤ 2.0e-16 |
| triangle | 4.3e-9 | 73 | 0.71 | 0.42 | ≤ 1.7e-16 |
| cubic checkerboard | L(29) = 2.0e-7: **kill at n = 29** | 61 | 0.31 | 0.11 | — |

  All three rows agree with the developer's log.
- **Developer commands:** `l2_r01_omega.py rotpi4 triangle`, `l2_r02_pro.py --jmeasure rotpi4 triangle cb_cubic`, `l2_r02_pro.py rotpi4 triangle` (PD-N?…-202: kills at n = 24 and 19–20) and `l2_r03_dots.py cb_cubic rotpi4` (PD-N?…-204). All 79 non-timing output lines are verbatim in the committed logs.
- **PD-T?…-204:**
  - local channel on the triangle: L(n) = μ(n) at n = 6–12;
  - two-pass window: μ ≈ 2e-16; triangle loss 1 → 7.4e-5; rotπ/4 4.2e-3 → 2.5e-4;
  - one-pass e_F > u^{3/4} at SO degrees on the triangle and rot0.3.

  All re-measured.

### Frozen L2-Q1 kill test as written

- **Clause (i), "underestimates by > 10× on any benchmark":** not fired. The developer's restriction to informative degrees is necessary; at rounding level the double-Gram floor alone would give L/E ≈ 60. The question's "within a constant factor" fails on the cubic checkerboard (overestimate 2.4e5, reproduced). The kill test does not test that side, and R01 reports it correctly.
- **Clause (ii), "a semi-orthogonal run with section error ≫ u":** **fires**, reproduced with my own runs:
  - J-sections: e_H = 4.9e-4 at loss 4e-16;
  - F-sections with one pass: e_F = 2.0e-12 and 1.45e-10 at L ≤ √u.

  The F-part survives only as a new claim with an added hypothesis (Theorem A plus local orthogonality). That is disclosed in R01 §3 but misreported in plan.md (F2).

### Cost accounting (PD-T?…-207 (d))

- Counts reproduce exactly (window 12 676; CGS2-all N(N−1) = 105 300).
- PRO-2D-J measures each J-row twice: once on the provisional r/β₀ (len O) and once on the final q̂_k (k). The provisional pass is redundant when nothing triggers. That is about n³/6 extra dots (≈ 2% of CGS2-all, 4.4% of total) — a minor inefficiency, honestly counted.
- PD-T?…-203 (d): "O(N²·n) flops with dense storage" is inconsistent. The dense replay as coded is O(N³) per run; O(N² n) needs T's band sparsity. It is still M-independent.

---

## 5. Protocol

- **Kill-criteria precedence:** IDEA?…-204's pre-registered rule gives "inconclusive". The kill rests on the post-hoc reference-free bound and the post-hoc unrotated reference, and this is disclosed in candidates.md, R01 §5 and PD-N?…-201. My extended-precision references now give the same verdict under the pre-registered *form* of the rule with a well-conditioned reference. Report the pre-registered verdict first, the post-hoc ones second, and this independent confirmation third. IDEA?…-209 was written after -208's smoke test and is disclosed.
- **Status labels and splits:** see F1 (205 scope) and F3 (PD-N for evidenced failures). 202 and 201 keep MEASURED parts by cross-reference to PD-N?…-201 and PD-T?…-204, which is acceptable.
- **PD-N eligibility (WORKFLOW L5 rule):**
  - PD-N?…-201 through -204 each house a failed mechanism with a scoped negative statement and evidence: eligible.
  - Gap: three other evidenced failures with disposition REJECTED: failed live only inside MEASURED PD-T files (F3).
- **R01.md:** "branch head SHA not recorded". The orchestrator should record it; the heads are given above.

## Findings by severity

| # | Severity | Location | Finding | Requested response |
|---|---|---|---|---|
| F1 | **High** (PROVED claim with a false quantifier) | PD-T?…-205, Statement and the sentence "the recursion is well defined …" | The Ĥ_A recursion is self-referential whenever an unformed A-product belongs to a column created by A. Exhaustively (n ≤ 5), well-defined ⟺ (C). 'adapt' violates (C) from degree 3 on rotπ/4, rot0.3, the disk and the square. | Restrict to (C)-selections (dev, mirror and alt qualify). Prove acyclicity under (C) or label it MEASURED (checked exhaustively for n ≤ 5). Note that part 4's drift bound needs no Ĥ. Fix R03 §7 and PD-T?…-206 Open items accordingly. No measured verdict changes. |
| F2 | Medium | plan.md round ledger, L2 R01 row | "Kill test not fired" is wrong: clause (ii) of the frozen kill test fired (J-sections everywhere off product sets; F-sections with one-pass windows). "J-part obstruction PROVED" is also wrong: the identity is PROVED, the obstruction is MEASURED (PD-N?…-201). The F-theorem needs local orthogonality, which the row does not say. | Correct the row. R01.md §3 already states it correctly. |
| F3 | Medium | candidates.md dispositions; PD-T?…-203 (b), -204 (a), -207 (a) | Three REJECTED: failed candidates with evidence have no PD-N of their own: IDEA?…-205 (E3), the one-pass F-part of IDEA?…-203, and IDEA?…-209 (killed on the cubic checkerboard). This conflicts with "a separate evidenced mechanism failure still gets its own PD-N" and with the split rule. IDEA?…-209 is "REJECTED" while PD-T?…-207 presents it as the L2 strategy. | Create scoped PD-N files or record why not. For -209, a narrowed successor candidate (non-clustered sets) would remove the tension. |
| F4 | Low–Medium | R02 §3 table ("BJ drift M-independent to M = 10⁵"), PD-T?…-207 (c) | The developer's own data decrease by about 6× over M = 1681 → 10⁵ at n = 24. My seeds show a 50× spread at M = 1681 and convergence to ≈ 7e-4. | Say "does not decay with M; ≈ 6–7e-4 at n = 24 for M = 10⁵ (2 seeds); M-independent at n ≤ 16". |
| F5 | Low | PD-T?…-203 title | "never underestimates the loss by more than 1.5×" is contradicted by E1D, U = 3.85 (triangle), in its own table. | Restrict to E1/E2/E2D/E3, or say 3.9×. |
| F6 | Low | PD-T?…-207 title vs (a); PD-N?…-204 title vs (b) | "13–70%" vs 0.16–0.71; "17–19×" vs 14–19×. | Align. |
| F7 | Low | PD-T?…-206, PD-N?…-201 (b) | θ_LB is described as a bound on "the principal angle to S_n". It bounds max_{s≤n} θ_s. | Reword. |
| F8 | Low | PD-T?…-201 Cor. A′ | Prop. L(b) is proved for L_k = ∅, but A′ is applied to runs with reorthogonalization (window, 2 L-passes, then a third window pass). The extension is routine but not written. The Theorem-A-vs-measurement link holds only up to N² factors under entrywise SO. | Add one line each. |
| F9 | Info | PD-N?…-201 Sources, PD-T?…-207 Sources | BJ + CGS2-all *is* ZN's V+A in grevlex order (Remark 3.2 rule; paper text via digest), so the drift applies to that published algorithm on these sets. Separately, the LIT?…-025 quotation "loss of orthogonality due to numerical cancellation" was not found in arXiv v2 (digest). | Record both carefully, with the UNVERIFIED caveat, before any statement about ZN's results. Check ZN's code. |

## Independent reruns (all executed; commands from `tracks/bivariate-lanczos/code/review_L2/`)

The environment is NumPy 2.5.3, SciPy 1.18.1, mpmath 1.3.0 and Python 3.13.18, on 2 cores. Run with `OMP_NUM_THREADS=1` where noted. Logs are in `topics/bivariate-lanczos-20261031/reviews/logs_L2/`.

```
python3 -I rl2_drift.py A B   > logs_L2/drift_AB.log    # rotpi4 + triangle references, kappa, LD runs  (≈ 3.5 min)
OMP_NUM_THREADS=1 python3 -I rl2_drift.py C > logs_L2/drift_C.log    # M = 1681, 1e4, 1e5 (≈ 3 min)
python3 -I rl2_drift_D.py     > logs_L2/drift_D.log     # L-shape, annulus, LD reference (≈ 1.5 min)
python3 -I rl2_thmA.py        > logs_L2/thmA.log        # Theorem A stress test (≈ 30 s)
python3 -I rl2_exact.py       > logs_L2/exact.log       # 202 / 205 exact checks + structural search
python3 -I rl2_cycles.py      > logs_L2/cycles.log      # 205 well-definedness vs condition (C)
python3 -I rl2_adapt_C.py     > logs_L2/adapt_C.log     # adapt selections vs (C)
OMP_NUM_THREADS=1 python3 -I rl2_omega.py > logs_L2/omega.log        # own E1/E1D and PRO-2D-J
python3 -I rl2_sections.py    > logs_L2/sections.log    # e_H, e_tau, e_F in LD; tensor control
# developer commands (from code/L2/):
python3 -I l2_r01_omega.py rotpi4 triangle              > logs_L2/dev_r01_omega_rerun.raw
python3 -I l2_r02_pro.py --jmeasure rotpi4 triangle cb_cubic > logs_L2/dev_r02_proJ_rerun.raw
python3 -I l2_r02_pro.py rotpi4 triangle                > logs_L2/dev_r02_pro_rerun.raw
python3 -I l2_r03_dots.py cb_cubic rotpi4               > logs_L2/dev_r03_dots_rerun.raw
```

Script SHA-256 values:

| Script | SHA-256 |
|---|---|
| rl2_lib | `7e434e463a68c0a2651af7b3fcdfe17195a966bed4feb152836a5692a2a4c061` |
| rl2_drift | `505c730cf1355366a7be627859b847e6bd989ccd0d84296c5d31cce913fd0566` |
| rl2_drift_D | `d077f67c9d885b711bc9d2410b8c31a0d0594c1d7120829e7f148ba764f67ed2` |
| rl2_thmA | `59158452f2ce3afa859b8568ebbcb17550436c22bca037b900e59a2a14faee3d` |
| rl2_exact | `252949f3c910ce64f663ea76e72f375f68155fcd968b6b529310d6675d046086` |
| rl2_cycles | `a65204be01a189495879f006cff3c79aebea61f8a40e02ae76f975355706f076` |
| rl2_adapt_C | `38b18b041b8087a1bfe7b7e54eb100836a314f0c59e05e9dce3b935de08b0b89` |
| rl2_omega | `e1acfe5f317470c84787142ca853b3c80c5994ac64c78e731354884547f0d816` |
| rl2_sections | `65c11cec501bd3c7ce09e08d4a8ed6138314995af62d9daf8cf64c127c73f311` |

## Remaining uncertainty

- **Simon:** Simon's own Theorem 5 (LAA 61) and Stewart's restatement could not be read, so the comparison rests on the Math. Comp. digest and Jia–Li.
- **ZN equivalence:** BJ = ZN rests on the paper text via digest; ZN's code was not inspected.
- **205 acyclicity:** acyclicity under (C) is checked, not proved.
- **Not rerun:**
  - E2, E2D, E3, and the other nine benchmarks of the ω table;
  - the alt, adapt and two-relation columns of PD-T?…-206;
  - the Padua and checkerboard controls of PD-N?…-201 (d);
  - R03 on its other sets;
  - wall-clock times;
  - M = 10⁶ (still Runs needed).
- **Realization variance:** drift magnitudes depend on the rounding realization (BLAS path) and on the node sample. At n = 24 they vary 15–50% between implementations and up to 50× between seeds at M = 1681. Only the orders of magnitude and the verdicts are robust.
