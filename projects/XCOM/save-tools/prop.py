"""Usage: python prop.py <PropName> [max=20] [ctxprop]
Decodes each occurrence of a serialized property in save_blob.bin (Int/Float/Bool/Name/Array count).
If ctxprop given, also prints the nearest preceding m_TemplateName value."""
import sys, os, struct, re
blob = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_blob.bin"), "rb").read()
def rstr(p):
    n = struct.unpack_from("<i", blob, p)[0]
    if n <= 0 or n > 200:
        return None, p
    s = blob[p + 4:p + 4 + n - 1].decode("latin1")
    return s, p + 4 + n
def decode(p):
    # p points at length prefix of property name
    name, q = rstr(p)
    q += 4
    typ, q = rstr(q)
    if typ is None:
        return None
    q += 4
    size, idx = struct.unpack_from("<ii", blob, q); q += 8
    if typ == "IntProperty":
        return typ, struct.unpack_from("<i", blob, q)[0]
    if typ == "FloatProperty":
        return typ, round(struct.unpack_from("<f", blob, q)[0], 3)
    if typ == "BoolProperty":
        return typ, blob[q]
    if typ == "NameProperty":
        s, _ = rstr(q)
        return typ, s
    if typ == "ArrayProperty":
        return typ, "count=%d size=%d" % (struct.unpack_from("<i", blob, q)[0], size)
    if typ == "StrProperty":
        s, _ = rstr(q)
        return typ, s
    return typ, "size=%d" % size
def last_template(p):
    k = blob.rfind(b"m_TemplateName\x00", 0, p)
    if k < 0:
        return "?"
    r = decode(k - 4)
    return r[1] if r else "?"
name = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 20
needle = struct.pack("<i", len(name) + 1) + name.encode() + b"\x00"
p = 0; k = 0
while True:
    p = blob.find(needle, p)
    if p < 0:
        break
    r = decode(p)
    if r:
        k += 1
        if k <= mx:
            print("@%d %s = %s %s   [state: %s]" % (p, name, r[0], r[1], last_template(p)))
    p += len(needle)
print("occurrences:", k)
