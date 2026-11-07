# D27 sole prospective wider-corner scalar contract

PRIMARY N1024 ONLY, h=pi/4,U=V=pi^2/32,q=1/7,PaxisUpper=5/7,
Dc=6211/7260,r=(22/7)^4/6144. No execution until complete proof,
idea/attempt, formulas, source and this SPEC are frozen AND ROOT RELEASE.

Command from repository root after release:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D27_corner/evaluate.py --run-once

Evaluate EXACTLY the accepted D20 full-phase Cnew/KD expressions and
D16 ACTUAL-origin E0, saving every positive component. Define

    T=(4L^2-3L)/pi^2,
    Mnew=[4L^2+(79/5)L]/pi^2+8/3+Cnew+2KD,
    delta=(1/7)T-Dc-Cnew-(5/7)KD-E0,
    diagonal_lower=(2/7)T-Dc-Cnew-(10/7)KD-E0,
    F=delta-r*Mnew, radial_coefficient=16F/pi^2.

These are analytically proved global-norm/actual-point-loss MAJORANTS,
not evaluations of actual S/lambda/model phase values. The D08 square
criterion is delta>Mnew*pi^4/6144; its normalization and origin Peano
factor are proved before evaluation. Pass iff all exact controls,
Mnew.lower>0,T.lower>0,F.lower>0. The entire first receipt is preserved
on failure; no source/precision/parameter/threshold fallback or retry.
No native, actual point, phase/board/root/quadrature/degree job or scan.

Exact controls:2>(7/5)^2; (1-5/7)/2=1/7;
8/3-4383/2420=6211/7260;6*32^2=6144;
r<1/60;1/7-r>0;5/7-(119/5)r>0;5/7-119/300=667/2100;
axis charge doubles exactly at the diagonal. The source additionally
checks the interval r lies strictly above the enclosed pi^4/6144.

Only D06 arithmetic definitions directed,I,ilog,atan_bounds execute,
AST-selected from SHA2569ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413.
No old main, mpmath, components/cases/phase inputs. Decimal50 basic
arithmetic is directed; correctly rounded ln is enclosed by adjacent
representables. Pi comes from exact rational alternating Machin bounds,
70terms at1/5 and20 at1/239. Soft4/hard5CPU covers startup/imports/
helpers/finalization, no children. One exclusive-create JSON receipt
records all intervals, controls, verdict, source/helper identities and
UTC. Report getrusage before serialization as a checkpoint, not exact
exit CPU. Essential receipt<16KiB. Independent mathematics/source/fresh
directed scalar review is required before root adoption.
