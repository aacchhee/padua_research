# N5-03 — All noncorner vertical-edge centers through phase radius 1/2

Aliases: adaptive edge rectangle; middle-line endpoint repair;
all-center actual-lambda/model margin.
2026-11-05. Developer Codex, assigned gpt-6.1-sol xhigh.
Input/rules head `c000899f3fb10d6ba0f1725341a045fe11ec943a`.
Provisional theory ID `PD-T?argmax-bridge-codex-N5-03`.
Initial status OPEN. Current theory status PROVED developer claim,
distinct review pending; disposition retained quantitative variant.

## Question and exact scope

For n>=64, m=n+1, epsilon in {-1,1}, complementary interior index
1<=q<=m-1 with epsilon^n*(-1)^q=-1, and |s|<=1/2, put
phi=(q*pi+s)/m. Prove actual lambda_n(epsilon,cos phi)<=S_n(0,s)-d
for one explicit universal d>=1/8192, then subtract the N1/N5 model
error to obtain a positive actual-lambda/cotangent-model margin.

## Mechanism, closest entries and exact distinction

Full reads: T185–192, T222/T224/T366, and N5-02. The exact two-copy
identity and finite positive numerator method are inherited. T222's
adaptive far blocks stop at phase radius 1/8; T224/T366's endpoint-line
construction stops at smaller radii. N5-02 has a central physical strip.
The new target covers **every interior complementary center**, both
vertical endpoints and phase signs at radius 1/2 with effective n=64.
It is a **quantitative variant with difference**, not a new cancellation
mechanism or a historical novelty claim.

## Cheapest decisive gate / kill before development

Near endpoint-distance indices 1..4, test the inherited parity-correct
single-line construction using a tighter middle range
3n/8<=l<=n/2, to improve the 1-minus-cos baseline while leaving phase
budget 1/2 in the band inequality. Far centers use adaptive rectangles
whose folded targets have 1-plus-cos baseline >=1/2. Prove exact counts,
normalization and positivity for both endpoint orientations before any
finite diagnostics. Kill this proposed uniform constant/domain if a
single admissible n, sign or parity breaks a needed inequality or the
final error subtraction is nonpositive. This is a decisive analytic test
of the selected geometry; it is not an E-C counterexample search.

The parent supplied this prospective repair; constants and assumptions
in that hint were explicitly unproved. The candidate is registered now,
before development beyond predecessor reading and an informal far-band
budget check. A useful quantified result or precise obstruction is due
at the first 20–30 minute checkpoint. No arbitrary variant quota.

## Literature and obstructions

No classical source proof is imported. N5's source records/access limits
are unchanged. N080 refutes only equal-phase E-P, not this defect target
or independently optimized E-C. Whole-cell phases extend beyond the
present radius and remain outside this claim. Nonnode corner centers
q=0,m are excluded; their zero-phase defect is zero, so a positive
uniform bound including them would be false.

## Considered alternatives and dispositions

| Candidate | Disposition / condition |
|---|---|
| Tightened endpoint middle lines plus far adaptive blocks | retained for development; exact target above |
| N5-02 fixed central rectangle extrapolated to all phases | equivalent failed proof construction already scoped in N5-02; no new claim of E-C failure |
| Moving rectangle over a full phase cell | deferred: first settle or obstruct the bounded radius-1/2 all-center target; no full-cell numerical scan |
| More finite ordering screens | abandoned as a proof route for this round; do not provide the required quantified control |

## Verification plan and open remainder

After the analytic gate, small representative exact/rational or
high-precision diagnostics may check line parities and normalization.
Independent mathematical review belongs to the parent. Corner dominance
still requires a rigorous primitive-model upper bound; this supporting
target does not settle E-C or PD-T099. Parent publication is required
before any round 4.

## Gate outcome and actual verification

The selected geometry survived the analytic gate with a stronger common
constant d=1/1024. Endpoint lines give Delta>1/864, far-small blocks give
Delta>=7/(768*pi), and far-middle blocks give Delta>=7/6144. Each is
strictly greater than 1/1024. Exact finite physical normalization and
parities are proved in `../theory/N5-all-edge-defect.md`; the N1/N5 error
is <1/524288 at n>=64, leaving actual lambda<M_n(0,s)-511/524288.

After the written proof, 56 selected-block diagnostics at n=64/65,
both endpoints and s=±1/2 passed: 32 endpoint lines, 16 far-small,
8 far-middle. The smallest selected-defect/case-floor ratio was
11.8382054813763, and finite polynomial/quotient values agreed within
2.003860985e-77 at 80 digits. Exact rational budget assertions also
passed. These are developer checks of the proof construction, not an
all-degree computer certificate or finite ordering screen. The receipt
is `../evidence/n5-all-edge-defect.json`. No failed round-3 test or
unrecorded alternate candidate occurred. Stop for parent publication and
distinct review; no round 4 is begun.
