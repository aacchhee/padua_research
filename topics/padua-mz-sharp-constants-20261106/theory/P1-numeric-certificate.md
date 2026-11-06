# PD-T?mz-sharp-codex-P1-04 — coarse rectangle enclosure

ID kind: PD-T.
Aliases: exact angular Darboux instance; constant-vector Schur certificate.
Split from: numerical instance of P1-03 finite rectangle reduction.
Split into: practical three-digit c_minus and c_plus enclosures remain OPEN.

## Statement and status

For the exact operator B identified in P1-01/02, put r=||B||. The finite
check at N=16,theta=256 certifies the exact enclosure

    L <= r <= U,
    -U <= c_minus <= -L,

where, with S=2^256,

    L=1524396659976380815246835773573053256156125250651221590007974186558840498736/S,
    U=55326534787122342745740713698404372650886854985644685910272386076268567928344/S.

Outward decimal display:

    0.013164946500379018110831 <= r <= 0.477809279990884889210594,
    -0.477809279990884889210594 <= c_minus
                              <= -0.013164946500379018110831.

Overall status: **PROVED**, computer-assisted local development with
distinct code/scalar/reduction reconstruction and actual rerun PASS.
Required Claude audit is separate.
This interval certifies no practical three-digit value. The inherited
strict positivity of c_plus gives only 0<c_plus<=r<=U; no c_plus
Galerkin/residual solve or improved positive spectral approximation is
claimed. Existing stronger analytic one-sided lower bounds for r may be
combined by the coordinator, but are not silently built into this output.

## Definitions, assumptions and dependencies

Use D={(a,b):a,b>0,a+b<1}, H=L²(D,ab da db), positive symmetric kernel
A=-B and c_minus=-||B|| from
[P1-elliptic-kernel.md](P1-elliptic-kernel.md) and
[P1-positive-spectrum.md](P1-positive-spectrum.md). The exact finite
reduction is [P1-rectangle-certificate.md](P1-rectangle-certificate.md),
equations (1),(4),(8)–(12). P4's already inspected integer interval module
supplies elementary arithmetic and the Machin pi enclosure. No elliptic
special-function library, floating quadrature or measured spectrum enters
the certificate.

## Finite reduction and arithmetic proof obligations

Take bins W_i=[i/N,(i+1)/N], h=1 on D and ||h||²=1/24. Source/target
outer cells i+j<N cover D; inner cells i+j<=N-2 lie inside D. For every
I_t(a;W_j), the implementation encloses all a in a target bin and all
theta in each angular cell. Since cos is decreasing on [0,pi], enclosed
endpoint cosines enclose each entire angular cell. Cosine Taylor terms
have ratio x²/[(2k+1)(2k+2)], decreasing to zero. Once <=1/2, twice the
first omitted absolute term bounds the remainder. The code stops with
that bound below 2^-128 and retains all interval rounding widths.

For dyadic interval x=[l,h]/S, sqrt(max(x,0)) is enclosed by
floor(sqrt(max(l,0)*S))/S and ceil(sqrt(max(h,0)*S))/S, computed with
exact integer isqrt and an exact-square test. Squaring intervals crossing
zero uses lower bound zero. The difference of positive square roots is
intersected with its independently proved nonnegative bound
[0,sqrt(v²-u²)]. No singular kernel value is ever evaluated.

Writing theta=pi*tau, uniform angular cells have exact width pi/T.
Consequently multiplying the interval sum of integrand values by
kappa_t/(pi*T) encloses the exact integral formula. Interval evaluation
over the entire target bin already accounts for target variation; no
uncomputed Hölder error is omitted.

The upper bound sums every full outer source rectangle, including all
triangle boundary cells, and maximizes the resulting upper endpoint over
all outer target rectangles. The accepted positive-kernel weighted
2ab/Schur argument gives r<=U. For the lower numerator, both source and
target cells are inner rectangles. Each outer scalar J_t integral is
bounded using the exact target-bin mass (2i+1)/(2N²) times the uniform
I_t enclosure; the source-bin mass was already integrated in I_t. Omitted
boundary terms are nonnegative. Summing these inner products and dividing
by the exact full-D mass 1/24 gives L<=r. These finite sums contain no
floating arithmetic.

## Preregistration, actual runs and provenance

The coordinator published protocol and source before execution at
`c1e6e59dd9155b87d9847155d3455d602a5f84e9`. Frozen protocol:
[ideas/P1-numeric-protocol.md](../ideas/P1-numeric-protocol.md). It permits
N8,theta64 and N16,theta256 only if the first has 0<L<U and costs less
than 60 CPU seconds. The first instance passed this trigger. Both sources
and the reduction remained unchanged during execution.

| Instance | Wall seconds | CPU seconds | Outward r enclosure |
|---|---|---|---|
| N8,theta64 | 0.117878 | 0.117550 | [0.007026920290102146979525,0.521909093569436129911493] |
| N16,theta256 | 1.959178 | 1.958864 | [0.013164946500379018110831,0.477809279990884889210594] |

The two authorized commands actually executed from repository root:

```
python topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 8 --theta 64 --output topics/padua-mz-sharp-constants-20261106/evidence/P1-rectangle-N8.json
python topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 16 --theta 256 --output topics/padua-mz-sharp-constants-20261106/evidence/P1-rectangle-N16.json
```

No heavy process was launched; total developer CPU time was about 2.08
seconds. No failed run, corrective source edit or unregistered grid was
used. Execution stopped after the two authorized instances, even though
the second output's generic trigger field is true; that field does not
authorize any third run.

| Source / input | SHA-256 |
|---|---|
| code/P1_rectangle.py | c65b45fc2d4748e21ae7540bb47824dbc033f0d22917e49ac68084b7c1652963 |
| code/interval_dyadic.py | 8a90618d19ffd8f8efde50bc9002b0b0e26f62d243b4086c674cedcf657945fc |
| ideas/P1-numeric-protocol.md | 568fc2b9f2de6b328d4d2d69980302aba984cac425b43e8c09fd6c31c49d647f |
| theory/P1-rectangle-certificate.md | 4cee5449c0b1634e4d868a41c474b0c938a5394bc87e8f45e197219508a911a9 |

Receipts [P1-rectangle-N8.json](../evidence/P1-rectangle-N8.json) and
[P1-rectangle-N16.json](../evidence/P1-rectangle-N16.json) record exact
endpoint integers, commands, versions and timings. All evidence is small;
no off-repository bulk artifact is required. Trusted dependencies are the
accepted analytic reduction, committed inspected code, unbounded Python
integer/Fraction/isqrt operations, and actual execution on Python3.12.14.

## Independent checks and limitations

The separate P1 mathematical worker confirmed the grid coverage,
inner/outer directions, normalized angular variable and exact h norm
before execution. That correspondence is supplementary analytic review,
not an actual rerun. The distinct review_response agent inspected the
code/scalars and finite reduction and actually reran N16 into its own
output, reproducing the exact interval endpoints bit for bit. Its report
[independent-checks-P1-numeric.md](../independent-checks-P1-numeric.md)
records PASS; committed rerun receipt
[check-P1-independent-N16.json](../evidence/check-P1-independent-N16.json)
has SHA-256
`6557a68428a6a31708485f4506808a0d9dff3eff156673991b30c83c053cc909`.
Shared scalar code is explicitly a trusted dependency; independent
execution does not mean independent implementation. Required Claude
focused audit remains separate.

The coarse constant h trial and small uniform grids leave a wide interval.
This shows the finite reduction can be executed rigorously, but supplies
no three-digit enclosure or useful positive extremal approximation.
Finer meshes, different h and sharper bounds require new prospective
authorization; none was run or silently fitted. The sharp decimal target
remains OPEN and the analytic P1 kernel identification is unaffected.

## History

2026-11-06; bounded two-instance technical campaign after c1e6e59
publication. Rules read 0205690b9c4e959a28e949083e9a1808735abf4b.
Requested Codex gpt-6.1-sol medium, serving-model metadata unexposed.
No Git, accepted S3 theory or shared-registry edits.
