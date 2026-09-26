r"""Studio v4 (folder kidstudio): a word-gated page in front of ComfyUI (pictures, songs) and Kokoro (speech).

Run:  venv\Scripts\python server.py   (or double-click start.bat)
Page: http://127.0.0.1:8787   (kid page, loopback only)
Keep: http://<LAN-IP>:8788    (download helper for the girls' phones, serves out/ only)
"""
import json, os, random, re, socket, threading, time, urllib.request, urllib.parse, datetime, io
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial

import gate

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LOG = os.path.join(HERE, "log")
ALLOW_PATH = os.path.join(HERE, "allow.txt")
PIN_PATH = os.path.join(HERE, "pin.txt")
COMFY = "http://127.0.0.1:8188"
KID_PORT = int(os.environ.get("KID_PORT", 8787))
KEEP_PORT = int(os.environ.get("KEEP_PORT", 8788))
GIRLS = ("K", "D")
LOCK = threading.Lock()

# ---------- choices (labels are what the girls read on screen) ----------
STYLES = {
    "cartoon":    "children's book illustration of {p}, colorful, cute, soft shapes",
    "anime":      "anime style illustration of {p}, colorful, cute, clean lines",
    "clay":       "claymation style, a clay model of {p}, colorful, cute, studio light",
    "pixel":      "pixel art of {p}, colorful, cute, 16-bit",
    "3d":         "3d animated movie style render of {p}, colorful, cute, soft lighting",
    "watercolor": "watercolor painting of {p}, soft colors, cute, paper texture",
    "crayon":     "a child's crayon drawing of {p}, colorful, naive, on white paper",
    "sticker":    "a die-cut sticker of {p}, bold outline, glossy, white background, cute",
    "comic":      "comic book style of {p}, bold ink, halftone dots, colorful, dynamic",
    "lego":       "{p} built from colorful toy bricks, brick toy style, studio light",
    "neon":       "neon glowing outline art of {p}, dark background, vivid colors",
    "plush":      "a soft plush toy of {p}, fluffy fabric, cute, studio light",
}
SHAPES = {"square": (1024, 1024), "wide": (1280, 768), "tall": (768, 1280)}

# Ingredient slots for PICTURE. Each slot is what she MUST decide; its signposts are what she CAN decide.
# A signpost is a dimension word plus a question the page speaks when tapped. Signposts never insert text:
# she has to describe her own choice in her own words. Edit freely; the page reads this at load.
PICTURE_SLOTS = [
    {"key": "subject", "label": "WHO OR WHAT", "hint": "the hero", "signs": [
        ("WHO", "who is in the picture?"), ("HOW MANY", "one, two, or many?"), ("SIZE", "how big is it?"),
        ("COLOR", "what color is it?"), ("DOING", "what is it doing?"), ("FEELING", "how does it feel?")]},
    {"key": "scene", "label": "WHERE", "hint": "the place", "signs": [
        ("PLACE", "where are we?"), ("TIME", "what time of day is it?"), ("WEATHER", "what is the weather?"),
        ("INSIDE OR OUTSIDE", "are we inside or outside?"), ("FAR AWAY", "what is far away, behind everything?"),
        ("SEASON", "which season is it?")]},
    {"key": "details", "label": "LOOK CLOSER", "hint": "small things", "signs": [
        ("CLOTHES", "what is it wearing?"), ("HOLDING", "what is it holding?"), ("TOUCH", "how does it feel to touch?"),
        ("LIGHT", "where does the light come from?"), ("HIDING", "what tiny thing is hiding?"), ("SURPRISE", "what is the one surprise?")]},
    {"key": "rules", "label": "YOUR RULES", "hint": "the camera and the law", "signs": [
        ("ANGLE", "from where do we look?"), ("CLOSE OR FAR", "are we close or far?"), ("MIDDLE", "what is in the middle?"),
        ("EDGE", "what touches the edge?"), ("ONLY", "only what? only one color? only one thing?"),
        ("NO", "what is not allowed in the picture?"), ("SAME", "what stays the same as last time?")]},
]
SPEAK_SLOTS = [
    {"key": "who", "label": "WHO", "hint": "the speaker or the hero", "signs": [
        ("NAME", "who is talking?"), ("HOW MANY", "one or many?"), ("AGE", "how old?"), ("FEELING", "how do they feel?")]},
    {"key": "does", "label": "DOES WHAT", "hint": "the action", "signs": [
        ("ACTION", "what happens?"), ("WHEN", "now, before, or later?"), ("HOW", "how is it done?"), ("WITH WHAT", "with what?")]},
    {"key": "where", "label": "WHERE", "hint": "the place", "signs": [
        ("PLACE", "where are they?"), ("TIME", "what time is it?"), ("WITH WHOM", "who is with them?")]},
    {"key": "then", "label": "AND THEN", "hint": "the next sentence", "signs": [
        ("NEXT", "what happens next?"), ("WHY", "why?"), ("QUESTION", "what do they ask?"), ("SHOUT", "what do they shout?")]},
]
SONG_SLOTS = [
    {"key": "who", "label": "WHO", "hint": "who the song is about", "signs": [
        ("NAME", "who is it about?"), ("YOU OR ME", "is it about you, or someone else?"), ("FEELING", "how do they feel?")]},
    {"key": "what", "label": "WHAT HAPPENS", "hint": "the story line", "signs": [
        ("ACTION", "what do they do?"), ("WHERE", "where does it happen?"), ("WHEN", "when?")]},
    {"key": "hook", "label": "THE HOOK", "hint": "the line that comes back", "signs": [
        ("REPEAT", "which words come back every time?"), ("SHOUT", "which word gets shouted?"), ("RHYME", "which two words sound the same at the end?")]},
    {"key": "end", "label": "THE END", "hint": "the last line", "signs": [
        ("CHANGE", "what is different at the end?"), ("WISH", "what do they want at the end?"), ("BYE", "how does the song say bye?")]},
]
STORY_SLOTS = PICTURE_SLOTS + [
    {"key": "say", "label": "SAY IT", "hint": "one sentence for this frame", "wide": True, "signs": [
        ("WHAT NEXT", "what happens next?"), ("FEELING", "how does the hero feel now?"), ("WHY", "why did it happen?"), ("SOUND", "what do we hear?")]},
]
SLOTS = {"picture": PICTURE_SLOTS, "speak": SPEAK_SLOTS, "song": SONG_SLOTS, "story": STORY_SLOTS}
SLOT_ORDER = {"picture": ["subject", "details", "scene", "rules"], "story": ["subject", "details", "scene", "rules"],
              "speak": ["who", "does", "where", "then"], "song": ["who", "what", "hook", "end"]}
# The story arc: one question per frame, asked by the page. Four frames, fixed.
ARC = [("BEGINNING", "who is it? where are they?"), ("PROBLEM", "what goes wrong?"),
       ("TRY", "what do they do about it?"), ("END", "how does it end?")]


def _sentence(x):
    x = x.strip()
    if not x:
        return ""
    x = x[0].upper() + x[1:]
    return x if x[-1] in ".!?" else x + "."


def compose(kind, slots):
    """Turn the filled slots into the text a generator gets. Returns '' when nothing is filled."""
    g = lambda k: str(slots.get(k, "")).strip()
    if kind in ("picture", "story"):
        return ", ".join(p for p in (g(k) for k in SLOT_ORDER["picture"]) if p)
    if kind == "speak":
        first = " ".join(x for x in (g("who"), g("does"), g("where")) if x)
        return " ".join(_sentence(x) for x in (first, g("then")) if x)
    if kind == "song":
        who, what, hook, end = g("who"), g("what"), g("hook"), g("end")
        parts = [x for x in (who, what) if x]
        if hook:
            parts += ["[chorus]", hook, hook]
        if end:
            parts += ["[verse]", end]
        if hook and (who or what or end):
            parts += ["[chorus]", hook]
        return "\n".join(parts)
    return ""


def clean_slots(kind, o):
    sl = o.get("slots")
    if not isinstance(sl, dict):
        return None
    keys = SLOT_ORDER.get(kind, []) + (["say"] if kind == "story" else [])
    out = {k: str(v).strip() for k, v in sl.items() if k in keys and str(v).strip()}
    return out or None

GENRES = {
    "pop":      "upbeat pop, catchy, bright, happy",
    "dance":    "dance pop, electronic, energetic, synths",
    "rock":     "pop rock, electric guitar, drums, energetic",
    "lullaby":  "soft lullaby, gentle piano, calm, sweet",
    "hiphop":   "hip hop, rap, beat, groovy, fun",
    "kpop":     "k-pop, bright synths, catchy hook, energetic",
    "musical":  "broadway musical, orchestral, dramatic, theatrical",
    "chiptune": "8-bit chiptune, video game music, bleeps, fast",
    "jazz":     "jazz, swing, piano, upright bass, playful",
    "reggae":   "reggae, laid back, offbeat guitar, sunny",
    "country":  "country, acoustic guitar, warm, cheerful",
    "epic":     "epic cinematic, orchestra, drums, heroic",
}
SINGERS = {"girl": "female vocals", "boy": "male vocals", "kids": "children's choir vocals", "robot": "vocoder robot vocals"}
MOODS = {"happy": "happy", "silly": "silly, funny", "dreamy": "dreamy, soft", "epic": "epic, powerful", "sad": "sad, emotional"}
TEMPOS = {"slow": 80, "normal": 115, "fast": 140, "crazy": 170}

VOICES = {  # label -> (kokoro voice id, lang_code)
    "heart": ("af_heart", "a"), "bella": ("af_bella", "a"), "nicole": ("af_nicole", "a"), "sky": ("af_sky", "a"),
    "sarah": ("af_sarah", "a"), "nova": ("af_nova", "a"),
    "adam": ("am_adam", "a"), "michael": ("am_michael", "a"), "puck": ("am_puck", "a"), "santa": ("am_santa", "a"),
    "emma": ("bf_emma", "b"), "alice": ("bf_alice", "b"), "lily": ("bf_lily", "b"),
    "george": ("bm_george", "b"), "daniel": ("bm_daniel", "b"), "fable": ("bm_fable", "b"),
    # v1 labels kept working
    "girl": ("af_heart", "a"), "boy": ("am_michael", "a"), "british": ("bf_emma", "b"), "slow": ("af_heart", "a"),
}

for g in GIRLS:
    os.makedirs(os.path.join(OUT, g), exist_ok=True)
os.makedirs(LOG, exist_ok=True)
if not os.path.exists(PIN_PATH):
    open(PIN_PATH, "w").write("2468\n")


def lan_ip():
    """Home-network address: prefer 192.168.x / 10.x, skip VPN (100.64-127.x) and loopback."""
    cands = []
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            cands.append(info[4][0])
    except Exception:
        pass
    def ok(ip):
        a = [int(x) for x in ip.split(".")]
        if a[0] == 127 or (a[0] == 100 and 64 <= a[1] <= 127) or (a[0] == 169 and a[1] == 254):
            return False
        return a[0] == 192 and a[1] == 168 or a[0] == 10 or (a[0] == 172 and 16 <= a[1] <= 31)
    good = [ip for ip in cands if ok(ip)]
    return good[0] if good else (cands[0] if cands else "127.0.0.1")


def clamp(v, lo, hi, default):
    try:
        v = float(v)
    except (TypeError, ValueError):
        return default
    return max(lo, min(hi, v))


# ---------- word logs (the counter feed) ----------
def girl_words(g):
    p = os.path.join(LOG, f"{g}.txt")
    words = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            parts = line.strip().split("\t")
            if len(parts) == 2 and parts[1] not in words:
                words.append(parts[1])
    return words


def log_words(g, toks):
    known = set(girl_words(g))
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    new = []
    with open(os.path.join(LOG, f"{g}.txt"), "a", encoding="utf-8") as f:
        for t in toks:
            if t.isdigit() or t in known or t in new:
                continue
            f.write(f"{stamp}\t{t}\n")
            new.append(t)
    return new


def build_log(msg):
    with open(os.path.join(LOG, "build.txt"), "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}\t{msg}\n")


def save_meta(girl, name, meta):
    meta["name"] = name
    meta["time"] = datetime.datetime.now().strftime("%H:%M")
    with open(os.path.join(OUT, girl, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(meta, f)


def gallery(girl):
    items = []
    d = os.path.join(OUT, girl)
    for name in sorted(os.listdir(d)):
        if name.endswith(".json"):
            continue
        ext = name.rsplit(".", 1)[-1].lower()
        kind = "picture" if ext in ("png", "jpg", "webp") else ("speak" if ext == "wav" else ("movie" if ext == "mp4" else "song"))
        meta = {"kind": kind, "text": "", "style": "", "secs": 0, "time": ""}
        try:
            meta.update(json.load(open(os.path.join(d, name + ".json"), encoding="utf-8")))
        except Exception:
            pass
        meta["url"] = f"/out/{girl}/{name}"
        meta["name"] = name
        items.append(meta)
    return items[::-1]


# ---------- ComfyUI ----------
def comfy_run(workflow, timeout=240):
    body = json.dumps({"prompt": workflow, "client_id": "kidstudio"}).encode()
    req = urllib.request.Request(COMFY + "/prompt", data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        pid = json.load(r)["prompt_id"]
    t0 = time.time()
    while time.time() - t0 < timeout:
        time.sleep(0.3)
        with urllib.request.urlopen(f"{COMFY}/history/{pid}", timeout=10) as r:
            hist = json.load(r)
        if pid in hist:
            st = hist[pid].get("status", {})
            if st.get("status_str") == "error":
                raise RuntimeError("ComfyUI error: " + json.dumps(st.get("messages", []))[:300])
            files = []
            for node in hist[pid].get("outputs", {}).values():
                for key in ("images", "audio", "gifs"):
                    files.extend(node.get(key, []))
            if files:
                return files, time.time() - t0
    raise TimeoutError("ComfyUI took too long")


def comfy_fetch(item):
    q = urllib.parse.urlencode({"filename": item["filename"], "subfolder": item.get("subfolder", ""), "type": item.get("type", "output")})
    with urllib.request.urlopen(f"{COMFY}/view?{q}", timeout=30) as r:
        return r.read()


def load_wf(name):
    with open(os.path.join(HERE, "workflows", name), encoding="utf-8") as f:
        return json.load(f)


def find(wf, class_type):
    for k, v in wf.items():
        if v.get("class_type") == class_type:
            return k
    raise KeyError(class_type)


def stamp():
    return datetime.datetime.now().strftime("%H%M%S")


def make_picture(girl, text, o):
    style = o.get("style", "cartoon")
    shape = o.get("shape", "square")
    count = int(clamp(o.get("count", 1), 1, 4, 1))
    seed = int(o["seed"]) if str(o.get("seed", "")).isdigit() else random.randint(1, 2**48)
    wf = load_wf("picture.json")
    sampler = find(wf, "KSampler")
    pos = wf[sampler]["inputs"]["positive"][0]
    wf[pos]["inputs"]["text"] = STYLES.get(style, STYLES["cartoon"]).format(p=text)
    wf[sampler]["inputs"]["seed"] = seed
    lat = find(wf, "EmptySD3LatentImage")
    w, h = SHAPES.get(shape, SHAPES["square"])
    wf[lat]["inputs"].update({"width": w, "height": h, "batch_size": count})
    files, secs = comfy_run(wf)
    slots = clean_slots("picture", o)
    names = []
    for i, it in enumerate(files[:count]):
        name = f"{stamp()}-{gate.tokens(text)[0]}-{i+1}.png"
        open(os.path.join(OUT, girl, name), "wb").write(comfy_fetch(it))
        meta = {"kind": "picture", "text": text, "style": style, "shape": shape, "seed": seed, "secs": round(secs, 1)}
        if slots:
            meta["slots"] = slots
        save_meta(girl, name, meta)
        names.append(name)
    build_log(f"picture {girl} {secs:.1f}s '{text}' {style} {shape} x{count} seed={seed} -> {names}")
    return names, secs, {"seed": seed}


def make_song(girl, lyrics, o):
    genre = o.get("genre", o.get("style", "pop"))
    singer = o.get("singer", "girl")
    mood = o.get("mood", "happy")
    tempo = o.get("tempo", "normal")
    seconds = int(clamp(o.get("seconds", 30), 10, 90, 30))
    seed = int(o["seed"]) if str(o.get("seed", "")).isdigit() else random.randint(1, 2**31)
    tags = ", ".join([GENRES.get(genre, GENRES["pop"]), SINGERS.get(singer, SINGERS["girl"]), MOODS.get(mood, "happy")])
    bpm = TEMPOS.get(tempo, 115)
    wf = load_wf("song.json")
    enc = find(wf, "TextEncodeAceStepAudio1.5")
    lat = find(wf, "EmptyAceStep1.5LatentAudio")
    sampler = find(wf, "KSampler")
    body = lyrics.strip()
    if not body.lower().startswith("["):
        body = "[verse]\n" + body
    wf[enc]["inputs"].update({"tags": tags, "lyrics": body, "seed": seed, "bpm": bpm, "duration": seconds, "language": "en"})
    wf[lat]["inputs"]["seconds"] = seconds
    wf[sampler]["inputs"]["seed"] = seed
    files, secs = comfy_run(wf)
    data = comfy_fetch(files[0])
    ext = os.path.splitext(files[0]["filename"])[1] or ".mp3"
    name = f"{stamp()}-{gate.tokens(lyrics)[0]}-song{ext}"
    open(os.path.join(OUT, girl, name), "wb").write(data)
    meta = {"kind": "song", "text": lyrics, "style": genre, "singer": singer, "mood": mood, "tempo": tempo, "seconds": seconds, "seed": seed, "secs": round(secs, 1)}
    if clean_slots("song", o):
        meta["slots"] = clean_slots("song", o)
    save_meta(girl, name, meta)
    build_log(f"song {girl} {secs:.1f}s {genre}/{singer}/{mood}/{tempo} {seconds}s seed={seed} -> {name}")
    return [name], secs, {"seed": seed}


# ---------- Kokoro ----------
_pipes = {}
def make_speech(girl, text, o):
    import soundfile as sf, numpy as np
    from kokoro import KPipeline
    label = o.get("voice", "heart")
    vid, lang = VOICES.get(label, VOICES["heart"])
    speed = clamp(o.get("speed", 0.75 if label == "slow" else 1.0), 0.5, 1.6, 1.0)
    if lang not in _pipes:
        _pipes[lang] = KPipeline(lang_code=lang)
    t0 = time.time()
    chunks = [audio for _, _, audio in _pipes[lang](text, voice=vid, speed=speed)]
    audio = np.concatenate(chunks) if chunks else np.zeros(2400)
    name = f"{stamp()}-{gate.tokens(text)[0]}.wav"
    sf.write(os.path.join(OUT, girl, name), audio, 24000)
    secs = time.time() - t0
    meta = {"kind": "speak", "text": text, "style": label, "speed": speed, "secs": round(secs, 1)}
    if clean_slots("speak", o):
        meta["slots"] = clean_slots("speak", o)
    save_meta(girl, name, meta)
    build_log(f"speak {girl} {secs:.1f}s {label} x{speed} '{text[:40]}' -> {name}")
    return [name], secs, {}


# ---------- say (TTS without counting), warm-up, dictation ----------
TTS_CACHE = os.path.join(OUT, "_tts")
os.makedirs(TTS_CACHE, exist_ok=True)
DICT = {}  # id -> {"who", "text"}
FRAMES = [
    "The {c} {a} is {v}.", "I love my {c} {a}.", "A {a} in the {p}.", "My {a} can {v0}.", "The {a} is {f}.",
    "I see a {c} {a}.", "The {a} likes {fd}.", "Two {c} {a}s.", "Look at the {a}.", "The {a} is in the {p}.",
]
POOL = {
    "c": ["red", "pink", "blue", "green", "yellow", "purple", "orange", "black", "white", "gold"],
    "a": ["cat", "dog", "pig", "fish", "horse", "dragon", "bird", "frog", "bear", "rabbit", "unicorn", "monkey"],
    "v": ["dancing", "singing", "swimming", "flying", "running", "jumping", "sleeping", "eating"],
    "v0": ["dance", "sing", "swim", "fly", "run", "jump", "sleep", "eat"],
    "p": ["school", "garden", "park", "sea", "sky", "forest", "kitchen", "castle"],
    "f": ["happy", "sad", "funny", "big", "small", "fast", "slow", "cute"],
    "fd": ["pizza", "cake", "candy", "apple", "ice cream", "chocolate", "milk", "cookies"],
}


def say(text, voice="heart", speed=1.0):
    """TTS to a cached wav; never touches the counters."""
    import hashlib
    key = hashlib.md5(f"{voice}|{speed}|{text}".encode()).hexdigest()[:16] + ".wav"
    path = os.path.join(TTS_CACHE, key)
    if not os.path.exists(path):
        import soundfile as sf, numpy as np
        from kokoro import KPipeline
        vid, lang = VOICES.get(voice, VOICES["heart"])
        if lang not in _pipes:
            _pipes[lang] = KPipeline(lang_code=lang)
        chunks = [a for _, _, a in _pipes[lang](text, voice=vid, speed=speed)]
        sf.write(path, np.concatenate(chunks) if chunks else np.zeros(2400), 24000)
    return f"/out/_tts/{key}"


def warmup(girl, n=3):
    words = [w for w in girl_words(girl) if len(w) > 2]
    random.shuffle(words)
    return words[:n]


def her_sentences(girl):
    out = []
    d = os.path.join(OUT, girl)
    for name in os.listdir(d):
        if name.endswith(".json"):
            try:
                t = json.load(open(os.path.join(d, name), encoding="utf-8")).get("text", "")
            except Exception:
                continue
            line = t.strip().split("\n")[0].strip()
            n = len(gate.tokens(line))
            if 2 <= n <= 8:
                out.append(line)
    return list(dict.fromkeys(out))


def dictation_target(girl):
    own = her_sentences(girl)
    if own and random.random() < 0.5:
        return random.choice(own)
    mine = [w for w in girl_words(girl)]
    fr = random.choice(FRAMES)
    vals = {}
    for k, opts in POOL.items():
        pref = [o for o in opts if o in mine]
        vals[k] = random.choice(pref) if pref and random.random() < 0.7 else random.choice(opts)
    return fr.format(**vals)


def diff_letters(target, typed):
    """Word-by-word letter diff. Returns list of words: [{t: target_word, letters: [[char, ok]]}], correct count."""
    import difflib
    tw, yw = gate.tokens(target), gate.tokens(typed)
    sm = difflib.SequenceMatcher(a=tw, b=yw)
    pairs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            pairs += [(tw[i], tw[i]) for i in range(i1, i2)]
        elif tag == "replace":
            for k in range(max(i2 - i1, j2 - j1)):
                pairs.append((tw[i1 + k] if i1 + k < i2 else None, yw[j1 + k] if j1 + k < j2 else None))
        elif tag == "delete":
            pairs += [(tw[i], None) for i in range(i1, i2)]
        else:
            pairs += [(None, yw[j]) for j in range(j1, j2)]
    words, correct, target_words = [], [], 0
    for t, y in pairs:
        if t is None:
            words.append({"t": "", "y": y, "letters": [[ch, False] for ch in y], "extra": True})
            continue
        target_words += 1
        if y is None:
            words.append({"t": t, "y": "", "letters": [[ch, False] for ch in t]})
            continue
        cm = difflib.SequenceMatcher(a=t, b=y)
        letters = []
        for tag, i1, i2, j1, j2 in cm.get_opcodes():
            if tag == "equal":
                letters += [[ch, True] for ch in t[i1:i2]]
            else:
                letters += [[ch, False] for ch in t[i1:i2]] or [["·", False]]
        ok = t == y
        if ok:
            correct.append(t)
        words.append({"t": t, "y": y, "letters": letters, "ok": ok})
    return words, correct, target_words


# ---------- story (4 frames, one movie) ----------
def story_path(girl):
    return os.path.join(OUT, girl, "story.json")


def load_story(girl):
    try:
        return json.load(open(story_path(girl), encoding="utf-8"))
    except Exception:
        return {"frames": [None] * len(ARC), "started": datetime.datetime.now().strftime("%H:%M")}


def save_story(girl, st):
    json.dump(st, open(story_path(girl), "w", encoding="utf-8"))


def story_frame(girl, n, o):
    """Make frame n (1-based): one picture from the slots + one spoken line. Returns (frame, secs, new_words)."""
    slots = clean_slots("story", o) or {}
    text = compose("story", slots)
    line = slots.get("say", "")
    if not text:
        raise ValueError("type who or what")
    if not line:
        raise ValueError("type what to say")
    o = dict(o, count=1, slots=slots)
    names, secs, extra = make_picture(girl, text, o)
    say_names, secs2, _ = make_speech(girl, line, {"voice": o.get("voice", "heart"), "speed": o.get("speed", 0.95), "slots": None})
    st = load_story(girl)
    fr = {"n": n, "arc": ARC[n - 1][0], "slots": slots, "text": text, "line": line, "pic": names[0], "say": say_names[0],
          "seed": extra.get("seed"), "style": o.get("style", "cartoon"), "shape": o.get("shape", "wide"),
          "time": datetime.datetime.now().strftime("%H:%M")}
    st["frames"][n - 1] = fr
    save_story(girl, st)
    build_log(f"story {girl} frame {n} {secs + secs2:.1f}s '{text}' / '{line}'")
    return fr, secs + secs2, st


def latest_song(girl):
    d = os.path.join(OUT, girl)
    songs = [os.path.join(d, f) for f in os.listdir(d) if f.rsplit(".", 1)[-1].lower() in ("mp3", "flac", "ogg", "m4a")]
    return max(songs, key=os.path.getmtime) if songs else None


def story_movie(girl):
    import movie
    st = load_story(girl)
    frames = [f for f in st["frames"] if f]
    if len(frames) < 2:
        raise ValueError("make two frames first")
    d = os.path.join(OUT, girl)
    pairs = [(os.path.join(d, f["pic"]), os.path.join(d, f["say"]) if f.get("say") and os.path.exists(os.path.join(d, f["say"])) else None) for f in frames]
    name = f"{stamp()}-story.mp4"
    t0 = time.time()
    total = movie.movie(pairs, latest_song(girl), os.path.join(d, name))
    secs = time.time() - t0
    lines = " / ".join(f["line"] for f in frames)
    save_meta(girl, name, {"kind": "movie", "text": lines, "style": f"{len(frames)} frames", "seconds": round(total, 1), "secs": round(secs, 1)})
    st["movie"] = name
    save_story(girl, st)
    build_log(f"movie {girl} {secs:.1f}s {len(frames)} frames {total:.1f}s -> {name}")
    return name, secs


def story_new(girl):
    p = story_path(girl)
    if os.path.exists(p):
        os.replace(p, os.path.join(OUT, girl, f"story-{stamp()}.json"))
    return load_story(girl)


# ---------- HTTP ----------
class Kid(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_json(self, obj, code=200):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def send_file(self, path, ctype):
        try:
            b = open(path, "rb").read()
        except FileNotFoundError:
            self.send_error(404); return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        p = urllib.parse.urlparse(self.path).path
        if p == "/":
            return self.send_file(os.path.join(HERE, "index.html"), "text/html; charset=utf-8")
        if p == "/api/choices":
            return self.send_json({"styles": list(STYLES), "shapes": list(SHAPES), "genres": list(GENRES), "singers": list(SINGERS),
                                   "moods": list(MOODS), "tempos": list(TEMPOS), "slots": SLOTS, "arc": ARC,
                                   "voices": [v for v in VOICES if v not in ("girl", "boy", "british", "slow")]})
        if p.startswith("/api/story/"):
            g = p.rsplit("/", 1)[-1]
            return self.send_json({"ok": g in GIRLS, "story": load_story(g) if g in GIRLS else None})
        if p.startswith("/api/warmup/"):
            g = p.rsplit("/", 1)[-1]
            return self.send_json({"words": warmup(g) if g in GIRLS else []})
        if p.startswith("/out/"):
            girl, _, name = p[5:].partition("/")
            if girl in GIRLS + ("_tts",) and name and "/" not in name and ".." not in name:
                ext = name.rsplit(".", 1)[-1]
                ctype = {"png": "image/png", "wav": "audio/wav", "mp3": "audio/mpeg", "flac": "audio/flac", "mp4": "video/mp4"}.get(ext, "application/octet-stream")
                return self.send_file(os.path.join(OUT, girl, name), ctype)
            return self.send_error(404)
        if p.startswith("/api/list/"):
            g = p.rsplit("/", 1)[-1]
            return self.send_json({"words": girl_words(g) if g in GIRLS else []})
        if p.startswith("/api/gallery/"):
            g = p.rsplit("/", 1)[-1]
            return self.send_json({"items": gallery(g) if g in GIRLS else []})
        if p.startswith("/api/keep/"):
            g = p.rsplit("/", 1)[-1]
            url = f"http://{lan_ip()}:{KEEP_PORT}/{g}/"
            try:
                import segno
                buf = io.BytesIO()
                segno.make(url).save(buf, kind="svg", scale=8, border=2)
                svg = buf.getvalue().decode()
            except Exception as e:
                svg = f"<p>{e}</p>"
            return self.send_json({"url": url, "svg": svg})
        self.send_error(404)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return self.send_json({"ok": False, "error": "bad json"}, 400)
        p = self.path
        if p == "/api/add":
            pin = open(PIN_PATH).read().strip()
            if str(data.get("pin", "")).strip() != pin:
                return self.send_json({"ok": False, "error": "wrong pin"})
            words = gate.tokens(data.get("word", ""))
            with LOCK:
                allow = gate.load_allow(ALLOW_PATH)
                with open(ALLOW_PATH, "a", encoding="utf-8") as f:
                    for w in words:
                        if w not in allow:
                            f.write(w + "\n")
            build_log(f"allow += {words}")
            return self.send_json({"ok": True, "added": words})
        if p == "/api/say":
            text = (data.get("text") or "").strip()[:200]
            if not text:
                return self.send_json({"ok": False})
            try:
                with LOCK:
                    url = say(text, data.get("voice", "heart"), clamp(data.get("speed", 1.0), 0.5, 1.6, 1.0))
            except Exception as e:
                return self.send_json({"ok": False, "error": str(e)[:200]})
            return self.send_json({"ok": True, "url": url})
        if p == "/api/dictate/new":
            girl = data.get("who")
            if girl not in GIRLS:
                return self.send_json({"ok": False, "error": "pick a color first"})
            text = dictation_target(girl)
            try:
                with LOCK:
                    url = say(text, data.get("voice", "heart"), clamp(data.get("speed", 0.9), 0.5, 1.6, 0.9))
            except Exception as e:
                return self.send_json({"ok": False, "error": str(e)[:200]})
            did = f"{girl}{int(time.time()*1000)}"
            DICT[did] = {"who": girl, "text": text}
            build_log(f"dictate {girl} new '{text}'")
            return self.send_json({"ok": True, "id": did, "url": url, "nwords": len(gate.tokens(text))})
        if p == "/api/dictate/check":
            d = DICT.get(data.get("id", ""))
            if not d:
                return self.send_json({"ok": False, "error": "press the ear first"})
            typed = (data.get("typed") or "").strip()
            words, correct, total = diff_letters(d["text"], typed)
            new = log_words(d["who"], correct)
            build_log(f"dictate {d['who']} check '{typed}' -> {len(correct)}/{total}")
            return self.send_json({"ok": True, "target": d["text"], "words": words, "correct": len(correct), "total": total,
                                   "new": new, "mywords": girl_words(d["who"])})
        if p == "/api/gen":
            girl = data.get("who")
            if girl not in GIRLS:
                return self.send_json({"ok": False, "error": "pick a color first"})
            text = (data.get("text") or "").strip()
            kind = data.get("kind", "picture")
            if kind in SLOTS and isinstance(data.get("slots"), dict):
                text = compose(kind, data["slots"]) or text
            allow = gate.load_allow(ALLOW_PATH)
            r = gate.check(re.sub(r"\[[^\]]*\]", " ", text) if kind == "song" else text, allow)  # song section tags are not her words
            if not r["ok"]:
                return self.send_json({"ok": False, "bad": r["bad"]})
            try:
                with LOCK:
                    fn = {"picture": make_picture, "speak": make_speech, "song": make_song}.get(kind)
                    if not fn:
                        return self.send_json({"ok": False, "error": "unknown kind"})
                    names, secs, extra = fn(girl, text, data)
            except Exception as e:
                build_log(f"FAIL {kind} {girl} '{text[:40]}': {e}")
                return self.send_json({"ok": False, "error": str(e)[:200]})
            new = log_words(girl, r["tokens"])
            return self.send_json({"ok": True, "urls": [f"/out/{girl}/{n}" for n in names], "url": f"/out/{girl}/{names[0]}", "text": text,
                                   "kind": kind, "secs": round(secs, 1), "new": new, "words": girl_words(girl), **extra})
        if p in ("/api/story/frame", "/api/story/movie", "/api/story/new"):
            girl = data.get("who")
            if girl not in GIRLS:
                return self.send_json({"ok": False, "error": "pick a color first"})
            if p == "/api/story/new":
                return self.send_json({"ok": True, "story": story_new(girl)})
            if p == "/api/story/movie":
                try:
                    with LOCK:
                        name, secs = story_movie(girl)
                except Exception as e:
                    build_log(f"FAIL movie {girl}: {e}")
                    return self.send_json({"ok": False, "error": str(e)[:200]})
                return self.send_json({"ok": True, "url": f"/out/{girl}/{name}", "secs": round(secs, 1), "story": load_story(girl)})
            n = int(clamp(data.get("n", 1), 1, len(ARC), 1))
            slots = clean_slots("story", data) or {}
            check_text = compose("story", slots) + " " + slots.get("say", "")
            r = gate.check(check_text, gate.load_allow(ALLOW_PATH))
            if not r["ok"]:
                return self.send_json({"ok": False, "bad": r["bad"]})
            try:
                with LOCK:
                    fr, secs, st = story_frame(girl, n, data)
            except Exception as e:
                build_log(f"FAIL story {girl} frame {n}: {e}")
                return self.send_json({"ok": False, "error": str(e)[:200]})
            new = log_words(girl, r["tokens"])
            return self.send_json({"ok": True, "frame": fr, "story": st, "url": f"/out/{girl}/{fr['pic']}", "say": f"/out/{girl}/{fr['say']}",
                                   "secs": round(secs, 1), "new": new, "words": girl_words(girl), "seed": fr["seed"]})
        self.send_error(404)


def serve_keep():
    handler = partial(SimpleHTTPRequestHandler, directory=OUT)
    handler.log_message = lambda *a: None
    ThreadingHTTPServer(("0.0.0.0", KEEP_PORT), handler).serve_forever()


if __name__ == "__main__":
    threading.Thread(target=serve_keep, daemon=True).start()
    try:
        urllib.request.urlopen(COMFY + "/system_stats", timeout=3)
        comfy = "ComfyUI: up"
    except Exception:
        comfy = "ComfyUI: NOT REACHABLE (pictures and songs will fail)"
    print(f"Studio  ->  http://127.0.0.1:{KID_PORT}    keep helper -> http://{lan_ip()}:{KEEP_PORT}/    {comfy}")
    build_log("server start " + comfy)
    ThreadingHTTPServer(("127.0.0.1", KID_PORT), Kid).serve_forever()
