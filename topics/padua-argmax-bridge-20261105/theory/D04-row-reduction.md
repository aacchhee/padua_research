# PD-T?argmax-bridge-codex-D04-row — A floor-free full-phase row reduction

ID kind: PD-T. Aliases: weighted H rows with exact endpoint constant;
linear-count outer reduction; D04 intermediate contract. Split from: D04
practical M_infty remainder, OPEN. Split into: none.

## Statement and exact model

Let integer R>=2 and n>=8R, m=n+1, L=log n. Work first on
alpha,beta>=0, alpha+beta<=pi, and put

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, P=p+q,
    D_n(u,v)=sum_{i+j<=n}h_i*h_j*cos(iu)*cos(jv),
    h_0=1, h_i=2 for i>0,
    G_n=D_n-cos(nu),
    delta_r=(1-r) mod 2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n,
    v_r=(r*pi+beta)/m,
    F_rk=(-1)^delta_r*G_n(u_rk,v_r)/2,
    R_r=sum_{k=0}^{n-1}|F_rk|,
    S_n=(nm)^-1 sum_{r=0}^{2m-1}R_r.

The subtracted cos(nu) is the exceptional highest first-coordinate mode;
it is part of every actual polynomial row. Use exactly the special set

    A_R={0,...,R-1} union {2m-R,...,2m-1}
           union {m-1,m} union {all exact polynomial-collision rows},
    O={0,...,2m-1} minus A_R.

A polynomial collision means u_rk-v_r or u_rk+v_r belongs to 2pi*Z for
some k. There are at most two such board points and at most two added
rows, so |A_R|<=2R+4. Their values are the finite polynomial values, not
limits of separately unweighted pole terms.

For 0<v<2pi, v!=pi, retain exactly N1-05's actual weighted profile:

    c_e=cos((alpha+beta)/2), c_d=cos((alpha-beta)/2),
    eta_-(v)=1/2+(alpha-beta+v)/(2pi),
    eta_+(v)=1/2+(alpha+beta-v)/(2pi),
    C_v=(p-q-2a cot(v/2))/4,
    D_v=(p+q+2a cot(v/2))/4,
    I(C,D,v)=integral_0^pi
       (|C cot X+D cot(X+v)|-|C cot X|-|D cot(X+v)|)dX,
    Phi_L(t)=sin(pi*t)[2L-psi(t)-psi(1-t)-2log pi]/pi,
                                                   0<t<1.

Extend Phi_L periodically and continuously, with Phi_L(integer)=1.
Its definition on (0,1) includes the nonnegative sine there. Put

    H(L,v)=[c_e Phi_L(eta_-(v))+c_d Phi_L(eta_+(v))]
                     /[2sin(v/2)]+I(C_v,D_v,v)/pi.

The integral is the ordinary bounded piecewise cotangent cancellation
integral, with arbitrary values at the finitely many poles. Ordinary
rows have v_r!=pi and their two sample offsets are noninteger.
Let Delta_R=E_infty-E_R be the exact continuous endpoint constant of
D04-reference-matching.md, equivalently its absolutely convergent series
(1). Define the new intermediate object, not a change to any old model,

    K_D04(n,R;alpha,beta)
      =(nm)^-1 sum_{r in A_R} R_r
                  +(1/m)sum_{r in O}H(L,v_r)+Delta_R.          (1)

Then

    |S_n-K_D04|<=E_D04(n;alpha,beta),                          (2)
    E_D04={ [52a/pi^2+352P/(3pi)]H_n+7a+2P/pi }/n
                               +10/n^2+20a H_n/(pi*n^2),     (3)

where H_n=sum_{k=1}^n 1/k. These bounds hold on the entire closed phase
diamond by separate absolute phases. In particular they cover a=0,
axes, vertices, moving numerator zeros, coefficient sign switches and
all exact polynomial collisions. No fixed-R error floor occurs.

The explicit choice R=2 is valid for every n>=16. It retains at most
eight exact polynomial rows and at most 2(n+1) ordinary H evaluations.
There is no conclusion for n<16 from that choice, and no all-degree
argmax or practical M_infty-rate conclusion from (2).

Status: **PROVED**, written analytic developer result, distinct review
pending. The target S_n-M_infty rate remains separately **OPEN**.

## Dependencies

- D03-cancellation-perturbation.md, frozen SHA256
  `3b4d989393eb942b5527be32f89254fcef6b3b3cc157a37960848780c74d290f`:
  distinct Astra xhigh acceptance reported by root; its bounded difference
  quadrature is the only D03 estimate used here.
- D04-reference-matching.md and its separate half-line theorem: the exact
  nondecaying reference constant and its explicit finite-n remainder.
- N1-02: actual two-channel identity, special set and collision count.
- N1-04/05: the weighted single-pole expansion and coefficient sum.
- N1-07/C08: the unchanged finite endpoint profiles/constants used by
  the reference-matching theorem. No old proof or model is edited.

## Proof

For an ordinary row, with X=(u-v_r)/2, the exact corrected polynomial
identity is

    F=C_v cot X+D_v cot(X+v_r).

Define its cancellation g by subtracting the two individual absolute
pole terms, and let

    T_r=sum_k g(X_rk)-(n/pi)*I(C_v,D_v,v_r).

The exact row decomposition, combined with the weighted pole theorem,
gives

    R_r/n=H(L,v_r)+T_r/n+epsilon_r,
    |epsilon_r|<=5(|C_v|+|D_v|)/n^2.

The full nonendpoint coefficient sum is at most
2m+4am H_n/pi, as proved in N1-01/05. Ordinary rows are a subset of
these rows. Consequently their total normalized epsilon is bounded by

    D_n^pole=10/n^2+20a H_n/(pi*n^2).                (4)

Here D_n^pole is an error label, distinct from the polynomial D_n.
All special rows in (1) are exact, so no row approximation or r_n term
is charged.

Put w=a cot(v/2)/2 and use the bounded reference g0=g(-w,w,v;X).
D03's accepted difference-quadrature estimate gives

    |(nm)^-1 sum_{r in O}(T_r-T0_r)|
                                <=112P H_n/(pi*n).  (5)

The D04 reference theorem gives

    |(nm)^-1 sum_{r in O}T0_r-Delta_R|
       <={[52a/pi^2+16P/(3pi)]H_n+7a+2P/pi}/n.       (6)

Combine the exact special rows, (4), (5), and (6). The coefficient of
P H_n/n is 112/pi+16/(3pi)=352/(3pi), proving (2)-(3).
The inherited separate phase evenness gives the other quadrants; the
two unequal coordinate meshes have not been interchanged.

## Evaluation obligations and limitations

Equation (1) is a countable explicit reduction to O(n) outer profile
values and a bounded number of exact rows. It is still degree-dependent.
Each exact row contains n actual polynomial values; a literal evaluation
of the displayed polynomial has further degree-dependent cost. No linear
end-to-end arithmetic or runtime bound is asserted. An efficient row
primitive, a rigorous evaluation of the bounded cancellation integral,
weighted digamma products and Delta_R, and outward arithmetic errors all
need a separately specified implementation and acceptance contract.

For a phase box, exact collision decisions cannot be inferred from its
center. A validated evaluator must enclose all changing pole products
and special membership, or split/retain additional actual rows with a
proved corresponding comparison. This theorem gives the pointwise
mathematical contract; it is not an interval certifier or a phase cover.
Likewise, replacing R_r by an approximation needs its own added error.
No sampled equality or finite floating precision is used here.

The ordinary outer profile sum and retained exact rows still need a
uniform comparison with D02's M_infty to obtain a practical compact
remainder. The auxiliary constant Delta_R cancels the reference cutoff
bias only; it does not replace that missing outer comparison. The old
M_far at R64,delta=.01 retains D01/D02's nondecaying cutoff bias. No old
near correction, certified degree range, producer or certificate changes.

## Verification and history

No native run, scalar numerical experiment, full-board calculation,
quadrature, fitting or validated phase cover was executed. The analytic
constants are supplied for distinct review; the developer does not
approve their use. Candidate and attempt are in the D04-owned records.
2026-11-06, root-supplied input 2db4a226dad798491be3ec2fe5ce0238e21cfaec; parent-requested Astra ultra,
serving metadata unexposed.
