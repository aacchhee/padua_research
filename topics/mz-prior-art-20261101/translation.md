# Translation lemmas used by the prior-art comparison

Author: Claude (Opus 5.5), 2026-11-01, rules `9739a0c` (unchanged at `64c3c79`). Status of each item: **PROVED** here as a routine supporting step for the literature comparison. Items T4 and T6 are conditional on the cited LITERATURE statement, as marked. None is registered as a new PD-T: none adds a new mathematical claim about CC beyond restating PD-T017/PD-T018 in operator language. Revised in response-01 to audit-01 (F1, F4, N1, N2); the original text is in Git history at `4f93713`.

Conventions are those of PD-T013/PD-T017: N≥2, θ_k=kπ/N, x_k=cos θ_k (0≤k≤N), ℓ_k∈Π_N the Lagrange cardinal polynomials, CC weights w_k=∫_{-1}^{1}ℓ_k dx>0 (PD-T013), Q_N(f)=Σ_k w_k f(x_k), and

  λ_−(N,n)=inf_{0≠p∈Π_n} Q_N(p²)/∫p²,  0≤n≤N.

## T1. Operator form of the minimum eigenvalue

For 0≤n≤N let V_n={(p(x_k))_{k=0}^N : p∈Π_n}⊂ℝ^{N+1} (so V_N=ℝ^{N+1}) and L_N v=Σ_k v_kℓ_k. Equip ℝ^{N+1} with ‖v‖_w²=Σ_k w_k v_k² and Π_N with ‖p‖²=∫_{-1}^1 p² dx. Define ‖L_N‖_n=sup_{0≠v∈V_n}‖L_N v‖/‖v‖_w.

**Lemma T1.** ‖L_N‖_n² = 1/λ_−(N,n) for every 0≤n≤N.

*Proof.* The evaluation map E:Π_n→V_n, p↦(p(x_k)), is linear and onto by definition. It is injective because a polynomial of degree ≤N vanishing at N+1 distinct nodes is zero. For p∈Π_n⊂Π_N, L_N(Ep)=p (uniqueness of interpolation). Hence for v=Ep≠0, ‖L_N v‖²/‖v‖_w² = ∫p²/Q_N(p²), and Q_N(p²)=Σw_k p(x_k)²>0 because all w_k>0 and Ep≠0. Taking the supremum over p gives 1/λ_−(N,n). ∎

**Corollary T2.**
(a) PD-T017 (∫p²≤K_N Q_N(p²) on Π_N) is equivalent to ‖L_N‖_N≤√K_N. That is, the weighted nodal ℓ²(w)→L²(dx) norm of Lobatto/CC interpolation is O(1+log N).
(b) PD-T018 (λ_−(N,N−1)≤128000/(log N)²) is equivalent to ‖L_N‖_{N−1}≥(log N)/√128000.
(c) V_{N−1}⊂V_N, so ‖L_N‖_{N−1}≤‖L_N‖_N. A source proving only ‖L_N‖_N≍log N would therefore imply the order in PD-T017 and the *full-space* statement λ_−(N,N)≲(log N)^{−2}. It would **not** imply PD-T018, whose growth witness must lie in V_{N−1}. Here V_{N−1} is the hyperplane where the T_N-coefficient of the interpolant vanishes, i.e. Σ''_k (−1)^k v_k=0 (double prime: endpoint terms halved), by the discrete cosine-transform formula for Chebyshev–Lobatto interpolation.

So "nodal-ℓ² to L² norm ≍ log N ⇔ λ_min ≍ (1+log N)^{−2}" holds when both sides refer to the same subspace (Π_N or Π_{N−1}) and the same weights w_k. The comparison constants transform by T1: c≤‖L_N‖_n/log N≤C is equivalent to C^{−2}≤λ_−(N,n)(log N)²≤c^{−2}. They are reciprocally squared, not literally the same constants (audit-01 N1).

## T3. Weight comparison

**Lemma T3.** For every N≥2 and 0≤k≤N, with Δ_N(x)=√(1−x²)/N+1/N²,

  ½ Δ_N(x_k) ≤ w_k ≤ 5 Δ_N(x_k).

*Proof.* Interior 1≤k≤N−1: PD-T017 §1 eq. (1) gives sinθ_k/N≤w_k≤5 sinθ_k/N, and eq. (2) gives w_k≥m_k/N²≥1/N². So w_k≥max(sinθ_k/N,1/N²)≥½Δ_N(x_k), and w_k≤5 sinθ_k/N≤5Δ_N(x_k). Endpoints: w_0=w_N equals 1/N² (N odd) or 1/(N²−1)≤2/N² (N even), so ½Δ_N(±1)=1/(2N²)≤w_0≤2/N²≤5Δ_N(±1). ∎

**Consequence.** If a source proves, for p∈Π_n, ∫p²≤C Σ_k μ_k p(x_k)² with μ_k≤A w_k for all k, then λ_−(N,n)≥1/(CA). If it proves Σ_k μ_k p(x_k)²≤C′∫p² with μ_k≥a w_k, then λ_+(N,n)≤C′/a. Quadrature-sum weights comparable to Δ_N(x_k) (Christoffel numbers of Lebesgue measure, local spacing Δx_k) can therefore be exchanged with CC weights at a cost of absolute constants. Such an exchange preserves orders (e.g. log N) but **never** a sharp constant such as an upper constant below 2.

## T4. What Mastroianni–Totik (2000) gives at CC nodes

Source statement (LITERATURE: Mastroianni–Totik, Constr. Approx. 16 (2000), §7, pp. 65–66; the algebraic Marcinkiewicz inequality stated as the translation of their Theorem 4.2 under x=cos t; read 2026-11-01 from the publisher PDF via AC's institutional access; audit-01 could not obtain these pages). For a doubling weight w on [−1,1] and 1≤p<∞ there are constants M, C_src such that for all n and all p_n∈Π_n,
∫|p_n|^p w ≤ C_src Σ_j |p_n(x_j)|^p Δ_n(x_j) w_n(x_j)
whenever x_j=cos ξ_j, ξ_j∈[0,π], −1=x_0<…<x_S=1, with **absolute** angular gaps |ξ_{j+1}−ξ_j| ≤ 1/(Mn). For every M there is also a converse inequality with constant C_M when the absolute gaps are ≥1/(Mn). (The ξ_j decrease as the x_j increase; audit-01 N1.) Here Δ_n(x)=√(1−x²)/n+1/n² and w_n(x)=Δ_n(x)^{−1}∫_{x−Δ_n(x)}^{x+Δ_n(x)}w.

**Normalization (audit-01 F1).** For w≡1 on [−1,1] the integral covers an interval of length 2Δ_n(x) truncated to [−1,1]. So 1≤w_n(x)≤2, with w_n=2 when [x−Δ_n,x+Δ_n]⊂[−1,1]. The specialized inequality therefore reads ∫p_n²≤C_CC Σ_j p_n(x_j)²Δ_n(x_j) with **C_CC:=2C_src**.

**Choice of M.** Increasing M only strengthens the upper-gap hypothesis, so the inequality persists for every M′≥M. Fix once and for all an admissible M with **M≥1**.

**Proposition T4 (conditional on the cited statement; PROVED from it).** With M≥1 and C_src as above, if N≥2πM and 0≤n≤N/(πM), then λ_−(N,n)≥1/(16π²M²C_src).

*Proof.* Put n″=⌊N/(πM)⌋. Since n is an integer with n≤N/(πM), we have n≤n″ and Π_n⊂Π_{n″}. Since N/(πM)≥2, n″≥N/(πM)−1≥N/(2πM)≥1. The CC absolute angular gaps are π/N≤1/(Mn″). The specialized inequality gives ∫p²≤2C_src Σ_j p(x_j)²Δ_{n″}(x_j). Because N/n″≤2πM and 2πM≥1, Δ_{n″}(x)=(N/n″)√(1−x²)/N+(N/n″)²/N²≤(2πM)²Δ_N(x). By T3, Δ_N(x_j)≤2w_j. Hence ∫p²≤16π²M²C_src·Q_N(p²). ∎

**What this does and does not give (audit-01 assessment adopted).** With M≥1 the window is n≤N/(πM)≤N/π<N/2. That lies inside the half-exactness range: there 2n≤N, p² has degree ≤N, CC integrates it exactly, and λ_−=λ_+=1 (PD-T013). So T4 is **no stronger than CC exactness**. A non-trivial consequence beyond half-exactness would need an admissible source constant M<2/π, and the source does not specify M. **Verdict for PD-T023/PD-T024: RELATED** (downgraded from "IMPLIES PART"). Mastroianni–Totik is context for small sampling ratios in general, not a prior proof of any part of the CC fixed-ratio theorem beyond what exactness already gives.

## T5. Why Lubinsky (1999) Theorem 1.7 stops at the CC endpoint case (analysis, not a source claim)

Lubinsky's Theorem 1.7 (Constr. Approx. 15 (1999), p. 583; the author manuscript was independently checked by audit-01) gives, for P∈Π_{n−1} at n ordered points satisfying the spacing condition (1.7),
∫|Pν|^p ≤ C Σ_j |P(t_j)|^p {∫_{t_{j−K}}^{t_{j+K+1}}|ℓ_jν|^p + δ_jω(t_j)^p/[δ_j|π_n′(t_j)|]^p}.
Here ω(t)=(|1−|t/b||+c)^σ with the **open** range −1/p<σ<1−1/p in (1.29), under |π_nν|≤ω (1.16) and (1.31): |1−|t_j/b||+c≥τδ_j.

Apply it with p=2, ν≡1, the N+1 Lobatto nodes (n=N+1, so P∈Π_N), b=1 and **c=N^{−2}** (audit-01 N2).
- **Nodal polynomial.** π(cos θ)=sin θ·sin Nθ, a multiple of (1−x²)U_{N−1}, so |π|≤(1−x²)^{1/2}≤√2(1−|x|)^{1/2}. The natural exponent is σ=1/2=1−1/p, exactly the excluded endpoint of (1.29). Fix any admissible σ<1/2. Since 1−|x|+c≤2, |π|≤√2(1−|x|+c)^{1/2}≤2(1−|x|+c)^σ, which is (1.16) after scaling π.
- **Condition (1.31).** At interior nodes θ_j∈[π/N,π−π/N], 1−|t_j|≍θ_j²∧(π−θ_j)² and δ_j=t_{j+1}−t_{j−1}≍sinθ_j/N. Hence 1−|t_j|+N^{−2}≳ (sinθ_j)² ≳ sinθ_j/N≳δ_j, using sinθ_j≥2/N. At the endpoints, 1−|t_j|=0 and c=N^{−2}≍δ_j. So (1.31) holds with an absolute τ. With c=0 it fails at ±1, and a fixed c>0 does not give the near-endpoint behaviour below.
- **Second coefficient.**
  - Interior nodes: |π′(t_j)|=N and ω(t_j)²≍(sinθ_j)^{4σ}, so δ_jω(t_j)²/[δ_jN]² ≍ (sinθ_j)^{4σ}/(N sinθ_j) ≍ w_j·(sinθ_j)^{4σ−2}.
  - Endpoints: |π′(±1)|=2N, δ≍N^{−2} and ω(±1)²=N^{−4σ}, so the coefficient is ≍N^{−4σ}≍w_0·N^{2−4σ}.

So for each **fixed** admissible σ<1/2, the coefficient exceeds the CC weight by a factor up to ≍N^{2−4σ} near ±1. No optimization in σ→1/2 is attempted, and the theorem's constant C=C(σ,…) is not tracked there. The direct fixed-σ specialization therefore yields neither an O(log N) CC-weighted bound nor a lower bound. The CC/Lebesgue case is the borderline it excludes.

## T6. Mastroianni–Milovanović–Notarangelo (2012) Corollary 2.2 at the CC nodes (added in response-01)

Source statement (LITERATURE: G. Mastroianni, G. V. Milovanović, I. Notarangelo, *On an interpolation process of Lagrange–Hermite type*, Publ. Inst. Math. (Beograd) (N.S.) 91(105) (2012) 163–175, DOI 10.2298/PIM1205163M; author PDF read 2026-11-01, pp. 163–167. The page image of p. 164 confirms "r ⩾ 1", where the text layer renders ⩾ as ">"; the same glyph mapping appears for "γ ⩾ 0" in (2.1).)
- **Setting.** x_k, k=1,…,m, are the zeros of the Jacobi polynomial p_m(v^α), v^α=(1−x²)^α. L_{m,r}(v^α,f) interpolates f at the x_k and matches f^{(j)}(±1) for j<r. For **r=1** this is Lagrange interpolation at the zeros together with ±1.
- **Corollary 2.2 (p. 167).** Let 1<p<∞, 1/p+1/q=1. For every P∈P_{m+2r−1},
  ‖Pv^γ‖_p ∼ (Σ_k Δx_k|Pv^γ|^p(x_k))^{1/p} + σ_m(P)/m^{2γ+2/p},
  with σ_m(P)=Σ_{j<r}(|P^{(j)}(−1)|+|P^{(j)}(1)|)/(j!m^{2j}) and constants independent of m and P, **if and only if** −1/p < r+γ−α/2−1/4 < 1/q.
- **Supporting statements (p. 167).** The ≲ direction "nodal ≲ continuous" holds for arbitrary α>−1, γ≥0, r≥1 and 1≤p<∞, citing Nevai III p. 675 together with Markov, Schur and Nikol'skiĭ. The Δx_k-sum may be replaced by Σ_kλ_m(v^{γp},x_k)|P(x_k)|^p with λ_m(v^{γp},x_k)∼v^{γp}(x_k)√(1−x_k²)/m **at the interior zeros x_k** (audit-02 E1). This is not a global formula: for example λ_m(1,±1)≍m^{−2} while √(1−x²)/m vanishes there. T6 treats the endpoint terms separately. Theorem 2.3 (p. 166) is the corresponding if-and-only-if for interpolation operators.

**Proposition T6 (conditional on Corollary 2.2, including its necessity part, which was not proof-audited here; PROVED from it).** At the CC nodes, inf_{N≥2} λ_−(N,N)=0. That is, sup_N ‖L_N‖_N=∞: there is no N-uniform converse inequality ∫p²≤C Q_N(p²) on the full interpolation space Π_N.

*Proof.* Take α=1/2, so p_m(v^{1/2}) is proportional to U_m. Its zeros are cos(kπ/(m+1)), k=1,…,m: the interior CC nodes for N=m+1. Take r=1, so P_{m+2r−1}=P_{m+1}=Π_N, with γ=0 and p=q=2.

- **The condition fails.** r+γ−α/2−1/4=1−1/4−1/4=1/2, which equals 1/q. The strict right inequality fails, so the two-sided equivalence (2.16) does not hold uniformly in m.
- **Only the converse direction can fail.** The "nodal ≲ continuous" direction is stated to hold for all parameters. So there is no constant C with ‖P‖_2≤C·Γ_m(P) for all m and all P∈Π_{m+1}, where Γ_m(P)=(Σ_kλ_m(1,x_k)P(x_k)²)^{1/2}+(|P(1)|+|P(−1)|)/m (Christoffel form, γ=0).
- **Comparison with Q_N.** λ_m(1,x_k)∼√(1−x_k²)/m ≍ sinθ_k/N ≍ w_k at interior nodes, by T3 (sinθ_k≥2/N there, so the 1/N² term is dominated). (|P(1)|+|P(−1)|)²/m² ≍ w_0(P(1)²+P(−1)²) since w_0≍N^{−2}. With (a+b)²≍a²+b², Γ_m(P)²≍Q_N(P²), with absolute constants.
- **Conclusion.** Hence there is no N-uniform C with ∫P²≤C Q_N(P²) on Π_N. By T1, sup_N 1/λ_−(N,N)=∞. ∎

**Scope (answers audit-01 F4).**
- T6 gives failure of a uniform bound, i.e. an unbounded subsequence. It gives neither a limit along every N nor a rate.
- It is a statement on the full space Π_N. Since V_{N−1}⊂V_N (T2(c)), it says nothing about λ_−(N,N−1).
- Three separate local results supply what no source read supplies (corrected in response-02, audit-02 R1). (i) PD-T019's single exact U_{N−1} evaluation: interior values vanish, so Q_N(U_{N−1}²)=Θ(1) while ∫U_{N−1}²=Θ(log N). Its Rayleigh quotient is Θ(1/log N), asymptotically 2/log N. This gives the **upper bound** λ_−(N,N−1)≤O(1/log N) and vanishing along every N; it is not an eigenvalue asymptotic. (ii) PD-T018's separate harmonic-combination witness gives the stronger upper bound λ_−(N,N−1)≤128000/(log N)². (iii) PD-T017 gives the matching lower bound. Together (ii) and (iii) give the order (1+log N)^{−2}.
- The Gauss-node criteria of Mastroianni–Russo (LIT-293) and Xu (LIT-296), and the same-weight Jacobi theory of König–Nielsen (LIT-294), are analogous classical borderline phenomena. They do not establish the CC statement by themselves.
