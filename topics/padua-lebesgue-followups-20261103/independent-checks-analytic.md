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
`afc8585aa1482a3b4c88c7898efd54a1e84db32487150b7848fa408765ec1b6d`
and `theory/t2-02-common-endpoint-expansion.md` at
`ae2c2bdc80fa584a1308995df61a83c26b5bf967ee7a96b26e75fb46e532e4ac`.
No mathematical finding remains for these files at these identities.

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

## Remaining review boundary

T3 general-position series and consequential evaluation code are still
awaiting submission. Required Claude audit remains PENDING independently
of the accepted supplementary scopes above.
