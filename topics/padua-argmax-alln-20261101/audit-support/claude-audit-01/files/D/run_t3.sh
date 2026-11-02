#!/bin/bash
cd "$(dirname "$0")"
python3 -B t3_global.py 17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32 4 > t3_g1.out 2>&1
python3 -B t3_global.py 33,36,41,47,48,50,51,56,57,63,64,65 4 > t3_g2.out 2>&1
python3 -B t3_global.py 80,81,99,100,101 3 > t3_g3.out 2>&1
python3 -B t3_global.py 127,128 3 > t3_g4.out 2>&1
python3 -B t3_global.py 200 2 > t3_g5.out 2>&1
echo done > t3_done.flag
