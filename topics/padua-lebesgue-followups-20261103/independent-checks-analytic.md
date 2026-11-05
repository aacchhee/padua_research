# Supplementary independent analytic checks — T2, T3 and T4

2026-11-03. Independent checker: Codex, configured `gpt-6-astra high`.
This report supplements, and does not replace, the required Claude audit.
No Git operations or developer-file edits were performed by this checker.

Rules/input head: `3f5196cf3639407c25b021fa30f70cc1d3ae113a`.
Scientific base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.

## Scope and reading

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoff 01,
LOG and plan. Read the complete state/IDEAS.md, including obstruction
and disposition tables. Relevant full inherited records read: PD-T098,
PD-T158/159, PD-T188, PD-T211/212/230, PR12 candidate records IDEA-286–305,
and P1-P2-edges. The developers' T2/T3/T4 gates and preregistered attempts
were read. This is adversarial checking of actual submitted mechanisms;
no new candidate mechanism or historical novelty claim is generated here.

The inherited inputs distinguish vertical numerators `1+z_±` from the
horizontal numerator `1+B`; simply swapping variables is not valid.
PD-T159 controls the absolute diagonal-offset deformation uniformly,
while a limit/rate requires the signed deformation and all endpoints.

## T2 analytic reconstruction — accepted within stated scope

Reviewed `theory/t2-01-edge-centre-minima.md` at SHA-256
`5b1156c384dbf22b9d6749a840f4d78c36f0a1e60a2e8d5fc12e30af309b4c42`
and `theory/t2-02-common-endpoint-expansion.md` at
`a61f3371445bae5bfa71f5b1947f63696697f97ac42c0f742c4eb4d587f98da3`.
No mathematical finding remains for these files at these identities.
Final T2 metadata records completed supplementary checks and verification
links; the initial identities are preserved in the T3 receipt. These
documentation changes introduce no new mathematical claim.

- Horizontal reduction: reflection replaces `1+B` by 1; the band
  substitution cancels its width factor. The phase integral has period
  pi and equals `2K`, giving the displayed `8/pi²` normalization.
  The squared modulus increases strictly with `p²` for every `y<1`.
  At the centre the symmetric triangle becomes half the square; the
  tangent substitution gives `2/((t+u)(1+tu))`. Its exact integral is
  `pi²/4`, hence the inherited horizontal value is exactly 1.
- Vertical reduction: the half-angle substitution gives the minimum of
  `2/(U²-x²)` and `2/(x²-L²)`; the fixed-switch Jacobian is exactly
  `dy/[x(1+|y|)]`. The factor `|p+cos b|` is essential. Pairing reflected
  rows gives `2 max(p,cos b)` and the split at `sin b=q`. The resulting
  positive excess above the inherited central g reproduces both
  formulas (2). The decreasing weighted tail average of `A(t)/t`
  proves F decreases, and then proves strict position monotonicity.
- Null rows where half-angle denominators vanish contribute zero measure;
  nonnegative integration and the inherited finite integral justify
  the changes of variables. These are statements about the limiting
  functions, with no finite-degree ordering implication.
- Endpoint estimate: the reciprocal-tangent split places both K and
  `log(4/t)` within `t/2` below the same quantity, so their difference
  is at most `t/2` (not an unproved asymptotic). Independently checked
  the logarithmic integral, coefficient `8log(2)/pi²` and constant
  `1/3+12log²(2)/pi²`. The common-band integrands are `min(X,Y)` and
  `min(X+1,Y-1)`; the Lipschitz bound and width at most `2d` give
  `4d/pi`. Thus the endpoint statements and explicit errors follow.

## T4 analytic reconstruction and independent executions — accepted

Reviewed the three submitted theory files and enclosure code at the
SHA-256 identities recorded in [the independent receipt](evidence/analytic-independent-t4.json).
The receipt pins t4-01 to `47e0a1b2476e125e4fa8582846f34b52d8fe2b559165941d54454f84445a7356`,
t4-02 to `7f84cbd0d68dd90750173249d91a0464c05dc35751e7b8ea09dd74cee6214fa7`,
and final t4-03 to `f0fb0c2e313c316cb62248f433653e183c17f1b470ed70cba54b9f2021ec33d8`.
The initial t4-03 hash is retained in the receipt. Its final addition states
the already verified decimal enclosures and trusted-base account; a third
full execution at the final theory hash again matched the regenerated
developer receipt exactly.
No mathematical finding remains for these files at these identities.

- Reconstructed the signed offsets and their pairing to the stated
  positive kappa integrand. The inherited bound is valid at all retained
  pairs, including offset one and the last row. The exceptional corner
  and normalization term are exactly `(1-L_n²)/(n+1)`.
- Verified the central-strip bound `13/(n delta²)` per normalized
  difference, the normalization contribution, Riemann endpoint cells,
  discarded rows, and finite/integral offset tails. The choice
  `delta=n^(-1/5), M=floor(n^(1/5))` satisfies its mesh restriction for
  every n>=32 and yields the stated 604 coefficient. The proof is over
  all integers and loses no parity-dependent endpoint mass.
- Independently reconstructed the pole cancellation, bounds
  `0<a_p<=4^(-p)`, `|b_q|<9^(-q)` and convolution/tail factors.
  In particular the geometric tail includes every omitted coefficient
  after order K and is `8/[3(K+2)4^(K+1)]`.
- Checked the cotangent pairing for even and odd n, the derivative
  estimate for the regular cotangent part, the harmonic trapezoid
  remainder and its cancellation. These give the claimed
  `|L_n-A_n|<=1/(4n²)` including n=1. The transfer from n to N=n+1/2
  proves the c-term with its displayed vanishing remainder.

Actually reran the frozen code at order64/bits320 with all ten finite-n
regressions, and at order80/bits384. Both executions exited 0. The first
result equals the developer JSON exactly; the second gives a narrower
ball with the same certified decimal brackets. The receipt records
commands, versions, output identities and trusted Arb/Python dependencies.
The finite-n regressions remain MEASURED, separate from the outward
coefficient calculation and analytic tail theorem.

Certified brackets independently reproduced:

`0.919710118388492535099518225790 < kappa < 0.919710118388492535099518225791`

`1.846160310423926079759838737947 < c < 1.846160310423926079759838737948`

Also executed the ancillary `t4_relations.py` PSLQ script separately:
exit 0 and exact agreement with its developer JSON. Both finite bases
returned no relation at the recorded height, tolerance and step limit.
This is MEASURED bounded-search evidence only; neither absence of a
closed form nor arithmetic independence follows. Identity and scope are
in the same independent receipt.

This accepts the constant and the explicit weak rate only. The `-1/N`
term, sharper `O(log N/N²)` remainder, full PD-T098 target and global
argmax claims are not established by these records.

## T3 formulas and separate numerical checks — accepted

Reviewed `theory/t3-01-general-position-series.md` at
`8eae6849e3a5c756356864bb97dcd3d9fd25b09d2ac58ec93bb96a9e054a3ce5`,
`code/t3_series.py` at
`55e2a9760e52f3ce522dddc707f87f60ff1d71877695ad2804485edd72cec259`,
and `code/t3_quadrature.py` at
`7f8f5772576ed8fe765adb9bf5328e9f8b90b88f2499edf928b45d522a14f656`.
No mathematical or numerical-enclosure finding remains at these hashes.
The final evaluator adds denominator-dependent sqrt precision for rational
m extremely close to 1. Inspected this narrow change and reran both full
series and Darboux commands against the final receipts: both exited 0 and
matched exactly. A separate exact `m=1-2^(-300)` control confirmed sqrt
containment and an upper endpoint strictly below 1.
Final T3 metadata and `evidence/t3-verification.md` were also reviewed;
they document the completed checks, numerical reduction and exact value
table without changing the analytic statements or proofs.
Full commands, versions and result identities are in
[evidence/analytic-independent-t3.json](evidence/analytic-independent-t3.json).

- Vertical: reconstructed the positive shifted binomial expansion,
  its weighted polynomial average P_k, the recurrence for M_l, and the
  exact remainder weight `1+p atanh(p)`. Ratio at most 1/2 holds for
  every interior angle; the prefactor is correctly nonuniform near
  endpoints. Central specialization is an exact identity with PD-T188.
- Horizontal centre: the two tangent changes of variables produce the
  stated logarithmic integral for I_k. Integration by parts gives its
  exact finite binomial expression, and `I_k<=I_0` proves the stated
  tail. The constant term is exactly 1, not a fitted normalization.
- Horizontal endpoint: independently expanded the differential-equation
  numerator and its total-derivative identity. The coefficient and d_k
  recurrences are correct; the logarithmic estimate plus reduction of
  order determines the integral-defined K uniquely. Checked positivity
  of every bracket, endpoint logarithmic integrability, polynomial U/W
  moments and the complete omitted-series majorant. The two charts cover
  all interior angles with ratio at most 1/2.
- Exact evaluator: reviewed interval signs, reciprocal ranges, integer
  square roots, Machin/atanh tails, exact polynomial cancellation and
  outward decimal floor/ceiling. A separate order72 run at m=0,1/4,1/2,
  3/4,99/100 exited 0 and matched the developer JSON exactly. The central
  vertical enclosure is `[0.5485148423995582,0.5485148423995583]`;
  horizontal centre is the exact singleton 1.
- Direct outward quadrature: separately reviewed and executed the
  directed Decimal Darboux checker. Its F and K values do not use the
  T3 series. Correctly rounded sqrt/ln are widened by adjacent Decimal
  values; algebra, summation and negation preserve outward bounds.
  Monotonicity supplies the vertical and inner-K endpoint sums; the
  outer product is bounded factorwise and the remaining endpoint strip
  has the stated explicit logarithmic upper bound. All five exact-series
  intervals lie in the independent quadrature intervals; rerun JSON
  equals the developer JSON exactly. These deliberately coarse intervals
  are an implementation crosscheck, not the source of the reported digits.

A separate checker-written floating diagnostic integrates the original
inherited double integrals, split at their exact fraction switches, for
those same five m. It agrees with the certified-series midpoints within
`3.6e-15`; this is explicitly MEASURED only and supplies no proof premise.
The small regeneration script is
[evidence/analytic-independent-double-diagnostic.py](evidence/analytic-independent-double-diagnostic.py).

## Final scope boundary

Within the exact reviewed identities, T2's limiting-function minimum and
endpoint theorems, T3's formulas/enclosures, and T4's constant with weak
explicit rate have passed this supplementary check. These claims have
written analytic proofs; numerical digits additionally have the executed
outward/exact reductions and separate reruns recorded above. No finite-n
edge ordering, effective argmax bridge, optimal corner remainder, or
universal closed-form exclusion is accepted or implied. The required
Claude audit remains PENDING and is not replaced by this report.

## Protocol qualification — T2/T3 prospective-gate timing

Follow-up review of the final [T2/T3 gate](gate-t2-t3.md), specifically
“Final dispositions and coverage reconciliation”, finds a disclosed
prospective-gate timing deviation. The developer reports completing the
inherited-theory, registry and P1/P2-attempt screen before derivation,
but reading some linked full predecessor bodies only during final
coverage reconciliation: the IDEA-303–305 registration paragraphs, the
full original T-A4a attempt, programme IDEA-206's detailed record and
the shortlisted FINAL_CANDIDATES registration paragraphs.

The applicable [workflow](../../agents/WORKFLOW.md), “Novelty gate and
candidate discipline”, says “Then read the full shortlisted entries and
their linked theory” and “Generate candidates only after that gate.”
The later coverage completion therefore does not establish that the full
required prospective gate was satisfied before mechanism development.
The initial “Gate before development” reading summary must be interpreted
subject to the explicit final timing correction; this check does not
endorse an unqualified claim that all linked bodies were read beforehand.

Disposition: acknowledged historical protocol deviation, preserved for
the required Claude audit; not retroactively cured or waived by this
supplementary mathematical acceptance. The later reading improves the
recorded predecessor coverage and reports no changed mechanism or proof
premise, but cannot change when that reading occurred. The report's
“no mathematical finding” conclusions remain confined to the pinned
proofs and numerical reductions; they are not clean protocol clearance.
No new mathematical or priority claim follows from this qualification.

The required Claude handoff must carry this timing qualification and ask
the auditor to review its disclosure and readiness implications. No
numerical rerun is called for: the final T2/T3 mathematical files remain
pinned to `5b1156c384dbf22b9d6749a840f4d78c36f0a1e60a2e8d5fc12e30af309b4c42`,
`a61f3371445bae5bfa71f5b1947f63696697f97ac42c0f742c4eb4d587f98da3` and
`8eae6849e3a5c756356864bb97dcd3d9fd25b09d2ac58ec93bb96a9e054a3ce5`.

## T4 editorial impact check — 2026-11-03

Compared the current three T4 theory files byte-for-byte with the parent's
raw-byte exports from commit `66eaf855ffd6c68f929996df0621032c4364af7d` in
`/workspace/scratch/lebesgue-analytic-editorial-baseline/`. All baseline
hashes equal the previously accepted hashes. Inspected every diff hunk.

| File | Previously accepted SHA-256 | Current SHA-256 |
|---|---|---|
| t4-01-corner-defect-limit.md | `47e0a1b2476e125e4fa8582846f34b52d8fe2b559165941d54454f84445a7356` | `ea514179f51e2208ef8b5566e5557625afd7ec518fc928f6c6592eb07f51d706` |
| t4-02-one-dimensional-remainder.md | `7f84cbd0d68dd90750173249d91a0464c05dc35751e7b8ea09dd74cee6214fa7` | `71ce5102541c5c7cdc2b4993195087652f1c76829b6b88e5a039464af83284b3` |
| t4-03-corner-constant.md | `f0fb0c2e313c316cb62248f433653e183c17f1b470ed70cba54b9f2021ec33d8` | `b7ffd40e6544d0c22ec9c1e35a35ad895b6acb1fa58e09f01347ce4bc1188398` |

The only mathematical-notation edit replaces the single carriage-return
byte before `m odd` in t4-01's first displayed sum with the literal TeX
`\rm odd` command. This restores the already intended odd-index condition,
which the definitions and proof explicitly use; it changes no domain,
coefficient, estimate, or proof obligation. All other edits update stale
supplementary-check status or add the completed-check link. Required Claude
audit and the sharper open targets remain explicitly pending/open.

Both T4 code hashes still equal their executed and accepted identities:
`t4_constant.py` is `b48d488e2229e7c60293673ffeeec0214fed344858f7ddaebe9975c0dd7347e5`;
`t4_relations.py` is `0861c4b156c5f515e2f8f37a7af036f5a718db8d4bc094cd44882874a8d35303`.
The earlier execution receipts retain their historical theory pins.
Acceptance transfers to the current theory hashes at exactly the prior
mathematical and numerical scopes; no fresh computation was required or
performed for these editorial changes. This impact check does not alter
or waive the explicit T2/T3 prospective-gate timing qualification above.
