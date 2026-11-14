# C02 actual-corner half-diamond development

Date: 2026-11-06. Auxiliary mathematical developer; rules/input
`4b728b04216a5490910780bc609a82b853058426`. Parent owns shared state,
Git, final IDs, status publication and independent review. This worker
owns only new `theory/C02-corner-*.md`, `ideas/C02-corner.md` and this
attempt record. C01 proof bytes remain unchanged.

The assigned target is a direct actual-corner comparison on the full
inward phase half diamond, without an unproved intermediate three-quarter
energy premise. The prospective gate, exact target, failure criteria and
retained alternatives are in [the idea record](../ideas/C02-corner.md).

## Initial decisive test

The same removed family as PD-T228 is retained. For n>=64 and signed
total phase<=1/2, the base plus-angle distance yields
`b>=5d/(6m)`. The delicate unremoved `r=j+1` indices have
`|T|>205/(768m)` and `|T|<1/26`, preserving `t>=1/(4m)`;
other differences have a wider separation. Endpoint coordinate
overshoots must be handled directly to retain `|sin u|,|sin v|<=3b`.
The B-family half angles remain below1.1, so its finite-polynomial
Hessian bound continues without a cardinal sign assumption.

These are analytic calculations only. No numerical diagnostic or degree
scan was executed. The improved `m/n` ratio and plus-angle bound lower
the normalized first/second f-derivative sums to320H and8240H.
The full signed orbit remainder is being written before freezing.

## Frozen developer result

The complete proof is in
[C02-corner-halfdiamond.md](../theory/C02-corner-halfdiamond.md).
It proves, for every n>=64 and inward rho<=1/2 at either nonnode
corner,

    lambda_n <= a Lambda_c+24000rho^2 log(n+1).

Thus the entire punctured patch is strictly below Lambda_c if
Lambda_c>240000log(n+1), in particular if log n>=610000. This
impractical number is an actual-corner sufficient threshold only.
The old PD-T228 proof bytes, C01 proofs and all shared records are
unchanged by this worker.

The displayed rational constants were checked once with Python's
standard-library Fraction, using these exact equalities/inequalities:

    (1536/5)(65/64)^2=2535/8<320,
    8(24576/25)(65/64)^3=32955/4<8240,
    8240+504/2+432+1080/2=9464,
    (99/100)(205/768)>1/4,
    2-65/384>9/5,
    19000(5/4)+5/2<24000,
    4000*610000-240054>0.

The invocation returned `Exact scalar budget checks passed; no phase
or degree samples.` It performed no floating point, scientific sample,
fit, finite-degree extension or evidence-producing sweep. These checks
are bookkeeping controls, not the independent reconstruction or a
computer-assisted proof premise. The full derivations are in the proof.

## Status boundary

The bounded theorem and its routine strict-patch corollary will be
kept separate from any parent global assembly. An enormous
corner-patch threshold is not an effective global onset. Intermediate
all-n energy remains outside this result. Distinct reconstruction and
the formal campaign audit remain separate from developer checking.
