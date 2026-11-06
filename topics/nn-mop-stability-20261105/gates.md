# Final development gate ledger

Original G0–G5 criteria in handoff01 remain unchanged. Plan/G3 prediction preceded experiments. u=2^-53; epsilon=2^-52 is distinct. G0/G1/G2 use the frozen six-size baseline grid N=4,8,12,16,24,32 in each family. The full every-integer N=4–64 expansion measures conditioning, not an extra61-size binary64 error experiment. Experimental verdicts remain finite MEASURED results; G3 also has a separate written analytic obstruction. No general stability theorem or certified floating enclosure is inferred.

| Gate | Verdict | Evidence / limit |
|---|---|---|
| G0 | PASS | All12 frozen PD-T290 E values reproduced exactly, including independent Astra rerun. Source/input identities checked; transport-only extraLF corrected. |
| G1 | FAILS the all-tested-cases C4 weak-stability threshold | E/(kappa*u)>10 for KrawN8/16 and HahnN8/12/16, using the mixed input metric and fieldwise output norm. At largeN kappa*u exceeds1, so this first-order comparison becomes uninformative. |
| G2 | FAIL | C4 excess>2 digits at HahnN8/16; stable-marginal C4 ratios182.39/220.68 exceed10. Layer recursion not cleared. Oracle-rounded marginals also leave substantial error. |
| G3 | scoped proportionality prediction refuted analytically | At each fixed N>=4 in the Krawtchouk proximity family, the exact signed-weight witness proves kappa*d_min tends to infinity. Finite sweeps remain MEASURED; Hahn asymptotics remain OPEN. Disjoint-support Angelesco full-triangle data are outside the stated domain. |
| G4 | forward threshold met; strict backward stability not achieved | Native LU and node-space QR improve several cases by >=2 digits with kappa*u<=1e-4. An exact dyadic compatibility residual proves strict joint-data backward error infinite for one accurate N=4 raw LU output. The dated two-component correction/data metric is an amendment, not a silent pass of the original backward limb. Numerical fits completed N=4/8; N=4 native pairs are small, N=8 fails100u mixed target. |
| G5 | reproduction gate PASS (one configuration, Octave 8.4, to the decade) | Large-N variation MEASURED; topic-metric comparison not yet run. Independent Octave9.4 source rerun also clears the selected gate; paper-data verification is review only in that executor. [Run](g5-run/README.md), [audit](audit-g5-01.md). |

A path-plus-anchor diagnostic can give complex nodes/negative weights and is not full NN backward error. Literal exact joint-data backward error may be infinite for incompatible raw arrays; any amended structured/mixed metric must be named without overwriting the original gate.

Dated interpretation, 2026-11-05: G4's forward-accuracy alternative has a measured/proved adverse backward result rather than a finite backward-stability certificate. Record forward gains separately; do not declare a stable NN solver from that alternative. The original strict backward target is generally ill-posed for rounded incompatible arrays. D5 defines a separate joint coefficient-correction/input-perturbation metric, whose nearest version is locally well posed for a frozen SPD norm; finite mixed-stability success needs its own evidence.

## G2 convention and margin (audit-01 MINOR15)

G2's HahnN8 antecedent is narrow: E/(kappa*u)=100.6929, or2.003 excess
digits, only about0.7% above100. With epsilon=2^-52 instead of the
pre-registered u=2^-53, no baseline case would trigger that antecedent.
The convention in plan.md is retained; no run/threshold was re-selected.
