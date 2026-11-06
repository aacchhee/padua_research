# Independent supplementary review — C08 closed far comparison

2026-11-06. Distinct reviewer: Codex `/root/c01_review`, parent-assigned
gpt-6-astra high; actual serving identity and effective effort are not
independently exposed. Rules/input:
`4b728b04216a5490910780bc609a82b853058426`; coordinator-supplied published
head for this assembly: `4ca11b8`. This is supplementary mathematical
review, not the separate formal Claude audit.

## Disposition and exact scope

**ACCEPTED. No unresolved mathematical finding.** For every integer
`n>=1000000` and every signed phase with `1/2<=|alpha|+|beta|<=pi`, the
unchanged C06 model and actual corrected primitive satisfy

    M_far(alpha,beta,log n)+1/2 < Lambda_c(n)-1/10,
    S_n(alpha,beta) < Lambda_c(n)-6/25.

Reviewed frozen source `theory/C08-far-model-comparison.md`, SHA-256
`0b69e38a8d27f36228c41374b51766bd7955d0bc11d9ba6239b0171d422ba8f3`.
It was read in full. This report reconstructs the new assembly and checks
the exact definitions, scopes, accepted source identities, endpoints,
strictness and unbounded degree argument. Separately accepted component
proofs are explicit dependencies, not relabeled as freshly audited here.

This is routine integration with no new mechanism, historical novelty or
priority claim. The workflow's no-novelty exception applies; a complete
IDEAS/registry or author-search audit is excluded. No numerical kernel,
quadrature, phase sample, fitted constant, energy argument or degree job
was used. Only the two assigned new C08 review files were written. Author
sources, previous reports, shared records and Git state were untouched.

## Frozen dependency closure

Executed `sha256sum` verified all the following source/report identities.
The source statements and model definitions were checked against their
accepted reports, including the integral report's focused correction.

| Dependency | Source SHA-256 | Accepted review SHA-256 |
|---|---|---|
| C06 compact error | `64d88fd3bce387630cf55fcc559fb88cc15cf9f27e93487fc662f5050e8d4520` | `fefdde45fd7b4d9de41570809f0ac15540bac10e14f233da715872c211fee3eb` |
| C08 weighted coefficient | `6d905b6c634043992af9f51b6871fe8bcc1ead3b6bc32ca1daa68d844d4e2f1a` | `65abbb37853966c1ad95b8bc76b93fbac06fc5179a305f0ec11fb9e0d878da5e` |
| C08 endpoint constant | `3bd4653b0cf2e1f33e42f8629c06a32b45b546f198e6659cf0203fb48240647c` | `56410cdfde511f65c855bb639e90a65b7329d16441e1c34280d1deea2e9dc05e` |
| C08 finite corner margin | `7cc8a9326d7b4c845a9d2982b95b1088cd28485454d500c0ab477cd5b3dddf81` | `4a8c0429561012b0265a73a822800be3891fd9260e43f498e493c03ebe020235` |
| C08 pole functional | `6cb61ebc3f3808c61bc8d72feb2bee3a57c1dbecf597a7915833b4f43c8cda67` | `d1d9fea50b982112251ec5b5fd7284264d897f56ae87c1d03d9457f760bc0375` |
| C08 corrected integral | `e76a45698ab5c0f2af53816fb74487fb929eff99011e8004e9f79e3f84f8f7a5` | `edb5c9439f89023ff547752bbf91803379aff99cf54ac6a978cd563933f83eb0` |

The earlier component reports' OPEN statements concern the then-unproved
assembly, not an extra hypothesis of the component inequalities. This
review does not promote the unused stronger targets `C_far<=5/2` or
`K_delta<=1/2`.

## Exact model and constant bookkeeping

C06 uses `R=64`, `delta=1/100`, the exact infinite convergent `h_R,g_R`
constants, the original finite endpoint sinc rows, and the full joint
profile `B=V+I/pi`. Its only degree argument is `L=log n`. The same
`b_full`, exceptional x mode `(n,0)` and normalization of `S_n` occur
in the comparison. No near-model truncated constant is substituted.

Expanding the defining `c_mesh` separates precisely

    E_64=C_R+D0(h_R(t_L)+h_R(t_R))
                +B0(g_R(t_L)+g_R(t_R)),
    K_delta=B0*kappa^2+2D0*kappa+(1/pi)integral B,
    C_far=E_64+K_delta,

where `B0=4a/pi^2`, `D0=U0/pi+B0 log pi` and
`kappa=log(delta/pi)`. The cutoff polynomial appears once, in
`K_delta`. No pole-functional cutoff charge is added again to its
accepted final bound. The separate endpoint and integral inequalities
therefore give

    C_far < 49/25+1/3000+49/50 = 8821/3000 < 3.

The endpoint estimate concerns the retained finite `E_64`, via a uniform
tail to its limiting expression; it does not replace the actual model
by an infinite endpoint model. The integral is the finite-cutoff combined
expression with its integrable central logarithm, not a sum of separate
divergent channel integrals.

The accepted coefficient, endpoint and integral results all include the
full closed first-quadrant triangle. Their weighted continuous products
cover `a=0`, vertices and integer pole offsets. C06's finite sinc convention
also supplies the unique `w=0` endpoint and all polynomial collisions.
In particular the corrected integral source uses a non-strict intermediate
product inequality when its sine coefficient vanishes; its final strict
bound comes from independent cutoff slack. That correction is present
in the exact hash used by the assembly.

## Degree-uniform coefficient loss

Write `u=1-a`, where

    a=cos((alpha+beta)/2)cos((alpha-beta)/2) in [0,1].

The accepted full-domain estimate is
`b_full-b_c<=3u/pi^2`, with `b_c=8k/pi^2` and
`k=gamma+log(8/pi)>3/2`. Multiplying by the positive `L` gives

    (4a/pi^2)L^2+b_full L
      -[(4/pi^2)L^2+b_c L] <= -(4L^2-3L)u/pi^2.

The source does not assume the false stronger global inequality
`b_full<=b_c`; the possible positive excess is fully paid here.
The positive log series give

    log 10 > 6(1/3+1/81+1/1215+1/15309)+2/9
           =58726/25515 >23/10.

Thus every `n>=10^6` has `L>69/5`. At that lower value,
`4L^2-3L=18009/25>720`, and its derivative is `8L-3=537/5>0`.
The derivative remains positive for larger L. Since `pi^2<10`, the
coefficient loss is at least `72u`, with the favorable strict inequality
whenever `u>0`. This proves the bound on the entire unbounded degree
range, not just at a checked degree. Equivalently the exact phasewise
model-minus-square derivative is at most `u(3-8L)/pi^2<0` on the far
domain. No monotonicity of the actual finite corner value is assumed.

## Far radius, actual corner normalization and strict margin

For `rho=alpha+beta in[1/2,pi]`, both cosine factors are nonnegative,
so `a<=cos(rho/2)<=cos(1/4)`. The alternating Taylor upper bound on
cosine gives

    u>=1/32-1/6144=191/6144>0.

The separately accepted finite corner result supplies, for each such
integer n, the actual value lower bound

    Lambda_c >= [(2/pi)(L+k)]^2+1/2-1/1000.

This has exactly the linear coefficient `b_c`, and its constant square
is strictly greater than `9/10`, since `k>3/2` and `pi^2<10`.
Combining the three bounds, with the half-unit terms canceled on the
correct sides, gives

    M_far+1/2-Lambda_c
      <3-9/10+1/1000-72*(191/6144)
       =-4393/32000 < -1/10.

This strictness is uniform on the closed far domain, including the
`rho=1/2` interface. It neither uses the origin nor divides by a phase
distance, a weight or `a`. Separate evenness of the primitive and the
absolute-phase model definition transfer the result to signed phases.
No exchange of the n and n+1 meshes occurs.

C06's independently accepted absolute error is strictly below `9/25`
on this same degree and phase domain. Hence

    S_n < M_far+9/25
        < Lambda_c-1/10-1/2+9/25
         =Lambda_c-6/25.

The two subtractions are distinct: the half unit belongs to the new
model comparison, whereas `9/25` is the finite primitive approximation.
There is no additional model error left to pay.

## Executed control and limits

One inline Python standard-library `Fraction` control checked the eight
scalar identities and signs used across this and the companion global
review. It exited zero in approximately `0.000089` process CPU seconds.
Outputs were `8821/3000`, `58726/25515`, `18009/25`, `537/5`,
`191/6144`, `-4393/32000`, `6/25`, and `869/28000`, respectively.
This is exact arithmetic corroboration of the displayed analytic argument;
it supplies no numerical approximation or sampled proof premise.

No BLOCKING, MAJOR or MINOR finding. The theorem supports the far case
of a global assembly; near noncorner and actual corner cases retain
their own hypotheses. The finite exact range 2–40 and unresolved
41–999999 gap are not changed by this review alone. Formal Claude
audit and any executable/backend validation remain separate.
