# PD-N?argmax-bridge-codex-D01-corner — The frozen C07 envelope misses the degree-1000 gate

ID kind: PD-N. Aliases: P4 fully charged reciprocal-sum envelope;
D01 corner bracket; K0_C07 primary-gate obstruction.
Split from: none. Split into: none.

## Statement and definitions

For n=1000, define K0_C07 by the exact real formulas in the frozen
[D01 contract](../code/post_audit_D01_corner/SPEC.md). Then

    K0_C07(1000)>1289/300>4.                              (1)

This is a negative statement about this specified allocation of C07's
derivative majorants. It is not a lower bound on the smallest possible
constant in an actual-function corner inequality.

In detail, m=n+1,tau=m/n,L=log m, and

    R={(j,r):0<=j<=n,0<=r<=m,j+r odd}
                       minus {(j,j+1):2j>=n},
    S=j+r, d=2n+1-S, g=|j-r+j/n|, q=1/6,
    A1=sum_R 1/[(S-q)(g-q)^3],
    A2=sum_R 1/[(S-q)^3(g-q)],
    A3=sum_R 1/[(S-q)^2(g-q)^2],
    G2=sum_R(g-q)^(-2),
    B20=sum_R(S-q)^(-2), C20=sum_R(d-q)^(-2).

All these sums are unweighted, exactly as in C07. Define

    C_f=16tau^3 A1/pi^4+4tau^3(A2+A3)/pi^2,
    H=1+log(2m),
    C_rem=30m^2/(pi^2 n^3)+18mH/(25n^3)
                  +3456mH/(25pi^2 n^3)+8/(nm),
    C_sine=50m G2/(9pi^2 n^2)+m(B20+C20)/(2n^2),
    C_strip=(28/5)[floor(n/2)+1/4]/m,
    K0_C07=C_f+C_rem+C_sine+C_strip-L/3.             (2)

These definitions, rather than a sampled cardinal Hessian, specify the
object being tested.

## Assumptions and status

Exact real arithmetic; the n=1000 odd board and enlarged collision strip
above; elementary pi^2<10 and the exponential power series.

Overall status: **PROVED**, by the elementary rational argument below.
No numerical output is a premise. Distinct review remains separate.
The finite-sample tests and the n=20000 kill outcome have **MEASURED**
status in [the attempt](../attempts/D01-corner.md), not in this claim.

Candidate disposition: **REJECTED: failed**, for the frozen envelope's
primary K0_C07(1000)<=4 target only.

## Negative-result scope

Attempted mechanism: replace C07's coarse allocations for A1/A2/A3 and
the reciprocal sine sums by their finite sums, retaining its derivative
majorants, harmless-term bound and collision Hessian charge as in (2).
Parameter scope of the proved failure: exactly n=1000. No rejection of
sharper phase geometry, weighted regular sums, sharper derivative
majorants, cancellation between contributions, another strip allocation,
or the actual-corner inequality follows.

## Depends on

C07-corner-million-onset sections1–6 for the origin of the allocated
terms; C05-corner-quarterangle-bound sections2,4,5 for the regular
derivative and harmless-term formulas. C02's corrected four-copy
normalization is recalled below. These provide the interpretation of
(2); the numerical lower bound (1) follows directly from its definitions.
No theorem is used below its stated degree floor to establish (1).

## Proof

Both (j,r)=(0,1) and (1,0) belong to R at n=1000. For each of them

    0<S-q<21/25, 0<g-q<21/25.

Indeed S-q=5/6, while g-q is respectively 5/6 and5/6+1/1000.
Each summand in each of A1,A2,A3 at either index therefore exceeds
(25/21)^4>2; the last inequality is exactly

    2*21^4=388962<390625=25^4.

All other summands are positive. Thus A1>4,A2>4,A3>4. Since tau>1
and pi^2<10, the first line of (2) gives

    C_f>(16/100)*4+(4/10)*8=96/25.                (3)

The complete strip charge is

    C_strip=(28/5)(500+1/4)/1001
            =28014/10010>279/100.                 (4)

The positive exponential series, already through degree11, gives

    exp(7)>sum_(k=0)^11 7^k/k!>1001,

so L=log1001<7. For an immediately checkable rational comparison,
the sum in this display is 41438755442/39916800>1001.
Finally C_rem,C_sine>=0. Combining (2)–(4) gives

    K0_C07>96/25+279/100-7/3=1289/300>4.

This proves (1), without floating-point evaluation or a finite
computer-assisted premise.

## Why (2) is the charged C07 budget

This paragraph identifies the tested candidate contract; it does not
extend a frozen theorem's degree domain. With N=nm, C07(3) has

    lambda=(1/N)sum_O e_j f_r |sum_four F_jr|,
    Lambda_c=(4/N)sum_O e_j f_r |F_jr(0,0)|.

The absolute value follows the four reflected copies. The exceptional
first-coordinate mode, endpoint values and initially zero cardinals
are retained. Symmetric coordinate second differences multiply the
regular f majorant C07(7) by 2/(N n^2). Its first three terms, after
P>=pi(S-q)/(2m) and |T|>=pi(g-q)/(2m), give exactly C_f. Its last
four terms are bounded by C_rem, the full displayed C07(13), without
rounding it to1/100.

For the odd sine channels C07(15) has factor1/(2n^2m). Applying
csc^2 T<=(25/9)T^(-2) and
csc^2 P<=pi^2[P^(-2)+Z^(-2)]/4, with the same geometric bounds,
gives precisely C_sine. Thus G2,B20,C20 are sums of a uniform
reciprocal envelope, not the phase-zero csc sum or a Hessian sample.

C07(24) gives (14/5)n rho^2 per collision-strip index after its two
symmetric pairs. The actual B weight is floor(n/2)+1/4: its (n,m)
endpoint has weight1/4, and the remaining floor(n/2) indices have weight
one. Division by N and rho^2<=2r2 give C_strip. Every removed index is
charged. The coefficient represented by (2) is consequently

    C_f+C_rem+C_sine+C_strip=L/3+K0_C07.

## Scope, checks and next obligation

The proved primary failure already ends this frozen trial. No validated
fixed-K upper bound or corner onset is established, and no old theorem,
quantifier or proof is changed. The measured n=20000 kill strengthens
the practical stop decision but is not promoted to a theorem.

If a different allocation is proposed later, it needs its own scope,
gate and proof. Merely evaluating these same sums with more precision
cannot cure (1). Replacing the envelope would require new derivative,
weight, cancellation or strip estimates; that possibility is outside
the present obstruction. The unrounded finite deformation lower bound
for Lambda_c and all new degree-floor checks would then remain separate
obligations. No actual argmax assertion follows here.

2026-11-06; rules/input4cf68980fa0538b53e2aea7174ed6e5782a34908.
Codex mathematical worker, parent-assigned Sol xhigh; serving metadata
unexposed. Provisional ID only; root owns Git and final registration.
