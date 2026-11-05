#!/usr/bin/env python3
"""Conservative whole-repository non-record inventory (same classifier as PR20)."""
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
paths=set(subprocess.check_output(['git','-C',str(ROOT),'ls-files','--cached','--others','--exclude-standard'],text=True).splitlines())
record_ext={'md','py','sh','tex','bib','svg','gitignore'}
rows=sorted((p,(ROOT/p).stat().st_size) for p in paths if (ROOT/p).is_file() and p.rsplit('.',1)[-1].lower() not in record_ext)
raw=''.join(str(size)+'\t'+p+'\n' for p,size in rows).encode();total=sum(n for p,n in rows)
print(json.dumps({'scope':'All tracked and nonignored prospective files, excluding exactly md/py/sh/tex/bib/svg/gitignore, matching PR20 conservative classifier; includes actual C/C++ sources and manifest metadata without subtracting them.','files':len(rows),'bytes':total,'limit_bytes':5000000,'margin_bytes':5000000-total,'margin_percent':100*(5000000-total)/5000000,'inventory_sha256':hashlib.sha256(raw).hexdigest()},indent=2))
