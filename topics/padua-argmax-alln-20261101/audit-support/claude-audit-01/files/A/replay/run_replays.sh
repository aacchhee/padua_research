#!/bin/bash
# Sequential replay of the committed general certificates with the unchanged checker.
A=/tmp/claude-0/-home-user-padua-research/efec27fb-ede8-54e4-a9c8-12b8741cbbba/scratchpad/audit01/A
cd /home/user/padua_research
T=topics/padua-argmax-alln-20261101
LOG=$A/replay/replay_log.txt
: > $LOG
echo "python: $(python3 --version 2>&1); PYTHONOPTIMIZE=[$PYTHONOPTIMIZE]; head $(git rev-parse HEAD)" >> $LOG
sha256sum $T/code/part3/finite_bernstein.py $T/code/part3/finite_general.py $T/code/part3/finite_general_check.py $T/code/part3/finite_general_run.py $T/code/part3/finite_n2_exact.py $T/code/part3/finite_general_controls.py >> $LOG
for N in 9 10 11 13 14 15 16; do
  CERT=$T/outputs/part3/finite_n${N}_general.json.gz
  OUT=$A/replay/finite_n${N}_claude_check.json
  START=$(date +%s.%N)
  python3 -B $T/code/part3/finite_general_check.py $CERT --output $OUT > $A/replay/finite_n${N}_claude_check.stdout 2> $A/replay/finite_n${N}_claude_check.stderr
  RC=$?
  END=$(date +%s.%N)
  echo "n=$N rc=$RC wall=$(echo "$END - $START" | bc) cert_sha=$(sha256sum $CERT | cut -d' ' -f1) out_sha=$(sha256sum $OUT 2>/dev/null | cut -d' ' -f1)" >> $LOG
done
# Developer adversarial controls on the n8 general certificate (writes only to --output).
START=$(date +%s.%N)
python3 -B $T/code/part3/finite_general_controls.py $T/outputs/part3/finite_n8_general.json.gz --output $A/replay/finite_general_controls_claude_n8.json > $A/replay/controls_n8.stdout 2> $A/replay/controls_n8.stderr
RC=$?; END=$(date +%s.%N)
echo "controls n8 rc=$RC wall=$(echo "$END - $START" | bc) out_sha=$(sha256sum $A/replay/finite_general_controls_claude_n8.json 2>/dev/null | cut -d' ' -f1)" >> $LOG
sha256sum $T/code/part3/finite_bernstein.py $T/code/part3/finite_general.py $T/code/part3/finite_general_check.py $T/code/part3/finite_general_run.py $T/code/part3/finite_n2_exact.py $T/code/part3/finite_general_controls.py >> $LOG
echo DONE >> $LOG
