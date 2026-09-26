"""Tests for the word gate. Run: venv\\Scripts\\python test_gate.py"""
import gate

ALLOW = {"pink", "cat", "dancing", "my", "name", "is", "i", "love", "squishies"}

def check(text, ok, bad=()):
    r = gate.check(text, ALLOW)
    assert r["ok"] == ok, (text, r)
    assert list(r["bad"]) == list(bad), (text, r)

check("pink cat", True)
check("pink unicorn", False, ["unicorn"])
check("Pink, cat!", True)
check("", False, [])
check("My name is K. I love squishies.", False, ["k"])
check("my name is 10", True)          # digits pass
check("pink   cat\n dancing", True)   # whitespace and newlines
check("pink unicorn unicorn dragon", False, ["unicorn", "dragon"])  # each bad word once
assert gate.tokens("I'm Pink-cat!") == ["i", "m", "pink", "cat"]
print("gate tests: 9 passed")
