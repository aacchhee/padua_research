# E14 — The complete noncorner half-near comparison from320

Status: **PROVED developer PAPER support**, distinct review pending.
Split from E14-assembly320. Requested Sol xhigh, serving metadata
unexposed,2026-11-07; rules5fac9e1. ONE fixed320. No computation,
source, scalar/endpoint/native/phase/degree/pack job.

For EVERY integer n>=320, every actual physical NONCORNER odd-center
chart with x=|alpha|,y=|beta|,r=x+y<=1/2 satisfies

    lambda_n<Lambda_c(n)-1/20000.                    (1)

Only an interior-index projected direction is assigned a floor; every
noncorner odd center has at least one. Actual corners are excluded.
This is not a complete global320 theorem. All original corrected
weights/highest coefficientONE, unequal n,m and collision values remain.

## 1. A lower bound for the EXACT negative beta baseline

Use accepted E11's SAME true Ec and Bbeta, with a=(cosx+cosy)/2,
q=sin y,b=2atan(q/(2a)), and kappa=4I4/pi². On the closed half
diamond a>0 and0<=y<=b<=r<=1/2. Indeed2a<=1+cosy proves b>=y;
the accepted half-angle identity proves b<=r. At y=0 define b=Bbeta=0.

For y>0, convexity of tan on[0,b/2] gives

    tan(e/2)<=(e/b)tan(b/2)=(e/b)*q/(2a),0<=e<=b.

Since sin e<=e and e<1, BOTH factors have the needed nonnegative
signs. Direct integration of the original baseline yields

    Bbeta >=(4/pi²)*(q/2)integral_0^b(1-e/b)*[-log e]de
           =q*b/pi²*[log(1/b)+3/2].                 (2)

The improper logarithm is integrable; the weight vanishes at b.
Now q>=23y/24,b>=y,b<=1/2,pi²<10,log2>69/100 give

    Bbeta>=beta0*y²,beta0=5037/24000=1679/8000>1/5. (3)

The y=0 case is direct. This lower bound is for the EXACT subtracted
term, not an unproved actual-beta monotonicity. It is a routine
consequence of accepted E11, not a new root rearrangement principle.
It supplies the slightly stronger coefficient(3) without selecting a
parameter after a numerical test. E11 therefore gives on this domain

    Ec<=(3/8)x^(3/2)-beta0*y².                     (4)

## 2. Keep the SAME complete finite relative allowance

All functions below are the literal E09-assembly384 section2 functions,
whose COMPONENT guards are n>=32,r<=1/2; one-sided origin is used
only from160. Let L=logn,H=1+L,m=n+1 and

    T=(4L²-3L)/pi²,ebar=D+Mesh+1/n,j>23/250,
    A4=4/n+40H/(pi*n²),C4=A4+20/n²,
    JN=[(3/2)H+16/5]/n+78/n²,
    kNx=[(19/2)H+(23/3)L+677/10]/n+82/n²,
    kNy=kNx+(17L+27)/n²,
    U=T-ebar+A4+r*JN+j.

The accepted SIGNED Tout already contains scalar Rlog; its separate
mesh allowance is r/(2n). No second log/old full mesh is added. The
ordinary, retained, outer, mesh and genuine finite cusp charges remain.
With E(0)>-ebar ONLY as a lower origin bound, exact origin conversion
delta_aE-uE(0) gives

    S-Lambda_c<=Ec-u*U+C4+kNx*x+kNy*y,
    u=1-(cosx+cosy)/2>=(47/192)(x²+y²).             (5)

The last non-strict inequality includes both zero coordinates. It is
the sine/cosine Taylor bound on x,y<=1/2, not a replacement u=r²/8.
The true Lambda_c remains symbolic and ebar is not a global norm.

## 3. ONE320 rational component bounds and their directions

Write320=2^8*(5/4). Positive atanh terms and geometric tails give

    6931/10000<log2<69315/100000,
    2231/10000<log(5/4)<22315/100000,
    57679/10000<L<5769/1000,H<6769/1000.           (6)

For explicit certificates, log2 is between
842/1215+2/15309 and that same sum plus1/78732; log(5/4) is
between488/2187 and that sum plus1/145800. These tails follow by
replacing remaining odd denominators by9 and5 respectively. All
comparisons in(6) are positive-denominator rational inequalities.
Use accepted157/50<pi<22/7,pi²>197/20,hr=log(5/2)+1/18<1.
Direct positive substitutions in the UNCHANGED D,Mesh give

    T>293/25,D<27/200,Mesh<7/400,ebar<249/1600,
    C4<677/50000,kNx<11031/20000,kNy<11056/20000,
    JN>2171/51200>21/500.                         (7)

Here T's lower rational numerator is
567277810036/48400000000>293/25. For D use
[(1040/197)*(6769/1000)+7]/320
+[10+6769/157]/320²<27/200. The leading mesh is bounded by
(41/100)*(2*(5769/1000)+2)/320 and its SAME three positive tails
total<14/320²; their sum is<7/400. No term is omitted. Then
ebar<27/200+7/400+1/320=249/1600.

For C4 its excess over1/80 is<16678/16076800<13/12500.
The kNx numerator is exactly bounded by705963/1280000<11031/20000;
adding db gives56602113/102400000<11056/20000. The JN lower
uses H>27/4 and retains its78/n². These are paper comparisons, no
scalar/degree endpoint evaluation.

At the base, (7),A4>1/80 and j>23/250 imply

    U>23337/2000+(21/500)r.                       (8)

This WHOLE base lower persists for all real n>=320 at fixed r.
Indeed ebar decreases and U increases. To check the latter rather than
assume a mixed direction, H<=n/4 for n>=32. For n>=320,L>5,pi²<10,

    T'>3/n,A4'>-32/(3n²),
    JN'>-3/(8n)-16/(5n²)-156/n³.

Thus for0<=r<=1/2,
(T+A4+rJN)'>(45/16)/n-(184/15)/n²-78/n³>0.
Adding -ebar' only helps. C4,kNx,kNy decrease by their positive
linear-log/inverse-power formulas. Integer Padua objects are never
asserted at noninteger n; these directions concern explicit scalars.

## 4. FRESH320 three-class projected floor

Use the accepted E01/E02 formulas at the SAME actual r, not their
old384 or512 numerical consequences. Put a_r=1-r²/4 and write the
middle-band formula Fh=Ah*a_r-Bh*r. At n320 its exact coefficients are

    Ah=1241317/9680000-679/251200-77392/3768000-97/38400,
    Bh=253869/2420000-35/25120-2000/150720-1/768.

They satisfy

    5123/50000<Ah<1281/12500,0<Bh<4447/50000.

An inspectable rational table bounds Ah's four positive pieces in
units10^-6 by(128235,128236),(2703,2704),(20539,20540),(2526,2527).
Bh's four pieces in units10^-7 lie in
(1049045,1049046),(13933,13934),(132696,132697),(13020,13021).
Addition/subtraction gives the bounds above, hence

    Fh>Lh(r)=5123/50000-4447r/50000-1281r²/50000.  (9)

The nearest/small classes must also be paid. At320
2[n/(n+1)](1/4-1/n)=158/321. On r<=1/2,
eta>(959/1000)a_r-r/2 and p_pi+r<=51/14. Thus

    Fn>(27/200)[(959/1000)a_r-r/2]
       >(11/100)(a_r-r/2),
    Fs=(35/286)(157/160)²*(a_r-r/2)
       >(11/100)(a_r-r/2).

The first factor check is442400>442017. The second-step difference
in Fn is3893a_r/200000-r/80>0 on this closed domain. Their common
lower exceeds Lh: the difference is
377/50000+1697r/50000-94r²/50000>0. Therefore EACH applicable
interior-index projection, hence the full noncorner defect, exceeds Lh.
All three underlying positive-loss floor formulas improve with n at
fixed r, so (9) and its three-class consequence hold for every n>=320.
Original two folded branches/weights and physical eligible directions
are those already proved; no projections are added or domain enlarged.

## 5. Exact anisotropic quadratic optimization and comparison

The prospectively fixed tangent, centered4/25, is
sqrt(x)<=(5/4)x+1/5, from (sqrt(x)-2/5)²>=0. Equations(4),(5)
then give a concave quadratic upper after a legal lower bound for U.

First suppose1/8<=r<=1/2. Equation(8) gives
(47/192)U>1143/400; its exact final cross-product slack is105.
Consequently

    S-Lambda_c<C4+l1*x+l2*y-d1*x²-d2*y²,
    l1=12531/20000,l2=11056/20000,
    d1=1911/800,d2=24539/8000.                     (10)

Here d1 subtracts15/32 from the cosine curvature, d2 ADDS
beta0=1679/8000, l1 adds3/40, and every finite coefficient in(7)
is retained. On x+y=r, maximizing over the ENTIRE line is a valid
upper for the nonnegative closed segment. Its EXACT value is

    -e*r²+f*r+g,
    e=d1*d2/(d1+d2),f=(d2*l1+d1*l2)/(d1+d2),
    g=(l1-l2)²/[4(d1+d2)].

Positive-denominator comparisons give

    e>13429/10000,f<29714/50000,g<1/4000.

Explicitly d1+d2=43649/8000,l1-l2=59/800;
e=468940290/349192000,g=3481/13967680, and
f=l2+1447801/34919200. Hence

    S-Lambda_c<1379/100000+29714r/50000-13429r²/10000.

Subtract this from(9). The lower difference is

    8867/100000-34161r/50000+(8233/6250)r²>1/20000

for ALL real r: completing its square reduces to the exact integer
comparison34161²=1166973921<1167373536=32*8233*4431.

For0<=r<=1/8, use(8) with its nonnegative r term dropped. Both
quadratic curvatures exceed2, so

    S-Lambda_c<677/50000+(627/1000)r-r²<77/1000.

The polynomial increases to r=1/8. Meanwhile Lh decreases there and
Lh(1/8)>9/100. This leaves a gap>13/1000>1/20000. The origin,
both axes, the r=1/8 seam and r=1/2 boundary are all included.
Together with lambda=S-Delta and the legal projection floor, this
proves(1) on the COMPLETE noncorner half-near diamond.

No finite signed T theorem or floor was transferred past its domain.
No beta-axis interpolation, actual smoothness of S, unknown maximizer,
asymptotic finite lower or E(0)>=0 premise was used. The old E12
fixed256 failure remains valid with its exact old recipe. Global320
and all other regions remain separate obligations. No scientific job.
