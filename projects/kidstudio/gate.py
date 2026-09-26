"""The word gate. Every token of the girl's text must be in the allow set."""
import re

_SPLIT = re.compile(r"[^a-z0-9]+")


def tokens(text):
    return [t for t in _SPLIT.split(text.lower()) if t]


def check(text, allow):
    toks = tokens(text)
    if not toks:
        return {"ok": False, "bad": [], "tokens": []}
    bad = []
    for t in toks:
        if t.isdigit() or t in allow:
            continue
        if t not in bad:
            bad.append(t)
    return {"ok": not bad, "bad": bad, "tokens": toks}


def load_allow(path):
    try:
        with open(path, encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip() and not line.startswith("#")}
    except FileNotFoundError:
        return set()
