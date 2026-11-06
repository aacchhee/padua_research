# Independent supplementary review — C08 endpoint constant

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules were read at
`4b728b04216a5490910780bc609a82b853058426`; the AGENTS/WORKFLOW/CODEX
diff to review input HEAD `547a473a6e1c1268ff4f1ada7243b12afb02d0bc`
is empty. Branch: `codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at the stated auxiliary scope, with no mathematical
finding.** The exact endpoint limit, uniform finite-cutoff error, and
strict upper constant hold on the full closed phase triangle. They do
not bound the remaining renormalized integral. The main far-model
comparison remains OPEN. Formal Claude audit is separate and pending.

## Frozen input and review scope

Reviewed `theory/C08-far-endpoint-constant.md`, SHA-256
`3bd4653b0cf2e1f33e42f8629c06a32b45b546f198e6659cf0203fb48240647c`.
The full source, C08 idea and attempt including the new-main delta
addendum, and C06's exact full-phase model contract were read. The
N1-04/06/07 definitions and proofs, locally proved PD-T269 cotangent
partial fraction, and accepted C08 weighted coefficient lemma were
used with their original scopes. This report checks the new analytic
lemma and its interface to the exact C06 endpoint constant; it does
not re-audit every C06 finite-mesh error estimate. Historical novelty,
priority and a full author-search/registry audit are excluded.

No numerical quadrature, fit, sample, mathematical program or
computational certificate was used. Checking commands were source
reads, hashes and the rules diff. Only this new report was written;
author sources, old reports, shared files and Git state were untouched.

## Model normalization

The retained C06 endpoint family is

    C_R=ell_0(beta)+sum_(r=1)^(R-1)ell_r(alpha,beta)
                     +sum_(r=1)^R ell_r(alpha,-beta).

In particular the two orientations have different last rows. The
h_R and g_R used here are N1-06's infinite convergent constants,
not the fixed-J truncated constants of the near model. The identities

    B0=4a/pi²,
    D0=U0/pi+B0 log pi=a[C(t_d)+C(t_e)]/pi²

follow from Phi0's exact definition and
sin(pi*t_d)=cos((alpha-beta)/2),
sin(pi*t_e)=cos((alpha+beta)/2). All weighted products have their
continuous interpretation. Thus E_R in the source is exactly the
endpoint part of C06's C_far. The terms
B0 log²(delta/pi)+2D0 log(delta/pi)+(1/pi) integral B remain outside
E_R. There is no replacement of the fixed R=64 model by an infinite
model in the claimed application.

## Shifted sums and exact row cancellation

The defining reciprocal series gives the recurrence, shifted harmonic
identity and reflection formula for psi with the stated signs.
For f(u)=1/u, the summed nonnegative trapezoid errors equal
log x-1/(2x)-psi(x). Their integral kernel is at most 1/8, and
integral_x^infinity f''=1/x². This proves the real-shift bound for
every x>0 without integer interpolation. Expanding log(r+q) and
-1/[2(r+q)] separately gives the source's error interval
[-5/(8r²),1/(2r²)], hence its absolute 5/(8r²) bound for 0<=q<=1.

Factoring each rational term in ell_r gives exactly

    ell_r=sin b/[pi(r+s)]
          +(2a/pi²)[H_r(q_-)+H_r(q_+)]/(r+s),
    q_-+q_+=1+s.

The factor 2 includes the spacing-two odd denominators. On the
anti-diagonal k+l=r-1, the two denominators add to r+s, proving
the reciprocal-product convolution formula directly.

For b=beta, q_-=1-t_d and q_+=t_e. Substitution of the reflection
identity shows the difference between the constant numerator and D0
is sin(beta)/pi+(a/pi)[cot(pi*t_e)-cot(pi*t_d)]. The cotangent
difference is -sin(beta)/a, so the cancellation is exact. For b=-beta
the complementary shifts and sine both reverse and give the same D0.
Thus the large-argument row formula (11) has no missing signed sine
term. Its extension to boundary phases uses large arguments r+q only;
no value psi(0) is assigned. For r>=64 its denominator stays positive,
including t=1 in the negative orientation.

## Identification of the constant

For fixed positive p,q, H_R(p)H_R(q) has the stated logarithmic
expansion. Its complement to the triangular convolution is the upper
triangle k+l>=R inside the square. Away from the axes, ordinary
Riemann convergence applies. The thin side k<=eta R contains at most
k+2 entries in each row, with its other denominator bounded below
by R(1-eta)-2. The source's bound by
R^-1 sum_(k<=eta R)(k+2)/(k+p) therefore has limiting size O(eta),
including the fixed-p harmonic residual O(log R/R). This justifies
the improper integral and its value pi²/6; the latter follows from
nonnegative integration of -log(1-u)/u and the local cotangent
partial fraction at zero. A one-layer change costs O(log R/R), so
the unequal last rows of C_R do not change the constant.

The signed sine contribution, including ell_0, is cos beta: the
series has exactly the difference 1/(r+t)-1/(r-t), not its negative.
The h_R series telescopes exactly to -psi(R+t); the centered g_R
tail is O(log R/R²), giving g_R=-log² R/2+o(1). Their products
cancel the logarithmic divergences from the two convolutions using
the exact D0 identity above. Each convolution contributes -pi²/6,
so the remaining expression is precisely source (14).

Writing the complementary psi values as half their sum and difference
gives the cross product

    [C(t_d)C(t_e)-pi² cot(pi*t_d)cot(pi*t_e)]/2.

The trigonometric product a*cot(pi*t_d)*cot(pi*t_e) equals
(cos beta-cos alpha)/2. Hence the signed sine term becomes a,
and the two triangular-complement constants subtract 2a/3.
The final coefficient is therefore a/3, with the other term
a*C(t_d)*C(t_e)/pi². This verifies both the normalization and sign
of the asserted limit.

## Uniform paired tail and boundary phases

Increasing R adds ell_R(alpha,beta) and ell_(R+1)(alpha,-beta).
The h_R and g_R differences subtract the corresponding reciprocals
and logarithmic reciprocals with exactly those same denominators.
D0 cancels before estimating. The remaining increment is
(2a/pi²)[J_R(t)+J_(R+1)(-t)]. All shifts q belong to [0,1] on the
entire triangle, since |alpha/pi|<=1-beta/pi.

The numerator of J_r(s) is -s/r plus an error bounded by
(5/4+64/63)/r²<23/(10r²). Dividing by r+s>=r-1 gives an error
less than 5/(2r³), as stated. The two leading fractions combine to

    -t(1-t)(2R+1)/[R(R+t)(R+1)(R+1-t)].

Their magnitude is less than R^-3; the two errors sum to less than
5R^-3. Multiplying by 2a/pi²<2/9 even gives 4/(3R³), so the
claimed 2/R³ has slack. Summing this uniform bound and comparing
the decreasing series with the integral from R-1 proves the strict
error 1/(R-1)².

Each finite E_R is continuous by N1-07's sinc charts and the
convergent h/g definitions, including its w=0 endpoint chart.
The uniform tail therefore supplies a continuous limit on the closed
triangle. Independently, write the claimed product as

    a C(t_d)C(t_e)
      =[cos((alpha-beta)/2)C(t_d)]
       [cos((alpha+beta)/2)C(t_e)].

Both factors have the already proved continuous endpoint value pi.
At either vertex their product is pi² and E_infty=1. On the open
a=0 edge the first weighted factor stays finite and the second tends
to pi. This covers joint approaches as well as approaches along an
edge. Interior identification and density now identify the same limit
at all boundary and collision phases. No uniform improper convolution
limit was assumed to obtain this result.

## Strict scalar upper and scope

The elementary gamma and log 2 inequalities give 7/2<C0<4 in
the needed strict directions. The accepted C08 weighted inequality
then bounds each positive weighted C factor by C0. Since 0<=a<=1,

    E_infty<=1/3+C0²/pi²
            <1/3+320/197=1157/591<49/25.

The final rational comparison is 28925<28959. At R=64 the error
is less than 1/3969<1/3000. These estimates apply to the exact
retained endpoint family throughout the full closed triangle.

The source explicitly leaves the renormalized integral unbounded.
Its conditional observation that an upper 53/100 for that integral
would suffice for C_far<5/2 is arithmetically valid, but supplies no
such premise. This acceptance does not establish the far-model
maximum comparison, the original global argmax claim, or any
historical novelty assertion.
