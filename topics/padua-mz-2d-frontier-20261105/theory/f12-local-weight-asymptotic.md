# PD-T?mz2d-frontier-codex-12 — logarithmic fixed-node weights with a global summable majorant

ID kind: PD-T.
Aliases: spectral-corner weight asymptotic; carrier-packet domination;
even-m Padua boundary weight limit.
Split from: the common supporting lemma for F1/F2 carrier packets.
Split into: signed negative and positive packet consequences are separate
PD-N?mz2d-frontier-codex-13 and -14.

## Statement

Let m run through the positive even integers, and use exactly the signed
Lebesgue Padua rule and coordinate order in the frozen definitions.
Write `w^(m)_(j,k)` for its weight at
`(cos(j*pi/m),cos(k*pi/(m+1)))`, where `j+k` is even. Define
`e_0=1/2` and `e_j=1` for every integer j>=1.

For every fixed pair j,k>=0 with j+k even,

\[
 \lim_{\substack{m\to\infty\\2\mid m}}
 \frac{m^4 w^{(m)}_{j,k}}{\log m}
 =-16e_je_k(-1)^j.                                    \tag{1}
\]

Moreover there is an absolute constant C, for example C=4096, such that
for every even m>=4 and every retained node,

\[
 |w^{(m)}_{j,k}|
 \le\frac{C}{m^4}\{(1+j)(1+k)+\log(m+1)\}.             \tag{2}
\]

In (2), j ranges up to m and k up to m+1; their distances are measured
from the particular corner (1,1). The inequality is intentionally large
away from that corner. It suffices for dominated convergence against
packets whose squared profiles decay as `(1+j)^(-4)(1+k)^(-4)`.

## Definitions

Put R=m/2, `theta_j=j*pi/m`, `phi_k=k*pi/(m+1)`, and

\[
 t_0=2,\qquad t_a=-\frac4{4a^2-1}\quad(a\ge1),\qquad
 S_R(t,s)=\sum_{a+b\le R}t_at_b\cos(2at)\cos(2bs).
\]

For finite m set endpoint factors `epsilon_0=epsilon_m=1/2`, all other
epsilon_j=1; similarly `eta_0=eta_(m+1)=1/2`. These finite-grid factors
are distinct from the fixed-limit e_j in (1). Let `h_m=2/(1-m²)`.

## Assumptions

Real exact arithmetic; even m>=4; the signed interpolatory weights for
unnormalized dxdy. No weight sign classification is assumed. The fixed
indices in (1) are held constant before the limit. No claim of uniform
convergence of (1) across all node indices is made.

## Status by part

Overall status: **PROVED** (analytic development; independent/Claude
audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Fixed-node asymptotic (1) | PROVED | Exact integrated cardinal formula and two thin spectral corners |
| Uniform bound (2) | PROVED | Absolute tail telescoping and explicit triangle estimate |

Candidate disposition: retained common supporting result. This is not
by itself a spectral theorem.

## Depends on

PD-T101's accepted cardinal formula, in exactly the normalization quoted
and integrated in PD-T111. The elementary absolutely convergent cosine
series `pi sin t=2−sum_(a>=1)4cos(2at)/(4a²−1)` on [0,pi]. This last
identity follows by integrating its cosine coefficients; a direct
Fourier-uniqueness justification is included below.

## Checks

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`.
No mathematical computation was executed by this developer. Separate
floating fixed-node probes from the numerical worker are finite checks,
not a dependency of this asymptotic. Independent analytic reviewers were
sent the decomposition and thin-corner argument before this file; their
completed written reports, if any, must be linked by the orchestrator.

## Sources

Full local predecessors PD-T101 (cardinal normalization as quoted in
PD-T111), PD-T106/111, and the complete gate in ../ideas-f12.md.
No external theorem or historical priority claim is used.

## Proof or evidence

### Exact weight and absolutely convergent tails

Integrate the accepted Padua cardinal formula. Only even coordinate
degrees survive, and `c_(2a) h_(2a)=t_a`, with c_0=1 and c_l=2 for l>0.
The exceptional x term integrates to `2h_m T_m(x_j)`. Thus at every node

\[
 w^{(m)}_{j,k}=\frac{2\epsilon_j\eta_k}{m(m+1)}
 \{S_R(\theta_j,\phi_k)-2h_m\cos(m\theta_j)\}.          \tag{3}
\]

The cosine coefficients of pi sin t on [0,pi] are t_a on the even
frequencies, and zero on the odd ones, by elementary integration.
Since `sum |t_a|<infinity`, their series converges uniformly to a
continuous function with those coefficients. The difference from pi
sin t has all cosine coefficients zero. Cosine polynomials are uniformly
dense among continuous functions on [0,pi] (via x=cos t and polynomial
approximation), so its squared integral is zero and the difference
vanishes. Consequently, with

\[
 f(t)=\pi\sin t,\qquad
 T_R(t)=\sum_{a>R}t_a\cos(2at),
\]

the absolutely convergent rectangle expansion gives exactly

\[
 S_R(t,s)=f(t)f(s)-f(t)T_R(s)-f(s)T_R(t)
           +T_R(t)T_R(s)-V_R(t,s),                    \tag{4}
\]
\[
 V_R(t,s)=\sum_{\substack{1\le a,b\le R\\a+b>R}}
 t_at_b\cos(2at)\cos(2bs).                            \tag{5}
\]

The factors with index zero cannot occur in the omitted triangle.
Telescoping gives

\[
 |T_R(t)|\le\sum_{a>R}\frac4{4a^2-1}
 =\frac2{2R+1}\le\frac1R.                             \tag{6}
\]

### Uniform triangle estimate

For a>=1, `|t_a|<=4/(3a²)`. Split (5) into a<=R/2, b<=R/2, and
both a,b>R/2. The first two pieces are disjoint because a+b>R.
In the first piece, b ranges over at most a integers, all greater
than R/2, so

\[
 \sum_{a\le R/2}|t_a|\sum_{b=R-a+1}^R|t_b|
 \le\frac{64}{9R^2}H_{\lfloor R/2\rfloor}.
\]

The second piece has the same bound. The remaining at most R² pairs
have product at most `256/(9R^4)`. Thus for R>=2,

\[
 |V_R(t,s)|
 \le\frac{128H_{\lfloor R/2\rfloor}+256}{9R^2}
 \le\frac{64(1+\log R)}{R^2}.                         \tag{7}
\]

Using (4), (6), `sin(theta_j)<=pi*j/m` and
`sin(phi_k)<=pi*k/m`, the absolute bracket in (3) is at most

\[
 \frac1{m^2}\left\{
 \pi^4jk+2\pi^2(j+k)+260+256\log R+\frac{16}3
 \right\}.                                           \tag{8}
\]

Here the final term bounds `m² |2h_m|` for m>=2. Multiplication by
`2epsilon_j eta_k/[m(m+1)] <=2/m²` proves (2) with C=4096; indeed the
coefficients in (8) are all smaller than 2048 and
`log R<=log(m+1)`. This bound also covers the moving far endpoint
halfweights, since they are at most one.

### The two thin corners supply the logarithm

Fix j,k. Set t=theta_j, s=phi_k with m=2R. Then
`2Rt=j*pi` exactly and `2Rs -> k*pi`. All terms in (4) other than
V_R are `O_(j,k)(R^(-2))` by (6) and `f(t),f(s)=O_(j,k)(R^(-1))`.
It therefore remains to show

\[
 \frac{R^2V_R(t,s)}{\log R}
 \longrightarrow (-1)^j+(-1)^k.                     \tag{9}
\]

For 0<delta<1/2 split the triangle into the strip a<=delta R,
the strip b<=delta R, and the remaining middle. In the first strip
b runs from R−a+1 to R. Uniformly there, as R grows,

\[
 R^2t_b\cos(2bs)=-\cos(k\pi)+O_k(\delta)+o_R(1),
 \qquad
 \cos(2at)=1+O_j(\delta^2).
\]

The R-uniform O(delta) error follows from b/R in [1−delta,1],
`R²t_b=-1+O(delta)+O(R^(-2))`, and continuity of cosine on this bounded
phase range. Also

\[
 \sum_{a=1}^{\lfloor\delta R\rfloor}a t_a
 =-\log R+O_\delta(1),                               \tag{10}
\]

because `a t_a=-1/a+O(a^(-3))`. Summing over the exactly a choices of b
shows that the first strip, after multiplication by R²/log R, equals
`cos(k*pi)+O_(j,k)(delta)+o_R(1)`. The second strip gives
`cos(j*pi)+O_(j,k)(delta)+o_R(1)`.

In the middle a,b>delta R, the absolute sum is at most
`16/(9delta^4 R²)`: there are at most R² pairs and each product is at
most `16/(9delta^4 R^4)`. For each fixed delta its contribution after
multiplication by R²/log R tends to zero. Let R tend to infinity first
and then delta decrease to zero. This proves (9), including j=0 or k=0.

Since m=2R, equations (4) and (9) give

\[
 \frac{m^2 S_R(\theta_j,\phi_k)}{\log m}
 \longrightarrow -4\{(-1)^j+(-1)^k\}.
\]

The exceptional term in (3) is O(m^(-2)) and hence disappears in this
normalization. On the retained checkerboard, (-1)^j=(-1)^k. For fixed
j,k the finite endpoint factors eventually equal e_j,e_k; the far
endpoints have moved away. Substitution in (3) proves (1). ∎

## Scope

Only the even-m subsequence is asserted, which is sufficient for the
separate countersequence theorems. The weight signs at growing indices
are not classified. Other corners and a uniform local asymptotic are
unneeded and are not silently inferred. The majorant (2) is uniform
over the whole grid, so the following packet arguments need no exchange
of a merely pointwise limit with an uncontrolled sum.

## Open items

Independent analytic reconstruction and required Claude audit; attach
the completed check records. An effective remainder and finite explicit
threshold are not supplied. They are not needed for the existential
countersequences, but would be needed to name an explicit violating m
from this proof alone.

## History

2026-11-05, Codex F1/F2 developer, requested gpt-6.1-sol xhigh; runtime
metadata unexposed. G0 PASS was received before mathematical tests were
authorized. This proof is analytic. Parent and two independent workers
received the delicate decomposition and domination before publication.
