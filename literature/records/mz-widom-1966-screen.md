# mz-widom-1966-screen — matrix-asymptotic pointers

- Access/read date: 2026-10-31. Reader: Codex; gpt-6.1-sol, high (explicit orchestrator assignment).
- Reading coverage: bibliographic discovery and attempted primary access only. Both mathematical contents are **FULLTEXT UNVERIFIED**; no theorem is imported.

## Source records

### LIT-053 — Widom, Hankel matrices

- Citation/pointer: H. Widom, *Hankel matrices*, Trans. Amer. Math. Soc. 121 (1966), 1–35, DOI <https://doi.org/10.1090/S0002-9947-1966-0187099-X>.
- Primary attempt: <https://www.ams.org/tran/1966-121-01/S0002-9947-1966-0187099-X/S0002-9947-1966-0187099-X.pdf> returned 403 in the connector.
- Locator/gap: no theorem/page inspected. A Hankel label alone supplies no CC extreme-eigenvalue law. Extract the exact matrix class and asymptotic before treating this as a prior result or usable template.

### LIT-054 — Widom–Wilf, small eigenvalues

- Citation/pointer: H. Widom, H. Wilf, *Small eigenvalues of large Hankel matrices*, Proc. Amer. Math. Soc. 17 (1966), 338–344, DOI <https://doi.org/10.1090/S0002-9939-1966-0189237-7>.
- Primary attempts: <https://www.ams.org/proc/1966-017-02/S0002-9939-1966-0189237-7/S0002-9939-1966-0189237-7.pdf> and Wilf's author reprints page returned 403. Search locates the paper, not an inspected theorem.
- Relation/gap: M2 uses a continuous/discrete mass-matrix generalized eigenvalue problem. A smallest eigenvalue of a monomial moment Hankel matrix is not invariant under nonorthogonal basis changes. An exact congruence/pencil map and hypotheses are required; “same flavour” is not an equivalence or a theorem.

## History

2026-10-31: honest inaccessible-source records, exact theorem checks pending.

## 2026-11-01 fulltext reading (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5. Access: free publisher/open PDF read through the WebFetch tool, which extracts the text layer and answers through a summarizing model. Coverage is therefore paraphrase-level; OCR formulas are partly garbled. Any formula-level use needs a page-image check. Rules `9739a0c`, 2026-11-01.

### LIT-053 — Widom, Hankel matrices

- Coverage: all sections via extraction (§1 Introduction; §2 numerical range, Lemmas 2.1–2.4, Thm 2.1; §3 positive Hankel matrices, Thms 3.1–3.4; §4 finite Hankel matrices, Thms 4.1–4.5, pp. 1–35).
- Statements: boundedness/compactness criteria for H=(c_{j+k}) with c_j=∫x^j dμ (Thms 3.1–3.2); eigenvalue-counting asymptotics (Thms 3.3–3.4); finite-section norm convergence, top-eigenvalue/eigenvector asymptotics (Thms 4.1–4.5). Smallest eigenvalues of finite sections, quadrature, Chebyshev nodes and CC weights are not addressed.
- **Verdict: RELATED, DIFFERENT SETTING.**

### LIT-054 — Widom–Wilf, small eigenvalues

- Coverage: whole note via extraction (page markers absent in extraction). Erratum Proc. AMS 19 (1968) not read (group B).
- Statement: for H_N=(c_{m+n}) with moments of α on [a,b] and Szegő-type condition ∫log w/√((x−a)(b−x))>−∞, the smallest eigenvalue satisfies λ_N∼const·(2N)^{1/2}σ^{−2(N+1)} (three cases; exponent 1/4 in a boundary case), σ depending only on [a,b].
- Relation: a standard eigenproblem for monomial moments, exponentially small. It is not a congruence-invariant pencil (discrete vs continuous Gram). **Verdict: RELATED, DIFFERENT SETTING**, as the earlier record anticipated.
