# Audit 02 — re-audit of Codex response-01 (NN MOP IEP)

- Auditor: Claude, `claude-opus-5-5`, effort xhigh, as handoff04 requires. Role: independent auditor of Codex development. I authored audit-01 and its checker. I developed none of the response's claims or code.
- Date: 2026-11-05 (UTC).
- Rules read at branch head `30a361d19a6c23fa1df950becbe73f635aa22e71`. AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md are byte-identical to `6ec5768` (audit-01).
- Audited response output: `5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b`. `30a361d` changes only handoffs/03 (status) and adds handoffs/04.
- Main: `5db1e01dcd2258f45de2adcaef43859e59734618`, merged at `9ec2a54`. Its diff on this topic's paths is nil. Its only `state/IDEAS.md` change adds the PR19 effective-argmax section (IDEA-336–348, PD-N084–086), which is unrelated to NN MOPs.
- **Verdict: response-01 ACCEPTED. Stage → PR.** No mathematical, status or evidence finding remains. Two editorial items (E1, E2) and one evidence-strengthening note (X1) go to PR preparation. They do not require re-audit when applied as worded.

## Audited hashes (SHA-256 at `5b36f8f`)

| File | SHA-256 |
| --- | --- |
| response-01.md | `6c9c6904bba8d7e2ab0d46c7ca181d005c972570143f26eb89849ac58b1a5a87` |
| theory/interior-divisor-nonvanishing.md (T?…03) | `1907b124c354d90acb9ed10bc94e4a0eb8410db380ad83d34c3502f8f2d51960` (= Astra-reviewed) |
| theory/marginal-reconstruction.md (T?…04) | `27384beb097b9b6df5ff7240c4c7dd6bb371e8de375be0961b2e9fb5bbe50c24` (= Astra-reviewed) |
| theory/c4-baseline-measurements.md (T?…05) | `7e8ba636efda72f51ff073bea1092e722aa136c5b28d2049cb331cf16766aeb1` |
| theory/terminal-division-obstruction.md (historical redirect) | `0b10cefe11f51810736f20b3c9d4bd364bef34d79849e90c4f8b1e60423a2ea3` |
| theory/fixed-site-dictionary-failure.md | `d30194d11302864e5bfb8bafadee6b3f94cc133e70493912feff66f419e49b55` |
| SPLITS.md | `debb3d28ed3f3cda80d4d495c897b599f0f17c9ba8b4dca805b08baafd286818` |
| source-recheck-01.md | `c653c0af0484ca69ae1b792545a8ffe9536efb934acc2fefe4c05fa4f6e71c82` |
| c4-baseline-01.md | `3f2f164d02b872dadfbce5dcec6cc5383c1969f3c40304f972808d121ddb8912` |
| code/c4_float_baseline.py | `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8` (= Astra-reviewed) |
| response-independent-01.md | `76e159f9b31c6336d7f6ceddf4fc0c2005961074393175e801032b9463cca894` |
| report.md | `ffe27972ad1335f661fd0e006c0af643affa19f047feda45ae8eed8b4185b0ef` |
| gate.md | `a6189a81e1f2fad4444af311df2121044070ab1dd8f7138796b839655417659e` |
| candidates.md | `17a04e594d01f358377ca4fc21511d3bb03a661ababd004763e801c6b48bc5ba` |
| literature.md | `28144a41a67863c1cadaab3cec58510cd64169c3ca98849bf7364444aed3ed1f` |
| exact-runs.md | `2fb02ca153f342654f4be7f731642a81e53eb399de34f10812f2aff984ffaccb` |
| independent-check.md | `f65cbbfdd5b7b479fe45a3bfe13e4052239660f6fdcf5e399a92a1f22eaabdf2` |
| results/nn-mop-iep-20261103.md | `c7ca566f3c36c308518e85ae3a5ef06e3299f42b3bb1d0ac89e3f2fe01b03524` |

## Coverage

- **Registry.** I read the complete `state/IDEAS.md` and every obstruction/disposition table in this session for audit-01, at base `440d107`. For the `5db1e01` merge I inspected the added PR19 section in diff form, with long rows truncated in my display. It concerns Padua argmax only. Shortlisted entries were reread: IDEA-117, 031, 090, 111, 193, and IDEA-197 with its linked PD-T095/PD-N042/PD-T102 dispositions.
- **Response files.** I read every response-owned file in full: response-01, source-recheck-01, SPLITS, T?…03, T?…04, T?…05, the historical redirect, the F2 record, the c4 receipt and the supplementary review. I also read all changed sections of gate, report, candidates, exact-runs, independent-check, literature, LOG and results. I did not reread literature/INDEX.md: no new attribution claim is made and no new LIT row is proposed.
- **Primary sources: not reached by me.** arxiv.org is still denied by this session's network policy; I retried once. So the FHV, Van Assche, Kozhan–Vaktnäs and arXiv 2608.25758 locators in source-recheck-01 are **developer-verified only**. I neither confirm nor contradict them. The written proofs of T?…03/04 do not depend on these sources (see F1). The Hahn and Kravchuk weight conventions are the developer's reading of p. 20 of 2608.25758. I checked only that the code implements them as stated, e.g. (2)_{M−k}/(M−k)! = N−k.

## Independent executions (auditor)

Environment: Linux container, Python 3.13.18, mpmath 1.3.0 in a scratch venv. Raw outputs are local and regenerable, not committed.

**R1.** `python3 topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py > $SP/layer.json`
- Exit 0; 6,367 bytes; SHA-256 `37c86d1d4ece08d631cfd65c0e1a1065841c23980fb6b2f851a1baab8c53f25e`. This is byte-identical to my audit-01 output in the same environment.
- Results: 24 cases, 467 sites, 809 divisions, 128 terminal zero-d sites, maximum divisor degree N−2. The developer replay's different raw hash (`9e3c53ec…`) is explained by its Python 3.12.14 field.

**R2.** `venv/bin/python topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family krawtchouk --sizes 4 8 12 16 24 32 --dps 140 220 > $SP/krawtchouk.json`
- Exit 0; 7,072 bytes; SHA-256 `023e9e28…3a08`.
- `cases` payload hash (sorted-key JSON) `997e57d9…17ca`.

**R3.** Same command with `--family hahn`.
- Exit 0; 7,101 bytes; SHA-256 `166da1a9…750c`.
- `cases` payload hash `bea2ecd8…3fd7`.

**R4.** `venv/bin/python topics/nn-mop-iep-20261103/audit-02/claude_exact_reference_check.py 8 12 16 24 > $SP/exactref.json`
- Exit 0; SHA-256 `0a1c4bb4…2249`.
- Auditor code SHA-256 `2ce646210d9699a3f51f3a3b99127c5dbf8d971425004cf4b42d63dfc9755405`. See X1.

Note: the handoff command lacks `/usr/bin/time`, which is unavailable here. My first attempt prefixed it, failed with exit 127 before Python ran, and produced empty files. R2 and R3 are the clean reruns.

Every value in my R2/R3 outputs equals the c4-baseline-01.md tables:
- E, correct digits and lost digits for all 12 cases, at the printed precision;
- 140/220-digit agreement, worst Hahn N32 at 1.41e−99;
- reference subtraction ratios, Krawtchouk 3…59 and Hahn 1.91…960.8;
- division counts 12…1426 and maximum divisor degree N−2;
- terminal |d|;
- all 12 input SHA-256 values;
- N=4 exact-check distances 2.43e−218 and 3.58e−217.

Relative error exceeds one exactly at Kravchuk N24/32 and Hahn N16/24/32, as stated. I compared values, not raw hashes: raw hashes differ by version, platform, argv and elapsed time, as the receipt says.

## Reconstruction and dispositions

### F1 — T?…03 PROVED: accepted

- **Kernel rank.** At |ν| = s the s conditions have rank s on degree ≤ s, because their first s columns form the invertible M_ν. The kernel is spanned by P_ν. This includes s = 0.
- **Successor difference.** P_{ν+e1} − P_{ν+e2} has degree ≤ s and lies in that kernel, so the successor-difference identity follows from normality alone. The x^s coefficient gives t_{ν+e1} − t_{ν+e2} = b_{ν,2} − b_{ν,1}; I checked the sign.
- **Nonvanishing.** d_ν = 0 would put a monic degree-(s+1) polynomial into the kernel of M_{ν+e1+e2}. The union of the successor conditions is exactly i ≤ n for L_1 and i ≤ m for L_2.
- **Axis cases.** Correct.
- **Locators.** The record cites Kozhan–Vaktnäs Lemma 2.18(b) only as a stronger LITERATURE statement. It claims locally only the proved direction. Correct.

### F1 — T?…04 PROVED: accepted

**(E) and (F).** I re-derived (E) term by term:
- P_{ν+e1} coefficient: b_{ν+e1,2} − b_{ν+e2,1};
- P_ν coefficient: d_ν b_{ν+e2,1} + S_{ν+e1} − S_{ν+e2}, with S = a_1 + a_2;
- P_{ν−e1} coefficient: a_{ν+e2,1} d_{ν−e1};
- P_{ν−e2} coefficient: a_{ν+e1,2} d_{ν−e2}.

(F) is direction 1 at ν multiplied by d_ν. Comparing coefficients gives exactly (A), (B1) and (B2). The record writes (B2) with S; this is the same as my audit-01 form.

**Independence of the expansion family.** The degrees s+1 and s are distinct. The two predecessors are independent by normality of M_ν. Axis and degree-zero cases drop the absent terms; the record argues this, it does not assume it.

**Validity range.** The identities are derived for |ν| ≤ N−2, which is where P_{ν+e1+e2} exists.

**Induction coverage.**
- The mixed a's on layer s+1 come from (A) with ν = η−e2 or ν = η−e1. They need η_1, η_2 ≥ 1, use divisors at η−e1−e2 (degree s−1), and are computed before that layer's b's.
- (B2) covers b_{η,1} with η_2 > 0; (B1) covers b_{η,2} with η_1 > 0.
- The axis a's, b_{(s+1,0),1} and b_{(0,s+1),2} come from marginal data. On the axes, P_{(k,0)} is the k-th marginal OP of μ_1, so a_{(k,0),1} = α_{1,k} and b_{(k,0),1} = β_{1,k}.
- Every coefficient on a layer is produced exactly once, with nothing unknown on the right side. N = 1 needs no division.

**Divisor-degree table.** t−2 for mixed a's and t−1 for b's: correct. The terminal d is used neither as a divisor nor as a numerator.

**Final boundary.** Uses (D) at |ν| = N−1, valid from normality of ν, ν+e1 and ν+e2, so b_{ν,1} = b_{ν,2}. Correct.

**Scope.** The record claims no converse characterisation of arbitrary arrays and no stability result. Correct.

**Dependence on sources.** The proof uses only T?…01, T?…03 and linear algebra, so its PROVED status does not rest on the primary sources I could not reach. The FHV layer paraphrase in source-recheck-01 (lower coefficients at k−1, diagonal at k) agrees with this independently derived organisation. Whether it is a faithful quotation remains developer-verified (coverage above).

### F1 — withdrawal of the PD-N?…01 failure classification: accepted

- **Original text preserved.** The original record's text is contained verbatim in the historical redirect. I checked this by programmatic substring comparison against `ae7e618`.
- **Split recorded.** SPLITS.md maps the interior assertion to T?…03, the terminal equality to T?…04, and the withdrawn C4-failure label to no final ID.
- **L5 respected.** No final PD-N was ever assigned, so no administrative negative record and no renumbering results. The withdrawn "failed" classification described a step outside C4's domain. That is not a scoped, evidenced failure of a mechanism anyone uses, so withdrawing rather than registering it is consistent with WORKFLOW L5.
- **No status upgraded without proof.** The positive content is now carried by written PROVED records. The original equalities are neither weakened nor deleted.
- **Split rule respected.** T?…03 is substantive because T?…04 depends on it, so it has its own record. T?…04 is not PARTIAL: its two parts are both PROVED.
- **Candidate record.** C4's candidate record now cites T?…04 and records the withdrawal with its reason. Both C4 and the withdrawn sub-mechanism are preserved.

### F2: accepted

The report, C2 and the PD-N?…02 record now state the following:
- the same-site test refutes only the literal dictionary;
- PD-T057's block conditions also couple neighbouring levels;
- the decisive mismatch is spectral: H_1 P = H_2 P = xP, versus independent joint values (x_l, y_l);
- no impossibility for lifted or covariant encodings is claimed.

The MEASURED counts and the narrow C2 disposition are unchanged. The developer correctly did not promote my 255-site full-lattice count into a result.

### F3 — T?…05 MEASURED: accepted

**Implementation.**
- Binary64 arithmetic is genuine: Python floats, with exact Fractions converted once per input.
- Stieltjes marginals use no reorthogonalisation; the A/B layers mirror T?…04.
- Divisor degrees and cancellation diagnostics are recorded.
- Every failure mode raises and is reported as a failure, not as success. `relative_error_below_one` is kept separate from `completed`.

**Metric.** The fieldwise sup-norm relative metric and the digits formula (ε = 2^−52) are as stated.

**Scope.** The record claims no general instability, no error-source attribution, no C3 comparison and no source-residual reproduction. The history honestly records the intermediate 100/160-digit reference failure.

**Supplementary review.** response-independent-01 covers proof reconstruction and full replays with payload comparison. It skipped the full IDEAS read under the stated non-novelty exception. That is acceptable for supplementary evidence; this audit performs the gate read.

### F4: accepted

Version-dependent raw hashes are distinguished from payload identity in exact-runs, independent-check and the C4 receipt. My audit-01 normalised reproduction is credited, not re-claimed.

### N1: accepted with a recorded limitation

Coverage is stated honestly per source, including what was not rechecked (ADY, ADV, Toda, KV Thm 3.19, FHV §2). The developer's access route (a web PDF service) is disclosed. My own primary coverage remains nil; see Coverage.

### N2: accepted

IDEA-197 and its PD-T095/PD-N042/PD-T102 records concern two commuting bivariate sections and their commutants. One spectral variable with two weights supplies no second coordinate. The non-applicability reason is sound.

## Remaining items for PR preparation (non-blocking)

- **E1 (editorial).** c4-baseline-01.md, "Divisor diagnostics", says terminal max |d| "grows to … 6.47 (Hahn N32)". It is not monotone: Hahn N24 has 71.15 (my R3 and the developer's own data). Reword to "reaches 33.86 (Krawtchouk N32) and 71.15 (Hahn N24)" or similar. The values are unchanged.
- **E2 (editorial).** In results/nn-mop-iep-20261103.md, the bullet "Known exact reduction; numerical question OPEN" still says "Correct FHV reconstruction needs a family of shifts and boundary information". That is true for the step-line route only. Add that the marginal route (T?…04) needs only the marginal Jacobi data, so the bullet agrees with T?…04. Also say "no C3 comparison" rather than "no C3/C4 floating-point comparison", since a C4-only pilot now exists. Mirror this in the RESULTS.md section at preparation.
- **X1 (evidence strengthening, optional citation).** My R4 compares the pilot's 220-digit reference with exact Fraction ground truth from the audit-01 moment solver at N = 8, 12, 16, 24 for both families. The reference/exact distance is ≤ 1.7e−190 in every case. The binary64 errors measured against exact values equal the reported E values (e.g. Kravchuk N24 72940.598…, Hahn N16 70.3138…). The receipt's limitation "only N4 has an independent exact reference formulation" may therefore be narrowed to "exact references at N ≤ 24 (audit-02 R4); N32 relies on precision convergence". This is MEASURED, finite and not a proof. Citing it is optional.
- **X2 (process).** At preparation, ID_CROSSWALK must record that PD-N?nn-mop-iep-codex-01 is withdrawn with no final ID, and the split mappings to T?…03/T?…04.
  - Need versus reservation: PD-T 5 of 8 (T?…01–05); PD-N 1 of 4 (N?…02); IDEA 4 of 8; LIT ≤ 12 of 12.
  - FHV and the other campaign-read sources may already have records on `claude/padua-literature-20261103` (PR21). Deduplicate same-source LIT entries against the live main/PR21 state rather than allocating twice.

## Remaining uncertainty

- Primary-source locators are not auditor-verified (N1 limitation).
- The error source in the C4 pilot (marginal Stieltjes versus layer amplification) is unmeasured. A cheap discriminating run would feed exactly rounded marginals into the binary64 layer recursion. It is listed under the topic's open items as "error-source decomposition"; it was not executed by anyone.
- Stable coupled NN updating remains OPEN. C3 remains deferred.

This acceptance covers the stated scope only. It does not declare readiness, which still needs PR preparation, and it does not authorise a merge.
