# PD-T?argmax-bridge-codex-C08-far-01 — Full-phase weighted coefficient comparison

ID kind: PD-T. Aliases: weighted regularized-pole increment; full-domain
log-degree monotonicity. Split from: the C08 far-model comparison, which
remains OPEN. Split into: none; the compact constant bound is separate.

## Statement and status

Let C(t) be precisely N1-04's reciprocal-pair function on0<t<1 and
C0=C(1/2). For every |theta|<=pi, with continuous endpoint products,

    cos(theta/2)[C(1/2+theta/(2pi))-C0]
                      <=(7/2)[1-cos(theta/2)].          (1)

On the full phase triangle alpha,beta>=0, alpha+beta<=pi, set
a=(cos alpha+cos beta)/2, k=gamma+log(8/pi), b_c=8k/pi^2, and use
exactly C06's coefficient b_full. Then

    b_full-b_c<=3(1-a)/pi^2.                            (2)

Consequently, for any fixed phase-only finite constant C_far, the
difference

    (4a/pi^2)L^2+b_full L+C_far
                       -[(2/pi)(L+k)]^2              (3)

is nonincreasing for L>=3/8 and strictly decreasing for L>3/8
whenever a<1. This includes all closed far phases and a=0.

**PROVED**, analytic developer lemma below; independent review and formal
audit remain separate. It does not prove a bound on C_far or the original
far comparison. No finite sample or numerical execution is a premise.
Gate and closest predecessors: ../ideas/C08-far-comparison.md.

Dependencies: N1-04's absolutely convergent C series; PD-T269 section4's
locally proved cotangent partial fraction; C06's exact b_full formula;
N1-16's elementary k>3/2. All are read, with no near-domain theorem
silently applied outside its stated phase region.

## 1. A useful cosine inequality from the cotangent partial fraction

Let0<=y<1 and c=cos(pi*y/2). The identity
tan z=cot z-2cot(2z), applied to the cotangent partial fraction proved
in PD-T269 section4, gives

    (pi/2)tan(pi*y/2)
                      =sum_(l odd>=1) 2y/(l^2-y^2).    (4)

For completeness this rearrangement is justified on every compact
subinterval of0<=y<1 by absolute convergence of the resulting series;
the original cotangent formula holds there by its Fourier-series proof.
At y=0 both sides have their continuous zero value. In particular,
comparing their derivative at zero gives
sum_(l odd>=1) l^(-2)=pi^2/8.

Set Q(y)=(1-y^2)/c. Its logarithmic derivative, by (4), satisfies

    Q'(y)/Q(y)=sum_(l odd>=3)2y/(l^2-y^2)
                    >=2y(pi^2/8-1).

Since Q(0)=1, integration and exp t>=1+t give

    Q(y)>=1+(pi^2/8-1)y^2.

Rearranging yields

    c*y^2/[(1-c)(1-y^2)]<=8/pi^2, 0<y<1.             (5)

No infinite product or external special-function inequality is required.

## 2. Bound the weighted reciprocal-pair increment

The symmetric C series gives exactly

    C(1/2+y/2)-C0
                  =4y^2 sum_(l odd>=1)1/[l(l^2-y^2)]. (6)

For l>=3 its denominator is bounded below by l(l^2-1), and the
spacing-two telescoping harmonic identity gives

    sum_(l odd>=3)1/[l(l^2-1)]=3/4-log2.             (7)

Indeed1/[l(l^2-1)]=(1/2)(1/(l-1)+1/(l+1))-1/l;
sum over l=3,5,... and use H_(2m)-H_m->log2.
Combine (5)–(7), noting also c*y^2/(1-c)<=8/pi^2, to obtain

    c[C(1/2+y/2)-C0]/(1-c)
                 <=(32/pi^2)(7/4-log2)<7/2.          (8)

For the last rational comparison, log2>69/100 follows from the first
three positive terms of2 atanh(1/3), and pi^2>197/20 gives
(32/pi^2)(7/4-log2)<(32*53/50)/(197/20)<7/2.
Symmetry handles negative y. At y=0 both sides in (1) vanish. As
y->1, the l=1 term in (6) shows the weighted left side tends to pi,
while the remaining terms tend to zero; pi<7/2. Thus (1) holds on
the complete closed interval, with theta=pi*y.

## 3. Apply the weighting before comparing logarithmic coefficients

Write e=alpha+beta, d=alpha-beta, c_e=cos(e/2), c_d=cos(d/2), so
0<=c_e,c_d<=1 and a=c_e*c_d. In the open triangle define

    D=C(1/2+e/(2pi))+C(1/2+d/(2pi))-2C0.

By (1),

    aD<=(7/2)[c_d(1-c_e)+c_e(1-c_d)]
       <=(7/2)(1-a),                                  (9)

because c_e+c_d<=1+c_e*c_d. Every displayed weighted term has the
continuous endpoint value proved above, so (9) extends to the full
closed triangle; an unweighted divergent C is never assigned a value.

Exactly as algebra, rather than a near-domain estimate, C06's coefficient
and C0=2gamma+4log2 give

    b_full-b_c=(2/pi^2)[aD+2a loga
                 +alpha sin alpha+beta sin beta-4k(1-a)].     (10)

This identity is initially written for a>0 and extends continuously to
a=0 using the weighted products and0log0=0. For0<=t<=pi,
t sin t<=2(1-cos t), since tan(t/2)>=t/2; endpoints follow by
continuity. Therefore alpha sin alpha+beta sin beta<=4(1-a).
Also a loga<=0 and k>3/2. Substitution in (10) yields

    b_full-b_c<=(2/pi^2)(7/2+4-6)(1-a)
                =3(1-a)/pi^2,

which proves (2). The boundary midpoint's positive coefficient excess
is allowed by this inequality.

Differentiate (3) in L. Its derivative is at most

    (1-a)(3-8L)/pi^2.

This proves the degree monotonicity assertion, including all a=0 limits.
The strict far case has a<=cos(1/4)<1.

## Scope and history

This supplies a proved reduction of the unbounded degree parameter to
a fixed logarithmic endpoint. The finite constant maximum and the
model's actual-primitive error are separate obligations; no global
argmax conclusion follows from (1)–(3) alone. No computation was run.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
