# D05 fixed special rows — distinct mathematical review

2026-11-06. Rules/input head
`41c4c804456fbaf952dda344a5ff9795a0252f64`.
Reviewer: Codex, distinct agent `/root/d01_corner_review`, parent-requested
`gpt-6-astra`, high. Runtime serving model/effort metadata are not
independently exposed. Author allocation: Sol xhigh. This supplementary
review does not replace the required cross-provider Claude audit.

## Verdict and frozen inputs

**ACCEPTED** for the explicitly new fixed-special-row model and the
unchanged D04 error bound, for every integer R>=2, n>=8R and every point
of the closed phase diamond. No BLOCKING, MAJOR or MINOR findings.
There is no claim that the new model equals the old moving-membership
model at a collision. No interval implementation, runtime, compact
M_infty remainder, relative increment estimate or argmax result follows.
The existing global threshold remains 500000.

Directly checked author SHA256 values:

| File, relative to this topic | SHA256 |
| --- | --- |
| theory/D05-fixed-special-rows.md | `5df0e17dce65cb917f967e3066a46b628e6cf9284c00e8e0b5af8816ebb2fc16` |
| ideas/D05-fixed-special-rows.md | `5cbddf0cfa482682afc858c25554c444667f10ec24d8ecc88ebf41cd1dadd652` |
| attempts/D05-fixed-special-rows.md | `3edc8ede6ac096e1b1f6702d1565fedbd02fb4fa82405b6b629b854f471287c3` |

The D04 dependency proofs and independent report are the same frozen
files checked directly in this agent's immediately preceding D05
half-line review: half-line `593c7e32...`, reference `bb89a7e3...`,
row reduction `2eed7940...`, independent report `cacbab62...`.
Their full identities are recorded in
[that review](independent-checks-D05-relative-halfline.md).

## Rules, gate, predecessor and timing coverage

AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md were read in this
agent session; the head remains the rules SHA above. Root alone owns
Git and shared records. This review writes only its assigned file.

The complete 1112-line state/IDEAS.md and all obstruction/disposition
tables were read earlier in this same agent session. Its directly
refreshed SHA256 remains
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
Thus the full identical-byte reading is retained, rather than asserting
another complete 291 KB read. Refreshed searches used continuity,
collision, fixed row, dense, weighted and Phi across the registry,
current D05 ideas, C06/C09 theory and literature INDEX. Search output
was deliberately capped; it is not a full reading of every match.

Read all three new author files completely. The full D04 support proofs
and independent report, N1-04, D03, PD-T220/PD-N079, PD-N132 and the
relative D05 candidate were read in this session before this review.
New full shortlist reads include C06-far-full-profile.md,
C09-row-convexity.md, N1-round4-endpoint-block.md (including its corrected
double-collision case), and the complete C11/C12 implementation attempts.
C06-far-compact-error.md was refreshed at its collision-continuation
and special-row passages. The unchanged N1/C08 endpoint context is
retained from the preceding reviews; its bounds are dependencies, not
new numerical evidence in this review.

The difference from C06 is real but modest: C06 already continues a
one-sided inequality using weighted pole products. The present contract
continues D04's two-sided error after also proving continuity of the
bounded cancellation integral, and openly defines a different model.
The same residual, continuity principle and weighted Phi are inherited.
This is a technical corollary/variant, not a historical novelty claim.
C09/C12's coefficient-relaxed whole-box construction is a different
object; its source acceptance and operation counts do not transfer here.

Timing NOTE (no action required): the author's canonical attempt says
the preliminary min-channel feasibility message preceded completion of
the final C11/C12 scope reads, while the complete written proof followed
them. This review preserves that qualification. It does not relabel the
preliminary observation as having followed a completed prospective gate,
or claim that this reviewer witnessed the author's timing independently.

## Independent reconstruction

### Fixed ordinary rows stay away from all problematic v values

For r in O_fixed, R<=r<=2m-R-1 and r is neither m-1 nor m. If r<=m-2,
its entire beta interval gives

    R*pi/m <= v_r <= (m-1)*pi/m.

If r>=m+1 it gives

    (m+1)*pi/m <= v_r <= (2m-R)*pi/m.

These are closed bounds, so dist(v_r,pi*Z)>=pi/m on every edge and
vertex as well. The half-angle sine is uniformly positive at each
fixed n,R, and |cot(v_r/2)| has the stated finite bound. On the triangle
a=cos((alpha+beta)/2)cos((alpha-beta)/2) lies in [0,1]. Since
|p-q|<=1 and p+q<=2, both actual coefficients are bounded by
(1+cot(R*pi/(2m)))/2. No n-uniform continuity constant is needed.

### The cancellation integral is jointly continuous

For finite channel values A,B, the triangle defect is zero if AB>=0
and -2min(|A|,|B|) otherwise. Consequently

    |g| <= 2 max(|C|,|D|) min(|cot X|,|cot(X+v)|).

On the pi-circle, the two pole distances have sum at least
e=dist(v,pi*Z), so one is at least e/2. The smaller cotangent magnitude
is therefore at most cot(e/2). Combined with the preceding separation,
this gives the author's finite constant majorant on all X and all
phases for each fixed ordinary row. Choosing zero at the pole points
is legitimate for this integral and does not assign any polynomial
sample value.

For a convergent phase sequence, coefficients and v converge. Away
from the limiting two poles the integrand converges pointwise; eventual
neighborhood separation from those poles makes this valid even though
the poles move with the sequence. The limiting exceptional set is finite
and has measure zero. Dominated convergence proves continuity of I.
The proof never divides by either coefficient, a, CD or a pole residue.
Thus it covers coefficient zeros, simultaneous zeros and sign changes.

### Weighted Phi and the exact endpoint constant are continuous

The singular part of -psi(t)-psi(1-t) is 1/t near zero and 1/(1-t)
near one. Multiplying by sin(pi*t)/pi gives limit 1 at both ends;
the finite L term tends to zero. Periodic continuation with integer
value 1 is therefore continuous, including crossings in either direction.
This is the complete weighted function, not an assigned value for an
unweighted singular digamma term. The actual coefficients c_e,c_d and
offsets are continuous, and the denominator 2sin(v_r/2) is separated
from zero. Hence each complete ordinary H is continuous.

For Delta_R, the left denominator j+t is at least j and the paired
right denominator j+1-t is also at least j. D04's accepted bound gives

    |Xi_j(t)+Xi_(j+1)(-t)| <= 8/(pi^2*j^2).

Every individual summand has positive logarithm/digamma arguments on
the closed triangle, including its vertices. The summable phase-uniform
majorant proves uniform convergence and continuity of the unchanged
Delta_R. Actual polynomial R_r and S_n are continuous finite sums,
and E_D04 is continuous and nonnegative. Fixed membership therefore
makes K_fixed continuous on the whole triangle.

### Dense-set extension preserves the whole two-sided inequality

For fixed r,k, a collision imposes an affine equation whose phase
gradient is (1/n,+/-1/m), which is nonzero. Only finitely many integer
periods can occur on the compact phase triangle. Thus all collisions
lie in finitely many proper affine lines. Every neighborhood of every
closed-triangle point contains an open interior wedge; finitely many
lines cannot fill it. One may therefore approach every edge, vertex,
line intersection or double collision from collision-free interior
phases. Density only within a particular boundary edge is unnecessary.

At those collision-free phases the D04 special set equals A_fixed
exactly, and its K_D04 equals K_fixed with the same normalization:
exact rows divided by nm, H rows divided by m, and one Delta_R added.
Apply the accepted D04 estimate there. Continuity of the three complete
functions S_n,K_fixed,E_D04 passes that exact two-sided inequality to
the limit. No extra collision error is introduced. In particular this
argument does not require continuity of the old moving-membership
K_D04, equality of the two models at the limiting collision, rowwise
equality R_r/n=H, or a pointwise extension of sampled g.

The original D04 error terms may remain conservative after this
extension; no term is dropped or enlarged. Defining K_fixed and the
bound by separate absolute phases, and using the inherited exact
evenness of S_n, proves the full signed diamond claim. The unequal
n and n+1 meshes are not interchanged.

### Double collision and row count

The illustrative n=16, beta=7pi/8, alpha=0 case gives m=17 and
v_31=15pi/8. Row 31 lies outside
{0,1,32,33,16,17}. Its two offsets are 1 and 0; C=D=0, but
c_e=c_d=sin(v/2)=cos(7pi/16)>0. Thus the weighted H equals 1,
with zero cancellation integral. The two pole samples are distinct.
The corrected N1-08 local proof gives F=n/2 at each, hence R_r=n.
Its allowed endpoint strip includes z=pi/8 here. Independently, the
same finite limits follow by varying beta in the exact expression
F=[a(1+cos v)+(q/2)sin v]/(cos u-cos v) on alpha=0:
at either collision the displayed numerator derivative is
-n*sin(beta)/(2m) and the denominator derivative is -sin(beta)/m,
giving n/2.
All other row samples vanish at the target phase. This is an exact
paper check, not a computation or a premise of the dense-set argument.

Since m>=8R+1, the first R labels, last R labels and central pair are
disjoint. Their count is exactly 2R+2. With R=2 this is six exact row
labels and 2m-6=2n-4 ordinary H labels for every n>=16. This is an
outer-row count only: exact rows still contain n samples, and no cost
for H, I, Delta_R or finite polynomial evaluation is established here.

## Execution and residual limits

No numerical helper, scalar test, native executable, board evaluation,
quadrature, fit, phase cover or degree job was run. The review consisted
of proof reconstruction, file reads/searches, `git rev-parse HEAD` and
hash checks. No author file, old proof, implementation, evidence,
shared record or Git state was changed. Only this review was written.

A whole-box evaluator still needs its own validated arithmetic and
integral/series error treatment. This theorem supplies neither such a
source contract nor an end-to-end complexity/runtime claim. It also
does not finish the separate D05 phase-relative comparison or practical
M_infty-rate targets. Parent was notified of the mathematical acceptance
before this report was written.
