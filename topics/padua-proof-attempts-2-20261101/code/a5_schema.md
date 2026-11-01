# A5 exact certificate schema, v1 (n=3 first)

JSON object (gzip is permitted for the one essential artifact):

```
{"format":"a5-n3-v1", "n":3, "patterns":[PATTERN...], "edges":[...], "corners":[...]}
```

The 1024 pattern records are ordered by `mask`=0,...,1023. Sign at index i is +1 iff bit i is set, else -1. Cardials are independently reconstructed by exact Vandermonde inversion for nodes `(cos(pi*j/3),cos(pi*k/4))`, lexicographic `(j,k)`, j+k even; monomials ordered by total degree then descending x exponent.

PATTERN has fields:

* `mask`: integer.
* `kind`: `flat` or `residual`.
* For `flat`, one gradient component must be identically zero (including constant polynomials), which excludes negative definite Hessian.
* For `residual`: `g`: polynomial encoded as list `[ix,iy,"a","b"]` of nonzero terms `(a+b*sqrt(2))*x^ix*y^iy`, rational strings `a,b`. Derive `A=P_x,B=P_y`, and verify exact divisions `a=A/g,b=B/g` (local symbols a,b unrelated to encoded coefficients). `g` need not be canonical: resultant nonzero ensures coprime residuals; on g=0 det Hessian vanishes.
* `kind` may instead be `unit` with `g`: verify one quotient A/g or B/g is a nonzero constant, so residual system has no solution.
* `xroots`,`yroots`: lists of intervals `["lo","hi"]` with rational endpoints, ordered/disjoint. Each list covers **all distinct real roots on R**, not just the square, of the nonzero rational polynomial norm of the respective residual resultant. Compute Rx=Res_y(a,b), Ry=Res_x(a,b), norm = R * conjugate(R), take squarefree part and primitive normalization. If resultant is nonzero constant its root list is empty. A singleton verifies exact rational root; nonsingleton endpoints must be nonroots and Sturm count exactly1. Verify total listed counts equals total real-root count by sign variations at +/-infinity. Thus no root isolation is run by checker.
* `pairs`: records for EVERY Cartesian pair, in lexicographic (i,j) order; `ij`=[i,j], `code` as below. Pair box Q is xroots[i] × yroots[j]. All codes are verified by exact rational intervals (sqrt2 bounded by a verified rational bracket), polynomial identities, or Krawczyk.

Pair `code`:

* `outside`: at least one coordinate interval has no intersection with (-1,1), including singleton +/-1.
* `gradient`: interval evaluation of A or B on Q excludes0.
* `sign`: `b`=cardinal index; interval evaluation sign[b]*L_b is strictly negative on Q.
* `hessian`: interval evaluation Hxx has lower>=0, or Hyy lower>=0, or detH upper<=0 (at least one).
* `regular`: `point`=[FIELD,FIELD], FIELD=["a","b"] encoding a+b*sqrt2. Exact point lies in Q, A=B=0, some L_b=0 and at least one physical derivative nonzero exactly. Additionally `C` is rational2x2 preconditioner; verify injectivity on Q from ||I-C*H(Q)||infinity<1. This proves the stationary point in Q is the exact regular crease/crossing and therefore excludes a lambda max. No tolerance coincidence.
* `root`: `box`=[["xlo","xhi"],["ylo","yhi"]] is a rational rectangle containing Q, with nonzero widths. `C` rational2x2 preconditioner. Verify Krawczyk K(c,Qbig) strictly inside Qbig and contraction ||I-C*H(Qbig)||infinity<1; H negative definite on Qbig (Hxx upper<0, detH lower>0). Verify all signed cardinals strictly positive on Qbig, and Qbig lies strictly inside square. This proves exactly one lambda strict max in Qbig and covers all stationary points in Q. `id` integer assigned only to accepted root records; distinct accepted root boxes must be disjoint unless same id+verified common root. Initially use pairwise-disjoint boxes and unique ids.

A `root` record may use `point` instead of Krawczyk existence (same FIELD encoding), provided exact A=B=0 at point in Q, with injectivity and negative definiteness on Qbig still verified. This handles rational-coordinate roots without giving zero-width Krawczyk rectangles.

If a pair cannot be disposed of by these predicates, it remains unresolved: extend schema explicitly; never success by depth/tolerance.

Boundary schema will be added before implementation. Interior checker can be implemented independently now. Trusted exact operations: SymPy algebra over QQ(sqrt2), rational Sturm arithmetic, Fraction rational interval arithmetic; no numerical root isolation/checker search.

## Boundary schema (n=3-v1)

`edges` is four EDGE records in this order: `(axis,side)=(0,-1),(0,1),(1,-1),(1,1)`. axis0 fixes x, tangent variable t=y; axis1 fixes y, tangent t=x. `zeros` is the ordered list of cardinal indices whose restriction is identicallyzero. `patterns` enumerates every canonical mask0..1023 whose bits at all zeros indices are0. For a canonical mask derive q(t)=P_mask restrictededge and D=q'(t). Each edgepattern has `mask`, `kind`=`flat` or `roots`. flat requires D≡0. roots has `roots`=[interval...], covering allreal distinctroots of squarefree QQnorm(D) exactly by the same suppliedSturm partitions as the interior. It also has `points`, one recordperroot in order with `i` and `code`:

* `outside`: interval has nointersection(-1,1).
* `derivative`: intervalevaluationD excludes0 (normconjugate root).
* `hessian`: intervalevaluationq'' has lower>=0, precluding cubicstrict tangentmaximum.
* `sign`: `b` nonzeroedgecardinal; sign(mask,b)*Lb|edge has strictlynegative upperbound.
* `regular`: `point` FIELD encoding exactt in interval, D(t)=0 exactly, at leastone nonzero restrictedcardinal=0 with nonzero tangentderivative; q'' excludes0 oninterval so D hasatmostoneroot. No such point can be a relativeλmaximum.
* `root`: `interval`=[rationalLo,rationalHi] nonzerowidth, contains projectedrootinterval, liesin(-1,1). Verify D has oppositeendpoint signs and q'' upper<0 on this largerinterval, proving exactlyoneroot. Alternatively `point` FIELD encoding exactrootinbothintervals gives existence. All nonzeroedgecardinals have strictlyconsistent sign(mask,b) throughoutlargerinterval. For every zerocardinal divideexactly by fixednormalcoordinate−side; quotient restricts toedge and intervalevaluation excludes0. Actual one-sidedcardinalsign is −side*sign(quotient), since inward fixedcoordinate−side=−side*u. `fullmask` is uniquelyderived by these signs plusnonzeroedgecardinalmask; checker verifies it. Inwardnormalderivative ofP_fullmask = −side*∂axisP_fullmask has strictlynegative upperbound onedgeatlargerinterval. Therefore λ coincideswiththissmoothpolynomial in a relative openneighbourhoodofitsuniqueroot, with strictnormaldescent and strict tangentmaximum. `id` enumerates edge maxima0..k−1 globally acrossfouredges in order. Rootintervals on sameedge mustpairwise disjoint. No duplicatemasks sharearoot because signs of nonzero restrictedcardinals arestrict.

A zero-normalcase cannot be acceptedbyroot; remainsunresolved untilanexplicitextension/rigorouslocalargument.

`corners` has fourrecords in order `(x,y)=(-1,-1),(-1,1),(1,-1),(1,1)`:

* `point`=[-1or1,-1or1].
* `kind`=`node` or `max`.
* node: verify exactcardinalvector hasone1 andallother0. λ≥1 globally excludesstrictmaximumatthispoint; arbitrarynearbyedge/interiorpointsalreadycoveredelsewhere.
* max: `zeros` exactindices with Lb(point)=0. Check everyof2^len(zeros) activefullsignmasks, withnonzero signsderived exactly. EveryactiveP must have both inwardderivatives strictlynegative exactly, soeachstrictlydecreasesonall nonzeroinwarddisplacements sufficientlynearcorner. FinitelymanyactiveP andcontinuityofnonzerocardinalsigns implyλstrictmaximum. `id` is0..k−1 forcornermaxima inrecordorder. No approximatecoincidence/discardneighbourhood.

If somecorner cannotbeclassifiedbythesesufficientpredicates, addmorecubiclocalclassification; do notsilentlyassumenode/cornerpatterns.

Boundary extension agreed with checker: `normal` has the same interval, sign, exact quotient/fullmask and strict tangent-root-existence predicates as `root`, but inward derivative has strictlypositive lowerbound. Such a point is excluded from the closed-square maxima count. No id is assigned. The producer explicitly verifies that for n=3 there is precisely one identicallyzeroedgecardinal: edge(axis0,side+1), index6, with first quotient restricting to(2t²+1)/3; it is never identicallyzero and multiplicity1. Checker verifies this rather than assuming it for higherdegrees.
