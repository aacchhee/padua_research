# Focused L3 re-audit: derivative formula, split statuses, and obstruction scope

Date: 2026-11-01. Auditor: independent Codex subagent `/root/audit_l3_certificates`; developer: Claude. Launch requested `gpt-6-astra`, reasoning effort `xhigh`, `fork_turns:none`, as recorded by the orchestrator; no independent runtime confirmation of model/effort is available to this subagent. No developer files or Git state were changed.

Rules read at **50b0d304001b48607527e5086a67045f534d9472**. Scientific candidate: **075d4074017445a0fd4d7443ffac97cd7f8c106b**. Response baseline: **5f523313b7b388cb114103734028f0a850dfeaad**. This is a focused re-audit of the response to audit-01, not a replacement for the unchanged certificate audit. Full source/evidence hashes and commands are in [manifest.json](L3-formula-scope/manifest.json).

## Scoped verdict

**T318's analytic formula and equivalence are confirmed. The original findings LF-M2, LC-M1, LC-L1, LF-R1 and LF-R2 are substantively resolved within this scope.** The general first-order isomorphism remains OPEN (T316); its finite floating rank observations remain MEASURED (T317). The all-degree obstruction radius question is correctly OPEN (T319). The per-degree Padua certificate theorems survive with the same certificate data and analytic proofs.

One new **low** evidence-description correction is requested below (LC2-L1): the new checker does not establish that its randomly perturbed functional has no positive representing measure, so it should not call that functional “non-measure.” This does not invalidate any part of T318, which is proved for every functional with positive-definite moment matrix. No new mathematical blocker was found.

The new developer checker was freshly executed and reproduced its six-case measurements. An independently written exact rational checker passed n=1,2,3 through fixed-basis moment matrices, including arbitrary mass and every moment direction. T302's revised residual conventions and N309 are audited separately by `/root/audit_l3_framework`; no independent verdict on those full new statements is substituted here.

## Coverage and disposition matrix

Reread current `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; response-01 and its impact map; L3 response-audit-01; SPLITS; T316–T319 in full; T301, T304 and T309 at the dependency boundary; relevant baseline-to-candidate diffs for T300/T311/T313/N301/N303, candidates, SUMMARY and report. The full prior reads of `state/IDEAS.md` and `literature/INDEX.md` are reused only after byte-identity verification. No new external literature was consulted or promoted to proof. The original audit-01 report and evidence remain frozen.

| Original finding / changed claim | Disposition in candidate | Independent check and verdict |
|---|---|---|
| LF-M2: unproved T304(c) isomorphism inside a PROVED file | T304 keeps factorization; T316 OPEN; T317 MEASURED; T318 new PROVED reduction; SPLITS records mapping | Correct separation. T318 proves the derivative and algebraic equivalence, not universal injectivity. **Resolved.** |
| LC-M1: decreasing finite lower bounds used to exclude a uniform obstruction radius | T313/N303/T300/SUMMARY/report withdraw the exclusion; T319 distinguishes chosen radius, positivity radius of P_n, and maximal obstruction radius | Correct logical repair. No limit or absence of a uniform radius is inferred. **Resolved.** |
| LC-L1: stale certificate status and rerun pointers | N303 certificate row PROVED; candidates rows 139/145/159 synchronized; T311 eight-value scope and n=1..7 fresh-rerun attribution corrected; T300 split list synchronized | Matches original audit evidence and the completed companion audit's exact equispaced n=1..7 execution. n=8 remains not freshly rerun. **Resolved.** |
| LF-R1 / protocol P4: backward obstruction headline presented as ruling out a finite-precision Greenbaum model | Report §0.3, Rank 1 and L3 theory/summary explicitly restrict to reading (E), retain (G) OPEN, small epsilon and per-degree radius quantifiers | Quantifiers and application scope now match the certificate proof. **Resolved.** |
| LF-R2: report rate theorem paraphrased by nonnegative-annihilator conditions | Report Rank 2 and SUMMARY use S0, S1 and Hessian condition (H); PSD-singular case OPEN | Matches T303. In particular S1 nonzero gives only a square-root lower bound; (H) adds attainability; PD Hessians give a fixed-radius obstruction. **Resolved.** |
| T318(a)–(d), new analytic result | Exact identity, derivative, Hankel-family span, rank criterion | Reconstructed independently below; no missing sign, mass factor, basis-derivative term or dimension hypothesis. **Confirmed.** |
| T317 new finite measurements | Six node sets, one specified weight vector per set, numerical ranks only | Fresh developer execution agrees; no all-n inference. **Confirmed as MEASURED.** |
| T319 routine definitions and finite evidence | rho_n vs delta_obs(n); U1/U2 OPEN; bounds and descriptive slopes separated | Definitions and inequalities hold; focused floating sampling confirms new node-attribution and slope wording. **Confirmed within its OPEN/MEASURED scope.** |
| N301/N303 propagated residual normalization | Bound against L_mu+E unchanged; multiply by s_E for normalized reference | Direct sign-separation calculation verifies this local propagation. Full T302/N309 re-audit belongs to companion report. |

The T311 prior “no independent rerun” wording is correctly replaced by three distinct provenance facts: original reconstruction computation, this subagent's audit-01 log review, and the framework subagent's actual audit-01 execution. This audit does not claim to have repeated the latter computation.

## Independent reconstruction of T318

### 1. Orientation and truncation

Let m be the fixed graded monomial column and let G=L(mm^T), X=L(xmm^T), Y=L(ymm^T). For an orthonormal coefficient matrix C, C^TGC=I and CC^T=G^{-1}. Consequently

`[H_x,H_y] = C^T F C`, with `F = X G^{-1} Y - Y G^{-1} X`.

For any two polynomials p_a,p_b in the chosen orthonormal basis, orthogonal projection gives

`(H_x H_y)_{ab} = L_tilde(xy p_a p_b) - L_tilde(R^x_a R^y_b)`.

Reversing x,y and subtracting gives **R^y_a R^x_b − R^x_a R^y_b**, exactly the sign in T318. Both degree-(2n+2) top forms are xy times the same product of degree-n top forms; they cancel. Thus the result belongs to V=Pi_(2n+1). The extension L_tilde used for the two separate products is arbitrary and disappears from their difference. No positivity or representability assumption on L beyond G positive definite is needed.

The arbitrary-L projection uses only L(f p_c) of degree at most 2n+1. There is no illicit application of the original truncated L to an uncancelled degree-(2n+2) polynomial.

### 2. Square interpolation and the moving orthonormal basis

At a square Pi_n-unisolvent measure with positive weights, evaluation Pi_n -> R^N is a bijection. Orthogonality against every polynomial in Pi_n therefore forces each projection remainder to vanish individually at all nodes. Products of two such remainders have zero value and first derivative there, so s_ab belongs to S1.

The Cholesky/Gram–Schmidt map is analytic on G positive definite. Differentiating L(s_ab(L)) gives E(s_ab)+L_mu(Ds_ab[E]). Every product-rule summand of Ds_ab has an unperturbed remainder factor that vanishes at every node. The second term is therefore zero, including all terms caused by variation of p_a and the projection. The actual nodal measure may evaluate the separate degree-(2n+2) product-rule terms; their sum is the derivative of a V-valued polynomial map.

There is also a direct basis check: at a square measure, F=0 because multiplication in the nodal algebra commutes. Differentiating C(L)^T F(L) C(L) leaves only C^T(dF)C. Both dC terms vanish. Thus a fixed-basis derivative calculation tests the same assertion without differentiating Cholesky numerically.

### 3. Mass normalization

T301(a) defines Phi for arbitrary positive mass and records Phi(cL)=Phi(L). T318 correctly uses that full domain, so E need not be mass preserving. For m=L_mu(1), normalizing to L_mu/m changes the tangent to `(E-E(1)L_mu/m)/m`, while the normalized basis and its remainder products change s_ab to m*s_ab. Since L_mu(s_ab)=0, evaluation of the normalized tangent on the normalized product is still E(s_ab). No extra factor is missing. The radial direction E=L_mu belongs to T and is killed by the derivative.

### 4. Rectangular dimensions, exterior square and Hankel normalization

The degree-n top coefficient matrix U has shape (n+1)x(n+1), is triangular with positive diagonal, and is invertible. The remainder coefficient matrices have shape (n+1)x(n+2): multiplication by y appends the zero coordinate and multiplication by x prepends it. Hence the quadratic-form coefficient matrix C(u,v) is symmetric of size (n+2)x(n+2). With `sym(A)=(A+A^T)/2`, q^T C(u,v) q equals the stated difference of products with no additional factor of two.

For 0<=i<j<=n, C(e_i,e_j) corresponds to

`B_ij(z,w) = (z-w)^2 * (1/2)(zw)^i h_(j-i-1)(z,w)`.

Symmetric matrices perpendicular to every Hankel matrix are exactly those whose symmetric bivariate polynomial B vanishes on the diagonal. Symmetry makes the diagonal factor double. Dividing by (z-w)^2 leaves a symmetric polynomial of bidegree at most (n−1,n−1). Conversely every such polynomial gives an allowed B, so this space has dimension R=n(n+1)/2.

The K_ij=(1/2)(zw)^i h_(j-i-1) have leading symmetric monomial m_(i,j−1), coefficient 1/2, and remaining terms with strictly larger minimum exponent. The bijection (i,j)->(i,j−1) makes their coefficient matrix triangular and nonsingular. For j=i+1 the basis element is the diagonal monomial z^i w^i and its coefficient is still 1/2. Thus the exterior-square map is an isomorphism onto Hankel-perpendicular matrices for all n, including n=1. This proves span{s_ab}=F independently of any unresolved injectivity of C->p_C.

### 5. Rank and the precise equivalence

Let D=dim V=(n+1)(2n+3), N=(n+1)(n+2)/2 and R=n(n+1)/2. The jet matrix has shape 3N x D; D−3N=R. Therefore dim(V*/T)=dim S1>=R, while the target Skew_(n+1) has dimension R. The map from all moment directions is represented by an R x D matrix of coefficients of the s_ab. Its rank is dim span{s_ab}=dim F. Restriction V*->S1* is surjective, with kernel T, so the induced quotient map is the transpose of the R-column map e_ab->s_ab.

It is an isomorphism exactly when `dim S1=dim F=R`. This is equivalent to independent 3N jets, injectivity of C->p_C on the R-dimensional Hankel-perpendicular space, and S1=F. The last condition is redundant if the first two hold but harmless. Independent jets alone do not prove injectivity. T316 retains that hypothesis and correctly leaves the remaining assertion OPEN. T318 does not use the unresolved equality S1=F as a premise of its proof.

## T319 and the preserved certificate conclusions

For compact K_delta, the dual cone is the polynomials nonnegative there. Since the positive nodal measure has strictly positive node weights, a nonnegative polynomial has L_mu(p)=0 iff it vanishes at every node. Compactness of the normalized dual-polynomial slice implies r(delta)=0 iff such a nonzero polynomial exists. This verifies T319's definition of delta_obs via the zero inradius. The property is independent of the positive weights. The supremum phrasing does not assert that the maximal radius is attained.

The prior PD-Hessian certificates imply positive sufficient radii, but establish no asymptotic upper bound. P_n is one available certificate, giving `0<rho_n<=delta_obs(n)` for n>=4. Taking finite running minima of any positive per-degree choices gives a nonincreasing chosen radius. Taking min with 1/n would even give a shrinking choice; neither operation addresses optimality or excludes a positive uniform obstruction radius.

The finite lower-bound table is reused from audit-01. A focused floating reconstruction of only the newly stated sampling attribution confirms that the first sampled negative circle is centered at (j,k)=(1,1) in every listed n=4,...,12. Descriptive fitted slopes are −4.0880940968 (sampled radii) and −8.2848971810 (printed lower bounds). These are finite MEASURED statistics, not asymptotic statements or exact negative-value certificates.

N301/N303 remain consequences of L_mu(p)=0 and E(p)<0 with p>=0 on the chosen K_delta. For every positive representing functional L_nu on K_delta, `(L_nu-(L_mu+E))(p)>=−E(p)`, so the norm separation is at least |E(p)|/||p||_*. Replacing L_mu+E by s_E(L_mu+E) multiplies the negative evaluation by positive s_E. The response's normalization propagation is therefore correct at this certificate boundary. The small-epsilon positive-definiteness restriction and reading-(E) scope remain necessary and are now explicit in the report.

## Actual executions and evidence limits

Working directory for every command: `/workspace/padua_research`. Python 3.12.14, NumPy 2.3.5, SymPy 1.14.0, Linux x86_64. Outputs are retained in the owned evidence directory; the manifest records their SHA-256 identities.

1. `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py`

   Exit 0; [fresh log](L3-formula-scope/developer-t318-rerun.log). All six cases reproduced. Maximum finite-difference discrepancy 2.67e-8; maximum arbitrary-functional identity discrepancy 1.33e-10; node jets at most 6.4e-12. Numerical derivative ranks, F ranks and dim S1 are 1,3,6,10,6,6. Minimum derivative singular values 4.223,9.643,15.36,28.61,12.76,120.8; maximum 6230. These agree with T317/T318 at the stated precision.

   Code review: Cholesky is oriented correctly; the independent projection-by-interpolation route at square measures and moment-coordinate finite differences are implemented consistently. The chosen arbitrary-functional perturbation preserves G positive definite: each matrix entry changes by at most 0.3*lambda_min(G)/N, hence its spectral norm is at most 0.3*lambda_min(G). The script drops the mathematically cancelled top degree after reporting its residual. It prints discrepancies and always returns 0; exit 0 alone is not a verification gate. The numerical output was inspected and compared with the stated tolerances. It is correctly labeled MEASURED, not an exact certificate.

2. `python3 -I topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/independent_t318.py`

   Exit 0; [independent checker](L3-formula-scope/independent_t318.py), [execution log](L3-formula-scope/independent-t318.log): **ALL EXACT ASSERTIONS PASS**. The checker imports no developer or reviewer code and uses exact SymPy rational matrices and separately implemented sparse polynomial arithmetic. It uses fixed monomials and dF directly, rather than the developer's Cholesky finite differences. Rational affine triangular node sets n=1,2,3 have deliberately nonunit masses 6,21,55. It checks every moment coordinate, all remainder node values and jets, sign, top-degree cancellation, low commutator rows, radial cancellation, normalization covariance, the arbitrary-L identity after changing only highest-degree moments, and equality of the derivative and quadratic-generator row spaces. The derivative matrices have shapes 1x10, 3x21, 6x36, with ranks=dim F=dim S1 equal to 1,3,6. Exact finite Hankel basis ranks n=1,...,8 are 1,3,6,10,15,21,28,36, testing the symmetrization factors. These are finite sanity checks; the all-n theorem rests on the analytic proof above.

   The first execution was deliberately interrupted (exit 130) after approximately six CPU minutes in SymPy's generic `J.rank()` at n=3. Its n=1,2 output and interruption status/source hash are retained. The traceback showed no failed assertion; n=3 derivative identities had passed before the rank print. Replacing generic rank elimination by exact `DomainMatrix` elimination yielded the complete successful run above, with identical test cases and identities. This first attempt is not counted as a completed verification.

3. `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/sampling_scope.py`

   Exit 0; [focused floating log](L3-formula-scope/sampling-scope.log). Checks only new sample-center attribution and the two descriptive slopes. It does not rerun the old interval positivity certificates and does not certify signs exactly.

4. Read-only identity/diff checks: `git diff --exit-code 3a9063b84d14ca0a5998378371e27643fde50a29 075d4074017445a0fd4d7443ffac97cd7f8c106b -- state/IDEAS.md literature/INDEX.md` exited 0. The [evidence recorder](L3-formula-scope/record_evidence.py) hashes candidate blobs and worktree files, verifies the old certificate-code/data hashes against audit-01, and records the baseline-to-candidate diff. It performs no Git mutation.

   Actual recorder command: `python3 -I topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope/record_evidence.py`, final exit 0. It confirms **43/44 inspected files identical to the pinned candidate**, all nine original certificate code/data entries unchanged, and only four additions in the full developer/reviewer L3 code/log trees (the T302/T318 new scripts and their logs), with no edits or removals. The one worktree/candidate difference is response-01.md's orchestrator bookkeeping line replacing “the commit adding this file” with the explicit candidate SHA; [exact diff](L3-formula-scope/post-candidate-metadata.diff). The recorder's first strict attempt detected that difference and exited 1; after inspecting the one-line metadata edit, both hashes and the explicit exception were recorded. No scientific candidate change was accepted silently.

Trusted computational dependencies for the new exact checks: Python integer arithmetic, SymPy Rational and exact matrix elimination, and the checker implementation. Floating evidence additionally trusts NumPy/BLAS and is not used to close an analytic proof obligation. The general isomorphism, n=8 equispaced certificate rerun, all-n radius behavior and actual finite-precision Greenbaum reading remain outside the established result.

## New low finding LC2-L1: “non-measure” is not established by the checker

Locations: T318 status row line 36 and Checks line 47; `tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py:173` and printed label at line 191. The code adds small random perturbations to the moment coordinates, maintains positive definiteness, and evaluates the identity. It does **not** establish failure of positive-measure representability on any stated support. Nonzero commutator excludes the same square-support commuting model, not all positive measures with more support points. Indeed positive moment-matrix functionals can be represented by nonsquare measures while their truncated sections do not commute.

Requested correction: use “arbitrary perturbed functional” or “functional not constructed from an explicit measure.” If “non-measure” is intended as a mathematical claim, specify the support and add a separating certificate. This is an evidence-label issue only: T318(a) already applies whether or not a measure exists, and its analytic proof and our exact check do not need nonrepresentability. Severity **low**; no status downgrade of T318 is warranted.

## Hash boundary and retained obligations

New proof T318 SHA-256: `f293c642ff08dd8677a85dc9582daeb07f0f92a391bacab295d9dd4840f56e19`.

New developer checker SHA-256: `8ade3424969a22c2aca1744ce5d8e612117a8c138ddeff9b2e17609d74ce0ea1`.

New developer log SHA-256: `fcc4cc02799253d15a96c531bf93798725e46b3363befa91aaff30839c885e08`.

T316 SHA-256: `8a149eaf2ac262824b82b31147042663420ebab68c79d38d0f447b291d2f7e55`.

T317 SHA-256: `49cf947440ca9e08f3422d563dc47eef836d3649f5dd798505956433f7888bdc`.

T319 SHA-256: `955dbfa15ad4c29d963586ef254bbc75e20d2af6ab8a4cad200264c93d4aaad7`.

The original n=3 certificate-data log SHA-256 remains `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`. The manifest records all other original certificate code/data identities. [The retained diff](L3-formula-scope/original-proof-scope.diff) shows that T312 is unchanged, T313's analytic proof and P_n are unchanged, N301/N303 retain their certificate reduction with scope/normalization/evidence edits, and T311's values are unchanged. No broad Padua certificate suite was repeated. The original all-n unisolvence assumption remains explicit in N303; no new literature acceptance is inferred.

The new theorem is independently checked but remains a developer result for AC's disposition. This report does not allocate final IDs, merge, approve a PR, or claim campaign-wide acceptance.
