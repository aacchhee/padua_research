"""Compare actually executed replay stdout to the pinned Claude reference."""
from pathlib import Path
import hashlib,json,re
OUT=Path(__file__).resolve().parent
TOL=1e-10
NUMBER=re.compile(r'(?<![A-Za-z_])[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')
rows=[]
for name in ['check','cell','interior','edgeprofile','strips','n2_edges']:
    ref=OUT.parent/(name+'.out'); run=OUT/(name+'.out')
    a,b=ref.read_text(),run.read_text()
    # Strip the NumPy scalar repr marker before tokenising numbers.
    aa=[float(s) for s in NUMBER.findall(a.replace('np.float64','scalar'))]
    bb=[float(s) for s in NUMBER.findall(b.replace('np.float64','scalar'))]
    maxdiff=max((abs(x-y) for x,y in zip(aa,bb)),default=0.) if len(aa)==len(bb) else None
    rows.append({'script':name+'.py','reference':str(ref),'replay':str(run),'reference_sha256':hashlib.sha256(ref.read_bytes()).hexdigest(),'replay_sha256':hashlib.sha256(run.read_bytes()).hexdigest(),'text_identical_after_outer_whitespace_strip':a.strip()==b.strip(),'numeric_tokens':len(aa),'same_numeric_token_count':len(aa)==len(bb),'max_abs_numeric_token_difference':maxdiff,'absolute_tolerance':TOL,'numeric_comparison_pass':maxdiff is not None and maxdiff<=TOL})
(OUT/'comparison.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
assert all(r['numeric_comparison_pass'] and r['text_identical_after_outer_whitespace_strip'] for r in rows)
