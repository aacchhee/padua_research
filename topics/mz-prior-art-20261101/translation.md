# Translation lemmas used by the prior-art comparison

Author: Claude (Opus 5.5), 2026-11-01, rules `9739a0c`. Status of each item: **PROVED** here as a routine supporting step for the literature comparison; it is not registered as a new PD-T (it adds no new mathematical claim about CC beyond restating PD-T017/PD-T018 in operator language). The auditor should check it as part of this topic.

Conventions are those of PD-T013/PD-T017: N≥2, θ_k=kπ/N, x_k=cos θ_k (0≤k≤N), ℓ_k∈Π_N the Lagrange cardinal polynomials, CC weights w_k=∫_{-1}^{1}ℓ_k dx>0 (PD-T013), Q_N(f)=Σ_k w_k f(x_k), and

  λ_−(N,n)=inf_{0≠p∈Π_n} Q_N(p²)/∫p²,  0≤n≤N.

## T1. Operator form of the minimum eigenvalue

For 0≤n≤N let V_n={(p(x_k))_{k=0}^N : p∈Π_n}⊂ℝ^{N+1} (so V_N=ℝ^{N+1}) and L_N v=Σ_k v_kℓ_k. Equip ℝ^{N+1} with ‖v‖_w²=Σ_k w_k v_k² and Π_N with ‖p‖²=∫_{-1}^1 p² dx. Define ‖L_N‖_n=sup_{0≠v∈V_n}‖L_N v‖/‖v‖_w.

**Lemma T1.** ‖L_N‖_n² = 1/λ_−(N,n) for every 0≤n≤N.

*Proof.* The evaluation map E:Π_n→V_n, p↦(p(x_k)), is linear and onto by definition, and injective because a polynomial of degree ≤N vanishing at N+1 distinct nodes is zero. For p∈Π_n⊂Π_N, L_N(Ep)=p (uniqueness of interpolation). Hence for v=Ep≠0, ‖L_N v‖²/‖v‖_w² = ∫p²/Q_N(p²), and Q_N(p²)=Σw_k p(x_k)²>0 because all w_k>0 and Ep≠0. Taking the supremum over p gives 1/λ_−(N,n). ∎

**Corollary T2.**
(a) PD-T017 (∫p²≤K_N Q_N(p²) on Π_N) is equivalent to ‖L_N‖_N≤√K_N, i.e. the weighted nodal ℓ²(w)→L²(dx) norm of Lobatto/CC interpolation is O(1+log N).
(b) PD-T018 (λ_−(N,N−1)≤128000/(log N)²) is equivalent to ‖L_N‖_{N−1}≥(log N)/√128000.
(c) V_{N−1}⊂V_N, so ‖L_N‖_{N−1}≤‖L_N‖_N. A source proving only ‖L_N‖_N≍log N therefore implies the order in PD-T017 and the *full-space* statement λ_−(N,N)≲(log N)^{−2}, but **not** PD-T018, whose growth witness must lie in V_{N−1}. Here V_{N−1} is the hyperplane where the T_N-coefficient of the interpolant vanishes, i.e. Σ''_k (−1)^k v_k=0 (double prime: endpoint terms halved), by the discrete cosine-transform formula for Chebyshev–Lobatto interpolation.

So "nodal-ℓ² to L² norm ≍ log N ⇔ λ_min ≍ (1+log N)^{−2}" holds exactly, with the same comparison constants, when both sides refer to the same subspace (Π_N or Π_{N−1}) and the same weights w_k.

## T3. Weight comparison

**Lemma T3.** For every N≥2 and 0≤k≤N, with Δ_N(x)=√(1−x²)/N+1/N²,

  ½ Δ_N(x_k) ≤ w_k ≤ 5 Δ_N(x_k).

*Proof.* Interior 1≤k≤N−1: PD-T017 §1 eq. (1) gives sinθ_k/N≤w_k≤5 sinθ_k/N, and eq. (2) gives w_k≥m_k/N²≥1/N². So w_k≥max(sinθ_k/N,1/N²)≥½Δ_N(x_k), and w_k≤5 sinθ_k/N≤5Δ_N(x_k). Endpoints: w_0=w_N equals 1/N² (N odd) or 1/(N²−1)≤2/N² (N even), so ½Δ_N(±1)=1/(2N²)≤w_0≤2/N²≤5Δ_N(±1). ∎

**Consequence.** If a source proves, for p∈Π_n, ∫p²≤C Σ_k μ_k p(x_k)² with μ_k≤A w_k for all k, then λ_−(N,n)≥1/(CA); if it proves Σ_k μ_k p(x_k)²≤C′∫p² with μ_k≥a w_k, then λ_+(N,n)≤C′/a. Quadrature-sum weights comparable to Δ_N(x_k) (Christoffel numbers of Lebesgue measure, local spacing Δx_k) can therefore be exchanged with CC weights at a cost of absolute constants. Such an exchange preserves orders (e.g. log N) but **never** a sharp constant such as an upper constant below 2.

## T4. What Mastroianni–Totik (2000) gives at CC nodes

Source statement (LITERATURE, Mastroianni–Totik, Constr. Approx. 16 (2000), §7, pp. 65–66, the algebraic Marcinkiewicz inequality stated as the translation of their Theorem 4.2 under x=cos t; read 2026-11-01). For a doubling weight w on [−1,1] and 1≤p<∞ there are constants M, C such that for all n and all p_n∈Π_n,
∫|p_n|^p w ≤ C Σ_j |p_n(x_j)|^p Δ_n(x_j) w_n(x_j)
whenever x_j=cos ξ_j, −1=x_0<…<x_S=1, with angular gaps ξ_{j+1}−ξ_j ≤ 1/(Mn); and, for every M, a converse inequality with constant C_M when the gaps are ≥1/(Mn). Here Δ_n(x)=√(1−x²)/n+1/n² and w_n(x)=Δ_n(x)^{−1}∫_{x−Δ_n(x)}^{x+Δ_n(x)}w. For w≡1, w_n≡1 (up to the endpoint truncation, which only changes constants).

**Proposition T4 (consequence, PROVED here from the cited statement; dependence on that LITERATURE statement explicit).** Let M,C be the Mastroianni–Totik constants for w≡1, p=2. If N≥2πM and 0≤n≤N/(πM), then λ_−(N,n)≥1/(8π²M²C).

*Proof.* Without loss of generality M≥1: a gap hypothesis ≤1/(Mn) is implied by ≤1/(M′n) for M′≥M, so the cited inequality persists with M replaced by max(M,1). Put n″=⌊N/(πM)⌋. Since n is an integer with n≤N/(πM), n≤n″, so Π_n⊂Π_{n″}; and N/(πM)≥2 gives n″≥N/(πM)−1≥N/(2πM)≥1. The CC angular gaps are π/N≤1/(Mn″). The cited inequality gives ∫p²≤C Σ_j p(x_j)²Δ_{n″}(x_j). Because N/n″≤2πM and 2πM≥1, Δ_{n″}(x)=(N/n″)√(1−x²)/N+(N/n″)²/N²≤(2πM)²Δ_N(x). By T3, Δ_N(x_j)≤2w_j. Hence ∫p²≤8π²M²C·Q_N(p²). ∎

Thus Mastroianni–Totik **implies part** of PD-T023/PD-T024: a positive lower Gram bound uniformly for n≤θ₀N with an unspecified absolute θ₀=1/(πM) and unspecified constant. It gives neither every θ<1, nor explicit constants, nor any upper constant below 2 (PD-T022), nor the endpoint law. For n≤N/2 the upper side is trivial anyway (exactness gives λ_+=1).

## T5. Why Lubinsky (1999) Theorem 1.7 stops at the CC endpoint case (analysis, not a source claim)

Lubinsky's Theorem 1.7 (Constr. Approx. 15 (1999), p. 583) gives, for P∈Π_{n−1} at n ordered points satisfying the spacing condition (1.7), ∫|Pν|^p ≤ C Σ_j |P(t_j)|^p {∫_{t_{j−K}}^{t_{j+K+1}}|ℓ_jν|^p + δ_jω(t_j)^p/[δ_j|π_n′(t_j)|]^p}, with ω(t)=(|1−|t/b||+c)^σ and the **open** range −1/p<σ<1−1/p in (1.29), under |π_nν|≤ω (1.16) and (1.31).

Apply it with p=2, ν≡1, the N+1 Lobatto nodes (n=N+1, so P∈Π_N), b=1. The nodal polynomial is π(cos θ)=sin θ·sin Nθ (a multiple of (1−x²)U_{N−1}), so |π|≤(1−x²)^{1/2}≤√2(1−|x|)^{1/2}. The natural exponent is σ=1/2=1−1/p, which is exactly the excluded endpoint of (1.29). For any admissible σ<1/2 one may normalize |π|≤C(1−|x|+c)^σ. At an interior node |π′(t_j)|=N and δ_j≍sinθ_j/N, so the second term is ≍ (sinθ_j)^{4σ}/(N sinθ_j) ≍ w_j·(sinθ_j)^{4σ−2}. Near the endpoints this exceeds the CC weight by a factor up to ≍N^{2−4σ}, and the theorem's constant C=C(σ,…) is not tracked as σ→1/2. So the theorem yields neither an O(log N) CC-weighted bound nor a matching lower bound. The CC/Lebesgue case is precisely the borderline it excludes; this is consistent with the logarithmic growth in PD-T017/PD-T018.
