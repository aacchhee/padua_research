#!/usr/bin/env python3
"""Check full-sweep coverage/precision agreement and emit a compact table.

Precision agreement remains a measurement, not an interval certificate.
"""
import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp


def compare(prefix,sizes,threshold):
    data,metadata = {},[]
    worst = mp.mpf(0)
    by_family = {}
    for family in ('krawtchouk','hahn'):
        loaded = []
        for precision in (180,260):
            path = Path(prefix+family+str(precision)+'.json')
            payload = path.read_bytes()
            d = json.loads(payload)
            assert [r['N'] for r in d['cases']]==sizes, 'incomplete or different size coverage'
            assert all(r['dps']==precision and r['family']==family for r in d['cases'])
            metadata.append(dict(path=str(path),bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest(),
                                 code_sha256=d['code_sha256'],baseline_sha256=d['baseline_sha256']))
            loaded.append(d)
        assert loaded[0]['code_sha256']==loaded[1]['code_sha256']
        assert loaded[0]['baseline_sha256']==loaded[1]['baseline_sha256']
        family_worst = mp.mpf(0)
        for a,b in zip(loaded[0]['cases'],loaded[1]['cases']):
            assert a['input_sha256']==b['input_sha256']
            for target in ('NN','step_line'):
                for model in ('mixed','componentwise','blocknorm'):
                    x,y = mp.mpf(a[target][model]['kappa']),mp.mpf(b[target][model]['kappa'])
                    error = abs(x-y)/abs(y)
                    assert mp.isfinite(error) and error<threshold, 'precision agreement failed'
                    family_worst = max(family_worst,error)
            data.setdefault(b['N'],{})[family] = b
        by_family[family] = str(family_worst)
        worst = max(worst,family_worst)
    return dict(worst_relative_agreement=str(worst),by_family=by_family,
                inputs=metadata,cases=[dict(N=N,
                    krawtchouk_NN=data[N]['krawtchouk']['NN']['mixed']['kappa'],
                    hahn_NN=data[N]['hahn']['NN']['mixed']['kappa'],
                    krawtchouk_step_line=data[N]['krawtchouk']['step_line']['mixed']['kappa'],
                    hahn_step_line=data[N]['hahn']['step_line']['mixed']['kappa']) for N in sizes])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prefix',default='/tmp/conditioning-full-')
    ap.add_argument('--sizes',nargs='+',type=int,default=list(range(4,65)))
    ap.add_argument('--threshold',default='1e-60')
    ap.add_argument('--markdown',action='store_true')
    args = ap.parse_args()
    with mp.workdps(320):
        result = compare(args.prefix,args.sizes,mp.mpf(args.threshold))
        if args.markdown:
            print('| N | NN Krawtchouk | NN Hahn | SL Krawtchouk | SL Hahn |')
            print('|---|---|---|---|---|')
            for row in result['cases']:
                print('| '+str(row['N'])+' | '+' | '.join(mp.nstr(mp.mpf(v),7) for k,v in row.items() if k!='N')+' |')
        else:
            print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
