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

### Q1 verdict — PASS (2026-11-12, orchestrator; LP subagent runs, evidence `evidence/lp-torus.json`, `lp-lattice.json`, `lp-cube.json`)

- **Q1a, torus: PASS.** For n = 2…8 the autocorrelation of 1_{A_n} has a₀ = m_n and Σa_k = m_n² in integer arithmetic, with spectrum in |k|₁ ≤ 2n−2. So f(0)/c₀ = m_n exactly (`lp_torus.py --q1a`).
- **Q1a, cube: PASS.** For n = 2…8, G = K_{n−1}² gives ∫∫G = D in exact rationals, and G(x,x) = K(x,x)² at the tested rational points (`lp_cube.py --q1a`).
- **Q1b: PASS, no violation.**
  - Every torus run (plain and Delsarte, all n, e) has m_n ≤ R_upper ≤ M_lat(n), up to the 3e-6 relative stopping tolerance above m_n.
  - M_lat(n) is an exhaustive HNF minimum for n = 2…8 and an upper bound only for n = 9…16, as the gate requires. The orchestrator re-verified every witness lattice independently (index and avoidance of 0 < |k|₁ ≤ 2n−2, exact enumeration with SymPy); all 15 PASS.
  - Cube: λ₃ ≈ 1.2104 ≤ 1.6358 (the D3 cap of Q0c), and λ₂, λ₃, λ₄ ≥ 1.
- **Q1c.** No rigorous lower bound above Fisher was obtained.
  - The branch-and-bound lower bound was incomplete for every run.
  - The only rigorous lower bound is therefore R_n ≥ m_n, from |D_n|².
  - All LP optima are cut-plane relaxation values. Each is an upper bound for its continuum LP, up to floating-point solution error, and is MEASURED.
- **Reproducibility caveat.** `lp_torus.py` was edited during the campaign (B&B fix, caps, threads), and four script SHA-256 values occur in `lp-torus.json`. The subagent reports that the early runs (n ≤ 5) were not recomputed under the final SHA. This affects reproducibility of the receipts, not the verdict, because nothing rigorous rests on these values.

### Q2 verdict (2026-11-12, orchestrator; MEASURED)

- **Plain torus LP (BRIEF E1 as written): KILL.**
  - The measured ρ_n = R_n/m_n lies in [1, 1 + 3·10⁻⁶] for every n = 2…12. The lower end is exact (|D_n|²); the upper end is the cut-plane optimum.
  - ρ_n − 1 is therefore zero within tolerance, which is at least as fast as any 1/n decay. So the pre-registered kill applies over the tested range n ≤ 12; the gate named n ≤ 16, and n = 13–16 were not run.
  - The data are consistent with the conjecture T(int 2O) = |O|; record -02 (b) gives R_n ≥ (n−½)³ T(int 2O). This consistency is MEASURED only and is not a proof of anything.
- **Delsarte torus LP: INCONCLUSIVE** (neither promising nor killed), at each schedule tested:
  - **e = n (K = 3n−2):** ρ^Del = 1.0818, 1.0811, 1.0841, 1.0801 at n = 5…8, so it is not non-decreasing over the last four degrees. (ρ−1)·n = 0.41, 0.49, 0.59, 0.64 is increasing, so it is not killed. It was not run for n ≥ 9.
  - **e = 4:** ρ^Del = 1.0548, 1.0493, 1.0450, 1.0412 at n = 7…10. Not promising: decreasing. Not killed: (ρ−1)·n = 0.38, 0.39, 0.41, 0.41 is increasing.
  - **e = 2:** ρ^Del = 1.0182 at n = 8, which is < 1.02, so not promising. (ρ−1)·n increases over n = 5…8, so it is not killed.
  - The existence question this screen was meant to inform is settled independently of the numerics: γ_A > 0 by record -03 (i), with a LITERATURE dependency. What remains is an explicit value (record -05), for which these finite values are not a premise.

### Q3 verdict — not exercised (2026-11-12)

No finite exclusion certificate was produced or submitted in session 1, so no finite exclusion is claimed.
- The torus route cannot exclude packages on the range of record -06, a proved limitation.
- The plain cube LP measured λ₃ ≈ 1.21 and λ₄ ≲ 1.20, against the required 1 + 3/n = 2 and 1.75. That LP cannot produce one at n = 3, 4 (MEASURED; `attempts/E3.md`).

## Addendum G (2026-11-12, before any run of the explicit-γ campaign) — AC: "I authorize up to seven rounds to make gamma explicit"

Target: record -05. That is, an explicit γ₁ > 0 with γ_A ≥ γ₁, and with it N ≥ (1+γ₁)n³/6 for every n (record -03 (ii′)) and an explicit package threshold.

- **G1, admissibility.** A candidate φ must be shown to satisfy the hypotheses of record -02 (c):
  - continuous, real, in L¹(ℝ³), with φ(0) = 1;
  - φ ≤ 0 on {|ξ|₁ ≥ 2};
  - φ̂ ≥ 0 everywhere.
  
  Each inequality needs a proof: an analytic argument, an exact or interval-arithmetic certificate with a stated tail bound, or a cited theorem. Sampling alone never suffices.
- **G2, value.** γ₁ = (3/4)∫φ − 1, or a certified lower bound for it, computed in exact or interval arithmetic.
- **G3, acceptance status.**
  - **PROVED.** Local certificate, committed checker, and an independent rerun on a separate code path.
  - **PROVED with LITERATURE dependency.** The certificate is a published theorem read in full text: its normalisation is transcribed and checked against record -02 (c), and its rigour is recorded.
  - **MEASURED.** A numerical optimum without a certificate. It is never reported as γ₁.
- **G4, sanity.** Any certified value must satisfy γ₁ ≤ 1/18 (record -04). A value above 1/18 means a bug.
- **Kill.** Two consecutive rounds without a new certified γ₁ or a strict improvement of the certified value end the campaign. The ceiling is 7 rounds.

### Addendum G — interim verdict (2026-11-12, after campaign round 2)

- **G1–G2: met.** The developer certificate is in `evidence/gamma-certificate.json`, verdict PASS; γ₁ = 0.0278415686907765546… > 1/36.
- **G3:**
  - PROVED with LITERATURE dependency, via DGOV Table 6: met (round 1).
  - Local PROVED: the certificate and the committed checker are done; the independent rerun is pending.
- **G4: met,** since 1/36 < γ₁ < 1/18.

### Addendum G — final verdict (2026-11-12)

**G1–G4 met; status PROVED (computer-assisted, local).**
- Developer checker `code/gamma_certificate.py`: PASS (`evidence/gamma-certificate.json`).
- Independent rerun on a separate code path, `code/gamma_certificate_indep.py`: PASS (`evidence/gamma-certificate-indep.json`, `independent-checks-gamma.md`). The orchestrator replayed it with the same verdict.
- γ₁ = 0.02784156869077655… ∈ (1/36, 1/18).
- The campaign used 3 of 7 rounds. The improvement direction was stopped after one empty round (round 3); the kill rule was not triggered.

### Q2 corrected verdict and Q1c correction (2026-11-13, response-01; audit-01 A6, A9)

This entry supersedes the 2026-11-12 "Plain torus LP: KILL" verdict above, which is kept for the record.

**Plain torus LP: NOT PROMISING; the pre-registered KILL is NOT established.**
- **Promising test: fails.** ρ_n < 1.02 at every tested n ≥ 8; the largest value is 1 + 4.6·10⁻⁶ at n = 8.
- **Kill test: not met.** The pre-registered kill needs the fitted n(ρ_n − 1) to be non-increasing over the last four tested degrees. From the stored upper values, n(ρ_n − 1) = 2.741·10⁻⁵, 2.644·10⁻⁵, 2.850·10⁻⁵, 3.247·10⁻⁵ at n = 9…12. These are not non-increasing, and no fit was supplied.
- **Why no fit is possible.** All of these values lie at the cut-plane solver's tolerance scale, and the exact lower bound is ρ_n ≥ 1. The data therefore do not determine the sequence ρ_n − 1, and no fit is meaningful.
- **Literature alternative.** The "T(2O) = |O|" alternative of the kill rule remains open (KLM p. 2).
- **What was wrong on 2026-11-12.** That verdict treated values within tolerance as zero. This was a rule added after the fact, not the pre-registered one.
- **Disposition.** The plain-LP route is deferred at the orchestrator's discretion, because it is not promising: the measured values are indistinguishable from Fisher. This is a discretionary stop, not a met KILL. It is also moot for γ: the Delsarte route (records -02, -03, -07) supersedes it, since D ≥ T.

**Q1c and Q2 numerical envelope, corrected.**
- The plain ratios lie in [1, 1 + 5.7·10⁻⁶], not [1, 1 + 3·10⁻⁶]. The maximum is 1 + 5.62·10⁻⁶ at n = 7; n = 8 and 9 are also above 3·10⁻⁶.
- The B&B lower bound was complete in three runs (n = 2, e = 0, 2, 4), with value 6.994 < m₂ = 7. It was incomplete in all other runs. The conclusion is unchanged: no rigorous lower bound above Fisher was obtained.
- **Reproduction command for the cube sanity control.** `--out` is required; the command in handoff 03 omitted it:

  `python3 -B topics/padua-effective-cubature-20261112/code/lp_cube.py --q1a --out <scratch>/q1a-cube.json`.
