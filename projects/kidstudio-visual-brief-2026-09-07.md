---
type: note
created: 2026-09-07
author: jep
project: tutoring
status: active
---

# Studio v6: visual overhaul brief (2026-09-07, 11:20)

Scope per Idan: aesthetics only, no feature changes, maximal wow. Two research agents ran in sequence (web only, nothing downloaded): inspiration and art directions, then implementable techniques. Both reports are appended verbatim below. "V" = verified on the source page, "I" = inferred.

## Four art directions (from the inspiration report, condensed)

| | Look | Palette | Type (all OFL, Google Fonts) | Signature | Risk |
|---|---|---|---|---|---|
| A | Comic print (Spider-Verse) | paper #FFF6E5, ink #14121A, cyan, magenta, yellow | Bangers, Shantell Sans, Comic Neue | CMYK misregistered titles snapping into register, halftone dots, result stage = comic panel with a "WHAM" sticker | small type must stay solid; light page changes the TV-room feel |
| B | Ink (Splatoon) | ink black #1B1B22, K pink #FF3FA4, D lime #A6FF2E, orange, purple | Titan One, Luckiest Guy, Baloo 2 | ink splats, boxes fill with ink when a word lands, ink wipe reveals in her color | SVG splat filters per frame are heavy; pre-render 6 splat shapes |
| C | Glass and aurora (Siri glow) | ground #0B0D1A, violet, cyan, pink, amber | Fredoka, Nunito, Space Grotesk | screen-edge hue glow while cooking, frosted panels that clear as the result forms | "same page, new gradient" |
| D | Paper craft and stickers (Pok Pok, Toca) | paper #FFF8EC, kraft, coral, teal, yellow, violet | Chewy, Shantell Sans, Patrick Hand | cut-paper layers, stickers peel on hover, rubber-stamp press, one quirky mascot | reads preschool to a 12-year-old |

## Recommendation: B, "Ink in water", dark variant

Why B over the agent's pick of A: the girls already own pink and green; ink color per girl maps onto that identity one to one, where comic print gives both girls the same CMYK. The single most jaw-dropping technique in the catalogue is the WebGL fluid simulation (ink swirling in water, reacting to the pointer with no drag, MIT, single file), and it belongs to an ink direction. Dark ground keeps the TV-room look Idan approved yesterday and keeps big white words at high contrast.

What she sees:

1. Ground: the fluid simulation in her ink color plus one secondary, at half resolution, slow, paused while she types (motion cap from the evidence list).
2. Title and labels: Titan One with a sticker stroke (`paint-order: stroke fill`), per-letter spring-in on load with a `linear()` spring; Baloo 2 for chips and words.
3. Panels: three glass panels max (ingredients, stage, words), blur under 20 px, grain overlay at 6 %, dark scrim under every text block.
4. GO: claymorphism button in her ink, squash on press, spring release, magnetic lean capped at 12 px.
5. Chips: staggered entrance 30 ms apart; selected chip lit, the rest dimmed (Persona 5 rule); signposts stay dashed.
6. Cooking: a goo-filtered blob in her ink with a conic progress ring inside; the screen edge glows in her color (Siri pattern) while the model works.
7. Reveal: ink wipe in her color (mask wipe) then a 1.5 s Polaroid develop, once; view transition morphs the stage between states.
8. Audio: radial visualizer with a bass-pulsing center disc; song result makes the panels bob on the beat (Hi-Fi Rush, subtle).
9. Movie: cinema curtain opens, letterbox, vignette, grain.
10. Sounds: ZzFX tap, confirm, error, success, with pitch jitter and an 80 ms rate limit; hover silent.
11. Milestone: one full-screen transformation, canvas-confetti stars and emoji fireworks for 3 s, only at milestones (Duolingo rule; confetti on every result is dropped to a small burst).
12. Guardrails: 56 px chips, 96 px GO, 24 px chip type, contrast 4.5:1 on every text block, `prefers-reduced-motion` swaps springs for fades and pauses the fluid.

Kept from v5: every feature, every layout region, the per-girl color, the milestone list, the counter.

## Build plan

| Step | What | Time |
|---|---|---|
| 1 | Copy `index.html` to `index-v6.html`, serve at `/v6`; the live page stays untouched | 5 min |
| 2 | Fonts (Google Fonts link, OFL), ground fluid sim vendored inline, palette tokens, glass panels, grain | 45 min |
| 3 | Type: sticker stroke, letter spring-in; chips, GO clay, magnetic lean, stagger | 45 min |
| 4 | Cooking blob + ring + edge glow; ink wipe + Polaroid reveal; view transitions | 45 min |
| 5 | Radial visualizer, beat bob, cinema curtain, ZzFX set, confetti milestone | 45 min |
| 6 | Screenshots of every tab in both colors, 60 fps check in Edge devtools, contrast check, then swap `/` to v6 | 30 min |

About 3.5 hours. Safe to run during or after the 14:00 session because nothing touches the live file until step 6.

## Options

A. Build B "Ink in water" now in `index-v6.html`; preview at `/v6` whenever you want; swap after the session.
B. Same, but direction A "Comic print" (the agent's pick).
C. Wait for your notes after the session, then build.

Say the word: A, B, or C, plus any direction from the table if you want a mix (the type and motion stack fits all four).

## Report 1: visual inspiration (agent, verbatim)

# Visual inspiration report: Kid Studio overhaul

## Section 1. Inspiration sources

| Example | URL | The stunning thing | Maps onto | V/I |
|---|---|---|---|---|
| Messenger (abeto), Awwwards Site of the Year 2025 | https://messenger.abeto.co and https://www.awwwards.com/sites/messenger | Two-color world (#81BFBC, #C9D5C3), one cheerful character, everything else silent. Restraint makes the motion read. | Stage: one calm ground color so the result is the only loud thing. Animation score 9.0/10 on Awwwards. | V |
| Lando Norris (OFF+BRAND), Site of the Year 2025 | https://www.awwwards.com/sites/lando-norris | Two colors only: neon lime #D2FF00 on near-black #111112. Bold two-color scheme carries the whole identity. | Per-girl accent: one accent + black, no rainbow. GO button in pure accent. | V |
| Igloo Inc (abeto), Site of the Year 2024 | https://www.awwwards.com/sites/igloo-inc | Grey-on-charcoal (#b6bac5, #383e4e) with transitions scoring 9.6/10 for animation. Motion carries a palette that is almost mute. | Stage transitions: rely on motion quality, less on color. | V |
| Umami Land (Google, Monks), Dev Site of the Year 2021 | https://www.awwwards.com/sites/umami-land | 2D illustration + 3D elements, palette #2779a7, #49c5b6, #ECD06F. Jury: playful animation blended with sound and world. | Filmstrip as a small theme park: each frame a ride car that rolls in. | V |
| Lusion v3, Site of the Year 2023 | https://lusion.co | White space, huge type, 3D storytelling. "We do not chase trends." | Header: giant type, one 3D object, nothing else. | V |
| Mat Voyce, kinetic type portfolio (2026 awards roundup) | https://matvoyce.tv | Letters stretch, snap, recombine on scroll without blocking readability. | Ingredient boxes: the typed word springs and settles in place. | V (via https://www.hontran.dev/blog/best-award-winning-websites-2026) |
| Spider-Verse title sequence (Art of the Title) | https://www.artofthetitle.com/title/spider-man-into-the-spider-verse/ | "Kirby dots and halftones, graffiti and street slaps", color offsetting and overprinting, spray-paint layer on everything, 3D rendered then treated to feel illustrated. | Whole-page art direction A below. Result stage = comic panel. | V |
| Persona 5 UI (Persona Central panel) | https://personacentral.com/persona-5-panel-concept-development-ui/ | Red + black + white, sub-colors removed so red dominates. White lines guide the eye. Lit vs dimmed areas encode priority. Goal: UI "intuitive and casually guiding" where casual means playful. | Option chips: the selected chip is lit, the rest dimmed. Word panel: one line leads the eye down the list. | V |
| Super Mario Bros. Wonder, Wonder Effect | https://www.mariowiki.com/Wonder_Effect | On trigger: wavy distortion at screen corners, background changes, blocks turn magenta, coins dance to music, voices shout "Won-der!". | Cooking state and reveal: the whole page warps at the corners while the result cooks. | V |
| Splatoon 3 UI | https://www.gameuidatabase.com/gameData.php?id=1512 | Ink splat wipes, thick sports-brand type, per-team ink color across HUD. | Art direction B. Per-girl ink color replaces per-girl neon. | I (Game UI Database blocked fetch) |
| Hi-Fi Rush | https://interfaceingame.com/games/hi-fi-rush/ and https://unwinnable.com/2023/07/21/in-hi-fi-rush-style-is-substance-165/ | Every UI element pulses on the music beat; onomatopoeia on every action; 2D cutscenes flow into 3D. | Song result: the whole stage bobs on the beat of the generated song. | I |
| Sable | https://www.gameuidatabase.com/gameData.php?id=1183 | Moebius ligne claire: clean uniform lines, flat warm color, no hatching. | A calmer fallback direction for the 12-year-old. | I |
| Pok Pok Playroom, Apple Design Award 2021 | https://www.sketch.com/blog/pok-pok/ | Whole app on 11 colors + white. Hand-drawn, no text, "if a child gets stuck, we've made a mistake." | Palette discipline for any direction: cap at 12 colors. | V |
| Toca Boca (Motionographer interview) | https://motionographer.com/2016/04/27/the-design-process-behind-toca-bocas-infectious-apps/ | "Things shouldn't be too perfect, there is still dirt in the corners, and there is always a weird, quirky element." Flat-shaded 3D. | One quirky idle character per screen (a mascot that reacts to typing). | V |
| Duolingo streak milestone animation | https://blog.duolingo.com/streak-milestone-design-animation/ | Full-screen custom animation fires only on milestone days. One transformation (Duo becomes a phoenix), rehearsed in rough passes for rhythm. | Milestone banner: replace the banner with a single full-screen transformation, reserved for milestones. | V |
| Blob Opera (Google Arts & Culture, David Li) | https://experiments.withgoogle.com/blob-opera | Four blobs sing; drag up for pitch, forward for vowel. Sound has a face. | Spoken-sentence and song results: a blob mouths the words. | V |
| Spotify Wrapped 2024 | https://alexjimenezdesign.substack.com/p/three-design-elements-that-made-spotify | Bold type on flat colors only, numbers enlarged and repeated as pattern, 2 to 3 visual treatments max. | Word-count panel: the number as giant pattern type. | V |
| Apple Intelligence Siri edge glow | https://dev.to/vector4wang/i-recreated-iphones-apple-intelligence-edge-glow-effect-on-mac-57f5 | 20 hue segments around the screen edge, 4 stacked blur layers (halo, mid, core, center), flowing continuously. | Cooking state: the TV bezel glows in the girl's color while the model works. | V |
| Lost in Play, Apple Design Award 2024 | https://developer.apple.com/news/?id=n4w6zydm | "Like a Saturday morning cartoon", gibberish speech instead of text, camera shakes when scary. | Story result: camera shake and squash on frame changes. | V |

## Section 2. Four art directions

All 20 fonts below confirmed present on Google Fonts (V, https://fonts.googleapis.com/css2 query returned all). OFL.txt confirmed in the google/fonts repo for Shantell Sans, Fredoka, Bangers, Press Start 2P, Bungee (V); the rest sit in the same `ofl/` tree (I).

### A. Comic print (Spider-Verse)

| Palette | Fonts | Signature motion | Reveal | Celebration | Risk |
|---|---|---|---|---|---|
| Paper #FFF6E5, ink #14121A, cyan #00C2FF, magenta #FF2D95, yellow #FFE600, red #FF3B30 | Bangers (titles), Shantell Sans (ingredient text, variable), Comic Neue (captions) | CMYK misregistration: title layers sit 3px apart and snap into register on hover. Halftone dot pattern via CSS radial-gradient. | The stage is a comic panel; the border draws itself, the image drops in with a rotated onomatopoeia sticker ("WHAM"). | Full-bleed Kirby-dot flash, panel grid shatters into pages. | Misregistration on small type kills legibility. Offset titles only; ingredient words stay solid black. CSS techniques at https://blog.logrocket.com/5-ways-style-text-css-inspired-spider-verse/ (V). |

### B. Ink (Splatoon)

| Palette | Fonts | Signature motion | Reveal | Celebration | Risk |
|---|---|---|---|---|---|
| Ground #F4F1EA, ink black #1B1B22, girl 1 pink #FF3FA4, girl 2 lime #A6FF2E, orange #FF7A00, purple #6A1BFF | Titan One (display), Luckiest Guy (GO button), Baloo 2 (UI) | Ink splats: SVG blobs with feTurbulence + feDisplacementMap, boxes fill with ink when a word lands. | Ink wipe in the girl's color uncovers the result. | Whole screen splatted, ink drips down, filmstrip frames pop out of the drips. | SVG filters at 1920x1080 per frame; pre-render 6 splat PNGs and animate with CSS masks. Fonts: the real Splatoon font is custom (I, https://www.devzery.com/post/unlocking-the-creative-world-of-splatoon-fonts). |

### C. Glass and aurora (Siri glow)

| Palette | Fonts | Signature motion | Reveal | Celebration | Risk |
|---|---|---|---|---|---|
| Ground #0B0D1A, violet #7C4DFF, cyan #00E5FF, pink #FF4DA6, amber #FFB347, glass rgba(255,255,255,.08) | Fredoka (display, variable wdth/wght), Nunito (body), Space Grotesk (numbers) | Screen-edge glow, 20 hue segments, 4 blur layers (Apple pattern above). Frosted panels with backdrop-filter. No parallax. | Glass clears: blur goes from 24px to 0 as the result forms behind it. | Aurora sweep across the whole screen, slow, one pass. | Closest to the current look; danger of "same page, new gradient". backdrop-filter cost is fine on a 4090 but every panel adds a compositing layer. |

### D. Paper craft and stickers (Pok Pok, Toca)

| Palette | Fonts | Signature motion | Reveal | Celebration | Risk |
|---|---|---|---|---|---|
| Paper #FFF8EC, kraft #D9B98A, ink #2B2B2B, coral #FF6B6B, teal #4ECDC4, yellow #FFD93D, violet #6C5CE7 (7 + white, under the Pok Pok cap of 12) | Chewy (display), Shantell Sans (ingredients), Patrick Hand (captions) | Cut-paper layers with soft shadows; stickers peel on hover (Comeau boop: 150 ms, spring tension 300, friction 10, V https://www.joshwcomeau.com/react/boop/). Press = rubber stamp. | A paper card flips or unfolds to show the result. | Paper confetti with physics, a "WOW" sticker slaps on crooked. One quirky corner character (Toca). | Reads preschool to a 12-year-old. Keep shapes sharp and the mascot dry-humored. |

Recommendation: A for maximum wow with the girls' typed English words as the visual hero. B second. Say the word.

## Section 3. Motion and reveal patterns

| Moment | Pattern | Seen in | URL | V/I |
|---|---|---|---|---|
| Page load | Staggered entrance: header slams, boxes drop one by one, 80 ms apart; total under 1.2 s | Spider-Verse titles; Awwwards preloader convention (GSAP timelines) | https://www.artofthetitle.com/title/spider-man-into-the-spider-verse/ | V (titles), I (timing) |
| Hover | Boop: brief spring transform that resets itself | Josh Comeau | https://www.joshwcomeau.com/react/boop/ | V |
| Press | Scale to 0.94 then spring back; must start within 0.1 s | NN/g animation guidance | https://www.nngroup.com/articles/animation-usability/ | V |
| Selected chip | Lit vs dimmed, a white guide line to the selection | Persona 5 | https://personacentral.com/persona-5-panel-concept-development-ui/ | V |
| Cooking wait | Screen-edge hue glow flowing around the bezel | Apple Intelligence Siri | https://dev.to/vector4wang/i-recreated-iphones-apple-intelligence-edge-glow-effect-on-mac-57f5 | V |
| Cooking wait | Wavy corner distortion, background shifts, coins dance | Mario Wonder | https://www.mariowiki.com/Wonder_Effect | V |
| Image reveal | Bold type on flat color, number as pattern | Spotify Wrapped 2024 | https://alexjimenezdesign.substack.com/p/three-design-elements-that-made-spotify | V |
| Audio reveal | A blob with a mouth sings the line | Blob Opera | https://experiments.withgoogle.com/blob-opera | V |
| Song reveal | UI pulses on the beat | Hi-Fi Rush | https://unwinnable.com/2023/07/21/in-hi-fi-rush-style-is-substance-165/ | I |
| Video reveal | Camera shake and squash between frames | Lost in Play | https://developer.apple.com/news/?id=n4w6zydm | V |
| Milestone | Full-screen single transformation, only at milestones | Duolingo | https://blog.duolingo.com/streak-milestone-design-animation/ | V |

## Section 4. Evidence check

- NN/g, physical development: 2 cm x 2 cm touch targets for young children; desktop designs should need only clicks or simple keys; precise drag is hard under 9. V https://www.nngroup.com/articles/children-ux-physical-development/
- NN/g, animation: repeated animations turn into "now it's getting annoying"; feedback must begin within 0.1 s; kids are less goal-oriented so they tolerate decoration better. Confetti on every result is the repeat case. V https://www.nngroup.com/articles/animation-usability/
- Eye-tracking, 45 Swedish children aged 9 and 12: ads with abrupt onset pulled gaze most; smooth-onset ads drew fewer saccades than static ones; task accuracy stayed at 95.9%. Sparks and pop-in elements should ease in. V https://pmc.ncbi.nlm.nih.gov/articles/PMC3921552/
- Font size, Israeli 2nd and 5th graders (n=45 each): smaller type hurt 2nd graders (87% to 79%) and helped 5th graders at 13 pt. Size is no ceiling for 9 and 12. Big type still earns its place for second-language words. V study, I inference. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0074061
- Vestibular triggers: large-area movement, parallax, zoom, background moving against foreground; opacity and color changes are safe. The lava lamp and mouse sparks are background movement behind text. V https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/ and https://w3c.github.io/wcag21/understanding/animation-from-interactions.html
- Sesame Workshop: tap is the most intuitive gesture; make children finish listening before options light up. V https://appleinsider.com/articles/12/12/24/sesame-workshop-wants-to-improve-ipad-apps-for-kids-with-free-developer-guidelines
- Palette cap: Pok Pok ships on 11 colors + white. V https://www.sketch.com/blog/pok-pok/
- Not verified: Interface In Game, Game UI Database, Inkipedia and Creative Bloq all refused fetches (403 or truncated). Splatoon, Hi-Fi Rush and Sable rows rest on search snippets.

## Report 2: techniques (agent, verbatim)

# Visual overhaul techniques for Kid Studio

Target: single-file page, Edge on Windows 11, 1920x1080, RTX 4090, readers aged 9 and 12. Tags: V = read on the fetched page, I = inferred from search snippets or prior knowledge, not opened. Versions were checked on 2026-09-07.

## 1. Backgrounds

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| Raw WebGL fragment shader, flowing gradient | Organic aurora / lava-lamp colour field, dark or light by swapping the palette | Alex Harri's article walks through stacked simplex noise plus sine waves and links full GLSL: https://alexharri.com/blog/webgl-gradients | Trivial on a 4090; run it at half resolution on a canvas with `image-rendering` upscaling for free headroom | V |
| Plasma generator | Same idea with 28+ presets, exports a standalone HTML or JS file, MIT | https://plasma.nusaiba.dev/ tune colours, speed, warp, then Export HTML and paste the shader into the page | Vendor the exported code, no runtime dependency | V |
| WebGL fluid simulation | Ink-in-water fluid that reacts to pointer moves (no drag needed, mousemove is enough) | https://github.com/PavelDoGreat/WebGL-Fluid-Simulation MIT, `index.html` + `script.js`, demo https://paveldogreat.github.io/WebGL-Fluid-Simulation/ | Heaviest option here, still fine on a 4090; the dat.gui dependency is only for the demo panel, drop it | V |
| three.js from cdnjs | Full 3D scene: floating blobs, particles, a spinning "studio" set | `https://cdnjs.cloudflare.com/ajax/libs/three.js/0.185.1/three.module.min.js` (ES module via `<script type="module">` or importmap; cdnjs no longer ships a `three.min.js` UMD build at this version) | Learning curve highest; overkill for a background alone | V |
| Vanta.js | Prebuilt three.js backgrounds: waves, fog, birds, net, clouds, halo, globe | Pattern from vantajs.com: load `https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js` then `https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.[[effect]].min.js`, call `VANTA.WAVES({el:"#bg"})` | Pins an old three r134; the site says "don't use more than one or two per page"; pin a version instead of `@latest` | V |
| OGL | Minimal WebGL library, ES module | `https://cdn.jsdelivr.net/npm/ogl@1.0.11/src/index.js` (source tree only, no UMD bundle listed) | Smaller than three, fewer examples | V |
| p5.js | Canvas-2D or WebGL sketches, generative particles | `https://cdnjs.cloudflare.com/ajax/libs/p5.js/2.3.2/p5.min.js` | Global-mode p5 owns the canvas; fine for a background layer, slower than a raw shader | V |
| CSS mesh gradient with `@property` | Animated aurora with zero JS: several radial layers whose centre positions and hues are registered custom properties tweened by `@keyframes` | `@property --hue { syntax: "<angle>"; inherits: false; initial-value: 0deg }` then animate `--hue`; Baseline since July 2024 in Chrome/Edge 89+, Firefox 128+, Safari 16.4+ (MDN) | Large blurred layers repaint every frame; keep the gradient on one fixed layer with `will-change: background` | V |
| Houdini paint worklet | Procedural patterns (confetti, dots, doodles) painted per element | Chromium native since 65, Safari 16.4 partial, Firefox behind a flag; catalogue at https://houdini.how/ (polyfill served from unpkg, which the artifact CSP would block, but the local page has no CSP) | Edge-only page so native works; the worklet must be a separate file or a Blob URL, so "single file" needs `CSS.paintWorklet.addModule(URL.createObjectURL(new Blob([src])))` | V for status, I for the Blob trick |

## 2. Typography

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| Fredoka (display) | Rounded, chunky, friendly; variable `wght` 300 to 700 and `wdth` 75 to 125; OFL 1.1; includes Hebrew | `https://fonts.googleapis.com/css2?family=Fredoka:wdth,wght@75..125,300..700&display=swap` | Two axes means one file can do every headline trick below | V (axes via csstypestudio / Fontsource), I for exact API URL shape |
| Baloo 2 (display alt) | Heavier, bouncier, variable weight, OFL | https://fonts.google.com/specimen/Baloo+2 | Google specimen pages return no text to fetch tools; confirm axes in the download | I |
| Lexend (text) | Designed for reading speed, variable weight, OFL; Shaver-Troup research validated at Vanderbilt per the search summary, replication status unknown | https://fonts.google.com/specimen/Lexend | Wide letter spacing eats horizontal room in chips | I |
| Atkinson Hyperlegible Next (text alt) | Braille Institute font built for character distinction, seven weights, variable, OFL 1.1 | https://github.com/googlefonts/atkinson-hyperlegible-next | Less playful than Lexend, more distinct b/d/p/q for a 9-year-old | I |
| Nunito (text alt) | Rounded body text that pairs with Fredoka in most pairing guides | https://fontfoundryhub.com/best-fredoka-font-pairings-alternatives/ | Softer contrast at small sizes | I |
| Variable axis "breathe" | Headline letters swell and relax per character | CSS { In Real Life }: `@keyframes breathe { 60% { font-variation-settings: 'wght' 700, 'wdth' 100 } 100% { font-variation-settings: 'wght' 100, 'wdth' 85 } }` with `animation-delay: calc(var(--char-index) * 400ms)` https://css-irl.info/variable-font-animation-with-css-and-splitting-js/ | `font-variation-settings` triggers layout each frame; keep it on headlines only, never on a 16-chip row | V |
| Variable hover | Weight or width jumps on hover | https://codepen.io/michellebarker/pen/LYbYbGM, Mandy Michael collection https://codepen.io/collection/XqRLMb/ (her own note: heavy on the CPU) | Same layout cost | I |
| Split text without GSAP | Per-letter spring-in on load | Wrap each character in a `<span style="--i:N">` in JS, animate with `animation-delay: calc(var(--i) * 40ms)` and a `linear()` spring; Splitting.js does the wrapping if wanted | Wrap words with `display:inline-block` so lines still break; add `aria-label` on the parent so screen readers get one word | I |
| GSAP + SplitText | Industry-standard split and stagger, now free for commercial use including all plugins ("GSAP is now 100% free for all users, thanks to Webflow's support") | `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.15.0/gsap.min.js` then `https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js`; `SplitText.create(".title",{type:"chars"})` then `gsap.from(split.chars,{y:100,autoAlpha:0,stagger:0.05})` | cdnjs does not host SplitText; the second URL is jsdelivr | V |
| Extruded 3D text | Chunky toy-block headline | Stacked hard-edged shadows, 1px steps: https://codepen.io/dudleystorey/pen/waqwBg ; Mandy Michael's layered-font method https://codepen.io/mandymichael/post/editable-stacked-fonts-with-css | 20 stacked shadows on a long headline repaints slowly if animated; animate `transform` only | I |
| Sticker outline on text | White "print" outline behind the fill | `-webkit-text-stroke: 8px white; paint-order: stroke fill;` Baseline since March 2024 for HTML text (MDN) | Stroke width scales with font size, so set it in `em` | V |

## 3. Materials

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| Glass panel | Frosted card over the shader background | `backdrop-filter: blur(16px) saturate(160%)`, 1px border `rgba(255,255,255,.35)`, `box-shadow: inset 0 1px 0 rgba(255,255,255,.5)` | Blur is the priciest filter; keep radius under 20px on panels over 400px and hold at most 3 or 4 glass elements per screen; never animate the radius (Empire UI guide, https://empire-ui.com/blog/backdrop-filter-css) | I |
| Grain overlay | Film / paper texture that kills the flat plastic look | Inline `<svg><filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/></filter></svg>` on a fixed `::after` at 4 to 8% opacity with `mix-blend-mode: overlay` https://css-tricks.com/grainy-gradients/ | Render once (static), never animate the turbulence seed each frame | V |
| Claymorphism buttons | Soft inflated 3D buttons that read as toys, the best fit for the GO button | One outer shadow plus two insets: `box-shadow: inset 10px 10px 40px rgba(255,255,255,.7), inset -10px -10px 40px rgba(0,0,0,.15), 20px 20px 60px rgba(0,0,0,.1); border-radius: 48px` https://superdesign.dev/styles/claymorphism generator https://hype4.academy/tools/claymorphism-generator | Big inset blur radii repaint on every state change; use `transform: scale()` for press, keep shadows static | I |
| Neumorphism caution | Same-colour embossing | Skip: low contrast by design, fails the 3:1 large-text floor on most palettes | none | I |
| Paper sticker cutout on images | White die-cut edge plus drop shadow around the generated image | SVG `feMorphology operator="dilate" radius="6"` then `feFlood` white, `feComposite in`, `feMerge` under the source (Codrops https://tympanus.net/codrops/2019/01/22/svg-filter-effects-outline-text-with-femorphology/), plus `filter: drop-shadow()` | Filter reruns on resize only; cheap | V for technique via search, I for exact values |
| Halftone / Ben-Day dots | Comic-print overlay for the "Comic" style | `background: radial-gradient(closest-side,#000,#fff) 0/1em 1em space` plus `filter: contrast()` ("3 declarations") https://frontendmasters.com/blog/pure-css-halftone-effect-in-3-declarations/ ; https://codepen.io/salt/pen/BQYrjR | Static, cheap | I |
| CRT scanlines + RGB split | Retro TV frame for the video stage | Scanlines `repeating-linear-gradient(0deg, transparent 0 2px, rgba(0,0,0,.25) 2px 4px)`; aberration = two coloured `text-shadow` or pseudo copies offset 2px red / cyan https://codepen.io/fand/pen/EgGwjg , https://aleclownes.com/2017/02/01/crt-display.html | Keep it a one-shot on reveal, not a permanent overlay, or the girls cannot read | I |
| Goo filter | Blobs and buttons that merge like liquid (cooking state, loading dots) | `<filter id="goo"><feGaussianBlur stdDeviation="10" result="blur"/><feColorMatrix in="blur" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 18 -7" result="goo"/><feComposite in="SourceGraphic" in2="goo" operator="atop"/></filter>` applied to the container https://css-tricks.com/gooey-effect/ | Apply to a small container with padding for bleed; the article warns it is resource intensive on large areas | V |

## 4. Motion

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| View Transitions (same document) | Crossfade or morph between studio state, cooking, and result with one call | `document.startViewTransition(() => swapDOM())`; give the result frame `view-transition-name: stage` so it morphs; style `::view-transition-old(stage)` / `::view-transition-new(stage)` (MDN). Supported Chrome/Edge 111+, Safari 18+, Firefox 144+ | Snapshots a static image of old state, so keep shader canvas out of named groups; Level 2 features vary by browser | V for API, I for versions via caniuse search |
| `linear()` easing springs | Real bounce and overshoot without JS | Generator https://linear-easing-generator.netlify.app/ presets Spring, Bounce, Elastic; supported Chrome/Edge 113+, Firefox 112+, Safari 17.2+ | Paste the generated list into a `--spring` custom property once | V |
| Overshoot bezier | One-line juice | `cubic-bezier(0.18, 0.89, 0.32, 1.28)` overshoots about 28%; `cubic-bezier(0.22, 1, 0.36, 1)` "plants" (fast in, long brake) | Overshoot on `transform` only | I |
| Squash and stretch on press | Toy feel on tap | `:active { transform: scale(1.05, .92) }` then release keyframe to `scale(.99, 1.02)` then `1` | Use `transform-origin: bottom` so it squashes on the ground | I |
| Anime.js v4 | Timelines, springs, stagger helpers in one 4.5.0 UMD | `https://cdnjs.cloudflare.com/ajax/libs/animejs/4.5.0/anime.umd.min.js`; spring easing docs https://animejs.com/documentation/easings/spring/ | Lighter than GSAP if SplitText is not needed | V for URL, I for API |
| Wobble spring micro-library | Damped harmonic oscillator, about 1.7 KB gzip, `stiffness` default 100, `damping` default 10 | https://github.com/skevy/wobble (vendor the dist file) | Drive `transform` per frame from its `onUpdate` | I |
| Hand-rolled spring | Zero dependency | Per frame: `v += (-k*(x-target) - c*v)/m*dt; x += v*dt` with k 170, c 26, m 1 (Josh Comeau's article explains the three knobs, no code) https://www.joshwcomeau.com/animation/a-friendly-introduction-to-spring-physics/ | Clamp dt at 32ms so a tab switch does not explode | V for article, I for numbers |
| Staggered entrance | Chips cascade in on load | `animation-delay: calc(var(--i) * 30ms)` with a spring `linear()`; 16 voices x 30ms = under half a second | Set `animation-fill-mode: both` so chips do not flash | I |
| Magnetic hover | Buttons lean toward the cursor | mousemove on the button, translate the inner span by `(dx*0.3, dy*0.5)`, reset on mouseleave https://codepen.io/a7rarpress/pen/rNqMEjK | Cap at 12px so the tap target never runs away from a child's finger | I |
| Cursor effects without drag | Sparkle trail or fluid ink following the pointer | Fluid sim above reacts to mousemove; or a canvas trail of 20 fading dots | Touch has no hover, so this is mouse-only sugar | I |
| Cooking: liquid fill | The GO button or a pot fills up as progress runs | `@property --p { syntax:"<percentage>" }`, `background: linear-gradient(0deg, var(--fill) var(--p), transparent 0)`; wave top via an SVG path animated with `translateX` | Progress is JS-driven, so set `--p` from the timer, no keyframes needed | V for `@property` example (MDN) |
| Cooking: progress ring | Conic ring with animated percentage, single element | `conic-gradient(var(--c) 0 var(--p), #eee var(--p) 100%)` with `@property --p` https://www.pyxofy.com/css-animation-property-and-conic-gradient-animation/ | Mask the centre with `mask: radial-gradient(...)` | I |
| Cooking: morphing blob | Goo dots merging under the goo filter, colour cycling | goo filter above + three bouncing circles | Keep the filtered box small (200px square) | V |
| Reveal: circle wipe | Result irises open from the centre | `clip-path: circle(0% at 50% 50%)` to `circle(75%)` over 600ms | GPU composited, cheap | I |
| Reveal: blur to sharp / Polaroid | Image "develops" | `filter: blur(20px) sepia(1) brightness(1.4)` to `none` over 1.5 s https://codepen.io/juancroldan/pen/vYVLYBx | Blur animation is expensive; limit to one image, 1.5 s, once | I |
| Reveal: mask wipe | Diagonal soft-edged wipe | `mask-image: linear-gradient(110deg, #000 40%, transparent 60%)` with `mask-size: 300% 100%` animated via `mask-position` | Cheap | I |
| canvas-confetti | Bursts, fireworks, stars, emoji | `https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.4/confetti.min.js` (jsdelivr equivalent `https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.4/dist/confetti.browser.min.js`). Burst: `confetti({particleCount:150, spread:70, origin:{y:.6}})`. Stars: `shapes:['star'], scalar:1.4`. Emoji: `shapes:[confetti.shapeFromText({text:'🌟', scalar:2})], scalar:2`. Fireworks: a `requestAnimationFrame` loop firing from `origin:{x:0}` and `{x:1}` with `angle:60` / `120` for 3 s | Own canvas layer, cheap; call `confetti.reset()` when the milestone closes | V |
| Scroll-driven animations | Gallery cards fade and rise as the grid scrolls | `animation-timeline: view(); animation-range: entry 0% entry 40%` (MDN) | Edge supports it; only the gallery scrolls, so limited use | V for syntax, I for support |

## 5. Sound and feel

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| ZzFX | Under 1 KB MIT synth for tap, confirm, error, whoosh; sounds designed in a browser tool and stored as one number array each | `https://cdn.jsdelivr.net/npm/zzfx@1.3.2/ZzFXMicro.min.js` or paste ZzFXMicro inline; designer https://killedbyapixel.github.io/ZzFX ; call `zzfx(...[,,925,.04,.3,.6,1,.3,,6.27,-184,.09,.17])` | Chiptune character; suits a kid studio | V |
| Hand-rolled Web Audio | Cleaner "soft" UI sounds: sine tap at 880 Hz for 60 ms with exponential decay; success = three sine notes C5 E5 G5 at 90 ms spacing; error = square 220 Hz to 180 Hz slide | One `AudioContext`, `OscillatorNode` + `GainNode`, `gain.exponentialRampToValueAtTime(0.0001, t+dur)` (MDN Web Audio basics, https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) | Browser autoplay policy: create or `resume()` the context inside the first click handler | I |
| Anti-annoyance rules | Sounds stay fresh | Randomise pitch by ±4% and gain by ±10% per play; keep 3 variations per action and rotate; rate-limit taps to one per 80 ms; mute chip hovers entirely (sfxengine.com, asoundeffect.com game-audio guides) | The guides give the principles; the numbers are my starting values | I |
| Haptic-like visual feedback | Every sound pairs with a 120 ms scale pulse so the sound is never the only cue | CSS as in section 4 | Needed for muted sessions | I |

## 6. Audio visualizer and video presentation

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| AnalyserNode basics | Frequency and waveform arrays each frame | `analyser.fftSize = 2048; getByteFrequencyData(arr)` for bars, `getByteTimeDomainData(arr)` for the ribbon (MDN visualizations page) | One analyser per `<audio>` via `createMediaElementSource`, connect it back to `destination` or the audio goes silent | V |
| Circular / radial bars | Bars radiate from a centre disc that pulses with bass (bins 0 to 8) | https://codepen.io/wrtchd/pen/aOGJEr and https://codepen.io/MyXoToD/pen/JYJGvG | Draw 64 bars at most, `ctx.rotate` per bar | I |
| Waveform ribbon | Smooth oscilloscope line, glow via `ctx.shadowBlur` | MDN draw loop divided by 128 to normalise | `shadowBlur` is slow; fake glow by drawing the line twice at two widths and alphas | V for loop, I for glow tip |
| Particle reaction | Particles burst on bass hits | Sum bins 0 to 8; if above a threshold that adapts (running average x 1.4), spawn 20 particles | Cap live particles at 400 | I |
| Lyrics / captions | Karaoke fill word by word | `background-clip: text` with a gradient whose stop moves per word, delay per word https://codepen.io/trongthanh/pen/dyRLmo | Word timing must come from the TTS output or be estimated from length | I |
| Cinema frame | Curtain, letterbox, vignette, grain, flicker on play | Curtain: two panels `translateX(-100%)` / `(100%)` over 1.2 s https://codepen.io/zuyie/pen/oLgQPL ; letterbox `aspect-ratio: 21/9` bars; vignette `box-shadow: inset 0 0 120px rgba(0,0,0,.6)`; grain from section 3; one-shot scanline flash from section 3 | All static after the intro | I |

## 7. Performance and legibility guardrails

| Technique | What it gives | How | Cost or risk | V/I |
|---|---|---|---|---|
| Composite-only animation | 60 fps | Animate `transform`, `opacity`, `clip-path`, `mask-position` only; never `box-shadow`, `filter: blur()`, `width`, `top`, `font-variation-settings` on more than a headline | The Polaroid blur is the one deliberate exception | I |
| backdrop-filter budget | No frame drops on the glass | Max 3 to 4 glass panels visible, blur under 20px, never animated (Empire UI) | Falls back to `background: rgba(255,255,255,.75)` if `@supports not (backdrop-filter: blur(1px))` | I |
| Layout thrash | Smooth JS | Batch reads then writes; use `ResizeObserver` for the visualizer canvas size; use `requestAnimationFrame` for all pointer-driven transforms | | I |
| Canvas sizing | Sharp shader and visualizer | Set `canvas.width = clientWidth * devicePixelRatio` once; the shader background may run at 0.5x and upscale | | I |
| `prefers-reduced-motion` | Respect the OS switch | `@media (prefers-reduced-motion: reduce)` swap springs for 200 ms fades; JS `matchMedia("(prefers-reduced-motion: reduce)").matches` pauses the shader and confetti (MDN pattern: reduce, do not remove) | | V |
| Contrast | WCAG 2.2 AA 1.4.3: 4.5:1 normal text, 3:1 large text (18 pt / 24 px regular or 14 pt / 18.5 px bold); AAA 1.4.6: 7:1 normal, 4.5:1 large | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html ; white on the glass over a busy shader needs a dark scrim behind text, or a 2 px sticker stroke | Check text over the moving background at its lightest frame | V |
| Tap targets | NN/g: minimum 1 cm x 1 cm (about 38 px at 96 dpi), larger for children; the Target app used 2 cm buttons | https://www.nngroup.com/articles/touch-target-size/ ; on this 1080p screen use 56 px chips minimum, 96 px GO, 8 px gaps | WCAG 2.5.8 minimum is 24 px, 2.5.5 enhanced is 44 px (I) | V for NN/g |
| Type size floor | Readable by a 9-year-old at arm's length from a monitor | 20 px body, 24 px chips, 40 px+ counters, 72 px+ title | | I |
| Motion cap | No nausea, no distraction during reading | Background shader speed low (a full colour cycle over 20 s or more), pause it while the girls type in the ingredient boxes | | I |

## Top 12 for this page, ranked by wow per hour

1. Fredoka `wdth,wght` variable headline with per-letter spring-in and sticker `paint-order` stroke. One font, three effects.
2. Plasma-exported raw WebGL aurora background, half-resolution canvas, palette per style chip.
3. Claymorphism GO button with squash-and-stretch press and a `linear()` spring release.
4. canvas-confetti milestone: star burst plus emoji shapes, fireworks loop for 3 s.
5. `@property` conic progress ring inside a goo-filtered blob for the cooking state.
6. Circle-wipe plus Polaroid develop for the result reveal (blur once, 1.5 s).
7. Glass panels with grain overlay, capped at three per screen, dark scrim under text.
8. ZzFX tap / confirm / success / error with pitch jitter and an 80 ms rate limit.
9. View Transitions between studio, cooking, and result with a named `stage` morph.
10. Radial visualizer with bass-pulsing centre disc and a fake-glow waveform ribbon.
11. Cinema curtain plus letterbox and vignette for the movie stage.
12. Staggered chip entrance and magnetic hover capped at 12 px.

Skipped on purpose: three.js scenes (hours for little extra over a shader), Houdini worklets (Blob-URL hack for single file, Edge-only benefit), neumorphism (contrast), permanent CRT overlay (legibility).
