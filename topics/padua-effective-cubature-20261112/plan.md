# Plan — padua-effective-cubature-20261112

Claude (Opus 5.5, orchestrator and mathematics), 2026-11-12. This is a working plan with no claim status. Claims live in `theory/` once written.

## 1. Session-1 scope and ownership

| Work | Owner (model) | Files |
|---|---|---|
| C0 corollary record and novelty gate | subagent C0 (Sonnet 5.5 high, mechanical assembly) | `theory/lebesgue-constant-corollary.md`, `novelty-gate-C0.md` |
| C0 independent check | separate subagent (Opus 5.5 high) | `independent-checks-C0.md` |
| Torus and cube LP code, lattice upper references, Q1 | subagent LP (Sonnet 5.5 high) | `code/lp_*.py`, `evidence/lp-*.json` |
| Q0 replay, literature, cap theorem, gates, LOG, results | orchestrator | everything else |

## 2. The two LP relaxations (derivations, to be moved into theory when used)

**Torus form (BRIEF §1.4).**
- Setting: lifted masses v_j > 0, Σ v_j = 1, exact on characters with |k|₁ ≤ 2n−2. Let f ≥ 0 on 𝕋³ with spectrum in that set.
- Then Σ_{j,l} v_j v_l f(t_j − t_l) = c₀, so f(0) Σ v_j² ≤ c₀ and M ≥ f(0)/c₀.
- The LP dual is: minimise the total mass of a positive measure ν that has an atom of mass 1 at 0 and is exact (ν̂(k) = 0) for 0 < |k|₁ ≤ 2n−2.
- A lattice rule containing 0 is dual-feasible with value M. Hence R_n ≤ M_lat(n) for every n. This is the source of the cap in gates.md, and it is elementary.

**Cube form (new formulation, to be checked).**
- Setting: positive cube rule (x_i, w_i), exact on Π_{2n−1} for μ. Let G(x,y) = Σ_r a_r(x) b_r(y) with all deg a_r, deg b_r ≤ 2n−1, and G ≥ 0 on cube².
- Then Σ_{i,j} w_i w_j G(x_i,x_j) = ∫∫G dμ⊗μ, so Σ_i w_i² G(x_i,x_i) ≤ ∫∫G.
- Write p_i = w_i K(x_i,x_i), with K = K_{n−1} the Christoffel–Darboux kernel of Π_{n−1}. Then Σ p_i = D (D1-01).
- If G(x,x) ≥ λ K(x,x)² on the cube and ∫∫G = D, then λ Σ p_i² ≤ D.
- Since Σ p_i² ≥ D²/N by Cauchy–Schwarz, N ≥ λ D. G = K² gives λ = 1, which is Fisher's bound.
- The optimum λ_n is capped by D/Σ p_i² of every positive rule; at n = 3 this means the D3 rule.
- **A package excluded at degree n needs λ_n > P/D = 1 + 3/n.** At n = 4 that is 1.75.

## 3. Arithmetic constraint on finite exclusions (orchestrator, to be proved in theory)

Suppose the torus LP is capped by lattice rules, i.e. R_n ≤ M_lat(n) ≈ (19/18) m_n. The only proved route from M to N is N ≥ M/8, and m_n/8 = n³/6 − n²/4 + O(n), while P = n³/6 + n² + O(n). So the plain torus LP cannot exclude a package unless roughly (1/18)·n³/6 > (5/4)n², i.e. n ≳ 135. The exact finite range needs explicit lattices at each n and goes in a PD-N record.

The cube LP is not capped by torus lattices (they are not sign-symmetric). Its finite values are therefore the only plain-LP candidate for E3 at small n.

## 4. Order of work

1. gates.md pushed → Q0 → launch LP code (Q1, then Q2 screen) and C0 in parallel.
2. Literature: the Turán constant of the octahedron; the bound T(2Ω) ≤ |Ω|/δ(Ω) via packings; Minkowski's 18/19 octahedron lattice packing. Record LIT entries after fulltext reads.
3. Theory: cap theorem (torus LP ≤ lattice rules; γ_LP ≤ 1/18); finite-range negative for plain-LP exclusions; cube-LP soundness lemma.
4. Decide E1 by Q2; E3 by the cube-LP values at n = 4, 5, 6; E2 deferred unless time remains.
