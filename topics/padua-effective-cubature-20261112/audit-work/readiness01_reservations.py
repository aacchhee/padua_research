"""Read-only pinned reservation inventory; semantic ownership review is separate.

Run from any cwd; writes only an off-repository JSON receipt. This does not
refresh remote heads: the report documents the independent GitHub collection.
"""
import argparse, hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HEADS={'main':'b5388c25a2a5ccb8d0faf816ab87023cf347bcd3',
 'PR27':'b918c1d5bedba60e8255d7d2b985dd6c70f4690a',
 'PR34':'b4e00bdaf2ea391489523c28a7f25f0f4fc24c49',
 'PR35':'be28d3267bf6117878190b10f2d29840e524eac7'}
REG=['PROOF_STATUS.md','state/IDEAS.md','literature/INDEX.md','ID_CROSSWALK.md']
OWN='topics/padua-effective-cubature-20261112/ALLOCATIONS.md'
RANGES={'PD-T':(674,683),'PD-N':(246,250),'IDEA':(756,765),'LIT':(716,720)}
PUB='de39dabc7301b0de1463aaf2dab99365c4d7789e'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def numbers(text,ledger=False):
 out={k:set() for k in RANGES}
 for ns in out:
  pref={'PD-T':r'(?:PD-)?T','PD-N':r'(?:PD-)?N','IDEA':r'IDEA-?','LIT':r'LIT-?'}[ns]
  if not ledger and ns.startswith('PD-'):pref=ns
  for m in re.finditer(rf'(?<![A-Za-z0-9]){pref}(\d{{3}})(?!\d)(?:\s*[–−-]\s*(?:{pref})?(\d{{3}})(?!\d))?',text):
   lo=int(m[1]);hi=int(m[2] or lo)
   out[ns].update(range(min(lo,hi),max(lo,hi)+1))
 if ledger:
  for line in text.splitlines():
   cells=[x.strip().strip('*') for x in line.split('|')]
   if len(cells)>2 and cells[1] in out:
    out[cells[1]].update(map(int,re.findall(r'(?<!\d)\d{3}(?!\d)',cells[2])))
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('/tmp/padua-readiness-reservations/inventory.json'));args=ap.parse_args()
 files=[];distinct={};foreign={k:set() for k in RANGES};allnums={k:set() for k in RANGES};foreign_hits=[]
 for label,head in HEADS.items():
  paths=git('ls-tree','-r','--name-only',head).decode().splitlines()
  paths=[p for p in paths if p.endswith('/ALLOCATIONS.md') or p in REG]
  assert set(REG)<=set(paths)
  for p in paths:
   b=git('show',head+':'+p);text=b.decode();blob=git('rev-parse',head+':'+p).decode().strip();ns=numbers(text,p.endswith('/ALLOCATIONS.md'))
   # These exact mentions in the current topic ledger explicitly disclose
   # a test fixture and unregistered foreign audit prose, not reservations.
   if p==OWN:
    ns['PD-T'].discard(999);ns['PD-N'].difference_update({303,304})
   row={'label':label,'head':head,'path':p,'blob':blob,'bytes':len(b),'maxima':{k:max(v,default=0) for k,v in ns.items()}}
   files.append(row);distinct.setdefault(blob,{'path':p,'bytes':len(b),'maxima':row['maxima']})
   for k,v in ns.items():
    allnums[k].update(v)
    if label!='PR34':
     foreign[k].update(v)
     overlap=sorted(v&set(range(RANGES[k][0],RANGES[k][1]+1)))
     if overlap:foreign_hits.append([label,p,k,overlap])
   if blob not in [r['blob'] for r in files[:-1]]:
    for i,line in enumerate(text.splitlines(),1):
     if re.search(r'\bLIT-?\d{4}\b',line):print('FOREIGN_ALIAS_CONTEXT',p,i,line)
 foreignmax={k:max(v,default=0) for k,v in foreign.items()};unionmax={k:max(v,default=0) for k,v in allnums.items()}
 assert foreignmax=={'PD-T':673,'PD-N':245,'IDEA':755,'LIT':715},foreignmax
 assert unionmax=={'PD-T':683,'PD-N':250,'IDEA':765,'LIT':720},unionmax
 assert not foreign_hits,foreign_hits
 assert git('log','--diff-filter=A','--format=%H',HEADS['PR34'],'--',OWN).decode().splitlines()==[PUB]
 subprocess.run(['git','merge-base','--is-ancestor',PUB,'47892f13411132488a82e9dcd512d80dc543cd71'],cwd=ROOT,check=True)
 original=git('show',PUB+':'+OWN).decode()
 for ns,(lo,hi) in RANGES.items():assert lo in numbers(original,True)[ns] and hi in numbers(original,True)[ns]
 out={'heads':HEADS,'copies_read':len(files),'ledger_copies':sum(r['path'].endswith('/ALLOCATIONS.md') for r in files),
 'unique_ledger_blobs':len({r['blob'] for r in files if r['path'].endswith('/ALLOCATIONS.md')}),'unique_blobs':len(distinct),
 'foreign_maxima':foreignmax,'union_maxima':unionmax,'foreign_range_hits':foreign_hits,'reservation_commit':PUB,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'files':files}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
if __name__=='__main__':main()
