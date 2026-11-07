# E04 restricted-domain complete constant bounds

Provisional PD-T?argmax-bridge-codex-E04-localconstant. Split from the
E04 fixed640 assembly; aliases: box root denominator; seven-eighths
central coefficient. Status: **PROVED developer support**, independent
review required. Paper only, 2026-11-07, requested Sol xhigh; serving
metadata unexposed. Input1045157; refreshed unchanged rules at8b014279.

For x=|alpha|,y=|beta|,r=x+y, put r2=x²+y². The SAME complete signed
constant C∞ of D37 satisfies, with continuous zero-log products:

* On CLOSED x,y<=1/2,r<=1:
  ΔC∞ <= (1/2)x^(3/2)+19r2/24
       +(7/15)x²[1+log(1/x)]+(7/60)y²[3/2+log(1/y)].
* On CLOSED r<=7/8:
  ΔC∞ <= (9/16)x^(3/2)+19r2/24
       +(51/100)x²[1+log(1/x)]+(51/400)y²[3/2+log(1/y)].

Here ΔC∞=C∞(alpha,beta)-C∞(0,0). These are restricted-domain
improvements of accepted D37-constant-wide, not transfers of D10's
half-radius constants or a claim of a quadratic modulus at zero.

## Exact reconstruction of the changed coefficients

Keep D37's entire rho<=1 baseline Δ(C∞−Ec)<=19r2/24, including its
new f4 table on5/4, H cutoff1/4, global derivative atoms and full
endpoint loss. None is changed or needed on a larger domain. In its
central root argument let a=(cosx+cosy)/2,p=|sin alpha|,v=p/2,
tau=v/a,b=2arctan(q/(2a)),theta=2arctan(v/a),q=|sin beta|.
The exact D37 positive-part J majorant and beta translation give

    pi² Ec <=2 integral_0^(pi/2) Z(v,a tan(e/2),e) de
                    +q integral_0^b -log(sin e) de.

Z is nonnegative, separately decreasing in s,e, with zeros/thresholds
handled by its positive part. On either stated domain,
y<=b<=y/a,x<=theta<=x/a,b,theta<=r<=1<pi/2,tau<1.
Split the first integral at min(2theta,pi/2). Enlarge ONLY its
nonnegative elementary majorant2v log(2/e) to2theta<=2. Never extend
Z pastpi/2 and never assert2theta<pi/2. If2theta>=pi/2 the tail is
empty; otherwise the same positive-root substitutions have
lambda<=tau/tan(theta)=(1−tau²)/2<=1/2. The three resulting coefficients
are respectively

    Af=16I4/[pi² sqrt(6a(2−tau))],
    hx=4/(a pi²), hy=1/(a pi²), I4<9/10.

The y-shift uses log(pi/2)<1/2 and the SAME sign-preserving translation.
The accepted integral bound I4<9/10 and these identities are exactly
D37/C01, including root collisions. At x=0 the root integral vanishes;
at y=0 the translated term vanishes. Thus all closed axes are retained.

On the BOX a>=7/8,p<=1/2,tau<=2/7, so6a(2−tau)>=9. With
pi²>197/20,

    Af<96/197<1/2,
    hx<640/1379<7/15, hy<160/1379<7/60.

The last comparisons are192<197 and9600<9653. On whole r<=7/8,
a>=1−r²/4>=207/256,p<=7/8,tau<=112/207. Consequently
6a(2−tau)>=453/64>(21/8)², and

    Af<768/1379<9/16,
    hx<20480/40779<51/100, hy<5120/40779<51/400.

These use12288<12411 and2048000<2079729. Every substituted factor
multiplies a nonnegative expression on x,y<=1, so upper-coefficient
replacement has the correct sign. Adding the unchanged baseline proves
both complete statements.

## Polynomial forms used by the assembly

The accepted elementary inequality sqrt(t)log(1/t)<=3/4 on[0,1]
gives the following upper polynomial coefficients, in the order
Bx*x^(3/2)+By*y^(3/2)+Qx*x²+Qy*y²:

| Domain | Bx | By | Qx | Qy |
| --- | ---: | ---: | ---: | ---: |
|BOX|17/20|7/80|151/120|29/30|
|rho<=7/8|189/200|153/1600|781/600|2359/2400|

Each coefficient follows by Bx=Af+3hx/4,By=3hy/4,
Qx=19/24+hx,Qy=19/24+3hy/2. No finite-n allowance or true-origin
charge is supplied by this support. There was no arithmetic script,
endpoint, scalar, native, phase or numerical integration job. Closest
predecessor and gate/disposition are in ideas/E04-assembly640.md.


## Root adoption —2026-11-07

Root adopts the exact frozen 3684-byte proof (SHA256 5cca41faec1813c675b17d5d633d7157fbc67bb35541fcec038adf707a19084e) after the distinct independent ACCEPT in [independent-checks-E04-assembly640.md](../independent-checks-E04-assembly640.md). Original proof bytes above are preserved. The opening pending-adoption wording is historical. Final Claude audit remains separate; no new numerical or source job was run.
