# type: lesson-tool | created: 2026-08-19 | author: jep | project: tutoring
# Refreshes tutoring-game-K.html and tutoring-game-D.html with the engine from
# tutoring-game-lab.html. Each girl's existing GAME/MORE blocks and <title> are
# PRESERVED from her current file — her customizations survive every engine update.
# The embedded blocks below are first-run seeds, used only if her file doesn't exist.
# Run: python3 ~/vault/projects/tutoring-game-copies.py
import os
import re

master = open("/home/jep/vault/projects/tutoring-game-lab.html").read()

K_GAME = '''const GAME = {
  name:   "K'S SKY GARDEN",   // give it a name!
  player: "\U0001F98B",               // any emoji you like
  world:  "garden",           // garden · city · candy
  sky:    "magic",            // magic = one whole day, sunrise to sunrise! or one color: pink, black, gold...
  move:   "zigzag",           // zigzag = hold to go up! · float = tap tap tap!
  speed:  3.5,                // how fast?
  hole:   190,                // big hole = relaxed, small hole = tricky
  trail:  "red",              // the line you draw in the sky
  floor:  "auto",             // auto · grass · ocean · road · candy
};'''

K_MORE = '''const MORE = {
  mode:   "level",            // level = finish one day, with hearts · free = play forever
  level:  15,                 // how long is the day?
  lives:  4,                  // how many hearts?
  jump:   9,                  // float mode: how strong is one tap?
  words:  ["FLOUR", "FLOWER", "OLIVE", "OIL", "RIGHT", "WAIT"],   // your words fly in the sky — catch them!
  labels: "on",               // on = everything tells you its English name · off = quiet sky
  sound:  "on",               // on · off — blips and chimes
  music:  "calm",             // calm · party · off
  listen: "picture",          // picture = a picture shows the word, write its name · on = it SAYS it · off = it shows the word
  storm:  "on",               // on = a word storm hits in the middle of the day
  password: "on",             // on = finishing a day sets a password for next time
  fx:     "on",               // on = butterflies + magic glow · off = plain (if the phone is slow)
  start:  "WAIT... HOLD TO FLY",
  win:    "WELL DONE!",
  lose:   "CAUGHT YOU!",
  again:  "ONE MORE",
  gate:   "WRITE IT!",
};'''

D_GAME = '''const GAME = {
  name:   "SQUISHY SKY",      // give it a name!
  player: "\U0001F9F8",               // any emoji you like
  world:  "candy",            // garden · city · candy
  sky:    "magic",            // magic = one whole day, sunrise to sunrise! or one color: pink, black, gold...
  move:   "zigzag",           // zigzag = hold to go up! · float = tap tap tap!
  speed:  4.5,                // how fast?
  hole:   165,                // big hole = relaxed, small hole = tricky
  trail:  "hotpink",          // the line you draw in the sky
  floor:  "auto",             // auto · grass · ocean · road · candy
};'''

D_MORE = '''const MORE = {
  mode:   "level",            // level = finish one day, with hearts · free = play forever
  level:  20,                 // how long is the day?
  lives:  3,                  // how many hearts?
  jump:   9,                  // float mode: how strong is one tap?
  words:  ["AGAIN", "WRONG", "WAIT", "TOGETHER", "BOUNCY", "SOFT"],   // your words fly in the sky — catch them!
  labels: "on",               // on = everything tells you its English name · off = quiet sky
  sound:  "on",               // on · off — blips and chimes
  music:  "party",            // calm · party · off
  listen: "picture",          // picture = a picture shows the word, write its name · on = it SAYS it · off = it shows the word
  storm:  "on",               // on = a word storm hits in the middle of the day
  password: "on",             // on = finishing a day sets a password for next time
  fx:     "on",               // on = butterflies + magic glow · off = plain (if the phone is slow)
  start:  "READY? HOLD TO FLY",
  win:    "YOU DID IT! DANCE!",
  lose:   "OH NO... WRONG!",
  again:  "DANCE AGAIN",
  gate:   "WRITE IT TO FLY AGAIN",
};'''

game_re = re.compile(r"const GAME = \{.*?\};", re.S)
more_re = re.compile(r"const MORE = \{.*?\};", re.S)
title_re = re.compile(r"<title>.*?</title>", re.S)

for initial, seed_g, seed_m in (("K", K_GAME, K_MORE), ("D", D_GAME, D_MORE)):
    path = f"/home/jep/vault/projects/tutoring-game-{initial}.html"
    g, m, title, source = seed_g, seed_m, f"<title>GAME LAB {initial}</title>", "seed defaults"
    if os.path.exists(path):
        current = open(path).read()
        got_g, got_m, got_t = game_re.search(current), more_re.search(current), title_re.search(current)
        if got_g and got_m:
            g, m, source = got_g.group(0), got_m.group(0), "her current file"
            if got_t:
                title = got_t.group(0)
        else:
            print(f"WARNING: {path} exists but its GAME/MORE blocks are unreadable — NOT touching it.")
            print("         Fix the blocks by hand (a missing }; usually) and rerun.")
            continue
    out = game_re.sub(lambda _: g, master, count=1)
    out = more_re.sub(lambda _: m, out, count=1)
    out = title_re.sub(lambda _: title, out, count=1)
    out = out.replace("Session-4 candidate: a zigzag sky game the girls remake",
                      f"{initial}'s copy. A zigzag sky game she remakes")
    open(path, "w").write(out)
    print(f"{path}  {len(out)} bytes  (config kept from {source})")
