# PD-N?padua-3d-20261106-codex-T2-01 — Three fixed cyclic generator formulas fail at degree two

ID kind: PD-N. Aliases: K/T/O first falsifiers. Split from: none. Split into: none.

## Statement / definitions / assumptions

Apply the canonical T3-01 cosine dictionary (T2 implementation details in t2-cyclic-dictionary.md) with all n≥1 and respectively
K:z=(1,n+1,(n+1)^2), T:z=(1,n+1,(n+1)(n+2)/2), O:z=(1,2n+1,2n²+2n+1).
Each fixed family is singular at its admissible n=2, where N=10 and M=19. This suffices to reject each as a family unisolvent at every n≥1. It does not exclude an infinite subsequence omitting2.

## Status by part

Overall status: PROVED (analytic explicit null polynomials below). The observed ranks9/10 and n1 quality values are MEASURED evidence in the receipt, not required for the proof. Candidate disposition: REJECTED: failed for each formula's every-degree target; no universal rank-one impossibility.

## Negative-result scope

Attempted mechanism IDEA?padua-3d-20261106-codex-T2-01, precisely the three formulas above. Degree2 only is the counterexample scope. No phases, unions, corrected generators or higher-degree subsequences are excluded.

## Proof

Write θ=2πk/19. For K at n2, (x,y,z)=(cos θ,cos3θ,cos9θ). Then T₂(z)=cos18θ=cos θ=x, so T₂(z)−x is a nonzero degree-two annihilator.
For T, (x,y,z)=(cos θ,cos3θ,cos6θ), and T₂(y)−z=0.
For O, (x,y,z)=(cos θ,cos5θ,cos13θ). The identity2xz=cos14θ+cos12θ=cos5θ+cos7θ gives 2xz−y−T₂(z)=0 because T₂(z)=cos26θ=cos7θ. All three polynomials have visibly nonzero coefficients and degree≤2. Distinct first coordinates establish correct cardinality before singularity is diagnosed.

## Depends on / checks / sources

Only elementary cosine identities and the stated nodes. ../code/t2_screen.py executed with the exact command in ../evidence/t2-cyclic-screen.json. It finds primitive integer nullvectors matching these polynomials and checks Dv=0. No external theorem used. n1 ranks4/4 are separate modular witnesses, not a rescue of the every-degree target. Independent computational replay pending; the displayed elementary proof is checkable without the run.

## Scope / open items / history

Every-degree K/T/O route ends under immutable D2. Their infinite-subsequence targets remain OPEN. Round2 normalized finite-class diagnostic is separate and does not reopen these killed formulas. 2026-11-06, rules ccd9e905d19c0c625c196c4a3f3e707058ed042a.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
response dispositions, ID-kind mappings and evidence changes were covered
by [Claude audit-02](../audit-02.md); its accepted mathematical scope is
recorded there. This dated correction changes no statement or status.
