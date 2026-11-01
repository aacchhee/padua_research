# PD-T?proof-attempts-2-codex-90 — Pole top form and detection of all lower-block leakage

ID kind: PD-T.
Aliases: B1 project-two/constrain-one detection; next-pole top form; parallel diagonal rational flag.
Split from: programme `OPEN_TARGETS.md` B1, lower-leakage/detection obligation.
Split into: none. Generic generation and the completed class theorem are separate records 91 and 92.

## Statement

Fix a finite integer `T>=3`. Let `z_i=(x_i,y_i)` be `M` real nodes in `[-1,1]^2`, with positive weights `w_i`, such that evaluation on `Pi_(T+1)` is injective; in particular `M>=dim Pi_(T+1)`. Write `s=x+y`. For arbitrary real offsets `a_1,...,a_(T+1)>2`, including repeated offsets, put

`ell_j=s-a_j`, `pi_j=prod_(r=1)^j ell_r`, `V_j=Pi_j/pi_j`, `W_j=V_j orthogonal-difference V_(j-1)`.

These are evaluated subspaces with the real inner product `sum_i w_i f(z_i)g(z_i)`. For `2<=t<=T`, set `k=t-2`, `a=a_(t+1)`,

`C_t=(W_(t-1)+W_t+xW_t+yW_t)/ell_(t+1)`,
`R_t=(I-P_(W_t)-P_(W_(t-1))) C_t`.

For a polynomial `p=sum_(d=0)^k p_d` with homogeneous components `p_d`, define its next-pole top form

`tau_(a,k)(p)=sum_(d=0)^k (s/a)^(k-d) p_d`, an element of `H_k`.

Then:

1. Each `r in R_t` has a unique linear functional `Lambda_r` on `H_k` such that, for every `p in Pi_k`,
   ` <r,p/pi_k> = Lambda_r(tau_(a,k)(p)) `.
2. The map `W_k -> H_k`, `q -> tau_(a,k)(pi_k q)`, is an isomorphism.
3. Consequently `r in R_t` and `r perpendicular W_k` imply `r perpendicular V_k`, hence `r in W_(t+1)`. Thus the constraint detects **every** lower-block leakage direction, for all these offsets, with no generic-rank assumption.
4. `dim R_t <= 2t+1`.

## Definitions

`Pi_j` is the real bivariate polynomial space of total degree at most `j`; `H_j` is its homogeneous degree-`j` part. `V_(-1)={0}`, `pi_0=1`. A rational function denotes its sampled vector, with its numerator uniquely identified at the displayed degree by injective evaluation. Multiplication by `x`, `y` or a pole factor is componentwise at the nodes. All projectors are for the fixed positive weighted inner product.

## Assumptions

The fixed finite degree ceiling, positivity, injectivity and real offsets in the statement are used explicitly. Since `s(z_i)<=2<a_j`, every `ell_j(z_i)<0`; all denominators are nonzero. The flag is nested because multiplying a degree-`j-1` numerator by `ell_j` embeds `V_(j-1)` into `V_j`. Its dimensions are `dim V_j=(j+1)(j+2)/2` and `dim W_j=j+1`. No claim is made for arbitrary complex poles, a sign-changing new/old pole ratio, or insufficiently determining samples.

## Status by part

Overall status: **PROVED**. Complete written proof and actual supplementary full-file inspections are recorded below; no computation is a dependency. Part 2 Claude audit remains PENDING.

| Mathematical part | Status / verification obligation |
| --- | --- |
| Pole top-form factorization, detection and rank bound | PROVED; written analytic proof below and actual independent full-file candidate inspections |

Candidate / claim disposition: retained exact completion route; no novelty claim.

## Depends on

Elementary finite-dimensional positive inner-product linear algebra and the explicit assumptions above. No part 1 theorem, source generic-rank claim or numerical measurement is used as a proved dependency.

## Checks

Parent Codex and both independent mathematical agents ACTUALLY read the complete frozen candidate file and found no mathematical blocker. Their exact reviewed hashes and scopes are in `../independent-checks-b1.md` and `../independent-checks-b1-topform.md`. These are supplementary full-file proof inspections, not Claude audit. Promotion changes status/verification metadata only; `../outputs/b1_status_metadata.json` records matching proof-body hashes before and after. No mathematical code was executed. Part 2 Claude audit remains PENDING.

## Sources

Programme `OPEN_TARGETS.md` B1; part 1 `attempts/T-B1-optional.md`; programme `checks/adversarial-gen1-3.md` (ii)(1), `checks/decisive-gen1-3.md` Finding 0; PD-N040. These identify the target and prior obstacles, not the proof below. Input provenance is in `../b1-input-preparation.md` and `../attempts/T-B1.md` at rules/input head `ec05862985460ed18d6756b2bd9b4c5266b39df2`.

## Proof

### 1. The precise top-form quotient

The map `tau=tau_(a,k)` is onto `H_k`, since it is the identity on `H_k`. Moreover

`ker tau = (s-a) Pi_(k-1)`

with the right side zero when `k=0`. Indeed `tau((s-a)q)=0` follows by cancellation of homogeneous components. Conversely each term `((s/a)^(k-d)-1)p_d` is divisible by `s-a` and its quotient has degree at most `k-1`. Hence `tau(p)-p` belongs to `(s-a)Pi_(k-1)`; if `tau(p)=0`, so does `p`. This proves the kernel identity without a rank assumption.

This is a literal homogeneous top form, in coordinates associated with the next pole. Put `X=x/(s-a)`, `Y=y/(s-a)`. Since `1/(s-a)=(X+Y-1)/a`, the expression `p(x,y)/(s-a)^k` is a polynomial of degree at most `k` in `X,Y`. Its homogeneous degree-`k` part is exactly `tau_(a,k)(p)(X,Y)`. Thus the functional used here is a projective top-form functional at the next pole. It is distinguished from the source's original-at-infinity skew/gauge functional, whose unproved rank assertions are unnecessary here.

### 2. Factorization of the lower pairings

Choose `f in C_t` projecting to `r`. Write

`f=(u+v+x h+y j)/(s-a)`,

where `u in W_(t-1)` and `v,h,j in W_t`. Projection off the top two old blocks does not alter pairings against `V_k`, so `<r,p/pi_k>=<f,p/pi_k>`.

If `p=(s-a)q`, `deg q<=k-1`, real componentwise cancellation gives

`<f,p/pi_k> = <u+v+xh+yj,q/pi_k>`.

Here `q/pi_k`, `xq/pi_k`, and `yq/pi_k` all lie in `V_k` (the latter two have numerator degree at most `k`). The first term vanishes because `u perpendicular V_k`; all other terms vanish after moving the real coordinate multiplier to the test vector, because `W_t perpendicular V_(t-1)` and `V_k subset V_(t-1)`. Thus the pairing vanishes on `ker tau`. The onto quotient map from part 1 gives a unique functional `Lambda_r` with the asserted formula. For `k=0`, the zero kernel gives the same conclusion directly.

### 3. Why the detector block sees the entire form

For `k>=1`, let `q in W_k` have `tau(pi_k q)=0`. By part 1 its numerator is `(s-a)b`, `deg b<=k-1`. Put `v=b/pi_(k-1) in V_(k-1)`. Then

`q=((s-a)/(s-a_k)) v`.

Both numerator and denominator of this ratio are strictly negative at every node, so the ratio is strictly positive. Orthogonality gives

`0=<q,v>=sum_i w_i ((s_i-a)/(s_i-a_k)) v(z_i)^2`.

Every summand is nonnegative with a strictly positive coefficient. Hence `v=0` as a sampled vector, and then `q=0`. The detector map is injective; domain and codomain both have dimension `k+1`, so it is an isomorphism. For `k=0` it is the identity on constant numerators.

If `r perpendicular W_k`, the factorization in part 2 and this onto detector imply `Lambda_r=0`. Therefore `r perpendicular V_k`. By construction `r` is also orthogonal to `W_(t-1)` and `W_t`, and `r in V_(t+1)`. Since `V_t=V_k direct-sum W_(t-1) direct-sum W_t`, we obtain `r in W_(t+1)`.

Finally the map `r -> (P_(W_(t+1))r,P_(W_k)r)` on `R_t` is injective. A vector in its kernel is orthogonal to `W_k`, hence belongs to `W_(t+1)` by the preceding argument, and its first component then makes it zero. The target has dimension `(t+2)+(t-1)=2t+1`, proving the rank bound.

### 4. Explicit transport from the ordinary top numerator forms

For comparison with the source's notation, let `Top_j:W_j->H_j` take the ordinary highest-degree part of the numerator `pi_j w`. This too is an isomorphism under the current assumptions. If that top part vanishes, `ell_j w` belongs to `V_(j-1)`, giving `0=<w,ell_j w>`; the strictly negative pole factor forces `w=0`. Dimensions give the isomorphism, with the constant case immediate.

Define the invertible map on `H_j`

`B_(j,a)=tau_(a,j) composed-with (w -> pi_j w) composed-with Top_j^(-1)`.

Its invertibility follows from the detector argument above applied at degree `j`. The maps `Top_j` and `tau_(a,j)` are thus explicitly distinguished: the former is the ordinary infinity top numerator, while the latter is the next-pole projective top form.

The homogenization formula defining `tau` is multiplicative when the degree bounds add. Since `tau_(a,1)(ell_m)=(1-a_m/a)s`, every `w in W_j`, `0<=j<=k`, has the exact lower-block pairing

`<r,w> = [prod_(m=j+1)^k (1-a_m/a)] Lambda_r( s^(k-j) B_(j,a)(Top_j w) )`.

Indeed its numerator with denominator `pi_k` is `(prod_(m=j+1)^k ell_m)(pi_j w)`; apply the factorization from part 2 and multiplicativity. Empty products are one. Possible zero scalar factors at coalescence cause no difficulty. This formula expresses all lower-block leakage through a single functional on homogeneous forms, with an explicit transport from each ordinary top numerator form; no source skew-form rank has been assumed.

## Scope and open items

This proves detection, not the reverse inclusion `W_(t+1) subset R_t`. That separate obligation is addressed by the coalescent structural witness and pole-only algebraic argument in record 91. The unrestricted multi-class B1 target remains separate; no numerical stability conclusion is asserted.

## History

2026-11-01, Codex `gpt-6.1-sol xhigh`, within the 16:35:09–18:35:09 UTC B1 box. Replaces an unsupported source skew-rank transfer by the explicit next-pole top-form quotient. Full proof written before status promotion; no computation or external theorem borrowed.
