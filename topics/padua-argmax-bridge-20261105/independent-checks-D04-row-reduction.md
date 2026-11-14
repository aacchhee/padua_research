# Supplementary independent check — D04 endpoint reference and row reduction

Rules/read input `084a64f6465956f9c75b5538f83752c30318f151`; observed D04
review HEAD `a6d7a788b3ce457a4631bbb507624303240c570c`. Rule and registry
diffs are empty. Reviewer: distinct Codex subagent `/root/d01_far_review`,
parent-requested Astra xhigh; actual serving metadata unexposed. Formal
Claude audit remains separate.

## Prospective bounded controls

Before execution: permit at most 20 process CPU-seconds for a separate
mpmath scalar script. Check three individual half-line expressions,
including t=0 and t=1, and four individual bounded reference rows:
(n,alpha/pi,beta/pi,r)=(16,.95,.02,2),(16,.95,.02,31),
(17,1/5,1/7,3),(17,1/5,1/7,32). These cover left/right folding,
wrapped/unwrapped arguments and both parities. Compare their direct g0
sample sums with the analytic integral and displaced digamma expression,
and check the displayed row comparison bound. Only 66 bounded g0 samples;
no corrected polynomial kernel, native executable, full board, new
quadrature, phase sweep, fit or certified numerical bound. The mathematical
review is independent of these floating controls. Final findings follow.

## Verdict and frozen inputs

**ACCEPTED at the three written supporting-result scopes; no unresolved
finding.** The half-line defect, endpoint reference matching and full-phase
row reduction have the stated quantifiers and constants. The practical
compact M_infty comparison remains **OPEN**, and no runtime, implementation,
phase-box certificate or new argmax onset follows. No author changes were
requested or made. This verdict is supplementary, not formal Claude approval.

All records were read in full and their supplied hashes verified:

| Record | SHA-256 |
| --- | --- |
| [D04-half-line-defect.md](theory/D04-half-line-defect.md) | `593c7e32f2cd4f83a68507e8c25ca26ca7f8e45e4735e20d373cc3efe3404e6f` |
| [D04-reference-matching.md](theory/D04-reference-matching.md) | `bb89a7e3c3b3c174c877e465500ddfd033ceba00e2e578aeae0151856024c622` |
| [D04-row-reduction.md](theory/D04-row-reduction.md) | `2eed7940022efbc0e018ddf6a06da68bb2b40d947af305e28d641c5d4b3050cf` |
| [D04-practical-target.md](theory/D04-practical-target.md) | `d44da0d2ddbb8be1e1f5023c1a1dc8221aea6b687bbc28c16af7152fcca0f7cd` |
| [D04-endpoint-reference idea](ideas/D04-endpoint-reference.md) | `ee89d5e2e5dd3be55191b99bd4597bed4c0dffd654c5e814840a1fc346881b30` |
| [D04-endpoint-reference attempt](attempts/D04-endpoint-reference.md) | `61113092149dc29b7c19c3d57fc529c782513c15f10b5f709911dcacee9732ce` |

The developer's recorded input is
`2db4a226dad798491be3ec2fe5ce0238e21cfaec`. This review checks the above
bytes at its observed later HEAD; it does not claim that later commits
were the input to development. No Git mutation or shared record was made.

## Analytic reconstruction and adversarial cases

**Half-line subtraction.** The residual r_v is continuous at y=pi/2,
decreases from cot(v)-1/v to -2/pi, then increases to zero. Its variation
is exactly `4/pi+cot(v)-1/v<=4/pi`. Comparing any shifted point in each
cell with the cell average costs at most that cell's variation, including
t=0 or1. Summing finite cells first yields the bound without assigning
separate values to divergent sums/integrals. The reciprocal finite defect
is precisely

    [psi(d+t+K)-psi(d+t)-log(d+K)+log d]/h.

Its limit is [log d-psi(d+t)]/h; the truncated cotangent sum and integral
stabilize, with integral -log sin(v). Thus both sign and normalization in
the half-line theorem are correct for arbitrary h>0. A sample at pi/2
adds zero and causes no cutoff ambiguity.

For g0 the two nonzero arcs have integral 2s log sin(v) each. The first
positive distance offset is t_-, and reflection of the second gives
1-t_+. Hence `T0=-2s[Q(h,v,t_-)+Q(h,v,1-t_+)]`, with two errors of
size 4/pi, giving 16s/pi. No pole is sampled. The assumptions for this
second statement retain 0<v<pi/2 from the first; the later application
folds endpoint rows into exactly that range and treats the center separately.

**Actual offsets and right folding.** On a left row, N1-02 gives
t_-=frac((1-s+x)/2+delta), while
t_+=frac((1+s+x)/2-delta). Since ordinary offsets are noninteger,
`1-t_+=frac((1-s-x)/2+delta)`. With d=nu-2delta, their shifted arguments
are exactly j+q_+-delta-k_+ and j+q_--delta-k_-. Thus both digamma
shifts and the sign in Theta follow from the actual mesh, not its limit.

On the right let j=2m-r, s=-beta/pi and z=2pi-v_r. The parity of j
equals that of r. The two cotangents interchange, and w_r changes sign;
after a translation of the integration variable this is precisely the
same folded reference with positive w=a cot(z/2)/2. The u mesh is
unchanged. The ordinary endpoint ranges are j>=R on the left and
j>=R+1 on the right; consequently nu>=2. No exceptional j=0 or right
j=1 chart enters the matching argument.

**Displacement and integer wraps.** Since q_+/- are in [0,1] and
delta<1/4, every displaced unwrapped argument is >=j-1/4. The bound
`psi'(u)<=1/u+1/u²<=2/j` holds already at j=2. Two displacements cost
at most 2nu/(mj)<=3/m, and the logarithmic change costs at most2/n;
together they are <=5/n. The prefactor is
`[2a/(pi² nu)]tau(z/2)`, with `0<=1-tau(u)<=u²`. Multiplying the
prefactor error by |B_j|<=2/nu costs <=a/m², while the displacement
cost is <=10a/(pi² n nu).

The theta values lie strictly between0 and5/4, so only floor values0
and1 occur. A wrap is an exact recurrence term -1/(y-1), not a smooth
Taylor remainder. Its phase location forces alpha+beta>=pi-z. On that
region e=alpha+beta>0, and

    a=(P/2)cot(e/2)<=(P/2)tan(z/2)<=Pz/2.

This gives A_j<=P/(pi m), including the continuous a=0 cases. Also
`y-1>=j-5/4>=(3/4)(j-1)`. Paying both possible wraps therefore costs
at most `8P/[3pi m(j-1)]`. This proves the displayed per-row bound (9),
including phases arbitrarily close to a sampled pole or wrap transition.
At theta=1 the auxiliary Theta is only a finite bookkeeping value;
the theorem does not use it for an actual collision row.

**Endpoint constant and all omitted terms.** Monotonicity of psi and
the C08 trapezoid bounds on [nu,nu+1] give |B_j|<=2/nu for nu>=1.
Thus each Xi is absolutely bounded by4a/(pi²nu²). The exact h/g
recurrences and finite ell_j identity give

    E_(j+1)-E_j=Xi_j(t)+Xi_(j+1)(-t).

All large digamma arguments and j+s denominators are positive for j>=2.
The closed-phase continuation therefore establishes this exact increment
at R=2; no R>=64 numerical tail estimate is being transferred. Summing
the absolutely convergent increments and using C08's accepted limit gives
Delta_R=E_infty-E_R with the correct sign and right-index offset.

On the finite endpoint ranges the reciprocal sums in nu and j-1 are
each <=2H_n. Summing the displacement/prefactor/wrap errors yields

    [20a/pi²+16P/(3pi)]H_n/n+2a/n.

Missing infinite tails start at nu>=m/2. An integral comparison on the
two shifted grids gives `16a/(pi²m)+32a/(pi²m²)<2a/n` for m>=17.
Every omitted endpoint collision has theta=1; the same phase inequality
then gives |Xi|<=2P/(pi m nu)<=P/(pi m). There are at most two such
rows, costing <=2P/(pi n). Their actual polynomial norms are retained
elsewhere, so neither a pole value nor a row is dropped.

The half-line errors sum to32aH_n/(pi²n), since w<=am/(pi nu).
For ordinary central rows, N1-02 gives
`|T0_r|<=4|w_r|/|sin v_r|=a/sin²(v_r/2)<=2a`.
At most m+1 rows lie in the closed central interval, so their normalized
sum is <3a/n. The designated central rows, including any v=pi row,
are excluded. Adding these charges gives exactly

    {[52a/pi²+16P/(3pi)]H_n+7a+2P/pi}/n.

Rows at z=pi/2 are central and their absent Xi terms are included in
the tail bound, avoiding any double count at that partition boundary.

**Row reduction and endpoint limits.** The corrected ordinary identity
uses F=(-1)^delta_r G_n/2 with G_n=D_n-cos(nu); its two cotangent
coefficients and normalization are unchanged. The actual weighted pole
expansion gives `R_r/n=H+T_r/n+epsilon_r` and
`|epsilon_r|<=5(|C|+|D|)/n²`. Dividing by m and using the full
nonendpoint coefficient sum gives10/n²+20aH_n/(pi n²). Exact special
rows incur no r_n or finite-row approximation error. Adding D03's
112PH_n/(pi n) to the reference error gives precisely352P/(3pi),
with no remaining cutoff floor.

At P=0 the perturbation vanishes; at a=0 the reference and all Xi
terms vanish. Their endpoint constants agree by C08's continuous
weighted convention. At phase vertices a=P=0, ordinary weighted factors
are interpreted by their specified continuous values, and polynomial
collisions remain special. The endpoints v=0,2pi and central v=pi are
always special. Signed phases use separate phase reflections and retain
the n and n+1 coordinate meshes. Thus these checks do not require an
interior-only argument or sign-fixed near-domain theorem.

For each fixed endpoint j>=2 the row comparison tends uniformly to Xi;
N1-05's residual and coefficient bounds give the displayed H/m limit.
Adding Xi cancels its two log(nu) terms and reproduces ell_j. This
checks the claimed matching interpretation as well as the final bound.

The condition n>=8R with R>=2 supplies n>=16, m>=17 and R<=n throughout.
For R=2 there are at most eight exact special rows and at most2(n+1)
ordinary H evaluations. These counts do not bound the work needed to
evaluate each polynomial row or each special function/integral.

## Gate and dependency coverage

The full 1112-line state/IDEAS.md read by this worker in D01 remains
unchanged at SHA256
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
That complete read, including obstruction tables, is carried forward only
at these identical bytes. D04 freshly searched half-line, truncated
cotangent, reciprocal, reference matching, digamma, matched defect,
equal-opposite and finite-part terms across the registry, current topic
ideas/theory, the closest predecessor candidates and literature INDEX.
The printed search was capped and is not claimed as a full read of every
matched file. No external source theorem or historical priority claim
is introduced.

Read all D04 records and the complete C08 endpoint-constant proof in this
review. Refreshed the full N1-04 pole proof and the exact N1-05 weighted
normalization, and reread the full IDEA336/337 and H2-H3 candidate records.
The complete N1-02/N1-03/N1-09 and N1-outer/endpoint records, and all D03
records, were read in the immediately preceding
[D03 review](independent-checks-D03-cancellation.md). Full N1-06/07/08,
D01/D02 and C06 source coverage is recorded in the same worker's
[D01](independent-checks-D01-far.md) and [D02](independent-checks-D02-far.md)
reviews. The C05 candidate and endpoint-increment statement/initial
identity were refreshed as a near-only predecessor; its full theorem is
not a D04 dependency and was not newly audited here.

The mechanism is a quantitative continuation of N1-03's symmetric
integral, D03's difference quadrature and C08's endpoint constant.
Its distinct proved property is the actual finite-mesh reference defect
with displaced/wrapped digamma arguments and a summable remainder.
C05/N1-09's near-only finite-h restrictions are not imported. The new
object K_D04 openly retains the original weighted H profile and actual
special polynomial rows. The D03 whole-kernel collision obstruction
therefore still applies to the abandoned unweighted substitution, without
invalidating this bounded-cancellation use. D01's old-model bias is also
retained. Alternatives and the OPEN compact practical target remain
separately recorded; no new negative theorem or priority claim is made.

## Executed controls and evidence

Executed once, after the prospective scope above, from
`/workspace/padua_research`:

```text
python topics/padua-argmax-bridge-20261105/code/post_audit_D04_row_review/check.py
```

The [independent script](code/post_audit_D04_row_review/check.py) is
4748 bytes, SHA256
`8176b43e1b229a188819e0102b1cbe8eb70445327c5f2cd566581cc5c7cf632c`.
It uses only its inline scalar inputs and mpmath, imports no developer
implementation, and records its own identity. Python3.12.14, mpmath1.3.0,
60 decimal digits; process CPU including imports **0.055539 seconds**,
no child process and no failed run. Its 20-second hard CPU cap was not
reached. No timing claim for the analytic review is inferred from this.

The [receipt](evidence/d04-row-review.json) is3990 bytes, SHA256
`daebd80bedeb79cd1e976cc7a6f889cd565ecc5d6b12758fbb173914809d957a`.
All three half-line expressions obey4/pi. The four original-orientation
reference rows reproduce the folded offsets; the first two have one wrap,
the last two none. Their largest |T0-Theta|/(16w/pi) is .063132;
the largest normalized matching error/bound ratio is .078052. These are
**MEASURED** floating controls, not interval enclosures or proof premises.
They do not execute or verify the entire row-reduction model, sum all
reference rows, compute E_R numerically, or cover all phases/degrees.
No new large artifact or external raw data is needed to rerun them.

## Remaining limits

The degree-dependent H sum and exact special rows still require a uniform
joint comparison with M_infty or a separately proved direct certifier.
Validated integral/digamma evaluation, collision membership on phase
boxes, arithmetic errors, an efficient polynomial-row routine, runtime
and a feasible margin/onset are all separate obligations. No native
job, corrected-kernel board, quadrature sweep, fit, cover or degree
certificate was executed here. The accepted supporting theorem does not
resolve those explicitly OPEN tasks or replace the formal Claude audit.
