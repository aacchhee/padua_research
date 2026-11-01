# A5 n=4 supplementary independent reduction inspection

Checker: Codex `/root/a2_independent_route`, requested gpt-6.1-sol xhigh; runtime-resolved model/effort metadata are not separately exposed. Date: 2026-11-01. Root alone owns Git. This is a supplementary independent mathematical inspection, **not the required Claude audit**, not a producer/checker execution, and not certification of an n=4 count.

## Provenance and reading scope

Read and independently reconstructed the FULL file `theory/proof-attempts-2-codex-08-quartic-finite-reduction.md` at 2026-11-01T09:46:38Z. The read-only `sha256sum` command returned:

`2a9778d2c6f7fb279488670bc7b2e0caa170d1928d83871e8616216e264f3b40`.

Observed workspace head: `c26a6adf6ebf701368f5de73fc319b0e55cdfc13`. Applicable rules were read at `3db1eee3fd9507c103c496bdf3da8157331359c5`; this is the n=4 continuation of the already gated A5 target. The complete A5 registry/source gate, model allocation and earlier full source readings are recorded in `independent-checks-a5-reduction.md`. No new literature or novelty claim is involved. Only this new receipt and the previously assigned receipt path are owned by this agent.

Coverage here includes every statement item and quantifier, definitions, assumptions, proof sections, and scope/open-item limitations of theory-08. No computation beyond provenance hashes/date/head was performed. The preliminary spatial diagnostic and any finite resultant/root artifacts were not executed or inspected by this review.

## Findings

**No mathematical finding identified within the declared supporting-theorem scope.** The written finite-reduction proof is complete at its stated analytic/algebraic level. In particular it retains the quartic cases that the cubic Hessian argument would incorrectly discard. Its PROVED supporting status does not supply a count or automatic termination of a subdivision scheme.

### Active signed polynomials and candidate types

For any finite family of real polynomials, `lambda=max_s P_s` and `P_s<=lambda` everywhere. Equality at an active pattern transfers a strict relative maximum of lambda to a strict relative maximum of EVERY active P_s. At an interior maximum the active gradients vanish. Flipping a vanishing L_i therefore forces its physical gradient to vanish too. The same argument on an open edge forces zero tangential derivative, but imposes no analogous zero normal derivative. Hence the exact regular-crease exclusions and arbitrary-crossing coverage are valid without assuming smoothness of lambda.

The finite sign-condition formulation covers identicallyzero cardinals, singular zero sets and disconnected sign regions. The square interior, four open edges and four corners exhaust the physical domain. No assumption about a geometric drawing or connected-component enumeration is used.

### Residual stationary system and projection resultants

If one derivative of P_s is identically zero, P_s is independent of that physical coordinate and has a line of equal values through each interior point, excluding strict maximality. With both derivatives nonzero, division by the full gcd G gives coprime nonzero residual a,b. A stationary point off G=0 must solve a=b=0.

If one residual is a nonzero constant, there is no residual common root. Otherwise the two coprime plane polynomials have a finite common zero set over an algebraic closure, and both coordinate resultants are nonzero (nonzero constants allowed). Every finite common root zeros both resultants. Specialization that lowers the eliminated-variable degrees can add extraneous resultant roots, but does not remove a genuine finite common root. Thus complete real-coordinate root partitions and **every** Cartesian interval pair provide finite coverage. Extra pairs and conjugate-embedding roots still require valid dispositions; the theorem does not silently discard them.

### Squarefree common-gradient factor and isolated-real points

Let F be the squarefree part of nonconstant G. The real zero sets of F and G agree. If F(z)=0 and grad F(z) is nonzero, the real implicit function theorem supplies a nonconstant smooth real curve segment through z in F=0. Along the segment G=0, so both derivatives of P_s vanish. The chain rule makes P_s constant along the connected segment, which excludes a strict interior maximum there.

Therefore a strict maximum on G=0 must satisfy `F=F_x=F_y=0`. This explicitly retains isolated-real zeros: a regular real point could not be isolated by the same implicit-function argument. No Hessian sign or nonsingularity is used to discard G=0.

The directional derivative construction makes the singular superset finite. Factor F into its distinct nonconstant irreducible K-factors f. Because the polynomial ring over K is a unique factorization domain and f is prime,

`f divides F_x+t*F_y` iff `f divides f_x+t*f_y`.

The latter derivative has smaller total degree than f, so divisibility means it is identically zero. For a fixed nonconstant f this identity can hold for at most one t: two distinct choices force both partial derivatives of f to vanish, impossible in characteristic zero. There are at most deg F factors, and hence at most deg F bad t values. Among the deg F+1 distinct integers 0,...,deg F, one therefore gives `gcd(F,F_x+t*F_y)=1`.

For that choice H=F_x+t*F_y is nonzero. If it is a nonzero constant, the included system has no common zero. Otherwise the coprime F,H system has a finite zero set and nonzero projection resultants. Every singular point of F is included because it zeros every directional derivative. Additional regular directional tangencies are harmless candidates requiring later classification.

Both examples in the theorem are appropriate. The isolated-real common-factor zero of `-(x^2+y^2)^2` is singular for F and retained. The singular-Hessian maximum of `-x^2-y^4` lies in the residual system with constant gcd and is retained too.

### Edge degeneracies and normal classification

A constant active restriction cannot account for a strict relative maximum because it would give nearby feasible edge points of the same value. All other restrictions have a nonzero derivative polynomial with finitely many roots, and identicallyzero restricted cardinals do not change that tangent polynomial when their signs are fixed.

Every derivative root is retained. For a nonconstant degree-at-most-four polynomial at a stationary point, strict one-dimensional maximality is equivalent to its first nonzero Taylor term having even order 2 or 4 and a negative coefficient. An odd cubic leading term excludes maximality; a vanishing quadratic term does not by itself exclude a quartic maximum. The proof explicitly leaves inward-normal tests, zero-normal cases and singular edge-cardinal zeros to separate exact local classification. It therefore makes no unsupported claim that tangential strictness suffices for a relative maximum on the square.

### Coefficient field and norm enumeration

The degree-four Padua coordinates lie in Q(sqrt(2),sqrt(5)), and an exact Vandermonde inverse preserves that field when defined. The norm assertion is restricted to a finite algebraic K/Q: the product of conjugate nonzero polynomials is nonzero, lies in Q[u], and vanishes at every chosen-embedding real root. Squarefree reduction preserves distinct roots. Complete Sturm counts and disjoint one-root intervals then cover the entire real root set. The theorem leaves actual field arithmetic, root partitions and dispositions to the eventual certificate, as required.

## Remaining obligations and status limits

This inspection accepts only the written finite-reduction argument at the hash above. It does not classify any actual quartic candidate, verify any polynomial gcd/resultant/root interval, prove a count, or establish a global argmax. Actual n=4 root dispositions, degenerate-boundary analysis, certificate/checker construction and independent execution remain required. A strict-maxima list alone would also leave non-strict global plateaus to a separate argument.

The n=4 count remains OPEN. The original n=3,...,8 target is unchanged. No developer proof, shared registry, code, or Git state was edited by this agent.

## Full spatial-certificate and global-proof inspection

On 2026-11-01, with workspace head `44be0080c69495cc6959e3d4c2b602fa73678d76`, read and independently reconstructed the FULL theory-09, theory-10, theory-11 and n4 schema files. Provenance commands began at 2026-11-01T10:02:25Z; own SHA-256 reads were:

| File | SHA-256 |
|---|---|
| `theory/proof-attempts-2-codex-09-spatial-certificate-correctness.md` | `c57750f73956ccbecaae1e5902d2592f829f0ef77e6c27412ec3db81406bbe93` |
| `theory/proof-attempts-2-codex-10-degree-four-maxima-count.md` | `9f829b3d71d1c774cbdefdf91873f6e2257b6475aed9fb0857c25f1c3c55ba45` |
| `theory/proof-attempts-2-codex-11-degree-four-global-argmax.md` | `dbf345f28e57742e2860a4ce3f1eba9c458e2910e00d30eda07a92f836a6540d` |
| `code/a5_n4_schema.md` | `eb11ef7928c9c2fc81c6cca597646dfe0c65c88a13a388b28baad3932e8c7ad3` |

These reads inspected the mathematical verification implication and its application to the proposed count/global certificate. They did not execute, inspect or accept the certificate bytes, producer code, independent checker code, reported leaf counts, interval outputs, or actual execution receipts. Theory-10 and theory-11 were explicitly OPEN at these hashes. This remains a supplementary mathematical check, not the Claude audit or an independent finite rerun.

**Conclusion:** no mathematical finding identified within the declared theory-09 implication or the conditional theory-10/-11 proof scopes. The following coverage records the points reconstructed independently.

### Theory-09: complete spatial cover and universal masks

A complete finite prefix leaf set covers the entire closed square under the prescribed exact midpoint splits. Closed siblings can share their boundary; uniqueness of the containing leaf is not needed. An actual maximum belongs to at least one leaf, and all inequalities are asserted on the entire closed leaf. Every active mask at any point of that leaf appears in the recomputed compatible-mask list: a genuinely positive/negative cardinal value cannot contradict a strict interval sign enclosing it, and an interval containing zero permits both choices. Requiring an exact full list prevents the old first-success early return.

For each compatible mask, the stated strict predicates have the required meaning:

- `flat` excludes strict interior maximality of P by coordinate independence.
- A gradient component excluding zero excludes stationarity.
- Strictly positive H_xx or H_yy, or strictly negative determinant, excludes even an ordinary non-strict local maximum. Equality alone is deliberately not an exclusion for quartics.
- `factor` puts every stationary point on G=0 when a residual component excludes zero. A verified nonzero partial of squarefree F on the leaf makes those points regular on a real common-gradient curve; P is constant there. Isolated-real factor zeros cannot pass this regularity predicate.
- `regular_point` supplies an exact stationary p and a convex rectangle U containing both p and the whole leaf. The contraction/injectivity inequality on U makes p the only possible stationary point in the leaf. A regular cardinal zero excludes even weak lambda maximality; an exact node excludes strict lambda maximality because lambda>=1=lambda(p). Mere proximity or intersection with a crease/node is insufficient, as the theorem correctly states.
- A `root` record supplies a genuine stationary p in a strictly interior root box R, negative definite Hessian and strict cardinal signs there. Its additional injectivity witness on U containing BOTH R and the whole leaf makes p the only possible stationary point of that mask in the leaf. This remains valid when the leaf is not contained in R. Every accepted root is itself a strict lambda maximum; disjoint R boxes establish distinctness, and repeated references to the same id count once.

The injectivity calculation is sound: integrating `I-C*H` along the segment between v,w in convex U gives an averaged error E with infinity norm below one. Equal gradients imply `(I-E)(v-w)=0`, hence v=w. No unconstrained Newton iterate is used.

### Theory-09: Krawczyk existence, strictness and uniqueness

For midpoint c, the mean-value integral of the gradient encloses the map `T(v)=v-C*grad P(v)` in the stated interval Krawczyk set. If that set lies strictly inside the closed rectangle R and the derivative infinity norm is below one, T is a contraction self-map of the complete rectangle. Banach gives one fixed point, and strict inclusion places it in the interior. The norm bound makes `C*H(c)` invertible by the Neumann argument, so C is invertible and a fixed point is a stationary point. Strict negative definiteness at that point gives a strict P maximum; strict cardinal signs give lambda=P nearby. Candidate selection by Newton is harmless only because none of these acceptance predicates depends on an unverified iterate.

### Theory-09: exact edge arrangement and every gap mask

The multiplicity-one cover is sufficient. Every chosen-embedding real root alpha of E belongs to an irreducible K-factor f that appears with multiplicity one in at least one restricted cardinal r_i. In characteristic zero f is separable; coprimality with the remaining factors gives `r_i'(alpha)!=0`. Thus every actual edge crease, including any crossing, is excluded exactly by the tangent active-polynomial condition.

The gap-sampling argument does not miss sign components even though root intervals may contain conjugate-embedding extras. Between two consecutive actual E roots, their distinct norm-root isolating intervals are disjoint and ordered; at least one supplied rational gap between consecutive norm intervals lies between the two actual roots. That sample lies in the desired actual sign component. The two unbounded actual components contain the exterior samples. Extra norm roots merely add samples in an unchanged actual component. Singleton rational intervals cause no exception. Samples outside all norm-root intervals cannot zero any r_i. Thus the distinct exact sample masks include every noncrease edge mask, including masks on the physical open edge.

For a nonconstant restriction, every remaining tangent critical point has `D_s=0` and E!=0. Squarefree reduction of D_s preserves its distinct roots, and removing its gcd with E removes only already-excluded creases. Complete norm partitions of D_r therefore cover all such points. Outside, wrong-embedding derivative, incompatible-sign and strictly positive second-derivative dispositions each fail a necessary condition. In particular a zero second derivative is not silently discarded.

An accepted edge root has strict signs of every r_i, strictly negative q'', endpoint derivative signs + then -, and a containing interval strictly inside the open edge. IVT supplies a derivative zero and strict negative q'' makes it unique. Strict cardinal signs at the root extend to a relative neighbourhood in the full square, making lambda the same physical P_s there. Strictly negative inward derivative plus tangent maximality proves a strict relative maximum; strictly positive inward derivative gives a feasible ascending direction. Zero-normal and tangent-degenerate cases remain unresolved unless a separate proof is supplied. The schema's rejection of unresolved cases is essential. Disjoint accepted edge intervals and separate strata make the ids distinct.

### Theory-09: corners and count implication

Exact node corners cannot be strict lambda maxima under constant reproduction. At a remaining corner, nonzero signs stay fixed and zero-cardinal signs range over every active pattern. Strict negativity of both inward partial derivatives for every active P_s persists in a common small neighbourhood, by finiteness and continuity. Integration along inward segments proves strict descent of their finite maximum. Combined with the complete interior/open-edge cover and genuine distinct root witnesses, this proves the stated count implication for EVERY finite accepted certificate. It does not imply that a search terminates or that an actual certificate has passed.

### Theory-10: pending finite count application

The application correctly requires the complete tree, every compatible-mask disposition, all four exact edge arrangements and every residual critical root, all corners, disjoint accepted witnesses, zero unresolved cases, and separate computational verification. It does not transfer the cubic Hessian necessity to quartics. Its reported absence of `regular_point`/`factor` fallbacks is a finite fact still to be checked, not a universal property of quartic polynomials. The source's measured 13/12/2 split is not an assumption. This review checks only that the stated finite acceptance obligations would establish the count.

### Theory-11: non-strict global maxima and value separation

The written conditional global proof avoids the cubic null-line argument correctly. At an interior global lambda maximum z, every active P_s has an ordinary possibly non-strict local maximum. The actual certificate is asserted to use only `gradient`, strict `hessian`, `root`, and `flat` interior predicates; this usage restriction must be verified with the finite data. Gradient/strict Hessian predicates exclude ordinary local maxima. A `root` predicate puts every stationary point of its leaf at the unique accepted root by hull injectivity; the separate rigorous root-value enclosure then bounds lambda there below 4. A `flat` predicate by itself would not exclude a non-strict maximum, but the additional bound P_s(Q)<4 on that exact leaf contradicts activity at a value >=C>4. Every flat occurrence must be covered; a bound for a different box or only a subset of masks would not suffice. The proof does not rely on the strict-count theorem alone.

On an edge, multiplicity-one crease regularity excludes even non-strict maxima. All noncrease masks and derivative roots are covered as above. Derivative/sign/outside/positive-curvature exclusions remain valid for ordinary maxima, and a positive actual inward derivative excludes a relative global maximum. A constant restriction q must equal +1 or -1 because each physical edge contains a Padua interpolation node. This is below C. The accepted certificate is required to have no unresolved zero-normal or tangent-degenerate case; hence every other possible edge maximum is one of the accepted roots whose rigorous value enclosure is below 4.

The exact corner threshold is valid. With `C=(13+sqrt(2)+2*sqrt(5)+sqrt(10))/5`, the elementary inequalities sqrt(2)>1, sqrt(5)>2 and sqrt(10)>3 imply C>21/5>4. The exact identification of the corner values as C and the bounds on ALL interior/edge root ids remain finite predicates, not computations performed by this agent. Compactness gives an attained global maximum; the interior/open-edge exclusions and exact node-corner values then leave precisely the two stated non-node corners.

No finite leaf/value bound, count, or global argmax is accepted here as execution evidence. Theory-10/-11 status upgrades require the separate checker and different-agent execution records.

## Targeted final n=3 interval-proof addendum

At the same provenance checkpoint, read the new theory-06 subsection **"Why the supplied interval predicates prove what they claim"** in full. This was a targeted addition review; the earlier full mathematical reviews of theory-05/-06/-07 are recorded in `independent-checks-a5-reduction.md`. Current final hashes supplied by own `sha256sum` command were:

| File under `theory/` | SHA-256 |
|---|---|
| `proof-attempts-2-codex-05-cubic-finite-reduction.md` | `ff45a9318405ca87770d6d32499864af18759ebca634653050fe6f4de84f1aab` |
| `proof-attempts-2-codex-06-degree-three-maxima-count.md` | `9a5588ef0cdeea29e79d1848fbbfa915f1a1e913230adbc3cbaaea65f75bf89e` |
| `proof-attempts-2-codex-07-degree-three-global-argmax.md` | `5894d7ae774ac91e5ac39f84ab907ecb4c0576c07937d34d2e962be0d638e01a` |

No mathematical finding in the added subsection. Inclusion-preserving Fraction operations enclose polynomial values/derivatives by induction. The verified infinity norm q<1 bounds the derivative of T on the whole convex rectangle. The Krawczyk enclosure contains T(Q); strict inclusion gives a contraction self-map and an interior fixed point. If C were singular, a nonzero left null vector would give eigenvalue one to I-CJ, contradicting the induced norm bound. Thus fixed points are gradient zeros. The same contraction estimate gives uniqueness of any two gradient zeros even when only an exact regular-point witness, rather than Krawczyk existence, is supplied. Negative definite Hessian and strict signed-cardinal signs give a strict lambda maximum. An exclusion for failed negative definiteness is understood to require a **verified failure of a necessary condition**, rather than mere inability to verify negative definiteness; actual checker predicates remain covered by the separate finite-code review.

The developer/root reported completed n=3 executions and status promotions. This addendum does not independently verify those runs or the newly inserted computational evidence; it refreshes the final document hashes and covers only the requested added analytic argument.
