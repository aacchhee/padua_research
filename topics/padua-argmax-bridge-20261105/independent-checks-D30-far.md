# Independent D30 far review — three frozen paper scopes

2026-11-06. Distinct checker: Codex subagent `/root/d30_far_review`;
author: `/root/d14_grid_norm`. Requested review allocation: gpt-6-astra,
xhigh. Actual serving model and effort metadata are unexposed; this record
does not certify that the requested model served. Rules/input head read:
`4f8c169171e55b7d5f00f57a8b3ce8340a498960`. This is a supplementary
independent mathematical check, not the formal cross-family audit or PR
readiness decision. Scope was bounded adversarial PAPER review, with sole
write ownership of this file. No scientific computation, scalar source,
native/build/phase/board/root/quadrature/degree job, Git operation, registry
edit or numerical endpoint evaluation was performed.

## Frozen inputs and verdict

Paths below are relative to this topic directory. All three byte counts
and SHA256 values were checked against the parent's pins before review.

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `theory/D30-wide-retained-rows.md` | 9493 | `39d9f2f5b3626aa6af4412a189c3788071ddde09e71b692050ccca854da2f1ac` |
| `theory/D30-inner-constant.md` | 3025 | `50d48871c104ceecc8312621d95e20398fca04fea85c1d78b390e57d4b844298` |
| `theory/D30-two-region-far.md` | 8731 | `b562020cce61772dab9c7241c5924cec6c00c95ae17ff5820775140c49c5edb7` |

**ACCEPT the three split paper results in exactly their stated scopes.**
No unresolved BLOCKING, MAJOR or MINOR finding was identified. The first
two supply proved analytic support, and the third proves a sufficient
implication with explicit accepted dependencies. BOTH inequalities
`F_inner(2048)>0` and `F_outer(2048)>0` remain **UNCOMPUTED**. This verdict
does not accept an unconditional far2048, near2048, actual-corner2048 or
global2048 theorem, and releases no computation. A failed sufficient gate
would not refute the actual far inequality.

## Read coverage and candidate gate

Read the rules, workflow, Codex role, IDEA template, the complete topic
LOG and current open campaign handoff, and the complete `state/IDEAS.md`,
including all obstruction and disposition tables. Read D30's complete idea
and attempt records and all three theory inputs. Read the relevant full
D07, D20 and D24 candidate entries. Mechanism searches included retained
rows, six rows, finite-h, two-region, fractional/quadratic constant bounds,
C01 and C08 across the registry, candidate/theory records and literature
index. No new candidate or historical-priority claim is made here.

Mathematical dependency reading included C01-near-central-upper,
C06-far-full-profile, C08-far-model-comparison,
C08-far-weighted-coefficient, D04-reference-matching,
D05-fixed-special-rows, D07-endpoint-finite-h,
D07-endpoint-central-rows, D07-endpoint-six-row-allowance,
D07-global-mesh, D07-global-outer, D10-axis-obstruction,
D16-phase-allowance, D20-global-retained-rows, D20-global-error,
D20-far-comparison, D24-extended-constant, D24-far-constant,
N1-round4-rows, N1-round5-endpoints and N1-regularized-pole. The relevant
operator, coefficient, collision and telescope arguments were checked
directly. This does not claim a fresh numerical audit of the inherited
limiting-origin Arb dependency.

The closest comparisons are D07's literal half-radius retained-row proof,
D20's global six-row full-profile budget, and D24's directional constant
modulus and global far constant. D30's distinguishing work is the fresh
three-quarter-domain endpoint/central proof, the away-from-zero `11u`
corollary, and retaining `a=1-u` in the inner error allocation. The phase
partition, error-to-phase ratio and monotonic transfer are standard
variants. The candidate record retains the rejected unsupported transfer
of the old half-radius constants and the central-integral/actual-row
substitution, as well as the old global allowance baseline and deferred
refinements. Those dispositions are appropriately scoped. Literature
coverage was a mechanism search, not a complete independent reading of
the literature index or a priority investigation; no exhaustive novelty
claim is supported or needed.

## 1. Actual retained rows on the wider closed domain

The operator match is literal: `G=D-cos(nu)` with highest first-coordinate
coefficient ONE; `F=(-1)^delta G/2`; `n` signed samples of parity opposite
to the row; normalization `1/(nm)`, `m=n+1`; and the four endpoint labels
`0,1,2m-2,2m-1` plus central labels `m-1,m`. The comparison is the SAME
`C2=ell0(beta)+ell1(alpha,beta)+ell1(alpha,-beta)+ell2(alpha,-beta)`
used in D04/D07/D20. Evenness in the row angle identifies the two right
endpoint rows without swapping the unequal coordinate meshes. Separate
absolute phases define the signed comparison objects; the proof makes no
false claim that each raw row label is individually beta-even.

The wider domain is freshly checked, not inherited from rho<=1/2:

* For rho<=3/4, `a>=55/64`, `P<=3/4`, and `v<7/33<pi/2`. The complete
  numerator of `2F` is at least `2a-P>=31/32`. Therefore the denominator
  determines the sample sign, with positivity exactly at `|z|<mu*w`.
* With `k=r+/-j` equal to 1 or 3, `w+/-z>=k*pi-rho>(19/8)k`, and subtracting
  `w/m<7/33<1/4` yields `mu*w+/-z>(17/8)k`. First excluded samples satisfy
  `|z|>w>mu*w`. The complete positive sets are `{0},{0},{-1,1}` for the
  three nonzero endpoint cases, with every listed sample present for both
  parities at n>=32. The closest row has no positive sample.
* At beta=0 the linked limit is
  `sin(beta)cot(beta/(2m))->2m`; consequently `T0=n(a-m)` and
  `R0=n(m-a)`. There is no invalid zero-times-pole substitution.

I reconstructed the finite identity (8) by factoring
`cosu-cosv=Dh*K/(2n^2)` and subtracting the displayed ell term. The partial
fraction identity

    mu/Dh-1/D = (1/(2m)) sum_(+/-) 1/[(mu*w+/-z)(w+/-z)]

is exact and nonnegative. The new denominator sums are
`sum 1/Dh<=512/867` and `S<=3584/2907<5/4`. The four negative `-a/m`
terms must remain grouped with their displacement `4a*S/m`: the result
lies in `[-4a/m,a/m)` and therefore costs at most `4a/n`. This cancellation
survives the wider-domain sum bound; it does not require the old `S<1`.

The remaining constants check separately: `K>49/50`,
`|H-1|<19/n^2`, total H cost `<90a/n^2`, and sine cost
`(358400/42483)P/n<=9P/n`. The three nonzero w values sum to
`4pi-beta`. Taylor gives `sin(beta)>=29beta/32>=beta^2` on this wider
interval, so the combined tau cost is at most `4P/n^2`. At beta=0 all
tau terms vanish in their linked forms. Thus the old `7P` and `71a`
constants have correctly been replaced, giving

    |Jend-C2| <= (4a+9P)/n + (90a+4P)/n^2.

For the two central rows, I checked that the invoked C06 inequality is
its n>=2 proof component, not the assembled n>=10^6 theorem. It is the
whole weighted periodic-Phi inequality, extended to finite-polynomial
collisions, with `Phi(integer)=1`; no unweighted pole is assigned a
value. It applies at v=pi, on both axes and at double collisions. The
N1 bound `|Phi0|<=4` supplies the stated central estimate.

Here `ce,cd>=119/128`, `ce*cd=a`, so `ce+cd<=256a/119`. The actual angles
are within pi/m of pi, hence `sin(v/2)>99/100`, `|cot(v/2)|<=pi/m`,
`V<=51200a/11781<(9/2)a`, and
`|C|+|D|<=P/2+a*pi/m`. Summing both actual rows gives

    Jcen <= 9a/m + 2PL/(pi*m) + 4aL/m^2
                         + 5P/(m*n^2) + 10pi*a/(m^2*n^2).

Using `L<=n/4`, the two small a terms cost at most a/n: one can use
`n^2+40/n<=(n+1)^2`. The two P terms cost at most `P(L+1)/n`. Consequently
the same central bound `(10a+P(1+L))/n` is valid on the genuinely wider
domain. Its nonnegativity is the actual absolute-row definition. Adding
the endpoint bound proves

    |J6-C2| <= [14a+P(10+L)]/n + [90a+4P]/n^2.

All endpoints of the phase domain and both n parities are covered. The
optional uniform corollary `[43/2+3L/4]/n+93/n^2` also checks, but the
phase-aware form is the one needed by the inner gate.

## 2. True constant on the closed inner strip

The accepted D24 directional modulus includes the positive fractional
term and both entropy terms. On `1/2<=x+y<=3/4`, splitting
`log(1/x)=log(1/rho)+log(rho/x)` and using `log(1/rho)<7/10` bounds the
nonfractional part by

    (197/120)x^2 + (16/15)y^2 + (5/8)xy.

The relative entropy products obey `x^2 log(rho/x)<=xy` and the analogous
y inequality, with continuous zero products at the axes. The tangent
bound `sqrt(x)<=(x+1/2)/sqrt(2)` combines with `rho>=1/2` to give
`x^(3/2)<=sqrt(2)x^2+xy/sqrt(2)`. Its weighted contribution is at most
`(16/21)x^2+(8/21)xy`. The resulting coefficients
`673/280,16/15,169/168` agree with the paper.

Weighted Young with cross coefficient `21/20` has positive determinant
`7/1600`, and yields at most `(729/280)x^2+(37/15)y^2`. Finally
`u>=61(x^2+y^2)/256` and `729/280<671/256` strictly, while
`x^2+y^2>0` throughout the strip. Therefore `DeltaC<11u` is strict even
on axes and the two seams. No fractional term was discarded. This
away-from-zero result does not challenge D10's positive fractional-axis
obstruction to a quadratic estimate through the origin.

## 3. Complete full-profile budget and the conditional application

I matched D30's displayed D, KD, Gg, Mesh, W, G0 and E0 against the
accepted D20/D16 functions and checked the exact telescope. It retains
the ordinary folded indices `k=2,...,m-2` on both sides and the literal
six-row set. `Delta2=E_infty-E2` has the required sign, with unchanged
`E2=C2+D0*H2+B0*G2`. The mesh spacing is pi/m. The accounting is

    Gintermediate-M_infty = (J6-C2)+Rmesh+(d/pi)Rlog,
    |S-M_infty| <= D+KD*P+Gg+|J6-C2|+Mesh+W.

D contains the complete D04 ordinary-row remainder. Gg is the global
outer bound, not the half-radius outer estimate. Mesh and the central
log charge W remain present. Ordinary collisions are not removed and
the argument is applied to actual phases before scalar majorization.
The old fixed-strip collision terms belong to a different telescope and
are not missing from this one.

The origin allowance is exactly
`E0=D+G0+Mesh+14/n+71/n^2`, controlling the ACTUAL finite origin value.
Using the old 71 here is legitimate: the origin remains inside the old
half-radius proof. Replacing it by a completed-limit constant, or setting
a separate origin error to zero, would be invalid; D30 does neither.

On the inner strip the error is exactly bounded by
`Cbase+A*(1-u)+K_inner*P`, with
`A=14/n+90/n^2` and `K_inner=KD+(10+L)/n+4/n^2`. The accepted C08
FULL logarithmic coefficient bound is the one giving model loss
`u*T-DeltaC`; a comparison to a-times the origin coefficient is not
substituted. The cosine lower `u0=191/6144` is valid at rho>=1/2, and
`P<=s(u)=min(2,sqrt(8u))`, with `s0=sqrt(191/768)`.

After dividing by u, the full inner error quotient is

    (Cbase+A+E0)/u + K_inner*s(u)/u - A.

It decreases on `[u0,1]`; `s(u)/u` is decreasing on both sides of u=1/2
and agrees at the seam. This establishes the claimed inequality with

    F_inner=u0*(T-11)-Cbase-A*(1-u0)-K_inner*sqrt(191/768)-E0

without presuming the sign of F_inner.

On rho>=3/4 the retained bound is the OLD GLOBAL
`E6old=(193+21L)/n+21600/n^2`, so `Cnew=Cbase+E6old`. The wide bound
is not extrapolated beyond its domain. The cosine lower is
`u_eta=2277/32768` and its sine majorant is `sqrt(2277/4096)`.
D24's strict `DeltaC<(25/2)u` retains its explicit inherited PD-T271
limiting-origin Arb dependency. The same quotient argument gives

    F_outer=u_eta*(T-25/2)-Cnew-KD*sqrt(2277/4096)-E0.

The limiting-origin premise and E0 have distinct roles and are both
present. Neither is newly numerically verified by this review.

For all-n transfer, `log(2048)>759/100` and `pi^2<10` give the displayed
exact rational lower `T(2048)>129789/6250>25/2`. Also T increases for real
n>=2048. I checked positivity and componentwise monotonicity of the
old charges, rather than assuming Cbase decreases merely because Cnew
does. For example the global outer expression can be collected as

    Gg = [7MA*L+111/2
       +(63+log2+4logpi+7logm+16log(2m)+(3/2)gpar)/pi]/m.

Each term decreases for n>=32; in particular `m*gpar'<1<gpar` and
`d(L/m)/dn=(1+1/n-L)/m^2<0`. D, KD, G0, Mesh and W have the accepted
componentwise decreasing bounds. The added A decreases, as does
`(10+logn)/n`, whose derivative is `(-9-logn)/n^2`. Thus both proposed
gates strictly increase for real n>=2048.

If BOTH gates are positive at the fixed endpoint, the phase ratios are
at least one and the stated uniform strict gap follows for every integer
n>=2048. The closed inner and outer regions overlap at rho=3/4 and cover
the entire closed far diamond, including rho=1/2, rho=pi, axes, a=0 and
polynomial collisions. This proves the sufficient implication only.

## Disposition and remaining obligation

Accept the three frozen paper scopes without mathematical amendment.
Preserve the original far2048 target as OPEN. The next application still
requires the two directed endpoint signs with every displayed charge
included, under a separately frozen and independently reviewed numerical
specification/source and root release. This report neither evaluates
those signs nor authorizes retuning, scanning, fallback jobs or a change
to any accepted old onset. The first D30 candidate and its rejected and
deferred alternatives remain intact.
