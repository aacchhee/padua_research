import sys,os,json,math,numpy as np,scipy.linalg as la
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lebesgue import exps_lex,exps_deg,basis,global_qr,mesh_max
from unisolvence import folded_parity, select
out=[]
for n in map(int,sys.argv[2:]):
    N=math.comb(n+3,3); row={'n':n}
    q,keys=folded_parity(n)
    for name,P in [('QR_deg',global_qr(n,exps_deg(n))),('QR_lex',global_qr(n,exps_lex(n))),('rQR',np.cos(2*np.pi*np.array(select(n,q,keys))/q))]:
        V=basis(P,n,exps_lex(n)); C=la.solve(V,np.eye(N))
        row[name]=[float(mesh_max(C,n,21)[0]),float(mesh_max(C,n,41)[0])]
    print(row,flush=True); out.append(row)
json.dump(out,open(sys.argv[1],'w'))
