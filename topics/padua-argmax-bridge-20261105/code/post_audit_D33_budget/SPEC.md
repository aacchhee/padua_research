# D33 sole fixed2048 pair of directed far gates

Status: **UNEXECUTED**. This source/proof/SPEC freeze needs distinct
prerelease review, publication and explicit ROOT RELEASE before any
scalar/control/source execution. Accepted D30 supplies the all-n
sufficient implication; BOTH fixed endpoint signs remain uncomputed.
Global2048 also depends on D31's separate near endpoint/fresh result
review. D31 prerelease acceptance is not its numerical success.

## One case and command

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D33_budget/evaluate.py --run-once

PRIMARY N2048 ONLY, BOTH inner and outer gates in the SAME one shot.
No alternate case, degree/phase/threshold preview/scan, parameter,
precision/source/cap rescue, retry or fallback. Exclusive directory

    local-output/argmax-bridge-20261105/post-audit-D33/budget

consumes the attempt even on failure. Do not delete/reuse it. Preserve
registration, complete first receipt and first failure/observed kill.
No near source is imported or evaluated by this FAR-only program.

## Literal complete formulas

For n2048,m=n+1,L=logn,H=1+L,b=4/pi²,r=log(5/2)+1/18 compute

    D=[(52/pi²)H+7]/n+10/n²+20H/(pi*n²),
    KD=[352H/(3pi)+2/pi]/n,
    MA=1/pi+4/pi²,gpar=1+log(2+8m/(3pi)),
    VB=23+[3gpar+14logm+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg
                                      +4logpi/(pi*m)+16/m,
    endpoint_rows=(181+19L)/n+21600/n²,
    central_rows=(12+2L)/n,E6old=endpoint_rows+central_rows,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n²-1)
             +b/(2n-1)²+[5+b(log(n+1/2)+2)]/[4(n-1/2)²],
    W=[3logm+log2+2logpi+2]/(pi*m),
    Cbase=D+Gg+Mesh+W,Cnew=Cbase+E6old,
    G0=[(28/pi²)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n²,T=(4L²-3L)/pi²,
    A=14/n+90/n²,Kinner=KD+(10+L)/n+4/n²,
    u0=191/6144,ueta=2277/32768,
    s0=sqrt(191/768),seta=sqrt(2277/4096),
    inner_row_charge=A*(1-u0),inner_phase_charge=Kinner*s0,
    inner_allowance=Cbase+inner_row_charge+inner_phase_charge,
    inner_margin=u0*(T-11),Fin=inner_margin-inner_allowance-E0,
    outer_phase_charge=KD*seta,outer_allowance=Cnew+outer_phase_charge,
    outer_margin=ueta*(T-25/2),Fout=outer_margin-outer_allowance-E0.

Record ALL39 outward intervals, including minimum_gate as the
monotone interval minimum of Fin and Fout, plus pi; no endpoint
value/charge is removed to shorten output. The inner and
outer true-constant coefficients are EXACT11 and25/2 respectively.

These are EXACT accepted D30 formulas. OuterCnew retains the OLD
GLOBAL four endpoint AND two central row charge. Inner retains the
NEW actual wide-six-row bound and a=1-u through A*(1-u0). EVERY
ordinary/GLOBAL regular-quadrature/mesh/log/ACTUAL-origin error is
retained unchanged. E0 is not a completed-limit origin or U0=0.
The same corrected polynomial, exceptional x mode, actual finite
collisions and matched C2 remain; no D20 telescope term is deleted.

PASS iff all25 exact controls are true,T.lower>25/2,Fin.lower>0
AND Fout.lower>0. Missing either sign is a first gate failure, with
no alternative run. No separate control/preview execution is allowed.
Controls check fixed2^11/log/T lower, both root squares, outer cosine
lower, wide row denominator/reciprocal/displacement/H/sine/central
weights and six-row constants, inner Young/11 constant, old global
endpoint/six-row constants and central/origin guards. They do not
replace the accepted D30 domain/operator proofs.

Accepted D30 already proves T(2048)>129789/6250>25/2>11 and
BOTH gates strictly increasing on realn>=2048. Positive endpoint
signs yield full FAR exclusion for EVERY integern>=2048, including
both closed regions1/2<=rho<=3/4 and3/4<=rho<=pi. Seams, axes,
vertices,a0 and actual polynomial collisions are included. This is
not an isolated2048 certificate or a numeric proof of all-n monotonicity.

## Arithmetic, identity and hard resources

Only code/data identities are executable pins. The helper is

    code/post_audit_D06_model_budget/evaluate.py
    bytes6126
    SHA2569ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413.

Select EXACTLY AST definitions directed,I,ilog,atan_bounds. Do not
import the old module or execute mpmath, components, old phase/case
loops/main. FREEZE.json pins that helper and the NEW executable;
check before/after computation and before completion. Prose is
identified by audit hashes, not executable pins.

Decimal precision50 basic operations use explicit outward rounding.
Correctly rounded ln/sqrt are expanded by one adjacent representable
in each direction. Pi uses exact Fraction alternating Machin series
70terms at1/5 and20terms at1/239, then directed decimal conversion.
All mathematical comparisons use Decimal or exact Fraction/int;
floating timers are operational only. Record Python/libmpdec versions.
This is the same accepted explicit arithmetic contract as D26/D20,
not a claim of fully hermetic Python or arithmetic-library independence.

Soft4/hard5 CPU seconds cover the WHOLE process lifetime, including
startup/imports/AST helper/exact controls/directed arithmetic/hash
checks/serialization/output/return. No children, native/build/kernel,
actual S/lambda/model point, phase/board/rootfinder/quadrature or
degree job. RLIMIT_CPU is absolute and applies through exit. The
before-receipt getrusage field is a CHECKPOINT, not exact exit CPU.

## Evidence, failure, completion and global boundary

Preregistration records fixed target, source/freeze, precision, limits
and UTC before executing helper definitions. A single budget-2048.json
retains all39 components/pi, all25 controls, verdict, code/helper/
freeze identities, runtime versions and CPU checkpoint. Every JSON
must be STRICTLY<16384B WHOLE; no component pruning/splitting to fit.
Raw files remain off Git; root alone copies essential evidence.

First source/freeze/arithmetic/control/sign/resource failure stops the
same consumed attempt and retains failure context. A hard kill may
prevent full failure serialization but still consumes the one attempt.
A passed=true artifact additionally needs actual observed EXIT0 and
unchanged published freeze. Distinct fresh directed replay/result
review remains required before adopting far2048; no prerelease report
or producer reading substitutes for that independent execution.

The NEW global target is EVERYn>=2048 with exactly the two parity-
correct actual corners. Its separate proof also requires D31's OWN
near2048 positive endpoint and final fresh review, plus already
accepted D27 actual-corner1024 radial1/8 and PD-T364 closed cover.
The FAR-only source must not assume/import that pending near result
or apply4096's1/16 floor at2048. A successful far job alone leaves
global OPEN until the other premises finish. No minimality, remaining
finite-degree closure, full D13 remainder or measured native speedup.

No source/control/scalar or scientific job ran in this PREPARATION.
Distinct prerelease audit, publication and explicit ROOT RELEASE are
still necessary before the exact command at the top.
