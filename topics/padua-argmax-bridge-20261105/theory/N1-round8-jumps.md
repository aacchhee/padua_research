# PD-T?argmax-bridge-codex-N1-18 — A uniform envelope for near-model branch artifacts

ID kind: PD-T. Aliases: exact retained-cell seam cancellation; collision
marks; H8 branch envelope. Split from: the OPEN residual increment
comparison N1-17. Split into: none. The model itself is unchanged.

## Statement

Use exactly N1-15's M_near, integer n>=10^6, m=n+1, h=pi/m,
L=log n, R=128, delta=1/1000, and alpha,beta>=0, alpha+beta<=1/2.
Let F_n be N1-17's residual increment after subtracting N1-16's exact
L^2 and L coefficients and its value at the origin. There exists a
continuous function Q_n on this phase triangle, Q_n(0,0)=0, such that

    |F_n(alpha,beta)-Q_n(alpha,beta)|<9/(2n).          (1)

Q_n is only an analytic decomposition of the already fixed residual:
replace its at most four approximate special rows by their exact
polynomial rows, remove the at most two noncentral collision marks,
and subtract the exact bounded strip/cutoff step functions specified
below. No replacement model or new correction term is proposed.

The independent contributions to the increment envelope are

    H8/Rhat special-row approximation:  <3/(10n),
    at most two noncentral collision marks: <4/n,
    at most two strip/outer seams:       <6/(1000n),
    the possible half-angle cutoff:     <2/n^3.        (2)

Their sum is <9/(2n). In particular it is below

    eta=107/3584000=1/4096-3/14000

for every n>=10^6. This proves that these branch artifacts alone fit
the remaining C1 allowance. It does not bound the continuous function
Q_n by the favorable coefficient loss, and does not prove C1.

## Status, assumptions and dependencies

Overall status: **PROVED**, analytic developer helper. Exact real
arithmetic and the original exceptional/collision convention. Required
distinct review and the formal Claude audit are separate. No computation,
fit, numerical integral or sample is a premise.

Dependencies: N1-01/02 row errors and ordinary cancellation estimate;
N1-04/05 regularized pole products and H; N1-09–11 exact corrected rows,
endpoint expansion and jump formula; N1-13/14 regular/central bounds;
N1-15 exact cell/special-row definition and H8 error; N1-16/17 exact
coefficient/residual definitions. The sources and their reviews were
read/refreshed before this bounded test. The candidate records the gate.

## Proof

### 1. Strip/outer cancellation is exact up to the endpoint residue

In N1-10 write

    E_s(z)=B(v_s(z))-[U0+(4a/pi)log z]/z
                              -(q_s/pi)log z-U_s,
    f_s=A(v_s(z))-4a/(pi z), B0=4a/pi^2,
    Z_n=U0/pi+B0 log(pi*n/m).

The endpoint expansion gives

    |E_s(z)|<=(7/4)z+(1/9)z|log z|.                  (3)

We first verify that (3) also holds on 0<z<=1/500, rather than using
the original statement beyond delta. In N1-10's proof the cotangent
error coefficient is 1/[3pi(1-z^2/24)]<1/9 on this interval, and the
other logarithm-replacement coefficient is
(4+z/2)/[pi(6-z^2)]<1/4. Its pole Taylor/denominator coefficient is
35/(4pi^2)+pi/6<3/2. All offsets remain in [1/4,3/4], the complete
numerator stays positive, and no coefficient switch occurs here.
These are exactly the three estimates producing (3); hence the
same explicit bound holds on the slightly enlarged interval.

At a strip cutoff K_s change, let the transferred centered cell be
D=[delta-h/2,delta+h/2]. Write u=h*b for a variable cell boundary.
The derivative of the strip's singular boundary expression is

    d[Z_n log b+(B0/2)log^2 b]
      =[U0/pi+B0(L+log u)] du/u.                     (4)

Indeed log(pi*n/m)+log b=L+log(h*b), exactly. The h_R/g_R constants
are independent of K_s, so they cancel in its increment. The regular
A, q_s log z and U_s terms have increments equal to their exact
cell integrals, including U_s/m=(1/pi) integral_D U_s. Consequently
the full strip increment, minus the exact removed/added H integral,
is precisely

    j_s(alpha)=-(1/pi) integral_D E_s(z) dz,           (5)

with its sign reversed for the opposite direction of transfer.
No L-dependent singular seam term survives.

Here D is inside (0,1/500): h/2<2/m, so its upper endpoint is
<1/990 and its lower endpoint >1/1100. Thus |log z|<8, and (3)
gives |E_s(z)|<(95/36)/990<3/1000. Since h/pi=1/m,

    |j_s|<3/(1000m).                                 (6)

For fixed n, each K_s can change at most once on 0<=beta<=1/2,
because t_L=beta/pi and t_R=1-beta/pi move by less than one. The
two corresponding seam lines are beta=constant. Their exact step
amplitudes (5) are continuous functions of alpha on the portions of
those lines in the triangle. Subtract the appropriate signed step
j_s(alpha) for each crossed seam, choosing the baseline value zero
at beta=0. This makes the strip/outer combination continuous. When
the step is active, alpha<=1/2-beta<=1/2-beta_seam, so its amplitude
is defined within the original phase triangle. The total increment
allowance is <6/(1000m)<=6/(1000n).

### 2. The half-angle jump cutoff has only one possible boundary step

In N1-11, K_b=floor(m/2-t_b), with t_L=beta/pi in [0,1/(2pi)] and
t_R=1-beta/pi. If m is odd neither index changes on this domain.
If m is even, only the left index has a step, between beta=0 and
its positive one-sided limit. The transferred cell is centered at
z=pi/2. The right index is constant.

The exact decomposition J_b=A2_b/z^2+A1/z+W_b shows that the change
in M_jump is

    j_half(alpha)=(1/(n*pi)) integral_D J_0(z) dz,
    D=[pi/2-h/2,pi/2+h/2].                            (7)

This follows by integrating each of its -1/b_K, log b_K and W_b
boundary terms; the retained constants cancel. At beta=0,

    J_0(z)=cot z*[p*alpha+2az cot(z/2)]/(2pi).

On D, |cot z|<=2|z-pi/2|, p*alpha<=1/4 and
2az cot(z/2)<=4. Thus |J_0(z)|<2|z-pi/2|. Its absolute integral
is <h^2/2, and therefore

    |j_half|<pi/(2n m^2)<2/n^3.                      (8)

The amplitude is continuous in alpha. Subtracting this one possible
boundary step makes the M_jump component continuous at beta=0.

### 3. Charge H8 errors once per phase, not per transition

Let R_r be the exact finite polynomial absolute row. N1-01 bounds
the normalized Rhat error on any subset of rows by r_n. N1-15 bounds
the combined H8 replacement error on its at most four special rows by
192/(450pi m). Thus the whole special-row discrepancy obeys

    |e_sp(alpha,beta)|<=r_n+192/(450pi m).             (9)

There may be degree-growing numbers of block-membership changes.
No such count is multiplied into (9): it bounds the entire special-row
approximation at each phase, including exact zeros, double collisions
and all admissible H8 branches. The increment relative to the origin
is bounded by twice its right side.

With pi<4 and H_n<=n, the explicit r_n is less than
1/n^4+1/(2n^3)<=1/n^3 for n>=2. Since pi>3 and m>n,

    2r_n+384/(450pi m)<3/(10n), n>=10^6.              (10)

Replacing these approximate rows by their exact rows is only an
auxiliary proof comparison. The M_near terms remain unchanged.

### 4. Actual noncentral collision marks have a small envelope

After (9), consider only the at most two collision rows outside the
permanent central pair {m-1,m}. The mark for such a row, with its
folded centered cell D_r, is exactly

    d_r=R_r/(n*m)-(1/pi) integral_(D_r) H(L,v_s(z)) dz.
                                                               (11)

Away from the collision locus that cell is ordinary; on the locus it
is replaced by the special row. Removing the mark (11) simply fills
that cell and leaves only the permanently special central rows. The
sum of marks is zero at the origin, where there is no noncentral
collision row. We bound all marks at a phase simultaneously.

Each collision has C_r=0 or D_r=0 by N1-05's sine-factor identities.
As C_r+D_r=p/2, this implies

    max(|C_r|,|D_r|)=p/2<=1/4.                       (12)

The possible collision angles lie within 1/2 of pi. A noncentral row
has epsilon=|v_r-pi|>=h: on the left r<=m-2 gives
epsilon>h, while r>=m+1 gives epsilon>=h on the right. Thus
|sin v_r|>=2/m. Taking the ordinary-row estimate from N1-02/04 to
the collision by continuity gives

    |R_r/(n*m)-H(L,v_r)/m|
       <=5/(n^2*m)+1/(2n).                           (13)

This limit uses continuity of the finite polynomial row. H is also
continuous at the collision with v_r not in pi*Z: Phi is regularized,
and I is continuous by dominated convergence using the bounded
minimum of the two separated cotangent magnitudes. Separate pole
factors are never assigned collision values. The only coalescing
physical central collision is already in the permanently special
pair; it is not part of (11)–(13).

It remains to compare H(center)/m with its cell integral. These cells
lie in z>pi-1/2-h/2>5/2, and have distance at least h/2 from pi.
Write H=A_s L+V_s+I_s/pi, V_s=N_s/[2sin(z/2)]. The sine chord/Taylor
bound on this interval gives sin(z/2)>9/10. The exact max formulas
then give Lip(A_s)<=5/(4pi). N1-13 has Lip(N_s)<=12/pi and |N_s|<=8;
1/[2sin(z/2)]<=5/9 and its derivative has magnitude <1/3. Therefore
Lip(V_s)<5. Centered-cell Lipschitz quadrature on both cells costs at
most

    [5L/8+10]/m^2 <1/(100n), n>=10^6.                (14)

For the I part use N1-14, I_s=d log(pi-z)+Z_s with d<=1/2 and
combined Var(Z_s)<15. Centered-cell BV quadrature on any two cells
costs at most 15/(2pi m). The log second-derivative integral over
the two cells is at most 4/h, exactly the same endpoint-distance
bound as N1-15; its error is at most d/(2pi m). Together these are

    <31/(12m).                                      (15)

Here (14) and (15) include the extra 1/pi for the I normalization;
no factor for the number of cells is applied to the combined variation.
Combining (13) for at most two rows with (14)–(15) gives

    |sum_r d_r|<=sum_r |d_r|
       <1/n+10/(n^2*m)+1/(100n)+31/(12m)<4/n.         (16)

This is an envelope for the marks at a phase, independent of the
number of different collision loci met while phases vary. It remains
valid when the two candidate rows coincide or one is already central:
duplicates are merged and fewer marks are charged.

### 5. The remaining residual is continuous; combine the allowances

Remove e_sp and the marks (11) from M_near only as an algebraic proof
decomposition. The remaining central rows are exact finite polynomial
rows and continuous in phase; its outer integral has no collision
holes. On its retained cells z stays away from both 0 and pi for fixed
n, so the continuous regularized pole products and ordinary cancellation
integrals vary continuously, including numerator-zero thresholds.
The finite endpoint rows and fixed strip constants also are continuous.
Subtracting the exact seam and possible boundary step functions of
sections 1–2 removes their only remaining floor discontinuities.

Now subtract the smooth even polynomial B_M L^2+b_M L and the value
of the resulting residual at the origin. Call this continuous
increment Q_n. The four removed increment allowances are (6), (8),
(10), (16), hence

    |F_n-Q_n|< [4+3/10+6/1000]/n+2/n^3<9/(2n).

Finally 9/(2*10^6)<107/3584000 is a direct rational comparison. This
proves (1)–(2) and the stated branch-budget conclusion.

## Scope, checks and next obligation

No mathematical computation or diagnostic was run; every bound is
analytic. The origin normalization, one-correction limit, exact model
and full C1 statement are unchanged. In particular Q_n may have an
entropy modulus and a finite-n cusp. Continuity alone does not bound
its increment at the required scale. The precise remaining comparison
is recorded separately in `N1-round8-modulus.md`; full C1 remains OPEN.

2026-11-06, input/rules `a8fad0526779216d184463d046591fdfea6783f6`.
Codex, parent-assigned Sol xhigh; serving metadata unexposed. The parent
proposed the seam identity, which is proved here rather than assumed.
No Git/shared-file operation, second model correction or new round.
