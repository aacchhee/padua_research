# Independent supplementary review — C08 finite corner margin

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; their diff to review
input HEAD `547a473a6e1c1268ff4f1ada7243b12afb02d0bc` is empty.
Branch: `codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at the stated corner-normalization scope, with
no mathematical finding.** Both asserted lower bounds hold for every
integer n>=10^6. No far-model maximum comparison follows from this
lemma alone. Formal Claude audit is separate and pending.

## Frozen source and coverage

Reviewed `theory/C08-far-corner-margin.md`, SHA-256
`7cc8a9326d7b4c845a9d2982b95b1088cd28485454d500c0ab477cd5b3dddf81`.
The full new source, C08 idea and attempt including their new-main
addendum, full C07 positive-deformation proof and accepted C07 review,
and full PD-T159, PD-T269 and PD-T270 proofs were read. The exact
finite normalizations, predecessor central-strip domains, derivative
constants and one-dimensional remainder are reconstructed below.

This is supplementary analytic review, excluding historical novelty,
priority and a full author-search/registry audit. No numerical premise,
quadrature, finite sample, fitted constant, mathematical program or
computational certificate was used. Source reads and file hashes were
the checking commands. Only this new report was written; no author
source, old report, shared file or Git state was changed.

## Exact finite sum and permission to discard pairs

PD-T159's corner formula has factor 4/[n(n+1)], actual weights
epsilon_j eta_k, and an additional 1/(n+1) from the finite polynomial
at the coincident endpoint (n,n+1). The other last-column terms
vanish. Its same-mesh square has factor 4/n² and symmetric endpoint
weights epsilon_j epsilon_k. On k=n the reference numerator is zero;
odd parity excludes the diagonal. Consequently the exact relation is

    Lambda_c=n L_n²/(n+1)+1/(n+1)+Delta_n.

There is no additional endpoint or parity correction in Delta_n.

For j<k, let A=cos a_j, B=cos a_k, d=A-B, and let u,v be
the nonnegative changes in their cosines under contraction by
tau=n/(n+1). The ordering b_k>a_j follows from n(k-j)>j,
and hence 0<=v<d. Direct subtraction gives

    d_jk=(1+A)v/[d(d-v)],
    d_kj=-(1+B)u/[d(d+u)].

For k<n, the monotonicity of
[cos(tau*x/2)/cos(x/2)]²-1 implies (1+A)v>=(1+B)u.
Its logarithmic derivative has the required nonnegative sign
tan(x/2)-tau*tan(tau*x/2). The positive term has the smaller
denominator, so the paired sum is nonnegative. For k=n the second
term is zero and the first is nonnegative directly. This verifies the
finite pairing without inferring it from the limiting integrand.

The symmetric weights are identical for the two orientations. The
actual excess eta_n-epsilon_n=1/2 adds only nonnegative actual
terms, while the same-mesh reference there vanishes. Every discarded
unordered pair therefore has nonnegative total contribution.

For J={ceil(n/10),...,floor(9n/10)-1}, each retained pair (j,j+1)
has odd parity and both indices strictly inside the grid. Its two
weights equal one. Distinct j give distinct unordered pairs, although
neighboring pairs can share a row index; sharing an index duplicates
no summand. Thus source (3) has exactly the factor 4/[n(n+1)]
and charges each retained orientation once.

## Quantified signed central-strip estimates

In PD-T269 section 2 choose delta=1/10, M=l=1. Its domain
condition n>=2(M+1)/delta=40 is well inside the present degree
domain. Both j/n and (j+1)/n belong to [delta,1-delta] for every
j in J, including the two possible fractional endpoints.

The predecessor's local factorization is
f(a,a+u)=H(a,u)R(u)/|u|, with
H=(1+cos(a+u))/sin(a+u/2) and R=|u|/[2sin(|u|/2)].
On this strip sin(a+u/2)>=delta, H(a,0)=cot(a/2)<=1/delta,
|H_u|<=2/delta², R<=2 and |R-1|<=u². These yield the stated
6/delta² bound for the difference from H(a,0)/|u|. Applying it
to the two meshes gives 12/(n delta²). The deformed reciprocal
uses (n+1)/n and contributes at most another 1/(n delta²), since
|s*l-t|>=delta. Thus the signed approximation constant 13 is
valid for each orientation. It is not merely a limit statement.

For l=1 the two functions are exactly

    h_+(t)=cot(pi*t/2)/pi [1/(1-t)-1],
    h_-(t)=cot(pi*t/2)/pi [1/(1+t)-1].

The reverse term d_(j+1,j) uses h_- at the row (j+1)/n,
as required by the predecessor definition. Its negative sign has
been retained. The cotangent and reciprocal factors give
|h_+|,|h_-|<=1/delta². Differentiating, using
|(cot(pi*t/2))'|<=pi/(2delta²), gives the available
|h_+'|,|h_-'|<=2/delta³ on the same strip. Moving only the
reverse argument by 1/n therefore costs at most 2000/n.
The two approximation errors cost 2600/n, giving exactly

    [d_(j,j+1)+d_(j+1,j)]/n>=h(j/n)-4600/n.

No positivity was assumed for the reverse orientation individually.

## Fractional cells and the integral margin

The retained cells have disjoint interiors and union
[ceil(n/10)/n,floor(9n/10)/n]. They omit total length less
than 2/n from [1/10,9/10]. Since |h|<=200, the omitted pieces
cost at most 400/n in the lower integral comparison. Each retained
left-endpoint rectangle differs from its integral by at most
4000/(2n²), and there are at most n rectangles. This adds
2000/n. Therefore the source's 2400/n total is valid for every
integer n, without assuming divisibility by 10.

Adding the two orientations gives
h(t)=2t² cot(pi*t/2)/[pi(1-t²)]. The local cotangent partial
fraction and the telescoping sum
sum_(k>=1)(4k²-1)^-1=1/2 give the exact identity

    t² cot(pi*t/2)/(1-t²)
       =2t/pi+(4t³/pi)sum_(k>=1)
                    1/[(4k²-1)(4k²-t²)].

All denominators are positive on the retained strip. Hence
h(t)>=4t/pi² and, since integral_(1/10)^(9/10)t dt=2/5,

    4 integral h >=32/(5pi²)>16/25.

The strict comparison uses only pi²<10; no numerical integral or
constant enclosure enters it.

Write P=|J|<=n and m=n+1. Combining the retained-pair inequality
with the signed approximation gives

    Delta_n >=(4n/m)[(1/n)sum_J h-4600P/n²]
             >=(4n/m)[integral h-7000/n].

The number 7000 is exactly 4600+2400. Thus

    Delta_n>((16/25)n-28000)/(n+1)>1/2.

For the final comparison the numerator after subtracting one half
is (7/50)n-28000-1/2, positive at one million and increasing.
This proves the strict defect bound on the entire unbounded degree
domain, and therefore proves the stated non-strict corner inequality
with margin 1/2. The informal observation that the displayed lower
bound exceeds 0.61 already at the left endpoint is also correct,
but is not needed for the theorem.

## Conversion to the logarithmic normalization

PD-T270 uses exactly PD-T159's L_n, including its odd-degree
half-weight term. Its error is |L_n-A_n|<=1/(4n²) for both
parities. On the present domain A_n-1/(4n²)>0 and
A_n<=log n+2. Squaring the lower bound and multiplying by n/m,
while retaining or discarding positive terms in the correct direction,
gives directly for the baseline itself

    n L_n²/m+1/m
       >=A_n²-A_n²/m-A_n/(2n²)
       >=A_n²-[(log n+2)²/n+(log n+2)/(2n²)].

Thus C07's argument bounds this baseline, independently of using
its lower bound on Lambda_c. Both error functions decrease for
n>=10^6: differentiation gives respectively
-log n*(log n+2)/n² and -(2log n+3)/(2n³).
At n=10^6, log n<14 bounds their sum by
256/10^6+8/10^12<1/1000. Inserting this estimate into the newly
proved margin gives

    Lambda_c>=A_n²+1/2-1/1000

for every integer n>=10^6, with no unspecified asymptotic onset.

## Findings and use boundary

No BLOCKING, MAJOR, MINOR or mathematical NOTE finding. The proof
improves the actual finite corner lower normalization. It supplies no
upper bound on the far-model integral, no far-model maximum theorem,
no global argmax result and no sharpened full corner expansion.
Those targets and the required formal audit retain their separate
status.
