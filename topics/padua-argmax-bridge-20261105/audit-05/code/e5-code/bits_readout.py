"""A3: integer bit readout of 2^-1022/2 under MXCSR modes. Usage: python3 -E -B bits_readout.py LIB"""
import ctypes, sys
import numpy as np
L = ctypes.CDLL(sys.argv[1]); L.get_csr.restype = ctypes.c_uint; L.set_csr.argtypes = [ctypes.c_uint]
d = L.get_csr(); FTZ, DAZ, RZ = 1 << 15, 1 << 6, 3 << 13
tiny = np.array([2.0**-1022])
for label, csr in [('default', d), ('FTZ|DAZ', d | FTZ | DAZ), ('round-toward-zero', d | RZ), ('FTZ only', d | FTZ), ('DAZ only', d | DAZ)]:
    L.set_csr(csr)
    try:
        q = tiny / 2
    finally:
        L.set_csr(d)
    print(label, hex(int(q.view(np.uint64)[0])))
