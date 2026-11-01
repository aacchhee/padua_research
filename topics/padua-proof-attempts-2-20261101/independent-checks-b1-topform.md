# Independent B1 lower-leakage/top-form module

2026-11-01. Codex subagent `/root/a2_independent_route`, requested gpt-6.1-sol xhigh; serving metadata is not separately exposed. Root started B1 at16:35:09UTC, ceiling18:35:09UTC. This worker owns **only this new receipt**. Lead `/root/a5_n4` owns the attempt/theory/code; `/root/a5_checker` owns the main independent B1 assessment. No mathematical computation or source execution is used below. Administrative reads/hashes are provenance only. This is supplementary proof development/reconstruction, **not the required Claude audit**.

## Gate and inputs actually read

Current rules remain d8b878b348a94575e7753e5a756d969d41d5bca8; its only change was the already-read repository-only results paragraph. WORKFLOW SHA256a8927be27a1fe8166e5bcf59c7da8e70618ae0a5f17d56131724baffdad49353. The registry SHA2564a7f365d0932048d4e861a817e758077f9c715c936d2191b1c2a5da63d14d0bb is byte-identical to this worker's complete783-line A4 reading and B3 refresh. That own reading covered every heading/identifier/alias/summary and all obstruction/disposition tables, including the MZ additions; B3 reread all obstruction tables and current programme/MZ dispositions. Before the B1 argument refreshed rational/pole/window/top-form/gauge/project-two/constrain-one/pole-cancellation synonyms and the target-specific full shortlist. No unrelated table or other agent's source reading is promoted into a theorem.

Read the full user request and B1 hypothesis list, FULL b1-input-preparation.md, FULL Part1 attempts/T-B1-optional.md, FULL decisive-gen1-3.md and adversarial-gen1-3.md, FULL programmeIDEA03/IDEA192, and FULL programmeN02/PD-N040. Read window_exact.py's actual algorithm and the relevant line/basis/pole-factory definitions in orf2d.py. These source code reads were not executions; the historical 'exact blocks' diagnostic uses double QR/SVD and remains MEASURED. The general source top-form/gauge/parity ranks are conditional, not inherited proofs. literature/INDEX.md was searched before source-attribution remarks; no external page, PDF or primary ORF book was opened.

Closest registered problem is precisely B1/IDEA192. The existing negative rejects tested floating window implementations, not the exact extraction identity. Part1's closure obstacle is retained: division by a fresh pole does not generally preserve an older rational space. The following argument uses an exact quotient/restriction map instead of assuming that closure. Verdict: completion of the registered target for one stated pole class, no novelty/priority claim. Lead registered T-B1 and its class before the mathematical run; there is no numerical rank premise here.

## Precise class and standing hypotheses

Fix a finite T>=2, M real nodes z_i=(x_i,y_i) in[-1,1]^2 and strictly positive weights omega_i. Assume evaluation is injective on Pi_(T+1); in particular M>=dim Pi_(T+1). Work with the real bilinear weighted inner product `<f,g>=sum_i omega_i f(z_i)g(z_i)`.

Choose the Ldiag class

`ell_j(x,y)=x+y-a_j`, `a_j>2`, `1<=j<=T+1`.

Distinct offsets may be imposed for the final general-position statement; coalescent offsets are temporarily allowed as a rank witness. Multiplying the source's normalized diagonal lines by fixed nonzero constants changes none of the rational subspaces or span/projection conclusions. The source's particular taper/order is not silently identified with every independent offset tuple.

Let pi_0=1, pi_j=product_(s=1)^j ell_s, V_j=Pi_j/pi_j and W_j=V_j orthogonal-difference V_(j-1), with V_(-1)=0. All denominators are nonzero on the nodes and every ell_j is strictly negative there. The spaces are nested because multiplying an old numerator by ell_j increases its degree by at most1. Injectivity gives dimW_j=j+1. Rational vectors and their unique formal numerators are identified only using this stated injectivity.

For2<=t<=T put k=t-2, ell=ell_(t+1), a=a_(t+1),

`C_t=(W_(t-1)+W_t+xW_t+yW_t)/ell`,

`R_t=(I-P_(W_t)-P_(W_(t-1)))C_t`.

Every candidate and remainder lies in V_(t+1). No full-window generation assertion is assumed.

## 1. The exact lower-block quotient

Use affine coordinates S=x+y,U=x-y. For q inV_k write q=P(S,U)/pi_k(S), degP<=k, uniquely. Define

`rho_a(q)(U)=P(a,U)`, a polynomial of degree at most k.        (1)

This map is onto: use numerators independent of S. For k>=1 its kernel is exactly

`{ ell*Q/pi_k : Q inPi_(k-1) }`,                            (2)

by polynomial division in S. For k=0 it is the zero kernel.

Let f inC_t have a representation

`f=(u+v+xw+yz)/ell`,

with u inW_(t-1) and v,w,z inW_t. If q=ell Q/pi_k belongs to(2), then real multiplication/cancellation gives

`<f,q>=<u+v+xw+yz,Q/pi_k>=0`.                              (3)

Indeed Q/pi_k is inV_k and orthogonal to u, while xQ/pi_k and yQ/pi_k still lie inV_k (their numerator degree is at most k), hence inV_(t-1), and are orthogonal to w,z inW_t. The same is true for v. For r=(I-P_Wt-P_W(t-1))f and any q inV_k, `<r,q>=<f,q>` because those two removed blocks are orthogonal toV_k. Thus every r inR_t annihilates the kernel(2).

Consequently there is a **unique** linear functional lambda_r on the(k+1)-dimensional space of univariate polynomials degree<=k for which

`<r,q>=lambda_r(rho_a(q))` for every q inV_k.               (4)

An explicit right-inverse formula is

`lambda_r(p)=<r,p(U)/pi_k(S)>`.

Uniqueness follows from surjectivity of rho_a. It is independent of any nonunique representation of f. This is the exact lower-block leakage functional: all dimV_k old coefficients are encoded by only k+1=t-1 numbers. The argument does not invoke the failed closure q/ell in an older space.

## 2. Homogeneous pole-line top forms and the source's top forms

To make the top-form bridge precise, homogenize P to total degree k:

`P^h(S,U,H)=H^k P(S/H,U/H)`.

Define its restriction to the projective new-pole line S=aH by

`E_(k,a)(q)(U,H)=P^h(aH,U,H)`.                            (5)

This is a homogeneous binary degree-k form. It is exactly the homogenization of rho_a(q), with dimension k+1; it is not merely the highest-degree part of P at infinity. Equation(4) equivalently defines one functional mu_r on these binary forms with

`<r,q>=mu_r(E_(k,a)(q))` for q inV_k.                      (6)

For a lower block q inW_j,0<=j<=k, write q=p_j/pi_j and homogenize p_j to degree j. Conversion to the common denominator pi_k gives the explicit all-block formula

`E_(k,a)(q)=[product_(nu=j+1)^k(a-a_nu)]*H^(k-j)*p_j^h(aH,U,H)`,

so

`<r,q>=mu_r([product_(nu=j+1)^k(a-a_nu)]*H^(k-j)*p_j^h(aH,U,H))`.       (7)

This is a precise top-form expression for every lower-block coefficient. Distinct offsets make the displayed scalar factors nonzero; the identity also holds at coalescence, where some vanish. It does not assume the source sketch's more restrictive infinity-top-form/gauge formula or its unproved skew ranks.

There is also a literal bridge to the source's highest-degree numerator form. Let `Top_j:W_j->H_j(S,U)` send p_j/pi_j to the homogeneous degree-j part of p_j. It is an isomorphism for **every** admissible Ldiag tuple, not merely generic tuples. If the degree were<j, then ell_j*q=p_j/pi_(j-1) lies inV_(j-1), and

`0=<q,ell_j*q>=sum_i omega_i ell_j(z_i)q(z_i)^2`

forces q=0 since ell_j<0. Dimensions finish the proof. For j=0 it is the identity. The composite `A_(j,a)=E_(j,a) composed with Top_j^(-1)` therefore gives the explicit change from source infinity-top forms to the pole-line forms in(7). Both are defined through fixed finite-dimensional linear maps; no generic rank is inherited or hidden by renaming the functional.

## 3. The W_(t-2) constraint detects all lower leakage

The restriction map rho_a onW_k is an isomorphism onto polynomials of degree<=k. For k=0 this is immediate. For k>=1 suppose q inW_k has rho_a(q)=0, so P=ell Q with degQ<=k-1. Put v=Q/pi_(k-1) inV_(k-1). Then

`q=(ell/ell_k)*v`,

and orthogonality gives

`0=<q,v>=sum_i omega_i [ell(z_i)/ell_k(z_i)]v(z_i)^2`.

The ratio is strictly positive everywhere. Thus v=0 and q=0. Both domain and codomain have dimension k+1, proving bijectivity. This is uniform over the fixed admissible measure and every outward offset tuple, including repeated offsets.

If r inR_t is orthogonal toW_k, equations(4) and this bijectivity imply lambda_r=0. Hence r is orthogonal to ALLV_k. Since by construction r is also orthogonal toW_(t-1) andW_t, while r lies inV_(t+1), it follows that

`{r inR_t:r perpendicular W_(t-2)} is contained inW_(t+1)`. (8)

This proves detection, with no numerical rank, source generation lemma or pole-genericity premise. It also gives the universal rank upper bound

`dimR_t <= (t+2)+(t-1)=2t+1`,                             (9)

because the lower-leakage map has image dimension at most k+1=t-1 and its kernel lies inW_(t+1). The reverse inclusion in(8) requires a separate rank/generation argument; detection alone is not substituted for it.

## 4. Independent reconstruction of the coalescent rank witness

The primary B1 checker supplied the following witness route; I independently reconstructed it before writing this section. Fix ANY c>2 and set every a_j=c. Let ell=x+y-c and define

`X=x/ell`, `Y=y/ell`, `A=1/ell=(X+Y-1)/c`.

For every j, V_j=Pi_j(X,Y): each old monomial divided by ell^j becomes X^rY^s A^(j-r-s), and conversely X^rY^s becomes x^ry^s ell^(j-r-s)/ell^j. The transformed nodes have positive original weights and injective polynomial evaluation throughT+1, because these are exactly the same evaluated spaces. The projective map has no singular node and c!=0.

The blocks W_j are therefore ordinary total-degree orthogonal polynomial blocks in X,Y. The candidate becomes

`C_t=A W_(t-1)+A W_t+XW_t+YW_t`.

Since X+Y-cA=1, it contains W_t. Polynomial multiplication by X orY sends W_t into W_(t-1)+W_t+W_(t+1). Multiplication by the affine A sends W_(t-1) into W_(t-2)+W_(t-1)+W_t. Consequently projection off the top two old blocks gives exactly

`R_t=span{P_W(t+1) XW_t,P_W(t+1) YW_t}+P_W(t-2) A W_(t-1)`.       (10)

The first span is ALLW_(t+1): multiplication by X,Y of the degree-t top forms spans every homogeneous degree-(t+1) form, and the top map on ordinary polynomial blocks is an isomorphism. The backward map in(10) is ontoW_(t-2). Its adjoint is `P_W(t-1) A:W_(t-2)->W_(t-1)`, which is injective: a nonzero polynomial block vector has a nonzero top form, and the nonconstant affine A has nonzero linear part, so their product has a nonzero degree-(t-1) top form and cannot lie inV_(t-2). Positivity and finite-dimensional adjoint duality prove surjectivity.

The two terms of(10) are orthogonal. Hence for this SAME coalescent offset tuple, for every2<=t<=T,

`R_t=W_(t+1) orthogonal-sum W_(t-2)`, `dimR_t=2t+1`.       (11)

This is a structural witness for each fixed admissible measure; it is not a generic-joint-data assertion or an unexecuted rank experiment.

## 5. Pole-only algebraic exceptional set, with the data fixed

Here is an explicit way to turn(11) into the requested generic-offset statement. Fix the nodes and weights once and for all. Let B_j(a) be the evaluated monomial numerator matrix divided rowwise by pi_j. Its entries are rational functions of the offsets. The weighted projectors

`P_Vj=B_j(B_j^T W B_j)^(-1)B_j^T W`, `P_Wj=P_Vj-P_V(j-1)`

are rational in the offsets; their Gram determinants are strictly positive throughout a_j>2 by the fixed injectivity assumption. The generator

`G_t=(I-P_Wt-P_W(t-1))*D_ell(t+1)^(-1)*[P_W(t-1),P_Wt,X0 P_Wt,Y0 P_Wt]`

has column span exactlyR_t. Here X0,Y0 are the original physical coordinate diagonal matrices, not the projectively transformed X,Y, and D_ell is the nonzero evaluated pole diagonal. All entries are rational in(a_1,...,a_(T+1)).

Choose a common polynomial denominator Q_t with no zeros on the outward domain and put Gtilde_t=Q_t G_t. Let F_t(a) be the sum of squares of all(2t+1)-minors of Gtilde_t. This is a finite explicitly defined polynomial in the pole parameters alone, with real coefficients depending on the FIXED nodes/weights. By(11), F_t(c,...,c)>0. Thus the finite product `F=product_(t=2)^T F_t` is nonzero at that same coalescent tuple and is not the zero polynomial.

Outside the proper real-algebraic set{F=0}, rankG_t>=2t+1 for all required t. Bound(9) forces equality. The constraint withW_(t-2), a space of dimension t-1, therefore has a kernel inR_t of dimension at least t+2. By(8) it is contained inW_(t+1), also dimension t+2. Consequently

`W_(t+1)={r inR_t:r perpendicular W_(t-2)}`               (12)

for all2<=t<=T simultaneously outside that pole-only exceptional set.

Although the witness has coalescent offsets, F is continuous and nonzero on a neighborhood of it; every ordering chamber of distinct offsets>2 meets that neighborhood. Therefore imposing distinct poles, or a fixed strict order, does not make the nonvanishing condition vacuous. No claim that F is nonzero at every outward tuple is made. This proof supplies a structural nonzero-minor witness for EACH fixed admissible measure, exactly as required; it does not replace pole genericity by generic nodes or weights.

## Scope and status boundary

The lower-leakage functional, homogeneous pole-line bridge and detection are written all-offset statements for the chosen real Ldiag class. The coalescent witness/rational-minor argument completes the target extraction identity generically in that class for each fixed admissible finite dataset and finite T. Primary lead/checker must integrate these supporting claims into their owned durable theory records and independently inspect their final formulations. No arbitrary complex-pole, Laurent, floating-stability or all-pole-class claim is inferred. No numerical rank or mathematical run was performed by this worker. Required Claude audit remains pending.

## Full-file inspection of the durable supporting proofs

After the preceding module was frozen and reported, root explicitly authorized this append. Actually read each complete saved file, including statement, assumptions, metadata/status, every proof section, scope and open items. Independently hashed the actual bytes after reading:

| Record | SHA256 actually inspected |
| --- | --- |
| theory/proof-attempts-2-codex-90-pole-topform-detection.md | `63a8d44dcc8e60f871697de4adf0f73a067843a48a8dc208980b187267ed2ad7` |
| theory/proof-attempts-2-codex-91-pole-only-generic-rank.md | `ebbb9084db570abab6eaa3ae36c5f0c2d8578d828dd46c2c7da2184efb09926b` |
| theory/proof-attempts-2-codex-92-generic-ldiag-constrained-window.md | `8fc4a6c646f6d3461b2634801bb5099665c11fe7d1f2fe90110c68b21d0f973f` |

Also actually read the complete primary checker's independent-checks-b1.md through its candidate dispositions, rather than inferring a completed written review from our earlier messages. Its B1–B8 proof and both weighted/unweighted lower-pairing formulas are consistent with the independent reconstruction above. No mathematical execution is asserted by this read.

**Record 90: no mathematical blocker found.** Checked the exact homogeneous quotient `tau_(a,k)(p)=sum_d(s/a)^(k-d)p_d`, including the zero-degree case, onto property, and kernel `(s-a)Pi_(k-1)`. Since `a>2`, all divisions by `a` are legitimate. Its projective interpretation is literal: replacing `x/(s-a),y/(s-a)` by projective coordinates sends each homogeneous numerator component to `p_d(X,Y)((X+Y-1)/a)^(k-d)`, whose highest-degree part is the displayed tau. Thus this version supplies a homogeneous next-pole top-form functional without identifying it with the source's unproved skew form. The kernel-annihilation proof pairs every term against the correct old degree space. Positivity of the new/old pole ratio proves detector bijectivity, including all repeated outward offsets; the rank upper bound follows from an injective two-block map and assumes no generic rank. Finally checked the literal ordinary `Top_j` isomorphism by strictly negative `ell_j`, invertibility of `B_(j,a)` by the same detector argument at degree j, multiplicativity of tau with added degree bounds, and the exact lower-block factors `prod_(m=j+1)^k(1-a_m/a)` and `s^(k-j)`. Those formulas are the homogeneous-coordinate version of equation(7) above; no missing denominator or infinity-top truncation is being silently discarded.

**Record 91: no mathematical blocker found.** Full projective conversion preserves every evaluated flag dimension through `T+1`, and the polynomial three-term property follows by degree and self-adjointness. The coalescent candidate generates the two surviving blocks independently: `XW_t+YW_t` has only the two removed old blocks besides its onto new block, and `A W_(t-1)` has only its onto backward block besides those removed blocks. The adjoint injectivity uses the nonzero linear part of A and determining evaluation, so it also covers the constant backward block at t=2. It proves projected rank, not merely generation in a quotient.

Checked the denominator construction explicitly. `h_j A_j` is polynomial rowwise; its Gram determinant `g_j` is strictly positive on the outward offset domain. Projectors computed with this scaled matrix have denominator `g_j`. Hence both factors of the product defining `M_t` are cleared by `G^2`, while the product of all node pole values clears the one diagonal inverse. The stated `q_t` is polynomial and nonzero on that domain. Sum-of-squared real minors therefore detects rank without a basis gauge or radical normalization. The rank polynomial is nonzero for EACH fixed admissible node/weight dataset at the same coalescent tuple for all finite t. Adding the collision factor is justified by the integral-domain property, even though it vanishes at the witness. Continuity also supplies nearby distinct tuples in every strict-order chamber. No joint-data genericity substitutes for the pole-only quantifier.

**Record 92: no mathematical blocker found.** Its full deduction uses rank `2t+1`, at most `t-1` detector constraints, and containment in the known `(t+2)`-dimensional new block to obtain both inclusions. The exception is one fixed-data polynomial in finitely many pole offsets. The statement retains nonvanishing denominators, positive weights, determining evaluation through `T+1`, a meaningful arbitrary finite `T>=3`, simultaneous t, and the chosen real parallel outward class. The source's fixed taper, other pole classes and finite-precision stability remain outside this theorem exactly as written. The broader target is not declared solved. These full-file mathematical inspections supplement, and do not replace, the pending required Claude audit.

## Bounded analytic check of the proposed fixed-taper specialization

Before its durable file exists, the proposed argument can be checked at the mechanism level only. Let `P=prod_t p_t` be the rank polynomial from record 91 **without the collision factor**. It is strictly positive at any common outward coalescent tuple. For a fixed finite taper with each offset `a_j(sigma)=2+sqrt(2)exp(-sigma*d_j)`, substitution into the finite polynomial P gives a finite REAL exponential sum. Combine equal rates and remove zero coefficients to write it as `sum_(j=1)^L c_j exp(-lambda_j sigma)` with distinct real rates. At sigma=0 the offsets coalesce at `2+sqrt(2)`, so this sum is strictly positive there and is not identically zero.

A nonzero sum of L distinct real exponentials has at most L-1 distinct real zeros. Induct on L: divide by one nonvanishing exponential, differentiate, and apply Rolle between any finite list of distinct zeros. The derivative is a nonzero sum of L-1 distinct real exponentials; the induction bound excludes any list of L zeros of the original sum, including an allegedly infinite set. This uses real rates, not a complex oscillatory zero theorem. Therefore only finitely many positive sigma can lose any required rank. Pairwise distinct taper exponents make the offsets distinct whenever sigma>0, without needing to put the collision factor into the coalescent nonvanishing check. An injective source change from positive sigma to its permitted positive minimum-offset parameter transfers finiteness. No particular experimental value is certified by this existence statement; no exceptional roots or values are located, and the coefficients are real, not asserted rational.

This is an independent derivation of the proposed finite-exception mechanism, not yet a claim that the eventual record 93 or its exact source taper indexing has been read. That requires a separate actual full-file read and hash below.

### Actual full-file inspection of record 93

Subsequently actually read FULL theory/proof-attempts-2-codex-93-source-ldiag-taper.md, including its statement, source conventions, assumptions, status, complete proof, scope and history. Independently hashed those bytes as SHA256 `2fa614b3e0175975934ff511d081238570692d89888188e159f0e5ec1af50df1`. Re-read the actual source `orf2d.py` taper and make_lines definitions, including the global even total pole-count assertion, the Ldiag branch's use of taper(n,eps_min), and identity near/reversed far ordering. These were source reads, not executions.

No mathematical blocker found. The statement correctly uses an even total count `m>=4`, `T=m-1`, determining evaluation on `Pi_m`, and all degrees `2<=t<=m-1`; it does not confuse the conjugate-class half-count with Ldiag's total count. Normalizing the source line gives exactly `a_j=2+sqrt(2)epsilon_j`. For either fixed order, the collision-free rank product is positive at sigma=0, so its finite REAL exponential specialization is not identically zero. Grouping rates before Rolle induction is necessary and is done. After multiplying by one exponential, the derivative has exactly one fewer nonzero distinct-rate term, establishing the bound on distinct real zeros even for a proposed infinite set. The finite union covers both source orders and all required degrees. Positive sigma makes the offsets pairwise distinct and outward, and `epsilon_min=exp(-sigma(sqrt(m)-1))` is the stated bijection onto `(0,1)`.

The finite exceptional sets are proper real algebraic sets with real coefficients in the precise finite-set sense stated; neither rational coefficients nor algebraic-number locations are inferred. Core record 91 separately provides the explicit pole-offset exceptional polynomial. Record 93 does not certify any individual experimental parameter, locate exceptional values, claim stable floating rank decisions, extend odd source-code coverage, or alter the broader multi-class target's scope. This is a completed actual full-file mathematical inspection, independent of the earlier mechanism outline. No mathematical computation or code execution by this worker was used. Required Claude audit remains pending.
