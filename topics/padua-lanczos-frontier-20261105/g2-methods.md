# G2 technical producer and lower-certificate record

Codex technical developer, requested gpt-6.1-sol medium; rules/read head
`0e493be7f9883e00e6260cf6b081c607a230177f`. No Git mutation. Read the full
saved W/R/F preregistration in `attempts/L2.md`, completed gate ledger in
`ideas-l1-l2.md`, and the complete new finite closure reduction before
implementation. The root and distinct reviewer cleared that reduction at
SHA-256 `44498c6230d0a59bbd0cfc4bc96600f0b401eb92ba9302b5c1d54cc569c8d5f9`
and explicitly authorized these computations. No new mechanism or primary
literature/priority claim is added.

## Prospective scope and prerequisites

The unchanged degree12 predicates are `C_12>=256` for W and `E_12>=16`
for R, separately on exact rational T24 and rotQ24, BJ selection, the saved
smooth exact-base rule class, and global source columns1,...,90. These
are first-order aggregate X-closure predicates, not span-condition tests or
actual IEEE statements. The raw monic source scale is
`tau_h²=||A_h b_parent||²`; normalized-source conversion in the analytic
reduction is retained. `||X||²` is1 on T24 and49/25 on rotQ24.

Before the first run, root fixed the cheap W screen order: stage11,
source6=(3,0), all nodes, then sources4,3,5 only if needed; stop on an
exact threshold pass. This is a subset **lower** on the unchanged global
90-source domain. The first source sufficed on both grids, so no later
source was tested. Source6 was a prospective candidate informed by the
inherited old BJ witness source; none of its old span values enters this
closure calculation.

The W source and predicates were written before execution; its source
hash was captured in the completion receipt rather than a separate
pre-run digest receipt. This chronology is explicit. No criterion or
source was changed after seeing a W result. The separate R helper digest
was recorded before its execution.

After the mathematical owner prospectively recorded the nonnegative
partial-trace lower and root/reviewer authorized it, the separate helper
computed

`E_12 >= sum_i ell_(11,6,i)/(90*M*||X||²)`.

The global denominator is29250 on T24 and110250 on rotQ24. This lower
retains the complete original independent-sign law. It is neither an exact
full expectation nor an expectation for a restricted-source random law.
Insufficient partial bounds would be inconclusive, never R FAIL.

## Exact construction and controls

`g2_screen.py` imports the unchanged `e1_exact.py`, SHA-256
`19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f`,
and separately rebuilds the degree12 BJ basis on each frozen grid.
All arithmetic is FLINT exact rational. It verifies all entries of the
full Gram matrix `B^T B=D`, positive d/tau², and the complete rational
coordinate expansion `X B_11=B_12 C_X`, including degree12 rows and j=0.
Coefficients above degree(j)+1 are checked zero. Sparse nonzero coefficient
lists then reduce response cost without dropping any expansion term.

The producer computes signed responses

`omega_jh(i)=x_i g_jh(i)-sum_l C_X(l,j)g_lh(i)`

**before squaring**, with every next-degree source/row present. No absolute
response envelope or triangle upper is used as a lower. The pure-X formed
child identity `omega_jh=-1` for its own child source and zero otherwise is
checked at every node and every pure-power input column through degree11.
The complete normal diagonal lies in[0,1]; its trace is checked as a
consistency identity, not as a replacement for the full Gram check.

For each tested source the producer evaluates ell at every node, selects
the exact maximum, and independently forms and projects that actual pulse's
monic closure matrix. Its exact normalized Frobenius gain equals ell;
rank-one impulse structure makes this also its spectral-output gain.
The compact floor of `max_i ell_i/||X||²` is a lower on C_12², not its
exact value. Scientific acceptance compares that rational lower with65536.

A separate small exact control uses10 generic triangular rational nodes
at degree2. It differentiates both full span projectors directly, retains
both moving-projector terms, and compares with the monic omega formula.
It repeats with alternative coefficient and normalization derivatives
propagated through the recurrence, verifying the same actual closure
projector derivative. These controls are developer computations; the
independent checker has its own construction and controls.

The R helper verifies screen/artifact identities and nonnegativity of all
selected ell values, then sums all M nodes with the full-law denominator.
Its integer floor is a lower on E_12. Omitted stages/sources contribute
nonnegative exact squared gains under the complete original law.

## Executed commands and outcomes

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g2_screen.py --set triangle --output-dir /tmp/padua-lanczos-frontier-g2/triangle-screen --receipt topics/padua-lanczos-frontier-20261105/evidence/g2-triangle-screen.json
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g2_screen.py --set rotated --output-dir /tmp/padua-lanczos-frontier-g2/rotated-screen --receipt topics/padua-lanczos-frontier-20261105/evidence/g2-rotated-screen.json
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g2_partial_r.py --screen-receipt topics/padua-lanczos-frontier-20261105/evidence/g2-triangle-screen.json --output-dir /tmp/padua-lanczos-frontier-g2/triangle-partial-r --receipt topics/padua-lanczos-frontier-20261105/evidence/g2-triangle-r-lower.json
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g2_partial_r.py --screen-receipt topics/padua-lanczos-frontier-20261105/evidence/g2-rotated-screen.json --output-dir /tmp/padua-lanczos-frontier-g2/rotated-partial-r --receipt topics/padua-lanczos-frontier-20261105/evidence/g2-rotated-r-lower.json
```

All four commands exited0. W runs took2.03s/69.87s; all stated exact
controls passed. Raw arrays, all-node ell values, exact rational bounds,
commands, versions and identities are recorded in the small case receipts.
Both original W/R predicates are certified by these developer lower bounds:

| Grid | fixed W source/node at stage11 | floor lower on C_12² | floor partial lower on E_12 |
|---|---|---:|---:|
| T24 | h6, node22=(-1,5/6) | 17525752205103 | 6457695691 |
| rotQ24 | h6, node1=(2/15,-27/20) | 6324995264 | 2606606 |

The W floors exceed65536 and R floors exceed16. These numbers are lower
certificates, not computed exact capacities/expectations. No full R trace
or all-source upper was needed or computed. This does not change the
original source domain, law, thresholds or target.

`evidence/g2-fixed-certificate.json` extracts the fixed source/stage/node,
integer floors and baseline/source pins for both grids. An independent
checker can regenerate everything from the repository and verify these
fixed lower inequalities without old temporary files. Receipt/artifact
identities in the certificate supply lineage only. The distinct checker
is separately owned; its acceptance/receipt is not this developer's work.
No theorem status or ID is assigned here.

## Retention and limits

Bulk baseline arrays and selected-source ell values remain under
`/tmp/padua-lanczos-frontier-g2`, manifested by path/byte size/SHA-256 and
regeneration commands. These are temporary working artifacts, not delivered
cold storage. Reproduction requires a new output directory and the pinned
python-flint dependency, with no polyrat checkout or historical bulk input.
Archival/delivery remains pending the orchestrator's prescribed procedure.

No actual working-precision PD-T055 conclusion, source activation,
probability lower bound, finite-epsilon uniformity or all-degree L2 proof
follows. Any SH_n extension needs its own weighted/gauge hypotheses and
independent mathematical work after accepted finite G2 checks. F remains
unimplemented and outside this run.
