import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3/pylib')
import mpmath as mp; mp.mp.dps=40
pi=mp.pi
Cf=lambda t:-mp.digamma(t)-mp.digamma(1-t)
def Phi(t):
    t=t-mp.floor(t)
    return mp.mpf(1) if t==0 else mp.sin(pi*t)/pi*(Cf(t)-2*mp.log(pi))
f=lambda w:Phi(mp.mpf(1)/2+w/(2*pi))
h=mp.mpf('1e-15')
left=(f(pi)-f(pi-h))/h; right=(f(pi+h)-f(pi))/h
J0=2*(mp.log(pi)-mp.euler)/pi
print('f\'(pi-)=',left,' f\'(pi+)=',right,' left-right=',left-right,' J0=',J0)
