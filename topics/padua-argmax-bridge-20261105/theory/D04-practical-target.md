# PD-T?argmax-bridge-codex-D04-target — Practical joint finite-degree comparison

ID kind: PD-T. Aliases: full M_infty rate; weighted outer-profile assembly.
Split from: the parent-requested D04 practical target.
Split into: D04-halfline, D04-reference, D04-row (supporting results).

## Statement and status

For D02's openly defined bias-completed full-phase model M_infty, prove
an explicit uniform error of the form

    |S_n(alpha,beta)-M_infty(log n;alpha,beta)|
                        <=C(alpha,beta)*(1+log n)/n

(or a separately specified honest alternative), with a practical stated
onset, ideally around 10^3--10^4, through the entire closed phase diamond
and polynomial collisions. The original fixed-cutoff M_far must instead
retain its exact nondecaying D02 bias. A phase-relative version against
S_n(0,0) may be considered only with its own complete error proof.

Status: **OPEN**. The newly proved supporting lemmas do not constitute
cases/conjuncts of this target and do not make its status PARTIAL.

## What the new dependencies establish

D04-half-line-defect.md gives the exact displaced digamma defect of the
bounded symmetric cancellation, up to a uniform O(w) error.
D04-reference-matching.md matches the entire reference sum to E_infty-E_R
with an explicit O((a+P)H_n/n) error, including phase wraps/collisions.
D04-row-reduction.md combines that result with the actual weighted pole
profiles and exact polynomial special rows to give a full-phase,
floor-free intermediate contract for R=2,n>=16.

## Remaining obligation

The intermediate K_D04 still has a degree-dependent ordinary H sum and
exact special rows. A quantitative joint comparison of those terms with
M_infty, or a separately justified direct interval certifier using them,
is not supplied by this developer block. In particular no outer-profile
quadrature error, phase-cover result, arithmetic implementation, runtime,
practical onset or argmax conclusion is inferred. D02's uniform limiting
theorem does not supply the missing practical rate.

## Retained unpursued and failing scopes

- Whole A-only kernel replacement remains abandoned by D03's exact
  collision example; bounded cancellation subtraction survives.
- Smooth h-Taylor through moving absolute-value zeros is not assumed.
- Independent fixed-R positive bounds retain their old floors; merely
  optimizing them is not the present joint proof.
- Phase-relative subtraction is deferred until the shifted-pole and
  outer-profile terms are controlled. No comparison is asserted here.

No new code/run or old near-model change occurred. Stop for independent
review of the separate PROVED supporting files before a new gated
outer-profile or certifier step. 2026-11-06, input 2db4a226dad798491be3ec2fe5ce0238e21cfaec, requested Astra
ultra; runtime model metadata unexposed.
