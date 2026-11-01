# PD-T?proof-attempts-2-codex-92 — B1 for generic real exterior parallel diagonal poles

Final ID: **PD-T196**. Provisional ID `PD-T?proof-attempts-2-codex-92` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-N040 / OPEN_TARGETS B1 (structural class split; measured implementation instability retained).

ID kind: PD-T.
Aliases: B1 project two/constrain one; finite-degree generic Ldiag theorem; pole-only generic exact extraction.
Split from: programme `OPEN_TARGETS.md` B1, completed for the class and quantifiers below.
Split into: supporting pole top-form/detection in record 90 and coalescent generic-rank witness in record 91. The unrestricted multi-class target is not silently narrowed or declared solved.

## Statement

For **every fixed** integer `T>=3`, every fixed `M` real nodes `z_i` in `[-1,1]^2` injective for `Pi_(T+1)`, and every fixed positive set of discrete weights, there is a proper real algebraic subset `E` of the offset space `R^(T+1)` with this property:

For all `a=(a_1,...,a_(T+1)) in (2,infinity)^(T+1)\E`, put `ell_j=x+y-a_j`, `pi_j=ell_1...ell_j`, `V_j=Pi_j/pi_j`, `W_j=V_j orthogonal-difference V_(j-1)`. Then the poles are distinct, all are nonvanishing at every node, all dimensions through degree `T+1` are full, and, simultaneously for every `2<=t<=T`,

`W_(t+1) = { r in R_t : r perpendicular W_(t-2) }`,

where

`C_t=(W_(t-1)+W_t+xW_t+yW_t)/ell_(t+1)`,
`R_t=(I-P_(W_t)-P_(W_(t-1))) C_t`.

In particular every vector on the right is orthogonal to `W_0,...,W_(t-3)`. Its lower-block pairings are precisely the next-pole top-form functional of record 90. The exception can be taken to be the zero set of the explicit finite polynomial `F` in record 91, depending on the fixed sampled measure and `T` alone as coefficients. Its complement meets each strictly ordered offset chamber.

## Definitions and assumptions

Spaces are real sampled rational-function spaces with the positive weighted inner product. `Pi_j` has total degree at most `j`, and `V_(-1)={0}`. Evaluation injectivity through `Pi_(T+1)` ensures `M>=dim Pi_(T+1)` and, after nonvanishing division, `dim V_j=dim Pi_j` and `dim W_j=j+1`. This is the free-offset real parallel diagonal class underlying source `Ldiag`: the source normalization `(x+y-2)/sqrt(2)-epsilon_j` differs by a nonzero scalar, with `a_j=2+sqrt(2)*epsilon_j`. “General position” here refers solely to offsets outside the explicitly constructed proper algebraic set for each fixed admissible sampled measure.

## Status by part

Overall status: **PROVED**. Actual supplementary full-file inspections found no blocker; Part 2 Claude audit remains PENDING.

| Mathematical part | Status / verification obligation |
| --- | --- |
| Exact extraction for all `2<=t<=T` in the stated generic real parallel class | PROVED; complete written deduction from records 90–91 and actual independent full-file candidate inspections |

Candidate / claim disposition: retained completion of the requested class theorem. No new numerical-stability or novelty claim.

## Depends on

- `PD-T?proof-attempts-2-codex-90`: exact lower-pairing top form, detector isomorphism and universal upper rank for all outward real offsets.
- `PD-T?proof-attempts-2-codex-91`: for each fixed admissible sampled measure, a structural coalescent rank witness and nonzero pole-only exceptional polynomial for finite `T`.

No part 1 theorem is needed. Part 1's stopped optional B1 attempt supplies history only, not an inherited proof. No source numerical or skew-form generic-rank assertion is assumed.

## Checks

The parent and both independent mathematical agents ACTUALLY inspected the complete frozen candidate proof, with no blocker. Their reviewed hashes/scopes are in `../independent-checks-b1.md` and `../independent-checks-b1-topform.md`. Promotion changed status/verification metadata only; before/after proof-body hashes match in `../outputs/b1_status_metadata.json`. No mathematical computer run is required; no source script was rerun or promoted into exact evidence. These reviews supplement the Part 2 Claude audit, which remains PENDING.

## Sources

Programme `OPEN_TARGETS.md` B1; full programme IDEA-192/PD-N040 record and decisive/adversarial gen1-3 history; part 1 `attempts/T-B1-optional.md`. Exact input definitions and pins: `../b1-input-preparation.md`; fresh gate, scope and original B1 ceiling: `../attempts/T-B1.md`, at read head `ec05862985460ed18d6756b2bd9b4c5266b39df2`.

## Proof

Fix the data and `T` first. Record 91 constructs a proper algebraic exception `E` in the pole offsets only, using positive Gram projectors and a coalescent projective witness valid for these very data. For `a` outside it, all offsets are distinct and `dim R_t=2t+1` for every required `t`.

Fix one such `t` and write `k=t-2`. The map `P_(W_k):R_t->W_k` has rank at most `dim W_k=t-1`. Its kernel therefore has dimension at least

`(2t+1)-(t-1)=t+2`.

Record 90 proves that every vector of this kernel belongs to `W_(t+1)`, whose dimension is exactly `t+2`. Thus the kernel equals `W_(t+1)`. This proves both inclusions, not merely an upper bound on leakage dimension. Since `V_k=W_0 direct-sum ... direct-sum W_k`, record 90's stronger factorization also supplies the claimed automatic orthogonality to every older block.

The same finite exceptional polynomial works simultaneously through `T`, because its rank factors are multiplied only over the finite set `t=2,...,T`. None of this changes the fixed nodes/weights, and none replaces a pole-only genericity assertion with genericity in joint data.

## Scope

This completes the user's B1 requested exact proof for **one precise pole class** and a meaningful arbitrary finite admissible ceiling `T`, not only the `t=2` case. It does not settle B1 for `Ppt`, `Pbhh`, `Pdiag`, unrestricted real directions, or sign-changing pole ratios. It does not say that an individual fixed tapered parameter sequence avoids `E`, or supply a numerical tolerance for rank decisions. Stability of the tested rational Lanczos implementations remains the separate scoped PD-N040 observation. A fixed finite node set is never asserted to be injective in unlimited degree.

The original broader B1 statement and its other classes remain OPEN at their original scope; the present restricted theorem retains its own exact statement and status.

## Open items

Supplementary full-file candidate inspections are complete. Part 2 Claude audit remains PENDING. No exact/interval experiment is a proof dependency, so there is no unexecuted mathematical rerun hidden in this theorem.

## History

2026-11-01, Codex `gpt-6.1-sol xhigh`, ordered B1 box starting 16:35:09 UTC and ending no later than 18:35:09 UTC. The explicit pole-only coalescent structural witness closes the genericity gap left by the source sketch and the stopped part 1 route. The broader source target is preserved; this file claims only its stated real parallel class.
