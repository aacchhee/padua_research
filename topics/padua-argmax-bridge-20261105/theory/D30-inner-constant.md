# PD-T?argmax-bridge-codex-D30-constant — Eleven times one-minus-a on the inner far strip

ID kind: PD-T. Aliases: anisotropic three-quarter constant strip;
entropy/Young corollary of the accepted D24 directional modulus.
Split from: D30 two-region far. Split into: none.

## Statement and status

For EVERY real signed phase pair on the CLOSED strip

    1/2<=rho=|alpha|+|beta|<=3/4,
    a=(cos|alpha|+cos|beta|)/2,u=1-a,

the TRUE completed constant of D02/D24 satisfies

    C_infty(alpha,beta)-C_infty(0,0)<11u.          (1)

Status: **PROVED analytic developer corollary**, distinct review pending.
The only substantive input is the accepted D24 directional modulus
on its correctly enlargedrho<=3/4 domain. No through-origin quadratic
claim, finite primitive/error estimate, onset or new numerical premise.

## Exact directional proof

Take x=|alpha|,y=|beta| andr2=x²+y². D24 gives

    DeltaC<=(8/15)x^(3/2)+(19/24)r2
       +(1/2)x²[1+log(1/x)]+(1/8)y²[3/2+log(1/y)]. (2)

All zero logarithmic products are continuous0. Withrho>=1/2,
log(1/rho)<=log2<7/10. Also log(rho/x)=log(1+y/x)<=y/x,
and similarly fory; multiplying by the vanishing quadratic extends
this bound to the axes. Thus the two log-relative terms are bounded
by(5/8)xy, and the nonfractional part of(2) is at most

    (197/120)x²+(16/15)y²+(5/8)xy.               (3)

For the fractional term, concavity gives the GLOBAL tangent bound
sqrtx<=(x+1/2)/sqrt2. Sincex+y>=1/2,

    x^(3/2)<=(x²+x/2)/sqrt2
                    <=sqrt2*x²+xy/sqrt2.

Using sqrt2<10/7, the fractional contribution is therefore at most
(16/21)x²+(8/21)xy. Inserting in(3) yields

    DeltaC<=(673/280)x²+(16/15)y²+(169/168)xy.    (4)

The elementary weighted Young inequality

    (169/168)xy<(21/20)xy
                     <=x²/5+7y²/5              (5)

holds forx,y>0; at an axis use the corresponding weak form. Its
second inequality follows from the positive determinant
(1/5)(7/5)-(21/40)²=7/1600>0, or completing the square.
Consequently(4) is bounded by

    (729/280)x²+(37/15)y²<=(729/280)r2.          (6)

On this stripr2>0, and the alternating cosine bound gives

    u>=r2/4-(x^4+y^4)/48>=61r2/256.

Finally729/280<11*(61/256)=671/256, since186624<187880.
Equations(6)--(7) prove the STRICT bound(1), including both axes
and both strip seams. Separate phase evenness does not exchange
n,m or assert symmetry of the finite primitive. QED.

## Scope and provenance

D24's fractional and both entropy terms have all been charged;
none is dropped as small. The quadratic ratio is asserted ONLY
away from zero. The accepted D10 positive fractional-axis obstruction
through phase zero remains intact. The outer regionrho>=3/4 still
uses the independent accepted25/2 coefficient, not this11 bound.
No scalar/native/phase/board/quadrature/degree job or fitting occurred.
2026-11-06, Codex gpt-6.1-sol xhigh30min paper allocation;
rules/input09cc533678a22b38f40b70be95426ebbe81faa93,
serving metadata unexposed. Distinct review required before adoption.


## Root review closure — 2026-11-06

Distinct [D30 review](../independent-checks-D30-far.md), SHA256 `9ae9c0415625b36f908c1cabe70e44fd64028af08ec162641dde58fdc9ab85b8`, accepts the wide actual-six-row bound, inner11u constant and conditional two-region far implication without unresolved findings. Root adopts those exact support scopes. Both2048 endpoint signs remain UNCOMPUTED here; no unconditionalfar/global2048 follows until the separately frozen D33 computation/result review and other assembly premises. Reviewed prefix is preserved; final Claude audit remains separate.
