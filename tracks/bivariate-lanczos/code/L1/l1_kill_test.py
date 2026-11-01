"""R01 decisive experiment for L1-Q1 (frozen kill test, plan.md) plus the pre-registered rotation pair
and loss-direction alignment. MEASURED only.

Usage: python3 -I l1_kill_test.py <runset> > logs/r01_<runset>.log
runsets: input3 | padua | irregular | rotation | swap | all
Writes a JSON line per (run, degree) to stdout prefixed with 'JSON ' for the analysis script.
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L

EPS = L.EPS
PHI = 1.0          # fixed oblique direction for the extra single section H_l = cos(PHI) H_x + sin(PHI) H_y


def analyse(name, P, w, nmax, methods=(('bj', 'block', 'cgs'), ('hl', 'exact', 'orth')), simax=True,
            degrees=None, dir_test=True):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    M = len(x)
    if degrees is None:
        degrees = list(range(4, nmax + 1, 4))
    Nof = lambda n: (n + 1) * (n + 2) // 2
    nq = nmax + 1 if dir_test else nmax
    if Nof(nq) > M:
        nq = nmax
        dir_test = False
    zN = x + 1j * y
    lN = np.cos(PHI) * x + np.sin(PHI) * y
    runs = []
    for (mname, win, orth) in methods:
        t0 = time.time()
        Q, coef, tab = L.recurrence(x, y, w, nq, win=win, orth=orth)
        G = Q.T @ Q
        U, _ = np.linalg.qr(Q)
        for n in degrees:
            Nn = Nof(n)
            loss = float(np.abs(G[:Nn, :Nn] - np.eye(Nn)).max())
            Un = U[:, :Nn]
            rx, thx, Sx = L.ritz_min(Un, x, True, want_vec=dir_test)
            ry, thy, Sy = L.ritz_min(Un, y, True, want_vec=dir_test)
            rz, thz, Sz = L.ritz_min(Un, zN, False, want_vec=True)
            rl, thl, _ = L.ritz_min(Un, lN, True)
            # joint minimiser: individual X and Y residuals with Rayleigh quotients, nearest node
            s = Sz[:, 0]; v = Un @ s; v = v / np.linalg.norm(v)
            rqx = np.vdot(v, x * v).real; rqy = np.vdot(v, y * v).real
            ex = float(np.linalg.norm((x - rqx) * v)); ey = float(np.linalg.norm((y - rqy) * v))
            inode, dnode = L.nearest_node(thz[0], P)
            rec = dict(run=name, method=mname, M=M, n=n, N=Nn, loss=loss,
                       res_x=float(rx[0]), res_y=float(ry[0]), res_z=float(rz[0]), res_l=float(rl[0]),
                       nconv_x=int(np.sum(rx < 1e-8)), nconv_y=int(np.sum(ry < 1e-8)),
                       nconv_z=int(np.sum(rz < 1e-8)),
                       thz=[float(thz[0].real), float(thz[0].imag)], node_dist=float(dnode),
                       zmin_xres=ex, zmin_yres=ey, thx=float(thx[0]), thy=float(thy[0]))
            # defects of the computed span under X and Y from one degree lower
            if n >= 1:
                Nm = Nof(n - 1)
                for nm, a in (('x', x), ('y', y)):
                    AU = a[:, None] * U[:, :Nm]
                    D = AU - Un @ (Un.T @ AU)
                    rec['defect_' + nm] = float(np.linalg.norm(D, axis=0).max())
            if dir_test:
                Qnew = Q[:, Nn:Nof(n + 1)]
                C = Un.T @ Qnew
                uu, sv, _ = np.linalg.svd(C, full_matrices=False)
                a = uu[:, 0]
                rec['newblock_loss'] = float(sv[0])
                for nm, S in (('x', Sx), ('y', Sy), ('z', Sz)):
                    k5 = min(5, S.shape[1])
                    al = [abs(np.vdot(S[:, i], a)) / np.linalg.norm(S[:, i]) for i in range(k5)]
                    rec['align_' + nm] = float(max(al))
                    rec['align1_' + nm] = float(al[0])
            runs.append(rec)
            print('JSON ' + json.dumps(rec), flush=True)
            print(f"{name:28s} {mname:3s} n={n:3d} N={Nn:5d} loss={loss:.1e} "
                  f"res_x={rx[0]:.1e} res_y={ry[0]:.1e} res_z={rz[0]:.1e} res_l={rl[0]:.1e} "
                  f"defX={rec.get('defect_x', 0):.1e} defY={rec.get('defect_y', 0):.1e} "
                  + (f"newloss={rec['newblock_loss']:.1e} al(x,y,z)=({rec['align_x']:.2f},{rec['align_y']:.2f},{rec['align_z']:.2f})"
                     if dir_test else ''), flush=True)
        print(f"# {name} {mname} done in {time.time() - t0:.1f}s", flush=True)
    if simax:
        t0 = time.time()
        Qc = L.recurrence_simax(x, y, w, nmax)
        Gc = Qc.conj().T @ Qc
        Uc, _ = np.linalg.qr(Qc)
        for n in degrees:
            Nn = Nof(n)
            loss = float(np.abs(Gc[:Nn, :Nn] - np.eye(Nn)).max())
            rz, thz, _ = L.ritz_min(Uc[:, :Nn], zN, False)
            rec = dict(run=name, method='simax', M=M, n=n, N=Nn, loss=loss, res_nk=float(rz[0]),
                       nconv_nk=int(np.sum(rz < 1e-8)))
            runs.append(rec)
            print('JSON ' + json.dumps(rec), flush=True)
            print(f"{name:28s} simax n={n:3d} N={Nn:5d} loss={loss:.1e} res_Nk={rz[0]:.1e}", flush=True)
        print(f"# {name} simax done in {time.time() - t0:.1f}s", flush=True)
    return runs


def main(which):
    print(f"# l1_kill_test.py runset={which} numpy={np.__version__} python={sys.version.split()[0]} EPS={EPS:.3e}")
    if which in ('input3', 'all'):
        P, w = L.nodes_random(1681, 0); analyse('random1681_s0', P, w, 40)
        P, w = L.nodes_random(6724, 0); analyse('random6724_s0', P, w, 40)
        P, w = L.nodes_tensor_cheb(41); analyse('tensorcheb41', P, w, 40, dir_test=False)
    if which in ('rotation', 'all'):
        P, w = L.nodes_random(1681, 0); analyse('random1681_s0_rot0.3', L.rotate(P, 0.3), w, 40)
        P, w = L.nodes_tensor_cheb(41); analyse('tensorcheb41_rot0.3', L.rotate(P, 0.3), w, 40)
        P, w = L.nodes_random(1681, 7); analyse('random1681_s7', P, w, 40)
        P, w = L.nodes_random(1681, 7); analyse('random1681_s7_rot1.0', L.rotate(P, 1.0), w, 40)
    if which in ('padua', 'all'):
        P, w = L.nodes_padua(48); analyse('padua48_cub', P, w, 48, degrees=list(range(4, 45, 4)) + [46, 47, 48])
        P, w = L.nodes_padua(80); analyse('padua80_cub', P, w, 48)
        P, w = L.nodes_padua(48); analyse('padua48_unif', P, np.ones(len(w)), 48,
                                          degrees=list(range(4, 45, 4)) + [46, 47, 48])
    if which in ('irregular', 'all'):
        P, w = L.nodes_lshape_random(3000, 1); analyse('Lshape_rand3000', P, w, 40)
        P, w = L.nodes_annulus_random(3000, 2); analyse('annulus_rand3000', P, w, 40)
        P, w = L.nodes_lshape_grid(61); analyse('Lshape_grid61', P, w, 40)
        P, w = L.nodes_lshape_grid(61); analyse('Lshape_grid61_rot0.3', L.rotate(P, 0.3), w, 40)
    if which in ('swap', 'all'):
        P, w = L.nodes_random(1681, 0); analyse('random1681_s0_swapxy', P[:, ::-1].copy(), w, 40, simax=False)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'input3')
