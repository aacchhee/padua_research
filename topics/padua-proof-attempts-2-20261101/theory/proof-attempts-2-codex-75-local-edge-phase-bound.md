# PD-T?proof-attempts-2-codex-75 — Vanishing gain of the primitive at small phase

ID kind: PD-T.
Aliases: A4(a) local even phase profile; paired Taylor bound with exact cusps.
Split from: central-envelope comparison after74's phase localization.
Split into: triangle-defect stability76 and the combined envelope conclusion are separate.

## Statement

For S_n(s) defined in74, there is an absolute C such that for every n>=2 and |s|<=pi/6,

\[
 S_n(s)\le\cos^2(s/2)\Lambda_c(n)
             +Cs^2\log(n+1)+C|s|.                          \tag{1}
\]

Consequently

\[
 0\le\sup_{|s|\le\pi/6}\{S_n(s)-\Lambda_c(n)\}
       =O(\log^{-2}n),                                    \tag{2}
\]

and in particular S_n(s_n)<=Lambda_c(n)+o(1) for every sequence s_n->0. Every exact zero-cardinal cusp and removable kernel value is retained in these inequalities.

## Assumptions and status

The exact periodic odd checkerboard, polynomial kernel and corrected mode are those of70/74. Overall status: **PROVED**, by the analytic estimates below; required Claude audit PENDING. No numerical calculation is a premise. The result concerns the primitive S_n, not a global maximum over the square.

## Depends on and independent contribution

70/74's exact phase expression, the elementary finite U_n Fourier sum and A2's corner lower bound. The indirect A1 dependency retains **PD-T?proof-attempts-codex-01 (audit pending)** with70's dated accepted/merged qualification.

The full local module was derived by `/root/a2_independent_route` in independent-checks-a4.md and independently rederived/read in full by the lead and `/root/a5_checker`. The proof below records that substantive contribution in a durable result, rather than treating the receipt alone as an unproved assumption. This is supplementary independent mathematics, not the required Claude audit.

## Proof

Put m=n+1,N=nm,u=j*pi/n,A=cos u,v_0=r*pi/m,v=v_0+s/m. Set a(s)=cos^2(s/2), b(s)=sin s/2. The exact expression from74 is

\[
 F_{jr}(s)=a(s)f(A,v)+b(s)g(A,v)
 =\frac{2\cos(s/2)\cos(v/2)\cos((v-s)/2)}{A-\cos v},       \tag{3}
\]

where f=(1+cos v)/(A−cos v), g=sin v/(A−cos v), with the polynomial D_n definition at coincidences. Folding the periodic first mesh gives j=0,…,n with half endpoint weights epsilon_j. The interior second rows pair F_jr(s) with F_jr(−s); the rows r=0,m occur singly. Thus, exactly,

\[
 S_n(s)=\frac2N\sum_j\epsilon_j
 \left\{\text{endpoint rows}+
 \sum_{\substack{1\le r<m\\j+r\;\mathrm{odd}}}
          (|F_{jr}(s)|+|F_{jr}(-s)|)\right\}.               \tag{4}
\]

### 1. Regular indices and derivative sums

Remove from the interior rows the family B={r=j+1,j>=2n/3}. On every remaining pair define L=|j−r|>=1 and d=min(j+r,2n+1−j−r)>=1. For |s|<=pi/6 put P=(u+v)/2,T=(u−v)/2, alpha=sin P,t=|sin T|. There is an absolute c_0>0 such that

`t>=c_0 L/m`, `alpha>=c_0 d/m`.                           (5)

Indeed if j>r, u−v_0>=pi L/m; if r−j>=3, v_0−u>=pi(L−1)/m. The only remaining odd difference is r=j+1; outside B, j<2n/3 and v_0−u>pi/(3m). Subtracting |s|/m<=pi/(6m) retains the stated gap. The distances of P from0 andpi are at least pi*d/(2m)−pi/(12m). Sine concavity proves(5). In particular each regular denominator keeps its sign throughout the phase window.

For each fixed signed odd difference j−r, the possible d values have multiplicity at most2. Hence their reciprocal sums are O(log m), their reciprocal p-th-power sums are O_p(1) for p>1, and there are O(m) pairs for that difference. Reciprocals of L obey the same harmonic comparisons.

Direct differentiation gives the pointwise bounds

\[
\begin{split}
 |f_v|&\le\alpha^{-1}t^{-2},\\
 |f_{vv}|&\le\tfrac12\alpha^{-2}t^{-2}+2\alpha^{-1}t^{-3},\\
 |g|&\le t^{-1},\qquad
 |g_v|\le(t^{-2}+\alpha^{-2})/4,\qquad
 |g_{vv}|\le(t^{-3}+\alpha^{-3})/4.                         \tag{6}
\end{split}
\]

Here f_v=−(1+A)sin v/(A−cos v)^2, and g_v=−(csc^2 T+csc^2 P)/4; sin v<=2sin P bounds f's derivatives. Combining(5)–(6) and the difference/d counts, with sums normalized by1/N and termwise suprema over the phase window, gives

\[
\begin{array}{ll}
 \sum |f_v|/m=O(\log m),&\sum |f_{vv}|/m^2=O(\log m),\\
 \sum |g|=O(\log m),&\sum |g_v|/m=O(1),\quad
                      \sum |g_{vv}|/m^2=O(1).               \tag{7}
\end{array}
\]

For example alpha^(-1)t^(-3) sums to O(m^4 log m), and alpha^(-2)t^(-2) to O(m^4), which become the f_vv estimates after division by Nm^2. The separate t^(-3),alpha^(-3) sums are O(m^4), giving the final bound.

Put E_jr(s)=F_jr(s)−a(s)f(A,v_0). Its second derivative is

`a''(f(v)−f(v_0))+2a'f_v/m+a f_vv/m^2+b''g+2b'g_v/m+b g_vv/m^2`.

The first difference is bounded by |s|/m times the corresponding supremum of |f_v|. All phase factors and their derivatives are uniformly bounded, so(7) bounds the normalized sum of sup|E''| by C log m. Since E(0)=0, symmetric Taylor's integral formula proves

\[
 \frac1N\sum_{\rm regular}|E_{jr}(s)+E_{jr}(-s)|
       \le Cs^2\log m.                                   \tag{8}
\]

### 2. Keep the numerator sign-change contribution

On a regular pair let chi=sign f(A,v_0). Its denominator has fixed sign and f(A,v_0)!=0. The exact identity |F|=chi F+2(−chi F)_+ separates the signed pairing(8) from its sign-change error. Formula(3), with v in(0,pi), shows that a numerator can become negative only when v−s>pi. Put sigma=|s|. Such rows have pi−v_0<=sigma, and in a changing term y=pi−v lies in(0,sigma). Its numerator has magnitude at most C sigma*y. If x=pi−u, then sin P=sin((x+y)/2) and y/sin P is uniformly bounded: use a sine chord when x+y<=pi, and a fixed positive lower bound when pi<=x+y<=7pi/6. Therefore the changing term costs at most C sigma/t<=Cm sigma/L.

There are O(m sigma+1) eligible r rows. In each one, summing L^(-1) over j gives O(log m). The normalized error is consequently

`Cs^2 log m+C|s| log m/m <= Cs^2 log m+C|s|`.              (9)

Zero numerator events are included. In particular no differentiability at an exact zero cardinal is assumed.

### 3. The removed family, including every removable collision

For B write h=n−j, so1<=h<=n/3, and put x=h*pi/n,y=(h*pi−s)/m. The exact factorization is

\[
 F_{jr}(s)=\cos(s/2)R_h(s)U_n(T),\qquad
 R_h(s)=\frac{\sin(y/2)}{\sin((x+y)/2)}.                     \tag{10}
\]

It follows from cos((v−s)/2)=−sin(nT) in(3), and remains valid at T=0 by the finite Fourier expression U_n(T)=sum_(l=−n+1,step2)^(n−1)exp(ilT). In the fixed phase window x,y are positive and bounded away from the opposite endpoint. Sine chords give |R_h|<=C and |R_h'|<=C/h. The finite sum gives |U_n|<=n and, since T'=−1/(2m), |d_s U_n(T)|<=n^2/(2m)<=n/2. Thus each term in B is Cn-Lipschitz, including its collisions. There are O(n) pairs and the normalized entire B sum is O(1)-Lipschitz in s and O(1) at0. Its excess over a(s) times its zero-phase value is at most C|s|.

### 4. Single endpoint rows

For r=0 the allowed j are odd and j>=1. Here |v|=|s|/m<=u/6. The denominator has fixed sign, the numerator in(3) is positive, and F_j0(s)−a(s)F_j0(0) is even and vanishes at0. Direct differentiation using |cos u−cos(s/m)|>=c(j/m)^2 gives a second-derivative bound C(m^2/j^4+m/j^2); after normalized summation this is O(1). Its contribution is therefore Cs^2.

For r=m the allowed h=n−j are even. If h>=2 the numerator is a(s)(1−cos(s/m))−b(s)sin(s/m), of magnitude at most Cs^2/m. The denominator is at least c(h/n)^2, so |F_jm(s)|<=Cn s^2/h^2; its zero-phase value is0. The normalized cost is O(s^2/n). At h=0 the original finite expression is

`H_(n,m)(s)=cos(s/2)U_n(s/(2m))`, `H_(n,m)(0)=n`.

The finite Fourier sum and |cos z−1|<=z^2/2 imply |U_n(s/(2m))−n|<=Cn s^2. Its excess over a(s)n is again Cn s^2, hence normalized O(s^2/n). This preserves the true endpoint value n, rather than the formal zero convention used only in71's translated-grid bookkeeping.

### 5. Combine and optimize

Insert(8)–(10), the sign-change error and endpoint bounds into the exact pairing(4). This proves(1). Since S_n(0)=Lambda_c, the supremum in(2) is nonnegative. A2 gives Lambda_c>=(4/pi^2)log^2n−54, while1−a(s)=sin^2(s/2)>=s^2/pi^2. For all sufficiently large n, absorb the smaller quadratic logarithmic error to obtain

`S_n(s)−Lambda_c(n) <= −c s^2 log^2n+C|s|`,

with absolute c>0. Completing the square bounds the right side by C^2/[4c log^2n], proving(2) and the asserted all-sequence consequence. ∎

## Checks, limitations and open items

The module was independently reconstructed analytically as recorded above, and the complete durable proof was fully read by root and both analytic workers with no blocking finding; all removable and sign-change families are retained. No script or phase fit was executed or needed. Required Claude audit remains PENDING. A phase bounded away from0 is outside this local estimate;74 supplies its separate exclusion. Triangle-defect stability76 and the combined central envelope77 are now complete separate results. Full-square neighbourhood/global claims A4(b)/(c) are not asserted.

## History

2026-11-01, Codex gpt-6.1-sol xhigh, within the15:24–18:24UTC box. Primary local derivation by `/root/a2_independent_route`, supplemented by full lead and central-worker reconstruction. The result is retained separately from the final envelope target.
