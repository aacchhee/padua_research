# PD-T007 — Quadratic-character description at q=2n+1

ID kind: PD-T. Aliases: quadratic Padua set, split/nonsplit trace sets.
Split from: supplied finite_field_padua.md Theorem 6.
Split into: none.

## Statement

Let `q=2n+1` be any odd prime power, `n>=1`, and let `chi:F_q->{0,+1,-1}` be the quadratic character with `chi(0)=0`. Put

`X={x:chi(x²-1)!=-1}`, `Y={y:chi(y²-1)!=+1}`.

Define `eps(x)=chi(2(x+1))` for `x!=-1`, `eps(-1)=chi(-1)`; define `delta(y)=chi(2(y+1))` for `y!=-1`, `delta(-1)=-chi(-1)`. Then the canonical `Pad_n` is

`{(x,y) in X cross Y: eps(x)=delta(y)}`.

Moreover `X union Y=F_q`, `X intersection Y={+1,-1}`, `|X|=n+1`, `|Y|=n+2`, and `|Pad_n|=(q+1)(q+3)/8`. This set is unisolvent for `P_n(F_q)`. Off `x=-1` and `y=-1`, the parity condition is `chi((x+1)(y+1))=1`.

## Definitions and assumptions

The split roots `u` run over `F_q^*`, and the nonsplit roots `v` run over `U={v in F_(q²)^*:v^(q+1)=1}`. Both are cyclic groups. Primitive roots give the usual half-axis orderings. Since `2n=-1` and `2(n+1)=1` in characteristic `p|q`, good characteristic is automatic.

## Status by part

Overall status: **PROVED** (independent developer proof; supplementary Astra check complete; Claude audit-01 accepted the mathematics). No novelty or general coding-weight-distribution claim.

## Depends on

`PD-T004`, `PD-T005`; elementary finite-field quadratic and Frobenius arithmetic.

## Proof

The equation `u²-2xu+1=0` has roots in `F_q` exactly when `x²-1` is a square or zero. Hence the trace-half image of `F_q^*` is exactly `X`. For nonsquare discriminant its two roots lie in `F_(q²)` and are interchanged by Frobenius, so each satisfies `v^q=v^-1`; repeated roots `v=+/-1` also satisfy this. Conversely, a root in `U` with square discriminant would lie in `F_q`, forcing `v=v^-1` and discriminant zero. Thus the trace-half image of `U` is exactly `Y`. These arguments prove the union and intersection claims. Inversion has exactly the fixed elements `+/-1` on either group, so its orbit counts give `|X|=(q+1)/2=n+1`, `|Y|=(q+3)/2=n+2`.

Write `x=(u+u^-1)/2`. If `u!=-1`, then `2(x+1)=(u+1)²/u`, so `chi(2(x+1))=u^((q-1)/2)` since `u+1` is a nonzero base-field element. For a primitive split root `u=zeta^j`, this equals `(-1)^j`. At `u=-1`, the parity is `(-1)^((q-1)/2)=chi(-1)`, precisely the exceptional definition of `eps`.

For `y=(v+v^-1)/2` with `v in U`, `v!=-1`, one still has `2(y+1)=(v+1)²/v` in `F_q`. Now `(v+1)^(q-1)=1/v`, because `(v+1)^q=(v+1)/v`. Taking the `(q-1)/2`-th power of `2(y+1)` gives

`chi(2(y+1))=(v+1)^(q-1) v^(-(q-1)/2)=v^(-(q+1)/2)=v^((q+1)/2)`.

For `v=eta^k`, this is `(-1)^k`. At `v=-1`, that sign is `(-1)^((q+1)/2)=-chi(-1)`, exactly the exceptional `delta`. Equality of signs is therefore exactly `j+k even`. Where both coordinates differ from `-1`, multiplying the two characters cancels the square factor `4`, giving the shortened parity condition. The count and unisolvence now follow from `PD-T004` and rationality from `PD-T005`.

## Checks and sources

The unmodified `quadratic_padua.py` checks primes `5<=q<=47` only. It supplies no extension-field execution. The separately implemented developer `verify_exact.py` checks `q=3,9` inside `F_81`, including the missing smallest field and a nonprime field. Details are in [measurements.md](measurements.md), with commands/hashes in the U0 evidence record. The general prime-power statement is proved above, not inferred from either finite scope.

Source Theorem 6 and secondary predecessor `LIT-014`, `LIT-015` are unverified provenance. No original-paper reading or absence-of-prior-art claim is inherited.

## Scope and open items

The `-1` endpoint exceptions are essential; the shortened character condition only applies off those two lines. General code weight distributions and character-sum applications remain outside scope. Supplementary Astra check complete; Claude audit-01 accepted the mathematics.

## History

2026-10-31, Codex U0; rules/base `d36722823441dc40c6e19d69a174459348dd309c`; assigned `gpt-6.1-sol xhigh`. Derived the nonsplit Frobenius identity and both endpoint parities explicitly, rather than relying on the supplied sketch.

2026-10-31, Codex response-01 A2: updated completed handoff references and Claude audit-01 acceptance metadata only; mathematical statements, proofs and epistemic statuses unchanged.
