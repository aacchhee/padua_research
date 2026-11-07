"""Bounded data-only return reads, streamed hashing and archive sizing."""
import hashlib
import zlib
from common import strict, digest
from evidence import require, safe

CHUNK = 1024 * 1024
MAX_MEMBER = 512 * CHUNK
MAX_TOTAL = 24 * 1024**3
MAX_COLLECTION = 16 * CHUNK


def bounded_inventory(z):
    infos = z.infolist()
    require(len(infos) <= 200000, 'ZIP member count limit')
    require(sum(i.file_size for i in infos) <= MAX_TOTAL, 'ZIP expanded total limit')
    for info in infos:
        safe(info.filename)
        require(0 <= info.file_size <= MAX_MEMBER, 'ZIP expanded member limit')
    require(z.getinfo('COLLECTION.json').file_size <= MAX_COLLECTION, 'collection size limit')
    collection = strict(z.read('COLLECTION.json'))
    require(type(collection.get('files')) is dict, 'collection inventory shape')
    for name, row in collection['files'].items():
        safe(name)
        require(type(row.get('bytes')) is int and 0 <= row['bytes'] <= MAX_MEMBER, 'inventory member bound')
        require(z.getinfo(name).file_size == row['bytes'], 'ZIP/inventory expanded size mismatch')
    return collection


def verify_payloads(z, collection):
    for name, row in collection['files'].items():
        h = hashlib.sha256(); count = 0
        with z.open(name) as stream:
            while block := stream.read(CHUNK):
                count += len(block)
                require(count <= row['bytes'], 'expanded stream exceeds inventory')
                h.update(block)
        require(count == row['bytes'] and h.hexdigest() == row['sha256'], 'payload inventory digest')


def verify_admissions(z, prefix, actual):
    names = sorted(n for n in z.namelist() if n.startswith(prefix + 'ledger/'))
    previous = None; admitted = []
    for i, name in enumerate(names):
        require(name == prefix + 'ledger/%06d.json' % i, 'ledger sequence')
        require(z.getinfo(name).file_size < 4096, 'ledger entry limit')
        data = z.read(name); row = strict(data)
        require(row['previous'] == previous and type(row['n']) is int and row['n'] not in admitted, 'ledger chain/retry')
        admitted.append(row['n']); previous = digest(data)
    require(actual <= set(admitted), 'unregistered attempt directory')
    return set(admitted)


def verify_history(z, prefix, access, run):
    names = z.namelist()
    history = [n for n in names if n.startswith(prefix + 'history/')]
    require(len(history) <= 1024, 'history entry count bound')
    for name in history:
        require(z.getinfo(name).file_size <= 65536, 'history entry size bound')
    summaries = {digest(z.read(n)): strict(z.read(n)) for n in history
                 if n.startswith(prefix + 'history/summary-')}
    require(summaries, 'append-only summary history required')
    current = z.read(prefix + 'summary.json')
    require(digest(current) in summaries, 'current summary missing from history')
    epochs = {}
    for name in names:
        if not name.startswith(prefix + 'history/preflight-'): continue
        require(z.getinfo(name).file_size <= 16384, 'preflight epoch bound')
        row = strict(z.read(name)); epoch = row['epoch']
        require(name == prefix + 'history/preflight-' + epoch + '.json' and epoch not in epochs, 'unique preflight epoch')
        require(row['inherited_SIGCHLD'] == 'SIG_DFL' and row['no_attempt_retry'] is True, 'startup provenance')
        if row['resume']:
            prior = summaries.get(row['previous_summary_sha256'])
            require(prior is not None and prior.get('quiescent') is True and prior.get('ECHILD') is True,
                    'resume requires preserved prior quiescence')
            require(prior['never_started'] == row['pending'], 'resume exact previous never-started set')
        else:
            require(row['previous_summary_sha256'] is None, 'fresh epoch has no prior summary')
        epochs[epoch] = row
    require(epochs, 'preflight epoch history required')
    for name in names:
        if not name.startswith(prefix + 'resume-'): continue
        row = strict(z.read(name)); epoch = row['epoch']
        require(epoch in epochs and epochs[epoch]['resume'] is True and row['pending'] == epochs[epoch]['pending'], 'resume/epoch linkage')
        require(name == prefix + 'resume-' + epoch + '.json', 'resume name/epoch linkage')
        require(row['provenance']['selected_cores'] == run['provenance']['selected_cores'], 'resume affinity changed')
        access.closure(row['provenance'])


def measure(path):
    """Exact raw digest and deflate payload length; bounded working memory."""
    h = hashlib.sha256(); size = 0; compressed = 0
    compressor = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
    with path.open('rb') as stream:
        while block := stream.read(CHUNK):
            h.update(block); size += len(block)
            compressed += len(compressor.compress(block))
    compressed += len(compressor.flush())
    return {'bytes': size, 'sha256': h.hexdigest()}, compressed
