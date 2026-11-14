# F02/F03 — Supplemental mathematical-validity review

2026-11-07. Independent reviewer `/root/f01_math_review`; requested/API
assignment `gpt-6-astra`, high; actual serving model/effort metadata unexposed.
Assigned rules/input SHA: `4a5de2012bad94601c713b2ff5517f2e3fb80af2`.
Observed branch HEAD at the start of this review:
`8df42b3c8a3b8a14708efc9a32d23933fb75190d`.
Read-only comparison of AGENTS.md, WORKFLOW.md and CODEX.md to the assigned
rules SHA showed no changes. Root owns Git and adoption.

## Scope and verdict

**ACCEPT at the frozen mathematical scopes below**, with no unresolved
mathematical finding:

- F02 proves the stated logarithmic discrepancy for the original exact
  full-band continuous reference. It therefore disproves a uniform one-sided
  `C/n` loss, and even a bounded loss, for that specific reference.
- F03's routine exact identities and the OPEN/deferred disposition are
  consistent. Neither origin-sign target nor the quarter-ebar fallback,
  an O(n) evaluator, or a new substantive theorem is proved there.

This is expressly a **mathematical-validity/dependency/edge review only**.
It supplies no independent novelty/priority or full-registry gate verdict,
no protocol waiver, no claim concerning F03's local registration chronology,
and no PR readiness or final-ID approval. Root assigned this limited scope;
WORKFLOW's explicit no-novelty audit exception applies. The F03 chronology
disclosure in its idea/attempt remains separate and unwaived. This distinct
supplemental review does not replace the final Claude handoff.

## Frozen inputs and coverage

Root supplied both frozen theory identities and all F03 record identities.
Independent `sha256sum` and `wc -c` matched them. The F02 idea/attempt
identities below were independently observed, returned to root, and then
explicitly confirmed by root. Mathematical acceptance is pinned to the
supplied theory; all six contextual/input files are now freeze-identified.

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F02-phase-floor-mesh-obstruction.md | 12697 | `dc25b2e333509b1c47441f7da7905ca35b1f241da824adf3b5d989c919f59834` |
| ideas/F02-phase-floor.md | 8301 | `f3f4ebaa7d418f0a0b84ad56559abebc02006eed272dfed59951c227abde35ee` |
| attempts/F02-phase-floor.md | 3741 | `55bebab44f74e00c842dfa9086c5170dcb93a3f7fb0de5d8665c184de23a377c` |
| theory/F03-origin-sign.md | 9268 | `76b6562d12dae58ce46cd8654963eda3adb35603146c56b3f3e1b14bbd33ddaf` |
| ideas/F03-origin-sign.md | 5167 | `5cc02e11a0e66b1cb248257369f58d62eb5db7245a725473567c96335b0b791a` |
| attempts/F03-origin-sign.md | 6592 | `a648bcfa192625415996d9a70dc3eb371c3d55b127709ee6c0913b26f6faeff9` |

All six files were read in full. Full predecessor theory reads in this
review: N5-two-phase-defect; PD-T159; PD-T211; PD-T226; PD-T266/267;
PD-T269/270/271; and PD-T364 phase-structure. C01-allclass's definitions,
folded normalization and relevant proof text were read, with its initially
truncated concluding portion recovered by a bounded read. The complete
E08-origin-lower theorem and its exact ebar domain were read earlier in the
same independent review session and retained as the named fallback
dependency. Accepted predecessors are dependencies, not newly reapproved
historical claims; their computational/source histories are not independently
rerun or recertified here.

## F02 independent reconstruction

### Exact finite object and exceptional values

For `J=1,K=2,alpha=beta=0`, the physical center is admissible at every
integer `n>=128`; `J+K` is odd for both degree parities. C01's folded
projection has coefficient `1/(nm)` and condition `r+k` odd. Passing from
the full periodic G expression to signed halves and folding the second
mesh gives exactly that coefficient. No additional factor of two is
introduced for the two first-coordinate cosine branches.

At a regular point put `x=cos(r*pi/n)` and `y=cos((k+/-2)*pi/m)`.
The two Chebyshev sums are `(-1)^r(1+x)` and `(-1)^k(1+y)`.
Since their parities are opposite, subtracting the exceptional
`cos(nu)=(-1)^r` gives the exact signed half `(1+y)/(x-y)`.
This verifies the numerator used throughout the witness.

For `2<=k<=n-2`, the straddling condition is exactly
`-2 < j+(k+j)/n < 2`, where `r=k+j` and j is odd. Precisely `j=-1,+1`
occur in the half circle; both are strict interior representatives.
Their two distinct reflections provide four periodic terms per bulk row.
The separately listed rows `k=1,n-1,n` exhaust the remaining physical
interior rows. At `k=n-1`, the regular partner has zero numerator and
zero defect, and its reflection is also zero.

Coprimality of n and m reduces quotient collisions to angular endpoints.
The zero-angle possibility violates odd-board parity. The admitted one is
`r=n,k=m-2,v_+=pi`. From the polynomial divided difference,
`G(pi,pi)=2n(-1)^n`, so its signed half is n. Its other half is -1;
the defect is exactly 2. Reflection fixes `r=n`, so it is counted once.
At `k=0,m` both halves coincide and have zero defect, preserving the literal
endpoint half weights. These facts establish the complete decomposition (7).

The remainder estimate uses the smaller regular half, so no uncontrolled
near-pole value is needed. At `k=1`, the chord denominator lower bound
`6/n^2` gives the stated normalized O(1) contribution. At `k=n`, the
cosine span is `2 sin(2pi/m) sin(pi/m)>=16/m^2`, and its largest numerator
is at most `9pi^2/(2m^2)`. Thus each defect is at most `9pi^2/8`.
Together with the single collision, the displayed bound on R_n follows.

### Uniform logarithmic coefficient and the other rows

The two exact angle differences in (9) have the correct adjacent-mesh
displacement. Factoring each cosine difference into its two sine factors
gives limits `pi^2(2-j)` and `pi^2(2+j)` after multiplication by N/k.
The numerators tend to 2. Hence for either j,

    k*d_(k,j)/N -> 4/(3*pi^2).

The proof supplies the summation uniformity it needs: choose fixed K0
large and delta small, then n large; throughout `K0<=k<=delta*n`,
the sinc factors, finite k-ratios and k/n displacement are simultaneously
controlled. The limiting denominator factors stay strictly positive.
Continuity of the minimum therefore transfers that uniform control to
the displayed defect coefficient. This is stronger than a fixed-k or
pointwise expansion and justifies the harmonic sandwich.

For fixed K0 the low rows contribute a bounded amount after normalization.
For fixed delta, the high rows contribute O_delta(1): their two denominator
magnitudes sum to the cosine span, giving (12). Near the upper endpoint,
the numerator vanishes quadratically in `t=pi-b`, while `sin b` vanishes
linearly; their ratio is bounded. Thus there is no uncharged second
harmonic tail. Nonnegativity gives the lower sandwich, and the bounded
outside contributions give the upper sandwich. The harmonic middle sum
divided by log n tends to one. Counting all four representatives proves
the coefficient `16/(3pi^2)` for the full integer sequence.

The continuous reference agrees literally with PD-T211's `2/pi^2`
integral and PD-T267's endpoint expansion. Applying that already-defined
integral identity at `gamma=2pi/m` gives coefficient `8log(2)/pi^2`.
No finite-n Riemann convergence is interchanged with the shrinking angle.
The positive atanh series proves `log 2>2/3`, so the difference coefficient
is strictly positive. It forces the integral minus Q_n to exceed every
bounded allowance and therefore every fixed `C/n` allowance eventually.

The negative scope is correct. A uniform all-center claim is disproved
by this admissible zero-phase sequence alone; no horizontal witness is
needed for that conclusion. Conversely, this Q_n itself grows positively,
so the witness does not refute a fifth-floor bound, a capped reference,
an endpoint-specific discrete certificate, or a global argmax statement.

## F03 independent reconstruction

PD-T159 and PD-T269 identify
`C_n=Lambda_c-L_n^2-kappa`, including the exceptional `1/m` and the
normalization term `-(L_n^2-1)/m`. PD-T270's bound on `L_n-A_n` gives
`|q_n|<=A_n/(2n^2)+1/(16n^4)` by direct squaring. Thus
`E_n(0)=C_n+q_n`; neither the limiting kappa nor a positive Delta_n alone
establishes a finite sign.

On each folded origin row `1<=r<=n`, coprimality excludes collisions.
The inequality `r-1<nr/m<r` and the specified parity give exactly r
positive representatives `-r+1,-r+3,...,r-1`. The signed row is n by
PD-T226, so its absolute row is `2P_r-n`. The endpoint rows are
`R_0=n^2` and `R_m=n`; after division by nm their contributions are
`n/m` and `1/m`. Folding the other two copies yields (3) with those
two contributions distinct. Both degree parities use the same argument.

The cotangent addition identity on the symmetric positive set gives
`P_r=w_r*T_(n,r)` with precisely `a_r=(1-r/m)/2`. Every argument is
regular. The n-term cotangent identity gives n only after replacing the
partial sum by the complete signed row. For `r<n` there are actual
negative samples, so `P_r-n=Z_r>0`; at `r=n`, Z_n=0. Substitution gives
exactly (6). PD-T269/270 imply that the deleted mass has leading order
`(4/pi^2)log^2 n`, so this substitution cannot serve as a vanishing
remainder. The record correctly attributes this to the existing partial-
row issue and creates no new impossibility theorem.

For the two-pole subtraction, B has endpoint values `1/pi` and `-1/pi`.
Reversing the order in the second reciprocal sum gives the positive
argument `n-r+1-a_r`, verifying both signs and shifts in (7).
The remaining V_n is genuinely still the displayed nested sum. The
coarse boundedness estimate costs `8M/pi`, as follows from
`w_r<=2m/(pi*r)` and exactly r residual terms in row r. This is only an
upper estimate and is not misreported as the actual error's asymptotic
size. No identity collapses that residual, and no signed uniform remainder
is supplied; the OPEN target and DEFERRED route status therefore remain
appropriate. The sufficient inequalities involving b_n and ebar/4 have
the correct direction, and the accepted E08 fallback keeps its n>=160
domain.

## Activity, findings and limits

No BLOCKING, MAJOR, MINOR or NOTE mathematical finding was identified.
Only this new owned review file was written; developer and shared files
were not edited. Commands actually used were read-only `git rev-parse`,
`git diff`, `rg`, `cat`, bounded `sed`, `wc -c`, and `sha256sum`, plus
owned prose editing. No scientific scripts/imports, numerical calculations,
scalar/phase/degree endpoints, quadrature, native/compiler jobs or Git
mutations occurred. File hashes and text metadata are not scientific runs.
PD-T271's existing outward enclosure was read as a predecessor record,
not executed or used to infer a finite origin sign.

The verdict does not prove the fifth floor, either F03 lower target,
an O(n) origin evaluator, a new analytic onset, any finite-degree coverage,
full I06/D13, historical novelty, or protocol/readiness closure. Later
replacement mechanisms need their own prospective scope and independent
review. Root may adopt the F02 scoped negative and the accurately OPEN F03
record at these exact hashes; final Claude audit remains separate.
