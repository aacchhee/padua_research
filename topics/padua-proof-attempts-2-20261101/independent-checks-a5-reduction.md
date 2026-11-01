# A5 supplementary independent reduction and checker advice

Checker/contributor: Codex `/root/a2_independent_route`, requested gpt-6.1-sol xhigh; runtime-resolved model/effort metadata are not separately exposed. Rules read at `3db1eee3fd9507c103c496bdf3da8157331359c5` on 2026-11-01. Root alone owns Git. This is supplementary mathematical proof support, **not the required Claude audit**, and not a certification of any maxima count. Only this new file is owned by this agent.

## Reading and gate receipt

Reread the complete user attachment, `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md` at the recorded head. Repeated the target-specific relaxed registry scan: complete headings, IDs, aliases and summaries of the 496-line `state/IDEAS.md`, all source/campaign/current disposition tables, and every obstruction table. The previous A2 full registry reading was available; bounded rereads covered the A5 scan at this head.

Mechanism searches across state, topics, tracks and literature used `local.max`, `crease`, `crossing`, `sign.pattern`, `degenerate`, `Sturm`, `resultant`, `semialgebraic`, `stratif`, and `active.sign`. Full shortlist/source reads:

- Charter IDEA-048 (the complete registry entry: contextual Padua maxima question).
- Programme IDEA-17, its full candidate entry, and theory `programme-ideas-claude-06-padua-lebesgue-maxima-counts.md`.
- Source `OPEN_TARGETS.md` A5 and A5-partial.
- All 461 lines of `t3_certify.py` and all 151 lines of `t3_degenerate.py`.
- All 269 lines of part-1 theory `proof-attempts-codex-03-degenerate-maxima.md` and audit-01 F2.

The cardinal-polynomial convention and current task are the ones already pinned by root. The target is completion of a registered proof obligation, not a novelty claim. The one-maximum-per-Lissajous-cell mechanism is already refuted; it is not used. The old floating Newton/discard logic and near-crease coincidence tolerance do not certify a count. Audit F2 explicitly leaves the corner and edge-node handlers outside part-1's local theorem; the alternative finite polynomial enumeration below is intended to avoid relying on those handlers.

If reused, the part-1 local result must be named **PD-T?proof-attempts-codex-03 (audit pending)**, with the dated qualification that part-1 Claude audit-01 at `95279b833bca5967fcf47c1b71a56ff622185b4e` accepted its mathematical scope while upstream disposition records remain pending. This advice does not expand that scope.

## Elementary all-active-polynomials reduction

Let the real cardinal polynomials be L_1,...,L_N, set `P_s=sum_i s_i L_i` for `s in {-1,+1}^N`, and let `lambda=sum_i |L_i|`. Pointwise,

`lambda(z)=max_s P_s(z)`.

Call s active at z when `s_i=sign(L_i(z))` for every nonzero L_i(z); zero terms allow either sign. If z is a strict local maximum of lambda relative to the square, then **every active P_s has a strict local maximum there relative to the same square**. Indeed, for every sufficiently close distinct w in the square,

`P_s(w) <= lambda(w) < lambda(z) = P_s(z)`.

Conversely, if every active P_s has a strict relative local maximum at z, the finitely many active branches have a common neighbourhood of strict decrease. Every inactive branch has a strictly smaller value at z and remains below lambda(z) on a small enough neighbourhood. Hence lambda itself has a strict relative local maximum. This equivalence uses all active branches, not merely the one selected numerically.

At an interior point this gives `grad P_s(z)=0` for all active s. Flipping the sign of one zero cardinal changes the gradient by `2 grad L_i(z)`, so every zero L_i must satisfy `grad L_i(z)=0`. Therefore every regular crease point is excluded, including any crossing at which at least one vanishing cardinal has nonzero gradient. No coincidence tolerance or enumeration of crossing angles is required for this implication. Singular zero points remain to be classified.

On the relative interior of an edge, the same argument forces every active tangential derivative to vanish, and hence every zero cardinal has zero tangential derivative. It does **not** force its normal derivative to vanish. In outward-normal notation, all active first-order necessary inequalities are equivalent to

`outward_derivative(g) - sum_(i in Z) |outward_derivative(L_i)| >= 0`,

where Z is the zero-cardinal set and g is the signed sum of nonzero cardinals. Strict inequality, together with strictly negative tangential curvature for all active branches, is a useful sufficient condition. Equality needs additional analysis; it must not be silently accepted or discarded.

## Exact cubic limitation and interior finite reduction

The following additional simplifications apply to **degree at most three**, hence directly to n=3. They are not asserted for n>=4.

If a cubic P has an interior strict local maximum z, its Hessian H(z) is negative definite. The necessary negative-semidefinite condition is standard. If H has a nonzero null vector v, the exact restriction along z+t*v has zero linear and quadratic terms. Its cubic term is either nonzero, in which case one sign of t increases P, or zero, in which case the entire line restriction is constant. Both contradict strictness. This proves negative definiteness, including polynomials of degree below three.

Set `A=P_x`, `B=P_y`; these have degree at most two. If either derivative is identically zero, no negative-definite Hessian is possible. Otherwise suppose

`A=G*a`, `B=G*b`

for a common polynomial factor G. At every point G=0 the Hessian has rows `a*grad G` and `b*grad G`, so its rank is at most one. Such points cannot be cubic strict maxima. Dividing by the full bivariate gcd leaves coprime residual polynomials a,b. Their common complex zero set is finite, with at most four points by the elementary degree-two intersection bound. Consequently all n=3 interior strict maxima occur among a finite, rigorously isolatable set of stationary points. The producer/checker must still establish that its actual elimination and lifting data cover that set.

A further useful uniqueness fact is that H_P is affine in (x,y). The set `{H_P negative definite}` is convex. If two critical points lay there, the segment between them would lie there too, and strict concavity along that segment would contradict the vanishing gradients at both ends. Thus each signed cubic has at most one strict local maximum anywhere in the plane. A certified such point can dispose of that entire signed pattern, but absence still needs an exclusion certificate.

The cubic restriction is essential. For example `-(x^2+y^2)^2` is a quartic with a strict maximum and zero Hessian; its gradient has a common factor vanishing at an isolated real point. The cubic rank/null-line argument cannot discard that case at n=4.

## Boundary advice and remaining verification

Physical coordinates remove the artificial angular degeneracy caused by the cosine map. For instance, if an edge-vanishing cardinal factors as `(x-1)*Q(x,y)` and Q is nonzero at the candidate on x=1, its sign is fixed on a sufficiently small neighbourhood inside x<=1. It therefore contributes one smooth signed polynomial there. If Q also vanishes, that additional degeneracy must be treated exactly.

For a cubic restricted to an open edge, a strict local maximum requires zero tangential derivative and strictly negative tangential second derivative: if that second derivative vanished, the remaining cubic restriction would be odd or flat. Thus candidate tangential locations come from quadratic derivative roots.

The following proposed one-sided classification was communicated to the developer as advice, not as an inspected implementation or completed boundary certificate. In inward/tangential coordinates `(u,v)`, with u>=0, assume `P_v=0` and `h=P_vv<0` at the candidate. Put `a=P_u`. Then a<0 gives a strict relative maximum and a>0 excludes it. If a=0, a negative-definite Hessian gives a strict maximum and an indefinite Hessian excludes it. If a=0 and det H=0, take the null vector `w=(1,-P_uv/h)` and the cubic coefficient along w. A negative coefficient gives a strict one-sided maximum; a positive one excludes it; zero gives an exactly flat feasible ray and excludes strictness. Sufficiency in the negative cubic case follows by completing the negative tangential square and absorbing mixed cubic terms into its quadratic term plus an O(u^4) remainder. All derivatives and equality cases must be checked exactly at the algebraic candidate, for every active branch.

For corners, a finite homogeneous-Taylor alternative was also suggested. In inward coordinates u,v>=0, any positive gradient component excludes a maximum; two negative components suffice. If one is zero and the other negative, local monotonicity in the latter coordinate reduces the question to the one-sided cubic on the zero-gradient axis. If both gradients vanish, write the homogeneous terms as q2 and q3: strict corner maximality requires q2<=0 on the quadrant and q3<0 on every nonzero direction where q2=0. Necessity follows along rays; sufficiency follows by compactness of the unit quadrant, separating neighbourhoods of the q2-zero directions from the region where q2 is uniformly negative. Exact tests reduce to low-degree univariate signs and roots plus the two axes. This has not yet been checked against the producer's actual corner data or certificate schema.

No source count is certified by these boundary suggestions. The final finite reduction must include every boundary case actually needed, and its checker must verify the corresponding hypotheses.

## Suggested certificate/checker design

1. Enumerate all 1024 masks at n=3. A deterministic canonical mask sets `s_i=+1` whenever L_i(z)=0, using the actual sign otherwise. Every lambda maximum has exactly one canonical mask. Count only that mask, while using all active masks for the local classification. This avoids tolerance clustering and cross-pattern algebraic duplicate tests.
2. For interior stationary systems, retain exact common-factor identities, a nonzero elimination polynomial, rational root intervals, and exact lifting/coverage data. Generic linear-subresultant lifting is cheap; degenerate fibers require a separate certificate and must not be dropped merely because a denominator vanishes. A rational separating shear may simplify fibers, but nonreduced stationary roots can still be exceptional.
3. One strong optional schema uses a rational univariate representation with parameter t=x+c*y, squarefree p(t), denominator u(t) coprime to p, and coordinate numerators X,Y. With D=det H, identities of the form `D^m*p(t) in (A,B)` and `D^m*(u(t)*x-X(t)) in (A,B)`, likewise for y, prove coverage of every nondegenerate stationary point. The certificate can supply the explicit ideal-combination coefficients, so the checker verifies identities by polynomial arithmetic. Conversely, divisibility after substitution verifies that lifted points solve A=B=0. No uniform exponent m is assumed without checking the actual identities.
4. At n=3 all polynomial coefficients lie in the ordered field Q(sqrt(2)). A small independent checker can implement field elements as pairs of Fractions. Their signs are decidable exactly by rational sign comparisons and squaring. Univariate Sturm sequences work directly over this field, so a rational norm polynomial and conjugate-root filtering are unnecessary. Rational dyadic intervals and exact Sturm counts can establish disjoint root coverage, including endpoint cases.
5. Evaluate lifted coordinates and derivatives in rigorous intervals, with a rationally verified positive sqrt(2) bracket. To decide exact cardinal zeros, split the representation polynomial by a gcd with the composed cardinal numerator where needed; polynomial divisibility proves zero, and a strict interval sign proves nonzero. Apply the analogous test to cardinal gradients at interior zeros. Thus a near-crease point is either proved off the crease or treated as an exact zero.
6. The certificate must account for every signed pattern and every elimination root, including excluded or extraneous fibers, with an explicit reason. The independent checker verifies the certificate rather than repeating the root search. Its actual execution by another subagent and all provenance/output records remain required.

## Execution and status limits

This agent performed only source reads, text searches, and the read-only `git rev-parse HEAD` provenance check. No exact/interval mathematical computation, numerical search, producer run, checker run, or count comparison was executed. There is therefore no independent computational rerun receipt here. The primary developer owns all durable theory claims and counting code; no new theory ID is allocated by this note.

At the time this advice was saved, the complete n=3 producer was reported running by root. Its theory-05 proof and output had not yet been read by this agent. Any later full proof inspection must record the exact file hash and coverage separately. Counts 15/27/25/41/50/62 and interior 7/13/14/25/33/44 remain source MEASURED candidate counts until the entire reduction, rigorous certificate, checker, and independent execution requirements are satisfied.

## Full independent proof inspection of theory-05

At 2026-11-01T09:32:02Z, read and independently reconstructed the FULL file `theory/proof-attempts-2-codex-05-cubic-finite-reduction.md`. Own provenance command `sha256sum` returned:

`ed7e0a82ccf507425d5d6e158bb9cba5adb11ef82f8a4413b4b6e673757c0582`.

The workspace head observed by the read-only provenance command was `24b3f74b0f39d4e49ee8f9333f7819183e3bcd82`; the rules were already read at `3db1eee3fd9507c103c496bdf3da8157331359c5`. No developer file was edited. This inspection is mathematical reconstruction of the supporting theorem, not an execution or an audit of its producer/checker.

**Conclusion within the declared scope:** no mathematical finding identified in the inspected theorem. Its supporting PROVED status is consistent with its stated finite-reduction scope. It does not establish a maxima count. Coverage included every statement item, quantifiers, assumptions, all proof sections, and the limitations/open items.

- The theorem permits an arbitrary finite family of real polynomials of total degree <=3; all-active strict maximality and exact regular-crease/crossing exclusion hold for that generality. They require neither unisolvence nor a Padua identity. The node exclusion is explicitly conditional on cardinal constant reproduction, so it is not asserted for an arbitrary unrelated polynomial family.
- The cubic Hessian and common-factor arguments are valid exactly as stated. Zero derivative polynomials are handled before division. At G=0 the displayed Hessian is an outer product and has rank at most one. A full gcd gives coprime residual derivatives; the alternative exact factorization is acceptable only with the stated nonzero-resultant verification.
- **Projection and degree drops:** a finite common root of the residual equations makes both Sylvester resultants vanish, including a specialization that reduces one or both eliminated-variable degrees. The specialized Sylvester determinant may acquire extra zeros, but this cannot remove a genuine finite common root. Coprime residual polynomials have nonzero resultants in each projection, with nonzero constants allowed. Degenerate constant-polynomial cases have no omitted common root. The proof uses only the implication from common root to projected root and disposes of every Cartesian pair, so no converse, unique fiber, subresultant division, or generic-projection assumption is hidden.
- The field-norm statement is correct for degree-three Padua coefficients in Q(sqrt(2)): a nonzero polynomial has nonzero norm, every real root in the chosen embedding is a root of that norm, and squarefree reduction preserves its distinct real roots. Extraneous conjugate roots/pairs still require valid recorded dispositions, as the theorem explicitly states. Actual Sturm partitions and all-pair coverage have not been inspected here.
- At an open edge, every active restriction must be a strict one-variable maximum. A constant restriction is impossible; a stationary cubic with zero second derivative is odd or flat, so negative second derivative is necessary. Fixing signs of identicallyzero restricted cardinals does not alter the restricted polynomial and cannot remove a tangential candidate. Constant nonzero derivatives produce no candidate, while identicallyzero derivatives correspond to the already excluded constant restriction.
- The sufficient edge test has the correct local sign. Here the factor written `(normal-side)*Q` is understood as `(z_nu-side)*Q` in the physical edge coordinate z_nu, with inward distance u>=0 and `z_nu=side*(1-u)`. Thus `sign(z_nu-side)=-side` inside the square, giving exactly the displayed one-sided sign `-side*sign(Q)`. Nonzero Q and fixed signs of the other restrictions make lambda equal a single smooth polynomial in a relative neighbourhood. A strictly negative inward derivative plus a strict tangential maximum proves a strict relative maximum by local inward monotonicity. A strictly positive inward derivative excludes it. Zero-normal or zero-Q cases are not silently disposed of: the theorem expressly leaves them to separate exact resolution if encountered. It does not claim that its sufficient corner/edge tests decide every arbitrary cubic family.
- At a cardinal node, `lambda=1` and constant reproduction gives `lambda>=1` throughout the square, excluding strict maximality even when the function could be locally constant. At a non-node corner, finitely many active patterns with both inward derivatives strictly negative have a common neighbourhood of strict inward decrease. Nonzero-cardinal signs stay fixed there, so every actual nearby branch belongs to that active set. Their finite maximum therefore decreases strictly. No condition on inactive patterns is missing.
- The interior, four open edges, and four corners exhaust the closed square. The finite sign-stratum description also allows identicallyzero cardinals, singular zeros and disconnected sign sets; no numerical drawing of their curves is required for the all-pattern reduction. Counts remain OPEN until the finite root partitions, all dispositions and independent checker execution are verified.

### Conditional route from the strict list to the cubic global maximum

The additional argument supplied by root/developer was independently checked as a **conditional proof route**, without inspecting or asserting its proposed finite value bounds.

Suppose a cubic P has a non-strict interior local maximum z and singular Hessian. As before, exact restriction to a Hessian-null line is `P(z+t*v)-P(z)=c*t^3`; local maximality forces c=0. Take a small ball on which P<=P(z). Every sufficientlynear point of that line has value P(z) and lies inside this ball, so is itself an interior local maximum of P. Its gradient therefore vanishes. Consequently both derivative polynomials vanish on a real line segment, hence on the whole algebraic line. This contradicts coprimality of the two derivatives (or, equivalently, their finite common-zero set). Thus every non-strict local maximum of a cubic with nonzero coprime derivatives already has negative-definite Hessian and is strict.

For the intended Padua application, it would therefore suffice to verify separately:

1. Every signed polynomial outside a specifically listed flat/univariate exceptional set has nonzero coprime derivatives.
2. Every exceptional signed polynomial has its value everywhere below a rigorously established non-node-corner value.
3. Every edge contains a Padua node. Hence a signed polynomial constant on that edge has constant value +1 or -1, and cannot be active at a global maximum whose value exceeds 1.
4. Every remaining compatible edge derivative root has the exact boundary disposition required by the finite reduction, including any zero-normal case, and corners have their exact dispositions.

Under items 1–2, at any interior global maximum of lambda every active signed polynomial is a non-strict local maximum, lies outside the exceptional set, and therefore has negative-definite Hessian. Every active branch is then strict, and the finite all-active equivalence makes lambda strict there. On an open edge, item 3 excludes constant active restrictions; a nonconstant cubic active restriction has negative second derivative at its maximum. Item 4 must turn the resulting complete edge candidate list into valid relative classifications. A complete strict-maxima list with rigorous value separation would then locate all global maxima.

The developer reported plans to bound exceptional masks by exact interval panels and to verify the coprime/nonflat partition in the checker. This agent did **not** execute or inspect those calculations. No bound such as '<3', no number of exceptional masks, no completed count, and no global argmax is accepted as computational evidence by this receipt.

### Degree-four warning and bounded advice

No part of the just-inspected cubic theorem silently extends to n=4. Besides `-(x^2+y^2)^2`, the quartic `-(y-x^2)^2-x^2*y^2` has a strict maximum at the origin with rank-one Hessian and a vanishing effective quartic along the null direction. Thus simply checking a negative quartic coefficient on the Hessian-null line is not a complete degree-four classification. Coprime quartic gradients are cubics with at most nine complex intersection points, so an exhaustive elimination route remains possible, but degenerate fibers and critical points must be retained. As implementation advice only, opposite masks P and -P share a stationary system, and x-reflection permutes the n=4 Padua masks; verified mask orbits can reduce repeated stationary searches. No degree-four computation or finite coverage claim was made.

## Refreshed full theory-05 and draft theory-06/-07 review

At 2026-11-01T09:44:23Z, with workspace head `c26a6adf6ebf701368f5de73fc319b0e55cdfc13`, independently read the FULL current files below and obtained their SHA-256 values with a read-only provenance command:

| File under `theory/` | SHA-256 at this read |
|---|---|
| `proof-attempts-2-codex-05-cubic-finite-reduction.md` | `042d41b145182d321601db83d748e86278649866e8b6e9211cc13628c1c8816b` |
| `proof-attempts-2-codex-06-degree-three-maxima-count.md` | `cf892c0f16eafdcc55bc33f3c3691834457aa25fe0770ad98a66dca2075e40c3` |
| `proof-attempts-2-codex-07-degree-three-global-argmax.md` | `b1472c2642ee97e0a42de9f98acd36e00a9f6e0359e90ca09945a277a82c5760` |

The refreshed theory-05 reading confirms that its mathematical content is unchanged from the earlier full inspection; its prose-spacing edits introduce no new mathematical finding. The previous receipt remains applicable to the mathematical claims, with the new hash above identifying this refreshed version.

Theory-06 and theory-07 were both explicitly OPEN pending final finite verification and independent execution. This review checks the written mathematical reductions, **not** the producer/checker implementation, certificate bytes, run completion, or numerical values of pending interval fields. It is supplementary to the required Claude audit.

### Theory-06 count reduction

The intended exact board, physical-coordinate types, and 15=7+6+2 count are stated without narrowing the original n=3,...,8 target. Under the stated finite-check assumptions, the proof reduction is mathematically adequate:

- An exact monomial Vandermonde inverse, with its matrix identities, establishes the cardinals and constant reproduction. All 1024 signed cubics must be covered. Common-factor exclusion uses theory-05 only for strict interior maxima; it is not misused to settle non-strict global maxima.
- Complete projection partitions and EVERY Cartesian pair must receive a valid disposition. Uniqueness/injectivity on the whole discarded pair box is essential to the exact-crease exclusion; the prose requires it explicitly. A valid existence box with strict cardinal signs identifies one actual active mask and one strict maximum. Thus other masks cannot duplicate such an accepted interior maximum. Extraneous norm roots and projection pairs still require explicit dispositions.
- The edge reduction must cover every nonconstant restriction, every derivative root and all equality/zero cases encountered. The asserted special identity for L_6 on x=1, the complete list of identicallyzero edge restrictions, the exact factor signs, and the signs of the actual inward derivatives are **finite predicates still to be checked**, not inherited facts from this review. If those predicates hold, all surviving edge candidates have rigorous strict relative maxima and the two part-1 representatives are integrated without reusing the old floating neighbourhood discards.
- Exact corner values and all-active inward derivative tests give the four point dispositions. The separate interior and open-edge enumeration supplies full neighbourhood coverage, so the argument does not depend on the old (D)/(E) handlers.

One **minor clarification requested** in the inspected theory-06 version: proof step 4 says to cover all real roots of the norm of the tangent derivative without explicitly first discarding constant restricted q_s. The all-plus mask gives q_s=1 and an identicallyzero derivative, which has no finite real-root partition. Theory-05 already proves that a constant restriction cannot account for a strict edge maximum, so the mathematical repair is simply to state that constant restrictions are disposed of first, and derivative-root isolation applies to the remaining nonconstant restrictions. This was sent to root and the developer before this append. It is not an obstruction to the stated reduction once that existing branch is made explicit; this review does not assert that the checker already implements it.

### Theory-07 global-argmax reduction

No further mathematical finding was identified in the conditional written argument. Its additional finite assumptions are necessary and are not supplied merely by the strict count in theory-06.

1. The threshold separation is exact: for `C=17/6+(2/3)*sqrt(2)`,

   `C-15/4=(8*sqrt(2)-11)/12>0`,

   since both sides of `8*sqrt(2)>11` are positive and their squares are 128 and 121. This is a handwritten elementary verification, not a run of the finite certificate. The exact cardinal evaluation giving C at both non-node corners still belongs to the pending finite fields.
2. At an interior global maximum with value M>=C>3, every active signed cubic has a non-strict ordinary local maximum. A verified upper bound below 3 for **every** flat mask excludes those masks from the active set. For each remaining mask, constant gcd and nonzero projection resultants put all stationary points in a finite Cartesian set. The null-line argument produces a whole stationary segment if its Hessian is singular, contradicting that finite set. Thus all active Hessians are negative definite, and the finite active/inactive neighbourhood argument makes lambda itself strict. It must occur in the complete strict list.
3. Each edge has a Padua node; at such a node every signed cardinal sum has value +1 or -1. Therefore a restriction constant on that edge must have that value and cannot be active at a global maximum with value at least C>1. Every other active cubic restriction at an edge global maximum has zero first and negative second tangential derivative, so the complete edge enumeration covers it. Derivative/sign mismatch, positive tangential curvature, a regular restricted zero, and strictly positive actual inward derivative all exclude a non-strict global maximum too. The proof additionally requires that **every** surviving compatible candidate, including any potential zero-normal case, receives the claimed negative inward-derivative/strictness disposition. Under that verified condition, each possible edge global maximum belongs to the strict list.
4. Rigorous upper value enclosures below 15/4 must cover every accepted interior and edge root, rather than only rounded representatives. Then their values are below C. Compactness guarantees a global maximum, and the exhaustive interior/edge exclusions leave only the four corners. The node corners have value 1 and the two non-node corners have value C, proving the exact equality set.

The 32-panel flat-mask bounds, non-flat coprime partition, all candidate dispositions, and full accepted-root value enclosures have **not** been executed or inspected by this agent. No status upgrade of theory-06 or theory-07 follows from this mathematical review. The actual producer/checker and independent execution receipts remain separate obligations.

### Disposition of the theory-06 constant-restriction clarification

After the developer's correction, read the changed proof step 4 and obtained the new theory-06 SHA-256:

`189621815f34d81ef358f0a886ae0bda4c61d31f439522338baa5d8a89fe2f17`.

It now explicitly says to discard constant edge restrictions using result05 and only then isolate roots of the norm of the **nonzero** tangent derivative. This resolves the sole clarification requested in the preceding review. The prior complete mathematical inspection plus this bounded changed-paragraph read covers this revised proof version; the finite checks, evidence insertion and any later status changes remain outside this receipt.
