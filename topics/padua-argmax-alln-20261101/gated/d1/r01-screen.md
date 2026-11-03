# Direction 1, round 1: numerical screen

Status: pre-registered before execution, 2026-11-02. Numerical observations
will be **MEASURED**, float64; no enclosure or uniform inference.
Assigned developer: Codex, inherited `gpt-6.1-sol xhigh` (runtime does not
independently expose the exact model metadata). Scientific input/rules head
`7d308b10d946b607ae0690454f6c0103690775a4`; administrative head supplied by
the orchestrator `2dde541f1e5af239cae6e93e4438b9be89d15d87`.
No Git operation, shared log/results/handoff edit, or direction 2 work belongs
to this subtask.

## Registered claim, scope and predecessor

This is a numerical test of the already registered variant of IDEA305,
original Claude-02 and fallback-04, not a new mechanism or novelty claim.
The novelty gate is therefore not reopened by this bounded implementation.
With `m=n+1`, use the **full periodic** odd mesh
`0<=j<2n, 0<=r<2m, j+r odd`, `u=j*pi/n+alpha/n`,
`v=r*pi/m+beta/m`, and
`S=(2nm)^(-1) sum |G_n(u,v)|`.
The tested coefficient is `a=(cos(alpha)+cos(beta))/2`.
The hypotheses under screen are a global `S<=a*Lambda_c+O(log(n+1))`,
a vanishing local primitive gain, and a positive compact four-copy defect
`Delta=S-lambda`. All-n PD-T099 remains OPEN.

## Registered finite grids and budget

- Degrees: 16,32,64,128,256, in that order. Initial CPU budget about 180 s;
  stop at a completed degree if that budget is exhausted. No n=1024.
- Global phase grid: `(alpha,beta)=(i*pi/8,j*pi/8)` for integer
  `|i|+|j|<=8` (145 points). Record every sample and extrema of
  `(S-a*Lambda_c)/log(n+1)` and `S-Lambda_c`.
- Near-zero grids: for each `h=1/log(n+1)^2` and `h=1/n`, use
  `(alpha,beta)=(i*h/2,j*h/2)`, integer `|i|+|j|<=2`
  (13 points including zero). Record each amplitude's maximum excess,
  phase, and nonzero samples. No local optimizer is used.
- Compact macro grid: the nine ordered pairs with both coordinates in
  `{pi/4,pi/2,3pi/4}`. Round each pair to its nearest angular odd coset
  `(J*pi/n,K*pi/m)`, minimizing squared angular distance; break ties by
  lexicographic `(J,K)`. Evaluate the zero phase and all 12 nonzero points
  of the `h=1/log(n+1)^2` near grid at each coset. The actual rounded
  angles, phases, lambda, S, Delta and corner gap are retained.
- Moving strips: widths `k/n`, `k in {1,2,4,8}`, on all four sides and
  tangential ordinates `{pi/4,pi/2,3pi/4}` (48 points per degree).
  These widths are exact angular distances from the side, without rounding
  the normal coordinate. For each tangential ordinate round only the
  tangential coordinate to its nearest grid ordinate, choosing the parity
  whose normal phase is nearest the odd coset; record the resulting full
  phase. This is a finite moving-strip diagnostic, with no uniform claim.
- Validation before the screen: run existing `tests_common.validate()`;
  compare the full primitive against `Eval` majorant at generic phases
  `(0,0),(.17,-.11),(-.23,.07),(.09,.19)` around odd coset `(0,1)`
  for n=2,3,4,8,16; compare its zero phase against `Eval.lc` and the
  existing one-phase folded `Primitive`. Require absolute error <1e-9.

## Registered decision criteria

The global candidate fails this finite screening threshold if the largest
positive normalized remainder at n=256 is more than twice that at n=64
and is increasing across n=64,128,256. The local-gain formulation receives
a kill flag if a near-grid positive maximum exceeds 1e-4 at n=256 and
has failed to decrease from n=64 to128 to256. The compact-defect candidate
receives a kill flag if the compact minimum at n=256 is below .01 and
below half its n=64 value. Flags are planning criteria for these specific
finite trials, not asymptotic disproofs. Independently, preserve any clear
contradictory scaling pattern and its precise sampled scope; do not rewrite
criteria after seeing data. No flag is a proof of the candidate. Only a
concrete next analytic obligation can support the orchestrator's next gate.

## Registered command

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d1_screen_r01.py topics/padua-argmax-alln-20261101/outputs/gated/d1_screen_r01.json > topics/padua-argmax-alln-20261101/outputs/gated/d1_screen_r01.out`

Independent replay will be performed by the separately assigned checker.

## Pre-execution diagnostic addition, 2026-11-02

At the orchestrator's request, retain the same grids and add pairwise
triangle-defect lower bounds to each compact and strip sample. With the
four copies ordered `(--),(-+),(+-),(++)`, define
`Qv=sum w*(sum|G|-|G--+G-+|-|G+-+G++|)/4` and
`Qh=sum w*(sum|G|-|G--+G+-|-|G-++G++|)/4`.
Record and check `Delta>=max(Qv,Qh)` up to float64 tolerance, and tabulate
compact minima separately at zero and nonzero near phases. These are
diagnostics of the proposed pairwise lower-bound route, with no claim of
uniform convergence to a limiting defect. No new fit or altered kill
criterion is introduced.

## Completed run and finite observations

Executed the registered command from `/workspace/padua-argmax-alln`, with
Python 3.12 / NumPy and SciPy versions retained in the JSON. No randomness
was used. Every registered degree completed: 17.18886217 process CPU seconds,
17.195102787 wall seconds. The initial source and pre-execution note hashes
are embedded in the output. The preregistration portion above is preserved;
this completion record is an append after execution.

All following claims have status **MEASURED**. Existing matrix validation
passed, and the full periodic mesh, folded zero phase and four-copy checks
had maximum absolute error `5.329070518200751e-15` at n=2,3,4,8,16.
Across the compact/strip production samples, the largest absolute difference
between periodic S and four-copy majorant was `4.263256414560601e-13`.
The pairwise inequalities passed the recorded 1e-10 float tolerance.

| n | max `(S-a*Lc)/log(n+1)` | max local excess, `h=1/n` | compact min Delta, all near phases | compact min Qv | compact min Qh |
|---:|---:|---:|---:|---:|---:|
| 16 | 1.5993457963 | .0000350455061 | 1.8419070561 | .5938115136 | .9503716891 |
| 32 | 1.5429180748 | .0000946211494 | 1.7842389306 | .5742786634 | .9752647518 |
| 64 | 1.5014532911 | .0000598809081 | 1.7392967247 | .5598386346 | .9876092148 |
| 128 | 1.4702777188 | .0000293408081 | 1.7186690469 | .5540278322 | .9937601811 |
| 256 | 1.4462486836 | .0000176177240 | 1.7119286753 | .5511542427 | .9968386231 |

The global normalized-remainder maxima occur at sampled phases
`(alpha,beta)=(+-pi/2,+-pi/2)` with `a=0` (the selected sign depends on
float64 ties). For the requested alternative denominator `log(n)`, the
same raw samples give respectively 1.6343166282,1.5566173726,1.5070506622,
1.4726358879,1.4472654958. These are exact scalar rescalings of the measured
values, not additional runs. The registered near-zero amplitude was
`1/log(n+1)^2`, rather than exactly `1/log(n)^2`; the stored `h` makes that
choice explicit.

The global coarse-grid maximum of S-Lc is zero at zero phase at every
degree. The `1/log(n+1)^2` local-grid maximum, also including zero, is
zero at every degree. The finer `1/n` grid witnesses small **positive**
excesses, so an exact claim `S<=Lc` near the origin would be inconsistent
with these numerical samples. At n=256 its selected phase is
`(alpha,beta)=(-1/256,0)`. These positive values decrease across n=64,128,256;
no rigorous rate or supremum estimate is inferred.

At zero phase, compact minimum Qv values are
.5999199151,.5771000248,.5611606088,.5547398202,.5515715613;
compact minimum Qh values are
.9537814747,.9768336645,.9884065996,.9942012631,.9971001886.
For fixed sampled macro phi, Qv varies over the three sampled macro theta
values by at most `1.23e-15` over the five degrees. For fixed sampled macro
theta, Qh varies over the three sampled macro phi values by at most
`3.11e-15`. At n=256 the zero-phase central values are approximately
Qv=.5515715613, Qh=.9971001886. This separability is the strongest new
numerical discrimination for the pairwise route. It is not a proof of an
identity, of a uniform limit, or of a positive infimum on a continuum.
The full zero-phase defect varies substantially with both coordinates
(at n=256 the rounded central pair has Delta=3.8695512949, while the
compact zero-phase minimum is 1.7143985621).

The moving-strip minimum Delta values at n=16,32,64,128,256 are
.6218790475,.6476391780,.6986809255,.7590211352,.8212807013;
minimum corner gaps are 1.6518813620,2.1222143584,2.7016728196,
3.3778911195,4.1441934512. The selected minimum-Delta samples have width
1/n and central tangential ordinate. The samples include all four sides,
but do not cover arbitrary moving strips or phase-maximizing points.

All registered finite kill flags are **false**: the sampled global
remainder decreases, the finer local positive excess decreases on the
last three degrees, and the compact defect remains above 1.7.
This numerical subtask does not decide an unconditional GO. A concrete
next analytic obligation is to establish the sampled pairwise
cross-coordinate independence (or an adequate uniform replacement) and
then prove its compact positive lower bound. The primitive still needs a
two-phase logarithmic global remainder and a vanishing local-gain estimate
retaining collision values. Merely increasing these grids would not
discharge those obligations. No round 2 or later direction was executed.

## Evidence identity and remaining checks

| File | Bytes | SHA-256 |
|---|---:|---|
| `code/gated/d1_screen_r01.py` | 11002 | `b8003e252d62147b19f1bc02116fe84434672c5cfdb91cd1cc835f9ba5d339e4` |
| `outputs/gated/d1_screen_r01.json` | 860021 | `15c9d29a3d2b166ee54dc8a91fe7bff4c117cc85dc99184fa7bc7640a888e9ef` |
| `outputs/gated/d1_screen_r01.out` | 43818 | `a5487a62de947062cd3e9b94bb2750c30d9d3019e2ffa2eaadb7aae554ce640c` |
| pre-execution `gated/d1/r01-screen.md` | 4932 | `bc2e93a2fd22d1c550aabcc5726741585f5267ed48604ba83231fc4693260da2` |

Dependencies: `code/part3/tests_common.py` SHA-256
`c17e4ed6473b90ed2fa887d0bd2d0b3cf5f6625bbf0d75153a6fa07e26e2a3b7`;
`code/maj.py` SHA-256
`705139a65f225f66ed30f5c7f197cda9f54137c42fb10c8b6f452ab83c78909c`.
The pre-execution note hash deliberately differs from this note after the
completion append. The JSON retains the exact original note identity.
Generated artifacts are local working evidence; the orchestrator decides
which essential evidence to commit within the repository limits and
records any cold-storage disposition. No storage destination is invented.

Independent execution and required Claude audit are **PENDING** for this
new screen. The checker should rerun the script to its own output path and
compare non-time, non-argv fields, allowing the completion-append change in
the note's recorded source hash. Float64 checks and finite samples cannot
certify a supremum, asymptotic law, all-degree theorem or uniform defect.
