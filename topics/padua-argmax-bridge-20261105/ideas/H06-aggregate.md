# IDEA?argmax-bridge-codex-H06 — Weighted harmonic aggregation

Rules/input `ad257038cdff1d66f6e9c03d7ed43405c76cf6b0`, 2026-11-07.
Parent-released PAPERONLY H06; parent specifies Sol ultra, serving metadata
not independently exposed. Ultra is justified by the coupled endpoint and
global cancellations at log²(n)/n and log(n)/n and the need for a uniform
summed remainder, rather than a formal coefficient expansion. Root owns
Git and shared files. This worker owns only the H06 idea/attempt/theory.

## Candidate registered before derivation

With m=n+1, s=1,...,m-1, r=m-s, q=s/(2m), c=1-1/(2m), let

    D_s=psi(m-cs)-psi(q)-psi(m-q)+psi(cs),
    W_m=(4/(pi*m)) sum_s tan(pi*s/(2m))*D_s.

Proposed exact target is a parity-independent expansion of W_m through
order 1/m, with uniform O(log(m)/m²) remainder, strong enough in
combination with H04's smooth-residual theorem and the exact H01/F03
normalization to prove the original PD-T098 expansion

    Lambda_c(n)=A_(n+1/2)^2+kappa-1/(n+1/2)
                +O(log(n)/n²).

Any use of H04/H05 remains conditional until those separately owned
proofs are complete and accepted by the coordinator. Constants may be
identified from accepted PD-T269 after establishing existence of the
expansion. No numerical coefficient or unproved formal expansion enters.

## Predecessors, separation and first kill test

Read rules/workflow/Codex role, completed Campaign-H gate, F03 theory and
PD-T269/270/271. This is refinement of IDEA-287/288/358, not a priority
claim. F03 alone leaves the weighted harmonic aggregate uncontrolled;
PD-T269 establishes only the limit and a weak rate. The exact separation
is a proved 1/m coefficient with uniform O(log(m)/m²), preserving both
endpoints, both parities and the original polynomial normalization.

Before pursuing the full proof, test that each singular subtraction gives
a remainder whose *weighted sum* is at most this scale. A pointwise
asymptotic with a nonuniform endpoint error, an uncomputed 1/m term, or an
uncancelled log²(m)/m or log(m)/m charge kills that claimed separation.
Such failure defers this route and does not refute PD-T098.

## Status and verification

OPEN at registration. PAPERONLY: no jobs, code, native execution,
literature imports, new rounds or subagents. Independent mathematical
review remains required before adoption.
