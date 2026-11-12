# Audit04 part D — pruning campaign and exact pruned12/pruned16 sets

- Auditor: Claude subagent, Opus 5.5 xhigh (mathematical/computational adversarial audit). Developer: Codex.
- Candidate: `e7c9900ec7dc232d2e117cc72dd47b79c7a0fe26`. Handoff17 read via `git show dafb8c8` (that commit only touches handoffs 16/17). No Git state changes, no repository edits.
- Rules read: AGENTS (workspace head); WORKFLOW severity/fix sections and CLAUDE_ROLES audit section (e7c9900 archive).
- Execution: only in the archive copy `scratchpad/a4-D/src`, outputs in `scratchpad/a4-D/out/`. Python 3.13.18, NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1, no -O.
- Read in full: handoffs 16/17; pruning-summary/brief/certificate/protocol/results/review/artifacts/theory; theory/pruning-exact12, exact16, p1..p5.
- Read in part: gate, next-questions, manifest, LOG 847–895, usable-recipes diff, the relevant functions of pdpr_core/pdpr_certify/pdpr_run, and the five decoded receipts.
- No full IDEAS read. No novelty or priority claim is made or judged here. The P1/P2/P5 negatives were checked only as scoped finite MEASURED statements.

## Verdict

**No BLOCKING and no MAJOR finding.**
- Both PROVED rank claims are confirmed by my own checker, at new primes and in two new bases.
- Every P1–P5 headline number I recomputed reproduces to the reported digits.
- My independent A-path replays reconstruct both payload ID sets exactly.
- 4 MINOR findings (record/wording) and 6 NOTEs.

## 1. Exact rank

Checker: `checker/exact_rank_audit.py`. It imports no repository code.

- **Decoder:** filtered lexicographic product, i3 fastest, equal parities. It checks:
  - full count = ∏⌊m/2+1⌋ + ∏⌈m/2⌉ (637 / 1377);
  - IDs are plain ints, strictly increasing, in range;
  - decoded triples are distinct.
- **Exponents and L:** e = L·i/(2m) is checked to be integral. L = 312 = 2³·3·13 and 544 = 2⁵·17. cos(πi/m) = cos(2πe/L) is checked in floats.
- **Fields:** primes proved by complete trial division. ρ = h^((p−1)/L) with ρ^L = 1 and ρ^(L/q) ≠ 1 for each prime q | L.
- **Bases, both different from producer and reviewer:**
  - closed-form Chebyshev T_a(x_p) = (ρ^{ae} + ρ^{−ae})/2, so no recurrence;
  - reverse-lex monomials.
- **Arithmetic:** exact int64 elimination with p < 2³¹. Each two-residue product is < 2⁶² and is reduced immediately.
- **Minor:** the N pivot rows are rebuilt as a fresh square minor. Its determinant is computed with NumPy int64, and also with pure Python ints for n12.

Command: `python -I checker/exact_rank_audit.py <payload> N M p1 p2`.

| payload | K/N | p | ρ | rank Cheb/mono | det Cheb/mono |
|---|---|---|---|---|---|
| pruned12 (`ddf19d3d…`) | 546/455 | 1249 | 1152 | 455/455 | 276/894 |
| | | 2147482273 | 1854291815 | 455/455 | 1490998059/1601492952 |
| pruned16 (`ef79d609…`) | 1163/969 | 8161 | 1506 | 969/969 | 703/7620 |
| | | 2147468833 | 363867964 | 969/969 | 1984689800/1068165277 |

**Producer minors.** I rebuilt the stored `minor_row_ids` minors in producer column order with my closed-form evaluator. They give det = 106 (mod 313, ρ = 10) and det = 330 (mod 5441, ρ = 4639), exactly as stated. All stated order residues, primalities and p ≡ 1 mod L checks are correct (313/10, 937/15, 5441/4639, 6529).

**Reduction (pruning-certificate.md:62–144) is correct.**
- Z[ζ] ≅ Z[t]/(Φ_L).
- Φ_L(ρ) = 0 mod p follows from ∏_{d|L} Φ_d = t^L − 1 together with ρ having exact order L.
- Inverting 2 extends the map to R = Z[ζ, 1/2]. Determinants commute with the map and the entries are real.
- Hence E has full column rank and LS is unique for any positive weights.
- Since M > N, nothing is claimed about interpolation (exact12:19–23, exact16:18–22).

**int64 safety.**
- `field` enforces p < 2³⁰ before trial division.
- The recurrence reduces the product before doubling.
- Basis products are reduced pairwise.
- Elimination uses one f·row outer product with no dot accumulation.
- The reviewer's bounds 877032 / 42621312 equal (p−1)² + (p−1).

**Scope.** The rank proof is never offered as conditioning or quality: exact12:200–209, summary:26–28, artifacts:34–37 and 150–151, usable-recipes:154. The binary64 hash link is labelled MEASURED. My reconstructed nodes reproduce `d02960d3…` and `2709ac59…`.

Extra check, not independent: the producer `verify` run in the archive copy gives rank 455/det 106 and rank 969/det 330, hash-link True.

## 2. Construction replay

`checker/apath_audit.py` refits from scratch by SVD at every step.
- Score ‖C_i‖²/(1−h_i), admissible when 1−h_i > 1e-10.
- Ties within 1e-12·max(1,|best|) go to the smallest canonical index.

| replay | result | smallest relative score gap outside the tie band |
|---|---|---|
| 637→546 | exactly the payload IDs | 2.4e-7 |
| 1377→1163 | exactly the payload IDs | 1.3e-8 |

The largest tie set has 2 members. The IDs are therefore insensitive to the producer's QR-downdate arithmetic.

## 3. Measured claims P1–P5

Scripts:
- `measure_audit.py`: physical OLS via SVD map in the orthonormal product-Chebyshev basis; heap-greedy integer repeats checked by a KKT certificate; 41³ mesh, 2×2048 random clouds and 12 (n12) or 8 (n16) L-BFGS-B searches, all lower values.
- `p2p5_audit.py`, `n8_audit.py`, `p1_prefix_audit.py`, `u2_audit.py`: every candidate is a fresh fit, with no update formulas.

| claim | auditor recomputation | reported |
|---|---|---|
| P3 n12 A546 | trace 1.0595066, risk@B637 0.9310998, searched 35.460768 | match |
| rQR546 | 1.3303608 / 1.1620764 / 41.396784 | match |
| full 637 | 0.6961037 / 10.592580 | match |
| stored U2 | 1.6170865 / 1.1727064 / 26.007323 | match |
| n8 A198 | risk 0.905551867971524, mesh41 20.391846 | match (raw 0.9055518679715243) |
| n8 rQR198 | 1.0306963 / 25.230215 | match |
| n8 A182/A165 | — | match |
| P4 A1163 | 1.0864370 / 0.9480039 / 40.885058 | match |
| rQR1163 | 1.3583985 / 1.1858454 / 61.044587 | match |
| full 1377 | 0.6888394 / 12.740562 | match |
| P2 n6 | 112/112 noise-feasible, 0 training-feasible; min training ratio 1.286955794542 (row 69, risk 1.016871257) | identical |
| P2 n8 | 225/225 noise-feasible, 0 training-feasible; min training ratio 1.444398676589 (row 61, risk 1.008680912) | identical |
| P2 best-risk rows | 1.010870691 / 1.005887852 | identical |
| P5 | 48/100 pairs, 16/25 fixed, all admissible; training-feasible 0/0, noise-feasible 45/100; best (37,69) 1.405160305, (57,157) 1.438422141 | identical |
| P1 A prefixes | 44/112/223 at n4/6/8; failures driven by amplification (D rule not replayed) | match |

**Gate applications** (decoded receipts against the protocol):
- **P1 fails:** savings ≤ 1.33% < 10%.
- **P2 fails:** zero feasible deletions.
- **P3 passes:**
  - risk/norm ratios 0.8786/0.8061 at n8 and 0.8012/0.8566 at n12, all ≤ 0.95;
  - savings 12% and 14.29%; prefix CPU 0.069 s and 1.196 s;
  - not dominated: U2 has the better norm but the worse risk.
- **P4 passes:** ratios 0.7994/0.6698; 15.54% saving; 14.23 s prefix CPU. All four 969-site controls are worse on both metrics, while using 194 fewer sites.
- **P5 fails at both degrees.**
- The quoted percentages (33.76, 234.77, 36.35, 20.60, 20.06, 33.02, 43.39, 42.98, 40.19, 48.97, 25.70, 5.29/2.44, 3.86/1.74) are arithmetically consistent.

**Chronology (UTC).** Each protocol commit precedes its run, and each receipt's `protocol_commit` matches.

| round | protocol | run window | result commit |
|---|---|---|---|
| P1 | a05fa01 09:09 | ~09:12 | ccab7af 09:18 |
| P2 | 99a9f47 09:20, seed fix 143b5d0 09:26:25 | 09:26:43–47 | d57b2b1 09:32 |
| P3 | 650b49d 09:37 | 09:40:57–09:41:36 | 5623097 09:46 |
| P4 | 55a6a11 09:52:00 | 09:54–09:56 | e761a12 10:02 |
| P5 | 0e26f3e 10:11 | 10:13 | e7c9900 10:23 |

- The protocol is append-only apart from the one-line P2 seed swap (1020/1030 → 1520/1530), made before execution.
- Executed-source snapshot hashes equal the committed bytes.
- Push times were not verifiable.

**Noise normalization.** All five quantities are distinct and were each computed.

| map | tr(CCᵀ) | M·tr | M·tr/B | optimal integer @B (repeats) | (Σ‖C_i‖)²/B |
|---|---|---|---|---|---|
| A546 | 1.059507 | 578.491 | 0.908149 | **0.931100** (455×1, 91×2) | 0.888973 |
| rQR546 | 1.330361 | 726.377 | 1.140309 | 1.162076 | 1.109350 |
| U2 455 | 1.617087 | 735.774 | 1.155062 | 1.172706 (273×1, 182×2) | 1.111351 |
| A1163 | 1.086437 | 1263.53 | 0.917593 | **0.948004** (949×1, 214×2) | 0.900955 |

The docs use the integer value as "fixed-B risk" and never substitute M·tr/B for it (theory:261–267). Haar appears only as a labelled separate map.

**Budget.**
- Pruning rounds 5/15 (summary:4, LOG:893). Old counts 4/7/5 unchanged.
- Engineering, certificate and review runs count 0.
- CPU used: 17.1/900, 4.15/600, 38.4/900, 152.3/900, 3.95/120.
- "Ceiling, not quota" is stated repeatedly.
- Producer manifest `--verify` (producer code, archive copy): PASS, 310 artifacts / 1872829 B; master 16341 B < 16384.

## 4. Findings

**MINOR-1. Stale round counter.** pruning-results.md:10–11 says "current campaign count after P4 below is 4/15"; the actual count is 5/15 (results:414). Fix text:

> "P1 consumes **1 research round** (root publishes count boundaries); the completed campaign count after P5 below is 5/15."

**MINOR-2. Checker hash does not match the linked file.** theory/pruning-exact12.md:76–80 links `../code/pdpr_certify.py` as 15414 B / `0b4a815f…`. At e7c9900 that file is 16024 B / `ab3b092c…`; the old bytes are at e761a12. The replay command at :186 runs the current file. Only artifacts:131–140 explains this. Fix text, after the table:

> "Producer row = historical degree-12 creator revision at e761a12bcc7acfbf47dc6db77592854211931df5; the current shared checker is 16024 bytes, SHA256 `ab3b092cbf29d97ec456f6891cfc109d0f8dbe7652516ea961b301318f230241` ([compatibility](../pruning-artifacts.md#degree16-essential-artifact-and-backward-compatibility))."

**MINOR-3. User-facing noise numbers assume repeats the recipe does not use.**
- summary:32–38 and usable-recipes:134–135 quote only the fixed-B risk, which presumes 637/1377 observations with 91/214 sites measured twice.
- The recipe asks for one observation per site. At one observation per site the documented traces are 1.0595 / 1.3304 / 0.6961 (A / restricted QR / full, degree 12) and 1.0864 / 1.3584 / 0.6888 (degree 16) (results:209, 275).

Fix text, appended to summary:49:

> "With one observation per site the documented unit-noise traces are 1.0595 (546), 1.3304 (restricted QR 546) and 0.6961 (full 637) at degree12, and 1.0864, 1.3584 and 0.6888 at degree16; the fixed-B values above repeat 91/214 sites twice."

**MINOR-4. Delivery chronology not recorded.**
- The n12 build ran at 09:48:29 UTC (artifacts:84). That is before both the certificate reduction and the P4 appendix were committed (55a6a11, 09:52:00).
- protocol:378–379 says "degree16 transfer and then artifact"; protocol:473–476 says "If P4 passes … deliver n12/n16"; exact12:69–70 calls the reduction "already written, frozen".
- No scientific impact: the export is verification only, and the IDs are fixed and independently reproduced (§2).

Fix text, a dated note after artifacts:76:

> "Chronology: the degree12 build (09:48:29 UTC) followed P3's published pass 5623097 but preceded the commit of pruning-certificate.md and the P4 appendix (55a6a11, 09:52:00 UTC); the 'If P4 passes…deliver' condition therefore governed only the degree16 export in practice. IDs, rank and measurements are unaffected."

**NOTEs**

1. The P2 seed change was an in-place edit of a published appendix, not a dated correction like P3's. It is disclosed (LOG:862, review:63–64 and 122), was made pre-execution, and touched assessment seeds only.
2. The P4/P5 drivers were first committed together with their results. Snapshot hashes match, and the protocol required only the appendix to be published first.
3. Restricted QR beyond N:
   - geqp3 makes only N pivot choices on the N×M matrix Aᵀ, so sites N+1..k come from leftover swap order (n12 tail starts 218, 357, 316, …). This is disclosed at protocol:110–111.
   - The control is not a strawman. Auditor-only diagnostic with 30 uniform random 546-subsets: risk median 1.275 (min 1.208), mesh41 amplification median 80.0 (min 60.5). That is worse than restricted QR (1.162/41.0), which in turn is worse than A546 (0.931/35.4).
4. The payload schema `pdpr-canonical-parity-v1` and its field names differ from the placeholder at certificate.md:152. The certificate allows the implementation to choose (:149), but the difference is not stated.
5. "45/100 passing noise" (p5-boundary:17) means 45/48 at n6 and 100/100 at n8. The table makes this clear, but the sentence is easy to misread.
6. My independent searches converge to the same local maxima (35.460768, 41.396784, 40.885058, 61.044587). This corroborates the values as lower values only; it bounds no supremum.

## 5. Not tested

- globalQR, localdet, modern U2/fineDetC4 (raw-only inputs).
- The 12-target and sigma tables, and pointwise-variance maxima.
- P1 D/random/lex paths; P5 random-pair and A/D controls.
- Producer-seeded 28-start schedules and n8 searches.
- Timings; the reviewer's 937/6529 minors (I used other primes).
- Raw /tmp provenance and push times.

Floating matches evidence only the finite statements. The exact claims rest on the cited reduction plus my integer arithmetic: nonzero minors at 4 primes × 2 bases, and the producer minors replayed.

## Checker identities (`scratchpad/a4-D/checker/`, sha256)

- exact_rank_audit.py fb21a95a825a7c9d5fed1155763e18233c270699825aad2c91e39892290dede8
- measure_audit.py d57aae2f6fad242780cf4593acf7624e7f52c4cbe1e2e8fce2a18a6dfd8081e5
- apath_audit.py d5085667c0f1d4b606c9e88c996e864bb4eb487a34cec1701222b6afb5bcc6c3
- p2p5_audit.py ef92b7772a18e942ec084f76e1c86d7a44f1c09b50e97849710e820fdc861aec
- n8_audit.py 7972e790e1515b0a18e12be39bd49848e04d7953eba64b6a3c8df6ed97efd2f4
- p1_prefix_audit.py 6ae191ad87c2e31b564cc39452e98e34caf06e00b351e340a2034cabdb208123
- u2_audit.py ce3f69ddf7611b2544a54964d7e389d03fb049ac6b962534b97e3c0a12a7919d
- random_control_audit.py d9dbb011aa5f5397fd9179c7de857686e1d5edf99c8c64ab48ca40f96de18d98

Outputs in `scratchpad/a4-D/out/`: exact-rank-n12/n16.json, exact12/16.log, measure12/16.json, apath12/16.json, p2p5.json, n8.json, p1prefix.json, random12.json, producer-verify12/16.json, and decoded/.
