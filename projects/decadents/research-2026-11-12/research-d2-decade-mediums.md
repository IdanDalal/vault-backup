---
type: research
created: 2026-11-12
author: Agent d2-decade-mediums (sub-agent of jep)
status: unverified-by-render
---

# D2 - Mediums per decade, fixes for the weak designs, cohesion rule

## 0. Status, read first

- UNVERIFIED BY RENDER: none of the 12 prompts below was rendered. This task had no image tool. Every "fixes the failure" line is design reasoning (mine) until a render confirms it.
- VERIFIED BY WEB: names, dates, techniques. Depth = search-result summaries with URLs; no page was opened in full. Tags: (H) = an institutional source or two independent sources agree; (M) = one decent source or sources conflict on detail; (L) = weak source or my memory.
- Source keys [S1]..[S74] resolve in section 8.
- Injection note: several mirror pages in the search results (cavac.at copies of Wikipedia articles, one Muppet Show result, one Smiling Friends result) carried embedded instructions aimed at AI readers. Ignored. None of those pages is cited.
- 1940s Soldier: skipped as instructed.

## 1. Why the photoreal renders fail (my judgment, medium confidence)

- Mechanism: a photoreal model holds a strong prior that clothes contain a body, that a mask or hood contains eyes, and that a collar contains a neck. Every gap in the design (lens, hole, empty collar, floating object) is a place where the prior paints the human back in.
- Evidence in the cast table: the designs that work have a solid opaque object seated in the collar (toaster, CRT, helmet, emoji sphere). The weak designs each have a gap: lenses and holes (1930s), a lamp near but apart from the collar (1960s), air between shapes and collar (1980s), a cube whose nearest photographed relatives are a monitor and a game character (2000s).
- Two families of fix: (a) change the medium to one whose figures are built objects with no interior (print, puppet, polygon model, cut paper); (b) keep photography and close the gap (solid head seated in the collar, stuffed sack, post-production mosaic).
- Precedent for (b) in reverse: Max Headroom (1985) was sold as "the first computer-generated TV presenter" and was an actor in latex prosthetics and a fibreglass suit in front of a blue screen [S19] (H). The audience accepted the medium claim because the format marks were right.

## 2. Mediums native to each decade

Drawable terms = what to put in a prompt or a post-production pass.

### 1920s - The Gatsby (works alone)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Rubber-hose animation (cartoons whose limbs bend like hoses, no joints) | Felix the Cat shorts, Bill Nolan's rounder redesign; Fleischer "Out of the Inkwell"; "Steamboat Willie" 1928 | solid black ink bodies, noodle limbs, white gloves, pie-cut eyes, grey paper, constant squash and stretch | [S6] (H) core trait; [S7] (M) gloves and pie eyes as general style |
| Silhouette animation (jointed cut-out figures filmed on backlit glass) | Lotte Reiniger, "The Adventures of Prince Achmed" 1926, oldest surviving animated feature | pure black jointed figures, lace-fine cut edges, tinted single-colour backgrounds | [S25] (H) |
| German Expressionist film | "The Cabinet of Dr. Caligari" 1920 | flat sets at sharp angles, light and shadow painted onto canvas, high-contrast black and white | [S32] (H) |
| Art Deco poster lithography | A.M. Cassandre, "Nord Express" 1927, colour lithograph | streamlined geometry, vanishing-point speed lines, type framing the image | [S33] (H); airbrush claim unconfirmed |
| Silent-film grammar (intertitle cards = text cards cut between shots; iris = circular vignette that closes on one subject) | general silent-era practice | black card, white serif type, ornamental border; circular black mask around one figure | (L) my memory, unsearched |

- Fit (mine): the Gatsby is silent by design, so intertitle cards are his native speech. The iris vignette crops the frame to one figure and answers the "seated at a table pulls in extra figures" failure in post, with zero prompt risk. Stay photographic.

### 1930s - The Survivor (WEAK)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| WPA poster (Works Progress Administration, the US work-relief agency) | Federal Art Project posters 1936-1943; about 2,000 known, 900+ at the Library of Congress | screen print, 3 to 5 flat inks, stencil-hard edges, simplified figures, bold bottom band of type | [S8] (H) dates and count; flat-colour description (M), catalogue says "Screen prints - Color" |
| Fleischer cartoons | Betty Boop debut "Dizzy Dishes" 1930; Popeye | rubber hose continued, grey-scale ink wash, bouncing loop cycles | [S26] (H) for dates |
| Wood-engraving wordless novel (a story told only in prints) | Lynd Ward, "Gods' Man" 1929, 139 engravings; six novels 1929-1937 | black and white only, dense parallel hatching, towering shadows, small figure against huge forces | [S34] (H) |
| Puppetoons (replacement animation = a new carved puppet or part for each frame) | George Pal; advertising shorts from 1932 in the Netherlands; 40+ shorts for Paramount 1941-1947; about 9,000 carved parts per short | lathe-turned painted wood, enamel gloss, toy-like proportions, "colour cartoons in three dimensions" | [S35] (H) |
| Radio (audio medium, wooden table set) | 12 million US radio households in 1930, 28 million+ by 1939; first fireside chat 1933-03-12 | arched or upright walnut cabinet, cloth speaker grille, amber dial | [S63] (H) |
| Dust Bowl documentary photography (the current medium) | 1935 photos of children in goggles and home-made dust masks; Red Cross volunteers in masks, Liberal, Kansas | large-format black and white, caked dust, flat horizon | [S71] (M) captions disagree on "gas mask" versus "dust mask" |
| Modern proof the 1930s cartoon look is reproducible | "Cuphead" 2017: drawn on paper, inked by hand, watercolour backgrounds, 24 fps, scanned film grain | recipe above | [S70] (H) |

### 1950s - The Sitcom Dad (works)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| UPA limited animation (few drawings, design-led) | "Gerald McBoing-Boing" 1950 | flat graphic shapes, large fields of flat colour, bold outline, backgrounds reduced to a few lines | [S10] (H) |
| TV limited animation | Hanna-Barbera, late 1950s on; the collar or necktie hides the seam where a separately animated head meets a static body | thick outline, held body, head on its own layer, collar as dividing line | [S57] (M) popular sources; drawing counts unverified |
| Cut-paper title design | Saul Bass, "The Man with the Golden Arm" 1955 | torn or scissor-cut shapes, irregular edges, flat fill, bars sliding on black | [S36] (H) |
| Clay animation | Art Clokey, "Gumbasia" 1953; Gumby on "Howdy Doody" 1955 or 1956 | slab-cut clay, fingerprints, primary colours, toy-set backgrounds | [S37] (M) year conflict |
| Black-and-white multi-camera sitcom | "I Love Lucy" era; WandaVision's 1950s episode rebuilt it: 4:3, black and white, lens falloff at the frame edges | soft-edged 4:3 frame, flat high-key light, studio set | [S23] (H) |

- Fit (mine): stays photographic. One cheap gain: 4:3 black-and-white TV framing with soft edges.

### 1960s - The Hippie Grandma (WEAK)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Psychedelic concert poster | Wes Wilson at the Fillmore, Feb 1966 to May 1967; Victor Moscoso | lettering swollen to fill every gap, vibrating complementary colours (red on green, orange on blue), Art Nouveau curves | [S15] (M-H) |
| Psychedelic animated feature | "Yellow Submarine" 1968; art director Heinz Edelmann, director George Dunning; Edelmann wanted the look to change every five minutes | thin black outline, flat poster colour, pattern-filled clothes, Op Art backgrounds | [S12][S13][S14] (H) |
| "Animagic" stop-motion (Rankin/Bass brand name for puppet stop-motion) | "Rudolph the Red-Nosed Reindeer" 1964, shot at MOM Productions, Tokyo, under Tadahito Mochinaga | wire armature, carved wood heads, fabric and felt skin, snow-globe sets | [S17] (M) |
| Supermarionation (Gerry Anderson's name, coined 1960, for marionettes with electronic lip-sync) | "Thunderbirds" | glossy marionettes, visible strings, miniature sets | [S60] (H) term; broadcast year (L) |
| Life-size costume puppets | Sid and Marty Krofft: Banana Splits suits 1968; "H.R. Pufnstuf", NBC, Sept-Dec 1969, 17 episodes | performer inside foam and fleece, oversized built head, videotape colour | [S27] (M) |
| Liquid light show (coloured oils moved over a projector) | Joshua Light Show, founded 1967, house show at the Fillmore East from 1968 | rear-projected blobs of coloured mineral oil and alcohol, the same physics as the lamp | [S28] (H) |
| Cut-out collage animation | Terry Gilliam, "Storytime" 1968, then "Monty Python's Flying Circus" | Victorian photo cut-outs, soft-gradient bulbous shapes, jerky slides | [S38] (H) |
| The object itself | Astro lamp launched 1963 by Edward Craven Walker's firm Crestworth | tapered bottle, metal base and cap, slow wax blobs | [S66] (H) |

### 1970s - The Disco Anarchist (passable)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Drawn figure over photographed city | Ralph Bakshi: "Fritz the Cat" 1972 (photos traced); "Heavy Traffic" 1973 (real photos and stock footage as backgrounds, some blurred on purpose) | loose inked character, grainy photo background, deliberate mismatch | [S29] (H) |
| Educational TV cartoon | "Schoolhouse Rock" 1973, look set by art director Tom Yohe | loose hand-drawn line, flat colour, big lettering as picture | [S39] (M) |
| Scanimate (analog video synthesizer for TV graphics; eight built) | most 1970s flying logos; Emmy 1972 | glowing gold lettering, neon grids, star fields, soft analog smear | [S40] (H) |
| Punk collage and zine | Jamie Reid for the Sex Pistols 1976-1977 (ransom-note lettering); "Sniffin' Glue" 1976 (typewriter, felt-tip, photocopy) | cut newspaper letters, black-and-white photocopy burn, tape and scissor edges | [S30][S65] (H) |
| Sticker parody cards | Topps "Wacky Packages", peak 1973-1977 | painted fake product packaging, die-cut sticker | [S68] (M) |
| Felt hand puppets | "The Muppet Show", UK premiere 1976-09-05 | fleece and felt, ping-pong eyes | [S73] (H) date; build details (L) |

- Fit (mine): stay photographic. The archetype has two halves: disco ball covers "Disco"; photocopied ransom-note inserts and flyers cover "Anarchist" as cutaway artefacts.

### 1980s - The Yuppie (WEAK)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Memphis design (Milan design group, debut 1981, led by Ettore Sottsass) | "Carlton" bookcase 1981; "Bacterio" squiggle print 1978 | plastic laminate, primary plus pastel, asymmetric stacked solids, black-and-white squiggle | [S20] (H) |
| Early broadcast CGI | Dire Straits, "Money for Nothing" 1985; Bosch FGS-4000 plus Quantel Paintbox; animators Ian Pearson and Gavin Blair, later founders of Mainframe | blocky flat-shaded figures built from boxes, saturated solid colour, video scanlines | [S18] (H) |
| Fake CGI by practical means | Max Headroom, Channel 4, 1985-04-04 | shiny moulded suit, hard light, stuttered edit, moving line-grid background | [S19] (H) |
| Rotoscoped pencil (drawing traced over live footage) | a-ha, "Take On Me" 1985, animators Michael Patterson and Candace Reckinger | scratchy graphite line that boils, white paper, comic-panel frames | [S67] (H) credit; frame counts (L) |
| Claymation (Will Vinton's trademarked term) | California Raisins campaign, first aired 1986-09-14 | sculpted clay, finger marks, glossy eyes | [S31] (H) |
| Flat-colour fashion illustration | Patrick Nagel, "Rio" cover 1982 | bold black line, flat colour, white space, Art Deco geometry | [S41] (H) |
| Art-comic children's TV | "Pee-wee's Playhouse" 1986, designers Gary Panter, Wayne White, Ric Heitzman | clashing colour, puppets built into the furniture | [S42] (M) |
| Sticker trading cards | Topps "Garbage Pail Kids", June 1985 | painted portrait, nameplate banner, sticker die-cut | [S68] (H) |

### 1990s - Nostalgia Narcissist (done, liked)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Reality-TV confessional | MTV "The Real World", premiere 1992-05-21; credited with the confessional and the camcorder look | static chair shot, home-video colour, direct address | [S45] (H) |
| "Ugly-cute" TV animation | Klasky Csupo, "Rugrats" 1991 | asymmetrical characters, wobbly line, floor-level camera | [S43] (M) |
| First all-CGI TV series | "ReBoot", 1994-09-10, Silicon Graphics machines and Softimage | smooth plastic surfaces, primary colours, sparse sets | [S44] (H) |
| Full-motion video games (FMV = filmed actors on CD-ROM) | "Night Trap", Sega CD, 1992 | small video window, heavy compression, limited colour, grain | [S61] (M) |
| Animation anthology | MTV "Liquid Television" 1991 | many styles back to back | [S74] (H) |

- Fit (mine): stay photographic. The confessional format the whole show uses is this character's native invention; that is a free in-world joke.

### 2000s - The Edgelord (WEAKEST)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Flash web cartoon (Flash = vector animation software for browsers) | Homestar Runner site, 2000-01-01; Newgrounds portal | thick uniform outline, flat fills, one shadow tone, tweened sliding limbs, gradient backgrounds, small stage | [S46] (H) Homestar; Newgrounds and tweening (L) memory |
| Machinima (films acted inside a game engine) | "Red vs. Blue", 2003-04-01, shot in Halo | helmeted game models, bobbing heads as acting | [S21] (H) |
| PlayStation 2 era low-polygon 3D | PS2 character faces about 1,200 to 1,400 polygons; whole heroes around 4,000; textures 128 to 256 px | faceted shoulders, soft low-res textures, jagged edges, 480i | [S47] (M-L) forum and blog figures |
| Stop-motion with action figures | "Robot Chicken", 2005-02-20 | toy joints visible, sculpted plastic, miniature sets | [S48] (H) |
| Interpolated rotoscope (software-assisted tracing over live footage) | "Waking Life" 2001, "A Scanner Darkly" 2006; the film's "scramble suit" hides identity behind constantly shifting features | wobbling vector outline, sliding flat colour patches | [S49] (H) |
| Webcam and early video-sharing | low-resolution desk-top cameras | 320x240, blocky compression, monitor-glow lighting, high angle | (L) memory, unsearched |
| Period object | Motorola Razr V3, Nov 2004, 130 million sold, best-selling clamshell | thin metal flip phone, glowing keypad | [S64] (H) |

### 2010s - The Influencer (works)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Flat design | Apple iOS 7 era onward | zero texture, thin line icons, bright gradients | [S51] (M) |
| "Corporate Memphis" (flat tech-company illustration, named after the 1980s Memphis group) | Facebook "Alegria" system, 2017, by Buck with Xoana Herrera | flat geometric people, tiny heads, long limbs, blue or purple skin tones | [S51] (H) |
| Six-second loop video | Vine, 2013-01-24 to 2017-01-17 | abrupt loop, phone camera | [S52] (M) |
| Face filters | Snapchat Lenses, 2015-09-15, built on Looksery | tracked overlay on a selfie | [S53] (H) |
| Vinyl collectible | Funko Pop line, 2010-2011 | large squarish head, small body, black circular eyes, window box | [S72] (M) |

- Fit (mine): stay photographic, phone-vertical.

### 2020s - The iPad Toddler (done, liked)

| Medium | Defining works, dates | Look in drawable terms | Source, confidence |
|---|---|---|---|
| Source Filmmaker memes (Valve's free animation tool; closed beta 2012-06-27, open beta 2012-07-11) | "Skibidi Toilet", first episode 2023-02-07, made entirely in it | stiff game models, harsh default lighting, clipping | [S54] (H) |
| Blocky game avatars | Roblox-style | toy-brick bodies | (L) memory; IP flag |
| AI-generated imagery itself | 2022 onward | over-smooth surfaces, melting detail | (L) mine |

- Fit (mine): stay as is. If any character is allowed visible AI artefacts, it is this one, and only this one.

## 3. Fixes for the weak designs

Each prompt is written in positive terms only and is untested. Words deliberately absent from every prompt: the body parts the renders keep adding.

### 3.1 1930s Survivor - failure: eyes show through lenses or holes

| Option | Medium | Why it fixes the failure (mine) | Main risk |
|---|---|---|---|
| A | WPA silkscreen poster | a screen print is flat ink; a sack or a lens is one solid colour shape with nothing behind it; it is also how the 1930s state pictured ordinary workers | model adds garbled type; set all lettering in post |
| B | Carved-wood stop-motion puppet (Puppetoon family) | a 20 cm wooden puppet has no person inside; the sack is stuffed | model paints a face on the sack or carves one on the wood |
| C | Stay photographic, change construction: a scarecrow | a scarecrow is a stuffed sack by construction; straw at collar and cuffs also covers the no-skin rule | drifts to horror or to the 1939 MGM film scarecrow (IP); a painted face may appear |

Prompt A (112 words):
> 1930s American work-relief poster, hand-pulled silkscreen print in four flat ink colours: mustard yellow, rust red, deep navy, cream paper stock. A single standing figure in patched denim overalls, a wool coat, work gloves and heavy boots fills the frame from the knees up, centred. The head is a dusty burlap feed sack tied at the collar with twine, printed as one solid mustard shape with rust cross-hatch weave and a single stitched seam, a battered felt hat on top. Bold simplified shapes, hard stencil edges, slight ink misregistration, visible paper grain, navy sky above a low rust horizon with one leaning fence post. Wide empty cream band along the bottom edge.

Prompt B (about 105 words):
> Tabletop stop-motion puppet from a late-1930s Technicolor theatrical short. A hand-carved, lathe-turned wooden puppet twenty centimetres tall stands on a miniature dust-blown farm porch. Its body is painted wood dressed in tiny stitched denim overalls, a wool coat, knitted mittens and leather boots. Its head is a small burlap sack stuffed plump and smooth, cinched at the collar with twine, one seam down the front, a felt hat on top. Glossy enamel paint, visible wood grain and lathe rings, miniature props, painted backdrop of a yellow dust sky, warm key light from the left, shallow depth of field, saturated three-strip colour, fine film grain.

Prompt C (about 100 words):
> Black-and-white documentary photograph, 1936, large-format camera, fine silver grain, soft overcast light. A scarecrow sits upright on a wooden kitchen chair on a farmhouse porch, posed like an interview subject, framed from the knees up, centred. Its head is a plain burlap feed sack packed tight with straw, smooth and rounded, tied at the collar with twine, one coarse seam down the front, a battered felt hat on top. Straw pokes from the shirt collar and from both coat cuffs above stuffed work gloves. Patched denim overalls, wool coat, dust on every surface, flat plains and a leaning fence behind, deep focus.

- Recommendation (mine): A first. It is the only option that also gives the character a new visual identity that no other cast member can be mistaken for.

### 3.2 1960s Hippie Grandma - failure: lamp floats in front of a human head; bare limbs

| Option | Medium | Why it fixes the failure (mine) | Main risk |
|---|---|---|---|
| A | Felt-and-wool stop-motion puppet ("holiday special" family) | tabletop scale: a real miniature lamp fused into a puppet's collar; felt mittens and a floor-length kaftan leave nothing uncovered | the word "grandmother" pulls a puppet face; prompt uses costume cues only |
| B | 1968 psychedelic flat animation | the lamp is one outlined shape among shapes; the body is a single kaftan bell from collar to floor | drifts to a known film's characters (IP); colour edges flicker in video |
| C | Stay photographic: silhouette against a liquid light show | backlight turns the body to a black shape, so limbs and collar gap vanish; the lamp is the only lit object; the projection behind is the lamp's own physics at wall size | silhouette hides the costume work; lamp glow may reveal a shape behind the glass |

Prompt A (about 105 words):
> Stop-motion puppet from a 1960s television holiday special, photographed on a miniature set. A small puppet body, twenty centimetres tall, built on a wire armature and wrapped in felt and wool: ankle-length paisley kaftan in orange and purple, crocheted shawl, felt mittens, beaded necklaces, knitted slippers, round spectacles hanging on a bead chain. Fixed into the kaftan's high collar, brass base hidden by the shawl, is a miniature glowing lava lamp: a tapered glass bottle of amber liquid with slow magenta wax blobs and a brass cap. She sits in a tiny rocking chair on a set with daisy wallpaper and a shag rug. Soft warm studio lighting, visible felt fibres, 16mm colour film grain.

Prompt B (about 100 words):
> Frame from a 1968 psychedelic animated feature, hand-inked cel animation with flat poster colours. A tall seated figure drawn as one continuous bell-shaped kaftan from collar to floor, covered in swirling paisley and flower patterns in hot pink, orange, lime and violet, sleeves ending in white gloves holding knitting needles. Rising from the collar is a lava lamp shape: a tapered bottle in thick black outline, filled with flat orange and three floating magenta blobs, a small silver cap on top. Background of concentric rainbow sunbursts and Art Nouveau curls, thin black outlines, flat colour fills, slight cel dust and gate weave, 4:3 frame.

Prompt C (about 100 words):
> 1967 colour photograph on 35mm slide film, inside a ballroom during a liquid light show. A seated figure in a floor-length kaftan, long gloves and a fringed shawl appears as a crisp dark silhouette against a huge rear-projection screen of swirling oil-and-dye bubbles in magenta, amber and turquoise. Standing on the figure's shoulders, brass base tucked inside the high collar, is a real glowing lava lamp: a tapered glass bottle of amber liquid with slow red wax blobs and a brass cap, the brightest object in the frame. Rocking chair, knitting in the lap, strong backlight, soft halation around the lamp, saturated film colour, visible grain.

- Recommendation (mine): A first. Puppet scale is the one setting where a real lamp is the right size to be a head.

### 3.3 1980s Yuppie - failure: neck and chin appear under the floating shapes

Root cause (mine): "floating" plus "empty collar" describes a gap, and the model fills gaps. The toaster works because it sits in the collar. First move in any medium: stack the shapes into one solid totem whose base fills the collar.

| Option | Medium | Why it fixes the failure (mine) | Main risk |
|---|---|---|---|
| A | 1985 flat-shaded broadcast CGI | bodies made of separate primitives are the native grammar of that look; a stack of solids on a box torso is what the medium does by default | model modernises the render; add scanlines and colour bleed in post |
| B | Stop-motion cut-paper collage | paper pasted on a background has no depth; shapes can float above a paper collar with nothing behind them | reads as a modern craft video; needs period palette and terrazzo ground |
| C | Stay photographic, solid totem seated in the collar | closes the gap; same logic as the toaster and the CRT | drifts to a real Memphis lamp or bookcase (designs still sold; keep the stack original) |

Prompt A (about 105 words):
> Still frame from a 1985 computer-animated music video, flat-shaded polygon graphics rendered on a broadcast video system. A blocky character built from simple solids sits behind a desk: a boxy charcoal pinstripe suit torso with wide wedge shoulder pads, a red rectangular power tie, cuboid arms ending in white mitten blocks holding a brick-sized mobile phone. Rising from the white shirt collar is a stacked totem of primitives: a yellow cylinder, a tilted pink triangular prism, a turquoise sphere and a black-and-white squiggle-patterned cone on top. Hard-edged facets, solid saturated colours, gradient backdrop with a neon grid, soft video scanlines, slight colour bleed, 4:3 frame.

Prompt B (about 100 words):
> Stop-motion cut-paper collage in early-1980s music-television ident style, photographed from above on an animation stand. A figure assembled from cut paper and plastic laminate chips: a grey pinstripe paper suit jacket with huge triangular shoulders, a white paper shirt collar, a red tie, paper gloves holding a paper briefcase. Above the collar, pasted flat on the pastel background, a cluster of geometric cutouts: a yellow circle, a pink triangle, a turquoise zigzag, a black-and-white squiggle-print rectangle, each casting a thin soft shadow. Terrazzo-speckled mint background, crisp scissor edges, visible paper fibre and glue ripple, even copy-stand lighting.

Prompt C (about 105 words):
> 1986 colour photograph on 35mm film, direct flash, glossy magazine advertising look. A seated executive figure in a double-breasted charcoal pinstripe power suit with wide padded shoulders, white shirt buttoned to the top, red silk tie, black leather gloves, hands folded on a glass desk beside a brick-sized mobile phone. Seated firmly in the shirt collar like a lamp in its socket is a solid postmodern sculpture: a stacked totem of glossy laminate solids, yellow cylinder base filling the collar, pink tilted wedge, turquoise sphere, black-and-white squiggle-patterned cone on top. Pastel office with a glass-brick wall and venetian-blind shadows, saturated colour, sharp focus, film grain.

- Recommendation (mine): C first because it is one variable (solid versus floating) and tells whether the medium change is needed at all. A second.

### 3.4 2000s Edgelord - failure: drifts to a CRT (1990s collision) or a Minecraft head (IP)

Root cause (mine): a pixel-textured cube has two dominant relatives in training data, and both are forbidden. Any prompt that keeps "cube" plus "pixel" will keep sliding toward them. Either the pixelation moves out of the model into post, or the head object changes.

| Option | Medium | Why it fixes the failure (mine) | Main risk |
|---|---|---|---|
| A | Webcam-quality photography plus a censor mosaic added in post (mosaic = the block blur TV uses to hide an identity) | keeps the owner's pixel-block idea; the blocks are made by a deterministic video filter, so the model never sees the word cube; a mosaic is documentary-native and fits an anonymous troll | a mosaic implies a hidden face under it, which bends the "no face, stands for everyone" rule; the hood interior must be rendered as plain dark cloth |
| B | PS2-era low-polygon 3D render, head = case-modded PC tower | a game model has no person inside; the tower keeps "computer" while dropping the screen (CRT drift) and the cube (Minecraft drift) | viewers under 25 may read "gaming PC" as current; disc trays and blue tube light must carry the date |
| C | Flash web cartoon, head = open clamshell phone | vector flat shapes carry no texture to drift; the flip phone dates the image within one second | a second screen-head in a cast that already has the CRT; model may draw a smartphone |

Prompt A (about 100 words; better result expected from rendering the hood plain and applying the mosaic in post):
> Frame from a 2004 webcam video, 320 by 240 pixels, chunky compression blocks, washed colour, soft focus, slightly high camera angle from the top of a monitor. A slouched figure in an oversized black zip hoodie with the hood up sits at a cluttered computer desk in a dark bedroom, lit by cold blue screen glow from the left. The entire hood opening is covered by a large square censor mosaic, a ten-by-ten grid of flat blocks in charcoal, violet and black, like the privacy blur on a television news interview. Black knit gloves on a keyboard, studded belt, wallet chain, band posters, energy drink cans, tangled cables, video noise.

Prompt B (about 95 words):
> Screenshot from a 2002 console video game cutscene, real-time low-polygon 3D graphics at 480i. A character model with visibly faceted shoulders and blocky mitten hands wears a black hoodie, baggy cargo trousers with a wallet chain, and skate shoes, textures soft and low-resolution. Mounted on the hoodie collar is a tall black desktop computer tower: a vertical rectangular case with two disc-drive trays, a round power button, an acrylic side window glowing electric blue, and orange flame decals along the side. Dim bedroom environment with flat-lit posters and a single blue point light, jagged aliased edges, slight texture shimmer, 4:3 frame, subtle interlace lines.

Prompt C (about 108 words):
> Frame from an early-2000s web cartoon made in vector animation software, 550 by 400 pixel stage. Thick uniform black outlines, flat colour fills with one darker shade for shadow, radial-gradient background in dark red and black. A slouching character in a black hoodie, studded belt, baggy jeans with a wallet chain and chunky skate shoes, both hands buried in the hoodie pocket. Rising from the hood is a giant silver clamshell mobile phone standing open: a small square screen glowing blue with a pixel-flame wallpaper on the upper half, a numeric keypad on the lower half, a stubby antenna on top. Slightly stiff pose, simple cast shadow, a loading bar along the bottom edge.

- Recommendation (mine): A first. It is the cheapest test, it preserves the original concept, and the unstable part of the image is produced by a filter that cannot drift.

## 4. Lateral moves

### 4.1 Replacement heads for the 2000s cube (mine)

| # | Head | Reads "2000s" | Reads "Edgelord" | Collision | IP | Verdict |
|---|---|---|---|---|---|---|
| 1 | Censor mosaic over a hood (post effect) | medium; framing carries the date | strong: anonymous poster | none | none | best overall |
| 2 | Case-modded PC tower, blue tube light, flame decals | medium-strong with disc trays | strong: forum troll's machine | low: box, but tall and screenless | none if generic | best physical object |
| 3 | Open silver clamshell phone | strong (Razr sold 130 million from 2004 [S64] (H)) | weak; clothes must carry it | medium: another screen | generic clamshell only; avoid one maker's keypad pattern | best date stamp |
| 4 | Hood drawstring pulled fully shut, a puckered knot of cloth | weak; clothes carry it | strong: "leave me alone" | low: echoes the Soldier's void | none | cheapest costume fix |
| 5 | Tall black energy-drink can, neon lightning | medium | strong | none | high if it resembles a real brand's claw mark | usable with an invented label |
| 6 | Burned CD-R, marker scrawl, rainbow sheen | strong | weak | medium: mirror and iridescence echo the disco ball and the 2020s visor | none | skip |
| 7 | Guy Fawkes mask | strong | strong | none | high: licence held by Time Warner per 2011 reporting [S50] (M) | skip |
| 8 | Magenta-and-black checkerboard cube ("missing texture" look from game engines) | weak outside gamers | medium | cube shape remains | pattern linked to one engine | skip |

### 4.2 The character seen only through an artefact of its decade (mine; dates sourced above)

| Decade | Artefact | What it buys |
|---|---|---|
| 1920s | silent-film intertitle card and iris vignette; sheet-music cover | speech for a silent character; crop to one figure |
| 1930s | work-relief poster pasted on a brick wall; the character printed on a flour sack | flat ink, no lens interior; the sack becomes the page |
| 1950s | appliance print advertisement; boxed TV-dinner sleeve | the toaster in its natural habitat |
| 1960s | concert poster; LP sleeve | lettering and colour carry the decade with the lamp as logo |
| 1970s | photocopied gig flyer with ransom-note type; parody sticker card | the "Anarchist" half |
| 1980s | sticker trading card with nameplate; action figure in a blister pack; laminated corporate ID badge | a card or a toy has a moulded or painted body, so the collar gap never arises |
| 1990s | yearbook page; photo-booth strip; FMV game window | repeats of one figure on a page are a real period format |
| 2000s | forum avatar (100 px square) plus signature banner; social profile page shot from a high angle; burned-CD sleeve | the Edgelord exists natively as a tiny square image, which is the cube idea with a legitimate reason |
| 2010s | profile grid; vinyl collectible in a window box | toy logic again |
| 2020s | video-call tile; avatar tile | none needed |

- Video behaviour: an artefact shot is a slow camera move over a still object. That is the easiest shot type for AI video because the subject does not act. All lettering is set in post.
- Legal: invent every brand, mill, band and card series. Topps settled a suit from the Cabbage Patch Kids owners over Garbage Pail Kids and changed the designs [S68] (H); parody packaging close to a real trade dress is the risk.

### 4.3 Practical-costume logic (faceless by construction)

| Device | Decade | Why |
|---|---|---|
| Scarecrow | 1930s | stuffed sack, straw cuffs |
| Life-size costume puppet (Krofft family [S27] (M)) | 1960s | a built head on a performer in tights and gloves; photographic |
| Felt hand puppet or marionette | 1960s, 1970s | puppet hands are mittens |
| Tailor's form or valet stand wearing the suit, shapes hung above as a wire mobile | 1980s | "an empty suit" as a literal yuppie joke; strings explain the floating; stills only, since a moving empty suit invites the model to add a body |
| Action figure with swappable head (Robot Chicken method [S48] (H)) | 1980s, 2000s | moulded plastic neck peg ends the argument |
| Hood cinched shut | 2000s | cloth only |

### 4.4 Framing devices

| Device | Fits | Why |
|---|---|---|
| Anonymous-witness interview: backlit silhouette | 1930s, 1960s, 2000s | a documentary convention that removes detail by light alone |
| Censor mosaic in post | 2000s | deterministic, IP-free |
| Iris vignette, intertitles | 1920s | crops extra figures, gives the silent mask a voice |
| The collar rule: every head sits in a collar, scarf or neckline, and the collar is always in frame | whole cast | Hanna-Barbera used the collar as the seam between a moving head and a still body [S57] (M); the same seam can be the visual signature of this cast and the place where object meets costume |
| Dust-caked goggles and cloth dust mask in place of the gas mask | 1930s | period-true (1935 photographs [S71] (M)); caked dust gives the lenses a solid surface; untested |

## 5. Cohesion

### 5.1 Verified precedents of one ensemble in mixed mediums

| Work | What mixes | What binds it | Source, confidence |
|---|---|---|---|
| "The Amazing World of Gumball" (Cartoon Network, creator Ben Bocquelet) | 2D, puppetry, CGI, stop-motion, Flash and live action, sometimes in one scene; backgrounds blend 3D render and photographs | origin story: Bocquelet reused characters from rejected commercial pitches and placed them over a photograph of a school; one shared photographic world and one comic voice | [S1][S2][S3][S4] (H); [S5] (M) |
| "Spider-Man: Into the Spider-Verse" 2018 | each Spider-character keeps the style of its home universe: black-and-white noir, anime, flat cartoon | the differences are the premise, stated in the story | [S22] (M) reviews |
| "Chip 'n Dale: Rescue Rangers" 2022 | hand-drawn, black-and-white, clay, CG, motion capture and puppet characters living in live-action Los Angeles | one live-action city; each style is treated as that character's biology | [S24] (H) |
| "Smiling Friends" | rotoscoped, CGI, stop-motion and live-action guests in a 2D show | constant main cast and deadpan tone | [S59] (M) |
| "Don't Hug Me I'm Scared" (web 2011, Channel 4 2022) | puppetry, live action, 2D, CGI, stop-motion, clay | three constant puppets and one set | [S69] (H) |
| "Marcel the Shell with Shoes On" (feature, premiered 2021) | stop-motion character in a live-action mockumentary | shot twice: live action first, then animation matched to on-set lighting notes; deliberately haphazard documentary camera | [S56] (H) |
| "WandaVision" 2021 | each episode rebuilds one decade's sitcom: black and white and 4:3 for the 1950s and 1960s, then wider ratios (1.33 to 1.78 to 2.39), period-correct effects, grain and softness per episode | same two leads, same house plan, a stated reason for the changes | [S23] (H) |
| "Heavy Traffic" 1973 | drawn characters over real photographs and stock footage | the mismatch is the style | [S29] (H) |
| "Yellow Submarine" 1968 | the look changes every few minutes by design | one voice cast, one journey | [S14] (M) |

### 5.2 What binds such a cast (mine, derived from the table)

1. One premise stated early and never broken (rejected mascots; a multiverse; a spell). Here: a family made of decades.
2. One constant frame. Here: the confessional. Same seat height, same shot size, same eye-line, same lower-third caption design in every medium.
3. One constant construction rule. Here: object head seated in a collar, no skin.
4. One shared physical anchor translated into each medium. Example: the same armchair or the same family photograph, redrawn as ink, felt, polygons, pixels.
5. One sound world: the same interviewer voice and room tone under every medium.
6. Advantage of this show: one character per shot. No frame ever needs two mediums composited together, which is the expensive part of every precedent above.

### 5.3 Recommendation and rule (mine)

Rule, one sentence: **every decade appears in the format its own era used to put ordinary people on a page or a screen.** For some decades that format is a photograph, for others it is a print, a puppet or a polygon model. The rule reads as intent only if the photographic decades also show format marks (ratio, cadence, artefacts). Then no decade is "the normal one".

| Decade | Verdict | Format under the rule | Format marks, mostly added in post |
|---|---|---|---|
| 1920s | stay photographic | silent film | black and white, 4:3, intertitle cards, iris vignette, stepped cadence |
| 1930s | CHANGE | work-relief silkscreen poster (fallback: scarecrow photograph) | 4 inks, misregistration, paper grain, 12 fps holds |
| 1940s | other researcher (comics) | - | - |
| 1950s | stay photographic | black-and-white multi-camera sitcom | 4:3, soft frame edges, high-key light |
| 1960s | CHANGE | felt stop-motion puppet (fallback: silhouette photo) | 16mm grain, 12 fps re-step, miniature set |
| 1970s | stay photographic | 16mm colour, with photocopied punk inserts | grain, glowing synthesizer-style titles |
| 1980s | CHANGE if the solid totem fails in photo | 1985 broadcast CGI | 4:3, scanlines, colour bleed |
| 1990s | stay | camcorder confessional | home-video colour |
| 2000s | stay photographic, degrade | webcam, censor mosaic | 320x240, 15 fps, compression blocks |
| 2010s | stay | phone vertical video | 9:16 |
| 2020s | stay | phone vertical, visible AI gloss allowed | 9:16 |

- Result: three or four non-photographic decades (1930s, 1940s, 1960s, possibly 1980s) spread through the timeline, never adjacent except 1930s-1940s.
- Counterpoint (mine): the changed decades are exactly the weak ones, so a viewer could read the mix as a repair. The format marks on the photographic decades are the defence. If only the weak ones change and the rest stay clean modern photographs, the mix will read as inconsistency.
- On "low quality" (mine, hypothesis): three candidate causes. (1) Photoreal plus an impossible object exposes every physical error. (2) Default AI finish is over-smooth and centred; period formats add constraints (few inks, grain, ratio) that read as craft. (3) Finish level differs between characters. Test: for one weak character, show the photoreal render beside one changed-medium render, same pose, and let the owner pick by eye. One round answers whether medium is the lever.

## 6. Production reality: behaviour in a 3 to 5 second AI video shot

General, sourced: generative video still struggles with visual consistency and style coherence for cel-style animation [S58, arXiv survey] (H). Vendor documentation reports that models drift toward photorealism without a style reference, and that they synthesise continuous motion, so stop-motion cadence wanders between about 8 and 12 fps; suggested repair is to re-step the clip to a fixed rate in post [S58, vendor FAQs] (L, vendor tests). Starting from an approved still (image-to-video) is the standard consistency lever (L, vendor claim).

| Medium | Versus photoreal | Why (mine unless tagged) | Legal flag |
|---|---|---|---|
| Silkscreen poster | easier | flat fills hide temporal error; motion can be 2 or 3 held poses plus a camera push | WPA posters: "no known restrictions" per the Library of Congress [S8][S9] (H); name no artist |
| Wood engraving | harder | hatch lines crawl frame to frame; use as stills with camera moves | Lynd Ward's books are still in copyright; describe, name nobody |
| Rubber-hose cartoon | similar | limb morphing is on-style; outline thickness wanders | the 1928 "Steamboat Willie" Mickey and 1930 Betty Boop are public domain in the US, later versions and trademarks are live [S26] (H); avoid all named characters |
| Carved-wood or felt puppet stop-motion | easier look, harder cadence | models render felt and wood convincingly; cadence needs a post re-step to 12 fps | "Animagic", "Puppetoon", "Claymation" are brand names; describe the build |
| Psychedelic flat animation | similar | flat colour holds; vibrating colour edges flicker | the 1968 film and its characters are owned; several poster artists are living; name none |
| Life-size costume, photographic | similar | models add a smiling face to mascot heads | Krofft characters are owned |
| 1985 flat-shaded CGI | easier | simple solids are stable; model may upgrade the render, so degrade in post | the Dire Straits characters and Max Headroom are owned; generic blocky figures are free |
| Cut-paper collage | easier | paper texture is stable; motion is slides and swaps, cheap to do by hand from stills | Memphis furniture designs are in production; keep shapes original |
| Low-polygon 3D | easier | stiff motion is on-style | no game characters, no console logos; Minecraft has commercial-use guidelines that bar brand promotion with its assets [S62] (M) |
| Flash-style vector | similar; cheaper done by hand | tweened limbs from one AI still in any 2D rigging tool beat AI video for stability | none if original |
| Webcam degrade plus post mosaic | easiest | low resolution and 15 fps hide artefacts; the mosaic is a filter | none |
| Artefact shots (card, box, poster, badge) | easiest | the subject is a still object; the camera moves | invent all brands; avoid real trade dress |
| Machinima, Source Filmmaker look | similar | stiff game acting is on-style | built on game assets (Halo, Valve) in the originals [S21][S54] (H); use original models only |

Style and the law, sourced: US copyright does not protect a style as such, but the Copyright Office has said an "in the style of" output that reproduces protectable elements of a specific work can infringe, and that state publicity law may reach a style closely identified with one person [S55] (M, law-firm summaries of the 2025 reports; the Part 3 report was a pre-publication version). Working rule (mine): describe the look in drawable terms, name no living artist, no studio, no character, no brand.

## 7. The five highest-value changes, ranked (mine)

1. **2000s Edgelord: drop the model-rendered cube.** Hooded figure in webcam framing, censor mosaic added in post; fallback head = case-modded PC tower. Removes the IP drift, the CRT collision and the weakest design in one step. Cost: one render plus one filter.
2. **1980s Yuppie: make the shapes one solid totem seated in the collar.** Same logic as the toaster. Test in photo first; if the neck returns, move to 1985 flat-shaded CGI.
3. **1930s Survivor: move to the work-relief silkscreen poster.** Flat ink has no lens interior; fallback is the scarecrow photograph.
4. **1960s Hippie Grandma: rebuild as a felt stop-motion puppet** with the lamp fused into the collar; fallback is the silhouette against a liquid light show.
5. **Cast-wide: adopt the format rule and the collar rule,** and add period format marks in post to the decades that stay photographic (ratio, cadence, grain, intertitles for the 1920s). This turns the mix into intent and is the cheapest test of the "low quality" complaint.

## 8. Sources

- [S1] https://en.wikipedia.org/wiki/The_Amazing_World_of_Gumball
- [S2] https://studiosoi.de/gumball
- [S3] https://en.wikipedia.org/wiki/Ben_Bocquelet
- [S4] https://www.skwigly.co.uk/ben-bocquelet/
- [S5] https://tvtropes.org/pmwiki/pmwiki.php/WhatCouldHaveBeen/TheAmazingWorldOfGumball
- [S6] https://en.wikipedia.org/wiki/Rubber_hose_animation
- [S7] https://TVTropes.org/pmwiki/pmwiki.php/Main/InkblotCartoonStyle
- [S8] https://loc.gov/pictures/collection/wpapos
- [S9] https://blogs.loc.gov/picturethis/2020/12/revisiting-rights-free-wpa-posters-perennial-favorites-on-enduring-themes/
- [S10] https://animationobsessive.substack.com/p/what-the-upa-style-actually-is ; https://skwigly.co.uk/100-greatest-animated-shorts-gerald-mcboing-boing
- [S12] https://en.wikipedia.org/wiki/Heinz_Edelmann
- [S13] https://graphicarts.princeton.edu/2013/10/10/heinz-edelmann/
- [S14] https://www.thebeatles.com/node/15
- [S15] https://eyeondesign.aiga.org/celebrating-the-50th-anniversary-of-the-summer-of-love-with-seminal-psychedelic-posters/ ; https://www.davisart.com/blogs/curators-corner/the-psychedelic-poster/ ; https://www.cooperhewitt.org/2017/06/15/25337/
- [S17] https://www.mentalfloss.com/holidays/christmas/rudolph-the-red-nosed-reindeer-tv-puppets-auction
- [S18] https://medium.com/pcmag-access/the-history-of-computer-animated-music-videos-bc3e8c2c40c5 ; https://www.vice.com/en/article/dire-straits-money-for-nothing-video
- [S19] https://en.wikipedia.org/wiki/Max_Headroom
- [S20] https://en.wikipedia.org/wiki/Memphis_Group ; https://www.wallpaper.com/design-interiors/memphis-design-group-definitive-guide
- [S21] https://en.wikipedia.org/wiki/Red_vs._Blue
- [S22] https://www.slashfilm.com/563304/spider-man-into-the-spider-verse-analysis ; https://www.hollywoodreporter.com/behind-screen/how-spider-man-got-a-makeover-spider-verse-1165982
- [S23] https://ibc.org/trends/behind-the-scenes-wandavision/7468.article ; https://www.postmagazine.com/Publications/Post-Magazine/2021/March-April-2021/Cover-Story-Disney-s-I-WandaVision-I-.aspx ; https://bleedingcool.com/tv/wandavision-cinematographer-breaks-down-frame-changes-on-series
- [S24] https://d23.com/a-to-z/chip-n-dale-rescue-rangers-film/ ; https://digitaltrends.com/movies/chip-n-dale-rescue-rangers-visual-effects-interview-vfx-animation
- [S25] https://en.wikipedia.org/wiki/The_Adventures_of_Prince_Achmed
- [S26] https://www.npr.org/2025/12/26/nx-s1-5649395/public-domain-2026-copyright-betty-boop-pluto ; https://www.deseret.com/entertainment/2026/01/02/betty-boop-public-domain-2026/
- [S27] https://clickamericana.com/eras/1960s/about-h-r-pufnstuf-the-completely-wacky-vintage-kids-tv-show-plus-see-the-opening-credits
- [S28] https://en.wikipedia.org/wiki/Liquid_light_show ; https://frieze.com/article/light-laboratories
- [S29] https://en.wikipedia.org/wiki/Heavy_Traffic ; https://catalog.afi.com/Film/54973-HEAVY-TRAFFIC
- [S30] https://api.vam.ac.uk/v2/object/O171337 ; https://anothermag.com/art-photography/15047/jamie-reid-death-sex-pistols-god-save-the-queen
- [S31] https://www.mentalfloss.com/entertainment/tv/california-raisins-how-bunch-dried-grapes-became-hit-band ; https://si.edu/object/california-raisin:nmah_1170672
- [S32] https://www.metmuseum.org/art/collection/search/294442 ; https://bfi.org.uk/features/100-years-cabinet-dr-caligari
- [S33] https://collections.vam.ac.uk/item/O89673
- [S34] https://en.wikipedia.org/wiki/Gods%27_Man ; https://blogs.loc.gov/loc/2020/11/lynd-wards-eerie-early-graphic-novel-gods-man/
- [S35] https://en.wikipedia.org/wiki/Puppetoons
- [S36] https://en.wikipedia.org/wiki/Saul_Bass ; https://www.bfi.org.uk/lists/celebrating-saul-basss-centenary-10-essential-title-sequences
- [S37] https://en.wikipedia.org/wiki/Gumby ; https://www.televisionacademy.com/features/news/news/gumby-creator-art-clokey-dies-88
- [S38] https://www.openculture.com/2011/08/terry_gilliams_diy_cutout_animation_show.html ; https://www.skwigly.co.uk/100-greatest-animated-shorts-storytime-terry-gilliam/
- [S39] https://en.wikipedia.org/wiki/Thomas_Yohe ; https://cartoonresearch.com/index.php/a-class-act-the-50th-anniversary-of-schoolhouse-rock/
- [S40] https://en.wikipedia.org/wiki/Scanimate ; https://hackaday.com/2021/03/31/scanimate-analog-video-synths-produced-oceans-of-motion-graphics
- [S41] https://en.wikipedia.org/wiki/Patrick_Nagel
- [S42] https://www.tcj.com/the-artists-and-cartoonists-who-designed-pee-wee-hermans-world-part-one/
- [S43] https://www.yahoo.com/entertainment/technology-generation-viewers-inform-rugrats-161526289.html
- [S44] https://en.wikipedia.org/wiki/ReBoot ; https://www.denofgeek.com/tv/reboot-30-years-later-cgi-kids-show-ahead-of-its-time
- [S45] https://www.museum.tv/tv-encyclopedia-14/reality-television-us ; https://en.wikipedia.org/wiki/The_Real_World:_New_York ; https://www.mentalfloss.com/entertainment/tv/mtv-the-real-world-reality-tv-show
- [S46] https://gizmodo.com/an-oral-history-of-homestar-runner-the-internets-favor-1791519879
- [S47] https://blog.playstation.com/2019/12/16/the-polygonal-evolution-of-5-iconic-playstation-characters/ ; https://polycount.com/discussion/180178/what-was-the-modeling-texturing-workflow-and-tools-used-during-the-playstation-era ; https://gamingbolt.com/metal-gear-solid-2-a-technical-retrospective-of-hideo-kojimas-masterpiece
- [S48] https://www.inverse.com/entertainment/robot-chicken-oral-history ; https://awn.com/animationworld/go-behind-scenes-robot-chicken-puppet-and-costume-fabrication
- [S49] https://www.screendaily.com/a-scanner-darkly/4027478.article ; https://www.reelviews.net/reelviews/scanner-darkly-a
- [S50] https://techcrunch.com/2011/08/29/we-are-time-warner-we-are-making-a-ton-of-money-from-those-v-for-vendetta-masks-thanks/ ; https://boingboing.net/2011/08/29/every-time-an-anonymous-protester-dons-a-guy-fawkes-mask-time-warner-goes-ka-ching.html
- [S51] https://en.wikipedia.org/wiki/Corporate_Memphis ; https://eyeondesign.aiga.org/what-the-think-pieces-about-corporate-memphis-tell-us-about-the-state-of-illustration/ ; https://designlobster.substack.com/p/144-design-deja-vu
- [S52] https://productmint.com/what-happened-to-vine/
- [S53] https://techcrunch.com/2015/09/15/snapchat-starts-charging-0-99-for-3-replays-adds-face-effect-lenses
- [S54] https://developer.valvesoftware.com/wiki/Source_Filmmaker ; https://cartoonbrew.com/biz/valve-releases-source-filmmaker-and-meet-the-pyro-65504.html ; https://wikiwand.com/en/articles/Skibidi
- [S55] https://www.thefashionlaw.com/resource-center-snapshot-the-copyright-offices-first-generative-ai-report/ ; https://www.skadden.com/-/media/files/publications/2025/05/copyright_office_weighs_in_on_ai_training_and_fair_use.pdf ; https://ipwatchdog.com/2025/05/12/copyright-office-weighs-ai-fair-use-amidst-major-leadership-shakeup/
- [S56] https://www.awn.com/animationworld/how-stop-motion-masters-chiodo-bros-tackled-marcel-shell-shoes ; https://www.inverse.com/entertainment/marcel-the-shell-interview
- [S57] https://metvtoons.com/stories/why-are-hanna-barbera-characters-always-wearing-ties ; https://tvtropes.org/pmwiki/pmwiki.php/Main/RingAroundTheCollar ; https://cartoonresearch.com/?p=69841
- [S58] https://arxiv.org/abs/2501.06250 ; https://invideo.io/faq/how-do-you-stop-ai-from-drifting-into-photorealism-when/ ; https://invideo.io/faq/why-does-ai-generated-stop-motion-animation-have/ ; https://invideo.io/faq/can-ai-video-generators-produce-stable-frame-rates-for/
- [S59] https://wikiwand.com/en/articles/Smiling_Friends
- [S60] https://en.wikipedia.org/wiki/Supermarionation
- [S61] https://www.hardcoregaming101.net/night-trap/
- [S62] https://www.minecraft.net/article/commercial-usage-guidelines-updated
- [S63] https://www.pbs.org/opb/historydetectives/feature/radio-in-the-1930s ; https://www.history.com/this-day-in-history/fdr-gives-first-fireside-chat
- [S64] https://en.wikipedia.org/wiki/Motorola_Razr_V3
- [S65] https://rocksbackpages.com/Library/Article/isniffin-gluei-a-fanzine-that-epitomized-punk ; https://www.udiscovermusic.com/?p=42083
- [S66] https://en.wikipedia.org/wiki/Lava_lamp ; https://en.wikipedia.org/wiki/Mathmos
- [S67] https://beforesandafters.com/2020/02/20/a-has-rotoscoped-1985-music-video-for-take-on-me-has-been-watched-a-lot ; https://www.mentalfloss.com/article/641682/a-ha-take-on-me-music-video
- [S68] https://promotion.topps.com/garbage-pail-kids ; https://collectorsweekly.com/cards/wacky-packages
- [S69] https://www.channel4.com/press/news/dont-hug-me-im-scared-press-pack-interview-becky-sloan-joe-pelling-and-baker-terry-0
- [S70] https://unity.com/madewith/cuphead ; https://gamesradar.com/the-making-of-cuphead
- [S71] https://www.kansasmemory.gov/category/5761 ; https://infosys.ars.usda.gov/WindErosion/multimedia/dustbowl/dustbowlpics.html
- [S72] https://www.wikipedia.org/wiki/Funko ; https://www.mentalfloss.com/fun/toys/maximum-cute-how-funko-conquered-toy-world
- [S73] https://www.britannica.com/topic/The-Muppet-Show
- [S74] https://en.wikipedia.org/wiki/Liquid_Television

Unsourced items, flagged in place as (L) memory: silent-film intertitles and iris; Newgrounds and tweening detail; webcam specifications; Roblox avatar look; "Thunderbirds" broadcast year; Muppet build materials; early-1980s music-television idents as a cut-paper precedent; cold-cathode case lighting as a 2000s marker.
