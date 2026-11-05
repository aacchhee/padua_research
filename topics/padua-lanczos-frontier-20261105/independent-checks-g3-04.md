# G3 n3 independent exact checker — prospective plan

Rules read at `12879b5666a93f2ca88d89c3deaa7a152f883cc3`; unchanged rules verified against the previous read. Codex technical independent checker, requested gpt-6.1-sol medium; runtime effort metadata not independently exposed. Scope is only the accepted L5a finite reduction at n=3,D=7, not new mechanism/novelty generation or any n4–8/G3-trend/U2 claim. Producer implementation will not be read or imported. Original G1 files remain untouched.

## Exact distinct implementation

Use Sympy's algebraic field QQ(sqrt(2)) and its exact domain-matrix linear algebra, distinct from the producer's hand-written Fraction-pair elimination. The positive real embedding is fixed by sqrt(2)>0 and 1<sqrt(2)<2. Extract exact rational a,b from each field element a+b sqrt(2); decide signs by rational signs and, for opposite signs, comparing a² with2b². No decimal root ordering or float acceptance is allowed.

Independently reconstruct all ten nodes from the exact cosines for j=0..3,k=0..4,j+k even, retaining the frozen order and full R² balls. Build all36 monomials of total degree<=7, the full30-by36 value/xpartial/ypartial jet matrix, its exact rank and complete kernel. Check both the annihilation identity and independent kernel rank; do not assume historical predicted ranks or quadratic-generator completeness.

Lower: recover and hash the exact baseline source Git blob separately. Parse the producer's small polynomial coefficient certificate; verify it is the actual recovered baseline, nonzero and degree<=7. Reconstruct every jet, Hessian and every local Taylor coefficient by exact binomial expansion; check Hessian positive definiteness, mu=det/trace>0 and the finite coefficient-sum inequality at the stated rational L. No historical decimal radius or sampled direction is an input.

Upper: independently evaluate the entire reconstructed kernel at each listed node plus rational translation; require U>0, exact full-ball membership hx²+hy²<=U², every retained weight strictly positive in the chosen embedding, exact weighted dependence in every kernel coordinate, and full evaluation rank equal to the complete kernel dimension. Do not trust the producer's basis, ranks, margins or summary. Basis-invariant positive dependence permits this independently chosen kernel basis.

## Inputs and controls

Stable certificate schema communicated by producer: `lower.json` contains L and terms `[xpower,ypower,[a,b]]`, rational strings representing a+b sqrt(2); `upper.json` contains U,q, points `[nodeindex,hx,hy]` and matching positive `[a,b]` weights. Producer implementation stays unread. The baseline source is Git blob `c88017135d020db69ecf438794f0710dc5a09fda`,3963bytes,SHA-256 `287e8dd0bdaa60d93d728045fcd47c5c75832813657f4849081fe4b1e0629e8b`.

Meaningful rejected controls will corrupt the polynomial, lower radius/Taylor criterion, weight sign/balance, ball membership, point rank, node index and field encoding. A positive unmodified control must pass again. Failed upper search or malformed-certificate rejection is not a negative statement about the optimal radius.

## Prospective caps and execution gate

Write this plan before any scientific reconstruction or test. Then inspect installed Sympy API/dependency readiness, and execute from a copied/hash-pinned stable certificate pair under `/tmp/padua-lanczos-frontier-g3-independent`. Entire prototype, including rank/lower/upper and controls, is externally capped at600seconds; stop with explicit INCOMPLETE if needed. No heavier follow-up, n4–8 run, or bracket/trend status is authorized here. Copy only small exact certificates/receipt as directed by root, keeping large reconstructed matrices/raw logs outside Git. Final receipt must record actual commands, hashes, trusted Sympy/Python versions, ranks, exact identities/sign checks and measured cost.

## Execution status

Plan written before implementation or scientific execution. Producer reports stable lower L=1/512 and a provisional upper U=1,q4,12points; final upper may improve. These values are unverified proposals until this distinct checker executes. Root owns Git, the scientific record and any final bracket status.

## Executed exact result — 2026-11-05

The distinct Sympy checker executed successfully on the final frozen pair. Main-checker elapsed time was1.330798089seconds (module-import/startup time is outside that internal timer); the entire process had a600-second external cap,580-second internal cap and2GiB address-space limit. Python3.12.14 / Sympy1.14.0 were used; no producer code was read or imported.

Full degree7 monomial count36; node count10; exact first-jet matrix30x36 has rank30. The independently computed complete kernel has dimension6, exact row rank6 and J*B^T=0. The actual20-term baseline polynomial recovered independently from the pinned historical Git blob matches the certificate exactly, has degree7, and passes30 exact value/derivative zeros, all10 positive-definite Hessians and all10 finite Taylor whole-ball inequalities at L=1/512.

The final upper certificate U=1/2,q8 has12 retained points and12 strictly positive exact weights. Every point is in its stated closed Euclidean node ball; six points are outside the square, and were correctly retained because the scope is full R² balls. The independently reconstructed full-kernel evaluation matrix has exact rank6 and all6 weighted balance coordinates vanish exactly. No generator-subspace assumption or floating acceptance was used.

Nine malformed controls were rejected with the intended exact failure: changed actual polynomial (baseline mismatch); lower radius1 (Taylor inequality); negative retained weight; positive but unbalanced weights; off-ball point; rank-deficient one-point subset; invalid node index; invalid field encoding; proper kernel subspace. The original lower and upper passed again after all mutations. Detailed exact node margins and rejection reasons are in `evidence/g3-independent.json`. This is actual independent finite verification at n3; no n4–8 bracket, full G3 trend/decision, optimal value or U2 status is claimed by this checker. Root/theory owner controls the finite result statement.

Frozen certificate inputs: lower2704bytes SHA-256 `48ea29641bde627b69a069ffa01687089f6decc0258ab0afa516ca69863b7e3c`; upper2136bytes SHA-256 `5c0c70e976711b31d0eed6c91b1c422fd8247ec9805a630e669618b47b9ef2a3`. Actual checker source10387bytes SHA-256 `ec595ad0effc0df8c4a6e1a0ca95d0d2632bc00ea8eb2126fc3a25629fcfa2f4`. The baseline text was independently recovered with `git cat-file blob c88017135d020db69ecf438794f0710dc5a09fda`; its3963bytes and complete SHA above were asserted before parsing. Historical printed ranks/radii/statuses were ignored as acceptance data.

Actual invocation from `/workspace/padua_research`:

```sh
timeout 600s python -B topics/padua-lanczos-frontier-20261105/code/g3_independent.py --lower /tmp/padua-lanczos-frontier-g3-independent/inputs/lower.json --upper /tmp/padua-lanczos-frontier-g3-independent/inputs/upper.json --baseline /tmp/padua-lanczos-frontier-g3-independent/inputs/pstar-source.json --out /tmp/padua-lanczos-frontier-g3-independent/check-n3 --receipt /tmp/padua-lanczos-frontier-g3-independent/receipt.json
```

For a fresh output directory, the committed producer certificate pair may replace the copied input paths; the baseline is recovered from the pinned Git blob and hash-checked by this checker. The raw independent kernel/nodes, input copies, stdout log and receipt remain local temporary artifacts under `/tmp/padua-lanczos-frontier-g3-independent`; no external archival retention is claimed. `inventory.json` there records every raw artifact's size/hash for the orchestrator's storage index.
