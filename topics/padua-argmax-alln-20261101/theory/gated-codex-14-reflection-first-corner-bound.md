# PD-T228 (PD-T?argmax-alln-gated-codex-14) — Reflection-first uniform corner bound

Final registration: **PD-T228**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: direction2 round2; reflected-cardinal quadratic comparison; average before absolute values; 237000 corner remainder.
Split from: uniform local-corner obligation P3 for PD-T099.
Split into: the eventual global assembly is recorded separately in gated-codex-15. The all-degree target and finite bridge remain OPEN.

## Statement

Use exactly the even-checkerboard nodes, weights and corrected polynomial kernel of PD-T101. Put m=n+1, N=nm, c=(-1,-1), and

   z_n(alpha,beta)=(-cos(alpha/n),-cos(beta/m)),
   a=(cos alpha+cos beta)/2, rho=alpha+beta.

For every integer n>=2 and every alpha,beta>=0 with rho<=1/64,

   lambda_n(z_n(alpha,beta))
      <=a*Lambda_c(n)+237000*rho^2*log(n+1).                           (1)

The same estimate holds in inward angles at the other nonnode corner. In particular, if

   Lambda_c(n)>2370000*log(n+1),                                      (2)

then lambda_n(z_n(alpha,beta))<Lambda_c(n) whenever0<rho<=1/64. Condition (2) holds for every n with log n>=10^7. Under (2), strict comparison also holds at every inward physical point c+h with0<h_x+h_y<=2^(-17)/n^2. This is an explicit but very coarse local threshold and a uniform physical radius, not an effective global threshold.

## Definitions and assumptions

For the physical odd board O={(j,r):0<=j<=n,0<=r<=m,j+r odd}, let e_j,f_r be the half endpoint factors. Write

   F_jr(alpha,beta)=(-1)^j*G_n((j*pi+alpha)/n,(r*pi+beta)/m)/2,

where G_n=D_n-cos(nu) is the corrected finite cosine polynomial of PD-T101/185. Every apparent collision is evaluated by that polynomial. Lambda_c(n)=lambda_n(-1,-1), whose value at the other nonnode corner is the same. All statements use exact real arithmetic. The absolute value is applied after summing the four reflected kernel values belonging to one cardinal.

## Status by part

Overall status: **PROVED**, by the complete finite reflection and derivative argument below. Supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Uniform all-n local estimate (1), rho<=1/64 | PROVED | Exact reflection normalization, absolute symmetric Taylor bounds, finite polynomial collision family |
| Strict local comparison under (2), including log n>=10^7 and physical radius2^(-17)/n^2 | PROVED | Elementary cosine bounds and PD-T157 |

These are a bound and its elementary local consequence. No global-maximizer localization or finite-degree global certification is claimed by this file. Candidate disposition: retained quantitative variant of P3 / Claude-02 / fallback-04 / IDEA305. No priority claim.

## Depends on

- PD-T101: corrected coefficient kernel, weights and cardinal formula.
- PD-T185 and gated-codex-03: divided-difference numerator and polynomial extension, with the same exceptional x-mode convention.
- Gated-codex-07, proof sections1 and3: regular pointwise derivative/sum bounds and global finite-sum Hessian bound on the removed B family. The particular inequalities reused are restated and their application to the absolute averaged remainder is proved below. No primitive numerator-sign estimate is transferred.
- PD-T157: Lambda_c(n)>=(4/pi^2)*log^2 n-54, used only for the explicit sufficient local threshold.

## Proof

### 1. Exact cardinal normalization at the actual corner

Let the original node indices be p,q with p+q even. The corrected cardinal formula and product-to-sum give, at physical angles theta,phi,

   L_pq(cos theta,cos phi)
      =(w_pq/4)*sum_(sigma,tau=+-1) G_n(theta+sigma*p*pi/n,phi+tau*q*pi/m).

Take theta=pi-alpha/n and phi=pi-beta/m. Reflect the indices by

   j=n-p, r=m-q.

Since n+m=2n+1 is odd, j+r is odd. Reflection preserves both endpoint factors and weights. G_n is2*pi-periodic and even in each angular coordinate separately. Consequently the four arguments reduce, with their multiplicities, to

   (j*pi/n+sigma*alpha/n,r*pi/m+tau*beta/m).

The sign (-1)^j is the same for all four copies; it does not depend on sigma or tau. Since G_n=2*(-1)^j*F_jr, this gives the exact identity

   L_pq(z_n)=(e_j*f_r/N)*(-1)^j*sum_(sigma,tau) F_jr(sigma*alpha,tau*beta).

Hence

   lambda_n(z_n)=(1/N)*sum_O e_j*f_r*|sum_(sigma,tau)F_jr(sigma*alpha,tau*beta)|, (3)
   Lambda_c(n)=(4/N)*sum_O e_j*f_r*|F_jr(0,0)|.                        (4)

The finite cosine-polynomial argument proves these identities also at collisions, at endpoints where reflected copies coincide, and where the zero-phase cardinal vanishes. Half weights and repeated copies are both necessary. The sole physical odd-board corner collision(n,m) maps to original node index00; its F_0 value is n, not a formal quotient zero. The zero row r=m,j<n has zero F_0 and remains within (3).

### 2. Regular absolute symmetric Taylor remainder

Remove B={(j,r) in O:r=j+1,j>=2n/3}. On R=O minus B let

   f=(1+cos v)/(cos u-cos v),
   g_u=sin u/(cos u-cos v), g_v=sin v/(cos u-cos v).

The corrected divided-difference calculation gives

   F_jr(alpha,beta)=a*f-(sin alpha/2)*g_u+(sin beta/2)*g_v.             (5)

Every denominator on R stays nonzero along all phase paths with total size<=1/64. In fact, writing L=|j-r| and d=min(j+r,2n+1-j-r), the regular geometry of gated-codex-07 gives

   sin((u+v)/2)>=d/(2m), |sin((u-v)/2)|>=L/(4m), L,d>=1.

Its pointwise coordinate derivative estimates and finite multiplicity sums yield the following bounds, normalized by1/N, with H=1+log m. They hold uniformly along every such path and may be applied to the termwise majorants before integration:

| Regular sum | Bound |
|---|---:|
| sum max_i |f_i| / n | 1152 H |
| sum max_ij |f_ij| / n^2 | 55296 H |
| sum |g_*|, separately for each channel | 24 H |
| sum max_i |(g_*)_i| / n | 216 |
| sum max_ij |(g_*)_ij| / n^2 | 1080 |

Here i,j are ordinary u,v coordinates, so for a phase path v_0=(alpha_0,beta_0), |alpha_0|+|beta_0|=rho, the physical angular speed has L1 norm at most rho/n. Endpoint factors are at most1 and can be retained throughout.

For one such path set

   E_jr(s)=F_jr(s*alpha_0,s*beta_0)-a(s*alpha_0,s*beta_0)*F_jr(0,0), -1<=s<=1.

On R, F_jr(0,0)=f_0. Also E_jr(0)=0, |a'|,|a''|<=rho^2/2 and |a|<=1. Therefore differentiating a(f-f_0) twice bounds its normalized absolute second-derivative sum by

   576*rho^3*H+1152*rho^3*H+55296*rho^2*H.

Indeed sum|f(s)-f_0|/N<=1152*rho*H by the first row and integration. For each sine channel in (5), the three product-rule terms cost at most

   12*rho^3*H+216*rho^2+540*rho^3.

Thus the complete normalized sum of |E_jr''(s)| is at most59000*rho^2*H. This is an absolute derivative bound for the actual signed polynomial remainder before any final absolute value; it is not merely a signed inequality for the primitive. The numerical constant follows even using rho<=1 and H>=1:

   55296+576+1152+2*(12+216+540)=58560<59000.

Symmetric Taylor with E(0)=0 gives

   E(1)+E(-1)=integral_0^1 (1-s)*[E''(s)+E''(-s)] ds.

The total integral weight is1. Pair(+,+) with(-,-) and pair(+,-) with(-,+). After the triangle inequality, the regular contribution is therefore

   (1/N)*sum_R e_j*f_r*|sum_(sigma,tau) E_jr(sigma*alpha,tau*beta)|
      <=118000*rho^2*H.                                               (6)

No condition on the sign of F or its numerator occurs here. In particular the primitive's separate sign-change corrections, linear cusp and rho^(3/2) allowance are absent from (6).

### 3. Removed B family, including the removable endpoint

For r=j+1 write h=n-j, 0<=h<=n/3, and

   x_B=(h*pi-alpha)/n, y_B=(h*pi-beta)/m,
   X_B=(x_B+y_B)/2, T_B=(x_B-y_B)/2.

The exact finite-sum factorization is

   D_n=(-1)^n*[V_n(X_B)*U_m(T_B)+U_n(X_B)*V_n(T_B)],
   U_k(z)=sin(kz)/sin z,
   V_n(z)=cos((2n+1)*z/2)/cos(z/2).

U_k is its k-term finite Fourier sum, so |U_k^(q)|<=k^(q+1), q=0,1,2, globally, including h=0 and every sine collision. On the stated phase radius |X_B|,|T_B|<=1.1. The elementary secant bounds1.25,.625,1 for its zeroth, first and second derivatives, and n+1/2<=5n/4, give

   |V_n|<=5/4, |V_n'|<=2n, |V_n''|<=3n^2.

Each phase derivative of X_B,T_B has magnitude<=1/(2n), and their second derivatives vanish. With r_*=m/n<=3/2, the product-rule coefficient for |D_ij| is

   (n/4)*[3r_*+4r_*^2+(5/4)r_*^3+33/4]<=831n/128.

The corrected cosine term and factor1/2 in F therefore give

   |F_jr,ij|<=4n, |F_jr(0,0)|<=2n,                                  (7)

for all two phase derivatives. These are finite-polynomial bounds, including the endpoint h=0. No positivity hypothesis on B is needed.

For the same E as above, (7) yields |E''(s)|<=5n*rho^2. There are two symmetric pairs and at most n indices in B. Consequently

   (1/N)*sum_B e_j*f_r*|sum_(sigma,tau) E_jr(sigma*alpha,tau*beta)|
      <=10*rho^2.                                                    (8)

### 4. Assemble the cardinal bound and strict local consequence

For each physical odd index,

   sum_four F=4a*F_0+sum_four E.

Since a>0 on this radius, insert (6) and (8) into (3), and use (4):

   lambda_n(z_n)<=a*Lambda_c+118000*rho^2*(1+log m)+10*rho^2.

For m>=3, 1+log m<=2log m and10<=1000log m, proving (1) with237000.

The elementary cosine Taylor inequality gives, on0<=rho<=1/64,

   1-a>=rho^2/10.

For example, 1-cos t>=t^2/2-t^4/24>=(2/5)*t^2 in this range; then alpha^2+beta^2>=rho^2/2. Thus

   lambda_n(z_n)<=Lambda_c-rho^2*[Lambda_c/10-237000*log m].           (9)

This proves strict comparison under (2). To check the stated crude sufficient threshold, put L=log n>=10^7. PD-T157 and pi^2<10 imply Lambda_c>=.4L^2-54. Also log(n+1)<=L+1, so

   .4L^2-54>2370000*(L+1).

Indeed .4L^2>=4000000L on this range, and1630000L>2370054. Therefore (2) holds.

For the physical radius write h_x=1-cos xi,h_y=1-cos eta, with0<=xi,eta<=pi. The elementary cosine chord bound gives xi^2<=pi^2*h_x/2 and eta^2<=pi^2*h_y/2. Thus the inward phases alpha=n*xi,beta=m*eta satisfy

   rho^2<=(pi^2/2)*(n*sqrt(h_x)+m*sqrt(h_y))^2
          <=(pi^2/2)*(n^2+m^2)*(h_x+h_y)
          <=(13*pi^2/8)*n^2*(h_x+h_y)
          <(65/4)*n^2*(h_x+h_y).

If0<h_x+h_y<=2^(-17)/n^2, this is less than65/524288<1/4096=(1/64)^2. Hence0<rho<1/64 and (9) proves strict physical comparison. The exact coordinate relation also gives

   h_x+h_y=(alpha^2/n^2+beta^2/m^2)/2
            +O(alpha^4/n^4+beta^4/m^4),

with an absolute remainder bound from cosine Taylor. This explains the n^(-2) physical scale; the displayed chord argument supplies an actual sufficient radius without relying on an asymptotic approximation.

For even n, x reflection preserves the even checkerboard and maps c to the other nonnode corner; for odd n, y reflection does so. Those reflections permute the cardinal polynomials by uniqueness and preserve inward phase magnitudes. Hence all local statements transport to the second corner. QED.

## Scope and remaining items

The theorem gives an n-uniform scaled corner neighborhood and physical L1 radius2^(-17)/n^2 with an explicit local sufficient threshold. Global localization is supplied separately by gated-codex-11 and is assembled in gated-codex-15.

The huge sufficient local threshold is not a practical finite bridge. No claim here covers every degree17<=n<exp(10^7), or supplies an effective global entry threshold. The round1 slope/energy trial remains an alternative OPEN mechanism; it is not assumed here and has not been refuted.

## Checks, sources and history

Analytic derivation only; no numerical phase or degree scan is a premise. The inherited pointwise derivative constants were checked with their original normalization, rather than transferring only the primitive envelope. The exact reflection identity follows directly from the finite corrected cosine polynomial and includes every endpoint/zero/cardinal collision.

Rules and administrative checkpointaa1883f2fd9a837bb931ce804cb4b210c7475886; scientific source base7d308b10d946b607ae0690454f6c0103690775a4, plus D1 round6/D2 round1 locally checked records. Codex, parent-assigned gpt-6.1-sol xhigh,2026-11-02; runtime metadata not independently exposed. Preregistered gated/d2/r02-contract.md read before development. Supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). No imported external theorem, Git operation, shared-registry edit, future-round execution or direction3 work.

Documentation correction,2026-11-02: the explicit logarithmic lower bound is cited to PD-T157 (proof-attempts-2-codex-02-corner-explicit-leading.md), whose full statement/proof was read. PD-T159 is its corner-product comparison dependency, not the direct source of that displayed lower bound. No mathematical statement or proof changed.


### Documentation correction — 2026-11-02

F3: publication-time review labels are updated; the original proof and claim scopes are unchanged.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Supplementary independent review and required Claude audit are pending at initial publication
> Required Claude audit and supplementary independent review pending at initial publication
