"""Usage: python hexctx.py <needle> [after=96] [max=3] -> hex+ascii dump after each occurrence in save_blob.bin"""
import sys, os
blob = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_blob.bin"), "rb").read()
needle = sys.argv[1].encode()
after = int(sys.argv[2]) if len(sys.argv) > 2 else 96
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3
p = 0; k = 0
while True:
    p = blob.find(needle, p)
    if p < 0: break
    k += 1
    if k <= mx:
        seg = blob[p - 8:p + len(needle) + after]
        print("@%d" % p)
        for i in range(0, len(seg), 32):
            row = seg[i:i + 32]
            print("  " + row.hex(" ") + "  " + "".join(chr(c) if 32 <= c < 127 else "." for c in row))
    p += len(needle)
print("occurrences:", k)
