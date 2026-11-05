#!/usr/bin/env python3
"""Fetch pinned official Debian dependencies; extract locally without root.
Read cloud-runtime/network instructions before invocation. No vendoring to Git.
"""
import hashlib,pathlib,subprocess,urllib.request
BASE=pathlib.Path('local-output/argmax-bridge-20261105/phase-checker/runtime')
PACKAGES=[
 ('f/flint/libflint-dev_3.1.3-2_amd64.deb','484b6507b41a1669c8d58562eb53afeeb3955dbdf8e47d3ba4ba63aa14109928'),
 ('f/flint/libflint19_3.1.3-2_amd64.deb','81ac3b20d8a1f125100c84b10b3825a9344080575f88769b553dfe5b008b9e4a'),
 ('m/mpfr4/libmpfr-dev_4.2.2-1_amd64.deb','43cbe73a48cce65232ad5d4219a67dfdd0974f45aa88d381ae051d64052b996a')]
def main():
 BASE.mkdir(parents=True,exist_ok=True)
 for location,sha in PACKAGES:
  p=BASE/pathlib.Path(location).name
  if not p.exists():p.write_bytes(urllib.request.urlopen('https://deb.debian.org/debian/pool/main/'+location).read())
  if hashlib.sha256(p.read_bytes()).hexdigest()!=sha:raise RuntimeError('dependency digest mismatch: '+str(p))
  subprocess.run(['dpkg-deb','-x',str(p),str(BASE/'extracted')],check=True)
  print(p.name,sha)
if __name__=='__main__':main()
