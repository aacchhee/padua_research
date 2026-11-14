# Independent check E1: Delsarte bound, uniform Theorem A, cap

Checker: Claude subagent, Opus 5.5 (`claude-opus-5-5`), xhigh effort. I am an independent mathematical checker and did not write the records under review. This check supplements the Codex audit and does not replace it. I changed no Git state and edited none of the reviewed files. This file is the only one I wrote in the repository.

- Branch: `claude/padua-effective-cubature-20261112`.
- Assigned commit: `689354dda49704ff90836eea957cd0c3187208c4`.
- While I was reading, the orchestrator moved HEAD to `6680efe456ce0587cf52eeb286a404312aa3e50c`. `git diff --stat 689354d 6680efe` does not touch the reviewed theory files, the cap code or evidence, `literature-effective.md`, D1-01 or `agents/`. The SHA-256 of each reviewed theory file is the same at both commits: `delsarte-bound.md` b9583b2c…, `uniform-theorem-a.md` 3150edc7…, `lp-cap.md` 685faf93…, `explicit-gamma-target.md` a41bc895…. So the line numbers below hold at both commits. The working tree also has an uncommitted change to `code/lp_torus.py`, which is not mine and not reviewed.
- Rules read: `AGENTS.md`, `agents/WORKFLOW.md` (in particular "Durable records and status" and "Computation and evidence"), `agents/claude/CLAUDE_ROLES.md`.
- Scope: mathematics, literature transcription, the computer-assisted step and status labels. Novelty and the gate (`novelty-gate-E1.md`) are outside the task, so the full read of `state/IDEAS.md` was omitted.

Files under review, all in `theory/`:
- `delsarte-bound.md` (-02);
- `uniform-theorem-a.md` (-03);
- `lp-cap.md` (-04);
- `explicit-gamma-target.md` (-05, OPEN; light check only).

Supporting files read: `code/cap_critical_lattice.py`, `evidence/cap-critical-lattice.json`, `literature-effective.md`, `plan.md` §2–3, `LOG.md`, `results/padua-effective-cubature-20261112.md`, `topics/padua-3d-20261106/final-d1/finite-frame.md` (D1-01), `…/spectral-obstruction.md` (D1-04), `…/sources.md` L5–17.

## Summary

| Severity | Count | Items |
|---|---|---|
| BLOCKING | 0 | — |
| MAJOR | 1 | M1: the finite-LP limitation for 4 ≤ n ≤ 137 is asserted as proved but is not proved |
| MINOR | 7 | m1–m7 |
| NOTE | 8 | n1–n8 |

Every proof step of -02 (a)–(c), the cap -04 (a) and the lattice-rule cap -04 (b) is correct. I reconstructed each one independently. The KLM transcriptions are accurate. The lattice facts and the threshold 138 reproduce under both the committed script and my own separate method.

## 1. Proof reconstruction

### -02 (a): finite Delsarte inequality. Correct.

- D1-01 (`finite-frame.md` L15) gives lifted exactness for every character e^{ik·t} with |k|₁ ≤ 2n−2. This needs only Π_{2n−2} exactness and closed-cube nodes, and it gives M ≤ 8N and Σv_j = 1. Since the set {|k|₁ ≤ 2n−2} is symmetric under k ↦ −k, the sign convention ν̂(k) = Σ v_j e^{−ik·t_j} (`delsarte-bound.md` L39) does not matter.
- The identity Σ_{j,l} v_j v_l f(t_j − t_l) = Σ_k c_k |ν̂(k)|² holds because v_j is real, so Σ_j v_j e^{ik·t_j} is the conjugate of ν̂(k).
- The sign ranges are complementary integer ranges with no gap. ν̂ vanishes for 0 < |k|₁ ≤ 2n−2, and c_k ≤ 0 is required exactly for |k|₁ ≥ 2n−1. Coefficients with 0 < |k|₁ ≤ 2n−2 may have any sign. Hence the quadratic form is at most c₀.
- Dropping the off-diagonal terms needs v ≥ 0 and f ≥ 0. Then Cauchy–Schwarz gives 1 ≤ MΣv_j², and so M ≥ f(0)/c₀. The trivial case f(0) ≤ 0 is handled.

### -02 (b): periodization and transference. Correct.

- **Choice of L.** L = n − 1/2 is the largest L with 2L ≤ 2n−1. Then |k|₁ ≥ 2n−1 holds exactly when |k/L|₁ ≥ 2, so c_k = φ(k/L) ≤ 0 on the required range.
- **φ̂ ∈ L¹ and ∫φ̂ = φ(0).** The multiplication formula ∫φ̂G_ε = ∫φĜ_ε holds by Fubini, since φ ∈ L¹ and G_ε ∈ L¹. In ℝ³, Ĝ_ε(ξ) = ε^{−3/2}e^{−π|ξ|²/ε} is an approximate identity, and φ is bounded and continuous, so the integral tends to φ(0). Since G_ε ↑ 1 as ε ↓ 0 and φ̂ ≥ 0, monotone convergence gives ∫φ̂ = φ(0). Inversion then holds everywhere because φ and the inverse transform of φ̂ are both continuous.
- **Evenness.** φ is real and φ̂ is real, so φ is even. The record uses this in the last step of the coefficient computation (L84).
- **Fourier coefficients of Q.** Tonelli applies because φ̂ ≥ 0 is integrable. ∫_{[0,1)³} Q(s)e^{−2πik·s} ds = L³∫_{ℝ³} φ̂(Ly)e^{−2πik·y} dy. With x = Ly and dy = L^{−3}dx this is ∫φ̂(x)e^{−2πi(k/L)·x} dx = φ(−k/L) = φ(k/L). The L³ prefactor exactly cancels the Jacobian, so the scaling under ξ ↦ k/L is right.
- **P = Q a.e. implies P ≥ 0.** The coefficients agree, Q ∈ L¹(𝕋³), and coefficients determine an L¹ function uniquely. P is continuous and Q ≥ 0, so P ≥ 0 everywhere.
- **P(0) ≥ L³φ̂(0).** P(s) = Q(s) ≥ L³φ̂(Ls) a.e. Both P and s ↦ L³φ̂(Ls) are continuous, so the inequality holds everywhere, in particular at s = 0. Also φ̂(0) = ∫φ.
- **Final step.** Applying (a) to f(t) = P(t/2π), with c₀ = φ(0) = 1, finishes the proof.

### -02 (c): approximation by ψ_R = φ·g(·/R). Correct.

- g(0) = (h∗h̃)(0)/‖h‖₂² = 1 and ĝ = |ĥ|²/‖h‖₂² ≥ 0, using h real. ∫ĝ = g(0) follows by the argument of (b).
- ψ̂_R = φ̂ ∗ R³ĝ(R·). To justify this, write g(ξ/R) = ∫R³ĝ(Ry)e^{2πiξ·y}dy and apply Fubini with φ ∈ L¹ and ĝ ∈ L¹.
- ψ_R ≤ 0 wherever φ ≤ 0, because g ≥ 0. ψ_R is continuous with compact support and ψ_R(0) = 1.
- ∫ψ_R = ψ̂_R(0) → φ̂(0) = ∫φ, because φ̂ is bounded and continuous and R³ĝ(R·) is an approximate identity.

**Class comparison with KLM (task 2).** -02 (c) L30 uses the same class as KLM. KLM §5.2 p. 15 calls f "Delsarte admissible if f is a continuous real-valued function in L¹(ℝ^d) satisfying the conditions f(0) = 1, f(t) ⩽ 0 for t ∈ U^∁, and f̂ is a nonnegative function", and Definition 5.1 takes the supremum of ∫f. KLM imposes no compact support, no φ̂ ∈ L¹ hypothesis (it is derived, as in -02 (b)) and no smoothness. ℝ³ ∖ int(2O) = {|ξ|₁ ≥ 2} matches the (b) sign condition. int(2O) satisfies KLM (5.1)–(5.3). I found no mismatch.

### -04 (a): cap via the lattice B. Correct.

- **Change of variables.** Put ξ = Bη. Then dη = |det B|^{−1}dξ and η·y = ξ·B^{−T}y. So the transform of φ_B is |det B|^{−1}φ̂(B^{−T}y) ≥ 0, and its value at 0 is |det B|^{−1}∫φ.
- **Periodization with L = 1.** This step uses only continuity, compact support, evenness and transform ≥ 0, not the sign condition. It gives P ≥ 0 and P(0) ≥ |det B|^{−1}∫φ.
- **Upper bound on P(0).** P(0) = Σ_k φ(Bk) = 1 + Σ_{λ∈Λ∖0} φ(λ) ≤ 1, because every λ ≠ 0 has |λ|₁ ≥ 2 and so lies outside U.
- **Conclusion.** Hence ∫φ ≤ |det B| = 38/27. The ψ_R approximation of -02 (c) removes compact support.
- **T ≤ D.** This is right. KLM §4.2 p. 7 defines a Turán admissible function as "a bounded continuous real-valued function vanishing on U^∁, such that f̂ is nonnegative and f(0) = 1". Such a function is L¹ and so Delsarte admissible.

### -04 (b): finite lattice-rule cap. Correct.

- |G| = [L^⊥ : ℤ³] = [ℤ³ : L].
- The average over G of e^{ik·t} is 1_{k∈L}, since (L^⊥)^⊥ = L.
- c_k ≤ 0 on L ∖ 0, because every such k has |k|₁ ≥ 2n−1.
- f ≥ 0 and 0 ∈ G give f(0)/M_L ≤ c₀.

### Fisher consistency (-02 L107). Correct.

- m_n = |{k ∈ ℤ³ : |k|₁ ≤ n−1}| = (2n−1)(2n²−2n+3)/3 = (4n³−6n²+8n−3)/3.
- (4/3)(n−1/2)³ = (4/3)n³ − 2n² + n − 1/6 = m_n − (5/3)n + 5/6.
- I checked this exactly for n = 1…40, which determines the cubic identity, and checked the lattice count by brute force for n ≤ 12.
- φ₀ = 1_O∗1_O/|O| is (b)-admissible: it vanishes on {|ξ|₁ ≥ 2}, because O ∩ (O+ξ) ⊂ ∂O has measure 0 when |ξ|₁ = 2. Its integral is 4/3.

## 2. KLM application and transcription

I checked the source myself, from arXiv:2510.10172v1 (29 pp.). The PDF has sha256 eb034df3…; it was extracted with pypdf and kept in scratch, not committed.

| Item | Source text | Record | Verdict |
|---|---|---|---|
| Def. 5.1 (§5.2, pp. 15–16) | quoted above | `literature-effective.md` L8; -02 L30 | accurate |
| (6.2) (§6.1, p. 23) | "D(∆(A)) ⩾ m(A)", for A bounded measurable of positive measure, via m(A)^{−1}1_A∗1_{−A} | L12; -03 L46 | accurate |
| §6.5 (p. 25) | "if the convex body A is origin-symmetric, then ∆(A) is equal to the interior of the set 2A"; "a convex body A ⊂ ℝ^d is a spectral set if and only if it can tile the space by translations" | L11, L18; -03 L46–47 | accurate, verbatim |
| Thm 6.4 (p. 25) | "Let A ⊂ ℝ^d be a convex body. The equality D(∆(A)) = m(A) holds if and only if A tiles by translations." | L10; -03 L46 | verbatim; KLM defines a convex body as "a compact convex set with nonempty interior" |
| Proof of 6.4 (p. 26) | uses Thm 5.6(ii), (5.9) = Thm 5.4, Thm 5.8(ii), Lemma 5.7, Lemma 3.1, [KLM23, Thm 1.4] | L19 lists 5.4, 5.6, 5.8, KLM23; -03 L46 omits 5.8 | see n4 |

- **Δ(O) = int(2O).** This is correct, and it can be proved locally (see n4). If |t|₁ < 2, then t/2 lies in int O ∩ int(O+t), so the intersection has positive measure. If |t|₁ ≥ 2 and x ∈ O ∩ (O+t), the triangle inequality forces |x|₁ = 1, so the intersection lies in ∂O and has measure zero.
- **Applying Thm 6.4 with A = O.** O is compact, convex and has nonempty interior, so the theorem applies.
- **"O does not tile."** The route is sound, and labelling it LITERATURE is correct. GL Thm 1.1, as already applied in D1-04 L36, shows O is not spectral. "Tile ⇒ spectral" for convex bodies then gives non-tiling by contraposition. See m3 for a cleaner route that is already partly recorded.

## 3. Computations (commands actually run, Python 3.13.18)

Scratch directory: `/tmp/claude-0/-workspace-padua-research/e2057052-bb3b-5345-abf7-4ff7dc19c8ac/scratchpad/indep-e1/`. The source PDF is in `src/`, my scripts are in `scripts/`, and every script was run with `-I`.

**(1) Rerun of the committed script, from the repository root.**

`python3 -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py`, and again with the output path `…/indep-e1/rerun.json`. Code sha256 0516daa4af249dfe23f0861f3c0bc9eaba12b09330bd4d9dd9458b519b9a2f44 matches the evidence. The output gave det −38/27, enumeration radius 3, min nonzero ℓ₁ 2, 14 minimal vectors and verdict PASS. A field-by-field diff against `evidence/cap-critical-lattice.json` differs only in the `command` field (the output path).

I also checked the docstring reduction. |x|_∞ ≤ |x|₁ < 2 gives |c_i| < 2·max_i‖row_i(B^{−1})‖₁ = 3. Every vector with |x|₁ = 2 has |c_i| ≤ 3, so the count of 14 is complete.

**(2) My own separate method: `scripts/indep_lattice.py`** (sha256 1930652e…).

- The determinant is computed by a Leibniz permutation sum on the integer matrix A = 3B. This gives det A = −38, so det B = −38/27.
- Since Λ ⊂ (1/3)ℤ³, the script enumerates every y = 3x ∈ ℤ³ with 0 < |y|₁ ≤ 6. For each it tests membership by solving Ac = y with integer Cramer's rule: divisibility of each cofactor determinant by −38, followed by back-substitution.

`cd …/indep-e1/scripts && python3 -I indep_lattice.py` printed:

```
det(3B) = -38  => det B = -38 / 27 ; equals -38/27: True
nonzero lattice vectors with |x|_1 < 2: 0
lattice vectors with |x|_1 = 2: 14
minimal vectors (3x): [(-4,-1,1), (-3,1,-2), (-2,-3,-1), (-2,2,2), (-1,-2,3), (-1,-1,-4), (-1,4,-1), (1,-4,1), (1,1,4), (1,2,-3), (2,-2,-2), (2,3,1), (3,-1,2), (4,1,-1)]
```

**(3) Arithmetic: `scripts/indep_arith.py`** (sha256 5fa71cba…).

`python3 -I indep_arith.py` printed:

```
Fisher identity and m_n formula, n=1..40 (lattice count n<=12): True
d(m) = 8m^3 - 1092m^2 - 1470m - 883 (Descartes: exactly one positive root)
m in 1..137 with d(m)>0: [] ; d(137) = -127197 ; d(138) = 24785
sides at 138: 395140625 395115840
positive root ~ 137.83888742972138
d'(138) > 0: True
least n with (19/18)(2n-1)^3/48 > binom(n+2,3): 83 ; check monotone after: True
n=3 calibration (5/2)^3*(38/27)/8 = 2.7488425925925926
```

The script then prints, for n = 130, 135, 136, 137, 138, the relative margin of 8·binom(n+3,3) over (38/27)(n−1/2)³: 3.2e-3, 1.1e-3, 7.3e-4, 3.3e-4 and −6.3e-5.

Here d(m) = 19(2m−1)³ − 144(m+1)(m+2)(m+3). The coefficient expansion was asserted for m ∈ [−50, 300).

**(4) The record's own command** (-03 L69) printed `138`.

**Threshold verdict (task 4).** n₁ = 138 is correct. d has exactly one positive root, at about 137.84, so the inequality fails at every m = 1…137, not only at 137, and holds for every m ≥ 138.

The logic is in the right direction, provided "only" is read as "only if". Because γ_A ≤ 1/18, bound (ii) can exceed binom(n+3,3) only when n ≥ 138. Concretely:
- For n ≤ 137, it is proved that (ii) gives no exclusion, whatever the value of γ_A. Nothing is proved about whether packages exist at those n.
- For n ≥ 138, exclusion is proved only from the unknown threshold n₀(γ_A) ≥ 138. It equals 138 only if γ_A = 1/18.

-03 L22 and L75 state this correctly.

## 4. Findings

### MAJOR

**M1. `lp-cap.md` L46: the finite-LP limitation for 4 ≤ n ≤ 137 is not proved.** The same overstatement appears in `results/padua-effective-cubature-20261112.md` L17 and `LOG.md` L44.

L46 says that any route through 8N ≥ M and "an LP of these two kinds therefore leaves 4 ≤ n ≤ 137 undecided", and calls this "a proved limitation of these two relaxations". The "therefore" does not follow.

- The cap D ≤ 38/27 constrains only the continuous, uniform bound L³D of -02 (c) and -03 (ii).
- At a fixed n, the finite torus LP value R^Del_{n,K} can exceed L³D. It is bounded above only by M_lat(n), from part (b).
- M_lat(n) is known only to satisfy M_lat(n) ≥ (38/27)(n−1/2)³, by the packing bound. An integer lattice generally exceeds that bound by lower-order terms.
- To show the finite LP cannot exclude a package at n, one needs M_lat(n) ≤ 8·binom(n+3,3), or another dual-feasible torus measure of that size, at every 4 ≤ n ≤ 137.
- Near the top of the range the margin is thin: the relative margin is 3.3e-4 at n = 137 and 1.1e-3 at n = 135.
- The obvious integral scaling sΛ with s ∈ 3ℤ needs s = n+2 when n ≡ 1 (mod 3). Its index (38/27)(n+2)³ exceeds 8·binom(n+3,3) for every n, so no construction in the record covers those n.
- `evidence/lp-lattice.json`, cited at L45, does not exist at 689354d or at 6680efe.
- `plan.md` L33 itself says: "The exact finite range needs explicit lattices at each n and goes in a PD-N record."

**Fix:** restrict L46 to the uniform/continuous bound, which is proved: "(ii) and any bound of the form M ≥ L³·∫φ excludes no n ≤ 137". Move the finite-LP range claim to a separate MEASURED or OPEN item, or to a scoped PD-N, backed by an explicit lattice at each n with exact checks. Correct the results file and LOG to match.

### MINOR

**m1. `lp-cap.md` L45: the asymptotic cap (19/18 + o(1))·m_n is stated without proof, and its evidence file is absent.**

The claim is true. Since 3B is integral, s = 3⌈(2n−1)/6⌉ gives sΛ ⊂ ℤ³ with minimum 2s ≥ 2n−1 and s ≤ n+2. Its index is (38/27)s³ ≤ (19/18)(4/3)(n+2)³ = (19/18 + o(1))m_n. Add this two-line proof.

**m2. `lp-cap.md` L24 ("Records -02 and -03 (definitions only)") understates the dependencies.**

- The proof of (a) reuses the periodization of -02 (b) and the approximation of -02 (c).
- R^Del_{n,K}, R_n, K and M_lat(n) at L11 are not defined in the record. They appear only in `plan.md` §2.
- T(U) at L9 is not defined in any record. AGENTS.md requires definitions to be stated in the repository. Restate KLM's Turán admissibility, quoted in §1 above.

**m3. `uniform-theorem-a.md` L47: the non-tiling route.**

The logic is sound and the LITERATURE label is correct. But the "tile ⇒ spectral" direction for convex bodies is classical: Venkov–McMullen (convex tiles are lattice tiles) combined with Fuglede 1974 (lattice tiles are spectral). So the spectral detour implicitly contains Venkov–McMullen, which by itself already excludes O because its facets are triangles.

The record says Venkov–McMullen was "Not read". That is inconsistent with `final-d1/sources.md` L17, which records that the introduction of LM22 (LIT-660), which was read, "also states the Venkov–McMullen facet condition". I verified that the KLM §6.5 quotation used in the record is verbatim.

Suggestion: name Venkov–McMullen, as stated in the LIT-660 introduction, as the primary non-tiling citation, and keep the spectral route as corroboration.

**m4. `uniform-theorem-a.md` L39 lists (i) as a dependency of (ii). It is not one.**

N ≥ (1+γ_A)(2n−1)³/48 holds for the defined γ_A = (3/4)D − 1 whatever its sign. So (ii) is entirely local: -02 (c) and the definition of γ_A. Only (iii), and the positivity claim in the title, need (i).

**m5. `uniform-theorem-a.md` L1, L18 and L62: the scope of "uniform form" and "explicit n₀".**

- Even in the best case γ_A = 1/18, bound (ii) is weaker than the classical bound N ≥ binom(n+2,3) (D1-01) for every n ≤ 82. The first improvement is at n = 83; see computation (3).
- So (ii) is non-trivial only for n ≥ 83.
- n₀(γ, γ_A) is "explicit" only as a function of the unknown γ_A, and n₀ ≥ 83 always.
- The statements are true, but this should be in Scope, so that "for every n ≥ 1" is not read as an improvement for every n.

**m6. `delsarte-bound.md` L109 and `explicit-gamma-target.md` L18 cite `../evidence/lp-torus.json`, which is not in Git at either commit.**

Neither record uses it as a premise. Mark it as pending under Runs needed, or remove the citation until the file exists.

**m7. `literature-effective.md` L22 ("asymptotes to D(2O)") and `delsarte-bound.md` L129 ("turns the asymptotic problem … into Delsarte's D(2O)") claim more than is proved.**

Only the lower bound R^Del ≥ L³D is proved. The matching upper bound, R^Del/L³ → D, would follow from the conversion sketched in -05 L10, with a loss factor that tends to 1, but that sketch sits in an OPEN record. Reword as "is bounded below by", or label the asymptotic equality CONDITIONAL on the -05 conversion.

### NOTE

**n1. `delsarte-bound.md` L14: confusing wording.** With real c_k, the condition f ≥ 0 already forces c_{−k} = c_k. Suggested wording: "c_k real; f real-valued (hence c_{−k} = c_k)".

**n2. `uniform-theorem-a.md` L69: the argument for "all m ≥ 138" is muddled.** "The window m < n+2000 lies beyond its last real root" does not say what is needed. The correct argument: by Descartes' rule, d(m) = 8m³ − 1092m² − 1470m − 883 has exactly one positive root, about 137.84. The window check is then unnecessary. This also gives failure at every m ≤ 137.

**n3. `uniform-theorem-a.md` L70: the chain "N ≥ (1+γ_A)·125/48 ≤ 2.75" mixes ≥ and ≤.** Write instead "the bound (1+γ_A)·125/48 is at most 2.75". The value 2.7488 is correct.

**n4. `uniform-theorem-a.md` L46: two inputs can be proved locally.**
- Δ(O) = int(2O) has a two-line proof (§2 above).
- (6.2) for A = O is already proved locally in -02 L107.
- Moving both to local proofs leaves only Thm 6.4 and non-tiling as LITERATURE.
- The list of KLM proof ingredients at L46 omits Thm 5.8(ii), Lemma 5.7 and Lemma 3.1. `literature-effective.md` L19 includes 5.8.

**n5. `literature-effective.md` L15 paraphrase of KLM p. 2.** The source reads: tiles and balls are Turán domains "(and of course their linear images are too)"; products of Turán domains are Turán; and "we know the quantity T(U) for no other origin-symmetric convex body". The paraphrase omits linear images and "origin-symmetric". -03 L78 has the same omission. The citation split at L16 ([AB02, KR03] for tiles, [Gor01, KR03, Gab24] for balls) is not how p. 2 groups the citations: p. 2 cites [Gor01, AB02, KR03] jointly, and p. 27 cites [Gor01], [KR03], [Gab24] for the ball.

**n6. `explicit-gamma-target.md` L10 (OPEN; light check).**
- The construction itself is sound:
  - B(k) = |P ∩ (P+k)| = 0 for k ∈ ℤ³ ∖ 0, for any fundamental domain P, so ψ(0) = c₀;
  - ∫ψ = Σc_k = f(0);
  - ψ̂ = |1̂_P|² times a trigonometric polynomial that is ≥ 0;
  - ψ ≤ 0 outside an ℓ₁ ball enlarged by r.
- The Brunn–Minkowski value r ≥ 6^{1/3} = 2(3/4)^{1/3} ≈ 1.817 holds when r = max_{z∈P−P}|z|₁, the ℓ₁-diameter of P. Read literally as "ℓ₁-diameter of P − P", r would be twice that.
- ρ^Del_L and the level convention are not defined in the record, so the factor ((2L+1)/(2L+r))³ cannot be checked. With -02's convention (L = n−1/2, c_k ≤ 0 for |k|₁ ≥ 2L) and ρ normalized by (4/3)L³, I get (2L/(2L+r))³.
- "Equivalent" should read "sufficient": the route goes in one direction only.
- L24 is correct.

**n7. `lp-cap.md` L51 writes `python -B`.** The environment provides `python3`. My rerun with `python3 -B` reproduces the evidence.

**n8. Status labels (task 5).**
- **-02 PROVED: justified.** The proof is complete, elementary and checkable, and it uses only D1-01 (PROVED) and KLM's definition.
- **-03 "PROVED with explicit LITERATURE dependency": justified.** It follows the same convention as D1-04 (PD-T557). The dependencies on Thm 6.4 and non-tiling are explicit, and the proof is not inherited. After m4, (ii) can be labelled fully local.
- **-03's relation to D1-04 (L57–64) is accurate.**
  - -03 implies D1-04's statement: take γ = γ_A/2 and n₀ from (iii).
  - -03 uses only D1-01, not D1-02/03, and its exactness hypothesis is weaker (2n−2).
  - The trade-off is a heavier import. D1-04 needs GL1.1 only, and D1-04 L32 explicitly avoids any "non-tiling slogan". -03 imports KLM Thm 6.4, which rests on KLM's duality machinery and [KLM23], plus non-tiling.
  - L64 calls the literature overlap "LIT-659/660". In fact LIT-660 is used only through KLM's report.
- **-04 PROVED.** Part (a) is a computer-assisted finite check. WORKFLOW ("Computation and evidence") requires a proved reduction, exact arithmetic, committed code and evidence, and an independent rerun.
  - The reduction is proved in the docstring and verified above.
  - The arithmetic is exact (Fractions).
  - The code and evidence are committed.
  - The independent rerun is supplied by §3 (1) and (2) of this file.
  - The main statements (a) and (b) are therefore justified as PROVED. The "Consequences recorded" bullet at L46 is not (M1), and must be rescoped or split before the record's claims are reported as proved.

## 5. Remaining uncertainty

- I did not check KLM's duality proofs (§§4.5–5.7), [KLM23], GL or LM22. They remain LITERATURE.
- I did not compute M_lat(n) for any n. M1 records that the claim is unproved, not that it is false.
- I did not read Kuperberg (LIT-663) for the -02 L114 quotation.
- I did not run the uncommitted LP code (`lp_torus.py`, `lp_lattice.py`, `lp_cube.py`).
