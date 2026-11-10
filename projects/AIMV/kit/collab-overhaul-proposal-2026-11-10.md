---
type: project
created: 2026-11-10
author: jep
status: active
---

# Proposal: how Idi and jep work on videos, rebuilt (2026-11-10)

Idi's ask (verbatim, 2026-11-10): "I'd rather overhaul our interaction/collaboration/co-operation process entirely ... We need some sort of interface that fits our audio-visual needs." Research: 3 agents, 5 repos, 3 creators. Files (outside the vault, read-only notes): `D:\work\aimv-lab\pa-video\research\collab-2026-11-10\` (`brief.md` pain points P1-P7, `r-design.md`, `r-process.md`, `r-creators.md`, `jep-own-tools.md`).

## The pain points (2026-11-08 session)

P1 walls of text · P2 builder notices flood the chat · P3 voice-typed timestamp lists, drift between versions · P4 confusing option tables · P5 45-min render, then watch, then type notes · P6 look choices argued in words · P7 status lives in scrollback

## The shape: three pages, one quiet chat

| surface | what Idi does there | what it replaces | fixes | source |
|---|---|---|---|---|
| 1. Review Room (one page per version) | plays the video; pauses; clicks the frame; speaks his note (dictation); the note pins to song time + plate + x,y; previous version plays beside it at the same song time | the voice-typed list, jep cutting frames, the 5 s drift | P3, P5 | Imaginative Prompting's frame-click ("his most-used feature"), open-design pins + anchored/stale/lost ladder, hyperframes side-by-side |
| 2. Decision page (one per ruling) | sees equal-size cards (stills or synced A/B clips with the song), one axis per page, jep's pick marked, a "keep as is" card; clicks one | A/B/C tables in chat | P4, P6 | impeccable decision page, IP option sheets, open-design form rules (5 questions max, defaults filled) |
| 3. Studio board (one, pinned) | glances at TO WATCH / TO DECIDE / DONE; each builder run is one line | chat relays, long plan files | P2, P7 | IP status block, superpowers progress ledger, Bright Mirror's "interrupt only when needed" |
| chat | gets a link and one question, under 150 words | everything else | P1 | all three |

## Under the hood (jep's side; no action from Idi)

| change | fixes | source |
|---|---|---|
| song time is the clock: every note, still and clip is stamped `v3 · plate · 2:30.70` (burned into review renders); the song is locked, so a note never drifts | P3 | r-design, r-creators |
| sheets before renders: beat sheet + seam strips + stills go to the Review Room first; the 45-min render only after he passes them; look calls on stills and 5-10 s clips | P5, P6 | hyperframes, Degenerative Pixels' small steps |
| a judge before Idi: a fresh agent scores each fixed shot against the approved target still; Idi sees a shot at 8/10+ or when it stalls (3 rounds max) | P5 | dream-loop, our polish method |
| one coordinator per wave: builders write reports to files and return 5 lines; the board gets one line; the chat hears nothing until a decision is needed | P1, P2 | superpowers |
| rulings log: every call jep makes for him = one line "what · why · cost if wrong", numbered, on the board; he overrules by index | P1, P4, P7 | superpowers |
| look rulings become numbers (a LOOK spec: values, lens events, banned list), asked once | P4, P6 | impeccable |

## Where the pages live

Claude Artifacts (hosted, private, phone-readable): dictation, comments, a shared database jep reads, read-aloud of jep's replies. Limit: 20 MB per video file, so the Review Room plays the video as per-plate clips (~25 s each at full 1080p) plus a continuous lower-quality proxy; the full-quality MP4 stays on the PC for the continuous watch. jep's call (HOW): Artifacts, because dictation and phone access only work there.

## Skipped, with reasons

superpowers plugin install (injects a mandatory-skill rule into every session; its approval gates clash with the vault rules) · impeccable install (live mode can launch agents with permission checks off) · dream-loop's image generation (needs paid API keys: plan-only billing) · hyperframes as an engine (we keep ours; rebuild its review sheets with ffmpeg)

## Evidence quality

Small: superpowers' evals are author-run (n = 2-5, one project); dream-loop has one demo; Degenerative Pixels describes a frame-marking editor but never showed it; Bright Mirror publishes no process. IP's frame-click is his own statement on his public pages (strongest signal: the same habit Idi already has).

## Build order (rec)

1. Review Room for v3: Idi's v3 notes go in by voice at the frame (first use, real notes). Cost: about 2-3 hours of jep work (clip encoding, page, notes table, read-back test).
2. Studio board: the first page jep keeps current.
3. Decision page: first use = the colour brainstorm (R35's open half).
4. Under-the-hood changes roll into wave 3.
