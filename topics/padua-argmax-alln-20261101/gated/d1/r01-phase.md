# Direction 1, round 1 — two-phase primitive estimates

Date: 2026-11-02. Developer: Codex, parent-assigned gpt-6.1-sol xhigh;
runtime metadata is not independently exposed. Rules/snapshot head:
`2dde541f1e5af239cae6e93e4438b9be89d15d87`; scientific input:
`7d308b10d946b607ae0690454f6c0103690775a4`. This directory is an exported
snapshot, without a local Git repository. No Git operation was performed.

Round contract: [PROTOCOL](../PROTOCOL.md), direction 1 round 1. Assigned
scope is the analytic primitive, not the four-copy defect, corners,
effectivity, future rounds, or a global all-degree conclusion.

## Gate and retained variants

Before development, read AGENTS, WORKFLOW, CODEX, handoff04, protocol,
the complete IDEAS headings/aliases/summaries and all its obstruction and
disposition tables (full registry, in overlapping chunks), full shortlisted
IDEA-305 registration, original Claude-02 with amendments, fallback-04,
part2 theory74–76, and current theory04/05. Mechanism searches covered
`phase`, `two.phase`, `coset`, `shift`, `pole`, `primitive`, `majorant`,
`triangle defect` across these topic attempts, gates, theory and registry;
the literature INDEX was screened for these terms. No external source is
transferred and no historical novelty claim is made.

Closest candidate: IDEA-305, original Claude-02, fallback-04. Verdict:
**implementation variant**, extending the primitive estimate from one
phase to two. The separation criterion is uniformity for two independently
shifted meshes while preserving polynomial collisions and numerator sign
changes. A two-phase contribution larger than logarithmic globally, or a
nonvanishing small-phase excess, kills the corresponding proposed bound.
Numerical agreement is not a proof. This round uses analytic estimates;
the small identity sanity check recorded at the end has no proof role.

Retained unsuccessful or insufficient variants:

| Variant | Disposition / exact reason |
|---|---|
| Absolute sine-channel bound locally | Insufficient: gives only \(C\rho\log n\), whose optimization against the quadratic leading loss need not vanish. Retained globally. |
| Copy PD-T190's sign-change row count verbatim | Failed proof step: the extra \(-\sin\alpha\sin u\) channel permits width \(y\asymp\sqrt{\rho x}\), not just \(O(\rho)\). Repaired below by splitting in \(x\). This does not refute the desired inequality. |
| Divide the top collision family into independent rational channels | Abandoned proof route: creates artificial poles. Use the finite trigonometric sum identity below. |
| Primitive maximal exactly at zero phase | Already failed in prior MEASURED scope (Claude-01); not reasserted. The target is vanishing excess. |

## Exact statement and status

Let \(n\ge2,m=n+1,N=nm\),
\(\Gamma^- =\{(j,r):0\le j<2n,0\le r<2m,\ j+r\text{ odd}\}\).
Use PD-T185's finite polynomial \(D_n\), and put

\[
 G_n(u,v)=D_n(u,v)-\cos(nu),\quad
 F_{jr}(\alpha,\beta)=\tfrac12(-1)^j
 G_n(j\pi/n+\alpha/n,r\pi/m+\beta/m),
\]
\[
 S_n(\alpha,\beta)=N^{-1}\sum_{\Gamma^-}|F_{jr}(\alpha,\beta)|,
 \qquad a(\alpha,\beta)=\tfrac12(\cos\alpha+\cos\beta).
\]

This normalization is the shifted-lattice majorant, because
\(|\Gamma^-|=2N\) and \(|G|=2|F|\). At \((0,0)\),
\(S_n=\Lambda_c(n)\), including the polynomial value at \((\pi,\pi)\).

**Round claim A (written analytic proof, independent review pending).**
There is an absolute \(C\) such that, for every \(n\ge2\) and
\(|\alpha|+|\beta|\le\pi\),

\[
 S_n(\alpha,\beta)\le a(\alpha,\beta)\Lambda_c(n)
                                  +C\log(n+1).                 \tag{A}
\]

**Round claim B (written analytic proof, independent review pending).**
There are absolute \(\rho_0>0,C\), for example a sufficiently small
\(\rho_0\le\pi/48\), such that for all \(n\ge2\) and
\(\rho=|\alpha|+|\beta|\le\rho_0\),

\[
 S_n(\alpha,\beta)\le a(\alpha,\beta)\Lambda_c(n)
                         +C\rho^2\log(n+1)+C\rho.             \tag{B}
\]

Consequently the nonnegative supremum over this fixed phase neighborhood
of \(S_n-\Lambda_c\) is \(O(\log^{-2}n)\). In particular
\(S_n(\alpha_n,\beta_n)\le\Lambda_c(n)+o(1)\) whenever both phases
tend to zero.

Status of the all-square target PD-T099: **OPEN**. The claims above are
development lemmas requiring distinct review and the eventual Claude
audit; this round file makes no accepted-registry status change. They
should receive their own durable theory home if retained after review.
The proof is analytic, with no finite computation as a premise.

Dependencies: accepted polynomial/kernel convention PD-T185, zero-phase
normalization PD-T189, and corner lower bound PD-T159. The mesh argument
below extends PD-T189/190 rather than interchanging the asymmetric meshes.

## 1. Verify the numerator before estimating

Write \(u=j\pi/n+\alpha/n,v=r\pi/m+\beta/m\), \(j+r\) odd,
and \(P_n=T_m+T_n\). Direct angle addition gives

\[
 P_n(\cos u)=(-1)^j\{\cos\alpha(1+\cos u)-\sin\alpha\sin u\},
\]
\[
 P_n(\cos v)=-(-1)^j\{\cos\beta(1+\cos v)+\sin\beta\sin v\}.
\]

Subtract \(\cos(nu)=(-1)^j\cos\alpha\) from the divided difference.
For unequal cosines this gives exactly

\[
 (-1)^jG_n(u,v)=
 \frac{(\cos\alpha+\cos\beta)(1+\cos v)
            -\sin\alpha\sin u+\sin\beta\sin v}{\cos u-\cos v}.
                                                               \tag{1}
\]

Thus \(F=af-\tfrac12\sin\alpha\,g_u+\tfrac12\sin\beta\,g_v\), where
\(f=(1+\cos v)/(\cos u-\cos v)\) and
\(g_u=\sin u/(\cos u-\cos v),g_v=\sin v/(\cos u-\cos v)\).
At equal cosines only the original finite polynomial defines \(F\).
Formula (1) is used only with a nonzero denominator or after clearing it.

Reflecting the periodic first and second indices to their physical meshes
shows that the sum is the endpoint-weighted average of the four phases
\((\pm\alpha,\pm\beta)\). With endpoint factors \(e_j,f_r\), this is

\[
 S_n=\frac1N\sum_{\substack{0\le j\le n,0\le r\le m\\j+r\ {\rm odd}}}
 e_jf_r\sum_{\sigma,\tau=\pm1}|F_{jr}(\sigma\alpha,\tau\beta)|.
                                                               \tag{2}
\]

Endpoint duplication in (2) is intentional: at a reflected endpoint the
two values agree by evenness of the original polynomial, and the half
weight restores the original count. In particular simultaneous negation
pairs the regular signed Taylor terms exactly.

## 2. Global bound (A)

Work in (2), with base angles \(u_0=j\pi/n,v_0=r\pi/m\). Interior
shifted angles lie in \([0,\pi]\) for the full diamond. Remove all
endpoint rows and columns, and the fixed strip
\(|u_0-v_0|\le8\pi/n\). In that strip both shifted angles are within
\(10\pi/n\) of \(u_0\). The divided difference is bounded by the
maximum of \(|P_n'|\) on their cosine interval. Using
\(|T_k'(\cos t)|\le\min(k^2,k/|\sin t|)\), its size, and hence
\(|F|\), is at most
\(Cn/(\sin u_0+1/n)\). There are \(O(1)\) second indices for each
first index, so the normalized strip sum is \(O(\log(n+1))\).
This also bounds the removed zero-phase reference sum. Collisions are
included by the polynomial derivative bound.

On the far set put \(P=(u_0+v_0)/2,T=(u_0-v_0)/2\). Each shifted
denominator stays within fixed positive factors of the base denominator,
including intermediate shifts of just one coordinate. Uniformly in the
other angle and with the far-set exclusion retained,

\[
 \sum_j|\sin T|^{-1}\le Cn\log(n+1),\qquad
 \sum_j\sin^{-2}T\le Cn^2,                                \tag{3}
\]

and the analogous sums over \(r\) have \(m\) in place of \(n\).
These follow from the sine chord inequality and harmonic/reciprocal-square
series; no arbitrary fractional pole is allowed into the sum.

For a first-coordinate shift \(|h|\le\pi/n\), exact subtraction gives

\[
 |f(u_0+h,v_0)-f(u_0,v_0)|
 \le C\{ |h|\cot(u_0/2)+h^2\csc^2(u_0/2)\}\sin^{-2}T.
                                                               \tag{4}
\]

Indeed the numerator of the difference is
\((1+\cos v_0)|\cos(u_0+h)-\cos u_0|\), the cosine difference is
at most \(|h|\sin u_0+h^2/2\), and
\(\sin P\ge\sin(u_0/2)\cos(v_0/2)\). For the subsequent
second-coordinate shift the identical argument uses
\(\sin((u+v_0)/2)\ge\cos(u/2)\sin(v_0/2)\), giving (4) with
\(v_0,m\) in place of \(u_0,n\). Summing (4), (3),
\(\sum_{j=1}^{n-1}\cot(u_0/2)=O(n\log(n+1))\), and
\(\sum\csc^2(u_0/2)=O(n^2)\), gives normalized cost
\(O(\log(n+1))\) for both deformations. Also
\(|\sin u|+|\sin v|\le C\sin((u+v)/2)\) on this far interior set,
so both sine channels cost \(O(\log(n+1))\) by (3).

Each removed endpoint row/column costs \(O(1)\): within \(O(1/n)\)
of its matching endpoint there are \(O(1)\) entries of size \(O(n^2)\),
and outside it the bounded numerator divided by a squared angular distance
sums to \(O(n^2)\). The same applies to the reference rows. Finally
\(a\ge0\) on the fundamental diamond, since
\(a=\cos((\alpha+\beta)/2)\cos((\alpha-\beta)/2)\).
The triangle inequality, the reference identity and these estimates prove
(A).

## 3. Local regular set and signed Taylor estimate

In the physical mesh remove
\(B=\{r=j+1,j\ge2n/3\}\), including \((n,m)\). For every remaining
odd pair put
\(L=|j-r|\ge1,d=\min(j+r,2n+1-j-r)\ge1\).
For all phase choices of total size at most \(\rho_0\), and along their
straight paths from zero, the shifted half angles satisfy

\[
 t=|\sin((u-v)/2)|\ge cL/m,\qquad
 b=\sin((u+v)/2)\ge cd/m.                                 \tag{5}
\]

For \(j>r\), the base difference is at least \(\pi L/m\); for
\(r-j\ge3\) it is at least \(\pi(L-1)/m\). The only residual odd
difference is \(r=j+1\), for which the nonremoved indices have base
gap at least \(\pi/(3m)\). The perturbation is at most \(\rho_0/n\).
This proves the first bound for small fixed \(\rho_0\). The distances
of the half sum from its endpoints give the second. Thus all regular
denominators retain their base signs.

In the derivatives below, \(P=(u+v)/2,T=(u-v)/2\) are the shifted
half angles, so \(b=\sin P,t=|\sin T|\). On this set
\(|\sin u|+|\sin v|\le Cb\), also for the slight endpoint
overshoots. Differentiating the rational functions therefore gives, for
either coordinate derivative and every second derivative,

\[
 |\nabla f|\le Cb^{-1}t^{-2},\quad
 |\nabla^2 f|\le C(b^{-2}t^{-2}+b^{-1}t^{-3}),              \tag{6}
\]
\[
 |g_u|+|g_v|\le C(t^{-1}+b^{-1}),\quad
 |\nabla g_u|+|\nabla g_v|\le C(t^{-2}+b^{-2}),\quad
 |\nabla^2 g_u|+|\nabla^2 g_v|\le C(t^{-3}+b^{-3}).         \tag{7}
\]

For example \(g_u=-(\cot T+\cot P)/2\),
\(g_v=-(\cot T-\cot P)/2\). The bounds on \(f\) follow by
differentiating its numerator/denominator; the sine factors in denominator
derivatives are bounded by \(Cb\). For fixed signed \(j-r\), the
possible \(d\) have multiplicity at most two. Consequently, with all
sums normalized by \(1/N\), (5)–(7) imply

\[
 \sum|\nabla f|/n=O(\log m),\quad
 \sum|\nabla^2f|/n^2=O(\log m),\quad
 \sum(|g_u|+|g_v|)=O(\log m),
\]
\[
 \sum(|\nabla g_u|+|\nabla g_v|)/n=O(1),\quad
 \sum(|\nabla^2g_u|+|\nabla^2g_v|)/n^2=O(1).               \tag{8}
\]

Termwise suprema along the small phase paths obey the same estimates.
For example the \(b^{-1}t^{-3}\) double sum is
\(O(m^4\log m)\), while \(b^{-2}t^{-2}\) sums to \(O(m^4)\);
division by \(Nn^2\) gives (8). Replacing \(n\) by \(m\) in a
coordinate scaling changes only absolute factors.

Let \(E(\alpha,\beta)=F(\alpha,\beta)-a(\alpha,\beta)f(u_0,v_0)\).
Apply one-variable symmetric Taylor to
\(E(t\alpha,t\beta)\), \(-1\le t\le1\). It vanishes at zero.
Its second derivative consists of \(a''(f-f_0),2a'f',af''\),
and the three product-rule terms for each sine channel. Formula (8),
\(|a'|\le C\rho^2,|a''|\le C\rho^2\) along this path, and
\(|f-f_0|\le C\rho|\nabla f|/n\), show that the normalized
sum of its absolute second derivatives is at most \(C\rho^2\log m\).
Thus the normalized signed excess in either simultaneous-negation pair
in (2) is at most \(C\rho^2\log m\).

## 4. Numerator sign changes: the new two-phase issue

On the regular set choose \(\chi=\operatorname{sign}(\cos u_0-\cos v_0)\),
also when the reference numerator is zero. Then
\(|F|=\chi F+2(-\chi F)_+\). The first term is handled above.
The second is precisely the contribution of negative numerators in (1).

Put \(x=\pi-u_0,y=\pi-v_0,X=x-\alpha/n,Y=y-\beta/m\).
The numerator of \(F\) is

\[
 A=a(1-\cos Y)-\tfrac12\sin\alpha\sin X
                         +\tfrac12\sin\beta\sin Y.        \tag{9}
\]

If \(A<0\), \(a\ge c>0\) and the sine chord inequality give
\(|Y|^2\le C\rho(x+\rho/n+|Y|)\). Therefore

\[
 |Y|\le C(\rho+\sqrt{\rho x}),\qquad
 y\le C(\rho+\sqrt{\rho x}).                              \tag{10}
\]

Choose a fixed sufficiently large \(K\). If \(x\le K\rho\), (10)
implies \(x,y\le C\rho\). Here the numerator magnitude is at most
\(C\rho(|X|+|Y|)\), while
\(|\sin((u+v)/2)|\) is comparable to \(x+y\) on the regular mesh
by (5). The endpoint perturbations are a small fraction of \(x+y\)
because \(j+r\le2n+1\) is odd and the only zero \(x+y=0\) pair is
in \(B\). Hence

\[
 (-\chi F)_+\le C\rho/t\le Cm\rho/L.
\]

There are \(O(n\rho+1)\) eligible first rows, and each has a harmonic
\(L^{-1}\) sum \(O(\log(n\rho+2))\). Their normalized cost is
\[
 C(\rho^2+\rho/n)\log(n\rho+2)
                  \le C\rho^2\log m+C\rho.               \tag{11}
\]

If \(x>K\rho\), (10), with \(K\) enlarged, gives \(|Y|\le x/2\)
and \(|X|\ge3x/4\). Elementary cosine chords give
\(|\cos X-\cos Y|\ge cx^2\), including \(x\) near \(\pi\).
Also \((-A)_+\le C\rho x\). Each contributing term is at most
\(C\rho/x\), and the number of possible second indices in that row
is \(O(m(\sqrt{\rho x}+\rho)+1)\). Summing first indices,
whose nonzero \(x\)'s have spacing \(\pi/n\), yields

\[
 C\rho^{3/2}+C\rho^2\log(2+1/\rho)
                      +C\rho\log(m)/m\le C\rho.          \tag{12}
\]

For the middle term the harmonic sum starts at
\(x\ge\max(K\rho,\pi/n)\); hence its normalized size is
\(O(1+\log\min(n,1/\rho))\), justifying the bound also when
\(\rho<1/n\). Formulas (11)–(12) hold for every reflection of the
phases. This proves the required sign-change estimate without assuming
a width \(O(\rho)\) in the far rows. The case \(\rho=0\) is exact
normalization and is excluded only from expressions containing \(1/\rho\).

## 5. Finite-sum bound for the removed collision family

For \(r=j+1\) write \(h=n-j\),
\(x=(h\pi-\alpha)/n,y=(h\pi-\beta)/m\),
\(X=(x+y)/2,T=(x-y)/2\). For \(h\le n/3\), set
\(U_k(z)=\sin(kz)/\sin z\), interpreted by its finite Fourier sum.
Then, everywhere including collisions,

\[
 D_n(u,v)=(-1)^n\{U_m(X)U_m(T)-U_n(X)U_n(T)\}
\]
\[
 =(-1)^n\{V_n(X)U_m(T)+U_n(X)V_n(T)\},\quad
 V_n(z)=\frac{\cos((2n+1)z/2)}{\cos(z/2)}.                 \tag{13}
\]

The identity follows by subtracting the two sine quotients; finite sums
extend it to every vanishing sine. The arguments \(X,T\) stay in a
fixed interval where \(\cos(z/2)\) is bounded below. Thus
\(|V_n|\le C,|V_n'|\le Cn\),
\(|U_m(T)|\le m,|U_m'(T)|\le Cm^2\). For \(h\ge1\),
\(|\sin X|\ge ch/n\), giving
\(|U_n(X)|\le Cn/h\) and
\(|U_n'(X)|\le Cn^2(1/h+1/h^2)\).
For \(h=0\), the global finite-sum bounds \(n,Cn^2\) suffice.
Every phase derivative of \(X,T\) is \(O(1/n)\).
Equation (13), and the corrected cosine term, consequently imply

\[
 |F|+|\partial_\alpha F|+|\partial_\beta F|\le Cn.          \tag{14}
\]

There are \(O(n)\) such pairs. Their normalized sum is \(O(1)\)
at zero and \(O(1)\)-Lipschitz in the phases. Its excess over
\(a\) times its reference value is therefore \(C\rho\).
This covers the actual polynomial corner value rather than replacing it
by the formal rational numerator zero. Combining (8), (11)–(14), and
(2) proves (B).

## 6. Consequence, gate and precise remaining obligation

On the small phase neighborhood,
\(1-a\ge c(\alpha^2+\beta^2)\ge c'\rho^2\). PD-T159 gives
\(\Lambda_c\ge(4/\pi^2)\log^2n-54\). For sufficiently large \(n\),
(B) therefore implies
\[
 S_n-\Lambda_c\le-c\rho^2\log^2n+C\rho.
\]
Completing the square gives the stated \(O(\log^{-2}n)\) supremum.
No explicit constant or effective degree threshold is asserted.

Recommendation: **GO to a distinct review/reduction round**, conditional
on independent inspection of the written estimates. New information is
the two-phase algebra, the finite-sum collision estimate (13), and the
square-root sign-change support estimate (10) with discrete costs
(11)–(12). The next discriminating test is to independently verify these
three estimates and the regular Hessian sums; after that combine the
primitive localization with a compact-uniform positive paired defect at
the same phases. A positive lower bound at zero phase alone is insufficient:
the defect estimate must permit both phases tending to zero, arbitrary
moving macroscopic points, and the edge-to-interior strips. A separately
owned paired-defect note is being developed by the orchestrator.

STOP this formulation if a counterexample invalidates (A) or (B) without
a viable stated repair. Neither these estimates nor a positive compact
defect establishes a physical-coordinate corner radius or effectivity.
No later round was executed by this worker.

Checks actually executed: read/search commands, written analytic
reconstruction, and
`python topics/padua-argmax-alln-20261101/code/gated/d1_phase_r01.py > topics/padua-argmax-alln-20261101/outputs/gated/d1_phase_r01_sanity.json`.
Python 3.12.14, NumPy 2.3.5, fixed seed 20261102, degrees 2,3,8,17,31,64:
480 cleared numerator identities had maximum float64 absolute discrepancy
4.12e-13; 135 collision-family factorizations had maximum discrepancy
1.08e-11; six constructed coincident-angle cases retained finite values.
This is **MEASURED** sanity evidence only, not an independent rerun,
uniform bound, exact-arithmetic certificate or proof premise.

Runs needed: independent mathematical review of (5)–(14), including the
sign-change counts and endpoint cases. Source identities, output identity
and byte sizes are recorded in `outputs/gated/d1_phase_r01_sources.json`.

## Round 2 publication note — 2026-11-02

The separate Astra xhigh reconstruction reported no blocking mathematical
finding in claims A/B; see [independent round-1 check](../../gated/checks/d1-r01.md).
The review-pending wording above records the round-1 checkpoint. Claim A is
now preserved separately as [global primitive bound](../../theory/gated-codex-02-two-phase-global-bound.md),
and claim B as [local primitive gain](../../theory/gated-codex-03-two-phase-local-gain.md).
The required Claude audit remains pending. The original statements and
failed proof variants above are retained unchanged. A rendering-only missing
backslash in the displayed decomposition after (1) was corrected.
