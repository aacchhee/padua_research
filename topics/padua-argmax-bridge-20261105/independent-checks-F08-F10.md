# F08/F09/F10 — Supplemental mathematical-validity review

2026-11-07. Reviewer `/root/f01_math_review`; requested/API assignment
`gpt-6-astra`, high; actual serving model/effort metadata unexposed.
Rules/input `4a5de2012bad94601c713b2ff5517f2e3fb80af2`; observed starting
HEAD `61cf9ab5d143cea993ce2cde6d88302a6c10b7bc`. Read-only comparison of
AGENTS.md, WORKFLOW.md and CODEX.md to the assigned rules was unchanged.
Root owns Git, shared records, adoption and source/execution release.

## Final mathematical verdict and audit boundary

**F08 mathematical ACCEPT** at the
refreshed frozen scopes below: its two local supporting results are valid,
and the complete K<=100 target remains OPEN. One minor missing-domain
statement was corrected by the author with root authorization and refrozen;
the corrected statement and all final hashes were checked. No unresolved
F08 mathematical finding remains. **F09 mathematical ACCEPT** at the root-
confirmed frozen scope below, with no unresolved mathematical finding.
**F10 mathematical ACCEPT** for its fixed-premise, old-f/GRID conditional
tree transformation and separate discovery/retained key inclusions.
All eleven final input hashes were rechecked after root's final freezes.
No unresolved mathematical finding remains in these exact scopes.

This is exclusively mathematical validity, dependencies and edge cases.
It gives no independent novelty/priority/full-registry gate verdict,
protocol waiver or PR-readiness approval. Root explicitly assigned this
limited scope under WORKFLOW's scoped no-novelty audit exception. Earlier
unwaived chronology findings remain separate. Final Claude review is not
replaced by this supplemental audit.

## F08 reconstruction

Root confirmed the following final freeze, all hashes/bytes independently
matched. The original coefficient5545B SHA
`51ebec3ce5a0faad6c77f53bef4d30aa4fad2e96bec0221c628b721c2dbf5b4c`
and attempt4180B SHA
`a1ac2c8b07a761c4f42651d879662fb86b85e738a1e0ac94dca483b03dcff89e`
are superseded by the explicit-domain correction and its append-only
attempt disclosure, not retrospectively reidentified.

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F08-entropy-constant-coefficients.md | 5698 | `f6ceba152b2616f19920cddfb26807556f04ad5fbd5172aea1e6377a5e89dfd9` |
| theory/F08-entropy-constant-kernel.md | 4843 | `eb228da05d127433b4138e08c3315fcb5a8f1f568c74dce1c5f723596033a879` |
| theory/F08-entropy-constant.md | 5478 | `94427ac789f2f327ccfc7ab46cc63a6289fd99d6d6a556ca4bb372a6f592782c` |
| ideas/F08-entropy-constant.md | 7558 | `fde7544167fe043cd2dc5ed9b942f8b41cc40e8994e9c500065da53c671769c5` |
| attempts/F08-entropy-constant.md | 5482 | `75458d997208cfb06c491bfe26075016f948a09fc8b7b375925dbc913dc69902` |

The three theory files and both idea/attempt records were read in full,
including the final coefficient correction and attempt appendix. Fresh
full dependency reads include F04-entropy-cell, N1-round6-
central-log and E12-signed-outer-coupling; C06-far-compact-error sections
1–2 were read for the general entropy formulas and domain reconstruction.
E14-wide-signed-outer was read in full for the following F09 review. Earlier
accepted dependency reviews are retained as such, not independently rerun.
No full IDEAS/INDEX or independent novelty gate is claimed.

### Actual two-sided coefficient

For v<0, differentiating the same-sign entropy gives
`J_s=-log(-v)+log(2u)+o(1)`. For v>0 at a fixed interior e*, the root
regime holds near v=0. Rationalizing the derivative with
`(s cos e*)^2-D^2=s^2-u^2` gives
`J_s=log v-log(2u)+2log(tan e*)+o(1)`.
Integrating from the continuous value J(u,u,e*)=0 gives precisely

    |v|log|v|-(1+log(2u))|v|+2v_+log(tan e*)+o(|v|).

On the assigned balanced phase box, a>0 and an interior coefficient-zero
crossing has u>0. The actual tan curves have derivative magnitude
`(a/2)sec^2(e*/2)>0`; the absolute-value switch s_R=0 cannot coincide
with s_R=u>0. Thus v=kappa(e-e*)+O((e-e*)^2). At this fixed interior
point J_e=O(|v|), and the other terms defining B are smooth after combining
the exact J/R/log identity. The singular coefficient of B is |kappa|.
Neither the o(|v|) remainder nor the regular coefficient 2log(tan e*)
is asserted uniform as e* approaches zero.

Minor scope finding returned to root: the original coefficient statement
did not explicitly repeat the balanced-box/F04 phase guard. A full-C06
interpretation would be false: when alpha+beta=pi and p=q>0, a=0 and
s_L=s_R=u identically. Root authorized the author to make the intended
registered balanced-box guard explicit. The corrected frozen statement now
does so, also specifying separate absolute phases and 0<e*<pi/2. The
finding is CLOSED; it required no new bound or extension of the result.

### Uniform diagonal endpoint estimate

For c in[1/10,1/4], u=sin(c)/2 lies in[1/24,1/8], while a>=31/32.
For 0<e<=1/64, w=a tan(e/2)<=e<u/2. The exact profile identity gives
s_L=u+w,s_R=u-w,b_L=0,b_R=-2w,d=0. The origin subtraction is therefore
retained: the two B formulas are R(u,u+w,e)-qlog(pi-e) and
R(u,u-w,e)-2wlog(sin e)+qlog(pi-e).

The two explicit endpoint entropies H satisfy
`|H(u,u+/-w)-wlog w|<=4w`. For the plus branch the derivative of xlog x
has magnitude below three on the specified compact interval; for the minus
branch `(1-z)(-log(1-z))<=z` bounds the remaining entropy term. The generic
bound `0<=R_e<=2s` at fixed s yields `|R-H|<e`. The estimates for tan,
`|w-(a/2)e|<=e^3/6`, and `log(sin e/e)` then give the stated safe 10e
remainders, with opposite coefficients +a/2 and -a/2. The endpoint values
are -qlog pi and +qlog pi. No equality of their different Q offsets or
hole lengths follows from these opposite coefficients.

### Translated prototype cell and hole kernels

Scaling the crossing cell by x=c+hy gives the exact coefficient
`|theta|-(1/4+theta^2)=-(1/2-|theta|)^2` and the stated P primitive.
On[0,1], P lies in[-1/4,0] and ylog y in[-1/e,0]; hence |B|<=1/2.
This proves the crossing-cell bound uniformly at a sample or boundary.
The centered root has A=-1/4, so the leading logarithmic coefficient is
sharp. For an exterior root, f''=1/|x-r| is positive and decreases as the
root moves away. The positive integral-minus-midpoint Peano kernel makes
the endpoint limit maximal; the exact endpoint value is
`h^2(1/4-log(2)/2)`. This proves the h^2/8 bound by continuity, without
assuming a globally finite derivative variation across a root.

For the hole, scaling x=ell*y and subtracting ell*f_r(0) gives exactly
`A0=(1-zeta)^2-1/2` and the displayed B0. The same compact primitive
bounds give |B0|<=1/2. At r=0 the integral equals P(ell), establishing
sharpness of the coefficient 1/2. For exterior roots in[-pi,pi], distances
are at most 2pi. Absolute continuity and the weighted derivative integral
give constants 9/4 and 7/4 on the two sides, so the common 5/2 is safe.
All limiting equalities use the continuous exact primitive.

### Whole-target boundary

These are local coefficient and prototype-kernel supports. They do not
prove the complete balanced-box target K<=100 (or 50). The target remains
OPEN, with only F04's accepted K120000 feasibility bound available. In
particular no uniform joint residual in |alpha-beta|/h, nonlinear entropy
coordinate remainder, complete unequal-grid budget or four-hole residual
budget has been supplied. The file's OPEN/deferred dispositions preserve
those missing obligations rather than promoting the supports to a whole
operator result.

## F09 frozen inputs and complete reconstruction

Root confirmed the final three-file freeze. All three files were read in
full and their hashes and byte counts independently matched:

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F09-outer-em2.md | 21124 | `3511dc24e66eef691efd0ae019fec016cd4d1b44a3179bddfb3fec847a7c8a91` |
| ideas/F09-outer-em2.md | 5673 | `d52b6cb638335ed21a5c2f43bec9da0d22dc278b1021bd9fe2b5f9f76214c457` |
| attempts/F09-outer-em2.md | 4688 | `bfd92cf0bdcac152b5d56593a60cb17816e7bf71d463a13fe899aa8ceed1dd1b` |

The accepted claim is the full literal T expansion with explicit phase-only
Gamma_T and K41000 for every n>=32 and CLOSED signedrho<=1. It includes
Rlog and excludes Rmesh, ordinary/retained row errors and origin conversion.
It is feasibility, not a useful onset estimate or a whole finite-error bound.

The frozen proof's endpoint
inventory and proposed Gamma_T algebra check against E12/E14: the max-profile
endpoint charge A equals 2p+(2t-1)q for p>=q and (1+2t)q for p<q. Thus
`-A+q(2t-1)+2d=-2p`, including axes and equality. The B endpoint terms
combine with the two exact log-Gamma product constants to give the stated
q and d coefficients in Gamma_T. In detail, the pole endpoints are w,-w
and the common Pc; evenness AND periodicity identify the two central
values. The entropy endpoint H is the finite generic J remainder, including
its continuous p=q and double-zero values. Both initial B values are
-dlog pi, and the central values are H-/+qlog pi. These produce every
boundary term in (G), with no presumed equal offsets or omitted initial log.

### Entropy estimate through the missing origin band

The new proof explicitly rechecks F04's premises without its lower-rho
guard. On the full closed diamond, a>=49/64, a-(p+q)/2>=17/64 and the
tan-curve slope magnitude is at least a/2>1/3. The quartic leading
coefficient remains negative at u=0, so its root count never becomes an
identically-zero exception. The right absolute-value branches share the
same quartic. The coefficient-zero and absolute-value sites and both
endpoints stay in the feature ledger; coincident sites reduce the count.

The generic R formulas give the same integrable logarithmic derivative
envelope. At u=0 R and its derivative terms vanish directly; no inverse-u
limit is used. The polynomial critical equations and their identically-zero
cases justify finite monotonicity counts for the truncated variations.
Restriction to disjoint retained intervals charges only variation inside
them. The remaining derivative-factor jumps and the artificial half-interval
join are explicitly charged. Thus the 400log(6/v) truncated bound is valid
without global finite Var(B'). The original bad-cell count, crossing-cell
modulus, actual four hole lengths and boundary corrections then reproduce
K120000 uniformly down to rho=0. This is a proved extension, rather than
an unstated inference from the previously accepted band.

### Max and pole profiles, with their derivative atoms

The boundary-corrected BV-derivative lemma uses the actual centered cells
and the endpoint-subtracted holes. Its two contributions are
`pi Vsum/(8m^2)` and `13pi M/(2m^2)`; the hole-square bound is valid for
both offsets throughout[0,1]. For the max profiles, the initial half is
strictly inactive. On the central half, |Z'|<=2 and Var(Z')<=1. Monotone
changes among branch slopes 0,-1,-2 charge all switches, also when they
coalesce or lie at a sample. Vsum<=12 and M<=2 safely yield 64/m^2.

For the pole profiles the full periodic measure bound, including the
negative atom, gives Var(V_s')<=16. Near zero the intact quotient
`(V_s-V0)/z=integral_0^1 V_s'(vz)dv` gives bounded first and second
derivatives from the smooth principal-period third derivative; all shifted
arguments stay in that period. This avoids a false singular 1/z estimate.
The initial P_s' variation is below16 per side. On the central half the
three differentiated products cost at most24,10,2, with every atom in
the V_s' product counted. There is no joining jump at pi/2. Consequently
M<=12,Vsum<=104 give the conservative paired 400/m^2 bound. This BV
claim is about P_s', not the entropy derivative.

### Uniform finite logarithms and total error

The finite Gamma products preserve exactly m-3 samples and all four holes.
The real Stirling remainder is justified by the written positive Binet
integrand bound: its bracket lies between zero and v/12, giving remainder
between zero and 1/(12x). For x=m+c, c in[-2,0], m>=33, the log(1+c/m)
remainder is uniform: the linear cost is at most 5/m and the logarithmic
and Stirling costs are below 3/m and 1/m. The safe 10/m^2 individual Q error
therefore holds for every offset, not just fixed phases. All Gamma
arguments are positive with the stated lower guards.

Combining the two initial log constants gives the q coefficient in (G).
Combining the two central log constants with +4dlog pi from the B endpoints
gives the d coefficient `log(2/pi)-logGamma(2-t)-logGamma(1+t)`.
The weighted log errors are below14/m^2; changing logm to logn in the
uncancelled coefficient costs below2/m^2. Shift retains its entire accepted
beta(17L+27)/m^2 allowance and contributes no first-order coefficient.

The complete aggregate is therefore at most

    [40000(1+logm)+81logm+443]/m^2
                           <=41000(1+logm)/m^2.

All axes, p=0, p=q, zero phase, moving/coalescing features, sample equality
and degree parities are included by the uniform proofs and exact conventions.
No fixed-phase asymptotic is used as a moving-phase bound. Gamma_T is
finite, continuous at the entropy degeneracies and phase-only; at zero
it and the exact T vanish. No other component of the finite telescope is
silently absorbed into this theorem.

## F10 frozen inputs and conditional proof

Root confirmed the following final freeze; all three files were read in
full and hashes/byte counts matched:

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F10-prune-contract.md | 15074 | `9f003a9979eb4febf41efdab75148c176281bcbcc6ecaeeeb6f36bc95075dafe` |
| ideas/F10-prune-contract.md | 5440 | `5429270f3cf81c8fd621a5697baf2502fdc7c598c00d86eaafb95949ea3ad4e2` |
| attempts/F10-prune-contract.md | 6839 | `f030974e82f4a2f67577f072dbda0a1db94e2c4f5be339f657f6aeb8de71fd57` |

For this conditional proof,
fresh full TEXT-only reads cover D19-adaptive-norm, final_hybrid_engine's
SPEC.md, checker.py and producer.py. The engine.py grid/cache/discovery/
final-norm block was also read; no full engine/runtime audit is claimed.
The checker, producer and SPEC hashes match the source identities recorded
in the attempt. This is a mathematical-contract check, not implementation
approval or a fresh review of numerical/runtime code.

### Guard and fixed-premise coupling

For positive-width raw unit boxes, the clipped closed triangle patch is
nonempty precisely when the raw lower sum is at most one; equality is
retained. The proposed lower bound 2/5 gives rho>=2pi/5>5/4 because
157/50-25/8=3/200>0. Thus the complete physical patch lies in F07's
closed domain at n>=256, including tangencies; below256 the E15 guard
is unchanged. The old predicate implies the new one. This argument uses
raw geometry, not canonical folded vertex membership or a sampled center.
The strict analytic gaps compare the same S with true Lambda_c, not the
rounded origin lower L.

The existing source processes OUTSIDE, then analytic, then vertex queries.
It computes all13 canonical grid premises and Mcoarse before discovery,
and supplies that norm throughout traversal. Canonicalization folds
above the hypotenuse and reverses coordinates only on it; it is idempotent
and preserves values without changing raw widths or guards. In the theorem's
fixed extensional enclosure map, any surviving common box therefore has
identical vertex keys, values, numeric predicate arguments and outcome.
A failed numeric node consequently uses the same weighted split, exact
midpoint, tie rule and children. Different fresh enclosure results are
explicitly outside this hypothesis.

### Structural induction, final norm and distinct key sets

Induct on binary paths of the finite old source-generated tree. At an
outside node both rules stop. At a newly eligible analytic node the new
tree stops before querying and replaces the complete old subtree. Otherwise
both procedures query the same keys and either accept the same numeric
leaf or recurse into identical children. This proves every new numeric
query path and final numeric leaf is an unchanged old one; no old parent
numerical estimate is transferred to the new analytic parent. Closed
coverage follows because each replacement covers its full parent patch.

The old-f assumption is sufficient to retain final GRID: an old f survives
or has a newly analytic ancestor. All13 grid values remain, so the final
norm and L are unchanged. The surviving numeric and corner witnesses
therefore retain their exact accepted premises. D19 TREE absorption is
not invoked on an incomplete sampled cover, and no unconditional norm
switch or new fresh-verification success is inferred.

Taking key unions over surviving query paths gives Dnew subset Dold;
taking them over surviving final nonempty numeric leaves gives Qnew subset
Qold. Both unions still include the mandatory grid. Internal-node-only
queries belong to D and need not belong to Q. Shared/canonical/grid keys
are counted once, so a deleted occurrence is not automatically a saved
key. Strict reduction and an ordered first-query subsequence are correctly
not claimed. Under source-generated-tree provenance, the old preorder
does identify which nodes reached the query step, so the conditional
data-only reconstruction consequence is also valid without inspecting
numerical values. No such reconstruction was executed here.

These checks support only the proposed finite mathematical witness
transformation. The unchanged parser still recognizes the old guard and
descriptor. Source integration, replay, resources, certificate size, actual
call success, performance, new finite degrees and global onsets remain
outside this review.

## Activity

Only text reads/searches, hash/byte metadata, collaboration and this owned
review-file write. No scientific script/import, numerical calculator,
scalar, degree, phase, endpoint, native, quadrature, compiler or fixture
job. Ordinary tool overhead is unmeasured. No author/shared/Git edits.
