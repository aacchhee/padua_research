# Independent supplementary review — C06 full compact-model error

2026-11-06. Distinct Codex reviewer `/root/c06_far_review`, parent-allocated
Astra high; runtime serving identity/effective effort are not independently
exposed. Rules were read at supplied input
`b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`; the coordinator owns Git,
publication and shared records. This supplements the required Claude audit.

## Disposition

**Accepted at its stated approximation scope; no unresolved mathematical
finding.** For every integer n>=10^6 and every phase in the closed diamond,
the exact R=64, delta=1/100 model in the submission satisfies

    |S_n-M_far(alpha,beta,log n)|<9/25.

This is an approximation theorem only. The full-phase maximum of M_far,
its comparison with the finite-n corner value, and an n>=10^6 far or global
argmax conclusion remain separate **OPEN** obligations. The binary64 diagnostic
is not a proof premise and was not independently rerun here. This review does
not certify a numerical integrator or a floating implementation of the model.

The reviewed source is `theory/C06-far-compact-error.md`, SHA-256
`64d88fd3bce387630cf55fcc559fb88cc15cf9f27e93487fc662f5050e8d4520`.
Executed `sha256sum` confirmed this identity before and after the substantive
reading. Only this new report was written; author files, prior reviews,
shared records and Git state were untouched.

## Reading and scope

Read the complete frozen submission and its preregistered follow-up candidate.
The preceding full-profile review in `independent-checks-C06-far.md` records
the complete reconstruction of original N1-02/03/04/05/06/07/08, N2's exact
normalization, the corrected F1 double-collision case, and the exact full-domain
b_full integral. Those sources and their constants remain the premises here.
For the new parts, read the complete N1-10, N1-13 and N1-14 proofs and checked
which arguments are generic and which statements have rho<=1/2 hypotheses.
The new proof reconstructs its enlarged ranges; no near-only theorem is used
outside its stated domain.

This is a correctness review of the specified quantitative continuation.
No new mechanism or historical novelty claim is generated or reviewed, so the
workflow's no-novelty exception applies. The recorded candidate/closest-variant
context from the preceding review was retained; no exhaustive independent
novelty-gate claim is made. AGENTS, WORKFLOW, CODEX, handoff06 and LOG were
read during that review and this is a continuation under the same assignment.

## Model contract and endpoints

The source specifies the exact continuous periodic Phi_0, with integer value
one, rather than a truncated numerical approximation. Its h_R and g_R constants
are the original centered-cell convergent series, with their respective tails
1/(8b^2) and (log b+2)/(8b^2). Coefficients multiplying those tails remain
explicit in c_mesh. The finite ell profiles use the signed sinc combination
before evaluating a removable denominator, with the unique w=0 value one.
These match N1-07, including both signs of b and the exceptional (n,0) mode.

The only degree argument in M_far is L. The endpoint profiles have O(R^2)
finite terms, and its exact series/integrals do not hide a sum of n rows.
This does not by itself give a rigorous implementation with constant arithmetic
cost at arbitrary requested precision. At the a=0 edge, p=q, the cancellation
integral has s=u and is zero; at either phase vertex the endpoint definitions
remain finite. The original F1 simultaneous polynomial collision is retained
through the unchanged N1-08 endpoint theorem.

## Full-range regular pole variation

The N1-04 reciprocal-pair series is valid throughout 0<t<=1/2, not just the
smaller interval used in N1-10's statement. Its differentiated summable bounds
give R<=1, R'<=16/3 and R''<=608/27 there. The five second-derivative terms
in Phi_0 have total bound 2822/81<35. Reflection across t=1/2 is smooth
(the defining symmetric pole series has zero derivative there); period joins
have the stated derivative jump of magnitude <6.

Each composed eta traverses half a period and meets at most one integer jump.
The factor 1/(2pi) in differentiation therefore gives

    Var(N_s') <= (c_e+c_d)[35/2+6]/(2pi) <=47/(2pi).

The same factors give Lip(N_s)<=12/pi, Var(N_s)<=12 and sup|N_s|<=8.
This argument does not require small phases. For
d0(z)=1/[2sin(z/2)]-1/z, the derivative of sin^2 x-x^2 cos x is
x^2 sin x-2cos x(x-sin x)>=0 on [0,pi/2], using the displayed sine
and cubic bounds. Hence d0 increases from zero to 1/2-1/pi.

The fundamental-theorem identity
(N_s(z)-N_s(0))/z=integral_0^1 N_s'(tz)dt is valid with the piecewise
derivative and its one-sided limits. Variation under this averaging is at most
Var(N_s'). Product variation then gives precisely

    sup|P_s|<=4+4/pi<6,
    Var(P_s)<=10+7/(2pi),

so the combined variation is <23. Integer-offset derivative jumps and the
phase-vertex endpoint limits do not invalidate these bounds.

## Generic cancellation and its enlarged central range

For J=I((u-s)/2,(u+s)/2,e), direct integration of the two short
opposite-sign intervals gives the source's separation-independent entropy
formula when s<=u. The two sine products in that calculation are
c sin(e)/u and b sin(e)/u, so the separation logarithms cancel exactly.
For s>u, the channel-equality equation is sin(2x+e)=s sin(e)/u.
Its two-root and no-root alternatives give the displayed formula(10) and
J=2s log(sin e), respectively. Limits handle u=0, c=0 and root coalescence.

After subtracting 2(s-u)_+ log(sin e), differentiating gives

    R_e=2[u cos e-sqrt((u^2-s^2 sin^2 e)_+)]/sin e >=0

for s>u, and zero for s<=u. For fixed u it increases with s until saturated.
In the root regime,
R_s=log[(s cos e-D)/(s cos e+D)], with D<=u cos e, giving the stated
integrable logarithmic bound. In the no-root regime R_s=0. The finite e=0
entropy and the e=pi/2 value give |R|<=max(2u,s+u)log2. Thus the full generic
identity and derivatives, not the near-domain conclusion, support this use.

On the central curves, u=p/2<=1/2 and s<=3/2. The integral of the
parameter-derivative envelope over [0,S] is at most
2u[1+log((S+u)/u)], with continuous zero limit at u=0. At S=3/2 its
maximum over u<=1/2 is 1+log4<5/2. The left curve has one monotone piece
and the right at most two. Their parameter-motion cost is therefore <15/2.
Monotonicity of R_e bounds the two separation-motion costs by <3 in total.

For k_s=2(s_s-u)_+, the common e=0 value is d=(q-p)_+<=1,
|k_s'|<=2a, and |k_s-d|<=2a tan(e/2). Applying these to the two product
terms in(13) gives variation <9/2 per side. Combining with the R costs gives
total variation <39/2<20. The independent sup bounds are
|R|<3/2, |(k_s-d)log(sin e)|<6/5 and
|d log(sin e/e)|<1/2, giving sup|Z_s|<4.

Both product terms tend to zero at e=0. The R terms have the same limiting
entropy from s_L(0)=s_R(0)=q/2. This proves the central extension, including
p=q, p=0 and a=0. No division by a small phase enters a final bound.

## Interior regular part and quadrature

On all expanded cells z>=delta-h/2>delta/2, the full-domain max formulas
give sup A<300 and Var(A)<600. The regular pole decomposition gives
sup|V|<1700 and Var(V)<3223.

On the endpoint halves, cot(z/2) yields s<=401. The two curves have
total variation <800 and at most three monotone pieces. Therefore k has
variation <1600 and sup<=802. Since -log(sin z)<7, product variation
is <22428. The same generic R argument now at S=401 gives parameter-motion
cost <24 and separation-motion cost <604. These imply the claimed endpoint
I variation <24000 and sup|I|<6000. The central subtraction
I-d ell=Z_s+d log(pi/2) has total variation <20 and sup<5, matches the
endpoint pieces at the cutoffs, and has equal limits at pi. There is no
additional jump to charge. Consequently sup|W|<4000 and Var(W)<12000
follow after division by pi>3 and addition of V.

The ordinary interior cells are disjoint. For H_reg=A L+W, centered BV
quadrature costs at most (300L+6000)/m. The full interior interval and the
cell union differ by at most four omitted special cells plus boundary pieces
of total length <=h. Their regular-part cost is <=(1500L+20000)/m.
Every original first/last R row lies in the endpoint strip, leaving at most
two central and two collision special rows in the interior. Their actual
finite-polynomial norms are bounded by (1200L+6800)/m plus their own
single-pole approximation errors, by the already reviewed continuity upper.

Ordinary sample distances from pi are >=h, hence their cell distances are
>=h/2. The two truncated logarithm variations total <=2log m. Including
d/pi and the outer normalization gives the midpoint cost log m/(pi m).
The at most four missing cells have length <=4h. The superlevel intervals
of |ell| show that their integral is maximized by the centered interval,
whose integral is 4h[1+log(pi/(4h))]. This is bounded by 4h(1+log m).
The exterior boundary pieces have ell=0. The total logarithmic cost is
therefore <(2L+3)/m. This includes the two central cells and every collision
hole, without assuming their locations avoid the singularity.

Adding the four displayed interior contributions gives exactly
(3002L+32803)/m. Its n>=10^6 uniform bound is <3/40; no uncharged central
integral or special row remains.

## Endpoint join, single shared errors and scalar budget

The original H4 theorem applies: n>=10^6 exceeds both 8R and
ceil(2pi R/delta). It includes all extracted endpoint rows and endpoint
collision holes exactly. Ordinary endpoint residuals cost Q. The endpoint
and interior ordinary rows are disjoint subsets of N1-02's nonspecial rows,
so their cancellation errors together cost E_n once. Their pole errors and
the interior special-row pole errors are disjoint subsets of the same
nonendpoint coefficient sum, so D_n is charged once. There is no Rhat/r_n
error because the special rows are polynomially exact. H4's own collision
replacement error is already in e4 and is not an omitted cancellation error.

The coefficient integral joins b_end to exactly b_full, as reconstructed in
the preceding full-diamond review. The interior constant integral is exactly
the one in the model contract. Thus the complete absolute error is bounded
by e4+Q+E_n+D_n+E_interior.

Independent rational envelopes at n=10^6,L<14 give:

| Component | Checked envelope / consequence |
|---|---|
| Finite endpoint rows | 0.10400179 <0.104002 |
| Mesh error | 0.004905341294 <0.004906 |
| Collision replacement | <0.000059 |
| Their total e4 | <0.11 |
| Q | strictly <0.14 |
| E_n | <=1001891/31500000 <0.032 |
| D_n | <11/100000000000 <10^-9 |
| Interior replacement | <74831/1000000 <0.075 |

For Q the rational envelope from pi>3 and log1600<8 is exactly
(2/300)[7+(2/3)(5+16)]=7/50. The original substitutions are strict,
so Q<7/50; the equality of the rational envelope is harmless. All ratios
with logarithms decrease for n>=10^6, as do the n^-2 and higher-order terms.
Hence the final strict bound is .357000001<.36=9/25, uniformly on the
whole closed diamond and for both parities.

## Executed checks and review limits

Executed two inline `python -` Fraction controls in `/workspace/padua_research`
with Python 3.12.14, no random seed or external package. The first exited1
only because the reviewer's Q-envelope assertion used strict '<' instead of
the exact equality just explained; the other eleven predicates passed. This
was a control transcription issue, not a source finding. The corrected control
exited0 and passed all twelve predicates in 0.000119107 process CPU seconds.
It checked the seven component envelopes, the Q-envelope equality, final sum,
elementary exponential bounds, W variation and Phi_0 second-derivative sum.
No author code or mathematical claim was changed in response.

These exact arithmetic controls supplement the written analytic reconstruction;
they do not replace a continuum argument with samples. No numerical integral,
phase grid, finite-degree kernel run, fit or independent replay of the author's
binary64 diagnostic was performed. The frozen full compact-model error claim
has no remaining scoped finding. Formal Claude audit, any material follow-up,
and the separately owned model-maximum comparison remain outstanding.
