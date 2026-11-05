# PD-T?lanczos-frontier-codex-L5a — Finite certificates bracketing the optimal obstruction radius

ID kind: PD-T.
Aliases: full first-jet-kernel positive span; finite LP upper certificate; local Taylor lower certificate; G3 verifier reduction.
Split from: finite-certification preparation for original L5 / PD-T075(U2); no U2 conjunct is settled here.
Split into: actual certified finite Padua brackets, if obtained, need their own records/evidence.

## Statement

Fix a finite real algebraic node set Z={z_1,...,z_M} in R², integer D>=2 and V=Pi_D. Put K_t=union_i closed B(z_i,t) and

    Delta(Z,D)=sup{t>=0: some nonzero p in V vanishes on Z
                                      and p>=0 on K_t}.

The supremum is taken in the extended nonnegative reals [0,+infinity], with sup(empty set)=0. This convention covers arbitrary node sets with no nonzero degree-D vanisher; the Padua n3--8 application has positive feasible radii from the stated predecessor certificates.

Let F be a specified subfield of the real algebraic numbers containing all node coordinates, with its real embedding fixed. In the full monomial basis of V let J be the value/first-partial evaluation matrix, and let B have columns an F-basis of ker_F J; d=number of columns. Write s_1,...,s_d for those polynomials and v(w)=(s_1(w),...,s_d(w)).

**Upper certificate.** For U>0, suppose exact finite data specify W={w_1,...,w_q} contained in K_U and real numbers lambda_a>0 such that

    sum_a lambda_a v(w_a)=0,
    rank [v(w_a)^T]_a=d.                                  (U)

Then Delta(Z,D)<=U. If d=0 the same conclusion holds without point/weight data. This bound concerns the entire real polynomial class, not only F-coefficient candidates or a generator subspace.

For any fixed U>0 at which no nonzero p in V vanishing on Z is nonnegative on K_U, a finite certificate (U) exists with every point of the form z_i+h, h in Q², ||h||<U and with positive lambda_a in F. This existence statement supplies completeness of finite positive-spanning witnesses at an infeasible radius; it is not a cost bound for the bounded proposer.

**Lower certificate.** Let L>0 and nonzero p in F[x,y], deg p<=D. Suppose its value and first derivatives vanish at each z_i. Let H_i=Hess p(z_i) be positive definite and choose positive mu_i<=lambda_min(H_i). Write its exact finite expansion as

    p(z_i+(u,v))=one-half*(u,v) H_i (u,v)^T
                           +sum_{a+b>=3} t_iab u^a v^b.

If

    sum_{k=3}^D [sum_{a+b=k}|t_iab|]*L^(k-2)<=mu_i/2
                                      for every i,        (L)

then p>=0 on every full ball closed B(z_i,L), and Delta(Z,D)>=L. One may take mu_i=det(H_i)/trace(H_i)>0. All sums are finite. The lower certificate need not be optimal.

For Padua Z=P_n and D=2n+1, a pair of accepted data sets gives the genuine finite bracket L<=delta_obs(n)<=U of PD-T075. No bracket value, G3 verdict or all-degree limit is asserted in this record.

## Definitions

The first-jet matrix has one row each for p(z_i), p_x(z_i), p_y(z_i), in the complete degree<=D monomial coordinates. A complete kernel certificate is JB=0, rank B=d and rank J=dim V-d, with all ranks evaluated in the specified real embedding of F. For the evaluation matrix A, row a is v(w_a)^T. U and L may be rational dyadics even though nodes, basis entries and dependence weights are algebraic.

For the Padua application use exactly P_n={(cos(j*pi/n),cos(k*pi/(n+1))):j+k even}, j=0,...,n and k=0,...,n+1. Balls are in all of R², not clipped to [-1,1]². The certificate degree is2n+1, not2n or2n+2. It is not assumed that the PD-T065 quadratic-generator image equals the whole first-jet kernel.

## Assumptions

Exact real algebraic arithmetic with an explicitly certified embedding/sign convention. Complete monomial space and full first-jet kernel. Upper data satisfy genuine point membership, strict positive weights and full rank. Lower data include the actual nonzero polynomial, exact jets, PD Hessians and every Taylor term. No finite sample is used to infer positivity between points. For the completeness assertion, rational translations are allowed and U>0. No generic-rank or unisolvence conjecture is assumed.

## Status by part

Overall status: PROVED (written elementary analytic reduction; distinct supplementary Astra high reconstruction and convention impact accepted; required Claude scientific/protocol audit pending).

| Part | Status | Evidence / remaining gap |
|---|---|---|
| Correctness/existence of the stated finite certificate forms | PROVED | Direct proof below; no computational premise |
| Actual Padua n3--8 brackets or G3 trend | OPEN, separate task | No producer/checker execution or finite certificate claimed |

The second row describes the application task, not a weakening or PARTIAL classification of this analytic reduction. Original PD-T075(U2) remains OPEN. Candidate disposition: retained standard finite-cone/local-Taylor variant of saved L5-01 and PD-T059(e); no historical novelty claim.

## Depends on

Elementary finite-dimensional linear algebra, compactness and separating hyperplanes. PD-T075 supplies the exact optimal-radius target, not a proved upper estimate. PD-T058/059, PD-T069 and PD-N020/022 supply context/baseline lower polynomials; no numerical radius or unproved kernel-generator equality is imported. The lower Taylor coefficient-sum criterion is already used by the reviewer code `tracks/bivariate-lanczos/code/review_L3b/padua_delta0.py` cited in PD-T075, and is a known validation component, not a new mechanism. All mathematical certificate implications are proved directly below.

## Checks

This mathematics developer executed no numerical, symbolic or exact scientific run. This is an analytic verifier reduction, not a completed computer-assisted finite bracket. Actual use requires committed exact producer/checker code, small exact certificate data or retrievable manifests, and independent execution. The original prospective implementation is in ideas-l5-continuation.md; subsequent root-delegated technical work has its own g3-methods.md and independent-checks-g3-04.md records and supplies no premise of this analytic proof. The candidate record identifies the existing lower-helper implementation and recoverable n3 polynomial input; reading them is not rerunning them. Only root can delegate code/Git work.

Supplementary [independent analytic review](../independent-checks-frontier-04.md#l5-analytic-finite-certificate-reduction) by distinct Codex `/root/g0_review`, assigned gpt-6-astra high, accepts original input SHA256 `c684b6bbbedc44a8d23730dd9a43ef5aaf75d8f63848c282c4306a2bf20a26ce` and the subsequent empty-set convention/history update at SHA256 `8a43ca4dcf1283fd7b9fcab8a6d0713696daff2167fd8402547b92d7646e84db`. The complete proof and verifier inequalities were preserved. This metadata reports that bounded acceptance without importing any finite endpoint, technical execution, G3 verdict or all-degree result. Runtime model metadata is not independently exposed. Required later Claude audit and original gate-timing disposition remain pending.

## Sources

Full relevant repository predecessor coverage is recorded in ideas-l5-continuation.md. Di Dio--Schmudgen and Blekherman repository records were read as digest-based reports with primary gaps; their theorems are not imported as proof steps. No new primary fulltext or historical-priority claim.

## Proof or evidence

### Full real kernel and upper correctness

Since F is a subfield of R and J has entries in F, its rank over F equals its rank over R: a nonzero minor remains nonzero in the specified embedding, and all larger minors vanish in either field. The exact basis B therefore spans ker_R J with arbitrary real coefficients. This is why a full-kernel check controls every real polynomial in the target class.

If a polynomial p vanishes at the nodes and is nonnegative on K_U with U>0, each node is an interior local minimum, so both first partials vanish there. Thus p lies in the real first-jet kernel and p=sum_j c_j s_j for some real c. At the certificate points Ac>=0 entrywise. Positive dependence gives

    0=lambda^T A c=sum_a lambda_a p(w_a).

Every summand is nonnegative and every weight is strictly positive, hence Ac=0. Full column rank forces c=0 and p=0. If d=0 this follows directly from the local-minimum observation. No admissible nonzero polynomial exists at U, and monotonicity K_U subset K_t for t>=U excludes every larger t. Therefore the supremum of feasible radii is at most U. A negative point for one polynomial has played no role.

### Existence of a finite upper certificate at an infeasible radius

Suppose d>0 and there is no such nonzero polynomial at U. For every unit c in R^d, p_c=sum c_j s_j is nonzero, so some w in K_U has c dot v(w)<0. By continuity, w can be replaced by a point z_i+h with rational h and ||h||<U while preserving strict negativity: interior rational translations are dense in each closed ball. Strict negativity persists for all c' in a neighborhood of c. Compactness of the unit sphere supplies finitely many such points W for which every unit c has c dot v(w)<0 at some w in W.

Consequently zero lies in the interior of conv{v(w):w in W}; otherwise a separating/supporting hyperplane through zero gives a nonzero c with c dot v(w)>=0 for every selected point, contradicting the preceding property. Thus the positive cone of the evaluation vectors is all R^d, and the evaluation matrix has rank d. For each vector v_a choose a nonnegative combination of the selected vectors equal to -v_a. Adding these q relations gives a zero dependence whose coefficient at every a is at least1, so a strictly positive real zero dependence exists.

The equation A^T lambda=0 has coefficients in F and an F-basis of its nullspace by Gaussian elimination. Express the strictly positive real solution in that basis and approximate its real coordinates by rationals. The resulting F-coefficient solution is still strictly positive, since positivity is open. This proves the stated existence. This proof supplies neither a maximal point-grid size nor a bound on reconstruction heights or running time. A finite proposer may fail inconclusively.

### Lower correctness on whole balls

For a real symmetric positive definite2-by-2 matrix H, its positive eigenvalues satisfy lambda_max<=trace(H), so lambda_min=det(H)/lambda_max>=det(H)/trace(H). Thus the proposed mu_i is a valid positive lower eigenvalue bound. PD can be checked by H_11>0 and det H>0.

Let h=(u,v), r=||h||<=L. Since |u|,|v|<=r, the exact finite Taylor expansion and (L) imply

    p(z_i+h)>=mu_i*r²/2
                    -sum_{k=3}^D [sum_{a+b=k}|t_iab|]*r^k
               >=r²*(mu_i/2
                    -sum_{k=3}^D [sum_{a+b=k}|t_iab|]*L^(k-2))
               >=0.

This includes every direction and the ball boundary. At r=0 the value is exactly zero. The polynomial is nonzero and has the permitted degree, hence is admissible at L and proves the lower bound. The calculation is finite and does not rely on sampled directions or an asymptotic Taylor remainder.

## Exact checker contract (prospective, NOT RUN)

1. Reconstruct the exact Padua nodes with certified algebraic coordinates/embedding and verify n, parity, cardinality and D=2n+1. One possible common field is generated by alpha=2cos(pi/[n(n+1)]), with coordinates T_(j(n+1))(alpha/2), T_(kn)(alpha/2). If used, the minimal polynomial, its selected real root and all sign tests must be certified, not inferred from a floating root ordering. Other exact smaller composita are acceptable if their node identities and embedding are independently checked.
2. Build J in the full degree-D monomial basis. Independently recompute rank/kernel or verify JB=0 plus exact ranks dim V-d and d. Do not assume d=n(n+1)/2 or generator completeness. A claimed rank must have exact elimination/minor evidence; tolerances do not count.
3. Upper: read each point's node index and rational translation h, verify ||h||²<=U² exactly, evaluate the complete kernel basis, verify A^T lambda=0 exactly, every retained weight>0 in the real embedding, and rank A=d. Zero proposed weights must be deleted before checking retained rank. Strict positive balance in a proper subspace is insufficient.
4. Lower: read actual p coefficients, verify p!=0 and degree<=D, reconstruct every node jet and local Taylor coefficient t_iab, verify the Hessian PD signs, compute valid mu_i and check the finite inequality(L) at every node. Rational outward coefficient bounds may replace exact absolute values only with explicit inclusion/sign certificates. No printed historical decimal or finite direction sample is acceptance data.
5. Independent checker must execute from the small certificate inputs and frozen source pins, recomputing the algebraic identities/ranks/distances/signs instead of trusting the proposer. Field arithmetic and sign/embedding checks are trusted dependencies to name. Successful endpoints become finite statements only after the code, data and actual independent receipt exist. Failed certificate reconstruction or bounded search is INCONCLUSIVE for the optimal radius.

## Scope

Finite certificate construction/validation for a fixed node set and degree. At Padua n3--8, these are legitimate optimal-radius brackets if accepted data are later supplied. No actual finite value, sharpness, numerical trend, U2 direction, all-degree obstruction radius, or complexity bound is proved. PD-T144's upper estimate for the named rho_n is not an upper certificate here. A lower test using P_n remains only a lower bound on delta_obs.

## Open items

Distinct mathematical check of this reduction is accepted as recorded above. Actual root-delegated n3 producer/checker work, full G3 n3--8 brackets and its original trend/otherwise decision, and later required Claude audit including earlier gate-timing disposition remain separate obligations. U2 and all asymptotic attempts remain blocked by G3.

## History

2026-11-05, Codex `/root/l1_l2`, assigned gpt-6.1-sol xhigh, runtime metadata not independently exposed. Rules/input headbb67c1ee830d468fa33007e15008d5574d00ccf4. Completed source/delta gate before this finite development. Saved positive-spanning proposal was previously an unfinished G0-blocked draft; this record supplies an explicit analytic reduction and exact verification obligations, without claiming any executed bracket. No code, scientific run, Git mutation, final ID or self-audit.

2026-11-05: after distinct Astra high analytic acceptance of input SHA256 `c684b6bbbedc44a8d23730dd9a43ef5aaf75d8f63848c282c4306a2bf20a26ce`, added the reviewer's general-definition hygiene convention sup(empty set)=0 in [0,+infinity]. No proof argument, certificate inequality or Padua application changed. The reviewer was asked to confirm this limited impact; durable review metadata will be linked when available. Actual G3 endpoints/independent execution are separate and are not claimed here.

2026-11-05: distinct reviewer accepted the convention/history update at8a43ca4d; linked the durable section and corrected current pending-review metadata only. No further scientific definition, proof or certificate inequality changed. Original accepted hashes and the earlier history are retained.
