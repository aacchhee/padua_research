#!/bin/bash
# usage: chain.sh family ; runs 260 then 180
B=${AUDIT_OUT:?set AUDIT_OUT to an output directory containing runs/}
cd /home/user/padua_research
f=$1
for p in 260 180; do
  date -u +%FT%TZ > $B/runs/conditioning-full-$f$p.start
  python3 topics/nn-mop-stability-20261105/code/conditioning_timed.py $B/runs/conditioning-full-$f$p.time.json topics/nn-mop-stability-20261105/code/conditioning.py --family $f --sizes $(seq 4 64) --dps $p --check > $B/runs/conditioning-full-$f$p.json 2> $B/runs/conditioning-full-$f$p.log
  echo "exit $?" > $B/runs/conditioning-full-$f$p.exit
  date -u +%FT%TZ >> $B/runs/conditioning-full-$f$p.exit
done
