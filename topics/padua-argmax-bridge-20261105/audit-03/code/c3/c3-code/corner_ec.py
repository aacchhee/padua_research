import mpmath as mp; mp.mp.dps=30
I4=mp.quad(lambda t: mp.sqrt(1-t**4),[0,1]); h=mp.pi/4
p=mp.sin(h); a=(1+mp.cos(h))/2
print('I4',I4,'<319/360',I4<mp.mpf(319)/360)
print('general central bound at (h,0):', 4*I4/mp.pi**2*p**1.5/mp.sqrt(a), ' with I4<319/360:', 4*mp.mpf(319)/360/mp.pi**2*p**1.5/mp.sqrt(a))
print('rho<=1 displayed bound 5x^{3/2}/12 at x=h:', 5*h**1.5/12)
print('M(256) main part', (4*mp.log(256)**2+mp.mpf(79)/5*mp.log(256))/mp.pi**2+mp.mpf(9)/4)
