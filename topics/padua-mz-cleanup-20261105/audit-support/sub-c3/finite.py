import sys, numpy as np, importlib.util
from math import log, pi, cos, sin
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('g1', '/home/user/padua_research/topics/padua-mz-cleanup-20261105/code/g1_spectral.py')
g1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(g1)

def my_weights(m):
    # independent moment solve: sum w T_a(x_j)T_b(y_k) = h_a h_b, a+b<=m, nodes j+k even
    x = np.cos(np.pi*np.arange(m+1)/m); y = np.cos(np.pi*np.arange(m+2)/(m+1))
    nodes = [(j,k) for j in range(m+1) for k in range(m+2) if (j+k)%2==0]
    mons = [(a,b) for a in range(m+1) for b in range(m+1-a)]
    h = lambda r: 0.0 if r%2 else 2.0/(1-r*r)
    V = np.array([[np.cos(a*np.pi*j/m)*np.cos(b*np.pi*k/(m+1)) for (j,k) in nodes] for (a,b) in mons])
    rhs = np.array([h(a)*h(b) for (a,b) in mons])
    w = np.linalg.solve(V, rhs)
    W = np.zeros((m+1,m+2))
    for (j,k),v in zip(nodes,w): W[j,k]=v
    return W
for m in [6,7,12,13,20,21]:
    W1 = g1.weights_dct(m); W2 = my_weights(m)
    print('m',m,'max|dct-moment|', np.max(abs(W1-W2)), 'sum', W1.sum())
