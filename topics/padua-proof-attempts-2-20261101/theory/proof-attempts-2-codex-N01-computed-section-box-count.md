# PD-N?proof-attempts-2-codex-01 — The symmetrised-product count fails inside positive-pivot computed sections

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

ID kind: PD-N.
Aliases: B3 four-atom family; shrinking square at an isolated joint node; half-integer computed-section count; fixed-n fixed-p counterexample.
Split from: registered OPEN_TARGETS B3, symmetrised-product count S(alpha).
Split into: none. The separate C1 common-cluster obstruction is supporting80; it is not the mechanism used here.

## Statement

Fix n=1, N=dim Pi_1=3, p=1/10 and T=1/1000000. For EVERY real t with 0<t<=T define the positive four-node measure

mu_t = ((1-t)/3)(delta_(0,0)+delta_(1/2,1/2)+delta_(-1/2,1/2)) + t delta_(0,-1/2).

Let H(t) be its EXACT degree-one multiplication sections in the fixed graded Gram–Schmidt order(1,y,x), with positive leading coefficients. Put h=sqrt(t/10), Q_t=(-h,h)^2 and delta_t=||[H_x(t),H_y(t)]||_2. Then:

1. H(t) belongs to the requested computed-section class S_1(4), and EVERY parent recurrence pivot is >=p uniformly.
2. `0<delta_t=9t/[sqrt(6)(25t+2)^(3/2)]->0` as t->0, and the COMPUTED marginal spectral boundary gap obeys `g(H(t),Q_t)>=sqrt(delta_t)/10>0`.
3. The specified symmetrised-product formula gives `n_box(H(t))=1/2`.
4. The FIXED commuting positive-pivot reference H(0) belongs to N(H(t),Q_t): `d(H(t),H(0))<=g(H(t),Q_t)/2`. Its joint count in Q_t is1, contradicting the required equality to n_box. Thus B3(ii) fails for EVERY t in the stated interval; B3(i) is actually satisfied on this family.

Consequently, taking for example `t_m=1/[10^6(m+1)]`, m>=1, gives the precise fixed-n,p negative form in OPEN_TARGETS. For these fixed n,p, S(alpha) fails for EVERY alpha>1/2 and EVERY finite positive C(n,p). This concerns the SPECIFIED symmetrised-product count; it does not refute other count objects F or a nearby-commuting-pair theorem.

The alternative compatible degree-one order(1,x,y) is covered by ONE fixed permutation of the last two basis vectors for all t, as explained below. No member-dependent gauge rotation is allowed or used.

## Definitions

Use B3's classes, not the similarly named Lanczos C_n: S_1(4) consists of positive-measure sections on four square-supported Pi_1-determining nodes; C_1 consists of FULLY commuting positive-pivot pattern pairs, equivalently three-node sections. Pair distance is `max(||Delta H_x||_2,||Delta H_y||_2)`. The reference radius is HALF the COMPUTED spectral boundary gap g.

For a pair H and the open square Q_t, set `M_x=h^2 I-H_x^2`, `M_y=h^2 I-H_y^2`, `S=(M_x M_y+M_y M_x)/2`. The requested count is `n_box=(n_+(S)-3+n_+(M_x)+n_+(M_y))/2`, with n_+ the number of STRICTLY positive eigenvalues. All these matrices are nonsingular on this family.

## Assumptions

Exact positive-measure arithmetic and operator2-norm, 0<t<=T, the fixed compatible graded basis with positive leading coefficients. All four fixed nodes lie in[-1,1]^2; weights are normalized and strictly positive. No floating sign/eigenvalue selection, asymptotic fit, rounded cluster rotation, extra uniform lower bound on reference pivots, or unstructured compression is used.

## Status by part

Overall status: **PROVED** (complete written family/reduction below; exact symbolic identities/sign certificates and actual different-executor replay). Required Claude audit PENDING.

| Mathematical part | Status | Evidence |
|---|---|---|
| positive M>N sections and uniform pivot lower bound | PROVED | direct moments and explicit basis |
| positive commutator, uniform computed gap and valid reference | PROVED | explicit spectra and uniform norm bounds |
| noninteger n_box=1/2 throughout the interval | PROVED | exact rational determinant/trace identities and sign bounds |
| fixed-n,p rejection of every alpha>1/2 for this count | PROVED | the source's sufficient negative form |

Candidate / claim disposition: **REJECTED: refuted** for S(alpha) with the specified symmetrised-product count on the stated computed-section class at n=1,p=1/10. The candidate C3 construction succeeds as a counterexample; the rejected object is the robustness assertion, not the construction.

## Negative-result scope

Attempted mechanism: programme IDEA?programme-ideas-claude-09 / IDEA-198, its restricted negative N01, and registered B3's extension of symmetrised-product box counting to positive-pivot computed sections with an exponent alpha>1/2.
Parameter range: EXACT fixed n=1, M=4, p=1/10, the four-node family above, ALL 0<t<=10^-6 and shrinking OPEN squares Q_t. Neither an all-n counterexample nor a failure of every delta-only count is asserted. The reference distance here is O(delta), while the SPECTRAL BOUNDARY GAP is of order sqrt(delta): this disproves part(ii), not the separate reference-existence/Lin question. The informal route's pair-distance phrasing is not substituted for the precise negative-form gap condition.

## Depends on

Direct finite-dimensional positive-measure section definitions, simultaneous diagonalization in the square three-node case, elementary spectral theory and exact polynomial algebra. PD-T?programme-ideas-claude-01 supplies the existing commuting-pattern/three-node interpretation, but H(0) is also constructed directly below. REQUIRED prerequisite PD-T?bivariate-lanczos-claude-304(a) was read in full at pin a2dd845b8a231e1b00733e1361e2a9ad3bad222f; its localized SUPPORT-radius lower bound is context, not an inferred pair-distance or gap estimate. C1/support80 is not a dependency of this counterexample.

## Checks

NEW frozen exact driver `../code/b3_four_atom_exact.py`, SHA256 `b33647b8cff4c1b23e9b9089f9822fe307e1f8980786eec043b8bfc9ad3f9b7b`. It constructs G,G_x,G_y from the FOUR declared positive nodes/weights, checks all rational moment-section and weighted-selfadjoint identities, commutator support and delta^2, derives det S and tr S, and gives rational coefficient-tail sign certificates for EVERY 0<t<=T. It makes no floating sign decision and does not merely sample t.

Developer ACTUAL command (repository root):

`PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/b3_four_atom_exact.py --expect-source-sha256 b33647b8cff4c1b23e9b9089f9822fe307e1f8980786eec043b8bfc9ad3f9b7b --output topics/padua-proof-attempts-2-20261101/outputs/b3_four_atom_exact.json`

ACTUAL EXIT0,0.2893616s,8975byte output. A DIFFERENT executor ACTUALLY ran the same frozen driver with OWN `../outputs/b3_four_atom_independent.json`, EXIT0,0.330651232s,8974bytes SHA256 `21eb93c3a5d34c3c43633d678034b5c4347c8e478bd1860873a7c79ddadb9575`. Full JSONs agree after removing ONLY metadata.seconds; exact proof-payload SHA256 `8fe7d5937ae698c255823bed941376e3f0338d972114ca93f333127564df2bc7`. Source before/after hashes match. Python3.12.14, SymPy1.14.0. Independent execution receipt `../independent-execution-b3.md`; these checks supplement the required Claude audit, not replace it.

The exact rational similarity used by the driver is explained in the proof; a nonsymmetric rational matrix is never silently assigned symmetric inertia without that similarity.

## Sources and gate

User B3 request and programme OPEN_TARGETS65–79 at the accepted scientific setting pinned9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; current inspected byte identities and impact checks in `../b3-input-preparation.md`. The FULL783-line relaxed registry/obstruction/disposition gate, mechanism searches, closest full entries, C1/C2/C3 registrations and pre-run kill criteria are in `../attempts/T-B3.md`, before the exact run. This is proof completion of an existing target, with no novelty/priority claim or author contact. No external literature theorem is needed for the new family proof.

## Proof or evidence

### 1. Actual positive sections and pivots

Write u=25t+2, m=(2-5t)/6, v=(1-t)u/36, r=sqrt((1-t)/6), s=sqrt(v), c=(1+5t)/sqrt(6u), beta=m(1-25t)/u. Direct moments give

`E[x]=E[xy]=0`, `E[y]=m`, `E[y^2]=(2+t)/12`, `E[y^3]=m/4`, `E[x^2]=r^2`, `E[x^2 y]=r^2/2`.

Hence the actual normalized Gram–Schmidt basis is `(1,(y-m)/s,x/r)`, with positive leading coefficients. The first three fixed nodes are noncollinear: their evaluation determinant for(1,y,x) is-1/2. Thus the FOUR-node support is Pi_1-determining for every t and all four positive weights define S_1(4). The two symmetric sections are exactly

`H_x=[[0,0,r],[0,0,c],[r,c,0]]`,

`H_y=[[m,s,0],[s,beta,0],[0,0,1/2]]`.

The positive parent pivots are r and s. Since `r^2=(1-t)/6>1/100` and `s^2=(1-t)(25t+2)/36>1/100` throughout0<=t<=T, their minimum is>=p=1/10. Cyclicity is direct: e_0,H_x e_0,H_y e_0 span R^3 because r,s>0. All source pattern requirements hold. Multiplication by x,y is bounded by1/2 on this positive support, so the sections are symmetric contractions.

Because x is orthogonal to both1 and y-m for EVERY t, switching the allowed order to(1,x,y) merely swaps the last two normalized basis polynomials. One FIXED permutation conjugates BOTH sections for the whole family. This preserves their operator norms, commutator norm, spectra, inertia, minimum positive pivot, reference distance and the physical square Q_t. Thus no basis-order loophole or member-dependent rotation is used.

### 2. Exact commutator and computed gap

The commutator has only its last2x2 skew block nonzero, with entry

`k=c(1/2-beta)-rs=9t/[sqrt(6)u^(3/2)]`.

Thus delta_t=k>0 and tends to0, with `delta_t^2=27t^2/(2u^3)<4t^2`, hence delta_t<2t.

H_x has eigenvalues0 and +/-A, where

`A^2=r^2+c^2=(1+11t)/(2u)>1/5`.

The2x2 block of H_y has trace `tau=(2-5t)/(2u)>2/5` and determinant `-6t/u<0`. Its eigenvalues have signs lambda_-<0<lambda_+, with lambda_+>tau>2/5 and

`|lambda_-|=(6t/u)/lambda_+ <(15/2)t<8t`.

The third H_y eigenvalue is1/2. For our T, `8t<=h/2` (equivalently2560t<=1) and h<1/10. Therefore lambda_- lies strictly between-h/2 and0; all the other nonzero marginal eigenvalues have absolute value>2/5. The distance of EVERY marginal eigenvalue from BOTH square endpoints +/-h is consequently at least h/2. This proves the COMPUTED gap bound

`g>=h/2=sqrt(t)/(2sqrt(10))>=sqrt(delta_t)/10>0`,

where `(h/2)^2=t/40=2t*(1/80)>2t/100>delta_t/100`, using `delta_t<2t`. This is a spectral boundary-gap estimate, not a statement about support-node spacing or pair distance.

It also proves n_+(M_x)=n_+(M_y)=1: exactly one marginal eigenvalue is inside(-h,h), the others are outside, and no boundary eigenvalue occurs.

### 3. Exact symmetrised-product inertia

One can check the following identities by direct expansion. To make that finite check independently repeatable, use the orthogonal UNNORMALIZED basis(1,y-m,x), G=diag(1,v,r^2), D=diag(1,s,r). Its rational section matrices are

`T_x=[[0,0,r^2],[0,0,(1+5t)/u],[1,(1+5t)/6,0]]`,

`T_y=[[m,v,0],[1,beta,0],[0,0,1/2]]`.

They satisfy `G T_x=G_x`, `G T_y=G_y` from the declared moments, and `H_x=D T_x D^-1`, `H_y=D T_y D^-1`. Every polynomial expression in the pair, including S, is transported by this ONE common similarity. Thus the rational determinant/trace calculations are exactly those of the real symmetric S; its inertia is real symmetric inertia.

Define the explicit polynomial

`F(t)=39062500t^7-261718750t^6+555468750t^5-321968750t^4-103933375t^3-9406197t^2-109640t-21700`.

Exact expansion gives

`det S=t^2(2t-5)(25t^2-53t-5)F(t)/[8000000u^6]`,

`tr S=[46875t^5-173125t^4+116525t^3+36429t^2+3220t+100]/[100u^3]`.

The signs hold on the ENTIRE interval. Indeed t<=T<1/100, the only positive nonconstant coefficients of F are at degrees5 and7, and

`F(t)<=-21700+555468750/100^5+39062500/100^7<-21699<0`.

Both2t-5 and25t^2-53t-5 are negative, so det S<0. The trace numerator is at least `100-173125/100^4>99>0`. Thus S is nonsingular and has positive trace and negative determinant. In dimension3 this means exactly one negative and two positive eigenvalues: three negatives would force negative trace. Consequently

`n_box=(2-3+1+1)/2=1/2`

for EVERY 0<t<=T. This is exact inertia, not a small-t numerical sign or an extrapolated leading coefficient. The separately repeated symbolic checks also give `det S/t^2 -> -217/204800` as a sanity identity, but that limit is not substituted for the explicit interval signs above.

### 4. Explicit commuting reference and its uniform distance bound

H(0) is the degree-one section pair of the three noncollinear base nodes with weights1/3. Since M=N=3, the weighted evaluation matrix is square orthogonal, so these full multiplication operators commute. Their positive pivots r(0),s(0) are nonzero; hence H(0) belongs to B3's C_1. Its joint spectrum is exactly the three declared base nodes. Only(0,0) lies in Q_t since h<1/10, so `N_Qt(H(0))=1`.

Here is the FULL uniform norm estimate, without relying on a code boolean. Throughout0<=t<=T,

`|m-m0|<t`, `|r-r0|<=t`, `|s-s0|<3t`, `|c-c0|<4t`, `|beta-beta0|<7t`.

For r, rationalize `sqrt(1-t)-1`. For s use `v-v0=(23t-25t^2)/36` and `s+s0>=s0=1/sqrt(18)`, giving `|s-s0|<=23sqrt(18)t/36<3t`. For c write `f(t)=1/sqrt(6(25t+2))`, so `|f'|<=25/(8sqrt(3))<2`, `f(t)<=1/sqrt(12)` and `c=(1+5t)f(t)`: the bound is `<(5/sqrt(12)+2)t<4t`. For beta write `z=(1-25t)/(2+25t)`, so `0<=z<=1/2` and `|z-1/2|=75t/(2u)<=75t/4`; then

`|m z-m0/2| <= (5t/6)(1/2)+(1/3)(75t/4)=(20/3)t<7t`.

H_x(t)-H_x(0) is a symmetric star with norm `sqrt((r-r0)^2+(c-c0)^2)<5t`. For H_y's symmetric2x2 block the largest absolute row sum is<10t, bounding its operator norm; the third entry is unchanged. Therefore

`d(H(t),H(0))<=10t<=h/4<=g/2`,

since16000t<=1 on our interval. Thus H(0) really belongs to the REQUIRED reference ball and its count1 contradicts n_box=1/2. Alternatively the noninteger count alone makes the conjunction(i),(ii) impossible because any genuine joint count is an integer; the explicit reference above proves the more precise failure of(ii).

### 5. Fixed-n,p quantifiers

For t_m as stated, all hypotheses use the SAME n=1,p=1/10,c=1/10 and M=4. Delta_m>0 tends to0 and(ii) fails for every m. For any alpha>1/2,

`g_m/delta_m^alpha >= (1/10)delta_m^(1/2-alpha) -> infinity`.

Hence for every finite positive C(n,p), all sufficiently large m meet BOTH g>0 and g>=C delta^alpha while violating(ii). This is precisely the source's sufficient negative form and refutes S(alpha) at those fixed n,p. ∎

## Scope

The symmetrised-product formula fails even on genuine positive, cyclic, uniformly positive-pivot degree-one computed sections with M>N. The failure uses shrinking boxes around an ISOLATED joint node, not a repeated joint eigenvalue; the literal common-cluster obstruction does not apply. Reference existence holds here, so no failure of a structure-preserving quantitative Lin statement is claimed. No conclusion about S_F, boxes with an additional fixed geometric lower bound, other degrees, or every nearly commuting count is inferred.

## Open items

Required Claude audit and root integration/registry proposals under their original ownership. Broader questions for other count objects and reference-existence rates remain OPEN. There is no unexecuted mathematical computation needed for the stated family; its two actual exact runs and complete written interval argument are present.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh; rules b5bba7cf1328b1f207aea001a439c3fe4af0146f. Registered C3 before code, froze source before first run, then wrote this full scoped negative after two actual exact executions. Root and another analytic reader independently reconstructed the section matrices/leading Schur mechanism; these supplement, not replace, required Claude audit. No novelty or priority claim.


Audit-01 F7 field-scope clarification: the frozen driver's `squared_gap_and_reference_inequalities: true` reports only its two scalar endpoint inequalities. It does not machine-check eigenvalue localization, `g>=h/2` or `d<=10t` on the whole interval; those are supplied by the written proof. Claude's separate `audit-support/claude-audit-01/b3/b3_audit_independent.py` and its certificate verify the whole-interval spectral/reference claims independently. The developer driver, hash and outputs are unchanged; its boolean is not promoted into a broader certificate.
