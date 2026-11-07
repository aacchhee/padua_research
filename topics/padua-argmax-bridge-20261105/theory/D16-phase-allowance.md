# PD-T?argmax-bridge-codex-D16-allowance — Phase-dependent absolute near budget

ID kind: PD-T. Aliases: pre-uniformization absolute error; actual-origin
allowance. Split from: D16 prospective onset. Split into: none.

## Statement, definitions and status

For the corrected primitive S_n and TRUE completed model M_infty of D02,
integer n>=32 and rho=|alpha|+|beta|<=1/2, put m=n+1,L=log n,H=1+L,
b=4/pi^2, r=log(5/2)+1/18 and

    D=[(52/pi^2)H+7]/n+10/n^2+20H/(pi*n^2),
    KD=[352H/(3pi)+2/pi]/n,
    G=[(21/5)L+(9/4)log(2m)+1022/15]/m,
    G0=[(28/pi^2)L+111/2+23/pi]/m,
    M=b(2L+2r)/n+[4+b(L+1/n)]/(4n^2-1)
          +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    W=[3log m+log2+2log pi+2]/(pi*m),
    C=D+G+M+14/n+71/n^2,
    K=KD+W+(8+L)/n+4/n^2,
    E0=D+G0+M+14/n+71/n^2.

Then

    |S_n(phase)-M_infty(phase,L)|<=C(n)+K(n)rho,       (1)
    |S_n(0)-M_infty(0,L)|<=E0(n).                    (2)

C,K,E0 are positive and decrease for all real n>=32. Status: **PROVED**
analytic developer result, distinct review pending. Exact real arithmetic
and natural logs. This is not a phase-relative error theorem.

## Dependencies and proof

D08-near-representation(1) is valid n>=32 and bounds the error by
E_D04+E_global+Bmesh+(d/pi)Blog+B6 at the ACTUAL absolute phase.
D04-row-reduction(3), D07-global-outer(2),(4), D07-global-mesh(6), and
D07-endpoint-six-row-allowance(1) supply exactly those quantities.
All retain the unequal n,m meshes, exceptional highest x mode,
weighted collisions, six actual polynomial rows and continuous endpoints.

On the near triangle a<=1, p=sin|alpha|,q=sin|beta|,
P=p+q<=rho and d=(q-p)_+<=P<=rho. Therefore E_D04<=D+KD*rho.
D07's uniform near simplification gives E_global<=G. D08's accepted
|D0|<=4,|Z_n|<=5,|h2(t)+h2(1-t)|<=2r and B0<=b give Bmesh<=M.
The logarithmic mesh cost is <=rho*W. Finally

    B6<=(14+rho*(8+L))/n+(71+4rho)/n^2.

Adding gives (1), without claiming any cancellation between phases.

At the actual origin a=1,p=q=P=0,d=(q-p)_+=0, so no logarithmic
mesh charge or P-dependent row cost remains. D07-global-outer(2) has
Gpar=0, M_A=4/pi^2,V_A=8/pi^2,V_B=23+46/pi,
Q(0,2h)=28/m and C_B<8. Hence its right side is at most

    [4L/pi^2+V_B/2+24L/pi^2+28+16]/m=G0.

The same conservative M remains valid at this actual phase; no value of
U0 or D0 is invented. In particular U0 is the D05 weighted numerator
N_L(0)=N_R(0), not a sine; D0=U0/pi+B0*log pi. We need only its
already accepted absolute bounds, never a claim U0=0. Substitution
in the full D08 component assembly now gives (2).

For monotonicity, D,KD and the final inverse-power terms are positive
sums of (cL+d)/n^j,j>=1 and decrease for L>3. G decreases by the
literal derivative numerator (21/5)(1+1/n)+9/4 minus its numerator,
negative for n>=32. G0's derivative numerator is
(28/pi^2)(1+1/n-L)-111/2-23/pi<0.
W's derivative numerator is3-[3log m+log2+2log pi+2]<0.
For M, (2L+2r)/n decreases. Split its second term into
(4+bL)/(4n^2-1)+b/[n(4n^2-1)]; the latter decreases, and the former
has derivative numerator b(4n^2-1)/n-8n(4+bL)<0 for L>=1.
The third term decreases. With V=5+b(log(n+1/2)+2), its last term
decreases because b(n-1/2)/(n+1/2)-2V<0 (b<1/2,V>5).
This proves every assertion for the complete unbounded range.

## Checks and scope

No numerical premise enters (1)--(2). The current bounded application,
source identities and sole scalar contract are in the D16 idea/attempt.
Full finite relative error remains OPEN; old D11 source and conclusions
are unchanged. Source/rules full SHA8040e0b2c9869a7871ad1825e9b9c746186db084,
2026-11-06, parent-requested Codex Sol xhigh; serving metadata unexposed.


### Supplementary review closure — 2026-11-06

Distinct mathematical reconstruction ACCEPTED this unchanged developer
scope; [independent-checks-D16-budget.md](../independent-checks-D16-budget.md),
report SHA25662d9c92d6f6a48734dcff56da2df8048e8fad6ddc8ff79ad3bae057e3672aa6c.
The preceding pending supplementary-review wording is historical. Exact
review scope, process notes and computational provenance remain in that
report. Final Claude audit is separate; executable instance/source release
is not implied by acceptance of a sufficient mathematical contract.
