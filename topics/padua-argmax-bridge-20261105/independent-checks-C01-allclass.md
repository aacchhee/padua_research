# C01 all-class half-radius defect: independent mathematical reconstruction

Rules/input: `4b728b04216a5490910780bc609a82b853058426`; main supplied by the coordinator: `f654e32daff27b6846849311092f6daebbbf235b`.
Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.
Frozen proof: `theory/C01-allclass-defect.md`, SHA256 `858634a7f38bbd870fa652e059c1fff72e2102ea3ca374f24506bce0f3f5b9fd`.
Verdict: ACCEPTED for both projected floors and their all-noncorner consequence at the stated n>=64, |alpha|+|beta|<=1/2 scope. No unresolved finding. Formal Claude audit remains separate.

## Scope and reading

This is an independent proof reconstruction of the finite analytic inequality, its normalizations, parity coverage, uniform endpoint budgets and proposed mathematical checker premise. It does not approve new executable source, measured diagnostics, historical novelty or priority. Accordingly the full IDEAS audit is outside scope. The candidate and attempt were read to identify the precise claimed difference and rejected shortcuts; their novelty-gate account is not independently certified here.

Read the frozen proof in full; PD-T364 `phase-structure.md` in full, including its periodic/folded projection and endpoint-multiplicity derivations; PD-T215's full pairwise projection record; N5-03 and N5-04's full finite selections; N3's enclosure and pair-defect implementation reduction; and C1's model comparison. For the present theorem only the exact polynomial/cardinal/projection identities are inherited. Its enlarged phase radius, both parities, horizontal estimates and every numerical lower constant were reconstructed directly below. No asymptotic predecessor or measured output supplies an inequality.

## Exact kernel and weights

Writing x=cos u and y=cos v, at odd integer mesh parity p+q the angle-addition identities give

    (-1)^p P_n(x)=cos(alpha)(1+x)-sin(alpha)sin u,
    (-1)^p P_n(y)=-cos(beta)(1+y)-sin(beta)sin v.

Subtracting (-1)^p cos(nu)=cos(alpha) after division by x-y cancels the x contribution exactly. Dividing by two gives the numerator

    A(u,v)=[cos(alpha)+cos(beta)](1+cos v)/2
           -sin(alpha)sin u/2+sin(beta)sin v/2.

This explicitly preserves the exceptional first-coordinate mode. In a horizontal pair the second angle v is fixed, so its baseline is 1+cos v in both halves. An interchange of the meshes would not justify this calculation.

In each periodic projected profile the coefficient is 1/(4N). Folding the reflected coordinate counts two orientations at each interior physical row and one at endpoints. Replacing both G values by their common-sign halves multiplies the pair defect by 2. Thus the coefficient becomes 1/N with half endpoint weights, exactly as (7) and (8). The horizontal two integers J+j and J-j have the same parity; the signed halves therefore have a common sign. The vertical parity is r+k=J modulo 2, and the horizontal parity is s+j=K modulo 2. All selected physical rows below are interior, so their weight is exactly 1/N. No factor 2 from the physical-edge formula can be imported.

On the whole phase diamond, a>=15/16 and the total absolute sine perturbation in A is <=1/4. A baseline >=2/5 therefore gives A>=1/8; a baseline >=1/2 gives A>=7/32. These bounds require no favorable sine sign. Polynomial collisions in the total identities are preserved; the chosen subsets have strictly separated denominators.

## Near endpoints: all eight selections

For vertical K at distance s=1,...,4 from an endpoint, select n/8-1 or more integers l in [3n/8,n/2]. The four table rows have offsets eta=0,1,1,0 respectively for bottom odd, bottom even, top odd, top even s. Their base displacement has absolute value <=5pi/8. The complete perturbation obeys

    (m/n)|alpha|+|beta| <=65/128 <3pi/8.

It follows that w lies strictly between b-t and b+t. At the lower endpoint, r+k=eta=1-s=J modulo 2. At the upper endpoint, r+k=n+eta=n+s=J modulo 2. This checks every J of the required parity, including even K when n is even; it does not infer missing cases from endpoint J values.

The vertical band bounds reduce to affine functions of n with positive slopes. At n=64 their lower and upper slack expressions are pi/2 and 2pi, both >1/2. Thus b±t stay in [3pi/10,3pi/5] for all n>=64. Both the positive and negative cosine orientations have baseline >2/5: cos(3pi/10)<3/5, and cos(3pi/5)>-1/2. Each denominator is less than the full span 2t<= (8pi+1)/m <27/m in absolute value. The resulting pair defect is >m/108, with at least n/16 selected rows. The normalization therefore gives Q_v>1/1728.

For horizontal J at distance s=1,...,4, take l in [3m/8,m/2]. The four offsets are eta=0,-1,-1,0. The base displacement again has magnitude <=5pi/8, while

    |alpha|+(n/m)|beta| <=1/2 <3pi/8.

Thus w is strictly between b-t and b+t. At the bottom the selected parity is s'+j=eta=1-s=K modulo 2. At the top it is s'+j=m+eta=m+s=K modulo 2. These identities also cover interior K of either parity and both endpoint K classes when their odd-center condition holds.

The weakest horizontal band estimate, after m=n+1, is

    (3n/40-37/8)pi >=1/2.

At n=64 its left side is 7pi/40>1/2, already implied by pi>3. Its slope is positive. The upper-band expression is (n/10-9/2)pi, whose n64 value is 19pi/10>1/2. All subsequent n satisfy both. Since w lies between the targets, the fixed second-angle baseline is 1+cos w at the bottom and 1-cos w at the top, both >2/5. The two actual horizontal numerators are therefore >=1/8 without changing the exceptional mode. Span <27/n gives pair defect >n/108, and at least m/16 rows give Q_h>1/1728.

All chosen physical row indices and periodic representatives are strictly interior to their prescribed ranges at n64; the displayed affine ranges retain this for increasing n. Distinct l values give distinct physical rows. The denominator separation remains strict even when rho=1/2 or an integer lies exactly on a closed selection boundary.

## Remaining centers and uniform parity counts

For vertical endpoint distance at least 5, gamma=min(phi,pi-phi) satisfies gamma>4pi/n. The inequality follows by clearing n(n+1): n(pi-1/2)>4pi, valid at n64 and increasing thereafter. For horizontal distance at least 5, gamma=min(theta,pi-theta)>4pi/m follows directly from (5pi-1/2)/n>4pi/(n+1).

For small gamma, the chosen physical row lies in [pi/3,pi/2], and the periodic angle lies within gamma/2 of it. For vertical pairs both target-angle baselines are >=1/2; for horizontal pairs the fixed periodic second angle lies in [pi/4,7pi/12], whose baseline is >=1/2. Both constructions have pair defect >=7/(32gamma). The physical-row and parity-grid counts are respectively at least M/12 and L gamma/(4pi), with (M,L)=(m,n) vertically and (n,m) horizontally. Dividing by N gives 7/(1536pi).

For middle gamma, choose physical rows in [pi/12,pi/6] and periodic angles within half that row angle of gamma. The relevant vertical targets lie in [0,2pi/3]; horizontal fixed v lies below 7pi/12. Both numerator baselines are >=1/2. The cosine span is <=1, so each pair defect is >=7/16. Physical-row counts are at least M/16, and either shifted parity supplies at least L/48 periodic representatives per row. Their normalized total is 7/12288. These count bounds need only M,L>=48, satisfied from n64.

The infinite shifted-grid count is legitimate: selected intervals lie strictly within (0,pi), and phase shifts have magnitude <=1/2, so no index below zero or at least twice the mesh size contributes an unrepresented point. Reflection of the physical row for centers near the upper endpoint preserves mesh spacing, interior weights and either parity count. Its cosine targets are exactly the displayed reflected targets; no sine equality is needed because sine perturbations were bounded absolutely. At gamma=pi/6 both constructions remain valid.

Finally 1/1728>1/2048, 7/12288>1/2048 and 7/(1536pi)>1/2048 (even pi<4 suffices). These strict constant comparisons prove both claimed floors uniformly, not merely a lower bound along a sampled phase sequence.

## Consequence and implementation boundary

Every noncorner odd center has interior K or interior J. PD-T364 gives Delta>=Q_v,Q_h and lambda=S-Delta, so the corresponding projected floor establishes Delta>1/2048 and lambda<S-1/2048. Actual nonnode corner centers are exactly the remaining odd endpoint pairs; they are excluded, and their zero-phase defect is zero.

The mathematical premise suitable for a future checker is exact integer n>=64 and a validated bound

    max(|alpha_lo|,|alpha_hi|)+max(|beta_lo|,|beta_hi|)<=1/2.

Under that full-box guard, the constant lower bound 1/2048 applies on each admissible noncorner physical intersection. An intersecting-only diamond test is insufficient for whole-box use. True-corner handling stays separate. This proof licenses the analytic premise, not any yet-unreviewed implementation of it. It cannot be used in n32 calibration.

No mathematical computation, numerical scan, new degree, cover replay or optimization was run for this review. The proof alone supports the stated analytic result. The earlier profile-review controls consumed about 2.31 CPU seconds; no consequential run is added here. The primitive upper comparison, far phases, true-corner conditions, effective argmax onset and complete certificate complexity remain unresolved by this theorem.
