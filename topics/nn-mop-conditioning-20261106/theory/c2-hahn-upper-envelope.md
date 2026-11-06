# PD-N181 — separate terminal maxima lose the Hahn rate

ID kind: PD-N. Aliases: product-of-maxima upper obstruction;
Hahn center/endpoint mismatch. Split from: none. Split into: none.

## Statement and precise scope

Use P,Q2,W2 of `c2-hahn-terminal-rate.md` at the balanced terminal index,
for each M>=2. The exact second-weight derivative row has norm

    D_M=sum_(k=0)^M W2(k)|P(k)Q2(k)|/M!.

Consider its simple, valid upper envelope

    E_M=(sum_(k=0)^M W2(k))*max_k|P(k)|*max_k|Q2(k)|/M!.

Then D_M<=E_M, but

    limsup_(M->infinity) E_M^(1/M)>=beta>12.4>rho_H,
    beta=2sqrt((11+5sqrt(5))/2)*(3125/256)^(1/4).          (1)

In particular E_M cannot be bounded by C M^a rho_H^M for any fixed
C>0 and a. Thus replacing the two factors by separate global maxima
cannot prove a matching rho_H upper, even for this terminal row.

This result only rejects that estimate. The exact correlated row has
rate rho_H by the dependency; a full-input/four-field upper for the
Hahn NN map remains OPEN. It does not refute that target, assert a
larger full-map rate, or rule out a different Cauchy-kernel argument.

## Definitions, status and dependencies

Exact M+1 integer nodes, alpha1=1,alpha2=3/2,gamma=1, and balanced index
(ceil(M/2),floor(M/2)), as in the terminal-rate proof. W2 is
unnormalized. Its total mass is (9/2)_M/M!, a polynomial-order factor.
Changing to normalized weights leaves this envelope unchanged because
the dual scales inversely with that normalization.

Overall status: PROVED (scoped failed-route lemma).
Candidate: [IDEA-596](../candidates-response-C2.md#ideann-mop-cond-codex-c2-03-r4--separate-global-maxima),
a retained subform of parent C2-03.
Candidate disposition: REJECTED: failed (global-maxima decoupling); retain
pointwise correlation and the full sharp-Hahn target. Closest entries:
IDEA-534/535 and C2-03. No external theorem or novelty claim.

Depends on `c2-hahn-terminal-rate.md` equations (3)--(6), their strict
signs, and its elementary positive-coefficient finite-type argument.
No numerical fit or additional asymptotic theorem is needed.

## Proof

The signs in the dependency show every summand of the parity derivative
has the same sign. Hence its magnitude is exactly the row norm D_M,
and the elementary inequality D_M<=E_M follows.

Restrict to M=4l+2. Then k=M/2 is an integer, the second-weight row
j=M/2 is odd, and i=(j-1)/2=l. The explicit terminal polynomial gives

    |P(M/2)|/M!
      =(M+1)! T_(M,M/2)/((2M+6)_M(M/2+1)).              (2)

Writing s=M/2, its positive coefficient is

    T_(M,M/2)=[z^s](1-z)^(-4)G(z)^s,
    G(z)=(2-z)/(1-z)^2=sum_(j>=0)(j+2)z^j.

The saddle rG'(r)/G(r)=1 has the unique solution
r0=(3-sqrt(5))/2 in (0,1), and

    G(r0)/r0=(11+5sqrt(5))/2=lambda.

The positive-evaluation upper bound and finite-type lower from section6
of the dependency apply to this G as well: its constant, linear and
quadratic coefficients are positive; its normalized coefficient law
at r0 has mean one and finite moments. For clarity the lower uses
fixed finite q of mean one approximating that law, n_j=floor(sq_j)
for j>=2, n1=s-sum_(j>=2)j n_j and n0=s-n1-sum_(j>=2)n_j.
All counts are eventually nonnegative and their type entropy tends
to zero as the truncation increases. Thus

    lim_(s->infinity) T_(2s,s)^(1/s)=lambda.

Integral bounds for log(n!) give log(n!)=n log n-n+O(log(n+1)).
The fixed shifts of the factorials contribute O(log M), so

    lim ((M+1)!/(2M+6)_M)^(1/M)=4/27.

Equation (2) therefore yields, along M=4l+2,

    lim (|P(M/2)|/M!)^(1/M)=(4/27)sqrt(lambda).          (3)

All terms of Q2(M) have the same negative sign. Retain only the row
j=M/2, i=l in its positive magnitude. Formula (3) of the dependency
gives

    |Q2(M)| >= (2M+4)_M/((2M+4+j)j!(M-1-j)!)
                     *(M+5/2)_i/((5/2)_i(M+7/2+i)).     (4)

Since j/M->1/2 and i/M->1/4, the same log-factorial integral estimate
(or its gamma half-integer form, from (1/2)_r=(2r)!/(4^r r!)) gives

    lim [(2M+4)_M/((2M+4+j)j!(M-1-j)!)]^(1/M)=27/2,
    lim [(M+5/2)_i/(5/2)_i]^(1/M)
         =(5/4)^(5/4)/(1/4)^(1/4)=(3125/256)^(1/4).

The remaining factor in (4) is polynomial, and the positive total
weight has Mth-root limit one. Multiplying (3),(4), and using the
independent admissible maxima in E_M proves its limsup lower in (1).

For an exact rational separation, sqrt(5)>559/250 implies
sqrt(lambda)>333/100, and (3125/256)^(1/4)>1863/1000;
these follow by squaring or taking fourth powers. Thus
beta>2*(333/100)*(1863/1000)=12.40758>12.4.
Meanwhile rho_H<7+3sqrt(3)<61/5=12.2, because sqrt(3)<26/15.
Hence beta>rho_H. A polynomial times rho_H^M has Mth-root limit
rho_H, contradicting (1) if it bounded E_M for all M. This completes
the scoped route rejection.

## Checks and remaining targets

This is an analytic statement; no finite computation establishes its
limsup. The underlying polynomial and dual identities already have
exact defining-moment checks in the terminal receipt and a separate
independent reconstruction. A useful full-map route must retain their
correlation at each k and extend to arbitrary indices, both weight
channels, common node forcing and all four NN fields. None of those
extensions follows by enlarging E_M or by fitting the terminal row.

## History

2026-11-06: Codex gpt-6.1-sol xhigh; local rules/source
76ba4214b100c86a44941f5e9a662ce9ce48efb8, published topic pin
b4a04981d42c7cd872957facf5e3995e4096ca67. Prospective round4 subroute
gate in `../novelty-gate-C2.md`. No Git/shared registry mutation.

2026-11-06 response, Codex gpt-6.1-sol high, rules/source `3d5b29d`:
added the explicit round-4 candidate ID/link for MAJOR-3. Statement,
proof, PROVED negative status and rejected scope are unchanged.

## Final ID aliases (2026-11-06)

- `PD-N?nn-mop-cond-codex-C2-01` → `PD-N181`.
- `IDEA?nn-mop-cond-codex-C2-03-r4` → `IDEA-596`.
