# PD-T?argmax-bridge-codex-D02-far-bias — Exact full-phase cutoff bias

ID kind: PD-T. Aliases: bias-completed far constant; endpoint finite part;
signed cutoff completion. Split from: D02 far joint-remainder target, OPEN.
Split into: the actual-primitive limit and finite-n bound have their own
record D02-far-uniform-limit.md. No old model or theorem is changed.

## Statement and definitions

Use the corrected odd-board primitive and the exact C06 definitions on
alpha,beta>=0, alpha+beta<=pi; extend by separate absolute phases. Write
p=sin alpha, q=sin beta, P=p+q, a=(cos alpha+cos beta)/2,
B0=4a/pi^2, D0=U0/pi+B0 log pi and

    S0(z)=[U0+(4a/pi)log z]/z,
    Z_s(z)=B(v_s(z))-S0(z), v_L(z)=z, v_R(z)=2pi-z.

The notation S0(z) in this file denotes only the singular row profile,
not the primitive at phase zero. For any integer R>=2 and
0<delta<=pi/4 define the C06 parameter family, openly distinguished from
its unchanged published R64,delta=.01 member, by

    E_R=C_R+D0[h_R(beta/pi)+h_R(1-beta/pi)]
               +B0[g_R(beta/pi)+g_R(1-beta/pi)],
    K_delta=B0 log^2(delta/pi)+2D0 log(delta/pi)
               +(1/pi) integral_delta^(2pi-delta) B(v)dv,
    C_(R,delta)=E_R+K_delta.

Every finite sinc collision and w=0 endpoint uses C06/N1-07's continuous
polynomial-compatible definition. The central integral has the inherited
integrable logarithm. Let C(t)=-psi(t)-psi(1-t), t_d=1/2+(alpha-beta)/(2pi),
t_e=1/2+(alpha+beta)/(2pi), and use the continuous weighted products in

    E_infty=a/3+a C(t_d)C(t_e)/pi^2.                       (1)

Then the finite part K_0=lim_(delta downarrow 0) K_delta exists uniformly
on the entire closed phase diamond and is continuous. So is

    C_infty=E_infty+K_0.                                  (2)

For every R>=2 and 0<delta<=pi/4 the exact identity is

    beta_(R,delta):=C_infty-C_(R,delta)
      =E_infty-E_R+(1/pi) integral_0^delta [Z_L(z)+Z_R(z)]dz. (3)

This supplies an exact, degree-independent signed bias functional. With

    Q(P,delta)=(2delta/pi)[7+(P/pi)(5+2log(4pi/delta))],

its computable truncation error and, for R>=64, its absolute size obey

    |beta_(R,delta)-(E_infty-E_R)| <= Q(P,delta),
    |beta_(R,delta)| < 1/(R-1)^2+Q(P,delta).               (4)

The newly declared model is

    M_infty(alpha,beta,L)=B0 L^2+b_full L+C_infty.         (5)

Here b_full is the unchanged exact C06 full-phase coefficient. Formula
(5) is a new far model with the full constant; no modification of the
fixed near model or silent correction to M_far is made. Identification
with the true S_n limit is a separate theorem in D02-far-uniform-limit.md.

## Assumptions and status

Exact real arithmetic and the stated closed diamond. **PROVED** by the
analytic argument below. Distinct supplementary review and final Claude
review are not self-approval. No numerical quadrature or fitted limit is
a premise. Both degree parities are irrelevant to this constant identity.

Depends on: N1-05 (N1-joint-endpoint-profile.md), especially its full-phase
bound (2) and continuous residual tail; N1-06/07 definitions; C08-far-03
(C08-far-endpoint-constant.md), including uniform E_R convergence and
weighted endpoint extension; C06-far-compact-error.md sections 1–2 for
continuity and the uniformly controlled central logarithm.

## Proof

For 0<epsilon<delta<=pi/4, direct subtraction of the two finite
renormalizations gives

    K_epsilon-K_delta
       =(1/pi) integral_epsilon^delta [Z_L(z)+Z_R(z)]dz.  (6)

Indeed the integral of 2S0(z)/pi is
(2U0/pi)log z+B0 log^2 z. Expanding the logarithmic polynomial defining
K_delta shows exactly the same delta-dependent terms; the remaining
constant is independent of delta. Thus their difference cancels, with
the sign in (6). No divergent channel integrals are separated.

N1-05 proves on each endpoint, including a=0 and axes,

    |Z_s(z)|<=7+(P/pi)[3+2log(4pi/z)].                   (7)

The envelope is integrable at zero, uniformly for P<=2. Integrating it
on both ends gives Q(P,delta), which tends uniformly to zero. Equation
(6) therefore proves that K_delta is uniformly Cauchy and that its
limit satisfies K_0-K_delta=integral_0^delta(Z_L+Z_R)/pi.
This is a finite, ordinary improper integral of the combined residual.

For each positive delta, K_delta is continuous in phase. Away from
v=pi this follows from the continuous regularized pole factors and the
C06 generic J formula. At the center, write B=W+d*ell/pi as in C06,
where d=(q-p)_+, ell=log(2|v-pi|/pi) on |v-pi|<=pi/2 and zero elsewhere.
C06 proves a phase-uniform bound on the continuous regular remainder on
any fixed interior interval. The only additional domination is a constant
times |ell|, which is integrable. Dominated convergence proves continuity
of the integral, including coefficient switches and collisions. A uniform
limit of these continuous functions is continuous.

C08-far-03 proves that E_R tends uniformly to (1) and
|E_R-E_infty|<1/(R-1)^2 for R>=64, with the weighted continuous boundary
convention. Combining that theorem with (6) proves (2)–(4). The algebra
C_(R,delta)=E_R+K_delta is exactly C06's C_R+c_mesh+integral B/pi.
It holds for every R>=2 where those defining expressions exist; the
R>=64 restriction belongs only to the displayed convenient tail bound.
This proves the claimed identity on all closed phases. QED.

## Scope, checks and open items

The exact fixed-model bias is beta_(64,1/100); it need not vanish. In
particular a missing strip integral is only one part of the bias:
E_infty-E_64 is retained with its sign. This answers the limitation in
the D01 interior diagnostic without inferring a limit from its samples.

The missing integral on (0,eta) in any evaluation of (3) is rigorously
bounded by Q(P,eta); a floating quadrature estimate on [eta,delta] is
still not a validated enclosure. No diagnostic was needed for this proof.
The small-degree O((1+log n)/n) contract and useful argmax onset remain
OPEN in D02-far-joint-target.md.

History: 2026-11-06, rules/input 084a64f6465956f9c75b5538f83752c30318f151.
Codex hard-math developer, parent requested Astra ultra with prospective
LOG justification; serving metadata unexposed. Gate in ideas/D02-far-joint.md.
