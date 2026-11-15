# type: tool | created: 2026-11-15 | author: jep | project: DECADEnts
"""Film finish in code: one recipe per decade, applied to a finished picture. No model, no GPU.

Usage (second ComfyUI's Python: Pillow + numpy):
  python.exe -I film_finish.py <decade> <in.jpg> <out.jpg> [strength 0..1]     (default: Idi's strength for that decade)
  python.exe -I film_finish.py --batch <jobs.json>        jobs: [{"decade": "1940s", "src": "...", "dst": "..."}]
The output keeps the input's pixel size, so a finished picture can be cross-faded over its original.
Decades: 1920s 1930s 1940s 1950s 1960s 1970s 1980s 2000s 2010s. The grain is seeded from the file name: same in, same out.
"""
import io
import json
import os
import sys
import zlib

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

LUMA = np.array([0.2126, 0.7152, 0.0722], dtype=np.float32)


def to_f(im):
    return np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0


def to_im(a):
    return Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8), "RGB")


def luma(a):
    return a @ LUMA


def blur(a, r):
    return to_f(to_im(a).filter(ImageFilter.GaussianBlur(r))) if r > 0 else a


def soften(a, r, mix=1.0):
    return a * (1 - mix) + blur(a, r) * mix


def halation(a, thresh, radius, strength, tint=(1.0, 0.45, 0.25)):
    m = np.clip((luma(a) - thresh) / (1 - thresh), 0, 1)[..., None]
    glow = blur(a * m, radius) * np.array(tint, dtype=np.float32) * strength
    return 1 - (1 - a) * (1 - np.clip(glow, 0, 1))


def tone(a, lift=0.0, gain=1.0, gamma=1.0, s=0.0, white=1.0):
    a = np.clip(a * gain, 0, 1) ** gamma
    if s:
        a = a * (1 - s) + (a * a * (3 - 2 * a)) * s
    return lift + (white - lift) * a


def saturate(a, k):
    lum = luma(a)[..., None]
    return lum + (a - lum) * k


def split_tone(a, shadows=(0, 0, 0), highlights=(0, 0, 0)):
    lum = luma(a)[..., None]
    return a + (1 - lum) ** 2 * np.array(shadows, dtype=np.float32) + lum ** 2 * np.array(highlights, dtype=np.float32)


def channel_gain(a, gains):
    return a * np.array(gains, dtype=np.float32)


def mono(a, w=(0.30, 0.59, 0.11)):
    g = a @ np.array(w, dtype=np.float32)
    return np.repeat(g[..., None], 3, axis=2)


def _noise(rng, h, w, size, channels):
    hs, ws = max(2, int(h / size) + 1), max(2, int(w / size) + 1)
    out = np.empty((h, w, channels), dtype=np.float32)
    for c in range(channels):
        n = rng.normal(0, 1, (hs, ws)).astype(np.float32)
        up = np.asarray(Image.fromarray(n, "F").resize((w, h), Image.BICUBIC), dtype=np.float32)
        out[..., c] = up / (up.std() + 1e-6)
    return out


def grain(a, rng, amount, size=1.4, colour=0.0):
    h, w = a.shape[:2]
    lum = luma(a)[..., None]
    weight = 0.2 + 0.8 * 4 * lum * (1 - lum)
    n = _noise(rng, h, w, size, 1)
    if colour:
        n = n * (1 - colour) + _noise(rng, h, w, size * 1.6, 3) * colour
    return a + n * amount * weight


def vignette(a, strength, power=2.2, cx=0.5, cy=0.5):
    h, w = a.shape[:2]
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.sqrt(((x / w - cx) * 2) ** 2 + ((y / h - cy) * 2) ** 2) / 1.4142
    return a * (1 - strength * np.clip(r, 0, 1) ** power)[..., None]


def edge_soft(a, radius, power=2.5):
    """Lens softness that grows toward the corners."""
    h, w = a.shape[:2]
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.clip(np.sqrt(((x / w - 0.5) * 2) ** 2 + ((y / h - 0.5) * 2) ** 2) / 1.4142, 0, 1) ** power
    return a * (1 - r[..., None]) + blur(a, radius) * r[..., None]


def misregister(a, dx):
    out = a.copy()
    for c, shift in ((0, dx), (2, -dx)):
        ch = Image.fromarray(a[..., c], "F").transform((a.shape[1], a.shape[0]), Image.AFFINE,
                                                      (1, 0, shift, 0, 1, 0), Image.BICUBIC)
        out[..., c] = np.asarray(ch, dtype=np.float32)
    return out


def dust(a, rng, specks, hairs, scratches=0, strength=0.6):
    h, w = a.shape[:2]
    light = Image.new("L", (w, h), 0)
    dark = Image.new("L", (w, h), 0)
    dl, dd = ImageDraw.Draw(light), ImageDraw.Draw(dark)
    for _ in range(specks):
        x, y, r = rng.uniform(0, w), rng.uniform(0, h), rng.uniform(0.6, 2.2)
        (dl if rng.uniform() < 0.75 else dd).ellipse((x - r, y - r, x + r, y + r), fill=int(rng.uniform(120, 255)))
    for _ in range(hairs):
        x, y = rng.uniform(0, w), rng.uniform(0, h)
        pts = [(x, y)]
        ang = rng.uniform(0, 6.28)
        for _ in range(int(rng.uniform(6, 16))):
            ang += rng.normal(0, 0.35)
            x, y = x + np.cos(ang) * 5, y + np.sin(ang) * 5
            pts.append((x, y))
        (dl if rng.uniform() < 0.6 else dd).line(pts, fill=int(rng.uniform(90, 200)), width=1)
    for _ in range(scratches):
        x = rng.uniform(0.05, 0.95) * w
        dl.line([(x, 0), (x + rng.normal(0, 3), h)], fill=int(rng.uniform(40, 110)), width=1)
    lm = np.asarray(light.filter(ImageFilter.GaussianBlur(0.6)), dtype=np.float32)[..., None] / 255.0
    dm = np.asarray(dark.filter(ImageFilter.GaussianBlur(0.7)), dtype=np.float32)[..., None] / 255.0
    return a + lm * strength - dm * strength * 0.8


def light_leak(a, colour, strength, width=0.22, side="left"):
    h, w = a.shape[:2]
    x = np.linspace(0, 1, w, dtype=np.float32)[None, :, None]
    if side == "right":
        x = 1 - x
    m = np.clip(1 - x / width, 0, 1) ** 2 * strength
    return 1 - (1 - a) * (1 - m * np.array(colour, dtype=np.float32))


def uneven(a, rng, amount):
    """Slow exposure drift across the frame (hand-developed prints, old projectors)."""
    h, w = a.shape[:2]
    n = _noise(rng, h, w, max(h, w) / 3.0, 1)
    return a * (1 + n * amount)


def jpeg_trip(a, quality, scale=1.0):
    im = to_im(a)
    w, h = im.size
    if scale != 1.0:
        im = im.resize((max(8, int(w * scale)), max(8, int(h * scale))), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, subsampling=2)
    im = Image.open(io.BytesIO(buf.getvalue())).convert("RGB")
    if scale != 1.0:
        im = im.resize((w, h), Image.BICUBIC)
    return to_f(im)


def unsharp(a, radius, amount):
    return a + (a - blur(a, radius)) * amount


def fringe(a, strength):
    hot = (luma(a) > 0.86).astype(np.float32)[..., None]
    halo = np.clip(blur(np.repeat(hot, 3, axis=2), 3.0)[..., :1] - hot, 0, 1)
    return a + halo * np.array([0.35, -0.10, 0.60], dtype=np.float32) * strength


SEG = {"0": "abcdef", "1": "bc", "2": "abged", "3": "abgcd", "4": "fgbc", "5": "afgcd", "6": "afgedc", "7": "abc",
       "8": "abcdefg", "9": "abfgcd", " ": "", "'": "'"}


def datestamp(a, text, colour=(1.0, 0.42, 0.08), height=0.034, margin=0.045):
    """Orange seven-segment date in the lower right corner, as compact cameras of the 1980s burned in."""
    h, w = a.shape[:2]
    dh = max(10, int(h * height))
    dw, t, gap = int(dh * 0.52), max(2, int(dh * 0.13)), int(dh * 0.24)
    total = sum((dw + gap) if ch != "'" else (t + gap) for ch in text)
    x, y = int(w - w * margin - total), int(h - h * margin - dh)
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    for ch in text:
        if ch == "'":
            d.rectangle((x, y, x + t, y + int(dh * 0.25)), fill=255)
            x += t + gap
            continue
        m = dh // 2
        seg = {"a": (x + t, y, x + dw - t, y + t), "g": (x + t, y + m - t // 2, x + dw - t, y + m + t - t // 2),
               "d": (x + t, y + dh - t, x + dw - t, y + dh), "f": (x, y + t, x + t, y + m),
               "b": (x + dw - t, y + t, x + dw, y + m), "e": (x, y + m, x + t, y + dh - t),
               "c": (x + dw - t, y + m, x + dw, y + dh - t)}
        for s in SEG[ch]:
            d.rectangle(seg[s], fill=255)
        x += dw + gap
    core = np.asarray(mask.filter(ImageFilter.GaussianBlur(0.8)), dtype=np.float32)[..., None] / 255.0
    glow = np.asarray(mask.filter(ImageFilter.GaussianBlur(dh * 0.22)), dtype=np.float32)[..., None] / 255.0
    col = np.array(colour, dtype=np.float32)
    a = 1 - (1 - a) * (1 - glow * col * 0.55)
    return a * (1 - core * 0.9) + core * 0.9 * np.clip(col + 0.25, 0, 1)


# ---- recipes -------------------------------------------------------------------------------------------------------

def r1920s(a, rng):
    """Silent-film still: orthochromatic grey, glowing highlights, coarse grain, dark corners, dust and scratches."""
    a = mono(a, (0.12, 0.58, 0.30))
    a = edge_soft(soften(a, 0.8), 3.0)
    a = halation(a, 0.66, 12, 0.38, (1, 1, 1))
    a = tone(a, lift=0.035, gamma=1.04, s=0.3, white=0.94)
    a = uneven(a, rng, 0.05)
    a = vignette(a, 0.42, 2.0)
    a = grain(a, rng, 0.046, 1.6)
    a = dust(a, rng, 40, 3, 2, 0.42)
    return channel_gain(a, (1.0, 0.985, 0.95))


def r1930s(a, rng):
    """Large-format documentary print: full grey scale, sharp centre, fine grain, a few specks, silver-warm paper."""
    a = mono(a, (0.30, 0.59, 0.11))
    a = edge_soft(soften(a, 0.7), 2.5)
    a = tone(a, lift=0.03, gamma=0.97, s=0.45, white=0.955)
    a = vignette(a, 0.26, 2.4)
    a = grain(a, rng, 0.038, 1.2)
    a = dust(a, rng, 10, 1, 0, 0.32)
    return channel_gain(a, (1.0, 0.99, 0.955))


def r1940s(a, rng):
    """Kodachrome slide: dense blacks, heavy reds, cool shadows, soft lens, visible grain, slight colour misregister."""
    a = edge_soft(soften(a, 1.0), 3.5)
    a = misregister(a, 0.7)
    a = tone(a, lift=0.012, gamma=1.10, s=0.55, white=0.965)
    a = saturate(a, 1.12)
    a = channel_gain(a, (1.045, 0.985, 0.94))
    a = split_tone(a, shadows=(-0.012, 0.0, 0.03), highlights=(0.035, 0.012, -0.03))
    a = halation(a, 0.72, 9, 0.22, (1.0, 0.4, 0.2))
    a = vignette(a, 0.28, 2.4, 0.47, 0.54)
    a = grain(a, rng, 0.034, 1.3, 0.3)
    return dust(a, rng, 10, 1, 0, 0.35)


def r1950s(a, rng):
    """Kodachrome advertising page: creamy glow, pushed pastels, warm cast, fine grain."""
    a = soften(a, 0.7)
    a = halation(a, 0.72, 10, 0.18, (1.0, 0.95, 0.85))
    a = tone(a, lift=0.0, gamma=1.06, s=0.6, white=1.0)
    a = saturate(a, 1.22)
    a = channel_gain(a, (1.03, 1.0, 0.955))
    a = split_tone(a, shadows=(0.012, 0.0, -0.005), highlights=(0.02, 0.012, -0.025))
    a = vignette(a, 0.24, 2.4)
    return grain(a, rng, 0.026, 1.2, 0.25)


def r1960s(a, rng):
    """Faded Ektachrome snapshot: lifted blacks, magenta-red drift, soft lens, grain, an orange light leak."""
    a = edge_soft(soften(a, 1.0), 3.0)
    a = tone(a, lift=0.065, gamma=1.0, s=0.2, white=0.95)
    a = saturate(a, 0.9)
    a = channel_gain(a, (1.04, 0.955, 0.965))
    a = split_tone(a, shadows=(0.035, -0.005, 0.01), highlights=(0.02, 0.015, -0.03))
    a = light_leak(a, (1.0, 0.45, 0.12), 0.32, 0.2, "right")
    a = vignette(a, 0.28, 2.2)
    return grain(a, rng, 0.038, 1.6, 0.35)


def r1970s(a, rng):
    """Drugstore colour print: yellowed, low black density, green-cyan shadows, soft, grainy."""
    a = edge_soft(soften(a, 0.55), 2.0)
    a = tone(a, lift=0.05, gamma=1.0, s=0.2, white=0.96)
    a = saturate(a, 0.97)
    a = channel_gain(a, (1.02, 1.0, 0.93))
    a = split_tone(a, shadows=(-0.006, 0.014, 0.01), highlights=(0.02, 0.012, -0.02))
    a = vignette(a, 0.2, 2.2)
    return grain(a, rng, 0.032, 1.6, 0.4)


def r1980s(a, rng):
    """Compact-camera flash print: hot centre, fast falloff, saturated warm colour, reddish blacks, a burned-in date."""
    a = soften(a, 0.7)
    a = tone(a, lift=0.02, gain=1.06, gamma=1.05, s=0.5, white=0.985)
    a = saturate(a, 1.16)
    a = channel_gain(a, (1.025, 1.0, 0.965))
    a = split_tone(a, shadows=(0.025, 0.0, 0.0), highlights=(0.01, 0.006, -0.012))
    a = vignette(a, 0.3, 1.8, 0.5, 0.42)
    a = grain(a, rng, 0.03, 1.3, 0.4)
    return datestamp(a, "'87 3 14")


def r2000s(a, rng):
    """Early digital compact: clipped highlights, over-sharpened edges, purple fringe, blotchy colour noise, JPEG blocks."""
    a = tone(a, gain=1.1, gamma=1.03, s=0.3)
    a = channel_gain(a, (0.985, 1.01, 1.0))
    a = fringe(a, 0.5)
    a = grain(a, rng, 0.03, 2.6, 0.9)
    a = jpeg_trip(a, 62, 0.62)
    a = unsharp(a, 1.6, 0.9)
    a = vignette(a, 0.3, 1.8)
    return jpeg_trip(a, 34)


def r2010s(a, rng):
    """Phone photo through a 2015 filter: milky blacks, teal shadows, warm highlights, dark corners."""
    a = soften(a, 0.4)
    a = tone(a, lift=0.075, gamma=0.98, s=0.25, white=0.97)
    a = saturate(a, 0.93)
    a = split_tone(a, shadows=(-0.012, 0.02, 0.035), highlights=(0.035, 0.015, -0.03))
    a = vignette(a, 0.34, 2.0)
    a = grain(a, rng, 0.02, 1.2, 0.3)
    return jpeg_trip(a, 78)


PAPER_TINT = {"1920s": (0.97, 0.955, 0.92), "1930s": (0.975, 0.965, 0.93), "1940s": (0.975, 0.965, 0.935),
              "1950s": (0.98, 0.97, 0.94), "1960s": (0.975, 0.955, 0.925), "1970s": (0.97, 0.955, 0.9),
              "1980s": (0.985, 0.98, 0.96)}


def paper_mask(a0):
    """1 inside the photograph, 0 on a white print border, when the picture carries one; None when it has no border."""
    lum = luma(a0)
    sat = a0.max(axis=2) - a0.min(axis=2)
    h, w = lum.shape
    white = (lum > 0.8) & (sat < 0.12)
    k = max(3, int(min(h, w) * 0.012))
    if min(white[:k].mean(), white[-k:].mean(), white[:, :k].mean(), white[:, -k:].mean()) < 0.9:
        return None
    rows, cols = white.mean(axis=1), white.mean(axis=0)
    top = next(i for i in range(h) if rows[i] < 0.6)
    bottom = next(i for i in range(h - 1, -1, -1) if rows[i] < 0.6)
    left = next(i for i in range(w) if cols[i] < 0.6)
    right = next(i for i in range(w - 1, -1, -1) if cols[i] < 0.6)
    if bottom - top < h * 0.5 or right - left < w * 0.5:
        return None
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rectangle((left, top, right, bottom), fill=255)
    return np.asarray(m.filter(ImageFilter.GaussianBlur(1.5)), dtype=np.float32)[..., None] / 255.0


RECIPES = {"1920s": r1920s, "1930s": r1930s, "1940s": r1940s, "1950s": r1950s, "1960s": r1960s, "1970s": r1970s,
           "1980s": r1980s, "2000s": r2000s, "2010s": r2010s}


# Idi's slider positions on the T8 sheet, 2026-11-15: how much of each recipe he wants. 1970s and 2000s: he judged the
# finish worse, so those decades stay unfinished (2000s was his slider at 0; 1970s is jep's reading of "worse").
STRENGTH = {"1920s": 0.5, "1930s": 1.0, "1940s": 0.75, "1950s": 0.5, "1960s": 0.5, "1970s": 0.0, "1980s": 0.75,
            "2000s": 0.0, "2010s": 1.0}


def finish(decade, src, dst, strength=None):
    if strength is None:
        strength = STRENGTH[decade]
    a0 = to_f(Image.open(src))
    if strength <= 0:
        to_im(a0).save(dst, "JPEG", quality=93)
        return a0.shape[1], a0.shape[0]
    rng = np.random.default_rng(zlib.crc32(os.path.basename(src).encode()) + int(decade[:4]))
    a = np.clip(RECIPES[decade](a0.copy(), rng), 0, 1)
    m = paper_mask(a0)
    if m is not None and decade in PAPER_TINT:      # the border is paper: tint it, keep it free of film grain and blur
        paper = a0 * np.array(PAPER_TINT[decade], dtype=np.float32) + rng.normal(0, 0.006, a0.shape[:2] + (1,)).astype(np.float32)
        a = np.clip(paper * (1 - m) + a * m, 0, 1)
    if strength < 1.0:
        a = a0 * (1 - strength) + a * strength
    to_im(a).save(dst, "JPEG", quality=93)
    return a.shape[1], a.shape[0]


if __name__ == "__main__":
    if sys.argv[1] == "--batch":
        with open(sys.argv[2], "r", encoding="utf-8") as fh:
            jobs = json.load(fh)
        for j in jobs:
            w, h = finish(j["decade"], j["src"], j["dst"], float(j["strength"]) if "strength" in j else None)
            print("%s %dx%d -> %s" % (j["decade"], w, h, os.path.basename(j["dst"])))
    else:
        s = float(sys.argv[4]) if len(sys.argv) > 4 else None
        print(finish(sys.argv[1], sys.argv[2], sys.argv[3], s))
