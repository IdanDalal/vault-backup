---
type: project-brief
created: 2026-08-22
author: jep
project: tutoring
status: in-progress
---

# 3D Game — Playtest 1 friction list + upgrade plan (Sat 2026-08-22 evening)

Idan's first human playtest of the complete A+B+C build. Companion to [[tutoring-game-3d-verbs]] and [[tutoring-game-3d-brief]]. This note is the START-HERE for the next build session (fresh conversation). Master: `~/game3d/island.html`; sources `~/game3d/src/`; build `node ~/game3d/tools/build.mjs`; probes `~/render-tools/{gauntlet3d,slicec3d,persist3d}.mjs`.

## Friction list (Idan, verbatim intent) + status

1. **Story circle underwater** — FIXED same evening: placement scan now requires height 2–3 above water plus a dry 5×5 ring, with a grassy near-base fallback. Probe-verified dry. It landed close to the plaza; redistribute when the island grows.
2. **Island too small** — accepted for next session: grow 96×96 → 128×128 or 160×160 (laptop is primary target; chunk count scales fine). Redistribute biomes, words, structures with more breathing room.
3. **Text layering law (Idan's ruling):** in-universe text gets real 3D presence (carved/painted/engraved on world objects, perspective-correct); meta-text lives on the stylized 2D screen plane. Current sprite billboards violate this. Research agent dispatched (3D text techniques: embedded subset fonts + TextGeometry, world-anchored canvas planes, troika/MSDF, voxel letters, decals). Digest will be appended below.
4. **Capitalization system** — one coherent ruleset needed; three styles currently coexist ("Green Forest" / "cat" / "GREEN"). K & D are Hebrew L1 (caseless), so case is pedagogy, and rules need justification. Research agent dispatched (lowercase-first literacy evidence, caseless-L1 learners, kids' reading apps' practice, keyboard-caps confusion). My starting proposal to validate: word cards/labels/book cards lowercase; sentences with true sentence capitalization; names and place-set names capitalized as proper nouns; decorative UI smallcaps allowed as meta-text register only.
5. **Visuals need a lot of work** — Idan: currently closer to the stock-Minecraft negative anchor than the Townscaper positive one. Specific indictments: (a) flower sprites blurry with semi-transparent square halos (alpha/filtering bug — alphaTest fix likely) and repetitive; (b) prop geometry "one abstraction level from a toddler's doodle" (snake, garden flowers barely recognizable); (c) flat prototype-editor look — wants shadows/materials/advanced effects; inspiration source he named: 2026 modded-Minecraft shader screenshots (path-traced as north star, simpler shader mods as the realistic tier); (d) static floaty world — wants wind and dynamic motion. TWO research agents dispatched: shader/lighting upgrades (shadow maps now allowed: laptop primary!) and procedural detail + animation (better low-poly creatures, instanced vegetation, vertex-shader wind, water waves, ambient life). Digests will be appended below.

## Standing context for the next session

- The no-timers law, the no-dead-sentences law ("The sun is red" changes the actual sun), untimed catch, grow-only stakes: all remain binding.
- Art contract in [[tutoring-game-3d-brief]] still governs palette/fog/ACES; the phone-first perf ceilings (no shadow maps, no antialias) are RELAXED because the laptop is the primary target now — revisit each ceiling deliberately, keep the phone rescue ladder as degrade path.
- Rate budget: Idan authorizes pushing limits hard through Sunday; game must be ready Monday 2026-08-25 morning.
- Verification ritual unchanged: every visual change passes the screenshot gauntlet vs the calibration anchors before claiming quality; sky/fog/exposure/materials = one owner per pass.

## Research digests

### Digest 4/4 first: Capitalization ruleset (agent returned 2026-08-22; evidence-graded)

Master principle: **case is information, never decoration, in any text a child reads or types.** Capitals appear exactly where English grammar puts them so the girls (Hebrew L1 = caseless, so every exposure teaches) can induce the rules.

Evidence base, graded: lowercase-first is mainstream literacy practice (~90–95% of running text is lowercase; phonics + Montessori convention — solid). ALL-CAPS "inherently harder" via word-shape/bouma is DEBUNKED (Larson/Microsoft: parallel letter recognition; the 5–10% caps reading penalty is a practice effect) — but the practice-effect argument itself says beginners should train on lowercase forms, so the design conclusion survives the debunking. Reading-focused kids' apps converge on lowercase words + sentence-case sentences (Teach Your Monster, Starfall, Duolingo ABC; Endless Alphabet's all-caps is criticized and its reading-focused sequel switched to lowercase). Uppercase keycaps → lowercase glyphs is a real documented kid confusion (thin evidence, cheap mitigation: show lowercase targets; typing programs all do). Teaching sequence for capitals: sentence-first-word → people's names → I → proper nouns/places; model in real sentences.

The rules (each traceable to the above):
1. World word cards: lowercase ("cat").
2. Catch typing slots: lowercase, identical to the card. **The current ALL-CAPS displays are the one thing that must go.** Optional: one-time keycap hint teaching A→a mapping.
3. Garden labels: lowercase.
4. Word-book headwords lowercase; example sentences sentence case + period.
5. Signposts: Title Case ("Green Forest") — CORRECT as-is: place names are proper nouns; the signpost MODELS the rule. Optional teaching moment: "capital G because it's the forest's name, like your name."
6. Workbench sentences: sentence case; auto-capitalize first word + supply period now, make choosing the capital a challenge knob later (opinion, no research either way).
7. Story books: normal sentence case throughout (their model of authentic print).
8. Bot name tags: Capitalized names (free repetitions of the names rule for caseless-L1 kids).
9. Decorative UI chrome: small-caps allowed as a separate meta-register, used sparingly; NO collectible/typable vocabulary may ever appear in it (synthesis, untested, matches Starfall/Duolingo menu practice).

Net change: word cards and signposts stay as-is (now justified); kill all-caps in catch UI + anywhere vocabulary renders; enforce sentence case in built sentences and books.

### Digest 1/4: Shader/lighting upgrades (agent returned 2026-08-22)

Minecraft-pack meta-lesson (Photon/Complementary/BSL/Bliss feature surveys): **shadow + water + grade** are the three effects everyone credits; palette and motion separate tech-demo from cozy. Ranked build order (effect → key implementation → est. LOC → iGPU cost):

1. **Static directional shadow map** — biggest single jump. PCFSoft, tight ortho frustum fit to island, 2048 map, bias + normalBias (normalBias fixes acne on axis-aligned voxel faces), and the decisive trick: `renderer.shadowMap.autoUpdate=false`, `needsUpdate=true` only on block edits → shadow pass is near-free at runtime. ~50 LOC.
2. **Warm-cool light palette + vertical gradient tint** — warm sun ~#FFF0D6, cool blue-violet shadow side, per-vertex vertical gradient (cooler/darker at block bases) baked at mesh time. Townscaper/Monument Valley soul. ~25 LOC, free.
3. **Color grade + vignette final pass** — one full-screen ShaderPass: filmic/lift-gamma-gain curve + saturation + warm tint + soft vignette; this is the packs' "vibrant color mapping" and nearly free. ~70 LOC.
4. **Stylized water shader** — scrolling 2-octave noise normals, fresnel blend toward sky-horizon color (FAKE reflection reads true at glancing angles), high-exponent sun glint, shore-distance color lerp + foam band from per-vertex distance-to-land (already computed!). ~180 LOC, single material, no passes.
5. **Baked colored lamp light into vertex colors** — BFS/radial falloff flood from lamp blocks at mesh build; rethinking-voxels look at zero runtime cost. ~90 LOC. (Also fixes the dark-cave backlog item.)
6. **Sun-tinted height fog** — onBeforeCompile fog-chunk patch: fog lerps toward sun color by dot(viewDir,sunDir), density falls with height (Sneha Belkhale "fog hacks" pattern). ~60 LOC, free.
7. **Waving foliage** — vertex sway masked to leaf/foliage via attribute. ~40 LOC, free. (Overlaps digest 3.)
8. **Cloud shadows drifting on terrain** — scroll low-freq noise multiplied into the directional term in the Lambert chunk (Photon's most-loved detail). ~50 LOC.
9. **Thresholded HALF-RES bloom** — UnrealBloomPass is the documented expensive bloom; half resolution + high luminance threshold (only emissives/glints pass) keeps iGPU safe. ~300 LOC inlined, shares composer with 3.
10. **Radial-blur godrays, golden-hour only** — quarter-res bright pass + 2×~6-tap radial blur toward sun screen pos, fade when sun high/offscreen. ~150 LOC.

1–8 need NO composer; 3+9+10 share one. Cut from the bottom.

**Do-not-bother list:** SSAO/GTAO (baked vertex AO is the right voxel tool), Reflector/SSR water (re-renders whole scene, confirmed), three-good-godrays (per-pixel shadowmap raymarch, wrong cost class), CSM (one tight cascade suffices at this island size), TAA/DoF/motion blur/lens flares, LUT textures (analytic curves instead), physical sky models, realtime per-lamp point lights (vertex bake + bloom reads better).

Caveats: LOC/cost tiers are estimates; Townscaper internals (vertex AO, foam contours) are talk/tweet lore, unverified primary; no hard iGPU benchmarks exist per effect. Key sources: Photon README (github.com/sixthsurge/photon), Casey Primozic procedural-gamedev writeup (cprimozic.net), Belkhale fog hacks (snayss.medium.com), Andrew Berg volumetric scattering (medium), three.js forum shadow-optimization + bloom-optimize + Reflector-performance threads.

### Digest 3/4: Procedural detail + living motion (agent returned 2026-08-22)

**Shared toolkit — the style engine:** `flatShading: true` + low-segment smooth primitives (spheres 6–10 seg) = the crafted low-poly look for free. Vocabulary beyond Box: scaled Sphere (ellipsoid/egg = biggest single upgrade over boxes), Capsule, tapered Cylinder, 4-segment Cone (ears/beaks), Lathe (revolved profiles: bird bodies, tulip cups), Icosahedron(r,1) + per-vertex jitter + computeVertexNormals (rocks, canopies), Tube along CatmullRom (tails, stems), Extrude/Shape (fins, wings). The Aviator signature move: taper boxes by editing attributes.position then recompute normals. Merge parts with vertex colors → ONE geometry per prop, one draw call; scatter via InstancedMesh + setColorAt hue jitter. Cuteness lore (unverified craft consensus): head ≈ 40–50% of volume, no neck (overlap hides seam under flat shading), stubby tapered limbs, black-dot eyes wide + LOW on face, one light belly/muzzle patch, one asymmetric accent; Maaloul birds = oversized white eyes + pupils that look at things (pupil-lerp toward player = cheapest personality). Marching cubes (three addons) feasible if baked once at load for hero props; merged primitives give 90% of blobby charm free.

**Prop recipes (full pseudocode in agent transcript; keywords):** quadruped = horizontal capsule body + overlapping sphere head + sphere muzzle + 4-seg cone ears + tapered cylinder legs + tube tail; sheep = jittered sphere clumps; bird = single egg sphere + 4-seg cone beak + big white eye circles + pupil offsets + hinged wing (translate geometry so origin = shoulder, rotate to flap, no bones) + fan tail; fish = lens-scaled sphere + fan tail counter-phased to body yaw sine; flower = bent-stem cylinder + fanned scaled-sphere petals or lathe tulip cup, merged → InstancedMesh, per-instance scale/rot/HSL jitter; tree = tapered 6-seg trunk + 2–4 overlapping jittered icosahedron blobs in two adjacent greens (beats textured-quad "fluffy" approach for our style); pine = stacked cones.

**Sprite-halo fix stack (the flower bug):** (1) `alphaTest: 0.5` with `transparent: false` — discards fragments, writes depth, kills all sorting artifacts including the squares punching water; (2) dilate canvas art: paint RGB 2px oversized (or whole-canvas petal color) so transparent texels never hold white/black RGB; (3) `texture.colorSpace = SRGBColorSpace` (a wrong colorspace alone caused a documented halo, discourse #69149); (4) 128–256px source, alphaTest 0.35 or `alphaHash` if mipmaps thin cutouts at distance; (5) BEST: stop texturing vegetation — instanced 5-vertex tapered grass blades + geometry flowers need zero alpha; 20–60k blades in one InstancedMesh is iGPU-safe (Codrops fluffy-grass claims ~1M via chunking+LOD on a 2018 i3, unverified).

**Motion shortlist ranked:** 1. vertex-shader wind on grass/flowers/canopy via onBeforeCompile begin_vertex injection: 2-octave sine keyed to worldPos, height-weighted so bases pin (~30–50 LOC, the single biggest "alive" win); 2. water motion, Aviator method: coarse plane, per-vertex orbits with random amp/speed, recompute normals per frame (CPU-fine at 32×32) or 2–3 summed shader sines (~20–60 LOC); 3. fireflies/pollen/butterflies: Points + additive radial-gradient dot + 3 unsynced sines, pulse at dusk (~40 LOC, huge mood); 4. prop idle without bones: volume-preserving squash-stretch (scale.y sine, x=z=1/√y), ear/tail twitch on 4–9s randomized timers, pupil-follow (~10 LOC each); 5. 2–3 birds on lissajous paths banking into turns, flap-then-glide (~30 LOC; skip boids at n=3); 6. canopy sway fold into wind; 7. flag wave on the lighthouse (~20 LOC).

### Digest 2/4: World-space text techniques (agent returned 2026-08-22)

**Legibility ground rules:** angular size is the master variable — 15–20 arcmin cap height comfortable, go bigger for kids: word cards readable at 4–12m need **letter cap heights ~15–20cm world units**. Rotation ≥60° off face-on kills reading regardless of size (IEEE VRW 2020) → must-read text faces the approach or yaw-tracks gently. Kids' typography research: clear sans faces, larger sizes, looser spacing; the game teaches reading so TRUE lowercase letterforms are non-negotiable for vocabulary. Always contrast + outline/halo.

**Recommendation matrix (technique per text type):**
- **Collectible word cards** (the core teaching surface): **troika-three-text** SDF glyphs on a thin 3D card mesh (~2cm box), capHeight ≥15cm, sdfGlyphSize 128, dark text + white outline; card yaw-oscillates or yaw-faces the player (never pitch). Verified facts: MIT; ~129KB min total to inline (91.3 troika-three-text UMD + 5.1 worker-utils + 9.6 three-utils + 10.8 webgl-sdf-generator + 12.1 bidi-js, unpkg v0.52.5); parses ttf/otf/woff (NOT woff2). **Three offline traps, all verified:** (1) default font fetches Roboto from Google CDN → MUST set `font:` explicitly; (2) unicode fallback fetches jsDelivr → stay ASCII + point `configureTextBuilder({unicodeFontsURL})` at a dead path; (3) font loads via plain XHR on a URL string (FontResolver.js) → embed as base64 → Blob → `URL.createObjectURL`, and `configureTextBuilder({useWorker:false})` is the guaranteed file:// fallback (one-time SDF hitch). Smoke-test the blob route FIRST. Fallback if troika misbehaves: canvas planes with max anisotropy.
- **Garden labels** (short, close 1–3m): **TextGeometry** with embedded subset typeface.json — facetype.js (gero3.github.io/facetype.js) has a verified "Restrict character set" field; ~40–70 glyphs ≈ 10–20KB (estimate, generate to confirm; helvetiker full = 61.7KB verified). Small bevel, curveSegments 4–5, raised dark letters on wooden stakes, merge per material. Extruded letters shine close-up (shadows, tactile bevel).
- **Signposts** (3–10m, oblique): **canvas-texture planes on 3D signboards** — power-of-two canvas so mipmaps generate, `anisotropy = max (16)` (THE fix for oblique text smear), bold sans ≥40% board height, baked bevel strokes, boards angled 15–30° toward the path.
- **Notice board sentences** (close, face-on, multi-line): large canvas plane (2048×1024 on ~1.2m board), paper texture, loose line spacing; or troika `maxWidth` wrapping if already inlined.
- **Bot name tags: KEEP billboards, deliberately** — argued: tags are annotations addressed to the player (meta function), and a world-fixed tag is unreadable while circling a bot (the 60° cliff). Compromise that satisfies the layering law: **yaw-only billboarding** on a canvas plane (vertical world orientation, perspective scaling; "a little sign that politely turns to you"), retire screen-aligned sprites.
- **Meta/UI text: HTML/CSS overlay** (already our architecture) — browser rasterizer sharpness, and it enforces the diegetic/meta boundary cleanly.
- **Decorative landmarks** (island name arch, GARDEN gate): **voxel letters** from 5×7 uppercase bitmasks (~1KB table) → InstancedMesh cubes; uppercase-only decor register (5×7 lowercase is illegible and pedagogically wrong for vocabulary).
- **Carved-into-stone flavor:** canvas plane flush on face (1cm offset / polygonOffset) with baked inner-shadow bevel + optional build-time normal map from the same raster. AVOID DecalGeometry (pointless on flat voxel faces) and CSG engraving (bloat).

Diegetic-UI context: Half-Life Alyx layering model (diegetic flavor / spatial-billboarded critical labels / screen-space meta) matches Idan's ruling exactly; even Valve needed a custom high-x-height sans for world signage. Budgets: everything above stays far under 2MB total. Key sources: troika README + FontResolver.js + unpkg (verified), facetype.js, CSS-Tricks WebGL text survey, three.js Texture.anisotropy docs, sbcode engraving, IEEE VRW 2020.

### Shared reading list for the build session (priority order, all ungated)

codrops The Aviator tutorial (tympanus.net/codrops/2016/04/26) · Yakudoo codepens LVyJXw (birds), YXxmYR (lion), YGxYej (rabbit), poqazQo (skating bunny) — the whole animal vocabulary is in their source panels · smythdesign.com/blog/stylized-grass-webgl (BOTW 5-vertex blades, closest match) · codrops fluffiest-grass 2025/02/04 (instancing/chunk/LOD numbers) · douges.dev/blog/threejs-trees-1 · discourse 26694 + al-ro.github.io/projects/grass · sbcode.net/threejs/gerstnerwater · elliezen fireflies codepen qmoqMv + github thebenezer/threejs-fireflies · discourse 69149 (halo fix) · codrops 2025/07/10 InstancedMesh current-API reference. Summer Afternoon has no public technique devlog (verified absence in the forum thread; only toon shading + three-mesh-bvh + reactive grass confirmed).
