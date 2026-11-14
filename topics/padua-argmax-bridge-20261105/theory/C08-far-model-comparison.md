# PD-T?argmax-bridge-codex-C08-far-02 — Uniform far comparison from degree one million

ID kind: PD-T. Aliases: compact far constant maximum; million-degree
far-model exclusion; full closed far diamond. Split from: the C08 task.
Split into: substantive inputs are the separately recorded weighted
coefficient, endpoint constant, finite corner margin, pole functional
and complementary renormalized integral. Their scopes are listed below.

## Statement and status

Use exactly C06's fixed full-phase model, with R=64, delta=1/100 and
the original corrected exceptional kernel mode. For every integer n>=10^6
and every real phase pair with1/2<=|alpha|+|beta|<=pi,

    M_far(alpha,beta;log n)+1/2<Lambda_c(n)-1/10,       (1)
    S_n(alpha,beta)<Lambda_c(n)-6/25.                 (2)

Here S_n is the corrected odd-board primitive of PD-T216/N2/C06, and
Lambda_c is its actual nonnode-corner value S_n(0,0). In particular the
requested M_far+1/2<Lambda_c holds on the entire closed far diamond,
including axes, vertices, a=0, all polynomial collisions and both parities.
The threshold is the literal integer bound n>=10^6, with no unspecified
asymptotic onset or degree enumeration.

**PROVED**, by the complete analytic assembly below. Independent
supplementary review of the newly assembled theorem and formal Claude
audit are separate. No numerical quadrature, phase sampling, fitted
coefficient, finite-energy extrapolation or new model correction is
a proof premise. Near phases and the physical actual-corner patches
have their separately owned comparisons; this file proves the far case.

## Exact definitions and dependencies

It suffices to use alpha,beta>=0 and alpha+beta<=pi; the fixed model
uses separate absolute phases. Put L=log n and

    a=(cos alpha+cos beta)/2,
    M_far=(4a/pi^2)L^2+b_full L+C_far,
    C_far=C_R+c_mesh+(1/pi)integral_delta^(2pi-delta)B(v)dv.

All definitions are exactly C06-far-compact-error.md equations(1)–(7).
Specifically C_R is N1-07's finite endpoint-row sinc profile;
c_mesh uses N1-06's exact infinite h_R,g_R series, not a truncated
diagnostic approximation; B=V+I/pi is the full joint profile with its
integrable central logarithm. Every removable pole product and the
w=0 endpoint use the stated continuous finite-polynomial conventions.

The proof uses these separately written analytic results:

1. C06-far-compact-error.md: |S_n-M_far|<9/25 throughout the full
   closed diamond for every n>=10^6. Frozen source
   64d88fd3bce387630cf55fcc559fb88cc15cf9f27e93487fc662f5050e8d4520.
2. C08-far-weighted-coefficient.md: b_full-b_c<=3(1-a)/pi^2,
   where b_c=8k/pi^2 and k=gamma+log(8/pi)>3/2. Frozen source
   6d905b6c634043992af9f51b6871fe8bcc1ead3b6bc32ca1daa68d844d4e2f1a.
3. C08-far-endpoint-constant.md: the exact retained endpoint part
   E_64<49/25+1/3000 throughout the closed triangle. Frozen source
   3bd4653b0cf2e1f33e42f8629c06a32b45b546f198e6659cf0203fb48240647c.
4. C08-far-corner-margin.md: Lambda_c>=A_n^2+1/2-1/1000, with
   A_n=(2/pi)(L+k), every n>=10^6. Frozen source
   7cc8a9326d7b4c845a9d2982b95b1088cd28485454d500c0ab477cd5b3dddf81.
5. The complementary worker's C08-far-integral-bound.md:
   K_delta<49/50 on the full closed triangle. Frozen source
   e76a45698ab5c0f2af53816fb74487fb929eff99011e8004e9f79e3f84f8f7a5.
   Its scalar input C08-far-pole-functional.md proves H<1/2 and
   charges the finite delta cutoff, frozen source
   6cb61ebc3f3808c61bc8d72feb2bee3a57c1dbecf597a7915833b4f43c8cda67.

The author read the complete complementary integral proof and checked
its exact normalization, reversed inequality after multiplication by the
negative logarithm, sine-log antiderivative and finite-cutoff charges
before this assembly. This is development checking, not independent
self-approval. The source diagnostic is MEASURED context only.

## 1. Bound the complete constant without altering the model

Write B0=4a/pi^2, D0=U0/pi+B0 log pi and kappa=log(delta/pi).
The exact model constant decomposes as

    C_far=E_64+K_delta,
    E_64=C_R+D0[h_R(t_L)+h_R(t_R)]
                    +B0[g_R(t_L)+g_R(t_R)],
    K_delta=B0*kappa^2+2D0*kappa
                          +(1/pi)integral_delta^(2pi-delta)B.

This is just N1-06's stated c_mesh formula; no terms are inserted,
deleted or counted twice. By dependencies3 and5,

    C_far<49/25+1/3000+49/50=8821/3000<3.           (3)

The endpoint limit used to prove dependency3 is an analytic bounding
device with its uniform tail; the actual fixed R=64 endpoint family
is retained in (3). The cancellation and pole-function cutoff errors
are already charged in dependency5. Thus (3) is uniform also where
a=0 or an offset crosses an integer.

## 2. Compare both logarithmic coefficients on the unbounded degree range

Set u=1-a. On the full phase triangle0<=a<=1. Dependency2 gives

    [(4a/pi^2)L^2+b_full L]-[(4/pi^2)L^2+b_c L]
                         <=-(4L^2-3L)u/pi^2.       (4)

Every n>=10^6 satisfies L>69/5. One elementary check is

    log10=3log2+log(5/4)
       >6(1/3+1/81+1/1215+1/15309)+2/9>23/10.

The function4L^2-3L is increasing on this degree range, and
4(69/5)^2-3(69/5)=18009/25>720. Since pi^2<10, (4) implies

    [(4a/pi^2)L^2+b_full L]-[(4/pi^2)L^2+b_c L]
                                                   <=-72u. (5)

This handles every larger degree analytically. In particular the proof
does not assume b_full<=b_c, which is false at the boundary midpoint;
its positive weighted excess has been included in (4).

## 3. The far coefficient loss exceeds every retained constant

If rho=alpha+beta>=1/2, then

    a=cos(rho/2)cos((alpha-beta)/2)<=cos(1/4).

Taylor's alternating cosine bound therefore gives

    u>=1-cos(1/4)>=1/32-1/6144=191/6144.           (6)

Dependency4 supplies the actual finite corner lower. Expanding its
square yields

    Lambda_c>= (4/pi^2)L^2+b_c L+(2k/pi)^2
                                                +1/2-1/1000.

Its constant square is strictly greater than9/10, because k>3/2
and pi^2<10. Combining this with (3),(5),(6) gives

    M_far+1/2-Lambda_c
       <3-9/10+1/1000-72*(191/6144)
        =2101/1000-573/256=-4393/32000<-1/10.       (7)

This proves (1) for all first-quadrant far phases. Both the model and
primitive use separate phase evenness, proved in their defining sources;
no coordinate-mesh swap is invoked. Thus (1) holds on the stated full
closed far diamond.

Finally dependency1 and (1) give

    S_n<M_far+9/25
       <Lambda_c-1/10-1/2+9/25
        =Lambda_c-6/25,

which is (2). Every estimate used includes its own boundary/collision
conventions, so the finite degree and phase limits require no additional
pointwise extension argument at this stage.

## Scope, history and remaining review

The original C08 task M_far+1/2<Lambda_c is proved as written, with
extra slack. The earlier sufficient candidate C_far<=5/2 and the
stronger integral candidate K_delta<=1/2 were not needed and remain
unproved; their dispositions are preserved in the idea/attempt records.
The successful proof uses the unchanged original model, the proved
weaker constant C_far<3, and a genuinely stronger finite corner lower.
The earlier OPEN checkpoint is superseded for the original target only;
no failed estimate or empirical fit has been relabeled a proof.

This theorem supplies the far-phase part of a global assembly. It does
not extend the certified finite degrees2–40, prove the remaining smaller
degrees, or replace the separately established near noncorner and actual
corner predicates. The parent owns global assembly, publication and all
Git/shared records. Distinct review of this exact frozen assembly and
formal Claude audit are still separate requirements.

No mathematical program, numerical integral, fit or phase scan was run
in C08. All new comparison and constant bounds are analytic. Earlier
proofs remain frozen and unchanged.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426;
current merged input547a473a6e1c1268ff4f1ada7243b12afb02d0bc, rules unchanged.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
