#!/usr/bin/env python3
"""Exact arithmetic of the E14-wide-signed-outer constant aggregation (sections 4-6)
and the E14 wide 155/2 collection.  Auditor Claude Opus 5.5 xhigh."""
from fractions import Fraction as F
import sys
ok = True
def chk(name, c):
    global ok; ok &= c; print(("PASS " if c else "FAIL ") + name)
# (7)-(10): |V_s|<=17rho/4, |V_s'|<=5rho/2, |V''|<=31rho/20, quotient 31rho/40 var 31pi rho/80<31rho/25 (pi<16/5)
chk("31*pi/80<31/25 with pi<16/5", F(31,80)*F(16,5) == F(31,25))
chk("Var initial: (17/4)(1/5)+(1/5)(5/2)(pi/2) <= value at pi=16/5 = 33/20 (strict since pi<16/5) [run1 used < at pi=16/5: auditor script bug]", F(17,4)*F(1,5)+F(1,5)*F(5,2)*F(16,5)/2 == F(33,20))
chk("Var P_s initial 31/25+33/20=289/100", F(31,25)+F(33,20) == F(289,100))
chk("sup P_s initial 5/2+17/20=67/20", F(5,2)+F(17,20) == F(67,20))
chk("central Var 27/4+17/16+5/12=395/48", F(27,4)+F(17,16)+F(5,12) == F(395,48))
chk("  27/4 = 9*(3/4); 17/16=(17/4)(1/4); 5/12=(5/4)(1/3)", 9*F(3,4)==F(27,4) and F(17,4)*F(1,4)==F(17,16) and F(5,4)*F(1,3)==F(5,12))
chk("central sup (17/4)(3/4)+(5/4)(2/3)=193/48", F(17,4)*F(3,4)+F(5,4)*F(2,3) == F(193,48))
tot = F(289,100)+F(395,48)+4*F(67,20)+2*F(193,48)
chk("(14) total = 39073/1200 < 33", tot == F(39073,1200) and tot < 33)
# (17)->(1): 33 + [23 logm + 175/4 + log2 + 2logpi + 2]/pi with pi>3, logm<=L+1/32, log2<7/10, logpi<23/20
const = 33 + (F(23,32) + F(175,4) + F(7,10) + 2*F(23,20) + 2)/3
chk("constant = 33+65/4+23/96 = 4751/96 < 50", const == 33 + F(65,4) + F(23,96) == F(4751,96) and const < 50 and const > 49)
chk("log coefficient 23/3 (20+3 over pi>3)", F(20+3,3) == F(23,3))
print("OVERALL", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
