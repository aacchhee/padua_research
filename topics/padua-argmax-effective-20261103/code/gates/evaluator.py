"""O(n²) corrected rhombus kernel, float samples only, not enclosures."""
import numpy as np

class Evaluator:
    def __init__(self, n, dtype=np.float64):
        self.n = n
        self.dtype = dtype
        j, k = np.nonzero((np.arange(n+1)[:,None] + np.arange(n+2)[None,:]) % 2 == 0)
        pi = np.arccos(dtype(-1))
        self.pi = pi
        self.th = j.astype(dtype)*pi/n
        self.ph = k.astype(dtype)*pi/(n+1)
        self.w = (2*np.where((j==0)|(j==n), .5, 1.) * np.where((k==0)|(k==n+1), .5, 1.)/(n*(n+1))).astype(dtype)
    def U(self, k, z):
        # Reduce before sin(kz). The removable values are supplied by sinc.
        q = np.rint(z/self.pi).astype(np.int64)
        r = z-q*self.pi
        return k*np.sinc(k*r/self.pi)/np.sinc(r/self.pi)*np.where((q*(k-1))%2, -1, 1)
    def g(self, u, v):
        s, t = (u+v)/2, (v-u)/2
        return self.U(self.n+1,s)*self.U(self.n+1,t) + self.U(self.n,s)*self.U(self.n,t) - np.cos(self.n*u)
    def point(self, theta, phi):
        signed = np.zeros_like(self.w)
        absolute = np.zeros_like(self.w)
        for sx in (1,-1):
            for sy in (1,-1):
                g = self.g(theta+sx*self.th, phi+sy*self.ph)
                signed += g/4
                absolute += np.abs(g)/4
        return float(np.dot(self.w,np.abs(signed))), float(np.dot(self.w,absolute))
    def corner(self):
        # The odd endpoint indices are precisely the two nonnode corners.
        return [(j,k) for j in (0,self.n) for k in (0,self.n+1) if (j+k)%2]
