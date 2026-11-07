# D18 sole prospective scalar budget

N=7000 ONLY. No fallback, threshold/phase search, theta/precision/source
retune or retry. Formula/derivation/idea/source/SPEC must be frozen before
execution; accepted D17 corner scope is already an explicit prerequisite.

Command from repository root:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D18_budget/evaluate.py --run-once

Evaluate EXACTLY D18-phase-far-majorant's Af,Bf,s0=sqrt(191/768),
u0=191/6144 and g=1+log(1+2S/s0), with S=1/2+32/pi. Af is the
constant coefficient extracted from the COMPLETE D05 scalar expression
at a=1,p=P=d=0,|U0|=8,H=1+logN; this is raw coefficient extraction,
not application of a physical theorem at a fake phase. All13 base
components, including the full e4/I0/pole/TZ charges, are saved.
Bf=ED1+I1+Z1 uses the EXACT displayed positive coefficients; the written
majorant proves it controls p,d,P<=s(u), without deleting any term.

Near evaluates unchanged D16 C,K,E0, D11 T,A=77/96,
B=((47/192)T-113/72)/2,J=27A^4/(256B^3). Fixed allocation3/4 ONLY:

    NearGate=1/16-C-E0-(64/27)J-K^2/B,
    FarGate=u0*(T-22)-Af-Bf*s0-E0.

Pass globally iff B>0,T>22 and BOTH directed lower gate endpoints>0.
Record near/far verdicts separately, retaining any failed budget. No
actual S/lambda/model phase value, kernel, native/board/root/quad or
other degree computation executes. If far fails, its value is only a
failed SUFFICIENT gate, never a uniform actual gap or a negative argmax.

D06 helper definitions directed,I,ilog,imax,atan_bounds,components are
AST-selected from SHA2569ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413;
never its main/mpmath/cases/phase_inputs. Decimal50 basic operations are
directed. Documented correctly rounded Decimal ln and sqrt are enclosed
by adjacent representables at the directed input endpoints. Pi comes from
exact rational alternating Machin bounds70terms at1/5,20 at1/239.
One fresh exclusive-create JSON receipt saves all intervals, verdicts,
source/helper identities and UTC. Soft4/hard5CPU includes startup,
imports/helpers/finalization, no children. Report getrusage sample before
serialization as a checkpoint, not an observed exact exit CPU. Source
changes after first execution require separate review; no hidden rescue.
Independent Astra mathematics/source/fresh arithmetic review is required.
