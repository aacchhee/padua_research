# Independent supplementary review of N1 round 5

Reviewer: distinct Codex `/root/review_n1_round4`, requested Astra high;
serving metadata are not independently exposed. Input head
`fc8c2885f47b08cecc7f65328db0e740cbc205ea`. AGENTS, WORKFLOW and CODEX
were read during the preceding review; their diff from rules commit
`121ae257a71564025ddc2da8f53d19478f5d7dd4` to this input is empty.
This is a supplementary mathematical check, not the required Claude audit.

## Frozen scope and method

| Source | SHA-256 |
|---|---|
| N1-09, `theory/N1-round5-jumps.md` | `f74923448719b5475c8a5422162e25b71919f4cb56a5f65f8753fb0bc05c1f34` |
| N1-10, `theory/N1-round5-endpoints.md` | `c694f98b2c7f8f01b6911df409208d113e651801e875fe069fb454f92b76a928` |
| Contract, `ideas/N1-round5.md` | `8b476bf79bd40ef2e6da27d9ad31b7c18c028c919fc43d52226a705f44476b41` |

All listed files were read and their identities checked with `sha256sum`.
The preceding round-4 review supplies the already-read N1/N2 definitions
and shifted-series dependencies; its report and developer sources are
untouched. This check reconstructs the specific quantitative continuation
of IDEA-337/459. It assesses no new mechanism, priority claim or registry
disposition. The workflow's no-novelty review exception applies; no new
full IDEAS read is claimed. No numerical fit, mathematical program or
independent computational rerun was performed. `git rev-parse HEAD`,
read-only rule/source diffs and source reads establish provenance only.

## N1-09: accepted at the written row-model scope

No mathematical finding remains in the frozen N1-09 proof.

Since cos t>=1-t²/2 and alpha²+beta²<=1/4, a>=15/16; also P<=1/2.
For either effective sign of beta, the complete numerator on z<=pi/2
is at least 2a-P>0. Thus the denominator alone fixes the sign. On the
finite endpoint rows, w/m<=pi/8. The last positive index on each side
has a strict distance at least pi-1/2-pi/8 from nv, while the next
excluded index lies strictly outside. This proves the exact fixed index
set -r+1,-r+3,...,r-1 for either parity. For r=0 the smallest absolute
odd-grid angle exceeds beta/m; all entries are negative. The signed-row
identity gives (5) and its beta=0 limit n(a-m). The positive numerator
also excludes endpoint collisions here. The retained F_j can be
evaluated by N2's exact two-trigonometric-variable numerator quotient,
so their polynomial notation does not require a growing polynomial sum.

At x=0, the dominant C cot x changes from sign -sign C to sign C.
Its finite-channel contribution to the one-sided difference is therefore
2 sign(C)D cot v. At x=-v, the finite channel is -C cot v, yielding
-2 sign(D)C cot v. These independently recover both jump signs.
For q_b=1/2-frac((x-b)/pi), the n shifted values sum exactly to
1/2-t=-B1(t). Subtracting the two jump ramps makes g continuous and
adds only a constant to its regular derivative. The ramps have zero
integral. Thus their exact grid contribution is J_r with the stated
minus signs, and the residual has derivative variation Var(g'_reg).

For a folded left endpoint, C<0,D>0. Writing u=2x+z gives
cos u-cos z=-2sin(x+z)sin x, which is negative for 0<x<pi-z.
The positive numerator therefore fixes which opposing channel is smaller:
g=-2D cot(x+z) on (0,pi/2-z) and g=-2C cot x on
(pi/2,pi-z), and zero elsewhere. The derivative on the first piece
decreases from 2D csc²z to 2D; including its two jumps to zero gives
variation 4D csc²z. The other piece similarly gives 4|C| csc²z.
At z=pi/2 both pieces vanish; the written inequality still holds.
Reflection or translation handles the right endpoint without assuming
a derivative estimate for arbitrary C,D in the central region.

The centered-cell sample-sum error kernel has magnitude at most h_0/8.
Its integral against df' therefore gives h_0 Var(f')/8, which is exactly
pi(|C|+|D|)csc²z/(2n) after jump removal. On either endpoint
|C|+|D|<=2a/z+q/2. After dividing by nm, applying
csc²z<=pi²/(4z²), and summing the two copies of z>=pi k/m, k>=R,
the reciprocal-cube term is a*m²/[4n²(R-1)²] and the reciprocal-square
term is q*pi*m/[8n²(R-1)]. Replacing q by P proves the first two
terms of E5 with all normalization factors retained.

In the central region, after excluding m-1,m, the distances from pi
are at least pi*l/m with each positive l occurring at most twice.
The sine chord gives sum 1/|sin v|<=mH_n. Also csc²(v/2)<=2 and
there are at most m+1 central rows. These recover P H_n/n+4a/n.
The other approximations are exactly those whose aggregate was bounded
by r_n in N1-02; replacing some of them by exact endpoint rows only
reduces that bound. Neither an extra e_rows nor an unnormalized jump
term has been inserted.

For R=128 and n>=10^6, m/n<=9/8 makes the first E5 term smaller
than 1/40000. H_n/n<15/10^6 and P<=1/2 bound the central terms by
11.5/10^6<1/80000. The second endpoint term and r_n together are
smaller than 1/10^6. Their displayed sum is strictly below 1/8192.
These comparisons use inequalities valid for every n in the range,
not a finite numerical run. The accepted conclusion is the row-model
error; K5 still has a growing ordinary outer sum at this stage.

## N1-10: accepted at the written endpoint H-profile scope

No mathematical finding remains in the frozen N1-10 proof.

Integrating the two fixed cancellation branches gives
2(D-C)log(sin z)=(2a cot(z/2)+q)log(sin z) on the left;
effective beta reversal replaces q by -q on the right. Subtracting
(4a/z)log z+q_s log z leaves the two terms in (4): the cotangent
correction is at most a*z*|log z|/[3(1-delta²/24)], and replacing
log(sin z) by log z costs at most (4a+q*delta)z/(6-delta²).
After division by pi these are bounded by z|log z|/9+z/4.

Differentiation of the uniformly summable R series gives exactly
R''=4 sum k/(k²-t²)²+16t² sum k/(k²-t²)³. The bounds on the two
sums are 32/3 and 320/27. The five contributions to Phi_0'' are
bounded respectively by 10/3,10,608/81,32/3,10/3, whose sum is
2822/81<35. The original symmetric C series is smooth near 1/2,
so reflection creates no derivative jump there. All used offsets lie
strictly inside [1/4,3/4]. Their slopes give numerator derivative
U1 on the left, -U1 on the right, and second derivative at most
35/(2pi²). Taylor's remainder divided by z costs 35z/(4pi²);
the denominator correction costs pi*z/6. Together they are below
3z/2. Thus the full remainder is the stated
z[7/4+log(1/z)/9], with no inverse offset distance.

The envelope is increasing on the relevant tiny interval and is G'.
Forward cells of length h from each sample are disjoint and lie in
[Rh,delta+h]. Multiplication by 1/m=h/pi proves the two-strip bound
2[G(delta+h)-G(Rh)]/pi. Using delta+h<251/250000, pi>3 and
log(1/(delta+h))<9 gives exactly the stated rational bound
6363101/6750000000000<10^-6. Only sample positions z<=delta enter
this residual argument; slightly extended centered cells are used
separately for smooth coefficient quadrature.

Every coefficient switch is beyond pi-1/2, so the exact regular
coefficient is (q_s+2a cot(z/2)-4a/z)/pi on all retained cells.
Its antiderivative has the stated W_a sign. Combining A_s L with the
singular B term gives Z_n=U0/pi+B0 log(pi*n/m) exactly, so |Z_n|<=5
independently of L. Both scalar cutoffs and the lower cell endpoints
remain present. Applying the N1-06 series tails at b_s gives e_HG;
b_s>317 and monotonicity of [6+(log x)/2]/x² yield
e_HG<9/(4*317²)<1/40000. Applying the same tails after J=4096
gives e_const<10^-6. This remains valid whether K_s lies below or
above J, and at t_L=0 or t_R=1.

The two variations of the regular coefficient total at most
a*u_max/3. Centered-cell BV quadrature, multiplied by L/pi,
therefore costs a*L*u_max/(6m)<10^-8. There is no omitted initial
interval. For log z the derivative-variation integral is at most
1/l_s, giving sample-sum error h/(8l_s). Multiplication by q/(pi*m)
and summation give exactly q/[4pi*m*(R-1/2)]<10^-9. The U_s terms
are constant on each mesh and contribute U_s N_s/m exactly.
All four small errors plus e_HG fit below 1/32768 as written.

## N1-11: accepted at the written full jump-sum scope

Additional frozen file `theory/N1-round5-jump-sum.md`, SHA-256
`cd81ff9539c3eba5c34d3361d855a371dafc7230c635087682541640c93851bf`.
Its hash was checked and its entire proof read. Read PD-T270's full
local proof, including the cotangent remainder derivative estimate used
here. No mathematical finding remains in N1-11.

On the left, substitution of the two B1 values gives
cot(z)[(C+D)alpha+(D-C)(z-beta)]/pi, which is exactly (5).
On the right, the original signs are C>0,D<0 and cot v=-cot z.
Reducing the offsets modulo one gives B1 values
(alpha-beta-z)/(2pi) and (alpha+beta+z)/(2pi). The resulting jump is
cot(z)[(C+D)alpha+(C-D)(z+beta)]/pi, precisely (5) with
b=-beta and q_b=-q. There is no extra reflection sign. All these
offsets stay strictly between integers for rho<=1/2,z<=pi/2, so
there are no collision holes. The central special rows are outside
these halves. Both actual index ranges are exactly R,...,K as claimed.

Expanding cot z=1/z+v and using
cot z cot(z/2)=csc²(z/2)/2-1 gives the reciprocal-square coefficient
-2ab/pi and reciprocal coefficient (p*alpha-q*beta+4a)/(2pi).
The remainder is exactly W_b; its value at zero is
q_b/(2pi)+5ab/(6pi). Normalizing by 1/(nm) and setting z=h(k+t)
therefore gives coefficients A2_b*m/(n*pi²), A1/(n*pi), and
1/(n*pi) on the regular integral, with the finite cell limits retained.

For the regular-part estimate, v decreases from zero and has total
variation at most 7/10 on [0,8/5]. The small extension past pi/2 is
legitimate because tan y<=y/(1-y²/2), y<3/100. Also w=-v'(z/2),
so PD-T270's |v''|<1 gives |w'|<=1/2, variation<=4/5, and
|w|<=17/15. With |p*alpha-q*beta|<=1/4, the two product variation
terms are bounded by exactly the four numerator terms in (7), plus
A/pi for the last linear term. Their sum is less than 2; direct
sup bounds are also below 2. The final cell ends before pi/2+h/2<8/5.
Thus each regular sample sum differs from its exact-cell integral/h
by at most 1, and the two normalized errors total at most 2/(nm).

For x^-2 the centered-cell error is negative and its tail has magnitude
at most (1/8) integral_b^infinity 6x^-4 dx=1/(4b³). Consequently
the finite reciprocal-square sum is Q_R-1/b_K+epsilon_2 with
epsilon_2>=0, not the opposite sign. The harmonic sum similarly has
the positive tail in (10). Since b_K>=n/2, |A1|<3/4,
sum|A2_b|<=2/pi and m/n<=9/8, the two weighted cutoff tails are
less than 1/n³. Combined with the regular quadrature they are below
3/n². Truncating both constants after their one k=R term costs at
most 1/(27R³)+1/(16nR²), by the same tails and pi>3,m/n<=2.
For R=128,n>=10^6 their total with 3/n² is below 1/40000000.
Neither a missing L factor nor an n-dependent constant truncation is
hidden in this calculation. The bounded integrals remain exact model
functions, whose eventual numerical evaluations still need enclosure.

## N1-12: accepted at the written endpoint-assembly scope

Additional frozen file `theory/N1-round5-assembly.md`, SHA-256
`b1bec75ce4fbd3ea7767e56a913ca262ae679070401c948bc36346443b770f43`.
Its hash and full statement/proof were checked. No mathematical finding
remains in N1-12.

Start with exact B_n in ordinary rows. N1-09's corrected cancellation
estimate supplies E5 independently of any approximation of B_n, while
the remaining special Rhat errors are bounded by r_n. Thus using this
auxiliary model legitimately avoids adding an ordinary N5 pole-norm
error and then paying again for its replacement. N1-04's sine-weighted
error multiplied by the complete coefficient-sum bound gives exactly
D_n=10/n²+20aH_n/(pi*n²). Collision rows remain in A_R throughout.

All 2R finite endpoint rows lie inside z<=delta, since their distances
are at most pi R/m<delta. There are no other special rows in z<=pi/2.
The remaining strip is exactly the two N1-10 index ranges. M_strip
therefore replaces its normalized H terms once. M_jump replaces the
normalized jumps on the full halves z<=pi/2, including their portion
with z>delta. The last H sum retains exactly those other ordinary rows,
so neither its jumps nor its profile terms are lost or duplicated.
The first two special-row sums retain normalization 1/(nm), M_strip
uses 1/m, and M_jump uses 1/(nm), as required.

The finite endpoint F_j admit the previously verified sinc/T formula
with O(1) evaluation count per selected j; the r=0 signed row has its
explicit beta=0 continuation. This establishes the stated O(R²) count
without evaluating G_n through its polynomial expansion. The remaining
outer sum is explicitly retained and has not been declared compact.

Uniformly for n>=10^6, H_n<=1+log n and monotonicity of
(1+log n)/n² give D_n<10^-8. Adding the displayed rational bounds gives

    1/40000+1/80000+1/10^6+1/10^8+1/32768+1/40000000
      <1/14000<1/4096.

The additional endpoint-compaction portion is below 1/8192 separately,
as is the N1-09 allocation. Thus the stated component test for this
single correction passes analytically. This does not establish that
the unfinished central/interior reduction fits the remaining budget.

## Completion and limits

All four frozen round-5 proofs are accepted at their exact written
scopes, with no unresolved finding. Central/interior outer compactification, the model maximum,
the complete comparison budget, B3 PASS and an effective onset remain
OPEN. This report is independent analytical reconstruction, not a rerun
or formal Claude audit.
