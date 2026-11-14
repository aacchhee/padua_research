# Independent review of the MZ-CC plan (plan-cc.md, correspondence-cc.md)

Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), effort high (as assigned), 2026-11-13. Independent internal reviewer. I did not write the plan or any reviewed record.
Read at head 761e884: BRIEF.md, plan-cc.md, correspondence-cc.md, manuscript.tex (CC text, 16 siamart pages when built in /tmp), manuscript-insert.md (with the K2/K4 addenda), the 13 PR #31 theory records named in the task, final-id-map.json, PROOF_STATUS rows PD-T013–027 and PD-T522–548, PD-T017/018/019/022/025 records, LIT-633.

**Verdict:** the plan is sound and scope-faithful in its theorem rows. There are no BLOCKING findings. Three MAJOR items must be fixed before writing: wording about what is "open", an unproved pointer to PD-T531, and the page budget.

## (a) Coherence and order

- **MINOR a1. The exact U evaluation is misplaced.** The plan places Prop 8.1 (PD-T019) in §8. It is also used in §4, to motivate the harmonic witness, and in §6, for the onset (see M1). Move the exact formulas (eq:Uexact, 5-line proof) to §4.1 as a lemma. Keep only the N=512 certificate and the An–Wu discussion in §8.
- **NOTE a2. Optional reorder: fixed ratios before the endpoint.** §7 (PD-T023/024) uses only §2–3 and the weight lemma. Placing it as §4 gives the reader the sequence half-exactness → fixed ratio → endpoint (min, max, consequences). Thm 3.2 and Thm 7.1 then sit together. Either order is coherent; the current one is acceptable.
- **MINOR a3. Lemma 5.1 (PD-T548, closed-form C_ij) is misplaced.** Only the certificate (Prop 5.4/App. C) uses it. Thm 5.3 does not. State it in App. C, with at most a one-line pointer in §5.
- The rest of the order is right. §3 (R=M−H+K) must precede §5, because PD-T530 reuses the decomposition and the H-integral. §5 must precede §6, because κ_2 needs Λ_edge. I found no duplicated statement.

## (b) Scope of planned statements

All PROVED rows in correspondence-cc.md match their records. I checked the PD-T526 quantifiers (N≥2, all of Π_{N−1}), PD-T546 (all N, Π_{N−1} and Π_N, finite bound (2) only for log N≥16), PD-T530 ([1,3/2], all N), PD-T529 ([1,5/3]), PD-T547 (one-sided) and PD-T544 (1600). Findings:

- **MAJOR M1. "No effective onset" (plan §6, §9) is inaccurate and must be reworded.**
  - PD-T019 gives the exact quotient of U_{N−1}. I checked it in exact rational arithmetic: the quotient is <1/3 for every N≥57 (S_57>3; the even-N factor N²/(N²−1) decreases), and it is >1/3 at N=56.
  - Hence, with PD-T526, 1−η_N=λ_−(N,N−1) for all N≥57, analytically. That is far better than the e^{619.7} onset quoted in the corollary record.
  - PD-T531 also gives a computable ε_N for λ_max.
  - What is genuinely open is narrower: a practical rate in Thm 4.5/5.3, and the decimal value of Λ_edge. Say exactly that. Add "N≥57" to Cor 6.1 (record update plus a 3-line proof).
- **MAJOR M2. The §9 sentence that "a computable bracket exists in the repository" must go.** It asserts a theorem that the paper does not prove, which breaks AC's rule. Drop it. If an open-problem sentence is wanted, write "a rate of convergence in Theorem 5.3 usable at computable N". Also fix the omission reason for PD-T531: the >0.05 widths of audit A8 are float estimates of the formula (MEASURED), not certified values.
- **MINOR b1. Λ_edge ≥ 1.0044369 is computer-assisted (PD-T547).** Say so in the abstract and in Thm 1.3. Cor 6.1(b)'s numeric interval inherits this. Alternatively, state the analytic [8/π⁴, 12/π⁴] and add the certified refinement separately.
- **MINOR b2. Measured items.** PD-T532 (1.0044369188…) and Table 1 λ_+ (1.004437035 at N=1280) must be labelled MEASURED and placed next to the certified one-sided bound, with the explicit sentence "no digit beyond the certified lower bound is claimed". PD-T525: keep it only with the warning from the K2 addendum. Do not describe K2 as evidence against equality.
- **NOTE b3. Optional sharper form of Thm 3.4.** The proof of PD-T526 actually gives λ_max ≤ 1+β_N: N²/(2(N²−1)) for even N and (N+1)/(2(N+2)) for odd N, so it is <3/2 for odd N and limsup ≤3/2. Stating this exceeds the registered statement and would need a registry scope update. Otherwise keep it as a remark inside the proof.

## (c) PD-T531 omission; appendix feasibility

- **The omission is sound.**
  - Nothing else in the paper depends on PD-T531. PD-T530 is independent of it (the dependency runs the other way).
  - Its proof needs about 3–4 extra pages of Lipschitz/quadrature constants, and it yields no usable digits.
  - The BRIEF says "may", not "must".
  - The consequence is that the paper's Thm 5.3 is purely qualitative. Say so plainly in the statement.
- **Page estimates from the records.** These assume SIAM's ~400–450 words per page for dense mathematics, with the terse records expanded about 1.3–1.5× for readable prose.
  - **Appendix A (π⁴/8):** 8–10 pp as separate records (PD-T522 0.3; PD-T523 3; PD-T544 2; PD-T545 0.7; PD-T546 assembly 3.5–4).
  - **Appendix B (Λ_edge):** 8–9 pp as written (PD-T528 derivation 0.7; PD-T529 3; Λ_edge≥1 addendum 0.6; PD-T530 4–4.5).
  - **Appendix C:** 4–5 pp (PD-T548 2–2.5; the PD-T547 reduction, scalar enclosures and checker 2–2.5).
- **MAJOR M3. The 30–34-page target is unrealistic.** The main text grows from 16 to about 23–24 pp, giving about 42–46 pp in total without the shortenings below and about 37–40 with them. Tell AC now. SINUM accepts long papers, but an editor will ask for the appendices to earn their length.
- **Shortening without losing rigor:**
  1. **One transfer lemma in Appendix A.** For arbitrary nodal data u on one edge, I_N u(cos(πt/N)) = (2N sin πt/(πt))S(t) + (2N/(πt))(Eg)(t) + cotangent remainder + cross term, with the bounds (6), (8) of PD-T546 and PD-T544. PD-T523 §2–3 then reduces to "apply the lemma to g_k=f(log k/L)": its pointwise residual (D)/(E) is the smooth special case of PD-T544, and its (G) is PD-T546 §1. Saves about 2 pp. Both directions then visibly rest on ‖V‖=2/π (PD-T522 → PD-T545 and PD-T523).
  2. **Weaken Prop 5.2 to qualitative fixed-J convergence.** Keep form convergence, positive definiteness of C, boundedness and liminf ≥ Λ_edge. Only PD-T531 uses the explicit constants (1)–(3), 1000J(1+A⁴)/N², and so on. Record this as "weakened, reason: constants only serve the omitted PD-T531". Saves about 1.5 pp.
  3. **Move PD-T548 to Appendix C**, as in a3.
  4. **Reuse §2 and §3 instead of repeating.** The weight bound |w_k−(π/N)sinθ_k|≤2/(N²−1) belongs in Lemma 2.2 (it is already in its proof). The H-integral identity and K≤β_N M belong in Thm 3.4. Appendices B and A then cite them.
- **NOTE c1. Keep the analytic Λ_edge≥1 addendum.** Step 5 of PD-T530 needs it. Using PD-T547 instead would make Thm 5.3 computer-assisted.

## (d) Title, abstract, headline

- **MINOR d1. The title's "Sharp" overclaims.** Only π⁴/8 is a sharp evaluated constant: Λ_edge is characterized but not evaluated, and 5/3 and the fixed-ratio constants are not sharp. Suggested titles:
  - *The Clenshaw–Curtis Gram spectrum beyond half-exactness: sharp logarithmic endpoint asymptotics and Marcinkiewicz–Zygmund constants*
  - *Endpoint Marcinkiewicz–Zygmund constants of Clenshaw–Curtis quadrature*
- **Headline suggestion.** The intro already shows that λ_−(N,N)^{−1/2} is the norm of Lagrange interpolation I_N from CC-weighted ℓ² to L². So Thm 4.5 on Π_N is equivalent to ‖I_N‖ = (2√2/π²+o(1)) log N. This is a sharp converse-MZ constant, which is the natural SINUM selling point. It is a one-line corollary, but it still needs its proof line in the paper.
- **Abstract order:** sharp π⁴/8 (with the interpolation-norm form) → uniform 5/3 → λ_max → Λ_edge (variational endpoint operator; certified Λ_edge ≥ 1.0044369, computer-assisted; decimal open) → consequences (η_N, κ_2, fixed ratio, hyperinterpolation) → methods → prior work. Avoid "explicit all-N two-sided bounds" next to "sharp": the all-N constants 1/K_N and 128000 are crude.

## (e) Notation conflicts beyond the plan's list

| Symbol | Meanings that collide |
|---|---|
| S | S_N odd-harmonic sum (Prop 8.1); S_N(θ) weight bracket (Lemma 2.2, which the plan now promotes); S in eq:colH; S(t) discrete primitive (App. A); s_j=(−1)^j |
| E | E=diag(2,1,…) (Lemma 2.3); energy Σ\|g_k\|²/k; operator E in Eg (PD-T546 itself flags this); E_k(f) |
| V | Volterra V; mass V (Prop 8.2); form domain V and core 𝒱_0 (PD-T530) |
| M, D, C | M, D, C each double as matrices, forms and constants: mass M vs M=⌊N/L⌋ vs M(g); defect D vs D(g), D_N model matrix and D_N constant in (2); C_N constant vs C_N, C model Gram vs C_*, C_0, C_f |
| F | F_N, F_n Fejér kernels; F=Vf; F_g cosine transform; F_j(x) in PD-T529 §3; F_j=f_j in PD-T548 |
| A | A_ρ (Thm 3.2 proof); A_θ (Cor 7.2); A_J=2H_J/π+1; A=πJ |
| θ | θ_j node angles vs fixed ratio θ (Cor 7.2) |
| ε | ε=1−n/N vs ε=2/L² |
| J | J=⌊N/2⌋ vs model truncation J (J=512) |
| c_k | c_0=c_N=2 (PD-T546) vs c_0=c_N=1/2 (PD-T528/529): opposite conventions for one symbol; also c_i=Q(fP_i) |
| a, d | a: Chebyshev coefficients; nodal a_k=(−1)^k u_k; trial amplitudes; a_j=πj. d: d_N (ADE); d=dim Π_n; d_k=min(k,N−k); d=\|i−j\|; d_j=Cin(2a_j) |
| m | m_j weight floor vs m_J=λ_min(C_J) |
| t | microscopic variable θ=πt/N (App. A) vs θ=t/N (App. B): same letter, scale differs by π |
| L, K | add L_N∈{N,N+1} (PD-T526 proof); K=⌈L²⌉; kernel k(v) |
| R | discrete mass R; constant R (eq:rowH); R_{N,j}(t) |
| λ | λ_± (manuscript) vs λ_min/λ_max (plan, PD-T546/530): choose one |

## (f) Results the plan forgot

- **MAJOR (= M1).** The N≥57 onset from PD-T019.
- **MINOR.** The interpolation-norm form of the π⁴/8 result (d).
- **MINOR.** Literature: the Volterra norm 2/π is classical (audit A9: Halmos, Problem 188). It needs a read LIT record before citing; otherwise state that the computation is elementary and make no claim.
  LIT-633 is applicable only after a same-symbol identification that the records do not make. Cite it, if at all, in the open-problem sentence on a symbol identification of Λ_edge.
- **NOTE.** One-line motivating remarks from proved negative records:
  - PD-N006: strictly alternating trials leave Π_{N−1}. This explains the endpoint-cancelled p_{N,j} and the reflected trial.
  - PD-N005: absolute-cardinal column bounds fail. This explains why PD-T544 keeps signs.
  - PD-N104: sign discarding has no uniform floor. This explains the reflected completion in Thm 3.4.
  If included, they go in the correspondence table.
