"""Build exact endpoint extension in scratch and publish a toolchain receipt."""
if not __debug__:
    raise RuntimeError("T1 native build refuses optimized Python")
import argparse,hashlib,json,os,shutil,subprocess,sys,sysconfig
from pathlib import Path

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',required=True);ap.add_argument('--compiler',default='cc');a=ap.parse_args()
    target=Path(a.output_dir).resolve();target.mkdir(parents=True,exist_ok=True)
    here=Path(__file__).resolve();source=here.with_name('t1_native.c');source_sha=digest(source)
    compiler=shutil.which(a.compiler)
    if compiler is None:raise RuntimeError('compiler unavailable')
    binary=target/('_t1_native'+sysconfig.get_config_var('EXT_SUFFIX'));temporary=binary.with_name(binary.name+'.building')
    command=[compiler,'-O3','-shared','-fPIC','-I'+sysconfig.get_path('include'),str(source),'-o',str(temporary)]
    subprocess.run(command,check=True)
    if digest(source)!=source_sha:raise RuntimeError('source changed during build')
    os.replace(temporary,binary)
    receipt={'source_sha256':source_sha,'binary_path':str(binary),'binary_sha256':digest(binary),'command':command,
      'compiler_path':compiler,'compiler_sha256':digest(compiler),'compiler_version':subprocess.check_output([compiler,'--version'],text=True),
      'python':sys.version,'python_executable':sys.executable,'soabi':sysconfig.get_config_var('SOABI'),
      'build_script_sha256':digest(here)}
    output=target/'build-receipt.json';output.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n');print(output)
if __name__=='__main__':main()
