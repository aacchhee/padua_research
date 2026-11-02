# PD-T?argmax-alln-gated-codex-13 — Exact physical corner variation and an aggregate radius reduction

ID kind: PD-T.
Aliases: direction2 round1; canonical nonnode corner derivatives; zero-cardinal correction; weighted-gradient corner radius.
Split from: supporting local-corner obligation for PD-T099/P3.
Split into: none. Uniform slope and energy estimates remain OPEN obligations outside the proved statement.

## Statement

For every integer n>=2 put m=n+1 and use precisely the even-checkerboard nodes, positive weights and corrected cardinal polynomials of PD-T101. Let c=(-1,-1), a_j=cos(j*pi/n), b_k=cos(k*pi/m), tau_j=(-1)^(n+j), and w_jk=2*epsilon_j*eta_k/(n*m). Define Z={(j,0): j>0 even}, and let I be all checkerboard indices except Z and (0,0).

The following statements hold in exact arithmetic.

1. Exactly the cardinals indexed by Z vanish at c. At the removable index (0,0),

   L_00(c)=(-1)^n/m,
   (L_00,x(c),L_00,y(c))=-(-1)^n*((2n^2+1)/(6m),(2n+1)/6).

2. For every index other than (0,0), put d=b_k-a_j, C=1-b_k. This d is nonzero. Then

   L_jk(c)=2*w_jk*tau_j*C/d,

   L_jk,x(c)=2*w_jk*tau_j*[-n^2*C/(2d)+n*(a_j*b_k-1)/d^2-C*a_j/d^2+2C*(1-a_j^2)/d^3],

   L_jk,y(c)=2*w_jk*tau_j*[-m^2*C/(2d)+n*(a_j*b_k-1)/d^2+C*(1+2b_k)/d^2+2C*(1-b_k^2)/d^3].

   On I the sign is tau_j*sign(m*j-n*k), equivalently tau_j for j>=k and -tau_j for j<k. On Z both derivatives equal -2*w_j0*tau_j*n/(1-a_j).

3. Write A_n=D_(1,0)lambda_n(c), B_n=D_(0,1)lambda_n(c). For all s,t>=0,

   D_(s,t)lambda_n(c)=s*A_n+t*B_n.                                      (1)

   In particular, the inward derivative is linear on the whole inward quadrant, including the contribution from initially zero cardinals. Set V_jk=|L_jk(c)| on I and let q_x,q_y be the bracket expressions in part2 divided by C/d. Then the exact slope reduction is

   A_n=-(n^2+2)/(6m)+sum_I V_jk*q_x(j,k),
   B_n=-(n+2)/6+sum_I V_jk*q_y(j,k).                                  (2)

   The total absolute zero-cardinal contribution to each axis is exactly (n-1)/6.

4. Put Lambda_n=max_[−1,1]^2 lambda_n and

   W_n=sum_(L_jk(c)!=0) [L_jk,x(c)^2+L_jk,y(c)^2]/|L_jk(c)|.

   For every h_x,h_y>=0 with c+h in the physical square, H=h_x+h_y satisfies

   lambda_n(c+h)<=Lambda_c+A_n*h_x+B_n*h_y+(W_n/2)*H^2
                 +Lambda_n*[exp(n^2*H)-1-n^2*H].                     (3)

All four parts are algebraic identities or inequalities. No universal negativity, bounded normalized energy, uniform corner radius or all-degree argmax conclusion is asserted.

## Definitions and assumptions

All derivatives in this record are physical x,y derivatives. The one-sided directional derivative is the limit along c+u(s,t), u down to0. Lambda_c=lambda_n(c). Endpoint factors epsilon_j,eta_k are1/2 at the appropriate mesh endpoints and1 elsewhere. Cardial values and derivatives are those of finite polynomials, including all removable values.

## Status by part

Overall status: **PROVED**, by the analytic proof below. Supplementary independent review and required Claude audit are pending.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Exact mask, values, gradients and slope reduction | PROVED | Corrected polynomial kernel and quotient expansion with separate removable index |
| Aggregate upper model (3) | PROVED | Locally derived Lobatto endpoint functional bound and scalar inequality |

Candidate disposition: retained quantitative variant of original P3 / Claude-02 / fallback-04. No historical novelty or transferred external-source theorem is claimed.

## Depends on

PD-T101: exact corrected coefficient kernel, positive weights, cardinality and unisolvence. Elementary finite sums, polynomial interpolation, cosine identities and the Chebyshev differential equation, derived from T_n(cos theta)=cos(n theta), are used below. The upper model itself does not require direction1. Its proposed application uses gated-codex-02 and PD-T159 to bound Lambda_n/Lambda_c, and gated-codex-11 to localize large-degree maximizers.

## Proof

### Values and gradients, retaining the removable index

Let G_n(u,v) be the corrected cosine kernel: the rhombus cosine polynomial has its exceptional x mode (n,0) reduced from coefficient2 to1. Product-to-sum gives

   L_jk(cos theta,cos phi)=w_jk/4 * sum_(sigma,eta=+-1) G_n(theta+sigma*j*pi/n,phi+eta*k*pi/m).

At theta=phi=pi the reflected copies agree. On an odd periodic mesh u=J*pi/n+xi, v=K*pi/m+zeta, J+K odd, the elementary divided difference P_n=T_(n+1)+T_n gives

   G_n(u,v)/(2*(-1)^J)
     = {[(cos(n*xi)+cos(m*zeta))/2]*(1+cos v)
           -[sin(n*xi)/2]*sin u+[sin(m*zeta)/2]*sin v}
       /(cos u-cos v).                                                (4)

This follows by writing P_n(cos u)=(-1)^J[cos(n*xi)*(1+cos u)-sin(n*xi)*sin u], the analogous expression at v, and subtracting the corrected cos(nu) term. It is an identity off collisions; the original polynomial supplies collision values.

At c use J=n+j, K=m+k, so cos u=-a_j, cos v=-b_k. Coprimality shows a_j=b_k only if (j,k)=(0,0) or (n,m); the latter is outside the even checkerboard. Thus every index except00 admits regular differentiation in (4). Its value is the asserted 2*tau_j*C/d. Differentiating twice in xi at zero, its half-kernel second derivative is

   -n^2*C/(2d)+n*(a_j*b_k-1)/d^2-C*a_j/d^2+2C*(1-a_j^2)/d^3.

Differentiation twice in zeta gives the analogous displayed y formula. For completeness, the numerator derivatives for xi are N_0=C, N'_0=n*sin(j*pi/n)/2, N''_0=-n^2*C/2+n*a_j; denominator derivatives are d, sin(j*pi/n), a_j. For zeta they are N'_0=(1-m/2)*sin(k*pi/m), N''_0=-m^2*C/2-n*b_k; denominator derivatives are d,-sin(k*pi/m),-b_k. These substitutions prove the two formulas directly. Reflection leaves the second derivatives unchanged. Since x=-cos xi=-1+xi^2/2+O(xi^4), the physical derivative is exactly the second angle derivative, with no extra scaling factor.

At00 evaluate the corrected coefficient kernel directly. Summing over the b modes at fixed a shows its corner coefficient totals are tau_j times1 at a=0,n and times2 at1<=a<n. Thus G_n(pi,pi)=2n*(-1)^n and its second u derivative is

   -(-1)^n*[2*sum_(a=1)^(n-1) a^2+n^2]
      =-(-1)^n*n*(2n^2+1)/3.

For each b>=1, the a-mode sum gives coefficient2*(-1)^n, so its second v derivative is -2*(-1)^n*sum_(b=1)^n b^2=-(-1)^n*n*m*(2n+1)/3. Multiplication by w_00=1/(2nm) proves the three removable formulas.

Now C=0 exactly when k=0. The00 exception was handled above; all other such indices vanish, and no other cardinal vanishes. Since cosine decreases strictly on [0,pi], sign d=sign(m*j-n*k). On the even checkerboard outside00 this is positive for j>=k and negative for j<k: m*j-n*k=n*(j-k)+j, and its possible endpoint equality(n,m) is excluded. The zero-row gradient formulas follow by substituting b_k=1,C=0 in part2.

### Zero contributions and inward linearity

For any finite absolute-polynomial sum, directional differentiation gives

   D_v lambda(c)=sum_(L(c)!=0) sign(L(c))*gradient L(c).v
                   +sum_(L(c)=0)|gradient L(c).v|.

Each zero gradient has equal x and y components. Therefore its absolute directional contribution is 2*w_j0*n*(s+t)/(1-a_j) for s,t>=0, proving (1).

The zero contribution to either axis is

   Z_n=(2/m)*sum_(j>0 even) epsilon_j/(1-cos(j*pi/n))
       =(1/m)*sum_(r=1)^floor(n/2) epsilon_(2r)*csc^2(r*pi/n)
       =(n^2-1)/(6m)=(n-1)/6.

Here the elementary finite identity sum_(r=1)^(n-1)csc^2(r*pi/n)=(n^2-1)/3 follows by logarithmically differentiating the finite sine product for sin(nz): sum_(r=0)^(n-1)csc^2(z+r*pi/n)=n^2*csc^2(nz). Subtract the r0 term and let z->0, using csc^2 z=z^(-2)+1/3+O(z^2). The finite product itself follows immediately by factoring the n roots of unity in exp(2iz). Pair r with n-r, retaining a half weight at r=n/2 when n is even. Combining Z_n with the sign-adjusted00 gradients gives (2).

### Endpoint derivative bound derived directly from polynomial roots

Let ell_i be the univariate Lagrange polynomial at t_i=cos(i*pi/n), i=0,...,n, ordered decreasingly. For 1<=r<=n,

   sign ell_i^(r)(-1)=(-1)^(n+r+i),
   sum_i |ell_i^(r)(-1)|=T_n^(r)(1).                                  (5)

To see the sign, for i<n factor out x+1 from ell_i. All remaining roots exceed-1, so its coefficients in powers of x+1 alternate in sign after the linear coefficient. The denominator product has sign(-1)^i, giving the stated sign at every nonzero derivative. For i=n all n roots exceed-1, giving sign(-1)^r, which agrees. Since T_n(t_i)=(-1)^i, differentiating its Lagrange expansion proves the equality in (5). For r=0 the same norm is1.

Differentiating (1-x^2)T_n''-x*T_n'+n^2*T_n=0 at x=1 gives

   (2r-1)*T_n^(r)(1)=[n^2-(r-1)^2]*T_n^(r-1)(1),

hence 0<=T_n^(r)(1)<=n^(2r). Tensor interpolation at the two Lobatto meshes implies, for every polynomial p of degree<=n in each variable,

   |partial_x^r partial_y^s p(c)|<=n^(2r+2s)*||p||_infinity.

For each r,s choose signs sigma_B to agree with the mixed derivatives of the Padua cardinals at c and apply this bound to p=sum_B sigma_B*L_B. Its supremum norm is at most Lambda_n. Consequently

   sum_B |partial_x^r partial_y^s L_B(c)|<=n^(2r+2s)*Lambda_n.           (6)

No external Markov or endpoint theorem is imported into this derivation.

### Aggregate Taylor inequality

Write L_B(c+h)=l_B+g_B.h+R_B. The exact finite Taylor expansion and (6) give

   sum_B |R_B|<=Lambda_n*[exp(n^2*H)-1-n^2*H].                         (7)

For l_B!=0 the elementary inequality |z|<=(z^2+l_B^2)/(2*|l_B|), applied to z=l_B+g_B.h, gives

   |l_B+g_B.h|<=|l_B|+sign(l_B)*g_B.h+(g_B.h)^2/(2*|l_B|).

For l_B=0 use |g_B.h| directly. Apply the triangle inequality only to R_B, sum, use (1), and bound (g_B.h)^2<=H^2*(g_B,x^2+g_B,y^2). This proves (3) even if initially nonzero cardinals change sign inside the neighborhood. No termwise sign-stability assumption is needed. QED.

## Scope and next falsifiable lemma

Equation (3) isolates a quantitatively compatible physical radius mechanism. Suppose constants a>0,b>=0,K>0 and N exist such that for n>=N,

   A_n,B_n<=-a*n^2*Lambda_c,
   W_n<=b*n^4*Lambda_c,
   Lambda_n<=K*Lambda_c.                                               (8)

Then kappa=min(1,a/(b+e*K)) gives, for 0<H<=kappa/n^2,

   lambda_n(c+h)<=Lambda_c-(a/2)*n^2*Lambda_c*H<Lambda_c.

Indeed exp(z)-1-z<=e*z^2/2 for0<=z<=1. This is an implication with explicit hypotheses, not a claim that (8) has been proved. Direction1 gives the last inequality eventually (indeed Lambda_n/Lambda_c<=1+O(1/log n)); its threshold and the finite bridge remain separate. The first two uniform inequalities are OPEN. A useful exact next lemma is A_n,B_n<=-n^2*Lambda_c/8 and W_n<=n^4*Lambda_c for every n>=2, or a proved eventual version with explicit constants. The constants are trial bounds, not asserted theorems.

Unlike a raw coefficient bound of order n^6, (3) has the scale needed to match gated-codex-11. Individual gradient/value ratios need not be bounded by O(n^2), and neither fixed-n slope negativity nor the numerical weighted-energy screen proves (8). The unknown finite bridge prevents an all-n conclusion even after an eventual local theorem.

## Checks, sources and history

The proof is analytic; numerical screens are supplementary and recorded separately by the assigned screen worker in gated/d2/r01-screen.md. No numerical output is a premise. The derivative formulas were communicated to that worker for comparison against the independent corrected coefficient-matrix evaluator. Required Claude audit and supplementary independent mathematical review remain pending.

Source base7d308b10d946b607ae0690454f6c0103690775a4; round input checkpointaa1883f2fd9a837bb931ce804cb4b210c7475886. Rules AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md were read from that checkpoint. Codex, parent-assigned gpt-6.1-sol xhigh,2026-11-02; actual runtime metadata not independently exposed. Bounded direction2 round1 work only. No external 1-D source theorem, Git operation, shared registry change, direction3 development or future-round execution.
