# PD-T?argmax-bridge-codex-N1-09 — Coupled finite-h and pole-jump row model

ID kind: PD-T. Aliases: corrected cancellation quadrature; exact finite-h
endpoint rows; inverse-square cutoff error. Split from: the single
round-5 corrected model contract; its full outer compactification remains
OPEN. Split into: none. Previous proofs and their scoped budget failure
are unchanged.

## Statement and corrected model

Let alpha,beta>=0, rho=alpha+beta<=1/2, n>=8R, and R>=2 be integers.
Put m=n+1, L=log n, a=(cos alpha+cos beta)/2, p=sin alpha,
q=sin beta, P=p+q. Use N1-02's special rows A_R (first/last R, the two
central rows and every actual polynomial-collision row). Use its exact
definitions C_r,D_r,t_r^-,t_r^+,I and Vhat_r, with the corrected
exceptional mode. All phase extensions below use separate absolute
phases, not an exchange of the two meshes.

Replace the endpoint rows in A_R by the exact finite-h formulas below.
Other rows in A_R retain N1-01's Rhat_r. For an ordinary row let
z_r=min(v_r,2pi-v_r). If z_r<=pi/2, add to Vhat_r

    J_r=-j_0*B1(t_r^-)-j_1*B1(t_r^+),
    B1(t)=t-1/2, 0<t<1,
    j_0=2 sign(C_r)*D_r*cot v_r,
    j_1=-2 sign(D_r)*C_r*cot v_r.                      (1)

For pi/2<v_r<3pi/2 add zero. Actual collision rows are special, so no
endpoint value of B1 at a sampled pole is required. Define K5 to be
the sum of these rows divided by nm. Then

    |S_n-K5|<=r_n+E5(n,R),                             (2)
    E5= a*m^2/[4n^2(R-1)^2]
       +P*pi*m/[8n^2(R-1)]+P*H_n/n+4a/n,             (3)

where r_n=[7pi^4/1800+7pi^3 H_n/900]/n^4 is N1-01's bound.
This is uniform on the entire stated half diamond, including zero phases
and all central collisions. The exact finite-h rows replace N1-07's
asymptotic row approximation; its e_rows is not added to (2).

For R=128 and every n>=10^6,

    r_n+E5(n,128)<1/8192.                              (4)

This satisfies the first allocated error portion of the round-5
contract. K5 still contains an ordinary outer sum until its separate
compactification is proved. Equation (4) is not B3 PASS, an upper bound
on K5's maximum, or an effective argmax onset.

### Exact finite-h endpoint terms

For the left endpoint take effective phase b=beta and r=0,...,R-1;
for the right take b=-beta and r=1,...,R (original row 2m-r). Write

    w=r*pi+b, v=w/m, delta_r=(1-r) mod2,
    F_j=(-1)^delta_r G_n((j*pi+alpha)/n,v)/2,
    T_r^(b)=n*[a-(sin b/2)*cot(w/(2m))].

The exact absolute rows are

    R_0^(beta)=-T_0^(beta),
    R_r^(b)=-T_r^(b)
                  +2*sum_{j=-r+1,-r+3,...,r-1} F_j,   (5)

with T_0^(0)=n(a-m). These are O(R^2) finite polynomial-compatible
terms independent of n. They are retained as functions of h=1/n, rather
than replaced by their h=0 values.

## Status and dependencies

Overall status: **PROVED**, analytic developer proof; independent review
pending. N1-01/N2 supply the corrected finite row and signed identity;
N1-02 supplies the cotangent norm approximation, central-row convention
and coarse cancellation bound. The jump signs, finite-h signs and new
second-order quadrature estimate are proved here. No computation, fit
or external theorem is used. Candidate: ../ideas/N1-round5.md.

## Proof

### 1. Uniform positive numerator and the finite row indices

On rho<=1/2,

    a>=15/16, P<=1/2, 2a>P.

After folding v to z=min(v,2pi-v), its effective beta sign may change,
but the complete numerator

    2a(1+cos z)-p sin u+(sin b)sin z

is strictly positive for 0<=z<=pi/2: it is at least 2a-P>0.
Consequently the sign of F is exactly the sign of cos u-cos z.
This conclusion concerns the complete corrected kernel, not either
cotangent channel separately.

For the finite endpoint rows, w<=pi R, so z=w/m<=pi/8. Among integers
j opposite in parity to r, the positive-denominator indices are exactly
j=-r+1,-r+3,...,r-1. For instance their extreme positive index obeys

    nv-[(r-1)pi+alpha]
       =pi+b-alpha-w/m>=pi-1/2-pi/8>0.

The negative extreme similarly has nv+z_j>=pi-1/2-pi/8. The first
excluded indices have separation at least pi-1/2 in the opposite
direction. Thus all inequalities are strict and independent of phase
or parity. For r=0 every odd-grid denominator is negative. The exact
signed-row identity then gives (5). At beta=0 its complete-row limit is
T_0=n(a-m), and no pole factor is evaluated separately. There are no
endpoint collisions in these finite rows on this half diamond.

### 2. Exact jumps and removal by periodic ramps

For generic C,D,v use N1-02's function

    g(x)=|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|.

Its one-sided jump at x=0 is 2 sign(C)D cot v: a dominant C cot x
has opposite signs on the two sides, and subtracting the other absolute
value contributes no jump. At x=-v, the other finite channel is
-C cot v, so the jump is -2 sign(D)C cot v. These are exactly (1).

Let q_b(x)=1/2-frac((x-b)/pi) away from its jump. It has jump +1,
mean zero and constant derivative -1/pi off the jump. On an n-point
shifted grid avoiding b, direct summation gives

    sum_k q_b(x_0+k*pi/n)=-B1(frac((x_0-b)/(pi/n))).

Subtract the two jump amplitudes times these ramps from g. The resulting
periodic function f is continuous, with its continuous values assigned
at the two former jumps. Its derivative off breakpoints equals g'_reg
plus a constant; hence Var(f')=Var(g'_reg). Its mean is I/pi. Thus the
exact grid contribution of the subtracted ramps is J_r in (1).

### 3. Endpoint derivative variation and corrected quadrature

After folding or translating the endpoint row, its coefficients have
C<0,D>0, because 2a cot(z/2)>=2a>P. For 0<z<pi/2 the positive-numerator
fact in section 1 fixes every minimum in g: its only nonzero pieces are

    g(x)=-2D cot(x+z),  0<x<pi/2-z,
    g(x)=-2C cot x,     pi/2<x<pi-z.                  (6)

Indeed on each of those intervals the two channels oppose, while the
complete F is negative. Elsewhere the channels have the same sign.
The derivatives of the two pieces are 2D csc^2(x+z) and
2C csc^2 x. Including their jumps to the zero derivative outside the
pieces, their variations are respectively 4D csc^2 z and
4|C| csc^2 z. Therefore

    Var(g'_reg)=4(|C|+|D|)csc^2 z.                    (7)

At z=pi/2 the pieces are empty and the corresponding upper bound still
holds. Reflection/translation preserves variation, so (7) bounds the
right endpoint as well. No arbitrary-C,D derivative claim is being made
through a coalescing root: positivity of the complete numerator fixes
the pieces on this stated phase domain.

For a continuous periodic f with derivative of bounded variation, center
a cell of length h_0=pi/n at each sample. Taylor's integral remainder,
or integration against the measure df', gives the cell error kernel

    (h_0/2-|x-x_k|)^2/(2h_0),

whose magnitude is at most h_0/8. Constant and linear terms cancel.
Summing the cells bounds the sample-sum minus n/pi times its integral
by h_0 Var(f')/8. Applied to the ramp-subtracted f, this proves

    |sum_k g(x_k)-(n/pi)I-J_r|
       <=[pi/(2n)]*(|C|+|D|)csc^2 z.                 (8)

### 4. Summing the corrected and uncorrected regions

On either endpoint |C|+|D|<=a cot(z/2)+q/2<=2a/z+q/2.
For z<=pi/2, csc^2 z<=pi^2/(4z^2). Outside A_R let
k=min(r,2m-r-1)>=R; then z>=pi k/m and each k occurs at most twice.
Divide (8) by nm, sum both endpoints, and use

    sum_{k=R}^infinity k^-3<=1/[2(R-1)^2],
    sum_{k=R}^infinity k^-2<=1/(R-1).

The result is

    a*m^2/[4n^2(R-1)^2]+q*pi*m/[8n^2(R-1)],

bounded by the first two terms of (3).

In the central region pi/2<v<3pi/2 use N1-02's original row error
P/|sin v|+a csc^2(v/2). Excluding rows m-1,m gives a distance from pi
of at least pi*l/m with positive integer l, each occurring at most
twice. Sine chords yield sum 1/|sin v|<=m H_n. Also csc^2(v/2)<=2
and there are at most m+1 central rows. After division by nm their
total is at most P H_n/n+4a/n. Every exact collision is special and
uses its actual polynomial contribution via N1-01.

The remaining single-pole and special-row approximations are the same
as in N1-02, except that endpoint rows now have zero approximation error.
Their combined error is therefore still at most r_n. This proves (2).

### 5. Preregistered first error budget

For n>=10^6, H_n/n<=(1+log n)/n<15/10^6; the last scalar function is
decreasing for n>1 and log(10^6)<14. Also m/n<=9/8, a<=1 and P<=1/2.
For R=128, the first term of E5 is less than 1/40000, its central
terms are less than 1/80000, and its second term together with r_n is
less than 1/10^6. The elementary comparison

    1/40000+1/80000+1/10^6 <1/8192

proves (4). For the r_n estimate one may use pi<4,H_n<=n in N1-01;
the resulting terms of orders n^-3,n^-4 are already below 10^-12.
All constants come from the written inequalities, not a fit or sampled
comparison. This test evaluates only the first error allocation.

## Scope, checks and history

This single coupled correction changes both certificate losses:
O(1/R) becomes O(1/R^2), and the finite endpoint rows are exact functions
of h rather than incurring N1-07's old row bound. It thereby escapes the
specific unchanged-certificate floor. It does not erase that earlier
negative result or claim a second model correction.

The endpoint outer reduction, its allocated error, central/interior
outer compactification and the maximum comparison remain separate
obligations. No full B3 PASS, B4 release or explicit argmax n1 follows.
The model is defined here on rho<=1/2, the current proved N5 budget
domain; the older full-diamond statements remain unchanged elsewhere.

No mathematical computation was performed. An independent adversarial
check of the frozen contract was requested by root while this proof was
written; distinct review of this exact file remains pending. 2026-11-06,
round 5 after fc8c288, requested gpt-6-astra ultra. The contract and all
retained correction terms preceded the proof in ../ideas/N1-round5.md.
