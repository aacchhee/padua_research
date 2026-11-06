import numpy as np,sys
S,G=sys.argv[1],sys.argv[2]
cols=['Hcore','Hkry','Hreo','Bcore','Bkry','Breo']
for fam in ['kravchuk','hahn']:
    p=np.loadtxt(f'{S}/data_experiment1_{fam}.dat',skiprows=1); o=np.loadtxt(f'{G}/ours_{fam}.dat')
    assert (p[:,0]==o[:,0]).all()
    L=np.log10(o[:,1:7]/p[:,1:7])
    print('==',fam,'rows',len(p))
    print('N  '+' '.join(f'{c:>8}' for c in cols)+'   (log10 ours/paper)')
    for i in range(len(p)): print(int(p[i,0]),' '+' '.join(f'{x:8.2f}' for x in L[i]))
    for j,c in enumerate(cols):
        bad=[int(p[i,0]) for i in range(len(p)) if abs(L[i,j])>1]
        print(c,'max|log|=%.2f'%abs(L[:,j]).max(),'N with |log|>1:',bad)
    if fam=='kravchuk':
        i=list(p[:,0]).index(10); print('GATE N=10 core: paper=%.6e ours=%.6e log10=%.3f'%(p[i,1],o[i,1],L[i,0]))
