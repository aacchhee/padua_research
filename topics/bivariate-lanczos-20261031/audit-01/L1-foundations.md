# Independent Codex audit: L1 foundations and L4

Auditor: Codex, assigned `gpt-6-astra`, xhigh, separate from the Claude developers and reconstructors. Model/effort are the configured assignment; no independent runtime attestation is exposed. Date: 2026-11-01. Rules read at `3a9063b84d14ca0a5998378371e27643fde50a29`. Scientific candidate: `5ccfac223f466a9105450365d8c6c3781ff7d922`. All eight audited theory files and the rerun checker were compared byte-for-byte with that candidate using `git show`; all match. No developer files or Git state were changed.

## Scope and verdict

The audited results are PD-T?bivariate-lanczos-claude-101–106, -108 and -401. The proofs of 101–106 and the L4 theorem withstand reconstruction, subject to their explicit exact-arithmetic, first-order, no-breakdown and product-measure assumptions. The main fixed-order triangular-selection result in 108 is also correct. Its statement needs the explicit selection qualification and normalization below. No high-severity mathematical counterexample was found in this scope. No general loss bound, numerical stability theorem, universal novelty claim, or acceptance of the rest of L1 is supplied by this verdict.

| Result | Scoped verdict |
|---|---|
| 101, coefficient supports and formed columns | Confirmed, under U(n+1) and fixed graded order |
| 102, local relations and defect recursion | Confirmed as first-order bounds plus exact residual identities; no all-orders bound is claimed |
| 103, growing-block Paige identity | Confirmed, including the complex bilinear case; controls only one boundary combination |
| 104, node rows and implicit-operator residual | Confirmed as exact algebra on computed quantities |
| 105, exact product factorization | Confirmed for the idealized propagator; conditional FP transfer remains separate in substance and needs the status disposition below |
| 106, exact omega recurrence | Confirmed; the existing exact-window index correction is necessary |
| 108, normalized triangular selection | Confirmed after the routine statement qualifications F1–F2; literal unrestricted part 3 is too broad |
| 401, commuting-operator band-Krylov obstruction | Confirmed under U(2m+1); affine bound and staggered-start representation also confirmed |

## Findings requiring disposition

### F1 — Medium: state the triangular selection condition in 108(3)

Location: `tracks/bivariate-lanczos/theory/window-recurrence-row-selection-of-jacobi-pencil.md:18`; compare its Proof 3, which already contains the missing condition.

The statement says **any** assignment with a parent of degree one less is another triangular selection with the same exact solution. Degree alone does not ensure either triangular support or a nonzero pivot. For a fixed ordered basis, the selected relation must have last nonzero coefficient at the intended child, with a nonzero coefficient there. An admissible multiplication of the intended leading monomial suffices.

Exact counterexample to the degree-only wording: take the 16 distinct nodes

`(x,y) = (a, c+a/2)`, with `a,c in {-1,-1/3,1/3,1}`,

and uniform positive weights. This set satisfies U(3): an invertible linear coordinate change reduces it to a 4-by-4 product grid, and a polynomial of total degree at most 3 vanishing there vanishes identically. Set n=2. Assign the X-relation of parent `(1,1)` to the target `(2,0)`. The parent has the stated degree one less, but its coefficient at the **later** unknown `(2,1)` is `sqrt(5)/3`, so the selected row is not triangular. The independent checker verifies that value exactly.

Action: replace the degree-only condition with the condition already used in the proof: every selected row has nonzero child coefficient and no later unknown. Specify that changing admissible parents preserves the fixed monomial order and exact basis. The phrase “HL BIT's mirror x ↔ y” should distinguish this from actually exchanging the coordinate ordering: on the same example, the normalized first degree columns of x-first and y-first Gram–Schmidt have overlap `1/sqrt(5)`, so their value vectors are not identical. Their degree spaces agree and their bases are related by an orthogonal change within each degree. This distinction does not refute the fixed-order `mirror` parent rule used in the previous review's code.

### F2 — Low: include normalization in the pencil left-inverse claim

Location: the same file, lines 10–17 and status row at line 35.

The displayed stacked relations are homogeneous. Their matrix C(z) has the nonzero vector p(z), with p0=1, in its nullspace; consequently it cannot have a left inverse as a map on all N_n unknowns. Its rank is exactly N_n−1: the standard selection supplies N_n−1 triangular pivot rows. The invertible L*(z) of 104 additionally contains the row `e0^T`, which is not a homogeneous pencil relation.

For the exact n=2 example above, C(z) has shape 6-by-6 and rank 5 at z=(2/7,−3/8); adjoining `pi0=1` gives shape 7-by-6 and rank 6. At n=1 the homogeneous system has two rows and three unknowns, while the normalized system is square. Thus “overdetermined” also needs the qualification n≥2 for the normalized system.

Action: write the normalized system `[e0^T; C(z)] pi = [1;0]`, or eliminate pi0 and invert the selected coefficient matrix on the remaining unknowns. State `L*(z)p(z)=e0`, and call the normalized system square for n=1 and overdetermined for n≥2. The intended propagator formula and its proof survive unchanged.

### S1 — Status/splitting item for the integrating auditor

Location: `tracks/bivariate-lanczos/theory/product-measure-propagator-factorization.md:37`, with `Split into: none` at line 6 and overall PROVED at line 31.

Part 2′ is a separately labeled CONDITIONAL assertion about the computed propagator, while the substantive exact factorization is PROVED. The final record should follow the repository's split-first rule: retain the proved exact theorem and its ID/status; give the conditional FP transfer its own durable claim if retained as a substantive conclusion, or explicitly reclassify it as a minor routine perturbation observation rather than an additional theorem part. The integrating auditor is consolidating this with analogous mixed-status files. This is not a request to downgrade the exact product theorem.

## Independent proof reconstruction

**101.** Multiplying the parent's leading monomial by the designated coordinate produces the child's leading monomial; every earlier monomial remains earlier. Induction gives positive leading coefficient, uniqueness of the fixed-order Gram–Schmidt basis, and no breakdown under U(n+1). Symmetry moves a coordinate multiplier to the earlier vector: a coefficient vanishes if that product precedes the parent. This gives the stated F and J supports, including the different lower-block cutoffs. Counting retained rows yields 2t−1, 2t and 2t+1. Applying J to an F relation and using JF=FJ gives the implicit-column formula. The use of a basis through degree t+1 is sufficient: J applied to the parent lies through degree t, so the further F product stays through t+1. The real/complex change of orthonormal basis gives the Z/N_k Ritz identification in exact arithmetic.

**102.** Once h and beta are stored, dot-product errors enter their values and are not an extra local residual term. Expanding the coordinate product, vector update and normalization gives the BJ constant in the file to first order; the corrected h bound is required. For MGS, a unit-vector projection decreases residual norm at zeroth order; the first-order normalization deviation and coefficient accumulation are absorbed in the stated generous constant. The two-pass coefficient-sum error must be included, as the existing correction notes. These arguments keep M and the window fixed as u tends to zero and are not rigorous finite-u gamma bounds. Projecting the J-multiplied local relation onto the complement of the next computed span gives the defect recursion; the interleaved projectors cannot be omitted.

**103.** Transposing Q^T A Q gives `CT+cB+Q^T E=T^T C+B^T c^T+E^T Q`. Decomposing T=S+K and C=I+Delta+R+R^T gives the antisymmetric commutator equation. In the lower triangle, RS−SR depends only on entries of R within S's bandwidth; this proves locality. Taking the upper triangle and restoring the lower/diagonal parts gives the stronger matrix identity `RS−SR=Omega−cB`. Contracting with s gives the stated bilinear formula. The norm bounds follow from Frobenius bounds on triangular parts and submultiplicativity. Complex transpose, not conjugate transpose, is essential. Division by `||Bs||` in the explanatory corollary applies only when Bs is nonzero; the undivided inequality remains valid when Bs=0. No norm control on all the new block's components follows.

**104.** The node-row equation is the scalar local relation at that node, with row zero fixing the initial value. Positive beta makes L lower triangular and invertible. The recursive implicit J column has degree support through one degree above its source, by induction; all terms needed on the right are already defined. Applying J to the F relation, substituting `JQ=Q HJ+Cres`, and using commutation leaves precisely the displayed forcing `EF HJ e_parent−Jf`. Projection annihilates the polynomial-coordinate term, giving the defect bound. Square/rectangular arrays can be consistently interpreted through the stated leading-degree restrictions or zero padding.

**105.** Under the explicitly added probability normalization, tensor products of marginal orthonormal polynomials have the correct leading monomials and form the unique graded basis. Multiplication stays on each fixed x-degree F-chain, plus the J initial chain. The second-kind sequence solves the homogeneous marginal recurrence after the initial index and has Casoratian −1; solving the two initial conditions gives `rho^[s]_j=b_s(r_(s−1)sigma_j−sigma_(s−1)r_j)`. Superposition gives the forced solutions. The displayed quadratic-in-n bound is conservative but follows by two triangle inequalities and the row-norm bounds `|r_j(eta_b)|≤1/sqrt(v_b)`. The non-product statement is only a statement about a nonzero cross-chain coefficient, not a universal instability statement. Existing corrections extending the within-degree matrix to include j=0 must govern its reading. Conditional small perturbations do not give exact product factorization for computed coefficients.

**106.** Take the inner product of a local relation with q_l and move the symmetric multiplier to q_l. Substitution of its F relation or implicit J relation proves the identity for every permitted pair, regardless of orthogonality. For an l outside the exact window, both arguments of the propagated Gram term are from earlier degrees; the original stronger degree inequality was false and its existing correction is adequate.

**108.** The standard selected pencil row is the negative of the corresponding L row, and polynomial completeness proves consistency for every z. With pi0 fixed, any triangular selection with nonzero pivots yields the same p(z). This is the corrected, provable form of parts 1–3. The two-relation block construction spans S_n because multiplying all degree-(n−1) polynomials by both coordinates, together with S_(n−1), spans every degree-n monomial. It need not produce the same particular orthonormal basis without an ordering/alignment choice.

**401.** For a band member B after the initial block, `B=span(V)+A B_previous` gives `codim_B(B intersect AB)≤m`. One band cycle increases dimension by at most m. Therefore, if S_m and S_(m+1) both occur, AS_m lies in an intermediate member of dimension less than dim S_(m+1), hence in S_(m+1). Commutation with the two diagonal coordinates forces A diagonal. Since q0 has no zero component, Aq0 gives a degree-(m+1) interpolating polynomial g; multiplying by x^m and U(2m+1) forces deg g≤1. A constant cannot generate enough dimensions. A nonconstant affine multiplier has intersection exactly A S_(m−1), yielding codimension m+1 and contradiction. Padding starts proves the n-start corollary under the stated stronger unisolvence when needed. If S_n is still in the initial start block, m≥dim S_n≥n+1 directly, completing the edge case omitted in the affine corollary's short proof. For orthogonalized staggered starts q_(a,0), the vectors F^b q_(a,0) have leading monomials x^a y^b plus earlier terms, so their triangular span is S_n; raw x^a q0 is not necessary. Fixed finite grids eventually lose U(d); no all-degree obstruction on an arbitrary fixed finite set is asserted.

## Executed verification and provenance

See [manifest.json](L1-foundations/manifest.json) for full source SHA-256, Git blob identities, byte sizes, commands and output hashes. The source files were read directly from the workspace, and their candidate-byte comparisons passed. Commands were run from `/workspace/padua_research`:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I -u tracks/bivariate-lanczos/code/review_L1/rv_exact_checks.py > topics/bivariate-lanczos-20261031/audit-01/L1-foundations/reviewer_exact_rerun.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-01/L1-foundations/check_foundations.py > topics/bivariate-lanczos-20261031/audit-01/L1-foundations/independent_exact.log 2>&1
```

Both completed with exit code zero. Environment: Python 3.12.14, SymPy 1.14.0, NumPy 2.3.5. The historical checker seeds Python's random generator with 31102026. The new checker has deterministic rational/grid inputs and imports no developer or previous-reviewer module. The historical exact checker itself has SHA-256 `be0cbd8a95771f25235c8247a3452ff6d4465662ca56c1b098d9632326cfa63f`.

The historical checker rerun found zero structural violations (385 generic, 55 repeated-coordinate, 164 square-case forbidden entries), zero implicit-column discrepancies, zero Paige-identity discrepancies in five rational real and one complex case, and a nonzero negative control when the bandwidth was deliberately violated. The simulated rational run had zero node/residual discrepancies and zero errors in 155 omega pairs. Product off-chain coefficients vanished exactly; non-product controls did not. Its 50-digit marginal impulse check had maximum error 2.6728e-51; this is high-precision numerical corroboration, not exact arithmetic. Affine codimensions were n+1 for n=1..4; two-line controls demonstrated escape without the required unisolvence.

The independent checker additionally found zero violations in 55 structural entries, exact matrix-level Paige equality with complex S and a dense skew part K, exact residual/node identities, and 39 exact omega-pair equalities. Exact rank checks confirmed the affine and orthogonalized-staggered-start claims at n=1,2. The 108 counterexamples and normalization ranks above were obtained by exact arithmetic. Independent double CGS/ORTH recurrences through degree 8 on a sheared grid and a triangle, with residuals recomputed in long double and u=2^-53, had maximum residual/stated-bound ratios 0.04155, 0.02484, 0.06624 and 0.03505 respectively. These finite numerical ratios corroborate, but do not prove, the first-order constants.

| Artifact | SHA-256 |
|---|---|
| `L1-foundations/check_foundations.py` | `6a0a7e8e6bffd1f6cec7c0e4fdb65d131e3434d6205aef7bdabde58df9f1037d` |
| `L1-foundations/independent_exact.log` | `679164554b7018a1f6a0e4f874669b90c6584ca08003a510bf5033eb804e95ad` |
| `L1-foundations/reviewer_exact_rerun.log` | `01b6a329bd09f4ed329ac3a99716e3366e84e2417a72b5d9a21698c2f730e1e0` |
| `L1-foundations/manifest.json` | `410e2821057205ee3da64540f9cef8c7ad03b1489e2f9326cdf6127a78b95646` |

The checker plus two logs total 15,099 bytes; each is below 1 MB. They are necessary small audit evidence. Root controls any commit. No external archive has been selected; archival remains pending.

## Coverage and limits

Read: AGENTS.md, WORKFLOW.md, CODEX.md; full state/IDEAS.md including all obstruction/disposition rows; full literature/INDEX.md in bounded chunks; topic plan, report and audit handoff; all eight theory files; pertinent L1 candidate records 101–111 and 401 and correction sections; R02/R03; pertinent L1 reconstruction-01 and response sections; recurrence/checker source; the BPS literature record. No new research mechanism was proposed. The novelty gate was used to inspect the existing mechanisms, not to claim priority. Literature comparisons in this report remain repository-source reports: no original PDF or new external literature source was inspected. The cloud runtime skill/status was read; no network work or credentials were used.

Later L1 measured claims, the rational growth certificate 113, claims 110–115, and L2/L3/L5 are assigned to other auditors. Historical timing/MEASURED tables beyond the described reruns were not revalidated here. Small exact tests are discriminating checks of the proofs, not finite reductions proving arbitrary degree. FP overflow, underflow, breakdown, degree-uniform error constants and asymptotic amplification remain outside the established results. The scientific candidate stays unchanged pending developer dispositions of F1–F2 and the integrating auditor's status finding.
