# Internal referee report: exposition and notation (MZ-CC manuscript)

- Referee: Claude Opus 5.5, effort high. Did not write the paper; no manuscript edits, no git state changes.
- Manuscript: `tracks/mz-constants/paper/manuscript.tex` at head d2e8000 (d2e80007686706d8805debf168f4ee389134d55e),
  sha256 6f53026d...; refs.bib sha256 84c81943...
- Build: `tools/build.sh ... /tmp/ref-expo`: 31 pages, no undefined references, no log or BibTeX warnings, no overfull boxes.
- Page map (PDF): Sec 1 pp.1-4 (literature ~1.5 pp.), Sec 2 p.5, Sec 3 pp.7-8, Sec 4 pp.9-13, Sec 5 pp.14-15,
  Secs 6-7 pp.16-17, Sec 8 p.18, Sec 9 pp.19-20, App A pp.20-24, App B pp.25-27, App C pp.28-29, references pp.30-31.
- Line numbers refer to manuscript.tex at d2e8000. Severity: MAJOR (a SINUM referee would ask for a change), MINOR, TYPO.
- I spot-checked arithmetic while reading for exposition (constants in Thms 3.2, 3.4, 4.1, 4.3 cases, 7.1, Prop 8.1,
  Lemma A.1, A.5 assembly, B.1 limits, B.2 identities). I found no mathematical error; findings below are about presentation.

## Overall assessment

The paper reads as a coherent SINUM paper with an accurate abstract. The proved scope matches the theorems, and the
computer-assisted part is labelled in the abstract, Theorem 1.3, Section 5 and Corollary 6.1. The rename pass removed
nearly all harmful clashes in `notation-cc.md`: H1-H9 are applied, and H10 is handled by the note at l.876-878.
Four presentation problems remain that a referee would ask to fix:
(i) the circular Theorem 3.1 / Theorem 3.2 / Corollary 3.3 arrangement;
(ii) the endpoint model in Section 5 is defined before it is explained;
(iii) Appendix B has no roadmap or limit dictionary;
(iv) repository and process language in the data statement and at the end of Appendix C.
After these, about 1-1.5 pages can be cut from duplicated remarks without losing explanation, and about 0.75 page
should be added in Section 5 and Appendix B.

---

## A. MAJOR

**1. MAJOR: Section 3 structure is circular and redundant (Thm 3.1 `thm:upper`, l.462-495; Thm 3.2 `thm:ratio-upper`, l.497-525; Cor 3.3 `cor:ratio-endpoint`, l.527-539).**
Theorem 3.1 states the quantitative bound 2-4/N+4/N^2, but its proof gets that bound from the *next* theorem.
Corollary 3.3 then restates the same display and ends "This proves the endpoint refinement used in Theorem 3.1".
The A=2M-R argument in the proof of 3.1 is the ρ=1 case of the A_ρ argument in 3.2, so Theorem 3.1 adds nothing
that 3.2 and 3.3 do not already give. Remark 3.5 (l.628-639) then derives a weaker, superseded bound.
Fix:
- Make the current Thm 3.2 the first theorem, "Theorem 3.1 (Degree-sensitive upper estimate)". Append to its
  proof: "For ρ=1 the matrix A_1=2M-R is the one used in the qualitative threshold; positivity of Q_N(p^2) follows
  from positive weights and unisolvence on Π_N."
- Make the current Cor 3.3 "Corollary 3.2 (Endpoint upper constant)". Add the positivity statement and "for N=2
  every quotient equals one; for N≥3 the inequality is strict".
- Delete the current Thm 3.1 and Remark 3.5. Keep the observation that Lemma 2.2 is reused in Theorem 3.4 as one
  sentence before Theorem 3.4.
- Update l.130 to "This combines Theorems 3.1 and 3.3 and Remark 3.4" (new numbers) and l.457-460 to match.
- Net effect: about -0.6 page, and one argument instead of two.

**2. MAJOR: The endpoint model (Section 5, l.1035-1074) is defined before it is explained.**
The reader meets ĝ, 𝖬, 𝖰, ω_j, ζ_j and χ_j with no indication of what s, ξ or g stand for. The explanation
("numerator is the limit of ...", l.1065-1074) comes after the definition and is incomplete. The key dictionary
exists only inside proofs in Appendix B (l.1934-1938, 1975-1991):
- s is the rescaled Chebyshev index i/N;
- the coefficients are a_i ≈ g(i/N);
- ξ=Nθ is the microscopic angle;
- the two endpoints x=±1 give the profiles ĝ^±.

Fix: before "For g∈L^2(0,1) put", insert a heuristic paragraph along these lines:
> "Write p=\sum_{i<N}a_iT_i and suppose that the coefficients vary on the scale N, a_i\approx N^{-1}g(i/N)
> with g on [0,1]. Near x=1, at \theta=\xi/N, one has p(\cos(\xi/N))=\sum_ia_i\cos(i\xi/N)\approx\widehat g(\xi),
> and \dd x=\sin\theta\dd\theta\approx\xi\dd\xi/N^2, so N^2\int p^2 near x=1 tends to \mathsf M(g).
> The nodes x_j sit at \xi=\pi j, and N^2w_j\to\omega_j (Appendix B.1), so N^2Q_N(p^2) tends to \mathsf Q(g),
> the term |\widehat g(0)|^2 coming from the endpoint node x_0 (weight N^{-2}).
> Degree at most N-1 means a_N=0, i.e.\ g(1)=0; the functions \zeta_j, which vanish at s=1, are the coefficient
> profiles of the admissible polynomials p_{N,j} below. The endpoint x=-1 gives a second, independent profile,
> and both endpoints are handled together in Appendix B.3."

Then define the model. Add to the "removable singularities" sentence that χ_j(πk)=δ_jk is what makes the
nodal sampling diagonal. In the paragraph after Thm 5.2 (l.1104-1106), 𝖸 and 𝖹 are used before Appendix B defines
them. Either define them there (two displays, from l.1890-1893) or write "with the Laplace-type form 𝖸 and the
compact form 𝖹 defined in Appendix B.2". Length: +0.4 page; I think this is the most valuable addition.

**3. MAJOR: Appendix B (l.1797-2038) has no roadmap, and its two lemmas have no stated purpose.**
B.2 opens with definitions of 𝒱, 𝖸, 𝖹 and two untitled lemmas (`lem:core-dense`, `lem:continuum`). The reader is
not told that:
- 𝖸 and 𝖹 are the limits of the reflected and transition matrices Y_N and Z_N;
- the factor 1/2 in (B.continuum) comes from equal-parity pairs being half of all pairs;
- the second inequality of (eq:continuum) is just the definition of Λ_edge, carried to the closure.

Fix:
- Add at the start of Appendix B: "B.1 proves Proposition 5.1 by explicit profiles of the trial polynomials p_{N,j}.
  B.2 extends the model forms from 𝒱_0 to their form domain 𝒱 and proves the continuum identity
  𝖰=𝖬+½(𝖹-𝖸), the limit of R=M-Y+Z. B.3 proves Theorem 5.2: a maximizing sequence yields weak endpoint
  profiles g^±; Z_N converges because it is compact, and Y_N is controlled by Fatou's lemma because it is positive."
- Add the dictionary as a four-row display or small table:
  - rescaled a^TM_Na → 𝖬(g)
  - a^TR_Na → 𝖰(g)
  - a^TY_Na → ½𝖸(g)
  - a^TZ_Na → ½𝖹(g)

  The coefficient vector is a_i=g(i/N) (i≥1), a_0=g(0)/2, normalized as at l.1936.
- Give the two lemmas titles: "Lemma B.1 (Density of the core)" and "Lemma B.2 (Continuum identity)".
- After Lemma B.2 add one sentence: "The second relation in (B.x) restates Q ≤ Λ_edge M from the definition
  (5.x), extended by continuity."
- Length: +0.3 page.

**4. MAJOR: Repository and process language is visible (data statement l.1452-1467; Appendix C l.2148-2156).**
AC asked for no repository IDs or process words in visible text. Currently visible:
- "evidence", "receipts", "producer", "second checker";
- the internal directory `topics/padua-mz-sharp-constants-20261106/`;
- file names `P4-trial-J512.json`, `P4_rayleigh.py`, `P4-rayleigh.json`, `check-P4-independent.json`;
- `tracks/mz-constants/code/reproduce.py`;
- "A separate reviewer reconstructed the reduction ... obtaining the same verdict", which is an unverifiable
  process claim about an anonymous party inside a proof appendix;
- "the committed code".

Suggested replacement for the data statement (keep AC's placeholders):
> "**Data and code availability.** The code and data supporting this paper are archived at [Zenodo DOI to be added]
> (repository https://github.com/aacchhee/padua_research, commit [to be fixed at submission]). The archive contains
> the exact trial vector of Appendix C, the interval-arithmetic program that produces the enclosures (C.x), an
> independent exact-rational program that recomputes them, their output logs, and the script that computes
> Table 9.1; a README lists the files. All other results are proved analytically."

Replace the last paragraph of Appendix C with:
> "The trial vector, the enclosure program, a second program that assembles the quadratic forms independently in
> exact rational arithmetic (sharing the scalar enclosures), and their output logs are in the archive listed in the
> data availability statement; both programs give the enclosures above. The trusted base consists of the formulas
> of Lemma C.1 and Section 5, the scalar bounds above, exact integer and rational arithmetic, exact parsing of
> binary64 strings, and the archived code."

If AC wants the file list kept, move it into the archive README rather than the paper.

---

## B. Structure, motivation and flow (MINOR)

5. **MINOR. Section 4 opening (l.657-664).** The section starts with the definition of H_s and K_N and gives no
orientation. Insert before "Write H_s": "This section determines λ_-(N,N-1). Theorem 4.1 (weighted cardinal estimate)
and Theorem 4.3 (harmonic witness) fix the order (log N)^{-2} for every N with explicit constants. Section 4.1
identifies the limit π^4/8 by a one-dimensional model near the endpoints; the longer proofs are in Appendix A."

6. **MINOR. Witness motivation (l.766-770).** The sentence "Strictly alternating nodal values with positive amplitudes
would represent a full degree-N interpolant, so we enforce both the degree and the endpoint cancellation explicitly"
is hard to parse. Replace with:
> "Alternating nodal data (-1)^k|v_k| are the natural candidates, but they generally have a nonzero T_N coefficient
> and so do not define an element of Π_{N-1}. The witness below is a combination of U_r of parity N-1. It lies in
> Π_{N-1} by construction, and each term vanishes at both endpoints."

7. **MINOR. Top Chebyshev coefficient, used four times without a common statement** (l.769, l.1071-1073, l.1692-1694,
l.1785 "b_N"). Add to Lemma 2.1 (`lem:identities`) one sentence:
> "The interpolant of nodal data u has T_N-coefficient N^{-1}\sum_k(-1)^k\gamma_k u_k; in particular it lies in
> Π_{N-1} iff \sum_k(-1)^k\gamma_ku_k=0."

Then cite it at the four places. This also justifies "Their two nonzero nodal values cancel the coefficient of
T_N" (l.1070).

8. **MINOR. Section 4.1 heuristic (l.874-888).** This is good, but say why ‖·‖_h is the right norm, which is the
step a reader needs before Lemmas 4.8-4.9: "With g_k=k a_k/N, the CC energy of data supported near x=1 is
\sum_k w_k|u_k|^2\approx\pi^2\|g\|_h^2, since w_k\approx\pi^2k/N^2 (Lemma A.1(a))."
Also write "squared L^2 norm" (l.883, 885); the factors π^2 log N and 2(log N)^3 multiply squared norms.
Add "(made precise in Lemma A.1)" after the heuristic.

9. **MINOR. l.1020-1025** ("Neither lemma uses smoothness, signs or cancellation of the input. The first is where
signs are retained"). "Signs" refers first to the input g and then to the kernel. Rewrite:
> "Neither lemma assumes smoothness or a sign pattern of g. In Lemma 4.8 the signs of the kernel are kept: the pole
> part of Φ_k is summed by the orthogonality (A.1) of shifted sinc functions, whereas estimating the cardinal
> functions in absolute value would lose a factor log N. Lemma 4.9 supplies the leading constant: ..."

Also, the Methods paragraph (l.189) calls this a "discrete Hilbert transform"; add "(the kernel 1/(t-k) in (A.3))"
so the phrase is anchored.

10. **MINOR. One name for V.** "Volterra operator" (l.191) vs "primitive operator" (Lemma 4.7 title, l.890) vs "V"
(l.1025). Use "the Volterra (primitive) operator V" at first use and "V" afterwards. ‖V‖=2/π is classical; cite it
(e.g. Halmos, *A Hilbert Space Problem Book*, Problem 188, or the Wirtinger-type inequality in Hardy-Littlewood-Pólya,
*Inequalities*, Thm. 257) and keep the short proof as "for completeness".

11. **MINOR. Weighted Schur test is stated three times ad hoc** (l.716-720 after its use at l.712; l.1247-1250;
l.1557-1559). State it once as Lemma 2.4:
> "Let B=(B(x,y)) be a nonnegative kernel on σ-finite spaces X,Y, ψ>0 on Y, φ>0 on X. If \int B(x,y)ψ(y)\dd y\le
> Γ_rφ(x) and \int B(x,y)φ(x)\dd x\le Γ_cψ(y), then \|B\|_{L^2\to L^2}^2\le Γ_rΓ_c."

Cite it in Thm 4.1, Thm 7.1 and A.1. This also removes "For completeness ..." and "This proves the stated version
without an interpolation theorem" (l.716-720), which currently comes *after* the inequality is used at l.712-714.

12. **MINOR. Appendix A roadmap.** After the notation paragraph (l.1473-1482), add: "A.1-A.2 prove Lemmas 4.8 and 4.9;
A.3 gives the representation of the interpolant near the endpoints that reduces both directions to these lemmas;
A.4 proves the trial bound (Prop. 4.5) and A.5 the finite reverse bound (4.x)."

13. **MINOR. "Through all integers N"** appears five times (l.136, 151, 915, 935, 1090) as an unexplained idiom.
At its first use write: "as N→∞ through all integers (not only along even or odd N)". Afterwards "as N→∞" suffices,
or keep the phrase now that it is defined.

14. **MINOR. Literature section (l.207-314, about 1.5 pp.).**
- (a) The "Attribution" paragraph (l.209-219) concerns Section 8 and the folded moments of Section 2. Move its
  second half (ASV eq. (7)-(8), the generic upper-Gram mechanism) to the start of Section 8. Rename the heading to
  "Prior ingredients" and replace "established prior algebra" with "classical".
- (b) The bullet "The exact CC evaluation in Lemma 4.2 ..." (l.275-281) is about this paper, not the literature, and
  its phrase "and hence vanishing for every N" is garbled. Delete it; the same point is made at l.766-767.
- (c) Mastroianni-Totik is discussed at l.282-288 and again at l.1172-1175. Keep it in one place; Section 7's
  opening can say "(see Section 1.2)".
- (d) "not known theoretically" is said at l.87-88 and again at l.312-313; delete the second.
- (e) "Nevai's quasi-Lagrange theorem includes the CC nodes" (l.245-246) has no pinpoint. Add the citation
  [LIT-063, Thm. x].
- Saves about 0.4 page.

15. **MINOR. Section 8 repetition.**
- l.1330-1339 repeat the converse-MZ literature and the An-Wu setting already given at l.1298-1302. Keep only:
  "Lemma 4.2 alone gives q_{512}<1/3; the certificate above gives the sharper value needed for the threshold 3/4.
  The pair m=513, n=511 lies in the range n+2≤m≤2n+1 of [46, Cor. 4.1]. We are not aware of a published correction."
- l.1391-1392 ("Using only exactness through N permits ...") is subsumed by k≤min(n,d_N-n). Delete it.
- Section title: "Hyperinterpolation and the three-quarter assumption of An and Wu" is more informative for SINUM.
- l.1298-1299: "An and Wu assume ... in its main theorem. Its Section 4" mixes "they" and "its". Write "[46] assumes
  ... in its main theorem; its Section 4 ...", or use "their" throughout.

16. **MINOR. Duplicate "open" statements.** That the decimal value of Λ_edge is open is stated in the abstract, l.1119-1122,
Remark 6.2 (l.1160-1168) and Section 9. Delete Remark 6.2 and fold its one new point into open problem 2 in Section 9:
the bound (4.x) is coarse and Theorem 5.2 has no rate.

17. **MINOR. Remark after Thm 4.3 (l.863-868).** "vacuous throughout all computationally feasible full-spectrum
calculations considered here" is process-flavoured. Replace with:
> "The constant 128000 serves only to fix the order: 128000/(log N)^2<1 requires log N>357.8. For N in the range of
> Table 9.1 the constant polynomial gives the better bound, and the table does not determine the leading constant."

---

## C. Notation (compared with notation-cc.md after the rename pass)

Applied: H1 (ϑ), H2 (σ_±), H3 (ϖ_j), H4 (ν_θ), H5 (Y, Z at l.579), H6 (W_N), H7 (𝖰, 𝖰_J, C_c), H8 (𝒜, ℬ, 𝒞),
H9 (N_i), M1 (Ω_j, Ξ, Θ^{e,o}), M2 (|μ|), M3 (λ̄), M4 (X_1, X_2), M5 (k^*), M7 (Υ_u, S̄), M9 (Γ_r, Γ_c),
M12 (φ_{N,j}), M13 (𝖬_{ij}). H10 is handled by the in-text note at l.876-878, and κ_2 is now defined (l.168).
Not applied: M4 for the model truncation J, M6 (d_N), M8 (p_N), M10 (c_k, c_i), M11 (t), M14 (K(ϖ)), T13 (u_N).

18. **MINOR (new clash from the rename). σ_± vs σ_N.** σ_N is defined in Thm 4.6 (l.945) and used in A.5 (l.1760, 1793).
σ_± is the support of f in A.4 (l.1687-1710), the adjacent subsection. Fix: put the support in log-scale notation,
supp f⊂(y_-,y_+). This pairs with item 20.

19. **MINOR (new clash from the rename). ν_θ (l.802, Thm 4.3: ⌊1/sinθ⌋) vs ν(t)=|sin t|+1/N (l.1190, Thm 7.1).**
The scopes are different, so this is tolerable, but use ν for one of them only. Suggested fix: write N_θ:=⌊1/sinθ⌋ in Thm 4.3.

20. **MINOR (harmful within one proof). x as the physical variable vs x=log t/L.** In the proof of Prop 4.5 (A.4),
l.1714 has ∫_0^1|P_u|^2 dx with x∈[-1,1] physical, while l.1718 says "after x=log t/L". Lemma 4.7 and Section 4.1
(l.882) also use x for the log scale. Fix: use y for the log-scale variable in Section 4.1, Lemma 4.7 (f(y)=cos(πy/2))
and A.4. y is otherwise used only in App B's Laplace variable, which is a different appendix.

21. **MINOR. S_N (odd harmonic sum, Lemma 4.2, Prop 8.1: S_8, S_57, S_512) vs S_m=\sum_{k≤m}g_k/k (A.2, l.1569-1591)
vs S(t), S^♭ (Lemma 4.9, A.3-A.5).** S_8 and S_m are both "S with an integer subscript" with two meanings.
Fix: rename the odd harmonic sum to H^{\mathrm o}_N=\sum_{j\le N}(2j-1)^{-1}, matching H_s. About 15 occurrences
(l.742-766, 1312-1325).

22. **MINOR. p_N has three meanings:** the harmonic witness (l.784-857), the trial interpolant (Prop 4.5, l.926-930,
A.4) and the maximizer (B.3, l.1972). The first two are in the same section. Fix (M8): call the witness w_N or p^{\mathrm H}_N.

23. **MINOR. J has four meanings:** ⌊N/2⌋ (Thm 4.6), ⌊T⌋ (Lemma 4.9; consistent with the first at T=N/2), the model
truncation (Prop 5.1 "u∈R^J", l.1077; App C J=512) and the dyadic index j in 𝒥_j. Fix: write the model truncation as
m or 𝖩 (Prop 5.1, l.1054-1058, Section 9 l.1433, App C l.2090-2096).

24. **MINOR. u carries five meanings:**
- u_N∈{N,N+1} and an even integer u (Thm 3.4, l.594-602);
- Schur weights u_j=m_j^{-1/2} (Thm 4.1, l.702-719);
- nodal data u_k (Thm 1.2, Cor 4.6, App A);
- model coefficients u∈R^J (Sec 5, App C);
- u=1-i/N (l.1943).

Fix: u_N → N_e (and the dummy u → ℓ or e) in Thm 3.4; Schur weights → ψ_j in Thm 4.1. Keep u for nodal data and
model coefficients (they correspond).

25. **MINOR. t has three meanings in the main text:**
- t=2n/N-1 (Thm 3.2 proof, l.506);
- t=Nθ/π (Thm 4.1, Section 4.1, App A);
- the circle angle with t_j=θ_j (Thm 7.1).

Fix: in Thm 3.2 write ρ^{1/2} instead of t (three occurrences). In Thm 7.1 use θ and θ_j=jπ/N for 0≤j<2N.

26. **TYPO/MINOR. Two symbols for the same quantities.** c_k=1/γ_k (l.681, 1474) duplicates γ_k (l.328), and m_k=1+d_k
(l.425 vs l.1600) duplicates in App A. Write a_kγ_k for a_k/c_k and m_k for 1+d_k, or say once "c_k=1/γ_k" at l.681.
The vector c_i=Q(fP_i) (Prop 8.2, l.1358) is a third c; rename it \hat f_i.

27. **TYPO. u^{l}, u^{r} (l.1655)** denote the parts near x=1 and x=-1. "l" for the right end x=1 is confusing.
Rename them u^{+} and u^{-}, matching g^± in App B.

28. **MINOR. Terminology for Q_N(p^2) vs ∫p^2.** The main text says "CC energy" and "continuous mass" (l.883-884,
l.1065-1066), A.4 says "Discrete energy"/"Continuous mass", and B.1 says "Continuous mass"/"Discrete mass"
(l.1837, 1848). Pick one pair, e.g. "discrete energy Q_N(p^2)" and "continuous mass ∫p^2", define it once in
Section 1 (after (1.3)), and use it in A.4 and B.1.

29. **TYPO. W_N is defined inside a proof but used later.** W_N is defined in the proof of Lemma 2.3 (l.437) and used in
B.1 (l.1852-1855). Define it in Lemma 2.1: "w_j=(2γ_j/N)W_N(θ_j), where W_N(θ) denotes the bracket in (2.2)".

30. **Tolerable, no action needed:** K(ϖ) in App C vs K_N, K(t); 𝒱 vs V; Ω_j vs ω_j; Ξ vs ξ; d_N vs d_k (scopes
disjoint; d_k never appears with index N); M_0 vs M; H(t,j) vs H_s.

---

## D. Undefined or forward-used symbols

31. **MINOR. Π_n is never defined.** It is first used at l.98 and l.100; the abstract says "polynomials of degree at
most n", but the text does not. Add to "Setting": "Π_n denotes the real polynomials of degree at most n; where
complex coefficients are allowed (Thm 4.6) this is said explicitly."

32. **MINOR. l.68-70.** "Let Q(f)=\sum_j w_jf(x_j) approximate a finite positive measure μ" should read "approximate
integration against". Also introduce P_i: "and let G=(Q(P_iP_j))_{i,j} for a real L^2(μ)-orthonormal basis
(P_i) of a polynomial space."

33. **MINOR. Cor 1.4(3) (l.173-178).** k is not quantified. Replace "under the reproduction condition of Section 8"
with "for every 0≤k≤\min(n,d_N-n)". Keep the definitions of 𝓛_n and E_k.

34. **TYPO. App C.** Ci (l.2120) and γ (Euler's constant, l.2128) are undefined, and γ clashes with γ_j. Add
"Ci(x)=-\int_x^\infty\cos v\,v^{-1}\dd v" and write the identity as Cin(x)=γ_E+log x-Ci(x), "γ_E Euler's constant".

35. **MINOR.** 𝖸, 𝖹 are used in Section 5 (l.1105) but defined in App B (see item 2). ‖·‖_2 in Prop 8.2 (l.1345)
should say "the L^2(μ) norm".

36. **TYPO. l.1173.** "the classical algebraic Marcinkiewicz inequality" is fine, but the sampling constant M
(l.283-287) is a further use of M. Write it as M_{MT} or "the constant of [51]".

---

## E. Visible process language (beyond item 4)

37. **MINOR. Visible process wording; each fix is a one-line replacement:**
- l.486 "proving the qualitative threshold without the coefficient floor" → "This proves that Q_N(p^2)<2∫p^2." (goes away under item 1).
- l.720 "This proves the stated version without an interpolation theorem." → delete (item 11).
- l.860 "This covers every remaining N, without an unperformed finite check." → "This covers every remaining N; no finite computation is needed."
- l.1212 "No continuous sampling theorem is assumed." → delete, or "The identity is purely algebraic."
- l.1336 "The finite certificate uses no floating spectrum." → "The proof uses only exact rational inequalities."
- l.1312 "For a short exact certificate at N=512" → "To obtain the sharper bound at N=512".
- l.1405-1411 "The values are measurements" → "The values are floating-point computations".
- Table caption "Measured CC spectra" → "Computed extreme eigenvalues of G_{N,N-1}".
- App C l.2101 "The check encloses" → "The computation encloses".
- Visible "certificate" (Section 1 outline, Sec 8, App C title) is standard for computer-assisted proofs; keep it.

---

## F. Abstract and introduction vs theorems

38. **MINOR. Abstract.**
- (a) "For the Lebesgue Clenshaw–Curtis rule" reads oddly. Use "For Clenshaw–Curtis (CC) quadrature with respect to
  Lebesgue measure on [-1,1], on the N+1 Chebyshev extrema, ...". This also defines "CC", which is used later in the
  abstract.
- (b) "the smallest eigenvalue satisfies (log N)^2λ_min→π^4/8; equivalently, interpolation ... has norm" is not
  exactly equivalent. The interpolation norm is λ_-(N,N)^{-1/2} (Cor 4.7). Write "at n=N-1 and n=N the smallest
  eigenvalue satisfies ...; at n=N this says that interpolation ... has norm ...".
- (c) "all eigenvalues lie below" → "all eigenvalues are at most".
- (d) "the condition number" → "the condition number of G_{N,N-1}".

All quantitative claims match Theorems 1.1-1.3 and Cor 1.4, and the computer-assisted part is labelled.

39. **MINOR. l.88-89.** "This paper answers that question, up to the decimal value of one constant" slightly
overclaims. At fixed ratio the constants are explicit but not sharp (l.182). Write:
> "This paper settles the question qualitatively at every degree ratio below one and sharply, as N→∞, at the endpoint
> degree n=N-1, up to the decimal value of one constant."

40. **TYPO. l.114.** The parenthesis about ASV/An-Wu parameters is needed only in Section 8. Move it to l.1298.

41. **OK.** Theorem 1.2 states 128000/(log N)^2 "for every N≥2" and l.863-868 explains that it is vacuous for
practical N. That is accurate. The intro corollary and Cor 6.1 agree on N≥57.

---

## G. Tables, captions, references, placeholders

42. **TYPO. Table 9.1.**
- Use a leading zero (0.259849025) per SIAM style, and align on the decimal point (siunitx `S` columns or `r`).
- The caption duplicates the last column header; shorten it to "Computed extreme eigenvalues of G_{N,N-1}
  (double precision, rounded)."
- The cross-check at l.1408-1410 covers N≤81 only, not the tabulated N≥40 range beyond 81. Say "as a consistency check
  on smaller cases".

43. **MINOR. Bibliography (siamplain output, `manuscript.bbl`).**
- (a) [LIT-065] Smith: "Erdős–turán" prints in lowercase. In refs.bib write `Erd{\H{o}}s--{T}ur{\'a}n`.
- (b) [LIT-045] is cited as both "the arXiv version" (l.214) and "the published version" (l.312), but there is one
  entry. Add the arXiv identifier (refs.bib's coverage field says arXiv 2601.04708 v1) as a separate @misc entry or
  as a note, and cite each version explicitly. Also check that "252 (2027)" is final; otherwise use "to appear".
- (c) Remove second URLs: arXiv html links in LIT-046 and LIT-056, the arXiv link in LIT-294, and Lubinsky's personal
  PDF link with "%20" in LIT-064. SIAM prints DOIs; one URL per entry.
- (d) LIT-052 (Recent Progress in Inequalities, 1998): add the editor (G. V. Milovanović), the series
  (Math. Appl. 430) and the publisher (Kluwer, Dordrecht).
- (e) LIT-061: "Comptes Rendus de l'Académie des Sciences de Paris" → "C. R. Acad. Sci. Paris". Optionally abbreviate
  all journal names to ISO4 (SIAM copy-editing does this, but a clean submission helps).
- (f) Pinpoint citation style: "Trefethen's Theorem 5.2 and formulas (5.2)–(5.4) ... [55]" → "[55, Thm. 5.2 and
  (5.2)–(5.4)]"; "Chapter 4 of ... [49]" → "[49, Chap. 4]"; "Its Section 4 ... Corollary 4.1 [46]" →
  "[46, Sect. 4, Cor. 4.1]". The literature referee should verify the Trefethen pinpoint.

44. **Placeholders that must remain for AC** (do not remove; list for the submission checklist):
- (1) `\author{[Authors to be decided by AC]}` and `\headers{...}{[Authors to be decided by AC]}` (l.24, 27);
- (2) the thanks footnote "This document is not for submission." (l.27), to be replaced by affiliation and
  **funding** (SIAM requires funding information in the first-page footnote; no placeholder exists yet, so add one);
- (3) keywords and MSC codes (l.55-62). Consider adding 41A05 (interpolation) and 42C05 (orthogonal polynomials);
- (4) commit hash `[to be fixed at submission]` and `[Zenodo DOI to be added]` (l.1456);
- (5) **missing placeholder:** l.1450 "treated in a companion paper" has no citation. Add `\cite{[companion MZ-SP paper, in preparation]}` or a bib stub;
- (6) TeX comments with `PD-T?mz-paper-claude-01` (l.973, 1132, 1377) are invisible but contain "?". Harmless; clean them before arXiv upload, because TeX source is public there.

---

## H. Length

45. **Where to cut (about -1.5 pp. in total):**
- Section 3 merge and Remark 3.5 deletion (item 1): -0.6 p.
- Literature list (item 14): -0.4 p.
- Remark 6.2 (item 16): -0.15 p.
- Section 8 repetitions (item 15): -0.25 p.
- l.433-436 "For example, uniqueness follows from density ..." (standard; one clause suffices): -2 lines.
- l.711 "The harmonic bounds deliberately overcount distances near the endpoints." keep only if it helps; otherwise drop.

Do **not** cut the derivations in A.1 (sinc orthogonality), A.2, A.5 or C.1. They are what makes the constants
checkable, and AC values them.

46. **Where more explanation is needed (about +0.75 p.):**
- Section 5 model heuristic (item 2): +0.4 p.
- App B roadmap and dictionary (item 3): +0.3 p.
- Section 4 opening (item 5) and the ‖·‖_h motivation (item 8): +0.1 p.
- One further point in B.3: the profiles g^± are even/odd combinations of e_N and o_N. Say that g^+ is the profile
  at x=+1 and g^- at x=-1 (because T_i(-x)=(-1)^iT_i(x)), which is why the model has one endpoint and the bound
  sums over ±. One sentence after (B.profile-weak).

Net result: about 30 pages, with a clearer Section 5.
