# PD-T?drift-codex-03 — First-order normal-quotient map of the vector-operation errors of a scalar CGS2 graph in a formal relative-error model

ID kind: PD-T.
Aliases: operation-to-residual bridge; scalar coefficient errors lie in the normal kernel; vector-operation amplitudes determine the first-order normal map in the formal relative-error model.
Split from: E2's explicit-family/rounding explanation target, which remains OPEN beyond this stated model.
Split into: none.

## Statement

Use the real nodes, ordering, exact monic b_k, d_k and fixed admissible choices of PD-T?drift-codex-01. Set q_k=b_k/sqrt(d_k). Consider the following **specified scalar implementation** of full classical Gram-Schmidt twice for each k>=1, in increasing prior-column order:

1. a_i = A_k(i) q_p(i), one scalar product per node.
2. c_l = Dot(q_l,a), l=0,...,k-1. Dot uses scalar products and left-to-right addition.
3. t_i = sum_(l=0)^(k-1) q_l(i)c_l, using scalar products, starting with the l=0 product, and then left-to-right additions. Set r_i=a_i-t_i.
4. e_l=Dot(q_l,r), and v_i=sum_l q_l(i)e_l, in the same orders. Set z_i=r_i-v_i.
5. beta=Norm(z), from a sum of scalar squares, a square root, and any scalar relative roundings. Set q_k(i)=z_i/beta, one scalar division per node.

There is no starting-vector perturbation. Every scalar operation with exact real operands/result w is replaced by w(1+epsilon delta_o), with independent fixed |delta_o|<=1. Operands include the perturbed values from preceding operations. This defines a smooth formal arithmetic model near epsilon=0. It is the permissive standard relative-error model; it does not require that the chosen deltas are the actual IEEE roundings, including for operations that happen to be exact.

At epsilon=0, steps 1–5 give the exact orthonormal basis q_k. Let alpha_kl be the monic recurrence coefficients for the chosen A_k and parent. For each local **vector arithmetic** operation o at node i and column k, define a rational monic amplitude m_kio as follows:

| Operation | m_kio |
|---|---|
| Coordinate multiplication in step 1 | (A_k b_p)_i |
| Product q_l(i)c_l in the first matrix-vector product | -alpha_kl b_l(i) |
| Addition through index l>=1 in the first matrix-vector product | -sum_(h=0)^l alpha_kh b_h(i) |
| First subtraction a_i-t_i | b_k(i) |
| Second subtraction r_i-v_i | b_k(i) |
| Final component division z_i/beta | b_k(i) |

All other local operations contribute zero to the first-order **normal quotient**: dot-product roundings and scalar norm roundings contribute polynomial vectors; the second matrix-vector product has zero exact operands e_l and therefore its own products/additions have zero first-order local rounding terms.

Define

    f_k(i)=sum_o m_kio delta_kio.

Let g and R_s be the exact frozen responses and projector from PD-T?drift-codex-01. Then the actual span of the formally computed columns obeys

    theta_s(epsilon)=|epsilon| ||R_s V D_s^(-1/2)||_2+O(epsilon^2),
    V_k=sum_(h<=k) diag(g_kh(z_i)) f_h.

Thus the first-order standard-model span map is fully specified by rational local vector-operation amplitudes and rational frozen responses. This identity includes all scalar operations of the stated implementation; it does not identify a BLAS implementation whose reduction order is unspecified.

## Definitions

The output theta_s is the largest principal-angle sine between S_s and the span of the computed columns, whether or not those computed columns are orthogonal. The normal quotient ignores polynomial evaluation vectors in S_s. The delta parameters have the **l-infinity** standard-model bound max_o|delta_o|<=1. An l2-operation condition is a separate sensitivity convention, not the scalar standard model.

For the full specified model, write K_inf for the supremum of the first-order output norm over those bounded delta parameters. With

    rho_hi=sum_o |m_hio|,
    L_op^2=max_(h,i,o) m_hio^2 R_s,ii sum_k g_kh(z_i)^2/d_k,
    U_inf^2=sum_(i,k) [sum_h |g_kh(z_i)| rho_hi]^2/d_k,

we have L_op<=K_inf<=U_inf. A stronger coherent-node witness is available: fix a node i and a target column t, and take delta_hio=sign(g_th(z_i)m_hio), with every other-node delta zero. Then

    C_it^2=R_s,ii [sum_h |g_th(z_i)|rho_hi]^2/d_t <= K_inf^2.

For the same error choices, using every output column instead of only t gives the stronger exact gain

    Cfull_it^2=R_s,ii sum_k [sum_h g_kh(z_i)sign(g_th(z_i))rho_hi]^2/d_k
              <= K_inf^2.

Take sign(0)=0. These are admissible l-infinity error choices and rational squared endpoints. The coherent witness can be evaluated at any subset of nodes/targets as a lower certificate; it need not be globally maximizing. A multi-node support witness is also available: for any row l with R_s,ll>0 and target t,

    S_ti=sum_h |g_th(z_i)|rho_hi,
    M_lt^2=[sum_i |R_s,li| S_ti]^2/(R_s,ll d_t) <= K_inf^2.

It uses delta_hio=sign(R_s,li g_th(z_i)m_hio), with sign(0)=0. Any selected row/target pair supplies a valid lower certificate; no maximization over all choices is assumed.

A row-free multi-node lower bound is

    E_t^2=sum_i R_s,ii S_ti^2/d_t <= K_inf^2.

Indeed choose independent node signs s_i in {+1,-1} and local errors delta_hio=s_i sign(g_th(z_i)m_hio). These give target column R_s(s*S_t)/sqrt(d_t). The average squared norm over the finite set of 2^M node-sign patterns equals E_t^2, so some pattern attains at least that value. A deterministic exact greedy pattern also attains at least E_t^2: process nodes in any fixed order, keep c_l=sum_(processed i) b_l(i)S_ti s_i, choose the next sign as sign(-sum_l b_l(i)c_l/d_l), using +1 at a tie, then update c_l. Its exact attained target-column gain is

    G_t^2=[sum_i S_ti^2-sum_l c_l^2/d_l]/d_t >= E_t^2.

All these quantities are rational, and each target supplies an actual formal standard-model error vector, not a randomized numerical estimate. One may restrict to coordinate multiplications only or component divisions only; the same formulas bound that **subset** map. A subset lower endpoint also lower-bounds K_inf for the full model, whereas a subset upper endpoint does not upper-bound the full model.

## Assumptions

Exact positive pivots; injectivity through the specified degree; fixed choices under perturbation; no overflow, underflow or data perturbation; a formal relative perturbation of the listed scalar arithmetic; exact q_0. Degree-independent constants and a uniform finite-epsilon remainder are not claimed.

## Status by part

Overall status: PROVED (analytic model reduction and bounds; Claude audit-01: CONFIRMED, wording corrections applied in response-01; Codex re-audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Complete first-order scalar-operation normal map for steps 1–5 | PROVED | Explicit differentiation below |
| Rational l-infinity lower/upper bounds | PROVED | Rank-one witness and absolute-sum bound below |

Candidate / claim disposition: retained as a bridge for the stated formal model. A statement about activation by deterministic IEEE rounding or an all-degree growth rate remains OPEN.

## Depends on

PD-T?drift-codex-01's exact frozen recurrence and graph-angle argument. Its assumption of exact perturbed full projection is not imposed on this theorem: the proof below directly differentiates a computed recurrence instead.

Closest predecessors (added in response-01, audit finding P-F6; **not dependencies**, nothing below is used in the proof): PD-T042 / IDEA-141 (exact first-order derivative of the window coefficient map with respect to coefficient errors, with on/off-pattern gains, on product-type measures), PD-T043 / IDEA-142-144 (term-wise and closed-loop dot-product rounding through that coefficient map; Gaussian term-wise noise and the mixed-precision `dot64` model, MEASURED) and IDEA-139 (coefficient-aware forcing, REJECTED as a loss predictor, PD-N009(b)). Separation: (i) *output functional*: PD-T042/043 concern the **Gram** matrix of the windowed-recurrence output (orthogonality defect), where in the tested models the coefficient errors carry the measured loss; this record concerns the **span** of the fully orthogonalized columns, in which the same coefficient, dot-product and norm errors lie in the polynomial kernel and vanish at first order. It is the span-output counterpart of those Gram-output results and says nothing about the orthogonality defect. (ii) *error model*: PD-T042 is an exact derivative on product-type measures and PD-T043 uses Gaussian noise or an actual mixed-precision dot product, whereas here every scalar operation of a specified CGS2 implementation carries an independent formal relative error |delta|<=1 (an l-infinity operation graph) at arbitrary rational nodes and fixed choices, with no stochastic or IEEE model. Nothing here confirms or contradicts those findings.

## Checks

Written after root explicitly authorized E2 development on E1's tightened finite property certificate. The scalar-subset/full-graph finite results are separate evidence; no computer proof is claimed by this analytic reduction alone. Supplementary independent mathematical reconstruction of the full chain rule and the added support/sign-witness bounds found no gap (see the topic's independent mathematical check). Full independent operation-by-operation dual-number trajectory reconstruction was an outstanding supplementary check when this record was written; the audit-01 reviewer has since run it at degrees 3 and 4 (14 and 20 generic rational nodes, all four rules, 5454 scalar operations per case, agreement with the amplitude table to 1.3e-80; no degree-12 replay was run).

The developer executed `tracks/bivariate-lanczos/code/drift/e1_cgs2_verify.py`; `topics/padua-lanczos-drift-20261101/evidence/e1-cgs2-graph-verification.json` records exact rational dual-number checks at degree three for all four rules on both primary grids. Per rule, T24 had 2925 local graph-gradient identities and 26325 zero second-pass-operation checks; rotQ24 had 5625 and 50625. All passed. This verifies local primitive amplitudes, not the complete normalized trajectory or an actual IEEE realization; it is developer execution, not independent rerun.

## Sources

Closest coefficient-error predecessors PD-T042 / IDEA-141 and PD-T043 / IDEA-142-144 (and IDEA-139), with the separation stated under Depends on. Standard relative-error model, explicitly restated rather than imported as a theorem. Existing PD-T046 includes normwise local recurrence error and a non-breakdown factor; the present claim gives the first-order normal quotient of a fully specified scalar implementation. No priority claim.

## Proof or evidence

At zero perturbation the first pass gives exact coefficients c_l, the residual r=b_k/sqrt(d_p), the second-pass coefficients e_l=0, and beta=sqrt(d_k/d_p). In particular

    sqrt(d_p) q_l(i)c_l=alpha_kl b_l(i),
    sqrt(d_p) r_i=sqrt(d_p) z_i=b_k(i).

For the derivative of a relative operation w(1+epsilon delta), the **local** rounding term is w(0)delta. Operand derivatives are carried separately by the chain rule.

Differentiate the entire first matrix-vector product. Derivatives of c_l are scalar coefficients multiplying the unperturbed polynomial vector q_l; all dot-product rounding errors are included in these coefficient derivatives. The remaining local errors are products q_l(i)c_l and partial-sum additions, with negative signs because this matrix-vector product is subtracted. Multiplying by sqrt(d_p) yields exactly the two corresponding amplitude rows. The step-1 product gives (A_k b_p)_i, and the first subtraction gives b_k(i).

In the second pass, e_l(0)=0. Derivatives of e_l, including every local dot-product rounding term, again multiply q_l and so enter only as scalar coefficients on earlier polynomial vectors. Terms involving dot q_l times e_l(0) vanish. Every local product/addition inside v has zero exact baseline and thus zero local first-order rounding. The final subtraction has unperturbed result r_i and contributes b_k(i) after multiplying by sqrt(d_p).

All errors in computing beta, including errors induced by perturbations of z, have a scalar derivative dot beta. In differentiating q_k=z/beta, this produces a scalar multiple of q_k; it is a polynomial vector of degree deg k. The local relative rounding of each final division contributes q_k(i)delta at its own node. Since beta sqrt(d_p)=sqrt(d_k), its monic recurrence amplitude is b_k(i).

To justify eliminating the scalar terms even after future propagation, put w_k=sqrt(d_k) dot q_k, using the **fixed unperturbed** d_k. Differentiating the full formed relation and multiplying by sqrt(d_p) yields

    w_k=A_k w_p-sum_l alpha_kl w_l+f_k+h_k,

where h_k is a scalar combination of b_0,...,b_k. This includes dot c_l, dot e_l, dot beta, and all local dot/norm scalar errors. (The exact scaling is beta sqrt(d_p)=sqrt(d_k) and c_l sqrt(d_p)/sqrt(d_l)=alpha_kl.) Hence h_k lies in S_(deg k). If V obeys the same frozen recurrence with source f only, induction shows w_k-V_k belongs to S_(deg k), exactly as in PD-T?drift-codex-01. Therefore R_s[w_0,...,w_(N_s-1)]=R_s[V_0,...,V_(N_s-1)]. The graph-angle proof from that file applies to the span of any differentiable full-rank column family, without requiring perturbed orthogonality. This proves the derivative formula.

For the bounds, allowing one local delta to equal one and all others zero produces a single node/source impulse of amplitude m_kio. Its projected output is rank one, with the squared gain stated in L_op. For arbitrary bounded deltas, |f_h(i)|<=rho_hi. The unprojected normalized response entry has absolute value at most sum_h|g_kh(z_i)|rho_hi/sqrt(d_k). Summing its squares gives U_inf^2. Final projection contracts Frobenius norm and spectral norm is at most Frobenius norm. For the coherent-node witness all source vectors are supported at the same node i, so the final normal output has the common column factor R_s e_i and is rank one. The selected signs make the target response sum_h|g_th(z_i)|rho_hi. Its target-column norm proves C_it; summing the squared responses of all columns gives the exact rank-one spectral norm Cfull_it. For the multi-node witness, w=R_s e_l/sqrt(R_s,ll) is a unit vector orthogonal to S_s. The chosen signs make its inner product with output column t equal to sum_i|R_s,li|S_ti/sqrt(R_s,ll d_t). The output spectral norm is at least that one-column inner product. This proves M_lt. For the node-sign average, E[s_i s_j]=0 for distinct i,j and R_s^T R_s=R_s, giving the stated diagonal sum. For the greedy rule, each new cross-term in v^T R_s v is -2s_i S_ti sum_l b_l(i)c_l/d_l because R_s,ij=-sum_l b_l(i)b_l(j)/d_l for i!=j. The chosen sign makes it nonnegative. The diagonal terms sum to sum_iR_s,ii S_ti^2; hence the final target-column norm is at least E_t^2. Expanding v^T R_s v=||v||^2-sum_l(b_l^T v)^2/d_l gives the exact attained G_t^2 formula. Rationality follows from rational m,g,d,P entries.

## Scope

This is a formal **per-scalar-operation** model, different from the aggregate residual norm of E1. In particular coordinate multiplication supplies (A b_p)_i delta, not ||A b_p|| delta at an arbitrarily chosen node. Component division supplies b_k(i)delta. The aggregate node witness may therefore overstate the standard-model single-operation witness. Dot and norm errors can still affect coefficients, orthogonality and finite-error behavior; only their first-order span-normal contribution vanishes in this fixed-choice baseline model.

For actual IEEE arithmetic, a formal adversarial delta may be unattainable; a subtraction by exact zero is one example. Deterministic floating-point evaluation is piecewise constant/discontinuous as a function of real data and is not being differentiated here. A positive lower bound on K_inf is capacity within the stated error model, not a lower bound for every actual run. The untouched old L2 implementation uses BLAS, whose scalar reduction order is not fixed by this theorem.

## Open items

Independent dual-number operation-level replay (done at degrees 3 and 4 by the audit-01 reviewer; degree 12 not run); exact finite scalar-subset/full-map certificates; a concrete actual-rounding realization; explicit-family uniform degree bounds and matching finite-epsilon estimates. Zero local errors remain permitted, so no unavoidable pathwise drift lower bound follows.

## History

- 2026-11-01: Codex mathematics developer, requested gpt-6.1-sol xhigh, exact runtime metadata unexposed. Root authorized E2 after the tightened E1 finite certificate. This file records an analytic scalar-model bridge, while preserving the original E2 family/rate target as OPEN.

- 2026-11-01: Added coherent-node, projected-row and node-sign expectation/greedy lower certificates during the post-E1 scalar search. These are routine support/norm consequences in the same formal model; no target/parameter change and no historical preregistration claim.

- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F8: title and alias reworded so that neither reads as an IEEE or causal claim (provisional ID kept); original wording: «# PD-T?drift-codex-03 — First-order scalar-CGS2 rounding map in the polynomial normal quotient»; alias «…; vector arithmetic controls first-order span drift.»
- 2026-11-01 (Claude response-01, Sonnet 5.5): P-F6: added the closest coefficient-error predecessors PD-T042/IDEA-141, PD-T043/IDEA-142-144 and IDEA-139 with a separation statement under Depends on and Sources; no mathematical content changed; original Sources wording: «Standard relative-error model, explicitly restated rather than imported as a theorem.»
- 2026-11-01 (Claude response-01, Sonnet 5.5): status line, Checks and Open items updated for the audit-01 trajectory replay at degrees 3-4 (status PROVED unchanged); original wording: «Overall status: PROVED (analytic model reduction and bounds; independent audit pending).»; «Full independent operation-by-operation dual-number trajectory reconstruction is an outstanding supplementary check.»
