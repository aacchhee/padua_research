import math
pi = math.pi
H0 = 0.3100022644073144; C0 = 2*0.5772156649015329+4*math.log(2); bst = C0-3.5
d0 = C0*bst/pi**2; g0 = 4*(math.log(pi)**2-math.log(2)**2)/pi**2; j = H0+d0-g0
for n in [32, 160, 192, 256, 320, 1000]:
    m = n+1; L = math.log(n); H = 1+L
    T = (4*L**2-3*L)/pi**2; b0 = 4/pi**2; r0 = math.log(2.5)+1/18
    D = ((52/pi**2)*H+7)/n+10/n**2+20*H/(pi*n**2)
    Mc = b0*(2*L+2*r0)/n+(4+b0*(L+1/n))/(4*n**2-1)+b0/(2*n-1)**2+(5+b0*(math.log(n+0.5)+2))/(4*(n-0.5)**2)
    eb = D+Mc+1/n
    KD = ((6+16/(3*pi))*H+2/pi)/n
    A4 = 4/n+40*H/(pi*n**2); C4 = A4+20/n**2; dbeta = (17*L+27)/n**2
    JN = (1.5*H+16/5)/n+78/n**2; JW = (1.5*H+6)/n+148/n**2
    kNx = ((19/2)*H+(23/3)*L+67.7)/n+82/n**2; kWx = ((19/2)*H+(23/3)*L+77.5)/n+152/n**2
    UN0 = T-eb+A4+j; UW0 = T-eb+A4+j
    gn = 1+math.log(2+8*m/(3*pi)); MA = 1/pi+4/pi**2
    Gg = (7*MA*L+111/2+(63+math.log(2)+4*math.log(pi)+7*math.log(m)+16*math.log(2*m)+1.5*gn)/pi)/m
    Wn = (3*math.log(m)+math.log(2)+2*math.log(pi)+2)/(pi*m)
    CE = D+Gg+(64+16*L)/n+318/n**2+Mc+Wn
    Mn = (4*L**2+15.8*L)/pi**2+2.25+CE+2*KD
    print('n=%5d T=%.3f D=%.4f M=%.4f ebar=%.4f K_D=%.4f A4=%.4f C4=%.4f J_N=%.4f k_Nx=%.4f U_N(rho=0)=%.3f  CEbar=%.3f  M(n)=%.3f' % (n, T, D, Mc, eb, KD, A4, C4, JN, kNx, UN0, CE, Mn))
