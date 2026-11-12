"""Read-only: decompress an XCOM 2 WOTC save (UE3 chunked LZO1X) in memory and report which names of interest occur.
Usage: python savescan.py "<save file name>" [dump]
Writes nothing unless 'dump' is given (then writes the decompressed blob next to this script for further greps)."""
import sys, struct, os, re, collections

def lzo1x(src, outlen):
    out = bytearray()
    ip = 0
    n = len(src)
    def copy_match(dist, length):
        start = len(out) - dist
        if start < 0:
            raise ValueError("bad match")
        if dist >= length:
            out.extend(out[start:start + length])
        else:
            for i in range(length):
                out.append(out[start + i])
    t = src[ip]
    state = "top"
    if t > 17:
        ip += 1
        t -= 17
        if t < 4:
            state = "match_next"
        else:
            out.extend(src[ip:ip + t]); ip += t
            state = "first_literal_run"
    while True:
        if state == "top":
            t = src[ip]; ip += 1
            if t >= 16:
                state = "match"
                continue
            if t == 0:
                while src[ip] == 0:
                    t += 255; ip += 1
                t += 15 + src[ip]; ip += 1
            out.extend(src[ip:ip + t + 3]); ip += t + 3
            state = "first_literal_run"
        elif state == "first_literal_run":
            t = src[ip]; ip += 1
            if t >= 16:
                state = "match"
                continue
            dist = 1 + 0x0800 + (t >> 2) + (src[ip] << 2); ip += 1
            copy_match(dist, 3)
            state = "match_done"
        elif state == "match":
            if t >= 64:
                dist = 1 + ((t >> 2) & 7) + (src[ip] << 3); ip += 1
                length = (t >> 5) - 1 + 2
                copy_match(dist, length)
            elif t >= 32:
                t &= 31
                if t == 0:
                    while src[ip] == 0:
                        t += 255; ip += 1
                    t += 31 + src[ip]; ip += 1
                dist = 1 + (src[ip] >> 2) + (src[ip + 1] << 6); ip += 2
                copy_match(dist, t + 2)
            elif t >= 16:
                dist = (t & 8) << 11
                t &= 7
                if t == 0:
                    while src[ip] == 0:
                        t += 255; ip += 1
                    t += 7 + src[ip]; ip += 1
                dist += (src[ip] >> 2) + (src[ip + 1] << 6); ip += 2
                if dist == 0:
                    break  # end of stream
                dist += 0x4000
                copy_match(dist, t + 2)
            else:
                dist = 1 + (t >> 2) + (src[ip] << 2); ip += 1
                copy_match(dist, 2)
            state = "match_done"
        elif state == "match_done":
            t = src[ip - 2] & 3
            if t == 0:
                state = "top"
            else:
                state = "match_next"
        elif state == "match_next":
            out.extend(src[ip:ip + t]); ip += t
            t = src[ip]; ip += 1
            state = "match"
    if outlen and len(out) != outlen:
        raise ValueError("length mismatch %d != %d" % (len(out), outlen))
    return bytes(out)

def load(fn):
    b = open(fn, "rb").read()
    magic = bytes.fromhex("c1832a9e")
    p = b.find(magic)
    blob = bytearray()
    nchunks = 0
    while p >= 0 and p < len(b):
        if b[p:p + 4] != magic:
            p = b.find(magic, p)
            if p < 0:
                break
        _, blocksize, ctot, utot = struct.unpack_from("<IIII", b, p)
        q = p + 16
        blocks = []
        got = 0
        while got < utot:
            c, u = struct.unpack_from("<II", b, q); q += 8
            blocks.append((c, u)); got += u
        for c, u in blocks:
            blob.extend(lzo1x(b[q:q + c], u)); q += c
        nchunks += 1
        p = q
    return bytes(blob), nchunks

if __name__ == "__main__":
    d = r"C:\Users\Idi\Documents\My Games\XCOM2 War of the Chosen\XComGame\SaveData"
    blob, n = load(os.path.join(d, sys.argv[1]))
    print("chunks", n, "decompressed bytes", len(blob))
    if len(sys.argv) > 2 and sys.argv[2] == "dump":
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_blob.bin")
        open(out, "wb").write(blob)
        print("wrote", out)
    for pat in [rb"ResCard_[A-Za-z0-9_]+", rb"CovertActionRisk_[A-Za-z0-9_]+", rb"CovertAction_[A-Za-z0-9_]+"]:
        c = collections.Counter(m.decode() for m in re.findall(pat, blob))
        print(pat.decode(), len(c), "distinct")
        for k, v in sorted(c.items()):
            print("   ", v, k)
