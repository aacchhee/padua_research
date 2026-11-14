# Independent check E1b: exactness range E, threshold 110, lattice witnesses

Checker: Claude subagent, Opus 5.5 (`claude-opus-5-5`). I am an independent mathematical checker and did not write the records under review. This check supplements the Codex audit and does not replace it. I ran no Git command. I edited none of the reviewed files, and this file is the only one I wrote in the repository. Scratch outputs are under the session scratchpad and are not committed.

Rules read: AGENTS.md at the working tree. Branch ref file `.git/refs/heads/claude/padua-effective-cubature-20261112` = `03d2b8bf6be5baafd20b1d40b018f811c408d5fb`. The working tree was being edited while I checked: `lp-cap.md` L53 changed from "137" to "109", and record -06 appeared. Line numbers refer to the files as last read. File sha256 prefixes at that point: delsarte-bound `395012340bd6b6b8`, uniform-theorem-a `bde589ba2fdc638f`, lp-cap `107a33655b4962ef`.

## Scope checked

1. `theory/delsarte-bound.md` (d) and its proof (L34–38, L112–116), and whether (a)–(c) use only what (d) supplies.
2. `theory/uniform-theorem-a.md` (ii′), (iv), the Check at L75 and the Fisher-crossover claim at L84.
3. `theory/lp-cap.md` (b) and the exactness-E bullet and consequences (L11, L46, L51–53).
4. `code/pdn_lattice_witness.py`: exhaustiveness, det/index logic, and the reduction to lp-cap (b). I also verified the witnesses with my own separate code.
5. A cross-check against `topics/padua-3d-20261106/theory/r08-lattice-minima.md`, and what D1-01 (`topics/padua-3d-20261106/final-d1/finite-frame.md`) states.

## Mathematical verification

**(d) orbit averaging.** Let θ ∈ [0,π]³ and let G = {±1}³ act on 𝕋³. The orbit-stabiliser theorem gives |Stab| = 8/s at every orbit point. G is abelian, so the stabilisers are in fact equal. So (1/8)Σ_σ δ_{σθ} puts mass (8/s)/8 = 1/s on each distinct point, which matches D1-01's weight w/s. The identity also holds when θ_j ∈ {0, π}, because −π ≡ π mod 2π.

**Chebyshev product.** (1/8)Σ_σ e^{−ik·σθ} = Π_j ½(e^{−ik_jθ_j} + e^{ik_jθ_j}) = Π_j cos(k_jθ_j) = Π_j T_{|k_j|}(cos θ_j). This product has total degree |k|₁. Under the product measure, ∫Π_j T_{a_j} dμ = Π_j ∫T_{a_j} dμ₁, which is 0 unless every a_j = 0. So ν̂(k) = 0 for 0 < |k|₁ ≤ E, and ν̂(0) = Σw_i = 1. Correct.

D1-01 (finite-frame.md L15, L33) states the same lift and argument with the range fixed at |k|₁ ≤ 2n−2 and hypothesis Π_{2n−2}. (d) is the verbatim extension to Π_E, so the claim "for E = 2n−2 this is the D1-01 statement" is accurate.

**(a)–(c) use only what (d) supplies.**
- (a) uses five facts: v_j ≥ 0 (positive weights), Σv_j = 1, ν̂(k) = 0 on 0 < |k|₁ ≤ E, c_k ≤ 0 on |k|₁ ≥ E+1, and M ≤ 8N (s_i ≤ 8).
- (b) needs c_k = φ(k/L) ≤ 0 for |k|₁ ≥ E+1 = 2L ⇔ |k/L|₁ ≥ 2. The periodization and the estimate P(0) ≥ L³∫φ hold for every L > 0, half-integer or not.
- (c) only wraps (b).

So M ≥ ((E+1)/2)³ D(int 2O). At E = 2n−1 this is M ≥ n³D. **Confirmed.**

Sanity check (my own): lattice torus designs also satisfy the hypotheses of (a)–(d), so every merged minimum det (min ℓ₁ ≥ 2n, E = 2n−1) must be ≥ (4/3)n³. This holds for all n = 1…16, with tight cases 38 ≥ 36, 304 ≥ 288 and 1026 ≥ 972.

**(ii′).** n³D/8 = n³(4/3)(1+γ_A)/8 = (1+γ_A)n³/6. Correct.

**(iv) and the one-positive-root argument.**
- 19n³ − 18(n+1)(n+2)(n+3) = n³ − 108n² − 198n − 108. I checked this identity at 350 integers, which is more than enough for a cubic.
- The coefficient signs are + − − −, so there is one sign change. Descartes' rule then gives exactly one positive root, numerically 109.812.
- So the cubic is negative on (0, 109.81) and positive after it. The inequality holds exactly for n ≥ 110.
- Values: 25289000 > 25286688 at n = 110, and 24605551 < 24615360 at n = 109. Both match L75.
- If γ_A ≤ 1/18, then for n ≤ 109 the bound (1+γ_A)n³/6 ≤ binom(n+3,3), so "can never close 4 ≤ n ≤ 109" is correct.

**Fisher crossover.**
- (ii′) vs binom(n+2,3): 19n³ ≤ 18n(n+1)(n+2) ⇔ n² − 54n − 36 ≤ 0 ⇔ n ≤ 54 (root 54.66). It first improves at n = 55. Confirmed.
- The (ii) form is weaker exactly for n ≤ 82. Confirmed.
- The superseded threshold 138 is confirmed, with sides 395140625 > 395115840.

**lp-cap (b) with E.** In (1/M_L)Σ_{t∈G} f(t) = c₀ + Σ_{k∈L∖0} c_k, the only input is c_k ≤ 0 on L∖0. If L avoids 0 < |k|₁ ≤ E, then L∖0 ⊂ {|k|₁ ≥ E+1}, where (d)-admissible f has c_k ≤ 0. Correct.

**Reduction used by record -06.** Take L with min ℓ₁ ≥ 2n and M_L ≤ 8P, where P = binom(n+3,3). Then f(0)/c₀ ≤ M_L ≤ 8P, so f(0)/(8c₀) ≤ P, with equality allowed. Excluding a package needs a bound strictly greater than P, so it cannot exclude one. Such an L also avoids |k|₁ ≤ 2n−2, so it caps the E = 2n−2 LPs too. Plain-LP f are Delsarte-admissible with vacuous sign conditions. **Confirmed.**

**`min_l1_at_most` (L45–55).**
- `inv3` builds the adjugate transpose correctly: C[j][i] = cofactor(i,j)/det.
- For k = Ac, c_i = Σ_j (A⁻¹)_{ij}k_j, so |c_i| ≤ max_j|(A⁻¹)_{ij}|·|k|₁ ≤ max_j|(A⁻¹)_{ij}|·E. The rows of `Ai` are rows of A⁻¹. `floor` is valid because c_i is an integer, and Fractions are exact. The test is exhaustive.
- det/index: A is an integer matrix with columns as the basis, so [ℤ³ : Aℤ³] = |det A|.
- `--extra` row-basis inputs are transposed to columns correctly (L110).
- Sorting by det and taking the first passing candidate is correct. Optimality over the candidates is not needed.

## Findings

**MAJOR-1 (process; transient).** `theory/limitation-torus-lp-finite.md` L17 and L61 still contain `RANGE_PLACEHOLDER` and `CHECKS_PLACEHOLDER`. `evidence/pdn-lattice-witness.json` and `../evidence-manifest.json` (L9, L57) do not exist yet. Meanwhile `LOG.md` L12, `report.md` L103 and `attempts/E1.md` L33 already list -06 as PROVED.
Fix: fill S and Checks from an actual run, commit the evidence file, and only then let the LOG, report and attempts rows say PROVED.

**MINOR-1.** `lp-cap.md` L11 (statement (b)) and L46 (proof) hard-code 2n−2. The exactness-E version exists only as a "Consequences" bullet (L52), and it has no row in the status table. Record -06 L36 depends on that bullet.
Fix: state (b) for general E, avoiding 0 < |k|₁ ≤ E and with c_k ≤ 0 for |k|₁ ≥ E+1. Replace "2n−1" in L46 by "E+1". Add the status row.

**MINOR-2.** `uniform-theorem-a.md` L83 says "the unknown threshold n₀(γ_A) ≥ 110". But n₀ is defined in (iii), L22, as n₀(γ, γ_A), for the different inequality N ≥ (1+γ)·binom(n+2,3) and using the (ii) form.
Fix: name the package threshold separately. For example, n_pkg(γ_A) is the least n beyond which (1+γ_A)n³ > (n+1)(n+2)(n+3). Optionally restate (iii) with (ii′), using n³ in place of (n−½)³.

**MINOR-3.** Title, alias and dependency lines still show only the 2n−2 / (n−½)³ form, while (d) now proves its own lift exactness for every E. These are delsarte-bound.md L1, L3 and L64, and uniform-theorem-a.md L1.
Fix: add "M ≥ n³D (exact on Π_{2n−1})" to the aliases. In L64, note that (d) re-proves the lift exactness for range E and takes only the lift construction and M ≤ 8N from D1-01.

**NOTE-1 (lattice witnesses are capped at 109).** By Betke–Henk (LITERATURE, as used in r08-lattice-minima L44–46), det L ≥ 38n³/27 whenever min ℓ₁ ≥ 2n. And 38n³/27 > 8·binom(n+3,3) holds exactly when 19n³ > 18(n+1)(n+2)(n+3), which is the same cubic: n ≥ 110.
- So lattice witnesses at E = 2n−1 cannot exist for n ≥ 110, and the -06 method is maximal at 4…109.
- My n = 109 run found index 1822682. The bound 8P is 1823360, with margin 678, and 38n³/27 = 1822633.4.
- lp-cap L53 ("margin thin near n = 109") is accurate. -06 L66 should say that the lattice cap cannot settle n ≥ 110 (conditional on that literature), not merely that LP values are unknown.

**NOTE-2.** "Classical bound N ≥ binom(n+2,3)" (uniform L84) is the plain Fisher bound. Sharper odd-degree bounds for centrally symmetric measures (Möller/Mysovskikh type) would move the crossover past 55. I did not check those bounds; the claim as worded (vs binom(n+2,3)) is correct.

**NOTE-3.** D1-01 assumes distinct nodes; (d) does not say so. This is harmless: coincident atoms only add nonnegative off-diagonal terms f(0)v_jv_l in the proof of (a), and M ≤ 8N still holds.

**NOTE-4 (robustness).** `pdn_lattice_witness.py` L142 would raise TypeError if `best` were None. That cannot happen for E ≤ 2n−1, because some integral sB with 3 | s ≥ n is always a candidate (L65–68). The default `--nmax 140` is pointless for E = 2n−1 beyond 109 (NOTE-1).

## What I executed (Python 3.13.18; outputs summarised)

1. `python3 -B code/pdn_lattice_witness.py --nmin 47 --nmax 50 --extra evidence/lp-lattice.json --perturb --out <scratch>/check_pdn.json`. Took 7.4 s. Script sha256 `819558d6…6642514`.
   - Rows (n, 8P, idx E=2n−2, idx E=2n−1): 47 156800 147343 148064; 48 166600 155648 155648; 49 176800 164241 165602; 50 187408 177309 178126.
   - All rows covered.
2. The same command for n = 2…16. The E=2n−1 indices were 14, 38, 144, 196, 304, 635, 774, 1026, 1723, 1976, 2432, 3610, 4030, 4750, 7073, all covered. The E=2n−2 indices equal the M column of `evidence/lp-lattice.json` for every n = 2…16.
3. The same command for n = 108, 109. Took 20 s. n=108: 1772928 (= 108·B) at both E. n=109: 1816021 / 1822682, both ≤ 8P.
4. My own separate checker, `<scratch>/indep.py`, which shares no code with the script.
   - Method: enumerate every k ∈ ℤ³ with |k|₁ ≤ E+6 and test membership by adj(A)k ≡ 0 (mod det A), using numpy int64. Products stay below 10⁸, so there is no overflow. Determinants are recomputed independently.
   - Applied to every witness above (n = 2…16, 47…50, 108, 109; both E). In every case det = reported index, the true min ℓ₁ ≥ E+1, index ≤ 8P, and index ≥ 38((E+1)/2)³/27.
   - True min ℓ₁ values, for example: n=48 → 96 at both E; n=109 → 217 / 218.
5. Randomised cross-test, `<scratch>/rt.py`. On 399 random integer 3×3 matrices (entries in [−9, 9], E ∈ [1, 14]), `min_l1_at_most` agreed with brute force in every case, with 0 mismatches. Negative controls: for every witness, `min_l1_at_most(A, m)` is True and `min_l1_at_most(A, m−1)` is False, where m is the true minimum.
6. Integer arithmetic (an inline `python3 -I -c`): the polynomial identity, the values at 109 and 110, thresholds 110 / 138, crossovers 54 / 82, and the real root 109.812. All match the records.
7. Cross-check with r08 minima (n ≤ 16, min ℓ₁ ≥ 2n). Every E=2n−1 witness is ≥ the merged minimum, and they are equal at n = 3, 6, 9, 12, 15 (38, 304, 1026, 2432, 4750). LOG L66 cites only 9, 12 and 15; 3 and 6 are also equal.

Not executed: `code/pdn_check_ball.py` and `code/evidence_manifest.py`, which appeared during the check. I did not run the full n range or regenerate `evidence/pdn-lattice-witness.json`, which does not exist yet.

## Verdict

Parts (d), (ii′), (iv) and the lp-cap (b) exactness-E remark are **correct**, and the arithmetic reproduces exactly. The witness script's exhaustiveness argument and its det/index logic are **correct**. Witnesses for n = 2…16, 47…50, 108 and 109 were re-verified by an independent method and are consistent with the merged r08 minima.

No BLOCKING findings. MAJOR-1 must be closed before -06 can be called PROVED in LOG/report: the record has placeholders and its evidence is missing. MINOR-1 to MINOR-3 are wording and structure fixes.

## Orchestrator dispositions (2026-11-12)

- **MAJOR-1: fixed.** The full witness run finished; S was filled in from `evidence/pdn-lattice-witness.json`, written by `code/pdn_check_ball.py` from the full search output. Record -06's Checks section records the commands and outputs, and `evidence-manifest.json` was generated and verified. All of this was committed in the outputs commit, before -06 is relied on as PROVED in the handoff.
- **MINOR-1: fixed.** lp-cap now states (b′) for general E, with a status row and a proof line. Record -06 cites (b′).
- **MINOR-2: fixed.** The package threshold is renamed n_P(γ_A) in uniform-theorem-a Scope and is distinguished from n₀(γ, γ_A).
- **MINOR-3: fixed.** The titles and aliases of -02/-03 now show both exactness forms, and the -02 dependency line points to (d).
- **NOTE-1: adopted** in -06 Open items and the lp-cap Consequences: no witness can exist for n ≥ 110 (packing bound, LITERATURE).
- **NOTE-2: recorded, not pursued.** The crossover is stated against binom(n+2,3) only.
- **NOTE-3, NOTE-4: no change.** The crash path is unreachable for E = 2n−1, since the sB candidates always satisfy it. `--nmax 140` is kept so that the run also shows the failures for n ≥ 110.
- LOG and -06 now cite equality with the r08 minima at n = 3, 6, 9, 12, 15.
