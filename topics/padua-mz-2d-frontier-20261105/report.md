# Signed Padua MZ frontier — development report

Branch `codex/padua-mz-2d-frontier-20261105`, [draft PR23](https://github.com/aacchhee/padua_research/pull/23). Rules/input83cf6f1ee244f2e72057332a7ec04ee74db1f0de; development base440d1079e42c3ef21c40d1cf8870f5b206410c6a; response base5db1e01dcd2258f45de2adcaef43859e59734618 (merged without conflicts). Codex development: gpt-6.1-sol xhigh mathematics, medium technical work; distinct supplementary reconstruction: gpt-6-astra high. **Claude Opus5.5 xhigh [audit-01](audit-01.md): mathematics ACCEPTED at stated scopes; P3 editorial findings answered in [response-01](response-01.md).** Claims below are development results, with provisional IDs; merged registries are untouched.

## Outcomes

For the actual signed interpolatory Lebesgue Padua rule, the universal spectral conjectures are false, while the direct coefficient operator has a uniform continuous-input norm. All conventions are inherited without change from the merged [definitions](../padua-mz-2d-20261101/definitions.md).

| Target | Development result | Durable record |
|---|---|---|
| F1 / PD-T110, endpoint upper threshold below2 | **Refuted analytically:** lambda_plus(m,m−1)→+infinity along evenm. Opposite-parity polynomial carrier has Q(p²)/logm→8ab/9>0 and bounded continuous norm. | [Upper carrier](theory/f12-eventual-upper-carrier.md), provisional PD-N…14 |
| F2 / PD-T028, universal positivity, positive log-order and eta→1 | **Refuted analytically:** lambda_minus(m,m−1)→−infinity along evenm. Negative carrier has Q(p²)/logm→−16ab/9 and bounded continuous norm; hence eta diverges on that subsequence. | [Negative carrier](theory/f12-eventual-negative-carrier.md), provisional PD-N…13 |
| F3 / PD-T116, signed strong MZ at every fixed ratio | **Sharp threshold classification:** eta=0 for0<=theta<=1/2 by exactness. For every1/2<theta<1, negative and positive carriers fit Pi_floor(theta*m) eventually; signed extrema diverge in opposite directions along evenm. | [Threshold](theory/f3-fixed-ratio-threshold.md), provisional PD-N…f3-01; both carrier records |
| F4 / PD-T114, actual C→L2 norm | **PROVED:** every m>=2,0<=n<m satisfies2<=||H_(m,n)||<=C*=28.3763348311…<30. | [Weighted-L1 density proof](theory/f4-uniform-density-bound.md), provisional PD-T…f4-01 |
| 1-D sibling PD-T027 | **OPEN:** sharp CC upper limit and uniform gap remain unresolved. The absolute-coefficient intermediary cannot supply a uniform gap. | [Scoped obstruction](theory/f12-1d-sign-discard-obstruction.md), [boundary escape](theory/f12-harmonic-boundary-escape.md) |

No explicit finite onset or smallest violating degree follows from the analytic carrier proofs. The new finite m1600 negative float hit is a separate uncertified observation. No odd-m classification or sharp extremal growth law is claimed.

## Why the spectral conclusion changes

The common [weight theorem](theory/f12-local-weight-asymptotic.md), provisional PD-T…12, derives at every fixed retained near-corner index j,k, along evenm,

`m^4 w_jk/logm → −16 e_j e_k (−1)^j`, with e_0=1/2 and e_j=1 otherwise.

An explicit whole-grid majorant controls the sum; this is not an inference from two negative corner weights. Multiplying localized degree-r Fejer polynomials by exact polynomial carriers selects the required sample parity while staying below the prescribed total-degree cutoff. Finite cosine identities evaluate the limiting energy, and dominated convergence handles every retained node. Continuous squared norms stay bounded independently ofm. This proves existential countersequences without a numerical premise.

The positive-reference [smooth diamond theorem](theory/f3-smooth-diamond-reference.md) separately supplies explicit two-sided sampled-energy equivalence at every fixed ratio. Its constants are large but completely specified. It concerns a positive regularized product-sine rule, and survives the refutation of the signed rule.

The F4 proof uses the exact norm `sup_(||p||2=1) Σ|w_z||p(z)|`. The signed density is a triangular Chebyshev approximation to pi²sin(theta)sin(phi), with uniform error<=68/(3m). A raw Chebyshev sampling loss of at mostm(1/2+1/pi) cancels that error; the positive main density is bounded through elementary CC weights. Divergent absolute-Gram bounds remain divergent. A uniform C→L2 norm does not imply an L2→L2 bound on the polynomial Gram operator, so it is consistent with the carrier countersequences.

## Gates and actual computation

Original criteria and dated dispositions are preserved in [gates.md](gates.md), handoff01 and the pre-registration files. Only actual completed scopes count.

- **G0 PASS:** exact m10 producer, independent cyclotomic nodal m10 (276 moments,3025 Gram pairs),1221 region checks, and float m10/20/30/40 agree with PD-T107/108. [Receipt](independent-checks-g0.md).
- **G1 m60 cost PASS:** hybrid C/GMP pencil and FLINT congruences accepted m60 in46.912s. A separate Python Fraction/repeated-reflection checker reconstructed3349800 H/Q entries and837000 offblock zeros, then accepted fresh transforms in232.594s. Baselines10/20/30/40 also independently replayed. **m60 strict brackets:** minimum(0.188593,0.188594), maximum(1.802011,1.802012). m80 is also independently accepted: minimum(0.172730,0.172731), maximum(1.816497,1.816498); producer302.437s and independent569.136s. Larger producer and independent scopes are listed separately in [certifier-results](certifier-results.md) and [independent receipt](independent-checks-cert.md); they must not be relabeled a complete certified integer range.
- **G2 INCONCLUSIVE:** pre-registered full heldout grid600/800/1000 was not completed for the upper extreme. The m600 upper solve was stopped after a recorded640s wall without a completed result, after a prior ncv40 attempt. Completed full endpoint grid extends through400; minimum-only runs include800/1000/1200/1600, with the last two explicitly posthoc. No fitted order or positive limiting gap is claimed. Analytic upper divergence supplies a separate answer.
- **G3 KILL original R1:** upper eigenvector at m400 has only0.29345 continuous L2 mass in the prescribed K10 edge union, below50%. The lower eigenvector changes to a corner-dominated family at400. Quadrature is degree-sufficient tensor Gauss with separate order refinement; maximum fraction change6.48e−11. This measured route kill does not rule out all limiting operators.
- **G4 finite screen:** every integer m2..239 was run at both n=m−1/m−2 (476 rows), with no threshold hit and maximum residual3.70e−11. Exact development acceptance covers2..60 plus80; independent acceptance specifically10/20/30/40/60/80. Coverage and degrees are recorded in [numerical-results](numerical-results.md) and the compact receipts. The planned every-integer2..300 float screen was stopped at its recorded coverage; exact acceptance at sparse larger degrees is not gap-free coverage. The analytic all-ratio countersequences replace the proposed positive asymptotic-plus-finite closure, with this dated scope change recorded rather than a false numerical PASS.
- **G5 NOT RUN:** original explicit-input/fit screen remains preregistered. The all-m analytic norm theorem resolves boundedness directly; no unrun numerical certification is credited.

The posthoc float minimum at m1600,n1599 is approximately−0.0234144165903, residual1.95e−13. This point has no exact/outward finite witness certificate. Its saved vector and regeneration command are manifested; it is not used in the analytic refutations. Fejer and corner-kernel trial quotients throughm2000 remain positive in their tested parameters; upper carrier probes grow slowly. Those finite tests and all unsuccessful/deferred mechanisms are retained in [ideas-f12](ideas-f12.md) and the attempts.

## Independent checking and evidence limits

[Supplementary Astra reconstruction](independent-checks-math.md) records exact file hashes and actual separate analytic and finite checks. It supplements the completed required [Claude audit-01](audit-01.md); its P3 documentation response is [response-01](response-01.md). [Independent exact replay](independent-checks-cert.md) shares FLINT and the signed-dominance predicate but reconstructs the full pencil in a different language and alias implementation, uses fresh transform proposals, and actually executes every listed acceptance.

The 84-entry evidence-manifest.json remains the frozen development inventory at dee638408505c9977f3febd98fdd42c9bc512c92; auditor additions and this documentation response are outside that historical inventory. It was verified against that exact Git candidate, rather than represented as a current-tree inventory; audited preparation must refresh the derived inventory. Scientific code, receipts and auditor records are unchanged by response-01.

Code, short receipts and durable proofs are committed. Bulk exact matrices, eigenvectors and large screens are regenerable scratch output, with identities and commands; Padua cold-storage delivery is pending. No Windows access, external-machine computation or archival durability is claimed. [COLD_STORAGE.md](COLD_STORAGE.md) and the inventory distinguish actual staging from future delivery.

## For the paper

A signed-Padua MZ note can state the even-m fixed-node logarithmic weight theorem, the two explicit polynomial carrier countersequences (hence the sharp half-degree signed threshold), the independent uniform C→L2 coefficient-operator bound, and optionally the positive-reference diamond theorem. Dependencies are the locally proved cardinal normalization PD-T101, analytic CC results PD-T017/022 and exact duality PD-T112, plus the newly written proofs. Finite m60/80 evidence and the m1600 float hit are illustrations at their exact scopes. No historical priority is claimed; PR21's literature comparison remains unmerged and is not a proof dependency. Claude audit-01 has accepted the mathematics; audited preparation must precede manuscript adoption or shared-registry changes. The explicit carriers prove existence only and are not usable finite witnesses at feasible degrees: the auditor’s MEASURED extrapolations (log m about55 or172–3464 in the tested families; [audit-01 A2](audit-01.md), [carrier-fit report](audit-01-support/subagent-f3/audit-diamond.md)) illustrate scale, do not bound an onset, and do not explain the unrelated m1600 float hit.

## Remaining obligations

Claude xhigh audit-01 accepted the mathematics and statuses; response-01 records A1–A7 dispositions. Next is final-ID/shared-registry preparation with a fresh reservation union scan, preserving AC’s OPEN-plus-refuted display for PD-T028/110/116. Constructive finite thresholds, exact certification of the m1600 hit, sharp growth constants, odd-m behavior and the1-D PD-T027 question remain separate open tasks. Only AC merges.
