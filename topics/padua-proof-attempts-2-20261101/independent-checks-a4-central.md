# Independent A4(a) central-envelope proof and inspection

Rules read at `3062f77f5ead1d888fa319a7c3a20371d4f305f7`.
Codex `/root/a5_checker`, assigned gpt-6.1-sol xhigh for this bounded analytic
subtask; serving-model metadata is not separately exposed. Root owns the
15:24–18:24UTC A4 box, Git and handoffs; lead owns theory70–79 and a4 code.
This worker owns only this new record. This is supplementary independent
mathematics, not the required Claude audit. All A5/N8 files remain frozen.

Final bounded-subtask outcome: the precisely defined central envelope satisfies
R_cen(n)-C_grid(n)=o(1), over both parities. The complete assembly and inspection
of74–77 are recorded below. This identifies neither the source's searched
runner-up nor the largest noncorner maximum on the square.

## Reading and refreshed gate before the candidate

Read the full user request, all three current rule files, A4 input preparation,
T-A4a and the complete all-edge identity70. Re-read accepted A1/PD-T101's
normalization and rhombus proof, and source05/PD-T099's exact MEASURED search
definition. The full736-line registry gate had already been performed by this
worker for N7. A bounded read-only content diff against that pinned blob
`d6570b2b20a9f882b02ca4e79cd737a5fa13179e` shows the preparation's first736-line
blob `51d0d9cf79507b0b92e930a19882b942ecb94486` differs only in the three
read-in-full administrative/scientific qualifications at IDEA197, IDEA206 and
PD-N042. Read the complete new47-line MZ registration and all PD-N044–053 rows.
No Git state was changed; metadata/content-diff Git commands were read-only.

Refreshed midpoint/central/edge/localization/stationarity/Lebesgue/Dirichlet/
Bernstein searches in the registry and relevant local theory/literature. Broad
truncated search output was narrowed before relying on it. Full new shortlist:
IDEA217 with PD-T111/PD-N048 and IDEA226 with PD-T115; their signed quadrature
and oversampled reconstruction statements do not give the pointwise Padua
envelope bound requested here. The original IDEA048 / IDEA206 programme and
accepted A1 remain the closest entries. The signed corner-weight obstruction
does not refute this different point-value question. No priority or novelty
claim, new source reading or external author contact is made.

## Exact task and separation to preserve

Put m=n+1 and

R_cen(n)=max{lambda_n(epsilon,cos t):epsilon=±1,
                         |t-pi/2|<=pi/m}.

The auxiliary complementary grid phases have beta=q*pi/m and
epsilon^n*(-1)^q=-1. For odd n, the selected non-node midpoint uses q=m/2 and
epsilon=(-1)^(q+1). For even n, q is the unique odd integer nearest m/2,
distance1/2, and either x edge has the same value by x reflection. Denote this
selected grid value by C_grid(n). Lead/odd-midpoint worker are establishing its
gap from Lambda_c; this assessment must prove or bound R_cen-C_grid, rather
than assume it. The source R_search is still a different MEASURED object.
In particular n3's midpoint8/3 is not searched runner-up3.021223, and odd
n≡3mod12 includes exact midpoint zero-cardinal cusps.

## Considered candidate C1: phase-profile localization

Closest predecessor: the exact edge kernel70 and the lead's complementary-grid
triangle-defect identity. This is a registered-target continuation, not a new
kernel or a novelty claim. Write t=beta+s/m around a complementary phase.
The proposed sufficient bound is

lambda_n(epsilon,cos(beta+s/m))
 <= C_grid(n)-c*s²*log²n+C*s²*log n+C*|s|+o(1)

on a fixed small phase window, together with an outside-window leading-order
deficit that localizes the central maximizer there. It would give maximal gain
O(log^-2 n)+o(1). A physical one-sided slope O(n), including every cusp, and a
corresponding negative phase curvature of order log²n is an alternative local
form of the same route suggested independently by root.

Cheapest decisive analytic test: derive the common phase factors exactly and
determine whether the residual one-sided phase slope is O(1) or O(log n).
The latter crude bound only gives O(1) gain and does not prove the target o(1).
An exact cusp is not silently assigned derivative zero. Need also rule out a
larger branch on the other edge or away from the small phase window.

No mathematical script or numerical fit has run in this subtask. Any later
consequential computation requires prior finite-scope registration and an
actual different-agent rerun. The current localization/value-error target is
OPEN at registration; no runner-up equivalence or all-n A4 assertion was assumed.

## Exact periodic decomposition: independently derived

Write N=nm and a_j=j*pi/n. On the periodic odd checkerboard

Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd},

define v_r(s)=r*pi/m+s/m and, using the POLYNOMIAL divided difference70,

H_(j,r)(s)=((-1)^j D_n(a_j,v_r(s))-1)/2,
S_n(s)=(1/N)sum_(Gamma^-) |H_(j,r)(s)|.

Away from coincident cosines this is exactly

H_s(A,v)=a(s)*(1+cos v)/(A-cos v)+b(s)*sin v/(A-cos v),
a(s)=cos²(s/2), b(s)=sin(s)/2, A=cos a_j.                 (C2)

Proof: P_n(A)=(-1)^j(1+A). Since j+r is odd,
P_n(cos v)=-(-1)^j[cos(s)(1+cos v)+sin(s)sin v]. Insert
these into70's divided difference and subtract the corrected mode. The
polynomial definition supplies every removable value, rather than separately
assigning limits to the two fractions in(C2).

For any complementary beta=q*pi/m and physical edge epsilon, reflect the
x-index if epsilon=-1, then translate the periodic b-index by q. Complementarity
epsilon^n*(-1)^q=-1 makes the resulting checkerboard precisely Gamma^-.
Physical half endpoint weights equal one quarter of the periodic reflected
sum. Therefore, EXACTLY,

lambda_n(epsilon,cos(beta+s/m))=S_n(s)-Delta_n(beta,s),       (C3)

where Delta is the physical weighted sum of
|H_s(A,beta+s/m+b_k)|+|H_s(A,beta+s/m-b_k)|
-|H_s(A,beta+s/m+b_k)+H_s(A,beta+s/m-b_k)|.
The arguments of H in this expression mean the corresponding translated
periodic indices, so original D_n defines coincidences. This sum is nonnegative.
The two individual absolute sums agree by k->-k, which proves the normalization
S_n(s)=N^-1 sum_(Gamma^-) |H|. A non-node corner gives the same periodic odd
sum at s=0, hence S_n(0)=Lambda_c(n) EXACTLY. Finally r->-r preserves odd parity
and sends (s,v) to(-s,-v); D_n is even in its second argument. Consequently
S_n(s)=S_n(-s), including every removable term.

## Completed supporting lemma: stability of the triangle defect

**Analytic statement.** Suppose beta_n=q_n*pi/(n+1) is any complementary grid
phase on either permitted edge, beta_n->pi/2, and s_n->0. Then

Delta_n(beta_n,s_n)->g,

where, putting A=cos u and c=sin b,

g=(1/pi²) integral_0^pi integral_0^pi d_0(u,b) du db,

d_0=2*min((1-c)/(A+c),(1+c)/(c-A)) if -c<A<c, and0 otherwise.
Values on the finitely many singular curves can be chosen arbitrarily within
the bounded one-sided limits. This is the same central complementary-grid
triangle-defect constant as the lead/odd-midpoint derivation. In particular
0<g<infinity. This lemma alone gives no upper bound for S_n(s) and does not
close R_cen-C_grid=o(1).

**Proof.** Put phi=beta+s/m. Eventually |s|<=1/4 and
phi in[5pi/12,7pi/12]. For 0<b<pi let z_+=cos(phi+b),
z_-=cos(phi-b). Their separation is2sin(phi)sin b>=sin b. At least one
denominator |A-z_±| is therefore at least sin b/2. The numerator of either
term in(C2) has absolute value less than3. Thus the triangle defect d obeys

0<=d<=2min(|H_+|,|H_-|)<=12/sin b.                        (C4)

This remains true if the OTHER term is removable: the term with the separated
denominator is regular and bounds the minimum. At b=0 or pi the two original
D_n terms coincide, so d=0 exactly.

Fix 0<delta<=pi/12. When 0<b<=delta, both phi±b lie in[pi/3,2pi/3].
When pi-delta<=b<pi their cosines have the same corresponding bounds.
In either case1+z_±>=1/2, a(s)>=63/64 and |b(s)|<=1/8, so BOTH numerators
are at least47/128>0. Thus d can be positive only when A lies between z_+
and z_-. A coincident denominator with a positive numerator cannot occur
on the actual grid, because the polynomial identity proving(C2) would force
that numerator to vanish. The angular interval of possible u has length at
most2b at the first endpoint, or2(pi-b) at the second. Hence a fixed b-grid
row has at most2n*b/pi+2 eligible physical j-indices at the first endpoint.
Ignore parity and endpoint half weights for this upper bound. From(C4),
sin b>=2b/pi and w_jk<=2/N, the contribution of k=1,...,K,
K=floor(m*delta/pi), is at most

(24/N)sum_(k=1)^K[n+pi/b_k]
 =24K/m+(24/n)sum_(k=1)^K1/k.

The other endpoint has the same estimate. In particular the combined discrete
tail is bounded by100[delta+(1+log m)/n], uniformly in these beta,s. No sign
assumption has been made on the bulk, and exact endpoint rows contribute0.
The corresponding integral tails are O(delta).

On delta<=b<=pi-delta, (C4) gives the uniform bound12/sin delta. Remove
angular tubes of width eta around the two pole curves
u=fold(phi+b),u=fold(phi-b), and the corresponding limiting curves at
phi=pi/2. Each is a finite union of lines with slopes±1 in(u,b). For every
b-grid row their tubes contain O(n*eta+1) j-indices, uniformly in phi; their
total weighted mass is O(eta+1/n). Their contribution is therefore
O_delta(eta+1/n), even at exact removable grid values.

Outside these tubes all denominators are bounded away from zero uniformly:
for u,v in[0,pi], |cos u-cos v|>=2|u-v|²/pi². The rational expression(C2)
and its triangle defect consequently converge uniformly to the limiting
function d_0 as phi->pi/2,s->0. Absolute value is Lipschitz, so no separate
zero-cardinal/sign-boundary exception is required there.

The bounded limiting function on the truncated strip is continuous except
on the two pole lines; it is Riemann integrable. The positive checkerboard
weighted sums converge to pi^-2 times its angular integral: the full-tensor
part is an ordinary trapezoidal Riemann sum, while the alternating part tends
to0 by pairing adjacent j-indices for continuous approximants. Tube bounds
give the same conclusion for this bounded piecewise continuous function,
uniformly over either parity of the reflected checkerboard.

Take n->infinity with delta,eta fixed, then eta->0, then delta->0. The uniform
tail estimate proves the asserted joint limit. At phi=pi/2,s=0 the two
numerators are1∓sin b; the denominators have opposite signs precisely when
-sin b<A<sin b, giving exactly the displayed d_0. It is positive on an open
rectangle about (u,b)=(pi/2,pi/4), so the integral is strictly positive.
The tail estimate and bounded truncated strip prove finiteness. End proof.

This is a written supporting proof offered to the lead for a separate durable
theory slot if used; it is not an independent Claude audit. No mathematical
computation or numerical fitting is a dependency.

## Final independent full inspection of74–77

The entire proof of74 was read and reconstructed. The fixed-width
near-diagonal strip contains every moving pole; the polynomial divided
difference there is bounded using |T_l'(cos t)|<=min(l²,l/|sin t|). The bound
C_L*n/(sin u+1/n), summed over O_L(1) second indices per first index, gives
O(log n) after normalization. Outside that strip both sine denominator factors
are comparable with their unshifted values. Exact subtraction of E reduces
mesh deformation to reciprocal-square and cotangent sums, with normalized
error O(log n). The G channel has the same logarithmic bound. The endpoint
rows contribute O(1) using the polynomial definition. Thus the coefficient
cos²(s/2) of Lambda_c is preserved uniformly on[-pi,pi]. No pole exception,
parity hypothesis or global-corner premise was found.

The ENTIRE local module in independent-checks-a4.md lines318–470 and the full
durable75 were read and independently reconstructed. In particular:

- The small-window moving-denominator family r=j+1,j>=2n/3 is handled
  separately, not discarded.
- The regular sine gaps use the odd index difference and retain a uniform
  gap after the phase shift. Fixed-difference reciprocal d sums have bounded
  multiplicity, giving the stated harmonic and higher-power estimates.
- Direct derivatives of f and g give75(7), including the f_vv mixed inverse
  powers and O(1) scaled g derivatives. Symmetric Taylor pairing removes first
  order only in the primitive S_n.
- Actual numerator sign changes remain a positive error. Only rows near the
  negative cosine endpoint contribute, with total
  O(s²log m)+O(|s|log m/m); these events are not assumed absent.
- The removed family has the exact finite U_n cancellation through moving
  coincident cosines. Its normalized absolute sum is O(1)-Lipschitz, with no
  lower bound imposed on a formerly vanishing denominator.
- Separate r=0,m estimates retain the true H_(n,m)(0)=n and finite expression
  cos(s/2)U_n(s/(2m)); no formal zero or independent E/G limit replaces it.

A2 source01 was re-read in full, including the harmonic proof of
Lambda_c>=(4/pi²)log²n-54. Thus75's completion of the square gives a uniform
primitive excess O(log^-2 n). No blocker was found in75.

The full76 was checked against the proof supplied above. It preserves exact
physical/periodic normalization, all-sequence quantifiers, endpoint numerator
47/128, the100-tail bound, bounded-other-denominator argument at removables,
moving-pole tube counts and checkerboard Riemann density. No discrepancy or
missing zero-cardinal exception was found. The separate odd-midpoint agent
also independently reconstructed this complete defect argument.

The full77 was read, including its scope, numerical-source attribution and
every assembly step below. Its rational enclosure for g is attributed to73
and the actual two-agent Fraction evaluation in independent-execution-a4-g.md.
That receipt, including actual exit confirmations and its distinction between
file comparison and execution, was read. No execution of that code is claimed
by this worker. Source72's integral normalization and73's positive
integral/series description were also read in full. Later editorial77 wording
was checked: the n3 counterexample prevents C_n=R_search for all degrees; it
does not refute a possible identification of R_cen with a global competitor,
which remains OPEN.

No finding was identified in74–77 within this declared analytic scope. This
is supplementary reconstruction, not the required Claude audit.

## Completed assembly, retaining all nearest-grid choices

Let C_n=C_grid(n) be the selected sequence. Its angle lies in the defining
central cell: exactly pi/2 for odd n and at distance pi/(2m) for even n. The
phase identity and the joint defect limit at s=0 give

R_cen(n)>=C_n=Lambda_c(n)-g+o(1).                           (C5)

For each n choose ANY maximizer (epsilon_n,phi_n) in the compact definition
of R_cen. On that same edge choose a nearest complementary ordinate
beta_n=q_n*pi/m. Permissible q indices form one parity class of spacing2, so
|phi_n-beta_n|<=pi/m. Put s_n=m(phi_n-beta_n). Then |s_n|<=pi and
|beta_n-pi/2|<=2pi/m; hence beta_n->pi/2 and lies strictly between0 andpi
for all sufficiently large n.

The nearest ordinate need not be the selected C_n point: it may be an endpoint
ordinate on the other odd-degree edge, a tied nearest ordinate or an ordinate
just outside the central cell. All retain the complementary parity and the
same central limit. No uniqueness, stationarity or differentiability of the
maximizer is used, and central-cell endpoint maxima are included.

Use R_cen=S_n(s_n)-Delta_n(beta_n,s_n), Delta_n>=0,74 and(C5). Then

sin²(s_n/2)*Lambda_c(n)<=C log(n+1)+g+o(1).

The A2 lower bound and sine chord on[-pi,pi] imply
|s_n|=O(log^-1/2 n). Thus every maximizing angle is within
O(1/[m sqrt(log n)]) of SOME complementary ordinate. This does not claim that
every maximizer lies near the one selected odd midpoint on the same edge.

Eventually |s_n|<=pi/6. Result75 gives
S_n(s_n)<=Lambda_c(n)+O(log^-2 n). Result76 applies to these SAME moving
phases and gives Delta_n(beta_n,s_n)->g. Therefore

R_cen(n)<=Lambda_c(n)-g+o(1).

Together with(C5), this proves

R_cen(n)=Lambda_c(n)-g+o(1),
0<=R_cen(n)-C_n=o(1).                                     (C6)

If 'best central complementary grid value' means the maximum G_n over all
complementary grid points inside the central cell, then C_n<=G_n<=R_cen.
Hence0<=R_cen-G_n<=R_cen-C_n=o(1) too. No assumption that the selected odd
midpoint is exactly best at finite n is needed.

Exact midpoint cusps, including n≡3mod12, do not invalidate(C6):75 retains
numerator sign changes and every finite U_n value, while76 is a joint limit
through moving singular/zero-cardinal events. This argument never sets the
derivative of the ACTUAL lambda midpoint branch to0 by symmetry. Only the
periodic primitive S_n is paired as an even function.

## Retained subroutes, rules impact and stop

The crude absolute G-channel estimate O(|s|log n) was considered and found
insufficient: balancing it with log² curvature gives only O(1) gain. It is an
inadequate estimate, not a refutation of the target. Exact pairing and sign
changes replace it. A classification of exact midpoint zeros via cyclotomic
intersections was considered but not used or claimed: the uniform argument
retains ALL zeros without classification. Sharper second derivatives for the
exceptional family were unnecessary; its proved Lipschitz cost suffices.

At root d8b878b348a94575e7753e5a756d969d41d5bca8 the changed WORKFLOW
results paragraph was re-read. It makes results repository-only; mathematics,
models, evidence and registry rules are unchanged. The user's TOPIC-only write
scope and root's exclusive results/Git/handoff ownership remain in force.

Root stopped A4 mathematics at2026-11-01 16:13:22UTC after the authorized
central-envelope formulation reached its done criterion. Full inspections,
normalization/tail proof and assembly were completed before that stop; only
this administrative consolidation and content hashing followed. No A4
mathematical script, fit or extra numerical run was performed by this worker.
No global A4(b)/(c), critical-branch uniqueness, R_search identity or
full-square runner-up statement is proved here. Claude audit remains PENDING.

## Exact proof inspection pins

Full proof bodies74–77 were read before stop. Lead then synchronized only
status metadata and clarified77's Scope; the latter wording was read above.
Proof sections remain unchanged. The resulting whole-file pins are:

| File under theory/ | Bytes | SHA-256 |
|---|---:|---|
| `proof-attempts-2-codex-74-global-edge-phase-localization.md` |9459|`e77c0fc3d9370fdd946d82463fa2c566e5b5c8367e3109dd41f99963d9952a1c`|
| `proof-attempts-2-codex-75-local-edge-phase-bound.md` |9347|`4d7fb4dab757d33c8378ae4bba4b67fad50b3bd1d36b861da0ab217377198cb6`|
| `proof-attempts-2-codex-76-central-triangle-defect-stability.md` |7266|`349efba80c37a660fca108064cbf53a2a7512a24e737b1f949274646a9bdc499`|
| `proof-attempts-2-codex-77-central-edge-envelope-expansion.md` |8769|`cadcfbdead5b1e69ab703edafef3c895f43de44f7503b292ee855dac0e4e74a3`|

A later metadata-only append must be tracked as a changed file identity; this
receipt does not silently cover unseen proof edits. It is ready for root's
checkpoint and frozen after its final content hash is reported. It supplies
the bounded central-envelope subtask, not approval of the entire topic or a
replacement for Claude.
