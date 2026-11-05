# PD-T?argmax-bridge-codex-N1-01 — Full-diamond absolute-row quadrature model

ID kind: PD-T. Aliases: two-phase row assembly; moving negative sets.
Prior provisional alias: PD-T?argmax-bridge-N1-01.
Split from: none. Split into: none. The compact-in-degree N1 target remains OPEN.

## Statement (written before computation)

Let n>=2, m=n+1, N=nm, h=pi/n and a=(cos alpha+cos beta)/2.
Define the explicit row model M_n below. Using N5's proved
partial-cotangent quadrature lemma with error 7 q h^4/7200, one has

    |S_n(alpha,beta)-M_n(alpha,beta)| <= r_n,
    r_n = 7*pi^4/(1800*n^4) + 7*pi^3*H_n/(900*n^4),

uniformly on |alpha|+|beta|<=pi, including every transition and collision.
Here H_n=sum_{k=1}^n 1/k can be replaced above by 1+log n.

This is an explicit approximation with degree-dependent outer sums. It
is **not** the required fixed-size compact model M(alpha,beta,log N), does
not bound its own maximum, and does not certify any new degree or threshold.

## Definitions

Use PD-T364's corrected finite polynomial G_n=D_n-cos(nu), odd periodic
board, and S_n=(nm)^-1 sum |F| with F=(-1)^j G_n/2. By separate phase
evenness it is enough to define the model for alpha,beta>=0,
alpha+beta<=pi, then use absolute phases elsewhere.

For r=0,...,2m-1 put delta_r=(1-r) mod 2,
u_k=(delta_r*pi+alpha)/n+2k*pi/n (0<=k<n), v_r=(r*pi+beta)/m,
and F_rk=(-1)^delta_r G_n(u_k,v_r)/2. Put

    A=cos alpha+cos beta, p=sin alpha, q=sin beta,
    C_r=(p-q-A*cot(v_r/2))/4,
    D_r=(p+q+A*cot(v_r/2))/4.

For the interior row range 1<=r<=2m-2, v_r lies in (0,2pi),
and these coefficients are finite. Write

    T_r=n*[a-(q/2)*cot(v_r/2)].

Let Cset_r={k: cos u_k=cos v_r} be the exact collision indices. At them
F is defined by the finite polynomial, equivalently
(-1)^delta_r*[P_n'(cos v_r)-cos(nu_k)]/2, P_n=T_(n+1)+T_n.
At endpoints use the polynomial directly.

For regular indices let E_r be exactly those where F_rk<0. They are
specified without evaluating the high-degree kernel: put

    c_r=A*(1+cos v_r)+q*sin v_r,
    B_r={u in [0,2pi): cos u<cos v_r},
    I_r={u in [0,2pi): p*sin u>c_r}.

Then E_r consists of the grid points (with u reduced modulo 2pi) in
B_r symmetric-difference I_r, excluding Cset_r and all exact numerator
zeros. This exclusion is a fixed convention: inclusion would not change
the exact row sum but can change the approximate model within its error.
Each set is a union of a bounded number of intervals, with endpoints
given by arccos(cos v_r) and the solutions of sin u=c_r/p. For p=0,
I_r is the full circle if c_r<0 and empty if c_r>=0. Thus the formula
also specifies p=0 and the tangent thresholds c_r=+/-p.

For either sign, map x_k=(u_k+/-v_r)/2 modulo pi into (0,pi) on E_r.
Partition the resulting selected progression into contiguous blocks,
breaking at the wrap and any excluded collision. Each step is h; each
selected point occurs once, with at most n points in each channel.

N5 supplies a block approximation Q_h to the cotangent sum. Specifically,
for a block x_i=h(i+t), i=b,...,e, with l=x_b-h/2, z=x_e+h/2, let

    w(x)=cot x-1/x+1/(pi-x),
    W(x)=log(sin x/[x*(pi-x)]),
    Q_h = (1/h)*sum_{i=b}^e [1/(i+t)-1/(n-i-t)]
          +[W(z)-W(l)]/h -(h/24)*[w'(z)-w'(l)].

W,w' have their removable values at 0,pi. The displayed harmonic
terms are exact (or evaluated by shifted harmonic/digamma differences).
Define Q_r^- and Q_r^+ by summing the block formulas in each channel.
Empty channels have Q=0.

Define

    Rhat_r=T_r-2*C_r*Q_r^- -2*D_r*Q_r^+
            +2*sum_{k in Cset_r} max(-F_rk,0),

and retain the two endpoint rows exactly:

    M_n=(1/N)*[sum_k |F_0k|+sum_k |F_(2m-1),k|
                         +sum_{r=1}^{2m-2} Rhat_r].

## Assumptions and status

Overall status: **PROVED**, by the analytic assembly below using
[N5's proved lemma](N5-partial-cotangent.md). This is a developer claim;
distinct mathematical review and Claude audit are pending. Exact real
arithmetic. The model is defined before
fits or implementation tests; there is no empirical remainder assumption.
The two-phase signed-row identity and algebraic assembly below are routine
lemmas, not separate global results. PD-T099 remains OPEN.

## Depends on

PD-T364 for S and the corrected kernel; PD-T216/T217 for its numerator;
PD-T226 for the signed-row/cotangent precedent. The concurrent N2 record
`N2-row-decomposition.md` owns the general two-phase row decomposition;
the independently derived identity below is verification material, not
a separate new claim. N5's independently owned
partial-cotangent remainder is PD-T?argmax-bridge-codex-N5-01,
equations (2)–(4). The N2 identity has provisional ID
PD-T?argmax-bridge-codex-N2-01.
The N1 developer read and reconstructed its full proof before this upgrade;
this is dependency verification, not an independent audit of either author.

## Proof of assembly

The exact numerator gives, away from collisions,

    F_rk=C_r*cot((u_k-v_r)/2)+D_r*cot((u_k+v_r)/2).

Finite Fourier summation over k kills first-coordinate frequencies
1,...,n-1 and retains frequencies 0 and n with the exceptional coefficient
one. Therefore

    sum_k F_rk = n/2*[(-1)^delta_r D_n^(1)(v_r)+cos alpha],
    D_n^(1)(v)=1+2*sum_{j=1}^n cos(jv).

Since sin((n+1/2)v_r)/sin(v_r/2)
=(-1)^r*[q*cot(v_r/2)-cos beta], this is T_r. This identity uses
the finite Fourier polynomial at all removable points.

The sign of F at regular indices is the sign of
(c_r-p*sin u_k)/(cos u_k-cos v_r). Thus the stated symmetric-difference
set is exact; no constant-sign assumption on a phase region is made.
The identity sum |F|=sum F+2 sum(-F)_+ yields the exact row formula
with Q replaced by the true cotangent partial sums. The explicit collision
negative parts are necessary because a collision need not be assigned a
rational value or assumed positive at arbitrary phases.

Each cotangent channel contains at most n points. N5's lemma therefore
bounds its total error by e_n=7*n*h^4/7200, independently of the number
and placement of sign blocks. The r-th row error is at most
2*e_n*(|C_r|+|D_r|).

Now |C_r|+|D_r|=max(p,|q+A*cot(v_r/2)|)/2
<=1+a*|cot(v_r/2)|. For 1<=r<=2m-2 and beta in [0,pi],
the angular distance of v_r from {0,2pi} is at least
pi*min(r,2m-r-1)/m. Using |cot(v_r/2)|<=2/dist(v_r,{0,2pi}) gives

    sum_{r=1}^{2m-2}|cot(v_r/2)| <= (4m/pi)*H_(m-1),
    sum_r (|C_r|+|D_r|) <=2m+(4a*m/pi)*H_n.

The distance integers are 1,...,m-1, each twice. Division by N yields

    |S-M| <= [7*pi^4/(3600*n^4)]*[2+(4a/pi)*H_n] <= r_n.

The extracted rows have no approximation error. This covers beta=0 and
beta=pi, alpha=0 and alpha=pi, a=0 on the boundary, exact numerator zeros,
grid wraps, tangent sign thresholds and every exact collision. At parameters
where blocks change, the estimate is applied to the exact block membership
at that parameter; continuity of a chosen block enumeration is unnecessary.

## Checks and scope

The prescribed developer diagnostic was executed after the model was
written: 125 rational-phase cases at n=2,3,4,5,8,17,33,48, mpmath 70 digits,
including 69 collision indices and 62 direct finite-polynomial cases.
No sign mismatch occurred; maximum error/r_n was 0.005277862 and the
signed/cotangent identity errors were at most 3.204e-51. These are
MEASURED implementation diagnostics with no outward roundoff enclosure,
not proof premises. The exact command, source/raw hashes and versions are
in [attempts/N1.md](../attempts/N1.md) and [receipt](../evidence/n1-rows.json).
Independent rerun and distinct mathematical review remain needed.

The degree-dependent rows, exact endpoint rows and harmonic differences
have not been reduced to a compact continuous parameter problem. A small
approximation error alone does not make a maximum comparison or B3 PASS.

## History

2026-11-05, Codex mathematical developer, parent-requested gpt-6-astra ultra;
rules 98d6c00. Formula and error claim written before computation; N5 owns
the quadrature lemma. Independent supplementary check and Claude audit pending.

Same-day coordination: N2 independently derived and owns the full-phase
row identity. N1 retains its independent derivation only as verification
and an equivalent candidate alias; the claimed distinction is solely the
uniform quadrature-error assembly.

Same-day dependency completion: N5 published a complete analytic proof
with SHA-256 `67e5a8e85c4098d72b1804558b547579ed5e52046b7197acd0875b6b007f7d82`.
After reading its pole-removal and exact one-cell kernel argument, N1
replaced the initial CONDITIONAL status with PROVED for the quantitative
row model only. No scope, formula, constant or compactification claim
changed; independent review remains pending.
