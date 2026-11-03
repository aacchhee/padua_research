# Supplementary independent check — exact finite O-Lt obstruction

Rules/source snapshot: `328be35e55143013047ec03a70e9906e82b95353`. Date: 2026-11-01. Reviewer: Codex `/root/pairing_check`, configured by the parent as `gpt-6-astra`, high effort (spawn settings reported by the parent; runtime model metadata is not separately exposed). Role: independent supplementary mathematical checker, not the required Claude auditor. No Git, shared registry, developer source, or handoff modifications were performed.

## Verdict and scope

**PASS at the exact finite O-Lt scope, after one corrected arithmetic display.** The inherited strict interior maxima in the two specified diamond cells give a rationally certified reversal at n=4. This supplies the requested actual independent execution and a separately implemented rational reconstruction. Required Claude audit remains pending; integration must retain the checker and small evidence records.

This check covers the existing candidate's precise finite formulation, its coordinate assignment, its maximum-of-list value comparison, and its scope boundaries. It makes no priority, novelty, or new general mechanism claim, and does not judge the candidate-generation campaign or the fallback P3–P5 mechanism. Accordingly the complete `state/IDEAS.md` was not reread under the workflow's no-novelty-content exception. Read: rules, WORKFLOW, Codex role, handoff02, topic ideas/gate, fallback candidate records, P3–P5/pairing attempt, N01, measured06 for scope separation, inherited PD-T165/166 theory, and relevant original n4 checker/global-producer code. Numerical O-R/E-C results in measured06 were not independently rerun or approved by this check.

## Finding and disposition

**F1 — exact displayed subtraction inconsistent by 2^-96 (resolved).** Initial N01 displayed a valid but slightly smaller lower bound
`109849648881666471971902409063/39614081257132168796771975168`
for V_b, then said that subtracting the displayed upper bound for V_a yielded the sharper stated reversal. That displayed subtraction was smaller by one unit of `1/79228162514264337593543950336`. The developer replaced the displayed V_b lower bound by the actual maximum inherited lower endpoint,
`219699297763332943943804818127/79228162514264337593543950336`.
The revised proof at SHA-256 `c04cc91fb8e22e051b1b05d5b9f37a32196b483fb2ec895025eae45d3d72130c` was rechecked. The final exact reversal and the qualitative counterexample are unchanged. No unresolved mathematical finding remains in the stated scope.

## Independent executions actually performed

Python 3.12.14, standard library, exact `fractions.Fraction` arithmetic. From repository root:

```sh
python topics/padua-argmax-alln-20261101/code/part3/pairing_exact_check.py topics/padua-argmax-alln-20261101/outputs/part3/pairing_screens.json --output topics/padua-argmax-alln-20261101/outputs/part3/pairing_exact_independent.json
python topics/padua-argmax-alln-20261101/code/part3/pairing_independent_reconstruction.py
```

Both executions exited 0 and reported PASS. First execution took approximately9.1 seconds and wrote a distinct independent receipt. Second took approximately8.7 seconds and wrote `outputs/part3/pairing_independent_reconstruction.json`. The second script imports no developer module; it uses24 arctan terms and a degree48 cosine Taylor polynomial, independently enumerates all15 odd-sum centers in the n4 rectangle, and verifies membership in one cell plus strict exclusion from all other cells for every root box. It does not recompute the inherited root or value certificates.

## Mathematical checks

The inherited nodes have j+k even. Thus in mesh coordinates Q=[0,4]×[0,5], the two non-node corners are exactly (0,5),(4,5). Odd-sum integer centers with ℓ1 radius1 form a diamond tiling up to boundaries. Distinct centers have ℓ1 distance at least2, so strict membership cannot overlap.

The accepted physical root intervals bound x=cos(πq1/4), y=cos(πq2/5). Each proposed lower angular endpoint is checked by a cosine lower enclosure lying above the physical upper endpoint; each proposed upper angular endpoint is checked by a cosine upper enclosure lying below the physical lower endpoint. The orientation is therefore correct because cosine decreases on [0,π]. The second implementation explicitly asserts that its rational endpoint arguments lie in that interval. The Machin identity and alternating arctan remainder give the outward π enclosure. The cosine Taylor remainder is valid because the next odd coefficient is zero and every derivative of cosine/sine has absolute value≤1. Numerical inverse cosine is not trusted.

All13 root rectangles lie strictly inside their assigned cells. The smallest verified margin from an assigned diamond boundary is2047/10000. Full grouping:

| Cell | Root IDs |
|---|---|
| (3,4) | 0 |
| (2,3) | 1,2,3,4,8,9 |
| (3,2) | 5 |
| (2,1) | 6,7,11 |
| (1,4) | 10 |
| (1,2) | 12 |

The original inherited checker verifies strict cardinal signs and a negative definite Hessian for each accepted root, so its signed-polynomial interval is an enclosure of λ, not the wrong signed branch. The global checker verifies that its provided value interval contains the recomputed root-value interval, with lower/upper endpoints in the conventional order. Those accepted facts are dependencies here, not new executions.

For a=(3,2), b=(2,1), c=(4,5), the displacement is (-1,-1). Squared distances from c are10 and20; from the other corner they are18 and20. Hence c is uniquely nearest to a and tied for nearest to b, and the step moves away from c. Taking the maximum of lower endpoints in b and the maximum of upper endpoints in a is valid for V_b−V_a, and yields exactly

`5008831434656004615594354983/79228162514264337593543950336 > 3161/50000 = 0.06322`.

The separate reconstruction finds zero eligible comparisons for the unique-nearest O-L rule and six for O-Lt. Thus this witness cannot refute O-L. The original IDEA03 wording left the partition, corner rule, and pairing undefined. O-Lt is an informed followup after initial grouping/value inspection, not a blind preregistration. Neither this exact comparison nor completeness of the local-maxima list bounds suprema on artificial diamond boundaries. Whole-diamond O-R, arbitrary alternative pairings, E-C/E-P, and all-degree PD-T099 remain outside the negative conclusion.

## Content identities and inherited-proof boundary

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `code/part3/pairing_exact_check.py` | 3290 | `39a701f79f60052272a7af6fadbe021761e3becd33793c1e1746033eb4705098` |
| `outputs/part3/pairing_screens.json` | 106627 | `f602acf48d82b91a26db422164836a4529828d027488f9f1b20e58497c8a93c2` |
| `outputs/part3/pairing_exact_independent.json` | 503 | `e968b360b37ae9d66e876b90c8f273dd5e1b748a0a18b1b74a1ce4bddc1c8fb3` |
| `code/part3/pairing_independent_reconstruction.py` | 3310 | `cc3edb6dd23279ba623ab891de2dac0b7b65df6467322998dc8622b41a51a83b` |
| `outputs/part3/pairing_independent_reconstruction.json` | 840 | `0b12bca1b3f005e393a314c921116439abb5a53608d58cbed890d9a0271b601d` |

Inherited artifacts under `topics/padua-proof-attempts-2-20261101/outputs/` are the accepted n4 compressed certificate SHA-256 `14a69a131b3c20416fd5521bd971efdadd4e3741f70546d0fc5f0d9f25a2cf61` and global value JSON SHA-256 `7bc43988a28848037f0b10b4e6c59cadb9dffa772e939175853e3769f7f6003a`. Their hashes match the accepted PD-T165/166 theory records and the supplied evidence. **The full original n4 proof was not replayed here.** Completeness, root existence/strict maximality, and value enclosures are inherited accepted dependencies. The new verified inference is only angular cell membership plus finite ordering. The supplementary receipt must not be described as an independent rerun of the complete n4 certificate or as completion of the required Claude audit.

## Final developer-record impact check

After the executions and F1 correction, the developer updated N01 to scoped PROVED, retaining the inherited dependency and required-Claude-audit limitations. Reviewed final N01 SHA-256 `b5e01d3992ceef524570da94f379d995e9bf71a29e7360e720a507be94b65a60`. Its corrected rational bound and mathematical statement are unchanged from the checked revision. The status update and links accurately reflect this supplementary check. Final fallback candidate record SHA-256 `94a29a32ef1a9035c141326f81b2e679745b6ae2bc2cc7c7eb4b85f9b42572b2`; attempt SHA-256 `1a21df14bd70482a8efb4eced115df47ede6622f1ba6552e91c6cac6b0fb4176`. Broad candidate novelty, measured screen reliability, and P3–P5 development remain outside this bounded verdict.

The parent authorized relocating the independent reconstruction script from the initially assigned output directory to `code/part3/`. Source bytes and SHA-256 are unchanged; the relative repository-root resolution remains correct. The command above was executed again after relocation and returned PASS, with the same reconstruction JSON bytes and hash.
