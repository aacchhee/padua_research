# Bounded independent analytic reading of the n7/n8 field proofs

Verification record, not a mathematical audit or a finite arithmetic replay.
Date2026-11-01. Reader: Codex `/root/a5_n4`, inherited gpt-6.1-sol xhigh; serving-model metadata independently unexposed. This worker authored the n6 predecessor40 and is independent of the n7/n8 developers, so this is a bounded supplementary reading of the new arguments, not an independent audit of the entire shared method. Required Claude audit remains separate and pending. No other worker's source/theory was edited.

Rules read at842dfaaeff524b4db4141d314afff6ad4a5b7721 and checked unchanged in subsequent heads. Reviewed complete text of:

| File under theory/ | SHA256 |
|---|---|
| proof-attempts-2-codex-50-degree-seven-principal-field.md | ee31f199cfc3ecaa66f9fd21fa01741d820ff78f1d11e02ef6b24e2e7431bb6a |
| proof-attempts-2-codex-60-degree-eight-principal-field.md | adfe98bb9f94f23dc16534f2a1e1b34362877c0fc914fa2eb4e89c3baf216d0e |

## Covered analytic parts

The degree arguments are valid: the cubic polynomials have no possible rational root±1, the quartic t⁴−4t²+2 is Eisenstein at2, and the compositum degree is12 because it is at most12 and divisible by both3 and4. The12 reduced tensor monomials span and therefore form a basis. Conditional on the explicitly stated nonzero conversion determinant and reduction identities, the primitive-element/minimal-polynomial and native-to-tensor interpretation arguments are valid. This reading does not substitute for verifying those finite identities.

The physical embedding arguments are valid on the stated outer brackets. I checked the Chebyshev products by elementary multiplication/recurrence:

- U6(t/2)=(t³−t²−2t+1)(t³+t²−2t−1);
- U7(t/2)=t(t²−2)(t⁴−4t²+2);
- U8(t/2)=(t²−1)(t³−3t−1)(t³−3t+1).

For the degree-seven cubic bracket, the stated values−1/125,33641/10^6 and derivative/other-factor monotonicity correctly isolate the largest U6 root. For the quartic bracket, hand fraction arithmetic gives P(46/25)=−31294/390625 and P(37/20)=3761/160000; P'=4t(t²−2)>0 above46/25, and the remaining U7 factors have no root there. For the degree-eight cubic, hand arithmetic gives Q(187/100)=−70797/10^6 and Q(47/25)=73/15625; Q'>0 above187/100, while t³−3t+1 is already positive and increasing there. Thus each sign-straddling sub-bracket selects the claimed largest Chebyshev root.

The interval interpretation is sound: after exact conversion, evaluation of the tensor polynomial on enclosing rational a/b intervals is inclusion-preserving, and exact outward floor/ceiling rounding retains inclusion. This supplies a chosen real embedding independently of any approximate symbolic root selector. The supporting field theorems properly assert no maxima count or search termination.

## Deliberate limits

I did NOT recompute either12×12 determinant, every conversion-matrix column, the displayed degree12 resultant/minimal-polynomial coefficient lists, any native-field implementation identity, or any cardinal/node/cone/count/value computation. I executed no mathematical script for this reading. Those obligations belong to the separate field replay, formal-quotient verifier and actual producer/checker executions. I did not inspect the full registry again as an ideas audit: this is a no-new-novelty, bounded proof reading inside the already gated A5 target, not a priority or novelty claim. The separately recorded current n6 gate covers the shared registry context.

Within these exact analytic limits I found no mathematical issue. This record endorses neither the unreviewed finite arithmetic nor an n7/n8 count, and is not the required Claude audit.
