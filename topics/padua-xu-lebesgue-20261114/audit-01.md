# Audit 01 — padua-xu-lebesgue-20261114 (session 1: X1 resolved; X2 vertex theory and partial argmax)

## 0. Identity, inputs, deviation

- **Auditor:** Claude Opus 5.5 (`claude-opus-5-5`), effort **xhigh**, role: independent auditor (CLAUDE_ROLES "Independent audit"). Model and effort were fixed by handoff 02 and AC's ruling (LOG, 2026-11-14 setup entry): adversarial audit with novelty content.
- **Independence.** I did not develop this work and had no access to the development conversation. I worked only from the repository, the staged fulltexts and web sources.
- **Disclosed deviation** (canonical record: LOG, entry "2026-11-14 15:30 — handoff 02 started"). AC chose to run this audit as a subagent spawned by the developer-orchestrator thread. I ran no git write command. I edited no existing file. The orchestrator commits my outputs unchanged.
- **Audited SHA:** `971beb79b8edb93835b20d1b9148e93d4ba3aba4`.
- **Head inspected:** `46dcd9227aa24fa88ab657b4e15318062219d73f`.
  - `git diff 971beb7 46dcd92` touches only `LOG.md`, `handoffs/01-work.md` (status line) and the new `handoffs/02-audit.md`.
  - No claim, code or evidence differs between the two.
- **Rules read at `46dcd92`:**
  - AGENTS.md (SHA-256 `c44a76f1…`);
  - agents/WORKFLOW.md (`65e6b726…`);
  - agents/claude/CLAUDE_ROLES.md (`35c6146f…`);
  - templates/HANDOFF.md, templates/THEORY.md (headings).
  - The rules were last changed in `be9a831` (contained in main's `76ba421`).
- **Base:** `origin/main` = `99a9b1d161e41a80c4fd425b63022c681fbe8779` (checked with `git ls-remote`), equal to the recorded base.
- **Environment:** Python 3.13.18, python-flint 0.9.0 (Arb), mpmath 1.4.1, numpy 2.5.3, scipy 1.18.1; 2 cores.
- **Where reruns ran.** All developer scripts were run on a byte-identical copy of the topic directory (`/tmp/audit/tc`), so that no default output path could overwrite committed evidence. My own scripts ran from `code/audit/`.

## 1. Files read and novelty scope

Novelty is in scope (X1 priority wording; X2 negative answers; new mechanisms in round X2-3).

- **Rules and protocol:** AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, templates/HANDOFF.md, templates/THEORY.md.
- **Topic, read in full:** BRIEF.md, LOG.md, rounds.md, gates.md (including the pre-registration history in `git diff e153416 af65855 9fbfa6d`: additions only), literature-xu-mp.md, novelty-gate-X1.md, novelty-gate-X2.md, report.md, independent-checks-X1.md, independent-checks-X2.md, results/padua-xu-lebesgue-20261114.md, handoffs/01-work.md and 02-audit.md.
- **Every `theory/` record, read in full and checked line by line:** X1-01…X1-08, X2-21…X2-28, X2-31…X2-34, X2-N29, X2-N30, X2-N35.
- **Attempts:** attempts/X2-round3.md was searched for novelty and gate entries; X1-round2.md and X2-round2.md were consulted where records cite them.
- **Literature notes:**
  - lit-notes/X1-novelty-exact-constant.md: §§1–6 and the full-text addendum, structure and verdicts;
  - lit-notes/X1-sources.md and X2-sources.md: §0–1b, §4, §6, §8 and the query logs.
- **Code read in full:** code/mp/research/x2r3_first_variation_arb.py. Read in part: x2_corner_arb.py, the g0/cmp checkers' interfaces, x2r3_checks.py (shift section). Evidence: all 15 committed JSON files (provenance fields), with mp-x2r3-first-variation.json and mp-x2r3_checks_b.json in full.
- **Merged dependencies:**
  - PROOF_STATUS rows PD-T159, PD-T269, PD-T270, PD-T271 (all PROVED, Claude audit-01 accepted);
  - PD-T159 record statement and eqs. (4)–(5);
  - PD-T269 record eqs. (1), (2), (9);
  - PD-T270 record eq. (2).
- **`state/IDEAS.md` (SHA-256 `80a13381…`, 1296 lines).**
  - Read in full: lines 1–645 (all seed, contextual and obstruction tables; MZ entries; bivariate-Lanczos seed). Also read in full: the Padua argmax sections (PR17, PR19, PR25), the Lebesgue follow-ups, and the PR12 and PR34 dispositions.
  - Read at row level (first 200–420 characters of every row): the bivariate-Lanczos final registration, MZ-2D, drift, Lanczos frontier/nonproduct, NN-MOP and 3D sections. Grep for Xu/Morrow/MP/vertex/symmetrization terms found no further hits in them.
  - Shortlisted and read in full: IDEA-047 (MP survey), IDEA-206 (checkerboard Lebesgue theory), IDEA-288/PD-T159 (same-mesh square) and IDEA-316 with its original candidate text (`topics/padua-argmax-alln-20261101/ideas.md`, FINAL_CANDIDATES.md). Also read in full: PD-N079 (`gated-codex-N01-majorant-coset-obstruction.md`) and IDEA-303 and IDEA-326–328 (rows).
- **Primary sources (pdftotext of the staged PDFs; page images rendered where symbols were lost):**
  - BCDMV, Computing 76 (2006): §2 pp. 312–313 (even n, nodes (2)), Conjecture (17) on p. 319 (page image rendered: "Λ^Xu_n ≲ (2/π log(n+1))², n → ∞"; "Moreover, the maximum is attained at the four vertices"), Table 7 on p. 323, closing remark on p. 324.
  - BdMV, JAT 141 (2006) 134–141: §§2–3 and the proof of Thm 1 (Lemmas 1–3).
  - BBDM, Constr. Approx. 63 (2026): node definition on p. 32; Remark 1 on p. 34; Lemma 1 on p. 45. §7 on p. 63, verbatim: "Numerically, the Lebesgue constant is attained at each corner of the square Q and the computed values are (n+1)(n+2)/2". §7.1 on p. 64: the two open problems, citing the x-symmetry as "Lemma 15".
  - Xu, JAT 87 (1996): title page only.
- **Not accessible to me:** Beberok, JAT 311 (2025) 106191 (doi.org fetch blocked; no open copy found); Xu's CUP 2025 book body; Szili–Vértesi 2009.
- **My own searches (2026-11-14, WebSearch/WebFetch):**
  - "Xu points" Lebesgue constant exact / vertices proof;
  - Xu interpolation Lebesgue constant = square of the univariate Chebyshev constant;
  - Xu *Minimal Cubature Rules* contents;
  - 2025–2026 arXiv Xu Lebesgue conjecture;
  - Beberok MP lower bound (two queries);
  - a WebFetch of arXiv 2605.23299 (it mentions MP points, but no corner values and no Xu points).

  No source stating Λ^Xu_n = L_n², the maximizer set, c* or the MP vertex values was found.

## 2. Reruns (actually executed; outputs in /tmp/audit/out, summaries committed)

| # | Command (from the topic copy) | Wall | Result |
|---|---|---|---|
| R1 | `python3 code/xu/g0_check.py --nmax 12 --out /tmp/audit/out/xu-g0.json` | 2 min 27 s | `G0_PASS True`; identical to `evidence/xu-g0.json` apart from the `command` field and timings |
| R2 | `cd code/mp && python3 g0_check.py --out /tmp/audit/out/mp-g0.json` | 91 s | identical to `evidence/mp-g0.json` (same exceptions); published MP/EMP values at n = 34…76 reproduced at the vertex |
| R3 | `cd code/mp && python3 cmp_check.py --out /tmp/audit/out/mp-cmp-check.json` | 58 s | `ALL_rows_consistent True`; identical to `evidence/mp-cmp-check.json` (same exceptions) |
| R4 | `cd code/mp/research && python3 x2_corner_arb.py --nmax 60 --out /tmp/a/arb.json` | 0.4 s | identical to `evidence/mp-x2-corner-arb.json` apart from `command`. c* ∈ [0.51695365336638144…, 0.51695365336768164…]; all seven flags true for every even n ≤ 60; f(42) < 0 < f(44), g(18) < 0 < g(20) |
| R5 | `python3 code/mp/research/x2r3_first_variation_arb.py --band --nmin 2 --nmax 3000 --out /tmp/audit/out/fv_band_2_3000.json` | 99 s | see below |
| R6 | `… --full --nmin 2 --nmax 24` | <1 s | identical to `evidence/mp-fv_full_2_24.json` apart from `wall_seconds` |
| R7 | `python3 -I code/xu/independent/ic_x1_a_vandermonde.py 10 500`, `ic_x1_b_grid.py 16`, `ic_x1_c_1d.py`, `ic_x1_d_enclosure.py`, `ic_x1_e_signs.py` | 17/75/18/114/4 s | all exit 0; output reproduces independent-checks-X1 §2 (0 violations or failures) |
| R8 | `python3 -I code/mp/independent/ic_x2_cstar.py --J 800 --JR 300`, `ic_x2_arb_finite.py --nmax 60 --extra 100,200,400,1000`, `ic_x2_stepB.py`, `ic_x2_vandermonde.py --nmax 20 --dps 60`, `ic_x2_bracket.py` | 5/4/1/245/105 s | all exit 0; acb enclosure c* ∈ [0.51695365336672179537, 0.51695365336697862536]; all flags true; bracket `all_inside` for 248 even n ≤ 5000 (margins 9.28 and 19.11) |

R5 details:
- Flags: `all_signs_certified`, `all_Dx_pos`, `all_Dy_pos`, `all_band_Tx_positive` and `Ty_nonpositive_only_at_(1,2)` are all true; count 1500.
- min D_x/M⁴ = 0.019340359539719576 and min D_y/M⁴ = 0.027351398762243292 (both at n = 2), identical to the evidence.
- Output: SHA-256 `0bed8871…`, 758 427 bytes.
- With the developer's `"wall_seconds": 105.7` substituted for my 99.0, the SHA-256 is `25db45028e782806e5361ec588cecb66297afca301eef2dfbeb1fa34425fc05a`, exactly the pinned hash, so the output is **byte-identical** apart from the timing field. All 25 thinned rows match.

### 2.1 Auditor's separate code path for X2-32 (gate G3) and further independent checks

Scripts (new, mine): `code/audit/audit_x2_fv_sep.py`, `audit_cmp_sep.py`, `audit_x2_misc.py`, `audit_x1_check.py`. SHA-256 values are in `evidence/audit-*.json`.

**Separate path for X2-32.**
- **Method.**
  - Every quantity comes from the **defining kernel sums**: ω U_i(x_p)U_j(y_q) = (8/N) sin w sin v sin(aw) sin(bv) with a = i+1, b = j+1, a+b ≤ M, and U_i'(1) = i(i+1)(i+2)/3.
  - Sines come from exact-rational `sin_pi` tables (no three-term recurrence), in Arb at 192 bits.
  - Nothing uses the closed forms N_x, N_y (X2-31) or A_{p,q} (X2-23).
- **Band mode.**
  - Band membership is decided by the certified sign of (−1)^p ℓ_a(1,1) from the defining sum.
  - Each column is scanned until the first certified positive node, plus one extra node, which was certified positive every time.
  - The two developer facts used only to bound the scan are X2-23 (b) for q' > p' and the monotone column structure.
  - Command: `python3 code/audit/audit_x2_fv_sep.py --mode band --ns <all even n ≤ 200>,300,500,700,1000,1500,2000,2500,2998,3000 --extra 1` (215 s).
  - Result: 109 values of n. All signs certified. D_x > 0 and D_y > 0 everywhere, and min D/M⁴ agree with R5.
  - `audit_cmp_sep.py`: band sizes are equal and the balls of λ_n(1,1), D_x, D_y overlap the developer's for all 109 n ("mismatches 0"). Example at n = 3000: band 4633, D_x = 4157838173448.6706 ± 3e−6, D_y = 4161141459491.4882 ± 4e−6.
- **Full mode (no band representation at all).**
  - D_x = Σ_a sgn ℓ_a(1,1) ∂_xℓ_a(1,1) is summed over all nodes, with every sign certified, and likewise D_y. This also gives λ_n(1,1) directly and λ_n(±1,−1) for n ≤ 30.
  - Range: n ∈ {2, 4, …, 40, 50, 60, 80}.
  - Result: all values agree with R5 ("mismatches 0"), and λ_n(1,−1), λ_n(−1,−1) contain n+1.

This independently confirms the X2-31 (c) band representation for these n.

**Consequences checked on the separate-path values:**
- X2-26: λ_n(1,1) > c*n², with c* taken at its upper end;
- X2-N30: λ_n < d_n for n = 2, 4, and λ_n > d_n for n ≥ 6;
- the X2-25 two-sided bracket.

All three hold for all 109 band-mode n, and in full mode for all n ≤ 80. R_3000 ≈ −17.44.

**X2-N35 in ball arithmetic.** `audit_x2_misc.py xi` computes, from the defining sum for G̃, the ratio Ξ_n(0.9/M, −0.9/M)/Ξ_n(0) (13 s):

| M | ratio | Ξ_n(0) |
|---|---|---|
| 62 | 1.0698576 ± 4e−8 | 1952.5200457 = λ_60(1,1) |
| 102 | 1.0752352 ± 3e−8 | 5323.2728467 = λ_100(1,1) |
| 202 | 1.0796015 ± 5e−8 | |

All three are **certified > 1**. See finding A-m5 for the developer's float value at M = 102.

**X2-33 spot check (`audit_x2_misc.py farfield`, float64, MEASURED).**
- Lemma (d) at 200 random offsets: sum/bound ≤ 0.35 for M ∈ {4, 6, 10, 20, 52, 102}.
- At 300 random points: λ/bound(a) ≤ 0.094 and λ/(stronger bound (b)) ≤ 0.0072 for n ∈ {4, 10, 20, 40}.

**X1 (`audit_x1_check.py`, MEASURED).**
- Method: my own float64 generalized Vandermonde in the product-Chebyshev basis plus E_j, with condition number ≤ 4.9.
- Range: n = 1…24.
- Results:
  - λ_n(v) = L_n² at V* to 6e−14, and λ_n = 1 at node vertices;
  - the grid argmax on θ = kπ/(8n), which contains every complementary point, is exactly V*;
  - the maximum over 4000 random points stays below L_n²;
  - L-BFGS-B local maxima away from the vertices have ratio ≤ 0.9013 (n = 24), and the values for n = 3, 5, 7, … reproduce independent check F1 (0.7757, 0.8002, 0.8243, …);
  - λ_1 ≡ 1.
- The X1-03 middle sum equals L_n² (mpmath, 60 digits) to 5e−60 at n = 50, 7e−59 at n = 101 and 1e−57 at n = 400.

**Committed evidence (all < 16 KiB):**
- `evidence/audit-reruns.json` (SHA-256 `589eb952…`);
- `evidence/audit-x2-separate-path.json` (`838d69b5…`);
- `evidence/audit-x1.json` (`52ef6647…`).

## 3. Mathematical review (reconstructed independently)

### X1 (Xu points)

- **X1-01.**
  - (a): the map (p,q) ↦ (r₀,s₀) is 2-to-1, exactly τ-invariant, and its surjectivity follows from the explicit preimage. Γ acts by sign changes on (r₀,s₀), which gives |F(ξ)| = 2^{3−β}. β = 2 occurs only for odd n, at (1,1) and (−1,−1).
  - §2: the three reindexings are correct, as are 𝒜s* = 𝒜 and the commutation of s* and c*.
  - §3 (i)–(iii): I re-derived every product-to-sum identity, including the signs E_k vs −E_l for n even, ½E_{min(k,l)} for n odd, and the top terms −½E₀ and +½E₀.
  - §§4–5: the descent through Im P = 0 and the count n(n+1)/2 + ⌈n/2⌉ = |X_n| are correct.
  - Note F7 (surjectivity of the evaluation map) is harmless: it is stated explicitly in §5.
- **X1-02.**
  - (b): χ is 4n-periodic and even, and χ(m+2n) = −(−1)^n χ(m).
  - (c): ω^odd = P(cos u) on [0, π/(2n)] with P = Σ(−1)^{k−1}ℓ_k. P has n−1 sign changes, so it is strictly increasing on [t₁, ∞) and the equality set is (π/n)ℤ. Here n ≥ 2 is genuinely needed, and n = 1 is treated separately.
  - (d) is correct.
- **X1-03.** The reduction to odd residues is correct, as is (r', s') = (|r−a_v|, |s−b_v|) for a_v, b_v ∈ {0, n}. The orbit average gives (|F'|/2)[t(p₀,q₀) + t(p₀+2n, q₀+2n)], and both t-values carry the same sign. The two trigonometric identities check, and so does the final sum ω(u_i)ω(u_j) = L_n².
- **X1-04.** Correct: a triangle inequality on fibres that partition C_n².
- **X1-05.**
  - Step 2 checked for both residue ranges.
  - Step 3: the pairs (i+1, j+1)/s and (i+1, j−1)/c lie in one fibre and have opposite signs whenever b ∉ {0,n} or a ∉ {0,n}.
  - Step 4: the odd-n vertex filter is correct, and so is n = 1.
  - **Headline confirmed:** Λ^Xu_n = L_n² for every n ≥ 1, and argmax = V* for every n ≥ 2, with no finite certificate.
- **X1-06.** The partial fractions from PD-T269 (9) and the block bookkeeping (3) are correct. So are (K2) and (K3) (the coefficient checks at m = 2, 4 and m ≥ 6), the summation formula (5), (7) via 2H_{2K} − H_K, the Wallis telescoping and the alternating-series enclosure. The constant is 7/(240π).
- **X1-07.** (a)–(c) follow, and the decimal constants check by hand: c₁ = 0.962523, πc₁/36 + π²/5184 = 0.08590 < 0.08611, c₁ + π/288 = 0.97343 < 1.
  - (d): I rendered the page image of BCDMV p. 319. The relation is "≲" with "n → ∞" and the setting is even n (p. 312, "we restrict to even degrees n"). The verdict holds under every reading of "≲": asymptotic ≤, O(·) or ∼.
  - (e) uses PD-T269 (1)–(2) as stated in that record, for n ≥ 2.
- **X1-08.** MEASURED; its OPEN sub-item (M3) is labelled correctly.

### X2 (Morrow–Patterson points, n even)

- **X2-21.**
  - Lemma 0: the character sums and the range argument hold; a₊ = M and b₊ = M+1 cannot both occur because a₊ + b₊ ≤ 2M.
  - Lemma 1: the four-case coefficient analysis is correct.
  - ∂x∂y P_M = G_n; Lemma 2 and the Proposition (lattice values, x ≠ y because gcd(M, M+1) = 1) are correct.
  - Part 3: the reflection parities check.
- **X2-22, X2-24.** Correct; the witness node (M−1, 2) checks for M = 4.
- **X2-23.** (a)–(e) re-derived. In (d) I checked the CRT representatives r₁, r₂, their fourfold distinctness, gcd(2M+1, 2N) = 1 and the fold. In (f) I checked the field-intersection argument; see A-m9 and NOTE n1.
- **X2-25.** Every step re-derived:
  - Lemma C (i)–(vii), including h̃ = P − Q, the h̃'' kernel and 68/15, and the one-sided derivatives at a_j, b_j. T₂ = 34π/15 + 32/π³ + 0.650526 + (32/π³)(ζ(3) − 1) = 9.012051 < 9.0121.
  - Lemma R and its consequence (R1).
  - Step A: τ̃ = ηr = jπ + μ, and the bijection onto R₊.
  - Step B: (B1)–(B6), including the case 1 − 2ε_c < 0 and ε_s < M²/(2M+1)² on V̂ < 1.
  - Step C: constants 0.00518, 0.00554, 9/π⁴, the 0.7247 bound and the P = 2M/π² comparison.
  - Step D: 2Mη = π − 2ς, η − ς = π/(4M), k ≤ i, (i+1)² ≤ 4i², and the tails 108/π⁶ and 80/(3π⁴).
  - Step E: 3.629, 2.529 + 0.8106 log M, 7.653 and 15.819.
  - The enclosure of c* is reproduced (R4, R8).
- **X2-26, X2-N30.** The tails for n ≥ 18 and n ≥ 42 are proved by elementary monotonicity, with g(20) ≈ 2.362 and f(44) ≈ 1.777. The finite parts were re-verified on my separate path.
- **X2-N29.** It follows from X2-22 and X2-24. I verified both BBDM statements verbatim on pp. 63–64, and BBDM's node set on p. 32.
- **X2-31.** I re-derived (a) by hand: both lattice-value reductions, the cancellation of the (1−x²)⁻¹d⁻² and (1−y²)⁻¹d⁻² terms, and N_x, N_y coefficient by coefficient. (b)–(e) are correct. The certificate does not use the ε-form Remark (only float-checked); it uses (a).
- **X2-32.**
  - Reduction: the band equals the scanned set. This uses X2-23 (b) for q' > p', the monotonicity of g in q', and the fact that a ball containing 0 aborts the run.
  - The sign rule makes ℓ_a(1,1) ≠ 0 for all nodes; X2-31 (c) gives D_x, D_y; X2-31 (d) gives the local maximum.
  - The finite reduction is proved, the arithmetic is rigorous (Arb), and checker and evidence are committed. Developer rerun: byte-identical. Separate code path: §2.1. **G3 is met.**
- **X2-33.**
  - Step 0: (K1) and (R) are correct, as is the |𝔡_k'| ≤ 2k·min(k, 1/|sin|) case split.
  - Step 1: the bijection ℤ/2N → 𝒯 and u_r, v'_r are correct.
  - Step 2: the separation ≥ δ and the j-th order statistic are correct; so are the arc tiling, the counts of cyclic distances, and the products (M+1)(2+L) and (M+1)(5+2L).
  - Step 4: the evenness/oddness symmetrization is correct, as are the shift to 𝒯' for θ₂ > π/2 and the uniformity of (d) in the offsets.
  - Step 5: ϑ is monotone, ϑ_1030 = 0.99908 < 1, and 3.0387·2.011·3.505 = 21.42 ≤ 21.5.
- **X2-34.** (a), (b), (d) are correct, and the identity G̃ = ¼∂α∂βD_M checks. (c) relies on X2-23 (f) (A-m9).
- **X2-28.** Lemma K is correct; it is (K1) at the lattice phases. The OPEN status is honest (A-m4).
- **X2-27, X2-N35.** MEASURED, labelled correctly. On N35 see A-m1 and A-m5.

## 4. Literature, novelty, gates, evidence

- **Literature verdicts (`literature-xu-mp.md` §§3–5).** Confirmed against the primary texts available:
  - BCDMV (17) is "≲", for even n.
  - BdMV Thm 1 is Λ ≤ 8((2/π) log n + 5)² + 4. The proof is a rotated product of 1-D sums, non-sharp (32/π²) and with no vertex statement. The X1-04 lift is a sharpening of this method and is rightly not claimed as new.
  - BBDM: O(n²) upper bound only, the two §7.1 problems, and the reported corner value (n+1)(n+2)/2.
  - Beberok 2025 is LITERATURE as read by the orchestrator. I could not open it (A-m7).
- **Novelty.**
  - X1: "Λ^Xu_n = L_n²" and "argmax = V*" were not found in the documented search, nor in mine. The wording "no matching result found in the documented search", with the stated coverage limits (CUP 2025 book body, Szili–Vértesi 2009, Della Vecchia–Mastroianni–Vértesi 2009 abstract only, arXiv via digests), is appropriate. No exhaustive claim should be made.
  - X2:
    - The c* constant, the vertex values and the negative answers to BBDM §7.1 were likewise not found.
    - Round X2-3 had **no novelty gate**, and its records miss the closest registry entries (A-m1).
    - The Padua mechanism IDEA-316 ("shifted-lattice majorant S(t) maximal at the coset"; REJECTED: refuted by PD-N079) is the direct analogue of the X2-34 Ξ_n bound and of the failed X2-N35 mechanism.
- **Gates.**
  - G0 (Xu, MP) was pre-registered at `e153416` before any code (`ae75132`). The G1-MP addendum `af65855` also precedes the runs. Later diffs are additions only.
  - The G0 PASS and G1 verdicts are as pre-registered. G1 Xu is superseded by X1-05 for the argmax and remains a MEASURED screen.
  - G2 is met (X1-03 checks: 60 digits, n ≤ 200; N = n, n₂ = 1).
  - G3 is met for X1 (analytic for all n) and for X2-32 (independent separate path, §2.1).
  - G4: published, and strengthened by X2-26.
  - G5 is respected.
  - The C-MP refutation clause ("independent rerun on path B") is satisfied by R3 plus my defining-sum values at (±1, ±1) for n ≤ 30.
- **Evidence hygiene.**
  - All 15 committed evidence files are ≤ 15 393 bytes. The pinned hashes of `mp-x2-corner-arb.json` and of `x2_corner_arb.py` match.
  - No PDF or text extract is tracked. `__pycache__` directories exist untracked and are gitignored.
  - Committed generated outputs stay small. For the timing-field hash and the unreferenced evidence files, see A-m6.
  - **License:** the repository has no LICENSE/COPYING file, and no source file carries an SPDX header. So whether AGPL-3.0-or-later applies cannot be confirmed from the repository. No third-party code was found copied into the topic's scripts: a grep for github/copied/adapted/Leb_MP found none. This is a NOTE for AC.

## 5. Findings

**BLOCKING: none. MAJOR: none.**

| ID | Severity | Locator | Finding | Requested disposition |
|---|---|---|---|---|
| A-m1 | MINOR | theory/X2-33, X2-34, X2-N35 (Sources); novelty-gate-X2.md (no round-3 rows); attempts/X2-round3.md | The round X2-3 mechanisms (far-field localization, the averaged shifted-lattice bound Ξ_n, the "zero shift maximal" route) were not gated, and their records omit the closest registry entries. These are: IDEA-316 / PD-N079 (Padua single-kernel shift-sum majorant; "S maximal at the coset" REJECTED: refuted), IDEA-206, IDEA-326–328 and PD-T215–T228 (Padua localization). X2-N35 is the MP variant of IDEA-316. The MP kernel differs, so the test was legitimate, but the record must say so. | Add a dated round-X2-3 addendum to novelty-gate-X2.md. Cite the closest entries in the three records. At PR preparation, register the IDEA entries with these predecessors (X2-N35: variant of IDEA-316, REJECTED: failed, MEASURED scope). |
| A-m2 | MINOR | results/padua-xu-lebesgue-20261114.md l. 32; LOG.md l. 74 | The summaries overstate X2-33 (c). It is not true that "every maximizer lies within angle ≤ 21.5 log²(n+2)/n of the vertex lines, for every n". The record proves sin θ₁, sin θ₂ ≤ ϑ_n for every even n, which is non-trivial only for n ≥ 1030. The bound ϑ_n ≤ 21.5 log²(n+2)/n holds for n ≥ 1030 only (ϑ_10 ≈ 36.8 > 13.3). The region is the four vertex boxes. | Reword the results file and PR body. Add a one-line dated correction under the LOG entry; do not rewrite it. |
| A-m3 | MINOR | report.md l. 3, §2 last bullets, §4; results file header l. 3 and l. 31 | Stale or incorrect process text. The report says round X2-3 is "in progress" and omits X2-31…N35. The report and the results header say every PROVED item was "confirmed by an independent subagent check", which is false for X2-31…34: those are confirmed only by this audit. "-32 … independent rerun pending" is now done (§2.1). | Update at PR preparation and cite audit-01. |
| A-m4 | MINOR | theory/X2-28 l. 128 ("PARTIAL in the sense of the workflow") and l. 32 (row "First variation … MEASURED"); X2-32 "Split from" | "P1 for every even n ≥ 2" is a plan item, not a registered target, so calling it PARTIAL misuses the status word. The MEASURED row is superseded by X2-32 (independent check m4). | Non-material fix: drop "PARTIAL", describe it as plan progress, and annotate the row "superseded by X2-32". Registering P1 as its own PARTIAL target would be a material change: do it only with a focused re-audit. |
| A-m5 | MINOR | theory/X2-N35 Statement/Checks; evidence/mp-x2r3_checks_b.json shift rows | (i) The float64 closed form of G̃ cancels catastrophically near x = y. At M = 102 the recorded Ξ_n(a)/Ξ_n(0) = 1.075249 differs from the certified 1.0752352 ± 3e−8 (§2.1). The cause is node (p,q) = (43,44), where x − y = −4.3e−6; there the float64 closed form gives 72661.5 against a true G̃ = 72566.1. The conclusion is unaffected. (ii) The Statement asserts the result at M ∈ {62, 102, 202}, but Checks quote values only for M = 202. | Note the accuracy limitation, or switch to the defining sum. Cite the certified values in `evidence/audit-x2-separate-path.json`. |
| A-m6 | MINOR | evidence/mp-x2r3-first-variation.json (`full_output.sha256`); evidence/mp-fv_full_2_24.json, mp-x2r3_checks_{b,c,t}.json, mp-corner-values.json, mp-cmp-identify.json | (a) The pinned SHA-256 of the regenerable 758 KB output covers the non-deterministic `wall_seconds` field. A rerun matches only after that field is substituted; I did this and got an exact match. (b) Six evidence files are cited by no theory record or gate verdict, and mp-fv_full_2_24.json lacks command and version fields. | Record a timing-free hash, or state the substitution. Reference each evidence file from the Checks of the record it supports, or add a short evidence index. |
| A-m7 | MINOR | theory/X2-26 Statement ¶ "≈ 7.5·10⁻⁴"; literature-xu-mp.md §3.1; lit-notes/X2-sources §1b, §8 item 1 | (Carried from independent check m3; still open.) The comparison constant rests on the orchestrator's transcription "(n/2+n+2)²", which is silently normalised to "(3n/2+2)²". Page and equation locators are still missing. I could not access the source. | Add "(as transcribed; display not re-checked)", or re-check the display and add locators, before any manuscript or LIT record uses the number. |
| A-m8 | MINOR | "Independent rerun: pending" lines in X2-21…26, X2-N29, X2-N30, X2-31…34, X2-N35, X2-27, X2-28; gates.md l. 66; LOG header l. 6 ("Claims: none yet") | Stale process text. The reruns have now been done (R1–R8, §2.1). | Update with a link to audit-01. These are auditor-recognised MINOR fixes. |
| A-m9 | MINOR | theory/X2-23 Assumptions l. 36 ("nothing else in this topic depends on (f)") and status row "(f) … not used elsewhere" | These statements are now stale. X2-34 (c) uses (f) for every n. X2-31 (b) cites (f) for n > 3000 (for n ≤ 3000, X2-32 certifies it independently). X2-28's remark also uses it. Under WORKFLOW, a part that another result depends on is substantive. (f) is correct, but it rests on a textbook fact whose locator (Washington, Prop. 2.4) is unverified (NOTE n1). | Correct the dependency statement. Add a verifiable citation or a two-line self-contained proof: compare the degree φ(lcm) of the compositum with φ(2M)φ(2M+2)/φ(gcd)). Decide whether (f) needs its own ID at PR preparation (proposal: keep it inside X2-23 but list it as a dependency in X2-34). |
| n1 | NOTE | X2-23 (f) | The Washington Prop. 2.4 locator for ℚ(ζ_a) ∩ ℚ(ζ_b) = ℚ(ζ_gcd) was not verified by me either. The fact itself is standard. Ball arithmetic confirms its conclusion for n ≤ 3000 (X2-32 and §2.1). | — |
| n2 | NOTE | X2-N35 | The auditor's Arb computation certifies Ξ_n(a) > Ξ_n(0) at M = 62, 102, 202. The negative statement could therefore be PROVED at these M. That would be a status change, and so material. | Developer's choice; it needs a focused re-audit if taken. |
| n3 | NOTE | X2-N30 Scope | Since Λ_n ≥ λ_n(1,1) > d_n for every even n ≥ 6, BBDM's reported value (n+1)(n+2)/2 is also refuted for the Lebesgue constant itself when n ≥ 6. For n ∈ {2, 4} only the vertex values are covered. | Optional remark. |
| n4 | NOTE | literature-xu-mp §2, X2-31 (e), X2-21 Sources | BBDM's x-symmetry is Lemma 1 (p. 45). Their §7.1 calls it "Lemma 15". The records use both labels. | Harmonise to "Lemma 1 (p. 45; cited as Lemma 15 in §7.1)". |
| n5 | NOTE | repository | There is no LICENSE file, so AGPL-3.0-or-later applicability cannot be confirmed from the repository. No third-party code is included. | AC's decision. |
| n6 | NOTE | X1 novelty | The coverage limits stand: the CUP 2025 book body, Szili–Vértesi 2009, Della Vecchia–Mastroianni–Vértesi 2009 (abstract only), and arXiv read through digests. My extra searches found nothing. | Keep the "not found in the documented search" wording. |
| n7 | NOTE | independent-checks-X2 m1, m2, M1 | I confirmed these as fixed (docstring, "convergent series" wording, committed arb evidence with hashes). Its m4 is superseded by X2-32 (A-m4). | — |
| n8 | NOTE | X2-25 constants | The thin margins are re-verified: T₂ = 9.012051 vs 9.0121; sup sin²x/x = 0.724611 vs 0.7247; Σe₁ = 2.01137 vs 2.012; 3.62807 vs 3.629; 1.11189 vs 1.1119. | — |
| n9 | NOTE | X2-N29/N30 dispositions | At registration, the *candidate* X2-C2 (the negative answer) is a retained, successful candidate. "REJECTED: refuted" applies to BBDM's external statements, which the PD-N records refute. | Keep this distinction in state/IDEAS.md. |

## 6. Per-claim verdicts

| NN | Record | Claimed | Verdict |
|---|---|---|---|
| 01 | X1-01 | PROVED | **Confirmed** (proof reconstructed; the lift is not claimed as new, which is correct) |
| 02 | X1-02 | PROVED | **Confirmed** (classical facts re-proved; attribution adequate) |
| 03 | X1-03 | PROVED | **Confirmed**, both parities |
| 04 | X1-04 | PROVED | **Confirmed**: Λ^Xu_n = L_n² for every n ≥ 1 |
| 05 | X1-05 | PROVED | **Confirmed**: argmax = V* for every n ≥ 2 (n = 1 separately) |
| 06 | X1-06 | PROVED | **Confirmed**; it depends on PD-T269 (9) exactly as stated there |
| 07 | X1-07 | PROVED | **Confirmed**, including the verdict on Conj. (17) (page image checked) and (e) |
| 08 | X1-08 | MEASURED | Label correct |
| 21 | X2-21 | PROVED | **Confirmed** |
| 22 | X2-22 | PROVED | **Confirmed** |
| 23 | X2-23 | PROVED | **Confirmed** (A-m9, n1) |
| 24 | X2-24 | PROVED | **Confirmed** |
| 25 | X2-25 | PROVED (computer-assisted enclosure) | **Confirmed**; enclosure reproduced (R4) and independently enclosed (R8) |
| 26 | X2-26 | PROVED (ball arithmetic n ≤ 16) | **Confirmed**; finite part re-verified on a separate path (A-m7 wording) |
| 27 | X2-27 | MEASURED | Label correct |
| 28 | X2-28 | OPEN | **Honest OPEN** (A-m4) |
| N29 | X2-N29 | PROVED negative; BBDM §7.1 statements REJECTED: refuted | **Confirmed**; scope exact; BBDM text verified |
| N30 | X2-N30 | PROVED negative (ball arithmetic n ≤ 40) | **Confirmed**; analytic for n ≥ 42; finite part re-verified |
| 31 | X2-31 | PROVED | **Confirmed** (closed forms re-derived by hand; band representation independently confirmed for n ≤ 80) |
| 32 | X2-32 | PROVED (computer-assisted, even n ≤ 3000) | **Confirmed**: proved finite reduction, rigorous Arb, committed checker and summary, byte-identical developer rerun, separate code path agreeing at 109 n up to 3000 |
| 33 | X2-33 | PROVED | **Confirmed** (Steps 2 and 4 re-derived; A-m2 concerns the summaries only) |
| 34 | X2-34 | PROVED (tool) | **Confirmed** ((c) depends on X2-23 (f); A-m9) |
| N35 | X2-N35 | MEASURED negative | **Eligible as PD-N** (a measured, scoped mechanism failure); A-m1, A-m5, n2 |

## 7. Remaining uncertainty

- Beberok JAT 2025 was not read by me. Its constant (≈ 7.5·10⁻⁴) and its eq. (2) are taken from the orchestrator's transcription. The local mathematics does not depend on it.
- Novelty rests on documented searches with the coverage limits in n6. In particular, Xu's CUP 2025 book body is unread.
- The cyclotomic fact behind X2-23 (f) is standard, but its citation locator is unverified. For n > 3000 the non-vanishing of ℓ_a(1,1) (used in X2-34 (c) and stated in X2-31 (b)) rests on it.
- Arb and python-flint are trusted, as in the developer's certificate. My separate path uses the same library but a different formula and different code. It is not a fully independent arithmetic library.
- X2-28 (the argmax, and lim Λ_n/n² = c*) is OPEN. The audit makes no statement on it beyond its honest labelling.

## 8. For the orchestrator

### 8.1 PR #36 AUDIT section (paste as one paragraph)

AUDIT — audit-01, Claude Opus 5.5 (claude-opus-5-5) xhigh, independent auditor run as a subagent by AC's choice (LOG 2026-11-14 15:30; no access to the development conversation; no git writes). Audited SHA `971beb79b8edb93835b20d1b9148e93d4ba3aba4` (head `46dcd92` inspected: only LOG/handoffs differ); rules at `46dcd92`; base `99a9b1d`. Read in full: every theory record (X1-01…08, X2-21…28, X2-31…34, X2-N29, N30, N35), gates, literature and novelty notes, independent checks, the merged dependencies PD-T159/269/270, and `state/IDEAS.md` (complete scan; Padua argmax sections and the shortlisted entries IDEA-047/206/288/316 and PD-N079 read in full); BCDMV p. 319 (page image: "≲", even n), BdMV Thm 1, and BBDM pp. 32, 45, 63–64 were checked against the primary texts. Reruns: every expected developer command was rerun and reproduces the committed evidence (xu/mp G0, cmp_check, x2_corner_arb n ≤ 60, x2r3 first variation n ≤ 3000 byte-identical up to the timing field, and all independent-check scripts). An auditor-written separate code path (defining kernel sums, no closed forms) confirms X2-32 at 109 values of n up to 3000 and in full-sum mode for n ≤ 80, so gate G3 is met; an Arb certificate confirms X2-N35 at M = 62, 102, 202, and an own Vandermonde check confirms X1 for n ≤ 24. Findings: BLOCKING 0, MAJOR 0, MINOR 9 (A-m1 round-X2-3 novelty gate and the closest entries IDEA-316/PD-N079; A-m2 overstated X2-33 summary; A-m3 stale report and results; A-m4 "PARTIAL" misuse in X2-28; A-m5 float cancellation in the X2-N35 M = 102 value, conclusion unchanged; A-m6 evidence hash and references; A-m7 Beberok constant transcription; A-m8 stale "rerun pending" text; A-m9 stale X2-23 (f) dependency statement), NOTE 9. All 23 claims are confirmed at their stated statuses: X1 (Λ^Xu_n = L_n² for every n ≥ 1; maximizers exactly the non-node vertices for every n ≥ 2; BCDMV Conj. (17) settled with "≲" read asymptotically) and X2-21…26, N29, N30, 31…34 PROVED; X1-08 and X2-27 MEASURED; X2-N35 MEASURED negative; X2-28 OPEN. Remaining uncertainty: Beberok 2025 and Xu's CUP 2025 book were not read; novelty means "not found in the documented search"; the X2 argmax stays OPEN. Accepted with MINOR findings; stage PR.

### 8.2 Recommended LOG stage

**PR.** The audit is accepted with at most MINOR findings. The MINOR fixes go into a MINOR-only response at PR preparation, and the readiness check verifies them by diff (WORKFLOW).

### 8.3 Handoff 03 (full text; the only permitted substitution is the SHA placeholder)

```markdown
# Handoff 03 — padua-xu-lebesgue-20261114 — MINOR-only response to audit-01 and PR preparation

- Status: open
- Previous handoff: [02-audit.md](02-audit.md) (done; see its status line)

- Next agent / model / effort: **Claude, Opus 5.5** (topic orchestrator; effort as configured) for the response and the PR preparation; mechanical registry and record edits may be delegated to **Sonnet 5.5 medium** subagents (WORKFLOW allocation; AC's standing preference). No Fable round.
- Role: orchestrator (developer response + PR preparation)
- Branch: `claude/padua-xu-lebesgue-20261114`, draft [PR #36](https://github.com/aacchhee/padua_research/pull/36)
- Input head SHA: `<SHA of the commit that adds audit-01.md>` (the commit that publishes this file comes later)
- Main / base: `99a9b1d` (recheck `origin/main` and every open PR at start)
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 xhigh (auditor of audit-01; committed unchanged by the orchestrator) · 2026-11-14

## Task

1. **Response.** Write `topics/padua-xu-lebesgue-20261114/response-01.md`. Answer every finding of `audit-01.md` §5 (A-m1 … A-m9; the NOTEs n1–n9 optionally) with: fixed (file and line), evidence-based rejection, or unresolved with reason. Disagreements stay in the file for AC; never edit audit-01.md.
2. **Apply the MINOR fixes, non-material only** (wording, links, stale process text, dated addenda, citations of closest entries, references to existing evidence). In particular:
   - A-m1: add a dated "round X2-3" addendum to `novelty-gate-X2.md`, recording the scan, the shortlist and the differences: IDEA-316/PD-N079, IDEA-206, IDEA-326–328, PD-T215–T228. Cite the closest entries in the Sources of X2-33, X2-34 and X2-N35.
   - A-m2: fix the X2-33 summary in the results file (and later in the PR body), and add a dated one-line correction under LOG l. 74.
   - A-m3, A-m8: update report.md, the results-file header and the "Independent rerun: pending" lines, linking audit-01.
   - A-m4: take the non-material option. Drop "PARTIAL" in X2-28 l. 128, and annotate the MEASURED first-variation row as superseded by X2-32.
   - A-m5: add the accuracy note to X2-N35, and cite `evidence/audit-x2-separate-path.json` for M = 62, 102, 202, without changing its status.
   - A-m6: record a timing-free hash or note the substitution in `evidence/mp-x2r3-first-variation.json`'s companion text, through a dated note in X2-32, not by rewriting pinned evidence. Reference each currently unreferenced evidence file from a record.
   - A-m7: qualify the ≈ 7.5·10⁻⁴ comparison as "as transcribed", or re-check Beberok's display and add locators.
   - A-m9: correct X2-23's dependency statement, add a verifiable citation or a short proof of the cyclotomic fact, and list X2-23 (f) under X2-34's dependencies.
   - Not in this step, because they are material: registering P1 as its own target (A-m4, alternative option), upgrading X2-N35 to PROVED (n2), and any change of a statement, quantifier or status. If AC wants any of these, do it and send that change to a focused re-audit (stage AUDIT).
3. **PR preparation** (WORKFLOW step 5, "Reserve fresh ranges", "Proportionate audit and records"):
   - Run the full reservation check: refresh `main` and all open PRs (drafts included), read every ledger and retired reservation, compute the per-namespace maxima. Reserve fresh ranges with headroom in a new `topics/padua-xu-lebesgue-20261114/ALLOCATIONS.md`, recording the heads checked and the date, and in the PR body. Needs:
     - PD-T: 20 (X1-01…08, X2-21…28, X2-31…34);
     - PD-N: 3 (X2-N29, N30, N35);
     - IDEA: the novelty-gate candidates X1-C1…C3 and X2-C1…C4, plus the round-3 mechanisms (far-field localization, averaged shifted-lattice bound, zero-shift maximality = IDEA-316 variant REJECTED: failed, first-variation band certificate) and the deferred plan items (P1-tail, W1–W3);
     - LIT: new primary-source records for Xu 1996, BdMV 2006, BBDM 2026 (upgrade of LIT-378 from UNVERIFIED, with locators p. 32, Lemma 1 p. 45, Thm 4 p. 53, §7 p. 63, §7.1 p. 64), Beberok JAT 2025 (as read; locators pending), Li–Sun–Xu 2009, Harris 2010, Xu JAT 2012, Dencker–Erb 2017, Erb 2016, Erb–Kaethner–Ahlborg–Buzug 2016, ETNA 2006 and CDMV 2005; addenda for LIT-486 (BCDMV) and LIT-379 (Kolomoitsev–Lomako).
   - Registry edits, applied directly and reviewed by diff:
     - `PROOF_STATUS.md` rows (statuses exactly as confirmed in audit-01 §6; X2-N29/N30 with `REJECTED: refuted` for the BBDM statements; X2-N35 MEASURED negative with `REJECTED: failed`; X2-28 OPEN);
     - a new `state/IDEAS.md` section, with dated addenda to IDEA-047 (MP survey: publication verified; X2 results; argmax OPEN) and cross-references to IDEA-206 and IDEA-316 (keep n9's distinction: X2-C2 is a retained, successful candidate);
     - `literature/INDEX.md` and records;
     - `ID_CROSSWALK.md` (provisional→final map and ledger link);
     - `RESULTS.md` (this topic's section only, from the corrected results file);
     - `state/CURRENT.md` (frontier: the X2 argmax, P1-tail, W1–W3; X1 closed).
   - Update the theory headers to the final IDs, keeping the provisional IDs as aliases. Update the results file and report.md. Fill the PR #36 WORK, AUDIT and PR sections; the AUDIT section is audit-01 §8.1. No novelty claim beyond "not found in the documented search", with the coverage limits of literature-xu-mp §5 and audit-01 n6.
4. Commit and push. Then, in a following commit, set this handoff's status to `done in <sha>` and add **handoff 04: readiness check**. The readiness check is done by a Claude Opus 5.5 high auditor distinct from the developer (fresh thread or subagent, AC's choice). It covers: the reviewed `git diff` of the shared registries; the MINOR-fix diff (confirm no material change); and the reservation refresh against current heads.

## Read first

- AGENTS.md, agents/WORKFLOW.md (Work cycle; Proportionate audit and records; Reserve fresh ranges), agents/claude/CLAUDE_ROLES.md at the branch head; record the SHA.
- `topics/padua-xu-lebesgue-20261114/audit-01.md` (all of it), LOG.md, results file, report.md, novelty gates, literature-xu-mp.md.
- The newest topic ledger and PR-preparation records on main for format: `topics/padua-effective-cubature-20261112/ALLOCATIONS.md` and `pr-preparation/`.
- `templates/IDEA.md`, `templates/LITERATURE_RECORD.md`, `templates/THEORY.md`.

## Scope limits

- No new mathematics. Do not reopen the AC decisions in the LOG (model allocation, Claude auditor, dropped MPX target). X2-28 stays OPEN; its continuation (P1-tail, W1–W3) is later development work.
- MINOR-only response: any material change (statement, quantifier, status, dependency, result-bearing code or evidence) returns the topic to AUDIT for a focused re-audit of that change.
- Never edit audit-01.md or the developer's pinned evidence; correct prose with dated addenda.
- No commits to main, merges, force-pushes, tags, or edits under `.github/`. Only AC merges. Commits authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Claude`, `Model: <actual model and effort>` and the session lines.

## Acceptance and outputs

- `response-01.md` answers every audit-01 finding; the MINOR fixes are committed separately from the registry edits, so the readiness diff shows them on their own.
- `ALLOCATIONS.md` with the reserved ranges and the heads checked; the final-ID map; registry edits applied; theory headers updated; RESULTS.md section; PR #36 body with WORK, AUDIT (audit-01 §8.1) and PR sections, including the decision requested from AC.
- LOG: stage PR, one line linking this handoff and one linking handoff 04.
- When done: commit the outputs; then, in a following commit, set this status to `done in <output-commit-sha>` and add handoff 04 (readiness check). Reply to AC with the short Continue prompt only.
```
