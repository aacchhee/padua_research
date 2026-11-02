# PD-T?argmax-alln-gated-codex-03 — Vanishing two-phase primitive gain

ID kind: PD-T.
Aliases: direction1 round1 claim B; two-free-angle PD-T190 extension;
square-root numerator sign-change estimate; local odd-coset primitive gain.
Split from: supporting primitive obligation in PD-T099; the all-square
all-degree target remains OPEN. Historical combined development record:
`gated/d1/r01-phase.md`, claim B.
Split into: none. Global localization is the separate supporting result
PD-T?argmax-alln-gated-codex-02.

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

There are absolute constants rho0>0 and C, with rho0 sufficiently
small and at most pi/48, such that for every n>=2 and every pair of real
phases with rho=|alpha|+|beta|<=rho0,

\[
 S_n(\alpha,\beta)\le a(\alpha,\beta)\Lambda_c(n)
                       +C\rho^2\log(n+1)+C\rho. \tag{B}
\]

Consequently

\[
 0\le\sup_{|\alpha|+|\beta|\le\rho_0}
       (S_n(\alpha,\beta)-\Lambda_c(n))=O(\log^{-2}n).
\]

In particular S_n(alpha_n,beta_n)<=Lambda_c(n)+o(1) whenever both
phases tend to zero. All polynomial collisions, exact zeros and absolute
value cusps are included.

## Assumptions

Exact real arithmetic and the corrected polynomial kernel convention
above. There is no differentiability assumption on the absolute values
at a zero term, no pole avoidance assumption, and no defect hypothesis.

## Status by part

Overall status: **PROVED**, by the analytic argument below; supplementary
independent Astra xhigh reconstruction completed. Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). The constants and threshold are non-effective in this record.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Uniform local primitive bound and vanishing supremum | PROVED | Signed Taylor terms, retained numerator signs, finite collision family and optimization |

Candidate disposition: retained implementation variant. The discarded
O(rho)-width sign-change proof step is retained in the round-1 record.

## Depends on

PD-T185 for the corrected polynomial kernel; PD-T189 for normalization;
PD-T156 (1), also PD-T157 (1), for Lambda_c >= (4/pi^2)log^2(n)-54. The exact algebra and reflection
normalization are reproduced below, as also used in the separate global
primitive record. The local argument does not assume the global inequality.

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

### 1. Verify the numerator before estimating

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

### 2. Local regular set and signed Taylor estimate

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

### 3. Numerator sign changes: the new two-phase issue

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

### 4. Finite-sum bound for the removed collision family

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

## Consequence

On the small phase neighborhood,
\(1-a\ge c(\alpha^2+\beta^2)\ge c'\rho^2\). PD-T156 (1), also PD-T157 (1), gives
\(\Lambda_c\ge(4/\pi^2)\log^2n-54\). For sufficiently large \(n\),
(B) therefore implies
\[
 S_n-\Lambda_c\le-c\rho^2\log^2n+C\rho.
\]
Completing the square gives the stated \(O(\log^{-2}n)\) supremum.
No explicit constant or effective degree threshold is asserted.

## Scope and open items

The theorem bounds the primitive's local excess. It does not assert that
zero is an exact primitive maximizer, a positive physical defect, an
effective constant or degree threshold, or a physical corner radius.
PD-T099 remains OPEN. The sharper quantitative error diagnosis in
[round 2](../gated/d1/r02-effectivity.md) is separate from this theorem's
statement and proof.

## History

The initial entry below records the publication checkpoint; its pending-review wording is superseded by the dated correction that follows.

2026-11-02: split claim B and its optimized consequence from the round-1
development record without changing either statement. The complete
regular-set, numerator-sign and finite-sum collision arguments are retained.
Supplementary Astra xhigh reconstruction completed; required Claude audit
remains pending. No final ID or shared-registry edit is made here.


### Documentation correction — 2026-11-02

F2: the original direct citations were “PD-T159 for Lambda_c >= (4/pi^2)log^2(n)-54” and “PD-T159 gives”. The explicit logarithmic lower bound is PD-T156 (1) / PD-T157 (1); PD-T159 supplies the separate corner-product comparison. Only citations changed. N6: the original proof subsection headings were numbered 1, 3, 4, 5 at level 2; they are now consecutive 1–4 subsections under Proof. Equation numbers and proof text are unchanged.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Required Claude audit
> PENDING
> Claude audit, which remains PENDING
