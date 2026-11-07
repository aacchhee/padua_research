# Supplementary independent check — D03 cancellation perturbation

Rules/read input: `084a64f6465956f9c75b5538f83752c30318f151`;
observed review HEAD `f1ba23cfbfb557dd491730f9837f5efe413e7c75`.
The AGENTS/WORKFLOW/CODEX and state/IDEAS.md diff between those commits
is empty. Reviewer: distinct Codex subagent `/root/d01_far_review`,
parent-requested Astra xhigh, actual serving metadata unexposed.
This supplements the still-pending formal Claude audit.

## Verdict and frozen scope

**ACCEPTED at the stated supporting-lemma scope. No unresolved finding.**
The difference quadrature bound is proved with its stated constants and
full phase/degree quantifiers. It does not bound the symmetric reference
error itself, the full S_n-M_infty remainder, or a useful global onset.
Those targets remain **OPEN**, as the developer records state.

Read in full and hash-checked:

| Record | SHA-256 |
| --- | --- |
| [D03-cancellation-perturbation.md](theory/D03-cancellation-perturbation.md) | `3b4d989393eb942b5527be32f89254fcef6b3b3cc157a37960848780c74d290f` |
| [D03-joint-finite-h idea](ideas/D03-joint-finite-h.md) | `6e53af24e65cfdea37f26656acb1fb7bd936664717901da782954f189c7c7f1a` |
| [D03-joint-finite-h attempt](attempts/D03-joint-finite-h.md) | `da316176177dd984326de390e9d8c086096403cff2226182df0dd35c24e19dfa` |

No developer edit was requested or made. The review owns this report only;
no Git action, shared record, source proof or evidence file was changed.

## Independent mathematical reconstruction

**Pointwise sandwich, including coefficient flips.** Let A=|w|. For A>E,
the perturbed coefficient signs match (-w,w). On arcs where cot x and
cot(x+v) have opposite signs both cancellations vanish. Otherwise their
minimum magnitudes lie between (A-E)min(|X|,|Y|) and
(A+E)min(|X|,|Y|), so the difference is bounded by 2E min(|X|,|Y|).
For A<=E, the perturbed cancellation has magnitude <=4E min(|X|,|Y|)
and the reference <=2E min(|X|,|Y|). Both are nonpositive, so their
difference costs the larger magnitude, not their sum. This covers sign
flips, zero coefficients and w=0. At E=0 the two functions agree exactly.

The shorter circle distance between the poles is e. By the triangle
inequality, at least one sample distance to its corresponding pole is
>=e/2; hence the smaller cotangent magnitude is <=cot(e/2). This proves
the stated M=4E cot(e/2). At a pole, the other cotangent is finite and
the min-channel expressions have finite one-sided limits. Assigning both
g values zero there makes f zero without asserting polynomial collision
values for either individual cotangent channel.

**Six arcs and derivative count.** The union of two poles, two cotangent
zeros and at most two perturbed numerator zeros has at most six points
on the pi-circle. Multiplication by sin x sin(x+v) gives exactly

    [(C+D)sin(2x+v)+(C-D)sin v]/2.

Because sin v is nonzero, an identically zero numerator requires C=D=0.
The reference numerator is the constant -w sin v and adds no roots;
w=0 simply removes that reference function. Coincident roots/zeros/poles
reduce the partition count, including e=pi/2.

All absolute-value signs are fixed within each open arc, so f is
b1 cot x+b2 cot(x+v). For opposite-sign nonzero b1,b2 its derivative
vanishes only when [sin(x+v)/sin x]^2=-b2/b1. The unsquared ratio has
constant sign on the arc and derivative -sin v/sin²x, with no zero;
its square is strictly monotone. Thus there is at most one stationary
point. Equal-sign or single nonzero coefficients give a fixed derivative
sign; both zero give a constant function. These cases justify at most
two monotone pieces per arc without differentiating across a moving zero.

Each monotone piece has variation <=2M. Six arcs therefore cost <=24M.
At either pole the route through the assigned value zero costs at most
|f_-|+|f_+|<=2M. Both poles add at most4M. Every other breakpoint is
continuous. Therefore the full periodic variation, including point values
and pole jumps, is <=28M=112E cot(e/2)<=224E/e. No root separation,
inverse-a factor or positive lower coefficient bound was used.

**Shifted mesh and ordinary-row normalization.** The centered-cell BV
inequality gives one half of the periodic variation for the sample-sum
minus n/pi times its integral. Every allowed sample is a continuity point;
numerator and cotangent zeros are harmless. Pole jumps inside cells remain
charged, and assigning values at unsampled poles does not change the
integral. Hence the exact difference of the two quadrature errors is
bounded by 56E cot(e/2)<=112E/e. There is no omitted mesh-spacing factor:
this is a bound for the unnormalized row sum.

For the actual coefficients, |(p-q)/4| and |(p+q)/4| are <=P/4.
Putting E=P/4 gives 28P/e_r per row. N1-02's actual special set excludes
the endpoint rows, central rows m-1,m and every sampled polynomial pole.
For r<=m-2, the distances to 0 and pi are respectively at least
pi*r/m and pi*(m-r-1)/m; the stated right-half k,l bounds follow in the
same way using 0<=beta<=pi. Thus

    1/e_r <= (m/pi)(1/k+1/l),
    sum_outside_A_R 1/e_r <= 4m H_n/pi.

Each positive k and l occurs at most twice and is <=n. Division by nm
gives exactly 112P H_n/(pi n), which is <=56P H_n/n since pi>2.
Summing absolute row bounds first also proves the result for any subset O.
No n>=8R or endpoint-strip condition is required here: all n>=2 and
2<=R<=n are allowed. Empty ordinary sets, including n=2,R=2 and R=n,
make the assertion immediate. The bound vanishes when P=0. Extension
uses the declared absolute-phase convention and phase reflections,
preserving the actual unequal meshes; no n/m exchange is involved.

## Whole-kernel collision diagnostic

The attempt's exact example is correct and has a separate scope from
the lemma. At n=4, m=5, alpha=3pi/5, beta=0, r=2, j=1, the odd-board
condition holds and u=v=2pi/5. Setting t=pi/5 gives a=sin²t,
p=sin(2t), C=0 and w=p/4>0. Consequently the unweighted symmetric
whole-kernel term -w cot((u-v)/2)+w cot((u+v)/2) has a genuine pole.
The actual corrected polynomial is finite.

An additional exact approach check makes that distinction explicit.
Hold beta,r,j fixed and write alpha=3pi/5+s. Then (u-v)/2=s/8,
C=s/4+O(s²), and D tends to p/2. The actual row expression therefore
tends to `2+cos(2pi/5)/2`, while the unweighted symmetric reference
has leading divergence `-2p/s`. Nearby noncollision rows do not remove
this obstruction to that naive whole-kernel comparison. Exactly at the
collision the row is special, so it is outside the lemma's quadrature
claim. Bounded g0 and g-g0 remain valid; no contradiction arises.

This verifies the illustrative reason for abandoning only the naive
whole-kernel subroute. It is not a new PD-N claim, a rejection of all
weighted references, or a failure of the retained perturbation lemma.
The N1 pole-product warnings already require keeping vanishing
coefficients with their poles and retaining actual polynomial rows.

## Dependencies, novelty gate and coverage

Read the complete D03 records above, the full
[N1-02 cancellation source](theory/N1-cancellation-quadrature.md),
[N1-03 endpoint source](theory/N1-endpoint-tail.md),
[N1-09 near-only source](theory/N1-round5-jumps.md), and full
[N1-outer](ideas/N1-outer.md) and [N1-endpoint](ideas/N1-endpoint.md)
candidates. The review reconstructed the relevant BV inequality,
actual mesh/collision exclusions and harmonic count directly. N1-09's
positive-numerator restriction is a comparison only and is not imported.
Earlier full source reading and exact normalization checks of N1-07,
D01, D02, the corrected kernel and the closest IDEA336/337/459 records
are documented in this same worker's
[D01 review](independent-checks-D01-far.md) and
[D02 review](independent-checks-D02-far.md); they were not newly reaudited
in their entirety for this bounded D03 lemma.

The complete 1112-line state/IDEAS.md read in D01 is unchanged, SHA-256
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
This continuation refreshed searches for symmetric/equal-opposite
references, difference quadrature, perturbation, sign partitions and
cancellation. N1-03 is the direct mechanism predecessor: it subtracts
the same reference at the integral level. D03's precise added property
is the variation and finite-mesh quadrature bound for the difference,
which retains P and eliminates the old fixed-R floor for that difference
only. N1-02 supplies the underlying BV method. The idea correctly records
this as a continuation with a separable property, preserves the deferred
phase-relative and smooth-Taylor alternatives, and claims no historical
priority or external source theorem. Its disclosure that the preliminary
paper sandwich preceded the written candidate, after the gate, is retained.

The separation test succeeds for this supporting result. It would fail
if the two cancellation functions were bounded separately, since that
would restore the symmetric a-dependent term; the proof explicitly avoids
that loss by controlling their difference. This does not complete the
separate finite-n matching of T0, endpoint rows and E_infty.

## Execution and remaining obligations

Analytical review only. Tools read/search the named records, checked hashes
and unchanged rule/registry diffs, and wrote this report. **No scientific
numerical run, native executable, full-board sum, quadrature, fit, Python
mathematical helper or generated receipt was executed.** No computation
is a premise, and no measured CPU total or instrumented analytical elapsed
time is asserted. The developer's recorded timing limitation remains.

The remaining mathematical work is the explicitly OPEN joint symmetric
reference/endpoint matching and practical whole-remainder bound. Its
fixed-R error or cutoff losses cannot be declared solved by (4). Formal
Claude audit and publication/registration checks remain separate.
