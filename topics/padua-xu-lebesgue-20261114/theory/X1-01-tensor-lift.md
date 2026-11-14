# PD-T?padua-xu-lebesgue-20261114-claude-01 — Tensor lift of the Xu fundamental functions

ID kind: PD-T.
Aliases: X1-01; rotated-torus lift; Xu interpolation as symmetrized tensor trigonometric interpolation; fiber-sum formula.
Split from: none (supporting identity for round X1-2 targets T1–T4).
Split into: none.

## Statement

Let n ≥ 1 be an integer (both parities). With the definitions below:

**(a) Fibers.** For every (p, q) ∈ C_n × C_n the point Φ(u_p, u_q) is a Xu node. The fibers F(ξ) = {(p, q) ∈ C_n × C_n : Φ(u_p, u_q) = ξ}, ξ ∈ X_n, are nonempty, partition C_n × C_n, are exactly the orbits of the group Γ, and |F(ξ)| = 2^{3−β(ξ)}, where β(ξ) ∈ {0, 1, 2} is the number of coordinates of ξ equal to ±1.

**(b) Unisolvence and lift formula.** For every ξ ∈ X_n there is exactly one ℓ_ξ ∈ V_n with ℓ_ξ(η) = δ_{ξη} for all η ∈ X_n (so X_n is unisolvent for V_n), and for all (u, v) ∈ ℝ²

  ℓ_ξ(cos(u+v), cos(u−v)) = Σ_{(p,q) ∈ F(ξ)} d_n(u − u_p) · d_n(v − u_q).   (1)

## Definitions

- z_k = cos(kπ/n). X_n = {(z_r, z_s) : 0 ≤ r, s ≤ n, r + s ≡ n+1 (mod 2)} (Xu points; `literature-xu-mp.md` §1).
- σ = +1 for n even, σ = −1 for n odd. E_j(x, y) = T_{n−j}(x)T_j(y) − σ T_j(x)T_{n−j}(y), T_k the unscaled Chebyshev polynomials. V_n = Π_{n−1} ⊕ span{E_j : 0 ≤ j < ⌈n/2⌉}, Π_{n−1} = bivariate polynomials of total degree ≤ n−1.
- C_n = {p ∈ ℤ/4nℤ : p ≡ n+1 (mod 2)} (2n residues; well defined because 4n is even). u_p = pπ/(2n).
- d_n(t) = (1/(2n)) (1 + 2 Σ_{j=1}^{n−1} cos(jt) + cos(nt)). Equivalently d_n(t) = sin(nt) cot(t/2)/(2n) for t ∉ 2πℤ and d_n(t) = 1 for t ∈ 2πℤ.
- Φ : ℝ² → Q = [−1,1]², Φ(u, v) = (cos(u+v), cos(u−v)). Φ is onto Q.
- τ(p, q) = (p+2n, q+2n), s(p, q) = (q, p), c(p, q) = (−q, −p) are commuting involutions of C_n × C_n (2n is even and −q ≡ q mod 2, so the class is preserved; τc = cτ because −2n ≡ 2n mod 4n). Γ = (ℤ/2)³ = {τ^a s^b c^e : a, b, e ∈ {0,1}}, of order 8, acting on C_n × C_n through them. The action need not be faithful (for n = 1, s and c act identically); only orbits and sums over the eight elements are used.

## Assumptions

Exact real arithmetic; the node set and the space V_n exactly as above. No kernel formula of Xu 1996 / BCDMV is used.

## Status by part

Overall status: **PROVED** (written proof below; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) fibers = Γ-orbits, sizes | PROVED | §1 below |
| (b) unisolvence and formula (1), every n ≥ 1 | PROVED | §§2–5 below |
| Agreement of (1) with Path A (arb Vandermonde) and Path B (Xu/BCDMV kernel) | MEASURED (verification only) | Checks |

## Depends on

Nothing beyond finite geometric sums and product-to-sum formulas. Not used: Xu's compact kernel, cubature exactness, PR #27.

## Checks

Run by the researcher on 2026-11-14 (Python 3.13.18, mpmath 1.4.1, python-flint 0.9.0), from the topic directory:

- `python3 code/xu/research/x1_lift_exact_check.py --nmax 10` → for n = 1..10, 3 seeded random points each, every node: arb enclosure (512 bits) of ℓ_ξ^{Path A}(x) − (right side of (1)) contains 0, max radius 1.8e−133; `ALL OK`. Path A (`code/xu/xu_exact.py`) solves the Vandermonde system of V_n and uses no kernel formula.
- `python3 code/xu/research/x1_lift_check.py` (mpmath 40 digits, n = 1..12, 6 seeded points each) → max |ℓ_ξ^{Path B} − (1)| over all nodes: `WORST 1.9905e-38` (n ≥ 2; Path B = `code/xu/xu_kernel.py`); fiber sizes {4, 8} (n even), {2, 4, 8} (n odd); Σ|F(ξ)| = 4n².

Outputs: `/tmp/x1r2/lift_exact.json`, `/tmp/x1r2/lift_check.json` (not committed; regenerate with the commands).

## Sources

- LITERATURE (context, not a proof input): Xu, JAT 87 (1996) §2 defines X_n and the interpolation space; conventions as fixed in `literature-xu-mp.md` §1.
- LITERATURE pointer, **digest-level read only** (WebFetch digests of ar5iv HTML, characters 0–100k and 200k–500k of 905k, 2026-11-14; not a fulltext read): Li–Sun–Xu, "Cubature formula and interpolation on the cubic domain", Numer. Math. Theory Methods Appl. 2 (2009) 119–152, arXiv:0808.0180, §3.3 (Prop. 3.6, Lemmas 3.7–3.8, Thms 3.9–3.10) derives interpolation on [−1,1]² at Chebyshev checkerboard nodes from lattice trigonometric interpolation with a symmetrization operator; the digest says the odd-n scheme is the one of their ref. [19] and the even-n scheme there has a different number of points. So an identity equivalent to (1) is very likely in the literature for at least odd n. **No novelty is claimed for (1).** The digest found no Lebesgue-constant statement in that paper's §3. The orchestrator should fulltext-read and LIT-register this source.

## Proof or evidence

**§0. The kernel d_n.** Σ_{|j|≤n−1} e^{ijt} = sin((n−½)t)/sin(t/2) for t ∉ 2πℤ, and sin((n−½)t) + cos(nt) sin(t/2) = sin(nt) cos(t/2). Hence 1 + 2Σ_{j=1}^{n−1}cos(jt) + cos(nt) = sin(nt) cot(t/2), which gives the two forms of d_n. d_n is an even, 2π-periodic trigonometric polynomial with d_n(0) = 1.

*Cardinality.* For p, p′ ∈ C_n the difference p − p′ = 2m is even and u_p − u_{p′} = mπ/n. If m ≡ 0 (mod 2n) then d_n(u_p − u_{p′}) = 1. Otherwise sin(n·mπ/n) = 0 and mπ/(2n) ∉ πℤ, so d_n(u_p − u_{p′}) = 0. Thus d_n(u_p − u_{p′}) = δ_{pp′} on C_n.

*Top frequency.* cos(n(u − u_p)) = cos(nu − pπ/2) = cos(nu)cos(pπ/2) + sin(nu) sin(pπ/2). For n even, p is odd and this is ε_p sin(nu), ε_p = sin(pπ/2) = ±1. For n odd, p is even and this is ε_p cos(nu), ε_p = cos(pπ/2) = ±1. Put κ_n(u) = sin(nu) (n even), κ_n(u) = cos(nu) (n odd). Then for p ∈ C_n

  d_n(u − u_p) ∈ 𝒯_n := span_ℂ{e^{iju} : |j| ≤ n−1} ⊕ ℂ κ_n.   (2)

**§1. Fibers (part (a)).** Let (p, q) ∈ C_n². Then p ± q is even; put r₀ = (p+q)/2, s₀ = (p−q)/2. These are well defined in ℤ/2nℤ, and r₀ + s₀ ≡ p ≡ n+1 (mod 2). Φ(u_p, u_q) = (cos(r₀π/n), cos(s₀π/n)) = (z_r, z_s), where r, s ∈ [0, n] are the representatives with r ≡ ±r₀, s ≡ ±s₀ (mod 2n). Since 2n is even, r + s ≡ r₀ + s₀ ≡ n+1 (mod 2), so Φ(u_p, u_q) ∈ X_n. Conversely (z_r, z_s) ∈ X_n is the image of (p, q) = (r+s, r−s), both ≡ r + s ≡ n+1 (mod 2). So the fibers are nonempty and partition C_n².

The map (p, q) ↦ (r₀, s₀) ∈ (ℤ/2n)² is exactly 2-to-1 onto {r₀ + s₀ ≡ n+1 (mod 2)}: (p, q) and τ(p, q) have the same image, and if (p, q), (p′, q′) have the same image then p′ ≡ p, q′ ≡ q (mod 2n) with (p′+q′)/2 ≡ (p+q)/2 (mod 2n), which excludes (p+2n, q) and (p, q+2n). On (r₀, s₀) the generators act by τ: identity, s: (r₀, −s₀), c: (−r₀, s₀). Two points of C_n² lie in the same fiber iff their images agree up to the signs (±r₀, ±s₀), i.e. iff they lie in the same Γ-orbit. The number of sign patterns is 2^{2−β} (r₀ ≡ −r₀ mod 2n iff r ∈ {0, n}, likewise s), so |F(ξ)| = 2 · 2^{2−β} = 2^{3−β}. ∎(a)

**§2. The fiber sum is Γ-invariant.** Fix ξ and put M_ξ(u, v) = Σ_{(p,q)∈F(ξ)} d_n(u − u_p) d_n(v − u_q). Using that F(ξ) is Γ-invariant and d_n is even and 2π-periodic:

- M_ξ(u+π, v+π) = Σ d_n(u − u_{p−2n}) d_n(v − u_{q−2n}) = M_ξ(u, v) (reindex by τ);
- M_ξ(v, u) = Σ d_n(u − u_q) d_n(v − u_p) = M_ξ(u, v) (reindex by s);
- M_ξ(−v, −u) = Σ d_n(v + u_p) d_n(u + u_q) = Σ d_n(u − u_{−q}) d_n(v − u_{−p}) = M_ξ(u, v) (reindex by c).

Define the operators (τ*h)(u,v) = h(u+π, v+π), (s*h)(u,v) = h(v,u), (c*h)(u,v) = h(−v,−u) on functions on ℝ²; they commute and are involutions on (2π)²-periodic functions. Let 𝒮 = ¼(1 + s* + c* + s*c*), with (s*c*h)(u,v) = h(−u,−v), and 𝒜 = ½(1 + τ*)𝒮. Then 𝒜M_ξ = M_ξ, and 𝒜 s* = 𝒜.

**§3. 𝒜 maps 𝒯_n ⊗ 𝒯_n into V_n ∘ Φ.** Write θ₁ = u+v, θ₂ = u−v, (x, y) = Φ(u, v) = (cos θ₁, cos θ₂). By (2) each product d_n(u − u_p)d_n(v − u_q) is a complex combination of the functions (i)–(iii) below; we show that 𝒜 maps each of them to P∘Φ with P in V_n ⊗ ℂ.

(i) h = e^{i(m₁u+m₂v)}, |m₁|, |m₂| ≤ n−1. τ*h = (−1)^{m₁+m₂}h, so 𝒜h = 0 if m₁+m₂ is odd. If m₁+m₂ is even put k = (m₁+m₂)/2, l = (m₁−m₂)/2; then m₁u+m₂v = kθ₁+lθ₂ and m₂u+m₁v = kθ₁−lθ₂, and
 𝒜h = 𝒮h = ½[cos(kθ₁+lθ₂) + cos(kθ₁−lθ₂)] = cos(kθ₁)cos(lθ₂) = T_{|k|}(x)T_{|l|}(y), with |k|+|l| = max(|m₁|,|m₂|) ≤ n−1. This lies in Π_{n−1}.

(ii) n even. For h = sin(nu)e^{imv}, |m| ≤ n−1: τ*h = (−1)^m h (n even), so 𝒜h = 0 for m odd. For m even put k = (n+m)/2, l = (n−m)/2 ∈ {1, …, n−1}, k + l = n. Then
 𝒮h = (i/2)[sin(nu)sin(mv) + sin(nv)sin(mu)], and, since nu+mv = kθ₁+lθ₂, nu−mv = lθ₁+kθ₂, nv+mu = kθ₁−lθ₂, nv−mu = lθ₁−kθ₂,
 sin(nu)sin(mv) + sin(nv)sin(mu) = ½[cos(lθ₁+kθ₂) + cos(lθ₁−kθ₂) − cos(kθ₁+lθ₂) − cos(kθ₁−lθ₂)] = T_l(x)T_k(y) − T_k(x)T_l(y).
 This is E_k if k < n/2, −E_l if k > n/2, and 0 if k = l; in every case it is in span{E_j : 1 ≤ j ≤ n/2 − 1} ∪ {0}. For h = e^{imu} sin(nv) = s*(sin(nu)e^{imv}) the same value results because 𝒜s* = 𝒜. For h = sin(nu) sin(nv): τ*h = s*h = c*h = h, so 𝒜h = h = ½[cos(nθ₂) − cos(nθ₁)] = −½E₀.

(iii) n odd. For h = cos(nu)e^{imv}, |m| ≤ n−1: τ*h = (−1)^{m+1}h (n odd), so 𝒜h = 0 for m even. For m odd (hence |m| ≤ n−2), with k = (n+m)/2, l = (n−m)/2 ∈ {1, …, n−1}, k ≠ l, k + l = n:
 𝒮h = ½[cos(nu)cos(mv) + cos(nv)cos(mu)] = ¼[cos(kθ₁+lθ₂) + cos(lθ₁+kθ₂) + cos(kθ₁−lθ₂) + cos(lθ₁−kθ₂)] = ½[T_k(x)T_l(y) + T_l(x)T_k(y)] = ½E_{min(k,l)},
 and 1 ≤ min(k, l) ≤ (n−1)/2. Again e^{imu}cos(nv) gives the same value. For h = cos(nu)cos(nv): invariant under τ*, s*, c*, and h = ½[cos(nθ₁)+cos(nθ₂)] = ½E₀.

**§4. Descent.** By §2 and §3, M_ξ = 𝒜M_ξ = P∘Φ with P ∈ V_n ⊗ ℂ. M_ξ is real-valued and Φ maps onto Q, so Im P vanishes on Q, hence identically (a polynomial vanishing on a set with nonempty interior); thus P =: P_ξ ∈ V_n and M_ξ = P_ξ∘Φ.

**§5. Cardinality and uniqueness.** Let η ∈ X_n and choose (p′, q′) ∈ F(η) (part (a)). By the cardinality of d_n,
 P_ξ(η) = M_ξ(u_{p′}, u_{q′}) = Σ_{(p,q)∈F(ξ)} δ_{pp′}δ_{qq′} = δ_{ξη},
because the fibers are disjoint. Hence the evaluation map V_n → ℝ^{X_n} is onto. V_n is spanned by n(n+1)/2 + ⌈n/2⌉ functions, and |X_n| = n(n+2)/2 (n even), (n+1)²/2 (n odd), which equals n(n+1)/2 + ⌈n/2⌉ in both cases. So the evaluation map is a bijection, the functions ℓ_ξ are unique, ℓ_ξ = P_ξ, and (1) holds. ∎

## Scope

An exact identity for every n ≥ 1 and both parities, derived from the definitions of X_n and V_n only. It gives an independent proof of unisolvence. It does not by itself bound the Lebesgue function; see X1-03 to X1-05.

## Open items

- Audit. Fulltext read and LIT record for Li–Sun–Xu 2009 (see Sources), to state precisely which part of (1) is already published.

## History

2026-11-14, Claude Fable 5.2 (xhigh), researcher of round X1-2 (subagent; no git access, rules as read by the orchestrator at `2d60e22`). Found while explaining why the vertex value is the perfect square L_n² (T0): in the rotated angles u = (θ₁+θ₂)/2, v = (θ₁−θ₂)/2 the Xu nodes form a tensor grid of 2n equispaced points per variable.
