# PD-T?padua-3d-20261106-codex-T10-04 — a uniform log-four parity-grid projection bound

ID kind: PD-T. Aliases: anisotropic Haar Gram; Fejer sampling; elementary polylog bound. Split from:none. Split into:none.

Task provenance: handoff06 T10.4. This is a supporting result for the log³ projection target, not a proved conjunct or case of that target.

## Statement and definitions

For every n>=1, take orders m=(n,n+1,n+1) and dual lattice

`L={ (m1 a1,m2 a2,m3 a3): a in Z³, a1+a2+a3 even }`.

Let H=L-perp, X=cos(2πH), and w the positive folded Haar weights. Let φ_α(x)=2^{s(α)/2} product_j T_{αj}(xj), |α|<=n, where s counts nonzero coordinates; these are orthonormal for product Chebyshev probability measure. Define raw hyperinterpolation Hn f=sum_α φ_α sum_X wφ_αf and weighted least-squares projection Pn onto Π_n. Then the exact Gram matrix is `G=I+e e^T`, where e indexes α=(n,0,0); Pn exists and `||Pn−Hn||∞ <=1`. There is an absolute constant C such that

`||Hn||∞ <= C log(n+2)^4`, and `||Pn||∞ <= C log(n+2)^4+1`.

For equal orders(n+1,n+1,n+1), the same bound holds and Hn=Pn. Overall status:**PROVED**. No novelty claim: positive cubature/hyperinterpolation and these parity families are established. The weaker logarithmic exponent here is an elementary self-contained result; log³ remains OPEN in a separate target.

## Gram calculation

H is the union of two rectangular torus grids: h_j=r_j/m_j and h_j=(r_j+1/2)/m_j, 0<=r_j<m_j. This follows from the defining annihilator equations m_jh_j all0 or all1/2 modulo1. The nonzero vectors of L of l1 norm<=2n consist exactly of ±(2n,0,0): any odd coefficient needs another odd coefficient, of combined norm at least2n+1; an even nonzero coefficient costs at least2m_j. In a product φ_αφ_β the frequency norm is at most|α|+|β|<=2n. Its only nonconstant extra Haar moment can therefore arise at α=β=(n,0,0). There φ²=1+cos(2nθ1), whose Haar average is2. All other Gram entries equal continuous orthogonality. Thus G=I+ee^T.

Since G^{-1}=I−ee^T/2, Pn=Hn−φ_e(x) sum_X wφ_e f/2. On X, |φ_e|=sqrt2; on the cube it is at mostsqrt2, and weights sum1. The correction operator norm is therefore at most1. Equal orders n+1 have no nonzero dual frequency of norm<=2n, giving G=I.

## An elementary continuous kernel estimate

Normalize Haar integration on the d-torus to mass1. Write D_n(t)=sum_{k inZ³,|k|1<=n} exp(ik·t). For r<=3 let S_M^(r)(t)=sum_{a_j>=0,sum a<=M} exp(i a·t). Its generating function in z is

`sum_{M>=0} S_M^(r)(t) z^M = (1−z)^{-1} product_j (1−z exp(it_j))^{-1}`.

For M>=0 choose rho=exp(−1/(M+1)). Cauchy's coefficient formula and Tonelli, integrating the absolute value first over all t_j and then the circle angle, give

`||S_M^(r)||L1 <= rho^(−M) J(rho)^(r+1) <= e J(rho)^(r+1)`,

where J(rho)=integral |1−rho exp(it)|^{-1} dt/(2π). The identity |1−rho e^{it}|²=(1−rho)²+4rho sin²(t/2), with the elementary linear lower bound for sin on[0,π/2], gives J(rho)<=C0 log(M+2). Decompose D_n by the support of k and its nonzero signs. A support of size r contributes a phase times S_(n−r)^(r), or0 if n<r. There are only finitely many (at most27) such pieces. Hence `||D_n||L1 <= C1 log(n+2)^4`.

## Discrete sampling does not add logarithms

For the normalized Fejer kernel F_M(t)=M^{-1}|sum_{j=0}^{M−1} e^{ijt}|², V_n=2F_(2n)−F_n has Fourier coefficients1 for |k|<=n. It reproduces every trigonometric polynomial with coordinate degree<=n. On any shifted uniform grid of length m>=n, averaging F_M retains only Fourier coefficients at multiples of m, so its average is at most1+2M/m. Therefore the average of |V_n| is at most2·5+3=13. Tensor the reproducing identity and use Tonelli to obtain, for every shift a and every such polynomial T,

`average_(rectangular m-grid+a) |T| <= 13³ ||T||L1`.

Both components of H have coordinate lengths>=n, so this applies to their average and every translate of D_n. Finally the cosine kernel satisfies the exact reflection identity

`K_n(cosθ,cosψ) = (1/8) sum_(epsilon in{±1}³) D_n(θ+epsilon ψ)`.

This follows by grouping Fourier frequencies by their coordinate absolute values. Positive folded weights mean the operator norm of Hn is the weighted sum of absolute kernel values, bounded by the average of the eight discrete sums above. Thus ||Hn||<=13³||D_n||L1, completing the proof.

## Assumptions, dependencies and scope

The proof uses only the explicitly defined parity grids, positive Haar weights and product Chebyshev measure; n>=1. No source theorem, finite computation, conjectural rank, or measured mesh maximum is required. This is an oversampled cubature projection, not minimal-node interpolation. Its node ratio tends3/2, not19/18. The rank-one correction has no implication that the inverse restriction matrix in T9-05 is uniformly bounded after extraction.

Closest literature: Cools–Poppe, Poppe–Cools and De Marchi–Vianello–Xu. The gate claims no new mechanism or priority. The extra logarithm comes precisely from the elementary Cauchy bound for a simplex kernel. Removing it requires a sharper continuous polyhedral Dirichlet L1 estimate, not a stronger sampling theorem. Independent mathematical audit remains required.

History:2026-11-06 Codex Sol xhigh assigned; self-contained supporting result developed while attempting the unresolved log³ target. Metadata later clarified that this is a supporting dependency, not a conjunctive claim split.
