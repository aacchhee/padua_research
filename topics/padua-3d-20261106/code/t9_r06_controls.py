#!/usr/bin/env python3
"""Reproduce inherited controls without legacy fixed temporary paths."""
import argparse,hashlib,json,platform,sys
from pathlib import Path
import numpy as np
import scipy
TOP=Path(__file__).resolve().parents[1];sys.path.insert(0,str(TOP/'code'));import t9_r06_maxima as m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.scratch.mkdir(parents=True,exist_ok=True)
 legacy=json.loads((TOP/'evidence/t9-maxima.json').read_text());qr=json.loads((TOP/'evidence/t9-r06-qr.json').read_text());rows=[]
 for n in (4,8):
  before=next(r for r in legacy['rows'] if r['n']==n and r['family']=='qr');now=next(r for r in qr['rows'] if r['n']==n);delta=abs(before['local']-now['local']);assert delta<1e-10;rows.append({'family':'qr','n':n,'old':before['local'],'new':now['local'],'abs_delta':delta})
 points=m.prev.points(2,'localdet');r=m.measure(2,'legacy_two_sweep',points,a.scratch,{})
 before=next(r for r in legacy['rows'] if r['n']==2 and r['family']=='localdet');assert abs(before['local']-r['local'])<1e-10
 rows.append({'family':'legacy_two_sweep','n':2,'old':before['local'],'new':r['local'],'abs_delta':abs(before['local']-r['local'])})
 out={'status':'MEASURED inherited controls reproduced; new localdet is a separate frozen one-sweep variant','command':sys.argv,'seed':0,'code_sha256':sha(__file__),'helpers':{Path(f).name:sha(f) for f in (m.__file__,m.prev.__file__)},'inputs':{str(f.relative_to(TOP)):sha(f) for f in (TOP/'evidence/t9-maxima.json',TOP/'evidence/t9-r06-qr.json')},'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'scratch':str(a.scratch),'rows':rows}
 a.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
