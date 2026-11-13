# audit-05 component D1a: spectral-obstruction proof reconstruction

- Auditor: Claude subagent, Opus 5.5 (`claude-opus-5-5`), xhigh. This is an independent mathematical audit of Codex development. The effort level is xhigh because the scope is an adversarial reconstruction of a non-effective asymptotic theorem.
- Candidate: `ec5c089f35fa2002a2ed2b293a41034364380170`. Head `acf0fbc` only adds handoff 20 and changes handoff 19's status line. I checked this with `git diff --stat ec5c089 acf0fbc`: 2 handoff files, nothing else.
- Rules: AGENTS.md (as supplied at the head) and the severity definitions in agents/WORKFLOW.md:49 and CLAUDE_ROLES.md:24 at `ec5c089`. I made no repository edits and no state-changing Git operations. All code ran in an isolated `git archive` copy.
- Scope: handoff 20 §B only, which is D1. I did not cover D2–D5, A/F, counters, the manifest or the LOG.

## Inputs read (SHA256 at ec5c089)

| File | SHA256 (prefix) |
|---|---|
| final-d1/README.md | 76abdeca |
| final-d1/spectral-obstruction.md (D1-04) | 33206f2d |
| final-d1/finite-frame.md (D1-01) | 6e02595b |
| final-d1/stationary-limit.md (D1-02) | 11c6c719 |
| final-d1/complete-law.md (D1-03) | 6db3f5dc |
| final-d1/weight-corollary.md (D1-05) | d99b5875 |
| final-d1/general-weight-open.md (D1-06) | e1c8162f |
| final-d1/reconstruction.md | adb6b469 |
| final-d1/sources.md | 30cf3286 |
| final-d1/gate.md / protocol.md / rounds.md / ideas.md | adfff151 / 2ea36269 / 2d3ed67a / c0e39d7e |
| frontier-assessment.md (C1 entry, lines 89–125) | 16609ff2 |
| code/fd1_controls.py / evidence/fd1-controls.json | e5bf2b92 / 8625e7f2 |

The four proof files are byte-identical to the hashes pinned in final-check/d1-audit.md. I skimmed that supplemental audit only after finishing my own reconstruction. I also read the D1 passages of paper-note-draft.md §2 and final-narrowed-report.md:7–15 to check that their wording matches.

## Verdict

**PASS. I found no BLOCKING or MAJOR gap.** I reconstructed every step listed in handoff 20 §B line by line, and the chain is valid as written:

finite projection → reflection lift → squeeze → pruning → uniform separation → compact stationary law with exact intensity → a.s. orthogonality → Bessel saturation → a.s. completeness → GL1.1 contradiction → quantifier negation.

Recommended statuses, unchanged from the developer's:

- D1-01, D1-02, D1-03: **PROVED** as local analytic lemmas, using standard background only.
- D1-04 and D1-05: **PROVED with explicit LITERATURE dependency** on Greenfeld–Lev Thm 1.1 (AC's E4 convention).
- D1-06: **OPEN**. It is correctly not promoted; H1 and H2 are labelled hypotheses.

I found two MINOR items (wording and record hygiene) and five NOTEs, listed below.

## Line-by-line reconstruction

**(1) Polynomial defect identity (finite-frame.md:9–13, 31). Correct.**
- Let B_ia = sqrt(w_i) phi_a(x_i). Exactness on Pi_(2n-2) gives B^T B = I_D. Then BB^T is a rank-D projection with diagonal p_i in [0,1], so sum(1 - p_i) = N - D. The row of P^2 = P gives sum_(j≠i) w_i w_j K_ij^2 = p_i - p_i^2.
- Positivity is used only through sqrt(w_i). The proof needs Pi_(2n-2) exactness, not 2n-1. Consequence: N >= D, so N_r >= D_r in the negation.

**(2) Reflection lift and squeeze (finite-frame.md:15–23, 33–46). Correct, including boundary nodes.**
- The sign group Z_2^d is abelian, so all points of an orbit share one stabilizer. Averaging over all 2^d signs is therefore uniform on the s_i distinct atoms. The average is prod cos(k_j theta_j) = prod T_|k_j|(x_j), of degree |k|_1.
- Stabilizers come **only** from coordinates x_j = ±1 (theta_j in {0, pi}). A coordinate x_j = 0 has theta = pi/2, whose orbit {pi/2, 3pi/2} has two points, so the task brief's "±1 or 0" is inaccurate for 0. The file states this correctly. Distinct cube nodes have distinct cosine vectors, so their orbits are disjoint.
- Rank gives m_n <= M, and folding gives M <= 8N. The exact count is m_n = (2n-1)(2n^2-2n+3)/3, so m_n ~ 4n^3/3 = 8·(n^3/6). The squeeze 1 <= M/m <= 8(N/D)(D/m) -> 1 needs no boundary estimate: boundary nodes can only lower M, and M >= m_n anyway.

**(3) Pruning, kernel limit and separation (stationary-limit.md:29–57). Correct. Separation is proved, not assumed.**
- At most (M - m)/eps <= sqrt(a_n)·m = o(m) atoms are discarded, so g_n/n^d -> |O| = 2^d/d!.
- Take the single off-diagonal term of row j. Dividing by q_j gives |D_n/m_n|^2 <= eta_j/q_l <= eps/(1 - eps) for every pair of distinct retained atoms. This uses positivity through the projection row identity.
- F_n(x_j - x_l + nz) = D_n(t_j - t_l)/m_n exactly, because F_n is nZ^d-periodic.
- Riemann-sum limit: C_n Δ O lies in an O(1/n) l1-shell, the cell oscillation is <= 2πR·sqrt(d)/n, and n^d/m_n -> 1/|O|. This gives F_n -> F uniformly on compacts.
- b depends only on F, not on r. Copies of the same atom are >= n apart. So L_n is b-separated (strictly) after a finite prefix.

**(4) Compactness, stationarity and intensity (stationary-limit.md:59–76). Correct.**
- X_b is a vaguely closed subset of a set of Radon measures with uniform local mass bounds. The sketch at line 61 is terse but standard (NOTE 3).
- P_n is exactly stationary: L_n is periodic, and U_n is uniform modulo nZ^d. Translation by any fixed s is continuous on X_b, so invariance passes to the weak limit along a single subsequence.
- Intensity: by the period-cell computation, E_(P_n) sum f = (g_n/n^d)·∫f exactly. The functional Λ -> sum f(λ) is continuous and bounded by C_(R,b,d)·||f||_∞, so mass cannot escape. Clusters are impossible because separation is uniform.

**(5) Limiting orthogonality (stationary-limit.md:78–85; reconstruction.md:16). Correct.**
- H_f is continuous: the product measure converges vaguely on separated configurations, and the diagonal equals sum f^2 because F(0) = 1.
- Two copies of one atom are separated by n|z| >= n > diam(supp f - supp f) for large n, so they never both enter H_f. Every remaining pair is controlled by (1) plus sup_K |F - F_n| -> 0, with at most C^2 terms. So H_f -> 0 uniformly in the translation, E_P H_f = 0, and taking cutoffs f_R gives F(λ - λ') = 0 for all distinct pairs a.s.
- F(λ - λ') = 0 is exactly <e_λ, e_λ'>_(L^2(O)) = 0 in the exp(2πi λ·x) convention.

**(6) Completeness (complete-law.md:21–42). Correct.**
- Plancherel: ∫|F|^2 = |O|/|O|^2 = 1/|O|.
- The mean measure is locally finite. It is identified as |O|·Leb from C_c tests and extended to nonnegative Borel tests by monotone convergence (Campbell). So E S(y) = 1 with no tail exchange.
- Bessel's inequality for the orthonormal h_λ against the unit vector h_y gives S <= 1, so S = 1 a.s. for each y. Intersect these events over y in Q^d. Pythagoras then puts h_y in the closed span H for every rational y.
- If g ⊥ H: g in L^2(O) ⊂ L^1, so its Fourier transform vanishes on Q^d, hence everywhere by continuity, hence g = 0. Completeness holds a.s. on one event.
- The density is exactly critical: |O| = 4/3 in the λ = nθ/(2π), exp(2πi λ·u) normalization, equivalently |O|/(2π)^3 in the exp(iλ·x) convention. The empty configuration has S = 0 and so has probability 0.
- The developer correctly notes that critical density alone is insufficient (Z∖{0}) and is not used.

**(7) Greenfeld–Lev Thm 1.1. Primary statement verified independently.**
- I downloaded arXiv 1602.08854v2 and read printed pp. 1–3 myself (39 pages, 508257 bytes, SHA256 `c9c201bec7f408a4195f4e01cf0e2f1e11c2cdd15704b7252c52f537f8cce37a` as served on 2026-11-12).
- Definition (1.1): Ω is bounded and measurable with positive measure. A countable Λ is a spectrum if {e^(2πi<λ,x>)} is orthogonal and complete in L^2(Ω).
- "Theorem 1.1. Let Ω be a convex polytope in R^d. If Ω is a spectral set, then all the facets of Ω must be centrally symmetric."
- D1-03 outputs exactly this kind of object: Λ is countable because it is locally finite. O is a full-dimensional convex polytope, and its facet conv(e1, e2, e3) is a triangle, which is not centrally symmetric (no vertex can be the centre, so vertices would pair up, giving an even number). spectral-obstruction.md:36 and sources.md:9 match the source exactly.

**(8) Quantifiers (spectral-obstruction.md:38–46). Correct.**
- The negation gives n_r >= r and N_r < (1 + 1/r)D_r. Together with N_r >= D_r this gives N_r/D_r -> 1 with no monotonicity needed. The rest of the chain then contradicts GL.
- Equivalently, liminf over n of (min N)/D_n > 1, where the minimum over positive rules exists by Tchakaloff.
- Normalization does not matter: dim Pi_n/dim Pi_(n-1) = (n+3)/n -> 1, so stating the result against dim Pi_n changes only γ. The Padua-cardinality exclusion (n > 3/γ) is correct. Nothing effective is claimed, which is correct.

**(9) Where the 2-D case escapes. Only at step (7).**
- In d = 2 every lemma runs unchanged and does produce a spectrum: the diamond is spectral with spectrum B^(-T)Z^2 of density 2 = |O_2|, and its facets are segments.
- I verified the Padua lift claims of reconstruction.md:35–41 by hand. The generator (π/n, π/(n+1)) has order lcm(2n, 2n+2) = 2n(n+1). The scaled lattice basis is (1,0), (1/2, n/(2(n+1))). The defect sums are n + 1 and 4n - 1. All η_j equal a_n/(1 + a_n) < ε_n, so no Padua atom is pruned. I also checked these numerically (below).
- The sphere and disk comparisons are labelled literature reports, not premises. The Marzo abstract ("no complete interpolation families for p≠2") and the AMO abstract (no orthogonal reproducing-kernel families on the ball for large k) match the sources.md descriptions; I read abstracts only. An auditor heuristic, not a claim: a sphere analogue would predict N >= (1+γ')n^2, which is consistent with known spherical designs of McLaren efficiency about 1 (N ≈ 4n^2/3). I found no conflicting literature.

**(10) Weight corollary (weight-corollary.md:21–27). Correct.**
- With v_i = p(x_i)w_i/c > 0, Σ v_i q(x_i) = ∫ q dμ for deg q <= 2n-1-k. Taking r = n - ceil(k/2) gives 2r - 1 <= 2n - 1 - k. N is unchanged and binom(r+2,3)/binom(n+2,3) -> 1, so γ_p = γ/2.
- The doubling paragraph is descriptive and not used by the conclusion. The comparability r/sqrt(1 - |x| + r) holds in both regimes (1 - |x| below or above r), and the box/ball sandwich is fine.
- In general-weight-open.md I checked both cheap examples (the point mass, and the curve measure via linear independence of t^a·e^((b+√2c)t)). H1 and H2 are clearly hypotheses. The general case is correctly left OPEN.

## Findings

| # | Sev | Location | Finding / disposition |
|---|---|---|---|
| F1 | MINOR | spectral-obstruction.md:9,19; weight-corollary.md:9–10,21; finite-frame.md:15 | **The node-location hypothesis is implicit.** The proof needs x_i ∈ [-1,1]^3: the arccos lift needs it, and so does v_i > 0 in D1-05, since p > 0 is assumed only on the closed cube. "Rule on [-1,1]^3" and "Nodes may lie on any cube face, edge or vertex" imply it, but ":19 … support geometry are otherwise unrestricted" could be read as allowing exterior nodes. Positive rules with exterior nodes do exist at low degree, e.g. degree 1 with nodes ±2e1 and weights 1/2. Fix: add "with all nodes in [-1,1]^3" to both statements, and the same in paper-note-draft.md §2 Theorem A. This clarifies scope and changes no proof. It is eligible as an in-place wording fix only if the orchestrator considers it pure wording; otherwise return it to Codex. |
| F2 | MINOR | finite-frame.md:5 and :52; stationary-limit.md:89 and :93; spectral-obstruction.md:56 | **Stale in-progress text.** These lines describe states that R3/R4 have since completed: "Original asymptotic target remains OPEN…", "Independent execution is requested from root. Next unresolved D1 step…", "It remains to show…", "still recorded as OPEN pending completeness…", "The mandatory final reconstruction still checks…". They are accurate as round history, but a reader of the canonical theory homes may misread the current status. Fix: add a dated one-line pointer such as "Superseded: completed in D1-03/D1-04, R4 reconstruction.md; current status in README", rather than rewriting the history. This is eligible as a stale-process MINOR fix. gate.md:22 is already superseded by its dated line 32, so no action is needed there. |
| N1 | NOTE | stationary-limit.md:57, 61 | L_n is strictly >b-separated, while X_b must use |λ - λ'| >= b to be vaguely closed. The intended meaning is clear; the wording could say ">= b". |
| N2 | NOTE | spectral-obstruction.md:42; finite-frame.md:46 | The lift is actually exact through l1 degree 2n-1, and the whole proof uses only Pi_(2n-2) exactness. The theorem therefore also holds, with the same D = dim Pi_(n-1), for rules exact through 2n-2. This is not claimed and nothing is required. |
| N3 | NOTE | stationary-limit.md:61 | The compactness and metrizability sketch is terse. It is standard (vague compactness of measures with uniform local mass bounds, plus closedness of >= b separation). A textbook pointer (Kallenberg, or Daley–Vere-Jones) would help a referee. It is not a gap. |
| N4 | NOTE | complete-law.md:13, 29–31 | Measurability of Λ ↦ S_Λ(y) is implicit: it is a monotone limit of continuous cutoff functionals on X_b. This is fine. |
| N5 | NOTE | sources.md:3, 7 | The developer says full-PDF bytes and hash were unavailable. The arXiv-served v2 bytes I obtained are recorded above as an observed retrieval identity. arXiv may re-render PDFs, so this is not a canonical hash and creates no new premise. |

## Executions actually performed (isolated copy only)

I exported the candidate with `git -C /workspace/padua_research archive ec5c089… | tar -x -C …/scratchpad/a5-D1a/tree`.

1. **Controls replay.**
   - Command: `cd …/a5-D1a/tree && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 …/venv/bin/python -B topics/padua-3d-20261106/code/fd1_controls.py --output …/scratchpad/a5-D1a/fd1-controls-claude05.json`
   - Environment: Python 3.13.18 and SymPy 1.14.0. The producer recorded Python 3.12.14.
   - Result: 0.403 s, all assertions passed. The `rows` are identical to the committed `evidence/fd1-controls.json` (Python equality check, including the node_defects SHA256s). Receipt SHA256 `b8a17bb5…13b`.
2. **Independent float64 identity checks.** I wrote my own script, `…/scratchpad/a5-D1a/checks/d1_sanity.py`, which is not derived from the producer code. Output is in `…/checks/d1_sanity.out`; result ALL_OK in 1.8 s. These are sanity checks, not a proof.
   - Rules checked:
     - 3-D product Gauss–Chebyshev, n = 2–5. All orbits have size 8; odd n includes the x = 0 coordinate.
     - 3-D product Lobatto–Chebyshev, n = 2–4. Orbit sizes 1/2/4/8.
     - 3-D mixed Gauss × Lobatto × Radau, n = 2–4. These have non-uniform lifted masses.
     - 2-D Padua, n = 2, 3, 5, 8, 10.
   - On every rule, these all held to <= 3e-11: moments, Σδ = N - D, δ >= 0, E*E = I, Σ η = M - m_n, η >= 0, the row identity, and m <= M <= 2^d·N.
   - Padua scaled lift at n = 10 and 40: exactly 2n(n+1) atoms. Every atom lies in the lattice spanned by (1,0) and (1/2, n/(2n+2)) (error <= 6.5e-11). The minimum periodic nearest-neighbour distance is 0.6985 at n = 40, approaching 1/√2.
3. **Sources.** I read GL v2 pp. 1–3 from the primary PDF text (pdftotext on the downloaded bytes, in their own directory). I read the Marzo math/0611503 and AMO 2101.08064 abstract pages only. I did not read GL's proof, LM, Kolountzakis or Kuperberg; those remain the developer's literature reports.

## Residual risk

- The single external dependency is GL Thm 1.1, a refereed Anal. PDE 2017 result corroborated by Lev–Matolcsi (Acta 2022). Its proof is not inherited, consistent with the E4 label.
- The local argument uses only standard measure theory and Fourier analysis, and I found no step that relies on an unstated estimate.
- The constants are non-effective. The theorem says nothing about finite n, signed rules, exterior nodes (F1), exactness below 2n-2, or interpolation without positive cubature. The files state these limits correctly, except that F1 should be made explicit.
- I make no novelty or priority judgement beyond confirming that the files disclaim priority and credit AMO, Kolountzakis and Kuperberg.
