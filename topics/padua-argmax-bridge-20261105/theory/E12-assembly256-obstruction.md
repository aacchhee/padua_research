# E12 — Current256 near-recipe failure with its negative beta baseline retained

Status: **PROVED scoped PAPER allocation failure**, distinct audit
pending; no global ID. Split from the OPEN E12-assembly256 target.
Requested Sol xhigh, serving metadata unexposed,2026-11-07;
rules5fac9e1. ONE fixed256, no scalar/endpoint/source/script/native/
phase/quadrature/degree/threshold/pack job.

This rejects an explicitly defined UPPER/LOWER-FORMULA comparison.
It is NOT an actual-function or defect counterexample, not a rejection
of min(Uabs,relative), and not a claim that global256 is false. E08's
different old-allocation failure is not substituted for the proof below.

## 1. The exact test retains u and the SUBTRACTED Bbeta

Use E09-assembly384 section2's SAME scalar functions at the ONE
prospectively selected n=256,m=257,L=log256,H=1+L:

    T=(4L²-3L)/pi², ebar=D+Mesh+1/n,
    A4=4/n+40H/(pi*n²), C4=A4+20/n²,
    JN=[(3/2)H+16/5]/n+78/n²,
    kNx=[(19/2)H+(23/3)L+677/10]/n+82/n²,
    kNy=kNx+(17L+27)/n².

All finite allowances used here keep their accepted n>=32,rho<=1/2
guards; the one-sided origin ebar is legal from160. Accepted E11
(final review3407c50d...) supplies the central MAJORANT

    R11(x,y)=kappa*(sin x)^(3/2)/sqrt(a)-Bbeta(a,sin y),
    kappa=4I4/pi²,I4=integral_0^1 sqrt(1-z^4)dz,
    a=(cosx+cosy)/2,
    Bbeta=(4/pi²)integral_0^b[sin(y)/2-a tan(e/2)]
                                   *[-log(sin e)]de,
    b=2atan(sin(y)/(2a)).

The regular upper is -j*u, j>23/250; its additional mixed loss is
EXACTLY0 at a balanced phase. The complete relative upper is

    S-Lambda_c<=R11-u*(T-ebar+A4+rho*JN+j)
                                  +C4+kNx*x+kNy*y. (1)

R11 is an UPPER for true Ec, not its value. At the prospectively
recorded x=y=t=1/6,rho=1/3 set a=cos t,p=sin t,u=1-cos t and

    U=T-ebar+A4+JN/3+j,
    P256=kappa*p^(3/2)/sqrt(a)-Bbeta(a,p)-u*U
                                      +C4+(kNx+kNy)/6. (2)

We prove P256>21389/230400>9/100. Exact u and the negative Bbeta
remain in the TESTED expression. Its failure needs an UPPER on Bbeta;
rejecting a looser upper obtained by first dropping Bbeta would not do.

## 2. Written elementary bounds, with no endpoint evaluation

The atanh series gives

    56/81<log2<842/1215+1/6804<111/160,
    11/2<L<111/20,H<131/20,197/20<pi²<10,pi>3.

After t^5/5 at t=1/3, replacing the remaining odd denominators by7
and summing the geometric powers gives the upper tail1/6804.
Since 4L²-3L increases here,

    T<10656/985<271/25,A4<1/50,JN<3/50,C4>1/64.

The accepted E06 constants give, as already used in E08,
j<8/25+40/197-36/125<1/4. Since ebar>=0,

    U<271/25+1/50+1/50+1/4<45/4,
    0<u<1/72, hence -u*U> -5/32.                  (3)

The last implication remains true if U<0. Combining the literal
positive coefficients,

    kNx=[(103/6)L+386/5]/256+82/256²
           >10297/15360,kNy>=kNx.                 (4)

Also I4>4/5, since sqrt(1-z^4)>1-z^4 on0<z<1. Thus kappa>8/25.
The sine polynomial gives p>215/1296>33/200, sqrt(p)>2/5, and
sqrt(a)<1. Consequently

    kappa*p^(3/2)/sqrt(a)>264/12500>1/50.          (5)

## 3. Bound the ACTUAL subtracted beta integral in the needed direction

Put c0=p/a=tan t,delta=p/2. Its actual endpoint obeys b<=c0, and

    a>71/72,p<t,c0<12/71<17/100,c0>t.

On0<e<b, tan(e/2)>=e/2 and sin e>=e*(1-c0²/6). With
zeta=-log(1-c0²/6), extending the POSITIVE majorant to0<e<c0 gives

    Bbeta<=(4/pi²)integral_0^c0
                       (delta-a*e/2)*[-log e+zeta]de
           =p²/(a*pi²)*[3/2-log c0+zeta].          (6)

This is the SAME exact baseline as(2). Its logarithm is integrable
at0; no entropy sign or generic-E equality is changed. Since
-log(1-s)<=s/(1-s),

    zeta<289/59711<1/200,-log c0<log6<9/5,
    Bbeta<(1/36)*(72/71)*(20/197)*(661/200)
          =26440/2797400<1/100.                   (7)

Here log6<9/5 uses inherited log2<7/10,log3<11/10. The final
comparison is2644000<2797400. No beta monotonicity is assumed.
Inserting(3)--(7) in(2) proves

    P256>1/64+10297/46080+1/50-1/100-5/32
          =21389/230400=9/100+653/230400.          (8)

## 4. Exact scope of the rejected floor-formula allocation

E01/E02's legal middle-band Fh has POSITIVE finite-n losses. At r=1/3
its leading integral is Ih=57997/180000. Dropping its losses bounds
the VALUE OF THAT LOWER FORMULA above:

    Fh(256,1/3)<(539/1936)*Ih
                 =31260383/348480000<9/100.       (9)

The other already legal selected bands Fw and shorter radius-one Ft
have smaller leading integrals143641/540000 and32227/180000, with
positive finite losses. The maximum of THESE middle-band guarantees
therefore also stays below9/100. Nearest/small class formulas cannot
replace the middle class in a universal minimum. An actual admissible
middle-class odd center is J=128,K=129 at n256,m257: both directions
are interior nearpi/2, J+K odd, and these phases remain physical.
Both applicable projections retain their original weights; their
defects are not added.

Thus THIS relative upper and the existing selected-band three-class
floor recipe cannot certify that point. Repairing THIS allocation must
improve its comparison by MORE than653/230400. This is neither an
upper on the actual defect nor a lower on the true required error.
A stronger justified floor, absolute/relative minimum, smaller complete
finite operator or another correlated majorant may escape the result.
No entire-toolkit or global256 failure follows. The main remains OPEN;
actual-corner support is separate. Candidate/test preceded derivation
after root's separate release. No scientific job or numerical call ran.


## Root adoption at reviewed scope —2026-11-07

Root adopts only the stated selected relative/floor-formula allocation failure at256, retainingexactu andsubtractedBbeta, after distinct [E12 corner/frontier ACCEPT](../independent-checks-E12-corner-frontier.md), report21214Bb7436e8f4c5f2d6c1e7c2fc0d7313c1f136648a489cdfd0cee3e8ef71e97df2a. The frozen5627B proof prefixc82eed5a185155cf69177ac21d6b6a016fa9a59a67dfe453a39841fa375b0247 is preserved. No global256 theorem or failure of the new absolute/relative minimum/actual argmax is inferred. All-real-n norm/corner and gate-before-development chronology were checked. Upstream findings remain unwaived; no new finding or numerical/source job occurred. Final Claude audit is separate.
