# PD-N?argmax-alln-codex-01 — tie-inclusive local-maxima ordering fails at n=4

ID kind: PD-N (provisional; allocate at PR preparation).
Aliases: O-Lt; tie-inclusive IDEA03 reading; diamond-cell certified-list ordering.
Split from: none. This is a scoped operationalization of the ambiguous IDEA?argmax-alln-claude-03, not a replacement for its wording.
Split into: none.

## Statement

For the degree-four even-checkerboard Padua Lebesgue function, put q=(4θ/π,5φ/π), Q=[0,4]×[0,5], and D_a={q∈Q: |q1−a1|+|q2−a2|≤1} for odd-sum integer centers a. Let V_a be the greatest value among the **strict interior local maxima of λ_4 on Q** whose locations lie in D_a; V_a is undefined if that set is empty. The proposed ordering

    V_b≤V_a whenever b−a∈{(±1,±1)},
    c is a closest non-node corner to both a,b,
    and |b−c|>|a−c|

fails. A witness is a=(3,2), b=(2,1), c=(4,5):

    V_b−V_a ≥ 5008831434656004615594354983 /
                    79228162514264337593543950336 > 0.06322.

Distance is Euclidean in mesh coordinates and ties are permitted. The failure is about V, not M_a=sup_{D_a}λ_4. Artificial diamond-boundary maxima are absent from V and are not certified by this claim.

## Definitions and assumptions

The node convention and λ_n are those of PD-T101. Non-node corners for n=4 are C={(0,5),(4,5)}. Coordinates and values are inherited from the accepted complete degree-four certificates PD-T165/PD-T166 (part2 records10/11), with root identifiers from the compressed certificate and enclosures from the global-value JSON. The checker checks their content identities, root grouping and rational inequalities; it does not rerun the original full n4 certification.

## Status by part

Overall status: **PROVED** (development result; independent exact checks PASS; required Claude audit pending). The orchestrator must publish the essential code/evidence/check records with this result before describing its computer-proof record as complete.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| Counterexample to the specified O-Lt ordering | PROVED | Exact rational developer checker plus independent replay and separate rational reconstruction PASS; inherited n4 certificates remain explicit dependencies |

Candidate disposition: **REJECTED: refuted** for the exact O-Lt formulation. The ambiguous original IDEA03, tie-excluding O-L, whole-diamond suprema and amended edge-centreward comparison are not rejected by this statement.

## Negative-result scope

Attempted mechanism: O-Lt, a separately dated tie-inclusive certified-list interpretation of IDEA03.
Parameter range: n=4, the two indicated diamond cells and the indicated corner. No claim about all partitions, all pairings or a whole-diamond comparison.

## Depends on

- PD-T165/166: degree-four complete strict-maxima classification and global-value enclosures in part2.
- Elementary cosine monotonicity on [0,π], Taylor's remainder bound, and the Machin identity π=16 arctan(1/5)−4 arctan(1/239).

## Checks and input identities

Source snapshot `328be35e55143013047ec03a70e9906e82b95353`.

| Input | SHA-256 |
|---|---|
| `topics/padua-proof-attempts-2-20261101/outputs/a5_n4_certificate.json.gz` | `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61` |
| `topics/padua-proof-attempts-2-20261101/outputs/a5_n4_global.json` | `7bc43988a28848037f0b10b4e6c59cadb9dffa772e939175853e3769f7f6003a` |
| `outputs/part3/pairing_screens.json` | `f602acf48d82b91a26db422164836a4529828d027488f9f1b20e58497c8a93c2` |
| `code/part3/pairing_exact_check.py` | `39a701f79f60052272a7af6fadbe021761e3becd33793c1e1746033eb4705098` |

Frozen checker command, from repository root:

```sh
python topics/padua-argmax-alln-20261101/code/part3/pairing_exact_check.py topics/padua-argmax-alln-20261101/outputs/part3/pairing_screens.json --output topics/padua-argmax-alln-20261101/outputs/part3/pairing_exact_check.json
```

Developer result: PASS, 13 roots grouped into six cells, exact positive reversal lower bound as stated. Standard-library checker imports no numerical optimizer, inverse trigonometric function, NumPy or producer module. Independent agent `/root/pairing_check` executed the checker to `outputs/part3/pairing_exact_independent.json` (SHA-256 `e968b360b37ae9d66e876b90c8f273dd5e1b748a0a18b1b74a1ce4bddc1c8fb3`), PASS. Its separate implementation uses24 arctan terms, degree48 cosine Taylor bounds, and enumerates all15 odd cell centers to check all13 root assignments. Its result is `outputs/part3/pairing_independent_reconstruction.json`, PASS. See [independent check](../independent-checks-pairing.md). Neither execution reruns the original full n4 proof. The required cross-family Claude audit remains pending.

## Proof

The complete inherited list has exactly one interior strict maximum (id5) assigned to D_(3,2), and three (ids6,7,11) assigned to D_(2,1). Other maxima are in four different diamond cells. Every root rectangle is converted to a rational outer angular box by checking its endpoints through cosine, rather than trusting numerical arccos.

For example, id5 lies in

    q1∈[7211/2500,28847/10000],
    q2∈[10903/5000,21809/10000],

whose maximal sum |q1−3|+|q2−2| is <1. Analogous strict rational inequalities assign ids6,7,11 to D_(2,1). The checker verifies **all thirteen** assignments, ensuring that no larger listed maximum was omitted from either cell. Each assignment lies strictly inside a unique tile.

The rational angular checks use thirty alternating arctan terms and the next-term bound for a rational π enclosure. The identity follows from tan(4 arctan(1/5))=120/119 and tan(4 arctan(1/5)−arctan(1/239))=1, with that angle in (0,π/2). At a rational endpoint angle t, the degree60 cosine Taylor polynomial has error at most t^62/62!. Cosine decreases on [0,π], so outward physical-coordinate root intervals imply the claimed rational angular boxes. The numeric midpoint is used only to propose boxes in the producer; the checker uses exact rational arithmetic on the proposed boxes.

Taking maxima of the inherited lower and upper value bounds gives

    V_(3,2) ≤ 26836308291084617416026307893 /
                  9903520314283042199192993792,
    V_(2,1) ≥ 219699297763332943943804818127 /
                  79228162514264337593543950336.

Their difference is the stated positive rational. Finally b−a=(−1,−1), squared distances from c are 10 and20, and c is nearest to a and tied for nearest to b. Thus all O-Lt hypotheses hold and its claimed inequality is reversed.

## Sources and scope limits

No 1-D literature theorem is used. The literature INDEX was consulted; original Brutman/Günttner/midpoint proofs remain unread. The witness does not assert that the greatest value on the whole diamond is an interior strict maximum; such an inference would require controlling its artificial boundaries.

## Open items

Required Claude audit and publication of the essential code, input identities and independent checks. Register only the exact O-Lt scope. Original IDEA03 and PD-T099 remain OPEN.

## History

2026-11-01, Codex, parent-assigned gpt-6.1-sol xhigh (runtime metadata not independently exposed). Original unique-nearest O-L grouping had zero eligible n4 comparisons; O-Lt was added as a separately dated formulation before its comparison was executed. The producer then found the exact witness above. No pre-existing criterion was overwritten.

Independent correction: the checker agent noticed that an initially displayed V_b lower endpoint was one 2^−96 unit below the greatest inherited lower endpoint. The display now uses the exact greatest lower endpoint; the computed counterexample and claimed rational margin were already correct. Independent reconstruction and corrected prose checked PASS.
