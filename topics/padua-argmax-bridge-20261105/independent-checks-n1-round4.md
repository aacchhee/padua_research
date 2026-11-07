# Independent supplementary review of N1 round 4

Reviewer: distinct Codex `/root/review_n1_round4`, requested Astra high;
serving metadata are not independently exposed. Rules AGENTS, WORKFLOW
and CODEX read at `121ae257a71564025ddc2da8f53d19478f5d7dd4`.
This supplements, and does not replace, the required Claude audit.

## Scope and provenance

The initial frozen component is N1-06,
`theory/N1-round4-mesh.md`, SHA-256
`efe346fd96a12ea4d822c398f98be68ce885953ae03654bbfc1983ccf5c4e0ba`,
published at the rules/input commit above. Its hash was checked with
`sha256sum`; `git rev-parse HEAD` established the input commit.

Read handoff 03, the previous independent endpoint review, N1-03/04/05
and the N1-01 row definitions, together with the round-4 candidate.
This is a quantitative correctness review of the existing IDEA-337/459
continuation. No new mechanism, priority claim, candidate disposition or
novelty claim is assessed or generated. The workflow's no-novelty review
exception therefore applies; the full IDEAS registry was not reread.
No numerical fit, quadrature, sample or mathematical program was run.
Shell operations only read sources and establish byte identity. Developer
proofs, prior reviews, shared records and Git state are untouched.

## N1-06 disposition: accepted at its stated supporting scope

No mathematical finding remains in the frozen mesh statement. The
following independent reconstruction checks the normalization, constants
and endpoint uniformity; acceptance does not include finite polynomial
rows, collision-hole corrections, interior quadrature or a global model.

The actual coefficient identity is A=2(|C|+|D|)/pi. With T=2a cot(z/2),
the two coefficient pairs consequently give

    pi A_L=max(p,q+T),       pi A_R=max(p,|q-T|).

Subtracting 4a/z gives exactly the three affine branches on the right
and the two on the left in the source. The correction
u=T-4a/z has derivative -a csc²(z/2)+4a/z²<=0 and magnitude at most
a*pi*z/6. Each max term increases as T decreases. Its total variation
is bounded by (p-q)_+ on the left and q+max(p,q) on the right.
Their sum is 2max(p,q). Thus the combined variation bound is 2M, with
M<=1/pi+pi/24<1/2; the bound has no inverse a.

The left switch solves T=p-q and is pi-alpha+beta. The right switches
solve T=p+q and T=q-p and are pi-alpha-beta and pi+alpha-beta.
They are correctly ordered and positive when a>0. Capping them at
delta accounts for absent pieces. W'=u for
W=4a log(2sin(z/2)/z); integrating the final right branch
q-u-8a/z yields the source's negative W(delta), positive W(c2), and
-8a log(delta/c2). All signs and log ratios in (9) follow. When a=0,
the diamond forces p=q and f_L=f_R=p/pi. For a>0 their endpoint
values are q/pi and -q/pi. These values need not have a joint limit
as a,z tend to zero, but the uniform bound plus convergence on every
interval bounded away from zero proves continuity of their integrals.

The centered-cell Peano kernel is -(1/2)(1/2-|u|)² and has absolute
bound 1/8. For 1/x its tail integral is 1/b², giving the positive
epsilon_h and bound 1/(8b²). For log(x)/x, integrating the envelope
(2log x+3)/x³ gives (log b+2)/b², with no sign assertion needed.
These bounds decrease for b>=3/2 and give uniform convergence also
at t=0,1. The resulting bound on |h_R| is the stated H_R^*.

The initial uncovered cell interval has length at most h(R+1/2),
and the final discrepancy has length at most h/2. Constant extension
past delta preserves variation. The Stieltjes quadrature error is at
most h Var(f)/2, so the two endpoint errors together, multiplied by
L/pi and using h=pi/m, are at most
(2R+3)ML/m<=(2R+3)L/(2m). No differentiability across a switch is used.

For either endpoint, multiplication by 1/m turns the singular part
into Z_n sum 1/(k+t)+B0 sum log(k+t)/(k+t), with

    Z_n=D0-B0*epsilon,       epsilon=log((n+1)/n).

Thus its coefficient contains no growing L. The cut-off cell endpoint
is X+lambda, |lambda|<=1/2; equality at a floor transition is harmless.
The harmonic and logarithmic tail errors have combined bound
[6+(1/2)log(X+1/2)]/[8(X-1/2)²]. Moving the cell endpoint to X costs
[5+(1/2)log(X+1/2)]/[2(X-1/2)] by the derivative of
Z_n log y+B0 log²y/2. These are precisely the two terms of C_X.

Substituting log X=L+kappa+epsilon gives, per endpoint,

    B0(L+kappa)^2/2+D0(L+kappa+h_R)+B0*g_R
      +epsilon*(D0-B0*h_R)-B0*epsilon^2/2.

In particular the epsilon*L terms cancel. Since |D0|<=4, B0<1/2
and epsilon<=1/n, both endpoint corrections sum to at most
(8+H_R^*)/n+1/(2n²). The polynomial coefficients are exactly B0,b,c_mesh.
The degree hypothesis implies X>=2R>=4 and K_s>=R, even at t_s=1.
Using X-1/2>=7X/8 and log(X+1/2)<=log m<=L+1 verifies
C_X<=5(1+L)/X. Combining all terms gives exactly (4), including the
constant R+10+H_R^*+10pi/delta.

At a=0 the log-squared coefficient vanishes and the harmonic U0 term
still contributes 2U0 L/pi; it was not dropped. At alpha=beta=0 both
regular integrals are W(delta)/pi. At the other two vertices a=p=q=U0=0
and the entire mesh is zero. Offsets t=0,1 require no separate limiting
series convention. These checks cover the full claimed closed domain.

## N1-07 disposition: accepted at its stated supporting scope

Additional frozen source: `theory/N1-round4-rows.md`, SHA-256
`7f5c1b44ad6d502b85b5b89c6a563c2e2d90ad65d86bb205063e4a86f3703b61`.
Its identity was independently checked with `sha256sum`. Read N2's
full row decomposition to verify the corrected kernel and signed-row
normalization. No numerical execution was added. No mathematical finding
remains in this finite-row statement.

For the first sinc channel, r-j=2k+1 gives
-cos((z-nv)/2+(r-j)pi/2)=(-1)^k sin((z-nv)/2).
For the second, j+r=2l+1 gives
cos((z+nv)/2-(j+r)pi/2)=(-1)^l sin((z+nv)/2).
These reproduce both signs and the common prefactor in (5). At the
reference value nv=w the two weighted sine numerators become -a and
+a. Their sum, after division by w, is exactly 4a/(w²-z²).
The sinc expression is continuous at either collision, and equality
with the finite polynomial on the dense regular set proves the stated
collision convention. No other T pole lies in the allowed arguments.

For the exceptional right row r=1, w=pi-beta and alpha<=w. Its two
cosines are sin((w+alpha)/2) and sin((w-alpha)/2), with sum<=w.
All other rows have w>=pi. Thus (c_e+c_d)/w<=2 is uniform even
through the exceptional vertex. With x=w/(2m), expansion of the sine
chord gives the stated A_n-1/w bound; the sine correction coefficient
is at most 1/[24(1-x²/6)]<1/10. The prefactor error per near index is
therefore at most 2/n+pi²R²/(5n²). The sinc shift costs at most 1/n.
Finally |T(y)-1|<=y² follows from
sin y-y cos y=integral_0^y t sin t dt and |sin y|>=|y|/3.
On the near set |z|<=pi(2R+3), giving the claimed
9pi²(R+1)²/n² T error. There are at most 2R+4 near indices, all inside
the half-open mesh because n>=8R; (10) follows with its exact constants.

On the far set |z|>=2w and v<=|u|/2. The two sine chords give
K>=4sqrt(2)/(3pi²)>1/6. The sinc product estimate gives
1-K<=(u²+v²)/12. Together these imply
|(1+cos v)/(2K)-1|<=u², as used in (11). The corrected N2 numerator
is exactly the one written in the source, including both sine signs.
Its a term costs at most 16a/(3n²) per index. Replacing nv by w
costs at most (128/9)a*w²/(n*z⁴), which is below the claimed factor 15.
Using |z|>=pi(|j|-1) proves the displayed reciprocal-square and harmonic
sum bounds. Since w²/z²<=1/4, these also yield the fourth-power bound
and the stated 1/n mesh-shift cost. The denominator lower bound u²/16
gives the two sine errors 8/(n|z|)+8w/(nz²); their sum is bounded by
(6H_n+3)/n. The total far error is consequently (10+6H_n)/n.

Outside the half-open mesh, |z|>=pi n on both sides, including its
excluded positive endpoint. The reference is bounded by 5/z² and its
two tails sum to at most 2/n. The full reference norm is at most 4R+9,
from at most 2R+4 near terms bounded by 2 and a far sum below 1.
Thus the n²-normalized error is exactly the source's
(6R+24+6H_n)/n plus its quadratic term. Multiplication by n/m changes
the target reference by at most (4R+9)/n, proving e_row with no hidden
factor of two or n/m.

The exact signed row divided by n² tends to -sin(b)/w. The already
proved absolute comparison and tails justify this signed limit and
summation. In the phase interior the positive reference indices are
precisely -r+1,-r+3,...,r-1: the diamond makes both bounding inequalities
strict. Applying |f|=-f+2f_+ gives the coefficient 8a and the positive
sin(b)/w in ell_r. Continuity via the sinc formula supplies the boundary
values, even when an enumerated term meets a pole. At r=1,w→0 the
profile is -sinc(w)+2sinc((w+alpha)/2)sinc((w-alpha)/2), which tends
uniformly to 1 for alpha<=w. Every other reference index tends to zero.
This confirms the special vertex value and its uniformity.

For r=0 every regular representative has |u|>v. Positivity requires
sin u>0 and yields F_+<=p/(u-v). The smallest positive mesh point has
u-v>=2alpha/n; p<=alpha bounds it by n/2, with the alpha=0 value
covered by continuity. The remaining indices contribute at most
nH_n/(2pi). The negative signed row differs from sinc(beta) by at most
1/m+pi²/(24m²). Adding the positive correction proves the sharper
bound stated before (3), and hence (3). Reflection of v preserves the
finite polynomial and row parity because 2m is even, so the right rows
are exactly those claimed. There are R left and R right rows, giving
(3+H_n)/n+(2R-1)e_row and no parity exception.

## N1-08 initial disposition: simultaneous-collision proof gap

Additional frozen source: `theory/N1-round4-endpoint-block.md`, SHA-256
`4a9b0f908f0b5cf12dbf56856bee47da47f860ef1c5f9fd5bf01f00676edc552`.
Its identity was checked with `sha256sum`. Read N1-02's definitions and
collision-count argument in addition to the dependencies above.

**F1 — MAJOR, proof coverage.** Section 2 assumes that the other channel
is an ordinary nonsingular cotangent norm. Both right endpoint offsets
can instead be integers simultaneously: alpha=0, beta=pi-z gives
eta_+=0 and eta_-=1. These are actual mesh collisions, for example
n=16,R=2,delta=pi/4,r=31,beta=7pi/8, where v=15pi/8 and z=pi/8.
This row is outside P_R. Here C=D=0, but each channel has its own finite
polynomial pole contribution. The second must not be replaced by the
zero ordinary norm. The theorem bound appears correct: c_e=c_d=sin(z/2)
and the two distinct pole contributions are n/2 each, so R_r=n and
H=1 exactly. Add this explicit case before applying the one-collision
argument. No correction to N1-06 or N1-07 is requested.

For v=z, the offset ranges permit only eta_-=1, equivalent to
alpha-beta=pi-z; the other offset cannot be an integer. For v=2pi-z,
the only possibilities are eta_+=0, equivalent to alpha+beta=pi-z,
and eta_-=1, equivalent to alpha-beta=-pi+z. In all cases C+D=p/2,
so the surviving coefficient is p/2. The channel poles are distinct
because 0<z<=pi/4. The two right types coincide when alpha=0 and
beta=pi-z, precisely the omitted F1 case.

The pole signs can be fixed without extrapolating a product of zero
and infinity. For a minus collision choose a representative u=v.
Then r-j=1 because alpha-beta+v=pi. The exact sine-coefficient identity
has positive sign and gives n*c_e/[2sin(z/2)]. For the right plus
collision choose u=-v. Since alpha+beta-v=-pi, j+r=1, again giving
the positive sign, now n*c_d/[2sin(z/2)]. Shifting representatives
by 2pi leaves these limits unchanged. The remaining cotangent value
is +cot z in the left-minus and right-plus cases, and -cot z in the
right-minus case. The first two cases thus have no cancellation.

In the right-minus case beta=alpha+pi-z and the diamond implies
alpha<=z/2. The absolute-value defect is bounded by twice the magnitude
of the other term, which is p cot z<=alpha/z<=1/2. This does not assume
that the other term is nonnegative, or that the pole term dominates.
It also holds when c_e=0. Dividing this absolute row correction by nm
gives exactly 1/(2nm), the second term of (6).

For a row with only one collision, the vanished channel has only its
one finite pole sample; the others
are zero. Its normalized value equals the integer-offset regularized
profile exactly, since F_n=Phi_L=1 at that offset. The other channel
is nonsingular on its mesh. N1-04's error multiplied by its coefficient
p/2 and then divided by m is at most 5/(2n²m). The cancellation
integral vanishes when one coefficient is zero. These observations
prove (6) with the written normalization, directly from polynomial
values rather than an assumed continuity of a separate absolute norm.

On the odd board each of mj-nr and mj+nr is bijective modulo 2nm:
the full-board kernel has (0,0),(n,m), which have opposite parity.
Each collision equation therefore selects at most one point, hence
there are at most two collision rows. Outside P_R, both endpoint
distances are at least pi R/m. N1-05's residual bound with P<=2 then
becomes [7+(2/pi)(3+2log(4m/R))]/m. Summing at most two corrections
gives every term of e_collision in (3), including 5/(n²m)+1/(nm).

The hypothesis places all of P_R inside the endpoint strips, since
its endpoint distances are at most pi R/m<=delta/2. Outside P_R the
left indexing is k=r with offset beta/pi; on the right it is
k=2m-1-r with offset 1-beta/pi. Their first admissible k is R and
their last is floor(delta*m/pi-t_s). Thus the unperforated mesh is
exactly N1-06, the P_R contribution is exactly N1-07, and filling then
restoring a collision adds one correction and never duplicates a row.
This proves c=C_R+c_mesh with the same b and B0 as N1-06.

Finally H_n<=1+L makes e_rows' numerator
A_R^*+B_R^*L, with exactly the stated A_R^*,B_R^*. Since n>=8R,
its quadratic term is bounded by D_R^*/(8R n). Also
log(4m/R)<=L+2 and n>=16 give e_collision<=26(1+L)/n.
Adding N1-06's constant R+10+H_R^*+10pi/delta gives the stated
R+36+H_R^*+10pi/delta in K4. The stronger (1+L)/n rate therefore
implies the exact preregistered H4 bound, with coefficient evaluation
count independent of n and the series tails already proved in N1-06.

## Scoped error-budget check

Also checked `theory/N1-round4-budget.md`, SHA-256
`b7c614fc9ceeeb1b407dade41086ba834fb0b7c01fa883f34bd4e02ac4f6bf9b`.
Its formula-only obstruction is accepted. At the corner E_(n,R)>2/R,
and (2R-1)10R>=15R² for R>=2. AM–GM applied to 1/R,1/R,15R²/n gives
3(15/n)^(1/3)>6/n^(1/3)>=3/50 for n<=10^6. Thus this unchanged uniform
certificate cannot meet gamma/2 when gamma<=3/25, even with zero other
errors. This is not a lower bound on true error or a full B3 verdict.
No numerical optimization was performed. The proposed repair and registry
disposition/novelty are outside this elementary inherited-formula check.

## F1 focused re-review: closed

Corrected N1-08 SHA-256:
`49c910ab1835008fd70cb2968fdea01773e427adc1541832c10dd379317fcc62`.
Read the developer response and reviewed the exact diff against
`7e457c7fc54b32b45b0870d53a5fd4c37cd45fce`. The added double-collision
case correctly proves R_r=n,H=1, hence zero correction. Section 2 now
restricts its ordinary-norm argument to one pole channel. The statement,
coefficients and error bounds are unchanged. F1 is resolved; the corrected
complete H4 endpoint proof is accepted. This proof repair does not spend
the campaign's permitted model correction.

## Completion and remaining scope

N1-06, N1-07, corrected N1-08 and the scoped budget calculation pass this
supplementary review. No unresolved finding remains. This does not include a
numerical evaluation or optimization of its error budget. N1-05's
integrable-strip cost Q remains outside that target. Interior outer
quadrature, the central chart, the complete comparison error, B3/B4,
an effective onset and PD-T099 are not accepted or upgraded. No formal
Claude audit has been performed by this agent.

Review is complete at the accepted hashes above. No developer source or
prior review was edited, no code or data artifact was needed, and no
mathematical program was run.
