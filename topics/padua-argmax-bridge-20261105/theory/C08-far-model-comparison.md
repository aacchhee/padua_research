# PD-T?argmax-bridge-codex-C08-far-02 — Fixed full-phase model comparison target

ID kind: PD-T. Aliases: compact far constant maximum; million-degree
far-model comparison. Split from: C08 task. Split into: the substantive
weighted coefficient and degree reduction is C08-far-01, separately
PROVED in C08-far-weighted-coefficient.md.

## Exact target and status

Use precisely C06's fixed full-phase model, with R=64 and delta=1/100:

    M_far(alpha,beta;L)=(4a/pi^2)L^2+b_full L+C_far,
    C_far=C_R+c_mesh+(1/pi)integral_delta^(2pi-delta) B(v)dv.

C_R is N1-07's finite endpoint-row sinc profile, c_mesh is N1-06(2)
with its exact infinite h_R,g_R series, and B=V+I/pi is N1-05's
joint constant profile. All endpoint/collision products use the actual
continuous conventions in these source proofs. No new correction is
introduced. The independently owned C06 compact-error proof fixes the
actual-primitive approximation contract.

The target remains **OPEN**:

    M_far(alpha,beta;log n)+1/2<Lambda_c(n)
      for every integer n>=10^6 and every alpha,beta>=0
      with1/2<=alpha+beta<=pi.                         (1)

The following is a sufficient compact obligation, also **OPEN**:

    C_far(alpha,beta)<=5/2 throughout the full closed triangle. (2)

This stronger constant bound is a candidate, not an assumed premise.
Failure of (2) would not refute (1).

## Why the compact obligation would suffice

This paragraph is a routine conditional calculation, not a proof of (1).
By the separate C08-far-01 lemma, b_full-b_c<=3(1-a)/pi^2. For
L>=log(10^6)>69/5,

    [(4a/pi^2)L^2+b_full L]
                 -[(4/pi^2)L^2+b_c L]<=-72(1-a),

because4(69/5)^2-3(69/5)=18009/25>720 and pi^2<10.
C07-corner-01 gives Lambda_c>=A_n^2-1/1000, with
A_n=(2/pi)(L+k), k>3/2. Its constant square is
(2k/pi)^2>9/10. On the far set,
1-a>=1-cos(1/4)>=191/6144. If (2) were established, then

    M_far+1/2-Lambda_c
       <=5/2+1/2-9/10+1/1000-72*(191/6144)<-1/10.

Thus (2) leaves a definite rational margin for the required1/2 error
budget. This reduction preserves all n>=10^6 and every boundary phase.

## Remaining obligations and evidence limits

The combined constant (2) still requires a complete analytic proof or
a bounded, independently reviewed validated enclosure. The endpoint
profile, mesh subtraction and cancellation integral must be combined
without losing their cancellations. The source diagnostic's35 floating
samples and reported quadrature errors are MEASURED context only and
do not prove (2) or (1). No new computation has been performed in C08.
The C07 corner theorem, all-class defect and C06 error proof do not by
themselves discharge this compact comparison.

## Retained stronger-corner alternative

The separate developer lemma C08-far-corner-margin.md proves the stronger
normalization Lambda_c>=A_n^2+1/2-1/1000 for every n>=10^6. With that
lemma, the relaxed compact budget C_far<=3 would imply (1) with exactly
the same rational slack calculation above. The separately proved endpoint
bound C08-far-endpoint-constant.md gives E_64<49/25+1/3000. Consequently
an upper bound1 for

    K=B0 log^2(delta/pi)+2D0 log(delta/pi)
                           +(1/pi)integral_delta^(2pi-delta)B

would suffice for the original target. This K bound remains OPEN and is
owned by the complementary C08 worker; it is not assumed here. The
original5/2 sufficient budget is retained rather than silently relabeled.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
