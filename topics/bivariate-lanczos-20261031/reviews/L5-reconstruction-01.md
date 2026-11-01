# L5 adversarial reconstruction 01: Givens deficit, pivot rules, prefix mechanism

**Auditor:** Claude Opus 5.5, effort high. I am an independent adversarial reconstructor (subagent) and did not write the L5 work. I changed no Git state. Date: 2026-10-31.
**Why this model and effort:** WORKFLOW gives Opus high/xhigh for a mathematical audit. The orchestrator assigned high. The mathematics here is routine: one rotation-error bound and one Schur-complement lemma. Most of the weight is on the independent numerical reruns.
**Branch:** `claude/bivariate-lanczos-20261031`.
- Head at the start of the audit: `dd919d24a3df6da6d0cdc01d427630ca4d62b3d8`.
- Head at the end: `3d6c0da931d7d394e3a6ec2c20dd4f6f9861f21d` (orchestrator WIP checkpoints).
- Between the two heads, no L5 file, audited theory file, `state/IDEAS.md` or plan §L5-Q1 changed. I checked this with `git diff --stat dd919d2 HEAD`: the only plan change is one L3 ledger line.
**Rules read:** `AGENTS.md`, `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md` at the branch head.

## Audited files (sha256)

| file | sha256 |
|---|---|
| theory/givens-updating-rotation-count-backward-bound.md (PD-T?…-501) | c1963f449602ea09dc9b97dd124e67cf48872b97526cd190ec0b2e5ae51070e0 |
| theory/givens-deficit-slopes-measured.md (-502) | 24c905cb898f95d9e4c6507157aa30742deddf2083ec32410158abbed50f6e77 |
| theory/prefix-unisolvence-order-statistics-measured.md (-503) | 865b477eb991667f31b630a0539e127ca135999bbeecdd695371399cc35427e7 |
| theory/unisolvent-prefix-extension-lemma.md (-505) | fb4d9fb9a4606db0b2aa2663834e1aa8e559a22c0562c1a2755ec51c8c1dd4dd |
| theory/largest-redundant-pivot-degradation.md (PD-N?…-506) | e46473e8d2e17defe0d4e18aac724ca8450404bb1ef2833af2d0a485b1327f7e |

## Read coverage

**Read in full:**
- `AGENTS.md`, `agents/WORKFLOW.md`, `CLAUDE_ROLES.md`.
- `plan.md`, including §L5-Q1 and History. Its L5-Q1 text is identical at both heads.
- `state/IDEAS.md` in two chunks: all 48 rows, OBST 01–15 and the disposition table.
- `directions/COMMON_RULES.md`, and in `directions/L5/`: BRIEF, STATUS, R01, R02, R03 and candidates.md.
- The five theory files listed above.
- `code/L5/givens_core.c`, `l5_lib.py`, `exp_r01.py` and `analyze_r01.py`; `prefix.py` (first 80 lines only).
- `code/inputs/f6_givens_vs_hl_deficit.py` and `f6_run_padua_large.py`.
- `repro/REPRO.md` §§1–4.3.
- The developer logs `analysis_r01b.txt`, `r03_x60.json` and `r03_x60_controls.jsonl`.

**Fulltext:** I read VB–C 2010 via pdftotext into the scratchpad only, pp. 388–401: the downside-up scheme (12), Algorithm 1 on p. 391, the 6×6 example on pp. 392–395, the pivot remark on p. 395, and Tables 1–2 on pp. 400–401.

**Online:** Connolly–Higham, "Probabilistic rounding error analysis of Householder QR factorization", MIMS EPrint 2022.5 (https://eprints.maths.manchester.ac.uk/2865/1/paper.pdf). I used it to check what Higham ASNA says (Thm 19.4, §19.6). I did not read Higham ASNA itself.

**Not read:** `literature/INDEX.md` beyond what L5 cites, Humet/ETNA 2014, and `exp_r01b.py`/`exp_r03*.py` in detail. I make no novelty claims.

## Independent implementation and reruns

**Code.** All in `tracks/bivariate-lanczos/code/review_L5/`. None of it imports or copies the developer's modules or the inputs.

| file | sha256 (first 16 hex) | content |
|---|---|---|
| `agivens.c` | fe12b714c7f06d48 | Algorithm 1 written from VB–C pp. 389–395: D = [w\|X\|Y], scheme (12), rule 'largest' = larger \|pivot\|. Double or long double; optional Qᵀ accumulation. |
| `alib.py` | 01139ca2e7ceec3f | Padua points and cubature weights; Chebyshev matrix via the three-term recurrence; long-double reference (3-pass CGS of the weighted Chebyshev matrix, H = QᵀXQ in long double); my own HL (window deg−2..deg, MGS ×2), CGS2 and Householder; LU-based prefix certificate; GEPP order. |
| `exp_review.py` | ccac2697dbc1675b | experiment drivers |
| `checks.py` | bf7870215b81714f | sanity checks |
| `analyze_review.py` | b405be32e9de0534 | analysis of my runs |
| `reanalyze_dev.py` | 070afa08293851e8 | re-analysis of the developer's logs (review, not a rerun) |
| `stage_check.py` | d476e5be37e8107e | rotation-stage disjointness check |

**Build.** `gcc 13.3 -O2 -ffp-contract=off -shared -fPIC`. The `.so` files are in the scratchpad (`AG_BUILD`), not in the repo.

**Environment.** Python 3.13.18, numpy 2.5.3, scipy 1.18.1, `OPENBLAS_NUM_THREADS=1`. Two cores, shared with other agents (load average about 4–5). Logs are in `reviews/logs_L5/`, 132 KB in total.

**Commands.** Run from `review_L5/`, with `AG_BUILD=<scratch>/build`:

| command | wall time | log |
|---|---|---|
| `python3 -I checks.py` | | `checks.log` |
| `python3 -I exp_review.py slopes a_slopes.jsonl 10 15 20 25 30 35 40 44` | 6m16s | `a_slopes.log` |
| `python3 -I exp_review.py kill b_kill.jsonl 30 40 50` | 4m55s | `b_kill.log` |
| `python3 -I exp_review.py repro60 c_repro60.jsonl` | 2m10s | `c_repro60.log` |
| `python3 -I exp_review.py unif d_unif.jsonl 66 136 231 496` | 4s | `d_unif.log` |
| `python3 -I analyze_review.py LOGDIR` | | `analysis_review.txt` |
| `python3 -I reanalyze_dev.py ../directions/L5/logs` | | `reanalysis_dev_r01.txt` |
| `python3 -I stage_check.py` | | `stage_check.log` |
| (inline computation) | | `unif_slopes.txt` |

**Sanity checks** (`checks.log`):
- The cubature-weighted Chebyshev Gram matrix is diagonal to 6e-19 for n = 4, 7, 10, 20, and the weights sum to 1.
- Givens double vs reference: 8e-16 to 4e-15 (n = 3, 6, 10). In long double: about 4e-17.
- The LU bounds lo ≤ σ_min ≤ up hold against exhaustive SVD at n = 6 and 10.

**Agreement with the developer.** My code reproduces several developer numbers to all printed digits. For example, at n = 20 the given order gives 9.9e-15 / 1.4e-14 and gepp gives 1.9e-14 / 2.8e-14 (scheme / largest). At n = 40, given gives 4.14e-14 / 1.54e-7 and gepp gives 7.16e-14 / 1.80e-11. At n = 50, gepp gives 1.22e-13 / 9.28e-10. This is expected: the algorithm and the sign normalisation are the same. The code was written independently, but the algorithm is not independent.

---

## Claim 1. PD-T?…-501: rotation-count backward bound

**Statement as I reconstruct it.** Algorithm G executes R ≤ M(M−1)/2 rotations. Under the model (F1)–(F3), there is an exactly orthogonal Q̃ such that:

‖(Ĥ_x − Q̃ᵀXQ̃, Ĥ_y − Q̃ᵀYQ̃)‖_F ≤ 2Rθν ≤ 16.5 u ν M(M−1)(1+O(u)), and ‖ŵ − Q̃ᵀv‖ ≤ 2Rε₁‖v‖.

This holds for any pivot map.

**Verdict: CONFIRMED WITH CORRECTIONS.** The scope is the backward statement as written. The interpretive remarks need correcting.

**What I verified.**
- I checked every step: Lemma 1, the counting (each index is in M−1 rotations), and Lemma 2.
  - In Lemma 2, ĉ = c(1+δ)/(1+θ_h), and its error is ≤ γ₃.
  - The rotated pair has error ≤ γ₂(1+γ₃)‖z‖ per component.
  - ε₁ = γ₃ + √2γ₂(1+γ₃) ≈ 5.83u.
- Lemma 3: the joint row/column bound √2Ξ and θ = √2ε₁(2+ε₁) ≈ 16.49u.
- The Theorem A induction, and the w-recurrence.
- The full-size formulation is consistent with the code, which updates only the active block: the entries outside the block are exact zeros.
- The model matches the input code and my own: hypot, three roundings per entry, no zero forcing.
- "Independent of the pivot map" is correct. Nothing in the proof uses how the angle was chosen.

**Findings.**

- **M1 (Medium). The statement is not a backward-stability result for the IEP, and the remark built on it overreaches.**
  - **Location:** R02 §3 ("the 'largest' catastrophe is not a failure of backward stability of the rotation sequence") and the theory-file Remark.
  - The conclusion of Theorem A is also satisfied by doing nothing: no rotations, Q̃ = I, Ĥ = diag(x, y), ŵ = v. It constrains neither ŵ ≈ ‖v‖e₁ nor the zero pattern below the pivots. Both are what make the output the solution of (13).
  - **I measured this** (`b_kill.jsonl`, Q̂ᵀ accumulated). On all-prefix-unisolvent orders, 'scheme' and 'largest' have the same backward residual ‖Q̂ᵀXQ̂ − Ĥ‖/‖(x,y)‖: 2.7e-15 at n = 30 and 4.4–4.5e-15 at n = 50.
  - They also have the same first-column residual: ‖|Q̂e₁| − √w‖ ≤ 3.8e-15, and ‖ŵ₂:‖/‖v‖ ≈ 8.5e-17.
  - In contrast, the structure defect (the largest entry below either candidate pivot, relative to ‖H‖_F/√M) tracks the forward error:

    | n, order | sdef, scheme | sdef, largest | forward error, largest | forward error, scheme |
    |---|---|---|---|---|
    | n = 50, gepp | 6.8e-14 | 8.4e-10 | 9.3e-10 | 1.2e-13 |

    The same holds on every row of `b_kill.jsonl`.
  - **Correction.** The developer's inference "different Q̃ whose first-column/zero-pattern structure is not that of the problem" is half wrong: the first column is right (the w-rotations are the same for every rule). The failure is entirely in the structural defect, which Theorem A does not see.
  - **What PD-N 506 should say.** 'largest' is backward stable as an orthogonal similarity with the correct first column. It loses the zero pattern at the level of the forward error. Theorem A is not evidence of IEP backward stability for any rule.
  - The theory file's Scope (iii) already says the zero pattern is not covered. The R02 sentence and the Remark should be reworded to match.

- **L1 (Low). The comparator citation is roughly right but the comparison is not like for like.**
  - **Citation:** Higham ASNA Thm 19.4 is the columnwise bound ‖Δa_j‖₂ ≤ γ̃_{mn}‖a_j‖₂, which implies the Frobenius form. Connolly–Higham 2022 cite it as Thm 19.4. The developer's "γ_{cMN}" is acceptable.
  - **First problem.** That bound is a backward error for the QR of the M×N weighted Chebyshev–Vandermonde matrix. Theorem A is a backward error for a two-sided similarity of (diag x, diag y). The Householder comparator's H also needs the error of forming QᵀXQ.
  - **Second problem.** The relevant Higham comparator for rotation counting is Givens QR (§19.6), whose worst-case bound is γ̃_{m+n−2}. That is linear because the rotations group into m+n−2 disjoint stages. The file does not mention it.
  - **Third problem.** The pre-registered kill criterion for IDEA 503 was "same M-exponent". The exponents are not the same: Givens M^{3/2}u relative, Householder M²u. The worst-case bounds favour Givens, the opposite of what is observed. The conclusion ("worst-case bounds cannot explain the deficit") stands, but not for the stated reason.
  - **Fourth problem.** No HL or CGS2 bound is cited at all.
  - **Suggested addition.** The probabilistic analyses (Higham–Mary; Connolly–Higham 2022: Householder √(mn)u, Givens QR (m+n)^{1/2}u) are the natural frame for Open item (2).

- **L2 (Low). The sharpness of Theorem A is not addressed against the stage structure.**
  - I checked by brute force (`stage_check.log`, M = 5, 12, 30) that the rotations of Algorithm 1 have a stage structure. Rotations (j,i) with equal j+i are pairwise disjoint, and any later rotation with a smaller or equal stage is disjoint from the earlier one. There are 2M−3 stages.
  - In Higham's one-sided Givens-QR setting, this gives a linear bound. In this two-sided setting, disjoint rotations do not commute in floating point (cross entries see a row operation and a column operation in a different order). So the transfer is not immediate.
  - Whether the worst-case relative bound can be improved from M^{3/2}u to Mu is OPEN. The file's phrase "its M-dependence is the worst case (all rounding errors aligned)" should not suggest the M^{3/2} order is attained. The file does say the constant is not claimed sharp.

**Status label.** PROVED (routine) is right for Theorem A as stated. The Remark's PROVED label applies only to "the same bound holds for any pivot map". The consequence drawn from it is inference, and my measurement corrects it (see M1).

---

## Claim 2. PD-T?…-505: all-prefix-unisolvent orders exist

**Statement as I reconstruct it.** In exact arithmetic, take N = dim Π_n distinct points that are unisolvent for Π_n. For a unisolvent K-prefix S with K < N, a next node z_ℓ is admissible iff (S_c e₁)_ℓ ≠ 0, where S_c is the Schur complement of the prefix block in V. Some admissible node exists, and max|s_ℓ| ≥ σ_min(S_c)/√(N−K). By induction an all-prefix-unisolvent order exists, and the GEPP order on V·T (T upper triangular) is one.

**Verdict: CONFIRMED.**

**Reconstruction.**
- det V = det B · det S_c, so S_c is nonsingular and its first column is nonzero.
- The bordered determinant equals det B · s_ℓ.
- A triangular change of basis multiplies leading minors by det T_K. Positive row scaling multiplies each prefix minor by the weights of its rows. So prefix unisolvence is basis- and weight-independent.
- In exact GEPP, the active matrix at step k is the Schur complement of the current prefix, and its pivot is max|s_ℓ| > 0.
- This also covers GEPP on row-scaled matrices. I used that to build two further unisolvent orders, geppR1 and geppR2.

**Edge cases.**
- Repeated x or y coordinates (Padua lines) are irrelevant to the argument. Coincident points are excluded by unisolvence.
- **M > N** (random nodes, where Algorithm 1 uses M graded monomials beyond degree n) is not covered as stated. The proof carries over verbatim whenever the M×M matrix of the nodes against the first M graded monomials is nonsingular (generic, not guaranteed). This is a minor scope note.
- Degree milestones play no role in the proof.
- **Finding L3 (Low).** The order produced by floating-point GEPP (scipy getrf) is an exact-arithmetic GEPP order only up to near-ties. Its use as "all prefixes unisolvent" in the measured claims needs the numerical certificate, which the developer supplies (in prefix.py) and I supply too (LU bounds, below).

**Status label.** PROVED is correct. It is elementary, and no novelty is claimed.

---

## Claim 3. Measured claims: PD-T?…-502, -503 (parts), PD-N?…-506

### 3a. Slopes (PD-T?…-502, L5-Q1 first clause)

**Rerun.** Padua points with cubature weights, my own implementation and reference. n = 10, 15, 20, 25, 30, 35, 40, 44, so M = 66 to 1035 over 8 sizes. Orders: given, sortx, r1–r3 (seeds 900+10n+k), and gepp.

| class (pooled OLS [95% t]; size-means OLS [95% t, df 6]) | Givens-scheme | HL | CGS2 | Householder* |
|---|---|---|---|---|
| 5 orders | 1.18 [0.96, 1.40]; 1.18 [1.00, 1.35] | 0.71 [0.68, 0.74] | 0.48 [0.46, 0.50] | 0.28 |
| structured (given, sortx) | 0.94 [0.89, 0.99] | 0.75 | 0.48 | 0.29 |
| random orders r1–r3 | 1.34 [1.08, 1.60] | 0.68 | 0.48 | 0.27 |
| gepp | 1.05 [0.98, 1.12] | 0.71 | 0.48 | 0.28 |

\*My reference is a long-double QR of the same Chebyshev matrix that Householder factors. This biases the Householder error low (0.28, against the developer's 0.38). The other methods are not affected at their error levels.

- Kill test as written, on my data: Givens 1.18 > 0.7, HL 0.71 < 0.9, CGS2 0.48 < 0.9. **Not killed.** This holds on the full range and on M ≥ 496.
- This confirms the developer's qualitative result over a range up to M = 1035. That is below the plan's ≥ 2000. The developer covers up to 2016, so the range above 1035 is not independently rerun (see Runs needed).

**Findings.**

- **M2 (Medium). The slope uncertainty is understated, and the model is misspecified.**
  - **Location:** `analyze_r01.py`, the 502 table and R01 §3.1.
  - **(i) The "cluster bootstrap" is not one.** It resamples replicates within each size, so it ignores lack of fit between sizes. The t-interval treats 35 points as independent, although the effective sample is the 7 sizes.
  - **(ii) Re-analysis of the developer's own logs** (`reanalysis_dev_r01.txt`): a fit to size-level means gives Givens-scheme, Padua cubature, 1.40 with 95% interval [1.01, 1.79] (df 5), against [1.09, 1.70] reported. The log–log quadratic term is +0.32 (t = 3.7), and +0.51 (t = 3.4) for the random orders. For the U(0.1,1) weights it is 1.55 [1.03, 2.06], curvature +0.40 (t = 3.4).
  - **(iii) The upper-range slopes are not statistically supported.** The developer reports 2.15 and 2.50 for M ≥ 496, which has only 4 sizes. In my data the size-means interval for that range is [−0.52, 3.31].
  - **Consequences.**
    - A single power law is the wrong summary for random orders. Their growth is driven by prefix conditioning (503 C), not by rotation count.
    - The pooled "1.40" mixes a slope of about 0.93 (structured) with a convex random-order curve.
    - Only the structured-order slope of about 0.93 [0.88, 0.99] is a clean power-law statement.
  - **Recommendation.** Report size-means intervals and curvature. Phrase the claim per order class.

- **M3 (Medium). The uniform-random family and the as-written verdict.**
  - The candidates.md operational reading, which the developer pre-registered, says: "called not killed overall only if no family triggers it". The uniform family triggers it: CGS2 1.57 and HL 2.28 in the developer's data.
  - My rerun also triggers it, already at M ≤ 496 (3 seeds): Givens 1.51, HL 1.49, CGS2 0.90 (`unif_slopes.txt`).
  - So the verdict on the frozen test, as written and as operationalised, is **KILLED (in one family)**.
  - R01, STATUS, the plan ledger and progress.md lead with "not killed on controlled families". This reading rests on two post-hoc steps:
    - **excluding** the uniform family as confounded (a confound was noted in advance, but no exclusion rule was set);
    - **adding** the arcsine family after the runs had started (`exp_r01.py` edited mid-run; disclosed). The arcsine family stops at M = 1326, not ≥ 2000.
  - The developer discloses both, so this is honest. But the headline should state the as-written verdict first and label the controlled-family reading as a post-hoc reinterpretation.
  - **A better confound control is available.** Normalising each instance by its own Householder error removes the per-instance conditioning. On the developer's uniform-family data (M up to 2016), the ratio slopes are:

    | method | ratio slope to Householder [95%] |
    |---|---|
    | Givens | +0.76 [0.06, 1.46] |
    | HL | +0.16 [−0.04, 0.37] |
    | CGS2 | −0.54 |

    So the Givens-versus-HL separation survives the confound there.
  - On my M ≤ 496 rerun the ratio slopes are +0.07 and +0.05: at small M the confound dominates completely.
  - The arcsine family is a reasonable control (cond slope 0.26). It is not a pre-registered one.

- **L4 (Low). The kill test cannot detect growth that is too steep.**
  - It kills only if Givens is ≤ 0.7. A random-order slope of 1.7–2.0, which the rotation-count picture does not predict either, passes.
  - The developer says this in prose ("not exactly 1 on random orders"). The plan's kill test was frozen, so this is a design remark only.

- **I1 (Informational).** "HL ∝ √M" is not supported. I measure 0.68–0.75 and the developer 0.71–0.81. The developer states this correctly.

**Verdict, 3a: CONFIRMED WITH CORRECTIONS.**
- The table numbers reproduce in kind on M ≤ 1035.
- The intervals are too narrow and the upper-range slopes are unsupported (M2).
- The headline verdict must read "killed as written in the uniform-random family; not killed in the other four families, a post-hoc reading" (M3).

### 3b. Prefix-mechanism kill (L5-Q1 second clause; PD-N 506 N2)

**Rerun.** Padua points with cubature weights, at n = 30, 40, 50. Orders:
- gepp (GEPP on my orthonormal Chebyshev matrix);
- geppR1 and geppR2: GEPP on randomly row-scaled matrices (log-normal, σ = 1.5, seeds 500+10n+k). These are all-prefix-unisolvent by Claim 2 and are not the developer's rpiv orders.

**Certificate.** The LU of the row-ordered matrix without pivoting gives, for every K:

1/(‖L_K⁻¹‖_F‖U_K⁻¹‖_F) ≤ σ_min(L_K U_K) ≤ |u_KK|.

- The backward residual of the factorisation is ≤ 6e-15.
- This is "certified" only in the exact arithmetic of the computed factors (MEASURED). It is valid as a numerical test because the residual is ≪ the lower bound.

| n | order | certified min_K σ_min ≥ | scheme | largest | ratio | catastrophe (≥1e3 and ≥1e-10) |
|---|---|---|---|---|---|---|
| 30 | gepp / geppR1 / geppR2 | 6.5e-5 / 2.2e-5 / 2.3e-5 | 4.2e-14 / 3.7e-14 / 4.3e-14 | 5.7e-13 / 1.2e-12 / 1.4e-12 | 14 / 34 / 33 | no |
| 40 | gepp / geppR1 / geppR2 | 2.4e-5 / 8.3e-6 / 8.8e-6 | 7.2e-14 / 7.4e-14 / 7.8e-14 | 1.8e-11 / 5.0e-11 / 6.8e-11 | 250 / 670 / 880 | no |
| 50 | gepp / geppR1 / geppR2 | 1.2e-5 / 4.3e-6 / 4.4e-6 | 1.2e-13 / 1.3e-13 / 9.9e-14 | 9.3e-10 / 2.1e-9 / 1.8e-9 | 7.6e3 / 1.6e4 / 1.8e4 | **yes, all three** |

**Verdict: CONFIRMED (kill fires).**
- With my own implementation, my own reference, two new unisolvent orders and my own certificate, 'largest' meets the pre-registered catastrophe definition on all-prefix-unisolvent orders at n = 50.
- The minimum prefix σ_min is above the pre-registered 1e-8 by more than 2 orders of magnitude.
- So the binary "only on non-unisolvent prefixes" form is refuted in this scope.

**Findings.**

- **M4 (Medium). The kill rests on the operational catastrophe threshold, not on the seed's magnitude, and PD-N 506 should scope this.**
  - The plan's object is the "≈ 7e-4" catastrophe. On well-conditioned unisolvent orders (σ_min ≥ 4e-6 in my runs; ≥ 4.7e-4 for the developer's gepp/rpiv), 'largest' stays ≤ 3.1e-9 up to n = 50.
  - Errors at 1e-4 to 1e-2 occur only on:
    - non-unisolvent orders, for example given at n = 44: 2.3e-6 (mine) and 3.4e-4 (developer, n = 50);
    - or the near-singular REPRO order with σ_min = 9.7e-10: 2.1e-4.
  - The data fit a **graded prefix-conditioning effect**: the 'largest' error rises as the minimum prefix σ_min falls (gepp 1e-9; random orders at σ ≈ 3e-9: up to 6e-7; REPRO 2e-4).
  - The developer's "graded, not binary" wording is right. The statement that would survive is "'largest' degrades on every order at a rate of about ×15–50 per Δn = 10, and catastrophically (≥ 1e-6) only on singular or near-singular prefix sequences in the tested range". It is neither tested nor refuted by the kill.
  - A further sign that the binary classification is fragile (developer data): n = 40 rand2 is "non-unisolvent" only because its K = 2 prefix has two nodes with equal x. Its 'largest' ratio (9.6e2 and 1.5e3) is the same as for the unisolvent rand1 and rand3.

- **L5 (Low). The classification tolerance is not the pre-registered one.**
  - R01's 2×2 table uses σ < 1e-11 for "singular". The pre-registered rule was "all prefixes ≥ 1e-8".
  - Under the pre-registered rule the count is 14, not 16. The developer discloses this. The kill fires either way.
  - Also, the n = 50 gepp and rpiv cases do not depend on the tolerance.

### 3c. REPRO n = 60 order (PD-T 503 C; R03 §3.3)

**Rerun.** Unit weights; perm = `default_rng(2).permutation(1891)`, the first draw as in `f6_run_padua_large.py`. Error is measured against my Householder H.

| method | error |
|---|---|
| scheme | 1.97e-12 |
| largest | 2.09e-4 |
| HL | 1.10e-14 |

These reproduce the developer's values exactly to the printed digits.

**Prefix check by exact SVD** of the leading blocks at 340 K: all K ≤ 300, a grid of every 50, and the 30 K with the smallest |u_KK|.
- min σ_min = 9.67e-10 at K = 114. This is identical to the developer's 9.667e-10.
- No σ_min < 1e-11 among the checked K.
- LU without pivoting is unusable as a certificate for this order (growth 1.4e9, residual 2e-8). So K > 300 off the grid is **not certified** by me. The full scan is in Runs needed.

**Verdict: CONFIRMED** for the numbers, and partially confirmed for "no singular prefix".
- **L6 (Low).** "The REPRO value is a typical draw" rests on 4 random permutations (5e-13 to 2e-11) and leaves the σ_min of 3 of them unmeasured. "Typical" should read "within the range of 4 draws".

### PD-N 506: other wording and protocol findings

- **M5 (Medium). The scope section contradicts the statement.**
  - **Location:** 506 "Negative-result scope" says "'No catastrophe at n ≤ 15' is part of the scope".
  - N1 itself and the developer's `analysis_r01b.txt` list a catastrophe at n = 15: given order, U(0.1,1) weights, 1.1e-2, ratio 1.6e12.
  - The data support "no catastrophe at n ≤ 10".

- **L7 (Low). The seed's suggestion is not the 'largest' rule.**
  - VB–C p. 395 (verified) suggests the larger pivot "if two pivots differ in some orders of magnitude". That is the pivk-κ rule with κ ≫ 1, not 'largest' (κ = 1).
  - 506's disposition "REJECTED (the seed-p. 395 suggestion …)" is supported only by N4 (pivk10 and pivk100 at n = 30 structured orders: 8.6e-9, 5.9e-12, 4.3e-3). It should cite N4 for that clause and not the 'largest' data.

- **L8 (Low). The disposition reason for IDEA 502 is inconsistent.**
  - candidates.md says "REJECTED: failed". 506 says "refuted".
  - By WORKFLOW, a claim whose negation is established in scope is "refuted". "Failed" applies to the 'largest' heuristic as a mechanism.

- **L9 (Low). PD-N bundling.**
  - 506 bundles the failure of the IDEA 504(b) magnitude rules (N4).
  - The IDEA 504(c) deferral rules (FIFO, τ = 1e-8 and 1e-3) are "REJECTED: failed" with MEASURED evidence, but they have no PD-N.
  - WORKFLOW: "A separate evidenced mechanism failure still gets its own PD-N." Either give 504(b)/(c) their own PD-N, or record why they are covered by 506.

- **L10 (Low). ID choice 506.**
  - It is valid: L5 range 5nn, provisional form correct.
  - The reason in LOG.md ("avoid a digit clash with PD-T 501") is cosmetic, because the namespaces are separate. Meanwhile IDEA 501–503 and PD-T 501–503 share digits but denote different things: IDEA 503 ↔ PD-T 501, IDEA 501 ↔ PD-T 502, IDEA 502 ↔ PD-T 503/PD-N 506, IDEA 504 ↔ PD-T 505.
  - Recommend an explicit crosswalk table in candidates.md.

- **Status labels.** These are correct:
  - 502 and 503: MEASURED.
  - 505: PROVED.
  - 501: PROVED (routine).
  - 506: MEASURED, negative statement.

- **Protocol.**
  - **(P1)** Kill criteria "written before testing" are only self-attested. All L5 files arrived in one commit (dd919d2), so ordering cannot be verified from Git.
  - **(P2)** Post-hoc items are disclosed in the records: the detector kill test was written after the n = 10 and 14 data; the 504c′ and 504c″ variants; the arcsine family; the tolerance deviation.
  - **(P3)** The frozen L5-Q1 text is unchanged and was applied. M3 is about the headline, not the application.

---

## Remaining uncertainty

- **Range.** My slope rerun stops at M = 1035 (developer: 2016). The upper-range behaviour and the U-weight and unit-weight families are not independently rerun.
- **Independence.** My Givens code is independent, but it implements the same algorithm, so bitwise agreement is expected. It checks the developer's implementation and bookkeeping, not the claims of the algorithm itself.
- **Certificate and reference.** The prefix certificate is numerical (MEASURED), not exact. The REPRO order's prefix scan is partial (340 of 1891 K). The Householder-ratio slopes on my reference are biased low.
- **Open questions.** Whether Theorem A can be sharpened via the stage structure is open. The mechanism of the 'largest' structure-defect growth is OPEN (the developer agrees).

## Runs needed (AC's servers syvert0/1/2)

From `tracks/bivariate-lanczos/code/review_L5/`, with `AG_BUILD` and `OPENBLAS_NUM_THREADS=1` set:

1. Slopes to M ≥ 2000 with my code: `python3 -I exp_review.py slopes OUT.jsonl 50 55 62`. Estimated 30–60 min. Long-double reference time grows as M³.
2. All-unisolvent orders at n = 62 and 70, to test whether 'largest' reaches ≥ 1e-6 on well-conditioned orders: `python3 -I exp_review.py kill OUT.jsonl 62 70`.
3. Full exact-SVD prefix scan of the REPRO order (all 1891 K, about 1 h), plus σ_min scans of the 3 other n = 60 random orders.
4. Uniform-random family M = 861 to 2016 with the Householder-ratio analysis: `python3 -I exp_review.py unif OUT.jsonl 861` (add 1326 and 2016 to TAB).
