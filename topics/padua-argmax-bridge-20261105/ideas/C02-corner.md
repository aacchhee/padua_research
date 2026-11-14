# IDEA?argmax-bridge-C02-corner — Half-diamond actual-corner reflection bound

Aliases: C02 actual corner; radius-half PD-T228 extension; average before
absolute values; explicit corner orbit remainder.

## Gate and assigned quantitative continuation — 2026-11-06

- Question / scope: extend the actual-corner comparison of PD-T228 from
  `rho<=1/64` to the complete inward half diamond `rho<=1/2`, with an
  explicit numerical remainder and an explicit degree floor. The parent
  assigned this variant after accepting the separate C01 global result.
- Mechanism / hypotheses: retain the corrected polynomial kernel and
  four reflected copies inside each cardinal absolute value. Keep the
  same removed collision family `B={r=j+1,j>=2n/3}`. Prove its regular
  complement stays separated on the larger phase domain; then apply
  symmetric Taylor to `F-a F0`. No new mechanism is proposed.
- Whole-registry baseline: the complete current 1075-line
  `state/IDEAS.md` headings, IDs, aliases, summaries and obstruction /
  disposition tables were read in the preceding C01 work. The current
  file SHA256 is
  `1aecb5461537870de64711fc8f48daa683dea57c6298cbf07bda51d4c52d2718`;
  the fresh tail read includes IDEA570--584 and their retained subroutes.
  This reuses that whole-registry coverage rather than claiming another
  independent full scan. Fresh searches across registry, Padua ideas,
  theories, logs and literature INDEX used `reflection-first`,
  `average before absolute`, `corner orbit`, `half diamond`, `rho 1/2`,
  `237000`, `weighted energy`, `PD-N085` and `PD-N086`, including aliases.
- Full relevant shortlist: IDEA330/331 in FINAL_CANDIDATES and their
  original gated/CANDIDATES entries; original fallback04 / IDEA305 /326;
  IDEA457/460/461 in H2-H3; current N3-bootstrap and N3-uniform-energy-r8;
  C01-effective, C01-near and C01-allclass candidate records. Linked
  load-bearing proofs PD-T228 and PD-T221 were reread in full, including
  all derivative and B-family bounds. PD-N085 and PD-N086 were reread
  in full. N3-bootstrap-corner and N3-uniform-energy-r8 were read in full
  to distinguish their energy/unknown-global-norm assumptions.
- Closest-entry separation: PD-T228 proves the same actual-function
  form only for `rho<=1/64`, with coefficient237000 and sufficient
  `log n>=10^7`. This candidate changes only explicit domain/constants:
  `n>=64,rho<=1/2`. An uncovered regular denominator or endpoint
  overshoot kills the proposed extension until repaired. If the old
  proof already supplied these full quantifiers, the result consolidates
  as an explicit verified scope extension rather than a new idea.
- Literature baseline / limitations: repository proof comparison only;
  INDEX Padua context/addenda inspected. No external theorem, fulltext
  transfer, historical novelty or priority claim. C01's new central
  cancellation estimate is not needed for this corner proof.
- Applicable obstructions: PD-N079 forbids a purely quadratic primitive
  comparison, but this is the actual reflected cardinal sum; primitive
  absolute values are not moved inside the orbit. PD-N085's affine
  per-cardinal sign test and PD-N086's coarse fixed signs are not used.
  All initial zeros and collisions must stay in the finite polynomial
  identity. No `M=Lambda_c`, `3/4` energy premise, all-n energy
  extrapolation or global argmax assumption is allowed.
- Verdict: quantitative domain/constant variant of IDEA331 / PD-T228,
  not a new reflection, Taylor or energy mechanism.
- Cheapest decisive test: prove regular `b,t` separation and the
  numerator sine bound for every signed phase of L1 size at most1/2,
  before any numerical work. The delicate surviving `r=j+1` strip and
  coordinate overshoots are tested separately, rather than invoking the
  old small-radius geometry outside its stated domain.
- Kill criterion: an unbounded denominator, a missing endpoint weight,
  a surviving first-order orbit term or an uncontrolled B-family
  collision stops the proposed theorem. A failure would concern this
  bounded extension, not the whole corner route or the argmax theorem.
- Test discriminability: exact separation and explicit derivative sums
  decide this all-degree phase-domain claim. A degree/phase sample
  cannot supply the quantifiers. Analytic work only is launched.
- Timing: the parent specified the precise domain, inherited mechanism
  and cheap geometry test before development. The initial algebraic
  sketch followed the prior C01 registry/shortlist coverage; the fresh
  larger-radius searches and source rereads above preceded this durable
  contract. No new mechanism or prospective numerical preregistration
  is claimed retrospectively.

## Exact proof target before durable proof writing

For every integer `n>=64`, put `m=n+1`, `rho=alpha+beta` and
`a=(cos alpha+cos beta)/2`. At either parity-correct nonnode corner,
inward `alpha,beta>=0,rho<=1/2`, aim to prove

    lambda_n(z_n(alpha,beta)) <= a Lambda_c + 24000 rho^2 log m.

The scalar consequence is strict actual-corner comparison whenever
`Lambda_c>240000 log m`; a deliberately coarse sufficient condition
is `log n>=610000`. This is a corner-patch threshold, not a global
argmax onset or model-approximation onset.

Optional computational controls are not launched. No executable, degree
extension, fit or CPU-heavy verification is needed. If a diagnostic is
later useful, its exact controls and <=60 CPU-second cap must be written
before execution. Separate independent reconstruction is the parent's
responsibility before using the enlarged patch as an accepted premise.

## Other considered routes

| Route | Precise disposition |
|---|---|
| Reuse old geometry without checking overshoots | Abandoned inference; its old stated radius is too small. Prove the larger-radius inequalities explicitly. |
| Weaken separation to `t>=L/(8m)` and enlarge the derivative coefficient | Retained fallback only; the sharper delicate-strip estimate appears to preserve `L/(4m)`, so the weaker version is unnecessary. |
| Use the N3 three-quarter energy bootstrap | Not used: intermediate all-degree energy is unresolved, while reflection gives a direct pointwise statement. No energy theorem is rejected. |
| Use the sharp C01 central primitive cancellation model | Deferred to N1's assigned model continuation. Actual corner reflection does not need its fractional residual. |
| Extend the theorem to all n>=2 at rho<=1/2 | Deferred; the present quantitative geometry explicitly uses `m/n<=65/64`. No small-degree failure is asserted. |

## Frozen developer outcome

The full analytic proof in `../theory/C02-corner-halfdiamond.md` proves
the exact n>=64, full-half-diamond bound with coefficient24000 and
the stated strict-patch corollary. The regular signed second-derivative
budget is9464rho²H, safely rounded to9500rho²H; two symmetric pairs
plus B give19000rho²H+10rho². Since log m>4 this is below
24000rho²log m. Disposition: retained quantitative variant.

One standard-library exact Fraction check verified the displayed
scalar arithmetic. No kernel, phase, degree or energy diagnostic was
launched. Separate independent reconstruction and the campaign's
formal audit remain pending; no global-onset or finite-bridge claim
follows from this theorem alone.

History: 2026-11-06, Codex auxiliary mathematical developer, inherited
parent allocation; serving model/effort independently unexposed. Rules /
scientific input `4b728b04216a5490910780bc609a82b853058426`. Only the
three assigned new C02-corner records are writable. No Git/shared-file,
old-proof or C01-source edit and no subagent delegation.
