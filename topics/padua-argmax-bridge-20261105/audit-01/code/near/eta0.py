from fractions import Fraction as F
n=F(500000); L=F(14); tau0=F(1001,1000); ell0=F(249,250000)
terms={}
terms['r_n']=1/n**2
terms['E5']=tau0**2/(4*127**2)+tau0/(508*n)+(L+1)/(2*n)+4/n
terms['D_n']=(10+F(20,3)*(L+1))/n**2
terms['strip']=F(9,4*158**2)+F(2,10**6)+F(1,10**8)+F(1,10**9)
terms['jump']=3/n**2+F(1,27*128**3)+1/(16*n*128**2)
terms['outer']=(L+8)/(n**2*ell0**2)+(F(6,5)*L+23)/(2*n)+(147/ell0**2+4/ell0)/(8*n**2)+F(5,2)/n+F(1,12)/n
terms['special']=F(32,225)/n
tot=sum(terms.values())
for k,v in terms.items(): print(k, float(v))
print('total',tot, float(tot))
claimed=F(12989329736187619160983471,38345245772322816000000000000)
print('claimed',float(claimed),'equal?',tot==claimed, 'diff',float(tot-claimed))
print('<1/1000?',tot<F(1,1000))
# sum (18)
s=F(2,1000)+F(1,10000)+F(11270,500000)+F(3000,500000)
print('(18)',s, s==F(383,12500), s<F(1,32), s-F(1,16), s-F(1,16)< -F(1,32), F(383,12500)-F(1,16))
# 11270
print('11270?',F(45000)/4+F(40)/2)
# C05 endpoint Hessian
print('hess', 128+255*(4+168), (512+3)*128**2+1, F(43988)+F(8437761)/n, F(43988)+F(8437761)/n<45000)
print('slope', 177*128, F(34)+F(22656)/n<35)
# quotient hessian coefficient
x=F(99,100)
q=1/(2*x)+1/(4*x**2)+(F(16,3)/x**2+F(32,9)/x**3)*F(1,10**7)
print('quot', float(q), q<1)
print('r2/n2', F(128**2)/n**2 < F(1,10**7))
# (u+-v)/2 bound with pi<22/7, r=128
pi_up=F(22,7)
print('arg', ((255*pi_up+1)/2), (255*pi_up+1)/2<403, F(403)/n<F(1,1000))
# 15000/n
print('15000/n', F(15000)/n<=F(3,100))
# (14) 
print('(14) coeff', F(1,3)+F(3,100))
# C04 allowance
A=47*F(131,10)**2/480+F(131,10)/240
print('A',float(A), A-F(1225,144)-F(32,9), float(A-F(1225,144)-F(32,9)), A-F(1225,144)-F(32,9)>F(19,4), A-F(395,48)>8)
c=F(15,32); k=F(19,4)
mx=27*c**4/(256*k**3)
print('alpha max',mx,float(mx), mx<F(1,20000))
