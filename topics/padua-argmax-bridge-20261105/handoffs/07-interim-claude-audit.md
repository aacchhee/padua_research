# Handoff 07 — Padua argmax bridge — interim Claude audit and own ideas

- Status: open
- Previous handoff: 06-campaign.md
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: independent auditor and independent idea proposer; **Codex implements next**
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `99c6b6f5ef75cbbd17e0127a0210c86eb2eb78d0`
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: WORK
- Written by / date: Codex, requested gpt-6-astra high; serving metadata unexposed · 2026-11-06

## AC's instruction — mandatory interpretation

AC requests: “Write things down, then I sent this to Claude for audit and
independent suggestions on how to close the remaining gap, then back to work.”
AC clarifies: “this will be interim audit and it has to come with own ideas
on how to close the gap and set branch to work”, and “codex does the work then”.

This is an **INTERIM audit**, not final approval or a merge-readiness check.
It has TWO mandatory deliverables: an independent audit AND Claude's own
independently developed ideas for closing the remaining gap. Merely reviewing
Codex's proposed next steps does not satisfy the second deliverable.

**Finish by setting/leaving the topic and PR stage WORK and handing actual
implementation back to Codex. Do not promote to PR, mark ready, merge, or
implement a new research campaign yourself, even if the interim audit is clean.**
This explicit AC instruction overrides the default clean-audit stage promotion.
Keep the existing branch name and PR27 draft; WORK refers to the work stage.

## Read first

Read current AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md,
then this handoff, ../report.md, ../../../results/padua-argmax-bridge-20261105.md,
../campaign-20261106.md, ../LOG.md, ../gates.md, ../rounds.md and ../ALLOCATIONS.md.
Follow proof dependencies in the actual theory records, not only summaries.
For novelty-bearing audit and your own ideas, read the full current
state/IDEAS.md, all relevant obstruction/disposition tables, shortlisted full
entries and linked theory; read literature/INDEX.md before attribution claims.
Main contains PR30's Padua/Lanczos results and PR28's NN-MOP additions.

The fresh fifteen-round campaign is **15/15 complete**. Its count must not
be reset or silently extended. AC explicitly requests work to resume with
Codex after this interim review; prepare a new clearly recorded WORK step
for that return. Do not ask AC again for routine already-authorized execution.

## Exact scientific boundary to audit

The claimed global equality set is proved at degrees2–40 and at every integer
**n>=500000**. The remaining gap is **41–499999**, and all-degree PD-T099 stays
OPEN. This is a sufficient onset, not a minimum-onset claim. The equality set is
{(-1,-1),(1,-1)} for even n and {(-1,-1),(-1,1)} for odd n.

The new half-million proof is entirely analytic, with no energy premise,
assumed global maximum, mass degree scan, or second near-model correction.
Its three cases at n>=500000 are:

- Far: S_n<Lambda_c-1/2000 throughout the closed far diamond rho>=1/2.
- Near noncorner: lambda_n<Lambda_c-1/32 for every admissible odd noncorner
  center at rho<=1/2, all physical signs and both parities.
- Actual corners: lambda_n<=Lambda_c-(alpha²+beta²)/6 on both full inward
  rho<=1/2 patches, with equality only at the origins.

The seven current C13 records are:

1. theory/C13-onset-budget.md — global assembly/index;
2. theory/C13-near-representation.md;
3. theory/C13-near-comparison.md;
4. theory/C13-corner-value-lower.md;
5. theory/C13-corner-comparison.md;
6. theory/C13-far-representation.md;
7. theory/C13-far-comparison.md.

All paths below are relative to this topic unless written from repository root.
Global source SHA256 is
`bc975d53831052f536604dcc2cc9d2552e0f79ba7826a2453708d9ba34ef5ea0`.
Supplementary independent-checks-C13-onset.md is
`e57cd31b2a4f1b987a634c0c9aee539357cd1edb232030ff5fea573a8a8c18e8`;
it preserves the original findings and the accepted focused repair disposition,
all seven new hashes and their proof mapping. The original combined C13 proof
received a MAJOR substantive-split finding and MINOR baseline clarification;
both are resolved without changing estimates, model parameters or threshold.
Attempt attempts/C13-onset.md records the exact changes. Do not confuse the
old first-freeze hash with the seven current audited inputs.

Independently reconstruct the lower-domain argument, not merely its scalar
arithmetic. In particular check strip/endpoint geometry and floor limits,
actual special rows/H8/collision holes, the same fixed model parameters,
monotonicity of every error envelope, the finite corner deformation and baseline
before adding it, and the narrow far slack. The actual lower bound is based on
B_n=n L_n²/(n+1)+1/(n+1), Lambda_c=B_n+Delta_corner; do not double-count deformation.
Near representation is <1/1000; the near S allowance is383/12500<1/32.
The independent exact far slack is
382900852945861/466667600000000000>1/2000. Scalars are controls, not substitutes
for the full-domain proof. All n>=10^6 predecessor statements retain their old
quantifiers; C13 explicitly re-estimates the lower domain.

Read the supporting C05 finite-h, C07 corner, C08 coefficient/endpoint/pole/
integral/comparison, C06 compact-error and C02 dense-defect proofs and reports.
The full corrected common-primitive/cover argument is PD-T364 at repository path
`topics/padua-argmax-effective-2-20261105/theory/phase-structure.md`.
Challenge all closed-boundary limits, a=0, coalescing poles, phase evenness,
endpoint multiplicities, physical-center classes and the exceptional x mode.
Original tight C1 with1/4096 is still OPEN and is not a needed premise.

The finite33–40 computer proof is theory/native-finite-range.md with committed
small certificates and separate GMP replays. The inherited exact checker lives
at repository path `topics/padua-argmax-effective-20261103/code/native_checker/`.
Its theorem, commands and evidence are linked in the finite record; the range
2–32 is inherited. Audit the finite reduction/checker and evidence as appropriate.
No new finite degree was certified in the fresh campaign.

## Cheap-certifier boundary to audit

One complete replay of the ORIGINAL immutable known-n32 certificate passed
364/364 leaves on fixed-work C03 mode0:46.08976645totalCPU,45.228637subprocess,
versus previous139.405409subprocess, about3.08x. No retry, mode switch, producer,
new tree or new degree. See independent-checks-C03-cheap-n32.md and its receipt.
The first C02 run failed76/364 in31.965CPU and remains preserved. Inspect the
acceptance predicates, exact input/source/runtime closure and scoped performance
comparison; do not turn one known-case timing into an all-degree cost law.

The point and row bounds are different experimental components:

- theory/C02-row-cotangent.md gives fixed-block point evaluation; C11's accepted
  CP640/J16 backend has measured point costs.150CPU at n128 and2.456CPU at n2048.
  This is not whole-certifier cost. Valid n2 partial radius can be3.34e-7;
  no universal1e-8 accuracy claim follows from the selected pilot.
- C09's coefficient relaxation gives a guarded O(n) scalar-operation whole-box
  upper method. The direct swept-root enumeration's Omega(n²w) obstruction is
  scoped to that method, not a general lower bound for all certifiers.
- C12 source code/cheap_rows_C12_box/box.cpp is
  `91700bd49211d97bf3b61e278936cdcb45f582e6673e18978ef59cb524340949`.
  Review independent-checks-C12-box.md includes forced whole-row fallback tests.
- C14 coherent eight shared(A,p,q) vertices are in theory/C14-global-vertices.md,
  hash`afdafd0d64d0af7db8d43d5430ed9d560bf5f2cdc11fbc46da57ed9516296b99`.
  Thin row-freezing error is distinct from the remaining O(w H_n²) global
  coefficient-cube relaxation; no total O(w/n) or first-order-cancellation claim.
- C15 source code/cheap_rows_C15_global/global.cpp is
  `7f50e06624e6fa1a01a98ae0fe1f9c166b1f10174d9042c11bc19f5b527c4b6c`;
  independent-checks-C15-global.md is
  `8f3f1a2259ad5ddc6e415d8f7a619f95e73163145bd940619f1b0f913f6c40fb`.
  Independently checked coherent max order, actual collision removal before
  artificial vertices, full J16 radii/tails, radians/rho and shared rollback.
  A late failure must remove the WHOLE actual row from EVERY vertex accumulator.

The native whole-box API is S-upper-only, LP64 n<=4096, nonnegative rational
rectangles wholly contained in the closed phase triangle. Negative-phase adapters,
triangle-straddling boxes, gradients, corner-orbit and defect collectors are NOT
implemented by that API. Do not infer a full certifier or bridge throughput.
C15 measured quality is mixed and about twice C12's n32 cost. Both row methods
still fail strict S<L_c on two selected known far leaves; this is enclosure
insufficiency, not a Padua counterexample. No replacement was adopted.

C08's MPFR producer component is separately checked after a geometry guard fix;
C10's complete-producer controller is only PREPARED, UNREVIEWED/UNRELEASED and
DEFERRED. Do not claim or launch a producer from that plan during this handoff.

## Interim audit deliverable

Write **audit-01.md**, explicitly headed INTERIM. Identify the audited source
commit, exact coverage, actual reviewer model/effort, executed commands and
findings with severity and locations. Reconstruct claims independently;
Codex/Astra supplementary reports are useful evidence, not a replacement for
this cross-model review. Preserve resolved findings and scoped failures.
No silent author-proof repair or promotion based on a report alone.

Use necessary independent exact/native checks proportionately, in fresh audit
output paths with registered caps. Do not erase one-shot outputs or turn audit
verification into rescue retries, a new producer, degree-extension campaign or
unbounded computation. Distinguish inspection from execution. Source guards,
ratio charts, row cuts, arbitrary coefficient poles, precision conversion,
all error radii and forced rollback deserve adversarial checks. Existing full
replay wrappers refuse output reuse; any necessary independent audit replay
must use a properly recorded fresh audit harness and unchanged candidate bytes.

## Mandatory OWN ideas deliverable

Write **audit-01-ideas.md** containing Claude's own independently developed,
ranked proposals to close41–499999 and/or make certification genuinely cheap.
Do not merely summarize Codex's suggestions or assume these fixed models are
the only route. Generate candidates AFTER the full novelty/obstruction gate.
Retain duplicate, failed or deferred ideas honestly; do not force a novelty claim.
Use separate provisional idea records when the workflow requires them.

Aim for3–5 concrete proposals spanning distinct viable mechanisms where possible.
For each give:

1. Exact target, domain and the proof/algorithmic distinction from the closest
   predecessor, with full relevant aliases/obstructions read.
2. Why the known scoped failures do or do not apply; remaining assumptions.
3. Cheapest decisive test, success/kill criterion, required precision, expected
   resource cost and what result would justify the next step.
4. How it could reduce the ACTUAL gap or full producer+checker cost, including
   missing corner/class/degree-block obligations. Point timings alone do not
   justify a finite sweep or Syvert pack.
5. A priority and a bounded, concrete first implementation/proof task for Codex.

The user deprioritizes more degrees with old technology and major cleanup.
The analytic upper boundary is now concrete; focus on useful new reductions,
tightness, batching or mathematical comparison rather than cosmetic extension.
The N4/N6 specified-family failures do not reject their broad targets; N5's
quarter target and original tight C1 remain open. The central fractional-axis
obstruction rejects only the stated quadratic-modulus family. Respect those
scopes when proposing alternatives.

**Claude proposes and audits; Codex does the subsequent development.**
Do not implement your new proposals or launch their research campaign now.

## Scope, evidence and publication

Only the handoff holder/orchestrator controls Git/PR; use disjoint subagent
files if delegating. No main push, PR merge, force push, tags, .github/settings
changes or unrelated cleanup. All pushes remain authorized to this working
branch. Keep PR27 draft: https://github.com/aacchhee/padua_research/pull/27 .

AC's temporary generated-output cap is10,000,000bytes. Current conservative
tracked-output inventory is7,915,495bytes. Essential evidence index v2 has124
rows and13,882bytes: columns are(path,bytes,sha256), with one triple per row.
All essential records are<16KiB. Authored proofs/reviews are not generated raw
output. Keep large traces, binaries and dependency manifests outside Git;
physical archival transfer is pending. C12's21,739B receipt was losslessly
minified to11,664B, with original and metadata history retained locally.
Do not split bulky evidence just to bypass the cap. Major cleanup is separate.

Final IDs and shared-registry application are deferred. ALLOCATIONS.md reserves
T392–431/N146–161/IDEA490–529/LIT598–613; current needs exceed some original
headroom. Refresh the live union and reserve more before later final assignment;
do not assign or renumber final IDs in this interim review. Do not edit global
registries merely to make this checkpoint look ready.

## Acceptance, WORK state and handback

Complete BOTH audit-01.md and audit-01-ideas.md. The latter must contain your
OWN ideas and a prioritized actionable Codex plan. Update topic LOG and PR body
with the interim verdict, findings and planned next work. **Set/leave stage WORK
regardless of a clean verdict; do not set PR or final readiness.**

Commit and push the interim outputs. Then, in a following handoff-only commit,
set this handoff status to done in that output SHA and create **08-...md** for
**Codex, gpt-6-astra high coordinator, Stage WORK**, to address audit findings
and implement the prioritized research plan. Specify bounded first tasks,
inputs, acceptance/kill criteria and what must remain frozen. AC has explicitly
requested that Codex do the work next; no routine permission question is needed.
Preserve the closed15-round campaign count and record the resumed work separately.
Only AC can merge; another final audit/readiness step remains for later.
