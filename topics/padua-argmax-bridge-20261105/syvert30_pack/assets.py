"""Trusted Debian arithmetic payloads; no download, installation or setup fallback.
Only producer invocation (after release) reads package archives through dpkg-deb.
"""
import io
import posixpath
from pathlib import Path
import subprocess
import tarfile
from common import digest
from plans import ASSET
OLD = 'local-output/argmax-bridge-20261105/phase-checker/runtime/'
NEW = 'local-output/argmax-bridge-20261105/final-assets-public-retrieval-network/'
PINS = [
    ('f/flint/', 'libflint-dev_3.1.3-2_amd64.deb', '484b6507b41a1669c8d58562eb53afeeb3955dbdf8e47d3ba4ba63aa14109928', OLD, 'libflint-dev', '3.1.3-2'),
    ('f/flint/', 'libflint19_3.1.3-2_amd64.deb', '81ac3b20d8a1f125100c84b10b3825a9344080575f88769b553dfe5b008b9e4a', OLD, 'libflint19', '3.1.3-2'),
    ('m/mpfr4/', 'libmpfr-dev_4.2.2-1_amd64.deb', '43cbe73a48cce65232ad5d4219a67dfdd0974f45aa88d381ae051d64052b996a', OLD, 'libmpfr-dev', '4.2.2-1'),
    ('m/mpfr4/', 'libmpfr6_4.2.2-1_amd64.deb', '75dddce11dabc7fc543712c33dc27b7f2ee66a111763eb5eac654d010b42cd92', NEW, 'libmpfr6', '4.2.2-1'),
    ('g/gmp/', 'libgmp-dev_6.3.0+dfsg-3_amd64.deb', '68f392cc03f896ecc3764eb4844d2a898ff016f47dda160465f152f811152b81', NEW, 'libgmp-dev', '2:6.3.0+dfsg-3'),
    ('g/gmp/', 'libgmp10_6.3.0+dfsg-3_amd64.deb', 'd0d0265eb01770f17afd0f7c8c0622f80479dcfbbe13653a0debeec61464e622', NEW, 'libgmp10', '2:6.3.0+dfsg-3')]

def trusted_assets(repo):
    members = {}; origins = []; packages = {}
    for directory, name, sha, local, package, version in PINS:
        path = Path(repo) / local / name; data = path.read_bytes()
        if digest(data) != sha: raise ValueError('pinned package bytes differ: ' + name)
        metadata = subprocess.check_output(['dpkg-deb', '-f', str(path), 'Package', 'Version', 'Architecture'], text=True)
        fields = dict(line.split(': ', 1) for line in metadata.splitlines())
        if fields != {'Package': package, 'Version': version, 'Architecture': 'amd64'}:
            raise ValueError('pinned package metadata mismatch')
        origins.append({'url': 'https://deb.debian.org/debian/pool/main/' + directory + name,
                        'snapshot_binary_api': 'https://snapshot.debian.org/mr/binary/' + package + '/' + version + '/binfiles?fileinfo=1',
                        'snapshot_package_index': 'https://snapshot.debian.org/package/' + directory.split('/')[1] + '/' + version + '/',
                        'sha256': sha, 'bytes': len(data), 'package': package, 'version': version, 'architecture': 'amd64'})
        packages['asset-packages/' + name] = data
        payload = subprocess.check_output(['dpkg-deb', '--fsys-tarfile', str(path)])
        with tarfile.open(fileobj=io.BytesIO(payload), mode='r:') as archive:
            for member in archive:
                rel = member.name.removeprefix('./')
                if member.isfile():
                    stream = archive.extractfile(member); members[rel] = ('bytes', stream.read())
                elif member.issym(): members[rel] = ('link', member.linkname)
    def resolve(name, seen=None):
        seen = set() if seen is None else seen
        if name in seen or name.startswith('/') or '..' in Path(name).parts: raise ValueError('unsafe package alias')
        seen.add(name); kind, value = members[name]
        if kind == 'bytes': return value
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), value))
        return resolve(target, seen)
    assets = {}
    for name in sorted(members):
        header = name.startswith('usr/include/')
        library = name.startswith('usr/lib/x86_64-linux-gnu/') and Path(name).name.startswith(('libflint.so', 'libgmp.so', 'libmpfr.so'))
        if header or library: assets[ASSET + '/' + name.removeprefix('usr/')] = resolve(name)
    assets[ASSET + '/include/gmp.h'] = resolve('usr/include/x86_64-linux-gnu/gmp.h')
    for needed in ['include/flint/flint.h', 'include/mpfr.h', 'include/gmp.h',
                   'lib/x86_64-linux-gnu/libflint.so.19', 'lib/x86_64-linux-gnu/libgmp.so.10', 'lib/x86_64-linux-gnu/libmpfr.so.6']:
        if ASSET + '/' + needed not in assets: raise ValueError('incomplete trusted arithmetic closure: ' + needed)
    return assets, packages, origins
