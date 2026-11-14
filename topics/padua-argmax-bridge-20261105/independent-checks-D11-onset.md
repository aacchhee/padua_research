# Independent D11 onset mathematical and scalar check

2026-11-06. Distinct Codex reviewer, parent-assigned gpt-6-astra high;
serving model/effort metadata is not independently exposed. Rules and input
HEAD: `5ecf97801631192fd10d84089c5a8c79bfb95138`, branch
`codex/padua-argmax-bridge-20261105`. Read AGENTS.md,
agents/WORKFLOW.md and agents/codex/CODEX.md. Root alone owns Git,
shared records, final IDs and range adoption. This is a supplementary
independent review, not the final cross-family Claude audit.

**Disposition: ACCEPTED within the stated D11 scope.** No unresolved
mathematical/source/arithmetic finding. The three separate results establish
near noncorner loss>7/1000, full closed far primitive loss>19/100, and exact
two-corner global argmax for every integer n>=16000, under their explicit
accepted dependencies and numerical trusted base. This report does not
approve a point-cover executable or certify additional finite degrees.

## Frozen inputs reviewed

The author supplied the following final freeze; read completely and checked
against these hashes after independent reconstruction. Paths are relative
to this topic unless stated otherwise.

| Input | SHA256 |
|---|---|
| theory/D11-near-comparison.md | `e07e8ebfe4d56122203826af6cdf6f9e47d948748cc3ed556b368fe966b99f18` |
| theory/D11-far-comparison.md | `2c170e950566749940c4ce71f6c9e4b0b644e0b5aad23ba9beb3cd6fa2eb835d` |
| theory/D11-global-comparison.md | `f716ef76151677d135a55151b3d32caca1134f68f2cee0ecf2cea310f01223e2` |
| attempts/D11-onset.md | `5c3ddd65bf40bd1ca047b0034419bb4f8fecdeaeb13a1cfe9f28d37b30d31de7` |
| code/post_audit_D11_onset/evaluate.py | `4c11d7f35b3943da46f7aeb2d54a0babcb87b24eb79ef31961a4513fd9d3a927` |
| code/post_audit_D11_onset/SPEC.md | `d3df582cd337107e63f124f08d25d64bc49ea8b41a65c3777876e4137b044738` |
| code/post_audit_D11_onset/budget-16000.json (4770 bytes) | `34675d877186c34f16a40c2dc5b2470c27ec2fbb40f62b338c2dd24e96583afb` |
| Author D06 arithmetic/component source | `9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413` |

The author's original execution-order departure is recorded canonically in
[attempts/D11-onset.md](attempts/D11-onset.md); this review does not erase it.
The reviewed prose correctly distinguishes a conditional formula evaluation
at execution time from subsequent acceptance of its premises.

## Scope and predecessor checks

Read the current state/IDEAS.md across its complete sections, aliases,
dispositions and obstruction tables, using smaller supplementary slices
where broad retrieval was truncated. Read full shortlisted IDEA336/337 in
padua-argmax-effective-20261103/ideas/r1-r2-r5.md and IDEA459 with its related
obstruction in padua-argmax-effective-2-20261105/ideas/H2-H3.md. Read the full
D11/C13/D08 onset ideas and the relevant C13 assembly, D08 near/far/global
architecture and D10 constant records. Searches included relative constant,
entropy, fractional, onset and one-minus-a across the registry and this
topic's ideas/theory. No new mechanism was generated and no literature or
priority claim is accepted here.

The disposition is a quantitative VARIANT of the existing three-case
primitive/defect assembly. The scalar maximum27A^4/(256B^3) is already
used in D08/C04; its use is not new. The actual distinction is the new
sufficient onset obtained from accepted D10's true fractional near
increment and22(1-a) far increment, with unchanged valid finite errors.
The axis/cusp obstruction is respected, since neither C_infty nor the
finite primitive is assumed to have a uniform quadratic upper through0.
PD-N079 and the old raw-profile failures do not refute this assembly.

Proof dependencies read for their actual application domains: C08-far-
weighted-coefficient; D10-relative-constant, D10-global-constant and
D10-far-relative-constant; D08-near-representation and D08-far-comparison;
D05-outer-comparison and the exact T_Z definition of D05-outer-profile-
variation; C02-defect-dense-band; D02-corner-comparison; and the full
PD-T364 phase-structure proof in padua-argmax-effective-2-20261105.
D10's accepted supplementary report is
`bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c`.
Its accepted analytic results are inputs, not newly claimed from numerical
agreement. The inherited PD-T271 trust/provenance was checked in the full
attempts/D08-corner-limit.md; no historical Arb computation was rerun.

## Independent mathematical reconstruction

Put u=1-a,r2=alpha²+beta²,rho=|alpha|+|beta| and L=log n. The exact
coefficient inequality b_full-b_c<=3u/pi² gives model excess at most
-uT+DeltaC, T=(4L²-3L)/pi². This is the actual C08 inequality; the invalid
relative-b shortcut from the earlier campaign is not used.

On rho<=1/2, the cosine remainder gives
u>=r2/4-(alpha^4+beta^4)/48>=47r2/192. For rho>0,
sqrt(rho)log(1/rho)<=2/e<3/4, while r2<=rho². D10's entropy term
is therefore at most rho^(3/2)/3, giving
DeltaC<=A rho^(3/2)+(113/72)r2 with A=77/96. Defining
B=[47T/192-113/72]/2, its positive endpoint and increasing T imply B>0
throughout n>=16000. Since r2>=rho²/2, model excess is bounded by
A rho^(3/2)-B rho². Substituting y=sqrt(rho), differentiation yields
maximum J=27A^4/(256B³). Origin and axes use continuous values and no
relative division by a vanishing phase. T and B increase, J decreases.
No eta0 bridge or second near correction enters this derivation.

The exact Ehat five-component formula was matched term-by-term to
D08-near-representation(2), whose actual representation domain is n>=32.
Its later Ehat<1/80 conclusion at40000 is not invoked at16000. Independently
checked every derivative: A_D/A_6 decrease by elementary log-over-power
calculus; A_G's numerator exceeds m times its derivative; A_log's numerator
exceeds3; the four A_M terms decrease after splitting its second term into
(4+bL)/(4n²-1)+b/[n(4n²-1)]. Thus Ehat decreases on n>=32.
Two absolute representation errors give S_n-Lambda_c<=J+2Ehat. Each
physical odd noncorner has at least one interior center coordinate, so
C02's applicable projected floor is strictly>1/16 from n4096. PD-T364
gives Delta>=max(Q_h,Q_v); the projections are not added. The independent
endpoint and monotonicity give the claimed physical near deficit>7/1000.

For the far domain, a=cos(rho/2)cos((|alpha|-|beta|)/2)<=cos(1/4),
so u>=191/6144. D10 gives DeltaC<22u, hence completed-model gap
>u(T-22). T(16000)>35 ensures the multiplier is positive, so the gap
exceeds F=(191/6144)(T-22). F increases thereafter. This argument keeps
closed boundary phases, a=0 and all weighted collisions; no inverse-a
argument or finite corner lower from a limiting constant is used.

The full U_F is precisely D05 at R2,delta pi/8, a=p=d=1,P=2,|U0|=8,
H_n<=1+L. Its domain is n>=ceil(2pi R/delta)=32. All phase substitutions
increase the nonnegative formula; the entropy dependence increases in
both arguments, including the continuous zero limit. Reconstructed all
13 FAR components, including e_rows/I_n, both pole charges and all four
T_Z contributions. In T_Z, epsilon=3h/2 and ell=5h/2 give the logarithms
log(4m/pi),log(8m/5),log(2m) used by the checker. These are exact
simplifications, not dropped terms. U_F decreases for n>=32: positive
log-over-power terms, the two C_X derivative tests, the collision terms,
fixed-constant I_n, and the increasing argument of positive decreasing
W(delta-h/2), all have the correct signs. The origin uses Ehat, not U_F.
The independent endpoint gives F-U_F-Ehat>19/100 for every n>=16000.

For global assembly, PD-T364's two odd rectangle vertices are physical
and their normalized L1 distances sum to2. Thus every point has a closed
rho<=pi physical chart. The seam rho=1/2 is included in both comparisons.
Near noncorners use the physical defect; near actual corners use the
separate D02 inward r2/4 loss valid n>=10000; far points use lambda<=S_n.
D02's strictness away from phase0 handles arbitrarily small inward phases.
Odd endpoint centers are(n,m) and(0,m) for even n, or(n,m) and(n,0) for
odd n; their cosine images are exactly the stated two corners. Node
centers are not added: nodes are covered at rho=pi. Endpoint weights,
reflection multiplicities, initially zero terms, chart ties, square edges
and finite-polynomial collision values remain in PD-T364's identities.
Every input floor is below16000; no old finite quantifier is transferred.

## Independent computation and arithmetic review

The independent source/spec were frozen and sent to root BEFORE execution.
Original command:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D11_onset_review/check.py

The first execution failed in its post-computation evidence identity guard.
The exact failure, original source, root-reviewed one-line repair, recovery
preregistration and timing limitation are preserved canonically in
[code/post_audit_D11_onset_review/RECOVERY.md](code/post_audit_D11_onset_review/RECOVERY.md).
One explicitly released recovery then ran, with no other degree, fallback,
retuning or further execution:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D11_onset_review/recover_once.py

Recovery exit0, **PASS_INDEPENDENT_D11_N16000**. All28 independently
reconstructed intervals lie inside the author's outward intervals. The
recovery evidence is fresh and6931bytes. In particular its interval
consequences are

    near gap > .00747769365011311931319511289825728 > 7/1000,
    far gap  > .19899350140355793239091683939325164 > 19/100.

The checker independently transcribes the mathematical formulas and imports
no author D11 or D06 evaluator. Only seven arithmetic function/class AST
nodes are selected from the accepted independent D08 checker, after its
full source hash check. No top-level assignment, old evaluate function,
old control or old40000/50000 job executes. The selected definitions were
read: directed interval addition/multiplication/division/negation/powers;
monotone max; exact dyadic rational logarithm reduction;90 positive atanh
terms with tail<=2*t^181/[181*(1-t²)]; and alternating arctangent bounds.
The independent pi bounds use exact Fraction Machin50/16 terms. Basic
Decimal arithmetic uses70digits and explicit outward rounding. Logs do
not call Decimal.ln. All divisors are positive on the evaluated intervals.

Separately inspected the author's complete D11 source and AST-selected
D06 definitions. Its50-digit basic operations are directed, pi is bounded
by exact rational alternating Machin70/20, and adjacent representables
around correctly rounded Decimal.ln enclose each log endpoint. AST
selection excludes the D06 mpmath import and old jobs. Every formula and
substitution matches the independent mathematical transcription. Interval
containment corroborates that source inspection; agreement alone is not
the analytic proof.

Runtime: Python3.12.14. Recovery child CPU measured by RUSAGE_CHILDREN was
0.112433s, wrapper CPU0.016066034s, wall0.11421665400121128s; internal checker
reported0.09599588599999999s. First-run CPU is UNKNOWN because its assertion
preceded the receipt. With the documented conservative1s first-run charge,
accounted aggregate is1.128499034s, below10s. This is not presented as a
measured exact aggregate; the failed run's enclosing tool reported0.3s wall.
No native/kernel, board, quadrature, root, phase-grid or finite-degree job ran.

| Independent artifact | SHA256 |
|---|---|
| code/post_audit_D11_onset_review/SPEC.md | `497f817581a072c314d325c74a47aeb3584968dffc296dd3c32182559b4d6469` |
| code/post_audit_D11_onset_review/check-first-failed.py | `abeb5d5c147cbd16cdb63843f7cf79c65aab465265c0379f409a31b12b4d429b` |
| code/post_audit_D11_onset_review/check.py | `4816e2ee9109baad796aceb59580c120a5dae8c48a41eb4daf87054750a742d7` |
| D08 independent arithmetic library | `37e58bc880259c27cd2282dab48231f11822452d6fd2db876c846d1b9a008485` |
| code/post_audit_D11_onset_review/recover_once.py | `b8c14f46aed6117922bb97fb54a9568c42e623938b0599eb9587480e43ebdd50` |
| evidence/post_audit_D11_onset_review/scalars.json | `965d1b915a9516f078e1996669ac6a140cd710c2f52d4ea94506bcde49b3761a` |
| evidence/post_audit_D11_onset_review/recovery-receipt.json | `c9b3e72d9a3c5f593744805487817a80aa4f82c5acfaf4c38adb3bb293756be9` |

## Findings, trust and limits

No unresolved BLOCKING, MAJOR or MINOR mathematical finding in the frozen
D11 scope. The developer's substantive near/far/global split is appropriate.
Author timing/provenance and reviewer recovery qualifications remain at the
canonical links above; no prose/source/evidence was silently repaired.
The reviewer edited only this report and its disjoint review source/evidence
paths; no author file, shared registry, handoff or Git state was changed.

Trusted dependencies are the stated accepted analytic inputs, Python exact
integer/Fraction operations, correctly directed Decimal basic arithmetic,
and the inspected finite series reductions. The accepted PD-T271 Arb
origin-constant premise and its exact-tail proof remain inherited numerical
trust; they were not freshly rerun here. This supplementary check does not
close the final Claude audit's upstream obligations. It leaves the original
all-degree bridge/gap41..15999, full finite S_n-a*S_n(0), executable whole-box
backend, runtime and minimal-onset questions unresolved. No historical
novelty, priority or new method is claimed. Root may integrate these reviewed
D11 scopes while retaining those limits and the canonical chronology.
