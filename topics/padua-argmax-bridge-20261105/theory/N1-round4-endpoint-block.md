# PD-T?argmax-bridge-codex-N1-08 — Complete compact endpoint block

ID kind: PD-T. Aliases: H4 endpoint compactification; joint singular sum
and finite polynomial rows. Split from: the full N1 compact profile,
which remains OPEN. Split into: N1-06 and N1-07 are its separately proved
supporting mesh and finite-row components, not parts of a full argmax
claim. Earlier reviewed statements remain unchanged.

## Statement

Use exactly the endpoint block E_(n,R,delta) preregistered in
../ideas/N1-round4.md. Explicitly, alpha,beta>=0, alpha+beta<=pi,
R>=2 is an integer, 0<delta<=pi/4, n>=ceil(2pi R/delta), m=n+1,
L=log n, v_r=(r*pi+beta)/m, z_r=min(v_r,2pi-v_r). Let

    P_R={0,...,R-1} union {2m-R,...,2m-1},
    X=(P_R union C_n) intersect {r:z_r<=delta},
    Y={r:z_r<=delta} minus X,

where C_n is the actual polynomial-collision row set, of cardinality
at most two. Use the corrected finite row norm R_r=sum_k |F_rk| and
N1-05's A(v),a,U0. The target block is

    E=(1/(nm))*sum_{r in X} R_r
       +(1/m)*sum_{r in Y}
          [A(v_r)*L+{U0+(4a/pi)*log z_r}/z_r].           (1)

Let b,c_mesh be the explicit coefficient functions in N1-06 and C_R the
finite polynomial-row profile in N1-07. Define

    c=C_R+c_mesh,       B0=4a/pi^2.

Then, uniformly throughout the closed phase diamond,

    |E-[B0 L^2+b L+c]| <= e4(n;R,delta),                (2)
    e4=e_mesh+e_rows+e_collision,
    e_collision=(2/m)*[7+(2/pi)*(3+2log(4m/R))]
                             +5/(n^2*m)+1/(nm).        (3)

Here e_mesh and e_rows are the explicit bounds in N1-06 and N1-07.
In particular this proves the preregistered H4 rate, with an explicit
constant and in fact only one growing logarithmic factor. Set

    A_R^*=4+(2R-1)*(10R+39),
    B_R^*=1+6*(2R-1),
    D_R^*=200*(2R-1)*(R+2)*(R+1)^2,
    K4=A_R^*+B_R^*+D_R^*/(8R)
                         +R+36+H_R^*+10pi/delta,

where H_R^* is N1-06's explicit constant. Then

    e4 <=K4*(1+log n)/n
        <=K4*(1+log n)^2/n.                            (4)

All coefficient formulas use finitely many terms and integrals depending
on R,delta, and convergent-series constants with proved tails. There is
no degree-dependent evaluation count. The sharper expression (3), rather
than the coarse K4 envelope, should be used in any later budget comparison.
The formula needs no microscopic transition variable or parity split;
the uniform sinc chart already includes those limits.

## Status, assumptions and dependencies

Overall status: **PROVED**, analytic developer proof; distinct review
pending. Exact real arithmetic. N1-06 proves the unperforated mesh
profile, N1-07 the finite endpoint-row profile, and N1-05 its integrable
constant-profile residual. N1-02/N2 supply the collision row count and
polynomial convention. The collision correction is proved below. No
numerical fit or source theorem is used.

## Proof

### 1. Which endpoint collision can occur

The coefficient identities of N1-05 use the offsets

    eta_-=1/2+(alpha-beta+v)/(2pi),
    eta_+=1/2+(alpha+beta-v)/(2pi).

For 0<v=z<=delta, only eta_-=1 can be an integer, and then
alpha-beta=pi-z and C=0, D=p/2. At that collision u=v modulo 2pi.
The polynomial-compatible limit of the vanishing-channel product is

    C*cot((u-v)/2) -> n*c_e/[2sin(z/2)] >=0,

where c_e=cos((alpha+beta)/2). The other contribution is
D cot z>=0. Thus the absolute value of their sum equals the sum of
their absolute values, including c_e=0.

On the other endpoint, v=2pi-z, there are two possible types, and they
can occur simultaneously. Both eta_-=1 and eta_+=0 hold exactly when
alpha=0 and beta=pi-z. In this case

    c_e=c_d=sin(z/2),       C=D=0.

The two pole samples u=v and u=-v modulo 2pi are distinct because
0<z<=pi/4. The polynomial-compatible sinc limits give F=n/2 at each
of these samples; all other samples vanish. Thus R_r=n. Meanwhile
I=0 and both integer-offset values Phi_L equal 1, so

    H(L,v)=(c_e+c_d)/[2sin(z/2)]=1,
    R_r/(nm)-H(L,v)/m=0.

This proves the zero-error case of (6) below without replacing either
finite pole contribution by a zero ordinary norm.

Otherwise the two right-end types occur separately.
If eta_+=0 then alpha+beta=pi-z, D=0, C=p/2 and u=-v modulo 2pi.
The vanishing-channel limit is n*c_d/[2sin(z/2)]>=0 and the other
term is C cot z>=0, so again there is no cancellation at that point.
If eta_-=1 then alpha-beta=-pi+z, C=0, D=p/2 and u=v modulo 2pi.
The pole limit is nonnegative but the other contribution is -D cot z.
Here 0<=alpha<=z/2, hence

    2|D cot z|=p cot z<=alpha/z<=1/2.                  (5)

The difference between the absolute value of these two finite terms and
the sum of their absolute values is therefore at most 1/2 in magnitude.
This explicitly retains the possible negative collision contribution.

These pole limits follow from the exact sine-coefficient identity and
sin(nt)cot t=n sinc(nt)T(t), as in N1-07. They are limits of the full
polynomial row on its actual phase mesh, not an independent substitution
of zero times an infinite cotangent. The two cotangent poles are distinct
because 0<z<=pi/4. The two closest rows are already in P_R, so the
remaining collision corrections never require z=0.

### 2. Comparison with the regularized profile at a collision

Let R_r be a collision row in the endpoint strips but outside P_R. If
both offsets are integers, the equality just proved gives zero error.
Otherwise there is exactly one pole channel on the row mesh. Its
vanishing coefficient contributes its single finite pole limit just
computed; its other n-1 samples are zero. The other channel is an
ordinary absolute cotangent norm with coefficient p/2. The cancellation
integral I is zero because one coefficient is zero. N1-04's profile
therefore gives, with H=N1-05's continuous regularized profile,

    |R_r/(nm)-H(L,v_r)/m|
       <=5/(2n^2*m)+1/(2nm).                          (6)

The first term bounds the nonvanishing channel's normalized pole-norm
error; its coefficient p/2<=1/2. The second term is (5) after dividing
by nm, and is unnecessary in the two nonnegative cases. The regularized
integer-offset profile equals 1 exactly, so its finite pole limit has
zero approximation error. This establishes (6) without replacing an
actual collision by an unproved continuation rule.

From N1-05,

    |H(L,v)-A(v)L-{U0+(4a/pi)log z}/z|
       <=7+(P/pi)[3+2log(4pi/z)], P=p+q<=2.            (7)

Outside P_R every endpoint distance satisfies z>=pi R/m. Thus (6)-(7)
bound the difference between the true normalized collision row and its
singular-model term in (1) by

    [7+(2/pi)(3+2log(4m/R))]/m
                          +5/(2n^2*m)+1/(2nm).

There are at most two such rows, proving the total error (3).

### 3. Assembly and explicit rate

For the left strip put r=k, t_L=beta/pi. For the right strip put
r=2m-1-k, t_R=1-beta/pi. Rows outside P_R are exactly
k=R,...,floor(delta*m/pi-t_s) on the two sides. If their collision holes
were temporarily filled with singular-model terms, their sum would be
N1-06's unperforated M_mesh. Restoring each actual collision row produces
exactly the correction bounded above. The first/last R polynomial rows
are N1-07's C_R plus its error e_rows. Hence (2)-(3) follow from these
two component theorems and the triangle inequality, with no missing
index, parity branch or endpoint factor.

For (4), use H_n<=1+L and n>=8R. N1-07 gives

    e_rows <=(A_R^*+B_R^* L)/n+D_R^*/n^2
       <=[A_R^*+B_R^*+D_R^*/(8R)]*(1+L)/n.

N1-06 supplies its bound (4). Finally R>=2, m=n+1, n>=16 imply
e_collision<=26(1+L)/n by log(4m/R)<=L+2 and pi>3.
Adding these bounds is precisely K4. Separate absolute phases extend
the definitions to the entire diamond, consistently with N1-01/05.

## Scope and next unresolved obligation

This closes H4 as it was preregistered: the singular endpoint mesh sums
and their finite exceptional rows are replaced jointly by a fixed-size
quadratic logarithmic family with an explicit full-phase remainder.
The earlier integrable strip residual still costs Q(P,delta), exactly
as in N1-05; it is not silently included in (1) or discarded.

The whole N1 model remains OPEN. Its central v=pi chart, interior outer
quadrature and complete S-minus-defect comparison are not supplied here.
In particular the previously proved E_(n,R) contains an O(1/R) error,
whereas the present finite-row estimate grows with R. Those costs must
be assembled before selecting a feasible R or an onset. The phase-only
chart itself survived; no bounded-offset correction has been spent.
There is no B3 PASS, certified new degree, effective n1 or B4 release.

## Checks and history

No mathematical computation or fit was performed. The separate child
developed the mesh lemmas and cross-checked the finite-row estimates;
it did not approve this assembly. Distinct review of the frozen files
is requested. The exact H4 target, error form and kill were recorded in
../ideas/N1-round4.md before this round's mathematical development.
2026-11-06, after parent-pushed bda45a4; Codex requested gpt-6-astra ultra.

2026-11-06, response to F1 in ../independent-checks-n1-round4.md:
the original proof omitted the simultaneous right-end double collision.
Its source is preserved at commit
`7e457c7fc54b32b45b0870d53a5fd4c37cd45fce`, original file SHA-256
`4a9b0f908f0b5cf12dbf56856bee47da47f860ef1c5f9fd5bf01f00676edc552`.
The explicit zero-error case above and the restriction of the subsequent
argument to one pole channel complete that proof case. The statement,
definitions, coefficient formulas and error bounds are unchanged.
Focused independent re-review is requested; this is a round-4 proof
response, not a new round or a correction of the model.
