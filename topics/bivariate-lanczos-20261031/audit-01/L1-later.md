# Codex adversarial audit: later L1 claims and L1 negative results

Rules `3a9063b84d14ca0a5998378371e27643fde50a29`.
Interpretation: independently audit PD-T?bivariate-lanczos-claude-107, -109–115 and PD-N?bivariate-lanczos-claude-101–106, with special attention to the exact certificate, product/derivative mathematics, empirical scope and mixed statuses.

Auditor: Codex subagent assigned `gpt-6-astra`, xhigh; the runtime does not independently expose model/effort metadata. Date: 2026-11-01 UTC. Developer: Claude. Candidate supplied by the orchestrator: `5ccfac223f466a9105450365d8c6c3781ff7d922`; rules/working head supplied: `3a9063b84d14ca0a5998378371e27643fde50a29`, branch `claude/bivariate-lanczos-20261031`. Only the orchestrator controls Git. This subagent performed no Git operations and changed no developer file. Exact inspected source identities, evidence hashes, sizes and commands are in [L1-later/manifest.json](L1-later/manifest.json).

## Scoped verdict

**Changes required, with no failure found in the central exact triangle certificate, moment-matching lemma, transfer bound or Gram-derivative formulas.** Two medium findings concern the still-overstated N101 statement and the mandatory split/status rules. Two low findings are literal mathematical wording errors. The core measured failure of a universal Ritz predictor, selection dependence and the checkerboard coefficient channel survive this audit. These are finite measured findings, not asymptotic theorems or explanations of every possible recurrence.

## Findings

### LL-M1 — N101 still asserts a measured range known to be unsupported (medium)

Location: `tracks/bivariate-lanczos/theory/ritz-residual-governance-fails-off-product-supports.md:12`, `:24`, `:32`, and the final History bullet. Its current Statement says a 10²–10¹⁴ excess for *every* listed set and *each* residual, but the range still includes rotation 0.05, shears and the rotated Beta probe. The cited `l1_defect_probe.py` did not compute Ritz residuals. PC-1 in `directions/L1/candidates.md` and R04 §6 explicitly acknowledges this; the History assertion that PC-1 is “folded in” is inaccurate. The seed-11 supplementary measurements supply Z residuals, not every object in the blanket statement.

I wrote a separate CGS/QR/Ritz implementation, without importing development or reconstruction code. On the documented seed-11 square rotated by 0.05, M=1681, n=24, it gives loss `4.209653459152918e-13`. At the Statement's scale 2^-52, loss/(scale/rho) is **3.72 (X), 3.93 (Y), 7.16 (Z)**, well below 100; the degree is informative because the loss exceeds 1000·2^-52. At 2^-53 the ratios are 7.44, 7.87, 14.31. See `L1-later/independent_checks.log`. Minor rounding differences from the original code do not bridge this gap; the developer's PC-1 itself reports the borderline case.

Required disposition: rewrite the operative statement with separate, exact set/residual/degree scopes for the main Ritz runs and the probe-only observations. Move superseded wording to History. Preserve the valid failure of a universal predictor: my independent pi/4 example has excess `8.82e10` for Z at scale 2^-52, and the exp(8xy) square has excess `1.61e5`. This finding does not restore either single-section or joint universal governance.

### LL-M2 — Substantive results with different statuses remain under one ID (medium)

Location: `tracks/bivariate-lanczos/theory/first-order-coefficient-channel-gains-product-type.md:5`, `:21`, `:38`. T114 has `Split into: none`, four substantive PROVED parts and a substantive MEASURED part. The measured gain census and first-order explanation are more than a routine verification: they appear in the result's title, the ranked report and T115's dependencies. `agents/WORKFLOW.md`, “Split results before assigning a file status,” requires their own durable file/ID; merely labelling parts does not satisfy the rule.

Required disposition: keep the derivative theorem PROVED under its own ID; move the gain census/channel measurements into a separate measured record, retaining explicit split mappings and history, and update dependencies. Do not downgrade the proved derivative theorem.

T113 also currently says overall PROVED while its separate Q40 extension is CONDITIONAL (`exact-certificate-propagator-growth-triangle.md:30–36`). **This audit completed the missing independent exact Q40 rerun**, documented below, so its stated condition can now be discharged by updating its status and citing this evidence. The central T24/Q24 theorem remains PROVED. T114 still requires a split. The root auditor should coordinate this with the analogous T105 status issue in the foundations scope.

### LL-L1 — Affine scaling requires positive scale, or a sign convention (low)

Location: `tracks/bivariate-lanczos/theory/exact-certificate-propagator-growth-triangle.md:12`.

“Under an affine change ... entries scale by c^-1” is false as written for c<0 under the stated positive-pivot normalization. For k=s, the inverse diagonal entry is 1/beta_s>0; reflecting coordinates leaves beta_s positive, whereas c^-1 would reverse its sign. For c=0 the transformed problem breaks down. Restrict this sentence to **c>0** (all certificate rescalings use c=2/m>0), or state that squared entries scale by c^-2 for c≠0 with the appropriate diagonal signs for unsquared entries. The impulse identity and finite certificate are unaffected.

### LL-L2 — “On-pattern” means potentially nonzero, not nonzero (low)

Location: `tracks/bivariate-lanczos/theory/first-order-coefficient-channel-gains-product-type.md:20` versus `:30`.

The iff statement calls on-pattern entries “nonzero in c*”. For a symmetric marginal all Jacobi diagonal coefficients a_j vanish, including the parent position that is on-pattern. For example, a symmetric three-point probability measure has a_0=0, and the (1,0) <- (0,0) entry satisfies the stated index condition but is zero. Use the Definition's correct wording “may be nonzero” or “structurally permitted.” The implemented pattern mask uses positions, so the numerical classification and formulas are unaffected. In interpreting the univariate comparison, h and beta remain independent coordinates of the coefficient map; a perturbation of a tied symmetric Jacobi parameter would combine the corresponding coordinate derivatives.

## Independent mathematical reconstruction

**T110.** Writing V_t=(P_t,P_{t-1}) gives the stated rectangular transfers. The response from block s is the appropriate first block of T_t...T_{s+1}(-D_s^-1 Phi_s,0). For arbitrary compatible matrices, the ordered-product telescoping identity gives x_b <= K + K sum epsilon_r x_{r-1}; induction with K product(1+K epsilon_r) proves the bound. This argument does not require invertibility of the rectangular transfers. The corrected sign note is right: the block of L^-1 itself is +D_s^-1. This is a genuine bound for any prescribed coefficients; its usefulness for a measure is a separate measurement.

**T111 and the T105 dependency.** The difference of parity-restricted and half-product integration is one half of a product of alternating sums. Ordered nodes turn these sums into divided differences of orders m and m+1. For a+b<=2m at least one of a<m or b<m+1 holds, so the difference is zero. Positive product moments then imply a positive-definite Gram matrix on Pi_m, giving unisolvence without relying on a separate charter theorem. Moment equality through 2n controls both orthogonalization and every coefficient creating a degree-<=n column. On product probability measures the recurrence separates into the x base chain and y descendant chains. The second-kind Casoratian is -1, giving rho=b_s(r_{s-1}sigma-sigma_{s-1}r); the normalization correction in T105 is necessary and sufficient for that formula.

My own exact rational checker uses nonuniform ordered X=(-3,-1,0,2,6), Y=(-4,-2,1,3,5,9), weights |1/omega'| and both parities. All **45 moments through degree 8** match half the product exactly for each parity. The degree-9 monomial x^4 y^5 has difference -1/2 and +1/2 respectively, checking the sharp degree boundary. This does not establish novelty; it independently tests the algebra and edge of the claim.

**T113.** Put D_k=||psi_k||^2 and gamma_k=sqrt(D_parent(s)) g_k/sqrt(D_k). The monic recurrence becomes the normalized recurrence because beta_k=sqrt(D_k/D_parent(k)) and h_kl=alpha_kl sqrt(D_l/D_parent(k)). At the impulse row gamma_s=1/beta_s. Thus the squared inverse entry is exactly D_parent(s) g_k^2/D_k, a rational number on integer grids. Off-window zeros and positive norms identify the exact orthogonal basis; no approximate eigenvalue or logarithm enters the comparison G(12)>=10^6G(6) or G(12)<=100G(6). The definition k>s is essential for Q24's G(2)=0.

Fresh execution of the pre-existing independent checker `review_L1b/rv2_certificate.py` is distinguished from newly written code: it is an independent *audit rerun*, not a claim that I authored that checker. I read its implementation and reduction. On **both T24 and Q24**, full Fraction Gram–Schmidt gives zero coefficients outside the exact window, all 4095 off-diagonal inner products vanish exactly, and the separate exact moment-matrix LDL construction agrees in every basis value and norm. The exact comparisons pass, with displayed log-ratio increments **8.686** and **0.795**. A further 60-digit triangular solve at three T24 nodes agrees with the impulse identity to relative error **1.85e-56**. `math.log10` is presentation only; Fraction and Python integer arithmetic are trusted for the finite certificate. Consequently **T113 part 2 is confirmed as PROVED**, within its finite dev-rule scope. A large propagator entry demonstrates amplification capacity, not that every rounding realization attains it.

The additional **Q40, n<=16** run completed in 48.1 seconds and independently discharged the previously missing rerun: every off-window coefficient is zero, all **11628** off-diagonal inner products vanish exactly, and the reported log10 G(6)=**2.080**, log10 G(16)=**3.088** reproduce part 3. This larger run uses full exact Gram–Schmidt and exact orthogonality; the checker's separate moment-LDL method is omitted for this size. This is evidence for the finite Q40 extension only. I did not freshly rerun T40 or rotated Q24.

**T114.** Differentiate the explicit recursion while holding all other coefficient coordinates fixed. The variation at k is -xi_l/beta_k; later variations obey the homogeneous product-type recursion. For a y-created column only its y chain is reached. For an x-created column the impulse moves along the x chain and each newly reached base starts its y chain. The resulting polynomial has degree at most the output column's degree even when the source l is in the same degree block. Therefore each Gram integrand has degree <=2n; moment equality and Fubini give exactly the two displayed formulas for A. Differentiating Xi^T Xi gives -(A+A^T). A beta perturbation uses source xi_k/beta_k, with no additional beta factor, as corrected. The structurally defined on/off decomposition is sound, subject to LL-L2.

The producer's full T114 check and census were rerun: **91 entries per family**, maximum scaled formula errors `1.1e-14` (cubic) and `1.6e-15` (equispaced); cubic off-pattern gains `9.9e11`/`1.3e14` at n=16/20, on-pattern maximum `5.0e3`; equispaced off-pattern `4.2e2`/`1.4e3`, on-pattern `5.6`. The first-order BJ predictions reproduce `1.8e-11`/`7.8e-9`. This extends the previous reconstruction's coverage, which had not rerun the gain census. It is still MEASURED, with no second-order error bound.

## Measured claims, negative results and interpretation

| Claim | Audit result and precise coverage |
|---|---|
| T107 | Listed finite regimes are plausible and partly reproduced; the general support classifier is correctly withdrawn. The iid predictor, mixed-precision F/J source split and block-Paige fraction tables were inspected as recorded evidence, not freshly reproduced here. |
| T109 | The exact finite certificate independently supports a priori amplification for the specified dev rule. Its original “selection, not truncation” inference is correctly refuted. The floating reference P* in R03 is a high-precision computation, not exact arithmetic. I did not rerun its complete orientation scan or P*=P table. |
| T112(e,f), N103(a) | Fresh near-product producer run: zero bound violations; informativeness 10.4/13.6/27.8 decades on square/rot0.05/rot0.3 and 0.4 on tensor. Excess/angle is 1.02 vs 4.39 at 0.025/0.2: the specified finite H_lin criterion fails. The code samples 28 nodes on the three random sets and **27** on tensor after deduplication, not 28 on all four. |
| T112(a,b), T114(5) | Cubic coefficient-channel behavior is corroborated by the gain and checkerboard reruns. Exact product-type coefficients do not imply a stable finite-precision computed basis. The bivariate weight range is about 1.8e-67 to 0.47; the stale 1.7e-33 figure in T112(a) is the x-factor range, as PC-12 explains. |
| T115, N104(c) | Fresh six-set actual-double closed-loop run reproduces **C/L in [0.56,1.86]** and the stated “survives” decision. Fresh actual-double open-loop run reproduces quartic ratios **21.58/12.95** and cubic m36 **16.40/21.13** at n16/20: the written decision is **inconclusive**, not rejected. The actual-dot experiment is a different rounding model from Gaussian term-wise noise, and does not retroactively validate that noise model. |
| N101 | The broad current range requires LL-M1. The universal factor-3 predictor still fails badly in the independent pi/4 and exp(8xy) examples. Tensor chain completion is correctly withdrawn as comparative evidence. |
| N102 | Fresh producer variant run on random1681 seed0: exact-window losses `3.8e-14,3.1e-12,3.9e-10,1.3e-7` at n8/12/16/20; block window similar. The producer's mode named “full” makes the N-products full but leaves first-column N* products windowed; it is not literally full orthogonalization of every product. Previous independent reconstruction supplied a separate full control. No fresh comparison to the original paper's source code was made. |
| N103(b,c) | Predictor failures and two-relation checkerboard failure remain scoped MEASURED observations. Their original full producer suites were not rerun in this audit. No theorem about all source models or all two-relation algorithms follows. |
| N104(a,b) | Generic absolute noise amplification is corroborated by the fresh gain run. The separate nonlinear random-sign experiment was reviewed, not freshly rerun. Its large failure is plausibly robust; no claim of a new rerun is made. |
| N105 | Own independent pi/4 n24 losses: dev **5.188e-3**, alt **1.822e-8**, full-window dev **2.993e-14**. This reproduces both selection dependence and a role for truncation. Other rules/families remain under their recorded finite measurement scope. |
| N106 | Own exp(8xy) square gives loss **3.950e-8** and excess **1.611e5** over 2^-52/rho_Z, confirming the sampled-square support-shape counterexample. Gaussian results were read, not rerun; the recorded operator-norm caveat is necessary. “Product support” here describes the sampling domain, not a tensor-product support of the finite empirical measure. |

The mixed-precision dot64 code rounds both long-double operands to float64 before BLAS dot products, then returns to long double. Thus “dot-product rounding alone” means this **specific mixed-precision operation, including conversion of its operands**. The experiment establishes sufficiency within a model, not necessity or exclusive causation in ordinary float64 code. This distinction matters alongside L2's later exact-window-dot experiments; no contradiction is implied by another source reproducing comparable loss.

The near-product producer calls its full-CGS2 float64 coefficients “exact to ~1e-15,” but orthogonality alone does not certify exact graded coefficients, as the campaign's own span-drift evidence demonstrates. Accordingly its transfer measurements are accepted as measurements of the computed reference coefficients, without importing a rigorous exact-data error bound. This does not affect the algebraic transfer theorem or the rational T113 certificate.

## Decision rules and provenance limitations

I independently reanalysed the five stored R01 raw files, excluding N=M and tensor41 n=40 as documented. At 2^-52 K1 is true; at 2^-53 K1 is false, with exactly the recorded sets on which Z predicts. This was **reanalysis of existing data**, not rerunning those original recurrences. See `rule_reanalysis.log`. Treating K1 as inconclusive is the defensible interpretation; replacing epsilon by unit roundoff cannot establish which mathematical object governs the loss.

Candidate records retain failures and disclose important adaptive choices: IDEA106/107 thresholds were post hoc; IDEA114/115 arose after diagnosing checkerboards; IDEA116 followed a small smoke test; IDEA119 reused the Lobatto flat control; IDEA120 used already-known ordinary BJ losses on all six sets. Criteria written before the model output is known are still not independent prospective validation of model selection. The blanket opening of `candidates.md` claiming all criteria predate experiments must be read subject to these explicit exceptions. I made no new novelty claim, performed no external literature search, and did not independently validate historical timestamps or WIP snapshots. The exact certificate's validity does not depend on a pre-registration claim.

Read coverage: full AGENTS.md, WORKFLOW.md, CODEX.md, state/IDEAS.md, literature/INDEX.md, audit-handoff.md, report.md, plan.md and L1/candidates.md; the full theory records for this assigned scope plus T105; L1 R04–R07; both L1 reconstruction reports; relevant implementation and log files identified in the manifest. T101–106/108 proofs and L4 are assigned separately; dependencies are reconstructed here only to the extent used in the later claims. Literature records and reviewer literature summaries do not become independently checked original sources in this audit.

## Executions and retained evidence

All commands were run from `/workspace/padua_research`, with prefix `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I -u`, and stdout redirected to `topics/bivariate-lanczos-20261031/audit-01/L1-later/<output>`. No seeds were changed in producer/reviewer scripts. The new checker uses default_rng(11) and explicit rational nodes. Each completed process returned exit code 0; the reported mathematical checks were also inspected rather than inferred from exit status alone.

| Script and arguments after the common prefix | Output |
|---|---|
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py triangle 24 12 integer mp` | `cert_triangle_rerun.log` |
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 24 12` | `cert_square_rerun.log` |
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 40 16` | `cert_square40_rerun.log` |
| `tracks/bivariate-lanczos/code/L1/l1_r06_gain_identity.py` | `gain_producer_rerun.log` |
| `tracks/bivariate-lanczos/code/review_L1b/rv2_closed_loop_sets.py` | `closed_loop_rerun.log` |
| `tracks/bivariate-lanczos/code/review_L1b/rv2_open_loop.py` | `open_loop_rerun.log` |
| `tracks/bivariate-lanczos/code/L1/l1_r04_near_product.py` | `near_product_producer_rerun.log` |
| `tracks/bivariate-lanczos/code/L1/l1_simax_variants.py` | `simax_producer_rerun.log` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.py` | `independent_checks.log` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.py rule` | `rule_reanalysis.log` |

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0; mpmath and full NumPy build details recorded in `environment.log`. Float64 epsilon 2^-52, long-double epsilon 2^-63. These differ from the developer's Python/NumPy versions, which is disclosed rather than treated as identical execution provenance.

Retention: only small necessary audit evidence and checker source are kept under the assigned directory, each far below 1MB. Source hashes and evidence sizes are in the manifest. No external cold-storage destination was invented; root integration controls the cumulative repository evidence budget. Outstanding coverage includes fresh reruns of the T40/rotated-Q24 extensions, the full T107 diagnostics and several N103/N104 predictor variants, multi-seed generalization and M=10^5–10^6 experiments. Those limits do not weaken the scoped exact finite theorem but do limit empirical generalization.
