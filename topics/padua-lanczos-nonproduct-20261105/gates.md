# Gate ledger

Criteria: [handoff 01](handoffs/01-work.md), with pre-run measurement conventions
in [plan.md](plan.md). No verdict below is inferred from an unexecuted run.

| Gate | Current verdict | Evidence / next obligation |
|---|---|---|
| N0 predecessor replay | PASS | [Executed replay](n0-replay.md): six SH cases, 88 symbolic identities, four requested degree-12 rows and 44 prefix rows agree exactly |
| N1 family admission | PASS for all used finite families | [Triangle](theory/p1-triangle-admission.md), [disk](theory/p2-01-family-admission.md), [SH weights](theory/p3-01-high-mode-weight-admission.md), [Padua](theory/p5-01-padua-admission.md); exact scopes and dimension bounds in each proof |
| N2 growth screen | INCONCLUSIVE on T24/H24; disk incomplete; algebraic families unrun | [Finite screen](theory/p6-n2-screen.md): inherited T24 and fresh H24 both fail to decide threshold. Disk8 complete,16 running. P3/P5 proofs use no fit premise |
| N3 bounded-order structure | REDIRECT P1/P2 to P4 | No bounded-order full-capacity closure obtained through8; [triangle probe](theory/p1-continuous-creator-probe.md), [disk probe](theory/p2-03-finite-recurrence-probe.md). Not a nonexistence theorem |
| N4 perturbation radius | PASS by analytic sufficient certificate | [P3 proof](theory/p3-03-uniform-capacity-radius.md): eta_0(n)=1/2 for all n>=2, including requested2–10. Weight mode changes with n; no maximal-radius claim |
