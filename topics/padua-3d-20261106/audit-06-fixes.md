# Audit 06 — auditor fixes (dated companion note), 2026-11-12

These fixes are made by the auditor under the WORKFLOW rule "Proportionate audit and records", which applies from the third audit round onward. They are committed separately from [audit-06.md](audit-06.md).

The orchestrator (Claude, claude-opus-5-5) applied them directly; none of the edited files is a current hash-pinned acceptance input. No claim statement, status, ID, disposition, proof, code or evidence changed.

| ID | File (location) | Edit |
|---|---|---|
| K1 (H-M1) | paper-note-draft.md:49 | Scope conformed to the canonical `final-d1/sources.md:46`: "for positive weights with all nodes in C … on the cube. Their definition allows nodes anywhere in R³ and real nonzero weights [p1]; the signed-weight and exterior-node cases and their n³/4+O(n²) conjecture remain open." The node definition at p1 was primary-read by the audit-06 subagent. |
| K1 (H-M1) | final-d1/gate.md:42 | "only for positive weights with all nodes in the closed cube and non-effectively; p1 allows nodes in R^d and real nonzero weights, so the signed-weight and exterior-node cases remain OPEN". |
| H-m1 | paper-note-draft.md:32 | "no such rule (positive, with all nodes in C, exact on Π_(2n−1)) with N=N_n exists". |
| H-m2 | paper-note-draft.md:71 | "Theorem A's non-effective result for arbitrary nodes in C". |
| H-m3 | final-d1/README.md:5 | "rule with all nodes in the closed cube has". |
| H-m4 | frontier-dispositions-20261112.md:9 | "a non-effective fixed excess over n³/6 for arbitrary nodes in the closed cube". |
| H-m5 | paper-note-draft.md:73 | δ is defined: "enhanced degree δ≤4 and δ≡0 mod6 (here δ=2n, the minimal nonzero dual l1 norm)". |
| H-m6 | paper-note-draft.md:118 | "Y. Lyubich, *Lower bounds for projective designs, cubature formulas and related isometric embeddings*". The coverage clause now reads "journal metadata not established here". |
| R-m1 | paper-note-draft.md:85 | "than the earlier value5.54 obtained in this work". |
| R-m2 | final-d4/results.md | Dated pointer added: the fd4 prose pins are retired by `response-05-provenance.md`, and current integrity rests on the master manifest. |
| R-m3 | response-05-provenance.md:86 | Receipt-consistent rounding: "`3.10e-14` and `3.62e-13`". |

**Returned to PR preparation:** H-m7, the Belgian-chapter co-author (Cools–Nuyens), the DOI 10.1007/978-3-540-74496-2_1 and the replacement of the full-book mirror link. The audit-06 subagent found these by index search only. The developer should verify them before changing the bibliography.
