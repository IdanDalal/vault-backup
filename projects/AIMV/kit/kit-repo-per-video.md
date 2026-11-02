---
type: project
created: 2026-11-02
author: jep
status: active
---

# Repo per video (plan; Idi's R9, 2026-11-02)

Idi: "One repo per video. I expect rapid iteration/evolution/progress of the engine." Each video repo is born as a fresh export of the previous video's repo and carries the tool that births the next one. Inputs: [[kit-open-source-audit]] (blockers, 14 steps), [[research-mp3-rights-2026-11-02]] (mp3 ships, option A), [[research-brightmirror-2026-11-02]] (notes + lyrics page).

## Lineage

`mexicat/pdoom-video` (MIT, Giacomo Magnanini) → `knowledge-cutoff` (video 1) → `<video-2>` → ... Every repo keeps every upstream MIT notice and a `LINEAGE.md` row: parent repo, parent commit, date, what changed in the engine.

## Steps

| # | step | output | blocked on |
|---|---|---|---|
| 1 | Clean export of `D:\work\aimv-lab\kc-engine` into `D:\work\aimv-lab\knowledge-cutoff-public` (audit steps 2-13), fresh `git init`, source repo untouched | KC repo, about 13 MB with the mp3 | holder name (Q1) |
| 2 | Ship the song: `audio/kc.mp3` + `audio/LICENSE.md` = rights file section 6 text (CC BY 4.0 "to the extent any rights exist", machine-generated disclosure, "MiniMax-Music3" credit); song data (`lyrics.json`, `audio.json`, `pitch.json`) ships under the same notice (audit D1 option A) | audio folder | Q1 |
| 3 | Audit D2-D6 at their recommendations: globe series → rounded values with cited sources; KC frames dropped; "Idi" attributions kept; "not affiliated with Anthropic" line; local-only scripts dropped or parametrised | clean tree | none |
| 4 | `tools/new-video.sh <name>`: copies the engine into a new folder, empties song, lyrics, scenes and data to stubs, writes README/PROCESS/LINEAGE templates, `cards/` (line cards) and `notes.json`, inits git | the self-reproducing step | none |
| 5 | Lyrics page per repo: click a line, the video jumps there; words light as sung; built from `lyrics.json` word times (Bright Mirror lesson 3) | `site/` folder, GitHub Pages | none |
| 6 | Verify: secret and path greps empty, clean-clone render of one still, size check (audit step 13) | probe log | none |
| 7 | GitHub: repo created private, push, file list reviewed, then public | live repo | Idi creates the empty repo (one click) or installs `gh` once; flip to public = his call |
| 8 | Video 2 repo = `new-video.sh` run on KC once the premise exists | video 2 repo | premise |

## Risks

- Audit step 6 (parametrise machine paths in 11 TS scripts, 6 shell scripts, 10 Python tools) is the biggest job, about half a session; a missed path leaks `C:/Users/jep` (the step 6 grep catches it).
- The mp3 embeds the full generation settings (seed, 4,120-character style prompt, lyrics): no paths or personal data; kept as proof of machine generation (rights file recommendation).
- Copying engine code forward per repo forks the engine N times; fixes made in video 3 never reach video 2. Accepted by R9: old repos stay frozen as records of their video.

## Open WHATs

1. Q1 RULED 2026-11-02 (Idi): "Chorus of Minds" on every MIT and CC BY line.
2. Q2 RULED 2026-11-02 (Idi): a `chorusofminds` GitHub organization holds the repos. Idi creates it (one web form, github.com/organizations/new); jep cannot.

## Status 2026-11-02

- Steps 1-4 and 6 DONE: `D:\work\aimv-lab\knowledge-cutoff-public`, one commit `c2dcb6f` (author Chorus of Minds; private session link amended out before any push), 204 files, 13.29 MB, no remote. Report: [[kc-public-export-2026-11-02]].
- Verified: private-path grep 0 hits (jep re-ran); name-guard `scan_repo.py` 225 objects 0 hits; kc-engine unchanged (HEAD `9be094d`); 4 stills rendered from the export (june1, spinning1, spinning2, kit-fx); `new-video.sh` test repo passes `bun install` + tsc and renders a blank plate.
- Org `chorusofminds` created by Idi 2026-11-02.
- Step 7 waits on: an empty private repo `knowledge-cutoff` in the org; then jep pushes over SSH, Idi reviews the file list, Idi flips it public.
- Step 5 (lyrics page) not started.
