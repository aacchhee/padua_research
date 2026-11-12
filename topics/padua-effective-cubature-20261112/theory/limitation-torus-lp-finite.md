# PD-N?padua-effective-cubature-20261112-claude-06 — the finite torus Delsarte LP with M ≤ 8N cannot exclude a Padua package at any n in S

ID kind: PD-N. This is a scoped negative: a proved limitation of one method on a finite range, not a refutation of any claim.
Aliases: finite lattice cap; E1-M1 finite range; "torus LP cannot close 4 ≤ n ≤ …".
Split from: the OPEN "Finite LPs" bullet of record -04. Split into: none.

## Statement

Let S be the set of degrees listed below (`covered_E2n-1` in `../evidence/pdn-lattice-witness.json`). For each n ∈ S there is an explicit integer lattice L_n = A_nℤ³ such that:
- every nonzero vector of L_n has ℓ₁-norm ≥ 2n;
- [ℤ³ : L_n] = |det A_n| ≤ 8·binom(n+3,3).

**Consequence.** Fix n ∈ S and any finite F ⊂ ℤ³. Let f = Σ_{k∈F} c_k e^{ik·t} satisfy the hypotheses of record -02 (a) at exactness E = 2n−1 (f ≥ 0, c₀ > 0, c_k ≤ 0 for |k|₁ ≥ 2n), or at E = 2n−2, or be a plain-LP polynomial for either exactness. Then f(0)/c₀ ≤ 8·binom(n+3,3).

So the lower bound N ≥ f(0)/(8c₀) obtained from record -02 (a) and M ≤ 8N never exceeds binom(n+3,3). This torus route therefore cannot exclude a positive closed-cube rule with binom(n+3,3) nodes exact on Π_{2n−1} at any n ∈ S, whatever spectrum is chosen.

**S = {2, 3, …, 109}** (computed 2026-11-12; see Evidence). With record -03 (iv), this means that **no Padua package at any 4 ≤ n ≤ 109 can be excluded by the torus Delsarte route in any form**: not by the uniform bound, and not by any finite LP at that degree.

For the weaker exactness E = 2n−2 (lattices with min ℓ₁ ≥ 2n−1), the witnesses cover n = 2…128. This is recorded for completeness only, because packages are exact on Π_{2n−1}.

## Assumptions and scope

- "The method" means exactly: the torus Delsarte or plain LP of record -02 (a), applied to the sign-orbit lift, followed by the conversion M ≤ 8N of D1-01.
- Not covered:
  - a sharper M ↔ N conversion that uses orbit sizes;
  - cube-native LPs (IDEA?…-claude-03/-06);
  - separation or Cohn–Elkies inputs;
  - SDP or three-point bounds;
  - any method that uses more than the lift's vanishing Fourier coefficients and positivity.
- This says nothing about whether packages exist at any n.

## Status

**PROVED** (exact finite check; the reduction is record -04 (b′)). The witnesses are verified by two separate code paths (Evidence). The search that found them is heuristic; that does not matter, because only the verified witnesses are used.

## Depends on

- Record -04 (b′): if L avoids 0 < |k|₁ ≤ E, then every f admissible at exactness E has f(0)/c₀ ≤ [ℤ³ : L]. A lattice with minimum ℓ₁ ≥ 2n avoids both 0 < |k|₁ ≤ 2n−1 and 0 < |k|₁ ≤ 2n−2. Plain-LP polynomials are Delsarte-admissible, with vacuous sign conditions.
- Record -02 (a), (d) and D1-01 (M ≤ 8N).

## Proof

Let n ∈ S, let L_n be its witness and let f be as in the Consequence. By record -04 (b′) with E = 2n−1, f(0)/c₀ ≤ [ℤ³ : L_n] ≤ 8·binom(n+3,3). Hence f(0)/(8c₀) ≤ binom(n+3,3). A rule with N = binom(n+3,3) is therefore consistent with every bound of this form. ∎

The finite facts used are |det A_n| and min_{0≠c} |A_nc|₁ ≥ 2n for each n ∈ S. They are checked as follows.

## Evidence

- **Search and first check.** `code/pdn_lattice_witness.py` searched these candidates for the least |det A| with min ℓ₁ ≥ E+1:
  - the roundings A = round(tB) of the Minkowski/Betke–Henk lattice B of record -04, for t ∈ [n−1, n+3] in steps of 0.005;
  - the integral scalings sB with 3 | s;
  - the subagent's lattices (`../evidence/lp-lattice.json`);
  - with `--perturb`, all ±1 entry perturbations of round(tB), t ∈ [n−½, n+1], whenever the base candidates miss 8·binom(n+3,3).
  
  Each accepted witness passes an exhaustive coefficient-box test. For k = Ac with |k|₁ ≤ E, c = A⁻¹k gives |c_i| ≤ max_j |(A⁻¹)_{ij}|·E, in exact rationals, so the box covers every such k.
- **Second, independent path.** `code/pdn_check_ball.py` enumerates the whole ℓ₁ ball |k|₁ ≤ E directly and tests membership by adj(A)k ≡ 0 (mod det A) in exact int64 arithmetic, with an overflow guard. It also recomputes |det A|. It shares no code with the search's exhaustiveness argument.
  - Negative controls: ℤ³ fails at E = 1; 7ℤ³ passes at E = 6 and fails at E = 7.
- **Cross-check with merged results.** `topics/padua-3d-20261106/theory/r08-lattice-minima.md` gives the exact minimum det for min ℓ₁ ≥ 2n, n ≤ 16. Every witness index here is ≥ that minimum, and at n = 3, 6, 9, 12, 15 they are equal (38, 304, 1026, 2432, 4750). For n ≤ 16 the merged minima alone would give the same conclusion; this record does not depend on them.
- **Commands and outputs.** See the Checks section and `../evidence-manifest.json`.

## Checks

Run by the orchestrator on 2026-11-12 (Python 3.13.18, NumPy as installed; versions recorded in the evidence file), from the topic directory.

1. Search: `python3 -B code/pdn_lattice_witness.py --nmin 2 --nmax 140 --extra evidence/lp-lattice.json --perturb --out <scratch>/pdn/witness-final.json`.
   - Script SHA-256 `819558d6…6642514`. It took 12 min 39 s of wall time.
   - Output: covered for E = 2n−1 at n = 2…109 (108 degrees), and uncovered for every n = 110…140, as the packing bound requires. For E = 2n−2 it covered n = 2…128.
   - The tightest case is n = 109, with index 1822682 against 8·binom(112,3) = 1823360.
   - The full output (38.8 KB) is in the session scratchpad only and is regenerable by this command.
2. Second path: `python3 -B code/pdn_check_ball.py --full <scratch>/pdn/witness-final.json --out evidence/pdn-lattice-witness.json`. It took 2 min 54 s. Output: `failures []` for all 139 × 2 witnesses, and a compact evidence file of 10952 bytes. The evidence records the search output's SHA-256 and the checker's SHA-256.
3. Independent Opus check (`../independent-checks-E1b.md`, separate code `indep.py`/`rt.py`):
   - re-verified the witnesses at n = 2…16, 47…50, 108 and 109;
   - matched `min_l1_at_most` against brute force on 399 random matrices.
4. Merged cross-check: every witness at n ≤ 16 is ≥ the r08 minimum (see Evidence).

## Open items

- n ≥ 110: no lattice witness of this kind can exist. The lattice packing bound for the octahedron (Minkowski, via Betke–Henk; LITERATURE, as in `topics/padua-3d-20261106/theory/r08-lattice-minima.md`) gives det L ≥ 38n³/27 for min ℓ₁ ≥ 2n, and 38n³/27 > 8·binom(n+3,3) for n ≥ 110 (the same cubic as record -03 (iv)). So 2…109 is the most this witness method can cover. Whether the torus LP excludes packages at some n ≥ 110 depends on finite LP values that are not known (independent check E1b NOTE-1).

## History

2026-11-12, Claude (Opus 5.5 xhigh, orchestrator). Written in session 1 after the LP numerics. It needs the Codex audit.
