# A5 n4 spatial certificate schema (draft v1, 2026-11-01)

Producer and schema are still under development; any unresolved record blocks a count claim. Separate checker must reconstruct exact cardinals; it may verify supplied trees/predicates but must not rerun a search.

## Exact input and intervals

n4 uses lexicographic `(j,k)` with `0<=j<=4,0<=k<=5,j+k even`, nodes `(cos(pi*j/4),cos(pi*k/5))`, total-degree monomials ordered degree then decreasing x exponent. Reconstruct 15 cardinals over Q(sqrt2,sqrt5) by exact Vandermonde inverse and verify VV^-1=I and sumL=1. Coefficients are a+b sqrt2+c sqrt5+d sqrt10, rational a,b,c,d. All calculations may use Fraction rational intervals; producer instead uses outward fixed dyadics with precision96 and scale S=2^96. Verify radical brackets `r=floor(sqrt(n*S*S))`, interval[r/S,(r+1)/S] for n2,5,10 by exact square inequalities. Every arithmetic operation rounds lower down and upper up; no binary float is a proof predicate.

The polynomial interval evaluation may use a natural monomial evaluation, intersected with the centered mean-value form `p(c)+p_x(Q)*(X-cx)+p_y(Q)*(Y-cy)`, where c is the dyadic midpoint. The checker can reproduce this exact interval algorithm. Polynomial derivative/sum identities are independently reconstructed.

## Whole-square tree and universal sign coverage

Certificate has `format=a5-n4-spatial-v1`, `n=4`, `precision=96`, `leaves`, `interior_roots`, `edges`, `corners`, and exact summary counts. Every leaf has binary `path` and `patterns`. Starting with [-1,1]^2, recursively split the widest side (x on equal width) at its exact midpoint; path0/1 selects lower/upper half. Supplied leaf paths must form a complete finite binary prefix partition of the root. No missing path or unresolved leaf may be accepted.

For each leaf Q evaluate all cardinals. Positive lowerbound forces + sign, negative upperbound forces -, interval containing0 permits either. The top field `pattern_order` is `compatible-mask`. The `patterns` list has exactly one disposition record for every compatible 15-bit mask in increasing order. The mask is derived from its list position; it is omitted from the record because it is redundant. The checker recomputes the complete mask list and requires the exact same length. This enumerates all32768 patterns when necessary; incompatible masks are excluded by a signed-cardinal strict interval bound. The certificate never stops a leaf at the first root. An implementation may use a compact branch record for a uniformly proved predicate, but that extension must be explicit.

## Interior dispositions

For mask m reconstruct P,A=P_x,B=P_y,H. At an interior strict lambda maximum every active P has a strict maximum, so the following predicates are sufficient:

- `flat`: A or B identically0. This P cannot have a strict interior maximum.
- `gradient`: interval A(Q) or B(Q) excludes0.
- `hessian`: interval Hxx has strictlypositive lowerbound, or Hyy strictlypositive lowerbound, or detH strictlynegative upperbound. Equality is not an exclusion for quartics.
- `regular_point`: supplied exact FIELD point p with A(p)=B(p)=0 and a regular zero cardinal (or p an exact node, where lambda>=1=lambda(p)). FIELD uses four rational coefficients in basis1,sqrt2,sqrt5,sqrt10. Supplied rational invertible preconditioner C has `||I-C H(U)||infinity<1` on rational rectangle U containing BOTH Q and p. The exact stationary point is therefore the only stationary point in U, so every stationary candidate in Q equals p and cannot be a lambda strict max. Mere intersection with a node/crease is insufficient.
- `factor`: independently derive exact G=gcd(A,B), a=A/G, b=B/G and F=squarefreepartG, checking A=Ga and B=Gb and nonconstantG. Interval a(Q) or b(Q) excludes0, and interval Fx(Q) or Fy(Q) excludes0. Every stationary point inQ then lies on a regular common-gradient curve, along which P is constant. Isolated-real/singular factor zeros fail this predicate and stay unresolved.
- `root`: reference to one `interior_roots` record with same mask. The root record provides rational box R strictlyinside square, rational C, and exact Krawczyk inclusion `K(c,R) subset interiorR`, contraction norm<1, Hxx(R)<0, detH(R)>0, and every signedL_i(R)>0. These prove a unique smooth lambda strict max inR. Additionally verify injectivity `||I-C H(U)||infinity<1` on supplied U containing Q andR. Thus all stationarypoints inQ are that one root. The leaf need not lieinsideR; the whole convex hull must pass the injection test.

For root records, Krawczyk uses the exact rational midpoint c, `c-C gradP(c)+(I-C H(R))*(R-c)`. C is fixed rational; exactinterval evaluation encloses its action. Preconditioners and candidate centers may be selected by exact rational midpoint / Newton arithmetic and are validated by these predicates. A failed iterate is never a discard.

Distinct root records must have disjoint R boxes, or a separately supplied injectivity proof on their convex hull showing the same root and the same canonical id. Initial implementation uses disjoint boxes and unique ids. One true root appearing in several leaves uses the same id. Count each id once.

## Boundary (final v1 schema)

Edges ordered `(axis,side)=(0,-1),(0,1),(1,-1),(1,1)`. Every restrictedcardinal `r_i(t)` must be a nonzero polynomial. Derive `E=sf(product r_i)` and verify E divides the product of every multiplicity-one factor from the squarefree factorizations of the r_i. Thus every actual E root is a regular zero of at least one restricted cardinal and cannot be an edge lambda maximum, including crossings. No root coincidence tolerance is used.

Each edge provides `E_norm_intervals`, covering all distinct real roots on R of primitive squarefree norm(E) to Q. Verify individual root counts and total count by Sturm, including exact singleton rational roots. `samples` is one rational point before the first interval, one strictly in every consecutive gap, and one after the last interval (or [0] if none). Evaluate all r_i exactly there; signs must be nonzero. `sample_masks` is exactly the sorted distinct masks thereby obtained. Extra conjugate norm roots subdivide true sign regions harmlessly. Every component of R minus the actual E zeros contains a sample, so all noncrease sign patterns occur in this list (proof09).

`patterns` has one ordered record per samplemask with explicit `mask`. If D=q_mask' is identically0, kind=`flat`. Otherwise kind=`roots`, derive `Dr=sf(D)/gcd(sf(D),E)` exactly; removing E roots loses only alreadyexcluded regular creases. Verify supplied `Dr_norm_intervals` cover all distinct real roots of primitive squarefree norm(Dr) on R by the same Sturm conditions. `points` has one record per interval in order, index `i` and code:

- `outside`: interval has no intersection with (-1,1), including singleton endpoints.
- `derivative`: interval Dr excludes0 (wrong embedding / extraneous norm root).
- `sign`: supplied `b`, interval sign(mask,b)*r_b has strictlynegative upperbound.
- `minimum`: q_mask'' has strictlypositive lowerbound. Equality is not a quartic exclusion.
- `root` / `normal`: larger rational `interval` U contains the supplied norm interval and lies strictly inside(-1,1). Every signed r_i is strictlypositive on U, q'' has strictlynegative upperbound, D(Ulo) strictlypositive and D(Uhi) strictlynegative. The inward derivative `-side*P_mask,axis` restricted to edge has strictlynegative upperbound (`root`) or strictlypositive lowerbound (`normal`). `root` has unique global edge `id` in record order. Sameedge accepted U intervals pairwise disjoint. `normal` is excluded. Zero normal or degenerate tangent cases remain unresolved until an explicit extension.

`corners` ordered(-1,-1),(-1,1),(1,-1),(1,1). Each has point and kind=`node` or `max`. Node means exact cardinalvector one1 and fourteen0, so lambda>=1 excludesstrictmaximum. A max record has exact `zeros` indices and next corner `id`. Nonzero signs derived exactly; enumerate ALL active patterns at zeroindices and verify both inward partial derivatives strictlynegative exactly. This proves a strict corner maximum. Any unresolved corner blocks acceptance.

The full certificate summary complete=true only when the whole interior tree, all four edges and all four corners are complete, with no unresolved record. The interior diagnostic flag interior_complete alone never certifies a closed-square count.
