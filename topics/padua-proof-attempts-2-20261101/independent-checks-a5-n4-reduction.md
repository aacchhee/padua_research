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
