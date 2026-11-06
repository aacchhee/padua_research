#!/usr/bin/env python3
"""Deterministic compact essential evidence from the frozen full raw receipt."""
import argparse,hashlib,json
from pathlib import Path
RAW_HASH='7ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2'
COLUMNS=['N','minimum','maximum','minimum_inverse_residual_2_float','maximum_inverse_residual_2_float','minimum_constraint_residual_float','maximum_constraint_residual_float']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def generate(raw):
 assert sha(raw)==RAW_HASH;source=json.loads(raw.read_text());assert source['completed'] and len(source['results'])==42;assert all(r['guards_pass'] and r['inverse_extrema_order_pass'] for r in source['results'])
 rows=[]
 for r in source['results']:
  lo=r['results']['minimum'];hi=r['results']['maximum'];rows.append([r['N'],lo['eigenvalue'],hi['eigenvalue'],lo['inverse_residual_2_float'],hi['inverse_residual_2_float'],lo['constraint_residual_float'],hi['constraint_residual_float']])
 return dict(format='S4-essential-CC-v1',status='MEASURED',raw_receipt_sha256=RAW_HASH,raw_receipt_bytes=raw.stat().st_size,generator_sha256=sha(__file__),code_and_proposal_sha256=source['code_and_proposal_sha256'],environment={k:source[k] for k in ['pin','preregistration_commit','python','numpy','scipy','mpmath','platform','threads','seed','tol','ncv','maxiter','inverse_residual_guard','constraint_guard']},columns=COLUMNS,rows=rows,scope='All42 registered rows, both N parities; no fits, no timing or work vectors. Full raw remains local pending archival.')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--raw',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--check',action='store_true');args=ap.parse_args();content=(json.dumps(generate(args.raw),separators=(',',':'),allow_nan=False)+'\n').encode();assert len(content)<16384
 if args.check:assert args.output.read_bytes()==content,'Essential bytes differ from frozen raw derivation.'
 else:args.output.write_bytes(content)
 print(json.dumps(dict(pass_check=True,rows=42,bytes=len(content),sha256=hashlib.sha256(content).hexdigest())))
if __name__=='__main__':main()
