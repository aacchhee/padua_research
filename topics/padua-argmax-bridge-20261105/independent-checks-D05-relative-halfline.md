# D05 relative half-line — distinct mathematical review

2026-11-06. Rules/input head
`41c4c804456fbaf952dda344a5ff9795a0252f64`.
Reviewer: Codex, distinct agent `/root/d01_corner_review`;
parent-requested `gpt-6-astra`, high. Runtime serving model/effort
metadata are not independently exposed. Author allocation was Sol xhigh.
This is supplementary independent mathematical review, not the required
cross-provider Claude audit or a registration/readiness approval.

## Verdict and immutable scope

**ACCEPTED at the written supporting scope.** No BLOCKING, MAJOR or
MINOR findings. The matched half-line estimates, fixed near-phase row
increment, and improved full-phase absolute endpoint charge are supported
by the paper proof. The full phase-relative S-K comparison remains
**OPEN/deferred**, not PARTIAL. No global degree threshold or certified
range changes; the existing global threshold remains 500000.

The three reviewed author files were hashed directly and match the
parent's frozen inputs:

| File, relative to this topic | SHA256 |
| --- | --- |
| theory/D05-relative-halfline.md | `c427301228146c5cb5f27eca51e77a833470701c2363888fba9e1318b1f3d174` |
| ideas/D05-relative-reference.md | `9b3e7c8047b8bc5c837e80cc85ae0773064b807cd69d555631286bfa29aec2f7` |
| attempts/D05-relative-reference.md | `d70a9c248d7cc3021a4c76c710216b6cb080b4fbc219192b70f916b83b60b919` |

These bytes were not edited. The accepted D04 dependency hashes were
also checked directly:

| Dependency | SHA256 |
| --- | --- |
| theory/D04-half-line-defect.md | `593c7e32f2cd4f83a68507e8c25ca26ca7f8e45e4735e20d373cc3efe3404e6f` |
| theory/D04-reference-matching.md | `bb89a7e3c3b3c174c877e465500ddfd033ceba00e2e578aeae0151856024c622` |
| theory/D04-row-reduction.md | `2eed7940022efbc0e018ddf6a06da68bb2b40d947af305e28d641c5d4b3050cf` |
| independent-checks-D04-row-reduction.md | `cacbab625421e4d269bc2a3047aa523caee8c4f08a709748721291178f9976d7` |

## Rules, gate and dependency coverage

Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md; the rules
have no changes from this agent's preceding review. Root alone owns Git
and shared records. The complete 1112-line state/IDEAS.md, including all
obstruction/disposition tables, was read in this same agent session for
D02. Its refreshed SHA256 is unchanged:
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
This carries forward the complete identical-byte reading; it does not
claim a new line-by-line 291 KB read during D05. Searches refreshed
half-line, residual, reference, relative, Bernoulli, cutoff, trapezoid
and PD-T270 across that registry, literature INDEX and topic gate records.
The author's more extensive prospective gate is retained in its idea.

Read the three D05 files in full, the three D04 support proofs, D04's
OPEN practical target and the distinct D04 report. The refreshed full
shortlist also includes D03's cancellation perturbation/candidate;
N1-04 regularized poles, N1-09 finite-h jump correction, N1-18 branch
artifacts, N1-19 OPEN modulus; PD-T220/PD-N079's primitive cusp;
PD-N132's leading-factor obstruction and its boundary-profile source;
and PD-T270's cotangent-remainder proof. Earlier D02 reading supplies
the unchanged underlying N1/C08 endpoint context. Truncated reading
output was followed by narrower reads for the missing N1-19 text.

The gate classification is justified: D04 already has this residual,
and N1-09 already has first-order jump corrections. D05 is a quantitative
variant estimating the increments of one matched functional and retaining
its boundary term. Neither its files nor this review claim historical
novelty, an external source theorem, or a new primitive smoothness result.

## Independent reconstruction of the scalar claims

Let A=pi/2. The local partial fraction is

    cot y-1/y = -2y sum_(l>=1) (pi^2 l^2-y^2)^(-1).

Twice differentiating on [0,A] gives exactly the negative series in
D05, with summable differentiated terms. Thus r' decreases from -1/3
to -1+4/pi^2 on the left. The right derivative at A is 4/pi^2;
the jump is +1, and the tail derivative 1/y^2 decreases to zero.
The three variation contributions are consequently

    (2/3-4/pi^2), 1, 4/pi^2,

whose sum is 5/3. The cutoff jump cannot be discarded. Giving r'(A)
either one-sided value preserves this total variation. The residual
itself decreases from 0 to -2/pi and returns to 0, so its total
variation and integral of |r'| are both 4/pi.

For one cell, integration of the absolutely continuous r gives the
stated K_t kernel with mean t-1/2. Its centered primitive B_t vanishes
at both cell boundaries. Its value at the corner is t(1-t)/2;
the possible interior minima are at least -(t-1/2)^2/2. Therefore
|B_t|<=1/8 for every real t in [0,1], including the endpoints.
Stieltjes integration against dr' then bounds the entire finite
zero-mean contribution by h Var(r')/8=5h/24. This includes the atom
at A. The cell-boundary terms vanish, and the terminal value r(v+Kh)
tends to zero. The mean term has the correct sign:

    (t-1/2)[0-r(v)] = (1/2-t)r(v).

Independently, the absolute cell defect is at most the variation of r
on that cell. Summing bounds the series of absolute defects by 4/pi.
This proves convergence without subtracting separately divergent
improper quantities. The sine chord together with
sin y-y cos y=integral_0^y u sin u du<=y^3/3 proves
0<=1/y-cot y<=pi*y/6, including its continuous endpoint limits.
These calculations yield the claimed bound pi*v/12+5h/24 on [0,A].

For each finite matched sum, the almost-everywhere v derivative is
the quadrature defect of r'. Cell variation bounds its magnitude by
5/3; the finite sums are absolutely continuous. Their pointwise limit
therefore has the same global Lipschitz constant. At a sample crossing
A, r remains continuous, so no extra jump in the finite sum is lost.
The t derivative is h times the sampled r' sum. Comparing |r'| with
its cell averages bounds its magnitude by 4/pi+h Var(|r'|), which is
at most 4/pi+5h/3. Passing to the limit proves the real-offset estimate.
Neither argument differentiates a moving absolute-value root.

The direct telescoping identity is
E(h,v,1)-E(h,v,0)=-r(v). Thus a circular offset distance would be
invalid. D05 explicitly avoids it. Reconstructing D04's finite
reciprocal subtraction gives Q-h^-1[log(v/h)-psi(v/h+t)]=E with the
stated sign. Two Q terms, each multiplied by -2w, give precisely
pi*w*v/3+5w*h/6, not half or twice that allowance.

## Actual offsets, boundary cases and normalization

For the fixed left/right sets, j>=2 and j<=floor(n/2)<m/2.
The signed shift is s=beta/pi on the left and -beta/pi on the right.
It follows that z>=3z0/4>0 and z<=A. The two offsets are positive;
indeed 1-s-x>=1/2 and the remaining displacement is positive.
Their only possible upper endpoint would require the extremal
phase difference and z=A simultaneously. The left constraints then
contradict j<m/2, and the negative right shift makes z<A. Hence
both offsets lie strictly in (0,1), for both parities, both axes and
rho=pi/2. The D04 floors are zero and no polynomial collision is
assigned a reference value.

Boundary check (NOTE, no action required): for even n the fixed left
row j=n/2 can attain z=A when alpha=0,beta=pi/2. Both offsets then
equal 1/2. This is covered by the theory's explicit extension to A.
The folded g0 is zero there, its sample/integral identity extends
continuously, and the digamma bookkeeping value need not be zero.
Thus this fixed-row statement must not be silently identified with
D04's strictly z<A endpoint partition. The attempt explicitly leaves
the changing partition contribution unresolved.

The exact shifts from the zero-phase offsets are

    |z-z0|=beta/m,
    theta_+/- -theta0=+/-alpha/(2pi)-n*s/(2m).

Their absolute sum is max(alpha/pi,n*|s|/m)<=rho/pi. With
h<=pi/16 and 3<pi<4, the offset Lipschitz coefficient is less than 2.
This gives the two U bounds in the theory. Along the z-segment,
sin(y/2)>=y/pi and y>=3z0/4 give the stated cotangent difference
8pi^2 beta/(9m z0^2); cot(z/2)<=2/z<=8/(3z0).

Using D=-a*cot(z/2)*U and subtracting aD(0,0), the product difference
has three coefficients after substitution:

    16rho*m/(3pi^2*j),
    [4pi^2/27+80/(9pi)]*beta/j,
    10pi*m*beta/(27n*j^2).

Each set's reciprocal sum is at most H_n. Their combined square sum
is bounded by 2[1/4+integral_2^infinity y^-2 dy]=3/2. After division
by nm, the coefficient relative to a*rho*H_n/n is bounded strictly by

    32/27 + 32/51 + 85/612 = 3583/1836 < 2.

The slack is 89/1836. These are manual rational calculations, not
executed numerical evidence. No division by a or rho is needed;
at rho=0 the actual difference is identically zero.

For the absolute full-diamond consequence, w<=a/z turns each row
bound into pi*a/3+5a*h/(6z). Fewer than 2m endpoint rows produce
2pi*a/(3n) after normalization. Their combined 1/nu sum is at most
2H_n and z=pi*nu/m; h=pi/n then gives exactly 5a*H_n/(3n^2).
This is valid with D04's collision exclusions and exact wrap terms
retained inside Theta. At a=0 the weighted reference vanishes; no
division by a or substitution of unweighted poles occurs. Adding
the unchanged D04 charges gives the attempt's absolute corollary.

## Remaining obligations and execution receipt

The review does not establish increments of Theta/(nm)-Xi, central
reference rows, changing endpoint/central membership, changing exact
collision membership, or weighted single-pole approximation errors.
The separately accepted D03 perturbation bound does not remove these
five gaps. Nor does this review infer a practical full M_infty rate,
argmax result, altered M_near correction, or native certificate.

Actual commands were read-only repository/rules/proof reads and text
searches (`cat`, `sed`, `rg`), `git rev-parse HEAD`, a rules-only
`git diff`, and `sha256sum`; the only write is this assigned report.
An initial read used nonexistent D05 idea/attempt filenames ending in
relative-halfline; those paths were corrected to relative-reference
before the complete reading. This was a read-path error, not a failed
mathematical run. No scalar program, native binary, board evaluation,
numerical quadrature, fit, degree job or producer was executed. No
computation was needed after the analytic constants checked. No child
agent, Git mutation, author edit, shared-log edit or evidence change
was made. Root was notified of acceptance before this report was written.
