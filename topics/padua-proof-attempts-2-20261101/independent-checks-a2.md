# A2 supplementary independent mathematical reconstruction

Checker: Codex `/root/a2_independent_route`, requested gpt-6.1-sol xhigh; runtime-resolved model/effort metadata are not separately exposed. Date: 2026-11-01. Rules read at `818ca4ad0942eb4743860f913a299ff30d959dae`. This is a supplementary Codex check and proof contribution, not the required Claude audit. Only this new file is owned by this agent; no Git mutation was performed.

## Scope and inputs

Read the task attachment, `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. Before mathematical development, read the complete 496-line `state/IDEAS.md` in bounded segments, including headings, identifiers, aliases, summaries and all obstruction/disposition tables. Search terms across state, topics, tracks and literature: `corner`, `stagger`, `cauchy`, `log.coefficient`, `Kolomoitsev`, `Lomako`, `Chebyshev.*Lebesgue`, `Lebesgue.*Chebyshev`. Read the full programme IDEA-17 entry, programme theory-04, and part-1 A1 theory. The literature index was opened before any source use; no PDF was opened and no full Kolomoitsev–Lomako reading is claimed. No argument below borrows that paper's method or theorem.

This is proof completion of registered A2. The projection-constant obstruction prevents the generic square lower-bound route from reaching 4/pi², but does not obstruct a positive corner sum. The failed CC absolute-cardinal-column route concerns another norm problem. No novelty or priority claim is made.

Dependency: **PD-T?proof-attempts-codex-01 (audit pending)**. Dated qualification, 2026-11-01: root reported that part-1 Claude audit-01 at `95279b833bca5967fcf47c1b71a56ff622185b4e` accepted A1 without a mathematical finding; upstream disposition records remain pending.

## Receipt for comparison theory-04

Read the FULL file `theory/proof-attempts-2-codex-04-corner-product-comparison.md`, checked at 2026-11-01T09:13:39Z with SHA-256:

`80272d3451a2a90663ce53c785399c122b2625ffb03f35c2dd4742f07c2034f8`.

The checked version states `|Lambda_c(n)-L_n²| <= 54` for every integer n>=2. Every proof section A–D was independently reconstructed. No mathematical correction remains within this declared scope.

1. **Summand and exceptional point.** For s=(-1)^j, a=j*pi/n, b=k*pi/(n+1), and j+k odd, the two product-to-sum numerators are s(1+cos a)/2 and s(1+cos b)/2. Their denominator is (cos a-cos b)/2. Hence D_n=s(2+cos a+cos b)/(cos a-cos b) and `|D_n-s|=2(1+cos b)/|cos a-cos b|`. Coprimality of n,n+1 leaves only endpoint coincidences. The odd board excludes (0,0). At (pi,pi), the finite rhombus sum is s(2n+1), so the corrected absolute value is 2n and its weighted contribution is exactly 1/(n+1). All other b=pi terms vanish.

2. **Exact square.** In the same-mesh sum simultaneous reflection j->n-j,k->n-k replaces 1+cos(k*pi/n) by 1-cos(k*pi/n), so averaging replaces the numerator by 1. On j>k set r=j+k, t=j-k; both are odd, t<=r<=2n-t, and the denominator is 2 sin(r*pi/(2n))sin(t*pi/(2n)). The two possible orders cancel that factor 2. Reflect r->2n-r. For t<n the diagonal coefficient is 1, off-diagonal coefficients are 2, and the terminal r=n coefficient is 1. For t=n, possible only when n is odd, the endpoint pair has weight 1/4. These are exactly the coefficients of the square of the odd csc sum with half terminal weight. Thus F_n=L_n², including odd-n endpoint weights.

3. **Deformation.** Exact subtraction gives equation (6) in theory-04. Since all a/2,b_i/2 are in [0,pi/2], `sin((a+b_i)/2)>=cos(a/2)sin(b_i/2)`. Dividing produces `cot(b_0/2)+cot(b_1/2)`. The chord bound and `cos x<=pi/2-x` give equation (7). For k<j, both T_i>=pi|j-k|/(2n), so their sines are >=|j-k|/n. For k>j put r=n-j and l=k-j: `sin T_1 >= [n(l-1)+r]/[n(n+1)]`, and `n+1-k<=r<=n`. The last inequality follows from `l*r <= n(l-1)+r`. Hence `E_jk<=pi²*n/(2*l²)` in both cases. The cases l=1 and k=n are included; k=0 or j=n have exactly zero deformation. Summing over odd l with weights at most 1 gives pi⁴/2 after normalization.

4. **Weights and normalization.** Both sums in the deformation comparison use the ACTUAL eta_k weights. The reference k=n terms vanish, so only at that stage may eta_n be replaced by epsilon_n without error. This does not assert that the actual k=n row vanishes. Thus the deformed sum compares directly to nF_n/(n+1), with no extra half-row error. From the sine chord bound, `L_n<=2*sum_(r odd<=n)1/r<=2+log n`: for odd r>=3, `1/r <= (1/2)*integral_(r-2)^r dt/t`. The derivative of `(log x+2)²/x` is `-log x*(log x+2)/x²<=0` for x>=1. Therefore F_n/(n+1)<=4. Including the exceptional endpoint gives `pi⁴/2+4+1/(n+1)<54` for n>=2.

Commands actually executed for this receipt were source reads/searches, `git rev-parse HEAD`, `sha256sum` on theory-04, and `date -u`. They are provenance checks, not mathematical exact/interval computations. No numerical run or computational proof is claimed.

## Independent one-dimensional asymptotic contribution

The following elementary derivation was supplied to the primary developer. Put A=pi/2, h=pi/(2n), and g(x)=csc(x)-1/x with g(0)=0. On [0,A], g is increasing. Indeed

`sin x / x >= (1+cos x)/2 >= sqrt(cos x)`;

the first inequality is equivalent to tan(x/2)>=x/2. Thus `sin² x>=x² cos x`, so `g'(x)=1/x²-cos x/sin² x>=0`. Also g(A)=1-2/pi and

`integral_0^A g(x) dx = log(4/pi)`.

Let Delta=2h. For even n, the odd-r sum is midpoint quadrature on [0,A]. On each interval the midpoint error is bounded by h times the variation of g there, giving total error at most h*g(A). For odd n, the midpoint intervals cover [0,A-h] and the half-weight terminal value contributes a right rectangle of width h on [A-h,A]. The first error is at most h*g(A-h), the last at most h*(g(A)-g(A-h)); again total error is at most h*g(A). Consequently

`|(2/n)*sum'_(r odd<=n) g(rh) - (2/pi)*log(4/pi)| <= (1-2/pi)/n`.

For B_n=sum'_(r odd<=n)1/r, write H_m=log m+gamma+e_m with `0<e_m<=1/(2m)`. This standard bound follows directly by applying the convex trapezoid inequality to 1/x on each interval [k,k+1] and telescoping the tail. For even n,

`B_n=H_n-(1/2)H_(n/2)`,

so its error from `(log n+gamma+log 2)/2` is at most 1/(2n). For odd n>=3,

`B_n=H_n-(1/2)H_((n-1)/2)-1/(2n)`.

The non-e_m part of the error is `q=(1/2)log(n/(n-1))-1/(2n)`, with `0<=q<=1/[2n(n-1)]`. Combining the two e_m bounds gives error at most `1/[2(n-1)]<=1/n`. At n=1 the same bound is immediate from 0<gamma<1 and 0<log 2<1. Therefore, for all n>=1,

`|L_n - (2/pi)*(log n+gamma+log(8/pi))| <= (1+2/pi)/n < 2/n`.

Squaring this estimate and using theory-04 yields the desired b coefficient with an explicit bounded remainder. This note is a supporting proof contribution; durable target statements and constants remain owned by the primary developer in theory-01/-02/-03.

## Limits

No maxima count, global corner-argmax theorem, A3 constant, or new literature claim was checked. The required Claude audit and any independent execution receipt for a developer exact/interval regression remain separate obligations. This agent executed no such regression.
