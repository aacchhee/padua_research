# PD-T?argmax-bridge-codex-N1-11 — Fixed-count pole-jump sum

ID kind: PD-T. Aliases: reciprocal-square jump constant; retained-cell
Bernoulli correction. Split from: the single round-5 corrected model.
Split into: none. This compacts its endpoint jump contribution, not the
remaining central/interior H-profile sum.

## Statement and model

Assume alpha,beta>=0, alpha+beta<=1/2, R=128 and n>=10^6. Put
m=n+1, h=pi/m, a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta.
For the left side use b=beta,t=beta/pi; for the right side use
b=-beta,t=1-beta/pi. In each case q_b=sin b and

    K=floor(m/2-t), a_t=R+t-1/2, b_K=K+t+1/2,
    A2_b=-2ab/pi, A1=(p*alpha-q*beta+4a)/(2pi),
    v(z)=cot z-1/z,
    w(z)=csc^2(z/2)-4/z^2,
    W_b(z)=[p*alpha+q_b*(z-b)]*v(z)/(2pi)+q_b/(2pi)
           +a*(z-b)*w(z)/(2pi)-a*(z-b)/pi.             (1)

Use the continuous extensions v(0)=0,w(0)=1/3. Let h_R(t) be the
centered harmonic constant of N1-06 and define

    Q_R(t)=1/a_t+sum_{k=R}^infinity {
          1/(k+t)^2-1/(k+t-1/2)+1/(k+t+1/2)}.          (2)

Superscript [R] means that only the single summand k=R is retained in
either defining series, including its initial term. Define

    M_jump=sum_b {
       A2_b*m/(n*pi^2)*[Q_R^[R](t)-1/b_K]
       +A1/(n*pi)*[log b_K+h_R^[R](t)]
       +(1/(n*pi))*integral_(h*a_t)^(h*b_K) W_b(z)dz }.
                                                               (3)

The sum has two terms; its constants have one series term each and its
two ordinary bounded integrals are part of the exact model. The actual
finite-h boundaries are retained. For N1-09's pole-jump terms,

    |(1/(nm))*sum_{r outside A_R, z_r<=pi/2} J_r-M_jump|
       <=3/n^2+1/(27R^3)+1/(16nR^2)
       <1/40000000.                                  (4)

No n-growing sum occurs in (3). The result includes zero phases by
continuous limits and uses no sampled or fitted coefficient.

## Status and dependencies

Overall status: **PROVED**, analytic developer proof; independent review
pending. N1-09 fixes the exact jumps and phase domain. N1-06 supplies the
centered harmonic constant and kernel. PD-T270 supplies the proved bound
|(cot z-1/z)''|<1 on [0,pi/2]; its full proof was read. The existing
child /root/n1/endpoint_check developed and checked this bounded target;
that contribution is not an independent audit.

## Proof

### 1. Exact jump and pole decomposition

On the left, C<0,D>0. The two Bernoulli values are
(alpha-beta+z)/(2pi) and (alpha+beta-z)/(2pi), respectively. Substituting
the jumps from N1-09 gives

    J_b(z)=cot z/(2pi)*
              [p*alpha+(q_b+2a cot(z/2))*(z-b)].       (5)

On the right the original coefficients have C>0,D<0, cot v=-cot z,
and the two Bernoulli values are (alpha-beta-z)/(2pi) and
(alpha+beta+z)/(2pi). Direct substitution gives (5) with b=-beta,
without an additional sign. All these offsets avoid integers on the
stated endpoint regions, so there is no omitted collision correction.
The endpoint regions outside A_R are exactly k=R,...,K on both sides.

The elementary identity

    cot z cot(z/2)=(1/2)csc^2(z/2)-1

now yields the exact decomposition

    J_b(z)=A2_b/z^2+A1/z+W_b(z).                      (6)

Here q_b*b=q*beta on either side. The regular endpoint value is
W_b(0)=q_b/(2pi)+5ab/(6pi).

### 2. Uniform regular-part variation including cutoff cells

The half-cell upper limit is at most pi/2+h/2<pi/2+1/100<8/5.
On 0<=z<=8/5, v is decreasing from zero. Elementary sine bounds give
|v(z)|<=7/10: on [0,pi/2] use |v|<=2/pi, and on the remaining
interval use cot z=-tan(z-pi/2), 0<=z-pi/2<3/100 and
tan y<=y/(1-y^2/2). Thus also Var(v)<=7/10.

Since w(z)=-v'(z/2), T270 applies at z/2<pi/2 and gives
|w'|<=1/2, Var(w)<=4/5 and |w|<=1/3+4/5=17/15.
Set D0=p*alpha-q*beta. We have |D0|<=1/4, |q_b|<=1/2 and a<=1.
The product-variation inequality applied to (1), with A=8/5, gives

    Var(W_b)<= { (1/4+A/2)*(7/10)+(A/2)*(7/10)
                 +(A+1/2)*(4/5)+A*(17/15) }/(2pi)
                  +A/pi <2.                         (7)

The same direct sup estimates, including the constant q_b/(2pi), give
||W_b||_infinity<2 on this interval. In particular no phase-dependent
singularity is hidden in the regular integral. Centered-cell BV
quadrature on its exact cell interval yields

    |sum_{k=R}^K W_b(h(k+t))
                  -(1/h)*integral_(h*a_t)^(h*b_K) W_b|
       <=Var(W_b)/2<=1.                              (8)

After normalization, the two regular pieces cost at most 2/(nm).

### 3. Reciprocal-square and harmonic tails

For f(x)=x^-2 the centered-cell kernel has absolute bound 1/8. Convexity
and integration of f''=6/x^4 imply

    sum_{k=R}^K 1/(k+t)^2=Q_R(t)-1/b_K+epsilon_2,
    0<=epsilon_2<=1/(4b_K^3).                        (9)

Indeed each summand minus its cell integral is nonpositive; the tail
omitted from Q_R has magnitude at most
(1/8)*integral_(b_K)^infinity f''=1/(4b_K^3). The identical bound with
b_J=J+t+1/2 controls truncation of Q_R after J. N1-06 gives

    sum_{k=R}^K 1/(k+t)=log b_K+h_R(t)+epsilon_h,
    0<=epsilon_h<=1/(8b_K^2),                        (10)

and the same truncation bound for h_R. Since b_K>=n/2,
|A1|<3/4, sum_b |A2_b|=4a*beta/pi<=2/pi and m/n<=9/8,
the combined cutoff tails in (9)-(10), after their coefficients in
(3), are less than 1/n^3. Together with (8) this is less than 3/n^2.

Finally b_R=R+t+1/2>=R. Truncating both constants after J=R adds at most

    (m/n)*(2/pi)/(4pi^2 R^3)
       +2*(3/4)/(8pi*n*R^2)
       <=1/(27R^3)+1/(16nR^2),                       (11)

using m/n<=2 and pi>3. Combining (6)-(11) proves (4). For R=128 and
n>=10^6, the scalar bound in (4) is less than 1/40000000 by rational
comparison; no numerical evaluation of W or its integrals is needed.

## Scope, verification and history

This settles the preregistered jump-compaction allocation. The two
integrals in (3) are exact model functions; an eventual interval
implementation must certify their evaluations. The central/interior
outer H-profile sum, its uniform quadrature and the maximum comparison
remain OPEN. No full B3 PASS or effective argmax onset follows.

No mathematical computation, fit or empirical test was run. 2026-11-06,
round 5 after fc8c288, requested gpt-6-astra ultra. Candidate and terms:
../ideas/N1-round5.md. All previous frozen proofs remain unchanged.
