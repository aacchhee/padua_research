# PD-T?proof-attempts-2-codex-93 — The source Ldiag taper has only finitely many exceptional parameters

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

ID kind: PD-T.
Aliases: B1 exact Ldiag taper; far/near ordering; real exponential-polynomial specialization.
Split from: specialization question left explicit in record 92.
Split into: none.

## Statement

Fix an **even** number of pole factors `m>=4` and put `T=m-1`. Fix any real nodes in `[-1,1]^2`, positive weights, and injective evaluation on `Pi_m`, with `M>=dim Pi_m`. For `sigma>0`, define the literal source `Ldiag` taper

`epsilon_j(sigma)=exp(-sigma*(sqrt(m)-sqrt(j)))`, `j=1,...,m`,
`a_j(sigma)=2+sqrt(2)*epsilon_j(sigma)`.

Normalization clarification (audit-01 F4): the prose source uses `a_j=2+epsilon_j`, whereas `orf2d.py` uses `a_j=2+sqrt(2)*epsilon_j`; the same proof holds for `a_j=2+kappa*epsilon_j` for each fixed `kappa>0`, with coalescent witness `c=2+kappa>2`.

Use either the displayed order (source `near`) or its reversal (source `far`) for the poles `ell_j=x+y-a_j`. There is a **finite** set `Z` of positive real `sigma`, depending on the fixed sampled measure and `m`, such that for every `sigma>0` outside `Z`, both source orders satisfy B1's equality simultaneously for all `2<=t<=T`:

`W_(t+1)={r in (I-P_(W_t)-P_(W_(t-1)))C_t : r perpendicular W_(t-2)}`.

Equivalently there are only finitely many potentially exceptional `epsilon_min` in `(0,1)`, using the source relation `epsilon_min=exp(-sigma*(sqrt(m)-1))`. No exceptional location or individual stored experimental parameter is certified or computed here.

## Definitions and assumptions

All spaces, weighted projectors and finite-sampling conventions are those of records 90–92. The source line factory uses `((x+y-2)/sqrt(2))-epsilon_j`; multiplication by the constant `sqrt(2)` gives the normalized pole above and does not change any flag or span. Its actual implementation asserts even total pole count, which is why that restriction is retained. This theorem does not silently extend code coverage to odd `m`.

For positive `sigma` all taper distances are positive and pairwise distinct; all offsets exceed 2. The auxiliary value `sigma=0` has every offset equal to `c=2+sqrt(2)>2` and is used only as the structural rank witness, not as an admissible distinct-pole taper.

## Status by part

Overall status: **PROVED**. Actual supplementary full-file inspections found no blocker; Part 2 Claude audit remains PENDING.

| Mathematical part | Status / verification obligation |
| --- | --- |
| Finite exceptional sets for the literal even-count source taper and both orders | PROVED; written analytic proof below and actual independent full-file candidate inspections |

Candidate / claim disposition: retained specialization of the registered target, no novelty claim.

## Depends on

Records 90–92, especially record 91's rank polynomials `p_t`, positive at coalescence, and record 90's detector. The elementary zero bound for real exponential polynomials is proved below. No external theorem or computation is needed.

## Checks and sources

Source definitions: programme `checks/code/decisive/gen1-3/orf2d.py`, `taper` and `make_lines('Ldiag',...)`, read without executing the module; exact source pins are in `../b1-input-preparation.md`. The parent and both independent mathematical agents ACTUALLY read this complete frozen candidate file and found no blocker; source taper definitions were independently reread. Exact reviewed hashes/scopes are in `../independent-checks-b1.md` and `../independent-checks-b1-topform.md`. Only status/verification metadata changed on promotion; before/after proof-body hashes match in `../outputs/b1_status_metadata.json`. Part 2 Claude audit remains PENDING.

## Proof

For the fixed data and `T`, take the polynomial

`P_0(a)=prod_(t=2)^T p_t(a)`

from record 91, **without its collision factor**. It is strictly positive when all offsets equal `c=2+sqrt(2)`. For each order permutation `rho` (identity or reversal), put

`f_rho(sigma)=P_0(a_(rho(1))(sigma),...,a_(rho(m))(sigma))`.

Substituting `a_j=2+sqrt(2)*exp(-beta_j*sigma)`, where `beta_j=sqrt(m)-sqrt(j)` is real, into a polynomial gives a finite real linear combination of real exponentials. Group equal exponent rates and delete zero coefficients to write

`f_rho(sigma)=sum_(l=1)^N c_l exp(-lambda_l*sigma)`

with distinct real `lambda_l` and nonzero real coefficients. This combination is not identically zero, since `f_rho(0)=P_0(c,...,c)>0`.

A nonzero such combination with `N` terms has at most `N-1` distinct real zeros. For completeness, the assertion is immediate for `N=1`. Order the rates increasingly and multiply by the nonvanishing exponential `exp(lambda_1*sigma)`. The derivative then has exactly `N-1` nonzero exponential terms with distinct rates. By induction it has at most `N-2` distinct zeros. If the original combination had `N` distinct zeros, Rolle's theorem between consecutive zeros would give at least `N-1` derivative zeros, a contradiction. This also excludes an infinite set of distinct zeros by selecting `N` of them. Only real rates are used; no complex-exponent zero bound is asserted.

Thus each `f_rho` has finitely many positive zeros. Take `Z` to be their union for the two source orders. For `sigma>0` outside `Z`, every required `p_t` is nonzero and the offsets are automatically distinct. Record 91 gives every maximal projected rank; record 90 and the deduction of record 92 give the asserted equality for every required degree and both orders.

The map `sigma -> epsilon_min=exp(-sigma*(sqrt(m)-1))` is a bijection from positive reals onto `(0,1)`, so it carries the finite exceptional set to a finite set. Each finite set is a proper real algebraic subset of its one-dimensional real parameter space: the product of the corresponding real linear factors defines it (the empty case uses polynomial 1). This does not claim rational coefficients, algebraic-number roots, or computed locations. The original pole-offset exceptional set remains the explicit algebraic set of record 91; the taper argument proves that this particular curve is not trapped in it.

## Scope and open items

The result is exact generic validity along the source taper, not a verification of any one `epsilon_min` or `sigma` used by the floating diagnostic. Its exceptional set may be a conservative superset of actual identity failures. No numerical-stability, all-pole-class or unbounded-degree statement is inferred. The broader multi-class B1 target remains OPEN outside these class results. Supplementary full-file candidate inspections are complete; Part 2 Claude audit remains PENDING.

## History

2026-11-01, Codex `gpt-6.1-sol xhigh`, during the original B1 box. Parent proposed the bounded specialization after independently inspecting core 90–92; lead and primary checker separately reconstructed the nonzero exponential-polynomial/Rolle argument. No mathematical code or sampled-rank calculation was run.
