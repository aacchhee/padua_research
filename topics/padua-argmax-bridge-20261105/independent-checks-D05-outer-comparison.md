# Supplementary independent check — D05 outer variation and full rate

Rules/read input: `084a64f6465956f9c75b5538f83752c30318f151`;
observed review HEAD: `41c4c804456fbaf952dda344a5ff9795a0252f64`.
AGENTS/WORKFLOW/CODEX and state/IDEAS.md are unchanged between those
commits. Reviewer: distinct Codex subagent `/root/d01_far_review`,
parent-requested Astra xhigh; actual serving metadata unexposed.
Formal Claude audit remains separate.

## Verdict and frozen scope

**ACCEPTED as written; no unresolved finding.** The full-phase variation
and signed strip estimates justify the joint comparison. For fixed R,delta
on the stated domain, the displayed error is uniformly
O((1+log n)/n) for the unchanged completed model M_infty. In particular
R=2,delta=pi/8 has the literal validity threshold n>=32.

The practical size of this error at 10^3--10^4 is not established, and
no phase cover, global argmax onset or implementation follows. That
stronger practical target correctly remains **OPEN**. This is supplementary
mathematical acceptance, not formal Claude approval or a degree certificate.

All four assigned records were read completely and their hashes checked:

| Record | SHA-256 |
| --- | --- |
| [D05-outer-profile-variation.md](theory/D05-outer-profile-variation.md) | `47fc61298520609f591c03eea323e93949d59d54cbcfa90e0d4943548113bd66` |
| [D05-outer-comparison.md](theory/D05-outer-comparison.md) | `d862ab5071de128577773b4a658c6c70f2859e2b2ff083074909372041ec7502` |
| [D05-outer-profile idea](ideas/D05-outer-profile.md) | `97aa5d4fe0475863bb210690a0461eaad9dbc9d3b2080d09b64d252c7b236845` |
| [D05-outer-profile attempt](attempts/D05-outer-profile.md) | `46f809ffc76939dbfd04db199118721382aa2dbaf6c47b48db47ad2484f7c53b` |

The author's recorded input is
`a6d7a788b3ce457a4631bbb507624303240c570c`. No author proof, shared
record or Git state was changed by this reviewer; no fix was requested.

## Reconstruction of the new variation estimate

**The large endpoint coefficient cancels exactly.** On either endpoint
half, the integral symmetries give J(u,s,z) with u=p/2,
s_L=w+q/2, s_R=|w-q/2| and w=a cot(z/2). Subtracting
J0=2w log sin(z) leaves

    k_s=2(s_s-u)_+-2w,
    k_L=max(q-p,-2w),
    k_R=max(-P,q-p-4w,-2w).

For the right formula, w>=q/2 gives max(-P,-2w), and w<=q/2 gives
max(q-p-4w,-2w); the displayed three-term maximum combines them exactly.
Both k functions increase as z increases, since w decreases. Their values
lie in [-P,P]; summed variation <=4P and summed sup norms <=2P imply
the product variation <=6P*(-log sin epsilon). No O(a/epsilon)
coefficient is left in this product estimate.

**The remainder costs only a logarithm.** The full-domain generic
formula gives |R_s|<=log((u+s)/|u-s|), and for s>u,
`0<=R_z<=2u cot z`; for s<=u its separation derivative is zero.
The left s curve is monotone, the right has at most two monotone pieces,
and both lie in [0,S], S=1/2+2a/epsilon>=u. Integration of the parameter
envelope therefore costs at most3G. Integrating the separation envelope
along both actual curves costs4u*(-log sin epsilon)=2p*ell. This yields

    sum Var(I_s-J0)<=3G+(2p+6P)ell.

The logarithmic singularity at s=u is integrable, and the root/no-root
formulas join continuously. Constant-curve cases have zero parameter
motion; at u=0, R vanishes identically. Thus no derivative division by
p, a or a root-separation parameter is needed. Coalescing transitions
and coefficients that vanish identically do not create omitted pieces.

**The singular reference replacement is uniformly bounded.** The identity

    J0-4a log(z)/z = f(z)log sin(z)+g(z),
    f=2a cot(z/2)-4a/z,
    g=4a log(sin(z)/z)/z

has continuous zero limits at zero. On [0,pi/2], |f'|<=a and |f|<=az
follow from the sine lower bound. Product variation gives less than3a
for f log sin. Also
`0<=1/z-cot z<=pi*z/6` and
`0<=-log(sin(z)/z)<=z²/(6-z²)<=z²/3` give
`|g'|<=4a(pi/6+1/3)` and variation less than7a. Paying10a per side
proves the endpoint bound with20a. The stated elementary bounds all
hold up to pi/2, not just asymptotically at zero.

**Central and numerator terms use full-domain sources.** C06's central
bound for I_s-d log(pi-z) has combined variation <20. On the central
halves the variation of4a log(z)/z is <3a per side; on the endpoint
halves subtracting d log(pi-z) costs at most d log2 per side. These
produce26a+20+2d log2 in V_B, with no jump at pi/2. C06's separate
regular numerator variation is <23 on the full phase triangle.

For the L coefficient, the exact two max formulas apply on all
0<z<=pi. The two increasing maxima have total change at most
2max(p,q); each decreasing u0=T-4a/z changes by4a/pi. Therefore
`V_A=2max(p,q)/pi+8a/pi²<3/2`. At a=0 the relevant maximum curves
are constant, and the same upper bound remains valid. This independently
accounts for every term of the displayed phase-dependent V_A,V_B.

The simpler constants also check: since2S+p<=6/epsilon,
`G<=p[1+log(6/epsilon)]+p log(1/p)` and p log(1/p)<=1/e.
The logarithmic coefficient in the numerator braces is at most17;
the constant part is <52. This gives V_B<=41+6log(6/epsilon).
At p=0, the assigned G=0 is the continuous limit for each epsilon>0,
and this uniform entropy bound still controls phase sequences depending
on n. At a=0 on the diamond edge p=q, the cancellation is exactly zero;
at p=q=0 its stated limiting conventions remain finite.

## Actual cells and signed strip comparison

Centered-cell BV quadrature costs h/2 times the cell variation, and
disjoint cells add without multiplying by the number of holes. The
ordinary D04 centers are at least hR from the folded endpoints and at
least h from pi. With epsilon=h(R-1/2), their full centered cells lie
in [epsilon,pi]. This includes beta=0,pi and all collision deletions.
For n>=8R, epsilon<=pi/4, 6/epsilon<=4m/pi<2m, and
log(2m)<=log n+1. Substitution gives the claimed
`(4log n+25)/(n+1)` bound. It is only for the regularized profile on
those actual cells; no missing interval is silently added to this result.

For the strip estimate, begin with both unperforated index blocks
R<=k<=K_s. The exact lower and upper cell boundaries are

    l_s=h(R+t_s-1/2),
    u_s=h(K_s+t_s+1/2), K_s=floor(delta/h-t_s).

Thus epsilon<=l_s<=lambda=h(R+1/2) and |u_s-delta|<=h/2, including
floor equalities. The degree condition ensures K_s>=R and
h<=delta/(2R). It follows that lambda<=5delta/8 and all expanded cells
lie below delta+h/2<=9delta/8<=9pi/64<pi/4. This last check matters:
the entire cell union stays inside N1-05's endpoint-envelope domain.

The two-side variation of Z on these cells is at most
`23+[3G+(2p+6P)ell+20a]/pi<=32+6log(6/epsilon)`.
Its quadrature charge is the first term of T_Z. The two initial missing
integrals are bounded together by Q(P,lambda), since W_P is positive
and decreasing. The two upper mismatches have combined length <=h,
so their normalized cost is W_P(delta-h/2)/m. Finally, deleting at most
two collision sample terms costs2W_P(hR)/m; every deleted sample has
z>=hR. The temporary collision profile values are well-defined weighted
profiles and never replace the actual polynomial rows.

This reconstructs T_Z with all its factors and signs. In particular
Q(P,lambda), with lambda proportional to1/m, is the initial loss;
Q(P,delta) is not charged. Writing lambda=h(R+1/2) explicitly gives

    Q(P,lambda)=2(R+1/2)/m *
       [7+(P/pi)(5+2log(4m/(R+1/2)))].

The logarithms in the other shrinking terms likewise involve epsilon
or hR. Since delta-h/2>=7delta/8, the upper-boundary term has a fixed
finite coefficient. Hence T_Z has the stated uniform fixed-parameter
rate with no residual cutoff floor.

Exact low-degree topology was checked algebraically, without a numerical
run: at n=32,R=2,delta=pi/8, X=33/8. For t=0, the two K values are4
and3; for t=1/2 both are3. At t=1/8 one upper center is exactly delta,
and the corresponding upper half-cell is charged in full. The included
left collision alpha=31pi/33,beta=0 occurs at r=2,z=2pi/33 and is
deleted from the residual block, while its polynomial row stays exact.
The double right-end collision alpha=0,beta=15pi/16 occurs at r=63,
z=pi/16: both board poles are in one row, so it deletes one residual
sample, not two rows. Both examples satisfy the stated strip geometry.

## Joint comparison and error accounting

The endpoint partition of K is exactly the N1-08 block E plus its ordinary
signed Z sum. N1-08 has the same R>=2, n>=ceil(2pi R/delta) hypotheses;
delta<=pi/8 is within its delta<=pi/4 domain. Its C_R and finite sinc
conventions, including simultaneous collisions, are unchanged. H_n<=1+L
gives precisely the restated e4 components. Thus the endpoint block is
replaced by its quadratic polynomial with error e4, and its residual
by the full signed strip integral J_Z with error T_Z.

Inside D=(delta,2pi-delta), ordinary entries of K are already H. The
D02 interior argument therefore needs no ordinary-kernel E_n term.
Its regular centered-cell cost is (VA*L+VW)/(2m). At most four omitted
special cells and boundary length h cost5(Astar*L+Wstar)/m. The four
actual special norms cost4(Astar*L+Vstar)/m, plus their weighted pole
profile errors. The central log costs d[4+5log m]/(pi m). These sum
to exactly I_n+D_pole. The special-row upper is a continuous bound
for the actual polynomial; H is not asserted equal to a collision row.
Nonnegativity of the actual norms and the triangle inequality suffice
for this two-sided integral replacement.

The budgets have distinct roles:

| Term | What it pays |
| --- | --- |
| E_D04 | Actual S to K: ordinary weighted poles, cancellation perturbation and matched reference |
| e4 | Exact endpoint block to its finite profile and mesh polynomial |
| T_Z | Ordinary endpoint residual samples to their signed full strip integral |
| I_n | Interior profile quadrature, missing cells and coarse actual special-row bounds |
| Additional D_pole | Weighted pole-profile error used only in bounding those interior special norms |

The D04 pole allowance and the additional D_pole each use a conservative
full coefficient-sum bound, for ordinary and interior-special uses
respectively. Adding them is conservative; it neither omits a share nor
requires subtracting a previously paid error. No r_n, old O(a/R) bound,
or fixed-model beta estimate is needed in K-to-M_infty.

The constant identity is exact:

    C_R+c_mesh+integral_D B/pi = E_R+K_delta,
    J_Z=K_0-K_delta,
    Delta_R=E_infty-E_R.

Together with the exact b_end plus integral A coefficient identity,
these give M_infty with no remaining R- or delta-dependent constant.
This establishes both displayed comparisons by the triangle inequality.
The sign of each added term agrees with D02 and D04; the unchanged
M_far's nondecaying bias has not been discarded or redefined.

For fixed R,delta, CX has order log(n)/n and the N1 endpoint errors have
that or smaller order. The interior phase factors are bounded on the
closed diamond, including the entropy limit; log m<=L+1 handles its
log term. E_D04 and both pole allowances also shrink. This proves the
uniform rate with the explicit displayed scalar bound. It does not
establish that the constants meet any practical margin.

## Dependency and novelty coverage

The complete 1112-line state/IDEAS.md previously read by this worker is
unchanged at
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
This full reading, including the obstruction tables, is carried forward
at identical bytes. Fresh D05 searches covered outer variation, signed
residuals, cell unions, bounded variation, endpoint logarithms, joint
strips and fixed strips in the registry, current candidates, relevant
N1 source files and literature INDEX. Capped search output is not
reported as a full read of every matched source.

Read both new proofs and the complete idea/attempt. Refreshed C06's
full-phase numerator/generic-integral/central variation proofs, N1-13
in full, N1-14's integral and derivative formulas, D02's complete
interior/topology argument, N1-08's exact block and rate hypotheses,
C06's coefficient integration and D02's signed bias identity. The full
matched upstream reading and audits of N1-02 through N1-08, C06, C08,
D01/D02, D03 and D04 are recorded in this same worker's earlier
[D01](independent-checks-D01-far.md), [D02](independent-checks-D02-far.md),
[D03](independent-checks-D03-cancellation.md) and
[D04](independent-checks-D04-row-reduction.md) reviews. That coverage is
reused explicitly rather than claiming another complete audit of every
old theorem. The D04 row/reference hashes remain respectively
`2eed7940022efbc0e018ddf6a06da68bb2b40d947af305e28d641c5d4b3050cf`
and `bb89a7e3c3b3c174c877e465500ddfd033ceba00e2e578aeae0151856024c622`.

Closest scope is N1-05's integrable residual envelope, N1-13/14's
regular/central variation, C06's full-domain extensions, D02's completed
constant and D04's matched row reference, within IDEA337/459's retained
full-profile continuation. D05 adds the bounded endpoint coefficient
after J0 subtraction, its logarithmic BV cost, and a signed strip
comparison that shrinks. It does not extend the near-only constants
by assertion. Retained alternatives and the switch to a fixed strip
after the initial variation test are disclosed in the idea/attempt.
No external theorem, historical priority claim or new negative result
is asserted. D01's old-model obstruction and D03's whole-kernel collision
warning retain their scopes.

## Execution and remaining limits

Analytical review only. Tools read/search the named files, check hashes
and unchanged rule/registry diffs, and write this report. No scientific
numerical code, scalar budget, native/kernel/board evaluation, quadrature,
phase sweep, fit or generated receipt was executed. The exact geometry
examples above are paper substitutions, not claims of a computational
rerun. No instrumented analytical elapsed time or scientific CPU total
is asserted.

The explicit full rate is accepted; numerical usefulness at the desired
onset, a validated phase margin, efficient evaluation, phase-box topology,
and any global argmax threshold are not assessed. The practical target
therefore remains OPEN, and formal Claude audit remains outstanding.
