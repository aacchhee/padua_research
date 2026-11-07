# PD-T?argmax-bridge-codex-N1-16 — Uniform corner comparison of both logarithmic coefficients

ID kind: PD-T. Aliases: exact near-model log coefficients; favorable
compact log-degree endpoint; absence of a linear phase cusp in b_M.
Split from: the OPEN near-model maximum comparison in C1.
Split into: none. This is a supporting coefficient theorem, not a
proved part of that comparison's degree/phase domain.

## Statement

Let alpha,beta>=0, alpha+beta<=1/2, r2=alpha^2+beta^2,
a=(cos alpha+cos beta)/2 and L=log n. Let M_near be exactly N1-15's
already fixed model, with R=128, delta=1/1000 and its stated integer
degree domain n>=10^6. Define C and U0 exactly as in N1-04/05 and put

    B_M=4a/pi^2,
    b_M=2U0/pi+[8a log2+4a loga
                        +2(alpha sin alpha+beta sin beta)]/pi^2,
    B_c=4/pi^2,
    k=gamma+log(8/pi), b_c=8k/pi^2.

There is a finite constant K, independent of the phases and n, such that

    |M_near-B_M L^2-b_M L|<=K.                         (1)

Both logarithmic coefficients satisfy the uniform inequalities

    B_M<=B_c-47r2/(48pi^2),
    b_M<=b_c-r2/(24pi^2).                              (2)

The coefficients extend smoothly and evenly in each phase through zero;
in particular b_M-b_c is O(r2), with no O(rho) phase cusp. This does not
exclude N1's exact finite-degree primitive cusp in the bounded remainder.

The corner is normalized by PD-T271:

    Lambda_c=B_c L^2+b_c L+O(1),                        (3)

where its log(n+1/2) is converted to L as proved below. Consequently, on
the integer-degree sequence t=1/log n, the compactified difference has
the uniform expansion

    t^2(M_near-Lambda_c)
       =-4(1-a)/pi^2+t(b_M-b_c)+O(t^2).                (4)

At t=0 this extends uniformly with value -4(1-a)/pi^2. Neither (1)
nor (4) bounds the unscaled finite part by the small C1 tolerance.

## Status, assumptions and dependencies

Overall status: **PROVED**, analytic developer result; distinct review
and the formal Claude audit remain separate. Exact real arithmetic,
the original corrected exceptional mode and all N1-15 collision/cell
conventions. No integral evaluation, fitted coefficient or numerical
pilot is a premise.

Dependencies: N1-04/05/06 give the pole series, exact A coefficient and
shifted constants; N1-07 gives a uniform bound on the finitely many
endpoint rows; N1-09–15 give the unchanged corrected model and its
regular/central bounds. PD-T269/270/271 and PD-T159 fix the corner
normalization and the locally proved harmonic estimate. All these
proofs were read; the frozen round5/6 and C1 reviews were read in full.

The bound K in (1) is only a uniform boundedness assertion. No useful
numerical value, modulus in phase or eventual-onset estimate is claimed.

## Proof

### 1. Extract the coefficients from the existing retained cells

Use f_s(z)=A(v_s(z))-4a/(pi z), s=L,R, on [0,pi] from N1-13. Set

    B0=4a/pi^2, D0=U0/pi+B0 log pi, q_s=+/-sin beta,
    kappa=log(delta/pi), epsilon=log(m/n), m=n+1.

N1-10's exact strip expression has the same singular terms as N1-06,
but retains the actual half-cell endpoints. In its notation,

    Z_n=D0-B0 epsilon,
    log b_s=L+kappa+epsilon+O(1/n),                    (5)

uniformly in phase. The second error in (5) follows from
|b_s-delta*m/pi|<=1/2, with delta fixed. The defining truncation counts
4096 and R are fixed; their h_R,g_R values are uniformly bounded on
0<=t_s<=1 by N1-06's convergent-series bounds. Thus the singular strip
terms give B0 L^2+(2B0 kappa+2D0)L+O(1). Every cross error in (5)
is bounded by a fixed multiple of (L+1)/n, which is bounded on the
whole degree domain. In particular no L times a truncation error is
lost: the h_R coefficient Z_n stays uniformly bounded.

The exact regular strip coefficient contributes

    (L/pi)*integral_0^delta(f_L+f_R)+O((L+1)/n).

Indeed its actual lower endpoints are O(R/n), its upper endpoints
delta+O(1/n), and ||f_s||<3/5 by N1-13. The remaining q_s log z and
U_s N_s/m terms are uniformly bounded: log z is integrable at zero,
U_s is uniformly bounded by the differentiated regular pole profile,
and 0<=N_s/m<=1. Hence

    M_strip=B0 L^2+
      [2B0 kappa+2D0+(1/pi)integral_0^delta(f_L+f_R)]L+O(1).
                                                               (6)

The ordinary outer cell union differs from the two intervals
[delta,pi] by total length at most 5h, h=pi/m: the two lower-end
differences total at most h, the central omitted ends total 2h because
t_L+t_R=1, and the two collision holes have total length at most 2h.
It lies above delta-h/2>delta/2. N1-13 bounds
|A_s|<=8/(pi delta)+3/5 there. Its L term is therefore

    (L/pi)*integral_delta^pi(A_L+A_R)+O(L/n).           (7)

The B part of H=A L+B is uniformly integrable on [delta/2,pi]. To see
this directly, write it as U0/z+P_s+I_s/pi. Here |U0|<=8 and |P_s|<6.
On z<=pi/2 the exact endpoint expression for I_s is
(2a cot(z/2)+q_s)log(sin z), uniformly integrable away from zero.
On z>=pi/2, N1-14 writes I_s=d log(pi-z)+Z_s with 0<=d<=1/2 and
|Z_s|<3. This also is uniformly integrable. Holes cannot increase an
absolute-integral bound. Thus (7) accounts for every unbounded outer
term, including all zero phases and collision-hole changes.

Every other model component is uniformly bounded. For the endpoint
rows this follows from N1-07: its finite profiles have absolute sum
bounded by 1+(2R-1)(4R+9), and its error e_rows is bounded by a fixed
multiple of (1+L)/n+1/n^2. This uses the old theorem only as a bound;
the model still retains N1-09's exact finite-h rows. For the at most
four remaining special rows, a simple bound can be reconstructed as
follows. N1-04 implies

    |sin(pi t)| B_n(t)/n <=2L/pi+4+5/n^2.

N1-05's coefficient products and sin(v/2)>=cos(1/4)>15/16 on these
rows bound the exact absolute row divided by n by 2(L+5). At an actual
collision the same bound follows by continuity of the finite polynomial
row from nearby noncollision phases; separate infinite cotangent
factors are never assigned a value. The Rhat approximation and N1-15's
H8 replacement add at most r_n+192/(450pi m) after normalization and
summation. Thus the whole special-row contribution is O((L+1)/n).
Finally N1-11's M_jump is bounded: its Q_R constant is bounded, m/n<=2,
log b_K/n is bounded, and its W_b integrals have bounded interval and
||W_b||<2. These arguments are uniform despite branch/cutoff changes.

Add (6) and (7), and integrate the 4a/(pi z) coefficient explicitly.
The kappa terms cancel, giving

    b_M=2D0+(1/pi)*integral_0^pi(f_L+f_R).             (8)

This proves uniform expansion (1) once that integral is evaluated.

### 2. Exact max-coefficient integral

Let p=sin alpha, q=sin beta and T(z)=2a cot(z/2). The exact formulas
from N1-06/13 are

    pi A_L=max(p,q+T), pi A_R=max(p,|q-T|).

Put x=max(alpha,beta), y=min(alpha,beta), e=x+y, d=x-y. Their sum
has only three pieces:

    pi(A_L+A_R)=2T,                    0<z<pi-e,
                 T+p+q,               pi-e<z<pi-d,
                 2sin x,              pi-d<z<pi.

This follows either by comparing the three maxima or by the switch
identities T(pi-e)=p+q and T(pi-d)=|p-q|. Empty pieces at y=0 or d=0
are allowed. Use integral T=4a log sin(z/2), subtract 8a/z before
taking the lower endpoint to zero, and use

    sin((pi-e)/2)sin((pi-d)/2)=a.

The trigonometric part of the finite integral is
8a log(2/pi)+4a log a. The constant parts total

    (p+q)*2y+2sin x*(x-y)=2(alpha p+beta q).

Consequently

    integral_0^pi(f_L+f_R)
       =[8a log(2/pi)+4a log a+2(alpha p+beta q)]/pi.

Insert this in (8) and D0=U0/pi+(4a/pi^2)log pi. This is exactly the
stated b_M. No approximation or dependence on R/delta remains in
either logarithmic coefficient.

### 3. The reciprocal-pair series gives a uniform quadratic bound

Write C0=C(1/2). Rearranging N1-04's absolutely convergent C series gives

    C(1/2+x)-C0
       =2x^2 sum_(j=0)^infinity
              1/[(j+1/2)((j+1/2)^2-x^2)].             (9)

Its x=0 value is zero. Here |x|<=1/(4pi)<1/12, so
(j+1/2)^2-x^2>=(35/36)(j+1/2)^2. Also
sum_(j>=0)(j+1/2)^-3=7 zeta(3), and
zeta(3)<1+1/8+integral_2^infinity t^-3 dt=5/4. Thus

    0<=C(1/2+x)-C0<=18x^2.

With x_-=(alpha-beta)/(2pi), x_+=(alpha+beta)/(2pi), define
D=C(1/2+x_-)+C(1/2+x_+)-2C0. Then

    0<=D<=9r2/pi^2<(15/16)r2,                        (10)

using pi>31/10 and hence pi^2>48/5.

For clarity C0=2gamma+4log2: substitute t=1/2 in N1-04's harmonic
definition, take symmetric partial sums, and use
H_(2j)-H_j ->log2. At the two actual offsets,

    U0=(a/pi)[2C0+D-4log pi].                         (11)

The sine factors producing (11) are respectively cos((alpha-beta)/2)
and cos((alpha+beta)/2), whose product is a. Substituting (11) into
the exact b_M expression yields the useful identity

    b_M-b_c=(2/pi^2)*
       [aD+2a log a+alpha p+beta q-4k(1-a)].          (12)

An elementary lower bound k>3/2 suffices. One fully rational check is:
PD-T270's harmonic estimate gives gamma>=H_10-log10-1/20. The positive
exponential series through degree10 at 2303/1000 exceeds10, so
log10<2303/1000; direct fractions give
H_10-2303/1000-1/20>23/40. Also pi<22/7 gives 8/pi>28/11. If
w=17/39, integration of the geometric series gives
log(28/11)=2(w+w^3/3+w^5/5+...)>2(w+w^3/3)>37/40.
The two strict lower bounds sum to 3/2. These are finite elementary
inequalities, independent of the optional numerical normalization pilot.

Set u=1-a. Taylor's alternating upper bound for cos on [-1/2,1/2]
gives u>=47r2/192. Also 0<a<=1, log a<=-u, and
alpha p+beta q<=r2. Applying these and (10), k>3/2 to (12) gives

    (pi^2/2)(b_M-b_c)
       <=[(15/16)a+1]r2-(2a+6)u
       <=[-15/32+(43/96)a]r2
       <=-r2/48.

This proves the second inequality (2); the first is
4u/pi^2>=47r2/(48pi^2).

Equation (9) is smooth and even in x on a neighborhood of all used
offsets. Its sum for x_-,x_+ is even in each phase, as are a, log a
and alpha sin alpha+beta sin beta. Thus b_M has the stated smooth
even extension. Its first derivatives vanish at the origin; the
bounded second derivatives on this compact phase set imply O(r2).

### 4. Corner normalization and the compact endpoint

PD-T271 has N=n+1/2 and
Lambda_c=B_c log^2 N+b_c log N+c+R_n. Its explicit R_n is bounded on
n>=10^6 and tends to zero. Since
0<=log(N/n)<=1/(2n), replacing log N by L changes its quadratic and
linear terms by O((L+1)/n), uniformly. This proves (3) with exactly
the b_c above, including both parities. Subtract (3) from (1) and
multiply by t^2 to obtain (4); all O constants are uniform in phase.

## Checks and limitations

The one preregistered 60-digit mpmath normalization pilot at n17/24/32
matched the corrected periodic S_n(0,0) and PD-T159's positive corner
sum to absolute discrepancy below 1.62e-59, including the actual
polynomial endpoint collision. It took 0.31307493 process CPU seconds,
exit0, under a 300-second CPU cap. This is **MEASURED calibration only**;
M_near was not evaluated and its n>=10^6 theorem was not used below
that range. Code/receipt: `../code/n1_near_r7_normalization.py` and
`../evidence/n1-near-r7-normalization.json`. No fit or numerical integral.

Both favorable coefficients vanish in the corner difference at the
origin. For phases of order 1/L their leading loss is only O(1), the
same scale as the uncontrolled bounded finite part. Therefore (4)
does not imply C1, any effective onset, or B3/B4 PASS. PD-T220's
finite-n cusp remains possible in that part; no pure quadratic bound
for M_near or S_n is claimed. No new model term or correction was used.

## Open items and history

The exact residual comparison and a falsifiable next bounded test are
in [the separate OPEN record](N1-round7-comparison.md). All-n PD-T099,
global range 2–40, the finite energy range 2–128, far phases and other
center classes are unchanged. Distinct supplementary review uses these
new files' frozen hashes; the coordinator owns publication and formal audit.

2026-11-06, after input `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
Codex mathematical worker; inherited model/effort, serving metadata
unexposed. Full gate and exact targets in `../ideas/N1-round7.md`.
