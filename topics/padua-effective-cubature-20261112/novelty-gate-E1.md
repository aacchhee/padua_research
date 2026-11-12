# Novelty gate — E1/E2/E3 mechanisms (session 1)

Claude (Opus 5.5, orchestrator), 2026-11-12, at branch head `0f1d797`.

## Scope and terms

- `state/IDEAS.md`, 1278 lines:
  - all section headings scanned, plus the obstruction table at L106–117 read in full;
  - the Padua 3D block L1157–1278 read row by row, every row's aliases;
  - full rows read for IDEA-616 (D1, PD-T557), IDEA-626/683/684/692 (octahedral packing, T9-PACK PD-T618), IDEA-645 (DST/Möller) and IDEA-654 (explicit octahedral Fourier lower bound).
- Terms grepped (case-insensitive) across `state/IDEAS.md`, `topics/`, `tracks/` and `literature/INDEX.md`:
  - "Delsarte", "linear program", "Turán/Turan", "Cohn–Elkies", "LP bound", "positive definite";
  - "packing", "18/19", "Christoffel", "leverage", "Möller".
- Hits:
  - "Delsarte/Turán" occurs only in `topics/padua-3d-20261106/frontier-2026-11-08/S4.md` L78 ("A Delsarte/Cohn–Elkies LP … would make c explicit. The lattice value is 1/18") and in S2 L67 (spherical-design consistency check);
  - no IDEA entry uses a Delsarte or Turán mechanism;
  - LIT-663 (Kuperberg) and LIT-640 (Betke–Henk) are the closest literature records.
- Literature: `literature-effective.md` (KLM 2025 read in full text; Kuperberg pp. 5 and 14–15 re-read).

## Candidates

| Provisional ID | Mechanism | Closest entries and difference | Separation criterion / kill test | Verdict and disposition |
|---|---|---|---|---|
| IDEA?padua-effective-cubature-20261112-claude-01 | Delsarte LP on the sign-orbit torus lift. f ≥ 0, with Fourier coefficients ≤ 0 beyond the exact range, gives M ≥ f(0)/c₀. Continuous transference gives M ≥ (n−½)³∫φ for Delsarte functions of int 2O. Strictness D(int 2O) > 4/3 comes from KLM Thm 6.4. | **IDEA-616/PD-T557 (D1):** same conclusion (fixed excess, positive closed-cube rules), different proof. D1 uses compactness to a stationary law plus Greenfeld–Lev spectrality. This route uses an inequality valid at every n, plus the Delsarte–tiling theorem. **IDEA-684/PD-T618:** lattice cosets only. **Kuperberg/Xu (LIT-663):** LP method for positive cubature is known in principle. **KLM:** no cubature application. | **Separation:** gives N ≥ c·(2n−1)³/48 for all n, with a single named constant. D1 gives only eventual existence. **Kill:** (a) a transcription error in KLM 6.4 or in Δ(O) = int 2O; (b) measured ρ^Del_n failing to exceed the Fisher trend at every tested n (Q2 adapted), which would signal a bug, since a theorem cannot fail numerically. | **Variant (new combination of known tools)**, survived. Records -02 (PROVED), -03 (PROVED with LITERATURE dependency) and -04 (cap, PROVED). No priority claim. |
| IDEA?padua-effective-cubature-20261112-claude-02 | BRIEF E1 as written: plain LP, spectrum ⊂ exact range ↔ Turán constant T(int 2O). | KLM p. 2: whether any convex body is non-Turán is a major open problem. T is unknown even for the regular octagon. | Deciding T(int 2O) > 4/3 would produce the first non-Turán convex body. | **Deferred** (not rejected). Superseded for the γ question by -01, since D ≥ T. Resume only if a non-Turán criterion such as KLM Cor 6.6 becomes checkable for O. MEASURED plain-LP values are still recorded (Q2). |
| IDEA?padua-effective-cubature-20261112-claude-03 | Cube-native LP: G(x,y) of bidegree ≤ (2n−1, 2n−1), G ≥ 0 on cube², G(x,x) ≥ λK(x,x)², giving N ≥ λD (plan.md §2). | Escapes the factor-8 loss and the torus-lattice cap, because sign-symmetry is built in. Capped by D/Σp_j² of any positive rule; this is 1.636 for D3 at n = 3 (Q0c). | Kill for E3: measured λ_4 ≤ 1.75 (P/D at n = 4) would mean it cannot exclude n = 4. | **Pending** numerics (LP subagent PART 3). |
| IDEA?padua-effective-cubature-20261112-claude-04 | Cohn–Elkies-type strengthening: impose f ≥ 0 only off a forbidden-difference region supplied by separation of high-leverage atoms. | BRIEF §1.4; S4 L78. | Needs a proved finite separation lemma for all atoms, not only high-leverage ones. | **Deferred.** Resume once a finite separation statement with explicit constants exists. |
| IDEA?padua-effective-cubature-20261112-claude-05 | E2 quantitative compactness: quantify D1-02/03 and the non-spectrality of O. | IDEA-616 chain. | Expected constants are far below those of -01. | **Deferred.** -01 already gives the uniform form. Resume if the certified-φ target (record -05) fails. |

## Verdict

One surviving mechanism (-01), recorded as a variant/new combination with no priority claim. The other candidates are deferred or pending with resume conditions. Final IDEA numbers are allocated at PR preparation.
