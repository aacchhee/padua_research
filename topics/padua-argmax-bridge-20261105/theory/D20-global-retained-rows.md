# PD-T?argmax-bridge-codex-D20-rows — Global fixed six-row comparison with C2

ID kind: PD-T. Aliases: endpoint operator match; full-phase central-pair
charge. Split from: D20 global hybrid error. Split into: none.

## Statement, definitions and status

For every integer n>=32, m=n+1, L=log n and absolute phases
alpha,beta>=0, alpha+beta<=pi, use EXACTLY D05-fixed-special-rows'
corrected polynomial G_n=D_n-cos(nu), signed samples F_rk, actual
R_r=sum_k|F_rk| and normalization 1/(nm). Put

    J6=[R_0+R_1+R_(2m-2)+R_(2m-1)+R_(m-1)+R_m]/(nm),
    E6(n)=(193+21L)/n+21600/n^2.

Let C2 be the UNCHANGED N1-07 finite profile C_R at R=2, also the C_2
in D04's exact endpoint constant E_2 and D07-global-mesh(7). Then

    |J6-C2|<=E6(n).                                      (1)

Define signed-phase objects by separate absolute phases, as in D05;
(1) holds on the entire closed signed diamond. Axes, a=0, vertices,
both parities and all finite-polynomial collisions are included.
Overall status: **PROVED**, written developer proof; distinct review
pending. This is a coarse global row bound, not D07's near-only B6.

## First decisive operator match

N1-round4-rows(4) compares EXACTLY the four first/last R2 rows with

    C2=ell_0(beta)+ell_1(alpha,beta)
                         +ell_1(alpha,-beta)+ell_2(alpha,-beta).

Its right-side signed row r,b=-beta is the original row 2m-r by
evenness of the corrected polynomial. Parity agrees because 2m-r and
r have the same parity. Its half-open signed n-point first-coordinate
mesh is a permutation modulo 2pi of D05's k=0,...,n-1 mesh. Thus the
absolute norm and 1/(nm) normalization are identical, including the
exceptional highest first-coordinate mode. N1-07's sinc formulas give
actual polynomial-compatible limits at removable terms, including
r=1,b=-pi,alpha=0. No unweighted pole norm is assigned a value.

Using H_n<=1+L in that theorem gives

    |[R_0+R_1+R_(2m-2)+R_(2m-1)]/(nm)-C2|
                     <=(181+19L)/n+21600/n^2.             (2)

The old e_rows is therefore a FOUR-row bound; it is not silently
transferred to J6. D04-reference-matching identifies the SAME C2 in
E_2=C2+D0 H2+B0 G2 and Delta_2=E_infty-E_2. It introduces no
central-row constant. We must bound the remaining central pair.

## Full-phase central-pair bound

Use C06-far-full-profile section1's actual weighted row inequality,
whose proof uses only N1-04's n>=2 weighted pole expansion and the
finite-polynomial triangle inequality. We use that proof at n>=32,
not C06's separate n>=10^6 assembled theorem below its floor:

    R_r/n<=A(v_r)L+V(v_r)+5(|C(v_r)|+|D(v_r)|)/n^2,
    |C|+|D|=(1/2)max(p,|q+2a cot(v/2)|),
    A=2(|C|+|D|)/pi,
    V=[c_e Phi_0(eta_-)+c_d Phi_0(eta_+)]/[2sin(v/2)].

Here a=(cos alpha+cos beta)/2, p=sin alpha,q=sin beta,P=p+q,
c_e=cos((alpha+beta)/2),c_d=cos((alpha-beta)/2). On the FULL
triangle c_e,c_d in[0,1], |Phi_0|<=4 and Phi_0(integer)=1.
The whole weighted inequality holds at v=pi and collisions by its
accepted polynomial-continuity proof; no pointwise cotangent identity
at a pole is presumed.

The two angles are v_(m-1)=pi-(pi-beta)/m and v_m=pi+beta/m.
For m>=33 their distances from pi are <=pi/m, so

    sin(v_r/2)>=1-pi^2/(8m^2)>99/100,
    |cot(v_r/2)|<=pi/m,
    V(v_r)<=4/sin(v_r/2)<9/2,
    A(v_r)<=P/pi+2a/m.

The tangent estimate follows from sec^2 x<=2 on[0,pi/4]. Applying
the row inequality to BOTH actual central rows gives

    0<=[R_(m-1)+R_m]/(nm)
      <=9/m+2PL/(pi*m)+4aL/m^2
                        +5P/(m*n^2)+10pi*a/(m^2*n^2)
      <=[10+P(1+L)]/n<=(12+2L)/n.                         (3)

For the simplification use a<=1, P<=2, L<=n/4 at n>=32,
4L/m^2+10pi/(m^2*n^2)<=1/n, and
2L/(pi*m)+5/(m*n^2)<=(L+1)/n. These follow directly from
pi<4,pi>2,m=n+1 and n>=32; n/4-log n is increasing and
log32<4<8. Adding (2) and (3) proves (1).

## Collisions, scope and provenance

D05's fixed ordinary set is the complement of EXACTLY these six
labels. Its dense-phase continuation does not remove an ordinary
collision row, so there is no collision hole in the new telescope.
The six actual rows already include their collisions by (2)--(3).
Consequently N1-08's e_collision, which paid for added/deleted
endpoint rows in a DIFFERENT moving-membership block, is unnecessary
here. We neither set it to zero in the old bound nor alter that bound.
No off-grid alias is treated as an actual polynomial collision.

This lemma does not use D07's near-only endpoint/central simplifications.
All old sources remain unchanged. No numerical/native/phase/board/
quadrature/root/degree job occurred in this paper proof. 2026-11-06,
parent-assigned Codex Sol xhigh; rules/input
ca8d52aa2a48c941473846ab884cccb25f1bdb9f; serving metadata unexposed.


## Root review closure — 2026-11-06

Distinct review [D20](../independent-checks-D20-global-hybrid.md), SHA256 `e1284bce7f95e332cba284cbafa03c7667772d7518076aea3d3596331cb82398`, accepts all four split scopes, including exact global argmax at every n>=7000. Root adopts the result: far gap3/40, accepted D18 near gap1/400 and D17 actual-corner loss1/8. The complete closed physical cover and both parity equality sets are retained. This dated closure preserves reviewed text and first scalar evidence; final Claude audit remains separate.
