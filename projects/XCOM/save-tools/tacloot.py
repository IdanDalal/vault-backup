"""Scan tactical saves for loot-drop states: class name, LootExpirationTurnsRemaining values, psi loot hints."""
import sys, os, struct, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from savescan import load
d = r"C:\Users\Idi\Documents\My Games\XCOM2 War of the Chosen\XComGame\SaveData"
def rstr(blob, p):
    n = struct.unpack_from("<i", blob, p)[0]
    if n <= 0 or n > 200: return None, p
    return blob[p + 4:p + 4 + n - 1].decode("latin1"), p + 4 + n
for fn in sys.argv[1:]:
    blob, n = load(os.path.join(d, fn))
    print("==", fn, "| bytes", len(blob), "| LootDropSplitter class refs:", blob.count(b"XComGameState_LootDropSplitter"), "| LootDrop refs:", blob.count(b"XComGameState_LootDrop"))
    name = "LootExpirationTurnsRemaining"
    needle = struct.pack("<i", len(name) + 1) + name.encode() + b"\x00"
    p = 0; vals = []
    while True:
        p = blob.find(needle, p)
        if p < 0: break
        q = p + len(needle) + 4
        typ, q = rstr(blob, q)
        if typ == "IntProperty":
            q += 4 + 8
            v = struct.unpack_from("<i", blob, q)[0]
            # loot item names nearby (LootableItemRefs are refs; look for 'Psi'/'Focus' strings within 600 bytes before)
            seg = blob[max(0, p - 700):p + 200]
            strs = [s.decode("latin1") for s in re.findall(rb"[ -~]{5,}", seg)]
            vals.append((p, v, [s for s in strs if "roperty" not in s and s not in ("None",)][-8:]))
        p += len(needle)
    print("   timers:", [v for _, v, _ in vals])
    for p, v, strs in vals[:12]:
        print("   @%d remaining=%d ctx=%s" % (p, v, strs))
