# PD-T?argmax-bridge-codex-C08-far-04 — A finite positive corner margin

ID kind: PD-T. Aliases: retained adjacent deformation pairs; effective
positive corner correction. Split from: C08 far comparison. Split into:
none. The far comparison remains a separate target.

## Statement and status

For every integer n>=10^6, let Lambda_c,L_n be precisely PD-T159's
corner value and same-mesh cosecant sum, and set
A_n=(2/pi)(log n+gamma+log(8/pi)). Then

    Lambda_c(n)>=n L_n^2/(n+1)+1/(n+1)+1/2,          (1)
    Lambda_c(n)>=A_n^2+1/2-1/1000.                  (2)

**PROVED**, analytic developer lemma. Independent review and formal
audit are separate; no computational evidence is used. This improves
only the finite lower normalization available to the far comparison.

Dependencies: C07-corner-positive-deformation.md's exact nonnegative
unordered-pair algebra; PD-T269 section2's explicitly proved central
term approximation; PD-T269 section4's positive cotangent expansion;
PD-T270 and C07's bound on the one-dimensional square remainder.
All these proofs were read in full. Gate: ../ideas/C08-far-comparison.md.

## 1. Retain only positive adjacent pairs

Put m=n+1, a_j=j*pi/n, b_j=j*pi/m, and
f(a,b)=(1+cos b)/|cos a-cos b|. Define the signed deformation

    d_jk=f(a_j,b_k)-f(a_j,a_k).

PD-T159's exact sums, with actual endpoint weights, give

    Lambda_c=n L_n^2/m+1/m+Delta_n.

C07 proves each unordered pair d_jk+d_kj is nonnegative under the
symmetric weights epsilon_j epsilon_k; replacing the second endpoint
weight epsilon_n by its actual eta_n only adds a nonnegative term.
Thus we may retain any collection of unordered pairs without estimating
the discarded pairs in absolute value.

Let J be the integers from ceil(n/10) through floor(9n/10)-1.
For each j in J retain the pair(j,j+1). Its weights are both one,
and all these unordered pairs are distinct. Therefore

    Delta_n>=(4/(nm))sum_(j in J)(d_(j,j+1)+d_(j+1,j)). (3)

## 2. Quantified comparison on the retained strip

Use delta=1/10 and offset l=1 in PD-T269 section2. Define on
[delta,1-delta]

    h_+(t)=cot(pi*t/2)/pi*[1/(1-t)-1],
    h_-(t)=cot(pi*t/2)/pi*[1/(1+t)-1],
    h(t)=h_+(t)+h_-(t).

The proof there establishes, for either orientation and every retained
central row,

    |d_(j,j+1)/n-h_+(j/n)|<=13/(n delta^2),
    |d_(j+1,j)/n-h_-((j+1)/n)|<=13/(n delta^2),
    |h_+'|,|h_-'|<=2/delta^3,
    |h_+|,|h_-|<=1/delta^2.                       (4)

Its domain condition n>=2(l+1)/delta=40 is satisfied. Both j/n and
(j+1)/n lie in the stated strip by the choice of J. These are signed
approximations, so the possibly negative h_- has not been dropped.
Moving its argument back by1/n costs at most2/(n delta^3).
Consequently, for t_j=j/n,

    [d_(j,j+1)+d_(j+1,j)]/n
             >=h(t_j)-[26/delta^2+2/delta^3]/n
              =h(t_j)-4600/n.                    (5)

We also need a completely specified mesh error. The union of cells
[j/n,(j+1)/n], j in J, misses total length less than2/n from
[1/10,9/10]. Since |h|<=200, these endpoint pieces cost at most400/n.
On each retained cell a left-endpoint approximation costs at most
sup|h'|/(2n^2), with |h'|<=4000. There are at most n cells. Thus

    (1/n)sum_(j in J)h(t_j)
                     >=integral_(1/10)^(9/10)h(t)dt-2400/n. (6)

Every fractional endpoint cell and the shift of the second orientation
has been included in (5),(6).

## 3. The retained integral already supplies a fixed margin

The two orientations combine to

    h(t)=2t^2 cot(pi*t/2)/[pi(1-t^2)].

PD-T269's positive partial-fraction identity, proved in its section4,
is

    t^2 cot(pi*t/2)/(1-t^2)
       =2t/pi+(4t^3/pi)sum_(k>=1)
                       1/[(4k^2-1)(4k^2-t^2)]>=2t/pi.

Therefore h(t)>=4t/pi^2. Its retained integral satisfies

    4 integral_(1/10)^(9/10)h(t)dt
                      >=32/(5pi^2)>16/25,          (7)

using pi^2<10. There are at most n pairs in J. Combining (3), (5)
and (6) with (7) gives

    Delta_n >=(n/m)[4 integral h-28000/n]
              >[(16/25)n-28000]/(n+1)>1/2.         (8)

For the last inequality, subtract1/2: its numerator is
(7/50)n-28000-1/2, positive already at n=10^6 and increasing.
This proves (1). In fact the displayed proof leaves more than0.61
at the left endpoint; the stated1/2 is a deliberate rational margin.

Finally C07-corner-positive-deformation.md section2, using PD-T270,
proves
n L_n^2/(n+1)+1/(n+1)>=A_n^2-1/1000 on n>=10^6.
Insert this in (1) to obtain (2).

## Scope and history

The retained-strip estimate is analytic and holds for every integer
degree in its domain. It is not extrapolated from any finite data.
No sharp corner constant or full asymptotic remainder is inferred.
The main far-model inequality still requires its own constant bound.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
