# PD-T?argmax-bridge-codex-C05-finiteh-02 — A finite near-model comparison with the larger defect budget

ID kind: PD-T. Aliases: retained-cell finite-degree assembly; exact
strip/outer cancellation; noncorner near comparison at n10^6.
Rules/input `4b728b04216a5490910780bc609a82b853058426`.
Status: **PROVED analytic developer result; independent review required**.

## Statement and exact scope

Use exactly N1-15's M_near, integer n>=10^6, m=n+1, L=log n,
alpha,beta>=0, rho=alpha+beta<=1/2, r2=alpha^2+beta^2, R128,
delta1/1000 and every already fixed truncated constant, actual cell,
floor and polynomial collision convention. Let F_n be the actual
residual increment of N1-17, and T the actual fixed-model limit (3) of
C02-near-explicit-onset.md, SHA256
`a42be2a78546b02eec20326beba872965abc20810b879b70c770ae0d33d2f928`.
Then

    |F_n(alpha,beta)-[T(alpha,beta)-T(0,0)]|
       <=45000*r2/n+40*beta/n+200*(L+1)/n.             (1)

In particular the same unchanged model satisfies

    M_near(alpha,beta,L)<Lambda_c(n)+1/32.             (2)

This is the prospectively registered larger-budget comparison, not
the original C1 tolerance 1/4096. The latter stays OPEN at n>=10^6.
The uniform one-sided 1/250000 error target also remains OPEN. This
proof changes no model or correction and runs no numerical cover.

With the independently reconstructed C02 projected floor >1/16 for
all noncorner odd centers at n>=4096, (2) has the following consequence:
every physical odd noncorner center and physical phase representation
with |alpha|+|beta|<=1/2, at n>=10^6, obeys

    lambda_n(theta,phi)<Lambda_c(n)-869/28000.         (3)

Separate absolute phases extend (1)-(2) as in N1-15. Actual corner
centers are excluded from (3); their comparison is a separate problem.
No claim covers rho>1/2, the finite gap below 10^6, or the global all-n
argmax. The certified degree and finite-energy ranges are unchanged.

## Dependencies and accounting choice

The endpoint increment is C05-finiteh-endpoint-increment.md, frozen
SHA256 `0e8616a3f23ba42ca31b5967d3e9bf44186472b8ff51d105da38c704cba693f7`.
The limiting comparison is C04-near-limit-comparison.md, specifically

    T-T(0,0)-G_n<1/50000+3/(2*10^9), n>=10^6.         (4)

N1-09–16 supply the unchanged model, endpoint expansion, cells and
coefficient identity. The full round5–8 sources and reviews, C01's
central proof, actual C02 near proof, and both C04 proofs were read.
C02's separate fixed jump and special-row bounds are reused below;
its coarse endpoint or outer/strip error is not reused.

We work with F_n directly, not N1-18's auxiliary Q_n. Thus actual H8
rows, collision holes and cutoff artifacts are all bounded in the exact
decomposition below. No additional 9/(2n) is added to (1) or (2). If
one later converts this F_n estimate to Q_n, the known envelope is
charged once in that conversion, not in this proof and then again.

## 1. Pair the actual strip boundary with the outer integral first

Use N1-10's notation t_L=beta/pi, t_R=1-beta/pi and

    h=pi/m, epsilon=log(m/n), B0=4a/pi^2,
    D0=U0/pi+B0*log pi, Z_n=D0-B0*epsilon,
    H_J=h_J(t_L)+h_J(t_R), G_J=g_J(t_L)+g_J(t_R),
    l_s=h*(R+t_s-1/2), u_s=h*(K_s+t_s+1/2),
    K_s=floor(delta/h-t_s), J=4096.

All finite truncations are exactly the model's existing ones. Define

    q_L=sin beta, q_R=-sin beta, U_L=U1, U_R=-U1,
    u_a(z)=2a*cot(z/2)-4a/z,
    f_s(z)=[q_s+u_a(z)]/pi,
    V_s(z)=L*f_s(z)+(q_s/pi)*log z+U_s.

On the interval containing delta and u_s the exact profile is

    H_s(L,z)/pi = S'(z)+V_s(z)/pi+E_s(z)/pi,
    S(z)=[U0/pi+B0*L]*log z+(B0/2)*log^2 z,           (5)

where N1-10/18 prove |E_s(z)|<3/1000. Here
|u_s-delta|<=h/2 and z is inside the proved enlarged endpoint interval.

Let x0=log pi-L, so log h=x0-epsilon. The singular boundary expression
of the strip obeys the exact identity

    Z_n*log(u_s/h)+(B0/2)*log^2(u_s/h)
       =S(u_s)-D0*x0+(B0/2)*x0^2
                    +D0*epsilon-(B0/2)*epsilon^2.    (6)

This follows by expansion; in particular the terms L*epsilon cancel.
Also N_s/m=(u_s-l_s)/pi exactly. Consequently combining this strip
with its outer integral starting at the same u_s, then moving their
common boundary to delta, changes the sum by exactly

    -(1/pi)*integral_delta^(u_s) E_s(z)dz.            (7)

Every singular, regular-A, q_s log z and U_s term cancels at that
boundary. This is an algebraic comparison of the existing terms, not
a new seam correction in M_near. Summing both sides of (7) costs
less than 3/(1000m), uniformly across every floor transition.

After extracting the same exact L^2,L polynomial as N1-16, the finite
epsilon contribution of both singular strips and their retained h_J
constants is exactly

    epsilon*(2D0-B0*H_J)-B0*epsilon^2.                (8)

The g_J terms have unchanged coefficient B0, so cause no additional
finite-degree error. With |D0|<4, |H_J|<12, B0<=4/9 and
0<epsilon<=1/n, the absolute value of (8) is <14/n.

For clarity, the remaining constant after setting epsilon=0 and
performing (6) at delta is exactly
D0*(2k+H_J)+B0*(k^2+G_J), k=log(delta/pi), as stipulated in T.
The full remaining L coefficient is exactly b_M by N1-16, because
the regular strip coefficient is integrated over [0,delta] and the
outer A coefficient over [delta,pi]. No model constant or logarithmic
coefficient has been replaced.

## 2. The two lower strip boundaries have a small paired loss

At boundary delta the only regular difference from the limiting full
strip integrals is

    -(1/pi)*sum_s integral_0^(l_s) V_s(z)dz.           (9)

The full q_s log z and U_s integrals cancel in the limit because their
two coefficients are opposite. Pair them before taking absolute values.
Since |l_L-l_R|<=h, |U1|<4, and q=sin beta<=1/2, their lower losses are

    U term: <=4/n;
    q log term: <=L/(2*pi*m)<L/(6n).                 (10)

For the logarithm, both l_s lie between 1/n and 1, so the derivative
of z log z-z on the interval between them has magnitude <=L. This
does not bound either individual integral by its endpoint supremum.

The q_s part of f_s has the same paired bound L/(2*pi*m). For its
common regular part use |u_a(z)|<=pi*z/6 on these endpoint intervals
and max l_s<516/n. Hence

    (L/pi^2)*sum_s integral_0^(l_s)|u_a(z)|dz
        <15000*L/n^2 < L/(60n).                     (11)

The last inequality uses n>=10^6. The total of (10)-(11) is at most
[4+(7/20)L]/n. Including (7)-(8), the entire strip/outer lower-boundary
error, after exact coefficient extraction, has magnitude

    <[18+3/1000+(7/20)L]/n <5*(L+1)/n.              (12)

The last comparison holds already for L>=3, while here L>13.
No R*L/n, delta^-1*L/n or L-dependent truncation loss was paid.

## 3. Central ends, every collision hole and all special rows

The two upper endpoints of the filled ordinary intervals in N1-15 are
h*(m-3/2+t_s). Their distances from pi total exactly 2h, using
t_L+t_R=1. At most two actual noncentral collision holes each remove
one centered cell of length h. Thus the union of upper omitted ends
and collision cells, on two folded copies, has total measure <=4h.
It lies in z>pi-1/2-h/2>5/2. Permanent central rows are not duplicated
as holes; repeated collision indices are merged as in the model.

On this region the max formulas from N1-13 imply |A_s|<1. Indeed
cot(z/2)<1 and p,q<=1/2. The regular pole numerator satisfies
|N_s|<=8 and sin(z/2)>4/5, giving |N_s/[2sin(z/2)]|<5. N1-14 gives
the exact central decomposition I_s=d*log(pi-z)+Z_s, where
0<=d<=1/2 and |Z_s|<3. All removed sets have epsilon0=pi-z<1.
Therefore

    |H_s(L,z)|<L+6+(1/6)*[-log epsilon0].             (13)

For a set of total measure M<=4h on two copies, decreasing
rearrangement and concavity give

    integral_set -log epsilon0 <=M*[1+log(2/M)]
                               <=4h*(L+1),          (14)

since 2/(4h)=m/(2pi)<n. This includes the improper intervals reaching
epsilon0=0. Multiplying by 1/pi, (13)-(14) bound the complete omitted
outer integrals by

    [4*(L+6)+(2/3)*(L+1)]/m <10*(L+1)/n.             (15)

N1-16 and C02 prove that each exact nonendpoint special row, including
its actual polynomial collisions, contributes at most 2*(L+5)/m.
There are at most four such rows. N1-15/18 bound their entire Rhat/H8
discrepancy by <1/n at a phase, regardless of the number of block
transitions. Thus the actual model special-row contribution is bounded
in absolute value by

    [8*(L+5)+1]/n <50*(L+1)/n.                       (16)

This accounts for both permanent central rows, all actual collision
rows, their exact polynomial values and the prescribed H8 compaction.
The corresponding removed integrals were separately and completely
included in (15). These are the actual row-plus-hole terms in M_near;
there is no additional collision-mark or H8 artifact envelope to add.

## 4. Retained finite jump functions and complete finite identity

C02's component proof, with the exact one-summand q_R(t), proves

    |M_jump-J_infinity|<10*(L+1)/n,
    J_infinity=(2a*beta/pi^3)*[q_R(t_R)-q_R(t_L)].     (17)

That bound keeps m/n, both exact half-cell cutoffs, retained harmonic
constants and W_b integrals. It includes the possible beta=0 half-angle
cutoff step and does not substitute an infinite jump constant.

Combine the exact algebra in (6)-(9), N1-16's coefficient identity,
and T's definition. With R_n=M_near-B0*L^2-b_M*L, one obtains

    R_n-T=E_end+E_rest, |E_rest|<75*(L+1)/n.           (18)

The four bounds contributing to E_rest are 5 from (12), 10 from (15),
50 from (16), and 10 from (17). This identity has not discarded a cell,
collision, truncated constant or finite-h term. In particular only the
endpoint component is compared through its phase increment; all other
errors are uniformly bounded at the two actual phases.

Subtract (18) at the origin. The endpoint helper gives (1), even with
150 in place of the displayed conservative 200. Every discontinuous
artifact of F_n is already included in its exact model terms above.
N1-18's auxiliary Q_n need not be introduced.

## 5. The larger-budget near comparison and noncorner consequence

The exact N1-17 identity is

    M_near-Lambda_c=M_near(0,0,L)-Lambda_c+F_n-G_n.

The origin term is <3/14000 by N1-15 and S_n(0,0)=Lambda_c. Apply
(1) and the accepted limiting comparison (4). On rho<=1/2,
r2<=1/4 and beta<=1/2. Also (L+1)/n decreases for n>1, and
log(10^6)<14. Thus uniformly for every integer n>=10^6,

    M_near-Lambda_c
       <3/14000+1/50000+3/(2*10^9)
                      +11270/10^6+200*15/10^6
       <1/32.                                       (19)

The final comparison is rational. This proves (2) without a numerical
model evaluation. It does not establish the original 1/4096 tolerance.

For a noncorner odd center, C02's accepted projected theorem supplies
Delta>1/16 at these degrees. The exact primitive comparison is
lambda=S_n-Delta, while N1-15 gives S_n<M_near+3/14000. Consequently

    lambda<Lambda_c+1/32+3/14000-1/16
          =Lambda_c-869/28000,

which is (3). Full physical phase boxes require the same whole-box
radius bound maxabs(alpha)+maxabs(beta)<=1/2; intersection with that
diamond is insufficient. Actual corner centers remain separate.

## Checks and limits

All bounds above are analytic. No fit, numerical integral, projected-Q
pilot, finite degree extension, full cover or second model correction
was run. A cheap exact rational arithmetic audit can verify the scalar
budgets; it cannot replace independent reconstruction of the exact
strip cancellation and full cell accounting. The endpoint helper and
this full assembly require distinct mathematical review before adoption.

The tight C1 target at n>=10^6, actual corner comparison, far phases,
the finite gap and all-degree argmax remain OPEN here. Equation (3)
is only the explicitly stated near noncorner result.
