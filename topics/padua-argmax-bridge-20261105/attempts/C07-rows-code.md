# C07 prospective point-S implementation contract

Input/rules b6e67b3c78cb668b6d2f9da5a5560537d2960bf3; Codex technical developer, serving metadata unexposed. This is integration of accepted mathematics, gate in ideas/C07-rows.md. Frozen C06 sources remain untouched.

Before tests: implement point-only S=(n(n+1))^-1 sum|F|, F=(-1)^j G/2, for exact rational phase fractions alpha/pi,beta/pi>=0 with sum<=1. Initially n<=64 controls, <=90 CPU seconds compile+tests. Four rows 0,2m-1,m-1,m retained via collapsed exact sine-ratio primitive with outward Arb160 arithmetic. Its entire sinc formula carries its complete ball radius; no retained-exact radius drop. Ordinary sign roots get outward balls, contiguous core blocks and <=5 ambiguous direct samples; channel wraps and strict positive pole-distance guards must pass. Use exact rational phases to recognize zero sine, A=0, vertices and collision turn parities. Numeric branch failures report failure. No reference O(n²) fallback.

Return full Arb ball and diagnostic outward binary64 bounds; compare with an independent 512-bit direct finite-board evaluation on a small fixed suite covering parities, axes, edges, vertices, exact collisions and generic phases. Reference source is separate from production row function. Closure/source/header/builder/runtime manifests local and compact receipt under16KiB. Whole-box/gradient/corner-orbit/defect and degree certification remain OPEN.

## Implementation contract and correctness reconstruction

Developer implementation, independent review pending. Public native entry in `code/cheap_rows_C07/point.cpp`:

    int c07_point_arb(long n,const char*alpha_pi,const char*beta_pi,arb_t out)

Both strings are exact rational numbers accepted by FLINT (for example `1/7`); their denominators must be nonzero and they are canonicalized. Guarded domain is LP64, 2<=n<=2147483647, alpha_pi,beta_pi>=0, alpha_pi+beta_pi<=1. Return0 encloses exact S at these phase points; failure returns1 and indeterminate output. Successful calls can be wide; valid points can be rejected by numerical guards. This is not an interval-phase API. The binary64 `c07_point` wrapper reports outward lower/upper endpoints, full radius and six counters, and requires checking its return code. No production caller or certificate producer was added.

Frozen C06 is included unchanged as a transitive source dependency, not loaded as an unpinned binary. Production has O(n) outer rows, four retained rows containing n finite evaluations each, at most five ordinary direct evaluations, and at most12 blocks per cotangent channel. Every polynomial moment and harmonic tail uses C06's fixed-order arithmetic. Big-integer/rational bit lengths and transcendental argument-reduction cost are separate; no constant bit complexity or practical speed improvement is claimed.

For each ordinary row, normalized u/(2pi)=(k+sigma)/n, sigma=(delta+alpha_pi)/2 in[0,1). D roots are exact rational v/(2pi) and 1-v/(2pi), folded when v>pi. For p>0 the two sine roots are enclosed by asin(c/p)/(2pi) and1/2 minus that root, with translates covering the seam. If c/p is strictly outside[-1,1], no sine root occurs. If it crosses an extremal value, outward scalar endpoints are clamped to[-1,1] and asin is evaluated at each exact clamped endpoint, then hulled. This encloses every possible true root, including tangency. A min/max-created ball can extend beyond the domain even when its underlying interval does not; the initial implementation safely rejected these cases, and final source uses endpointwise evaluation.

For a root ball in grid-index coordinates x=n*root-sigma, ceil(lower(x)) through floor(upper(x)) identifies all potentially coinciding grid indices. If this set has two or more members, reject. Its sole member goes into the direct set and gets cuts before/after it; if empty, ceil(lower(x)) is the grid cut between successive samples. Roots outside the finite grid range do not split it. Coincident roots/direct indices are merged by integer sets. The seam sample is included only for sigma=0. Reject >5 direct samples or >12 blocks per channel. Thus no omitted root can lie between grid samples within an unsplit core. Evaluate the actual numerator and denominator at a representative core sample: certified same/opposite signs label the entire core's discrete samples; otherwise reject. This implements a guarded root-to-index construction, not a scan of n samples.

Both channel wraps occur at D roots. Their shift is computed by exact rational floor, with y reduced modulo n; C06 then independently guards every block's strict pole distances. Every block enclosure includes its own analytic smooth/harmonic charges and rounding. Multiplication by the full C,D balls and summation over ALL ordinary rows carries these errors without a four-special-row substitution. Normalization is exactly n(n+1); signed row is n[(cos(alpha)+cos(beta))/2-(sin(beta)/2)cot(v/2)]. No x/y mesh exchange occurs.

At ambiguous samples and the four retained rows, the finite primitive is evaluated by

    G=R_(n+1)((u+v)/2)R_(n+1)((u-v)/2)
      +R_n((u+v)/2)R_n((u-v)/2)-cos(nu),
    F=(-1)^delta G/2.

For exact rational z/pi, choose exact nearest integer turn ell, x=z-ell*pi, and evaluate R_k(z)=(-1)^(ell*(k-1))*k*sinc(kx)/sinc(x). Since |x|<=pi/2, the denominator is bounded away from zero and Arb's entire sinc supplies the exact removable value. This is the collapsed finite polynomial identity; there is no frequency loop per primitive and no truncated C01 approximation. All Arb radii of these exact-function enclosures are carried through abs/max and the final sum. Hence retained-exact means zero row-model truncation, never a dropped arithmetic radius. No separate C01 analytic error is incurred because its approximation code is not used.

Exact alpha=0 uses p=0. Its identically-zero regular numerator row is recognized by v/pi=1+beta_pi (besides v=pi already covered by the retained rows), using c=4*cos(beta/2)*cos(v/2)*cos((v-beta)/2). Exact alpha+beta=pi sets A=0; exact vertex phase pairs return S=1 by the accepted N2/T365 endpoint identity. These are exact rational guards, not epsilon tests. The special zero-numerator row's signed-row ball is retained; no zero times an infinite cotangent is evaluated.

## Executed controls and preserved failures

An initial compile failed because this FLINT release's `fmpq_equal_si` signature is not const-correct; the comparison was replaced with `fmpq_cmp_si`. Its CPU was below0.6 seconds. The initial72-case integration suite ran at n=2,3,4,5,8,16,32,64, nine phase pairs per degree: origin, both axes, beta0 halfphase collisions, two open-edge phases including tangencies, both vertices, and a generic phase. It consumed80.659103 CPU seconds including compilation and the independent reference.

That first candidate (point source SHA36b9b4b603a8e077bab23cf79dba22f8239b1bfdc19c9a125b0db338448833f3) had64 successful calls:48 full reference-ball containments and16 exact-vertex outputs equal1, overlapping the wider512-bit reference balls. Eight sine-tangency cases were safely rejected; no invalid enclosure was observed. The entire failed/incomplete result remains local at `c07-rows/check-r0z5v7r5/controls.json`, SHA31e0c2c66c9b9084e06c259452ecb26a5cf05cdc1cd81e4a58c0c99abf02253e, with all original source snapshots and closure. This is not relabeled a completely passing suite.

After the endpointwise asin fix, final sources were frozen before one focused22-case rerun: all nine phase pairs at n2 and3, and the two previously problematic halfphase pairs at n4 and5. Actual4.299096 CPU seconds including fresh compile and reference. All22 native evaluations succeed. Eighteen nonvertex production balls CONTAIN the independent512-bit reference balls; at four vertices the reference contains the exact production value1. This converse-containment vertex control is reported explicitly, not presented as production containment of a wider ball. Full cumulative development CPU is under86seconds, below90. No further controls are authorized/executed in this round. Changed-source n8..64 cases were not rerun; their earlier generic successes remain historical diagnostics only.

Independent diagnostic reference in reference.cpp enumerates the board and evaluates the original finite cosine polynomial directly, with512-bit Chebyshev cosine recurrences and cumulative one-dimensional Dirichlet sums. It does not call the row/arc/C06 backend or collapsed sine-ratio primitive. Its O(n³) arithmetic is confined to `c07_compare`, never called from `pointS` or the production native entry. Final regular maximum S radius3.345788954929314e-25; final ordinary direct-set maximum1 and combined-channel block maximum4. Initial larger-degree diagnostic maxima were3 direct samples and6 combined blocks. Finite controls support no degree certification or complexity extrapolation.

Frozen identities:

- point.cpp: `8913a96d79f7d687c201f5e38efa5cceec5a18bdc88ed0ada8f578056e7e575e`.
- reference.cpp: `dc9c3e5f208a9919437e572d71e0bc3834f493db7ea8689b777fac6566ba8470`.
- control.py: `17cac7535df1f2b7c7c9436a140e3844ae2638cca191cb1ba18e5faad710c8d4`.

Receipt evidence/c07-rows-point.json pins the final raw local manifest `check-p8uhwohf/controls.json`, SHAb379a18214b48da01c82e090931c14fdbe7cc00370b77bc58745c5cc90d43ea6. It pins preprocessed source, original/transitive C07 and frozen C06 sources and all headers, builder/driver, compiler tools/closures, binary and linked/actually-loaded runtime identities. Loaded identities match before/after. Raw outputs stay local/regenerable, with no remote archival claim.

Disposition: complete developer implementation for successful guarded rational-phase point calls; independent mathematical/source review pending. General point-call success/tightness, arbitrary real phase input packaging, whole-box roots, gradients, corner orbits, defects, practical speed comparison and a production certifier remain OPEN. No shared source, mathematical theorem, C06 file, Git state, cover or certified degree changed.
