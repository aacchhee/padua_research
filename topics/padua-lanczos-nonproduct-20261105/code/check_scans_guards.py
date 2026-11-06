#!/usr/bin/env python3
"""Executed negative controls for the actual P6 interfaces, not a formula proof."""
import copy, hashlib, json, platform, subprocess, sys
from pathlib import Path
from p6_inputs import prepare
from p6_rows import validate
ROOT=Path(__file__).resolve().parents[1]
WORK=Path('/tmp/padua-lanczos-nonproduct-20261105/scan-review')
def identity(p):
    b=Path(p).read_bytes(); return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def main():
    results=[]
    def rejects(label,call):
        try:call()
        except (AssertionError,ValueError,ZeroDivisionError): results.append(label);return
        raise AssertionError('accepted malformed control '+label)
    base=json.loads((WORK/'H24_222/spec.json').read_text()); prepare(base)
    for label,mutate in [
        ('negative weight',lambda s:s['points'][0].__setitem__(2,'-1')),
        ('zero weight',lambda s:s['points'][0].__setitem__(2,'0')),
        ('duplicate node',lambda s:s['points'].append(s['points'][0])),
        ('bad rational',lambda s:s['points'][0].__setitem__(0,'1/0')),
        ('empty point set',lambda s:s.update(points=[])),
        ('bad family label',lambda s:s.update(family='../bad'))]:
        data=copy.deepcopy(base);mutate(data);rejects('input: '+label,lambda:prepare(data))
    row=json.loads((WORK/'H24_222/producer-bj.jsonl').read_text().splitlines()[0]);validate(row,'H24_222',325)
    for label,mutate in [
        ('restricted sources',lambda r:r.update(sources='one')),
        ('omitted source',lambda r:r.update(source_count=4)),
        ('wrong count',lambda r:r.update(point_count=324)),
        ('wrong trace',lambda r:r.update(normal_trace_exact='0')),
        ('missing Gram coverage',lambda r:r.update(exact_gram_pairs_checked=0)),
        ('illegal parent',lambda r:r['pivot_choices'].__setitem__(0,'Y')),
        ('false upper minimum',lambda r:r['upper_squared'].update(exact='1')),
        ('nonpositive endpoint',lambda r:r['Knode_squared'].update(exact='0')),
        ('nonpivot tie',lambda r:r.update(pivot_ties=[[2,1]]))]:
        data=copy.deepcopy(row);mutate(data);rejects('row: '+label,lambda:validate(data,'H24_222',325))
    raw=(WORK/'H24_222/input.txt').read_text();lines=raw.splitlines()
    samples={'extra token':raw+'extra\n','truncated input':'\n'.join(lines[:-1])+'\n','unnormalized weights':raw.replace(lines[1],'-1 -1 1',1),'nonpositive weight':raw.replace(lines[1],'-1 -1 0',1),'M_not_above_N':'1\n0 0 1\n'}
    native=[];temp=WORK/'negative-input.txt'
    for backend in ('producer','checker'):
        exe=WORK/'H24_222'/backend
        for label,raw in samples.items():
            temp.write_text(raw);cmd=[str(exe),str(temp),'3','bj','test']
            p=subprocess.run(cmd,text=True,capture_output=True,timeout=10)
            assert p.returncode!=0
            native.append(dict(backend=backend,control=label,returncode=p.returncode,diagnostic=p.stderr.strip()))
    p=subprocess.run([str(WORK/'H24_222/producer'),'--self-test'],text=True,capture_output=True,check=True)
    controls=json.loads(p.stdout)
    output=ROOT/'evidence/check-scans-guards.json'
    record=dict(status='PASS 15 Python rejection controls, 10 native rejections, native primitive self-test',command=[sys.executable,'-B',*sys.argv],python=platform.python_version(),checker=identity(__file__),code_inputs=[identity(Path(__file__).with_name(p)) for p in ('p6_inputs.py','p6_rows.py','p6_native.cpp','p6_scalar_check.cpp')],python_rejections=results,native_rejections=native,native_self_test=controls)
    output.write_text(json.dumps(record,indent=2)+'\n'); print(record['status'])
if __name__=='__main__':main()
