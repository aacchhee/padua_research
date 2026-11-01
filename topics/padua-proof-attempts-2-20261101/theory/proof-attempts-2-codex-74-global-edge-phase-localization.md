# PD-T?proof-attempts-2-codex-74 — Uniform leading phase bound and central phase localization

Final ID: **PD-T189**. Provisional ID `PD-T?proof-attempts-2-codex-74` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T099 (finite global or exact edge/central-scope split; full-square all-n statement remains OPEN).

ID kind: PD-T.
Aliases: A4(a) primitive phase; shifted odd-checkerboard bound; central maximizing phase tends to zero.
Split from: the remaining central-envelope comparison after70–73.
Split into: local phase gain and defect stability are separate supporting results; the final envelope conclusion uses both.

## Statement

Put m=n+1,N=nm and let

`Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd}`.

For every real s define, using70's polynomial D_n,

\[
 H_{jr}(s)=\frac{(-1)^jD_n(j\pi/n,r\pi/m+s/m)-1}{2},
 \qquad S_n(s)=\frac1N\sum_{\Gamma^-}|H_{jr}(s)|.              \tag{1}
\]

Then S_n is even, S_n(0)=Lambda_c(n), and there is an absolute constant C, independent of n>=2 and s in[−pi,pi], such that

\[
 S_n(s)\le\cos^2(s/2)\Lambda_c(n)+C\log(n+1).               \tag{2}
\]

Consequently, let R_cen(n) be the exact central vertical-edge envelope defined in T-A4a.md. At a point attaining it, choose a nearest complementary phase beta_n=q_n*pi/m on the same edge and write its angle as beta_n+s_n/m, |s_n|<=pi. Then

`s_n=O((log n)^(-1/2))`, in particular s_n->0.              (3)

This localizes only the phase within the specified central-edge envelope. It does not prove a global corner argmax or identify the historical searched runner-up.

## Assumptions and definitions

All node, corrected-mode and endpoint conventions are those of70. The nearest complementary phase satisfies epsilon^n(−1)^q_n=−1; for all sufficiently large n it lies strictly between0 andpi and beta_n->pi/2. O-constants below are uniform in s and n, except where an explicitly fixed diagonal-strip width L appears.

## Status

Overall status: **PROVED** (written uniform analytic bound and localization below; required Claude audit PENDING). This proof uses no mathematical computation. Root and both separate analytic workers have fully read/reconstructed it with no blocking finding, as recorded in independent-checks-a4.md and independent-checks-a4-central.md; no numerical evidence substitutes for the estimates.

## Depends on

70's polynomial divided difference,72's central grid values and A2's corner leading lower bound. The exact decomposition into S_n minus a nonnegative triangle defect is also derived below. The indirect literal dependency **PD-T?proof-attempts-codex-01 (audit pending)** has70's dated accepted/merged qualification. No constant-term conjecture or fitted gap is used.

## Proof

### 1. Exact phase algebra and its normalization

At u=j*pi/n,v=r*pi/m+s/m with j+r odd, the polynomial P_n=T_(n+1)+T_n has

`P_n(cos u)=(−1)^j(1+cos u)`,

`P_n(cos v)=−(−1)^j[cos s(1+cos v)+sin s sin v]`.

Insert these in the divided difference70. Away from equal cosines,

\[
 H_{jr}(s)=a(s)E(u,v)+b(s)G(u,v),\quad
 a(s)=\cos^2(s/2),\quad b(s)=\tfrac12\sin s,                 \tag{4}
\]

where E(u,v)=(1+cos v)/(cos u−cos v), G(u,v)=sin v/(cos u−cos v). At equal cosines(1), rather than separate limits of E and G, is the definition.

Reflection r->−r modulo2m preserves parity and sends(s,v) to(−s,−v), while D_n is even in its second argument. Thus S_n is even. Periodic reflection of both node meshes converts the endpoint-half-weight sums into the uniform periodic sum. The odd-board corner formula from A1 then gives S_n(0)=Lambda_c exactly, including the corner's singular term.

For any complementary beta=q*pi/m and chosen edge epsilon, reflect the first index about that endpoint and translate the second periodic index byq. The all-edge average70 shows exactly

\[
 \lambda_n(\epsilon,\cos(\beta+s/m))=S_n(s)-\Delta_n(\beta,s),
 \qquad\Delta_n(\beta,s)\ge0,                              \tag{5}
\]

where Delta is the weighted triangle defect of the two half-kernel terms. The equality follows termwise from |X+Y|=|X|+|Y|−defect; reflecting the physical half mesh gives the normalization1/N in(1). All terms retain the polynomial D_n at coincidences. Only nonnegativity of Delta is needed in this result.

### 2. Uniform elementary mesh estimates

By evenness take0<=s<=pi and h=s/m<=pi/m. Fold the first periodic mesh to u_j=j*pi/n in[0,pi], with endpoint half weights. For each interior second index1<=r<=m−1 put v_r=r*pi/m. Reflection of its two periodic copies gives two free angles V=v_r±h in[0,pi], with H of the form aE(u,V)±bG(u,V). The endpoint second rows r=0,m are considered separately below. The first-coordinate prefactor is2/N.

Fix L=8 and call a pair near-diagonal when |u_j−v_r|<=L*pi/n. The number of r indices for each j is bounded by a constant depending only on L. On a near pair, |u_j−V|<=(L+1)*pi/n. The divided difference of P_n over the cosine interval is bounded by its maximum derivative there. The exact Chebyshev identities give

`|T_l'(cos t)|<=min(l^2,l/|sin t|)`.

If sin u_j>=2(L+1)*pi/n, every intervening t has sin t>=sin u_j/2; hence the derivative is O_L(n/sin u_j). Otherwise the global derivative O(n^2) is O_L(n/(sin u_j+1/n)). Thus in both cases

\[
 |H(u_j,V)|\le C_L\frac n{\sin u_j+1/n}.                   \tag{6}
\]

The same applies to the zero-phase value E(u_j,v_r), interpreted by the polynomial kernel at its one exceptional endpoint. Since sin u_j>=2min(j,n−j)/n, summing(6) over j yields O_L(n^2 log(n+1)). There are O_L(1) near-diagonal rows perj. After normalization their contribution, and the corresponding reference contribution, is O_L(log(n+1)). No separate rational pole limit is used here.

On the complementary far set |u−v|>L*pi/n, define Sigma=(u+v)/2, d=(u−v)/2. For u,v in[0,pi], the distance of Sigma from either0 orpi is at least|d|. Sine concavity consequently gives sin Sigma>=|u−v|/pi and |sin d|>=|u−v|/pi. Changing v to V=v±h changes both half angles by at mosth/2. Since L=8, both sine factors stay within fixed positive factors of their old values. In particular

`|cos u−cos V| >= c |cos u−cos v|`                         (7)

with an absolute c>0. The following discrete sums, uniform in v on the far set, follow from sine concavity and comparison with the harmonic and reciprocal-square sums on a mesh of spacing pi/n:

\[
 \sum_j|\sin d|^{-1}=O(n\log(n+1)),\qquad
 \sum_j\sin^{-2}d=O(n^2).                                 \tag{8}
\]

Only indices separated by at leastL*pi/n occur, so no small fractional distance from an arbitrary v is omitted in these bounds.

### 3. The far-set error is only logarithmic

Exact subtraction gives

\[
 |E(u,V)-E(u,v)|
 =\frac{(1+\cos u)|\cos V-\cos v|}
        {|\cos u-\cos V|\,|\cos u-\cos v|}.                 \tag{9}
\]

Taylor's elementary remainder bound gives |cos V−cos v|<=h sin v+h^2/2. Also

`sin Sigma>=cos(u/2)sin(v/2)`,

so(1+cos u)/sin^2 Sigma<=2/sin^2(v/2). Using(7)–(9), and then(8), bounds the normalized sum of(9) by a constant times

\[
 \frac1{nm}\left\{
 h n^2\sum_{r=1}^{m-1}\cot\frac{v_r}2
 +h^2n^2\sum_{r=1}^{m-1}\csc^2\frac{v_r}2\right\}
 =O(\log(n+1)).                                           \tag{10}
\]

Indeed cot(v_r/2)<=2m/(pi*r), csc(v_r/2)<=m/r, h<=pi/m, and the two sums are respectively O(m log(m+1)) and O(m^2).

For the sine channel, |sin V|<=sin v+h. The inequalities sin v<=2sin Sigma and sin Sigma>=|sin d| give, on the far set,

\[
 |G(u,V)|\le C\{|\sin d|^{-1}+h\sin^{-2}d\}.
\]

Its normalized double sum is O(log(n+1)) by(8). Since0<=a<=1 and |b|<=1/2, the triangle inequality in(4), followed by(9)–(10), gives the far-set bound a times the zero-phase absolute sum plus O(log(n+1)).

Finally, the second-coordinate endpoint rows r=0,m contribute O(1). Within O(1/n) of their matching first-coordinate endpoint this follows from the global divided-difference bound O(n^2), with only O(1) indices. Away from that small neighborhood, |cos u−cos V| is bounded below by a constant times the squared angular distance to that endpoint, while the numerator in(4) is bounded. The sum of reciprocal squared endpoint distances is O(n^2), which becomes O(1) after the1/N normalization. The same bound holds for their zero-phase reference rows. Combining near, far and endpoint pieces proves(2).

### 4. Localization of the central maximizing phase

Continuity on the compact definition of R_cen gives a maximizer. A nearest complementary ordinate has phase distance at mostpi/m, so |s_n|<=pi and beta_n->pi/2. The concrete grid sequence in72 lies in the same central cell for all n; hence

`R_cen(n)>=C_n=Lambda_c(n)−g+o(1)`.

Use(5), Delta>=0 and(2) at the maximizing point. Thus

`sin^2(s_n/2) Lambda_c(n) <= C log(n+1)+g+o(1)`.

A2 gives Lambda_c(n)>=(4/pi^2)log^2 n−54. Consequently sin^2(s_n/2)=O(1/log n). For |s_n|<=pi, the sine chord inequality gives |s_n|<=pi|sin(s_n/2)|, proving(3). ∎

## Checks, scope and open items

No mathematical script, numerical phase fit or computational derivative estimate has been executed for this proof. Supplementary independent analytic reconstruction is complete. The bound supplies phase convergence; the separate local gain75 and stable defect76 now complete the central-envelope application77. Neither the local bound nor a global square assertion is silently included in this theorem. Full A4(b)/(c) remain outside the claim; required Claude audit is PENDING.

## History

2026-11-01, Codex gpt-6.1-sol xhigh, within the15:24–18:24UTC box. Fixed-width diagonal strips isolate every rational-pole coincidence, retaining the polynomial definition throughout. All earlier A5 source files remain frozen.
