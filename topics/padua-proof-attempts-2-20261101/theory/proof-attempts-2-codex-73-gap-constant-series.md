# PD-T?proof-attempts-2-codex-73 — Positive one-dimensional and alternating-series formulas for g

ID kind: PD-T.
Aliases: A4(a) central-grid gap constant; exact rational series; integrated triangle defect.
Split from: the constant g in72.
Split into: none; identification of the central envelope with its complementary-grid values remains separate.

## Statement

The explicitly defined constant g in72 satisfies

\[
 g=\frac8{\pi^2}\int_0^1
 \left(\operatorname{arsinh}x+\frac{x}{1+\sqrt{1+x^2}}\right)
             \operatorname{artanh}x\,dx
   =\frac8{\pi^2}\sum_{k=0}^\infty(-1)^k a_kJ_k,             \tag{1}
\]

where all series coefficients and moments are positive rational numbers,

\[
 a_k=\frac{{2k\choose k}}{4^k}
       \left(\frac1{2k+1}+\frac1{2k+2}\right),\qquad
 J_k=\frac1{2k+2}\sum_{r=0}^k\frac1{2r+1}.                  \tag{2}
\]

Writing S_K=sum_(k=0)^K(−1)^k a_kJ_k, every even K>=0 gives the strict, computable enclosure

\[
 \frac8{\pi^2}S_{K+1}<g<\frac8{\pi^2}S_K,\qquad
 |g-(8/\pi^2)S_K|<\frac8{\pi^2}a_{K+1}J_{K+1}.             \tag{3}
\]

In particular

\[
 \frac{47}{9\pi^2}<g<\frac{1651}{300\pi^2}.                 \tag{4}
\]

No decimal approximation, fit or numerical quadrature is required to define g or prove these bounds.

## Definitions and assumptions

g is exactly72's limiting corner defect for complementary central grid points. arsinh x=log(x+sqrt(1+x^2)) and artanh x=(1/2)log((1+x)/(1−x)). The integral at1 is improper; its integrand has only an integrable logarithmic singularity. These identities do not redefine g or the source runner-up.

## Status by part

Overall status: **PROVED** (written analytic formulas and strict tail theorem; required Claude audit PENDING).

| Part | Status |
|---|---|
| Positive1D representation and exact rational alternating series | PROVED |
| All finite bounds(3) and explicit first bounds(4) | PROVED |
| Any numerical evaluation at a chosen finite K | A supplementary finite execution, recorded only after actual run/replay |

## Depends on

72 and elementary substitutions, integration by parts, binomial Taylor series and positive-term integration. Its indirect A1 dependency retains the literal historical label **PD-T?proof-attempts-codex-01 (audit pending)** with the accepted/merged qualification in70. No asymptotic fit, KL remainder constant or unproved central-maximum statement.

## Checks

The positive1D formula and coefficients/moments/strict alternating bounds were independently reconstructed analytically in independent-checks-a4.md. A separately implemented exact Fraction evaluator code/a4g_series.py was frozen at SHA256510955136172a93206861f3a8252aa36460daa8c7965770d0fd6354209104ab9 and actually executed by its implementer and a different agent. Both exited0 and kept the source hash unchanged. K=64 bounds S65 and S64 were evaluated with exact integer/Fraction arithmetic and rigorous Machin arctangent bounds. The resulting proved rational enclosure is

`54850498619/100000000000 < g < 109705011071/200000000000`,

equivalently the exact outward decimal bounds0.548504986190<g<0.548525055355. No floating conversion or quadrature is used. The1754byte developer receipt outputs/a4g_series_developer.json has SHA2561f05b126bdd7ab13b2c1fb889019455d3f02ab9cce95bb76e369340c57e1f24c (0.003861s); the distinct replay outputs/a4g_series_independent.json has SHA2565032027b25a848c0fc08be9b03408d1f2ae40511f6975d61584734c79d2a15f9 (0.004015s). They agree after removing only elapsed_seconds. independent-execution-a4-g.md records both commands and scope. This supplementary evaluation applies to the same g defined in72 and makes no branch/envelope inference.

## Sources

Continuation of the registered A4(a) point-value target via71/72; full gate in T-A4a.md. This is a reformulation/evaluation of the same elementary positive defect constant, no historical novelty or priority claim.

## Proof

### 1. Integrate the inner angular variable exactly

Let c=cos t, s=sin t, Q=sqrt(1+c^2), k=tan(t/2), with0<t<pi/2. In72's inner integral the two fractions agree at cos a=−c^2. Put u=tan(a/2), so cos a=(1−u^2)/(1+u^2) and da=2du/(1+u^2). The endpoints a=t,arccos(−c^2),pi−t correspond to u=k,Q/s,1/k. Direct integration on the two subintervals gives

\[
 I(t)=2k\log\frac{1+c+Q}{\sqrt2}
       +\frac2k\log\frac{1-c+Q}{\sqrt2}.                    \tag{5}
\]

For example the first antiderivative is2k artanh(ku), and the second is k^(-1)log((u−k)/(u+k)). Endpoint subtraction reduces them to(5) using

`(1+c−Q)(1+c+Q)=2c`,

`(Q−1+c)(Q+1−c)=2c`, and `(1−k^2)/(1+k^2)=c`.

If R_±=log((1±c+Q)/sqrt2), then R_++R_−=log(1+Q), while R_+−R_−=arsinh c. Since k+k^(-1)=2/s and k−k^(-1)=−2c/s, equation(5) becomes

\[
 I(t)=\frac2{\sqrt{1-c^2}}
       \{\log(1+\sqrt{1+c^2})-c\operatorname{arsinh}c\}.
                                                               \tag{6}
\]

These expressions have the endpoint limits I(0)=0 and I(pi/2)=2log2; no divergent separate term is used as an endpoint value.

### 2. A positive integral by integration by parts

Define F(c)=log(1+sqrt(1+c^2))−c arsinh c. Then F(1)=0 and direct differentiation gives

`F'(c)=−arsinh c−c/(1+sqrt(1+c^2))`.

Substitute(6) into72 and change t to c. Thus

`g=(8/pi^2) integral_0^1 F(c)/(1−c^2) dc`.

Integrate by parts with derivative of artanh c equal to1/(1−c^2). The boundary term at0 is0. At1 it is also0: F' is bounded on[0,1] and F(1)=0, so F(c)=O(1−c), whose product with artanh c tends to0. The resulting positive integral is exactly the first expression in(1). Its logarithmic endpoint singularity is integrable.

### 3. Strict rational alternating bounds

The binomial expansions of arsinh x and of(sqrt(1+x^2)−1)/x, continuously defined at0, give

\[
 \operatorname{arsinh}x+\frac{x}{1+\sqrt{1+x^2}}
       =\sum_{k=0}^\infty(-1)^k a_kx^{2k+1}.                \tag{7}
\]

The central-binomial factor {2k choose k}/4^k is positive and strictly decreasing, as is the sum1/(2k+1)+1/(2k+2). Therefore a_k decreases to0. For0<=x<=1 the alternating remainder after K has magnitude at most a_(K+1)x^(2K+3), is nonzero for x>0, and has the sign of its first omitted term. These pointwise bounds remain valid at1 by the alternating-series limit.

Multiply the inequalities by artanh x>=0 and integrate. The remainder is bounded by a_(K+1)J_(K+1), and tends to0, because J_k<=J_0=1/2 and a_k->0. The inequalities are strict after integration over(0,1). Finally, expanding artanh x in its positive power series and integrating monotone partial sums gives

\[
\begin{split}
 \int_0^1x^{2k+1}\operatorname{artanh}x\,dx
 &=\sum_{l=0}^\infty
       \frac1{(2l+1)(2l+2k+3)}\\
 &=\frac1{2k+2}\sum_{r=0}^k\frac1{2r+1}=J_k,
\end{split}
\]

where the second equality is the telescoping partial fraction. This proves the series and all tail bounds(3). Its first three terms give S_1=47/72 and S_2=1651/2400; using the odd lower and even upper partial sums yields(4). ∎

### 4. Exact pi bounds used only for the reported rational enclosure

For completeness, the evaluator's Machin identity has an elementary exact justification. Put u=arctan(1/5),v=arctan(1/239). The tangent doubling formula gives tan(2u)=5/12, tan(4u)=120/119 and tan(4u−v)=1. Bounds1/5−1/375<u<1/5,0<v<1/239 and pi>3 show0<4u−v<pi/2. Thus4u−v=pi/4, proving pi=16u−4v. The alternating arctangent series at1/5 and1/239 bounds each value between its64-term odd-final partial sum and that sum plus its65th positive term. Combining lower/upper bounds with the displayed positive16 and negative4 coefficients proves the exact pi enclosure used by the Fraction evaluator; its final floor/ceiling operations are outward rational rounding. This supplies no additional assumption about g.

## Scope

An exact characterization and arbitrarily narrow rational/pi^2 enclosures of72's grid-gap constant. It is not proof that the source's searched runner-up or R_cen has this constant. No all-n global argmax follows from the value of g.

## Open items

Required Claude audit. Supplementary K64 exact evaluation and different-agent replay are complete. The central-envelope/critical-branch comparison is the substantive remaining A4(a) obligation.

## History

2026-11-01, Codex gpt-6.1-sol xhigh, within the15:24–18:24UTC box. The independently derived positive integral explains the same earlier double-integral constant; no finite fit was used to choose its formula or tail.
