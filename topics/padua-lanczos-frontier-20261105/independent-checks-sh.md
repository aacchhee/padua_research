# Independent adversarial check of SH_n

Date: 2026-11-05. Reviewer: Codex subagent `/root/sh_adversarial`, separate from developer `/root/l1_l2`. Assigned model/effort: gpt-6-astra xhigh; runtime model metadata is not independently exposed. The allocation is justified by the proposed all-degree structural mechanism: a final-degree high-mode normal witness and exact cancellation in the mirror rule. This is a supplementary independent Codex mathematical check; the required later Claude scientific/protocol audit remains separate.

## Verdict and immutable target

**ACCEPTED within the stated all-degree, first-order aggregate-source span-capacity scope. No unresolved mathematical finding at the frozen proof hash.** Acceptance is of the analytic argument below and its declared quantifiers, not of any larger L1, G1, full-scalar, IEEE, closure, or priority claim. No developer proof was edited during this check.

| Input | Pin |
|---|---|
| Integration/rules-read head | `79c3d6a211325eca6e8311b3ae03187c100a1d8a` |
| Earlier unchanged-rules head | `0e493be7f9883e00e6260cf6b081c607a230177f` |
| Main input, supplied by root | `21dbfc90257b952d8923f6d01739d12aa8d6e0a1` |
| Proof | [theory/l1-01-sheared-U-aggregate-separation.md](theory/l1-01-sheared-U-aggregate-separation.md) |
| Proof SHA256, checked before and after the computations | `9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d` |

The proof was explicitly frozen by its developer. Its acceptance applies to those bytes; later mathematical changes require impact review. The developer's statement that no experiments were run describes the development of that analytic record. The separately executed reviewer checks recorded here do not turn it into a computer-assisted proof.

## Coverage and predecessor discipline

The reviewer read the complete `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, current `handoffs/03-work.md`, `LOG.md`, `gates.md`, and `report.md`. The complete 955-line `state/IDEAS.md`, including every obstruction/disposition table and historical correction, was read in bounded ranges. This coverage was performed by this reviewer; earlier workers' completed gates were not substituted for reading.

Saved work read in full: this topic's `attempts/L1.md` and `ideas-l1-l2.md`; the old `topics/padua-lanczos-drift-20261101/directions/E2.md` and `ideas-e1.md`; and `topics/bivariate-lanczos-20261031/directions/L1/candidates.md`, including the IDEA130–144 history. Truncated combined reads were recovered with narrower reads. The complete SH proof and `templates/THEORY.md` were also read.

Relevant full predecessor records read in `tracks/bivariate-lanczos/theory/`:

| Record | File |
|---|---|
| PD-T029 | `window-coefficient-pattern-exact.md` |
| PD-T033 | `product-measure-propagator-factorization.md` |
| PD-T035 | `loss-regimes-node-propagator-measured.md` |
| PD-T036 | `window-recurrence-row-selection-of-jacobi-pencil.md` |
| PD-T038 | `near-product-transfer-perturbation-bound.md` |
| PD-T039 | `moment-matching-product-factorization-checkerboards.md` |
| PD-T041 | `exact-certificate-propagator-growth-triangle.md` |
| PD-T042 | `first-order-coefficient-channel-gains-product-type.md` |
| PD-T043 | `closed-loop-dot-product-rounding-carries-coefficient-channel.md` |
| PD-T044 | `product-measure-computed-propagator-transfer-conditional.md` |
| PD-T053 | `reference-free-span-drift-lower-bound.md` |
| PD-T054 | `condition-C-staircase-selections-acyclic-sections.md` |
| PD-T055 | `bj-universal-reorthogonalization-obstruction-open.md` |
| PD-T136 | `drift-codex-e1-01-span-derivative.md` |
| PD-T137 | `drift-codex-e1-02-rational-span-bounds.md` |
| PD-N009 | `r04-failed-scaling-and-predictor-hypotheses.md` |
| PD-N013 | `reorthogonalization-does-not-restore-graded-spaces.md` |
| PD-N015 | `one-relation-selections-do-not-keep-spans-near-Sn.md` |

Literature coverage consisted of the index's headings, metadata and scope prose, complete relevant rows LIT114 and LIT241–257, and the full `literature/records/barrio-pena-sauer-2010.md` record. It did not include every unrelated index entry or primary PDFs. A case-insensitive mechanism search for shear, latent product, same-degree chain/factor, normal quotient, and aggregate span was executed across these theory/saved-L1 locations and the BPS record. Relevant prior shear probes and the normal-quotient/Gram distinctions were inspected. No absence claim or historical-priority clearance follows from this bounded search.

Read-input SHA256 pins:

```text
AGENTS.md             c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b
agents/WORKFLOW.md     423e1bc005d61aaaec38a9d38660f48644618850590c53110b595898a41bde21
agents/codex/CODEX.md  28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b
state/IDEAS.md        908ffa8bc71ec21dc74f7cf7bd626c16d3fd4af65fbbfe313432bec59193f01c
literature/INDEX.md   c5342f00f6a4604076d1f89b2a2b6003e8374460548b7ca6e7685ac6c8858a16
```

## Independent analytic reconstruction

The following reasoning was checked independently, with special attention to whether a raw recurrence claim survives final projection onto the full degree-n space.

1. **Weights, DST and complete sample space.** For m=n+2 the sine vectors with frequencies 1 through m are eigenvectors of the symmetric path matrix with distinct eigenvalues. Their squared norms are (m+1)/2 by the finite geometric sum. Consequently the stated positive weights sum to one and make U_0 through U_(m−1) exactly orthonormal. The tensor basis has m² elements and spans all of R^M. The witness U_(n+1)(s) is within this range because n+1=m−1; it is not an aliased or missing grid mode.

2. **Physical nonproductness, dimensions and injectivity.** The leading part of U_r(x)U_j(y−2x) is 2^(r+j)x^r(y−2x)^j. Its only other monomials at that total degree have smaller y exponent, matching the prescribed order. Thus the orthonormal represented polynomials give a triangular basis of Pi_d through d=n+1, proving evaluation injectivity there. Distinct nodes follow from the invertible shear. M−N_n=(n+2)(n+3)/2>0. In the probability measure Cov(X,Y)=Cov(S,2S+T)=1/2, ruling out a product measure in the physical coordinates. The construction is explicitly a latent affine product; it does not establish a nonproduct result invariant under all affine changes of coordinates. Its oversampling ratio tends to two, so it is not an M≫N assertion.

3. **Exact creators and raw-product scales.** In the orthonormal tensor basis X shifts the first index with coefficients 1/2; Y shifts that index with coefficients 1 and the second with coefficients 1/2. Each chosen target has coefficient beta=1/2 and every other nonzero term precedes it, including the same-degree term (r+1,j−1) for a Y creator. Parents have degree at most n−1, so there is no upper-grid boundary case. Squaring these orthogonal expansions gives sigma_X²=(1+1[a≥1])/4 and sigma_Y²=1+1[a≥1]+(1+1[b≥1])/4. The BJ source at (n,0) has sigma²=1/2 because n≥2. Mirror Y parents have a=0, so all mirror scales are positive and at most sqrt(3/2). Each rule uses its own scales, not another rule's source norm.

4. **Monic conversion.** The monic column is b_h=2^(−d)q_h and has squared norm 4^(−d). A raw monic source is 2^(−(d−1))f_h, exactly the factor in its raw-product scale; the relative source budget is preserved. The frozen monic response is 2^(−d)V_h, and its output Gram factor is 2^d, giving the same normal output. This is the claimed first-order gauge conversion, not a claim that entire perturbed nonlinear runs are fixed rescalings.

5. **Differentiated coefficient and normalization channels.** Direct differentiation of beta_h q_h=A_h q_parent−sum_l c_hl q_l gives the frozen response plus the terms −sum_l dot(c_hl)q_l−dot(beta_h)q_h. An induction in the actual column order proves dot(q_h)−V_h lies in S_(deg h): the parent has one smaller degree, multiplication raises degree by at most one, and preceding columns have degree at most deg h. Same-degree predecessors cause no induction cycle. Hence these terms vanish only after projection by I−P_n. This is a normal-quotient argument; it does not assert that coefficient or normalization derivatives vanish in Gram or coefficient observables.

6. **Projector observable and quantifiers.** Positive residual norms at the exact run imply a smooth perturbed recursion for each fixed n and source vector f in a neighborhood of zero. Exact orthonormality gives ||(I−P_n)P_n(epsilon)||_2=||(I−P_n)Q_n(epsilon)||_2, so its derivative norm equals the normal frozen-output matrix norm. The theorem takes the limit at fixed (n,f), then a supremum over the finite-dimensional source sphere. No exchange of supremum and limit or degree-uniform remainder estimate is required. Arbitrary aggregate vectors in R^M are allowed by the stated model.

7. **BJ witness remains normal to full Pi_n.** With e=q_(n+1,0) and the single source f_(n,0)=e/sqrt(2), the source norm is one and all earlier-degree responses vanish. The same-degree chain is V_(n−j,j)=2(−2)^j f_(n,0). Every output is a multiple of the same unit vector e orthogonal to all of S_n. Thus final projection preserves the complete rank-one output, whose squared spectral norm is 2(4^(n+1)−1)/3. This establishes a span lower bound rather than merely a large unprojected inverse entry.

8. **Mirror cancellation and absent indices.** The X recurrence gives V_(1,j−1)=2S V_(0,j−1)+2f_(1,j−1). Inserting this in the Y boundary recurrence cancels 4S and leaves 2T, with the forcing −4f_(1,j−1). Solving the two one-variable recurrences gives exactly the displayed U-polynomial formulas. Negative indices mean zero; j=0 has an empty boundary sum. The source (1,n−1) used for output (0,n) is earlier within degree n. No future source or source at (0,0) is used. A source f_(1,c) occurs in the boundary sum only when c≤j−1, and in the direct sum only when c=j, so the individual coefficient bound does not miss a duplicated term.

9. **All-source mirror norm estimate.** The diagonal U multipliers have norm at most a+1. Thus each source-to-output coefficient has norm at most C=4(n+1)². There are exactly H=N_n−1 source positions and H nonconstant output columns. Writing f_h=sigma_h u_h gives sum||u_h||²=1, each output norm at most C sqrt(3H/2), and total Frobenius norm at most C sqrt(3/2)H=2sqrt(6)(n+1)²H. The spectral normal output is no larger. No random-source or independence premise is involved. A last-column normal source proves mirror capacity is strictly positive, making the ratio valid.

These steps prove the stated lower and upper bounds for every n≥2. They imply exponential separation up to a polynomial factor asymptotically. They do not claim matching exact rates or establish strict BJ-versus-mirror capacity ordering at every small degree.

## Separate exact finite checks actually executed

The reviewer wrote [code/sh_independent.py](code/sh_independent.py) independently without importing developer mathematical code. The finite calculations use Python arbitrary-precision integers in NumPy object arrays and SymPy rational polynomials. In the orthogonal tensor basis, 2S and 2T are path adjacency operators; this is orthogonally equivalent to the weighted node basis by the analytic DST identity. Thus no floating point evaluation of trigonometric nodes is used in these checks.

The executed command exited successfully:

```sh
python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output topics/padua-lanczos-frontier-20261105/evidence/sh-independent.json
```

Environment: Python 3.12.14, NumPy 2.3.5, SymPy 1.14.0. The receipt is [evidence/sh-independent.json](evidence/sh-independent.json), status `PASS_SUPPLEMENTAL_EXACT_FINITE_CHECKS`.

For each rule and n=2,3,4, the code differentiates full all-prior projection and positive normalization directly, keeping every projection-coefficient derivative. It separately assembles the frozen recurrence and verifies its normal image equals the full derivative for every source coordinate direction. It also verifies the degree bound on their difference, the orthonormal tangent identity, and the vanishing final normal image of sources lying in their own degree spaces. The BJ high-mode witness is checked as a complete column matrix. The mirror closed form is compared with the frozen recurrence for every source direction, then its relative-source Hilbert–Schmidt bound is checked against the theorem's upper bound. The Hilbert–Schmidt quantity here bounds the source-to-output-Frobenius map and is not reported as the spectral-output capacity itself.

| n | M | N_n | Source coordinate directions per rule | BJ witness gain squared | Mirror relative-source Hilbert–Schmidt squared | Stated mirror upper squared |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 16 | 6 | 80 | 42 | 515 | 48,600 |
| 3 | 25 | 10 | 225 | 170 | 2,442 | 497,664 |
| 4 | 36 | 15 | 504 | 682 | 8,461 | 2,940,000 |

The six Jacobian cases cover 1,618 source coordinate directions in total; this is an exhaustive coordinate-basis check at these degrees, with no random seed. Separate symbolic physical-polynomial reduction checked all 88 creator identities through degree 8 for the two rules, including triangular coefficients, pivots, raw-product scales, and monic factors.

| Artifact | SHA256 |
|---|---|
| `code/sh_independent.py` | `3d996f0f85f006350f5a29af72fd1cf26c25c8894b18db1cf451444f908230b8` |
| `evidence/sh-independent.json` | `776b97a5e213c0125f49bac2355bc6f4e48dd628b4c21d31cf7a9adc2ec6cbbd` |

These are supplemental finite consistency checks, with no finite reduction of the all-degree claim. They do not establish the theorem for untested degrees, and do not replace the analytic reconstruction. No nonlinear numerical trajectory, actual IEEE run, scalar-operation realization, malformed-control suite, or computer-assisted all-degree proof was executed or claimed.

## Scope and remaining handoff

The predecessor obstructions remain respected: physical product-factorization hypotheses of PD-T033/039 are not silently applied to Y=2S+T; the upper perturbation result PD-T038 supplies no missing lower bound; finite raw growth in PD-T041 is not promoted into projected growth; Gram/coefficient conclusions in PD-T042/043 are not conflated with span; PD-T053's closure-to-drift implication is not reversed; and PD-T054's acyclic exact selection criterion is not treated as a stability theorem. The aggregate-source normal-quotient mechanism is proved in the present weighted setting rather than imported from PD-T136 without checking its conventions.

No scientific dependency on the G1 experiment or finite L2 predicate is needed. G1's frozen cases/thresholds remain separate. Original L1's broader target and PD-T055's universal reorthogonalization/closure target remain OPEN to the extent stated in their own records. The free aggregate adversarial source does not establish scalar realizability, deterministic IEEE activation, every-error behavior, every-rule behavior, or a degree-uniform finite-epsilon regime.

The required later Claude audit must still examine scientific/protocol readiness, including the retained original pre-gate timing deviation and the scope of the novelty review. This supplementary mathematical acceptance does not clear that deviation or confer historical novelty. Root owns registry allocation, evidence manifest/integration, Git operations, and final handoff. The reviewer changed only the three owned SH review/check artifacts and performed no Git mutation.

## Metadata-only impact review — 2026-11-05

At root's request, this reviewer checked the subsequent SH record with whole-file SHA256 `f27a22c4c6f13d03710750f52eef4dc9bac31f27bd009beaa536866fbbe24d9f`. **The existing scoped mathematical acceptance extends to this metadata-only update.** The original audited input remains `9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d`; it is not retroactively replaced in the executed-check receipt or checker.

The reviewer inspected the revised status, verification addendum, open-item wording and history. Reversing only these metadata changes in memory, using the original audited wording retained in the review record, reproduced the complete original input SHA256 exactly. Direct comparison also confirmed that all seven named mathematical sections—Statement, Definitions, Assumptions, Depends on, Sources, Proof or evidence, and Scope—are byte-identical. This establishes the update's bounded impact independently of the author's reported concatenated-section digest `13325943c81b8f21760a2ed79f77ddf442bdf42609007aa108f4e4589bb7ac05`.

The revised metadata accurately distinguishes the developer's analytic proof from this reviewer's separate finite executions and retains the later Claude audit and original timing-deviation disposition. No mathematical computation was rerun, no checker or receipt was changed, and no Git mutation was performed. The pinned checker intentionally still requires the original audited proof bytes; running it against the revised whole file would fail its input-hash guard unless that original input were supplied. This metadata review does not claim a fresh execution against the revised file.

## Current-checker packaging and separate rerun — 2026-11-05

After that metadata-only review, root requested a bounded packaging repair so the current repository's checker could run against its current theorem. This subsequent step supersedes the preceding paragraph's description of the active checker guard. Root authorized changing the accepted proof hash and the recorded invocation metadata, preserving the scientific calculations and the original receipt.

The checker now requires accepted theorem SHA256 `f27a22c4c6f13d03710750f52eef4dc9bac31f27bd009beaa536866fbbe24d9f`. Its receipt command is constructed with `shlex.join(["python", *sys.argv])`, rather than hardcoding the historical output filename. These changes add only the standard-library `shlex`/`sys` imports, replace `PROOF_HASH`, and replace that command-metadata expression. Reversing exactly those edits in memory reproduced original checker SHA256 `3d996f0f85f006350f5a29af72fd1cf26c25c8894b18db1cf451444f908230b8`; all scientific calculations are unchanged.

The reviewer then actually executed this command once from the repository root:

```sh
python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output topics/padua-lanczos-frontier-20261105/evidence/sh-independent-current.json
```

The process exited with code 0 and printed `PASS_SUPPLEMENTAL_EXACT_FINITE_CHECKS`: six exact Jacobian cases at n=2,3,4 for both rules, plus all 88 symbolic creator identities through degree 8. The new receipt's complete `rows`, `symbolic`, and `environment` objects were compared with the historical receipt and agree exactly. Its recorded command matches the actual invocation above. This is a new executed finite verification against the accepted metadata update, justified by the packaging repair; it remains supplementary to the analytic proof.

| Current or preserved artifact | Bytes | SHA256 |
|---|---:|---|
| Current theorem | 20,813 | `f27a22c4c6f13d03710750f52eef4dc9bac31f27bd009beaa536866fbbe24d9f` |
| Current `code/sh_independent.py` | 9,244 | `db4df9f967e00c5d73168263526365c4d66199ff922b02e58953d046cf2daaba` |
| New [evidence/sh-independent-current.json](evidence/sh-independent-current.json) | 3,692 | `c31e23273316adcc15833076818eb0458c5d473114bfb1236af65506ef31a260` |
| Preserved historical `evidence/sh-independent.json` | 3,684 | `776b97a5e213c0125f49bac2355bc6f4e48dd628b4c21d31cf7a9adc2ec6cbbd` |

The historical proof/checker pins and receipt above remain records of the original execution; they are not replaced with current hashes. No external raw SH artifact was produced: the exact arrays remained in memory. The storage owner `/root/g0_attribution` was sent the new invocation, sizes, hashes and portable external-output recipe before finalizing its storage records. No Git mutation was performed, and no additional scientific scope or audit clearance is claimed.
