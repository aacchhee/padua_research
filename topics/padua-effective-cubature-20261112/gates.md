# Gates — padua-effective-cubature-20261112

Written by Claude (Opus 5.5, orchestrator) on 2026-11-12. This was committed and pushed **before** any run in this topic. Verdicts are appended below each gate with the date, the commit and the evidence path. A pre-registration is never edited after its first push. Changes go in a dated addendum.

Notation (BRIEF §1.2–1.4):
- A_n = {k ∈ ℤ³ : |k|₁ ≤ n−1}, m_n = |A_n| = (2n−1)(2n²−2n+3)/3;
- D = binom(n+2,3) = dim Π_{n−1}(ℝ³), P = binom(n+3,3) is the Padua package count;
- O = {|u|₁ ≤ 1}.

**Torus LP.** The torus Delsarte LP at degree n is

  R_n = sup { f(0)/c₀ : f = Σ_{|k|₁≤2n−2} c_k e^{ik·t} real, f ≥ 0 on 𝕋³ },   ρ_n = R_n/m_n.

Every positive torus measure exact on {|k|₁ ≤ 2n−2} has M ≥ R_n atoms.

**Cube LP.** The cube-native LP of `plan.md` §2 is

  λ_n = sup min_x G(x,x)/K_{n−1}(x,x)², taken over G of bidegree ≤ (2n−1, 2n−1) with G ≥ 0 on [−1,1]³ × [−1,1]³ and ∫∫G dμ⊗μ = D.

Every positive cube rule then has N ≥ λ_n D (proof to be written in theory before any use).

## Q0 — replay (kill: any mismatch)

- **Q0a.** Rerun `topics/padua-3d-20261106/code/fd1_controls.py` from the committed tree. Compare every recorded field with `topics/padua-3d-20261106/evidence/fd1-controls.json`, excluding only timestamps and paths. Outputs go to the scratchpad, never over the committed file.
- **Q0b.** Rerun `fd3_certify.py check` on `fd3-certificate.json`, writing a new receipt in the scratchpad. **Pass:** the checker reports the certificate valid.
- **Q0c.** Recompute from the D3 certificate centres, in floating point, the lifted torus atom count M₃ = Σ orbit sizes and the cube leverages p_j = w_j K₂(x_j,x_j). Check Σ p_j = 10 = D within 1e-10. This reference is used by Q1.

## Q1 — LP sanity (kill: violation, which means a bug)

- **Q1a.** For n = 2…8, the torus LP code evaluated at the fixed feasible f = |D_n|² must return f(0)/c₀ = m_n exactly, in integer arithmetic. The cube code at G = K_{n−1}² must return min_x G(x,x)/K(x,x)² = 1 and ∫∫G = D, in exact rational arithmetic.
- **Q1b.** Upper references. For each n tested:
  - **Torus.** R_n ≤ M_lat(n), the smallest index found of a sublattice L ⊂ ℤ³ with L ∩ {0 < |k|₁ ≤ 2n−2} = ∅. Its dual lattice rule is a positive exact torus design with M_lat(n) atoms. The search must be exhaustive over Hermite normal forms up to the reported index, or the value is reported only as an upper bound.
  - **Cube, n = 3.** λ₃ ≤ D/Σ_j p_j² for the D3 rule (Q0c).
  - **Both LPs.** The optimum must be ≥ the Fisher value: ρ_n ≥ 1, λ_n ≥ 1.

  A numerical value outside these bounds by more than the solver tolerance (1e-6 relative) kills the code until fixed.
- **Q1c.** The LP is discretized on a finite grid, so the computed optimum is an *upper* bound for R_n. Report a rigorous *lower* bound for R_n only after the true minimum of the computed f on 𝕋³ is controlled: a dense evaluation plus a Bernstein/derivative bound. Then f + ε is feasible. Numerical optima are MEASURED.

## Q2 — E1 asymptotic screen (MEASURED)

Pre-registered from handoff 01:

- **Promising** for a fixed fraction if ρ_n ≥ 1.02 at every tested n ≥ 8 and ρ_n is non-decreasing over the last four tested degrees.
- **Kill (fixed γ by plain torus LP):** ρ_n − 1 decreasing like 1/n or faster over the tested n ≤ 16, i.e. the fitted (ρ_n − 1)·n non-increasing over the last four degrees. Equally a kill: a literature or proof result T(2O) = |O|.

The screen is MEASURED only. It cannot prove or refute T(2O) > |O|.

Additional pre-registration (Claude, before runs):
- **Cap.** Every R_n ≤ M_lat(n) (Q1b). Hence, if the lattice of Minkowski's octahedron packing gives M_lat(n)/m_n → 19/18, plain LP can give at most γ_LP ≤ 1/18 in the torus normalisation. This is a proof obligation, written in `theory/`, not a measurement. The screen records ρ_n against M_lat(n)/m_n.

## Q3 — certificate acceptance (unchanged from handoff 01)

A finite exclusion at degree n needs all of:
- an exact rational dual certificate whose nonnegativity is proved, by an SOS or Fejér–Riesz certificate, or by exact sign analysis on a certified mesh with a derivative bound;
- a committed checker;
- an independent rerun on a separate code path.

It must not contradict D3 at n = 3: no certificate may claim N > 20 for every positive degree-5 rule. A torus-LP bound gives only M ≥ R_n. It converts to N only through a proved inequality, for example N ≥ M/8, or the orbit-weighted form written in theory.

## Verdicts

### Q0 verdict — PASS (2026-11-12, orchestrator, at commit 0abf5e7; outputs in the session scratchpad)

- **Q0a.** `timeout 1200 python -B topics/padua-3d-20261106/code/fd1_controls.py --output <scratch>/fd1-controls-replay.json` took 0.6 s on Python 3.13.18 with SymPy (pip, current). Compared with `topics/padua-3d-20261106/evidence/fd1-controls.json`, every field is identical except `seconds_measured`. Code SHA-256 is `e5bf2b92…292d1c`, matching the D1-04 record.
- **Q0b.** `python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt <scratch>/fd3-replay.json` returned verdict `PASS_EXACT_INTERVAL_NEWTON_AND_RANK`. Code SHA-256 is `b8ca61f9…780db`; certificate SHA-256 is `3677318c…18a7d`.
- **Q0c.** `python -B topics/padua-effective-cubature-20261112/code/q0_d3_leverage.py --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --output topics/padua-effective-cubature-20261112/evidence/q0c-d3-leverage.json` gave Σp_j = 10.000… (= D), Σp_j² = 6.11325824, and hence the cube-LP cap **λ₃ ≤ 1.63578890**. M₃ = 160, with all 20 nodes interior. These are MEASURED values at the dyadic centres; the true rule lies within 2^−100.

### Addendum (2026-11-12, before any LP run was reported) — Delsarte variant

After reading KLM 2025 (`literature-effective.md`), the orchestrator added the **Delsarte torus LP** R^Del_{n,K}: the plain LP plus frequencies 2n−2 < |k|₁ ≤ K with c_k ≤ 0 (record `theory/delsarte-bound.md` (a)). Q1a and Q1b apply to it unchanged; lattice rules remain upper references by record -04 (b). The Q2 thresholds are applied to ρ^Del as written for ρ. The plain-LP Q2 literature kill condition ("T(2O) = |O|") is neither met nor refuted: KLM report that it is open.
