"""Auditor B2: stdlib NPY parse of regenerated n12 joint_norm nodes vs payload bytes."""
import sys, json, base64, hashlib, struct, ast
raw = open(sys.argv[1], 'rb').read()
assert raw[:6] == b'\x93NUMPY'
major = raw[6]
hl = struct.unpack('<H', raw[8:10])[0] if major == 1 else struct.unpack('<I', raw[8:12])[0]
off = 10 if major == 1 else 12
hdr = ast.literal_eval(raw[off:off+hl].decode('latin1'))
body = raw[off+hl:]
pay = json.load(open(sys.argv[2]))
pb = base64.b85decode(pay['coordinates_base85'])
print(json.dumps({'npy_sha256': hashlib.sha256(raw).hexdigest(), 'npy_bytes': len(raw), 'header': str(hdr),
  'body_bytes': len(body), 'body_equals_payload': body == pb, 'payload_coord_sha256': hashlib.sha256(pb).hexdigest(),
  'payload_source_nodes_sha256_matches': hashlib.sha256(raw).hexdigest() == pay['source_nodes']['sha256']}))
