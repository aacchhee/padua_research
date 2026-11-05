import json
W='/tmp/claude-0/-home-user-padua-research/4e9db0f4-c32d-5606-95a7-0413431483a5/scratchpad/PROT/work/'
R='/home/user/padua_research/topics/padua-lanczos-frontier-20261105/evidence/'
ind=json.load(open(R+'g0-independent.json'))['runs']['baseline']['methods']
hist={'T24':{'dev':ind['dev']['historical_gap'],'mirror':ind['mirror']['historical_gap'],'alt':ind['alt']['historical_gap'],'adapt':ind['adapt']['historical_gap']}}
rep=json.load(open(R+'g4-replay.json'))
hin={}
for c in rep['cases']:
    hist[c['name']]={m:v['old_gap'] for m,v in c['checks']['methods'].items() if m in ('dev','mirror','alt','adapt')}
hin={'T24':'bd2a98cab06f16494f95d89697091aeacebd3a87fdbd760ffaac707bfc57a929','rotpi4':'a356501243b1fc883f795ee0908966b1fbeac4be09312e7eb8ee75f602229d42','triangle':'806ae0a1e54e9301955c9f7ddc52924922b3a8c51a7198174a0d476b291f0379'}
for core in ['default','SkylakeX','Haswell','Nehalem']:
    d=json.load(open(W+f'legacy-{core}.json'))
    print('==',core,'numpy',d['numpy'])
    for name,rec in d['cases'].items():
        ok=rec['input_sha256']==hin[name]
        print(f"  {name:8s} input_hash_match={ok}")
        for m,g in rec['gaps'].items():
            h=hist[name][m]
            print(f"     {m:7s} new={g!r:24s} hist={h!r:24s} equal={g==h} rel={abs(g-h)/h:.2e}")
