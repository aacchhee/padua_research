import numpy as np, sys
sys.path.insert(0,'.')
import importlib; g9=importlib.import_module('gen4_tests9')
def leb_cheb_zeros_at1(m):
    # m Chebyshev zeros (degree m-1), Lebesgue function at x=1: sum |l_j(1)| = (1/m) sum |T_m(1)/(1-x_j)| ... use direct formula l_j(x)=T_m(x)/((x-x_j) T_m'(x_j))
    x=np.cos((2*np.arange(m)+1)*np.pi/(2*m)); th=(2*np.arange(m)+1)*np.pi/(2*m)
    Tp = m*(-1)**np.arange(m)/np.sin(th)  # T_m'(x_j) = m sin(m th)/sin th, sin(m th_j)=(-1)^j
    return np.sum(np.abs(1.0/((1-x)*Tp)))
c1=(2/np.pi)*(np.euler_gamma+np.log(8/np.pi))
Pad={10:6.87710,20:9.19709,40:11.90986,80:15.01614,160:18.51540,320:22.40671,640:26.68919}
for n,L in Pad.items():
    a=leb_cheb_zeros_at1(n+1); b=leb_cheb_zeros_at1(n)
    asy=(2/np.pi)*np.log(n)+c1
    print('n',n,'Pad %.5f'%L,'| lam_{n+1}(1)=%.5f lam_n(1)=%.5f asym_n=%.5f'%(a,b,asy),'| Pad - lam_{n+1}^2 = %.4f'%(L-a*a),' Pad - lam_n^2 = %.4f'%(L-b*b),' Pad - lam_n*lam_{n+1} = %.4f'%(L-a*b),' Pad - asym_n^2 = %.4f'%(L-asy**2), ' Pad-(asym_{n+1})^2 = %.4f'%(L-((2/np.pi)*np.log(n+1)+c1)**2))
