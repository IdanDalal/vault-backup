"""Build Idi's black look for D:\\work\\vault without plugin code.

Inputs : current Minimal theme.css; his archived Style Settings + Minimal Theme Settings values.
Outputs: STAGE/themes/Minimal/{theme.css,manifest.json}, STAGE/snippets/idi-black.css, report on stdout.

How: the two plugins did two things. (1) They set CSS variables: reproduced as variable blocks.
(2) They added classes to <body>: reproduced by copying every theme rule gated on such a class and
replacing the class with a selector that always matches, keeping specificity.

Usage: python build_black.py PYLIB THEME_DIR STYLE_JSON MINIMAL_JSON STAGE_DIR
"""
import colorsys
import io
import json
import os
import re
import shutil
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, sys.argv[1])
import tinycss2  # noqa: E402
import yaml  # noqa: E402

theme_dir, style_json, minimal_json, stage = sys.argv[2:6]
css = open(os.path.join(theme_dir, "theme.css"), encoding="utf-8").read()
style = json.load(open(style_json, encoding="utf-8"))
mini = json.load(open(minimal_json, encoding="utf-8"))
NL = chr(10)

# ---------- settings definitions ----------
defs, all_setting_classes = {}, set()
for b in re.findall(r"/\*\s*@settings(.*?)\*/", css, flags=re.S):
    y = yaml.safe_load(b.replace("\t", "    "))
    for s in y["settings"]:
        if "id" not in s:
            continue
        defs[(y["id"], s["id"])] = s
        if s["type"] == "class-toggle":
            all_setting_classes.add(s["id"])
        if s["type"] == "class-select":
            for o in s.get("options", []):
                all_setting_classes.add(o if isinstance(o, str) else o.get("value"))


def hex_to_hsl(h):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    a = int(h[6:8], 16) / 255 if len(h) >= 8 else None
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    return round(hh * 360), round(ss * 100), round(ll * 100), a


dark_vars, light_vars, body_vars, active, skipped = [], [], [], set(), []
for key, val in style.items():
    parts = key.split("@@")
    d = defs.get((parts[0], parts[1]))
    if not d:
        skipped.append(key)
        continue
    sid, mode, typ = parts[1], (parts[2] if len(parts) > 2 else ""), d["type"]
    if typ == "class-toggle":
        if val is True:
            active.add(sid)
    elif typ == "class-select":
        if isinstance(val, str) and val not in ("", "none", "default"):
            active.add(val)
    elif typ in ("variable-themed-color", "variable-color"):
        target = dark_vars if mode == "dark" else light_vars if mode == "light" else body_vars
        fmt = d.get("format", "hex")
        if fmt == "hex":
            target.append(("--" + sid, val))
        elif fmt == "hsl-split":
            hh, ss, ll, a = hex_to_hsl(val)
            target += [("--%s-h" % sid, str(hh)), ("--%s-s" % sid, "%d%%" % ss), ("--%s-l" % sid, "%d%%" % ll)]
        else:
            skipped.append(key + " (format %s not handled)" % fmt)
    elif typ in ("variable-number", "variable-number-slider"):
        body_vars.append(("--" + sid, "%s%s" % (val, d.get("format") or "")))
    elif typ in ("variable-text", "variable-select"):
        body_vars.append(("--" + sid, str(val)))
    else:
        skipped.append(key + " (type %s)" % typ)

# defaults the plugin would switch on without a stored value
for (sec, sid), d in defs.items():
    k = sec + "@@" + sid
    if d["type"] == "class-toggle" and d.get("default") is True and style.get(k) is not False:
        active.add(sid)
    if d["type"] == "class-select" and k not in style and d.get("default") not in (None, "", "none", "default"):
        active.add(d["default"])

# Minimal Theme Settings plugin: classes and variables
active |= {mini["darkStyle"], mini["darkScheme"]}
for flag, cls, on in [("colorfulHeadings", "colorful-headings", True), ("colorfulFrame", "colorful-frame", True),
                      ("colorfulActiveStates", "colorful-active", True), ("focusMode", "minimal-focus-mode", True),
                      ("fullWidthMedia", "full-width-media", True), ("imgGrid", "img-grid", True),
                      ("labeledNav", "labeled-nav", True), ("underlineInternal", "links-int-on", True),
                      ("underlineExternal", "links-ext-on", True), ("folding", "minimal-folding", True),
                      ("bordersToggle", "borders-none", False), ("minimalStatus", "minimal-status-off", False),
                      ("trimNames", "full-file-names", False), ("devBlockWidth", "minimal-dev-block-width", True)]:
    if bool(mini.get(flag)) == on:
        active.add(cls)
for k in ("imgWidth", "tableWidth", "iframeWidth", "mapWidth", "chartWidth"):
    active.add(mini[k])
mini_vars = [("--font-ui-small", "%spx" % mini["textSmall"]), ("--line-height", str(mini["lineHeight"])),
             ("--line-width", "%srem" % mini["lineWidth"]), ("--line-width-wide", "%srem" % mini["lineWidthWide"]),
             ("--max-width", "%s%%" % mini["maxWidth"])]

BODY_CLASSES = active | all_setting_classes | {
    "theme-dark", "theme-light", "is-mobile", "is-tablet", "is-phone", "is-ios", "is-android", "mod-windows", "mod-macos",
    "mod-linux", "is-frameless", "is-hidden-frameless", "is-focused", "is-fullscreen", "is-maximized", "is-translucent",
    "is-popout-window", "show-inline-title", "show-view-header", "show-ribbon", "native-scrollbars", "obsidian-app",
    "minimal-theme", "css-settings-manager", "is-grabbing", "minimal-light", "minimal-light-tonal", "minimal-light-contrast",
    "minimal-light-white", "minimal-dark", "minimal-dark-tonal", "minimal-dark-black", "colorful-headings", "colorful-frame",
    "colorful-active", "minimal-focus-mode", "full-width-media", "img-grid", "labeled-nav", "links-int-on", "links-ext-on",
    "minimal-folding", "borders-none", "minimal-status-off", "full-file-names", "minimal-dev-block-width"}
BODY_CLASSES |= {c for c in re.findall(r"\.(minimal-[\w-]+-(?:light|dark))\b", css)}

ALWAYS = ":not(.jep-off)"
CLS = r"\.(-?[_a-zA-Z][\w-]*)"


def split_top(s, seps):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if depth == 0 and ch in seps:
            out.append(cur)
            out.append(ch)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def not_groups(sel):
    groups, i = [], 0
    while True:
        j = sel.find(":not(", i)
        if j < 0:
            return groups
        depth, k = 1, j + 5
        while k < len(sel) and depth:
            depth += sel[k] == "("
            depth -= sel[k] == ")"
            k += 1
        groups.append(sel[j + 5:k - 1])
        i = k


SCHEMES = set(re.findall(r"\.(minimal-[\w-]+-(?:light|dark))\b", css)) | {
    "minimal-light", "minimal-light-tonal", "minimal-light-contrast", "minimal-light-white", "minimal-dark",
    "minimal-dark-tonal", "minimal-dark-black", "colorful-frame", "labeled-nav", "links-int-on", "links-ext-on",
    "minimal-folding", "borders-none", "full-file-names", "minimal-dev-block-width"}
DEAD = (all_setting_classes | SCHEMES) - active
stats = {"copied": 0, "dropped_nonbody": 0, "negated": 0, "pruned_dead": 0}
per_class = {}
negated = []


def rewrite(sel):
    """Return the selector rewritten for 'active classes are always on', or None."""
    sel = sel.strip()
    classes = set(re.findall(CLS, sel))
    act = classes & active
    if not act:
        return None
    neg = set()
    positive = sel
    for g in not_groups(sel):
        neg |= set(re.findall(CLS, g)) & active
        positive = positive.replace(":not(" + g + ")", "")
    if neg:
        stats["negated"] += 1
        negated.append(sel)
        return None
    if set(re.findall(CLS, positive)) & DEAD:
        stats["pruned_dead"] += 1
        return None  # also needs a switch Idi never had on: can never match
    parts = split_top(sel, " >+~")
    for idx, comp in enumerate(parts):
        if comp in (" ", ">", "+", "~", ""):
            continue
        comp_classes = set(re.findall(CLS, comp))
        if not (comp_classes & active):
            continue
        others = comp_classes - BODY_CLASSES
        tag = re.match(r"^[a-zA-Z][\w-]*", comp)
        if others or (tag and tag.group(0) not in ("body",)):
            stats["dropped_nonbody"] += 1
            return None
        new = comp
        for c in sorted(comp_classes & active, key=len, reverse=True):
            new = re.sub(r"\." + re.escape(c) + r"(?![\w-])", ALWAYS, new)
        if not tag:
            new = "body" + new
        parts[idx] = new
    for c in act:
        per_class[c] = per_class.get(c, 0) + 1
    stats["copied"] += 1
    return "".join(parts)


def process(nodes, out, indent=""):
    for n in nodes:
        if n.type == "qualified-rule":
            prelude = tinycss2.serialize(n.prelude)
            sels = [s for s in split_top(prelude, ",") if s != ","]
            new = [r for r in (rewrite(s) for s in sels) if r]
            if new:
                body = tinycss2.serialize(n.content).strip()
                out.append(indent + ("," + NL + indent).join(new) + " {" + NL + indent + "  " + body + NL + indent + "}")
        elif n.type == "at-rule" and n.content is not None and n.lower_at_keyword in ("media", "supports", "container", "layer"):
            inner = []
            process(tinycss2.parse_rule_list(n.content, skip_comments=True, skip_whitespace=True), inner, indent + "  ")
            if inner:
                out.append(indent + "@" + n.at_keyword + tinycss2.serialize(n.prelude).rstrip() + " {" + NL + NL.join(inner) + NL + indent + "}")


rules = []
process(tinycss2.parse_stylesheet(css, skip_comments=True, skip_whitespace=True), rules)


def block(sel, pairs):
    seen, lines = {}, []
    for k, v in pairs:
        seen[k] = v
    for k, v in seen.items():
        lines.append("  %s: %s;" % (k, v))
    return sel + " {" + NL + NL.join(lines) + NL + "}"


HEAD = """/* idi-black.css
   Built by jep on 2026-11-11 from Idi's own values (archived Curtains and Idiverse configs:
   Minimal Theme Settings + Style Settings). Needs the Minimal theme. No plugin involved.
   Part 1: theme rules that the two plugins used to switch on, rewritten to apply always.
   Part 2: his colours and sizes, last, so they win.
   Regenerate with build_black.py; do not hand-edit part 1. */
"""
snippet = (HEAD + NL + "/* ---- Part 1: %d switched rules ---- */" % len(rules) + NL + (NL + NL).join(rules) + NL + NL
           + "/* ---- Part 2: variables ---- */" + NL
           + block("body" + ALWAYS + ALWAYS, mini_vars + body_vars) + NL + NL
           + block("body.theme-dark" + ALWAYS + ALWAYS, dark_vars) + NL
           + (NL + block("body.theme-light" + ALWAYS + ALWAYS, light_vars) + NL if light_vars else "")
           + NL + "/* ---- Part 3: two theme defaults that the plugins used to switch off ---- */" + NL
           + block("body" + ALWAYS + ALWAYS, [("--checklist-done-color", "var(--text-muted)")]) + NL
           + "body" + ALWAYS + ALWAYS + " .vertical-tab-nav-item.is-active," + NL
           + "body" + ALWAYS + ALWAYS + " .horizontal-tab-nav-item.is-active {" + NL
           + "  background-color: var(--interactive-accent);" + NL + "  color: var(--text-on-accent);" + NL + "}" + NL)

os.makedirs(os.path.join(stage, "themes", "Minimal"), exist_ok=True)
os.makedirs(os.path.join(stage, "snippets"), exist_ok=True)
for f in ("theme.css", "manifest.json"):
    shutil.copyfile(os.path.join(theme_dir, f), os.path.join(stage, "themes", "Minimal", f))
with open(os.path.join(stage, "snippets", "idi-black.css"), "w", encoding="utf-8", newline="") as f:
    f.write(snippet)

# ---------- report ----------
print("active classes (%d): %s" % (len(active), ", ".join(sorted(active))))
print()
print("rules copied per class:")
for c in sorted(active):
    print("   %-28s %s" % (c, per_class.get(c, 0) or "0  <-- no rule in this theme version"))
print()
print("selectors copied %(copied)d | dropped (class on a non-body element) %(dropped_nonbody)d | negated %(negated)d | pruned as unreachable %(pruned_dead)d" % stats)
print("dark vars %d | light vars %d | body vars %d | skipped keys: %s" % (len(dark_vars), len(light_vars), len(body_vars) + len(mini_vars), skipped))
print()
print("negated selectors (apply today because the class is absent; the plugin would have switched them off):")
for s in negated:
    print("   ", s[:150])
for v in ("--base-h", "--base-l", "--base-d", "--frame-background-h", "--line-width", "--line-width-wide", "--max-width", "--line-height", "--font-ui-small", "--header-height", "--bg3", "--ax1", "--ui1", "--tx1"):
    print("   var %-24s used %d times in theme" % (v, len(re.findall(re.escape(v) + r"\b", css))))
# parse check of the output
parsed = tinycss2.parse_stylesheet(snippet, skip_comments=True, skip_whitespace=True)
errs = [n for n in parsed if n.type == "error"]
print()
print("snippet: %d bytes, %d top-level rules, %d parse errors, braces %d/%d" % (
    len(snippet.encode("utf-8")), len(parsed), len(errs), snippet.count("{"), snippet.count("}")))
