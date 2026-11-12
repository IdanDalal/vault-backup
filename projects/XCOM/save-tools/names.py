"""Usage: python names.py <regex> [max=80]  -> tally of regex matches (bytes, ASCII) in save_blob.bin"""
import sys, re, os, collections
blob = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_blob.bin"), "rb").read()
c = collections.Counter(m.decode("latin1") for m in re.findall(sys.argv[1].encode(), blob))
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 80
print(len(c), "distinct")
for k, v in sorted(c.items())[:mx]:
    print("  ", v, k)
