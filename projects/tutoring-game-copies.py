# type: lesson-tool | created: 2026-08-19 | author: jep | project: tutoring
# Regenerates tutoring-game-K.html and tutoring-game-D.html from tutoring-game-lab.html,
# swapping only the GAME/MORE config blocks (per-girl session-loaded defaults).
# Run: python3 ~/vault/projects/tutoring-game-copies.py
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
  listen: "on",               // on = the gate SAYS the word, write what you hear · off = it shows the word
  storm:  "on",               // on = a word storm hits in the middle of the day
  password: "on",             // on = finishing a day sets a password for next time
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
  listen: "on",               // on = the gate SAYS the word, write what you hear · off = it shows the word
  storm:  "on",               // on = a word storm hits in the middle of the day
  password: "on",             // on = finishing a day sets a password for next time
  start:  "READY? HOLD TO FLY",
  win:    "YOU DID IT! DANCE!",
  lose:   "OH NO... WRONG!",
  again:  "DANCE AGAIN",
  gate:   "WRITE IT TO FLY AGAIN",
};'''

game_re = re.compile(r"const GAME = \{.*?\};", re.S)
more_re = re.compile(r"const MORE = \{.*?\};", re.S)

for initial, g, m in (("K", K_GAME, K_MORE), ("D", D_GAME, D_MORE)):
    out = game_re.sub(lambda _: g, master, count=1)
    out = more_re.sub(lambda _: m, out, count=1)
    out = out.replace("<title>GAME LAB</title>", f"<title>GAME LAB {initial}</title>")
    out = out.replace("Session-4 candidate: a zigzag sky game the girls remake",
                      f"{initial}'s copy, defaults loaded from her sessions. A zigzag sky game she remakes")
    path = f"/home/jep/vault/projects/tutoring-game-{initial}.html"
    open(path, "w").write(out)
    print(path, len(out), "bytes")
