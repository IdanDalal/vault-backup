---
type: proposal
created: 2026-09-11
author: jep
project: XCOM 2 WotC campaign
status: active
---

# XCOM 2: playstyle on record, and what jep can do with file access

## 1. Playstyle, Idi's words distilled (2026-09-11)

- Difficulty: Legend (highest). Second Wave options on, most of all Beta Strike (double HP for everyone), chosen to blunt the urge to kill every enemy before it acts once.
- Ironman: off, on purpose. Two reasons. Thematic: the style is slow, methodical, puzzle-solving, reloading constantly to reach the best scenario per decision, turn, mission, day, month. Technical: with four-digit mod counts the risk of irrecoverable save damage is non-zero.
- Saves: many kept for several days before deletion, as insurance against a dire situation worth hours of rollback.
- Loves: min-maxing, theorycrafting, build optimizing, experimentation, diversity, variety, dynamic cycles over static ones, customization, personalization, creative expression, cohesion and coherence, novelty, lore-friendliness over lore-accuracy.
- Campaign structure: built to be near-impossible on an honest Ironman run, then solved by reload.

This closes the "no difficulty or ironman ruling" gap from the 2026-09-10 sitrep.

## 2. The Reddit thread: not readable from here

Every anonymous route returned a wall: reddit.com and api.reddit.com (403), old.reddit.com (403), the page fetcher (barred from the domain), nine Redlib mirror instances (bot checks), a reader proxy (403 passed through). What leaked: title "You can now mod ANY game. Frontier LLMs solved reverse engineering, here are two real examples!", author u/SuperV1234, one example being Prey (2017) with an aim-down-sights and viewmodel mod produced through a frontier model. Source for that: a Korean AI-news summary at promppy.com, which states it is a summary and links back to Reddit. The author's blog (vittorioromeo.com) has no matching post through May 2026. Confidence high on the wall, medium on the Prey detail.

Two ways to get the full thread in front of jep, both yours: open it in Edge with the Claude in Chrome extension (the proven path for Perplexity and Nano Banana), or save the page and drop the file into `projects/XCOM/`.

Relevance to XCOM 2: low. That thread is about games without mod support, where an LLM reverse-engineers compiled code. XCOM 2 ships an official SDK with the game's UnrealScript source, so no reverse engineering is needed. The evolution for this project is script mods through the SDK, not decompilation. A related Hacker News thread (id 46888796, Feb 2026) reports the workflow for the no-SDK case: Ghidra decompiler output fed per-function to an agent; Gemini Flash drops the tail of long functions, Claude Opus and GPT 5.2 held up better. Anecdotal, one user.

## 3. What exists on this PC, verified 2026-09-11

| Thing | State |
|---|---|
| Game install | `C:\Program Files (x86)\Steam\steamapps\common\XCOM 2\XCom2-WarOfTheChosen\` present |
| Default configs | `XComGame\Config\`, 49 `Default*.ini` files (AI, class data, character stats, cheats, camera, and so on) |
| Workshop mods | 1,095 folders, 51 GB, each with its own `Config\XCom*.ini` overrides |
| Launcher DB | `C:\XCOM2 AML 1.6.0-beta\settings.json`, 1,094 active, per-mod `SteamTags`, `Dependencies`, `DateAdded` |
| User-side game data | `C:\Users\Idi\Documents\my games\XCOM2 War of the Chosen\XComGame\` (Config overrides, SaveData, Logs, CharacterPool). Exists, closed to jep |
| SDK | not installed (the free "XCOM 2 War of the Chosen SDK" Steam tool; needed to compile script mods) |
| Highlander | present in the launcher DB as v1.31.1 |

## 4. Access: three done-states, pick one

- A. Drop on request. You copy a folder (Logs, SaveData, Config) into `projects/XCOM/live/` when asked, same as the tutoring drop. Zero setup. Every read costs you a copy.
- B. Read-only grant. Give `jep` read access to the one folder `...\XCOM2 War of the Chosen\XComGame` through the folder's Properties, Security tab (a GUI action, no command). jep reads logs, saves, configs and the pool at will; writes still pass through your hand. Recommended: one action, then every item in §5 runs without you.
- C. Full grant. Read and write to that folder. jep applies config edits and save rotation directly. Fastest, and the one where a jep mistake reaches your live game. Not recommended until §5 items 1 to 3 have run clean for a few sessions under B.

## 5. What jep can do, ranked by value per your playstyle

1. Launch.log triage after every session. The game writes `Logs\Launch.log`; redscreens, "Accessed None", missing-mod and config-conflict lines land there. Delta report per session: new errors, which mod, what to toggle. Read-only. First value inside one session.
2. Config collision index. 1,094 mods each override `XCom*.ini` variables; the last writer wins by load order and nobody sees the losers. jep builds a who-sets-what table across all mod configs plus the 49 defaults, flags the same variable set by several mods, and turns the "MODS TO CONFIGURE MANUALLY" list in `Next Campaign Notes.md` into exact ini lines (WSR skin-only weapons, Amalgamation exclusions). Drafts for you under B, applied directly under C.
3. Theorycraft tables. Enemy stats (`DefaultGameData_CharacterStats.ini` plus the 88 enemy mods' overrides) against soldier and weapon stats, with Beta Strike doubling applied: hits-to-kill per weapon tier per enemy, aim and crit breakpoints, which Second Wave options interact with which mods. This is the min-max layer, generated from the actual numbers rather than wiki memory.
4. Save keeper. Saves are binary; jep never edits them. A rotation script copies `SaveData` before each session, keeps a rolling N days, names snapshots by campaign date, and reports which save is the last known-good after a crash. Your reload style protected against corruption at zero effort.
5. Pool and sheet reconciliation. The 13 spelling drifts between the bin and the sheet resolved to one list for your hand; after that, a per-session check that the pool bin and the sheet still agree, and reference cards per soldier assembled from both.
6. Sheet Mods tab sync. The tab trails the launcher by 90 mods. jep produces the missing rows with categories auto-filled from each mod's `SteamTags`, plus the 32 renamed or removed rows, for you to paste. Confirmed-column integrity check after every launcher change.
7. Campaign journal. Per session: missions played (from Launch.log and save names), what changed in the roster, a theorycraft note per puzzle solved. Feeds the "dynamic cycles" preference with a record you can review.
8. Script mods, later. With the SDK installed, jep writes and compiles UnrealScript mods: custom Second Wave options, a bespoke ability, a UI tweak. Needs the SDK (a Steam tool download on your account) and a test cycle in-game. The "mod any game" idea from the thread, applied to a game that already invites it.

Recommendation: B for access, then items 1, 2, 4 as the first quest list, in that order. Item 1 pays on the next session, item 2 turns the manual-config backlog into a paste job, item 4 protects the style you described. Say the word.

## 6. Sources

- promppy.com summary of the Reddit post, 2026-09-10: https://www.promppy.com/item/1566151 (summary only, per its own statement)
- Hacker News thread on LLM-assisted reverse engineering: https://news.ycombinator.com/item?id=46888796
- vittorioromeo.com blog index (no matching post): https://vittorioromeo.com/
- Game paths: verified by directory listing on this PC, 2026-09-11.
