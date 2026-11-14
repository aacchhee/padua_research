# PD-T?argmax-bridge-codex-D07-outer — Global regular-cell completion with six exact rows

ID kind: PD-T. Aliases: complete regularized outer quadrature; paired
initial-gap envelope; global profile with exact singular meshes.
Split from: the practical M_infty comparison, OPEN. Split into: the
exact global mesh and M_infty matching identity has its own D07 file.

## Statement and definitions

Let n>=16 be an integer, m=n+1, L=log n, h=pi/m. Work first on the
FULL closed phase triangle alpha,beta>=0, alpha+beta<=pi. Use exactly
the corrected polynomial S_n, its actual polynomial row norms R_r,
the weighted profile H(L,v)=A(v)L+B(v), a,p,q,P,U0,d and Delta_2
from the accepted D05-fixed-special-rows and D05-outer-profile-variation
theorems. In particular a=(cos alpha+cos beta)/2, p=sin alpha,
q=sin beta, P=p+q, d=(q-p)_+. Define the unchanged fixed sets

    A6={0,1,2m-2,2m-1,m-1,m},
    O6={0,...,2m-1} minus A6,
    J6=(nm)^-1 sum_(r in A6) R_r,
    t=beta/pi, t_L=t, t_R=1-t,
    v_L(z)=z, v_R(z)=2pi-z, z_(s,k)=h(k+t_s).

Thus the ordinary labels are EXACTLY k=2,...,m-2 on each folded
side. No actual polynomial collision is deleted from O6; the accepted
weighted continuity theorem makes its complete H value legitimate.
The six R_r values remain actual finite corrected polynomial rows.

Subtract precisely D05's references, with new letter T to avoid any
left-side ambiguity:

    T(L,z)={U0+(4a/pi)(L+log z)}/z,
    Z_s(z)=B(v_s(z))-[U0+(4a/pi)log z]/z,
    f_s(z)=A(v_s(z))-4a/(pi*z),
    F_s(L,z)=H(L,v_s(z))-T(L,z)-(d/pi)log(pi-z).

Use continuous regularized values at z=pi. The ordinary samples never
reach zero or pi. Define the new intermediate object openly by

    U(L)=(1/pi)integral_0^pi [F_L(L,z)+F_R(L,z)]dz,
    G_n=J6+Delta_2
          +(1/m)sum_s sum_(k=2)^(m-2) T(L,z_(s,k))
          +(d/(pi*m))sum_s sum_(k=2)^(m-2) log(pi-z_(s,k))
          +U(L).                                           (1)

These are ordinary convergent integrals after the displayed subtraction;
no separate divergent integral is assigned a value. Equation(1) is
not a change to M_far, M_infty or the frozen near model. The companion
D07-global-mesh.md removes the growing reference sums exactly and
states G_n-M_infty with all constants and six rows retained.

For an explicit full-phase bound put

    epsilon=3h/2, u=p/2, S=1/2+2a/epsilon,
    ell=-log(sin epsilon),
    Gpar=2u[1+log((S+u)/u)] if u>0, Gpar=0 if u=0,
    M_A=max(p,q)/pi+4a/pi^2,
    V_A=2max(p,q)/pi+8a/pi^2,
    V_B=23+{3Gpar+(2p+6P)ell+26a+20+2d log2}/pi,
    C_B=6+(4+4a/e)/pi <8,
    Q(P,x)=(2x/pi)[7+(P/pi)(5+2log(4pi/x))],
    E_global=(L*V_A+V_B)/(2m)+6L*M_A/m
                   +Q(P,2h)+4d log pi/(pi*m)+2C_B/m.        (2)

Here e=exp(1), distinct from c_e in the profile definition. With
K_fixed the accepted D05 six-row intermediate,

    |K_fixed-G_n|<=E_global,
    |S_n-G_n|<=E_D04+E_global.                              (3)

E_D04 is exactly D04/D05's accepted row-reduction error, not a new
allowance. Formula(2) is valid on the ENTIRE closed phase diamond by
separate absolute phases, including a=0, axes, moving numerator roots,
coefficient switches and weighted polynomial collisions.

On the CLOSED NEAR HALF DIAMOND |alpha|+|beta|<=1/2, the stronger
explicit simplification is

    E_global <= E_near(n)
      ={(21/5)log n+(9/4)log(2n+2)+1022/15}/(n+1).          (4)

E_near decreases for n>=16, and

    E_global<1/64 for every integer n>=10000                (5)

on this stated near domain. This meets only the prospective OUTER
component budget. Neither E_D04 nor G_n-M_infty is included in(5).

Status: **PROVED**, written analytic developer result, distinct review
pending. No numerical premise. The full useful M_infty allowance,
phase-relative comparison, implementation and global argmax remain OPEN.

## Dependencies and distinction from earlier claims

- Accepted D05-outer-profile-variation.md supplies the already proved
  epsilon-independent V_A and the full-phase V_B, and its actual-cell
  midpoint bound. These are NOT rebranded as a new lemma.
- Accepted D05-fixed-special-rows.md supplies the literal fixed six
  rows at R2,n>=16 with the same E_D04, even on collisions.
- N1-joint-endpoint-profile.md supplies |Z_s(z)|<=
  7+(P/pi)[3+2log(4pi/z)] for 0<z<=pi/4.
- N1-round6-regular-variation.md supplies near-half-diamond
  M_A<3/5,V_A<6/5; its exact max formulas are already used in D05.
- C06-far-compact-error.md sections1--2 supplies full-phase
  sup|P_s|<6 and sup|I_s-d log(pi-z)|<4 on pi/2<=z<=pi.

The new step completes the actual ordinary cell union AFTER both
singular subtractions, retaining exact reference sums and exact rows.
It does not reuse D02's separate fixed-strip I_n, approximate six
actual rows by C_R, or substitute a shrinking delta in old e_mesh.

## Proof

### 1. Exact cell geometry, without collision holes

For a fixed phase t in[0,1], the ordinary centers are
h(k+t), h(k+1-t), k=2,...,m-2. The corresponding centered cell
unions are exactly [l_s,u_s], where

    l_L=h(3/2+t), l_R=h(5/2-t),
    u_L=pi-h(3/2-t), u_R=pi-h(1/2+t).

Therefore

    l_L+l_R=4h,
    (pi-u_L)+(pi-u_R)=2h,
    min(l_L,l_R)>=3h/2=epsilon,
    max(l_L,l_R)<=5h/2<pi/4,
    min(u_L,u_R)>pi/2.                                (6)

The last two inequalities use m>=17. These identities include t=0
and t=1 literally. No phase floor or collision-membership assumption
has been replaced by a limit. Ordinary H values at weighted collisions
use the accepted fixed-row theorem, not equality to an actual row norm.

D05's BV midpoint bound gives

    |(1/m)sum_s sum_k F_s(L,z_(s,k))
                  -(1/pi)sum_s integral_(l_s)^(u_s) F_s|
                                 <=(L V_A+V_B)/(2m). (7)

### 2. Initial gaps and their paired concave envelope

Write exactly F_s=L f_s+Z_s-(d/pi)log(pi-z). The global coefficient
sup satisfies |f_s|<=M_A. Equation(6) therefore bounds the combined
initial L f_s integrals by 4L M_A/m.

Let W_P(z)=7+(P/pi)[3+2log(4pi/z)]. The accepted endpoint envelope
gives |Z_s|<=W_P. Its integral

    J_P(x)=integral_0^x W_P(z)dz
          =x[7+(P/pi)(5+2log(4pi/x))]

is concave, because J_P''(x)=-2P/(pi*x)<=0. Using (6),

    (1/pi)sum_s integral_0^(l_s)|Z_s|
       <=[J_P(l_L)+J_P(l_R)]/pi
       <=2J_P(2h)/pi=Q(P,2h).                         (8)

This also holds at P=0, where the envelope integral is linear. Using
a separate maximum length 5h/2 would discard this exact pairing.
Throughout the initial gaps, pi-z>=pi-5h/2>1, so
|log(pi-z)|<=log pi. The remaining initial charge is at most
4d log pi/(pi*m).

### 3. Central gaps after exact logarithm subtraction

The numerator regular part P_s=N_s/[2sin(z/2)]-U0/z has sup<6.
On pi/2<=z<=pi, C06's full-phase central theorem gives
|I_s-d log(pi-z)|<4, including its continuous endpoint limit. Since
log z/z<=1/e for z>1, it follows directly that

    |F_s(L,z)|<=L M_A+6+(4+4a/e)/pi=L M_A+C_B.

Their combined central missing length is 2h, so its normalized
integral is at most 2(L M_A+C_B)/m. Add this, the initial-gap charges
and(7) to obtain(2)'s E_global for the full F integral. The singular
meshes and six exact rows in K_fixed and G_n are identical and cancel
algebraically. This proves the first inequality in(3). The accepted
fixed-row bound |S_n-K_fixed|<=E_D04 proves the second.

For the numerical-looking constant C_B<8 no evaluation is needed:
e>5/2, a<=1 and pi>3 give C_B<6+(4+8/5)/3<8.

### 4. A useful near-half-diamond component constant

On rho=|alpha|+|beta|<=1/2 we have p,q,P,d<=1/2 and a<=1.
The accepted near bounds give M_A<3/5,V_A<6/5. Also
6/epsilon=4m/pi<2m. As in the D05 entropy estimate,

    Gpar<=p[1+log(6/epsilon)]+p log(1/p)
          <=(1/2)[1+log(2m)]+1/e,
    ell<=log(2m).

The braces in V_B are bounded by 50+(11/2)log(2m): use
3/e<3/2, 2p+6P<=4 and 2d log2<=log2<1. Thus

    V_B<40+(11/6)log(2m).

Furthermore log pi<6/5 and pi>3 imply
4d log pi/pi<4/5. The initial envelope term simplifies to

    Q(P,2h)=(4/m)[7+(P/pi)(5+2log(2m))]
            <=[94/3+(4/3)log(2m)]/m.

Insert these bounds and C_B<8 into(2). The L coefficient is
3/5+18/5=21/5, the log(2m) coefficient is11/12+4/3=9/4, and
the constant is20+94/3+4/5+16=1022/15. This proves(4).

For n>=16 the derivative numerator of E_near is

    (21/5)(1+1/n)+9/4
          -[(21/5)log n+(9/4)log(2n+2)+1022/15]<0.

Indeed the first two terms are <=42/5+9/4<11, while the constant
1022/15 exceeds68 and both logarithms are positive. Thus E_near
decreases. At n10000 both log n and log(2n+2) are below10:
the partial exponential sum gives e>163/60>19/7, and the exact rational
inequality (19/7)^10>20002 proves this. Hence

    E_near(10000)<3979/300030<1/64.

This and monotonicity prove(5), without samples or numerical code.

## Scope and checks

The general proof remains literal at a=0 and p=0 (Gpar=0 at p=0),
every phase edge, central/root transition and weighted collision.
Only the1/64 simplification uses the near half diamond. No statement
about unweighted pole limits or a physical corner follows. The new
outer charge removes the dominant separate I_n allocation, while the
six exact rows and global singular meshes retain their finite-h data.
Those terms still need their own controlled comparison to M_infty;
the companion exact identity does not declare that correction small.

No scalar numerical run, native/board evaluation, quadrature, phase
grid, fit or old-source change was executed. Analytic proof only,
awaiting distinct review. Original D05 and D06 statements stay frozen.
2026-11-06, parent-requested Codex Sol xhigh, input
`2e4ac49fa0687a7736bc1df82c12e6483b1c7a94`, bounded20min block.
