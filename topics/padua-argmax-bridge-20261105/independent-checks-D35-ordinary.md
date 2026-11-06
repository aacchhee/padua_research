# Independent D35 review — ordinary variation and its two applications

2026-11-06. Distinct checker: Codex `/root/d30_far_review`; developer:
`/root/d22_hard_near`. Requested review allocation: gpt-6-astra xhigh;
actual serving model and effort metadata are unexposed. Developer
allocation was the parent-authorized Astra ultra paper block. Rules read
at input head `eb9329c28be18d77eeb817f634202d626ee11f92`. Sole write
ownership: this report. This is a supplementary independent mathematical
review, not the formal cross-family audit or a PR-readiness decision.

Only file inspection/search, metadata hashing and this report write were
performed. No scientific calculation program, numerical experiment,
scalar source, native/build/phase/board/root/quadrature/degree job, Git
operation or shared-file edit was performed. Symbolic inequalities and
constant arithmetic below were reconstructed as paper arguments.

## Frozen inputs and verdict

All paths are relative to this topic. Byte counts and SHA256 pins match
the parent's request and the developer's final freeze.

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `theory/D35-ordinary-perturbation.md` | 9928 | `9b6a4136a16f1b26d0dd41fb8eff97d606e7c2c9675df78c9e73f79cc05e90d1` |
| `theory/D35-fixed-row-reduction.md` | 3883 | `ac6e1dcf51946c6346d36e2153d90c613cf338aab21fd15f4aa3047c8c09c151` |
| `theory/D35-relative-allowance.md` | 4580 | `ce8db303c9ef0be0952d97bf29da0ded6d65fda905d4ebc46e3b48334275bd24` |

**ACCEPT all three PROVED analytic scopes as frozen.** No unresolved
BLOCKING, MAJOR or MINOR mathematical finding was identified. In
particular the new universal variation estimate and the coefficient 6
are supported by a complete variation count, not by a sup-norm-to-BV
inference. The two applications preserve the exact models and remaining
charges. This acceptance proves no new onset and authorizes no scalar
source or execution. The full D13 vanishing relative remainder remains
OPEN.

## Coverage and candidate gate

Read the rules/workflow/Codex role and IDEA template at the current head;
the complete topic LOG was read in the preceding D30 review in this same
session, with its subsequent entries refreshed through the prospective
D35 allocation. The complete `state/IDEAS.md`, including every obstruction
and disposition table, was also read during that preceding review. For
D35 I refreshed the registry and mechanism searches and read the complete
D35 idea/attempt, D03 joint finite-h candidate, D13 relative candidate and
target, D22 origin candidate, and D25 outer-relative candidate. Current
registry SHA256 is
`d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef`;
literature index SHA256 is
`1f6f2acea05a6c65e11ba54646a6db46dbd5b947bb058f233d11bc542401ae61`.
These agree with the developer's gate pins.

Fresh mathematical reading covered all three D35 files, N2 row
decomposition, N1 cancellation quadrature, D03 cancellation perturbation,
D04 row reduction and reference matching, D05 fixed special rows, D13
endpoint reference and mesh support, D22 origin reduction, D25 outer
relative, D31 relative allowance, D16 actual-origin allowance and D10's
axis obstruction. The eight predecessor hashes in the D35 attempt were
checked and match. Earlier same-session D30 reading also covered the
actual weighted-pole, retained-row and D07 full-telescope dependencies.
Accepted predecessor results are used with their exact scopes; this
review is not a numerical rerun of any inherited evidence.

Mechanism searches included ordinary, perturbation, cancellation,
two-support, sign-stable, paired/reflection, moving-root, root-free,
variation, quadrature and relative, across the registry, local candidate,
theory and attempt records, LOG and literature index. Broad search output
was sometimes truncated; it is not presented as a fresh complete reading
of every unrelated source. No historical-priority or exhaustive literature
claim is being assessed or made. The local comparison is a quantitative
VARIANT of D03/N1, with D22/D25/D31 as application predecessors.

The distinguishing property is verifiable: in the sign-preserved regime,
the symmetric reference has one fixed cotangent branch on each of exactly
two supports. This permits a global two-root count and one additional
stationary point per support. D03 used a coarser all-arcs count. The
candidate's stated kill criteria would detect an internal reference
switch, extra stationary points or omitted pole jumps; none occurs.

The first considered reflected-row candidate is preserved and correctly
abandoned only in its incomplete same-phase form:
`v_(2m-r)(beta)=2pi-v_r(-beta)`, and both the sample shifts and the six
excluded labels obstruct the asserted pairing at unchanged positive beta.
This is not a refutation of every possible paired method. The quadratic
route is deferred, the small-reference sign-stable shortcut is abandoned,
and the full D13 target stays OPEN. PD-N079, PD-N132 and D10's fractional
constant obstruction are respected. No candidate history needs deletion
or replacement.

## 1. Universal variation: all regimes and all cuts

Write `A=|w|`. Periodicity in v and simultaneous reflection of x and v
reduce to `e=dist(v,pi Z)` in `(0,pi/2]`; reflection negates both
cotangents and therefore preserves each absolute-value cancellation,
the perturbation assumptions and variation. E=0 gives f=0 exactly.

When `A<=E`, the actual coefficient maximum is at most `A+E`, and the
reference maximum is A. N1's complete variation bound applies to each
g, including assigned pole values, all sign changes and roots. Thus

    Var(f) <= 8(2A+E)/sin(e) <= 24E/sin(e).

This covers A=E, w=0 and coefficient sign switches. The later support
argument is not used in this regime, so it has no unstated sign premise.

When `A>E`, both coefficients retain their respective opposite reference
signs. A simultaneous coefficient sign reversal leaves g unchanged. Let
their positive magnitudes be `b1,b2 in [A-E,A+E]`, and put
`X=cot(x), Y=cot(x+e)`. Both cancellations vanish where X and Y have
opposite signs. On their two same-sign supports,

    f=-2[min(b1|X|,b2|Y|)-A min(|X|,|Y|)].

For `0<e<pi/2` the supports are exactly
`I1=(0,pi/2-e)` and `I2=(pi/2,pi-e)`. On I1, `X>Y>0`, so the reference
always selects Y; on I2, `Y<X<0`, so it always selects |X|. No reference
switch is hidden inside either support. The sandwich by A-E and A+E
gives `|f|<=M=2E cot(e)`, since the selected reference magnitude never
exceeds cot(e). At e=pi/2 both supports are empty in this sign-preserved
regime, so f=0. Finite one-sided pole limits follow from the same bound.

The perturbed branch can change only at a zero of

    [(b1-b2)sin(2x+e)+(b1+b2)sin(e)]/2.

This numerator is not identically zero and has at most two distinct
zeros in one pi-period. Those are a TOTAL count, not two new roots per
support or per branch piece. A tangent root cannot increase the count.

The agreeing branch is monotone or constant. On the other branch the
actual expressions and stationary equations are:

| Support | Difference f | Stationary equation |
| --- | --- | --- |
| I1 | `-2b1 X+2A Y` | `[sin(x+e)/sin(x)]^2=A/b1` |
| I2 | `2b2 Y-2A X` | `[sin(x+e)/sin(x)]^2=b2/A` |

Both sines are positive on each support and the ratio has derivative
`-sin(e)/sin(x)^2<0`. Hence each displayed equation has at most one
solution on its ENTIRE support. Re-entering the same branch on a later
piece does not create a fresh stationary equation. Cutting at branch
roots and these stationary points gives at most four interior cuts in
total. Constant branches, coincident cuts, double roots, cotangent zeros
and stationary points at a branch root introduce no missing variation.

I also checked the path charge rather than inferring variation from the
supremum. Each support joins a cotangent zero with f-limit zero to a
pole with finite f-limit `a_i`, `|a_i|<=M`. Outside the support f=0 and
the assigned pole value is zero. For N_i interior cuts, the monotone
path variation is at most `|a_i|+2N_i M`, including the N_i=0 case.
Adding the pole jump costs a further |a_i|. The sum over both supports
is consequently

    Var(f) <= 2(N1+N2+2)M <= 12M
           =24E cot(e) <=24E/|sin(v)|.

This accounts for the whole periodic path, including the pole at the
period boundary. There is no variation on the remaining arcs. This
establishes the new universal theorem without a root-separation,
nonzero-coefficient or differentiable-parameter assumption.

## 2. Shifted quadrature and the exact coefficient 6

Centered cells of length pi/n give the periodic BV midpoint inequality
with kernel magnitude at most 1/2. The n samples avoid both poles, so
every sample is a continuity point; a sampled numerator root is allowed.
Pole jumps inside cells, or on their boundaries, are covered by the
variation measure. The argument works for n=1 as well as larger n and
for every shift. Therefore the difference quadrature is at most
`12E/|sin(v)|`.

The operator normalization was checked directly against N2/D03/D04:
the corrected highest first-coordinate coefficient is ONE, N2's signed
Q is divided by two to obtain F, and

    F=C(v)cot(x)+D(v)cot(x+v),
    C=-w+(p-q)/4, D=w+(p+q)/4,
    x=(u_rk-v_r)/2, x_(r,k+1)-x_rk=pi/n,
    S=(nm)^(-1) sum_r sum_k |F_rk|.

Thus `E=P/4` is correct. The reference T0 uses EXACTLY the actual v_r
and actual shifted x_rk of T. It is not a reference evaluated on an
origin grid. The per-row bound is `3P/|sin(v_r)|`, with no missing
factor of two or pi.

The row sum is valid only on the stated complement of A_R, which
contains the first and last R labels, BOTH central labels m-1,m and
EVERY actual polynomial-collision row. In particular the R=2 application
excludes all six fixed labels before collision exclusions. No estimate
for an arbitrary collection of merely interior rows is inferred.

For the remaining rows, the displayed k_r and l_r are positive and at
most n. With beta in `[0,pi]`, the distances satisfy
`d0>=pi*k_r/m` and `dpi>=pi*l_r/m`, including both closed beta endpoints.
The nearest multiple of pi has distance at most pi/2, so the sine chord
bound gives

    1/|sin(v_r)| <= (pi/2)(1/d0+1/dpi)
                  <=(m/2)(1/k_r+1/l_r).

Every positive k and every positive l occurs at most twice. Consequently
the sum over the full ordinary set is at most `2m H_n`; restricting to
an arbitrary subset only decreases this positive majorant. The final
normalization is exactly

    (3P)(2m H_n)/(nm)=6P H_n/n.

For small n or large R where the ordinary set is empty, the assertion is
vacuous and still valid. At all other allowed n>=2 the row exclusions
ensure v is not a multiple of pi and the actual mesh avoids both poles.
Both parities are covered by arbitrary shift. Signed phases use separate
absolute phases without exchanging the n and n+1 meshes. At P=0 the
perturbation vanishes identically.

## 3. Fixed-row application and collision continuation

For n>=8R, R>=2, start at a phase avoiding all polynomial collisions.
Then A_R equals the fixed special set and the exact D04/D05 identity is

    S-K_fixed=(nm)^(-1)sum_O T_r + Epsilon-Delta_R.

Replacing only the ordinary difference estimate gives this complete
ledger:

| Contribution | Preserved/new allowance |
| --- | --- |
| `sum(T-T0)/(nm)` | `6P H_n/n` (new D35) |
| `sum(T0)/(nm)-Delta_R` | `([52a/pi^2+16P/(3pi)]H_n+7a+2P/pi)/n` |
| Weighted pole error Epsilon | `10/n^2+20a H_n/(pi*n^2)` |
| Fixed special polynomial rows | Exact, with original weights |

The second line is the full D04 reference theorem, including its
displaced offsets, half-line defect, endpoint omissions, central
complement and Delta_R. It has not been reinterpreted as part of the new
perturbation theorem. Adding yields precisely the claimed coefficient
`6+16/(3pi)`, while all other terms stay unchanged.

At fixed n,R, D05 proves uniform ordinary-row separation from v in pi Z,
continuity of the complete weighted periodic Phi with integer value 1,
an integrable uniform majorant for the cancellation integral, continuity
of the actual finite-polynomial row norms, and uniform convergence of
Delta_R. Thus S, K_fixed and E35 are continuous on the closed phase
triangle. Collision-free phases are dense because the collision set is
contained in a finite union of affine lines. Passing only the COMPLETE
inequality to the limit proves the closed-domain assertion. Neither g0
nor a separately unweighted cotangent pole is declared to be an actual
polynomial value. R=2 therefore has exactly the six retained rows for
n>=16, including collisions and closed boundary vertices by continuity.

## 4. Near application: unchanged constant and actual origin

The D22/D31 telescope is unchanged:

    delta_a E = delta_a Erow + delta_a Eout + delta_a Eret
                          + delta_a Rmesh +(d/pi)Rlog.

At the actual origin, P=0 makes T-T0 zero on the origin's ordinary
mesh. This equality does not require replacing the actual phase mesh
by the origin mesh. The new phase perturbation cost is at most
`6rho H/n`. The other row-reduction costs remain:

* `4a/n` for the entire central reference complement, including both
  parity-dependent transition rows;
* `20/n^2+40aH/(pi*n^2)` for BOTH absolute weighted-pole errors;
* `rho(2H+10)/n` for D13's endpoint increment with the ENTIRE Delta_2.

Hence D35's row bound has the stated `rho(8H+10)/n`. As in D22,
collision continuation applies to the complete Erow only. The
nonnegative subtracted actual-origin central norms justify the
one-sided retained allowance, and do not give a two-sided relative
retained-row theorem.

The remaining charges match their accepted operators exactly:

    delta_a Eret <= [18a+P(8+L)]/n+(142a+4P)/n^2,
    |delta_a Rmesh|+(d/pi)|Rlog| <= rho(L+7/3)/n,
    |delta_a Eout| <= rho[(35/2)L+75]/n.

In particular D25's Eout retains its two actual shifted Q grids, all
removed initial and central intervals and the finite shift of the
origin profile F0. The D35 reference subtraction has not erased that
separate actual-origin mesh charge.

Collecting constants with a<=1 and P<=rho gives exactly

    Cnear=22/n+162/n^2+40H/(pi*n^2),
    K35=[8H+(39/2)L+286/3]/n+4/n^2.

The logarithmic coefficient is `1+1+35/2=39/2`, in addition to the
8H term. The other linear constants are `10+8+7/3+75=286/3`. The
additional `4/n^2` is retained. Thus the new result reduces only the
old ordinary 112/pi coefficient; Cnear does not change.

Finally, with `u=1-a>=0`, the exact identity is
`E(phi)-E(0)=delta_a E-uE(0)`. D16 controls the SAME actual finite
origin by `|E(0)|<=E0`, so the full `uE0` is required and present. It
has not been replaced by a completed-model origin or by zero. The
result includes phase zero, both axes, the closed rho=1/2 seam, both
parities and polynomial collisions.

Cnear is a positive sum of inverse powers and H/n^2 and decreases for
real n>=32. Writing `K35=(cL+b)/n+4/n^2` gives
`c=8+39/2`, `b=8+286/3>c>0`; its derivative has numerator
`c-cL-b<0`, plus the negative `-8/n^3`. The claimed all-n monotonicity
therefore needs no endpoint computation.

## Final disposition and limits

Accept the three frozen analytic supports without amendment. Their
models, row weights, highest corrected mode, unequal meshes and actual
finite-polynomial collisions agree with the accepted predecessors.
The improved estimate is linear in phase and does not establish a
quadratic primitive modulus, a uniform root-free neighborhood or a
fully vanishing finite relative remainder. Cnear is still positive.
Any physical noncorner comparison, actual-corner result, far result or
new global onset needs its own complete application and evidence. No
existing frozen scalar recipe or accepted degree range is changed by
this review.
