# Supplementary independent review of the onset-512 response

Rules/input: `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`, read 2026-11-08.
Role: distinct supplementary Codex reviewer; requested Astra xhigh because the
scope includes adversarial arithmetic and a new independent checker. Actual
serving model/effort metadata are not exposed. Root alone owns Git. This is
not the required substantive Claude audit and does not make PR 27 ready.

## Scope and prospective checks

Review only: the local frozen-engine 320..510 campaign and compact return;
J01/J02 analytic gates and elementary constants; I25's independent phase
checker and its prospective pilot/full-run protocols; the F03 support split
and both H04 derivative majorants. Historical audits and findings remain
unchanged. No native certificate computation is authorized by this report.

Read AGENTS, WORKFLOW, CODEX, handoff 29 including AC's dated decisions,
audit-03, the streamline architecture, I25 and its closest verification
predecessor IDEA-344, the complete IDEA registry (including its obstruction
and disposition tables), and the relevant paper formulas. This implements
approved I25 and architecture B; no new mechanism or novelty claim is made.

Before execution, the following cheap independent checks are registered here:

1. Run the registered Fraction-only J01/J02 checker once at source SHA-256
   `ff2859eeb9ccab91e8cfa996318e4f1129502dc90f5c2fa90754350453a51751`,
   saving independent stdout/stderr/exit and source identity under
   `/tmp/onset512-independent-review/`. Reconstruct its all-real-n steps,
   elementary constant brackets and exact rational consequences separately.
2. Run only synthetic scalar, interval and cover checks of I25: compare its
   sine intervals at fixed rational angles with independently constructed
   rational Machin/Taylor enclosures; test exact interval operations,
   removable ratios, and degenerate/closed polygon examples. No complete
   degree certificate is included in this independent smoke scope. Preserve
   all failures; do not alter developer sources.
3. Re-run process controls using the registered local runner's `controls`
   action in an exclusive scratch directory; this invokes no native engine.
   After the compact ZIP is complete, independently check its content hashes,
   exact population, primary/fresh equality, exits and accounting, then run
   the frozen data-only verifier. Any extra controls modify scratch copies.

Computations and proof adoption remain provisional until the corresponding
review below is complete. Source inspection, developer-reported execution,
and this reviewer's actual execution are distinguished throughout.

## Initial observations (before independent executions)

- The campaign runner's 260-second `RLIMIT_CPU` bounds wrapper self CPU,
  not the aggregate CPU of descendants. The unchanged engine separately
  enforces each pass's 120-second aggregate budget. The developer clarified
  this wording; no native computation needs repeating for that clarification.
- The preregistration records the validator identity but the runner does not
  enforce it at stage entry, and does not prospectively pin every imported
  operational helper. Root confirms the helpers were not edited during this
  epoch. The developer's during-run helper snapshot is explicitly supplemental
  evidence, not a retrospective preregistration.
- I25 reconstructs its own upper and lower bounds and recertifies the entire
  stored tree. The weaker comparisons `lo <= native_upper` are diagnostic
  consistency checks only; they do not validate the original native endpoints.
- Both H04 derivative majorants are valid. The former coefficient ordering
  is stronger. Replacing it by the requested ordering is not a repair of an
  invalid mathematical inequality.

## Results

### Analytic gates and elementary constants — accepted at the written scope

Reviewed frozen J01 SHA-256
`a74be3cfb90b03f24325c09c737166e17fced17d4ec7c5fd9a2f185d5923ce56`,
J02 `d4fc185afc308fc7363e3c82919f85a94e10215c997578ce807b31dae774c0ac`,
and checker `ff2859eeb9ccab91e8cfa996318e4f1129502dc90f5c2fa90754350453a51751`.
The exact command was `python3 topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py`
(the subprocess used that path resolved under the repository root). It ran
once independently, observed exit 0, Python 3.12.14, about 0.23 seconds wall.
Own output is `/tmp/onset512-independent-review/analytic.stdout`, SHA-256
`8ec242fede846448e4063f1d2d545b4d5192e55f7e917113542141f2f6424c55`;
stderr is empty; `analytic-observation.json` records command and identity.

| Exact outward receipt | Lower | Upper |
|---|---:|---:|
| maximum P512 | 0.040785 | 0.040786 |
| P512(1/2) | -0.143070 | -0.143069 |
| vertex radius | 0.147341 | 0.147342 |
| G(512,1) | 0.534264 | 0.534265 |
| lower surrogate for G(192,pi/2) | 0.098316 | 0.098317 |
| middle-class floor at 295 | 0.050064 | 0.050065 |
| kappa, K=3 | 0.917166 | 0.921489 |
| Cstar | 1.841232 | 1.847940 |

The proof review is separate from these finite evaluations. The decreasing
allowances and increasing T+A4 imply increasing U,d1,d2. Formula (4)
proves the unrestricted maximum and vertex decrease. For P(1/2), the
optimizer remains in the fixed nonnegative segment; pointwise decrease
there, with the uniform positive drop in C4, proves strict decrease of
the maximum. This covers every real n>=512, not a sampled integer grid.
The absolute-gate amplitude decreases in radius under the stated tangent
condition; its coefficient ratio decreases with n. Each term in G has the
claimed sign of n-variation. The floor has positive inverse-power losses
and therefore increases; its remaining two center classes are the unchanged
finite proofs. The closed half-radius, radius-one and far boundaries overlap.
Corner-256 retains the pi/4 square and 1/30 loss; far-192 retains its pi/2
guard and 3/100 gap. Finite coverage through 511 remains a separate obligation.

I reconstructed the endpoint cancellation, positive ap formula and geometric
ck tail, including radius 1/480 at K=3. Machin's identity, consecutive
arctangent sums, the positive atanh logarithm series, harmonic gamma bounds,
and convex trapezoid/midpoint zeta tails supply every scalar bracket. Even
zeta special values, Arb constants and numerical quadrature are absent.
Independent rational cross-multiplications give H0's extra margin
37/19700 above 7/25, g0's margin 7/24625 below 43/125, and the final
squared C_infinity gap 71/6250000. Thus j>23/250 and C_infinity<9/4
follow without an upper kappa<23/25 premise. No unresolved finding remains
in J01/J02; root may adopt PROVED at these stated scopes. This acceptance
does not adopt the new finite computation or remove the next Claude audit.

### F03 source split and H04 majorants — accepted focused response

The new supporting F03 file has SHA-256
`fbdeed2ef9ca419c84b3ba4ee99cd9832369998829b81356864edd227baf7efa`.
A read-only comparison against `git show b45e29fa1fe3dbfa2517ff8043e5d9c440870530:topics/padua-argmax-bridge-20261105/theory/F03-origin-sign.md`
confirms sections 1--3 are verbatim. H01/H04/H05/H06/H-sharp now identify
that PROVED support and its PD-T159/PD-T226 normalization. H05 distinguishes
its abstract series estimate from the corner identification. The original
sign/useful-lower target and proposed one-index evaluator remain OPEN;
neither becomes an H premise. This is an appropriate substantive split.

For H04 (reviewed SHA-256
`cd8a9462b0a3afe3a38dc324e82756ff5a5e39bd869c45e24cc7690c704e4b05`),
direct differentiation of f_k=t^2/(4k^2-t^2) gives

    f_k''=8k^2/(4k^2-t^2)^2+32k^2*t^2/(4k^2-t^2)^3.

Bounding those summands separately gives the historical coefficient ordering.
Bounding its combined numerator gives the requested new ordering. The new
summand exceeds the old one by `(4/27)(k^-2-k^-4)>=0` inside the common
8/pi factor. With the stated crude series bounds the old majorant is
<1088/243<5 and the new one is <128/27<5. Both are mathematically valid;
the historical inequality must not be labeled false. The new addendum
preserves that distinction and all downstream constants. Own exact results
are in `/tmp/onset512-independent-review/exact-support-checks.json`.

One preliminary text-comparison command failed because I assumed a different
heading depth and H06 filename; it made no scientific calculation or source
change. After inspecting the actual headings/path, the corrected comparison
above passed. No developer failure is inferred from that reviewer mistake.

### Campaign and I25 — review still in progress

The I25 **pilot gate is accepted**, before any consequential pilot launch, for
core `add4f1cb1246e71fd38f67b802a4e61dfb8ebe9244dda49326290b779030d485`,
controls `628096010388fb3a1860726092e91156e98e17f1c35055bbe31990d7a14af5ac`,
runner `0ad0021a40253a78935663af7aff6f548b986919acc0f50e45767097d800c019`,
J03 `008b7fe2fd4674d6b6471671b487e8fb14411de156861c83e4bfa2d15a85b20e`,
and preregistration
`e1fa7ab9788b0ebde8847ec12755444b8452d5f064a0e5bf6c2faf9ae7844398`
plus prospective amendment 01
`6cefeb23852752cb6ee74735f8a9056bc275448850afcd009c21aaf43a7aba03`.
The amendment supplies the originally missing outer wall timeout and runtime
identity; it changes no checker source or scientific population. The total
pilot cap is 3600 CPU seconds, with 3500 for its process and 100 for smoke
work. Both passes at exactly 41,199,238,511 and all 27 corruptions are required.

I independently reconstructed the finite diamond-to-product kernel identity,
both coordinate endpoint weights, four-reflection addition before absolute
value, exact collision parity, and Python-int guards before int64 operations.
For Taylor sine, each monomial has at most 38 rounding/conversion factors;
the coefficient majorant gives <77u*t, the remainder <u*t and argument
reduction <6u*t. The implemented 128u*t therefore encloses the exact result
under J03's explicit binary64 round-to-nearest/gradual-underflow model.
Nextafter-widened general operations and explicit pairwise sums preserve
inclusion. This is conditional on the stated computational semantics, not
an assertion that hardware arithmetic is exact.

The parser retains both closed children, exact tangencies and every
required folded key. Independent GRID/TREE norms bound every signed family.
The rational polygon routine includes all vertices, every true edge's
stationary maximum and nonsingular interior stationary points; a singular
interior maximum has a flat direction reaching the boundary. Near/far proxies
overlap at the physical seam. The actual three corner points and analytic
256/192 guards are reconstructed exactly. Stored endpoint comparisons are
only consistency diagnostics; each tree is recertified using the new bounds.
Native endpoint containment is expressly not claimed.

Own command `python3 -B /tmp/onset512-independent-review/scalar_controls.py`
passed **98** synthetic controls in about 5 CPU seconds. Outputs and both test
versions remain in that directory. Coverage includes independent exact
Machin/Taylor sine enclosures at 54 rational arguments (negative turns,
half-pi, tiny angles and denominators near 2^51), removable ratios, signed
pairwise sums, basic interval operations including subnormals, a singular
Hessian, a point intersection, malformed prefix covers and four closed
quarters. No complete certificate or native engine was run. The first test
version incorrectly demanded enclosure of its own overwide Taylor upper
above 1 at pi/2; intersecting that reference with the known [0,1] range fixed
the test. The initial failure and script are retained; checker bytes never
changed. This was a reviewer-test defect, not a hidden certificate retry.

The full run still needs a separate preregistration and exact 942-input
inventory; the pilot runner's initial additional-directory interface alone
does not enforce that scope. Pilot outcome and full-run acceptance remain
pending. Legacy PD-T271 strings inside frozen certificate metadata are schema
identities; J02 can replace their analytic numerical premise without editing
the historical certificate bytes. This distinction must remain explicit.

The campaign's cheap process controls were independently executed with
`runner.py controls /tmp/onset512-independent-review/process-controls`:
observed exit 7 stayed 7, an already reaped child was refused, inherited
ignored SIGCHLD was refused, and cleanup left no descendants. The control
record hash is `ccb80d7fb80f679801bb8ba864ce768ea519bc41c822073393d031856cc4efde`.
The real campaign and compact ZIP remain pending at this boundary.
