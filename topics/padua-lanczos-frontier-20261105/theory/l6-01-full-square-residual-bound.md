# PD-T336 — Explicit full-square residual bound for the PD-T145 family

Final registration (2026-11-05): **PD-T336**; status **PROVED** unchanged. Canonical provisional/historical aliases: `PD-T?lanczos-frontier-codex-L6-01`. See [complete map](../preparation/final-id-map.json). This is ID metadata only; original statement/proof and frozen input bytes retain their scopes.

ID kind: PD-T.
Aliases: complete-square commutator residual bound; e/6 commutator constant; square Q residual diagnostic.
Split from: the unfinished analytic draft in `attempts/L6.md`; supporting statement only, not a proved part of PD-T056(G).
Split into: the no-unbounded-e/u realization consequence is recorded separately as `PD-N?lanczos-frontier-codex-L6-01` in [l6-N01](l6-N01-complete-residual-realization-obstruction.md).

## Statement

Use spectral matrix norms throughout. Let `0<e<=1/300`. Let `Hx(e),Hy(e)` be the exact symmetric degree-one sections of the unit-mass PD-T145 measure

`mu_e = delta_(t,t)/6 + delta_(-t,-t)/6 + delta_(1,0)/3 + delta_(0,1)/3`, `t=sqrt(3e)`,

in the positive-leading orthonormalization of `(1,x,y)`. Then

`||Hx(e)||_2<=1`, `||Hy(e)||_2<=1`, `||[Hx(e),Hy(e)]||_2>=e/6`.                 (1)

Let X,Y be any real 3-by-3 matrices satisfying `XY=YX`, `||X||_2,||Y||_2<=1`, and let Q be any invertible real 3-by-3 matrix. Define the **complete** residuals

`Fx=XQ-Q Hx(e)`, `Fy=YQ-Q Hy(e)`.

Then

`||Fx||_2+||Fy||_2 >= e sigma_min(Q)/12`.                                  (2)

In particular, if `c>0`, `u>0`, each residual is at most `c u ||Q||_2`, and `||Q^TQ-I||_2<=1/2`, then

`e<=24 sqrt(3)c u<48c u`.                                                   (3)

The statement does not assert that a one-relation BJ recurrence controls both complete residuals. All omitted Y columns must be included in Fy before (2) or (3) is applied.

## Definitions

`[A,B]=AB-BA`; `sigma_min(Q)=1/||Q^-1||_2`; `kappa_2(Q)=||Q||_2||Q^-1||_2`. With upper triangular positive-diagonal Cholesky factor `R` defined by `M=R^T R`, sections use the convention `Hx=R^-T Cx R^-1`, `Hy=R^-T Cy R^-1`. This fixes both the order and the common orthonormal gauge. Simultaneous orthogonal changes of that gauge preserve (1), and (2) applies after changing Q in the same gauge.

## Assumptions

Exact real arithmetic. Matrices are precisely those defined above, without an unquantified consistency correction. Both residuals contain all three columns. No orthogonality assumption on Q is needed for (2); the Gram-loss bound is used only for (3). The original coordinate matrices `diag(0,1,0)` and `diag(0,0,1)` are examples of the permitted X,Y.

## Status by part

Overall status: PROVED (written analytic proof; distinct independent reconstruction PASS in [independent-checks-frontier-05.md](../independent-checks-frontier-05.md); later required Claude audit remains pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit section bounds (1) | PROVED | Rational commutator entry, Cholesky comparison and compression proof below |
| Complete-square residual lower bound (2) and consequence (3) | PROVED | Exact commuting-operator identity and spectral norm inequalities below |
| Actual-run realization, positive nearby model, or universal reading-(G) obstruction | OPEN | Not a claim of this theorem; PD-T056(G) retains its original status |

Candidate disposition: IDEA?lanczos-frontier-codex-L6-01 retained as this bounded diagnostic. Its separate realization rejection has the exact scope of l6-N01. No final ID assigned here.

## Depends on

PD-T145 supplies the explicit family and its moment matrices. They are reproduced below and the constants here are proved directly. PD-T057/058 fix the section and reading-(E)/(G) conventions. The elementary residual-commutator mechanism already appears in IDEA-106 / PD-T060; no novelty is claimed for the identity. No external result is required.

## Checks

This is an analytic proof, not a computer proof. No scientific code, numerical experiment, symbolic-program check, new output bytes or actual recurrence run was performed. Direct checks are displayed in the proof: the inverse M, the A/B entries, the commutator numerator, positive leading minors, determinant/trace conversion and Cholesky orientation. Unrun scientific commands: none assigned; the actual-run contract is separate and unexecuted.

Distinct reviewer `/root/reviewer`, requested `gpt-6-astra` high (runtime metadata not independently exposed), independently reconstructed the four-atom moments, inverse/A/B, scalar commutator entry, Cholesky orientation and conditioning comparison, compression norm, full residual identity and final constants: **PASS**, [durable review](../independent-checks-frontier-05.md), section "Additional root allocation: L6 necessary-condition review". Reviewed input SHA256 `d90d7e9fb15506202bf26c426ed0e574214f090bb8cf2065ba9ba6693ee82149`. The post-review changes to this file are acceptance/link/history metadata only; the statement, assumptions and proof body are unchanged. This is independent mathematical reconstruction, not a scientific rerun or the required later Claude audit.

## Sources

Internal PD-T145, PD-T060 and PD-T057/058 only. The literature INDEX and PR #21 P3 comparison/addendum were consulted for the completed gate in [ideas-l6-continuation.md](../ideas-l6-continuation.md); no unread or secondary external statement is used as proof and no external priority claim is made.

## Proof or evidence

**1. The moment matrices and similarity orientation.** In `(1,x,y)`, the measure gives

```
M  = [[1,   1/3,     1/3],
      [1/3, 1/3+e,   e  ],
      [1/3, e,       1/3+e]],
Cx = [[1/3,   1/3+e, e],
      [1/3+e, 1/3,   0],
      [e,     0,     0]],
Cy = [[1/3, e, 1/3+e],
      [e,   0, 0    ],
      [1/3+e,0,1/3  ]].
```

For example, the split origin mass changes exactly the three degree-two moments by e and changes no degree-one or degree-three moment. This gives these matrices directly. The positive leading minors of M are `1`, `2/9+e`, `(1+18e)/27`, so M is positive definite. For `M=R^T R`, set `A=M^-1 Cx`, `B=M^-1 Cy`. Then

`R A R^-1 = R(R^-1 R^-T)Cx R^-1 = R^-T Cx R^-1 = Hx`,

and similarly `Hy=R B R^-1`. In particular, `[Hx,Hy]=R[A,B]R^-1`; reversing this orientation would give the wrong norm comparison.

**2. The rational commutator entry.** Put `D=1+18e`. Multiplication of the displayed matrices gives

```
M^-1 = (1/D) [[3+18e, -3,       -3],
               [-3,    6+27e,    3-27e],
               [-3,    3-27e,    6+27e]].

A = [[0, a, b], [1, c, d], [0, f, d]],
B = [[0, b, a], [0, d, f], [1, d, c]],

a=9e(1+2e)/D,  b=3e(1+6e)/D,
c=(1+6e)/D,   d=-3e/D,  f=-12e/D.
```

The expression for B also follows by simultaneously swapping x and y (the last two coordinates) in A. The row-zero/column-one entry, indexing from zero, is

`[A,B]_(0,1)=a(d-f)+b(d-c)`

`= [81e^2(1+2e)-3e(1+6e)(1+9e)]/D^2`

`= 3e(12e-1)/D^2`.

Because `1-12e>=24/25` and `D<=53/50` on the stated interval,

`||[A,B]||_2 >= |[A,B]_(0,1)| >= (7200/2809)e`.                            (4)

**3. Conditioning and the e/6 bound.** The positive eigenvalues of M obey

`lambda_max(M)<=tr(M)=5/3+2e<2`, `det(M)=D/27>=1/27`.

Consequently `lambda_min(M)=det(M)/(lambda_2(M)lambda_3(M))>=1/108`, where the other two eigenvalues are each at most 2. Thus

`kappa_2(R)=sqrt(kappa_2(M))<=sqrt(216)<15`.

From `[A,B]=R^-1[Hx,Hy]R`, submultiplicativity and (4) give

`||[Hx,Hy]||_2 >= ||[A,B]||_2/kappa_2(R)`

`>= (7200/(2809 sqrt(216)))e > (480/2809)e > e/6`,

where the last inequality is `2880>2809`. The weaker non-strict lower bound in (1) follows.

For the upper norm bounds let V be the 4-by-3 weighted evaluation matrix of `(1,x,y)` at the four atoms, each row multiplied by the square root of its weight. Then `V^T V=M`, and `U=V R^-1` has `U^T U=I`. If `Dx,Dy` are the diagonal coordinate matrices on those four atoms, then `Hx=U^T Dx U` and `Hy=U^T Dy U`. Since `t=sqrt(3e)<=1/10`, every coordinate lies in `[-1,1]`. Hence `||Dx||_2,||Dy||_2<=1`, and both compressed section norms are at most one. This completes (1).

**4. The complete residual identity.** This step holds for arbitrary same-size Hx,Hy, commuting X,Y and invertible Q, with residuals defined as in the statement. Expand

`0=(XY-YX)Q`

`=Q(Hx Hy-Hy Hx)+Fx Hy-Fy Hx+X Fy-Y Fx`.

Therefore

`Q[Hx,Hy]=-Fx Hy+Fy Hx-X Fy+Y Fx`,

and

`||[Hx,Hy]||_2 <= ||Q^-1||_2 [(||Hy||_2+||Y||_2)||Fx||_2`

`                                      +(||Hx||_2+||X||_2)||Fy||_2]`.

Under the four norm-at-most-one bounds, the right side is at most `2||Q^-1||_2(||Fx||_2+||Fy||_2)`. Combining with (1) proves (2).

If each residual is at most `c u ||Q||_2`, (2) yields `e<=24 c u kappa_2(Q)`. The eigenvalues of `Q^TQ` lie in `[1/2,3/2]` under the Gram-loss hypothesis, so `kappa_2(Q)<=sqrt(3)<2`. This proves (3). ∎

## Scope

This is a necessary condition for exact complete-square relations to the specified sections. No actual run is exhibited. No claim says a window recurrence controls the omitted Y columns. Inconsistent raw data, a correction to those data, a nonsquare Q or a different section family require their own analysis. An ill-conditioned Q or e comparable with u is not excluded. Neither existence nor nonexistence of a positive nearby model for arbitrary actual runs follows.

## Open items

Parent-owned status integration and later required Claude audit. The prospective n1 fixed-operation contract is [l6-02](l6-02-actual-n1-implementation-contract.md). PD-T056(G), including actual n1 and Padua n3/4 output, consistency correction and a nontrivial localized-model radius, remains OPEN. This theorem is supporting material and does not change that target to PARTIAL.

## History

2026-11-05, Codex mathematical developer, requested `gpt-6.1-sol`, xhigh; actual runtime variant/effort not independently exposed; rules `9825d184517db81d0aad8542fbd6639f2164b803`. Completed the saved unfinished residual calculation after the continuation gate and exact target/kill were recorded. The saved weaker target `e<=48c u` is retained and sharpened to `e<=24 sqrt(3)c u`. The original early-draft gate timing deviation is preserved in the attempt and candidate record, not retroactively cured. No Git/shared-registry edit by this developer; no scientific execution.

2026-11-05: distinct Astra-high routine reconstruction PASS at the input hash in Checks. Acceptance metadata added after review; proof body unchanged. Broader actual-run target remains OPEN.

2026-11-05 audit-01 response, Codex statement/metadata worker; requested gpt-6.1-sol high; runtime variant/effort not independently exposed. Rules read at `7f50cae80f5372db7c278aef4ba4a0a05e1137ea`. L6-1: the no-run statements above describe this analytic author's earlier boundary, not the later technical execution. The unchanged frozen contract's current execution metadata are in [its additive companion](l6-02-execution-metadata-20261105.md); [L6-03](l6-03-frozen-n1-output.md) and [N02](l6-N02-frozen-n1-raw-data-nonrealizability.md) contain the later finite run/raw-branch outcome. L6-3: IDEA L6-01 remains **retained**, with the barrier PROVED; **REJECTED: refuted** attaches only to the hypothesized unbounded-e/u realization under N01's exact hypotheses. The saved pre-gate draft already contained the identity, e/6 and weaker e<=48cu; the analytic continuation/verification followed the completed gate. The saved candidate draft first entered Git at `0574c47` before its prospective source gate was complete. Later completed reading does not cure or waive that deviation; acceptance remains AC's decision. The dated chronology and missing-read/gate checkpoints are in [gate-timing-response-01.md](../gate-timing-response-01.md). No novelty or priority claim is added.

## History addendum — 2026-11-05 (handoff10; A-P1)

This result descends from L6-01 complete-residual commutator barrier, drafted before completion of the mandatory reading gate and first committed at `0574c47`. AC accepted the disclosed deviation on 2026-11-05. The deviation remains permanently disclosed, not waived and not cured. Completed-gate receipt: G6: `6012600`; these are publication SHAs, not worker input/rules SHAs. G6, L6-01, its scoped negative and the contract share `6012600`; their reported gate-before-development order within that commit is not established by Git. Earlier pending-decision wording is historical and is superseded by this dated acceptance record. See [gate-timing-response-01.md](../gate-timing-response-01.md).

## Merged-source attribution addendum — 2026-11-05

PR21 merged into main as `b4d292e`. The current source is [topics/padua-literature-20261103/p3-comparison.md](../../padua-literature-20261103/p3-comparison.md), unchanged memo blob `4741c38943f37ae05ba525552ceafc3f32ac5537`. The following per-statement attributions now cite that merged path with the same blob; earlier “unmerged” prose remains historical.

- completed-gate P3 comparison/addendum attribution: cite the merged P3 path and blob above; the original statement’s selected-source, version/page and primary-reading coverage limits remain unchanged.

This updates source location only. It asserts no new primary reading, proof import or exhaustive priority/novelty clearance.
