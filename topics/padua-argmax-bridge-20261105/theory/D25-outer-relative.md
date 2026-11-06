# PD-T?argmax-bridge-codex-D25-outer — Origin-relative regular outer error

ID kind: PD-T. Aliases: actual shifted-cell outer increment; root-free
small-phase alternative; weighted-profile BV translation.
Split from: D13's full finite relative remainder, which remains OPEN.
Split into: none. This is one substantive supporting operator theorem.

## Statement and exact operator

Let integer n>=32,m=n+1,L=log n,h=pi/m and take alpha,beta>=0 with
rho=alpha+beta<=1/2. Put

    a=(cos alpha+cos beta)/2, p=sin alpha,q=sin beta,
    d=(q−p)_+, ephase=alpha+beta, delta=alpha−beta,
    ce=cos(ephase/2), cd=cos(delta/2), a=ce*cd,
    t=beta/pi, v_L(z)=z,v_R(z)=2pi−z.

Use N1's unchanged weighted periodic Phi0, with Phi0(integer)=1, and
the actual corrected-kernel profile of D05/D07:

    C(v)=(p−q−2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4,
    I(C,D,v)=integral_0^pi
       (|C cot x+D cot(x+v)|−|C cot x|−|D cot(x+v)|)dx,
    N_s(z)=ce Phi0(1/2+(alpha−beta+v_s(z))/(2pi))
                 +cd Phi0(1/2+(alpha+beta−v_s(z))/(2pi)),
    U0=N_L(0)=N_R(0),
    A(v)=2(|C(v)|+|D(v)|)/pi,
    B(v_s(z))=N_s(z)/(2sin(z/2))+I(C(v_s(z)),D(v_s(z)),v_s(z))/pi,
    F_s(L,z)=A(v_s(z))*L+B(v_s(z))
          −[U0+(4a/pi)(L+log z)]/z−(d/pi)log(pi−z).

The bounded cancellation integral has the ordinary meaning; finitely
many pole values do not change it. All periodic Phi products use their
weighted continuous values, not separately unweighted singular limits.
The endpoints of F are used only by their integrable/continuous
regularized conventions from D05/D07. Define

    Q_tau[f]=(1/m)sum_(k=2)^(m−2) f(h(k+tau))
                                      −(1/pi)integral_0^pi f(z)dz,
    Eout(phi)=Q_t[F_L(phi)]+Q_(1−t)[F_R(phi)].        (1)

This is EXACTLY K_fixed−G_n in D07-global-outer, with its fixed six
actual polynomial rows and all singular reference sums cancelled.
Its origin Eout(0) uses the SAME n,m and offsets0,1. Then

    |Eout(phi)−a Eout(0)|
                    <=rho[(35/2)log n+75]/n.        (2)

The coefficient on the right decreases for all real n>=32. Signed
phases use the existing separate-absolute-phase convention; (2) holds
on the entire closed signed near diamond, both axes and both parities.
Overall status: **PROVED**, analytic developer theorem; distinct review
required. No numerical premise or new model term occurs.

## Dependencies and first exact subtraction

D05-outer-profile-variation and D07-global-outer supply the exact
profiles, row labels and centered-cell geometry. C06-far-compact-error
sections1--2 and N1-round6-regular-variation supply the weighted profile
derivative bounds and the generic cancellation formulas used below.
Their explicit full-domain scalar identities, not C06's finite onset,
are the premises. N1-regularized-pole supplies periodicity, symmetry,
sup|Phi0|<=4 and Lip(Phi0)<=12. No D22 conclusion is needed in this
proof; D22 is the intended later consumer. D13's full remainder stays
OPEN because the other complete row increments are not (2).

At zero phase F_L=F_R=:F0. Put W_s=F_s(phi)−aF0. Linearity gives

    Eout(phi)−a Eout(0)=Q_t[W_L]+Q_(1−t)[W_R]+Shift,
    Shift=(a/m)sum_(k=2)^(m−2)
       [F0(h(k+t))+F0(h(k+1−t))−F0(hk)−F0(h(k+1))]. (3)

The origin-integral terms cancel in Shift exactly. The finite shift
does not vanish by symmetry and is estimated in section5.

Use the ACTUAL centered cells of width h. Their initial missing
lengths and central missing lengths are, respectively,

    l_L=h(3/2+t), l_R=h(5/2−t), l_L+l_R=4h,
    c_L=h(3/2−t), c_R=h(1/2+t), c_L+c_R=2h.         (4)

Every retained cell lies in [epsilon,pi−epsilon], epsilon=h/2.
Also l_s<=5h/2<pi/4 and c_s<=3h/2<pi/2. Put
ell=−log(sin epsilon)<=log m, by the sine chord inequality.
The midpoint error of a BV function, after normalization, is at most
its variation divided by2m. Initial and central gaps are paid below.

## 1. Exact log-n coefficient difference

Write f_s=A(v_s(z))−4a/(pi*z), and f0=f_s at the origin. The actual
max formulas give, with T=2a cot(z/2),

    pi(f_L−a f0)=max(q,p−T),
    pi(f_R−a f0)=max(−q,p−T,q−2T).                 (5)

Both max expressions increase with z. Their combined variation is
at most2max(p,q), and each absolute value is at most max(p,q).
Consequently the two coefficient differences have combined variation
<=2rho/pi and sup<=rho/pi per side. Midpoint quadrature plus the
total6h missing length from (4) yields

    |Q_t[L(f_L−a f0)]+Q_(1−t)[L(f_R−a f0)]|
                                           <=7rho L/(pi*m). (6)

These are the exact max formulas, so coefficient switches are included.

## 2. Weighted pole numerator, including periodic derivative atoms

Let f(x)=Phi0(1/2+x/(2pi)). It is even and2pi-periodic. The accepted
bounds, after this literal change of variable, are

    |f|<=4, Lip(f)<2, |f''|<1 away from odd multiples of pi,
    Var_one_period(f')<41/(2pi)<7.                  (7)

For (7), |Phi0''|<35 on every open period and the derivative jump
at an integer has magnitude<6. The variation bound INCLUDES that
atom; it is not an assumption of a globally smooth derivative.

Exactly,

    N_L=ce f(z+delta)+cd f(z−ephase),
    N_R=ce f(z−delta)+cd f(z+ephase), N0=2f(z).

Set V_s=N_s−aN0, V0=U0−aU0(0), and r=ce+cd−2a. Since
0<=r<=(ephase²+delta²)/8<=rho²/4, (7) gives

    |V_s|,|V0|<=(9/2)rho.                          (8)

For0<=z<=pi/2 all shifted arguments lie strictly in(−pi,pi), so
the ordinary |f''|<1 bound is legitimate there. It gives

    |V_s'(z)|<=(9/4)rho.                           (9)

Indeed the two translation increments cost at most |delta|+ephase
<=2rho; the residual coefficient costs at most2r<=rho²/2.

On pi/2<=z<=pi the derivative may cross an atom. Instead use

    Var_I[f(.+b)−f(.)]<=|b| Var_one_period(f')<7|b|,

for |b|<=1/2 and I=[pi/2,pi]. To prove it, represent each derivative
difference by the signed measure Df' over the interval between its
arguments and integrate its absolute bound over I. Tonelli bounds
the measure's multiplicity by |b|. The enlarged interval has length
<2pi, so its total variation is at most one periodic total. This also
proves the statement when the shifted interval crosses the atom.
The residual r f term has variation at most7r on I. Thus

    Var_I V_s<15rho.                               (10)

Now d0(z)=1/(2sin(z/2))−1/z increases from0 to1/2−1/pi<1/5, as
proved in N1-13. The exact relative regular pole part is

    Pdiff_s=[V_s(z)−V0]/z+V_s(z)d0(z).             (11)

On[epsilon,pi/2], differentiating the quotient in (11) and using
(9) bounds its variation by(9/2)rho log m. The product variation is
at most2rho, by (8),(9), d0<=1/5 and pi/2<2. The same identities
give sup|Pdiff_s|<=4rho on the whole initial half.

On[pi/2,pi], use directly Pdiff_s=V_s/(2sin(z/2))−V0/z. The first
weight has sup<3/4 and variation<1/4; the second has sup<2/3 and
variation<1/3. Equations(8),(10) therefore give

    Var_[pi/2,pi] Pdiff_s<14rho, sup|Pdiff_s|<7rho.

The total variation over both sides is consequently at most
rho(9log m+32). Initial and central gap integrals cost, respectively,
16rho/m and14rho/m by their total lengths in (4). Midpoint quadrature
and these gaps prove

    |Q_t[Pdiff_L]+Q_(1−t)[Pdiff_R]|
                           <=rho[(9/2)log m+46]/m. (12)

## 3. Cancellation difference: the small-mesh root-free alternative

Denote I_s=I(C(v_s(z)),D(v_s(z)),v_s(z)). The relative cancellation
part left after the endpoint reference cancels is EXACTLY

    Cdiff_s(z)=I_s(phi,z)−a I_s(0,z)−d log(pi−z).   (13)

On0<z<=pi/2, put w=a cot(z/2), u=p/2. The generic parameters are
s_L=w+q/2,s_R=w−q/2>0. Both satisfy s_s sin z>=a−q/2>=11/16>u.
The accepted no-root formula J(u,s,z)=2s log(sin z) therefore gives

    I_L−aI_L(0)=q log(sin z),
    I_R−aI_R(0)=−q log(sin z).                     (14)

Thus the combined variation of (13) on[epsilon,pi/2] is at most
2rho ell+2rho log2 <=2rho ell+2rho. No entropy term is used here.

For the central half let e=pi−z, s0=a tan(e/2),
s_L=s0+q/2,s_R=|s0−q/2| and u=p/2. Use the EXACT generic identity

    J(u,s,e)=2(s−u)_+ log(sin e)+R(u,s,e),
    |R_s|<=log((u+s)/|u−s|),
    0<=R_e<=2u cot e if s>u, R_e=0 if s<=u.        (15)

For u=0,R=0. The logarithmic parameter singularity at s=u is
integrable; the root/no-root formulas have the continuous matching
established in C06. Define

    b_s(e)=2(s_s(e)−u)_+−2s0−d.

Both b functions decrease from zero. More explicitly,

    b_L=max(q−p,−2s0)−d,
    b_R=max(−p−q,q−p−4s0,−2s0)−d.

Their combined sup norm and combined variation are each at most3rho;
each individual sup norm is at most2rho. The actual central form is

    Cdiff_s=R(u,s_s(e),e)+b_s(e)log(sin e)
                                      +d log(sin e/e).     (16)

### Uniform variation on e>=epsilon

The parameter curves s_L,s_R have at most three monotone pieces in
total and lie in[0,S],S=a+q/2<=5/4. If p>0, their total parameter
contribution to the variation of R is at most3G, where

    G=p[1+log((S+p/2)/(p/2))]<=p[1+log(3/p)].       (17)

This is C06's elementary integral of the bound for |R_s| in (15).
The separation contribution along both curves is at most2p ell.

If rho<=epsilon²/8, there are in fact NO roots on this truncated
interval. Indeed, for e>=epsilon, the sine chord inequality gives
1−cos e>=2e²/pi²>e²/5, and therefore

    [a tan(e/2)−q/2]sin e
       >=3e²/16−rho/2>=e²/8>=rho>=u.               (18)

The bracket is positive. Both s parameters meet s sin e>=u, and
R=2u log(sin e) exactly. Its combined variation is at most2p ell.

If rho>epsilon²/8, use p<=rho and
p log(rho/p)<=rho/exp(1)<rho/2 to get

    G<=rho[3/2+log(3/rho)]
      <=rho[11/2+2ell].                            (19)

Here log24<4 and log(1/epsilon)<=ell were used. For p=0 both sides
are interpreted continuously and R=0 directly. Equations(17)--(19)
prove in BOTH regimes

    sum_s Var_[epsilon,pi/2] R(u,s_s(e),e)
                                  <=rho[33/2+8ell]. (20)

This is the explicit step that replaces the potentially unbounded
log(1/rho) by the actual mesh logarithm. No such replacement is made
without (18). The b products in (16) cost at most6rho ell. The two
d log(sin e/e) terms cost at most rho, because log(pi/2)<1/2.
Together with (14), the whole two-side variation of Cdiff on
[epsilon,pi−epsilon] is at most

    rho[39/2+16ell].                               (21)

All expressions join at z=pi/2. Partitioning at the finitely many
max/root transitions and integrating the locally integrable bounds
in (15) justifies (20)--(21) across those transitions.

### Integrable envelopes for every removed interval

On an initial interval, (14) and pi−z>1 give

    |Cdiff_s(z)|<=rho[log(pi/(2z))+log pi].          (22)

For the central gaps we need a pointwise bound, not an uncharged
endpoint value. Repeat the root-free alternative with epsilon=e.
In its root-free case |R|<=rho ell_e, ell_e=−log(sin e). Otherwise
|R(u,0,e)|=p log2<rho and the parameter integral in (17)--(19)
gives |R|<=rho[13/2+2ell_e]. Thus (16), |b_s|<=2rho and
|log(sin e/e)|<=log(pi/2)<1/2 imply, for0<e<=pi/2,

    |Cdiff_s(pi−e)|<=rho[7+4ell_e].               (23)

Both envelopes are integrable to the actual endpoints. The elementary
function x[1+log(c/x)] is concave. Apply it to the two initial lengths
whose sum is4h and the two central lengths whose sum is2h, using
ell_e<=log(pi/(2e)). The cancellation contribution to the normalized
gap errors, including the additional1/pi in F, is at most

    initial: (4rho/(pi*m))[1+log(pi*m/4)]
                                           <=4rho(3+log m)/(pi*m),
    central: (2rho/(pi*m))[11+4log(m/2)]
                                           <=rho[22+8log m]/(pi*m).

Midpoint quadrature applied to (21), plus these complete gap charges,
proves

    |Q_t[Cdiff_L/pi]+Q_(1−t)[Cdiff_R/pi]|
                        <=rho[175/4+20log m]/(pi*m). (24)

## 4. Combine the actual-mesh profile difference

The exact profile difference is

    W_s=L(f_s−a f0)+Pdiff_s+Cdiff_s/pi.

Consequently (6),(12),(24) pay every part of the first two terms in
(3), with their actual midpoint cells and every missing endpoint
interval. No ordinary row or weighted collision is deleted.

## 5. Bound the remaining actual-origin mesh shift

At zero phase the profile is explicitly

    F0=L f0+P0+Q0/pi,
    f0=(2cot(z/2)−4/z)/pi,
    P0=[2f(z)−2f(0)]/z+2f(z)d0(z),
    Q0=2cot(z/2)log(sin z)−4log z/z.              (25)

Every argument in the finite sum Shift lies in[2h,pi−h]. On this
interval the following derivative bound is valid almost everywhere:

    |F0'|<=(4/3)L+(2/3)log m+20/3.                (26)

Here are the elementary details. For z<=pi/2, D05's proved
|[2cot(z/2)−4/z]'|<=1 gives |f0'|<1/3; for z>=pi/2 the direct
bound (2+16/pi²)/pi<4/3 suffices. For P0 the quotient derivative
has magnitude<=1 because |(2f)''|<2 on(0,pi), with no interior
atom. Also0<=d0'<=pi²/32<1/3: writing x=z/2, its numerator is
sin²x−x²cos x<=x²(1−cos x)<=x⁴/2 and its denominator is
4x²sin²x>=16x⁴/pi². Thus |P0'|<=1+4/5+8/3<5.

On z<=pi/2 use D05's exact Q0=f log(sin z)+g decomposition, now
with f=2cot(z/2)−4/z and g=4log(sin z/z)/z. Its accepted elementary
bounds |f'|<=1,|f|<=z,|g'|<4 imply |Q0'|<=log m+5.
On z>=pi/2 set e=pi−z. Differentiate2tan(e/2)log(sin e);
its derivative has magnitude<=2ell_e+1, and the remaining derivative
of4log z/z has magnitude<4. Since e>=h, ell_e<=log m. Hence
|Q0'|<=2log m+5 everywhere needed. Division by pi>3 proves (26).

Each of the2(n−2) shifted arguments moves by beta/m. Their paths
stay in[2h,pi−h]. The absolute-continuity form of (26) therefore gives

    |Shift|<=rho/m[(8/3)L+(4/3)log m+40/3].        (27)

This pays the changing meshes explicitly. It is not inferred from
the variation of W, and no initial or central integral is counted
again in (27).

## 6. Final constants and all-n scope

Add (6),(12),(24),(27) in the EXACT identity(3):

    |delta_a Eout| <= rho/m {
        (7/pi+8/3)L+(9/2+4/3+20/pi)log m
                                    +46+40/3+175/(4pi)}.

Using pi>3 makes this at most

    rho/m [5L+(25/2)log m+887/12].                 (28)

Since log m<=L+1/n<=L+1/32, and887/12+25/64<75, (28) implies(2).
The derivative of[(35/2)log n+75]/n has numerator
35/2−[(35/2)log n+75]<0, proving the stated real-n monotonicity.

At rho=0 the exact subtraction in(3) is zero and (2) is literal.
The bounds cover signed phases by the established separate evenness
convention, both mesh parities, axes and the closed near seam. Weighted
Phi continuation and the generic continuous J formulas include
coefficient switches and moving roots; polynomial collision values
are not individually represented by unweighted poles anywhere here.

This proves only the regular outer operator increment. The physical
noncorner defect, actual-corner descent, full D13 relative remainder
and any improved analytic global onset are separate obligations.
No scalar, numerical integral, phase/native/board/root/degree job or
new model correction was used. Candidate and attempt are the owned
D25-outer-relative records.2026-11-06; input476208fe080cc79cae5b2578344b2e18f442a1e8;
requested Astra ultra, serving metadata unexposed. Distinct review is
required before root adoption; frozen D22 records remain untouched.
