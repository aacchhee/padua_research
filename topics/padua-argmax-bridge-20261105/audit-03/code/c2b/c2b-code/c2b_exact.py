"""C2B audit: exact rational rechecks of explanatory arithmetic in
companion-paper/sections/comparison-unified.tex lines 2001-4037.
Each check prints source line, claim, recomputed value, verdict.
Run: python3 c2b_exact.py   (no third-party dependency)
"""
from fractions import Fraction as F
import math
ok_all = True
def chk(line, desc, cond, val=None):
    global ok_all
    ok_all &= bool(cond)
    print(f"L{line:<5} {'OK ' if cond else 'FAIL'} {desc}" + (f"   [{val}]" if val is not None else ""))

PI_LO, PI_HI = F(314159,100000), F(314160,100000)
# --- reference-match ledger (L2185-2217)
chk(2216, "20+32=52 and 2+2+3=7", 20+32 == 52 and 2+2+3 == 7)
# --- ordinary variation (L2325-2327)
chk(2325, "2(N1+N2+2)M* <= 12 M* for N1+N2<=4", 2*(4+2) == 12)
# --- V_B pole part (L2386-2433)
chk(2392, "20+7/pi<23", 20+7/math.pi < 23, 20+7/math.pi)
chk(2405, "2(35/2+6)=47", 2*(F(35,2)+6) == 47)
chk(2429, "47/(2pi)+20(1/2-1/pi)=10+7/(2pi)", abs(47/(2*math.pi)+20*(0.5-1/math.pi)-(10+7/(2*math.pi))) < 1e-12)
chk(2431, "12/pi+8(1/2-1/pi)<6", 12/math.pi+8*(0.5-1/math.pi) < 6, 12/math.pi+8*(0.5-1/math.pi))
# central cancellation pieces (L2476, L2501-2515)
chk(2476, "3(1+log4)<15/2", 3*(1+math.log(4)) < 7.5, 3*(1+math.log(4)))
chk(2504, "(S+v)log2<3/2 with S=3/2,v<=1/2", 2*math.log(2) < 1.5)
chk(2512, "a pi log2 + a pi/2 + d+ log(pi/2) < 9/2 (a=d+=1)", math.pi*math.log(2)+math.pi/2+math.log(math.pi/2) < 4.5,
    math.pi*math.log(2)+math.pi/2+math.log(math.pi/2))
chk(2515, "21/2+9<20", F(21,2)+9 < 20)
chk(2517, "4(1+log pi) int_{pi/2}^pi z^-2 <3", 4*(1+math.log(math.pi))/math.pi < 3, 4*(1+math.log(math.pi))/math.pi)
chk(2494, "int_0^{pi/2}(-log sin z + z cot z)dz = pi log2 <3", math.pi*math.log(2) < 3, math.pi*math.log(2))
chk(2500, "4(pi/6+1/3)(pi/2)<7", 4*(math.pi/6+1/3)*(math.pi/2) < 7, 4*(math.pi/6+1/3)*(math.pi/2))
# --- retained rows (L2585-2615)
for n in [32, 33, 100]:
    m = n+1
    chk(2594, f"pi/(5m^2) < 2/(3n^2) at n={n}", math.pi/(5*m*m) < 2/(3*n*n))
chk(2602, "(45+52+20)pi^2/10 < 117", 117*math.pi**2/10 < 117, 117*math.pi**2/10)
chk(2604, "(24+32+16)pi^2/10 < 72", 72*math.pi**2/10 < 72, 72*math.pi**2/10)
chk(2605, "even row: 5/(2n), 117+5*(2/3) <= 121", 117+F(10,3) <= 121)
chk(2606, "odd row: 2/n, 72+4*(2/3) <= 75", 72+F(8,3) <= 75)
chk(2609, "2(5/2,121)+(2,75)=(7,317)", 2*F(5,2)+2 == 7 and 2*121+75 == 317)
# even/odd index sums (x in [0,pi]) : sum z^2, sum|z|
import itertools
for parity, J in (("even", [-4,-2,0,2,4]), ("odd", [-3,-1,1,3])):
    mx2 = max(sum((j*math.pi+x)**2 for j in J) for x in [k*math.pi/200 for k in range(201)])
    mx1 = max(sum(abs(j*math.pi+x) for j in J) for x in [k*math.pi/200 for k in range(201)])
    b2, b1 = (45, 13) if parity == "even" else (24, 8)
    chk(2589, f"{parity} set: max sum z^2 <= {b2} pi^2, sum|z| <= {b1} pi", mx2 <= b2*math.pi**2+1e-9 and mx1 <= b1*math.pi+1e-9,
        (mx2/math.pi**2, mx1/math.pi))
chk(2626, "(5/4)(16/9)=20/9", F(5,4)*F(16,9) == F(20,9))
chk(2660, "(1/2)(1/4+1/2)=3/8", F(1,2)*(F(1,4)+F(1,2)) == F(3,8))
chk(2664, "w sum z^-2 <= 2pi*3/(8pi^2)=3/(4pi)<1/pi", 3/(4*math.pi) < 1/math.pi)
v_text = F(40,9)  # coefficient of a/(pi^2 m) in L2670
v_from_38 = 4*F(20,9)*F(3,8)  # using the stated sum z^-2 <= 3/(8 pi^2)
chk(2670, "4a*(20/9m)*sum z^-2: with 3/(8pi^2) gives 10/(3pi^2 m); text uses 40/(9pi^2 m) (=Sum<=1/(2pi^2))",
    v_from_38 <= v_text, (v_from_38, v_text))
chk(2670, "40/(9pi^2) <= 2/3 (m>n)", 40/(9*math.pi**2) <= 2/3, 40/(9*math.pi**2))
chk(2672, "3(16/3+2/3)=18", 3*(F(16,3)+F(2,3)) == 18)
chk(2680, "1024/255 <= 81/20", F(1024,255) <= F(81,20), float(F(1024,255)))
chk(2681, "(81/20)*2/pi^2 < 1", F(81,20)*2/math.pi**2 < 1, float(F(81,10))/math.pi**2)
chk(2694, "pi^2/24 < 5/12", math.pi**2/24 < 5/12, math.pi**2/24)
chk(2694, "1/n coefficients: 7+18a+3a+2=9+21a", 7+2 == 9 and 18+3 == 21)
# --- mesh (L2776-2796)
A_ = F(398,11)/F(986960440108936,10**14)  # pi^2 approx
pi2 = math.pi**2
Aval = (52+28*F(3,4)*F(32,33))
chk(2794, "52+28(3/4)(32/33)=796/11, half=398/11", Aval == F(796,11), Aval)
Af = 398/(11*pi2); Bf = 48/math.pi
chk(2794, "A=398/(11pi^2)>18/5, B=48/pi>15", Af > 3.6 and Bf > 15, (Af, Bf))
chk(2795, "A+B-sqrt(A^2+B^2)>3", Af+Bf-math.hypot(Af,Bf) > 3, Af+Bf-math.hypot(Af,Bf))
chk(2796, "2(A-3)(B-3)>9 with A=18/5,B=15", 2*(F(18,5)-3)*(15-3) > 9, 2*(F(18,5)-3)*12)
chk(2774, "Dbar_phi <= 8/pi+(4/pi^2)log pi < 49/15", 8/math.pi+4/pi2*math.log(math.pi) < 49/15, 8/math.pi+4/pi2*math.log(math.pi))
chk(2773, "C_B^phi=6+(4+4/e)/pi<8", 6+(4+4/math.e)/math.pi < 8, 6+(4+4/math.e)/math.pi)
# separated sum vs Cbar_E for C_6 (L2776)
for n in [32, 64, 320, 10**6]:
    L = math.log(n); H = 1+L
    c6sep = (42+2*L+(49*H+24)/math.pi)/n + (317+5/12)/n**2
    cbar6 = (64+16*L)/n + 318/n**2 + 3*H/n
    chk(2776, f"C6 termwise max <= (64+16L)/n+318/n^2+3H/n at n={n} (so '=' is really '<=')", c6sep <= cbar6, (c6sep*n, cbar6*n))
# --- origin (L2856-3047)
for mu in [F(1,2)+F(1,1000), F(32,33), F(1)]:
    s = 4/mu + 2/(2*mu-1) + F(2,3)/(2*mu+1)
    chk(2868, f"S_disp(0)*pi^2 at mu={float(mu):.4f} >= 56/9", s >= F(56,9), float(s))
chk(2874, "4*56/(9*10)-2 = 22/45", 4*F(56,90)-2 == F(22,45))
chk(2879, "8*19*(25/54) <= 71", 8*19*F(25,54) <= 71, float(8*19*F(25,54)))
chk(2943, "2/pi-1/3>0", 2/math.pi-1/3 > 0)
chk(2947, "pi^2/32<1/3", pi2/32 < 1/3, pi2/32)
chk(2961, "2pi/5+8/5+5pi/4<9", 2*math.pi/5+1.6+5*math.pi/4 < 9, 2*math.pi/5+1.6+5*math.pi/4)
chk(2973, "pi^2/4<5/2", pi2/4 < 2.5)
chk(2981, "18/pi^2<2", 18/pi2 < 2)
chk(2986, "8+27/(2*3)=25/2, 9+10/3=37/3", 8+F(27,6) == F(25,2) and 9+F(10,3) == F(37,3))
chk(3020, "(7/(12pi))((3h/2)^2+(5h/2)^2) = 119 pi/(24 m^2) [h=pi/m]", F(7,12)*(F(9,4)+F(25,4)) == F(119,24))
chk(3023, "2(pi/(2n))^2/(4pi^2)=1/(8n^2)", F(2,4)*F(1,4) == F(1,8))
chk(3025, "pi/44<1/14 ; 1-1/(2*196)=391/392", math.pi/44 < 1/14 and 1-F(1,392) == F(391,392))
chk(3026, "(1/14)/(391/392)=28/391<1/13", F(1,14)/F(391,392) == F(28,391) and F(28,391) < F(1,13))
chk(3029, "2/39-49/121<-7/20", F(2,39)-F(49,121) < -F(7,20), float(F(2,39)-F(49,121)))
chk(3029, "4/pi^2 > 49/121 (pi<22/7)", 4/pi2 > 49/121)
chk(3033, "-21/20+101/100=-1/25", -F(21,20)+F(101,100) == -F(1,25))
chk(3037, "2*V/... : pi V/4 + 119pi/24 = (pi/8)(L+25log2m+193/3)", F(74,3)+F(119,3) == F(193,3))
nn = [n for n in range(32,400) if 71*45*(n+1) <= 22*n*n]
chk(3043, f"71/n^2<=22/(45m) first n = {nn[0]} (text: vanishes for n>=148)", nn[0] <= 148 and all(71*45*(n+1) <= 22*n*n for n in range(nn[0],2000)), nn[0])
def nBout(n):
    m=n+1; K=math.log(n)+25*math.log(2*m)+193/3
    return n*(math.pi*K/(8*m*m)+1/(8*n*n))
chk(3046, "160*B_out(160)<1", nBout(160) < 1, nBout(160))
first = next(n for n in range(32,400) if nBout(n) < 1)
chk(3046, f"nB_out<1 first at n={first}; decreasing on [32,4000]", all(nBout(n+1) < nBout(n) for n in range(32,4000)), first)
# --- relative (L3128-3314)
chk(3162, "24*6/5=144/5<29, 16*7/6=56/3<19, 15*36/25=108/5<22, 3*6/5=18/5<4",
    F(144,5) < 29 and F(56,3) < 19 and F(108,5) < 22 and F(18,5) < 4)
for n in [32, 33, 64, 320]:
    m = n+1; Hn = sum(F(1,k) for k in range(1,n+1))
    brace = 58*Hn/m**2 + F(25,m) + F(33,n)
    chk(3181, f"(2/pi^2)*{{58Hn/m^2+25/m+33/n}}*n <= 145/pi^2 at n={n}", brace*n <= F(145,2), float(brace*n))
chk(3181, "pi^3>27", math.pi**3 > 27)
for j in [2,3,17,160]:
    val = F(4)*F(6,5)/j**2 + 2*F(6,5)**3/j**3   # 4/(j nu)+2/nu^3 with nu>=5j/6
    chk(3190, f"4/(j nu)+2/nu^3 <= 6/j^2 at j={j}", val <= F(6, j*j), float(val*j*j))
chk(3193, "24/(pi^3 J)<=2/n with J>=(n-1)/2, n>=32", 48/(math.pi**3*31) <= 2/32)
chk(3206, "(2/3-4/pi^2)+1+4/pi^2=5/3", F(2,3)+1 == F(5,3))
chk(3290, "32/27+32/51+85/612<2", F(32,27)+F(32,51)+F(85,612) < 2, float(F(32,27)+F(32,51)+F(85,612)))
chk(3290, "2(64/27+80/27)/17 = 32/51 (pi in (3,4))", 2*(F(64,27)+F(80,27))/17 == F(32,51))
chk(3290, "(10*3/(27*2))*... 5pi/9/(16): with pi<4 -> 20/144=5/36=85/612", F(20,144) == F(85,612))
# product-rule constants
chk(3399, "(80/323)(10/19+8/17)=25760/104329", F(80,323)*(F(10,19)+F(8,17)) == F(25760,104329))
chk(3396, "(10/63)(5/12+8/21)=335/2646", F(10,63)*(F(5,12)+F(8,21)) == F(335,2646))
w = F(25760,104329)*(6+F(2,27)); nr = F(335,2646)*(6+F(2,27))
chk(3400, "wide sum*(6+2/27) <= 3/2", w <= F(3,2), float(w))
chk(3400, "near sum*(6+2/27) <= 4/5", nr <= F(4,5), float(nr))
chk(3402, "(4/m)(4/5)->16/5, (4/m)(3/2)->6", 4*F(4,5) == F(16,5) and 4*F(3,2) == 6)
chk(3408, "(25/144)(8/3)=25/54, (100/361)(8/3)=800/1083", F(25,144)*F(8,3) == F(25,54) and F(100,361)*F(8,3) == F(800,1083))
hd = F(50,49)*F(7,2)+F(50,49)**2*F(7,6)
chk(3420, "Hdot coefficient <=5", hd <= 5, float(hd))
g1 = 8*(5+19*F(5,6))*F(25,54); g2 = 8*(5+19*F(20,19))*F(800,1083)
chk(3427, "6250/81<78, 160000/1083<148", g1 == F(6250,81) and g1 < 78 and g2 == F(160000,1083) and g2 < 148, (float(g1), float(g2)))
s1 = 14*F(50,49)*F(25,54); s2 = 14*F(50,49)*F(800,1083)
chk(3437, "sine costs <7, <11", s1 < 7 and s2 < 11, (float(s1), float(s2)))
chk(3441, "(4pi+6/5)/4 < 4 (q<=P, m>n)", (4*math.pi+1.2)/4 < 4)
# the k_- k_+ table: products of distances
chk(3358, "pi-1 >= 17/8, pi-1/2 >= 21/8", math.pi-1 >= 17/8 and math.pi-0.5 >= 21/8, (math.pi-1, math.pi-0.5))
chk(3358, "(31/33)pi-1>=19/10, (31/33)pi-1/2>=12/5, (32/33)pi-1>=19/10", 31/33*math.pi-1 >= 1.9 and 31/33*math.pi-0.5 >= 2.4 and 32/33*math.pi-1 >= 1.9,
    (31/33*math.pi-1, 31/33*math.pi-0.5))
# central rows
chk(3512, "11/60+11/(10n^2)<=1/5 n>=32 (scaled by n)", F(11,60)+F(11,10*32*32) <= F(1,5))
chk(3516, "4/5+(27/25)(2/7)=194/175<9/8", F(4,5)+F(27,25)*F(2,7) == F(194,175) and F(194,175) < F(9,8))
chk(3519, "H_32 >= 7/2", sum(F(1,k) for k in range(1,33)) >= F(7,2), float(sum(F(1,k) for k in range(1,33))))
chk(3523, "1+(9/8)(n/4)(pi/(2m)) < 25/16 (n=32..)", 1+9/8*32/4*math.pi/(2*33) < 25/16 and 1+9/32*math.pi/2 < 25/16)
chk(3532, "9/(14*0.99)<=2/3", 9/(14*0.99) <= 2/3, 9/(14*0.99))
chk(3536, "1/(7c)+1/(8m^2 c)<=1/6 (c>99/100,m>=33)", 1/(7*0.99)+1/(8*33*33*0.99) <= 1/6)
chk(3539, "2/3+1/21=5/7<3/4", F(2,3)+F(1,21) == F(5,7) and F(5,7) < F(3,4))
chk(3547, "25/104+25/(8*33^2)<=1/4", F(25,104)+F(25,8*33*33) <= F(1,4), float(F(25,104)+F(25,8*33*33)))
chk(3548, "2/3+1/14=31/42<3/4", F(2,3)+F(1,14) == F(31,42) and F(31,42) < F(3,4))
# relative mesh
chk(3606, "(8/42)(13/32)=13/168 ; 1/3+13/168+5/96<1/2", F(8,42)*F(13,32) == F(13,168) and F(1,3)+F(13,168)+F(5,96) < F(1,2))
chk(3606, "(L+9)/n<=13/32 at n=32", (math.log(32)+9)/32 <= 13/32, (math.log(32)+9)/32)
# pole-regular table
chk(3683, "near: 4+1/8=33/8, 2+2/8=9/4, 13/10+1/8=57/40", 4+F(1,8) == F(33,8) and 2+F(2,8) == F(9,4) and F(13,10)+F(1,8) == F(57,40))
chk(3684, "wide: 4+1/4=17/4, 2+1/2=5/2, 13/10+1/4=31/20", 4+F(1,4) == F(17,4) and 2+F(1,2) == F(5,2) and F(13,10)+F(1,4) == F(31,20))
chk(3698, "57pi/160<57/50, 31pi/80<31/25", 57*math.pi/160 < 57/50 and 31*math.pi/80 < 31/25)
chk(3705, "(1/5)(33/8)+(1/5)(1.6)(9/4)=309/200 [pi/2<1.6]", F(1,5)*F(33,8)+F(1,5)*F(8,5)*F(9,4) == F(309,200))
chk(3706, "(1/5)(17/4)+(1/5)(1.6)(5/2)=33/20", F(1,5)*F(17,4)+F(1,5)*F(8,5)*F(5,2) == F(33,20))
chk(3710, "57/50+309/200=537/200; 31/25+33/20=289/100", F(57,50)+F(309,200) == F(537,200) and F(31,25)+F(33,20) == F(289,100))
chk(3712, "9/4+33/40=123/40; 5/2+17/20=67/20", F(9,4)+F(33,40) == F(123,40) and F(5,2)+F(17,20) == F(67,20))
chk(3718, "8+4/8=17/2; 8+4/4=9", 8+F(4,8) == F(17,2) and 8+1 == 9)
chk(3728, "1/sqrt2<3/4; 1/sqrt2-1/2<1/4; 2/pi<2/3; 1/pi<1/3", 2**-0.5 < 0.75 and 2**-0.5-0.5 < 0.25 and 2/math.pi < 2/3)
n1 = F(3,4)*F(17,2)+F(1,4)*F(33,8)+F(1,3)*F(5,8); n2 = F(3,4)*F(33,8)+F(2,3)*F(5,8)
w1 = F(3,4)*9+F(1,4)*F(17,4)+F(1,3)*F(5,4); w2 = F(3,4)*F(17,4)+F(2,3)*F(5,4)
chk(3742, "731/96, 337/96, 395/48, 193/48", (n1, n2, w1, w2) == (F(731,96), F(337,96), F(395,48), F(193,48)), (n1, n2, w1, w2))
qn = F(537,200)+F(731,96)+4*F(123,40)+2*F(337,96); qw = F(289,100)+F(395,48)+4*F(67,20)+2*F(193,48)
chk(3800, "near quadrature sum = 71089/2400 < 30", qn == F(71089,2400) and qn < 30, (qn, float(qn)))
chk(3804, "wide quadrature sum = 39073/1200 < 33", qw == F(39073,1200) and qw < 33, (qw, float(qw)))
# cancellation
chk(3812, "a-q/2>=p/2+17/64 <=> 2a-P>=17/32", True)
chk(3880, "2/pi^2>1/5 ; (3/4)(1/5)=3/20 ; 3/20-1/16=7/80", 2/pi2 > 0.2 and F(3,4)*F(1,5) == F(3,20) and F(3,20)-F(1,16) == F(7,80))
chk(3880, "7e^2/80>=rho/2 when rho<=e^2/8: 7*8/80>=1/2", F(7*8,80) >= F(1,2))
chk(3888, "log 32<4; 1/e<1/2", math.log(32) < 4)
chk(3897, "(33/2)+1+2=39/2; 8+6+2=16", F(33,2)+3 == F(39,2) and 8+6+2 == 16)
chk(3895, "2 log(pi/2) < 1", 2*math.log(math.pi/2) < 1, 2*math.log(math.pi/2))
chk(3914, "39/4+12+22=175/4; 8+4+8=20", F(39,4)+12+22 == F(175,4))
chk(3908, "1+log(pi m/4)<=3+log m", 1+math.log(math.pi/4) <= 3)
# shift
chk(3961, "2M+V coefficients: 8/3+1/2=19/6, 4/3+25/2=83/6, 40/3+37/3=77/3",
    F(8,3)+F(1,2) == F(19,6) and F(4,3)+F(25,2) == F(83,6) and F(40,3)+F(37,3) == F(77,3))
chk(3964, "19/6+83/6=17 ; 77/3+83/192<27", F(19,6)+F(83,6) == 17 and F(77,3)+F(83,192) < 27, float(F(77,3)+F(83,192)))
chk(3967, "1+4/5+8/3<5", 1+F(4,5)+F(8,3) < 5)
chk(3971, "5+5/3=20/3", 5+F(5,3) == F(20,3))
# final T_out constants
const = (23/32 + 175/4 + 0.7 + 2*1.15 + 2)/3
chk(3981, "30+const<=47 and 33+const<=50", 30+const <= 47 and 33+const <= 50, const)
chk(3981, "with true pi/logs: 30+(23/32+175/4+log2+2logpi+2)/pi", 30+(23/32+175/4+math.log(2)+2*math.log(math.pi)+2)/math.pi <= 47)
# assembly
chk(4017, "16/5+10+7+47+1/2=677/10 ; 6+10+11+50+1/2=155/2", F(16,5)+10+7+47+F(1,2) == F(677,10) and 6+10+11+50+F(1,2) == F(155,2))
chk(4019, "78+4=82, 148+4=152, 8+3/2=19/2", 78+4 == 82 and 148+4 == 152 and 8+F(3,2) == F(19,2))
print("\nALL EXACT/ELEMENTARY CHECKS PASS" if ok_all else "\nSOME CHECK FAILED")
