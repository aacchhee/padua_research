# E01 near frontier — Correlated defect bounds and explicit allocation obstructions

Provisional local results E01-F1/F2 (defect bounds), E01-R1 (near
reduction) and E01-N1 (scoped upper-allocation failure). Root restricts
this paper round to this one theory file; the named claims have separate
statements/statuses below, with no global ID allocation. The lower
GLOBAL-onset target remains OPEN. No aggregate PARTIAL or lower-onset
claim is made from supporting lemmas.

2026-11-06. Rules/input63c70b7c1c226be42a159b29d45de81fdeda22e4;
requested Sol xhigh, serving metadata unexposed. Gate/candidates and
actual paper-only activity are in ../ideas/E01-near-frontier.md and
../attempts/E01-near-frontier.md. Old D37/D39 results are unchanged.

## Exact objects, domains and inherited premises

Use precisely PD-T101/364's corrected finite Padua polynomial kernels,
exceptional highest first-coordinate coefficient ONE, original endpoint
weights and finite-polynomial collision values. Put m=n+1,N=nm,

    rho=|alpha|+|beta|, a_r=1-r^2/4,
    p=22/7>pi, p0=157/50<pi.

An ACTUAL physical odd center satisfies0<=J<=n,0<=K<=m,J+K odd,

    theta=(J*pi+alpha)/n in[0,pi],
    phi=(K*pi+beta)/m in[0,pi].

The exact identity is lambda_n=S_n-Delta_JK, with
Delta_JK>=max(Q_h(J),Q_v(K))>=0. Projections are not added. At
least one center index is interior at every noncorner odd center.
Actual nonnode corners are excluded from every defect-floor consequence.

For d(X,Y)=|X|+|Y|-|X+Y|, C02's full periodic projection has factor
1/(4nm); folding reflected preimages gives physical row factor1/(nm)
for each selected INTERIOR row, with BOTH opposite periodic branches
counted explicitly. Endpoint half weights and polynomial collision
values remain in the full definition; omitted terms are nonnegative.
The common-sign half kernel at regular denominators is

    H(u,v)=A(u,v)/(cosu-cosv),
    A=a_actual*(1+cosv)-(sin alpha/2)*sinu+(sin beta/2)*sinv,
    a_actual=(cos alpha+cos beta)/2>=a_r ifrho<=r,
    (|sin alpha|+|sin beta|)/2<=r/2.                  (1)

The horizontal baseline is STILL1+cosv at its actual fixed second
coordinate. No n,m interchange or fixed-cardinal-sign premise is used.
These are the accepted C02/PD364 identities, not new formula claims.

For either applicable projection let M,L be its adjacent physical and
periodic meshes (m,n vertically; n,m horizontally), and gamma the actual
center-angle distance from the nearest endpoint. They obey M,L>=n,
M/L<=65/64 when n>=64. In a physical row b=l*pi/M the two cosine
targets are z0+/-D, z0=cosgamma*cosb>=0,D=singamma*sinb.
Every chosen periodic cosine strictly between them has opposite
denominator signs. A positive common numerator lower A gives pair
defect at least2A/(D+|x-z0|). Selected denominators are regular.

## E01-F1 — Three radius-dependent floors through pi/4

Status: **PROVED developer analytic support**, distinct review required.
For EVERY integer n>=64 and every REALr with

    rho<=r<=pi/4,                                    (2)

define the following rational functions (r is in radians):

    a=a_r,
    eta_n(r)=a*[1-(4p+r)/n]-r/2,
    Fn(r)=[2eta_n(r)/(p+r)]*[n/(n+1)]*(1/4-1/n),
    Fs(r)=(35/286)*(1-6/n)^2*(a-r/2),
    A0(r)=97a/100-r/2,
    Iw(r)=5369a/15000-7379r/30000,
    Rw(r)=37621a/15000-3r/2,
    Fw(r)=(539/1936)Iw(r)-140A0(r)/(157n)
                       -400Rw(r)/(157n)-800A0(r)/(3n^2).

Then EACH applicable projection is at least

    min(Fn(r),Fs(r),Fw(r)).                          (3)

The individual functions correspond to an exhaustive center-class
proof; they are not floors asserted independently for all center classes.
The minimum in(3) is allowed to be negative at small n. No positive
floor or new global degree is inferred merely from its formula.

### Nearest four index distances: rebuilt geometry

For center-index distance1<=s<=4, choose C02's SAME physical rows
M/4<=l<=M/2 and offsets q=-(s-1),-(s-3),...,s-1, together with the
opposite periodic branch. The parity proof and index ranges depend on
the integer meshes, not on the half-radius bound: l+q>=13,
l+q<=M/2+3<L, and the two branches are distinct. The old displacement
estimate, derived by separating q and l mesh changes, is

    |M(w-b)|<=(s-1)pi+71pi/128+(65/64)|periodic_phase|.

To straddle the two targets, it suffices that

    |physical_phase|+(65/64)|periodic_phase|<57pi/128.

This is newly valid under(2), since its left side is at most
65pi/256<114pi/256. Thus every selected angle lies STRICTLY between
b-t and b+t, where0<t<=(s*pi+r)/M. Here
t<=(4*pi+r)/n<=17*pi/(4n)<pi/4 at n>=64; all angles stay in(0,pi).
Both actual cosine targets vertically, and the fixed periodic baseline
horizontally, are>=-t. Equation(1) therefore gives numerator at least
eta_n(r), which is positive on the full claimed domain. Indeed

    r<11/14, a>663/784, (4p+r)/n<187/896,
    eta_n(r)>194099/702464>1/4.                       (4)

The denominator span is at most2t, so each pair defect is at least
eta_n(r)/t. Count s offsets, two branches and at least M/4-1 rows:

    Q>=[2s eta_n(r)/(s*pi+r)]*(M/L)*(1/4-1/M)>=Fn(r).

The last step uses s/(s*pi+r)>=1/(pi+r), M/L>=n/(n+1),
and the strictly positive factors. Original endpoint weights are retained.

### Remaining small angles: correlate count and numerator

For s>=5, gamma>4*pi/L still holds in the enlarged domain: using
M<=L+1, it follows from L*(pi-r)>4pi, which is implied by
r<=pi/4,L>=64. When gamma<pi/6, choose physical rows
b in[pi/6,pi/3] and C02's two open periodic arcs
(b-gamma,b+gamma) and its reflection. They are disjoint and inside
their half-circles. Both vertical targets and the horizontal fixed
periodic cosine are>=cos(b+gamma)>=cos(pi/3+gamma).
The SAME numerator lower is consequently

    A_gamma=a*[1+cos(pi/3+gamma)]-r/2>0.

Each pair defect is at least2A_gamma/(sqrt3*gamma). The row count is
M/6-1 and the total periodic count is2Lgamma/pi-2. Hence

    Q>=[4/(pi sqrt3)]*(1/6-1/M)*h(gamma),
    h(g)=A_g*(1-c/g), c=pi/L.                         (5)

Do not independently minimize the numerator and the count. On the
CLOSED interval[4pi/L,pi/6], A>0,A'<0,A''<=0, so

    h''=A''(1-c/g)+2A'c/g^2-2Ac/g^3<0.

Thus the minimum is at an endpoint. The upper endpoint gives
h(pi/6)=(a-r/2)*(1-6/L). At the lower endpoint, the1-Lipschitz
cosine inequality gives

    h(4pi/L)>=(3/4)*[a*(3/2-4pi/L)-r/2].

Subtract h(pi/6). The difference is at least

    [1/8+(6-3pi)/L]*a+[1/8-3/L]*r>0,

since the two coefficients exceed or equal1/14 and5/64 at L>=64,
using pi<22/7. The entire SMALL-angle bound therefore keeps the
large-gamma endpoint instead of combining two incompatible worst cases:

    Q>=[4/(pi sqrt3)]*(1/6-1/n)*(1-6/n)*(a-r/2)
      >=(35/286)*(1-6/n)^2*(a-r/2)=Fs(r).            (6)

Here pi<22/7,sqrt3<26/15. Actual gamma=pi/6 can instead use the
middle case; taking the endpoint in this continuous lower estimate
does not omit a seam. Arc counts apply to either shifted parity.

### Middle angles: new shorter positive band

For gamma>=pi/6, the old physical band ending pi/4 need NOT retain
positive numerator at r=pi/4. Use the NEW band

    a0=pi/100, b0=pi/6, c=2, T=4log2,
    C=a-r/2, A(b)=C-a sinb.

Now A(b)>=(a-r)/2>47/1568>0, because a>663/784 andr<11/14.
The fixed-v horizontal argument in(1) remains valid. Both A and
A/sinb are positive decreasing on this band. The same two-branch
layer-cake count and finite physical mesh sums, now on THIS band, give

    Q>=T*I/pi^2-T*A0_exact/(pi*n)
                       -8R_exact/(pi*n)-8A0_exact/(n^2 sin a0),
    I=C*(b0-a0)+a*(cosb0-cosa0),
    A0_exact=C-a sin a0,
    R_exact=C log[tan(b0/2)/tan(a0/2)]-a*(b0-a0).    (7)

Every inverse-n and inverse-square loss is present. This is the exact
C02 positive-band argument, with its domain/numerator/count verified
anew; no old4096 or half-radius quantifier is widened by assertion.

Use sin(pi/100)>3/100,cos(pi/6)>433/500,cosa0<1 and
b0-a0=47pi/300>7379/15000. For the log ratio,
tan(pi/12)=2-sqrt3<27/100, tan(pi/200)>157/10000, so
the ratio is<2700/157<exp3: e>8/3 and80384>72900 suffice.
Thus

    I>Iw(r), A0_exact<A0(r), R_exact<Rw(r).

All upper substitutes are positive because they exceed the positive
exact quantities. C02's positive log2 series gives11/4<T<14/5.
Using p0<pi<p in(7) yields EXACTLY Fw(r) in(3), with correct signs.
The nearest, small and middle cases exhaust both applicable projections,
including both parities, physical edge classes and signed phases. QED.

### Uniform larger-radius consequence

For EVERY integer n>=512 and ACTUALrho<=pi/4, each applicable
projection, and therefore every noncorner full defect, is STRICTLY
greater than1/200. This consequence is **PROVED developer support**.

Indeed(4),p+r<4,n/(n+1)>1/2 and1/4-1/n>1/8 giveFn>1/128.
Also a-r/2>355/784>1/4, (1-6/n)^2>1/2 and35/286>1/10 give
Fs>1/80. For the middle formula, on the full radius domain

    Iw>1286915/11760000>1/10, A0<1, Rw<3.

Since539/1936>1/4,1340/157<9 and800/3<267,

    Fw>1/40-9/n-267/n^2.

At512 the two losses sum to4875/262144<1/50, since
243750<262144. They decrease thereafter, proving Fw>1/200.
Taking the three-class minimum proves the consequence. Actual corners
remain excluded; no floor is applied merely because a proxy intersects
the actual radius domain.

## E01-F2 — Stronger half-radius cap2 and the fixed768 floor

Status: **PROVED developer analytic support**, distinct review required.
For n>=64,rho<=r<=1/2, keep Fn and Fs above but use the larger
positive band[pi/100,pi/4]. Its positivity follows from
a>=15/16,sin(pi/4)<11/15 andr<=1/2. Define

    Ih(r)=2303a/5000-471r/1250,
    Rh(r)=4837a/1875-5r/3,
    Fh(r)=(539/1936)Ih(r)-140A0(r)/(157n)
                       -400Rh(r)/(157n)-800A0(r)/(3n^2).

Then each applicable projection is at least min(Fn,Fs,Fh).
Proof: b0-a0=6pi/25,cos(pi/4)>707/1000,cosa0<1 give I>Ih;
the log ratio is<10/3 by C02's explicit exponential series, giving
R_exact<Rh. The A0 and T bounds are unchanged. Apply the complete
finite formula(7) on this band. This retains r in every main/loss
term, rather than substituting r=1/2 before the final comparison.

All three bounds are increasing in n at fixed r. No monotonicity in r
is claimed for Fh at every small n: losses and the main term change
together. For a uniform floor choose r=1/2 directly in the theorem,
which is permitted for EVERY actualrho<=1/2. At that choice,

    Ih=19473/80000, A0=211/320, Rh=9511/6000.

The main term539Ih/1936>27/400. The total inverse-n coefficient
140A0/157+400Rh/157 is<19/4; the inverse-square coefficient is
1055/6<176. At the ONE root-proposed base n=768,

    (19/4)/768+176/768^2=239/36864<3/400,

because95600<110592. Hence Fh(1/2)>3/50 at768 and all larger n.
For nearest centers t<(4pi+1/2)/768<1/45, so the complete D37
2/3-numerator count givesFn>56/663>3/50. The new small-angle
bound satisfiesFs>=35*841*11/(286*1024*16)>3/50 already from64;
the integer comparison is16189250>14057472. Therefore

    Delta>3/50 for EVERYn>=768, ACTUALrho<=1/2,
                            at every NONCORNER odd center. (8)

This is a lower-domain improvement of a support lemma, not a positive
near upper gate or global onset768. The exact phase-dependent functions
remain available when a uniform floor does not close the upper budget.

## E01-R1 — Symbolic coupled near criterion, without a sampled maximum

Status: **PROVED analytic sufficient reduction**; its fixed512/768
positivity target remains OPEN. Use accepted D35 onrho<=1/2 and D16
actual-origin E0. Write L=logn,H=1+L,

    T=(4L^2-3L)/pi^2, V=T-E0,
    An=22/n+142/n^2+40H/(pi*n^2), Bn=20/n^2,
    CN=An+Bn,
    K35=[8H+(39/2)L+286/3]/n+4/n^2.

The unrelaxed D35 proof gives a_actual*An+Bn in place of CN. The
joint helper independently identified the same bookkeeping; this
restoration itself needs no new operator estimate. Its separate6rho/n
improvement requires its own completed theorem/review and is not assumed
in the accepted-D35 reduction here.

For n>=512,V>0 by PAPER bounds, not a scalar preview. At512,
6<L<63/10,H<8,pi^2<10 implyT>63/5. The SAME D37 coarse
E0 components, rechecked at512, give

    D<479/(9n)+190/(3n^2)<1/5,
    G0<1529/[18(n+1)]<1/5,
    Mesh<17/(2n)+14/n^2<1/50,
    14/n+71/n^2<15/n<1/25.

The rational comparisons are1229090<2359296,7645<9234,
436600<524288 and375<512. ThusE0<23/50<1/2 andV>121/10;
accepted T-increase/E0-decrease preserves positivity for alln>=512.

Let c0=47/192, bx=77/96,by=1/12 and

    qx*=c0*(V+An)-89/72, qy*=c0*(V+An)-23/24,
    Pn(x,y)=CN+bx*x^(3/2)+by*y^(3/2)
                         -qx* x^2-qy* y^2+K35*(x+y).

For ACTUAL x=|alpha|,y=|beta|,rho=x+y<=1/2,

    S_n(alpha,beta)-S_n(0)<=Pn(x,y).                 (9)

Proof: the model has loss-u*T; D35 pays +uE0, so combine FIRST
to-uV. Restore a_actual*An, then use u>=c0(x²+y²) and
a_actual<=1-c0(x²+y²). D22's proved fractional/logarithmic envelope
gives precisely(9). No positive-error origin is substituted for the
true symbolic S_n(0)=Lambda_c. Fractional/log terms have not been
discarded as purely quadratic near zero.

For n>=512 put

    Dn(r)=max(1/20,min(Fn(r),Fs(r),Fh(r))), r<=1/2.

The baseline1/20 is accepted D29 on its original guarded n>=512 domain.
A sufficient NONCORNER near condition at a fixedN>=512 is

    D_N(x+y)-P_N(x,y)>0 for ALLx,y>=0,x+y<=1/2.      (10)

It includes axes, zero phases and the closed seam. At every fixed phase,
Dn increases with n. Also

    Pn=Bn+[1-c0(x²+y²)]An-c0V(x²+y²)
                    +fractional/quadratic constants+K35*rho

decreases with n: An,Bn,K35 decrease, V increases, and
1-c0(x²+y²)>0. Thus(10), IF proved, transfers to EVERY integern>=N.
No unsupported monotonicity of the collected V+An is needed, and no
positive-q domain is needed for this direct polynomial inequality.

Setting z=sqrtx,w=sqrty turns(10) into a fixed polynomial/rational
positivity problem on the CLOSED quarter disk z²+w²<=1/2. All floor
pieces are rational in rho,n; Fn's denominator p+rho is positive.
Min/max branches must be validated, not guessed from samples. A future
exact finite proof could cover that domain with rational boxes, retaining
tangent cells and excluding only strictly empty cells, and bound ALL
required polynomial branches. That is a proposal, not source or a run.

## E01-N1 — Exact unchanged-allocation failures at512

Status: **PROVED scoped paper obstructions**. These concern the named
upper-envelope allocations, NOT a lower bound on actual S/lambda and
NOT a refutation of global512 or any other analytic route.

At n512, L=9log2 with2/3<log2<7/10. SinceE0>0,pi>3,

    V<T<391/25, K35>805/1536>1/2, CN>11/256.

Consequently the old D22/D37 qx,qy are<3; if either is nonpositive,
the old radical formula is inadmissible anyway. At the fixed phase
x=y=1/12 (ACTUALrho=1/6), the SAME old polynomial is strictly above

    CN+K35/6-(qx+qy)/144 >11/256+1/24=65/768.

Thus constraining its supremum from a quadrant to the actual half
diamond alone cannot close a1/20,3/50 or1/16 uniform-floor comparison.
65/768 also exceeds1617/24200, the old cap2 limiting uniform middle
floor. This says nothing against a legitimately stronger/correlated
floor, a sharper constant or a new finite increment estimate.

The distinct auditor independently checked that trial and supplied a
stronger fixed trialx=y=1/16. Its exact old polynomial is

    CN+K35/8+413/18432-47V/24576
                         >186119/1843200>1/10.

Even removing CN completely leaves106919/1843200>1/20, so cancelling
only a phase-independent constant with unchanged K35 cannot fix the
old1/20 allocation. These two rational trials are paper kills, not a
phase search or numerical evaluation of the primitive.

## Ranked next paper routes and the ONE prospective768 assembly

1. A stronger COMPLETE finite relative increment or sharper actual
   constant majorant is needed; do not rely on phase-zero equality to
   remove a nonvanishing bound. The assigned joint helper's frozen
   statement reports exactly-6rho/n-uAn versus D35 onrho<=1/2;
   distinct review/adoption remains its own obligation. It does not
   establish the full stalled D13 vanishing joint remainder.
2. Use the proved phase-dependent half-radius floors when a uniform
   floor wastes their larger small-rho numerator. The small-angle
   concavity proof avoids a real mismatch of independent worst cases.
3. The rebuilt larger-radius floor permits a LEGITIMATE new near/far
   seam R=pi/4, but only with a matching upper comparison and corner
   theorem. The original band cannot be silently extended. On the
   actual annulus1/2<=rho<=pi/4, use D37's radius-one constant and
   COMPLETE wide CW/KW allowance, not the half-radius D35 theorem.
4. Restoring a-times constants is safe but quantitatively limited;
   constrained optimization alone is already killed at512 above.

Root prospectively selected ONE next baseN768, not a threshold sequence.
The symbolic next route is: prove(10) onrho<=1/2; on the annulus use
the larger-radius floor and the D37 wide model bound with

    cR=91/384, qRx=cR*V-53/40, qRy=cR*V-119/120,
    UW=CW+x^(3/2)+(1/10)y^(3/2)-qRx*x²-qRy*y²+KW*rho.

Here u>=cR*(x²+y²) follows fromrho<=pi/4,pi²<10 and the alternating
cosine bound. Require min(Fn,Fs,Fw)-UW>0 throughout that ACTUAL
closed annulus. Its truth at768 is OPEN; the uniform1/200 consequence
alone is not asserted sufficient. Every actual corner additionally
requires the separately reviewed lower-degree D16 corner proof.

For FARrho>=pi/4 keep D37's fixed eta1/2 and all charges. On its
x,y<=1/2 box the corresponding gate becomes

    pi/8-CW-Psi(1,qBx,KW+1/2)-Psi(1/10,qBy,KW+1/2)>0,

with unchanged qBx=(47/192)V-53/40,qBy=(47/192)V-119/120.
The two large-coordinate gates GX/GY and outer GO are still required.
Moving the seam changes ONLY the justified constraint penalty; no floor
is applied to an outer proxy or an actual corner. The old512 wide
polynomial failure onrho1/2 is not cured by changing eta: its multiplier
adds zero at that seam. The new partition is a different matched proof,
not a reinterpretation of that failed allocation.

At768,L>13/2 fromlog3>1,log2>69/100, whileL<7,H<8.
ThusT>299/20,E0<1/2,V>289/20. D37's wide KW is<2/5.
Consequently qLx>(11/48)*(289/20)-53/40=1907/960>19/10,
qLy is larger, and3/(2sqrt2)+KW<15/14+2/5<19/10.
The old far radical/tail domains can therefore be rebuilt at this
new base by paper, rather than borrowing the1024 checks. Positivity
of the near/annulus/far/outer budgets is STILL OPEN.

Cheapest NEXT task: independent paper audit of the new floor geometry,
concavity, lattice-loss signs, domains and this matched768 reduction.
Only if a complete useful reduction survives should one prepare a
fixed768 exact polynomial/scalar source/SPEC, with complete first-failure
retention and distinct prerelease audit/publication/root release before
any endpoint job. This round creates no source and releases no execution.
No new finite degree, lower analytic onset or all-degree result is claimed.


## Root adoption after distinct focused audit —2026-11-06

Root adopts the reviewed radius-dependent floor formulas and their exact domains: EACH applicable noncorner projection/full defect >1/200 for EVERY n>=512 under ACTUAL rho<=pi/4; half-radius defect >3/50 for EVERY n>=768. The coupled near positivity criterion is a PROVED sufficient reduction, whose fixed768 positivity remains OPEN. Scoped old512 allocation barriers concern only their majorants. No lower global onset is inferred.

Distinct Astra xhigh [frontier audit](../independent-checks-E01-frontier.md),
SHA256 a0853a1e9675bcb841348edb2aaa8ae5a3c8776e2bced63a5c6326da27665db3,
accepts the unchanged reviewed prefix cc8e328405706f6cc5a5ea3fe8122818fb59482c8ac4841e0b6036252b775f11.
No numerical/source/native/pack job occurred. Global onset remains1024;
974 finite degrees remain OPEN. Final Claude review is separate.
