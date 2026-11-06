# PD-T?argmax-bridge-codex-D11-near — Physical near noncorner exclusion from degree16000

ID kind: PD-T. Aliases: entropy-absorbed true-constant near comparison;
fractional maximum with the C08 logarithmic loss.
Split from: D11 prospective global onset. Split into: none; the far and
global comparisons have separate D11 records.

## Statement and definitions

For every integer n>=16000 put m=n+1 and use precisely PD-T101/PD-T364's
corrected Padua cardinal polynomials, exceptional highest mode in x,
endpoint weights and finite-polynomial collision values. Let (J,K) be a
physical odd center, 0<=J<=n,0<=K<=m,J+K odd, which is NOT an actual
nonnode corner. If

    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m in[0,pi],
    rho=|alpha|+|beta|<=1/2,

then

    lambda_n(cos theta,cos phi)<Lambda_c(n)-7/1000.       (1)

Here Lambda_c(n)=lambda_n(-1,-1)=S_n(0,0). S_n is PD-T364's corrected
common primitive and M_infty is D02's TRUE completed model

    M_infty(psi,L)=(4a/pi^2)L^2+b_full(psi)L+C_infty(psi),
    a=(cos|alpha|+cos|beta|)/2, L=log n.

## Status and assumptions

Overall status: **PROVED**, developer analytic assembly with the frozen
directed scalar endpoint under the numerical contract below. Distinct
D11 mathematical/source/arithmetic review is **PENDING**; this is not an
independent acceptance or authority for root to adopt a new global range.
All analytic inequalities use exact real arithmetic and natural logs.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Physical exclusion (1) on the stated near noncorner domain | PROVED | Written reduction, all-n monotonicity and directed endpoint; D11 review pending |

## Depends on

- [C08 weighted coefficient](C08-far-weighted-coefficient.md): exactly
  b_full-b_c<=3(1-a)/pi^2 on the full closed phase diamond; B_c=4/pi^2.
- [D10 near constant](D10-relative-constant.md): on rho<=1/2,
  C_infty(psi)-C_infty(0)<=15*rho^(3/2)/32+(113/72)r2
  +(4/9)r2*log(1/rho), r2=alpha^2+beta^2.
- [D08 near representation](D08-near-representation.md): its FULL scalar
  formula Ehat(n) bounds |S_n-M_infty| on rho<=1/2 for n>=32, including
  zero. Only that formula and its valid domain are used; its later
  Ehat<1/80 at40000 is not used at16000.
- [C02 physical defect](C02-defect-dense-band.md): for n>=4096 and the
  full physical rho<=1/2 guard, Q_h>1/16 if0<J<n and Q_v>1/16 if0<K<m.
  PD-T364 gives lambda=S_n-Delta, Delta>=max(Q_h,Q_v).

D10's distinct supplementary acceptance is
[the D10 review](../independent-checks-D10-relative-constant.md), report
SHA256 `bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c`.

## Proof

### 1. Retain the coefficient loss and the true fractional constant

Separate phase evenness is used only for S_n,M_infty and their phase-only
bounds. The physical defect remains attached to its original signed
center. In this section take alpha,beta>=0. Write u=1-a and

    T(n)=(4L^2-3L)/pi^2.

The C08 inequality gives, exactly,

    M_infty(psi,L)-M_infty(0,L)
      <=-u*T(n)+C_infty(psi)-C_infty(0).               (2)

For t<=1/2, the alternating cosine bound gives
1-cos t>=t^2/2-t^4/24. Since alpha^4+beta^4<=r2/4,

    u>=r2/4-(alpha^4+beta^4)/48>=47*r2/192.           (3)

For rho>0 put x=log(1/rho). Differentiating x*exp(-x/2) shows its
maximum over x>=0 is2/e, at x=2. Also e>1+1+1/2+1/6=8/3, hence
2/e<3/4. Since r2<=rho^2, D10's entropy term obeys

    (4/9)r2*log(1/rho)
       <=(4/9)rho^(3/2)[sqrt(rho)*log(1/rho)]
       <=rho^(3/2)/3.

Thus, with the continuous value zero at rho=0,

    C_infty(psi)-C_infty(0)
       <=A*rho^(3/2)+(113/72)r2, A=15/32+1/3=77/96.  (4)

Define

    B(n)=[(47/192)T(n)-113/72]/2,
    J(n)=27*A^4/[256*B(n)^3].

The endpoint below gives B(16000)>3.5035>0. For all n>=16000,
L>=log16000>9 and

    T'(n)=(8log n-3)/(pi^2*n)>0,
    B'(n)=(47/384)T'(n)>0.

Consequently B>0 throughout that range, and J decreases there. Combining
(2)--(4) and r2>=rho^2/2 now yields

    M_infty(psi,L)-M_infty(0,L)
       <=A*rho^(3/2)-2B(n)r2
       <=A*rho^(3/2)-B(n)rho^2<=J(n).                (5)

For the last inequality put y=sqrt(rho). The polynomial A*y^3-B*y^4
has derivative y^2(3A-4B*y), so its global maximum over y>=0 is
27*A^4/(256*B^3). This is valid on the smaller closed near domain too.
The origin and axes are included by continuity; there is no division
by r2, assumed quadratic smoothness, or differentiation through a
moving absolute-value root.

### 2. Use the full finite near allowance at its actual domain

For clarity, the EXACT Ehat formula being evaluated is as follows. Put
b=4/pi^2,H=1+L and h0=log(5/2)+1/18. Then

    A_D={ [52/pi^2+176/(3pi)]H+7+1/pi }/n
                                  +10/n^2+20H/(pi*n^2),
    A_G=[(21/5)L+(9/4)log(2m)+1022/15]/m,
    A_M=b(2L+2h0)/n+[4+b(L+1/n)]/(4n^2-1)
             +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    A_log=[3log m+log2+2log pi+2]/(2pi*m),
    A_6=(18+L/2)/n+73/n^2,
    Ehat=A_D+A_G+A_M+A_log+A_6.                       (6)

D08 proves (6) majorizes its actual-phase component bound for every
integer n>=32 on the whole near domain. Here is a fresh all-degree
monotonicity check, so no endpoint is extrapolated numerically.
A_D and A_6 are positive sums of (cL+d)/n^j whose derivatives are
negative for L>3. A_G has numerator N with
m*N'=(21/5)(1+1/n)+9/4<N for n>=32, since its constant1022/15 alone
exceeds the left side. A_log decreases because its numerator exceeds3.
In A_M, (2L+2h0)/n decreases since L>3. Split its second term as
(4+bL)/(4n^2-1)+b/[n(4n^2-1)]; the first derivative numerator is
b(4n^2-1)/n-8n(4+bL)<0, and the second is a product of positive
decreasing factors. The third term decreases. For the last term set
V=5+b(log(n+1/2)+2); its derivative has the sign of
b(n-1/2)/(n+1/2)-2V<0, since b<1/2 and V>5. Hence Ehat decreases
for all real n>=32, in particular on n>=16000.

The sole frozen16000 receipt gives outward bounds

    Ehat(16000)<0.027003655663226,
    J(16000)<0.001014995023436,
    1/16-2Ehat(16000)-J(16000)>0.007477693650113>7/1000. (7)

These displayed rounded bounds suffice by exact terminating-decimal
arithmetic; the50-digit receipt retains tighter endpoints. Since Ehat
and J decrease, the last strict comparison holds for every n>=16000.
The near representation at both psi and zero, with S_n(0)=Lambda_c,
therefore proves

    S_n(psi)-Lambda_c<=J(n)+2Ehat(n)<1/16-7/1000.     (8)

### 3. Subtract one valid physical defect floor

At any noncorner physical odd center at least one of0<J<n or0<K<m
holds: the odd centers with two endpoint coordinates are precisely the
two actual nonnode corners. Since16000>=4096, C02 applies with its
physical signs, both adjacent meshes and full radius guard, and gives
Delta>=max(Q_h,Q_v)>1/16. Subtracting this from (8) proves (1).
The two projections are never added. Nodes, axes, boundary centers,
both degree parities and all polynomial collisions retain their exact
finite definitions.

## Checks, scope and open items

The frozen scalar source and evidence identities, command, numerical
trusted base, actual chronology and independent-check obligation are in
[the canonical attempt](../attempts/D11-onset.md). No scalar rerun or
native/board/quadrature/phase-grid execution was made while writing this
proof. The argument charges two absolute errors; the full relative
S_n-a*S_n(0) theorem remains OPEN. Actual corners and far phases have
separate comparisons. This is a sufficient onset, with no minimality,
new-mechanism or historical-priority claim.

## History

2026-11-06, resumed Codex mathematical developer, parent-assigned Sol
xhigh; serving metadata unexposed. Rules read at
`5ecf97801631192fd10d84089c5a8c79bfb95138`. Original preregistration/input
is retained in [the idea](../ideas/D11-onset.md). All old source, evidence,
parameters, corrections and theorem quantifiers remain unchanged.


### Supplementary review closure — 2026-11-06

Distinct Astra high reconstruction and independent directed scalar check
ACCEPTED this unchanged developer scope; no unresolved finding. See
[independent-checks-D11-onset.md](../independent-checks-D11-onset.md),
report SHA25650376e8ebf3dc6484763e8d3a68d7d416f25a62420edf3c2d5ba1605f9380217.
All28 independently reconstructed intervals lie inside the author bounds.
The preserved first hash-guard failure and single reviewed hash-only
recovery are documented there; author chronology remains in the attempt.
Final Claude audit remains pending. No finite enumeration was performed.
