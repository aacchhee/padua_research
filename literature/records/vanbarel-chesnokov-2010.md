# vanbarel-chesnokov-2010 — M. Van Barel and A. Chesnokov, "A method to compute recurrence relation coefficients for bivariate orthogonal polynomials by unitary matrix transformations", Numerical Algorithms 55 (2010) 383–402

- DOI / URL / supplied location: DOI 10.1007/s11075-010-9392-y (printed on the first page). Supplied location: AC local copy, `Downloads\padua\papers\s11075-010-9392-y.pdf` (staged at `/mnt/user-data/uploads/padua/papers/s11075-010-9392-y.pdf`; not copied into this repository). Received 9 December 2009, accepted 23 April 2010, published online 16 May 2010.
- Access and reading date: 2026-10-31.
- Reading coverage: complete full text (all 20 PDF pages read from pdftotext -layout output; Figure 2 (p. 397), Table 1 (p. 400) and Table 2 (p. 401) were checked against the rendered page images; the other figures (Figs. 1, 3–8) were not inspected beyond their captions and axis labels in the text layer). Journal pages are the running page numbers printed on the pages (pp. 383–402); mapping: journal page = PDF page + 382.
- Reader, model and effort: Claude Sonnet 5.5, high (literature subagent).
- Named gaps requiring future re-reading: Figures 3–7 (coefficient decay and least-squares error surfaces) were not inspected; the graphical matrices of the 6 × 6 example (pp. 391–395) lost their markers in the text layer and were not reproduced.

## Extracted published statements

### LIT?bivariate-lanczos-claude-151 — The inverse eigenvalue problem (13)

- Statement in faithful paraphrase: Given complex points ζ_i = (x_i, y_i), X = diag(x_i), Y = diag(y_i), weights w = (w_i) and an ordering scheme, find a unitary Q and upper generalized Hessenberg matrices H_x, H_y such that Qᴴ w = ‖w‖ e_1, Qᴴ X Q = H_x, Qᴴ Y Q = H_y (eq. (13)). With Φ the matrix of values of the orthonormal polynomials at the nodes, the paper identifies WΦ = Q (W = diag(w)), and the recurrence relations are xΦ = ΦH_x, yΦ = ΦH_y (eq. (9)), valid because the (m+1)-st orthogonal polynomial vanishes on the m+1 nodes. For real nodes H_x and H_y are symmetric. The univariate case is eq. (8) (unitary Hessenberg for complex points).
- Hypotheses and notation: discrete inner product (1) with positive weights; distinct nodes; exact arithmetic for (13).
- Page / theorem / equation: eqs. (6)–(9) pp. 387–388; eq. (13), p. 390.
- Reading evidence and limitations: Read in full.
- Relation to campaign claims (no inherited proof status): Same object as plan.md (Q, H_x = QᵀXQ, H_y = QᵀYQ with start vector proportional to √w); the 2010 H_x, H_y are given in generalized Hessenberg form (for real nodes symmetric), not truncated to a band by hand.

### LIT?bivariate-lanczos-claude-152 — Ordering scheme and the structure of H_x, H_y

- Statement in faithful paraphrase: With the graded lexicographic order of monomials, the recurrences for the first polynomials are written as x φ_k = [φ_1 … ] H_x(·,k) and y φ_k = [φ_1 … ] H_y(·,k) (eq. (10)); H_x and H_y are not Hessenberg but "generalized Hessenberg", with fixed sparsity structure determined by the order (eq. (11), displayed for the first six polynomials; the symmetric real-node patterns are shown). The polynomial φ_5 is the first reachable by multiplication both by x and by y, giving two equations; the paper uses the "downside-up" scheme (12) in which vertical arrows are multiplications by y and horizontal arrows multiplications by x (polynomials numbered 1 → 2 → 4 → 7 by x on the bottom row; 1 → 3 → 6 → 10 by y up the left column; etc.). The inductive scheme: for φ_k choose from the scheme (12) whether to use H_x or H_y, take the first unused column of that matrix, and mark it used (and mark the first unused column in the second matrix if φ_k can be obtained from both). The scheme generalizes to more variables by changing the monomial order and scheme (12).
- Hypotheses and notation: graded lexicographic order assumed in the applications; real nodes give symmetric H_x, H_y.
- Page / theorem / equation: eqs. (9)–(12), pp. 388–390.
- Reading evidence and limitations: Matrix patterns in (11) lost their markers in the text layer; the textual description is reliable, the pattern details are not.
- Relation to campaign claims (no inherited proof status): Fixes which of the two sections' entries are formed "by the recurrence" (pivot columns) versus implied; this is the pattern question of L1-Q1 for the 2010 algorithm. The paper does not state the number of nonzeros per column as a function of degree (it cites the √(8d) growth of [16]).

### LIT?bivariate-lanczos-claude-153 — Algorithm 1: point-by-point Givens updating

- Statement in faithful paraphrase: Start with D = [w | X | Y] ∈ C^{m×(2m+1)} (eq. (14)) and apply unitary similarity transformations to reach [Qᴴw | QᴴXQ | QᴴYQ] = Qᴴ [w|X|Y] diag(1, Q, Q) (eq. (15)) with zeros below the pivot positions (i, π(i)), i = 1, …, m. Algorithm 1 loops i = 2, …, n over the added points; for each i it loops j = 1, …, i−1, making the element d_{i,π(j)} zero by a Givens rotation Gᴴ built on the pivot (j, π(j)), then applies D ← GᴴD followed by the similarity D ← D diag(1, G, G); π(j) is a "w/x/y switch" selecting the weight, X or Y part. Each iteration adds one point ζ_i with weight w_i, i.e. changes the underlying inner product. Updating (adding points one by one) is supported; downdating "can be developed similar to [20]" (Van Barel–Bultheel 2001).
- Hypotheses and notation: pivots (i, π(i)) fixed by the ordering scheme; exact arithmetic for the statement.
- Page / theorem / equation: eqs. (14)–(15) and Algorithm 1, p. 391; downdating remark, p. 385.
- Reading evidence and limitations: Pseudocode read as printed; the rotation counts and cost per point are not stated in the paper (no operation count appears anywhere in the paper; see statement 157).
- Relation to campaign claims (no inherited proof status): The "2010 Givens point-by-point updating" of L5-Q1: O(i) rotations for the i-th point by the loop structure printed (my reading of the pseudocode, not an author statement), each acting on rows/columns of D.

### LIT?bivariate-lanczos-claude-154 — The 6 × 6 example and the chase

- Statement in faithful paraphrase: Section 4.2 works out the first six orthogonal polynomials with the downside-up scheme and real nodes, showing the matrix D at each step (pivots marked, zeros created by Givens rotations G_w(1,2), G_w(1,3), G_X(2,3), then for the sixth point G_w(1,6), followed by a left-to-right chase of the nonzeros in the last row through G_X(2,6), G_Y(3,6), G_X(4,6) and G_Y(5,6)). Because of symmetry, two zeros appear in the X part at certain steps. The final matrix elements are exactly the values in the recurrence system (10). In the 5th row there are two pivot positions, corresponding to the fact that the 5th polynomial can be derived either by multiplying by x or by y.
- Hypotheses and notation: real nodes (H_x, H_y symmetric); six points.
- Page / theorem / equation: Section 4.2, pp. 391–395.
- Reading evidence and limitations: The graphical matrices (markers ⊗, ⊕, ∗) are not legible in the text layer; the sequence of rotations is read from the captions.
- Relation to campaign claims (no inherited proof status): Worked instance only; no error analysis.

### LIT?bivariate-lanczos-claude-155 — The pivot remark (choice between two pivots in the 5th row)

- Statement in faithful paraphrase: At the 5th row, where there is a choice between the pivot in the X part and the pivot in the Y part, the ordering scheme (12) prescribes the pivot from the Y part, but "we could also choose the pivot from the X-part"; if the two pivots differ by orders of magnitude, "choosing the larger one may enhance the numerical stability". The element below the pivot position in the 5th row of the X part also becomes zero; the pivot for the 6th polynomial is then marked in the Y part, row 6.
- Hypotheses and notation: real nodes; six-point example; the alternative pivot choice would change the generalized Hessenberg pattern from the one produced by scheme (12), which the paper does not discuss.
- Page / theorem / equation: p. 395 (Section 4.2, last step of the 6 × 6 example; PDF page 13). The paper contains no theorem or numerical test of this heuristic.
- Reading evidence and limitations: Locator correction: the reported p. 392 is wrong; the remark is on p. 395 (p. 392 starts the 6 × 6 example). The phrase "may enhance" is a heuristic suggestion; no experiment on pivot choice, no rule beyond "larger" and no effect on the structure of the output matrices is reported.
- Relation to campaign claims (no inherited proof status): The only published pivot-rule statement for the 2010 algorithm; the campaign's L5 pivot-rule experiments cannot cite it as a result, only as a heuristic that is untested in the paper.

### LIT?bivariate-lanczos-claude-156 — Zero pivot signals an interpolating (vanishing) polynomial; Example 3

- Statement in faithful paraphrase: If one of the pivot elements becomes zero at some step, an interpolating polynomial that vanishes at all points used up to that step has been constructed (p. 389). Example 3: 20 equidistant points on each of two circles of radius 0.15 (centers (0.25,0.25) and (0.75,0.75)) plus 4 further points printed as "the 4 edges of the square" (44 points in all); the first zero pivot appears for the 28th orthogonal polynomial, a polynomial of degree 6, matching the theoretical estimate 2+2+1+1 (two circles, two lines), shown in Figure 8.
- Hypotheses and notation: floating-point detection of a "zero" pivot; the paper does not say what threshold was used.
- Page / theorem / equation: p. 389 (statement); Example 3, pp. 399–400 (Fig. 8, p. 400).
- Reading evidence and limitations: The zero-pivot threshold and the numerical size of the pivot are not stated (reading result).
- Relation to campaign claims (no inherited proof status): Matches HL BIT Corollary 2.2 (statement 103) in the exact case; floating-point rank decision is left unspecified, relevant to the non-unisolvent prefix mechanism in L5-Q1.

### LIT?bivariate-lanczos-claude-157 — Stability and efficiency claims, and absence of analysis

- Statement in faithful paraphrase: The abstract claims the inverse eigenvalue problem is solved "efficiently and in a stable way, using a sequence of Givens rotations", and the conclusions say the numerical examples "illustrate its good numerical stability" and that the algorithm is a basis tool for interpolation and discrete least squares (p. 401). The introduction says that when real points are taken the symmetry does not give a significant complexity reduction because the lower bandwidth grows with the size (p. 385), and that the method, compared with the HL 2D Lanczos method, has "similar efficiency and accuracy" but a different principle and allows adding data points one by one (p. 385). The paper gives no operation count, no backward or forward error bound and no analysis of error growth in the number of rotations or points.
- Hypotheses and notation: claims supported only by the experiments of Section 5.
- Page / theorem / equation: abstract p. 383; p. 385 (introduction); conclusions p. 401.
- Reading evidence and limitations: The absence statements refer to the pages read (the whole paper); this is a reading result, not an exhaustive negative literature search.
- Relation to campaign claims (no inherited proof status): The "claimed accuracy statements" are qualitative; the only quantitative evidence is in statements 158–161. The L5 kill test is not addressed by the source.

### LIT?bivariate-lanczos-claude-158 — Example 1 (orthogonality test) on 5,151 Padua points

- Statement in faithful paraphrase: Padua points of degree δ: m+1 = (δ+1)(δ+2)/2 points on the generating curve γ(t) = (−cos((δ+1)t), −cos(δt)), t ∈ [0, π]; the points are γ(kπ/(δ(δ+1))), k = 0, …, δ(δ+1) (printed with n in place of δ in one place). In Example 1 the N = 5,151 Padua points of degree n = 100 with identity weight matrix are used; with V = WΦ (values of the OPs at the nodes computed from the recurrence relations based on H_x, H_y) and R = |VᴴV − I| (elementwise), Fig. 2 plots max R(1:k,1:k) for k = 10:100:N. Read from the plot (log scale, approximate): the maximum grows from about 2×10⁻¹³ at the smallest k shown to just below 10⁻¹¹ at k = 5,151, rising steeply for k up to roughly 2,000 and slowly afterwards.
- Hypotheses and notation: Matlab, standard double precision; identity weights; the test measures orthogonality of the OP values computed through the recurrence, not Qᴴ Q − I of the transformation matrix.
- Page / theorem / equation: Section 5 intro and Example 1, pp. 396–397; Fig. 2, p. 397 (checked against the page image).
- Reading evidence and limitations: The numerical values are read from a plot (axis ticks 10⁻¹³, 10⁻¹², 10⁻¹¹) and are approximate; the paper does not state a number in the text. No comparison with HL on this problem.
- Relation to campaign claims (no inherited proof status): MEASURED-type source evidence, one node set (Padua, M = 5,151, unit weights), growth of the maximum orthogonality error from the ~10⁻¹³ to ~10⁻¹¹ scale as k grows; the benchmark of L1/L5 can be compared with this printed profile only after the same definition of R is reproduced.

### LIT?bivariate-lanczos-claude-159 — Example 2: least-squares solution on Padua points

- Statement in faithful paraphrase: Using the same basis, the Franke function on [0,1]² sampled at the 5,151 Padua points transformed from [−1,1]²: the LS coefficient magnitudes |c_k| fall to machine-precision size from k ≈ 3,000 (Fig. 3); polynomials of length 1,000, 3,000 and 5,151 have degree 44, 76 and 100; relative LS error surfaces for lengths 1,000 and 3,000 are shown (Figs. 4–5; axis scales suggest errors of order 10⁻⁷ and 10⁻¹⁴ respectively, read from axis labels and approximate); longer polynomials change nothing. For G(x,y) = exp((√(x²+y²))³) the coefficients decay more slowly (Fig. 6) and the relative error for length 4,000 (degree 88) is of the size corresponding to the coefficients (Fig. 7, axis scale ×10⁻¹¹ approximate).
- Hypotheses and notation: Matlab double precision; computed via the same row operations on W f as on w in Algorithm 1.
- Page / theorem / equation: Example 2, pp. 397–399; Figs. 3–7, pp. 397–399.
- Reading evidence and limitations: Error magnitudes are inferred from figure axis labels in the text layer and not from inspected plots; treat as approximate.
- Relation to campaign claims (no inherited proof status): Application evidence; no direct bearing on orthogonality-loss theory.

### LIT?bivariate-lanczos-claude-160 — Example 4 and Table 1: comparison with the HL method (small examples, vpa reference)

- Statement in faithful paraphrase: Both the new method and the HL method (ref. [16]) were implemented in Matlab and run in standard double precision (printed as "standard Matlab precision (32 digits)", apparently a misprint; UNVERIFIED) and in variable-precision arithmetic (vpa, 128 digits) for small examples; the vpa results of the two methods behaved identically. Data sets in [−1,1]²: (a) 15 Padua points, (b) 10 random points (averages over ten runs), (c) 10 points on a circle perturbed by noise of amplitude 10⁻⁴ or 10⁻¹⁰ (ill-conditioned). Notation: Q, H_x, H_y from the new method; U, A, B from HL; subscript s for the vpa results. Table 1 (relative errors, as printed; columns (a), (b), (c) amp = 10⁻⁴, (c) amp = 10⁻¹⁰): Q−U: 1e-15, 2e-15, 2e-12, 3e-6; U_s−U: 4e-16, 6e-16, 3e-12, 1e-6; U_s−Q: 1e-15, 1e-15, 2e-12, 3e-6; H_x−A: 7e-16, 6e-16, 1e-12, 8e-7; A_s−A: 2e-16, 2e-16, 4e-13, 8e-8; A_s−H_x: 6e-16, 6e-16, 7e-13, 5e-7; QᴴQ−I: 1e-15, 9e-16, 1e-15, 7e-16; UᴴU−I: 5e-16, 3e-16, 3e-16, 5e-16. The text notes that the H_x, H_y, A, B matrices did not differ in accuracy for the chosen scheme, so only one of them is shown.
- Hypotheses and notation: sizes 10 to 15 points only; norm type for "relative errors" is not stated in the caption.
- Page / theorem / equation: Example 4 text, p. 400; Table 1, p. 400 (checked against the page image).
- Reading evidence and limitations: Values transcribed from the image. Reading observation: in the most ill-conditioned column the factors Q−U and U_s−Q reach 3e-6 while QᴴQ−I and UᴴU−I stay at the 10⁻¹⁶ level, i.e. orthogonality of the computed basis does not indicate the accuracy of the computed H_x, H_y in this tiny example (M = 10).
- Relation to campaign claims (no inherited proof status): MEASURED-type source evidence only for M ≤ 15; the HL (CGS-with-ORTH) orthogonality UᴴU−I is at 3–5e-16 in all columns, so no loss of orthogonality is visible in HL at this size.

### LIT?bivariate-lanczos-claude-161 — Table 2: polynomial recovery, new method versus HL, and the authors' conclusion

- Statement in faithful paraphrase: Polynomials given as linear combinations of the basis polynomials (coefficient vectors: all ones; uniform [0,1]; uniform [0,100], no significant differences) were sampled at the data points and recovered as LS solutions; relative errors ‖c_comp − c‖/‖c‖ are given for the new method (norm1) and for HL (norm2) (Table 2): 496 Padua points 6e-13 and 1e-14; 861 Padua points 7e-13 and 2e-14; 1,326 Padua points 8e-13 and 4e-14; 105 random points 1e-10 and 3e-11; 496 random points 5e-13 and 5e-14; 36 points on a circle with noise amplitude 1e-2: 6e-6 and 5e-7. The authors conclude that Q, H_x, H_y "have on average a half-digit better precision" in the HL method, "which leads to the whole digit difference in the recovery problem", that both methods treat well- and ill-conditioned problems equally well, and that the slightly lower accuracy of the new method is compensated by its ability to add data points one after another.
- Hypotheses and notation: Matlab double precision; one run per entry as far as the text says (the ten-run averaging is stated for Table 1 only); coefficient and norm conventions as in the text.
- Page / theorem / equation: Table 2 and the text before it, p. 401; conclusions p. 401 (Table 2 and the surrounding text checked against the page image).
- Reading evidence and limitations: Reading observation (my arithmetic on one-digit printed values): the ratio of new-method to HL error is about 60, 35 and 20 for the three Padua sizes (more than the "whole digit" stated), about 3 and 10 for the two random sets, and about 12 for the circle set; over the Padua sizes M = 496 to 1,326 (a factor 2.7) the printed new-method error grows by a factor about 1.3 and the HL error by a factor 4. One-digit values from presumably single runs do not support a growth rate in M.
- Relation to campaign claims (no inherited proof status): The only published accuracy comparison between the Givens method and HL at M up to 1,326; it bears on the L5-Q1 statement (error growth with M) as a datum, not as a rate, and it contradicts a naive "HL grows slower" reading at this range only if the printed values are representative (UNVERIFIED).

### LIT?bivariate-lanczos-claude-162 — Statements about the HL method and about related literature (introduction)

- Statement in faithful paraphrase: Multivariate orthogonal polynomials for a graded monomial order satisfy a matrix form of recurrence, a generalization of the three-term relation (Dunkl–Xu book); "depending on the data points, recurrence relation matrices are block-tridiagonal, see [21]" (Xu, Adv. Appl. Math. 33 (2004)); in the multivariate case the number of nonzero terms in the recurrence grows with the degree, of order √(8d) where d is the number of polynomials generated so far (ref. [16], HL BIT). The method generalizes the univariate and unit-circle inverse eigenvalue approaches (Reichel; Elhay–Golub–Kautsky for real points; Ammar–Gragg–Reichel and Fassbender for the unit circle; Bultheel–Van Barel for vector OPs). Padua points are described as optimal points for total-degree interpolation in 2 variables with Lebesgue constant growing like the log squared of the degree ([5], [6]).
- Hypotheses and notation: informal introduction.
- Page / theorem / equation: pp. 384–385.
- Reading evidence and limitations: Statements are citations of other works; not checked here (the HL part is covered by record `huhtanen-larsen-bit-2002`).
- Relation to campaign claims (no inherited proof status): Links the 2010 paper to Xu 2004 (block-tridiagonal structure for discrete measures), a source to read for the L3 block-Jacobi conditions in the discrete case (not read).

## Search and attribution notes

- Method: pdftotext -layout output read page by page; page headers used for journal pages; Fig. 2 and Table 1 checked against rendered images.
- Reported locator check: the pivot remark is on p. 395 (not p. 392); Tables 1 and 2 are on pp. 400 and 401; the sentence on the "numerical stability" claim is in the abstract and conclusions.
- References bearing on finite-precision or accuracy analysis for this approach, for the orchestrator to chase: [12] Elhay–Golub–Kautsky (record `egk-1991`); [16] Huhtanen–Larsen (record `huhtanen-larsen-bit-2002`); [20] Van Barel–Bultheel, "Updating and downdating of orthonormal polynomial vectors and some applications" (Contemp. Math. 281 (2001) 145–162); [19] Van Barel–Bultheel, ETNA 3 (1995) 1–23; [2] Ammar–Gragg–Reichel, LAA 172 (1992) 315–336 (downdating Szegő polynomials); [1] Ammar–Gragg–Reichel (1991) (inverse unitary QR algorithm); [21] Xu, Adv. Appl. Math. 33 (2004) 615–632; [10] Chu–Golub, Inverse Eigenvalue Problems (2005) (survey). None of these was read.
- Not in the paper: any rotation-count or operation-count of Algorithm 1, any condition number or error bound, any comparison against Householder or CGS2.

## History

- 2026-10-31: record created from a complete reading of the supplied PDF (Claude Sonnet 5.5, high).
