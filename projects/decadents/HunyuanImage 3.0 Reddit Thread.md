# HunyuanImage 3.0 (80B) running natively in ComfyUI on a single 12–24 GB GPU: text-to-image, editing and style transfer, ~30 s per image

I've been working on native ComfyUI support for Tencent's HunyuanImage 3.0, the 80B mixture-of-experts image model (13B active per step). It isn't a wrapper around Tencent's pipeline: it uses the normal KSampler, the normal VAE Decode and ComfyUI's own memory management, which streams the experts from system RAM so the model fits on one consumer GPU.

What's in the gallery (all Instruct-Distil, 8 steps):

4-bit vs int8, same prompt and seed. Times are the whole generation on an RTX 3090.

image editing with the 4-bit weights. The instruction is at the top of each image.

style transfer with the 4-bit weights: two input images, the photo and a style reference.

These are picked from a bigger run: 60 prompts × 2 formats, 60 edits and 14 styles, one seed each, no rerolls. Most of the edits worked; a few didn't (snow that barely shows, a logo it wouldn't remove, a "make it night" that stayed day). The text-to-image prompts come from popular prompt posts on X.

What you get

All three models: Instruct-Distil (8 steps, the one to start with), Instruct (50 steps) and Base

Text-to-image, image editing, and multi-image fusion with up to 3 input images (that's how the style transfer works)

Optional prompt rewriting: the model expands your prompt first (slow, about 1 s per token)

Optional Spectrum speed-up: about 3.4× faster for the 50-step models

Ready-made weights: 4-bit W4A8 (44 GB), int8 (76 GB) and bf16 (150 GB, mostly for comparisons)

Example workflows for each model and task

Nothing to pip install

Speed (Instruct-Distil, about 1 megapixel):

GPU	4-bit W4A8	int8
RTX 4090	~22–26 s	~47–49 s
RTX 3090	~29 s	~54 s
It also runs with only 16 GB or 12 GB of VRAM (~30 s and ~32 s per image on a 4090 limited to that).

What you need

An NVIDIA GPU with 12 GB+

Lots of system RAM: ComfyUI held about 50 GB with the 4-bit file loaded. This is the real requirement, since the experts live in RAM and stream over PCIe every step.

A recent ComfyUI (late September 2026 or newer)

Links

Nodes: https://github.com/PedroMarinhoDev/ComfyUI-HunyuanImage3

Weights: Instruct-Distil · Instruct · Base

Every model, format and Spectrum setting side by side: https://pedromarinhodev.github.io/ComfyUI-HunyuanImage3/

Happy to answer questions. If something breaks, open an issue on GitHub with the traceback.


Upvote
787

Downvote

159
Go to comments

1
Repost

Share
Join the conversation

Sort by:

Top

Search Comments
Expand comment search
Comments Section
nenecaliente69
•
1mo ago
u/ArdascesIV avatar
ArdascesIV
•
1mo ago
This image model is bigger than minimax


Upvote
58

Downvote

Reply

Award

Share

u/ArttTaku avatar
ArttTaku
•
1mo ago
Agreed, 80GB for an INT8 model is out of my range for now... i know it can fit somehow in my system (5090), but I don't wanna tax my computer that much if there are other viable options out there.


Upvote
14

Downvote

Reply

Award

Share

u/Cukidzsi avatar
Cukidzsi
•
1mo ago
If it runs, and times are good, I will be more than willing to sacrifice my system RAM.


Upvote
1

Downvote

Reply

Award

Share

u/ACTSATGuyonReddit avatar
ACTSATGuyonReddit
•
1mo ago
What is the best image editor? I too have a 5090., Ultra 9, 64GB Ram. I bought it in April and have barely turned it on. I want to get back into AI for images, video, voice - make some videos including a memorial video for my mom who died in March.


Upvote
2

Downvote

Reply

Award

Share

u/ArttTaku avatar
ArttTaku
•
1mo ago
So far, the best editor for me was Qwen Image Edit 2511, but it does seem that Qwen Image 2.1 is even better, I haven't had time to try out yet, but will soon. Apparently there's a new model by Hunyan that's even better, but the base model is 80GB and that's way too big for a 5090, even though you can make it fit, it will always be straining, so, I'd stick with the Qwen models for now.


Upvote
1

Downvote

Reply

Award

Share

_VirtualCosmos_
•
1mo ago
about 2.5 times more


Upvote
2

Downvote

Reply

Award

Share

Rheumi
•
1mo ago
and about half an year older, too ;)


Upvote
2

Downvote

Reply

Award

Share

[deleted]
•
1mo ago
u/Dependent-Aide3621 avatar
Dependent-Aide3621
•
1mo ago
Have a 3090 24GB and 32GB RAM. What about swap / pagefile?


Upvote
25

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
No idea, give it a try if you can. Claude said it should offload to disk if RAM got tight but I never tested it.


Upvote
10

Downvote

Reply

Award

Share

Practical_Cell_8302
•
1mo ago
Let me know - i have also same but can only try on weekend


Upvote
3

Downvote

Reply

Award

Share

u/Nazi-Of-The-Grammar avatar
Nazi-Of-The-Grammar
•
1mo ago
This! If it works well with pagefile, that'll unlock it for a lot more people. On a 4090 + 32 GB RAM here.


Upvote
3

Downvote

Reply

Award

Share

u/alwaysbeblepping avatar
alwaysbeblepping
•
1mo ago
If it works well with pagefile, that'll unlock it for a lot more people. On a 4090 + 32 GB RAM here.

Using virtual memory is going to cause a lot of wear on your SSD. You'd be better off just reloading the the model on demand with mmap or whatever. ComfyUI theoretically will auto enable --fast-disk but you might want to make sure. Possibly also manually tune the cache parameters.


Upvote
1

Downvote

Reply

Award

Share

SRWindMill
•
1mo ago
Does it work?


Upvote
2

Downvote

Reply

Award

Share

SRWindMill
•
1mo ago
It works on 32 gb ram .. with lot of disk activity


Upvote
6

Downvote

Reply

Award

Share

cosmicr
•
1mo ago
It will work on 32gb ram easily for the W4A8 model. I'm running it right now - 7gb ram and 22gb vram in use.


Upvote
1

Downvote

Reply

Award

Share

[deleted]
•
1mo ago
u/Hoje-Na-IA avatar
Hoje-Na-IA
•
1mo ago
Now that you have tested the model, what do you think about it? Is it better than Klein 9B or Krea 2 in any aspect? I mean, those are very good and lightweight models. Is HI 3 better than those since it’s much bigger?


Upvote
16

Downvote

Reply

Award

Share

DelinquentTuna
•
1mo ago
It's dramatically better at t2i and prompt following. Better compared to the full-fat Flux.2.


Upvote
4

Downvote

Reply

Award

Share

DogeMoustache
•
1mo ago
Fit-Palpitation-7427
•
1mo ago
u/follimath avatar
follimath
•
1mo ago
Does it support native NVFP4 acceleration through comfy-kitchen, provided we package a NVFP4 quant in a format ComfyUI can consume? I assume your methodology/scripts for packaging it to ComfyUI format is on the repo, right? Thanks!


Upvote
12

Downvote

Reply

Award

Share

u/follimath avatar
follimath
•
1mo ago
•
Edited 1mo ago
I’m giving this a go - I’ll let you guys know how it turns out and share the weights if it works. The packaging methodology is not in the repo, so I will quantize the BF16 model already packaged for ComfyUI.


Upvote
1

Downvote

Reply

Award

Share

Otherwise-Piglet-775
•
1mo ago
35point1
•
1mo ago
Surprised it took this long for us to start trying this, I can’t wait to give a shot, thanks!


Upvote
7

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
It's only possible because Claude is so good now.


Upvote
12

Downvote

Reply

Award

Share

u/nauxiv avatar
nauxiv
•
1mo ago
The original Hunyuan 3.0 inference code already supported offloading, and bitsandbytes quantization worked as well.


Upvote
2

Downvote

Reply

Award

Share

SirCabbage
•
1mo ago
How does it compare to the current memory hog champion Flux 2.Dev? That's what I mostly use because even if other models get close, it feels like they never surpass even if they are faster.


Upvote
6

Downvote

Reply

Award

Share

u/Hoodfu avatar
Hoodfu
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Comment Image
Fantastic work! I'm still messing with sampler settings and upscaling but super happy so far. It's one of the most uncensored models we have available out of the box and it's got a good sense of humor on emotional faces and actions. I wouldn't say it's a Qwen 2.1/Krea 2/Ideogram 4 killer, but it's a great model to have alongside them. This took about 2.5 minutes on a 6000 pro/5090 with the 80 gig model convrot8 version of the model.


Upvote
5

Downvote

Reply

Award

Share

Violent_Walrus
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
I would like to buy a book of your collected prompts, please.


Upvote
5

Downvote

Reply

Award

Share

u/cadissimus avatar
cadissimus
•
1mo ago
•
Edited 1mo ago
Not killing qwen 2.1 whitout knowing alphabet as in their samples and also in your sample can be seen :p


Upvote
0

Downvote

Reply

Award

Share

u/leyermo avatar
leyermo
•
1mo ago
I think this model must be studied more


Upvote
5

Downvote

Reply

Award

Share

AltruisticList6000
•
1mo ago
Why does it have heavy horizontal stripes/line artifacts on most images? That looks unusuable if it can't be removed. Reminds me of flux.1 and Chroma HD, this specific artifact appears sometimes when using lowres-trained loras with them on very high resolutions.


Upvote
5

Downvote

Reply

Award

Share

u/CeFurkan avatar
CeFurkan
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
RTX 3090 vs RTX 4090 timings very close which means most of them time spent for Ram - GPU transfer


Upvote
4

Downvote

Reply

Award

Share

IvanSwan9
•
1mo ago
rtx3060 12gb + 32ram???


Upvote
4

Downvote

Reply

Award

Share

u/ArkCoon avatar
ArkCoon
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Local image edit models are in such a bad spot that people are now quantizing an 80B model that's a year old 😭

Krea 3, Ideogram 4.5 and Flux 3 weights can't drop soon enough.


Upvote
4

Downvote

Reply

Award

Share

jfreezer
•
1mo ago
The first picture makes a really cool parallelview


Upvote
3

Downvote

Reply

Award

Share

_LususNaturae_
•
1mo ago
Wow, thanks a lot! I'll give it a try. I've been wanting to try this model locally for a while, but I thought it was simply too big.

How does it compare to Krea 2 in terms of T2I?


Upvote
3

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
Krea 2 might have better quality but not as creative.


Upvote
5

Downvote

Reply

Award

Share

DJBFilmz
•
1mo ago
This better than Qwen 2.1? I was a bit disappointed in Qwen


Upvote
3

Downvote

Reply

Award

Share

u/Fenio_PL avatar
Fenio_PL
•
1mo ago
How could anyone be disappointed with such quality from just a 7B model? Qwen 2.1 was a game-changer for local, home-based AI.


Upvote
8

Downvote

Reply

Award

Share

DJBFilmz
•
1mo ago
u/cadissimus avatar
cadissimus
•
1mo ago
80B parameters and doesn't know alphabet


Upvote
3

Downvote

Reply

Award

Share

u/sleeping-in-crypto avatar
sleeping-in-crypto
•
1mo ago
Wow I’m giving this a shot. Might makes the comics I’m making much easier to manage


Upvote
2

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
it's pretty good with individual images but it might struggle with text and complex layouts.


Upvote
2

Downvote

Reply

Award

Share

u/Plus-Accident-5509 avatar
Plus-Accident-5509
•
1mo ago
Should this work at 8-bit on a 128GB strix halo?


Upvote
2

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
Should work, give it a try and let me know if you have an issue.


Upvote
2

Downvote

Reply

Award

Share

u/Plus-Accident-5509 avatar
Plus-Accident-5509
•
1mo ago
I tried the int8-convrot model and ran out of memory 30% in to loading the model. 4-bit weights works, but used 109GB of my 110GB GPU aperture. I assume the architecture has some aspects that are not optimal for unified memory.


Upvote
1

Downvote

Reply

Award

Share

MonkeyBoyPoop
•
1mo ago
Hell yeah—just need someone to implement a LoRA trainer for it. And maybe some spare GPUs. 😂


Upvote
2

Downvote

Reply

Award

Share

u/000TSC000 avatar
000TSC000
•
1mo ago
What VAE does this thing use?


Upvote
2

Downvote

Reply

Award

Share


2 more replies
Violent_Walrus
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter



Upvote
2

Downvote

Reply

Award

Share

u/frogsty264371 avatar
frogsty264371
•
1mo ago
I have two systems, which would be better to run hunyuanimage 3.0: 170HX 64gb vram / 32 GB ddr4 system 3090 24gb vram / 48 GB ddr5 cudimms Will it just sit resident in vram if there's enough or is there a better way to utilize high vram with this model?  Thanks


Upvote
2

Downvote

Reply

Award

Share

Netsuko
•
1mo ago
•
Edited 1mo ago
How on earth are you getting to 26s per image? On my 4090 with 64gb system ram, 4-bit W4A8 takes about 130s and int8 takes about 240 seconds per image. I must be doing something wrong because it doesn't hit my GPU at all.


Upvote
2

Downvote

Reply

Award

Share

u/PATATAJEC avatar
PATATAJEC
•
1mo ago
That banding…


Upvote
2

Downvote

Reply

Award

Share

roculus
•
1mo ago
RTX6000 PRO, Using the default provided workflow int8 80GB, the model fits into VRAM and generates 1024x1024 image in 20 seconds text2img, 30 seconds img2img but I'm getting some banding similar to what you see in the hair in the image of the two woman looking at the street sign example image.

limited image editing works well so far. any suggestions on getting rid of the banding? more steps, higher/lower guidance etc?


Upvote
2

Downvote

Reply

Award

Share

u/thevegit0 avatar
thevegit0
•
1mo ago
80gb the int8 😭


Upvote
2

Downvote

Reply

Award

Share

u/tehorhay avatar
tehorhay
•
1mo ago
Model loader is throwing an error: ValueError: orig_shape must be 2D, got (64, 6144, 4096)

Do I need comfy 0.39?


Upvote
2

Downvote

Reply

Award

Share

u/ArtificialAnaleptic avatar
ArtificialAnaleptic
•
1mo ago
I updated to dev. That fixed it.


Upvote
1

Downvote

Reply

Award

Share

Incognit0ErgoSum
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
My ai-toolkit fork can train loras for it as of today.

I recommend 64G of system ram to train the 4bit model and 128G to train the 8bit one. I've really only tested training the int8 model, but for a lineart remover edit lora, it trained in 100 steps, which was like 15 minutes. Just to manage expectations, if you have less ram than that, it's not going to work.

https://github.com/envy-ai/ai-toolkit-envy-optimized


Upvote
2

Downvote

Reply

Award

Share

Juiceman8686
•
1mo ago
This works great. I had Claude build an all in one workflow so you don't have to change workflows to perform a different task.

HunyuanImage3 - AIO Workflow


Upvote
2

Downvote

Reply

Award

Share

u/__ThrowAway__123___ avatar
__ThrowAway__123___
•
1mo ago
•
Edited 1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Works great. Int8_convrot works on a 3090ti and 96gb ram. Interesting to see an older model get revived. Only thing that seems to be missing is the preview as it is sampling. Something that I noticed is that faint horizontal lines can be visible in certain parts of the image (only tested the 8 step distill so far), not to a problematic degree but sometimes noticable.


Upvote
2

Downvote

Reply

Award

Share

u/Inevitable-Name-1701 avatar
Inevitable-Name-1701
•
1mo ago
No one notices that her thumb is in the wrong place—the woman has another index finger. Fg Bitbaggers


Upvote
2

Downvote

Reply

Award

Share

u/ArkCoon avatar
ArkCoon
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Can you do please do W6A8 quant as well? Native support was recently added to comfyui, quality loss is much lower than w4a8 u/LatentSpacer


Upvote
2

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
Working on it right now. It’s actually better than INT8. I’ll upload it soon. 


Upvote
2

Downvote

Reply

Award

Share

kemb0
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Do your times you show above include the optional prompt rewriting part or is that timing the pure image edit phase?


Upvote
1

Downvote

Reply

Award

Share

u/LatentSpacer avatar
LatentSpacer
OP
•
1mo ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
Just running with your prompts, no rewriting or chain of thought rewriting. Unfortunately it takes forever, I couldn't find a way to make it faster. it's 1-2s per token generated and yo need like 1000-2000 tokens. It makes a huge difference depending on the task, it turns your prompt into something it's trained for. I think the prompt rewrite is what makes it score high on the benchmarks.


Upvote
2

Downvote

Reply

Award

Share

u/No-Zookeepergame4774 avatar
No-Zookeepergame4774
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
One thing that might be doable is to use the prompt rewriting system prompt(s)—I assume this implementation uses one three from the Hunyuan 3 repo—but use a different LLM/VLM to do the rewriting. The results may not be quite as good (especially if those prompts were tuned for the results on the particular model), but there are a bunch of alternative models you could use with the built in Generate Text node that are generally strong and should be much faster than 1-2 tok/s on the hardware this was benchmarked on.


Upvote
2

Downvote

Reply

Award

Share

u/jimbarino avatar
jimbarino
•
1mo ago
Why is the prompt rewriting so insanely slow? Is there a reason we can't just use a different llm for the rewrite?


Upvote
1

Downvote

Reply

Award

Share

u/No-Zookeepergame4774 avatar
No-Zookeepergame4774
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Since this uses normal Comfy memory management, can I assume that it works with both the explicit --fast-disk option and the newer default automatic fast disk detection for streaming weights from disk instead of system RAM?


Upvote
1

Downvote

Reply

Award

Share

u/RobMilliken avatar
RobMilliken
•
1mo ago
Oof, fingers! Otherwise, great job!


Upvote
1

Downvote

Reply

Award

Share

DjSaKaS
•
1mo ago
5090 and 64gb should be fine also for int8 right?


Upvote
1

Downvote

Reply

Award

Share

Netsuko
•
1mo ago
int8 runs on my 4090 and 64gb, so, yes. Expect about 130s generate time per image


Upvote
2

Downvote

Reply

Award

Share

u/BrawndoOhnaka avatar
BrawndoOhnaka
•
1mo ago
This is really cool, but I would love to know what you prompted for that exact hairstyle on that brunette runway model because it is phenomenal.


Upvote
1

Downvote

Reply

Award

Share

twilliwilkinsonshire
•
1mo ago
Brother, that is just Anne Hathaway.


Upvote
1

Downvote

Reply

Award

Share

u/Ok-Option-6683 avatar
Ok-Option-6683
•
1mo ago
Does it change angles along with backgrounds natively? Has anybody tried?


Upvote
1

Downvote

Reply

Award

Share

FireFlamberge
•
1mo ago
Pelo nome no repositório, assumo que fala português

Parabéns pelo trabalho, estou baixando nesse momento


Upvote
1

Downvote

Reply

Award

Share

artisst_explores
•
1mo ago
Woah


Upvote
1

Downvote

Reply

Award

Share

Incognit0ErgoSum
•
1mo ago
•
Edited 1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
I'm currently testing training a lora on my custom ai-toolkit fork. You need an ungodly amount of system ram to train the int8 one, but the speed is about 13s per step on a 4090 and 128g of ddr4. You can probably train the 4bit one on 64g.

I'll push the code out as soon as I can confirm the lora actually works.

And you don't need 24g of vram to train it.


Upvote
1

Downvote

Reply

Award

Share

u/biggusdeeckus avatar
biggusdeeckus
•
1mo ago
Is the 90s looking woman in the input images ai generated? I honestly couldn't tell lol. If yes, what model and prompt did you use? I love the 90s look


Upvote
1

Downvote

Reply

Award

Share

Vyviel
•
1mo ago
Damn I only have 64GB ram I doubt it can fit an extra 50gb of stuff in there along with all the other ram it normally needs for the OS etc


Upvote
1

Downvote

Reply

Award

Share

Odd_Fix2
•
1mo ago
It's safe to say, without even thinking, that this new model is, unfortunately, much worse in every respect than the Krea 2 Turbo. It's safe to say it will suffer the same fate as the SD3 and all its derivatives.


Upvote
1

Downvote

Reply

Award

Share

MomentJolly3535
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
The model is 1 year old and was the best local model for long time in benchmarks, and it still one of the best edit model (i didn't compare it directly with the new Qwen 2.1 but i can tell you it's above everything else)


Upvote
1

Downvote

Reply

Award

Share


1 more reply
[deleted]
•
1mo ago
DelinquentTuna
•
1mo ago
Vyviel
•
1mo ago
Looks cool just curious any reason the prompt rewriting is so slow I can usually run decent sized LLMs locally that push out 20-40 tokens a second? Is it because the memory is totally full of the image model files or its built into the image model and not rewriting it with another LLM?

Maybe a silly question I dont exactly understand how that part works is the cot head a llm or something? Wonder if its faster to just get another model to do the rewrite and skip doing it in the workflow?


Upvote
1

Downvote

Reply

Award

Share

u/OracleofEpirus avatar
OracleofEpirus
•
1mo ago
I got an error on thinking mode



[ERROR] !!! Exception during processing !!! The expanded size of the tensor (999) must match the existing size (1024) at non-singleton dimension 0. Target sizes: [999, 4096]. Tensor sizes: [1024, 4096] [ERROR] Traceback (most recent call last): File "D:\Applications\ComfyUI_windows_portable\ComfyUI\execution.py", line 547, in execute


Upvote
1

Downvote

Reply

Award

Share

u/_godisnowhere_ avatar
_godisnowhere_
•
1mo ago
Thank you for this valuable contribution! I'm really thankful.


Upvote
1

Downvote

Reply

Award

Share

CutLongjumping8
•
1mo ago
•
Edited 1mo ago
u/Green-Ad-3964 avatar
Green-Ad-3964
•
1mo ago
what about a 5090 on a system with only 32GB of RAM?


Upvote
1

Downvote

Reply

Award

Share

u/fauni-7 avatar
fauni-7
•
1mo ago
I got a 4090+128GB RAM, what weights should I get for best text to image results? And also can it do img2img? Thanks for your work!


Upvote
1

Downvote

Reply

Award

Share

Winougan
•
1mo ago
It's really bad at long form text - I'll pass. For that size, you'd think it'd be a monster for creating legible words.


Upvote
1

Downvote

Reply

Award

Share

u/sketchfag avatar
sketchfag
•
1mo ago
Can barely tell the difference, how is this compared to Krea2?


Upvote
1

Downvote

Reply

Award

Share

u/detailteufel avatar
detailteufel
•
1mo ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Woah! I have to try this


Upvote
1

Downvote

Reply

Award

Share

jah-selassie
•
1mo ago
•
Edited 1mo ago
Comment Image
Works really well on my 4080 and 96GB of ram. Only hiccup was prompt rewriting which only seems to work when I set the resolution to 1024x1024; anything else and it just throws an error and refuses to work.

On I2I, It would be cool to have a node that would automatically resize an image to the nearest 'official' HunyuanImage resolution to avoid pixel drifting. Meanwhile, I've created a simple blueprint node with a few math nodes that does just that (attached).

Oh, and could you possibly share your prompt to transfer styles? I'm getting good results, but not as good as yours.

Thanks for sharing and all the hard work!