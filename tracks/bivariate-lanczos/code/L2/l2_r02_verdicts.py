"""R02 verdicts (rules in directions/L2/candidates.md, R02 pre-registration): IDEA?...-207 (selection rules, from
logs/r02_selection.raw), -208 (logs/r02_pro.raw), -209 (logs/r02_proJ.raw).
Usage: python3 -I l2_r02_verdicts.py <logdir> > <logdir>/r02_verdicts.txt"""
import sys, os, json
import numpy as np

U = 2.0 ** -53
SQRTU, U34 = U ** 0.5, U ** 0.75
NONPROD = {'rot0.3', 'rotpi4', 'disk', 'triangle', 'lshape', 'annulus'}


def Nof(n):
    return (n + 1) * (n + 2) // 2


def rows(path):
    import gzip
    if not os.path.exists(path) and os.path.exists(path + '.gz'):
        f = gzip.open(path + '.gz', 'rt')
    else:
        f = open(path)
    return [json.loads(l[5:]) for l in f if l.startswith('JSON')]


def main(d):
    sel = rows(os.path.join(d, 'r02_selection.raw'))
    print("# R02 verdicts (u = 2^-53)")
    print("\n## IDEA-207: per selection, fullcgs2 runs; kill: thetaLB > sqrt(u) or (drift > sqrt(u) with ref < 1e-11) on a"
          " non-product set; survive: thetaLB <= 1e3 u sqrt(N) and drift <= 1e3 max(ref, u sqrt(N)) everywhere")
    benches = []
    for r in sel:
        if r['bench'] not in benches:
            benches.append(r['bench'])
    for mode in ('fullcgs2', 'w2', 'tworel'):
        sels = []
        for r in sel:
            if r['mode'] == mode and r['sel'] not in sels:
                sels.append(r['sel'])
        for s in sels:
            kills, nosurv = [], []
            print(f"-- selection {s} ({mode}): max over degrees of (loss, thetaLB, drift [ref]) per benchmark")
            for b in benches:
                rr = [r for r in sel if r['bench'] == b and r['sel'] == s and r['mode'] == mode]
                if not rr:
                    continue
                last = rr[-1]
                mL = max(r['loss'] for r in rr); mlb = max(r['thetaLB'] for r in rr)
                kd = [r for r in rr if r['drift'] > SQRTU and r['ref'] < 1e-11]
                k = (b in NONPROD) and (mlb > SQRTU or bool(kd))
                surv = all(r['thetaLB'] <= 1e3 * U * np.sqrt(Nof(r['n'])) and
                           r['drift'] <= 1e3 * max(r['ref'], U * np.sqrt(Nof(r['n']))) for r in rr)
                if k: kills.append(b)
                if not surv: nosurv.append(b)
                first = next((r['n'] for r in rr if r['thetaLB'] > SQRTU), None)
                print(f"   {b:9s} n<= {last['n']:2d}: maxL={mL:.1e} max thetaLB={mlb:.1e} (first > sqrt u at n={first}) "
                      f"drift(nmax)={last['drift']:.1e} [ref {last['ref']:.0e}] {'KILL' if k else ''}")
            if mode == 'fullcgs2':
                v = 'KILLED on ' + ','.join(kills) if kills else ('SURVIVES' if not nosurv else 'inconclusive (not within survival band on ' + ','.join(nosurv) + ')')
                print(f"   => IDEA-207 for selection {s}: {v}")
    for fn, tag in (('r02_pro.raw', 'IDEA-208 PRO-2D (E1D trigger)'), ('r02_proJ.raw', 'IDEA-209 PRO-2D-J (J-rows measured)')):
        p = os.path.join(d, fn)
        if not (os.path.exists(p) or os.path.exists(p + '.gz')):
            continue
        R = rows(p)
        print(f"\n## {tag}: kill if L(n) > 10 sqrt(u) at some degree, or eF > u^(3/4) at a degree with L <= sqrt(u)")
        killed = []
        for r in R:
            st = r['stats']; full = r['full']
            frac = (st['dots_reorth'] + st['dots_measure']) / full
            tot = (st['dots_window'] + st['dots_reorth'] + st['dots_measure']) / full
            maxL = max(r['L']); maxeF = max([x.get('eF', 0) for x in r['recs'] if x['loss'] <= SQRTU] + [0])
            maxeH = max([x.get('eH', 0) for x in r['recs']] + [0]); maxdJ = max(x['defJ'] for x in r['recs'])
            kk = bool(r['kill_L'] or r['kill_F'])
            if kk: killed.append(r['bench'])
            print(f"   {r['bench']:9s} maxL={maxL:.1e} max eF(SO)={maxeF:.1e} max eH={maxeH:.1e} max defJ={maxdJ:.1e} "
                  f"reorth cols={st['n_reorth']:3d} (reorth+measure)/full={frac:.3f} total/full={tot:.3f} "
                  f"{'KILL ' + str(r['kill_L']) + str(r['kill_F']) if kk else ''}")
        print(f"   => {'KILLED on ' + ','.join(killed) if killed else 'survives'}")


if __name__ == '__main__':
    main(sys.argv[1])
