# Response to the internal referee reports on MZ-CC (math: F1-F18; exposition: items 1-46)

Editor: Claude Sonnet 5.5 (high effort). Base: head e7c8bd5 (manuscript.tex sha256 6f53026d..., refs.bib 84c81943...).
Edited files: `tracks/mz-constants/paper/manuscript.tex`, `refs.bib` only. No git state changes. `paper-sp/` untouched.
Result: manuscript.tex sha256 0335fdfa..., refs.bib e38b6745...; build `tools/build.sh ... /tmp/cc-ref`: 32 pages, zero LaTeX/BibTeX warnings, no over/underfull boxes, no undefined references. Diff: `/home/claude/mzwork/cc-referee.diff` (against HEAD).

## Numbering changes (before -> after), by label

| label | before | after | cause |
|---|---|---|---|
| thm:ratio-upper | Thm 3.2 | Thm 3.1 | section 3 restructure |
| thm:upper (kept as second label of the corollary) | Thm 3.1 | Cor 3.2 | merged into cor:ratio-endpoint |
| cor:ratio-endpoint | Cor 3.3 | Cor 3.2 | restructure |
| thm:five-thirds | Thm 3.4 | Thm 3.3 | restructure |
| rem:sign-boundary | Rem 3.6 | Rem 3.4 | restructure (old Rem 3.5, unlabelled, deleted) |
| sec:sharp-min | 4.1 | 4.2 | new subsection 4.1 |
| sec:order-min | (new) | 4.1 | F10 |
| lem:schur | (new) | Lemma 2.4 | exposition 11 (last item of section 2, no other number moves) |
| app:edge-fixed / app:edge-continuum / app:edge-limit | (new) | B.1 / B.2 / B.3 | subsection labels for cross-references |

No other theorem-like number changed. Equation numbers moved only in section 2 (new (2.3) = eq:topcoeff shifts eq:mass, telescope, floor, rowfloor, weightcomp by one) and section 3 (eq:RMHK 3.2 -> 3.1, eq:full 3.3 -> 3.2); the equation label `eq:zentry` (inside the deleted proof of old Thm 3.1) is gone; it was never referenced. Section 1 pointer text updated: "This is Theorems 3.1 and 3.3, Corollary 3.2 and Remark 3.4." All other cross-references are `\ref`-driven.

## Mathematics report

- **F1 Accepted.** Replaced the Prop 5.3 paragraph by the referee's wording (values 1.00443692, 1.00443695, 1.00443697 for J = 512, 1024, 2048; "still increase"; no digit beyond the certified bound claimed). Section 9 now adds "(and 1.0044369671... on zeta_1..zeta_2048, so the value for 512 is not converged)". The model truncation is now written `\mathsf J` there (see F15).
- **F2 Declined (orchestrator).** The 23/15 strengthening is not made. "Not sharp" said of 5/3 is replaced: section 1 now reads "We do not claim that the constants 5/3 and C_* are optimal" (C_* included for symmetry), and after Thm 3.3 "We do not claim that 5/3 is optimal; its point is that it is uniform in N...". The remark beta_N -> 1/2 giving limsup lambda_+(N,N-1) <= 3/2 is kept. **Candidate for a future registered claim:** referee's observation beta_N <= 8/15 for N >= 3 (max at N = 4), lambda_+(2,1) = 1, hence sup_N lambda_+(N,N-1) <= 23/15, and with min{1+rho, 1+beta_N} for N <= 8 even 95/63; consequences 1/3 -> 7/15 in Cor 6.1, 1+sqrt(23/15) < 2.2385 in (8.4), threshold (1+sqrt(8/15))/2 in (8.3). Not in the paper.
- **F3 Accepted.** Abstract now states: for n<N all eigenvalues lie in (0, min{1+rho_{N,n}, 5/3}] with rho = max{2n/N-1,0}^2, strictly below 1+rho when n>N/2, "whereas the largest eigenvalue exceeds two at n=N" (replaces the unclear "bound two fails").
- **F4 Accepted.** Abstract: "At the endpoint degrees n=N-1 and n=N the smallest eigenvalue satisfies...; at n=N this says that interpolation ... has norm ...".
- **F5 Accepted.** After (5.2) a sentence says Lambda_edge is the squared norm of the sampling map g -> (ghat(0), omega_1^{1/2} ghat(pi), ...) from V_0 (normed by M^{1/2}) to l^2, which by Lemmas B.1, B.2 extends continuously with the same norm to V. No new operator symbol introduced (all letters are taken). "Squared norm" in abstract, Thm 1.3 (already), section 5 intro.
- **F6 Accepted, recomputed.** K_N/(log N)^2 -> 32 pi^2 (pi+1)^2 = 5417.3 (K_{10^6}/log^2 = 5440). Gap = 128000 * 5417 ~ 6.9e8, so section 4.2 now says "differ by a factor of about 7*10^8 (here K_N ~ 32 pi^2 (pi+1)^2 (log N)^2, against 128000)".
- **F7 Accepted.** Section 1 bullet: "... = O(1/log N), hence lambda_-(N,N-1) -> 0 along all N, not only along a subsequence."
- **F8 Accepted, verified.** K_N is increasing (h_N and H_{floor(N/2)+1} increase), K_2 = 10232.7 > 3, so K_N^{-1} < 1/3 always. Cor 6.1 now reads K_N^{-1} <= 1-eta_N <= min{1, 128000/(log N)^2}; the proof states "K_N is increasing in N and K_2 > 10^4, so K_N^{-1} < 1/3".
- **F9 Accepted** by the restructure: old Remark 3.5 deleted (nothing referenced it; Lemma 2.2 stays, used in Thm 3.3 and Appendix B); the sign-boundary remark now speaks of "the signs of A_rho" in the proof of Thm 3.1.
- **F10 Accepted.** New `\subsection{The order of magnitude}` (4.1) before Thm 4.1, with a short section 4 opening (exposition 5); "sharp constant" is 4.2. Lemma A.1 (lem:endpoint-rep) gets the title "Endpoint representation of the interpolant" and the new Appendix A roadmap says explicitly that section A.3 contains Lemma A.1.
- **F11 Accepted, checked against code.** `interval_dyadic.taylor_integral` stops when ratio <= 1/2 and 2*(next term) <= 2^-128 (TAIL_BITS = 128). Appendix C bullet and the Laplace remainder note (< 2e-22 at 16 pi, dominating widths) added as proposed.
- **F12 Accepted.** Prop 8.2: compact domain Omega, f in C(Omega); also "||.||_2 is the L^2(mu) norm" (exposition 35).
- **F13 Accepted.** Both places say "yields no explicit information beyond [exactness]"; the sampling constant is named M_MT (exposition 36).
- **F14 Accepted (optional).** "each k lies in at most three sets J_j (we use the weaker bound four below, which only enlarges the constants)"; constants unchanged (switching to three would cascade into 80, sigma_N, tau_N).
- **F15 Partly accepted.** Done (all trivial and local): sigma_pm of A.4 -> y_pm; nu_theta of Thm 4.3 -> varkappa_theta; u_N and dummy u in Thm 3.3 -> N_e and m; Schur weights u_j -> psi_j; model truncation J -> sans-serif J (section 5, Prop 5.1, section 9, App C); c_i of Prop 8.2 -> fhat_i; witness p_N of Thm 4.3 -> fraktur p_N. Not done (scopes disjoint, non-trivial): K, H, delta, I/K(varpi) in Lemma C.1, u in Lemma B.2, M_0.
- **F16 Accepted** by the restructure (Thm 3.1 degree-sensitive first with proof; Cor 3.2 absorbs old Thm 3.1's statement including N=2 exactness and strictness for N>=3, and old Cor 3.3; positivity of Q_N(p^2) moved to the corollary proof; label `thm:upper` kept as second label of Cor 3.2 and no longer used in text).
- **F17 Accepted.** "their main theorem ... Their Section 4".
- **F18 Accepted.** "squared L^2 norm" in the section 4.2 heuristic.

## Exposition report

1. **Accepted** (orchestrator's order, not the referee's): see numbering table. Thm 1.1 pointer now cites Thm 3.1, Cor 3.2, Thm 3.3, Rem 3.4. The superseded 2-2/(pi N) remark deleted; Lemma 2.2 kept.
2. **Accepted.** Heuristic paragraph inserted before the endpoint model (referee text, with ghat defined inline); sentence that chi_j(pi k) = delta_jk makes nodal sampling diagonal; pointer for Y and Z to Appendix B.2.
3. **Accepted.** Appendix B roadmap, four-line dictionary (`gather*`), lemma titles "Density of the core" and "Continuum identity", the sentence after Lemma B.2, and the g^+/g^- sentence after (B.profile-weak).
4. **Accepted.** Data statement rewritten (archive, trial vector, interval program, independent exact-rational program, output logs, Table 9.1 script, README); no repository paths or file names remain. **Deferred to orchestrator/AC:** the archive README must list the files formerly named in the text: `P4-trial-J512.json`, `P4_rayleigh.py`, `interval_dyadic.py`, `P4_check_grouped.py`, `P4-rayleigh.json`, `P4-grouped-check.json`, `check-P4-independent.json`, `tracks/mz-constants/code/reproduce.py`. End of Appendix C replaced; "a separate reviewer..." removed. The new sentence "Both programs pass the exact comparison with 10044369/10^7, and their enclosures overlap; an independent re-run of the second program reproduces the verdict" is supported by the receipts `P4-grouped-check.json` and `check-P4-independent.json` (finite_threshold_pass True, producer_enclosure_overlap True).
5. **Accepted.** Section 4 opening.
6. **Accepted.** Witness motivation rewritten, citing (2.3).
7. **Accepted.** New (2.3) = eq:topcoeff (T_N-coefficient N^{-1} sum (-1)^j gamma_j u_j, derived in the proof of Lemma 2.1) cited at the witness remark, section 5 (p_{N,j}), A.4 and A.5.
8. **Accepted.** Weights/harmonic-norm sentence, "squared L^2 norm", "made precise in Lemma A.1".
9. **Accepted**, including "(the kernel 1/(t-k) in (A.3))".
10. **Partly accepted.** "Volterra (primitive) operator V" at first use, lemma title, and "V" afterwards; ||V|| = 2/pi called classical. **Deferred (literature):** no Halmos/HLP citation added because no verified reference or pinpoint is on file.
11. **Accepted.** New Lemma 2.4 (weighted Schur test, with proof), cited in Thm 4.1, Thm 7.1 and A.1; the old "for completeness" text and the "without an interpolation theorem" sentence are gone. In A.1 the kernel's row sums are at most 1/3+1/2 and column integrals 1/3, so norm^2 <= 5/18 < 1; the claim "norm at most one" is unchanged. **Please include Lemma 2.4 in the next audit.**
12. **Accepted.** Appendix A roadmap.
13. **Accepted.** Defined at first use (Thm 1.2); later occurrences kept.
14. **Partly accepted.** (a) heading renamed "Prior ingredients", "classical"; the move of text to section 8 declined (it removes no content but changes flow; left to AC). (b) garbled phrase fixed (cf. F7), bullet kept. (c) declined: both mentions of Mastroianni-Totik kept, wording fixed (F13). (d) second "not known theoretically" sentence deleted. (e) pinpoint `\cite[Thm.~6]{LIT-063}` added from `literature-mz-paper.md` (row 10: Thm 6, p. 695; read at text-extraction level, page-image check still open there).
15. **Partly accepted.** Section title "Hyperinterpolation and the three-quarter assumption of An and Wu", "their" throughout (cf. F17), redundant restatement of Cor 4.1 merged, subsumed sentence "Using only exactness through N permits..." deleted, "For a short exact certificate" reworded; analogies and [LIT-299] sentence kept (explanation).
16. **Declined.** Remark 6.2 kept (its label `rem:rate` unreferenced but it carries explanation; skipping cuts that remove explanation). Deferred to orchestrator if a cut is wanted.
17. **Accepted.** Reworded remark after Thm 4.3.
18. **Accepted** (sigma_pm -> y_pm). 19. **Accepted** (varkappa_theta). 20. **Accepted** (log-scale variable is y in the heuristic, Lemma 4.4 and A.4).
21. **Declined.** S_N vs S_m: not introduced by the rename pass, about 15 occurrences; deferred.
22. **Accepted** (witness -> fraktur p_N, local to Thm 4.3).
23. **Accepted** (model truncation sans-serif J).
24. **Partly accepted** (u_N -> N_e, Schur weights -> psi_j; the u = 1 - i/N of B.2 left, local).
25. **Partly accepted.** t removed from Thm 3.1 (sqrt(rho)); Thm 7.1 left (local, circle variable, many occurrences).
26. **Partly accepted.** "(c_k = 1/gamma_k)" stated at first use; c_i of Prop 8.2 -> fhat_i; m_k vs 1+d_k left.
27. **Accepted** (u^+, u^-). 28. **Accepted** (definition "discrete energy" / "continuous mass" in section 1 Setting, used in sections 4.2, 5, A.4, B.1). 29. **Accepted** (W_N defined in Lemma 2.1). 30. No action.
31. **Accepted** (Pi_n defined in Setting). 32. **Accepted.** 33. **Accepted** (Cor 1.4(3): f in C[-1,1], 0<=k<=min{n, d_N-n}). 34. **Accepted** (Ci, Euler's constant gamma_E). 35. **Accepted** (cf. items 2, F12). 36. **Accepted** (M_MT).
37. **Accepted**, every listed replacement (l.486 disappears with the restructure; l.720, 860, 1212, 1336, 1312; "floating-point computations"; table caption; "The computation encloses"). "Certificate" kept. Outline "lists computed values and open problems".
38. **Accepted** (a)-(d). 39. **Accepted** (softer sentence). 40. **Accepted** (parenthesis removed from Setting; section 8 now says m = N+1). 41. OK.
42. **Accepted.** Leading zeros, `r` columns (decimal alignment), shorter caption, "consistency check on smaller cases".
43. (a) accepted (`{T}ur{\'a}n`); (b) accepted: LIT-045 stays the published entry, `note = {arXiv:2601.04708}`; **deferred to AC:** confirm "252 (2027)" is final; (c) accepted (URLs removed from LIT-046, 056, 294, 064; LIT-061 keeps its single URL as the only locator); (d) **deferred (literature/AC):** editor, series and Kluwer imprint of LIT-052 are not verified (the literature note says verify first; Crossref unreachable from this sandbox); (e) LIT-061 abbreviated "C. R. Acad. Sci. Paris", ISO4 abbreviations of other journals skipped; (f) accepted for LIT-055, 049, 046, 063.
44. **Placeholders untouched** (author/thanks, keywords/MSC, commit hash and Zenodo DOI). **Deferred to AC/orchestrator:** funding placeholder (SIAM first-page footnote), citation for "companion paper" (needs the MZ-SP title; a bib stub should be added once paper-sp settles), MSC additions 41A05/42C05, `PD-T?mz-paper-claude-01` TeX comments to clean before arXiv upload (all `% IDs:` comments are public in the TeX source).
45. **Partly accepted.** Merge/delete in section 3, deleted duplicates in 1, 8; uniqueness aside trimmed to one clause (Lemma 2.3 proof). Net page count +1 (32) because of the added material (heuristic, roadmaps, Lemma 2.4, dictionary).
46. **Accepted** (all four additions).

## Items for the next audit

New or restructured material: section 3 (Thm 3.1 proof rewritten with sqrt(rho); Cor 3.2 merged statement), Lemma 2.4 and its three applications, eq:topcoeff, the section 5 sampling-map sentence and heuristic, Appendix B dictionary, F6 constant (about 7e8), F8 (K_2 > 10^4).
