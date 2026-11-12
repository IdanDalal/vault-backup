"""Usage: python ctx.py <ascii needle> [before=400] [after=200] [max=12]
Prints printable strings (>=4 chars) around each occurrence of needle in save_blob.bin."""
import sys, re, os
blob = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_blob.bin"), "rb").read()
needle = sys.argv[1].encode()
before = int(sys.argv[2]) if len(sys.argv) > 2 else 400
after = int(sys.argv[3]) if len(sys.argv) > 3 else 200
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 12
p = 0
k = 0
while True:
    p = blob.find(needle, p)
    if p < 0:
        break
    k += 1
    if k <= mx:
        seg = blob[max(0, p - before):p + after]
        strs = [s.decode("latin1") for s in re.findall(rb"[ -~]{4,}", seg)]
        print("@%d: %s" % (p, " | ".join(strs)))
        print()
    p += len(needle)
print("occurrences:", k)
