# D06 model-budget obstruction — distinct mathematics and scalar review

2026-11-06. Rules/review head
`f9b64a6351b58c40f3432b80dd4b24f88ab1c477`.
Reviewer: Codex, distinct agent `/root/d01_corner_review`, parent-requested
`gpt-6-astra`, high; serving model/effort metadata are not independently
exposed. Author allocation: Sol xhigh. This supplementary review does
not replace the formal cross-provider Claude audit.

## Verdict and scope

**ACCEPTED. No BLOCKING, MAJOR or MINOR findings.** The analytic negative
statement is proved for the specified frozen positive allowance, and the
scalar source faithfully evaluates that allowance. The 40 actual-phase
rows remain **MEASURED** planning values. The eight uniform rows are
conservative upper endpoints under Python Decimal's stated arithmetic
contract and the reviewed source; they are not sampled phase proofs.

The negative statement does not lower-bound the true approximation
error. It does not refute D05, M_infty, sharper local/relative estimates
or an argmax theorem. No future all-n passing threshold is inferred.
The existing global threshold remains 500000.

The one preregistered independent scalar review passed in
**0.314731976 process CPU seconds**, including imports, exact controls,
independent formulas and a fresh author replay. The replay's internally
reported CPU was 0.077154451 seconds. The original CSV was not changed.

## Frozen identities and gate

Directly checked input SHA256 values:

| File, relative to this topic | SHA256 |
| --- | --- |
| theory/D06-budget-obstruction.md | `c6a84753661475cb9cea9dad86a9395034fe723a7a46425bae4c8ac7b09ff605` |
| ideas/D06-model-budget.md | `6fc5b323b7f129252eb020179b82ff21643fcc0ec14873427d4faa93b978da04` |
| attempts/D06-model-budget.md | `15a9bb50960f2970246d30a32ba953bf691751e893d4c2ac22897504203ba6d5` |
| code/post_audit_D06_model_budget/evaluate.py | `9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413` |
| code/post_audit_D06_model_budget/evidence.csv | `52dfbb5b3babe61f71a76566428eb40e44b0145a56892874543af97fa0bd0566` |

The accepted D05 sources also match their review:

| Dependency | SHA256 |
| --- | --- |
| theory/D05-outer-comparison.md | `d862ab5071de128577773b4a658c6c70f2859e2b2ff083074909372041ec7502` |
| theory/D05-outer-profile-variation.md | `47fc61298520609f591c03eea323e93949d59d54cbcfa90e0d4943548113bd66` |
| independent-checks-D05-outer-comparison.md | `dd0cc60b9d84b6b288d2d508ee60f032d63e2a1fb6b20d36fdda51a2f39e7276` |

AGENTS/WORKFLOW/CODEX were read in this agent session; the rules-only
diff from the preceding 41c4c80 review to this head is empty. Root alone
owns Git/shared records. Because a negative claim is classified here,
the full registry gate is retained explicitly: this agent previously
read all 1112 lines of state/IDEAS.md and every obstruction/disposition
table. Its refreshed hash is still
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
No new full line-by-line reading of identical bytes is claimed.

Fresh searches covered budget, allowance, positive errors, floors and
endpoint constants in the registry, D05 idea and N1 endpoint source.
Read all D06 inputs in full, both D05 proof files, its complete accepted
review and candidate, D02's exact scalar/interior definitions and
topology, C02's projected-floor theorem, and N1-round4-budget.md.
Earlier full D04/N1/C06 and D01 obstruction readings remain in this
same reviewer session. Broad output truncation was followed by narrower
reads of the missing D05 review/candidate passages.

Closest negative predecessor N1-round4-budget obstructs a different
uncancelled E_(n,R)+e4 certificate through n<=10^6 by balancing R.
D06 instead fixes R=2,delta=pi/8 and examines D05's newer shrinking
joint allowance. It is a quantitative application and scoped mechanism
failure, not a new principle or historical novelty claim. The developer
already gated and accepted D05; D06's parameters and scalar matrix were
recorded before its run. No external literature theorem is transferred.

## Independent analytic reconstruction

With R=2, N1/D05's row formula becomes exactly

    e_rows=(4+L)/n+3[(59+6L)/n+7200/n^2]
          =(181+19L)/n+21600/n^2.

All components of the frozen B_n are nonnegative on n>=32. In
particular X=(n+1)/8>1/2, every logarithm used in the positive mesh
and collision allowances has its stated positive argument, and the
strip terms retain positive W_P/Q bounds. Thus B_n>=e_rows at every
phase, regardless of a or P. Differentiating e_rows gives the author's
strictly negative derivative for all real n>=1. At n10000,
log n>9 implies e_rows>352/10000>1/32; at n4096, log n>8 implies
e_rows>333/4096>1/16. Positivity of the omitted n^-2 term preserves
strictness. Monotonicity gives the entire stated integer ranges.

For the exact radian phase alpha=beta=1/4, a=cos(1/4)>=31/32.
Substituting delta=pi/8 into the interior logarithmic coefficient gives

    VA/2+9Astar = 9/pi+640a/pi^2 >257/4.

The coefficient 640 includes both the 64 from VA/2 and the 576 from
9Astar; no half or pi factor is missing. The other nonnegative pieces
give Vstar>=6, VV>=23, Jstar>=5 and VJ>=20. Therefore

    VW/2+5Wstar+4Vstar
      =VV/2+VJ/(2pi)+9Vstar+5Jstar/pi
      >=131/2+35/pi >297/4.

The central-log charge is nonnegative (and d=0 at this phase). Hence
I_n>[257log n+297]/[4(n+1)]. Its derivative numerator is
257(1+1/n-log n)-297<0 for n>=32. Evaluating the lower endpoint of
this decreasing comparison at n10000 gives
1305/20002>1/16. This proves the quarter-phase obstruction throughout
32<=n<=10000 without using any floating values.

The elementary logarithmic lower bounds are justified independently
by e<11/4: the series through 1/3! is 8/3 and the tail is at most
1/18, strictly below 11/4 in total. Exact rational powers give
(11/4)^9<10000, (11/4)^8<4096 and (11/4)^3<32. The sine/cosine
bound for a and pi<4,pi^2<10 have the required directions. Exact
rational controls reran these final comparisons, but the proof remains
analytic rather than a finite-degree numerical extrapolation.

C02's usable projected floors are restricted to noncorner odd centers,
their physical coordinate guards, and |alpha|+|beta|<=1/2. The 1/32
floor starts at n160 and the 1/16 floor at n4096. D06 correctly keeps
its formula inequalities at n>=32 distinct from those applicability
conditions. The quarter phase lies on that near-domain boundary;
the other sampled far phases do not acquire a defect floor from it.

## Formula/source correspondence and uniform substitutions

All 13 saved numeric columns were traced to D05/D04/D02. E_D04 retains
the harmonic H_n and the full 352P/(3pi) coefficient; its pole share
is not silently replaced by a phase-local improvement. e4 adds its
mesh, finite-row and collision shares once. I_n retains the complete
interior missing-cell/special-row charges. The additional D_pole is
the separate conservative interior-special allowance; it is distinct
from the ordinary share already paid in E_D04. T_Z is added once,
with four printed components, and no old fixed Q(P,delta) floor.

For an independent implementation the four T_Z parts simplify to

    [32+6log(4m/pi)]/(2m),
    (5/m)[7+(P/pi)(5+2log(8m/5))],
    [7+(P/pi)(3+2log(32m/(m-4)))]/m,
    (2/m)[7+(P/pi)(3+2log(2m))].

These were coded separately in the reviewer, together with the
simplified e_rows and interior coefficient, avoiding a direct call to
the author's components function for the independent comparisons.

Actual phase inputs use a=(cos alpha+cos beta)/2, p=sin alpha,
P=sin alpha+sin beta, d=(sin beta-sin alpha)_+, and the absolute value
of the complete N1 weighted U0. The author does not replace d by a
symmetric value or interchange meshes. At the symbolic midpoint,
a=0,p=1,P=2,d=0,U0=1 are entered exactly, retaining Phi_0(integer)=1.
Other phase values are floating evaluations of exact rational radians,
correctly labeled MEASURED; they are not certified trigonometric inputs.

For the uniform envelope, a<=1,p<=1,P<=2,d<=1,|U0|<=8 and
H_n<=1+log n are valid jointly as independent upper bounds. N1's
weighted numerator estimate explicitly supplies |U0|<=8. All formula
coefficients multiplying these inputs are nonnegative. For the only
less immediate term, g(u,S)=u[1+log(1+S/u)],

    partial_S g=u/(u+S)>=0,
    partial_u g=1+log(1+S/u)-S/(u+S)>0,

with continuous zero limit at u=0. Maxima and positive sums preserve
monotonicity. Thus substituting the independent maxima gives a true
uniform scalar upper without claiming simultaneous attainment.

## Decimal and Machin source review

The interval branch has no binary-float constants or divisions. Integer
and decimal-string conversion to Decimal is exact. Its injected unit
pi/pi may widen dependency-sensitive expressions but still encloses 1.
Every addition, subtraction, product and quotient is computed in an
explicit local precision-50 context with FLOOR for lower endpoints and
CEILING for upper endpoints; multiplication/division take all endpoint
pairs. Divisors avoid zero in the actual evaluations. Negation uses
copy_negate, avoiding ambient-precision rounding. The limited square
operator is multiplication of the interval by itself; its uses here
have positive arguments. imax takes the endpoint maxima correctly.

Decimal ln is correctly rounded with ROUND_HALF_EVEN independently of
the requested context rounding. The code does not mistake a FLOOR
context for directed ln: ilog evaluates the endpoint logarithm at
precision 50, then uses next_minus/next_plus in that same local context.
The adjacent neighbors enclose the exact real logarithm by correct
rounding and monotonicity. It therefore encloses the real function,
not merely a value in the ambient Decimal context. The final quantize
explicitly rounds upper endpoints toward +infinity to 12 decimal places.
The reviewed finite operands are far from overflow/underflow limits.

The rational arctangent series alternate with decreasing magnitudes;
their partial sum and partial sum plus next term enclose each atan.
For the negative Machin term the bound direction is reversed, producing
pl=16*a-4*d and pu=16*b-4*c. The identity itself follows from
tan(4atan(1/5))=120/119 and the subtraction formula with 1/239,
whose result is 1 in the correct angular branch. Hence the combination
equals pi/4 before multiplication by 4. Directed Decimal conversion
of the rational endpoints preserves the resulting pi enclosure.

The source audit supplies these arithmetic guarantees. The high-precision
floating controls below corroborate implementation behavior; they are
not a substitute for the directed-arithmetic argument. Trusted software
includes Python Decimal/libmpdec's documented arithmetic/ln contract.

## Independent run and small-artifact manifest

Preregistered scope before execution: one exact-byte replay into a
temporary directory, exact rational threshold/interval/log controls,
and independent recomputation of all 48 scalar rows; aggregate cap
10 CPU seconds, no native, kernel, board, quadrature or new-degree job.
The reviewer script imposes CPU soft9/hard10. The replay writes beside
its temporary copied __file__, never to the original evidence path.

Executed once from `/workspace/padua_research`:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D06_model_budget_review/check.py

Result: **PASS**, 654 checks. Exact categories: 12 signed interval
primitive checks; eight rational-series logarithm containments; the
log(1) endpoint case; six rational threshold comparisons; exact Machin
endpoint conversion. Operational/control categories: byte-identical
fresh replay, original-evidence preservation, 520 independently
recomputed MEASURED component strings, and 104 uniform-component
comparisons at 160 decimal digits. The interval and ln tests deliberately
used ambient precision 7 with ROUND_UP; all passed. Rational log controls
used the atanh series after power-of-two reduction, with an explicit
positive remainder bound after 80 terms. They are exact containment
tests, not comparisons against another floating logarithm.

Each independently computed uniform component lay below its saved
upper endpoint, by less than 1.0001e-12. This control agrees with the
final upward decimal quantization. The uniform total at n50000 is
0.061683200166<1/16. At n100000 the saved upper is 0.032158091315,
above 1/32, so that saved enclosure does not certify the smaller budget.
No monotonicity of the complete passing bound is inferred from these
eight degrees. Author historical CPU 0.097311284 is a reported record;
the review's separate measured timings are given above.

Environment: Python 3.12.14 (Clang 22.1.3), Linux x86_64/glibc2.41,
decimal 1.70 with libmpdec 4.0.0, mpmath 1.3.0. No seeds or randomness.
The process timer starts before scientific imports; interpreter startup
and a later read-only version query are outside that timer. The observed
run is well below the 10 CPU-second cap. No failed or retried scalar
run occurred.

| Local artifact relative to this topic | Bytes | SHA256 |
| --- | ---: | --- |
| code/post_audit_D06_model_budget_review/check.py | 6727 | `b5c6f6ef38f67886888e4b17614aa99ac5519b0fb3196a49e1b1e214abfc1098` |
| code/post_audit_D06_model_budget_review/receipt.json | 1144 | `e739fae5269dba450e9e3c924bde9b75dbc9fcd678677572900b5ce3939a4f18` |

These are small review source/receipt artifacts, submitted to root for
integration. Their source head is the rules/review SHA above; the source
and input hashes in this report identify uncommitted review work and
the frozen author inputs. The generating/checking command is the one
shown above, and its receipt is PASS. The temporary replay CSV was
compared byte-for-byte with the original 11121-byte CSV and removed
on temporary-directory cleanup; its identical hash is recorded in the
receipt. Reproduce with the stated Python dependencies and command;
timing fields and receipt hashes naturally change on regeneration.
Retrieve retained artifacts from the listed repository paths and verify
their hashes. No remote cold-storage delivery or long-term archive is
claimed; root owns retention/integration. No large artifact is required
for the analytic obstruction or the independently reproducible controls.

Only this report and the disjoint reviewer code/receipt were written.
No author file, old proof, source, CSV, shared record or Git state was
changed. Formal Claude audit and any proposed new budget/cancellation
mechanism remain separate obligations.
