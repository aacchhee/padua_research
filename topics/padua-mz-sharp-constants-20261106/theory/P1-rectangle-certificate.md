# PD-T541 — finite rectangle certificates for the norm

2026-11-06 ID history: `PD-T?mz-sharp-codex-P1-03` → `PD-T541`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: integrated scalar rows; semicircle endpoint integrals;
positive-vector upper certificate.
Split from: the numerical-certificate part of the supplied P1 route.
Split into: a numerical instance and execution record remain separate.

## Statement, dependencies and status

Use D,H,B,A=-B and r=||A|| from P1-elliptic-kernel.md and
P1-positive-spectrum.md. Write nu(da)=a da. For 0<=u<v<=1 put

    E_[u,v](s)=[sqrt((v^2-s^2)_+)-sqrt((u^2-s^2)_+)]/pi.

For t=0,1 define kappa_0=1, kappa_1=2 and

    I_t(a;[u,v]) = kappa_t/pi^2 * integral_0^pi
      [sqrt((v^2-(t-a cos(theta))^2)_+)
       -sqrt((u^2-(t-a cos(theta))^2)_+)] dtheta.       (1)

Then, almost everywhere for 0<a<1,

    I_0(a;[u,v])=integral_u^v S_all(a,a') a' da',
    I_1(a;[u,v])=integral_u^v S_alt(a,a') a' da'.       (2)

These are integrals of the scalar kernels against nu, not pointwise
bounds on the singular S_all. They are finite nonnegative continuous
functions of a. In particular

    0<=I_t(a;[u,v])<=kappa_t sqrt(v^2-u^2)/pi.         (3)

Exact tensor products of (1), followed by finitely many certified
one-dimensional integral bounds, give the upper/lower norm certificate
below. Its correctness is **PROVED** as analytic development, subject to
independent reconstruction. No numerical instance is supplied or claimed
to achieve three digits. Candidate ../ideas/P1-rectangle-certificate.md
preceded this extension. The predecessor and elementary functional facts
are those already named in the P1 gate; no source-paper theorem or
numerical premise is added.

## Exact removal of the source singularity

The scalar proof already established w_a(s)=1_{|s|<a}/(pi sqrt(a^2-s^2)),
q_aa'=w_a*w_a', S_all=q_aa'(0), and S_alt=2q_aa'(1).
Nonnegativity permits Tonelli. Direct integration gives

    integral_u^v a' w_a'(s) da' = E_[u,v](s).

Consequently I_t=kappa_t (w_a*E_[u,v])(t). The substitution
s=a cos(theta) in the arcsine probability integral is exactly (1).
There is no endpoint mass, elliptic diagonal value, or conditional series
exchange in this calculation. Null exceptional point pairs do not affect
the source integral.

The function E is nonnegative. Its supremum is sqrt(v^2-u^2)/pi:
as |s| increases to u the difference of square roots increases, and from
u to v the remaining square root decreases. Convolution with the
probability density w_a proves (3). The explicit moduli below establish
continuity even at a=0 and a=1 if these endpoint values are defined by
(1); only the interior values enter H.

For a source rectangle R=U x V inside the unit square define

    P_R(a,b)=8[I_1(a;U) I_0(b;V)
                  +I_0(a;U) I_1(b;V)].               (4)

The positive kernel A is also defined on the square product by its same
formula. Tonelli and its tensor form prove exactly

    P_R(x)=integral_R A(x,y) a'b' da' db'.             (5)

Equation (5) does not assert R is contained in D. Using a full rectangle
that crosses the triangle boundary produces an upper bound on its
intersection with D; it must not be used as an equality for that
intersection.

## Elementary uniform enclosures

For real p,q, |sqrt(p_+)-sqrt(q_+)|<=sqrt(|p-q|). For
0<=a,a_tilde<=1 and theta,theta_tilde in [0,pi],

    |(t-a cos(theta))^2-(t-a_tilde cos(theta_tilde))^2|
       <=2(t+1)(|a-a_tilde|+|theta-theta_tilde|).

It follows by treating the two square roots separately that

    |I_t(a;U)-I_t(a_tilde;U)|
      <=[2 kappa_t/pi] sqrt(2(t+1)|a-a_tilde|).       (6)

In particular the constants are 2 sqrt(2)/pi for t=0 and 8/pi for
t=1, each multiplying sqrt(|a-a_tilde|). These are uniform, deliberately
coarse moduli; no small derivative near a cutoff is presumed.

There is also an explicit quadrature enclosure. Partition [0,pi] into
intervals T_l, choose theta_l in T_l, and let rho=max_l sup_{theta in T_l}
|theta-theta_l|. Replacing the integrand in (1) by its value at theta_l
on each T_l incurs absolute error at most

    [2 kappa_t/pi] sqrt(2(t+1)rho).                   (7)

Point evaluations themselves must be enclosed with rigorous bounds for
pi, cos and square root. Alternatively interval evaluation of the two
square roots on each angular interval, clipped to the positive bounds
0 and sqrt(v^2-u^2), gives direct Darboux bounds; their weighted sum is
rigorous without using (7). Every cutoff and angular endpoint is
included by the positive-part definition. Refining (7) alone may be
expensive; its purpose is an explicit termination modulus, not a claim
of a practical three-digit budget.

Bounds for I_t on an entire target interval follow from a point bound
and (6). Bounds for P_R on a target rectangle follow by multiplying
nonnegative intervals in (4). For outer integration, partition a target
interval into W_l, use its exact nu-mass
(right(W_l)^2-left(W_l)^2)/2, and bound I_t on W_l using (6) or interval
evaluation. This gives finite bounds for

    J_t(U,V)=integral_U I_t(a;V) a da.                (8)

All formulas above allow rational interval endpoints. The only
transcendental enclosures needed in this reduction are elementary pi,
cos and square root. Direct evaluation of an elliptic integral is not a
certificate dependency.

## A finite upper certificate with all triangle cells accounted for

Take a finite rectangular grid partition of the unit square; discard
cells whose intersection with D has zero measure. Label the remaining
rectangles R_i and put C_i=R_i intersect D. Choose strictly positive
numbers h_i and set h(x)=h_i for x in C_i. Thus h is bounded, belongs to
H, and is positive almost everywhere. Shared grid edges are null.

For every i, rigorously establish a finite number Q_i satisfying

    sum_j h_j P_R_j(x) <= Q_i   for every x in C_i.    (9)

It is sufficient, and often simpler, to bound the left side on all of
R_i. Bounds (3), (6), (7) and (4) provide a literal finite way to check
(9). Full rectangles at the source boundary are included with their
positive contributions; none may be silently dropped for this upper
bound. Equation (5) gives

    Ah(x)<=sum_j h_j P_R_j(x)<=Q_i,
    U=max_i Q_i/h_i,             Ah<=U h.             (10)

The weighted 2ab inequality now proves r<=U. Indeed, symmetry and
nonnegativity of A give for real or complex f,

    |<f,Af>| <= integral integral A(x,y)|f(x)||f(y)| dmu(x)dmu(y)
      <= integral |f(x)|^2 [Ah(x)/h(x)] dmu(x)
      <= U||f||^2.

The middle inequality is 2pq<=p^2+q^2 with
p=|f(x)|sqrt(h(y)/h(x)), q=|f(y)|sqrt(h(x)/h(y)), followed by symmetry.
The absolute quadratic form characterizes the norm for a selfadjoint
operator, so no finite eigenvalue computation or irreducibility premise
is needed for this upper bound.

## A finite lower certificate

Let F be the indices of grid rectangles wholly contained in D, up to
null edges. For i,j in F, (5) gives the exact positive entry

    M_ij=integral_R_i integral_R_j A(x,y) dmu(y)dmu(x)
       =8[J_1(U_i,U_j) J_0(V_i,V_j)
            +J_0(U_i,U_j) J_1(V_i,V_j)].             (11)

Use (8) to prove lower bounds m_ij<=M_ij with m_ij>=0. Then

    N_L=sum_{i,j in F} h_i h_j m_ij <= <h,Ah>.

The omitted boundary cells contribute nonnegative terms, so their
omission is valid only for this lower bound. The exact denominator is

    d=||h||^2=sum_i h_i^2 mu(C_i)>0.

For rational grid endpoints and rational h_i, d is rational: on a cell
[u,v]x[s,t], integrate a/2 times
[(min(t,1-a))^2-s^2] where a<1-s, with breakpoints 1-t and 1-s. Each
piece is a polynomial integral with rational limits. Therefore

    L=N_L/d <= <h,Ah>/||h||^2 <= r <= U.              (12)

Using additional inscribed subrectangles in boundary cells can improve
the lower bound, but every such improvement needs its own proved
positive decomposition. The simple version (11)-(12) already defines a
complete finite certificate.

## Output obligations and limits

Equations (9)-(12) specify what a numerical developer must prove. The
published protocol must fix the rational grid, positive h_i, rounding
model, quadrature enclosure, resource cap and desired rounding test
before executing it. A floating eigenvector may suggest h_i, but is not
evidence for any inequality in (9)-(12). Its use must be covered by that
protocol, and all final h_i must be explicit exact positive inputs.

For a claimed three-digit value of c_minus, the final rational enclosure
[-U,-L] must lie inside one stated rounding bin, with independently
checked strict endpoints as needed by the chosen rounding convention.
A narrow-looking spectrum or stable mesh does not satisfy this test.
No particular h, mesh size, cost or successful rounding bin is asserted
here. If the explicit enclosure stays broad within the cap, certified
digits remain OPEN; the analytic kernel and norm identity are unaffected.

## History

2026-11-06, bounded round 3, analytic only. Requested model gpt-6.1-sol
xhigh; runtime model/effort metadata unexposed. Rules/input
0205690b9c4e959a28e949083e9a1808735abf4b. Candidate saved before deriving
the extension. No code, numerical computation or accepted-S3 edit.
