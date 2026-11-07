# PD-T?argmax-bridge-codex-D37-envelope — A fixed constrained inner-far upper

ID kind: PD-T. Aliases: half-multiplier anisotropic box; monotone
large-coordinate quartic tails. Split from: D37 global1024 candidate.
Split into: the all-n application is D37-assembly-global1024.

## Statement and status

Use the TRUE completed constant with D37-constant-wide's proved
directional modulus. For x,y>=0,1/2<=rho=x+y<=1 put
a=(cosx+cosy)/2,u=1-a. Let V>=0,K>=0 andC>=0 be any real constants.
Suppose an actual increment is bounded by

    Increment<=C-uV+DeltaC+K(x+y),
    DeltaC=C_infty(x,y)-C_infty(0,0).             (1)

Set Bx=1,By=1/10,cB=47/192,cL=11/48,

    qBx=cB*V-53/40,qBy=cB*V-119/120,
    qLx=cL*V-53/40,qLy=cL*V-119/120.

Require all q positive. Define the standard exact radical maximum

    z(B,q,k)=[3B+sqrt(9B²+32qk)]/(8q),
    Psi(B,q,k)=(B/4)z³+(k/2)z²
             =sup_(t>=0)[B*t^(3/2)-q*t²+k*t].  (2)

Then on the box x,y<=1/2,

    Increment<=C+Psi(Bx,qBx,K+1/2)
                       +Psi(By,qBy,K+1/2)-1/4. (3)

If additionally qLi>3Bi/(2sqrt2)+K for i=x,y, set

    Ex=Bx/(2sqrt2)-qLx/4+K/2,
    Ey=By/(2sqrt2)-qLy/4+K/2.

On the large-coordinate regions respectively,

    x>=1/2: Increment<=C+Ex+Psi(By,qLy,K),
    y>=1/2: Increment<=C+Ey+Psi(Bx,qLx,K).        (4)

These CLOSED regions cover the whole inner far strip, including all
seams and the axes. Status: **PROVED analytic sufficient envelope**,
distinct review pending. The multiplier1/2 is FIXED prospectively;
no coefficient fit, phase optimizer, numerical root or endpoint job.

## Directional reduction before enlarging a domain

D37-constant-wide gives

    DeltaC<=(3/5)x^(3/2)+(19/24)(x²+y²)
       +(8/15)x²[1+log(1/x)]+(2/15)y²[3/2+log(1/y)].

All actual coordinates are<=1. Since sqrt(t)log(1/t)<=2/e<3/4
on0<t<=1, the logarithmic terms are bounded by(2/5)x^(3/2)
and(1/10)y^(3/2), including their continuous zero values. Thus
the fractional coefficients become EXACTBx=1,By=1/10 and the
quadratic costs are EXACT19/24+8/15=53/40 and
19/24+(3/2)(2/15)=119/120.

For coordinates<=1/2, the alternating cosine bound yields
u>=r2/4-(x^4+y^4)/48>=cB*r2. On the whole rho<=1 domain it
gives u>=cL*r2. Multiplication by-V preserves the desired direction
because V>=0. Consequently(1) is bounded on its ACTUAL domain by

    C+fx(x)+fy(y), f_i(t)=Bi*t^(3/2)-qi*t²+K*t,

with the applicable B or L quadratic coefficients. No physical/model
theorem is applied to fictitious independent phase values.

## Fixed half-multiplier on the small-coordinate box

On the actual far strip rho>=1/2,
(1/2)(x+y)-1/4>=0. Add this nonnegative quantity to the polynomial
upper before maximizing. The result is bounded by(3), using the
separated supremum(2) on the larger nonnegative quadrant. Enlargement
is applied only to those explicit polynomial expressions AFTER their
valid original-domain reduction, never to the physical cosine bound.

For completeness, writing s=sqrt(t) gives the quartic
-q*s^4+B*s³+k*s². Its nonnegative maximizer solves
4q*s²=3B*s+2k and is the z in(2). Substitution gives the NONNEGATIVE
value Bz³/4+kz²/2. Zero B or k are included. This is accepted D22's
exact algebraic maximum, restated here, not a numerical root search.

## Large-coordinate monotonicity, rather than a mixed maximum

For t>=1/2,

    f_i'(t)=(3/2)Bi*sqrtt-2qi*t+K.

The stated condition makes f_i'(1/2)<0. Its derivative is
(3/4)Bi/sqrtt-2qi, which is negative throughoutt>=1/2 under the
same stronger condition. Hence f_i decreases from its boundary value
f_i(1/2)=Ei. Bound the other polynomial by its full supremum(2),
proving(4). At x=y=1/2 both bounds remain valid; nothing is omitted
by choosing overlapping closed cases. The upper may be negative,
which correctly certifies strict descent if the total is negative.

## Monotonicity and limitations

Psi decreases when q increases or k decreases by pointwise ordering
inside its supremum. Each boundary Ei decreases when qi increases
or K decreases. Therefore all three upper bounds decrease when V
increases and C,K decrease, once their stated positive domains and
tail conditions hold. The conditions themselves then persist.

This supplies a generic sufficient inner-far upper, not a positive
1024 budget, a full relative-error theorem or a claim about actual
argmax location. The finite allowance must establish(1) with EVERY
charge including the actual-origin conversion. No source/scalar/
native/phase/board/quadrature/degree job occurred. 2026-11-06,
Codex gpt-6.1-sol xhigh45min lead, inputeb9329c28be18d77eeb817f634202d626ee11f92,
serving metadata unexposed. Distinct review required before adoption.


## Current result and root final adoption — 2026-11-06

Current status: **PROVED** at this record's stated support/assembly scope. Final [D37 review](../independent-checks-D37-global1024.md), SHA256 `2ad8f232aa88bc15e360be7b61c1c110dd1f9ff2f667850167c7d456d57bcda5`, accepts the unchanged five paper scopes and sole primary/fresh independent1024 endpoints. All59intervals+pi,16domains,33controls,60containments pass. Root adopts exact two-corner global argmax EVERYintegern>=1024, near noncorner gap1/200 and complete closed far gap3/100, with accepted D27 actual-corner loss1/8. The harmless intermediate zero-phase strict-display NOTE W0 and explicit zero cases remain in the review. Historical conditional/OPEN endpoint wording above is preserved; no scope below1024 or minimal-onset claim follows. Final Claude audit remains separate.
