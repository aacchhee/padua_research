# PD-T?argmax-alln-gated-codex-02 — Global two-phase primitive bound

ID kind: PD-T.
Aliases: direction1 round1 claim A; two-free-angle PD-T189 extension;
odd-coset logarithmic primitive remainder.
Split from: supporting primitive obligation in PD-T099; the all-square
all-degree target remains OPEN. Historical combined development record:
`gated/d1/r01-phase.md`, claim A.
Split into: none. Local gain is the separate supporting result
PD-T?argmax-alln-gated-codex-03.

Date: 2026-11-02. Codex, parent-assigned gpt-6.1-sol xhigh; runtime
metadata not independently exposed. Rules/snapshot head
`2dde541f1e5af239cae6e93e4438b9be89d15d87`; scientific input
`7d308b10d946b607ae0690454f6c0103690775a4`.

## Statement and definitions

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

There is an absolute constant C such that, for every n>=2 and
every pair of real phases with |alpha|+|beta|<=pi,

\[
 S_n(\alpha,\beta)\le a(\alpha,\beta)\Lambda_c(n)
                                      +C\log(n+1). \tag{A}
\]

## Assumptions

Exact real arithmetic, PD-T185's corrected polynomial kernel and the stated
odd periodic mesh, including its collision values. There is no assumption
on a global maximizer or on a defect limit.

## Status by part

Overall status: **PROVED**, by the complete analytic argument below;
supplementary independent Astra xhigh reconstruction completed.
Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). No effective numerical value of C is claimed.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Uniform global primitive inequality | PROVED | Polynomial diagonal strip and far-mesh estimates below |

Candidate disposition: retained implementation variant, no novelty claim.

## Depends on

PD-T185 for the polynomial divided difference and corrected kernel;
PD-T189 for exact zero-phase corner normalization. Elementary sine chord,
harmonic and reciprocal-square estimates are proved or explained below.

## Checks

The written round-1 proof was independently reconstructed by a distinct
Astra xhigh checker with no blocking mathematical finding; see
[independent check](../gated/checks/d1-r01.md). This supplementary check does not replace Claude audit-01, which ACCEPTED the mathematics at its stated scope (record fixes pending). A small float64
algebra/collision sanity run is recorded in
[round 1](../gated/d1/r01-phase.md) and
[its receipt](../outputs/gated/d1_phase_r01_sanity.json); it is MEASURED,
has no proof role, and is not an exact-arithmetic certificate.
Source identities for the original proof and inputs are in
[round-1 source receipt](../outputs/gated/d1_phase_r01_sources.json).
This publication preserves the checked analytic proof rather than adding
a new numerical premise.

## Sources and candidate gate

Variant of IDEA-305, original Claude-02, fallback-04. The full registry
headings/aliases/summaries and obstruction/disposition gate and retained
failed variants are recorded in [round 1](../gated/d1/r01-phase.md).
No external source transfer or priority claim.

## Proof

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

## Scope and open items

This proves only a primitive leading-phase bound. It gives phase convergence
for near-corner-value competitors after an appropriate lower comparison,
but supplies neither the vanishing local excess nor a positive physical
defect. The local gain is recorded separately. No explicit constant, usable
degree threshold, corner neighborhood or all-degree argmax is asserted.
PD-T099 remains OPEN.

## History

The initial entry below records the publication checkpoint; its pending-review wording is superseded by the dated correction that follows.

2026-11-02: split claim A from the round-1 development record without
changing its statement or proof. The proof retains polynomial collisions;
the rendering-only missing backslash after (1) was fixed before splitting.
Round-1 independent reconstruction completed; required Claude audit remains
pending. No final ID or shared-registry edit is made here.


### Documentation correction — 2026-11-02

F5 provenance impact: the frozen [d1-r02 check](../gated/checks/d1-r02.md) pinned `d57b8d07709013a246259aa3095af340e2e2b2c5d60c44d7f332cf9b44f59dc9`, while the audited committed file before this correction was `39c2f217f1ce1ca618033f0ac32852ad47933817a240911d085764cf1e3b17b7`. Claude audit-01 sub-audit B compared that committed proof with r01-phase §§1–2 (identical) and reconstructed the committed result, resolving mathematical impact. This is an attributed audit conclusion, not a new developer rerun. The frozen receipt stays unchanged; this correction and current review wording account for the new file hash.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Claude audit PENDING
> Claude audit, which remains PENDING
