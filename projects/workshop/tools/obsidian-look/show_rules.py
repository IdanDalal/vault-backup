"""Print full theme rules whose selector list contains any of the given substrings. Read-only.
Usage: python show_rules.py PYLIB THEME_CSS SUBSTR [SUBSTR ...]"""
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, sys.argv[1])
import tinycss2  # noqa: E402

css = open(sys.argv[2], encoding="utf-8").read()
subs = sys.argv[3:]


def walk(nodes, ctx=""):
    for n in nodes:
        if n.type == "qualified-rule":
            pre = " ".join(tinycss2.serialize(n.prelude).split())
            if any(s in pre for s in subs):
                body = " ".join(tinycss2.serialize(n.content).split())
                print((ctx + " " if ctx else "") + pre[:400])
                print("     { " + body[:700] + " }")
        elif n.type == "at-rule" and n.content is not None and n.lower_at_keyword in ("media", "supports", "container", "layer"):
            walk(tinycss2.parse_rule_list(n.content, skip_comments=True, skip_whitespace=True),
                 "@" + n.at_keyword + " ".join(tinycss2.serialize(n.prelude).split()))


walk(tinycss2.parse_stylesheet(css, skip_comments=True, skip_whitespace=True))
