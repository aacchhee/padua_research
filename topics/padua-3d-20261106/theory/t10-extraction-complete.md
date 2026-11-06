# PD-T?padua-3d-20261106-codex-T10-09 — complete frozen extraction outcomes

ID kind:PD-T. Aliases: restricted QR verification; exact subset rank. Split from:none. Split into:none. Overall status:**MEASURED**, with exact finite rank certificates and floating mesh quality.

Task provenance: handoff06 T10.3 finite extraction outcome; no registered claim was split into conjuncts or cases.

## Statement and assumptions

For the same frozen best cubature snapshots and unchanged restricted-QR/boundary rules, extraction was completed for n2..16 (n2..7 in the initial quality receipt; n8..16 in `t10-extraction.json`). Every restricted-QR subset has exactly N=binomial(n+3,3) nodes, with a nonzero exact modular cyclotomic determinant certificate. The structured rule also selects N nodes, but its matrices fail the frozen numerical condition gate for n3..16. No exact structured deficiency claim is made.

## Finite quality outcomes

The additional n8..16 run completed both21³/41³ meshes wherever eligible. RestrictedQR41 at n8 is45.45826 versus primary inheritedQR45.53580, a slight finite-mesh win. At n9..16 restricted QR loses on that mesh, ending255.70930 versus161.50265 at n16. Thus “every extraction always loses” is false even at the measured-mesh level. The n6/7 losses remain valid finite observations, but numerical ineligibility of a structured set is not proof of the handoff's literal universal continuous-norm kill. The route is closed for this handoff by **completed finite outcomes of all listed rules**, not by an unsupported mathematical kill or whole-class obstruction.

The extraction norms do not recover the cubature projection's observed advantage, e.g. at n16 best cubature LS16.64112 versus restricted interpolation255.70930. T9-05 still requires a uniform inverse restriction bound to turn projection stability into interpolation stability. Neither the small n8 win nor the other losses resolve that degree-uniform question.

## Exact subset-rank reduction and certificate

Each selected coordinate is cos(2πh/q)=(ζ_q^h+ζ_q^(−h))/2. The unnormalized Chebyshev evaluation matrix therefore lies in R=Z[ζ_q,1/2]. The certificate chooses an odd prime p≡1 modq and a primitive qth root z in F_p. Since p does not divide q, the polynomial x^q−1 has distinct roots in F_p. A root of exact orderq is a root of Φ_q, so ζ_q↦z defines a ring homomorphism R→F_p. The producer evaluates Chebyshev recurrences modulo p and records the nonzero determinant of the resulting N×N matrix. A zero characteristic-zero determinant would map to zero, so the nonzero image certifies exact full rank. A deficient specialization would be inconclusive; none occurred. This argument certifies the exact algebraic node set selected by the frozen integer indices, irrespective of how binary64 QR chose those indices.

`code/t10_subset_rank.py` gives nonzero determinants for alln2..16, including n16 p83233, primitive root68835 of order9248, and determinant10955. The selected-node payload hashes match the final extraction's exact folded-key snapshots for n8..16. The code verifies exact root orders and uses integer modular elimination; actual primes are small enough that its int64 products are exact. These remain MEASURED computation records until the workflow's independent replay and evidence review are recorded; the algebraic reduction above does not alone upgrade the finite computation status.

## Checks and reproduction

The frozen helper `t10_lattices.py` remains43d074620c0ea271dbd94a774f472dd5fb0f23c7920204da3262775207f99c1f. Separate producers `t10_extract.py` and `t10_subset_rank.py`, receipts `t10-extraction.json` and `t10-subset-rank.json`, and `t10-manifest.json` pin code/input/evidence. The extraction receipt includes18 outcomes, exact selected-node hashes and the regenerate-only raw identity; all reported meshes completed, with no fallback. The rank receipt contains every prime/root/determinant witness. Commands are in the manifest; independent replay was requested from root's checker. No producer changes existing node snapshots or frozen helper code.

## Scope, sources and history

Closest mechanism IDEA027, T9-05 and standard approximate Fekete extraction; no novelty claimed. All conclusions are restricted to these frozen input families, rules and finite degrees. Structured exact ranks, continuous Λ maxima, and uniform N-node bounds remain unresolved. History:2026-11-06 same-rule verification addendum after the initial operational gate was recognized as insufficient for the literal kill wording. The canonical interrupted-invocation disclosure is in attempts/T10, without changing any result used here.
