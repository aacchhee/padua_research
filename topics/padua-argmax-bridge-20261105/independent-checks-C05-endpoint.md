# Independent supplementary review — C05 finite-h endpoint increment

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; their unchanged status at
review input HEAD `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3` was checked
in the preceding review. Branch: `codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at the stated endpoint-component scope, with no
mathematical finding.** The exact retained endpoint error has Hessian
entries below 45000/n and origin beta slope below 35/n, giving the stated
phase-increment bound. This is not a bound for the complete finite-degree
Q_n error. Formal Claude audit is separate and remains pending.

## Frozen source and method

Reviewed source: `theory/C05-finiteh-endpoint-increment.md`, SHA-256
`0e8616a3f23ba42ca31b5967d3e9bf44186472b8ff51d105da38c704cba693f7`.
The full source was read and its identity checked. The exact N1-09 row
formula, N1-07 profile, N1-15 retained-row indexing and N1-18 Q_n
construction are the unchanged dependencies previously read in full or
at their complete defining sections for this sequence of reviews. The
locally proved cotangent partial fraction was also read for C03/C04.
The proof below was reconstructed analytically from those identities.

This review covers the numerical constants, both signed endpoint charts,
the actual exceptional mode, the origin continuation, and the distinction
between endpoint and full-model error. Historical novelty, priority and
a full registry/search audit are outside scope. No mathematical program,
numerical row evaluation, quadrature, fit or sampled diagnostic was run.
Source reads and file hashes were the checking commands. Only this new
report was written; no author source, shared file, old review or Git state
was changed.

## Exact formula and endpoint bookkeeping

N1-09 gives R_r=-T_r+2sum F_j with exactly r positive indices
j=-r+1,-r+3,...,r-1. Its signed term is
T_r=n[a-(sin b/2)cot(w/(2m))]. Dividing by nm and subtracting
N1-07's ell_r leaves the first two terms of (6), with -a/m and
(sin b/w)[tau(v/2)-1]. The highest-mode correction is retained in a.

The cosine difference is exactly h²D_h K/2. Thus

    2F_j/(nm)=8mu*a*H/D_h+2mu*g/(D_h*K).

Subtracting 8a/D and splitting H=1+(H-1) gives all remaining terms
of (6), with the stated factors 8 and 2 and the exact mu=n/m.
There is no replacement of mu by one at this stage.

For the closest row, the exact -T_0 formula gives (7). At beta=0 it
reduces to e_0=-a/m, agreeing with the polynomial continuation
T_0=n(a-m) and ell_0=1. There is no evaluation of an isolated
cotangent pole at zero.

The left block is r=0,...,127 and the right block is r=1,...,128
with b=-beta. Therefore the total is one e_0, 127 paired rows and
one unpaired r=128 row: 256 rows in total, with no duplicate closest
row. Their nonzero-r weight is
2sum_(r=1)^127 r+128=128². The auxiliary signed phase diamond is
legitimate: the same complete-numerator positivity and denominator gaps
keep the positive index sets fixed for either sign of alpha or b.

## Small-angle and denominator bounds

For k=r+/-j, each sign traverses the positive odd list 1,...,2r-1.
The bound |alpha|+|b|<=1/2 gives w+/-z>(5/2)k. Subtracting
eta*w<4r/n<=512/10^6 leaves mu*w+/-z>(12/5)k, and similarly
mu*w>(12/5)r. All denominators are therefore positive with margins
uniform in r<=128, n>=10^6 and the entire auxiliary diamond.

The actual angles obey |u|,|v|<=4rh, so both sinc arguments have
magnitude at most 512/10^6<1/1000. The sinc integral bounds give
K>=99/100 and |K-1|<=(8/3)r²h². Product differentiation gives
the stated K_i and K_ij bounds; in particular the second derivative
bound is h²/6+(8/9)r²h^4<h²/4. The reciprocal rule then yields
|(1/K)_i|<=2rh² and |(1/K)_ij|<=h².

For H=N/K, N=(1+cos v)/2 satisfies the displayed bounds. Hence
|H-1|<=7r²h² and |H_i|<=4rh². In the Hessian, the two terms
without an extra small factor contribute less than
[(1/2)/(99/100)+(1/4)/(99/100)²]h²<0.77h². All other
products carry r²h²<=128²/10^12, so the stated h² bound follows.

The tau bounds (10) follow by termwise differentiation of the local
cotangent partial fraction. With |y|<=1/1000, pi>3 and sum k^-2<=2,
the resulting uniformly summable majorants fit |tau-1|<=y²,
|tau'|<=2|y| and |tau''|<=2, including zero. No finite-n derivative
is approximated by a limiting derivative in these estimates.

## Principal reciprocal displacement

Partial fractions give

    mu/D_h=(1/(2w))[1/(mu*w-z)+1/(mu*w+z)],
    1/D=(1/(2w))[1/(w-z)+1/(w+z)].

Subtracting proves (11) exactly with coefficient eta/2. For each
product q=1/(d_h*d), the linear factors have coordinate slopes of
magnitude at most one. The denominator gaps therefore imply
q<=1/(6k²), |q_i|<=49/(360k³)<1/(7k³), and

    |q_ij|<=2q[d^-2+(d*d_h)^-1+d_h^-2]<1/(5k^4).

Each sign traverses the same odd list. Bounding its reciprocal square
sum by 23/18<4/3, and higher powers by that same bound, gives exactly
S<=4/9, |S_i|<=8/21, |S_ij|<=8/15. Consequently the mesh
displacement term 4eta*a*S has first derivatives below 2/n and
Hessian entries below

    (4/n)(2/9+4/21+8/15)=1192/(315n)<4/n.

This important bound is uniform in the row number and uses the actual
finite displacement before estimating derivatives. It does not lose a
factor r or a small-phase denominator.

## All remaining row Hessians

For E=1/D_h, its partial fraction and mu*w>(12/5)r give
sum E<(25/(144r))H_odd(r)<2/r. The first derivative multiplier
is at most 5/6 and the second at most 25/24. These yield
sum|E_i|<2/r and sum|E_ij|<3/r. Combining them with the inverse-K
bounds gives the stated 4/r, 5/r and 7/r bounds for F=E/K and
its first two derivatives.

For the fourth term of (6), the six types of product-rule contributions
to the Hessian of a*(H-1)*E are bounded, after summing, by

    [7r+4+7r+2/r+16+21r]h²
      =[35r+20+2/r]h².

Multiplication by 8mu gives at most 456rh²<512r/n². The mixed
terms with a_i and E_i are both included; none is silently omitted.

For g, direct differentiation gives |g|<=2rh, |g_i|<=5rh and
|g_ij|<=5rh. The mixed derivative is zero. These bounds use the
sum |sin alpha|+|sin b|<=1/2 and the actual angle slopes h and
mu*h. The Hessian of the last term is therefore bounded by

    2[5rh*(4/r)+2*5rh*(5/r)+2rh*(7/r)]=168/n.

For k(w)=[tau(w/(2m))-1]/w, quotient differentiation gives the
three stated bounds r/m², 3/(4m²), and 4/(5rm²). Thus the
only nonzero Hessian entry of sin b*k(w) is at most
(r/2+3/2+2/(5r))/m²<3r/n². The closest-row product in (7)
has its beta second derivative bounded by
(1/48+1/4+1/2)/m²<1/n² and all other Hessian entries zero.
Finally each -a/m term contributes at most 1/(2n).

Summing over the exact 256-row block gives the explicit bound

    128/n+255*(4+168)/n+(512+3)*128²/n²+1/n²
      =43988/n+8437761/n²<45000/n.

This proves the Hessian assertion everywhere in the phase triangle,
including both axes via the smooth auxiliary extension. The bound is
for the whole retained block, not an error per transition.

## Linear term and Taylor increment

Replacing alpha by -alpha and pairing each summation index j with -j
preserves every finite row and profile term. Thus each e_r is even in
alpha. The r=1,...,127 b pairs are even in beta, and e_0 is even in
both variables. The origin alpha slope is therefore zero; the origin
beta slope is exactly -partial_b e_128(0,0), with no second unpaired
row or closest-row slope.

At alpha=b=0, a_b=0 and g=0. The five terms of (6) have slopes
bounded by 0, r/n², 2/n, 176r/n² and 32/n. For the fourth,
the two surviving differentiated products total at most
8[4rh²*(2/r)+7r²h²*(2/r)]<=176rh². For the last,
|g_b|=|sin v|<=4rh and sum|F|<4/r give 32/n. Hence

    |partial_b e_128(0,0)|<34/n+22656/n²<35/n.

Along the radial phase segment, the Hessian bound controls the second
derivative by (45000/n)(alpha+beta)². Taylor's integral remainder
therefore yields an absolute increment at most
35beta/n+22500(alpha+beta)²/n. Since (alpha+beta)²<=2r²,
this is bounded by the claimed 45000r²/n+40beta/n. Equality at
the zero phase is interpreted nonstrictly, as in the statement.

## Scope and completion

No BLOCKING, MAJOR or MINOR finding in the frozen endpoint helper.
No author repair was made or required before acceptance. The proof retains
the exact finite-h rows and their polynomial normalization throughout;
the old absolute N1-07 approximation error is not reused as an increment.

N1-18's construction leaves this endpoint component unchanged. Its
9/(2n) branch envelope is therefore not an additional term in this
endpoint estimate. The rest of the finite-degree Q_n assembly, including
the central rows, omitted cells and actual continuous proof corrections,
still needs its own estimates. Neither the original C1 budget nor the
separately mentioned weaker full-model comparison follows from this helper.
Formal Claude audit remains pending.
