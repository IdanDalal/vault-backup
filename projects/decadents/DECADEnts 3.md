# Research Report: "DECADEnts" - Production Bible & Technical Architecture

## 1. Character Architecture: The "Family of Time"

To reconcile the "Adult in Era" vs. "Age of Era" paradox, we will utilize a **"Sitcom Family"** framework. The characters aren't just random entities; they are a dysfunctional family living in a "Time House." Their _biological age_ corresponds to the years passed since their decade ended (making them relatable to that demographic today), but their _personality_ is the frozen archetype of their prime.

### 1.1 The Cast & The Grid

We fit 11 characters (1920s–2020s) into the D&D Alignment and Literary Conflict grids. Note that some slots share characters to accommodate the cast of 11.

**The "DECADEnts" Alignment Chart**

|**Alignment**|**Decade**|**Archetype**|**Logic**|
|---|---|---|---|
|**Lawful Good**|**1950s**|_The Sitcom Dad_|Obsessed with norms, "nuclear family" values, and lawns.|
|**Neutral Good**|**1960s**|_The Hippie Grandma_|Means well, loves peace, but is permanently "hazy."|
|**Chaotic Good**|**1970s**|_The Disco Anarchist_|Fights "The Man" with bad fashion and questionable hygiene.|
|**Lawful Neutral**|**1940s**|_The Soldier_|Follows orders, shouts constantly, violent but disciplined.|
|**True Neutral**|**1930s**|_The Survivor_|Silent, traumatized, hoards crumbs. Just exists.|
|**Chaotic Neutral**|**2020s**|_The iPad Toddler_|Pure chaos. No attention span. Screams if Wi-Fi cuts out.|
|**Lawful Evil**|**1980s**|_The Yuppie_|Corporate greed personified. Uses "synergy" unironically.|
|**Neutral Evil**|**2000s**|_The Edgelord_|Cynical, "South Park" republican, trusts nothing.|
|**Chaotic Evil**|**1920s**|_The Gatsby_|Partying while the world burns. Ignorant of consequences.|
|**Wildcards**|**1990s**|_Nostalgia Narcissist_|Oscillates between Good/Neutral. Thinks he's the main character.|
|**Wildcards**|**2010s**|_The Influencer_|Chaotic/Neutral. Lives for the algorithm.|

**The Literary Conflict 3x3 Mapping**

|**Conflict Type**|**Decade**|**Rationale**|
|---|---|---|
|**Man vs. Man**|**1940s**|Defined by WW2. Life is a literal battle.|
|**Man vs. Self**|**1990s**|"Slackers," identity crisis, grunge angst.|
|**Man vs. Nature**|**1930s**|The Dust Bowl. The environment is trying to kill them.|
|**Man vs. Society**|**1960s**|Counter-culture. Rejection of systems.|
|**Man vs. Machine**|**1920s**|Industrial revolution peaked. Fordism.|
|**Man vs. God**|**1950s**|Post-war existentialism hidden under religious conformity.|
|**Man vs. Reality**|**2010s**|Instagram filters vs. Truth. "Fake News."|
|**Man vs. Author**|**2000s**|4th wall breaking (meta-humor). Questioning the simulation.|
|**Man vs. No God**|**1980s**|Materialism is the new religion. "Greed is Good."|
|**Man vs. Tech**|**2020s**|Enslaved by the algorithm.|

---

## 2. Visual Strategy: The "Ryan George" Model with Abstract Heads

Your "Abstract Head" idea is **technically brilliant** for a solo workflow. It solves the hardest problem in AI video (facial consistency) by removing faces entirely.

**The Aesthetic:**

- **Body:** Humanoid, period-accurate clothing (generated via Flux LoRA).
    
- **Head:** Rigid 3D object (tracked in Blender).
    
- **Format:** "Pitch Meeting" style. One shot, one character, distinct background. Cuts every ~3-5s.
    

**Character Visual Dictionary:**

- **1920s:** **Porcelain Art Deco Mask.** Cracked glaze. _No Mouth._ (Silent).
    
- **1930s:** **Dusty Burlap Sack / Gas Mask.** Obscured features.
    
- **1940s:** **Steel Helmet** that casts a shadow over where the face should be. Just darkness.
    
- **1950s:** **Retro Toaster / Appliance.** Chrome finish reflecting the American Dream.
    
- **1960s:** **Lava Lamp.** Blobby, shifting colors inside glass.
    
- **1970s:** **Disco Ball / Pet Rock.**
    
- **1980s:** **Geometric Shapes** (Memphis Design). Floating triangles/squiggles.
    
- **1990s:** **CRT Monitor.** Displays static or "Please Stand By" bars.
    
- **2000s:** **Pixelated Cube.** Low-res texture (early 3D game aesthetic).
    
- **2010s:** **Instagram Icon / Emoji Head.** High gloss, flat design.
    
- **2020s:** **VR Headset / QR Code.** Face fully obscured by tech.
    

---

## 3. Technical Workflow: The "Constraint-Based" Pipeline

You asked if using **Blender** is a good idea. It is not just good; it is **essential**. It moves you from "generating" (random) to "rendering" (controlled).

### Step 1: The "Cold Start" Voice Pipeline (Copyright-Free)

_Goal: Create unique voices without stealing existing audio._

1. **Generation (Parler-TTS):** Use **Parler-TTS** (open source). It allows you to prompt for voice characteristics.
    
    - _Prompt:_ "A scratchy, high-pitched 1920s radio announcer voice, speaking quickly."
        
    - _Result:_ A unique audio clip.
        
2. **Refinement (Kokoro):** If Parler is too slow/low quality, use the Parler output as a **Reference** for **F5-TTS** or **Kokoro** (using its voice mixing).
    
3. **Acting (F5-TTS):** Once you have the "Master Voice File" (your generated reference), load it into **F5-TTS**. Now, type your script. F5-TTS will "act" the script using that unique voice.
    
4. **Post-Processing (Audacity):** Apply the era-specific "Technical Filter."
    

**Audio Filter "Recipes" (Audacity):**

- **1920s (Silent/Music):** No voice. Use **MusicGen** (locally) to generate "1920s ragtime piano, silent film score."
    
- **1940s (Radio):** High Pass Filter (300Hz) + Low Pass Filter (3kHz) + Distortion (Soft Overdrive).
    
- **1990s (VHS):** "Wow and Flutter" plugin (free VSTs exist) + slight background hiss.
    

### Step 2: The Blender "Greybox" (The Skeleton)

- **Scene:** Create a simple room.
    
- **Character:** Use a "Mixamo" character (free rigged humans).
    
- **Heads:** Parent a Cube/Sphere/CRT model to the Mixamo `Head` bone.
    
- **Animation:** Animate the head bobbing/rotating to the audio.
    
- **Output:** Render **two** videos from Blender:
    
    1. **Depth Map:** Black & White video showing distance.
        
    2. **Canny/Edge Map:** Line art video showing the _exact_ shape of your abstract head.
        

### Step 3: The Neural Render (Wan 2.1)

- **Tool:** ComfyUI running Wan 2.1 (720p version, upscaled later).
    
- **Input:** Your Blender Depth + Canny videos.
    
- **Prompt:** "1990s footage, man wearing flannel shirt, CRT monitor head, grunge aesthetic, VHS tracking error."
    
- **Logic:** The ControlNets (Depth/Canny) force the AI to keep the _shape_ of your CRT head, while the Diffusion model textures it to look photorealistic.
    

---

## 4. The "Endless" Content Strategy

The "Countryballs" Model:

This is the correct strategic comparison. Low barrier to entry, high distinctiveness.

**Pilot Episode Structure (Mockumentary):**

- **Title:** "The House of Time"
    
- **Format:** Confessional interviews (The Office style).
    
- **Opening:** The 1990s character is setting up the camera. "Is this thing on? Okay. Welcome to the house."
    
- **Beats:**
    
    - Intro 1920s (sitting in corner, black and white, text card says).
        
    - Intro 1940s (dives behind sofa thinking the camera flash is a grenade).
        
    - Intro 2020s (swipes the camera lens trying to scroll to the next video).
        

The "Drop-In" Loop:

Once the Pilot establishes the "Heads" = "Characters," you stop explaining.

- **Video 2:** "1980s tries to sell 2000s an NFT." (1980s calls it a "Ponzi," 2000s calls it "Crypto").
    
- **Video 3:** "1950s sees a Pride Parade." (Self-explanatory).
    

## 5. Feasibility Verdict

- **Financial:** $0. (All tools listed are free/open source).
    
- **Hardware:** RTX 4090 is perfect. It can run Wan 2.1 (quantized), MusicGen, and F5-TTS locally with acceptable speeds.
    
- **Effort:** High initially (building the Blender rigs and Voice Refs). Low subsequently (just swapping audio and re-rendering).
    
- **Unique Value:** The "Abstract Head" + "Specific Era Audio" combination creates a **high-sensory signature**. Viewers will recognize a "DECADEnts" video instantly by the _sound_ of the static or the _look_ of the CRT head, even before a joke is told.
    

**Next Step:** Do you want to proceed with generating the specific **Character Bible** (prompts for their looks) or the **Technical Setup Guide** (installing the specific ComfyUI nodes)?