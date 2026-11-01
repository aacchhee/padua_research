# PD-T023 — an explicit fixed-ratio CC lower bound

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T. Aliases: oversampled Fejér reconstruction; filtered weighted Schur bound.
Split from: M3 fixed-ratio two-sided target. Split into: none.

## Statement

Put
\[
C_0=2(1+\pi)^2,\qquad C_*=3C_0^2(1+2/\pi)
=12(1+\pi)^4(1+2/\pi).
\]
For all integers \(N\ge2\), \(0\le n<N\), and all real \(p\in\Pi_n\),
\[
\int_{-1}^1p(x)^2\,dx\le\frac{C_*}{(1-n/N)^2}Q_N(p^2).\tag{1}
\]
In particular, \(\lambda_{\min}(Q_N|_{\Pi_n})\ge(1-n/N)^2/C_*\), uniformly positive whenever \(n/N\le\theta<1\).

## Definitions and assumptions

The rule is Lebesgue CC on \(x_j=\cos(j\pi/N)\). On the circle \(\mathbb R/(2\pi\mathbb Z)\), \(d(t,s)\in[0,\pi]\) is the shorter angular distance, \(t_j=j\pi/N\), \(j=0,\ldots,2N-1\), and
\[
q(t)=p(\cos t),\quad \nu(t)=|\sin t|+1/N,\quad \epsilon=1-n/N.
\]
Circle integration uses ordinary \(dt\) on \([0,2\pi)\), without normalization. Nodal sums use counting measure unless their factor \(1/(2N)\) is written.

## Status and dependencies

Overall status: **PROVED** in development; pinned independent audit and prior-art screen pending. The constants are deliberately loose.

Depends on: PD-T017, section1, only its elementary CC-weight bounds: \(w_j\ge\sin(t_j)/N\) at interior half-circle nodes; \(w_0=w_N\ge N^{-2}\). That proof is local and explicitly reconstructs the Fourier series and weights. It has its own pending audit. No external classical MZ theorem or private result is assumed. All remaining ingredients are proved below.

## Proof

### 1. Exact filtered reconstruction

For integer \(m\ge1\), define the Fejér kernel by its finite polynomial
\[
F_m(t)=\sum_{|k|<m}(1-|k|/m)e^{ikt}
=\frac1m\left|\sum_{h=0}^{m-1}e^{iht}\right|^2.
\]
The equality follows by counting pairs with difference \(k\). Away from multiples of \(2\pi\), the finite geometric sum gives \(F_m(t)=\sin^2(mt/2)/(m\sin^2(t/2))\); its value at zero is \(m\). Define
\[
K(t)=\frac{NF_N(t)-nF_n(t)}{N-n},\tag{2}
\]
where \(nF_n\) is defined as zero at \(n=0\). Its Fourier coefficient at \(k\) is
\([\max(N-|k|,0)-\max(n-|k|,0)]/(N-n)\). Hence \(K\) has degree \(N-1\) and coefficient exactly one for every \(|k|\le n\), including \(|k|=n\).

For any trigonometric polynomial \(q\) of degree at most \(n\),
\[
q(t)=\frac1{2N}\sum_{j=0}^{2N-1}K(t-t_j)q(t_j).\tag{3}
\]
Indeed, expand both finite Fourier sums. The grid average of \(e^{i(l-k)t_j}\) is one when \(l=k\) and zero otherwise: \(|l-k|\le n+N-1<2N\) excludes every nonzero multiple of \(2N\). The remaining multiplier is the Fourier coefficient one. This proves (3) also at \(n=0\).

### 2. Kernel decay and the weighted operator

For \(d=d(t,0)>0\), \(\sin(d/2)\ge d/\pi\); this follows from concavity of sine on \([0,\pi/2]\). The geometric-sum formulas give
\[
mF_m(t)\le m^2,\qquad mF_m(t)\le\pi^2/d^2.
\]
Thus the triangle inequality in (2) gives
\[
|K(t)|\le\frac{2N}{\epsilon}\min\{1,\pi^2/(Nd)^2\}
\le\frac{C_0N}{\epsilon(1+Nd)^2}.\tag{4}
\]
The last scalar inequality follows by splitting \(Nd\le\pi\) and \(Nd\ge\pi\), and holds at \(d=0\) by continuity.

The function \(\nu\) is one-Lipschitz for circle distance and is at least \(1/N\). Consequently
\(\nu(t)/\nu(t_j)\le1+Nd(t,t_j)\). On setting \(z_j=\sqrt{\nu(t_j)}q(t_j)\), equation (3) becomes
\[
\sqrt{\nu(t)}q(t)=\sum_j H(t,j)z_j,\qquad
H(t,j)=\frac1{2N}K(t-t_j)\sqrt{\nu(t)/\nu(t_j)}.
\]
By (4),
\[
|H(t,j)|\le\frac{C_0}{2\epsilon}(1+Nd(t,t_j))^{-3/2}.\tag{5}
\]

For a fixed \(t\), each half-open distance shell \([k\pi,(k+1)\pi)\) in the scaled distance \(Nd\) contains at most two grid points: at most one in each direction on the circle, since each corresponding arc has length \(\pi/N\), the grid spacing. Thus
\[
\sup_t\sum_j|H(t,j)|
\le\frac{C_0}{\epsilon}\sum_{k\ge0}(1+k\pi)^{-3/2}
\le\frac{C_0}{\epsilon}(1+2/\pi)=:R.\tag{6}
\]
The integral comparison uses the decreasing summand and \(\int_0^\infty(1+\pi u)^{-3/2}du=2/\pi\). At the antipodal point a shell can only lose points; endpoints are included using half-open arcs. For a fixed node, symmetry in the two circle directions gives
\[
\sup_j\int_0^{2\pi}|H(t,j)|\,dt
\le\frac{C_0}{2\epsilon}\frac2N\int_0^\infty(1+u)^{-3/2}du
=\frac{2C_0}{\epsilon N}=:S.\tag{7}
\]

For completeness the needed Schur inequality follows from Cauchy–Schwarz:
\[
\left|\sum_jH(t,j)z_j\right|^2
\le\left(\sum_j|H(t,j)|\right)\sum_j|H(t,j)||z_j|^2.
\]
Integrate and apply (6)–(7), obtaining
\[
\int_0^{2\pi}\nu(t)|q(t)|^2dt
\le\frac{2C_0^2(1+2/\pi)}{\epsilon^2N}
\sum_{j=0}^{2N-1}\nu(t_j)|q(t_j)|^2.\tag{8}
\]

### 3. Return to the Lebesgue CC norm

At an interior half-circle node, \(\sin t_j\ge2/N\), by the concavity lower bound for sine and symmetry. Thus \(\nu(t_j)\le(3/2)\sin t_j\). The cited local weight bounds imply, at every half-circle node including endpoints,
\[
w_j\ge\frac2{3N}\nu(t_j).\tag{9}
\]
Since \(q\) and \(\nu\) are invariant under \(t\mapsto2\pi-t\),
\[
\sum_{j=0}^{2N-1}\nu(t_j)q(t_j)^2
\le2\sum_{j=0}^N\nu(t_j)p(x_j)^2\le3NQ_N(p^2).\tag{10}
\]
The first inequality deliberately overcounts the two endpoints. Finally,
\[
2\int_{-1}^1p^2=\int_0^{2\pi}|\sin t|q(t)^2dt
\le\int_0^{2\pi}\nu(t)q(t)^2dt.
\]
Combine this with (8) and (10) to obtain (1).

## Checks, sources and scope

The first kill tests are exact Fourier-plateau/no-alias checks for all \(0\le n<N\) in the finite executed range, not samples at a single ratio. See `tracks/mz-constants/code/m3_exact_check.py` and `topics/mz-constants/directions/M3/RUNS.md`. Optional spectra are MEASURED; the all-N statement follows analytically from the finite formulas and Schur estimates.

The orchestrator proposed the filtered-convolution route and the present developer reconstructed its full proof/constants. Classical de la Vallée Poussin/Fejér reconstruction and weighted MZ theory are potential prior art; their historical coverage is explicitly unresolved in the literature record. No priority claim is made.

This bound is useful at a fixed ratio. At \(n=N-1\) it degenerates as \(N^{-2}\), and is not the endpoint logarithmic result. It is split from the endpoint direction rather than replacing its sharper lower theorem. Independent pinned reconstruction remains pending.

## History

2026-10-31, Codex gpt-6.1-sol xhigh, rules `d36722823441dc40c6e19d69a174459348dd309c`: first M3 lower mechanism after M1 completion; exact normalized circle proof written before numerical confirmation.
