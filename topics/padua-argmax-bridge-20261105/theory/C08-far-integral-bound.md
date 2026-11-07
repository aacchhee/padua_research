# PD-T?argmax-bridge-C08-far-integral — A uniform renormalized integral bound

ID kind: PD-T. Aliases: paired full-phase cancellation upper; finite-cutoff
sine-log budget; complementary C08 compact-constant integral.
Split from: the C08 full far-model comparison. Split into: none. The
endpoint convolution, scalar pole functional and final comparison have
separately owned theory files.

## Statement, definitions and status

Use exactly the fixed full-phase model in C06-far-compact-error.md. For
alpha,beta>=0,alpha+beta<=pi define

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta,
    e=alpha+beta, d=alpha-beta,
    c_e=cos(e/2), c_d=cos(d/2), a=c_e*c_d,
    B0=4a/pi², D0=U0/pi+B0 log pi, delta=1/100.

Then the exact renormalized integral obeys

    K_delta=B0 log²(delta/pi)+2D0 log(delta/pi)
                +(1/pi)integral_delta^(2pi-delta)B(v)dv
             <49/50.                                      (1)

The domain is the full closed phase triangle, including a=0, axes,
vertices and every integer pole offset. Other quadrants use separate
phase evenness, with no exchange of the n and n+1 meshes. The degree
does not occur in (1). The central integral is the inherited improper
integral with its explicitly integrable logarithm.

Overall status: **PROVED**, analytic developer derivation below, pending
distinct supplementary review and formal audit. The originally proposed
stronger budget K_delta<=1/2 remains OPEN; (1) is sufficient after the
separate C08-far-corner-margin theorem improves the corner lower by1/2.
No numerical integration, finite sample or fitted constant is a premise.

Definitions and dependencies: B=V+I/pi, U0, Phi_0 and the continuous
combined pole products are exactly C06-far-compact-error equations(3)–(7).
That file's section2 reconstructs the generic J identity on the full
parameter range used here. C08-far-pole-functional proves the separate
global scalar H<1/2 and its explicit finite-cutoff bound. Its frozen
source at this derivation is SHA-256
6cb61ebc3f3808c61bc8d72feb2bee3a57c1dbecf597a7915833b4f43c8cda67.
The C08 weighted-coefficient proof's cotangent partial fraction supplies
sum_(k>=1)1/k²=pi²/6 as explained below. No near-domain two-phase theorem
is used outside its stated scope, and no model correction is introduced.

## 1. Split the exact renormalization into two finite combinations

Let l=log delta. Expanding the first two terms of (1) gives exactly

    K_delta=K_V+K_I,
    K_V=(2U0/pi)log(delta/pi)+(1/pi)integral_delta^(2pi-delta)V(v)dv,
    K_I=(4a/pi²)(l²-log²pi)
                      +(1/pi²)integral_delta^(2pi-delta)I(v)dv. (2)

This algebra preserves the cancellation of the two endpoint logarithms.
No bound on separate divergent channel integrals is being asserted.

Put f(x)=Phi_0(1/2+x/(2pi)), an even2pi-periodic continuous function.
The exact numerator of V is c_e*f(d+v)+c_d*f(e-v), and
U0=c_e*f(d)+c_d*f(e). Pairing v with2pi-v in the second channel shows

    K_V=c_e*H_delta(d)+c_d*H_delta(e),                       (3)

where H_delta is precisely the finite-cutoff functional in
C08-far-pole-functional. That theorem gives

    H_delta(x)<1/2+(12/pi²)(delta+delta³/48), all real x.

Both weights are nonnegative and at most1. Moreover
c_e+c_d<=1+c_e*c_d=1+a, because(1-c_e)(1-c_d)>=0. Thus

    K_V<(1+a)/2+27/1000.                                  (4)

Indeed the total cutoff charge is at most
(24/pi²)(1/100+1/48,000,000)<27/1000, using pi²>9.
This includes offset cusps: the scalar theorem accounts for their
negative derivative atoms and uses the global Lipschitz bound for the
missing interval. It does not assume differentiability at those offsets.

## 2. A one-sided cancellation bound on the entire folded interval

For0<z<pi put v_L=z,v_R=2pi-z and T=2a cot(z/2)>=0.
The exact two cotangent coefficients give the generic cancellation
parameters

    u=p/2,
    s_L=(q+T)/2, s_R=|q-T|/2,
    epsilon=min(z,pi-z), sin epsilon=sin z.                 (5)

The reductions to these parameters use only channel exchange, simultaneous
sign reversal and reversal on the cotangent circle. They are invariances
of I, not an interchange of the two original meshes.

For clarity, the generic full-range identity of C06 is

    J(u,s,epsilon)=2(s-u)_+ log(sin epsilon)+R(u,s,epsilon).

Its remainder satisfies R<=0 for every u,s>=0 and0<epsilon<=pi/2.
If s<=u this is immediate from the exact entropy expression

    R=2[c log(c/u)+b log(b/u)],
       c=(u-s)/2, b=(u+s)/2,

since c/u,b/u lie in[0,1]; the u=0 case is its continuous limit.
If s>u, C06's exact differentiated formula gives

    R_epsilon=2[u cos epsilon
                  -sqrt((u²-s²sin²epsilon)_+)]/sin epsilon>=0,
    R(u,s,pi/2)=0.

Therefore R(u,s,epsilon)<=0 in this case as well. The square-root
formula includes the no-root branch, and all equality/zero parameters
follow by the already established continuous J limits.

Consequently, with x_+=max(x,0),

    I(v_L)+I(v_R)<=[(q+T-p)_++(|q-T|-p)_+]log(sin z).

The sum in square brackets is at least

    q+T-p+|q-T|-p=2max(q,T)-2p>=2T-2p.

Since log(sin z)<=0, multiplying reverses this last inequality. We obtain
the full-domain upper

    I(v_L)+I(v_R)
       <=4a cot(z/2)log(sin z)+2p|log(sin z)|.               (6)

There is no hypothesis p<=q, a>0 or z<=pi/2 in (6). At z=pi/2 it
holds by continuity. At the central endpoint z=pi its right side is
integrable; the exact left side has the integrable logarithm already
proved in C06. Thus (6) can be integrated on delta<z<pi. The upper
becomes deliberately loose at a=0, but remains finite after integration.

## 3. Evaluate the sine-log baseline with its finite cutoff

First,

    integral_0^pi |log(sin z)|dz=pi log2.                    (7)

This standard identity follows directly by reflection about pi/2,
the double-angle formula and the substitution z=2t; all endpoint
logarithms are integrable. Hence the second term in (6), after division
by pi², contributes at most(2log2/pi)p<=9p/20. Here log2<7/10 and
pi>25/8 suffice.

For the first term define Li2(y)=sum_(k>=1)y^k/k² on0<=y<=1.
Termwise integration on compact subintervals, followed by monotone
convergence, gives the antiderivative

    integral 4a cot(z/2)log(sin z)dz
       =4a log²(2sin(z/2))-4a log²2-2a Li2(sin²(z/2)).     (8)

It can also be checked directly by differentiating. The cotangent
partial fraction used in C08-far-weighted-coefficient proves
sum_(l odd>=1)l^(-2)=pi²/8. Splitting the full reciprocal-square sum
into odd and even terms gives Li2(1)=pi²/6. Thus the value of (8)
at z=pi is -a*pi²/3.

Let y=sin²(delta/2). Adding the logarithmic polynomial in K_I to
the integrated baseline (8), then dividing by pi², yields exactly

    -c*a+(a/pi²){4[log²delta-log²(2sin(delta/2))]+2Li2(y)},
    c=1/3+(4/pi²)(log²pi-log²2).                           (9)

Because0<2sin(delta/2)<delta<1, the square-log difference in (9)
is negative. Also y<=delta²/4=1/40000 and
Li2(y)<=sum_(k>=1)y^k=y/(1-y). Therefore its entire positive
cutoff contribution is less than

    (2/pi²)y/(1-y)<=2/(9*39999)<1/100000.                 (10)

Only a<=1 and pi²>9 were used. Finally c>1/2: the elementary bounds
log pi>11/10, log2<7/10 and pi²<10 give

    c>1/3+(2/5)[(11/10)²-(7/10)²]
      =233/375>1/2.                                     (11)

Combining (6)–(11) with the exact split (2) proves

    K_I<-c*a+9p/20+1/100000.                            (12)

## 4. Close the numerical budget without a phase optimization

Equations(4),(11),(12), together with0<=a,p<=1, give

    K_delta<1/2+(1/2-c)a+9p/20+27/1000+1/100000
            <=1/2+9/20+27/1000+1/100000
             =97701/100000<49/50.

This proves (1) uniformly. At a=0 no term a*log a or a singular
unweighted pole value has been introduced; (3) uses the continuous f
itself. The two phase vertices and all collisions are consequently
covered by the same inequalities, not by a separate unproved limit.

## Scope, checks and history

The separately frozen endpoint theorem gives
E64<49/25+1/3000. Together with (1) it gives the useful compact
constant upper C_far<49/25+1/3000+49/50<3. This arithmetic consequence
is not a replacement for the separately owned full model comparison,
which also needs its weighted logarithmic coefficient, finite corner
lower and actual-primitive error premises.

No mathematical executable, sampled degree, phase sweep or interval
quadrature was run in this continuation. Every integral used in the
upper bound is evaluated or bounded analytically. The earlier diagnostic
is contextual only and was not used as a premise. The stronger initial
K_delta<=1/2 and exploratory H shape inequality remain OPEN; their
successful weaker replacements and reasons are recorded in
../ideas/C08-far-integral.md and ../attempts/C08-far-integral.md.

2026-11-06. Rules read at cc4e51210f51ff51c773dcdd458e25f934d02598;
current merged input547a473a6e1c1268ff4f1ada7243b12afb02d0bc, unchanged
rules. The refreshed gate includes the new NN-MOP registry entries.
Codex, parent-requested Astra ultra with prospective LOG justification;
serving metadata unexposed. C06 and all earlier proof bytes unchanged.
