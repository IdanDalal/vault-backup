---
type: research
created: 2026-11-02
author: Agent rights-research
---

# Shipping kc.mp3 in the public repo: rights research (2026-11-02)

**Verdict: ship it. No MiniMax text restricts redistributing an output file; the honest notice is CC BY 4.0 "to the extent any rights exist", plus a machine-generated disclosure and the "MiniMax-Music3" credit (option A, section 6).**

Not legal advice: neither the author of this file nor jep is a lawyer. Findings below are what the sources say, with a confidence per claim.

Method: anonymous reads only. Raw pages saved under `C:\Users\jep\.claude\jobs\99182c36\tmp\rights\` and grepped. Unread or walled pages are marked UNREAD. Prior research (`D:\work\AIMVs\ours\release\research\rights-rules.md`, audit rows B1 and D1) re-checked, not repeated.

## 1. MiniMax: every text that could touch the output

Primary sources read today:

| source | date on page | what it says about outputs | link |
|---|---|---|---|
| MiniMax-Music3 COMMUNITY LICENSE (HF) | licence file added 2026-08-11 (commit `9c47cc42`, "docs: format community license"); AUP "Last revised: August [6], 2026" | grant covers the "Software" only (weights, parameters, config, inference code, docs); outputs never defined, granted, reserved or restricted | https://huggingface.co/MiniMaxAI/MiniMax-Music3/raw/main/LICENSE |
| HF model card README | last edit 2026-10-26 (rename "MiniMax Agent" to "MiniMax Code") | no clause on outputs; frontmatter has no `license:` field; badge links to the licence above | https://huggingface.co/MiniMaxAI/MiniMax-Music3 |
| GitHub `MiniMax-AI/MiniMax-Music3` | last commit 2026-10-26 | no LICENSE file in repo (API: `license: null`); README badge points to the HF licence | https://github.com/MiniMax-AI/MiniMax-Music3 |
| MiniMax Open Platform (API) Terms | "Effective Date: March 30, 2026" | "As between you and us, and to the extent permitted by applicable laws, you retain your ownership rights in Client input and generated content." | https://platform.minimax.io/protocol/terms-of-service |
| MiniMax App and Web ToS (covers MiniMax Audio) | "Updated: June 19, 2025" | "We do not claim ownership of User Contributions or User Generated Content." Grants MiniMax a perpetual licence to that content | https://www.minimax.io/audio/doc/terms-of-service.html |
| MiniMax Audio Music Creation Terms | "Effective date: June 19, 2025" | "You are also responsible for clearly labeling AI-generated Output Content in your use to avoid misleading others." MiniMax "may embed identifiers or watermarks" | https://www.minimax.io/audio/doc/terms-of-service-music.html |
| MiniMax umbrella ToS | "Updated: April 15, 2026" | framework only; product terms control on conflict | https://www.minimax.io/terms-of-service-v2.html |
| Platform music-generation guide | undated | no sentence on copyright, ownership, commercial use or redistribution | https://platform.minimax.io/docs/guides/music-generation |

Exact licence clauses that matter:
1. Grant scope: "Permission is hereby granted ... to any person obtaining a copy of this Software, including the model weights, parameters, configuration files, inference code and associated documentation (the "Software"), to deal in the Software". Outputs sit outside the defined term. Confidence high.
2. Risk clause: "YOU SHALL BE SOLELY RESPONSIBLE FOR DETERMINING THE APPROPRIATENESS OF USING, REPRODUCING, MODIFYING, PERFORMING, DISPLAYING OR DISTRIBUTING ANY OF THE SOFTWARE OR OUTPUTS". This assumes outputs get distributed and puts the risk on us; it neither forbids nor grants. Confidence high.
3. Indemnity (a promise to cover MiniMax's losses): "YOU SHALL INDEMNIFY AND HOLD HARMLESS MINIMAX ... ARISING OUT OF OR RELATING TO ANY OF YOUR BREACH OF THIS LICENSE." Triggered only by a breach. Confidence high.
4. AUP item 11 (AUP = Acceptable Use Policy, Exhibit A): no dissemination "in or to any public environment ... without clearly and prominently disclosing that such information and/or content is machine-generated". A public GitHub repo is a public environment, so the mp3 needs the disclosure next to it. Confidence high.
5. AUP item 1 bans infringing third-party rights "through unauthorized reproduction, distribution". Applies only if the song copies someone else's work. No sign it does (prior research section 2). Confidence medium (no audio-fingerprint check run).
6. Clause 3.1 credit: "prominently display "MiniMax-Music3" on the user interface of commercial product or service". A repo is arguably no "product or service"; one credit line costs nothing. Confidence high on text, medium on scope.
7. Clause 1 (include the licence "in all copies or substantial portions of the Software"): an mp3 output is no copy of the Software, so the licence text need not ship with it. Confidence medium-high.

Answers:
- Grants output ownership: only the Platform (API) Terms ("you retain your ownership rights ... in ... generated content") and the App ToS ("We do not claim ownership"). Neither governs local open-weights use; both show MiniMax's corporate stance across its products is "the user keeps outputs". Confidence high on text, medium on applying the stance by analogy.
- Reserves output ownership: no MiniMax text found. Confidence high for the pages listed.
- Disclaims: the licence disclaims all warranty on "SOFTWARE OR OUTPUTS". Confidence high.
- Restricts redistribution of an output file: nowhere. Only conditions found: disclose machine generation (AUP 11; Audio Terms labelling duty) and no infringement (AUP 1). Confidence high.
- Contradicting claim found: mer.vin (2026-08-17) says the weights are "CC BY-NC 4.0" and "You cannot use the self-hosted model, or its output, in a product you charge for" (https://mer.vin/news/minimax-music-3-is-open-weight-but-not-open-for-business/). The primary licence text contains no Creative Commons terms; the README badge uses the `creativecommons` logo icon, a likely source of the error. Treat mer.vin as wrong. Confidence high.
- MiniMax ships its own sample output (`assets/minimax_ttm.wav`, 36 MB) inside the HF repo under the same licence. Confidence high (repo tree API).
- Comfy's licensing article (read 2026-10-31, prior research): Music 3 "uses the MiniMax-Music3 Community License. Commercial use is free for companies under the threshold". Confidence medium.

## 2. Comparable providers: output terms

| provider / model | who owns outputs | redistribution limits | confidence | source |
|---|---|---|---|---|
| Suno, free (Basic) | Suno: "we retain ownership of the songs you generate" | "you will only use such Outputs for your lawful, personal and non-commercial purposes" | high | https://help.suno.com/en/articles/2416769 ; https://suno.com/terms (revised 2026-08-10, effective 2026-09-03) |
| Suno, Pro/Premier | Suno "assigns to you all of its right, title and interest in and to any Output owned by Suno"; "no representation or warranty to you that any copyright will vest in any Output" | commercial use only for Downloads within plan allocations; outputs obtained other than via Suno's download channel prohibited | high | https://suno.com/terms |
| Udio | ToS page UNREAD (JS shell, fetch blocked) | secondary: downloads disabled since 2025-10-30 after the UMG settlement; walled garden as of 2026 reports | low-medium | https://www.webpronews.com/udio-halts-ai-song-downloads-after-copyright-settlement-with-umg-warner ; https://dynamoi.com/learn/ai-music-distribution/is-udio-music-still-downloadable |
| Stable Audio Open 1.0 | official HF repo gated (UNREAD by rule); ungated mirror card names licence `stable-audio-nc-community`. Stability Community License (2024-07-05): "You own any outputs generated from the Models or Derivative Works to the extent permitted by applicable law." Which licence currently governs SAO 1.0 unverified | no explicit output-distribution limit; outputs may not train foundation models | medium | https://stability.ai/community-license-agreement ; https://huggingface.co/audo/stable-audio-open-1.0 |
| ACE-Step v1 | Apache 2.0 weights; card silent on ownership | none; card asks users to avoid "Misrepresenting AI-generated music as human-created" | high | https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B |
| YuE (v1) | Apache 2.0; "We encourage artists and content creators to freely incorporate outputs generated by YuE into their own works, including commercial projects" | none; recommends "AI-generated" labelling | high | https://github.com/multimodal-art-projection/YuE/tree/YuE-v1 |
| YuE2 (2026-09-16 permission) | weights CC BY-NC 4.0 plus creator permission: individuals may "publish, distribute, sell, license or otherwise monetize those outputs"; "Generated outputs are not subject to the model weights' NonCommercial restriction solely because they were generated with YuE2" | none for individual creators; companies need a licence | high | https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE |
| Google Lyria (via Gemini API) | "Google won't claim ownership over that content." (Gemini API terms, effective 2026-03-23); Lyria outputs carry SynthID watermarks (secondary) | none stated; "You're responsible for your use of generated content, and for the use of that content by anyone you share it with" | high on text, medium that these terms govern Lyria | https://ai.google.dev/gemini-api/terms |
| ElevenLabs Music | page avoids an ownership statement: commercial use holds "As long as you hold the necessary intellectual property rights to your generated content" | free plan: "does not include a commercial license", distributions credited "Eleven Music"; paid: commercial licence | high | https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform |

Pattern: every provider that speaks either leaves outputs with the user or (Suno free) keeps them; none claims a copyright exists. MiniMax's open-weights licence sits with ACE-Step and YuE: silent or permissive, no output restriction. Confidence high.

## 3. Precedent: public repos that ship the song file

Checked via GitHub API (tree listing + README), 2026-11-02.

| repo | audio in repo | song source | statement attached | confidence |
|---|---|---|---|---|
| `mexicat/pdoom-video` (3,702 stars, MIT, our upstream) | `audio/pdoom.mp3` (3.4 MB) | third party: Udio original 2024, "Claude-Pop" Suno version by deckard | "the song and lyrics (`audio/`, `lyrics/`, `data/lyrics.json`) are not covered by it: they belong to their authors" | high |
| `JohnHeibel/PDoomVideo` (2,775 stars) | `assets/pdoom.mp3` (same 3,437,188 bytes) | same third-party song | no licence file at all; credits the 2024 YouTube source | high |
| `neelnanda-io/dont-go-quiet-on-me` | `audio/final/dgq_master.mp3` (6.3 MB) | own song, Suno v6 | "The song audio, the lyrics and the music video: (c) 2026 Neel Nanda, all rights reserved." | high |
| `nonunsaram/feel-the-agi-video` (pdoom fork) | `audio/feeltheagi.wav` (25.9 MB) | own song, Suno vocals and arrangement | `audio/LICENSE`: CC BY-NC-SA 4.0 for song and video; code MIT | high |
| `Salmisaari/eudoom-video` | `audio/pdoom_eu.mp3` | P(Doom) Suno version with lines re-sung by ElevenLabs Music | "The song and lyrics stay with the people who wrote and made them." | high |
| `raiscan/all-that-time-saved` | 5 mp3s incl. `assets/song.mp3` | UncleHerbert's song; generator not stated | `NOTICE`: "(c) 2026 UncleHerbert, all rights reserved" | high on statement, low on whether AI-made |
| `lycfyi/power-video` (pdoom fork) | none, gitignored | Grimes, commercial human song | "Not in the repo (copyright)" | high |
| `MiniMaxAI/MiniMax-Music3` (HF) | `assets/minimax_ttm.wav` | MiniMax's own Music 3 output | covered by the Community License; no output-specific note | high |

Channels:
- Degenerative Pixels (LGTM, The Simulation's Ending, Drop the Prompt): no repo or audio file linked. Descriptions say "Song: made with Suno v6" and link Spotify and YouTube Music releases; "Drop the Prompt" publishes the full Suno prompt and lyrics. They distribute commercially through streaming, no free file. Confidence high (YouTube descriptions read today).
- Bright Mirror (music.brightmirror.co): lyrics and notes pages only, YouTube links, no downloads, no tool named, no licence or AI statement on the index page. "System Prompt (For Humans)" description: membership plea plus lyrics link. Confidence high for the pages read.
- mexicat: see first row. File present today, no takedown visible in the repo (absence of evidence only). Confidence medium.

No public repo shipping a MiniMax Music 3 song with a licence statement was found (searches: "minimax music", "code-rendered music video", "suno song"). KC would be early. Confidence medium (GitHub search only, top results).

## 4. Law

Terms: **copyright** = exclusive right to copy and distribute a work; **public domain** = no one holds copyright, anyone may use; **certiorari** = Supreme Court review; **sound recording right** = copyright in the recorded sounds, separate from the song (melody and lyrics, the "musical work").

| source | what it actually held / measured | what it is popularly claimed to show | confidence |
|---|---|---|---|
| US Copyright Office, Part 2: Copyrightability (2025-01-29), https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf | Office policy, not a court ruling. "Copyright does not extend to purely AI-generated material, or material where there is insufficient human control over the expressive elements." "prompts do not alone provide sufficient control." Humans own "their works of authorship that are perceptible in AI-generated outputs, as well as the creative selection, coordination, or arrangement ... or creative modifications". Case by case | "AI art can never be copyrighted" (wrong: human parts and arrangement can be) | high |
| Thaler v. Perlmutter, D.C. Cir. No. 23-5233, decided 2025-03-18, https://media.cadc.uscourts.gov/opinions/docs/2025/03/23-5233.pdf | Copyright Act "requires all eligible work to be authored in the first instance by a human being"; a machine cannot be the listed author. Expressly left open how much AI help a human author may use: "line-drawing disagreements ... are neither here nor there in this case" | "Courts ruled AI output is public domain" (it ruled only on a machine listed as sole author) | high |
| Thaler cert. denied, No. 25-449, 2026-03-02 | Supreme Court declined review, no opinion | "Supreme Court confirmed human authorship" (a denial decides nothing on the merits) | high (consistent across https://www.scotusblog.com/cases/case-files/thaler-v-perlmutter and https://www.jdsupra.com/legalnews/supreme-court-denies-review-in-ai-2865518/) |
| Allen v. Perlmutter (D. Colo., 1:24-cv-02665) | pending; no ruling found | n/a | medium (https://dockets.justia.com/docket/colorado/codce/1:2024cv02665/237436) |
| Israel MoJ opinion 2022-12-18 | about using copyrighted works for machine learning (training) | sometimes cited as Israel's AI-output position; it addresses inputs | medium (secondary, https://www.legal500.com/guides/wp-json/wp/v2/comparative_guide/85890) |
| Israeli Copyright Act 2007 (WIPO unofficial translation), https://www.wipo.int/wipolex/en/text/202010 | s.4(a)(1) protects "Original works ... literary ... musical"; s.4(a)(2) protects "Sound recordings" separately, with no originality test stated; "Producer" = "the person who is responsible for the arrangements necessary for the making of" the recording; s.33: "The producer of a sound recording is the first owner of copyright in a sound recording." No human-authorship wording for any category | n/a; no Israeli ruling on AI outputs found | high on text (unofficial translation, Hebrew controls), low on how a court applies it to AI audio |
| Israeli commentary | "Israeli copyright law also implies a requirement for human authorship"; no formal registration system, so no Thaler-style test case | n/a | low-medium (https://dwo.co.il/who-owns-the-rights-to-works-created-by-artificial-intelligence/) |
| Anthropic Consumer Terms (2025-10-08), https://www.anthropic.com/legal/consumer-terms | "we assign to you all our right, title, and interest (if any) in Outputs" | n/a | high |

What this means for kc.mp3, layer by layer:
1. Sound recording (US): generated from a text caption and lyrics, no human edit of the audio ("no audio edits", handoff). Under Part 2 this is "purely AI-generated material": likely no US copyright. Confidence medium-high (Office view, untested in court for music).
2. Sound recording (Israel): s.4(a)(2) plus s.33 give a recording right to the "producer", the person who arranged its making, with no originality or authorship test in the text. Idi, an Israeli resident, arranged the making (ran the model on his GPU). A plausible reading gives Idi an Israeli sound-recording right. Untested for AI. Confidence low-medium.
3. Melody and arrangement (musical work): machine-made, needs an "original" work and implied human author in both countries: likely unprotected. Confidence medium.
4. Lyrics: Claude drafted, Idi selected and edited lines. Idi's perceptible edits and his selection and arrangement can carry copyright (Part 2); Claude's untouched lines likely do not; Anthropic assigns whatever rights it has to Idi. Confidence medium.
5. The video as a whole: human-directed audiovisual work incorporating AI parts; Part 2: "inclusion of elements of AI-generated content in a larger human-authored work does not affect the copyrightability of the larger ... work as a whole". Confidence medium-high.

Consequence: what can and cannot stop redistribution.
- Can stop us: a contract we signed (none forbids it, section 1), a third party's rights in copied material (none known), MiniMax AUP disclosure condition (met by the notice). Confidence high.
- Cannot stop us: absence of copyright leaves distribution open and removes only the power to enforce exclusivity. Confidence high.
- What we lose either way: in the US, Idi likely cannot stop others re-uploading the raw audio. That exposure already exists because the full song is on YouTube and can be ripped; the repo adds a clean file and a dated public record. Confidence high.
- Honest statement: "no rights claimed" overstates (lyrics edits, Israeli recording right may exist); "all rights reserved" overclaims in the US. Both CC0 and CC BY 4.0 are honest when scoped "to the extent any rights exist". CC's own guidance (Kat Walsh, 2023-08-18, https://creativecommons.org/2023/08/18/understanding-cc-licenses-and-generative-ai/): a CC licence "will apply to the creative work that you contribute"; CC encourages "CC0 for those works that do not involve a significant degree of human creativity". KC is mixed (human lyric edits plus machine audio), which fits a CC licence on the human layer. Confidence medium-high.

## 5. Practical risks of publishing the raw mp3

| risk | evidence | size for us | confidence |
|---|---|---|---|
| Third party registers the song in Content ID (YouTube's fingerprint system that auto-claims matching uploads) and claims Idi's own video | YouTube's eligibility rules exclude "Content released under Creative Commons or similar free of charge/open licenses" and "Public domain ... recordings, or compositions" (https://support.google.com/youtube/answer/2605065). A CC-licensed, publicly dated file gives Idi a documented basis to dispute. Misfires happen: 10-hour white-noise video got five Content ID claims, 2015-2018 (https://www.eff.org/deeplinks/2018/03/ten-hours-static-gets-five-copyright-notices) | low; risk exists already via YouTube ripping; a public licence plus git timestamp helps the dispute | high on rule text, medium on outcome |
| Re-upload and monetisation by others | Reddit anecdotes (Suno Pro creator: channel "exploiting my Suno song for ad revenue", takedown rejected), low-quality aggregator: https://reddit.sentinel-team.org/posts/1ra4sj1/snapshots/2026-02-27T16%3A10%3A11.976794Z | medium probability, low cost; same exposure exists without the repo | low |
| Impersonation uploads to streaming under an artist's name | Murphy Campbell case (AI covers placed on her Spotify profile), single secondary source: https://theslop-news.pages.dev/article/ai-cloned-her-voice-then-sued-for-her-own-songs/ | low (KC has no artist profile) | low |
| Distributor rules if Idi later releases KC to Spotify | DistroKid reportedly accepts AI music when the uploader holds the rights, with AI-credit disclosure; TuneCore/CD Baby reportedly reject fully AI works (secondary: https://dynamoi.com/learn/ai-music-distribution/does-distrokid-accept-ai-music). A CC licence lets others distribute too, and makes the track ineligible for Content ID monetisation | matters only if streaming release is planned | low-medium |
| YouTube disclosure | Altered or synthetic content rule: tick "AI use" for AI music as the main focus (https://support.google.com/youtube/answer/14328491; prior research section 3). Unchanged by the repo | none new | high |
| MiniMax AUP 11 in the repo | disclosure must sit next to the file; the notice below does it | none once the notice ships | high |
| Embedded metadata | `kc.mp3` carries an ID3 `TXXX:prompt` frame (8,197 bytes): the full ComfyUI graph - model filenames, seed 3327, the 4,120-character caption, the 2,722-character lyrics, cfg 1.7, 30 steps. No drive paths, usernames or emails found (searched `C:\`, `D:\`, ComfyUI) | publishes the exact prompt; doubles as provenance and machine-generated proof (Degenerative Pixels publishes its prompts) | high (parsed locally) |
| Repo size | 4,631,923 bytes, under GitHub's 50 MB warning | none | high |

## 6. Options

| option | what it does | rights posture | effect |
|---|---|---|---|
| **A (recommended)** ship full `audio/kc.mp3` + `audio/LICENSE.md` under CC BY 4.0 scoped "to the extent any rights exist" | repo renders out of the box; anyone may reuse the song with credit | honest in both countries; attribution enforceable where rights exist (lyric edits, Israeli recording right) | Content ID registration by others barred by YouTube's own rule; provenance and AUP disclosure travel with every credited copy |
| A-variant: same file, CC0 | public-domain dedication of any rights | honest; matches CC's advice for low-human-creativity works | drops attribution and the disclosure chain; irrevocable |
| B ship full mp3, "all rights reserved, included only to render the video" | Neel Nanda / raiscan model | overclaims in the US; may hold in Israel | blocks nothing in practice in the US; reads as stronger than the law supports |
| C link to YouTube only, ship no audio | upstream-fork model (lycfyi) | no statement needed | engine does not render KC from a fresh clone; contradicts Idi's ruling |
| rejected: low-bitrate preview | a 64 kbps copy is the same work in law | identical rights status | worse fidelity, zero legal gain |

Recommendation: **A**. Reasons: (1) no MiniMax text restricts it, and AUP 11 is met by the notice; (2) CC BY is the most accurate scope for a mixed human/machine work per CC's own guidance; (3) a CC licence makes the song ineligible for anyone's Content ID registration under YouTube's rules, the main practical threat; (4) attribution carries "machine-generated with MiniMax-Music3" downstream, keeping MiniMax's disclosure condition alive in copies; (5) matches the precedent class (pdoom forks ship the file with a separate audio notice). Keep the embedded ComfyUI prompt frame: it is the strongest machine-generated receipt and holds no personal data. If Idi wants to bar commercial reuse by others, swap to CC BY-NC 4.0 (the nonunsaram model); cost: blocks remixers who monetise, and "NC" is unenforceable wherever no right exists.

Placeholders for Idi's ruling: `<HOLDER>` (licence-holder name, open since audit D1), `<CHANNEL>` (YouTube channel name).

Draft `audio/LICENSE.md`:

```
# Knowledge Cutoff - song audio and lyrics

Files: audio/kc.mp3, data/lyrics.json, data/pitch.json, data/audio.json, data/asides.json

## Machine-generated content
The music and vocals in audio/kc.mp3 are machine-generated. They were produced locally
with the open weights of MiniMax-Music3 (https://huggingface.co/MiniMaxAI/MiniMax-Music3),
from a text description and lyrics, take seed 3327, with no audio edits.
The lyrics were drafted with Claude (Anthropic) and selected and edited by <HOLDER>.
The full generation settings are embedded in the mp3's metadata (ID3 TXXX "prompt").

Credit: MiniMax-Music3.

## Licence
To the extent that any copyright or related rights exist in these files, they are licensed
by <HOLDER> under the Creative Commons Attribution 4.0 International licence (CC BY 4.0):
https://creativecommons.org/licenses/by/4.0/

Parts generated entirely by a machine may carry no copyright in some countries.
Nothing here claims rights that do not exist.

Suggested attribution:
"Knowledge Cutoff" by <HOLDER> (https://youtu.be/-g6hYVec1Uo), machine-generated with
MiniMax-Music3, CC BY 4.0.

If you share this audio publicly, keep the machine-generated notice with it.

## Not covered
The code in this repository is under the MIT licence (see LICENSE). The MiniMax-Music3
model is under its own community licence and is not included here. The music video
on YouTube (<CHANNEL>) is not covered by this file.
```

Companion line for README Licence section: "The song audio and lyric data (`audio/`, `data/lyrics.json`, `data/pitch.json`, `data/audio.json`, `data/asides.json`) are excluded from MIT and covered by `audio/LICENSE.md` (CC BY 4.0, to the extent rights exist; machine-generated with MiniMax-Music3)."

Sources (all read 2026-11-02 unless marked):
- https://huggingface.co/MiniMaxAI/MiniMax-Music3/raw/main/LICENSE (7,373 bytes, md5 a5a2f8ab80aa45ad33584f702512f8e6)
- https://huggingface.co/api/models/MiniMaxAI/MiniMax-Music3/commits/main
- https://github.com/MiniMax-AI/MiniMax-Music3
- https://platform.minimax.io/protocol/terms-of-service
- https://www.minimax.io/audio/doc/terms-of-service.html
- https://www.minimax.io/audio/doc/terms-of-service-music.html
- https://www.minimax.io/terms-of-service-v2.html
- https://platform.minimax.io/docs/guides/music-generation
- https://mer.vin/news/minimax-music-3-is-open-weight-but-not-open-for-business/
- https://help.suno.com/en/articles/2416769 ; https://suno.com/terms
- https://www.udio.com/terms-of-service (UNREAD)
- https://stability.ai/community-license-agreement ; https://huggingface.co/stabilityai/stable-audio-open-1.0 (UNREAD, gated)
- https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B
- https://github.com/multimodal-art-projection/YuE (main and YuE-v1 branch, MODEL_LICENSE)
- https://ai.google.dev/gemini-api/terms
- https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform
- GitHub repos in section 3 (API reads)
- https://www.copyright.gov/ai/ and the Part 2 PDF
- https://media.cadc.uscourts.gov/opinions/docs/2025/03/23-5233.pdf
- https://www.wipo.int/wipolex/en/text/202010
- https://www.anthropic.com/legal/consumer-terms
- https://creativecommons.org/2023/08/18/understanding-cc-licenses-and-generative-ai/
- https://support.google.com/youtube/answer/2605065
- https://www.eff.org/deeplinks/2018/03/ten-hours-static-gets-five-copyright-notices
