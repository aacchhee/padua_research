# PD-T?proof-attempts-codex-03 — Exact local certificates for the two degree-three degenerate maxima

Final ID: **PD-T103** (2026-11-01; provisional heading retained as alias; reservation published at `020dcddd36fa1e3254cbf288701d5ab02d27c580`).

ID kind: PD-T.
Aliases: T-A5-partial; degree-three edge degeneracies; cardinal index 6; background critical-point and Hessian certificates.
Split from: the degenerate-point obligation of `PD-T?programme-ideas-claude-06`, OPEN_TARGETS A5-partial at `cadb35066160e466cb1704b9791ad6f374446422`.
Split into: none. Source and crosswalk integration applied during authorized PR finalization; see `../finalization/id-map.json`.

## Statement

Use the even-checkerboard Padua nodes of degree 3 and the cardinal ordering in the frozen `gen4_tests.py:padua`: lexicographic `(j,k)`, retaining `j+k` even. Set

\[
 z_\sigma=(\theta,\phi)=(0,\arccos(\sigma/\sqrt3)),\qquad \sigma\in\{+1,-1\}.
\]

The cardinal function indexed by 6, with grid label `(2,2)` and node `(-1/2,0)`, has value and angle gradient exactly zero at both z_σ. The background formed by excluding that cardinal has exactly zero angle gradient there. On each angle l1 disc

\[
 D_\sigma=\{(\theta,\phi):|\theta|+|\phi-\arccos(\sigma/\sqrt3)|\le21/10000\}
\]

the nonzero-cardinal signs are constant, the excluded cardinal is nonpositive, and

\[
 -\lambda_{\max}(H_{g_\sigma})-\|H_{L_6}\|_2>7/2.
\]

Thus each z_σ is the unique critical point and strict maximum of λ_3 on its disc. This rigorously covers the decimal radius `.002` neighbourhoods of both floating seeds recorded by the frozen search, without identifying those floating seeds with exact roots.

## Definitions

The square coordinates are x=cos θ,y=cos φ. All gradients and Hessians in the statement are in the angle coordinates. Write L_b(x,y) for the polynomial cardinal functions, and use the same notation for their compositions with the cosine map when taking angle derivatives. The background is

\[
 g_\sigma=\sum_{b\ne6}s_b^{(\sigma)}L_b,\qquad
 s_b^{(\sigma)}=\operatorname{sign}L_b(z_\sigma).
\]

The word disc here always means the closed l1 disc in the even angle extension; the corresponding maxima on the closed square are relative to that square. `H` denotes a symmetric 2×2 angle Hessian and `||.||_2` its spectral norm.

## Assumptions

Precisely the degree-three nodes, cardinal ordering and angle coordinates above. Exact polynomial algebra and rational interval arithmetic. No conclusion about unlisted maxima, other degenerate handlers or other degrees follows from the local certificate.

## Status by part

Overall status: **PROVED** (written local proof, exact/rigorous committed checker and evidence, actual independent rerun; Claude audit-01 ACCEPTED).

| Mathematical part | Status / evidence |
|---|---|
| L_6 and its angle gradient vanish at both exact representatives | PROVED; written identity and independently rerun exact checker |
| Both backgrounds have exact critical points, with explicit root enclosures | PROVED; polynomial identities and exact cosine bounds |
| Rigorous background/excluded-cardinal Hessian bound on discs covering radius .002 | PROVED; Fraction interval certificate with margin >7/2, independent rerun |
| Reconstructed list of calls at n=3,…,8 | Verification evidence, MEASURED execution receipt `../outputs/a5_trace.json` |
| Total maxima counts and global search completeness | Not asserted; remain MEASURED / OPEN in the source record |

The three local mathematical parts form this one substantive result. Exact polynomial differentiation, sign checks and the small matrix eigenvalue bound are routine steps of that local result. The source's global counting target is preserved and is not promoted.

## Depends on

`PD-T?proof-attempts-codex-01` gives unisolvence/cardinal normalization for the precise node family, if needed for the interpolation interpretation. The exact checker independently constructs the degree-three monomial Vandermonde inverse, so it does not import the numerical Padua kernel evaluator or an unproved source cardinal formula. Elementary cosine differentiation, the mean-value theorem, an alternating Taylor remainder and the symmetric-matrix row-sum eigenvalue bound supply the interval reduction.

## Checks

The reconstructed n=3,…,8 execution has exactly two `degenerate_max` calls, both accepted at n=3 with Z={6}; there are none for n=4,…,8. That trace is **MEASURED execution evidence**, not a proved search-completeness statement. This record's mathematical assertion concerns the two exact representatives and their local neighbourhoods.

From the repository root, root reconstructs every call by subclassing the frozen certifier and logging the existing method without changing its inputs or source:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-proof-attempts-20261101/code/a5_trace.py > topics/padua-proof-attempts-20261101/outputs/a5_trace.json
```

Developer exact command:

```text
python topics/padua-proof-attempts-20261101/code/a5_exact_certificate.py > topics/padua-proof-attempts-20261101/outputs/a5_exact_certificate.json
```

Python 3.12.14, SymPy 1.14.0; deterministic, no seed or tolerance in proof inequalities. The developer command completed successfully. The code constructs exact polynomial cardinals using a 10×10 inverse over algebraic coefficients, verifies symbolic identities and bounds every sign and Hessian entry using `fractions.Fraction` intervals. It separately verifies rational cosine bounds for the angle root intervals. The trace's IEEE doubles are converted to their exact binary rational values only for the finite seed-enclosure comparison. Trace arithmetic is not used to justify a mathematical identity.

Script SHA-256: `ffcc1508176aa0b60a0a709d41a6e736ca0a4b38ec8aa436d5d706f800431c84`. Developer output SHA-256: `279c8e7ca9c4781bb3c528a21f870162aab8402ea219e3ec339c4b9d676d25f3` (7,011 bytes); root trace SHA-256: `093fe1d4171f4416e28ba5e269f30378f4e32165f03bc5969a5d94919e92d468`.

Independent Codex agent `/root/a1_develop` actually executed the default exact command separately, producing `../outputs/a5_exact_independent.json`, byte-identical to the developer receipt, and inspected the complete mathematical proof with no finding. Its commands, coverage, identities and dependency limitations are in `../independent-checks-a5.md`. Its proof inspection preceded the administrative status/evidence update only; the mathematical argument is unchanged. The ordinary trace's candidate counts reproduce the frozen output; this is not certification of those counts. Essential evidence is small and committed; no cold-storage dependency is needed for this proof.

## Sources

Frozen task/source definition: `topics/programme-ideas-20261031/OPEN_TARGETS.md` A5-partial and A5, `audit-01.md` A1, `audit-support/proposal-review.md` P1, source THEORY -06 and `checks/code/response-02/padua_n3_edge_identity.py`. The source factorization was already identified; this work reconstructs it and adds exact backgrounds, enclosures and rigorous neighbourhood Hessian bounds. No new historical novelty claim or primary-source reading is asserted here.

## Proof or evidence

### 1. Reconstruct every use and distinguish exact roots from floating seeds

The wrapper logs every invocation, including unsuccessful invocations if any. Its six-degree receipt records:

| n | All `degenerate_max` calls | Accepted calls | Z |
|---|---:|---:|---|
| 3 | 2 | 2 | {6} in both |
| 4 | 0 | 0 | — |
| 5 | 0 | 0 | — |
| 6 | 0 | 0 | — |
| 7 | 0 | 0 | — |
| 8 | 0 | 0 | — |

No unsuccessful call is omitted. Separate corner and edge-node handlers are not this method and are outside the requested obligation.

| Decision | Floating seed (θ,φ), for identification only | Exact representative | Certified l1 seed distance upper bound | Frozen radius / proved radius |
|---|---|---|---:|---|
| n=3, call 1 | `(1.0373742372379587e-18, .9553166181245092)` | z_+ | 47/(5·10^17) | .002 / .0021 |
| n=3, call 2 | `(3.8340212234672264e-18, 2.186276035465284)` | z_- | 9/(25·10^16) | .002 / .0021 |

The checker compares exact binary rational seeds to the rational enclosures below and proves that each entire frozen-radius disc about its seed lies in D_σ. In particular it does **not** assert that the small nonzero machine θ values equal zero, or that arbitrary rounded φ values are exact critical points. This explicitly interprets the requested degenerate identities at the exact representative of each numerical decision.

### 2. Exact cardinal identity, background signs and stationary points

In the order b=0,…,9, the node labels are

\[
 (0,0),(0,2),(0,4),(1,1),(1,3),(2,0),(2,2),(2,4),(3,1),(3,3).
\]

Exact interpolation gives

\[
 L_6(x,y)=\frac{(x-1)(2x^2+x+2y^2-2)}3.
\]

The exact checker verifies this by constructing V and V^{-1}, checking VV^{-1}=I and extracting the seventh cardinal polynomial. Alternatively its values can be checked directly at the ten nodes, and unisolvence from result 01 gives uniqueness. At x=1 the polynomial and every y derivative vanish identically. In angle coordinates

\[
 \partial_\theta L_6=-\sin\theta\,(L_6)_x,\qquad
 \partial_\phi L_6=-\sin\phi\,(L_6)_y,
\]

so both derivatives vanish at z_σ.

The background sign vectors, with a zero at index 6, are

\[
 s^{(+)}=(1,1,1,1,-1,-1,0,1,1,-1),\quad
 s^{(-)}=(1,1,1,-1,1,1,0,-1,-1,1).
\]

The resulting explicit polynomials satisfy g_-(x,y)=g_+(x,-y), where

\[
 g_+(x,y)=\frac{4x^3+4x^2y+4x^2+2xy-x
 -(8+12\sqrt2)y^3+(2+12\sqrt2)y-1}{6}.
\]

Their interpolation values are precisely those sign vectors; the checker derives the same polynomials from the exact cardinal inverse. Along the edge,

\[
 (g_+)_y(1,y)=(4+6\sqrt2)(1-3y^2)/3.
\]

More generally, exact differentiation of the explicit polynomial gives

\[
 (g_+)_y=\frac{2x^2+x+1+6\sqrt2-(12+18\sqrt2)y^2}{3}.
\]

At x=1,y=1/√3 this is zero. Reflection gives the other background root. The θ derivative vanishes at θ=0 by its sine factor, proving ∇g_σ(z_σ)=0 exactly. The Lebesgue value at both points is

\[
 \lambda_3(z_\sigma)=1+8\sqrt3/27+4\sqrt6/9.
\]

### 3. Rigorous angle enclosures

The unique roots φ_σ of cos φ_σ=σ/√3 in (0,π) lie in the following exact decimal-rational intervals:

\[
 \phi_+\in[.955316618124509278,.955316618124509279],
\quad
 \phi_-\in[2.186276035465283960,2.186276035465283961].
\]

Both widths are 10^{-18}. This is an exact interval calculation, not a high-precision numerical observation. The code verifies by rational squaring the brackets for √2 and √3 with denominators 10^30; for example the lower √3 numerator is `1732050807568877293527446341505`, and its upper numerator is one larger. For any rational endpoint t used above (0<t<3), define

\[
 C_m(t)=\sum_{k=0}^m\frac{(-1)^k t^{2k}}{(2k)!}.
\]

The terms decrease from k≥1 since t²/[(2k+1)(2k+2)]<9/12. Hence C_41(t)<cos t<C_40(t). Exact rational endpoint comparisons give cos(lo)>σ/√3 and cos(hi)<σ/√3. Strict monotonicity of cosine on (0,π), and 3<π, prove the enclosures. No sine or arccos implementation is trusted by this root check.

### 4. Proved finite interval reduction for the Hessians

Let ρ=21/10000 and a=σ/√3. Every point in D_σ maps into

\[
 X=[1-\rho^2/2,1],\qquad Y=[a-\rho,a+\rho],
\]

because cos θ≥1−θ²/2 and cosine is 1-Lipschitz. Also |sin θ|≤ρ and |sin φ|≤1. Thus, for any polynomial f, its angle Hessian obeys

\[
 H_{tt}=(1-x^2)f_{xx}-xf_x,\quad
 H_{pp}=(1-y^2)f_{yy}-yf_y,\quad
 |H_{tp}|\le\rho\sup_{X\times Y}|f_{xy}|.
\]

The script substitutes exact rational intervals for X,Y and the verified radical brackets into these finite polynomial expressions. Its interval operations add endpoints, multiply by taking all four endpoint products, and use monotone integer powers (with zero included for even powers across zero). Reciprocals are used only on intervals excluding zero. Each operation is inclusion-preserving; induction on the expression gives an enclosure of each polynomial's range. All final displayed bounds are rounded outwards using exact integer division.

For a symmetric matrix with diagonal enclosures A,B and |offdiag|≤c,

\[
 \lambda_{\max}(H)\le\max(\sup A+c,\sup B+c),\qquad
 \|H\|_2\le\max(\sup|A|+c,\sup|B|+c).
\]

These follow either from the row-sum bound or from bounding the quadratic form's cross term by c(u²+v²). Therefore only the finite interval expressions above need checking; no floating eigenvalue solver or global Bernstein estimate enters the proof.

Both signs σ give the same following rigorous bounds on the larger radius .0021 discs:

| Quantity | Rational enclosure/bound |
|---|---|
| (H_g)_{tt} | [−4138027/10^6, −2059879/500000] |
| (H_g)_{pp} | [−2437681/250000, −189421/20000] |
| |(H_g)_{tp}| | ≤7/2000 |
| −λ_max(H_g) | ≥2058129/500000 = 4.116258 |
| ||H_{L_6}||_2 | ≤111763/200000 = .558815 |
| Direct interval lower bound on their difference | ≥889361/250000 = 3.557444 > 7/2 |
| Direct bound −λ_max(H_{g−L_6}) | ≥1780363/500000 = 3.560726 |

The difference bound is computed before outward rounding its two constituent quantities; even subtracting the displayed conservative bounds gives 3.557443>7/2. For comparison only, exact differentiation at the centres gives

\[
 H_g(z_\sigma)=\operatorname{diag}\left(-19/6-5\sqrt3/9,
 -8\sqrt6/3-16\sqrt3/9\right),\quad
 H_{L_6}(z_\sigma)=\operatorname{diag}(-5/9,0).
\]

The centre quantity used by the source's `mu0` formula is therefore exactly

\[
 \mu_0=47/18+5\sqrt3/9\in[3.573361,3.573362].
\]

The neighbourhood result above, rather than the final digits of an old floating `mu0`, is the rigorous replacement bound.

### 5. Signs, smoothness and local uniqueness

Every b≠6 satisfies s_b^{(σ)}L_b>0 on X×Y; the smallest certified lower bound over both signs is 1313/500000=.002626. The full per-cardinal rational bounds are in the receipt. Also

\[
 2x^2+x+2y^2-2\ge830907/500000>0
\]

on those boxes. Since x≤1, L_6≤0 there. Consequently λ_3=g_σ−L_6 throughout D_σ; the absolute value at the degenerate zero is represented by this single smooth polynomial in the angle variables. Both terms have zero angle gradient at z_σ.

By the Hessian bounds, H_{λ_3}≼−(7/2)I on the convex disc D_σ. Integrating its quadratic form along the segment from z_σ to any other point z in that disc gives

\[
 \lambda_3(z)\le\lambda_3(z_\sigma)-(7/4)\|z-z_\sigma\|_2^2.
\]

Hence z_σ is its unique critical point and strict maximum. The cosine map gives the asserted relative local maxima on the square edge x=1. This proves the three local obligations for both exact representatives. ∎

## Scope

This is the local degenerate-point obligation for the two decisions reconstructed from the n≤8 run. No identity is asserted at the literal rounded seeds. No proof of full maxima counts, no correction of a published count and no repair of unrelated box-discard logic follows. The radius .0021 is deliberately larger than the old .002 to cover the exact root enclosure, floating seed displacement and radius representation.

## Open items

Claude audit-01 is ACCEPTED. Obligation (2) is discharged for the `degenerate_max` path only; rigorous versions of the (D) corner and (E) edge-node certificates in `t3_degenerate.py` remain needed. The four other A5 obligations remain unresolved: (1) a proved finite reduction covering all maximum types and all search regions; (3) rigorous per-pattern root enclosures/exclusions on the whole region actually discarded; (4) all consistent sign-pattern decisions without the early return after one accepted root; (5) exact crease-crossing treatment replacing the 1e−10 near-coincidence rule. Global rigorous arithmetic and an independent counting checker are also still needed. The source's six candidate counts remain MEASURED.

## History

2026-11-01, Codex `/root/input_review`, assigned gpt-6.1-sol xhigh; resolved runtime metadata not separately exposed. Rules/source SHA `cadb35066160e466cb1704b9791ad6f374446422`. Development began after A1 and B5 reached their done criteria. Root supplied the all-call trace; this developer derived the exact backgrounds, roots and interval certificates. The original target's wording about numerical z_s is preserved as context, with the exact-representative/enclosure distinction stated explicitly rather than equating a floating iterate with an exact zero. After `/root/a1_develop` completed its separate exact run and proof inspection with no finding, the local result was promoted from verification-pending OPEN to PROVED. Required Claude audit remains pending. No existing source record was edited.
